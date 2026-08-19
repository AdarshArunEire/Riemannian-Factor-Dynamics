"""Bures-Wasserstein geometry on the SPD cone.

B1.2. Distance first; the barycentre iteration comes next and will be
checked against the Frechet objective built from this module.
"""

from typing import NamedTuple

import numpy as np

from rfd.spd.linalg import sym, spd_sqrt, spd_eigh, rebuild_spd


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


def bw_barycentre(S, tol=1e-12, max_iter=200, X0=None, strict=True):
    """Bures-Wasserstein barycentre of a stack S of shape (N, m, m).

    Alvarez-Esteban fixed point, initialised at the arithmetic mean:

        X <- X^(-1/2) ( (1/N) sum_i (X^(1/2) S_i X^(1/2))^(1/2) )^2 X^(-1/2)

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
    X = S.mean(axis=0) if X0 is None else np.asarray(X0)

    residual = np.inf
    for n_iter in range(1, max_iter + 1):
        lam, V = spd_eigh(X, strict)
        r = np.sqrt(lam)
        rX = rebuild_spd(r, V)          # X^(1/2)
        irX = rebuild_spd(1.0 / r, V)   # X^(-1/2), same decomposition

        T = spd_sqrt(sym(rX @ S @ rX), strict).mean(axis=0)

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
