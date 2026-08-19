"""B1.4 -- the loss module.

Convention under test everywhere: loss(H, S) with H the forecast and S the
target. The four distances do not care about order; QLIKE does, and one test
below pins that asymmetry so a future refactor cannot quietly reverse it.

Tolerances: amplification=cond throughout, except the AIRM congruence test
which is a distance identity and needs cond**2. Min measured headroom ~10x.
"""

import numpy as np
import pytest

from rfd.dgp.spd import (random_spd, random_spd_family, random_Q,
                         random_congruence, spectrum)
from rfd.spd.linalg import rebuild_spd, spd_log, spd_exp
from rfd.spd.airm import airm_barycentre
from rfd.eval.losses import (frobenius_loss, bw_loss, airm_loss,
                             logeuclid_loss, qlike_loss,
                             logeuclid_barycentre, LOSSES)
from tests.conftest import num_tol, geodesic_perturb

N = 200
N_BARY = 20
CONDS = [1e1, 1e3, 1e5]
MS = [3, 12]


def fro(X):
    return np.linalg.norm(X, axis=(-2, -1))


# --------------------------------------------------------------- all losses

@pytest.mark.parametrize("name", sorted(LOSSES))
@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_zero_iff_equal(rng, m, cond, name):
    """Every loss is zero on identical arguments and strictly positive on
    different ones. Necessary for all five, sufficient for none -- but a sign
    error or a dropped term shows up here first.

    Normalised by the loss between DIFFERENT matrices, which is the one
    denominator that is meaningful for all five at once: the four distances
    and QLIKE carry different units and no common absolute scale exists.

    DELIBERATELY LOOSE: amplification=cond**2 rather than cond. The binding
    case is BW, whose d2 is a difference of large traces and so leaves ~1e-14
    of relative residue on identical arguments -- only 1.4x inside the cond
    tolerance at cond=1e1. BW already has a tight dedicated zero test in
    test_bw.py normalised by the trace scale; this one is a five-way smoke
    check and can afford the slack.
    """
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    loss = LOSSES[name]

    baseline = loss(A, B)
    assert (baseline > 0).all()
    assert (np.abs(loss(A, A)) / baseline.mean()).max() < num_tol(
        amplification=cond ** 2)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_qlike_is_asymmetric(rng, m, cond):
    """qlike(H, S) != qlike(S, H), by a lot.

    This is the test that protects the argument convention. If someone
    reverses the order in a refactor the four distances stay green and only
    this one moves -- which is exactly why it is here rather than trusted to
    a docstring.
    """
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    fwd, rev = qlike_loss(A, B), qlike_loss(B, A)
    rel = np.abs(fwd - rev) / (0.5 * (fwd + rev))
    assert rel.max() > 1e-3          # not a metric, and provably so


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_qlike_minimised_at_truth(rng, m, cond):
    """QLIKE is minimised at H = S. Perturb the forecast away from the
    target and the score must rise -- the property that makes it usable as
    a forecast loss at all."""
    S = random_spd(rng, m=m, cond=cond, n=1)[0]
    f0 = qlike_loss(S, S)
    for _ in range(20):
        E = rng.standard_normal((m, m))
        H = geodesic_perturb(S, E / np.linalg.norm(E))
        assert qlike_loss(H, S) > f0


# -------------------------------------------------------------- Frobenius

@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_frobenius_matches_entrywise(rng, m, cond):
    """||H - S||_F^2 == sum of squared entries. Trivial, and the only loss
    where a closed form this direct is available."""
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    direct = ((A - B) ** 2).sum(axis=(-2, -1))
    got = frobenius_loss(A, B)
    assert (np.abs(got - direct) / direct).max() < num_tol(amplification=cond)


# ----------------------------------------------------------- log-Euclidean

