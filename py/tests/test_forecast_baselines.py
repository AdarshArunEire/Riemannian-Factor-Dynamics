import numpy as np

from rfd.forecast_baselines import (
    ewma_forecasts,
    fit_log_har,
    forecast_log_har,
    locf_forecasts,
    symmetric_coordinates,
    symmetric_matrices,
)


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
