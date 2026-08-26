import numpy as np
import pytest

from rfd.forecast import (
    filter_score_state_space,
    forecast_score_state_space,
    fit_score_state_space,
    fit_var1,
)


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