@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_logeuclid_equals_airm_when_commuting(rng, m, cond):
    """On a shared eigenbasis, log-Euclidean and AIRM agree exactly.

    The sharpest statement of what log-Euclidean IS: the flat approximation
    that coincides with AIRM wherever the cone is not being curved by
    non-commutativity. Two independent implementations, one answer.
    """
    Q = random_Q(rng, (N, m, m))
    a = spectrum(m, cond)
    b = spectrum(m, cond) * 2.5 + 1.0
    A, B = rebuild_spd(a, Q), rebuild_spd(b, Q)
    le, ai = logeuclid_loss(A, B), airm_loss(A, B)
    assert (np.abs(le - ai) / ai).max() < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_logeuclid_commuting_closed_form(rng, m, cond):
    """sum_i (log a_i - log b_i)**2 -- scalar arithmetic on two spectra."""
    Q = random_Q(rng, (N, m, m))
    a = spectrum(m, cond)
    b = spectrum(m, cond) * 2.5 + 1.0
    closed = ((np.log(a) - np.log(b)) ** 2).sum()
    got = logeuclid_loss(rebuild_spd(a, Q), rebuild_spd(b, Q))
    assert (np.abs(got - closed) / closed).max() < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_airm_invariant_logeuclid_is_not(rng, m, cond):
    """A NEGATIVE CONTROL, and the one that keeps the two apart.

    Under congruence by an invertible M, the AIRM loss is unchanged and the
    log-Euclidean loss is not. Asserting only the first would leave a bug
    that computed AIRM twice completely invisible; asserting the second
    catches it.

    Measured: log-Euclidean moves by 15-110% of its own value.
    """
    A = random_spd(rng, m=m, cond=cond, n=N)
    B = random_spd(rng, m=m, cond=cond, n=N)
    M = random_congruence(rng, m, n=N)
    MA, MB = M @ A @ M.mT, M @ B @ M.mT

    ai = airm_loss(A, B)
    assert (np.abs(airm_loss(MA, MB) - ai) / ai.mean()).max() < num_tol(
        amplification=cond ** 2)

    le = logeuclid_loss(A, B)
    assert (np.abs(logeuclid_loss(MA, MB) - le) / le.mean()).max() > 1e-3


# ------------------------------------------------------ log-Euclidean mean

@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_logeuclid_barycentre_equals_airm_when_commuting(rng, m, cond):
    """On a commuting family the log-Euclidean and Karcher means coincide.

    The load-bearing test for logeuclid_barycentre: comparing it against
    exp(mean(log)) would just restate its own definition. This compares it
    against an entirely different algorithm -- gradient descent in airm.py --
    that happens to land in the same place when the cone is flat.
    """
    Q = random_Q(rng, (m, m))
    specs = np.array([spectrum(m, cond) * (1.0 + j) for j in range(N_BARY)])
    S = np.stack([rebuild_spd(s, Q) for s in specs])
    le = logeuclid_barycentre(S)
    karcher = airm_barycentre(S, tol=1e-10, max_iter=500)
    assert karcher.converged
    assert fro(le - karcher.X) / fro(karcher.X) < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_logeuclid_barycentre_minimises_its_loss(rng, m, cond):
    """Perturb geodesically, the mean log-Euclidean loss must rise."""
    S = random_spd_family(rng, m=m, cond=cond, delta=1.0, n=N_BARY)
    X = logeuclid_barycentre(S)
    f0 = logeuclid_loss(np.broadcast_to(X, S.shape), S).mean()
    for _ in range(20):
        E = rng.standard_normal((m, m))
        Xp = geodesic_perturb(X, E / np.linalg.norm(E))
        assert logeuclid_loss(np.broadcast_to(Xp, S.shape), S).mean() > f0


@pytest.mark.parametrize("cond", CONDS)
@pytest.mark.parametrize("m", MS)
def test_logeuclid_barycentre_of_one(rng, m, cond):
    S = random_spd(rng, m=m, cond=cond, n=1)
    assert fro(logeuclid_barycentre(S) - S[0]) / fro(S[0]) < num_tol(
        amplification=cond)
