from pathlib import Path

import numpy as np
import pandas as pd

from experiments.run_bandwidth_boundary import (
    CONFIG_DEFAULT,
    PROFILE_NAMES,
    admissible_multiplier_ceiling,
    summarise,
)
from experiments.run_centre_rate import build_tasks, load_configuration


def test_boundary_profiles_are_small_independent_and_admissible():
    configs = [
        load_configuration(CONFIG_DEFAULT, profile) for profile in PROFILE_NAMES
    ]

    assert [config["profile"]["seed_namespace"] for config in configs] == [
        4204,
        4205,
    ]
    assert all(len(build_tasks(config)) == 32 for config in configs)
    assert all(
        len(build_tasks(config))
        * len(config["profile"]["bandwidth_multipliers"])
        == 96
        for config in configs
    )
    for config in configs:
        n = int(config["profile"]["n_values"][0])
        assert max(config["profile"]["bandwidth_multipliers"]) < (
            admissible_multiplier_ceiling(config, n)
        )


def test_requested_large_multipliers_are_invalid_at_4096_but_valid_at_8192():
    small = load_configuration(CONFIG_DEFAULT, "boundary_4096")
    large = load_configuration(CONFIG_DEFAULT, "boundary_8192")

    assert admissible_multiplier_ceiling(small, 4096) < 2.2
    assert admissible_multiplier_ceiling(large, 8192) > 2.4


def test_boundary_summary_keeps_source_and_interquartile_uncertainty():
    raw = pd.DataFrame(
        {
            "n": [8192] * 4,
            "bandwidth_multiplier": [2.2] * 4,
            "path_rms": [0.04, 0.02, 0.03, 0.05],
        }
    )

    result = summarise(raw, "new batch")

    assert result.loc[0, "source"] == "new batch"
    assert result.loc[0, "replicates"] == 4
    assert np.isclose(result.loc[0, "median"], 0.035)
    assert result.loc[0, "q25"] < result.loc[0, "median"] < result.loc[0, "q75"]
