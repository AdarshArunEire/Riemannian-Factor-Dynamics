"""Sphere geometry, transport frames, centre paths and lag operators."""

from dataclasses import replace
import pytest

import numpy as np

from rfd._maths.centre import CentrePathEstimate, LocalMeanResult, RICHARDSON_COEFFICIENTS, THREE_SCALE_MULTIPLIERS, ThreeScaleMeanResult, endpoint_flat_kernel, endpoint_flat_kernel_derivative, estimate_centre_path, fixed_overlap_weight, geodesic_blend, local_kernel_weights, positive_local_frechet_mean, positive_three_scale_means, resolve_one_sided_centre, richardson_correct_three_scale
from rfd._maths.centre_low_n import anchored_tangent_trend, graph_smoothed_polygon, piecewise_frechet_path, segmented_frechet_polygon
from rfd._maths.frame import PolygonalFrame, evaluate_polygon, polygon_cell_count, propagate_vertex_frame, regular_polygon_grid, transport_from_reference, transport_to_reference
from rfd._maths.geometry import AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY, sphere_barycentre, sphere_dist2, sphere_exp, sphere_inner, sphere_log, sphere_parallel_transport
from rfd._maths.lag import assemble_lag_operator, common_reference_tangent_rows, coordinate_tangents, decompose_lag_operator, extract_dynamic_factors, lag_cross_covariances, raw_ratio_rank, ridged_ratio_rank, tangent_coordinates, threshold_rank

# Primitive contracts for the sphere geometry adapter.

def test_exp_log_and_distance_agree_on_the_short_branch():
    base = np.array([1.0, 0.0, 0.0])
    tangent = np.array([0.0, 0.3, -0.2])
    point = sphere_exp(base, tangent)

    np.testing.assert_allclose(sphere_log(base, point), tangent, atol=2e-14)
    np.testing.assert_allclose(
        sphere_dist2(base, point),
        sphere_inner(base, tangent, tangent),
        atol=2e-14,
    )


def test_parallel_transport_preserves_tangency_and_inner_product():
    start = np.array([1.0, 0.0, 0.0, 0.0])
    end = sphere_exp(start, np.array([0.0, 0.25, -0.1, 0.0]))
    first = np.array([0.0, 0.2, 0.4, -0.3])
    second = np.array([0.0, -0.1, 0.25, 0.5])
    moved_first = sphere_parallel_transport(first, start, end)
    moved_second = sphere_parallel_transport(second, start, end)

    np.testing.assert_allclose(np.dot(end, moved_first), 0.0, atol=2e-15)
    np.testing.assert_allclose(
        sphere_inner(end, moved_first, moved_second),
        sphere_inner(start, first, second),
        atol=2e-14,
    )


def test_antipodal_log_and_transport_are_rejected():
    start = np.array([1.0, 0.0, 0.0])
    antipode = -start
    tangent = np.array([0.0, 1.0, 0.0])
    with pytest.raises(ValueError, match="antipode"):
        sphere_log(start, antipode)
    with pytest.raises(ValueError, match="antipode"):
        sphere_parallel_transport(tangent, start, antipode)


def test_weighted_barycentre_uses_relative_positive_weights():
    points = np.array(
        [
            [1.0, 0.0, 0.0],
            [np.cos(0.2), np.sin(0.2), 0.0],
            [np.cos(-0.1), np.sin(-0.1), 0.0],
        ]
    )
    weights = np.array([1.0, 2.0, 4.0])
    first = sphere_barycentre(points, weights=weights)
    scaled = sphere_barycentre(points, weights=13.0 * weights)

    assert first.converged and scaled.converged
    np.testing.assert_allclose(first.X, scaled.X, atol=2e-12)


def test_weighted_barycentre_one_hot_returns_selected_point():
    points = np.array(
        [
            [1.0, 0.0, 0.0],
            [np.cos(0.2), np.sin(0.2), 0.0],
            [np.cos(-0.1), np.sin(-0.1), 0.0],
        ]
    )
    result = sphere_barycentre(points, weights=np.array([0.0, 1.0, 0.0]))

    assert result.converged
    np.testing.assert_allclose(result.X, points[1], atol=2e-12)


