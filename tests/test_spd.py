"""Shared SPD linear algebra and the AIRM geometry."""

from tests.conftest import geodesic_perturb, num_tol
import pytest

import numpy as np

from rfd._maths.spd import *
from rfd._maths.spd import airm_barycentre, airm_dist2, airm_exp, airm_frechet, airm_log, g_mean, rebuild_spd
from rfd.simulate import random_Q, random_congruence, random_spd, random_spd_family, spectrum

# Naming convention in this file:
#   S       a random SPD matrix (or a stack of them) -- the input
#   R, Ri   S**(1/2) and S**(-1/2), DERIVED from S
#   X, Y    two independent random SPD draws


def rel_fro(X, ref):
    """Relative Frobenius residual, batched over the leading stack axis."""
    return np.linalg.norm(X - ref, axis=(-2, -1)) / np.linalg.norm(ref, axis=(-2, -1))


def test_spd_eigh_rejects_nan():
    """A NaN is rejected at the shared primitive instead of propagating."""
    S = np.eye(3)
    S[0, 1] = np.nan
    with pytest.raises(ValueError, match="NaN or Inf"):
        spd_eigh(S)


@pytest.mark.parametrize("cond", [1e1, 1e3, 1e5])
@pytest.mark.parametrize("m", [2, 3, 12])
def test_round_trip(rng, m, cond):
    """exp(log(S)) == S.

    Forward composition -- it does not amplify by kappa in practice, so
    amplification=cond is deliberately loose here (up to ~4e4x slack at
    cond=1e5). Kept uniform with the other tests rather than fitted.
    """
    S = random_spd(rng, m=m, cond=cond, n=100)
    assert rel_fro(spd_exp(spd_log(S)), S).max() < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", [1e1, 1e3, 1e5])
@pytest.mark.parametrize("m", [2, 3, 12])
def test_inverses(rng, m, cond):
    """R is really a square root, and Ri really whitens S."""
    S = random_spd(rng, m=m, cond=cond, n=100)
    tol = num_tol(amplification=cond)

    R = spd_sqrt(S)
    assert rel_fro(R @ R, S).max() < tol

    Ri = spd_invsqrt(S)
    assert rel_fro(Ri @ S @ Ri, np.eye(m)).max() < tol


@pytest.mark.parametrize("cond", [1e1, 1e3, 1e5])
@pytest.mark.parametrize("m", [2, 3, 12])
def test_gmean_symmetry(rng, m, cond):
    """X # Y == Y # X.

    Exact as mathematics (Ando: the geometric mean is the largest Z with
    [[X, Z], [Z, Y]] >= 0, manifestly symmetric in X and Y), so any residual
    measured here is PURE implementation error -- there is no modelling slack
    to hide in.

    g_mean decomposes only its FIRST argument, so the two calls run entirely
    different arithmetic. Amplification is cond**2: the intermediate
    X**(-1/2) @ Y @ X**(-1/2) sandwiches a different matrix, nothing cancels,
    and its condition number reaches kappa(X) * kappa(Y).

    NOT swept to cond=1e8: there eps*kappa**2 ~ 1, the intermediate goes
    numerically indefinite, and spd_sqrt's strict guard raises before any
    number comes back. That is the guard working, not a bug -- but it is a
    hard ceiling on g_mean in float64 and it constrains B1.3 (AIRM).
    """
    X = random_spd(rng, m=m, cond=cond, n=200)
    Y = random_spd(rng, m=m, cond=cond, n=200)
    assert rel_fro(g_mean(X, Y), g_mean(Y, X)).max() < num_tol(amplification=cond**2)


