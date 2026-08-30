"""Affine-invariant Riemannian metric (AIRM) on the SPD cone.

B1.3. The contrast with bw.py is the whole point of having both:

  BW    invariant under ORTHOGONAL conjugation only
  AIRM  invariant under congruence by ANY invertible M: d(MSM', MBM') = d(S,B)

That one extra symmetry is what makes the affine-equivariance test so sharp.
Almost no implementation error survives it, which is why the test contract singles it
out as the done-when.

Geometrically AIRM makes the cone a Hadamard space -- complete, simply
connected, non-positive curvature. The Frechet mean is therefore unique and
Riemannian gradient descent converges from any starting point. That is a
stronger guarantee than the Alvarez-Esteban fixed point carries, and it is
why the Karcher iteration needs no cleverness.
"""

from typing import NamedTuple

import numpy as np

from rfd.spd.linalg import sym, spd_eigh, rebuild_spd, spd_log, spd_exp


def _roots(X, strict=True):
    """X^(1/2) and X^(-1/2) from ONE eigendecomposition."""
    lam, V = spd_eigh(X, strict)
    r = np.sqrt(lam)
    return rebuild_spd(r, V), rebuild_spd(1.0 / r, V)


def airm_log(A, B, strict=True):
    """Riemannian logarithm -- the tangent vector at A pointing to B.

        Log_A(B) = A^(1/2) log(A^(-1/2) B A^(-1/2)) A^(1/2)
    """
    rA, irA = _roots(A, strict)
    return sym(rA @ spd_log(sym(irA @ B @ irA), strict) @ rA)


def airm_exp(A, V, strict=True):
    """Riemannian exponential -- move from A along tangent vector V.

        Exp_A(V) = A^(1/2) exp(A^(-1/2) V A^(-1/2)) A^(1/2)

    The inner exp runs with strict=False on purpose: V is a TANGENT vector,
    symmetric but freely indefinite, so a PSD check there would reject
    perfectly valid input.
    """
    rA, irA = _roots(A, strict)
    return sym(rA @ spd_exp(sym(irA @ V @ irA), strict=False) @ rA)


def airm_dist2(A, B, strict=True):
    """Squared AIRM distance:  || log(A^(-1/2) B A^(-1/2)) ||_F^2.

    Unlike BW's d2 this is a sum of squares, so it can never come out
    negative and needs no clipping. It does carry the kappa**2 exposure of
    the sandwich, exactly as g_mean does -- measured error tracks
    eps * kappa**2 across the grid.
    """
    _, irA = _roots(A, strict)
    L = spd_log(sym(irA @ B @ irA), strict)
    return np.linalg.norm(L, axis=(-2, -1)) ** 2


def airm_inner(A, U, V, strict=True):
    """AIRM inner product of tangent vectors ``U`` and ``V`` at ``A``.

    Leading dimensions broadcast.  In whitened coordinates this is simply
    the Frobenius inner product, which is also the convention used by the
    loading-space theory and the DGP.
    """
    _, irA = _roots(A, strict)
    normal_u = irA @ U @ irA
    normal_v = irA @ V @ irA
    return np.sum(normal_u * normal_v, axis=(-2, -1))


def airm_random_tangent(rng, A, count=1, structure="dense"):
    """Draw unnormalised symmetric tangent vectors at one SPD point.

    ``structure="commuting"`` restricts the draw to the eigenframe of ``A``.
    This produces the exact common-flat controls needed by the simulation
    programme; ``dense`` explores the full symmetric tangent space.
    """
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
    raise ValueError("AIRM tangent structure must be 'dense' or 'commuting'")


def airm_parallel_transport(V, A, B, strict=True):
    """Transport tangent vector V from A to B along the connecting geodesic.

        E = (B A^(-1))^(1/2) = A^(1/2) (A^(-1/2) B A^(-1/2))^(1/2) A^(-1/2)
        PT(V) = E V E'

    The second form is the one to compute: it never forms the non-symmetric
    product B A^(-1), so every square root taken is of a symmetric matrix.
    """
    rA, irA = _roots(A, strict)
    lam, U = spd_eigh(sym(irA @ B @ irA), strict)
    E = rA @ rebuild_spd(np.sqrt(lam), U) @ irA
    return sym(E @ V @ E.mT)


class KarcherResult(NamedTuple):
    X: np.ndarray
    n_iter: int
    residual: float
    converged: bool


def airm_barycentre(
    S,
    weights=None,
    tol=1e-11,
    max_iter=200,
    step=1.0,
    X0=None,
    strict=True,
):
    """Karcher mean by Riemannian gradient descent.

        G = sum_i w_i log(X^(-1/2) S_i X^(-1/2))          (gradient at X)
        X <- X^(1/2) exp(step * G) X^(1/2)

    ``weights=None`` gives the original equal-weight barycentre. Supplied
    weights must be finite and nonnegative with positive total mass. They are
    normalised internally, so only their relative sizes matter.

    Residual is ||G||_F, and it is a better criterion than BW's. G lives in
    the tangent space at X in NORMAL coordinates, so ||G|| is already
    affine-invariant: rescale every S_i and it does not move. BW's
    ||X - T|| needed an explicit /||X|| to get the same property.

    step is exposed but 1.0 is right. On a Hadamard manifold the full step
    converges globally; damping is the first thing to try only if a very
    widely dispersed family overshoots.

    Measured floor is ~6e-12 at m=12, kappa=1e5 -- looser than BW's ~1e-14,
    which is why the default tol here is 1e-11 rather than 1e-12.

    Does NOT raise on non-convergence -- check `.converged`.
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
        rX, irX = _roots(X, strict)
        logs = spd_log(sym(irX @ S @ irX), strict)
        G = np.tensordot(weights, logs, axes=(0, 0))

        residual = np.linalg.norm(G)
        if residual < tol:
            return KarcherResult(X, n_iter, float(residual), True)

        X = sym(rX @ spd_exp(step * G, strict=False) @ rX)

    return KarcherResult(X, max_iter, float(residual), False)


def airm_frechet(X, S, strict=True):
    """(1/N) sum_i d2_AIRM(X, S_i). Shares no code path with the iteration."""
    return airm_dist2(np.broadcast_to(X, S.shape), S, strict).mean()
