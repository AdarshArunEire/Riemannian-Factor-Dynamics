"""B1.2 -- Bures-Wasserstein distance. Barycentre not involved here.

All tolerances use amplification=cond: measured error tracks eps*kappa
across the grid (implied constant ~1, min headroom ~6x at safety=10).

Every comparison is normalised by the SCALE tr A + tr B, not by d2 itself.
d2 is a difference of large traces, so relative-to-d2 collapses as A -> B
for reasons that carry no information -- the same trap as testing a matrix
entrywise-relative when the bound is on the norm.
"""

import numpy as np
import pytest

from rfd.dgp.spd import random_spd, random_Q
from rfd.spd.linalg import rebuild_spd, sym, spd_sqrt
from rfd.spd.bw import bw_dist2, trace, bw_barycentre, bw_frechet
from tests.conftest import num_tol, geodesic_perturb

N = 200
CONDS = [1e1, 1e3, 1e5]
MS = [2, 3, 12]


def rel_to_scale(diff, A, B):
    return np.abs(diff) / (trace(A) + trace(B))


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_zero_on_identical(rng, m, cond):
    """d2(A, A) == 0. Weak as a claim, but it is a real cancellation of
    three large traces -- a sign error anywhere leaves O(tr A) behind."""
    A = random_spd(rng, m=m, cond=cond, n=N)
    assert (bw_dist2(A, A) / trace(A)).max() < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_symmetry(rng, m, cond):
    """d2(A, B) == d2(B, A).

    True as mathematics but NOT true of the code path: the formula
    square-roots its first argument only, so the two calls run different
    arithmetic. Same virtue as the g_mean symmetry test.
    """
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    assert rel_to_scale(bw_dist2(A, B) - bw_dist2(B, A), A, B).max() < num_tol(
        amplification=cond
    )


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_commuting_closed_form(rng, m, cond):
    """When A and B share an eigenbasis the matrices commute and

        d2 = sum_i (sqrt(a_i) - sqrt(b_i))**2

    This is the strongest test in the file: the right-hand side is scalar
    arithmetic on the two spectra and shares NO code path with the trace
    formula. It pins the constant and the factor of 2, which the symmetry
    and invariance tests cannot see.
    """
    Q = random_Q(rng, (N, m, m))
    a = np.geomspace(1.0, cond, m)
    b = np.geomspace(2.0, 3.0 * cond, m)
    A, B = rebuild_spd(a, Q), rebuild_spd(b, Q)
    closed = ((np.sqrt(a) - np.sqrt(b)) ** 2).sum()
    assert rel_to_scale(bw_dist2(A, B) - closed, A, B).max() < num_tol(
        amplification=cond
    )


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_rotation_invariance(rng, m, cond):
    """d2(U A U', U B U') == d2(A, B) for orthogonal U. Every term is a
    trace, so this must hold exactly in theory -- it checks that the
    eigen-machinery is not leaking a basis dependence."""
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    U = random_Q(rng, (N, m, m))
    rotated = bw_dist2(U @ A @ U.mT, U @ B @ U.mT)
    assert rel_to_scale(rotated - bw_dist2(A, B), A, B).max() < num_tol(
        amplification=cond
    )


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_scaling(rng, m, cond):
    """d2(cA, cB) == c * d2(A, B).

    Squared BW is 1-homogeneous (so BW itself scales as sqrt(c)). Catches a
    misplaced square root that symmetry and rotation invariance both survive.
    """
    c = 7.3
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    diff = bw_dist2(c * A, c * B) - c * bw_dist2(A, B)
    assert (np.abs(diff) / (c * (trace(A) + trace(B)))).max() < num_tol(
        amplification=cond
    )


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_triangle_inequality(rng, m, cond):
    """d(A,C) <= d(A,B) + d(B,C).

    BW is a genuine metric. This is the only global property here: it holds
    for every triple rather than following from an algebraic identity, so it
    catches sign and normalisation errors the identities cannot.
    """
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    C = random_spd(rng, m=m, cond=cond, n=N)
    slack = (
        np.sqrt(bw_dist2(A, B)) + np.sqrt(bw_dist2(B, C)) - np.sqrt(bw_dist2(A, C))
    )
    tol = num_tol(amplification=cond) * np.sqrt(trace(A) + trace(C))
    assert (slack > -tol).all()


# ---------------------------------------------------------------------------
# barycentre
# ---------------------------------------------------------------------------
# N_BARY is small because the iteration runs up to ~75 sweeps at cond=1e5.
# tol=1e-12 sits an order above the measured stalling floor (~1e-14).

N_BARY = 20
BARY_TOL = 1e-12


