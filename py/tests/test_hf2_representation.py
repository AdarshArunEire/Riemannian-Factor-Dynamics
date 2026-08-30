from copy import deepcopy

import numpy as np
import pandas as pd
import pytest

from experiments.run_hf2_representation import (
    CONFIG_DEFAULT,
    blocked_fold_masks,
    build_design,
    indexed_lag_cross_covariances,
    load_configuration,
    load_panel,
    phase_data,
    select_arm_rank,
    validate_configuration,
)


def test_hf2_design_separates_rank_tuning_from_representation_evaluation():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_panel(config)
    tuning = phase_data(panel, config, "tuning", smoke=False)
    evaluation = phase_data(panel, config, "evaluation", smoke=False)
    design = build_design(config, panel, smoke=False)

    assert tuning["covariances"].shape == (26 * 168, 20, 20)
    assert evaluation["covariances"].shape == (26 * 168, 20, 20)
    assert tuning["hours"][-1] < evaluation["hours"][0]
    assert design["rank_policy"] == "independent arm-specific validation rank, then frozen"
    assert design["matched_rank_diagnostic"] is True
    assert design["forecast_head"] is None
    assert design["sealed_evaluation_year"] == 2025


def test_hf2_weekly_folds_hold_out_every_hour_and_embargo_training_edges():
    n = 8 * 168
    train0, heldout0, blocks0 = blocked_fold_masks(
        n, block_hours=168, validation_parity=0, embargo_hours=24
    )
    train1, heldout1, blocks1 = blocked_fold_masks(
        n, block_hours=168, validation_parity=1, embargo_hours=24
    )

    assert np.array_equal(blocks0, blocks1)
    assert np.array_equal(heldout0, ~heldout1)
    assert train0.sum() == train1.sum() == 4 * 120
    within = np.arange(n) % 168
    assert np.all((within[train0] >= 24) & (within[train0] < 144))


def test_indexed_lag_products_do_not_join_disconnected_blocks():
    rows = np.asarray([[1.0], [2.0], [100.0], [200.0]])
    indices = np.asarray([0, 1, 10, 11])
    result = indexed_lag_cross_covariances(
        rows, indices, max_lag=1, demean=False
    )

    # Only (1, 0) and (11, 10) are real lag-one pairs.  Concatenation would
    # incorrectly add the enormous cross-gap pair (10, 1).
    assert result.pair_counts.tolist() == [2]
    assert result.divisors.tolist() == [4]
    np.testing.assert_allclose(result.covariances[0, 0, 0], (2.0 + 20000.0) / 4.0)


def _rank_scores(method: str, losses_by_rank: dict[int, float]) -> pd.DataFrame:
    rows = []
    for fold in range(2):
        for block in range(4):
            for rank, loss in losses_by_rank.items():
                rows.append({
                    "phase": "tuning",
                    "fold": fold,
                    "block": block,
                    "method": method,
                    "rank": rank,
                    "frobenius2": loss,
                    "qlike": loss,
                    "bw2": loss,
                })
    return pd.DataFrame(rows)


def test_arm_specific_rank_selection_can_choose_different_ranks():
    candidates = [1, 2, 3]
    parent = _rank_scores("parent_rfm", {0: 10.0, 1: 8.0, 2: 7.0, 3: 7.5})
    rfd = _rank_scores("rfd_piecewise6", {0: 10.0, 1: 9.0, 2: 8.0, 3: 6.0})
    scores = pd.concat([parent, rfd], ignore_index=True)

    parent_rank, _ = select_arm_rank(scores, "parent_rfm", candidates)
    rfd_rank, _ = select_arm_rank(scores, "rfd_piecewise6", candidates)

    assert parent_rank == 2
    assert rfd_rank == 3


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda c: c["experiment"].update(rank_tuning_weeks=20), "26-week"),
        (lambda c: c["representation"].update(piecewise_segments=12), "piecewise-6"),
        (lambda c: c["representation"].update(max_lag=200), "max_lag"),
        (lambda c: c["rank_selection"].update(candidates=[1, 2]), "1 through 21"),
    ],
)
def test_hf2_rejects_protocol_drift(mutation, message):
    config = deepcopy(load_configuration(CONFIG_DEFAULT))
    mutation(config)
    with pytest.raises(ValueError, match=message):
        validate_configuration(config)
