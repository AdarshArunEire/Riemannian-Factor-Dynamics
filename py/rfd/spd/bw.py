"""Bures-Wasserstein geometry on the SPD cone.

B1.2. Distance first; the barycentre iteration comes next and will be
checked against the Frechet objective built from this module.
"""

from typing import NamedTuple

import numpy as np

from scipy.integrate import solve_ivp

from rfd.spd.linalg import sym, spd_sqrt, spd_invsqrt, spd_eigh, rebuild_spd


def trace(A):
    """Batched trace over the trailing (m, m) block."""
    return np.trace(A, axis1=-2, axis2=-1)


def bw_dist2(A, B, strict=True):
    """Squared Bures-Wasserstein distance.

        d2(A, B) = tr A + tr B - 2 tr (A^(1/2) B A^(1/2))^(1/2)

    Batched over any leading axes; A and B broadcast against each other.

    Only the EIGENVALUES of A^(1/2) B A^(1/2) are needed -- the cross term is
    the sum of their square roots -- so this uses eigvalsh rather than
    building the matrix square root through spd_sqrt. Same arithmetic, no
    eigenvectors computed.

    Two numerical facts that shape how you test this:

    * d2 is a difference of large traces, so it loses relative accuracy to
      cancellation as A -> B. Compare d2 values against the scale
      tr A + tr B, NEVER relative to d2 itself.
    * For the same reason d2 comes out slightly negative when A == B. Tiny
      negatives are clipped to zero. A significantly negative value is not
      roundoff and raises under strict.
    """
    rA = spd_sqrt(A, strict)
    lam = np.linalg.eigvalsh(sym(rA @ B @ rA))
    cross = np.sqrt(np.clip(lam, 0.0, None)).sum(axis=-1)

    trA, trB = trace(A), trace(B)
    d2 = trA + trB - 2.0 * cross

    scale = trA + trB
    bad = d2 < -1e-10 * scale
    if strict and np.any(bad):
        raise ValueError(f"BW d2 significantly negative at {np.flatnonzero(bad)}")
    return np.maximum(d2, 0.0)


def bw_lyapunov(A, U, strict=True):
    """Solve ``A L + L A = U`` for symmetric positive-definite ``A``.

    This is the basic BW musical map.  It is an eigensystem wrapper, but the
    geometry built from it is not interchangeable with AIRM geometry.
    """
    lam, eigenvectors = spd_eigh(A, strict)
    coordinates = eigenvectors.mT @ sym(U) @ eigenvectors
    denominator = lam[..., :, None] + lam[..., None, :]
    return sym(eigenvectors @ (coordinates / denominator) @ eigenvectors.mT)


def bw_inner(A, U, V, strict=True):
    """BW inner product ``1/2 tr(U L_A[V])`` with batched broadcasting."""
    return 0.5 * np.sum(sym(U) * bw_lyapunov(A, V, strict), axis=(-2, -1))


def bw_optimal_map(A, B, strict=True):
    """Optimal Gaussian transport map from covariance ``A`` to ``B``."""
    root = spd_sqrt(A, strict)
    inverse_root = spd_invsqrt(A, strict)
    middle = spd_sqrt(sym(root @ B @ root), strict)
    return sym(inverse_root @ middle @ inverse_root)


def bw_log(A, B, strict=True):
    """BW logarithm at ``A`` pointing to ``B`` on the full-rank branch."""
    displacement = bw_optimal_map(A, B, strict) - np.eye(A.shape[-1])
    return sym(displacement @ A + A @ displacement)


def bw_exp(A, U, strict=True):
    """BW exponential on its compatible full-rank normal branch.

    ``Exp_A(U) = (I + L_A[U]) A (I + L_A[U])``.  The positive-definiteness
    check on ``I + L_A[U]`` is the finite-sample version of the Exp margin in
    the BW theorem boundary.  Silently crossing it would generate a point on
    the wrong branch even though the matrix product can remain PSD.
    """
    generator = bw_lyapunov(A, U, strict)
    step = np.eye(A.shape[-1]) + generator
    if strict and np.any(np.linalg.eigvalsh(step) <= 0.0):
        raise ValueError("BW exponential left its compatible full-rank branch")
    return sym(step @ A @ step)


