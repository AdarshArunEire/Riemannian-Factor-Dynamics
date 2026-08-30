from pathlib import Path

import numpy as np
import pytest

import experiments.run_appfin_score_filter as harness
from experiments.run_appfin_score_filter import (
    CONFIG_DEFAULT,
    METHOD_LABELS,
    _decode,
    _run_rfd_origins,
    build_design,
    load_configuration,
    parent_origin,
    validate_configuration,
)
from experiments.run_appfin_identification import load_panel
from rfd.forecast import forecast_var1
from rfd.geometry import BW_GEOMETRY


def _write(path: Path, value: np.ndarray) -> None:
    np.savetxt(path, np.asarray(value).reshape(np.asarray(value).shape[0], -1), delimiter=",")


def test_appfin_score_filter_contract_is_the_frozen_four_arm_replay():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_panel(config["source"])
    design = build_design(config, panel, 36)

    assert design["initial_train_months"] == 204
    assert design["forecast_months"] == 36
    assert design["first_target_month"] == "2017-01"
    assert design["last_target_month"] == "2019-12"
    assert design["rank"] == 2
    assert design["methods"] == list(METHOD_LABELS.values())
    assert "no latent-score truth" in design["scope"]

    worker = harness.R_WORKER.read_text(encoding="utf-8")
    assert "resume <-" in worker
    assert 'parent score origin", target_index, "reused' in worker
    assert 'saveRDS(.Random.seed' in worker
    assert 'assign(".Random.seed"' in worker


def test_score_filter_configuration_rejects_unstable_or_invalid_guards():
    config = load_configuration(CONFIG_DEFAULT)
    config["head"]["maximum_transition_radius"] = 1.0
    with pytest.raises(ValueError, match="maximum_transition_radius"):
        validate_configuration(config)

    config = load_configuration(CONFIG_DEFAULT)
    config["head"]["bw_step_margin"] = 0.0
    with pytest.raises(ValueError, match="bw_step_margin"):
        validate_configuration(config)


def test_uniform_bw_decoder_returns_spd_and_reports_clipping():
    centre = np.eye(2)
    tangent = np.diag([-4.0, 0.2])
    forecast, health = _decode(centre, tangent, step_margin=0.05)

    assert np.linalg.eigvalsh(forecast)[0] > 0.0
    assert 0.0 < health["clip_factor"] < 1.0
    assert health["raw_step_min_eigenvalue"] < 0.0
    assert health["forecast_condition_number"] >= 1.0


def test_parent_origin_changes_only_the_score_head(tmp_path: Path):
    config = load_configuration(CONFIG_DEFAULT)
    rank = 2
    matrix_size = 2
    scores = np.empty((40, rank))
    scores[0] = np.array([0.1, -0.05])
    for index in range(1, len(scores)):
        scores[index] = np.array([0.01, -0.005]) + scores[index - 1] @ np.array(
            [[0.75, 0.05], [-0.03, 0.6]]
        )
    var_score, _ = forecast_var1(scores)
    centre = np.eye(matrix_size)
    row_mean = np.zeros((matrix_size, matrix_size))
    loadings = np.array([
        [[0.08, 0.0], [0.0, 0.0]],
        [[0.0, 0.02], [0.02, 0.0]],
    ])
    tangent = row_mean + np.tensordot(var_score, loadings, axes=([-1], [0]))
    r_forecast = BW_GEOMETRY.exp(centre, tangent)

    _write(tmp_path / "scores.csv", scores)
    _write(tmp_path / "loadings.csv", loadings)
    _write(tmp_path / "row_mean_tangent.csv", row_mean[None])
    _write(tmp_path / "mean.csv", centre[None])
    _write(tmp_path / "var_score.csv", var_score[None])
    _write(tmp_path / "var_forecast.csv", r_forecast[None])

    result, health = parent_origin(tmp_path, rank, matrix_size, config)

    assert set(result) == {"var", "kf"}
    assert result["var"].shape == (2, 2)
    assert result["kf"].shape == (2, 2)
    assert health["var_score_r_parity_error"] < 1e-12
    assert health["var_forecast_r_parity_error"] < 1e-12
    assert health["kf_transition_radius"] < 1.0


def test_rfd_expanding_replay_never_passes_the_target_to_fit(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    config = load_configuration(CONFIG_DEFAULT)
    config["source"]["experiment"]["initial_train_months"] = 3
    observations = np.stack([np.eye(2) * value for value in range(1, 7)])
    seen = []

    def fake_origin(training, _config):
        seen.append(training.copy())
        forecast = training[-1].copy()
        health = {"var_clip_factor": 1.0, "kf_clip_factor": 1.0}
        arrays = {
            "var": forecast,
            "kf": forecast,
            "scores": np.zeros((len(training), 1)),
            "var_score": np.zeros(1),
            "kf_score": np.zeros(1),
            "lag_eigenvalues": np.ones(2),
        }
        return {"var": forecast, "kf": forecast}, health, arrays

    monkeypatch.setattr(harness, "rfd_origin", fake_origin)
    result, _ = _run_rfd_origins(
        observations, config, 2, tmp_path, "unit-test", force=False
    )

    assert [sample.shape[0] for sample in seen] == [3, 4]
    np.testing.assert_array_equal(seen[0], observations[:3])
    np.testing.assert_array_equal(seen[1], observations[:4])
    np.testing.assert_array_equal(result["var"][0], observations[2])
    assert (tmp_path / "rfd_origins" / "target_003.npz").is_file()
    assert (tmp_path / "rfd_origins" / "target_004.json").is_file()