def _commuting_stack(rng, m, cond, n):
    """n SPD matrices sharing one eigenbasis, with their spectra.

    On a commuting family BW reduces to Euclidean geometry on the square
    roots, so the barycentre has eigenvalues (mean_i sqrt(s_ij))**2 in that
    shared basis. Closed form, no iteration involved.
    """
    Q = random_Q(rng, (m, m))
    specs = np.array([np.geomspace(1.0 + j, cond * (1.0 + j), m) for j in range(n)])
    return np.stack([rebuild_spd(s, Q) for s in specs]), specs, Q


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_minimises_frechet(rng, m, cond):
    """THE independent check.

    Perturb the answer along random symmetric directions and confirm the
    Frechet functional goes UP. bw_frechet shares no code path with the
    iteration, so unlike the stationarity residual this cannot pass by
    construction.

    Perturbation is GEODESIC, not additive: an additive step of 1e-2*||X||
    leaves the cone entirely once kappa is large, and every perturbation
    would be skipped. Measured: 0 of 20 survived at m=12, kappa=1e5.
    """
    S = random_spd(rng, m=m, cond=cond, n=N_BARY)
    res = bw_barycentre(S, tol=BARY_TOL)
    assert res.converged

    f0 = bw_frechet(res.X, S)
    for _ in range(20):
        E = rng.standard_normal((m, m))
        Xp = geodesic_perturb(res.X, E / np.linalg.norm(E))
        assert bw_frechet(Xp, S) > f0


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_commuting_closed_form(rng, m, cond):
    S, specs, Q = _commuting_stack(rng, m, cond, N_BARY)
    closed = rebuild_spd((np.sqrt(specs).mean(axis=0)) ** 2, Q)
    res = bw_barycentre(S, tol=BARY_TOL)
    assert res.converged
    err = np.linalg.norm(res.X - closed) / np.linalg.norm(closed)
    assert err < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_orthogonal_equivariance(rng, m, cond):
    """bary({U S_i U'}) == U bary({S_i}) U'.

    BW is invariant under simultaneous orthogonal conjugation -- but NOT
    under general congruence. That is AIRM's property, not this one, and
    conflating them is the mistake B1.3 exists to avoid.
    """
    S = random_spd(rng, m=m, cond=cond, n=N_BARY)
    X = bw_barycentre(S, tol=BARY_TOL)
    U = random_Q(rng, (m, m))
    XU = bw_barycentre(U @ S @ U.mT, tol=BARY_TOL)
    assert X.converged and XU.converged
    err = np.linalg.norm(XU.X - U @ X.X @ U.mT) / np.linalg.norm(X.X)
    assert err < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_scaling(rng, m, cond):
    """bary(c S) == c bary(S), since d2 is 1-homogeneous."""
    c = 7.3
    S = random_spd(rng, m=m, cond=cond, n=N_BARY)
    X = bw_barycentre(S, tol=BARY_TOL)
    Xc = bw_barycentre(c * S, tol=BARY_TOL)
    assert X.converged and Xc.converged
    err = np.linalg.norm(Xc.X - c * X.X) / np.linalg.norm(c * X.X)
    assert err < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_of_one(rng, m, cond):
    """The barycentre of a single matrix is that matrix. Trivial as
    mathematics, but it is the only test here that would catch a mean taken
    over the wrong axis."""
    S = random_spd(rng, m=m, cond=cond, n=1)
    res = bw_barycentre(S, tol=BARY_TOL)
    err = np.linalg.norm(res.X - S[0]) / np.linalg.norm(S[0])
    assert err < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_stationarity(rng, m, cond):
    """X == (1/N) sum_i (X^(1/2) S_i X^(1/2))^(1/2).

    SEMI-TAUTOLOGICAL and labelled as such: the loop terminates on exactly
    this residual, so it mostly re-reports the stopping rule. Kept because
    it would catch a residual computed on the wrong iterate, and because
    BUILD.md's done-when names it. The Frechet test above is the one doing
    real work.
    """
    S = random_spd(rng, m=m, cond=cond, n=N_BARY)
    res = bw_barycentre(S, tol=BARY_TOL)
    assert res.converged
    rX = spd_sqrt(res.X)
    T = spd_sqrt(sym(rX @ S @ rX)).mean(axis=0)
    assert np.linalg.norm(res.X - T) / np.linalg.norm(res.X) < BARY_TOL


@pytest.mark.parametrize("m", MS)
def test_barycentre_iterations_well_conditioned(rng, m):
    """BUILD.md done-when: under 50 iterations for well-conditioned input.

    Only asserted at cond=1e1. At 1e5 it legitimately needs ~75 -- that
    slowdown is the phenomenon, not a failure, and belongs in experiments/.
    """
    S = random_spd(rng, m=m, cond=10.0, n=N_BARY)
    res = bw_barycentre(S, tol=BARY_TOL)
    assert res.converged
    assert res.n_iter < 50
