from copy import deepcopy

import numpy as np
import pytest

from experiments.run_hf3_score_diagnostic import (
    CONFIG_DEFAULT,
    _loading_coordinates_at_reference,
    build_design,
    fit_blocked_var1,
    load_configuration,
    load_frozen_source,
    orthogonal_loading_alignment,
    validate_configuration,
)
from rfd.estimators.frame import PolygonalFrame
from rfd.estimators.lag import coordinate_tangents, tangent_coordinates
from rfd.geometry import BW_GEOMETRY


def test_hf3_design_loads_only_2024_and_inherits_frozen_hf2_ranks():
    config = load_configuration(CONFIG_DEFAULT)
    _, panel, _ = load_frozen_source(config)
    design = build_design(config, panel, smoke=False)

    assert design["development_years_loaded"] == [2024]
    assert design["sealed_evaluation_year"] == 2025
    assert design["sealed_year_loaded"] is False
    assert design["frozen_ranks"] == {"parent_rfm": 19, "rfd_piecewise6": 19}
    assert design["selects_or_tunes_any_choice"] is False
    assert design["kalman_status"] == "inherited_non_promoted_sensitivity"


def test_loading_alignment_removes_rotation_without_changing_subspace():
    anchor = np.asarray([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    source = np.asarray([[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]])
    rotation, diagnostics = orthogonal_loading_alignment(anchor, source)

    np.testing.assert_allclose(rotation @ source, anchor, atol=1e-12)
    assert diagnostics["minimum_canonical_correlation"] == pytest.approx(1.0)
    assert diagnostics["largest_principal_angle_degrees"] == pytest.approx(0.0)


def test_cached_identity_loadings_transport_back_to_the_fold_reference():
    config = load_configuration(CONFIG_DEFAULT)
    _, _, source = load_frozen_source(config)
    with np.load(source / "tuning" / "fold_0.npz", allow_pickle=False) as cache:
        frame = PolygonalFrame(
            cache["parent_rfm_vertex_times"],
            cache["parent_rfm_vertices"],
            BW_GEOMETRY,
        )
        identity_loadings = cache["parent_rfm_identity_loadings"][:3]
    reference_coordinates = _loading_coordinates_at_reference(identity_loadings, frame)
    reference_vectors = coordinate_tangents(
        reference_coordinates, BW_GEOMETRY.tangent_basis(frame.reference_point)
    )
    identity = np.eye(frame.reference_point.shape[0])
    returned = tangent_coordinates(
        BW_GEOMETRY.transport(reference_vectors, frame.reference_point, identity),
        identity,
        BW_GEOMETRY.tangent_basis(identity),
        BW_GEOMETRY,
    )

    np.testing.assert_allclose(returned, identity_loadings, rtol=2e-6, atol=2e-7)


def test_blocked_var_ignores_enormous_cross_week_seam():
    transition = 0.8
    first = np.asarray([1.0, 0.8, 0.64, 0.512, 0.4096])
    second = 1000.0 * first
    scores = np.concatenate((first, second))[:, None]
    blocks = np.asarray([0] * first.size + [1] * second.size)

    fit = fit_blocked_var1(scores, blocks)

    assert fit["transition_count"] == 8
    assert fit["coefficients"][1, 0] == pytest.approx(transition, abs=1e-10)
    assert fit["var_r2"] == pytest.approx(1.0)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda c: c["experiment"].update(development_year=2025), "2024"),
        (lambda c: c["source"]["frozen_ranks"].update(parent_rfm=18), "rank 19"),
        (lambda c: c["source"].update(max_lag=5), "six lags"),
        (lambda c: c["head_policy"].update(primary="ridge"), "VAR"),
        (lambda c: c["head_policy"].update(kalman="retune"), "Kalman"),
    ],
)
def test_hf3_rejects_protocol_drift(mutation, message):
    config = deepcopy(load_configuration(CONFIG_DEFAULT))
    mutation(config)
    with pytest.raises(ValueError, match=message):
        validate_configuration(config)
