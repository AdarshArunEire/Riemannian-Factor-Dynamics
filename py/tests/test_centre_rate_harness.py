from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd

from experiments.run_centre_rate import (
    CONFIG_DEFAULT,
    Scenario,
    _bootstrap_slopes,
    _cell_summary,
    _intrinsic_rms,
    _target_and_actual_centre_configs,
    build_tasks,
    centre_path,
    load_configuration,
    run_task,
    scenarios_from_configuration,
)
from rfd.geometry import AIRM_GEOMETRY


def test_all_declared_profiles_parse_and_have_the_locked_workloads():
    expected_rows = {
        "smoke": 6,
        "centre_rate": 3456,
        "discrepancy": 2304,
    }
    for profile_name, expected in expected_rows.items():
        config = load_configuration(CONFIG_DEFAULT, profile_name)
        tasks = build_tasks(config)
        rows = len(tasks) * len(config["profile"]["bandwidth_multipliers"])
        assert rows == expected


def test_recorded_profiles_separate_rate_and_discrepancy_claims():
    rate = load_configuration(CONFIG_DEFAULT, "centre_rate")
    discrepancy = load_configuration(CONFIG_DEFAULT, "discrepancy")

    assert [item.label for item in scenarios_from_configuration(rate)] == [
        "bias_only",
        "variance_only",
        "full",
    ]
    assert all(
        item.regime == "discrepancy_coherent"
        for item in scenarios_from_configuration(discrepancy)
    )
    assert np.isclose(
        max(rate["profile"]["bandwidth_multipliers"])
        * rate["estimator"]["bandwidth_constant"]
        * min(rate["profile"]["n_values"])
        ** (-rate["estimator"]["bandwidth_exponent"]),
        0.2943601909,
    )


def test_controlled_centre_discrepancy_has_the_declared_power():
    config = load_configuration(CONFIG_DEFAULT, "discrepancy")
    scenario = Scenario("discrepancy_coherent", 0.25)
    time = np.linspace(0.0, 1.0, 41)
    measured = []
    for n in (256, 512):
        target, actual = _target_and_actual_centre_configs(config, scenario, n)
        target_points = centre_path(time, AIRM_GEOMETRY, target)
        actual_points = centre_path(time, AIRM_GEOMETRY, actual)
        measured.append(
            _intrinsic_rms(AIRM_GEOMETRY, actual_points, target_points)
        )

    assert np.isclose(measured[0] / measured[1], 2.0**0.25, rtol=2e-12)


def test_one_real_harness_task_returns_a_complete_finite_row(tmp_path: Path):
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["profile"]["n_values"] = [64]
    config["profile"]["regimes"] = ["bias_only"]
    config["profile"]["discrepancy_exponents"] = []
    config["profile"]["bandwidth_multipliers"] = [0.7]
    tasks = build_tasks(config)

    rows = run_task(
        config,
        tasks[0],
        AIRM_GEOMETRY,
        [0.7],
        tmp_path / "examples",
    )

    assert len(rows) == 1
    row = rows[0]
    assert row["status"] == "ok"
    assert np.isfinite(row["path_rms"])
    assert np.isfinite(row["broad_path_rms"])
    assert row["minimum_ess"] > 1.0
    assert row["nonconverged_stages"] == 0


def test_summary_and_bootstrap_recover_an_exact_synthetic_slope():
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["profile"]["slope_fit_n_min"] = 128
    config["profile"]["bootstrap_replicates"] = 25
    rows = []
    for n in (128, 256, 512):
        for replicate in range(4):
            value = (1.0 + 0.01 * replicate) * n ** (-3.0 / 7.0)
            rows.append(
                {
                    "status": "ok",
                    "regime": "full",
                    "a_label": "none",
                    "bandwidth_multiplier": 1.0,
                    "n": n,
                    "path_rms": value,
                    "vertex_rms": value,
                    "path_sup": 2.0 * value,
                    "broad_path_rms": 1.2 * value,
                    "richardson_gain": 1.2,
                    "actual_centre_rms": 0.0,
                    "paired_discrepancy_rms": 0.0,
                    "fallback_rate": 0.0,
                    "minimum_ess": 20.0,
                    "maximum_iterations": 3,
                    "elapsed_seconds": 0.1,
                }
            )
    raw = pd.DataFrame.from_records(rows)

    summary = _cell_summary(raw)
    slopes = _bootstrap_slopes(raw, config)
    primary = slopes.loc[slopes["metric"] == "path_rms"].iloc[0]

    assert len(summary) == 3
    assert np.isclose(primary["slope"], -3.0 / 7.0, atol=1e-12)
    assert primary["slope_q025"] < -0.40
    assert primary["slope_q975"] > -0.46
