"""B4.1 -- configurable, geometry-neutral LSRFM data generation.

The suite tests scientific controls rather than implementation details: path
geometry, factor lag laws, loading/drift orientation, transported tangent
norms, the four drift/factor corners, structured flats and reproducibility.
"""

from dataclasses import replace

import numpy as np
import pytest

from rfd.dgp.lsrfm import (
    AR1FactorConfig,
    CentrePathConfig,
    LoadingConfig,
    LSRFMConfig,
    NoiseConfig,
    VAR1FactorConfig,
    centre_path,
    centre_path_diagnostics,
    generate_ar1_factors,
    generate_loadings,
    generate_lsrfm,
    generate_reference_tangent_noise,
    generate_var1_factors,
    rescaled_time,
)
from rfd.geometry import AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY


GEOMETRIES = (AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY)


def linear_profile(time):
    return time


def geometry_fixture(geometry):
    """Small compatible base point, drift and safe simulation scales."""
    if geometry.name in {"airm", "bw"}:
        base = np.diag([1.0, 1.5, 2.0])
        drift = np.diag([1.0, -0.5, 0.25])
        if geometry.name == "bw":
            return base, drift, 0.08, 0.025, 0.01
        return base, drift, 0.2, 0.08, 0.03
    base = np.array([1.0, 0.0, 0.0, 0.0])
    drift = np.array([0.0, 1.0, 0.0, 0.0])
    return base, drift, 0.2, 0.08, 0.03


def baseline_config(
    geometry,
    *,
    rank=2,
    drift_on=True,
    factors_on=True,
    noise_on=True,
    orientation="random",
):
    base, drift, drift_scale, factor_scale, noise_scale = geometry_fixture(geometry)
    return LSRFMConfig(
        centre=CentrePathConfig(
            base_centre=base,
            drift_direction=drift,
            drift_scale=drift_scale if drift_on else 0.0,
            profile=linear_profile,
        ),
        factor=AR1FactorConfig(
            rank=rank,
            persistence=np.linspace(0.35, 0.75, rank) if rank else 0.0,
            scale=factor_scale if factors_on else 0.0,
        ),
        loading=LoadingConfig(orientation=orientation),
        noise=NoiseConfig(scale=noise_scale if noise_on else 0.0),
    )


def intrinsic_gram(geometry, base, vectors):
    rank = vectors.shape[0]
    return np.array(
        [
            [geometry.inner(base, vectors[i], vectors[j]) for j in range(rank)]
            for i in range(rank)
        ]
    )


def intrinsic_norms(geometry, bases, vectors):
    return np.sqrt(
        np.array(
            [geometry.inner(base, vector, vector) for base, vector in zip(bases, vectors)]
        )
    )


@pytest.mark.parametrize("geometry", GEOMETRIES, ids=lambda item: item.name)
def test_linear_unit_drift_has_declared_length_and_energy(geometry):
    """Normalising V makes drift_scale equal length and its square equal energy."""
    n = 12
    config = baseline_config(geometry, rank=1).centre
    path_time = np.concatenate(([0.0], rescaled_time(n)))
    path_centres = centre_path(path_time, geometry, config)
    length, energy = centre_path_diagnostics(path_time, path_centres, geometry)

    np.testing.assert_allclose(length, config.drift_scale, rtol=2e-7, atol=2e-9)
    np.testing.assert_allclose(
        energy,
        config.drift_scale**2,
        rtol=3e-7,
        atol=2e-9,
    )


def test_componentwise_ar1_controls_variance_and_lag_separately():
    persistence = np.array([0.2, 0.65, -0.4])
    scale = np.array([0.4, 0.8, 1.2])
    factors = generate_ar1_factors(
        np.random.default_rng(20260819),
        60_000,
        AR1FactorConfig(3, persistence, scale),
    )
    variance = factors.var(axis=0)
    lag_one = np.array(
        [np.corrcoef(factors[:-1, j], factors[1:, j])[0, 1] for j in range(3)]
    )

    np.testing.assert_allclose(variance, scale**2, rtol=0.05)
    np.testing.assert_allclose(lag_one, persistence, atol=0.025)


def test_var1_supports_cross_factor_lag_structure():
    transition = np.array([[0.55, 0.20], [0.0, 0.35]])
    innovation = np.array([[0.25, 0.04], [0.04, 0.16]])
    factors = generate_var1_factors(
        np.random.default_rng(8),
        50_000,
        VAR1FactorConfig(transition, innovation),
    )
    fitted = np.linalg.lstsq(factors[:-1], factors[1:], rcond=None)[0].T
    np.testing.assert_allclose(fitted, transition, atol=0.025)


def test_unstable_var_is_rejected():
    with pytest.raises(ValueError, match="stable"):
        generate_var1_factors(
            np.random.default_rng(9),
            5,
            VAR1FactorConfig(np.diag([1.01, 0.4]), np.eye(2)),
        )


@pytest.mark.parametrize("geometry", GEOMETRIES, ids=lambda item: item.name)
@pytest.mark.parametrize(
    ("orientation", "overlap"),
    (("aligned", 1.0), ("orthogonal", 0.0), ("mixed", 0.35)),
)
def test_loadings_are_orthonormal_with_declared_drift_overlap(
    geometry,
    orientation,
    overlap,
):
    base, drift, *_ = geometry_fixture(geometry)
    loadings = generate_loadings(
        np.random.default_rng(10),
        base,
        rank=2,
        drift_direction=drift,
        geometry=geometry,
        config=LoadingConfig(orientation=orientation, drift_overlap=overlap),
    )
    unit_drift = drift / np.sqrt(geometry.inner(base, drift, drift))

    np.testing.assert_allclose(
        intrinsic_gram(geometry, base, loadings),
        np.eye(2),
        rtol=2e-9,
        atol=2e-9,
    )
    actual = abs(float(geometry.inner(base, loadings[0], unit_drift)))
    if orientation == "orthogonal":
        assert max(abs(geometry.inner(base, item, unit_drift)) for item in loadings) < 2e-9
    else:
        np.testing.assert_allclose(actual, overlap, atol=2e-9)


