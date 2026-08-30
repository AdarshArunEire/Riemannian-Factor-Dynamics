from copy import deepcopy

import numpy as np
import pandas as pd
import pytest

from experiments.analyze_appfin_centre_diagnostic import (
    _geodesic_shrink,
    _selected_evaluations,
    _verdict,
)
from experiments.run_appfin_centre_diagnostic import (
    CONFIG_DEFAULT,
    _circular_block_indices,
    build_design,
    load_configuration,
    validate_configuration,
)
from experiments.run_appfin_identification import load_panel
from rfd.geometry import BW_GEOMETRY


def test_frozen_centre_diagnostic_design_is_exact():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_panel(config)
    design = build_design(config, panel)

    assert panel["panel"].shape == (240, 12, 12)
    assert design["holdout_block_months"] == 12
    assert design["holdout_folds"] == 20
    assert design["tangent_dimension"] == 78
    assert design["shrinkage_lambdas"] == pytest.approx(
        np.linspace(0.0, 1.0, 11)
    )
    assert design["constant_centre_null"]["replicates"] == 99


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda c: c["diagnostic"].update(holdout_block_months=13), "holdout"),
        (
            lambda c: c["diagnostic"].update(
                shrinkage_lambdas=[0.1, 0.5, 1.0]
            ),
            "lambdas",
        ),
        (lambda c: c["diagnostic"].update(bootstrap_replicates=18), "replicates"),
        (lambda c: c["diagnostic"].update(workers=9), "workers"),
    ],
)
def test_configuration_rejects_unpredeclared_designs(mutation, message):
    config = deepcopy(load_configuration(CONFIG_DEFAULT))
    mutation(config)

    with pytest.raises(ValueError, match=message):
        validate_configuration(config)


def test_circular_block_bootstrap_preserves_contiguous_twelve_month_runs():
    indices = _circular_block_indices(
        np.random.default_rng(410), n=240, block=12
    )

    assert indices.shape == (240,)
    assert np.all((0 <= indices) & (indices < 240))
    blocks = indices.reshape(-1, 12)
    expected_steps = np.ones((blocks.shape[0], 11), dtype=int)
    assert np.array_equal(np.diff(blocks, axis=1) % 240, expected_steps)


def test_bw_geodesic_shrink_has_exact_endpoints_and_valid_midpoint():
    global_centre = np.diag([1.0, 4.0])
    local = np.stack([np.diag([4.0, 1.0]), np.diag([9.0, 16.0])])

    at_global = _geodesic_shrink(global_centre, local, 0.0)
    midpoint = _geodesic_shrink(global_centre, local, 0.5)
    at_local = _geodesic_shrink(global_centre, local, 1.0)

    assert np.array_equal(at_global, np.broadcast_to(global_centre, local.shape))
    assert np.array_equal(at_local, local)
    assert np.isfinite(midpoint).all()
    assert np.all(np.linalg.eigvalsh(midpoint) > 0.0)
    assert BW_GEOMETRY.dist2(global_centre, midpoint) == pytest.approx(
        0.25 * BW_GEOMETRY.dist2(global_centre, local)
    )


def _fake_scores() -> pd.DataFrame:
    rows = []
    for fold in range(4):
        parity = fold % 2
        for month in range(2):
            common = {
                "fold": fold,
                "fold_parity": parity,
                "month_index": 2 * fold + month,
                "month": f"200{fold}-{month + 1:02d}",
                "qlike": 1.0,
                "relative_frobenius2": 1.0,
                "displacement_from_fold_global2": 0.0,
                "crossfit_to_full_path2": 0.0,
            }
            rows.append({
                **common, "method": "global", "family": "global",
                "kind": "base", "lambda": 0.0, "bw2": 10.0,
            })
            rows.append({
                **common, "method": "positive_local", "family": "positive",
                "kind": "base", "lambda": 1.0, "bw2": 9.0,
            })
            rows.append({
                **common, "method": "richardson", "family": "richardson",
                "kind": "base", "lambda": 1.0, "bw2": 12.0,
            })
            for family in ("positive", "richardson"):
                for coefficient in (0.0, 0.5, 1.0):
                    if parity == 0:
                        target = 0.5 if family == "positive" else 0.0
                    else:
                        target = 1.0 if family == "positive" else 0.5
                    rows.append({
                        **common,
                        "method": f"{family}_shrink_{coefficient:.1f}",
                        "family": family,
                        "kind": "shrink",
                        "lambda": coefficient,
                        "bw2": 8.0 + 4.0 * abs(coefficient - target),
                    })
    return pd.DataFrame(rows)


def test_alternating_split_tunes_on_one_parity_and_evaluates_the_other():
    evaluations, selections = _selected_evaluations(_fake_scores())

    assert selections["A"] == {"positive": 0.5, "richardson": 0.0}
    assert selections["B"] == {"positive": 1.0, "richardson": 0.5}
    assert set(evaluations.loc[evaluations["assignment"].eq("A"), "evaluation_fold_parity"]) == {1}
    assert set(evaluations.loc[evaluations["assignment"].eq("B"), "evaluation_fold_parity"]) == {0}


def test_verdict_treats_unshrunk_and_selected_positive_paths_as_one_family():
    evaluations = pd.DataFrame([
        {"assignment": "A", "method": "positive_local", "lambda": 1.0,
         "mean_bw2": 8.0, "bw_error_reduction_percent_vs_global": 20.0},
        {"assignment": "A", "method": "global", "lambda": 0.0,
         "mean_bw2": 10.0, "bw_error_reduction_percent_vs_global": 0.0},
        {"assignment": "B", "method": "selected_positive_shrink", "lambda": 0.5,
         "mean_bw2": 9.0, "bw_error_reduction_percent_vs_global": 10.0},
        {"assignment": "B", "method": "global", "lambda": 0.0,
         "mean_bw2": 10.0, "bw_error_reduction_percent_vs_global": 0.0},
    ])

    verdict = _verdict(evaluations, {"constant_centre_p_value": 0.01})

    assert "partially shrunk moving centre" in verdict
    assert "calendar-sensitive" not in verdict
