from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.run_bw_closure import (
    CONFIG_DEFAULT,
    BWTask,
    _base_and_directions,
    _model_config,
    build_tasks,
    generate_fit_sample,
    load_configuration,
    run,
    run_task,
)


def test_frozen_bw_workloads_have_every_declared_cell():
    smoke = load_configuration(CONFIG_DEFAULT, "smoke")
    closure = load_configuration(CONFIG_DEFAULT, "bw_closure")

    assert len(build_tasks(smoke)) == 9
    assert len(build_tasks(closure)) == 496
    keys = {
        (task.group, task.scenario, task.n, task.replicate)
        for task in build_tasks(closure)
    }
    assert len(keys) == 496


def test_rate_spine_and_frozen_bandwidth_match_the_canonical_design():
    config = load_configuration(CONFIG_DEFAULT, "bw_closure")
    rate_tasks = [task for task in build_tasks(config) if task.group == "rate"]

    assert {task.scenario for task in rate_tasks} == {"R-COMM", "R-CURVED"}
    assert {task.n for task in rate_tasks} == {512, 1024, 2048, 4096, 8192}
    task = next(task for task in rate_tasks if task.n == 512)
    model = _model_config(config, task)
    assert model.bandwidth == pytest.approx(0.5 * 1.3 * 512 ** (-1.0 / 7.0))
    assert model.n_cells == int(np.ceil(512 ** (2.0 / 7.0)))


def test_commuting_and_noncommuting_paths_are_structurally_distinct():
    commuting_base, commuting_first, _ = _base_and_directions(3, 1.6, "commuting")
    curved_base, curved_first, _ = _base_and_directions(3, 1.6, "curved")

    assert np.allclose(commuting_base @ commuting_first, commuting_first @ commuting_base)
    assert not np.allclose(curved_base @ curved_first, curved_first @ curved_base)


def test_commuting_generator_stays_diagonal():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    specification = deepcopy(config["regime_groups"]["rate"]["R-COMM"])
    task = BWTask("rate", "R-COMM", 16, 0, specification)
    sample, _, _, _ = generate_fit_sample(config, task)

    off_diagonal = sample.observations - np.eye(3) * np.diagonal(
        sample.observations, axis1=-2, axis2=-1
    )[:, None, :]
    assert np.max(np.abs(off_diagonal)) < 2e-9
    assert np.min(np.linalg.eigvalsh(sample.observations)) > 0.0


@pytest.mark.parametrize(
    "scenario",
    ["H-SIGNED", "H-NEAR", "H-RANKLOSS", "H-EXP", "H-DISPERSION"],
)
def test_each_isolated_hostile_probe_reaches_its_declared_outcome(scenario):
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    task = next(task for task in build_tasks(config) if task.scenario == scenario)
    row = run_task(config, task)

    assert row["status"] == "ok"
    assert row["boundary_verdict"] == "pass"


def test_signed_exit_activates_fallback_without_silent_clipping():
    config = load_configuration(CONFIG_DEFAULT, "smoke")
    task = next(task for task in build_tasks(config) if task.scenario == "H-SIGNED")
    row = run_task(config, task)

    assert bool(row["probe_fallback_activated"])
    assert row["fallback_count"] == 1
    assert "exp_failure" in row["fallback_reason"]
    assert row["generated_min_eigenvalue"] > 0.0


def test_parent_written_probe_output_is_resumable(tmp_path: Path):
    config = deepcopy(load_configuration(CONFIG_DEFAULT, "smoke"))
    config["profile"]["output_dir"] = str(tmp_path / "bw_probe")
    config["profile"]["workloads"] = {
        "hostile": {
            "regimes": ["H-NEAR"],
            "n_values": [128],
            "replicates": 1,
        }
    }

    run(config, workers=2)
    run(config, workers=2)
    raw = pd.read_csv(tmp_path / "bw_probe" / "raw.csv")

    assert len(raw) == 1
    assert raw["status"].iloc[0] == "ok"
    assert raw["boundary_verdict"].iloc[0] == "pass"
