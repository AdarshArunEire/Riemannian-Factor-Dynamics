import numpy as np

from rfd.forecast import (
    fit_coordinate_har,
    fit_ridge_vhar,
    forecast_coordinate_har,
    forecast_ridge_vhar,
)


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
