"""Forecast heads, baselines and losses."""

from tests.conftest import geodesic_perturb, num_tol
import pytest

import numpy as np

from rfd._maths.spd import airm_barycentre, rebuild_spd
from rfd.forecast import LOSSES, airm_loss, ewma_forecasts, filter_score_state_space, fit_coordinate_har, fit_log_har, fit_ridge_vhar, fit_score_state_space, fit_var1, forecast_coordinate_har, forecast_log_har, forecast_ridge_vhar, forecast_score_state_space, frobenius_loss, locf_forecasts, logeuclid_barycentre, logeuclid_loss, qlike_loss, symmetric_coordinates, symmetric_matrices
from rfd.simulate import random_Q, random_congruence, random_spd, random_spd_family, spectrum

def _panel(n: int) -> np.ndarray:
    time = np.arange(n, dtype=float)
    output = np.zeros((n, 2, 2))
    output[:, 0, 0] = np.exp(0.01 * time)
    output[:, 1, 1] = np.exp(-0.004 * time)
    output[:, 0, 1] = output[:, 1, 0] = 0.02
    return output


def test_symmetric_coordinate_roundtrip():
    matrices = _panel(4)
    np.testing.assert_allclose(
        symmetric_matrices(symmetric_coordinates(matrices), 2), matrices
    )


def test_locf_and_ewma_are_causal_and_spd():
    training = _panel(20)
    targets = _panel(4) * 1.1
    locf = locf_forecasts(training[-1], targets)
    ewma = ewma_forecasts(training, targets, 0.8)

    np.testing.assert_allclose(locf[0], training[-1])
    np.testing.assert_allclose(locf[1], targets[0])
    assert np.all(np.linalg.eigvalsh(ewma) > 0.0)

    changed = targets.copy()
    changed[2:] *= 100.0
    np.testing.assert_allclose(
        ewma_forecasts(training, changed, 0.8)[:3], ewma[:3]
    )


def test_log_har_forecasts_are_spd_and_do_not_see_current_or_future_targets():
    training = _panel(220)
    targets = _panel(5) * 1.05
    fit = fit_log_har(training, daily_window=24, weekly_window=168)
    forecasts = forecast_log_har(fit, training, targets)
    assert forecasts.shape == targets.shape
    assert np.all(np.linalg.eigvalsh(forecasts) > 0.0)

    changed = targets.copy()
    changed[2:] *= 50.0
    np.testing.assert_allclose(
        forecast_log_har(fit, training, changed)[:3], forecasts[:3],
        rtol=1e-12, atol=1e-12,
    )


# B1.4 -- the loss module.
#
# Convention under test everywhere: loss(H, S) with H the forecast and S the
# target. The four distances do not care about order; QLIKE does, and one test
# below pins that asymmetry so a future refactor cannot quietly reverse it.
#
# Tolerances: amplification=cond throughout, except the AIRM congruence test
# which is a distance identity and needs cond**2. Min measured headroom ~10x.

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


def _noisy_ar1(seed: int = 19, n: int = 2400):
    rng = np.random.default_rng(seed)
    transition = np.array([[0.84, 0.06], [-0.03, 0.62]])
    state = np.zeros((n, 2))
    for index in range(1, n):
        state[index] = (
            transition @ state[index - 1]
            + 0.18 * rng.standard_normal(2)
        )
    observed = state + 0.55 * rng.standard_normal((n, 2))
    return state, observed


def test_kalman_filter_recovers_noisy_amplitudes_better_than_raw_scores():
    state, observed = _noisy_ar1()
    train = 1600

    fit = fit_score_state_space(observed[:train], max_iter=100)
    filtered = filter_score_state_space(observed, fit).filtered_states
    raw_error = np.mean((observed[train:] - state[train:]) ** 2)
    filtered_error = np.mean((filtered[train:] - state[train:]) ** 2)

    assert fit.converged
    assert filtered_error < 0.55 * raw_error


def test_kalman_head_improves_one_step_forecasts_under_measurement_noise():
    state, observed = _noisy_ar1(seed=23)
    train = 1600
    state_fit = fit_score_state_space(observed[:train], max_iter=100)
    kalman = filter_score_state_space(observed, state_fit)
    var = fit_var1(observed[:train])
    var_predictions = np.stack([
        var.forecast(observed[index - 1])
        for index in range(train, observed.shape[0])
    ])
    kalman_error = np.mean(
        (kalman.predicted_states[train:] - state[train:]) ** 2
    )
    var_error = np.mean((var_predictions - state[train:]) ** 2)

    assert kalman_error < var_error