# B1.3 -- affine-invariant Riemannian metric.
#
# Two tolerance regimes, measured rather than guessed:
#
#   DISTANCE identities   amplification = cond**2
#       airm_dist2 sandwiches a different matrix between two copies of
#       A^(-1/2), so nothing cancels and the intermediate reaches
#       kappa(A)*kappa(B). Same structure as g_mean. Min headroom ~11x.
#
#   BARYCENTRE identities amplification = cond
#       Much better behaved: the Karcher iterate is an average of logs, and
#       averaging is where the errors cancel. Min headroom ~4x.
#
# That the two differ by a whole power of kappa is worth noticing. It says the
# mean is numerically kinder than the metric it is built from.

N = 100
N_BARY = 20
BARY_TOL = 1e-10          # above the measured ~6e-12 floor at m=12, kappa=1e5
CONDS = [1e1, 1e3, 1e5]
MS = [3, 12]


def rel(x, ref):
    return np.abs(x - ref) / np.abs(ref)


def fro(X):
    return np.linalg.norm(X, axis=(-2, -1))


# ---------------------------------------------------------------- distance

@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_dist_zero_on_identical(rng, m, cond):
    A = random_spd(rng, m=m, cond=cond, n=N)
    assert airm_dist2(A, A).max() < num_tol(amplification=cond ** 2)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_dist_symmetry(rng, m, cond):
    """d2(A,B) == d2(B,A). The formula square-roots its first argument only,
    so the two calls run different arithmetic."""
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    d = airm_dist2(A, B)
    assert (np.abs(airm_dist2(B, A) - d) / d.mean()).max() < num_tol(
        amplification=cond ** 2)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_dist_affine_invariance(rng, m, cond):
    """d2(M A M', M B M') == d2(A, B) for ANY invertible M.

    THE defining property. BW satisfies this only for orthogonal M; AIRM
    satisfies it for every invertible one, and essentially no wrong
    implementation does.

    M has a controlled condition number for a reason -- see
    random_congruence's docstring.
    """
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    M = random_congruence(rng, m, n=N)
    d = airm_dist2(A, B)
    moved = airm_dist2(M @ A @ M.mT, M @ B @ M.mT)
    assert (np.abs(moved - d) / d.mean()).max() < num_tol(amplification=cond ** 2)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_dist_inversion_invariance(rng, m, cond):
    """d2(A^-1, B^-1) == d2(A, B).

    Distinctive: BW has no such property. It follows from M = A^(-1/2) style
    congruence plus the fact that log(Y^-1) = -log(Y), so it is a genuine
    check on the log rather than a restatement of affine invariance.
    """
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    d = airm_dist2(A, B)
    inv = airm_dist2(np.linalg.inv(A), np.linalg.inv(B))
    assert (np.abs(inv - d) / d.mean()).max() < num_tol(amplification=cond ** 2)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_dist_commuting_closed_form(rng, m, cond):
    """Shared eigenbasis => d2 = sum_i (log a_i - log b_i)**2.

    Scalar arithmetic on two spectra, no shared code path with the matrix
    log. This is what pins the metric; the invariance tests cannot.
    """
    Q = random_Q(rng, (N, m, m))
    a = spectrum(m, cond)
    b = spectrum(m, cond) * 2.5 + 1.0
    closed = ((np.log(a) - np.log(b)) ** 2).sum()
    got = airm_dist2(rebuild_spd(a, Q), rebuild_spd(b, Q))
    assert rel(got, closed).max() < num_tol(amplification=cond ** 2)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_dist_triangle(rng, m, cond):
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    C = random_spd(rng, m=m, cond=cond, n=N)
    slack = (np.sqrt(airm_dist2(A, B)) + np.sqrt(airm_dist2(B, C))
             - np.sqrt(airm_dist2(A, C)))
    assert (slack > -num_tol(amplification=cond ** 2)).all()


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_exp_log_roundtrip(rng, m, cond):
    """Exp_A(Log_A(B)) == B. Checks the two maps are actually inverse and
    that the tangent space bookkeeping is right."""
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    back = airm_exp(A, airm_log(A, B))
    assert (fro(back - B) / fro(B)).max() < num_tol(amplification=cond ** 2)


# ------------------------------------------------------------- barycentre

