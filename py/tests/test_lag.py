"""B4.4 -- tangent rows, lag operator, loading space and selectors."""

from dataclasses import replace

import numpy as np
import pytest

from rfd.estimators.frame import (
    PolygonalFrame,
    evaluate_polygon,
    transport_from_reference,
)
from rfd.estimators.lag import (
    assemble_lag_operator,
    common_reference_tangent_rows,
    coordinate_tangents,
    decompose_lag_operator,
    extract_dynamic_factors,
    lag_cross_covariances,
    raw_ratio_rank,
    ridged_ratio_rank,
    tangent_coordinates,
    threshold_rank,
)
from rfd.geometry import AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY


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