def test_fixed_filter_is_causal_in_future_observations():
    _, observed = _noisy_ar1(seed=31, n=400)
    fit = fit_score_state_space(observed[:250], max_iter=80)
    changed = observed.copy()
    changed[330:] += 100.0

    original_result = filter_score_state_space(observed, fit)
    changed_result = filter_score_state_space(changed, fit)

    np.testing.assert_allclose(
        original_result.filtered_states[:330],
        changed_result.filtered_states[:330],
    )
    np.testing.assert_allclose(
        original_result.predicted_states[:331],
        changed_result.predicted_states[:331],
    )


def test_next_forecast_matches_the_transition_of_last_filtered_state():
    _, observed = _noisy_ar1(seed=37, n=400)
    fit = fit_score_state_space(observed[:300])

    forecast, filtered = forecast_score_state_space(observed[:300], fit)

    expected = fit.mean + fit.transition @ (
        filtered.filtered_states[-1] - fit.mean
    )
    np.testing.assert_allclose(forecast, expected)


def test_fitted_state_space_is_stable_and_covariances_are_positive():
    _, observed = _noisy_ar1(seed=47, n=600)

    fit = fit_score_state_space(observed)

    assert max(abs(np.linalg.eigvals(fit.transition))) < 1.0
    assert np.linalg.eigvalsh(fit.process_covariance).min() > 0.0
    assert np.linalg.eigvalsh(fit.measurement_covariance).min() > 0.0
    assert np.isfinite(fit.log_likelihood)


@pytest.mark.parametrize(
    "scores",
    [
        np.ones((7, 2)),
        np.ones((10, 0)),
        np.vstack((np.ones((9, 2)), [np.nan, 0.0])),
    ],
)
def test_state_space_rejects_invalid_training_scores(scores):
    with pytest.raises(ValueError):
        fit_score_state_space(scores)


def _scores(n: int = 260, rank: int = 3) -> np.ndarray:
    time = np.arange(n, dtype=float)
    return np.column_stack([
        np.sin(time / (8.0 + index)) + 0.002 * (index + 1) * time
        for index in range(rank)
    ])


def test_coordinate_har_shapes_and_scalar_rank_are_supported():
    scores = _scores(rank=1)
    fit = fit_coordinate_har(scores[:230])
    forecasts = forecast_coordinate_har(fit, scores[:230], scores[230:])

    assert fit.rank == 1
    assert fit.coefficients.shape == (4, 1)
    assert forecasts.shape == (30, 1)
    assert np.isfinite(forecasts).all()


def test_coordinate_har_is_causal_in_the_revealed_block():
    scores = _scores()
    training = scores[:230]
    revealed = scores[230:]
    fit = fit_coordinate_har(training)
    baseline = forecast_coordinate_har(fit, training, revealed)
    changed = revealed.copy()
    changed[5:] += 1000.0
    altered = forecast_coordinate_har(fit, training, changed)

    np.testing.assert_allclose(altered[:6], baseline[:6])
    assert not np.allclose(altered[6:], baseline[6:])


def test_ridge_vhar_is_invariant_to_component_rescaling():
    scores = _scores()
    scale = np.array([0.1, 3.0, 20.0])
    fit = fit_ridge_vhar(scores[:230], ridge=1e-3)
    scaled_fit = fit_ridge_vhar(scores[:230] * scale, ridge=1e-3)
    original = forecast_ridge_vhar(fit, scores[:230], scores[230:])
    scaled = forecast_ridge_vhar(
        scaled_fit, scores[:230] * scale, scores[230:] * scale
    )

    np.testing.assert_allclose(scaled / scale, original, rtol=1e-9, atol=1e-9)


def test_coordinate_har_does_not_use_other_score_coordinates():
    scores = _scores()
    fit = fit_coordinate_har(scores[:230])
    baseline = forecast_coordinate_har(fit, scores[:230], scores[230:])
    changed_training = scores[:230].copy()
    changed_training[:, 1:] *= 100.0
    changed_revealed = scores[230:].copy()
    changed_revealed[:, 1:] *= 100.0
    changed_fit = fit_coordinate_har(changed_training)
    changed = forecast_coordinate_har(
        changed_fit, changed_training, changed_revealed
    )

    np.testing.assert_allclose(changed[:, 0], baseline[:, 0])
