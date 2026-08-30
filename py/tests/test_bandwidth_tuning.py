from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd

from experiments.run_bandwidth_tuning import (
    CONFIG_DEFAULT,
    score_candidates,
    validation_configuration,
    validation_contrasts,
)
from experiments.run_centre_rate import (
    build_tasks,
    load_configuration,
    run_task,
)
from rfd.geometry import AIRM_GEOMETRY


def test_tuning_and_validation_workloads_are_small_and_seed_independent():
    tuning = load_configuration(CONFIG_DEFAULT, "bandwidth_tune")
    validation = load_configuration(CONFIG_DEFAULT, "bandwidth_validate")
    tuning_tasks = build_tasks(tuning)
    validation_tasks = build_tasks(validation)

    assert len(tuning_tasks) == 64
    assert len(tuning_tasks) * len(
        tuning["profile"]["bandwidth_multipliers"]
    ) == 320
    assert len(validation_tasks) == 128
    assert tuning["profile"]["seed_namespace"] != validation["profile"][
        "seed_namespace"
    ]
    assert not np.array_equal(
        tuning_tasks[0].seed_sequence.generate_state(8),
        validation_tasks[0].seed_sequence.generate_state(8),
    )


def test_selection_uses_mean_log_cell_medians_and_breaks_ties_downward():
    rows = []
    for n, scale in ((4096, 1.0), (8192, 0.7)):
        for replicate in range(3):
            for multiplier, relative in ((1.3, 1.2), (1.5, 1.0), (1.7, 1.0)):
                rows.append(
                    {
                        "n": n,
                        "replicate": replicate,
                        "bandwidth_multiplier": multiplier,
                        "path_rms": scale * relative * (1.0 + 0.01 * replicate),
                    }
                )
    scores = score_candidates(pd.DataFrame(rows), [1.3, 1.5, 1.7])

    assert scores.iloc[0]["bandwidth_multiplier"] == 1.5
    assert np.isclose(scores.iloc[0]["error_above_best_percent"], 0.0)
    assert scores.loc[
        scores["bandwidth_multiplier"] == 1.3,
        "error_above_best_percent",
    ].iloc[0] > 19.0


def test_validation_profile_pairs_baseline_with_the_frozen_winner():
    config = validation_configuration(CONFIG_DEFAULT, 1.9)

    assert config["profile"]["bandwidth_multipliers"] == [1.0, 1.9]
    assert config["profile"]["seed_namespace"] == 4202
    assert len(build_tasks(config)) * len(
        config["profile"]["bandwidth_multipliers"]
    ) == 256


def test_paired_validation_contrast_has_reader_facing_sign():
    rows = []
    for n in (4096, 8192):
        for replicate in range(5):
            baseline = 0.10 * (1.0 + 0.01 * replicate)
            winner = 0.08 * (1.0 + 0.01 * replicate)
            rows.extend(
                [
                    {
                        "n": n,
                        "replicate": replicate,
                        "bandwidth_multiplier": 1.0,
                        "path_rms": baseline,
                        "broad_path_rms": 0.11,
                    },
                    {
                        "n": n,
                        "replicate": replicate,
                        "bandwidth_multiplier": 1.9,
                        "path_rms": winner,
                        "broad_path_rms": 0.10,
                    },
                ]
            )
    contrasts = validation_contrasts(
        pd.DataFrame(rows),
        baseline=1.0,
        winner=1.9,
    )

    np.testing.assert_allclose(
        contrasts["paired_error_reduction_percent_median"],
        20.0,
    )
    np.testing.assert_allclose(
        contrasts["winner_richardson_reduction_percent_median"],
        18.4,
    )


def test_largest_candidate_runs_inside_the_fixed_overlap_boundary(
    tmp_path: Path,
):
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "bandwidth_tune"))
    config["profile"]["n_values"] = [4096]
    config["profile"]["replicates"] = 1
    tasks = build_tasks(config)

    rows = run_task(
        config,
        tasks[0],
        AIRM_GEOMETRY,
        [1.3, 2.1],
        tmp_path / "examples",
    )

    assert [row["status"] for row in rows] == ["ok", "ok"]
    assert all(row["nonconverged_stages"] == 0 for row in rows)
    assert all(row["fallback_count"] == 0 for row in rows)
