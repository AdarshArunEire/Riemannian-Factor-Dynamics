from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.analyze_paper1_controls import core_summary, paired_effects
from experiments.run_paper1_controls import (
    CONFIG_DEFAULT,
    ControlTask,
    _control_directions,
    build_tasks,
    generate_control_sample,
    load_configuration,
    resolved_regimes,
    run,
    run_task,
)
from rfd.estimators.lag import tangent_coordinates
from rfd.geometry import AIRM_GEOMETRY


def test_frozen_workloads_have_every_declared_cell():
    core = load_configuration(CONFIG_DEFAULT, "control_core")
    phase = load_configuration(CONFIG_DEFAULT, "phase_curve")

    assert len(resolved_regimes(core)) == 11
    assert len(build_tasks(core)) == 11 * 3 * 32 == 1056
    assert len(resolved_regimes(phase)) == 15
    assert len(build_tasks(phase)) == 15 * 32 == 480


@pytest.mark.parametrize(
    ("regime", "expected_overlap"),
    [("I-A", 1.0), ("I-M", 1.0 / np.sqrt(2.0)), ("I-O", 0.0)],
)
def test_complete_loading_span_has_the_declared_drift_overlap(
    regime, expected_overlap
):
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    # n enters the component seed.  n=128 caught a projection bug in which a
    # later mixed loading regained a component along the drift direction.
    task = ControlTask(128, 0, regime, config["core_regimes"][regime])
    sample, base, drift = generate_control_sample(config, task, AIRM_GEOMETRY)

    overlap = np.linalg.norm([
        AIRM_GEOMETRY.inner(base, loading, drift) for loading in sample.loadings
    ])
    assert overlap == pytest.approx(expected_overlap, abs=5e-9)


def test_component_streams_are_shared_across_compatible_regimes():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    first_task = ControlTask(64, 0, "B0", config["core_regimes"]["B0"])
    second_task = ControlTask(64, 0, "C0", config["core_regimes"]["C0"])
    moving, moving_base, _ = generate_control_sample(config, first_task, AIRM_GEOMETRY)
    fixed, fixed_base, _ = generate_control_sample(config, second_task, AIRM_GEOMETRY)

    moving_noise = AIRM_GEOMETRY.transport(
        moving.tangent_noise, moving.centres, moving_base
    )
    fixed_noise = AIRM_GEOMETRY.transport(
        fixed.tangent_noise, fixed.centres, fixed_base
    )
    assert np.allclose(moving.factors, fixed.factors)
    assert np.allclose(moving.loadings, fixed.loadings)
    assert np.allclose(moving_noise, fixed_noise)


def test_curved_path_uses_two_tangent_directions_but_radial_uses_one():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    curved_task = ControlTask(64, 0, "G-C", config["core_regimes"]["G-C"])
    radial_task = ControlTask(64, 0, "B0", config["core_regimes"]["B0"])
    curved, base, _ = generate_control_sample(config, curved_task, AIRM_GEOMETRY)
    radial, _, _ = generate_control_sample(config, radial_task, AIRM_GEOMETRY)
    basis = AIRM_GEOMETRY.tangent_basis(base)
    curved_rows = tangent_coordinates(
        AIRM_GEOMETRY.log(base, curved.centres), base, basis, AIRM_GEOMETRY
    )
    radial_rows = tangent_coordinates(
        AIRM_GEOMETRY.log(base, radial.centres), base, basis, AIRM_GEOMETRY
    )

    assert np.linalg.matrix_rank(curved_rows, tol=1e-10) == 2
    assert np.linalg.matrix_rank(radial_rows, tol=1e-10) == 1


def test_rough_and_smooth_paths_share_endpoints_but_not_midpoints():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    smooth_task = ControlTask(64, 0, "B0", config["core_regimes"]["B0"])
    rough_task = ControlTask(64, 0, "V-R", config["core_regimes"]["V-R"])
    smooth, _, _ = generate_control_sample(config, smooth_task, AIRM_GEOMETRY)
    rough, _, _ = generate_control_sample(config, rough_task, AIRM_GEOMETRY)

    assert np.allclose(smooth.centres[-1], rough.centres[-1])
    assert not np.allclose(smooth.centres[31], rough.centres[31])


@pytest.mark.parametrize("regime", ["C0", "C1", "G-C", "V-L", "V-R"])
def test_representative_smoke_tasks_complete(regime):
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    row = run_task(
        config, ControlTask(64, 0, regime, config["core_regimes"][regime])
    )

    assert row["status"] == "ok"
    assert row["rfd_fallback_count"] >= 0
    assert row["rfd_nonconverged_stages"] == 0
    assert np.isfinite(row["rfd_centre_path_rms"])
    if row["true_rank"] == 0:
        assert np.isnan(row["rfd_loading_error"])


def test_parallel_runner_is_resume_safe_and_parent_written(tmp_path: Path):
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["core_regimes"] = {"C0": config["core_regimes"]["C0"]}
    config["profile"]["n_values"] = [64]
    config["profile"]["output_dir"] = str(tmp_path / "parallel")

    run(config, workers=2)
    run(config, workers=2)
    raw = pd.read_csv(tmp_path / "parallel" / "raw.csv")

    assert len(raw) == 1
    assert raw["status"].iloc[0] == "ok"


def test_analysis_reports_mean_median_bootstrap_and_win_rate():
    rows = pd.DataFrame({
        "status": ["ok"] * 4,
        "regime": ["C0"] * 4,
        "regime_label": ["fixed"] * 4,
        "regime_class": ["null"] * 4,
        "n": [512] * 4,
        "true_rank": [2] * 4,
        "rfd_threshold_rank": [2] * 4,
        "known_centre_threshold_rank": [2] * 4,
        "fixed_centre_threshold_rank": [2] * 4,
        "rfd_nonconverged_stages": [0] * 4,
        "rfd_fallback_count": [0] * 4,
        "rfd_centre_path_rms": [0.1] * 4,
        "rfd_loading_angle_degrees": [1.0] * 4,
        "rfd_factor_nrmse": [0.2, 0.3, 0.2, 0.3],
        "rfd_loading_error": [0.1, 0.2, 0.1, 0.2],
        "rfd_observation_reconstruction_rms": [0.8, 0.9, 0.8, 0.9],
        "rfd_signal_reconstruction_rms": [0.7, 0.8, 0.7, 0.8],
        "known_centre_loading_error": [0.05] * 4,
        "known_centre_factor_nrmse": [0.1] * 4,
        "known_centre_observation_reconstruction_rms": [0.7] * 4,
        "fixed_centre_loading_error": [0.2, 0.4, 0.2, 0.4],
        "fixed_centre_factor_nrmse": [0.4] * 4,
        "fixed_centre_observation_reconstruction_rms": [1.0] * 4,
        "fixed_centre_signal_reconstruction_rms": [1.0] * 4,
        "noise_lag_row_size": [0.01] * 4,
        "rfd_fallback_rate": [0.0] * 4,
    })

    summary = core_summary(rows)
    effects = paired_effects(rows, repeats=200, seed=5)

    assert "rfd_factor_nrmse_mean" in summary
    assert "rfd_factor_nrmse_median" in summary
    observation = effects.loc[effects["metric"] == "observation reconstruction"].iloc[0]
    assert observation["median_improvement_percent"] == pytest.approx(15.0)
    assert observation["rfd_win_percent"] == 100.0