def test_balanced_antipodes_have_no_selected_spherical_mean():
    points = np.array([[1.0, 0.0, 0.0], [-1.0, 0.0, 0.0]])
    with pytest.raises(ValueError, match="initializer"):
        sphere_barycentre(points)


# B4.3 -- polygonal paths and derivative-free transported frames.

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


# B4.2 -- temporal-kernel layer of the moving-centre estimator.

def test_default_kernel_has_the_required_endpoint_contract():
    endpoints = np.array([0.0, 1.0])
    np.testing.assert_array_equal(endpoint_flat_kernel(endpoints), 0.0)
    np.testing.assert_array_equal(endpoint_flat_kernel_derivative(endpoints), 0.0)
    np.testing.assert_array_equal(
        endpoint_flat_kernel(np.array([-0.1, 1.1])),
        0.0,
    )


def test_default_kernel_has_unit_continuous_mass():
    grid = np.linspace(0.0, 1.0, 10_001)
    mass = np.trapezoid(endpoint_flat_kernel(grid), grid)
    np.testing.assert_allclose(mass, 1.0, atol=2e-12)


def test_forward_and_backward_weights_look_on_the_declared_side():
    time = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    forward = local_kernel_weights(time, 0.3, 0.3, "forward")
    backward = local_kernel_weights(time, 0.3, 0.3, "backward")

    np.testing.assert_allclose(forward.weights.sum(), 1.0)
    np.testing.assert_allclose(backward.weights.sum(), 1.0)
    np.testing.assert_array_equal(np.flatnonzero(forward.weights), [3, 4])
    np.testing.assert_array_equal(np.flatnonzero(backward.weights), [0, 1])
    assert forward.support_count == backward.support_count == 2
    assert 1.0 < forward.effective_sample_size <= 2.0
    assert 1.0 < backward.effective_sample_size <= 2.0


def test_invalid_or_empty_local_windows_raise_cleanly():
    time = np.array([0.1, 0.2, 0.3])
    with pytest.raises(ValueError, match="bandwidth"):
        local_kernel_weights(time, 0.2, 0.0, "forward")
    with pytest.raises(ValueError, match="no observations"):
        local_kernel_weights(time, 0.9, 0.1, "forward")
    with pytest.raises(ValueError, match="side"):
        local_kernel_weights(time, 0.2, 0.1, "sideways")


@pytest.mark.parametrize(
    ("geometry", "point"),
    (
        (AIRM_GEOMETRY, np.diag([1.0, 2.0, 3.0])),
        (BW_GEOMETRY, np.diag([1.0, 2.0, 3.0])),
        (SPHERE_GEOMETRY, np.array([1.0, 0.0, 0.0])),
    ),
    ids=("airm", "bw", "sphere"),
)
def test_positive_local_mean_recovers_constant_observations(geometry, point):
    time = np.linspace(0.1, 0.9, 9)
    observations = np.broadcast_to(point, (time.size,) + point.shape).copy()
    result = positive_local_frechet_mean(
        observations,
        time,
        target=0.2,
        bandwidth=0.6,
        side="forward",
        geometry=geometry,
    )

    assert result.converged
    assert result.support_count == np.count_nonzero(result.weights)
    assert 1.0 <= result.effective_sample_size <= result.support_count
    np.testing.assert_allclose(result.weights.sum(), 1.0)
    np.testing.assert_allclose(result.point, point, rtol=2e-11, atol=2e-12)


