from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.run_parent_rfd_bw_parity import (
    CONFIG_DEFAULT,
    METHODS,
    METHOD_METRICS,
    RAW_COLUMNS,
    _append_row,
    _read_raw,
    _summarize,
    build_tasks,
    load_configuration,
    validate_configuration,
)


def test_overnight_plan_is_paired_known_rank_and_includes_low_n():
    config = load_configuration(CONFIG_DEFAULT, "overnight")
    tasks = build_tasks(config)

    assert len(tasks) == 4 * 6 * 24
    assert {task.n for task in tasks} == {240, 512, 2048, 8192}
    assert {task.scenario for task in tasks} == {
        "P-HOME", "R-FIXED", "M-ALIGNED", "M-MIXED",
        "M-ORTHOGONAL", "M-CURVED",
    }
    assert {task.specification["rank"] for task in tasks} == {2}


def test_validation_rejects_a_selector_or_wrong_structural_rank():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    config["regimes"]["P-HOME"]["rank"] = 1

    with pytest.raises(ValueError, match="supplied true rank"):
        validate_configuration(config)


def test_append_rows_are_durable_and_machine_readable(tmp_path: Path):
    path = tmp_path / "raw.csv"
    first = {column: np.nan for column in RAW_COLUMNS}
    first.update({"scenario": "P-HOME", "n": 240, "replicate": 0, "status": "ok"})
    second = dict(first, scenario="M-CURVED", replicate=1)

    _append_row(path, first)
    _append_row(path, second)
    frame = _read_raw(path)

    assert list(frame["scenario"]) == ["P-HOME", "M-CURVED"]
    assert list(frame["replicate"]) == [0, 1]


def test_summary_reports_direct_multipliers_and_writes_plots(tmp_path: Path):
    rows = []
    for replicate, scale in enumerate((1.0, 1.2)):
        row = {column: np.nan for column in RAW_COLUMNS}
        row.update({
            "scenario": "P-HOME", "n": 240, "replicate": replicate,
            "status": "ok",
        })
        for method_index, method in enumerate(METHODS, start=1):
            for metric in METHOD_METRICS:
                row[f"{method}_{metric}"] = method_index * scale
        rows.append(row)

    _summarize(pd.DataFrame(rows), tmp_path)
    summary = pd.read_csv(tmp_path / "summary.csv")

    assert summary.loc[0, "rfd_over_parent_converged_signal_rms_median"] == pytest.approx(1 / 3)
    assert summary.loc[0, "rfd_win_rate_vs_parent_converged"] == 1.0
    assert (tmp_path / "report.md").is_file()
    assert (tmp_path / "signal_reconstruction.png").is_file()
    assert (tmp_path / "paired_signal_multiplier.png").is_file()
