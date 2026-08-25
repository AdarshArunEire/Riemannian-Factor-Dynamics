from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.run_end_to_end import (
    CONFIG_8192,
    CONFIG_DEFAULT,
    RAW_COLUMNS,
    analysis_rows,
    bandwidth_variants,
    build_tasks,
    load_configuration,
    maximum_admissible_multiplier,
    paired_contrasts,
    plot_results,
    production_multiplier,
    run_task,
    summarize,
    validate_configuration,
)
from rfd.geometry import AIRM_GEOMETRY


def test_capped_schedule_uses_more_bandwidth_then_stops_growing():
    config = load_configuration(CONFIG_DEFAULT, "factor_baseline")
    estimator = config["estimator"]
    values = [production_multiplier(n, estimator) for n in (256, 512, 1024, 2048, 4096, 8192)]

    assert np.all(np.diff(values) >= 0.0)
    assert values[-1] == pytest.approx(2.1)
    assert values[-2] < 2.1
    assert all(value <= 2.1 for value in values)


def test_every_bandwidth_variant_is_strictly_inside_the_boundary():
    config = load_configuration(CONFIG_DEFAULT, "factor_baseline")
    estimator = config["estimator"]
    for n in config["profile"]["n_values"]:
        maximum = maximum_admissible_multiplier(
            n,
            bandwidth_constant=estimator["bandwidth_constant"],
            bandwidth_exponent=estimator["bandwidth_exponent"],
            overlap_fractions=tuple(estimator["overlap_fractions"]),
        )
        assert max(bandwidth_variants(n, estimator).values()) < maximum


def test_recorded_workload_and_seed_namespace_are_stable():
    recorded = load_configuration(CONFIG_DEFAULT, "factor_baseline")
    smoke = load_configuration(CONFIG_DEFAULT, "smoke")
    tasks = build_tasks(recorded)

    assert len(tasks) == 4 * 3 * 32
    assert len(tasks) * 2 == 768
    assert not np.array_equal(
        tasks[0].seed_sequence.generate_state(8),
        build_tasks(smoke)[0].seed_sequence.generate_state(8),
    )


def test_8192_extension_is_separate_reaches_cap_and_has_fresh_seeds():
    original = load_configuration(CONFIG_DEFAULT, "factor_baseline")
    extension = load_configuration(CONFIG_8192, "factor_baseline_8192")
    original_tasks = build_tasks(original)
    extension_tasks = build_tasks(extension)

    assert len(extension_tasks) == 3 * 32
    assert len(extension_tasks) * 2 == 192
    assert extension["profile"]["seed_namespace"] == 4502
    assert extension["estimator"] == original["estimator"]
    original_experiment = {
        key: value for key, value in original["experiment"].items() if key != "id"
    }
    extension_experiment = {
        key: value for key, value in extension["experiment"].items() if key != "id"
    }
    assert extension_experiment == original_experiment
    assert production_multiplier(8192, extension["estimator"]) == pytest.approx(2.1)
    assert not np.array_equal(
        original_tasks[0].seed_sequence.generate_state(8),
        extension_tasks[0].seed_sequence.generate_state(8),
    )


def test_combined_analysis_rejects_overlapping_rows(tmp_path: Path):
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": "old", "n": 8192, "matrix_size": 2, "replicate": 0,
        "variant": "production", "status": "ok",
    })
    source = tmp_path / "source.csv"
    pd.DataFrame([row]).to_csv(source, index=False)
    config = deepcopy(load_configuration(CONFIG_8192, "factor_baseline_8192"))
    config["profile"]["analysis_include_raw"] = [str(source)]

    with pytest.raises(ValueError, match="overlapping result rows"):
        analysis_rows(config, pd.DataFrame([row]))


def test_configuration_rejects_boundary_hugging_reference():
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["estimator"]["reference_multiplier"] = 99.0
    with pytest.raises(ValueError, match="violates the boundary"):
        validate_configuration(config)


def test_tiny_task_runs_the_whole_pipeline_twice_on_one_draw():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    task = build_tasks(config)[0]
    rows = run_task(config, task, AIRM_GEOMETRY)

    assert [row["variant"] for row in rows] == ["production", "reference"]
    assert [row["status"] for row in rows] == ["ok", "ok"]
    assert rows[0]["seed_spawn_key"] == rows[1]["seed_spawn_key"]
    for row in rows:
        assert row["tangent_dimension"] == 3
        assert row["fixed_fit_rank"] == row["true_rank"] == 2
        assert row["lag_row_error"] >= 0.0
        assert row["operator_error"] <= row["assembly_bound"] + 1e-12
        assert row["null_eigenvalue"] <= row["lag_row_error"] ** 2 + 1e-12
        assert 0.0 <= row["loading_subspace_error"] <= 1.0 + 1e-12
        assert np.isfinite(row["factor_score_nrmse"])
        assert np.isfinite(row["signal_reconstruction_rms"])
        assert row["fallback_count"] >= 0


def test_summary_percentages_and_largest_matrix_plot_render(tmp_path: Path):
    rows = []
    for replicate in range(3):
        common = {
            "status": "ok", "n": 512, "matrix_size": 4,
            "tangent_dimension": 10, "replicate": replicate,
            "true_rank": 2, "threshold_rank": 2,
            "ridged_ratio_rank": 2, "raw_ratio_rank": 1,
            "oracle_lag_row_size": 1.0, "operator_error": 0.1,
            "oracle_gap": 0.5, "assembly_gap_ratio": 0.2,
            "null_eigenvalue": 0.01, "empirical_energy_R": 0.8,
            "elapsed_seconds": 1.0, "bandwidth_multiplier": 1.5,
            "factor_score_nrmse": 0.3, "observation_reconstruction_rms": 0.4,
            "signal_reconstruction_rms": 0.2,
        }
        rows.extend([
            {**common, "variant": "reference", "centre_path_rms": 0.10,
             "lag_row_error": 0.08, "loading_subspace_error": 0.20},
            {**common, "variant": "production", "centre_path_rms": 0.08,
             "lag_row_error": 0.06, "loading_subspace_error": 0.15},
        ])
    raw = pd.DataFrame(rows)
    summary = summarize(raw)
    contrasts = paired_contrasts(raw)

    assert len(summary) == 2
    assert summary.loc[
        summary["variant"] == "production", "threshold_rank_accuracy_percent"
    ].iloc[0] == 100.0
    assert contrasts["centre_path_rms_reduction_percent_median"].iloc[0] == pytest.approx(20.0)
    assert contrasts["loading_subspace_error_reduction_percent_median"].iloc[0] == pytest.approx(25.0)

    plot_results(summary, contrasts, tmp_path)
    assert (tmp_path / "plots" / "01_end_to_end_rates.png").is_file()
    assert (tmp_path / "plots" / "02_paired_loading_gain.png").is_file()
    assert (tmp_path / "plots" / "03_rank_accuracy.png").is_file()
