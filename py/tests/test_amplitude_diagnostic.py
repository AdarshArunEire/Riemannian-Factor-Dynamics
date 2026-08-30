from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.analyze_amplitude_diagnostic import paired_attribution, validate_raw
from experiments.run_amplitude_diagnostic import (
    CONFIG_DEFAULT,
    aligned_score_metrics,
    build_tasks,
    load_configuration,
    run,
    run_task,
)
from experiments.run_paper1_controls import ControlTask, generate_control_sample
from rfd.estimators.lag import tangent_coordinates
from rfd.geometry import AIRM_GEOMETRY


def test_frozen_diagnostic_workload_is_exact():
    config = load_configuration(CONFIG_DEFAULT, "diagnostic")

    tasks = build_tasks(config)

    assert len(tasks) == 3 * 64 == 192
    assert sorted({task.n for task in tasks}) == [240, 512, 2048]
    assert {task.regime for task in tasks} == {"B0"}


def test_scalar_calibration_detects_pure_attenuation():
    target = np.arange(1.0, 13.0).reshape(6, 2)

    metrics = aligned_score_metrics(0.5 * target, target)

    assert metrics["nrmse"] == pytest.approx(0.5)
    assert metrics["calibrated_nrmse"] == pytest.approx(0.0, abs=1e-12)
    assert metrics["norm_ratio"] == pytest.approx(0.5)
    assert metrics["cosine"] == pytest.approx(1.0)
    assert metrics["scale"] == pytest.approx(2.0)


def test_oracle_true_score_is_exact_without_observation_noise():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    specification = dict(config["core_regimes"]["C2"])
    task = ControlTask(64, 0, "C2", specification)
    sample, base, _ = generate_control_sample(config, task, AIRM_GEOMETRY)
    basis = AIRM_GEOMETRY.tangent_basis(base)
    local = AIRM_GEOMETRY.log(sample.centres, sample.observations)
    reference = AIRM_GEOMETRY.transport(local, sample.centres, base)
    rows = tangent_coordinates(reference, base, basis, AIRM_GEOMETRY)
    loading_rows = tangent_coordinates(
        sample.loadings, base, basis, AIRM_GEOMETRY
    )
    centred_scores = rows @ loading_rows.T
    centred_scores -= centred_scores.mean(axis=0)
    target = sample.factors - sample.factors.mean(axis=0)

    assert aligned_score_metrics(centred_scores, target)["nrmse"] < 1e-9


def test_smoke_task_returns_all_crossed_variants():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    task = build_tasks(config)[0]

    row = run_task(config, task)

    assert row["status"] == "ok"
    for variant in ("ot", "oo", "ft", "of", "ff"):
        assert np.isfinite(row[f"{variant}_nrmse"])
        assert np.isfinite(row[f"{variant}_calibrated_nrmse"])
        assert 0.0 <= row[f"{variant}_cosine"] <= 1.0 + 1e-12


def test_parallel_runner_is_append_only_and_resume_safe(tmp_path: Path):
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["profile"]["n_values"] = [64]
    config["profile"]["replicates"] = 2
    config["profile"]["output_dir"] = str(tmp_path / "parallel")

    run(config, workers=2)
    run(config, workers=2)
    raw = pd.read_csv(tmp_path / "parallel" / "raw.csv")

    assert len(raw) == 2
    assert (raw["status"] == "ok").all()
    validate_raw(raw, config, allow_incomplete=False)


def test_paired_attribution_uses_the_declared_two_by_two_contrast():
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["analysis"]["bootstrap_replicates"] = 100
    raw = pd.DataFrame({
        "n": [128, 128],
        "ot_nrmse": [0.2, 0.2],
        "oo_nrmse": [0.3, 0.3],
        "ft_nrmse": [0.5, 0.5],
        "of_nrmse": [0.4, 0.4],
        "ff_nrmse": [0.9, 0.9],
        "ff_calibrated_nrmse": [0.6, 0.6],
    })

    table = paired_attribution(raw, config).set_index("contrast")

    assert table.loc["row cost at true directions", "median"] == pytest.approx(0.3)
    assert table.loc["RFD-direction cost on oracle rows", "median"] == pytest.approx(0.2)
    assert table.loc["row-direction interaction", "median"] == pytest.approx(0.2)
    assert table.loc["RFD scalar-calibration gain", "median"] == pytest.approx(0.3)