def _bw_geodesic_state(A, B, t, strict=True):
    displacement = bw_optimal_map(A, B, strict) - np.eye(A.shape[-1])
    step = np.eye(A.shape[-1]) + t * displacement
    point = sym(step @ A @ step)
    velocity = sym(displacement @ A @ step + step @ A @ displacement)
    return point, velocity


def bw_geodesic(A, B, t, strict=True):
    """Point at time ``t`` on the canonical full-rank BW geodesic."""
    return _bw_geodesic_state(A, B, t, strict)[0]


def bw_christoffel(A, X, Y, strict=True):
    """Levi-Civita Christoffel map in the ambient symmetric coordinates."""
    lx = bw_lyapunov(A, X, strict)
    ly = bw_lyapunov(A, Y, strict)
    return sym(A @ ly @ lx + ly @ lx @ A - lx @ Y - ly @ X)


def _bw_transport_one(V, A, B, strict, rtol, atol):
    if np.array_equal(A, B):
        return sym(V)

    m = A.shape[-1]
    displacement = bw_optimal_map(A, B, strict) - np.eye(m)

    def parallel_equation(t, flattened):
        transported = sym(flattened.reshape(m, m))
        step = np.eye(m) + t * displacement
        point = sym(step @ A @ step)
        velocity = sym(
            displacement @ A @ step + step @ A @ displacement
        )
        return (-bw_christoffel(point, velocity, transported, strict)).ravel()

    solution = solve_ivp(
        parallel_equation,
        (0.0, 1.0),
        sym(V).ravel(),
        method="DOP853",
        t_eval=(1.0,),
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise RuntimeError(f"BW parallel transport failed: {solution.message}")
    return sym(solution.y[:, -1].reshape(m, m))


def bw_parallel_transport(
    V,
    A,
    B,
    strict=True,
    rtol=1e-9,
    atol=1e-11,
):
    """Numerical Levi-Civita transport along the canonical BW geodesic.

    Unlike AIRM and sphere transport, full noncommuting BW transport has no
    small closed-form wrapper in this codebase.  We integrate the proved
    Christoffel ODE.  Leading dimensions of ``V``, ``A`` and ``B`` broadcast,
    so this serves both one vector and a time-indexed stack.
    """
    V, A, B = np.asarray(V), np.asarray(A), np.asarray(B)
    if V.shape[-2:] != A.shape[-2:] or V.shape[-2:] != B.shape[-2:]:
        raise ValueError("V, A and B must share their trailing matrix shape")

    leading = np.broadcast_shapes(V.shape[:-2], A.shape[:-2], B.shape[:-2])
    matrix_shape = V.shape[-2:]
    if not leading:
        return _bw_transport_one(V, A, B, strict, rtol, atol)

    vectors = np.broadcast_to(V, leading + matrix_shape)
    starts = np.broadcast_to(A, leading + matrix_shape)
    ends = np.broadcast_to(B, leading + matrix_shape)
    result = np.empty_like(vectors, dtype=float)

    for index in np.ndindex(leading):
        result[index] = _bw_transport_one(
            vectors[index], starts[index], ends[index], strict, rtol, atol
        )
    return result


def bw_random_tangent(rng, A, count=1, structure="dense"):
    """Draw unnormalised BW tangent vectors at one SPD point."""
    A = np.asarray(A)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A must be one square SPD matrix")
    if count < 0:
        raise ValueError("count must be nonnegative")

    m = A.shape[0]
    if structure == "dense":
        raw = rng.standard_normal((count, m, m))
        return sym(raw)
    if structure == "commuting":
        _, eigenvectors = spd_eigh(A)
        diagonal = rng.standard_normal((count, m))
        return sym((eigenvectors * diagonal[..., None, :]) @ eigenvectors.T)
    raise ValueError("BW tangent structure must be 'dense' or 'commuting'")


class BarycentreResult(NamedTuple):
    """Deliberately not a bare matrix.

    Returning a tuple means `bw_barycentre(S) @ M` raises instead of silently
    doing something wrong, and it forces the caller past `.converged`. The
    iteration count is the diagnostic N-12 will want.
    """

    X: np.ndarray
    n_iter: int
    residual: float
    converged: bool


def bw_barycentre(
    S,
    weights=None,
    tol=1e-12,
    max_iter=200,
    X0=None,
    strict=True,
):
    """Bures-Wasserstein barycentre of a stack S of shape (N, m, m).

    Weighted Alvarez-Esteban fixed point, initialised at the weighted
    arithmetic mean:

        X <- X^(-1/2) ( sum_i w_i (X^(1/2) S_i X^(1/2))^(1/2) )^2 X^(-1/2)

    ``weights=None`` gives the original equal-weight barycentre. Supplied
    weights must be finite and nonnegative with positive total mass. They are
    normalised internally, so only their relative sizes matter.

    provably convergent on the full-rank cone. Writing
    T(X) = (1/N) sum_i (X^(1/2) S_i X^(1/2))^(1/2), a fixed point satisfies
    X^(1/2) X X^(1/2) = T^2, hence X = T -- so the AE fixed point and the
    Agueh-Carlier stationarity condition X = T(X) coincide, and the natural
    residual is

        ||X - T(X)||_F / ||X||_F

    which T already gives us for free each sweep. Measured on the CURRENT
    iterate before the update, so the returned residual describes the
    returned X.

    On tol. Measured stalling floor is ~1e-14 to 1e-15 relative -- of order
    10-100 * eps, NOT eps*kappa**2. The kappa**2 growth that afflicts g_mean
    does not appear here because the residual is normalised by ||X||, and
    that is a norm-scale quantity. tol=1e-12 converges across
    m in {2,3,12} and kappa up to 1e5; tol=1e-15 stalls.

    Iteration counts at tol=1e-12 (m=12): ~10 at kappa=1e1, ~30 at 1e3,
    ~58 at 1e5. That growth curve is the empirical BW-SHRINKING-MARGIN
    picture and is what experiments/ should sweep properly.

    Does NOT raise on non-convergence -- check `.converged`. A sweep that
    wants to record stalls should not have to catch exceptions.
    """
    S = np.asarray(S)
    if S.ndim < 3 or S.shape[0] == 0:
        raise ValueError("S must contain at least one matrix")

    if weights is None:
        weights = np.full(S.shape[0], 1.0 / S.shape[0])
    else:
        weights = np.asarray(weights, dtype=float)
        if weights.shape != (S.shape[0],):
            raise ValueError(f"weights must have shape ({S.shape[0]},)")
        if not np.isfinite(weights).all():
            raise ValueError("weights contain NaN or Inf")
        if np.any(weights < 0.0):
            raise ValueError("weights must be nonnegative")
        total = weights.sum()
        if total <= 0.0:
            raise ValueError("weights must have positive total mass")
        weights = weights / total

    X = np.tensordot(weights, S, axes=(0, 0)) if X0 is None else np.asarray(X0)

    residual = np.inf
    for n_iter in range(1, max_iter + 1):
        lam, V = spd_eigh(X, strict)
        r = np.sqrt(lam)
        rX = rebuild_spd(r, V)          # X^(1/2)
        irX = rebuild_spd(1.0 / r, V)   # X^(-1/2), same decomposition

        roots = spd_sqrt(sym(rX @ S @ rX), strict)
        T = np.tensordot(weights, roots, axes=(0, 0))

        residual = np.linalg.norm(X - T) / np.linalg.norm(X)
        if residual < tol:
            return BarycentreResult(X, n_iter, float(residual), True)

        X = sym(irX @ (T @ T) @ irX)

    return BarycentreResult(X, max_iter, float(residual), False)


def bw_frechet(X, S):
    """Frechet functional (1/N) sum_i d2_BW(X, S_i).

    The barycentre minimises this. Shares no code path with the iteration,
    which is the entire point -- the stationarity residual cannot check the
    iteration against itself.
    """
    return bw_dist2(np.broadcast_to(X, S.shape), S).mean()
