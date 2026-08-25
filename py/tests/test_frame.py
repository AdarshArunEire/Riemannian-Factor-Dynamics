"""B4.3 -- polygonal paths and derivative-free transported frames."""

import numpy as np
import pytest

from rfd.estimators.frame import (
    PolygonalFrame,
    evaluate_polygon,
    polygon_cell_count,
    propagate_vertex_frame,
    regular_polygon_grid,
    transport_from_reference,
    transport_to_reference,
)
from rfd.geometry import AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY


def test_cell_count_implements_the_declared_two_thirds_rule():
    assert polygon_cell_count(1.0 / 8.0) == 4
    assert polygon_cell_count(1.0, constant=2.1) == 3
    assert polygon_cell_count(2.0, minimum=5) == 5


def test_regular_grid_has_exactly_one_more_vertex_than_cells():
    grid = regular_polygon_grid(4, start=0.2, stop=0.8)
    np.testing.assert_allclose(grid, [0.2, 0.35, 0.5, 0.65, 0.8])


def test_polygon_hits_vertices_exactly_and_uses_geodesic_midpoints():
    vertices = np.array(
        [
            np.diag([1.0, 1.0]),
            np.diag([4.0, 1.0]),
            np.diag([4.0, 9.0]),
        ]
    )
    frame = PolygonalFrame(np.array([0.0, 0.5, 1.0]), vertices, AIRM_GEOMETRY)
    result = evaluate_polygon(frame, np.array([0.0, 0.25, 0.5, 1.0]))

    np.testing.assert_array_equal(result.cell_indices, [0, 0, 1, 1])
    np.testing.assert_allclose(result.fractions, [0.0, 0.5, 0.0, 1.0])
    np.testing.assert_allclose(result.points[0], vertices[0])
    np.testing.assert_allclose(result.points[1], np.diag([2.0, 1.0]))
    np.testing.assert_allclose(result.points[2], vertices[1])
    np.testing.assert_allclose(result.points[3], vertices[2])


@pytest.mark.parametrize(
    ("geometry", "point", "vector"),
    (
        (
            AIRM_GEOMETRY,
            np.diag([1.0, 2.0]),
            np.array([[0.3, 0.1], [0.1, -0.2]]),
        ),
        (
            BW_GEOMETRY,
            np.diag([1.0, 2.0]),
            np.array([[0.3, 0.1], [0.1, -0.2]]),
        ),
        (
            SPHERE_GEOMETRY,
            np.array([1.0, 0.0, 0.0]),
            np.array([0.0, 0.6, -0.8]),
        ),
    ),
    ids=("airm", "bw", "sphere"),
)
def test_constant_centre_makes_polygonal_transport_the_identity(
    geometry,
    point,
    vector,
):
    vertices = np.broadcast_to(point, (4,) + point.shape).copy()
    frame = PolygonalFrame(np.linspace(0.0, 1.0, 4), vertices, geometry)
    propagated = propagate_vertex_frame(frame, vector)

    np.testing.assert_allclose(
        propagated,
        np.broadcast_to(vector, propagated.shape),
        rtol=2e-10,
        atol=2e-11,
    )


def test_commuting_airm_flat_has_zero_closed_loop_holonomy():
    log_diagonals = np.array(
        [
            [0.0, 0.0],
            [0.2, 0.0],
            [0.2, 0.3],
            [0.0, 0.3],
            [0.0, 0.0],
        ]
    )
    vertices = np.array([np.diag(np.exp(value)) for value in log_diagonals])
    frame = PolygonalFrame(np.linspace(0.0, 1.0, 5), vertices, AIRM_GEOMETRY)
    initial = np.array([[1.0, 0.0], [0.0, 0.0]])
    propagated = propagate_vertex_frame(frame, initial)

    np.testing.assert_allclose(propagated[-1], initial, atol=8e-15)


def test_unit_sphere_triangle_holonomy_matches_curvature_times_area():
    # Three right-angle geodesic edges enclose area pi/2. Unit-sphere
    # curvature is one, so Gauss--Bonnet predicts a pi/2 frame rotation.
    vertices = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    frame = PolygonalFrame(np.linspace(0.0, 1.0, 4), vertices, SPHERE_GEOMETRY)
    initial = np.array([1.0, 0.0, 0.0])
    final = propagate_vertex_frame(frame, initial)[-1]
    rotation = np.arccos(np.clip(np.dot(initial, final), -1.0, 1.0))

    np.testing.assert_allclose(rotation, np.pi / 2.0, atol=2e-15)
    np.testing.assert_allclose(
        np.linalg.norm(final - initial),
        2.0 * np.sin(rotation / 2.0),
        atol=2e-15,
    )


@pytest.mark.parametrize(
    ("geometry", "vertices", "reference_vectors"),
    (
        (
            AIRM_GEOMETRY,
            np.array(
                [
                    np.diag([1.0, 2.0]),
                    np.diag([1.4, 1.7]),
                    np.diag([2.0, 1.3]),
                ]
            ),
            np.array(
                [
                    [[0.2, 0.05], [0.05, -0.1]],
                    [[-0.1, 0.03], [0.03, 0.15]],
                ]
            ),
        ),
        (
            BW_GEOMETRY,
            np.array(
                [
                    np.diag([1.0, 2.0]),
                    np.diag([1.4, 1.7]),
                    np.diag([2.0, 1.3]),
                ]
            ),
            np.array(
                [
                    [[0.2, 0.05], [0.05, -0.1]],
                    [[-0.1, 0.03], [0.03, 0.15]],
                ]
            ),
        ),
        (
            SPHERE_GEOMETRY,
            np.array(
                [
                    [1.0, 0.0, 0.0],
                    [np.sqrt(0.5), np.sqrt(0.5), 0.0],
                    [0.0, 1.0, 0.0],
                ]
            ),
            np.array(
                [
                    [0.0, 0.2, -0.1],
                    [0.0, -0.1, 0.3],
                ]
            ),
        ),
    ),
    ids=("airm", "bw", "sphere"),
)
def test_transport_to_polygon_and_back_recovers_reference_vectors(
    geometry,
    vertices,
    reference_vectors,
):
    frame = PolygonalFrame(np.array([0.0, 0.5, 1.0]), vertices, geometry)
    times = np.array([0.25, 0.8])
    local = transport_from_reference(frame, reference_vectors, times)
    recovered = transport_to_reference(frame, local, times)

    np.testing.assert_allclose(
        recovered,
        reference_vectors,
        rtol=2e-8,
        atol=2e-9,
    )


def test_frame_rejects_bad_time_and_shape_contracts():
    with pytest.raises(ValueError, match="strictly increasing"):
        PolygonalFrame(
            np.array([0.0, 0.5, 0.5]),
            np.repeat(np.eye(2)[None], 3, axis=0),
            AIRM_GEOMETRY,
        )

    frame = PolygonalFrame(
        np.array([0.0, 1.0]),
        np.repeat(np.eye(2)[None], 2, axis=0),
        AIRM_GEOMETRY,
    )
    with pytest.raises(ValueError, match="time range"):
        evaluate_polygon(frame, np.array([1.1]))
    with pytest.raises(ValueError, match="one leading item per time"):
        transport_from_reference(frame, np.eye(2), np.array([0.2, 0.4]))
