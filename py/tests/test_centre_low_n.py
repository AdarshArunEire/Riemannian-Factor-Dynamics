from copy import deepcopy

import numpy as np
import pytest

from experiments.run_centre_tournament import (
    CONFIG_DEFAULT,
    build_design,
    load_configuration,
    validate_configuration,
)
from rfd.estimators.centre_low_n import (
    anchored_tangent_trend,
    graph_smoothed_polygon,
    piecewise_frechet_path,
    segmented_frechet_polygon,
)
from rfd.geometry import BW_GEOMETRY


def _diagonal(values):
    return np.stack([np.diag(value) for value in values])


def test_frozen_n240_tournament_design():
    config = load_configuration(CONFIG_DEFAULT)
    design = build_design(config)

    assert design["sample_size"] == 240
    assert design["matrix_size"] == 12
    assert design["holdout_folds"] == 20
    assert design["graph_strengths"] == [0.25, 1.0, 4.0]
    assert design["piecewise_segments"] == [2, 3, 4, 6]


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda c: c["tournament"].update(holdout_block_months=13), "holdout"),
        (lambda c: c["tournament"].update(shrinkage_lambdas=[0.1, 1.0]), "lambdas"),
        (lambda c: c["tournament"].update(graph_strengths=[0.0]), "strength"),
        (lambda c: c["tournament"].update(piecewise_segments=[1]), "segment"),
    ],
)
def test_tournament_configuration_rejects_invalid_design(mutation, message):
    config = deepcopy(load_configuration(CONFIG_DEFAULT))
    mutation(config)
    with pytest.raises(ValueError, match=message):
        validate_configuration(config)


def test_anchored_tangent_trend_preserves_a_constant_path():
    point = np.diag([2.0, 5.0])
    observations = np.broadcast_to(point, (8, 2, 2)).copy()
    result = anchored_tangent_trend(
        observations,
        np.linspace(0.1, 0.8, 8),
        np.array([0.05, 0.5, 0.95]),
        point,
        BW_GEOMETRY,
    )

    assert np.allclose(result.points, point, rtol=1e-11, atol=1e-11)
    assert result.diagnostics["clipped_targets"] == 0


def test_piecewise_frechet_path_uses_only_its_segment():
    observations = _diagonal([
        [1.0, 4.0], [1.0, 4.0], [9.0, 16.0], [9.0, 16.0]
    ])
    result = piecewise_frechet_path(
        observations,
        np.array([0.1, 0.2, 0.8, 0.9]),
        np.array([0.15, 0.85]),
        2,
        BW_GEOMETRY,
    )

    assert np.allclose(result.points[0], observations[0], atol=1e-10)
    assert np.allclose(result.points[1], observations[-1], atol=1e-10)
    assert result.diagnostics["minimum_segment_count"] == 2


def test_segmented_frechet_polygon_is_continuous_and_returns_its_frame():
    observations = _diagonal([
        [1.0, 4.0], [1.0, 4.0], [9.0, 16.0], [9.0, 16.0]
    ])
    targets = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
    result = segmented_frechet_polygon(
        observations,
        np.array([0.1, 0.2, 0.8, 0.9]),
        targets,
        2,
        BW_GEOMETRY,
    )

    assert result.frame.vertices.shape[0] == 4
    assert np.allclose(result.points[0], observations[0], atol=1e-10)
    assert np.allclose(result.points[-1], observations[-1], atol=1e-10)
    assert np.all(np.linalg.eigvalsh(result.points) > 0.0)


def test_graph_smoothing_preserves_constant_positive_vertices():
    point = np.diag([2.0, 3.0])
    vertices = np.broadcast_to(point, (4, 2, 2)).copy()
    result = graph_smoothed_polygon(
        np.linspace(0.0, 1.0, 4),
        vertices,
        np.linspace(0.0, 1.0, 9),
        1.0,
        BW_GEOMETRY,
    )

    assert np.allclose(result.points, point, rtol=1e-10, atol=1e-10)
    assert np.all(np.linalg.eigvalsh(result.points) > 0.0)
