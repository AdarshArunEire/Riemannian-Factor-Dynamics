from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd

from experiments.run_score_filter_bw import (
    CONFIG_DEFAULT,
    MATRIX_METRICS,
    REPRESENTATIONS,
    build_tasks,
    load_configuration,
    run,
    run_task,
)


def test_recorded_score_filter_grid_covers_full_sample_range():
    config = load_configuration(CONFIG_DEFAULT, "overnight")

    tasks = build_tasks(config)

    assert len(tasks) == 4 * 6 * 16 == 384
    assert sorted({task.n for task in tasks}) == [240, 512, 2048, 8192]
    assert {task.scenario for task in tasks} == {
        "R-FIXED", "M-ALIGNED", "M-ORTHOGONAL", "M-CURVED",
        "M-CURVED-NOISELESS", "M-CURVED-NOISY",
    }


def test_one_bw_score_filter_task_returns_all_heads_and_safe_forecasts():
    config = load_configuration(CONFIG_DEFAULT, "smoke")

    row = run_task(config, build_tasks(config)[0])

    assert row["status"] == "ok", row["error_message"]
    assert row["n_train"] == 128
    assert row["n_test"] == 32
    for representation in REPRESENTATIONS:
        assert np.isfinite(row[f"{representation}_var_forecast_nrmse"])
        assert np.isfinite(row[f"{representation}_kf_forecast_nrmse"])
        assert 0.0 <= row[f"{representation}_kf_measurement_fraction"] <= 1.0
        assert row[f"{representation}_kf_radius"] < 1.0
        for head in ("var", "kf"):
            for metric in MATRIX_METRICS:
                assert np.isfinite(row[f"{representation}_{head}_{metric}"])
            assert row[f"{representation}_{head}_forecast_min_eigenvalue"] > 0.0
            assert 0.0 < row[f"{representation}_{head}_clip_min_factor"] <= 1.0


def test_score_filter_runner_is_append_only_and_resumable(tmp_path: Path):
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["profile"]["n_values"] = [160]
    config["profile"]["replicates"] = 1
    config["profile"]["scenarios"] = ["R-FIXED"]
    config["profile"]["output_dir"] = str(tmp_path / "score-filter")

    run(config, workers=1)
    run(config, workers=1)
    raw = pd.read_csv(tmp_path / "score-filter" / "raw.csv")

    assert len(raw) == 1
    assert raw.loc[0, "status"] == "ok"
    assert (tmp_path / "score-filter" / "summary.csv").is_file()
    assert (tmp_path / "score-filter" / "amplitude_forecast.png").is_file()
