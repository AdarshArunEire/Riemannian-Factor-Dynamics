"""B4.2 -- temporal-kernel layer of the moving-centre estimator."""

import numpy as np
import pytest

from rfd.estimators.centre import (
    CentrePathEstimate,
    RICHARDSON_COEFFICIENTS,
    THREE_SCALE_MULTIPLIERS,
    LocalMeanResult,
    ThreeScaleMeanResult,
    endpoint_flat_kernel,
    endpoint_flat_kernel_derivative,
    estimate_centre_path,
    fixed_overlap_weight,
    geodesic_blend,
    local_kernel_weights,
    positive_local_frechet_mean,
    positive_three_scale_means,
    resolve_one_sided_centre,
    richardson_correct_three_scale,
)
from rfd.estimators.frame import evaluate_polygon
from rfd.geometry import AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY


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
