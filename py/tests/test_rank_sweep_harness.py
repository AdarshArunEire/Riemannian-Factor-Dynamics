from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.run_rank_sweep import (
    CONFIG_DEFAULT,
    _row_key,
    _selector_specs,
    build_tasks,
    load_configuration,
    plot_results,
    run_task,
    signal_parameters,
    summarize,
    validate_configuration,
)


def test_rank_grid_varies_dimension_and_rank_and_keeps_8192():
    oracle = load_configuration(CONFIG_DEFAULT, "rank_oracle")
    tasks = build_tasks(oracle)
    pairs = {(task.tangent_dimension, task.rank) for task in tasks}

    assert len(tasks) == 15_936
    assert {task.n for task in tasks} == {512, 2048, 8192}
    assert {task.tangent_dimension for task in tasks} == {3, 6, 10, 21, 36}
    assert (10, 8) in pairs
    assert (21, 10) in pairs
    assert (36, 10) in pairs
    assert all(rank < dimension for dimension, rank in pairs)


def test_feasible_grid_keeps_full_pipeline_8192_endpoint():
    feasible = load_configuration(CONFIG_DEFAULT, "rank_feasible")
    tasks = build_tasks(feasible)

    assert len(tasks) == 1_056
    assert {task.n for task in tasks} == {512, 2048, 8192}
    assert {task.tangent_dimension for task in tasks} == {6, 10}
    assert max(task.rank for task in tasks) == 8


@pytest.mark.parametrize("profile", ["equal", "decaying", "weak_tail"])
@pytest.mark.parametrize("rank", [1, 2, 6, 10])
def test_signal_profiles_preserve_total_factor_scale(profile, rank):
    config = load_configuration(CONFIG_DEFAULT, "rank_oracle")
    persistence, scales = signal_parameters(config, rank, profile)

    assert persistence.shape == scales.shape == (rank,)
    assert np.linalg.norm(scales) == pytest.approx(
        config["experiment"]["total_factor_scale"]
    )
    assert np.all(np.abs(persistence) < 1.0)
    if profile == "weak_tail" and rank > 1:
        assert scales[-1] < scales[0]


def test_rank_zero_is_not_duplicated_across_signal_profiles():
    config = load_configuration(CONFIG_DEFAULT, "rank_oracle")
    tasks = build_tasks(config)
    null = [
        task for task in tasks
        if task.n == 512 and task.matrix_size == 4 and task.rank == 0
    ]

    assert len(null) == config["profile"]["replicates"]
    assert {task.signal_profile for task in null} == {"equal"}


def test_oracle_smoke_produces_independent_selector_rows():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    tasks = build_tasks(config)
    assert len(tasks) == 3

    rows = run_task(config, tasks[1])
    assert len(rows) == len(_selector_specs(config)) == 7
    assert {row["method"] for row in rows} == {
        "threshold", "raw_ratio", "ridged_ratio"
    }
    assert all(row["status"] == "ok" for row in rows)
    assert len({_row_key(row) for row in rows}) == len(rows)
    assert all(np.isfinite(row["selected_rank"]) for row in rows)


def test_feasible_smoke_runs_complete_geometry_pipeline():
    config = load_configuration(CONFIG_DEFAULT, "feasible_smoke")
    rank_one = next(task for task in build_tasks(config) if task.rank == 1)
    rows = run_task(config, rank_one)

    assert all(row["status"] == "ok" for row in rows)
    assert all(row["mode"] == "feasible" for row in rows)
    assert all(row["tangent_dimension"] == 3 for row in rows)


def test_summary_reports_accuracy_and_error_direction(tmp_path: Path):
    rows = []
    for replicate, selected in enumerate((2, 1, 3, 2)):
        rows.append({
            "mode": "oracle", "n": 512, "matrix_size": 3,
            "tangent_dimension": 6, "true_rank": 2,
            "signal_profile": "equal", "method": "threshold",
            "ridge_multiplier": np.nan, "replicate": replicate,
            "status": "ok", "selected_rank": selected,
            "correct": int(selected == 2), "rank_error": selected - 2,
            "lambda_r": 0.1, "lambda_r_plus_1": 0.01,
            "signal_to_threshold": 10.0, "null_to_threshold": 1.0,
        })
    summary = summarize(pd.DataFrame(rows))

    assert summary["accuracy_percent"].iloc[0] == pytest.approx(50.0)
    assert summary["underselect_percent"].iloc[0] == pytest.approx(25.0)
    assert summary["overselect_percent"].iloc[0] == pytest.approx(25.0)
    plot_results(summary, tmp_path)
    assert (tmp_path / "plots" / "01_selector_accuracy_by_rank.png").is_file()
    assert (tmp_path / "plots" / "02_threshold_phase_map.png").is_file()


def test_configuration_rejects_invalid_mode_and_ridge():
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["profile"]["mode"] = "changing_rank"
    with pytest.raises(ValueError, match="mode"):
        validate_configuration(config)

    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["estimator"]["ridge_multipliers"] = [1.0, -1.0]
    with pytest.raises(ValueError, match="ridge_multipliers"):
        validate_configuration(config)
