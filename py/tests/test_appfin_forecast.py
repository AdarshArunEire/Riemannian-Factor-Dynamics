from pathlib import Path

import numpy as np
import pytest

import experiments.run_appfin_forecast as harness
from experiments.run_appfin_forecast import (
    CONFIG_DEFAULT,
    ROOT,
    baseline_forecasts,
    build_design,
    expanding_origins,
    load_configuration,
    parent_stage_digest,
    rfd_stage_digest,
    run_rfd_forecasts,
    score_forecasts,
    validate_configuration,
)
from experiments.run_appfin_identification import load_panel
from rfd.forecast import fit_var1, forecast_var1


def test_var1_recovers_the_parent_normal_equation_model():
    transition = np.array([[0.7, 0.1], [-0.2, 0.55]])
    intercept = np.array([0.3, -0.1])
    scores = np.empty((80, 2))
    scores[0] = np.array([1.2, -0.7])
    for index in range(1, scores.shape[0]):
        scores[index] = intercept + scores[index - 1] @ transition

    fit = fit_var1(scores)
    forecast, same_fit = forecast_var1(scores)

    np.testing.assert_allclose(fit.coefficients[0], intercept, atol=2e-10)
    np.testing.assert_allclose(fit.coefficients[1:], transition, atol=2e-10)
    np.testing.assert_allclose(
        forecast,
        intercept + scores[-1] @ transition,
        atol=1e-12,
    )
    np.testing.assert_allclose(same_fit.coefficients, fit.coefficients)


def test_var1_rejects_singular_scores_without_hiding_a_ridge():
    scores = np.ones((12, 2))
    with pytest.raises(np.linalg.LinAlgError, match="no ridge"):
        fit_var1(scores)


def test_frozen_forecast_contract_and_origins_are_exact():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_panel(config)
    design = build_design(config, panel, 36)

    assert design["initial_train_months"] == 204
    assert design["forecast_months"] == 36
    assert design["first_target_month"] == "2017-01"
    assert design["last_target_month"] == "2019-12"
    assert design["rank"] == 2
    assert design["max_lag"] == 6
    origins = expanding_origins(204, 36)
    assert origins[0] == (204, 204)
    assert origins[-1] == (239, 239)


def test_configuration_rejects_a_noncausal_or_misaligned_bridge():
    config = load_configuration(CONFIG_DEFAULT)
    config["rfd"]["future_centre_policy"] = "oracle"
    with pytest.raises(ValueError, match="carry_terminal"):
        validate_configuration(config)

    config = load_configuration(CONFIG_DEFAULT)
    config["experiment"]["forecast_months"] = 35
    with pytest.raises(ValueError, match="must equal"):
        validate_configuration(config)


def test_parent_worker_calls_the_literal_published_forecaster():
    source = (
        ROOT / "experiments" / "parent_rfm_forecast_worker.R"
    ).read_text(encoding="utf-8")
    assert "dyn_RFM(" in source
    assert '"main_func.R"' in source
    assert "test_size = test_size" in source
    assert "batch_size = batch_size" in source


def test_parent_cache_is_not_invalidated_by_an_rfd_only_change():
    baseline = load_configuration(CONFIG_DEFAULT)
    changed = load_configuration(CONFIG_DEFAULT)
    changed["rfd"]["forecast_step_margin"] = 0.1

    assert parent_stage_digest(baseline, 1) == parent_stage_digest(changed, 1)
    assert rfd_stage_digest(baseline, 1) != rfd_stage_digest(changed, 1)


def test_expanding_rfd_orchestrator_never_passes_the_target_to_the_fit(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    observations = np.stack([np.eye(2) * value for value in range(1, 7)])
    config = {"experiment": {"initial_train_months": 3}}
    seen = []

    def fake_origin(training, _config):
        seen.append(training.copy())
        forecast = training[-1].copy()
        diagnostics = {
            "forecast_clip_factor": 1.0,
            "forecast_min_eigenvalue": float(np.linalg.eigvalsh(forecast)[0]),
            "fallback_count": 0,
        }
        arrays = {
            "forecast": forecast,
            "terminal_centre": forecast,
            "forecast_score": np.array([0.0]),
            "var_coefficients": np.zeros((2, 1)),
            "lag_eigenvalues": np.array([1.0, 0.0]),
        }
        return forecast, diagnostics, arrays

    monkeypatch.setattr(harness, "run_rfd_origin", fake_origin)
    forecasts, _ = run_rfd_forecasts(
        observations,
        config,
        forecast_months=2,
        output=tmp_path,
        digest="unit-test",
        force=False,
    )

    assert [sample.shape[0] for sample in seen] == [3, 4]
    np.testing.assert_array_equal(seen[0], observations[:3])
    np.testing.assert_array_equal(seen[1], observations[:4])
    np.testing.assert_array_equal(forecasts[0], observations[2])
    assert (tmp_path / "rfd_origins" / "target_003.npz").is_file()
    assert (tmp_path / "rfd_origins" / "target_004.json").is_file()


def test_parent_ewma_and_loss_argument_order_are_explicit():
    observations = np.stack([np.eye(2) * value for value in range(1, 7)])
    baselines = baseline_forecasts(
        observations,
        initial_train_months=3,
        forecast_months=2,
        ewma_lambda=0.5,
    )
    np.testing.assert_array_equal(baselines["LOCF"][0], observations[2])
    expected_state = np.zeros((2, 2))
    for index in range(3):
        expected_state = 0.5 * expected_state + 0.5 * observations[index]
    np.testing.assert_allclose(baselines["EWMA"][0], expected_state)

    truth = observations[3:5]
    lagged = observations[2:4]
    long, summary = score_forecasts(
        {"perfect": truth.copy()},
        truth,
        lagged,
        np.array(["a", "b"]),
    )
    np.testing.assert_allclose(long["frobenius2"], 0.0)
    np.testing.assert_allclose(long["qlike"], 0.0)
    assert summary.loc[0, "method"] == "perfect"
