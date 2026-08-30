from copy import deepcopy

import numpy as np
import pandas as pd
import pytest

from experiments.run_hf1_centre_gate import (
    CONFIG_DEFAULT,
    blocked_fold_masks,
    build_design,
    load_configuration,
    load_development_panel,
    paired_method_table,
    permute_complete_blocks,
    select_centre_method,
    validate_configuration,
)


def test_hf1_frozen_design_and_sealed_year_boundary():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_development_panel(config)
    design = build_design(config, panel, smoke=False)

    assert panel["covariances"].shape == (52 * 168, 20, 20)
    assert str(panel["hours"][0]) == "2024-01-01T00:00:00.000000000"
    assert str(panel["hours"][-1]) == "2024-12-29T23:00:00.000000000"
    assert design["unused_2024_remainder_hours_recorded_profile"] == 48
    assert design["sealed_evaluation_year"] == 2025
    assert design["negative_control"] == "richardson"


def test_blocked_folds_are_complementary_and_embargo_training_edges():
    n = 8 * 168
    train0, valid0, block0 = blocked_fold_masks(
        n, block_hours=168, validation_parity=0, embargo_hours=24
    )
    train1, valid1, block1 = blocked_fold_masks(
        n, block_hours=168, validation_parity=1, embargo_hours=24
    )

    assert np.array_equal(block0, block1)
    assert np.array_equal(valid0, ~valid1)
    assert not np.any(train0 & valid0)
    assert not np.any(train1 & valid1)
    within = np.arange(n) % 168
    assert np.all((within[train0] >= 24) & (within[train0] < 144))
    assert train0.sum() == train1.sum() == 4 * 120


def test_complete_week_permutation_preserves_every_hour_inside_each_week():
    observations = np.arange(6 * 4).reshape(24, 1, 1)
    shuffled, order = permute_complete_blocks(
        observations, block_hours=4, rng=np.random.default_rng(12)
    )

    assert sorted(order.tolist()) == [0, 1, 2, 3, 4, 5]
    for new, old in enumerate(order):
        np.testing.assert_array_equal(
            shuffled[new * 4:(new + 1) * 4],
            observations[old * 4:(old + 1) * 4],
        )


def _fake_scores(
    piecewise6_gain: float,
    piecewise12_gain: float,
    *,
    broad_gain: float = 0.5,
) -> pd.DataFrame:
    gains = {
        "global": 0.0,
        "broad_positive": broad_gain,
        "piecewise6": piecewise6_gain,
        "piecewise12": piecewise12_gain,
        "richardson": -2.0,
    }
    rows = []
    for block in range(12):
        wobble = (block % 3 - 1) * 0.05
        for method, gain in gains.items():
            rows.append({
                "block": block,
                "method": method,
                "frobenius2": 10.0 - gain + wobble,
                "qlike": 8.0 - gain + wobble,
                "bw2": 4.0 - 0.2 * gain + wobble,
            })
    return pd.DataFrame(rows)


def test_selection_prefers_piecewise6_when_both_losses_show_clear_tied_gain():
    config = load_configuration(CONFIG_DEFAULT)
    summary = paired_method_table(_fake_scores(2.0, 2.01))
    result = select_centre_method(summary, config)

    assert result["selected_method"] == "piecewise6"
    assert {"piecewise6", "piecewise12"}.issubset(result["eligible_positive_methods"])


def test_selection_returns_global_when_one_primary_loss_does_not_clear_one_se():
    config = load_configuration(CONFIG_DEFAULT)
    scores = _fake_scores(0.0, 0.0, broad_gain=0.0)
    summary = paired_method_table(scores)
    result = select_centre_method(summary, config)

    assert result["selected_method"] == "global"


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda c: c["crossfit"].update(folds=3), "two complementary"),
        (lambda c: c["candidates"].update(negative_control="global"), "Richardson"),
        (lambda c: c["selection"].update(primary_losses=["bw2"]), "primary losses"),
        (lambda c: c["dependent_null"].update(replicates=10), "at least 19"),
    ],
)
def test_hf1_rejects_design_drift(mutation, message):
    config = deepcopy(load_configuration(CONFIG_DEFAULT))
    mutation(config)
    with pytest.raises(ValueError, match=message):
        validate_configuration(config)
