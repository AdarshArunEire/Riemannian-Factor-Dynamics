from pathlib import Path

import numpy as np
import pandas as pd

from experiments.run_b45_comparators import (
    RAW_COLUMNS,
    _projector_from_rows,
    _summarize,
    run_task,
)
from experiments.run_end_to_end import CONFIG_DEFAULT, build_tasks, load_configuration


def test_projector_uses_the_row_span_and_is_basis_invariant():
    rows = np.array([[1.0, 0.0, 1.0], [0.0, 2.0, 0.0]])
    transformed = np.array([[2.0, -1.0], [1.0, 3.0]]) @ rows

    first = _projector_from_rows(rows)
    second = _projector_from_rows(transformed)

    assert np.allclose(first, first.T)
    assert np.allclose(first @ first, first)
    assert np.allclose(first, second)


def test_comparator_smoke_replays_one_complete_dgp_draw():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    row = run_task(config, build_tasks(config)[0])

    assert row["status"] == "ok"
    assert row["true_rank"] == 2
    assert row["tangent_dimension"] == 3
    assert row["global_mean_converged"]
    for metric in (
        "known_centre_loading_error",
        "fixed_centre_loading_error",
        "known_centre_factor_nrmse",
        "fixed_centre_factor_nrmse",
        "known_centre_observation_reconstruction_rms",
        "fixed_centre_observation_reconstruction_rms",
        "global_mean_centre_path_rms",
    ):
        assert np.isfinite(row[metric])
        assert row[metric] >= 0.0
    assert row["known_centre_loading_error"] <= 1.0 + 1e-12
    assert row["fixed_centre_loading_error"] <= 1.0 + 1e-12


def test_comparator_summary_writes_machine_and_human_outputs(tmp_path: Path):
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "status": "ok", "n": 128, "matrix_size": 2,
        "known_centre_loading_error": 0.1,
        "fixed_centre_loading_error": 0.2,
        "known_centre_factor_nrmse": 0.3,
        "fixed_centre_factor_nrmse": 0.4,
        "global_mean_converged": True,
    })
    _summarize(pd.DataFrame([row]), tmp_path)

    summary = pd.read_csv(tmp_path / "summary.csv")
    assert summary["known_centre_loading_error_median"].iloc[0] == 0.1
    assert summary["fixed_centre_loading_error_median"].iloc[0] == 0.2
    assert (tmp_path / "report.md").is_file()