@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_affine_equivariance(rng, m, cond):
    """bary({M S_i M'}) == M bary({S_i}) M'.

    The original test contract's done-when, and it earns the billing: it constrains the whole
    iteration -- initialisation, gradient, retraction, stopping rule -- in
    one line, and it holds for arbitrary invertible M rather than only
    rotations.
    """
    S = random_spd_family(rng, m=m, cond=cond, delta=1.0, n=N_BARY)
    M = random_congruence(rng, m)
    a = airm_barycentre(S, tol=BARY_TOL)
    b = airm_barycentre(M @ S @ M.mT, tol=BARY_TOL)
    assert a.converged and b.converged
    ref = M @ a.X @ M.mT
    assert fro(b.X - ref) / fro(ref) < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_two_equals_gmean(rng, m, cond):
    """For N=2 the Karcher mean IS the geometric mean A # B.

    A cross-module check: g_mean lives in linalg.py and shares no code with
    the gradient descent here. Two independent routes to the same matrix.
    """
    S = random_spd_family(rng, m=m, cond=cond, delta=1.0, n=2)
    r = airm_barycentre(S, tol=BARY_TOL)
    assert r.converged
    ref = g_mean(S[0], S[1])
    assert fro(r.X - ref) / fro(ref) < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_commuting_closed_form(rng, m, cond):
    """Shared eigenbasis => the Karcher mean is the LOG-EUCLIDEAN mean,
    eigenvalues exp(mean_i log s_ij). Note this is exp-of-mean-log, where
    BW's was (mean sqrt)**2 -- the two geometries genuinely disagree even in
    the easy commuting case."""
    Q = random_Q(rng, (m, m))
    specs = np.array([spectrum(m, cond) * (1.0 + j) for j in range(N_BARY)])
    S = np.stack([rebuild_spd(s, Q) for s in specs])
    r = airm_barycentre(S, tol=BARY_TOL)
    assert r.converged
    ref = rebuild_spd(np.exp(np.log(specs).mean(axis=0)), Q)
    assert fro(r.X - ref) / fro(ref) < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_minimises_frechet(rng, m, cond):
    """Perturb the answer, the Frechet functional must rise. airm_frechet
    shares no code path with the iteration, so unlike the gradient-norm
    residual this cannot pass by construction. Perturbation is GEODESIC --
    an additive one leaves the cone at large kappa and the test silently
    stops asserting anything."""
    S = random_spd_family(rng, m=m, cond=cond, delta=1.0, n=N_BARY)
    r = airm_barycentre(S, tol=BARY_TOL)
    assert r.converged
    f0 = airm_frechet(r.X, S)
    for _ in range(20):
        E = rng.standard_normal((m, m))
        Xp = geodesic_perturb(r.X, E / np.linalg.norm(E))
        assert airm_frechet(Xp, S) > f0


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_barycentre_of_one(rng, m, cond):
    S = random_spd(rng, m=m, cond=cond, n=1)
    r = airm_barycentre(S, tol=BARY_TOL)
    assert fro(r.X - S[0]) / fro(S[0]) < num_tol(amplification=cond)


def test_weighted_barycentre_uses_relative_positive_weights(rng):
    S = random_spd(rng, m=3, cond=10.0, n=3)
    weights = np.array([1.0, 2.0, 4.0])
    first = airm_barycentre(S, weights=weights)
    scaled = airm_barycentre(S, weights=11.0 * weights)

    assert first.converged and scaled.converged
    np.testing.assert_allclose(first.X, scaled.X, rtol=2e-11, atol=2e-12)


def test_weighted_barycentre_one_hot_returns_selected_observation(rng):
    S = random_spd(rng, m=3, cond=10.0, n=3)
    result = airm_barycentre(S, weights=np.array([0.0, 1.0, 0.0]))

    assert result.converged
    np.testing.assert_allclose(result.X, S[1], rtol=2e-11, atol=2e-12)
