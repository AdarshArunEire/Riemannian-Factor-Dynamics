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

from rfd.spd.bw import (
    bw_clip_exp_tangent,
    bw_exp,
    bw_inner,
    bw_log,
    bw_parallel_transport,
)

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


def test_exp_log_distance_and_metric_agree_on_compatible_branch():
    """The new DGP primitives share the established BW distance convention."""
    base = np.diag([1.0, 1.5, 2.0])
    tangent = np.array(
        [[0.08, 0.02, 0.0], [0.02, -0.04, 0.01], [0.0, 0.01, 0.03]]
    )
    point = bw_exp(base, tangent)

    np.testing.assert_allclose(bw_log(base, point), tangent, rtol=2e-12, atol=2e-12)
    np.testing.assert_allclose(
        bw_dist2(base, point),
        bw_inner(base, tangent, tangent),
        rtol=2e-11,
        atol=2e-13,
    )


def test_parallel_transport_preserves_bw_inner_product():
    """The numerical Christoffel ODE is an isometry, not an SPD congruence."""
    start = np.diag([1.0, 1.4, 2.0])
    endpoint_tangent = np.array(
        [[0.06, 0.015, 0.0], [0.015, -0.03, 0.01], [0.0, 0.01, 0.02]]
    )
    end = bw_exp(start, endpoint_tangent)
    first = np.array([[0.1, 0.02, 0.0], [0.02, -0.04, 0.01], [0.0, 0.01, 0.03]])
    second = np.array([[-0.02, 0.01, 0.015], [0.01, 0.05, 0.0], [0.015, 0.0, 0.04]])
    moved_first = bw_parallel_transport(first, start, end)
    moved_second = bw_parallel_transport(second, start, end)

    np.testing.assert_allclose(moved_first, moved_first.T, atol=2e-13)
    np.testing.assert_allclose(
        bw_inner(end, moved_first, moved_second),
        bw_inner(start, first, second),
        rtol=3e-8,
        atol=3e-10,
    )


def test_exp_rejects_the_wrong_bw_normal_branch():
    base = np.eye(2)
    # L_I[U] = U/2, so I + L_I[U] has a negative first eigenvalue.
    incompatible = np.diag([-3.0, 0.0])
    with pytest.raises(ValueError, match="compatible"):
        bw_exp(base, incompatible)


def test_exp_reconstruction_clip_is_inactive_inside_the_margin():
    base = np.eye(2)
    tangent = np.diag([-0.4, 0.2])

    clipped = bw_clip_exp_tangent(base, tangent, step_margin=0.05)

    assert clipped.factors == pytest.approx(1.0)
    np.testing.assert_allclose(clipped.tangent, tangent)
    assert clipped.raw_step_min_eigenvalues == pytest.approx(0.8)


def test_exp_reconstruction_clip_returns_largest_compatible_radial_step():
    base = np.eye(2)
    incompatible = np.diag([-4.0, 0.0])

    clipped = bw_clip_exp_tangent(base, incompatible, step_margin=0.05)
    point = bw_exp(base, clipped.tangent)

    assert clipped.raw_step_min_eigenvalues == pytest.approx(-1.0)
    assert clipped.factors == pytest.approx(0.475)
    np.testing.assert_allclose(point, np.diag([0.05**2, 1.0]), atol=1e-14)


def test_weighted_barycentre_uses_relative_positive_weights(rng):
    S = random_spd(rng, m=3, cond=10.0, n=3)
    weights = np.array([1.0, 2.0, 4.0])
    first = bw_barycentre(S, weights=weights)
    scaled = bw_barycentre(S, weights=11.0 * weights)

    assert first.converged and scaled.converged
    np.testing.assert_allclose(first.X, scaled.X, rtol=2e-11, atol=2e-12)


def test_weighted_barycentre_one_hot_returns_selected_observation(rng):
    S = random_spd(rng, m=3, cond=10.0, n=3)
    result = bw_barycentre(S, weights=np.array([0.0, 1.0, 0.0]))

    assert result.converged
    np.testing.assert_allclose(result.X, S[1], rtol=2e-11, atol=2e-12)