def test_zero_weight_sphere_antipode_never_reaches_the_local_mean():
    time = np.array([0.1, 0.4, 0.5, 0.6])
    observations = np.array(
        [
            [-1.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [np.cos(0.1), np.sin(0.1), 0.0],
            [1.0, 0.0, 0.0],
        ]
    )
    result = positive_local_frechet_mean(
        observations,
        time,
        target=0.4,
        bandwidth=0.2,
        side="forward",
        geometry=SPHERE_GEOMETRY,
    )

    assert result.converged
    assert result.weights[0] == 0.0
    assert np.dot(result.point, observations[0]) < 0.0


@pytest.mark.parametrize(
    ("geometry", "point"),
    (
        (AIRM_GEOMETRY, np.diag([1.0, 2.0, 3.0])),
        (BW_GEOMETRY, np.diag([1.0, 2.0, 3.0])),
        (SPHERE_GEOMETRY, np.array([1.0, 0.0, 0.0])),
    ),
    ids=("airm", "bw", "sphere"),
)
def test_three_scale_stage_ladder_remains_positive_and_ordered(geometry, point):
    time = np.linspace(0.01, 0.99, 99)
    observations = np.broadcast_to(point, (time.size,) + point.shape).copy()
    bandwidth = 0.4
    result = positive_three_scale_means(
        observations,
        time,
        target=0.2,
        bandwidth=bandwidth,
        side="forward",
        geometry=geometry,
    )

    assert result.all_converged
    np.testing.assert_allclose(
        [stage.bandwidth for stage in result.stages],
        bandwidth * np.asarray(THREE_SCALE_MULTIPLIERS),
    )
    support_counts = [stage.support_count for stage in result.stages]
    assert support_counts[0] > support_counts[1] > support_counts[2]
    np.testing.assert_allclose(
        result.points,
        np.broadcast_to(point, result.points.shape),
        rtol=2e-11,
        atol=2e-12,
    )


def synthetic_three_scale(points, *, converged=True):
    stages = tuple(
        LocalMeanResult(
            point=point,
            weights=np.array([1.0]),
            target=0.5,
            bandwidth=multiplier,
            side="forward",
            support_count=1,
            effective_sample_size=1.0,
            n_iter=1,
            residual=0.0,
            converged=converged,
        )
        for point, multiplier in zip(points, THREE_SCALE_MULTIPLIERS)
    )
    return ThreeScaleMeanResult(0.5, 1.0, "forward", stages)


def test_richardson_coefficients_preserve_signal_and_annihilate_two_bias_orders():
    coefficients = np.asarray(RICHARDSON_COEFFICIENTS)
    scales = np.asarray(THREE_SCALE_MULTIPLIERS)
    np.testing.assert_allclose(coefficients.sum(), 1.0)
    np.testing.assert_allclose(coefficients @ scales, 0.0, atol=2e-16)
    np.testing.assert_allclose(coefficients @ scales**2, 0.0, atol=2e-16)


def test_richardson_reproduces_the_tiny_diagonal_airm_example():
    tangent_stages = np.array(
        [
            [[0.256, 0.0], [0.0, -0.048]],
            [[0.232, 0.0], [0.0, -0.076]],
            [[0.21775, 0.0], [0.0, -0.088875]],
        ]
    )
    identity = np.eye(2)
    points = AIRM_GEOMETRY.exp(identity, tangent_stages)
    result = richardson_correct_three_scale(
        synthetic_three_scale(points),
        AIRM_GEOMETRY,
    )

    assert result.succeeded
    expected_point = AIRM_GEOMETRY.exp(identity, np.diag([0.202, -0.101]))
    np.testing.assert_allclose(
        result.correction_tangent,
        AIRM_GEOMETRY.log(points[0], expected_point),
        atol=2e-14,
    )
    np.testing.assert_allclose(
        result.point,
        expected_point,
        atol=2e-14,
    )


@pytest.mark.parametrize(
    ("geometry", "point"),
    (
        (AIRM_GEOMETRY, np.diag([1.0, 2.0])),
        (BW_GEOMETRY, np.diag([1.0, 2.0])),
        (SPHERE_GEOMETRY, np.array([1.0, 0.0, 0.0])),
    ),
    ids=("airm", "bw", "sphere"),
)
def test_richardson_leaves_three_identical_stage_means_unchanged(geometry, point):
    result = richardson_correct_three_scale(
        synthetic_three_scale([point, point, point]),
        geometry,
    )

    assert result.succeeded
    assert result.failure_reason is None
    np.testing.assert_allclose(result.correction_tangent, 0.0, atol=2e-14)
    np.testing.assert_allclose(result.point, point, atol=2e-13)


def test_richardson_reports_bw_normal_branch_exit():
    anchor = np.eye(2)
    far_middle_stage = np.diag([9.0, 1.0])
    result = richardson_correct_three_scale(
        synthetic_three_scale([anchor, far_middle_stage, anchor]),
        BW_GEOMETRY,
    )

    assert not result.succeeded
    assert result.point is None
    assert result.failure_reason.startswith("exp_failure:")
    assert "compatible full-rank branch" in result.failure_reason


def test_richardson_refuses_a_nonconverged_stage_mean():
    point = np.eye(2)
    result = richardson_correct_three_scale(
        synthetic_three_scale([point, point, point], converged=False),
        AIRM_GEOMETRY,
    )
    assert not result.succeeded
    assert result.failure_reason == "stage_mean_nonconvergence"


def test_fixed_overlap_weight_is_c2_and_has_fixed_one_third_width():
    left, right = 1.0 / 3.0, 2.0 / 3.0
    assert fixed_overlap_weight(0.0) == 0.0
    assert fixed_overlap_weight(left) == 0.0
    assert fixed_overlap_weight(0.5) == pytest.approx(0.5)
    assert fixed_overlap_weight(right) == 1.0
    assert fixed_overlap_weight(1.0) == 1.0

    epsilon = 1e-4
    assert fixed_overlap_weight(left + epsilon) < 1e-8
    assert 1.0 - fixed_overlap_weight(right - epsilon) < 1e-8


def test_resolved_bw_richardson_failure_uses_the_broad_positive_stage():
    anchor = np.eye(2)
    stages = synthetic_three_scale(
        [anchor, np.diag([9.0, 1.0]), anchor]
    )
    result = resolve_one_sided_centre(stages, BW_GEOMETRY)

    assert result.used_fallback
    assert result.fallback_reason.startswith("exp_failure:")
    np.testing.assert_array_equal(result.point, anchor)


def test_resolved_failure_refuses_a_nonconverged_broad_fallback():
    stages = synthetic_three_scale(
        [np.eye(2), np.eye(2), np.eye(2)],
        converged=False,
    )
    with pytest.raises(RuntimeError, match="broad positive stage"):
        resolve_one_sided_centre(stages, AIRM_GEOMETRY)


@pytest.mark.parametrize(
    ("geometry", "point"),
    (
        (AIRM_GEOMETRY, np.diag([1.0, 2.0])),
        (BW_GEOMETRY, np.diag([1.0, 2.0])),
        (SPHERE_GEOMETRY, np.array([1.0, 0.0, 0.0])),
    ),
    ids=("airm", "bw", "sphere"),
)
def test_complete_constant_centre_path_is_exact_without_fallback(geometry, point):
    n = 80
    time = np.arange(1, n + 1, dtype=float) / n
    observations = np.broadcast_to(point, (n,) + point.shape).copy()
    vertex_times = np.linspace(0.0, 1.0, 7)

    result = estimate_centre_path(
        observations,
        time,
        vertex_times,
        bandwidth=0.2,
        geometry=geometry,
    )

    assert isinstance(result, CentrePathEstimate)
    assert result.fallback_count == 0
    assert result.fallback_rate == 0.0
    assert result.minimum_effective_sample_size > 1.0
    np.testing.assert_allclose(
        result.vertices,
        np.broadcast_to(point, result.vertices.shape),
        rtol=3e-10,
        atol=3e-11,
    )
    evaluated = evaluate_polygon(result.polygon, time)
    np.testing.assert_allclose(
        evaluated.points,
        np.broadcast_to(point, evaluated.points.shape),
        rtol=3e-10,
        atol=3e-11,
    )

    assert result.estimates[0].forward is not None
    assert result.estimates[0].backward is None
    assert result.estimates[-1].forward is None
    assert result.estimates[-1].backward is not None
    middle = result.estimates[len(result.estimates) // 2]
    assert middle.forward is not None
    assert middle.backward is not None
    assert middle.blend_weight == pytest.approx(0.5)


def test_richardson_path_improves_a_smooth_commuting_airm_control():
    n = 400
    time = np.arange(1, n + 1, dtype=float) / n

    def tangent_curve(values):
        first = 0.35 * values + 0.20 * values**2 + 0.12 * values**3
        second = -0.20 * values + 0.08 * values**2 - 0.10 * values**3
        return np.stack([first, second], axis=-1)

    observations = np.array(
        [np.diag(np.exp(value)) for value in tangent_curve(time)]
    )
    vertex_times = np.linspace(0.0, 1.0, 13)
    truth = np.array(
        [np.diag(np.exp(value)) for value in tangent_curve(vertex_times)]
    )
    result = estimate_centre_path(
        observations,
        time,
        vertex_times,
        bandwidth=0.2,
        geometry=AIRM_GEOMETRY,
    )

    broad_vertices = []
    for estimate in result.estimates:
        if estimate.forward is None:
            broad = estimate.backward.stages.stages[0].point
        elif estimate.backward is None:
            broad = estimate.forward.stages.stages[0].point
        else:
            broad = geodesic_blend(
                estimate.forward.stages.stages[0].point,
                estimate.backward.stages.stages[0].point,
                estimate.blend_weight,
                AIRM_GEOMETRY,
            )
        broad_vertices.append(broad)
    broad_vertices = np.stack(broad_vertices)

    corrected_rms = np.sqrt(
        np.mean(AIRM_GEOMETRY.dist2(result.vertices, truth))
    )
    broad_rms = np.sqrt(
        np.mean(AIRM_GEOMETRY.dist2(broad_vertices, truth))
    )

    assert result.fallback_count == 0
    assert corrected_rms < broad_rms
    assert corrected_rms < 0.002


def test_complete_path_rejects_a_bandwidth_that_breaks_fixed_overlap_windows():
    time = np.linspace(0.1, 1.0, 10)
    observations = np.repeat(np.eye(2)[None], 10, axis=0)
    with pytest.raises(ValueError, match="fixed boundary regions"):
        estimate_centre_path(
            observations,
            time,
            np.linspace(0.0, 1.0, 4),
            bandwidth=1.0 / 3.0,
            geometry=AIRM_GEOMETRY,
        )


def _diagonal(values):
    return np.stack([np.diag(value) for value in values])






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


# B4.4 -- tangent rows, lag operator, loading space and selectors.

GEOMETRY_POINTS = (
    (AIRM_GEOMETRY, np.diag([1.0, 2.0]), 3),
    (BW_GEOMETRY, np.diag([1.0, 2.0]), 3),
    (SPHERE_GEOMETRY, np.array([1.0, 0.0, 0.0]), 2),
)


@pytest.mark.parametrize(
    ("geometry", "point", "dimension"),
    GEOMETRY_POINTS,
    ids=("airm", "bw", "sphere"),
)
def test_geometry_supplies_a_metric_orthonormal_tangent_basis(
    geometry,
    point,
    dimension,
):
    basis = geometry.tangent_basis(point)
    gram = geometry.inner(
        point,
        basis[:, None, ...],
        basis[None, ...],
    )

    assert basis.shape[0] == dimension
    np.testing.assert_allclose(gram, np.eye(dimension), atol=2e-11)


@pytest.mark.parametrize(
    ("geometry", "point", "dimension"),
    GEOMETRY_POINTS,
    ids=("airm", "bw", "sphere"),
)
def test_tangent_coordinate_round_trip_is_exact_in_the_metric_basis(
    geometry,
    point,
    dimension,
):
    basis = geometry.tangent_basis(point)
    expected_rows = np.arange(1, 2 * dimension + 1, dtype=float).reshape(
        2,
        dimension,
    ) / 20.0
    vectors = coordinate_tangents(expected_rows, basis)
    recovered_rows = tangent_coordinates(vectors, point, basis, geometry)

    np.testing.assert_allclose(recovered_rows, expected_rows, atol=3e-13)


def test_tangent_coordinate_batching_matches_individual_bw_rows():
    point = np.diag([1.0, 1.5, 2.0])
    basis = BW_GEOMETRY.tangent_basis(point)
    rng = np.random.default_rng(812)
    raw = rng.standard_normal((17, 3, 3))
    vectors = 0.5 * (raw + raw.mT)

    batched = tangent_coordinates(
        vectors, point, basis, BW_GEOMETRY, batch_size=4
    )
    individual = np.stack([
        tangent_coordinates(vector, point, basis, BW_GEOMETRY)
        for vector in vectors
    ])

    np.testing.assert_array_equal(batched, individual)


def test_tangent_coordinates_rejects_invalid_batch_size():
    point = np.eye(2)
    basis = BW_GEOMETRY.tangent_basis(point)
    with pytest.raises(ValueError, match="batch_size"):
        tangent_coordinates(
            np.zeros((2, 2, 2)), point, basis, BW_GEOMETRY, batch_size=0
        )


@pytest.mark.parametrize(
    ("geometry", "vertices"),
    (
        (
            AIRM_GEOMETRY,
            np.array(
                [
                    np.diag([1.0, 2.0]),
                    np.diag([1.3, 1.8]),
                    np.diag([1.7, 1.4]),
                ]
            ),
        ),
        (
            BW_GEOMETRY,
            np.array(
                [
                    np.diag([1.0, 2.0]),
                    np.diag([1.3, 1.8]),
                    np.diag([1.7, 1.4]),
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
        ),
    ),
    ids=("airm", "bw", "sphere"),
)
def test_observation_logs_return_to_their_original_reference_rows(
    geometry,
    vertices,
):
    frame = PolygonalFrame(np.array([0.0, 0.5, 1.0]), vertices, geometry)
    time = np.array([0.2, 0.7])
    basis = geometry.tangent_basis(frame.reference_point)
    dimension = basis.shape[0]
    expected_rows = np.vstack(
        [
            np.linspace(0.01, 0.03, dimension),
            np.linspace(-0.02, 0.015, dimension),
        ]
    )
    reference_vectors = coordinate_tangents(expected_rows, basis)
    local_vectors = transport_from_reference(frame, reference_vectors, time)
    local_centres = evaluate_polygon(frame, time).points
    observations = geometry.exp(local_centres, local_vectors)

    result = common_reference_tangent_rows(observations, time, frame)

    np.testing.assert_allclose(result.rows, expected_rows, rtol=3e-8, atol=3e-9)
    np.testing.assert_allclose(
        result.reference_vectors,
        reference_vectors,
        rtol=3e-8,
        atol=3e-9,
    )
    np.testing.assert_allclose(result.local_centres, local_centres, atol=2e-13)
    assert result.tangent_dimension == dimension


def test_parent_lag_convention_uses_common_tail_and_full_row_divisor():
    rows = np.array(
        [
            [1.0, 0.0],
            [2.0, 1.0],
            [4.0, -1.0],
            [3.0, 2.0],
            [6.0, 1.0],
        ]
    )
    result = lag_cross_covariances(rows, max_lag=2)
    centred = rows - rows.mean(axis=0)
    expected_lag_1 = centred[2:].T @ centred[1:-1] / rows.shape[0]
    expected_lag_2 = centred[2:].T @ centred[:-2] / rows.shape[0]

    np.testing.assert_allclose(
        result.covariances,
        np.stack([expected_lag_1, expected_lag_2]),
    )
    np.testing.assert_array_equal(result.pair_counts, [3, 3])
    np.testing.assert_array_equal(result.divisors, [5, 5])
    assert result.tail_mode == "common"
    assert result.normalization == "row_size"


def test_available_pairs_and_pair_count_normalization_are_explicit():
    rows = np.arange(18, dtype=float).reshape(6, 3)
    result = lag_cross_covariances(
        rows,
        max_lag=3,
        tail_mode="available",
        normalization="pair_count",
    )

    np.testing.assert_array_equal(result.pair_counts, [5, 4, 3])
    np.testing.assert_array_equal(result.divisors, [5, 4, 3])
    for covariance, lag in zip(result.covariances, result.lags):
        expected = (
            result.centred_rows[lag:].T
            @ result.centred_rows[:-lag]
            / (rows.shape[0] - lag)
        )
        np.testing.assert_allclose(covariance, expected)


def test_lag_operator_is_the_positive_semidefinite_square_of_the_row():
    rng = np.random.default_rng(41)
    lag_row = lag_cross_covariances(rng.standard_normal((20, 4)), max_lag=3)
    result = assemble_lag_operator(lag_row)

    np.testing.assert_allclose(
        result.matrix,
        sum(gamma @ gamma.T for gamma in lag_row.covariances),
        atol=3e-16,
    )
    np.testing.assert_allclose(
        result.matrix,
        result.stacked_row @ result.stacked_row.T,
        atol=3e-16,
    )
    np.testing.assert_allclose(result.matrix, result.matrix.T, atol=2e-16)
    assert np.linalg.eigvalsh(result.matrix).min() >= -2e-15


def test_squaring_lags_prevents_opposite_lag_matrices_from_cancelling():
    rows = np.zeros((4, 2))
    template = lag_cross_covariances(rows, max_lag=2, demean=False)
    gamma = np.array([[2.0, -1.0], [0.5, 3.0]])
    opposed = type(template)(
        covariances=np.stack([gamma, -gamma]),
        lags=template.lags,
        centred_rows=template.centred_rows,
        row_mean=template.row_mean,
        pair_counts=template.pair_counts,
        divisors=template.divisors,
        tail_mode=template.tail_mode,
        normalization=template.normalization,
    )
    result = assemble_lag_operator(opposed)

    np.testing.assert_allclose(opposed.covariances.sum(axis=0), 0.0)
    np.testing.assert_allclose(result.matrix, 2.0 * gamma @ gamma.T)
    assert np.linalg.norm(result.matrix) > 0.0


def test_common_rigid_coordinate_gauge_only_conjugates_the_operator():
    rng = np.random.default_rng(42)
    rows = rng.standard_normal((30, 5))
    rotation, _ = np.linalg.qr(rng.standard_normal((5, 5)))

    original = assemble_lag_operator(
        lag_cross_covariances(rows, max_lag=3)
    ).matrix
    rotated = assemble_lag_operator(
        lag_cross_covariances(rows @ rotation, max_lag=3)
    ).matrix

    np.testing.assert_allclose(
        rotated,
        rotation.T @ original @ rotation,
        atol=3e-15,
    )
    np.testing.assert_allclose(
        np.linalg.eigvalsh(rotated),
        np.linalg.eigvalsh(original),
        atol=3e-15,
    )


@pytest.mark.parametrize(
    ("kwargs", "message"),
    (
        ({"max_lag": 0}, "max_lag"),
        ({"max_lag": 5}, "max_lag"),
        ({"max_lag": 1, "tail_mode": "split"}, "tail_mode"),
        ({"max_lag": 1, "normalization": "mystery"}, "normalization"),
    ),
)
def test_lag_row_rejects_ambiguous_or_invalid_conventions(kwargs, message):
    with pytest.raises(ValueError, match=message):
        lag_cross_covariances(np.ones((5, 2)), **kwargs)


def test_svd_spectrum_reconstructs_the_lag_operator_without_negative_roundoff():
    rng = np.random.default_rng(43)
    result = assemble_lag_operator(
        lag_cross_covariances(rng.standard_normal((40, 6)), max_lag=4)
    )
    spectrum = decompose_lag_operator(result)
    reconstructed = (
        spectrum.eigenvectors
        @ np.diag(spectrum.eigenvalues)
        @ spectrum.eigenvectors.T
    )

    assert np.all(spectrum.eigenvalues >= 0.0)
    assert np.all(np.diff(spectrum.eigenvalues) <= 0.0)
    np.testing.assert_allclose(
        spectrum.eigenvectors.T @ spectrum.eigenvectors,
        np.eye(6),
        atol=2e-15,
    )
    np.testing.assert_allclose(reconstructed, result.matrix, atol=3e-15)


def test_rank_two_persistent_dgp_recovers_loading_space_and_both_proved_selectors():
    rng = np.random.default_rng(51)
    n, dimension, rank = 2_000, 5, 2
    loadings, _ = np.linalg.qr(rng.standard_normal((dimension, rank)))
    persistence = np.array([0.8, 0.55])
    scale = np.array([1.5, 1.0])
    factors = np.empty((n, rank))
    factors[0] = scale * rng.standard_normal(rank)
    for time_index in range(1, n):
        factors[time_index] = (
            persistence * factors[time_index - 1]
            + scale
            * np.sqrt(1.0 - persistence**2)
            * rng.standard_normal(rank)
        )
    rows = factors @ loadings.T + 0.05 * rng.standard_normal((n, dimension))

    lag_operator = assemble_lag_operator(
        lag_cross_covariances(rows, max_lag=3)
    )
    spectrum = decompose_lag_operator(lag_operator)
    fit = extract_dynamic_factors(spectrum, rank)
    threshold = threshold_rank(spectrum.eigenvalues, threshold=0.01)
    ridged = ridged_ratio_rank(spectrum.eigenvalues, ridge=0.01)

    true_projector = loadings @ loadings.T
    fitted_projector = fit.loadings @ fit.loadings.T
    assert np.linalg.norm(fitted_projector - true_projector, ord=2) < 0.02
    assert threshold.rank == rank
    assert ridged.rank == rank
    np.testing.assert_allclose(
        fit.fitted_centred_rows + fit.residual_rows,
        lag_operator.lag_row.centred_rows,
        atol=3e-16,
    )
    np.testing.assert_allclose(
        fit.factor_scores,
        lag_operator.lag_row.centred_rows @ fit.loadings,
        atol=2e-16,
    )
    np.testing.assert_allclose(
        fit.residual_rows @ fit.loadings,
        0.0,
        atol=2e-14,
    )


def test_row_error_controls_assembly_and_the_first_beyond_rank_eigenvalue():
    rng = np.random.default_rng(52)
    dimension, rank, lag_count = 6, 2, 3
    loadings, _ = np.linalg.qr(rng.standard_normal((dimension, rank)))
    target_covariances = np.stack(
        [
            loadings @ rng.standard_normal((rank, rank)) @ loadings.T
            for _ in range(lag_count)
        ]
    )
    defects = 0.002 * rng.standard_normal(
        (lag_count, dimension, dimension)
    )
    estimated_covariances = target_covariances + defects

    template = lag_cross_covariances(
        np.zeros((10, dimension)),
        max_lag=lag_count,
        demean=False,
    )
    target_row = replace(template, covariances=target_covariances)
    estimated_row = replace(template, covariances=estimated_covariances)
    target_operator = assemble_lag_operator(target_row)
    estimated_operator = assemble_lag_operator(estimated_row)
    spectrum = decompose_lag_operator(estimated_operator)

    row_size = np.sqrt(
        sum(np.linalg.norm(gamma, ord=2) ** 2 for gamma in target_covariances)
    )
    row_error = np.sqrt(
        sum(np.linalg.norm(defect, ord=2) ** 2 for defect in defects)
    )
    assembly_bound = 2.0 * row_size * row_error + row_error**2

    assert (
        np.linalg.norm(
            estimated_operator.matrix - target_operator.matrix,
            ord=2,
        )
        <= assembly_bound + 2e-14
    )
    assert spectrum.eigenvalues[rank] <= row_error**2 + 2e-14


def test_raw_ratio_counterexample_selects_two_while_proved_selectors_select_one():
    row_error = 0.01
    eigenvalues = np.array([1.0, row_error**2, 0.0])
    threshold = 0.01

    raw = raw_ratio_rank(eigenvalues, max_rank=2)
    thresholded = threshold_rank(eigenvalues, threshold)
    ridged = ridged_ratio_rank(eigenvalues, ridge=threshold, max_rank=2)

    assert raw.rank == 2
    assert raw.ratios[1] == 0.0
    assert thresholded.rank == 1
    assert ridged.rank == 1


def test_raw_ratio_exposes_undefined_zero_over_zero_candidates():
    result = raw_ratio_rank(np.array([1.0, 0.0, 0.0]), max_rank=2)

    assert result.rank == 1
    assert result.ratios[0] == 0.0
    assert np.isnan(result.ratios[1])


def test_zero_rank_fit_preserves_only_the_coordinate_intercept():
    rows = np.array([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
    spectrum = decompose_lag_operator(
        assemble_lag_operator(lag_cross_covariances(rows, max_lag=1))
    )
    fit = extract_dynamic_factors(spectrum, rank=0)

    assert fit.loadings.shape == (2, 0)
    assert fit.factor_scores.shape == (3, 0)
    np.testing.assert_allclose(fit.fitted_centred_rows, 0.0)
    np.testing.assert_allclose(
        fit.reconstructed_rows,
        np.broadcast_to(rows.mean(axis=0), rows.shape),
    )
