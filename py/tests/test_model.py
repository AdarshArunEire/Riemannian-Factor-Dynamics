"""End-to-end contracts for the composed RFD model."""

import numpy as np
import pytest

from rfd.estimators.lag import coordinate_tangents
from rfd.geometry import AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY
from rfd.model import RFDConfig, fit_rfd


GEOMETRY_CASES = (
    (AIRM_GEOMETRY, np.diag([1.0, 1.6])),
    (BW_GEOMETRY, np.diag([1.0, 1.6])),
    (SPHERE_GEOMETRY, np.array([1.0, 0.0, 0.0])),
)


def _small_manifold_series(geometry, point, n=48):
    time = np.linspace(0.0, 1.0, n)
    basis = geometry.tangent_basis(point)
    phase = 2.0 * np.pi * time
    rows = np.column_stack(
        [
            0.025 * np.sin((index + 1) * phase)
            + 0.01 * np.cos((index + 2) * phase)
            for index in range(basis.shape[0])
        ]
    )
    vectors = coordinate_tangents(rows, basis)
    centres = np.broadcast_to(point, (n,) + point.shape)
    observations = geometry.exp(centres, vectors)
    return observations, time, basis.shape[0]


@pytest.mark.parametrize(
    ("geometry", "point"),
    GEOMETRY_CASES,
    ids=("airm", "bw", "sphere"),
)
def test_full_rank_fit_round_trips_manifold_observations(geometry, point):
    observations, time, dimension = _small_manifold_series(geometry, point)
    config = RFDConfig(
        bandwidth=0.2,
        n_cells=3,
        max_lag=2,
        rank_method="fixed",
        rank=dimension,
    )

    fit = fit_rfd(observations, time, geometry, config)

    assert fit.rank == dimension
    assert fit.tangent_rows.rows.shape == (time.size, dimension)
    assert fit.loadings.shape == (dimension, dimension)
    assert fit.factor_scores.shape == (time.size, dimension)
    assert fit.reconstructed_observations.shape == observations.shape
    np.testing.assert_allclose(
        fit.reconstructed_observations,
        observations,
        rtol=3e-7,
        atol=3e-8,
    )


def test_threshold_selector_returns_rank_zero_on_a_constant_path():
    n = 42
    point = np.diag([1.0, 1.7])
    observations = np.broadcast_to(point, (n, 2, 2)).copy()
    time = np.linspace(0.0, 1.0, n)
    config = RFDConfig(
        bandwidth=0.2,
        n_cells=3,
        max_lag=2,
        rank_method="threshold",
        threshold=1e-10,
    )

    fit = fit_rfd(observations, time, AIRM_GEOMETRY, config)

    assert fit.rank == 0
    assert fit.factor_scores.shape == (n, 0)
    np.testing.assert_allclose(fit.spectrum.eigenvalues, 0.0, atol=1e-25)
    np.testing.assert_allclose(
        fit.reconstructed_observations,
        observations,
        atol=2e-12,
    )


def test_fit_retains_every_intermediate_operator_identity():
    observations, time, dimension = _small_manifold_series(
        AIRM_GEOMETRY,
        np.diag([1.0, 1.5]),
        n=50,
    )
    config = RFDConfig(
        bandwidth=0.2,
        n_cells=4,
        max_lag=3,
        rank_method="fixed",
        rank=1,
    )

    fit = fit_rfd(observations, time, AIRM_GEOMETRY, config)

    np.testing.assert_allclose(
        fit.lag_operator.matrix,
        fit.lag_operator.stacked_row @ fit.lag_operator.stacked_row.T,
        atol=2e-16,
    )
    np.testing.assert_allclose(
        fit.factors.fitted_centred_rows + fit.residual_rows,
        fit.lag_row.centred_rows,
        atol=3e-16,
    )
    assert fit.reconstructed_reference_vectors.shape == (time.size, 2, 2)
    assert fit.reconstructed_local_vectors.shape == (time.size, 2, 2)
    assert fit.centre.polygon is fit.centre.polygon
    assert fit.spectrum.eigenvalues.shape == (dimension,)


@pytest.mark.parametrize(
    ("kwargs", "message"),
    (
        ({"rank_method": "fixed"}, "rank is required"),
        ({"rank_method": "threshold"}, "threshold is required"),
        ({"rank_method": "ridged_ratio"}, "ridge is required"),
        ({"rank_method": "mystery"}, "rank_method"),
        ({"rank_method": "fixed", "rank": -1}, "nonnegative"),
    ),
)
def test_config_rejects_implicit_or_invalid_rank_rules(kwargs, message):
    with pytest.raises(ValueError, match=message):
        RFDConfig(
            bandwidth=0.2,
            n_cells=3,
            max_lag=2,
            **kwargs,
        )


def test_fit_rejects_nonfinite_observations_before_geometry_runs():
    observations = np.broadcast_to(np.eye(2), (20, 2, 2)).copy()
    observations[5, 0, 0] = np.nan
    config = RFDConfig(
        bandwidth=0.2,
        n_cells=3,
        max_lag=2,
        rank_method="fixed",
        rank=1,
    )

    with pytest.raises(ValueError, match="finite"):
        fit_rfd(
            observations,
            np.linspace(0.0, 1.0, observations.shape[0]),
            AIRM_GEOMETRY,
            config,
        )