@pytest.mark.parametrize("geometry", (AIRM_GEOMETRY, BW_GEOMETRY), ids=lambda item: item.name)
def test_commuting_loading_structure_creates_exact_spd_flat(geometry):
    base, drift, *_ = geometry_fixture(geometry)
    loadings = generate_loadings(
        np.random.default_rng(11),
        base,
        rank=2,
        drift_direction=drift,
        geometry=geometry,
        config=LoadingConfig(structure="commuting"),
    )
    commutators = loadings @ base - base @ loadings
    np.testing.assert_allclose(commutators, 0.0, atol=2e-12)


def test_sphere_rejects_spd_only_commuting_structure():
    base, drift, *_ = geometry_fixture(SPHERE_GEOMETRY)
    with pytest.raises(ValueError, match="dense"):
        generate_loadings(
            np.random.default_rng(12),
            base,
            rank=1,
            drift_direction=drift,
            geometry=SPHERE_GEOMETRY,
            config=LoadingConfig(structure="commuting"),
        )


@pytest.mark.parametrize("geometry", GEOMETRIES, ids=lambda item: item.name)
def test_noise_has_declared_norm_after_parallel_transport(geometry):
    n = 5
    config = baseline_config(geometry, rank=1)
    time = rescaled_time(n)
    centres = centre_path(time, geometry, config.centre)
    reference_noise = generate_reference_tangent_noise(
        np.random.default_rng(13),
        n,
        config.centre.base_centre,
        geometry,
        config.noise,
    )
    noise = geometry.transport(
        reference_noise,
        config.centre.base_centre,
        centres,
    )
    norms = intrinsic_norms(geometry, centres, noise)
    np.testing.assert_allclose(norms, config.noise.scale, rtol=3e-7, atol=3e-9)


@pytest.mark.parametrize("geometry", GEOMETRIES, ids=lambda item: item.name)
@pytest.mark.parametrize(
    ("drift_on", "factors_on"),
    ((False, False), (True, False), (False, True), (True, True)),
    ids=("all-off", "drift-only", "factor-only", "full"),
)
def test_all_four_drift_factor_corners(geometry, drift_on, factors_on):
    config = baseline_config(
        geometry,
        rank=1,
        drift_on=drift_on,
        factors_on=factors_on,
        noise_on=False,
    )
    sample = generate_lsrfm(np.random.default_rng(14), 5, geometry, config)

    assert sample.geometry_name == geometry.name
    assert sample.observations.shape == sample.centres.shape
    assert sample.factor_effects.shape == sample.centres.shape
    assert sample.tangent_noise.shape == sample.centres.shape
    assert sample.factors.shape == (5, 1)
    if geometry.name == "sphere":
        np.testing.assert_allclose(
            np.linalg.norm(sample.observations, axis=-1), 1.0, atol=2e-12
        )
    else:
        assert np.linalg.eigvalsh(sample.observations).min() > 0.0

    base_stack = np.broadcast_to(config.centre.base_centre, sample.centres.shape)
    if drift_on:
        assert np.max(geometry.dist2(sample.centres, base_stack)) > 1e-8
    else:
        np.testing.assert_allclose(sample.centres, base_stack, atol=2e-12)
    if factors_on:
        assert np.max(geometry.dist2(sample.observations, sample.centres)) > 1e-10
    else:
        np.testing.assert_allclose(sample.observations, sample.centres, atol=2e-10)


@pytest.mark.parametrize("geometry", GEOMETRIES, ids=lambda item: item.name)
def test_generation_is_reproducible_from_the_rng_seed(geometry):
    config = baseline_config(geometry, rank=1)
    first = generate_lsrfm(np.random.default_rng(15), 4, geometry, config)
    second = generate_lsrfm(np.random.default_rng(15), 4, geometry, config)

    for field in (
        "observations",
        "centres",
        "factors",
        "loadings",
        "factor_effects",
        "tangent_noise",
        "time",
    ):
        np.testing.assert_array_equal(getattr(first, field), getattr(second, field))
    assert first.centre_path_length == second.centre_path_length
    assert first.centre_path_energy == second.centre_path_energy


def test_zero_rank_is_a_real_factor_null_not_a_special_case_crash():
    config = baseline_config(AIRM_GEOMETRY, rank=0, factors_on=False, noise_on=False)
    sample = generate_lsrfm(np.random.default_rng(16), 4, AIRM_GEOMETRY, config)
    assert sample.factors.shape == (4, 0)
    assert sample.loadings.shape == (0, 3, 3)
    np.testing.assert_allclose(sample.observations, sample.centres, atol=2e-12)


def test_configuration_objects_are_independently_replaceable():
    """A stress grid can change one causal lever without rebuilding the rest."""
    original = baseline_config(AIRM_GEOMETRY)
    changed = replace(original, noise=replace(original.noise, persistence=0.7))
    assert changed.centre is original.centre
    assert changed.factor is original.factor
    assert changed.loading is original.loading
    assert changed.noise.persistence == 0.7
