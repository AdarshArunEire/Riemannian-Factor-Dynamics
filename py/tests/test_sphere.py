"""Primitive contracts for the sphere geometry adapter."""

import numpy as np
import pytest

from rfd.sphere import (
    sphere_barycentre,
    sphere_dist2,
    sphere_exp,
    sphere_inner,
    sphere_log,
    sphere_parallel_transport,
)


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
