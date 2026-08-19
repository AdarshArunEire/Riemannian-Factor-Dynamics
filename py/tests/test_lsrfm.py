"""B4.1 -- locally stationary Riemannian factor-model DGP.

These tests check the mathematical contracts of the generator.  They avoid
pinning random draws or private implementation details: the relevant truths
are path geometry, factor moments, tangent norms, positive definiteness, and
reproducibility from an explicit RNG seed.
"""

import numpy as np

from rfd.dgp.lsrfm import (
    AR1FactorConfig,
    CentrePathConfig,
    LSRFMConfig,
    NoiseConfig,
    centre_path,
    centre_path_diagnostics,
    generate_airm_loadings,
    generate_airm_lsrfm,
    generate_airm_tangent_noise,
    generate_ar1_factors,
    rescaled_time,
)
from rfd.geometry import AIRM_GEOMETRY
from rfd.spd.linalg import spd_invsqrt, spd_sqrt


def linear_profile(time):
    """Move once along a single geodesic from amplitude zero to one."""
    return time


def airm_unit_direction(base_centre):
    """A deterministic unit AIRM tangent direction at an SPD base point."""
    m = base_centre.shape[-1]
    normal = np.zeros((m, m))
    normal[0, 0] = 1.0 / np.sqrt(2.0)
    normal[1, 1] = -1.0 / np.sqrt(2.0)
    root = spd_sqrt(base_centre)
    return root @ normal @ root


def baseline_config(
    *,
    m=3,
    rank=2,
    drift_scale=0.25,
    factor_persistence=0.8,
    factor_scale=0.4,
    noise_scale=0.2,
):
    """Small, well-conditioned configuration shared by integration tests."""
    base_centre = np.diag(np.linspace(1.0, 2.0, m))
    return LSRFMConfig(
        centre=CentrePathConfig(
            base_centre=base_centre,
            drift_direction=airm_unit_direction(base_centre),
            drift_scale=drift_scale,
            profile=linear_profile,
        ),
        factor=AR1FactorConfig(
            rank=rank,
            persistence=factor_persistence,
            scale=factor_scale,
        ),
        noise=NoiseConfig(scale=noise_scale),
    )


def test_linear_unit_drift_has_declared_length_and_energy():
    """For mu(u)=Exp_mu0(nu*u*V), ||V||=1: L=nu and E=nu**2."""
    n = 24
    drift_scale = 0.4
    config = baseline_config(drift_scale=drift_scale).centre
    path_time = np.concatenate(([0.0], rescaled_time(n)))
    path_centres = centre_path(path_time, AIRM_GEOMETRY, config)

    length, energy = centre_path_diagnostics(
        path_time,
        path_centres,
        AIRM_GEOMETRY,
    )

    np.testing.assert_allclose(length, drift_scale, rtol=1e-11, atol=1e-12)
    np.testing.assert_allclose(
        energy,
        drift_scale**2,
        rtol=1e-10,
        atol=1e-12,
    )


def test_ar1_factors_have_target_variance_and_lag_one_correlation():
    """The variance correction separates factor scale from persistence."""
    persistence = 0.8
    scale = 0.7
    factors = generate_ar1_factors(
        np.random.default_rng(20260819),
        n=50_000,
        config=AR1FactorConfig(
            rank=3,
            persistence=persistence,
            scale=scale,
        ),
    )

    variance = factors.var(axis=0)
    lag_one = np.array(
        [np.corrcoef(factors[:-1, j], factors[1:, j])[0, 1] for j in range(3)]
    )

    np.testing.assert_allclose(variance, scale**2, rtol=0.06)
    np.testing.assert_allclose(lag_one, persistence, atol=0.025)


def test_airm_loadings_are_orthonormal_at_the_base_centre():
    """The loading Gram matrix under the AIRM tangent metric is identity."""
    base_centre = np.diag([1.0, 2.0, 4.0])
    loadings = generate_airm_loadings(
        np.random.default_rng(11),
        base_centre,
        rank=4,
    )

    inverse_root = spd_invsqrt(base_centre)
    normal_loadings = inverse_root @ loadings @ inverse_root
    gram = np.einsum("aij,bij->ab", normal_loadings, normal_loadings)

    np.testing.assert_allclose(gram, np.eye(4), rtol=1e-12, atol=1e-12)


def test_airm_noise_has_the_declared_tangent_norm_at_every_centre():
    """Reference noise is unit-normalised and transport preserves its norm."""
    n = 18
    noise_scale = 0.3
    config = baseline_config(noise_scale=noise_scale)
    time = rescaled_time(n)
    centres = centre_path(time, AIRM_GEOMETRY, config.centre)
    noise = generate_airm_tangent_noise(
        np.random.default_rng(12),
        n,
        config.centre.base_centre,
        centres,
        AIRM_GEOMETRY,
        config.noise,
    )

    inverse_roots = spd_invsqrt(centres)
    normal_noise = inverse_roots @ noise @ inverse_roots
    norms = np.linalg.norm(normal_noise, axis=(-2, -1))

    np.testing.assert_allclose(norms, noise_scale, rtol=1e-11, atol=1e-12)


def test_generated_sample_has_expected_shapes_and_spd_observations():
    """The integrated DGP returns one valid SPD observation at every time."""
    n, m, rank = 16, 3, 2
    sample = generate_airm_lsrfm(
        np.random.default_rng(13),
        n,
        AIRM_GEOMETRY,
        baseline_config(m=m, rank=rank),
    )

    assert sample.observations.shape == (n, m, m)
    assert sample.centres.shape == (n, m, m)
    assert sample.factors.shape == (n, rank)
    assert sample.loadings.shape == (rank, m, m)
    assert sample.tangent_noise.shape == (n, m, m)
    assert sample.time.shape == (n,)
    assert np.linalg.eigvalsh(sample.observations).min() > 0.0


def test_all_off_placebo_returns_the_constant_centre():
    """With drift, factors, and noise off, every observation equals mu0."""
    n = 10
    config = baseline_config(
        drift_scale=0.0,
        factor_scale=0.0,
        noise_scale=0.0,
    )
    sample = generate_airm_lsrfm(
        np.random.default_rng(14),
        n,
        AIRM_GEOMETRY,
        config,
    )
    expected = np.broadcast_to(config.centre.base_centre, sample.observations.shape)

    np.testing.assert_allclose(sample.centres, expected, rtol=1e-13, atol=1e-13)
    np.testing.assert_allclose(
        sample.observations,
        expected,
        rtol=1e-12,
        atol=1e-12,
    )
    assert sample.centre_path_length < 1e-12
    assert sample.centre_path_energy < 1e-12


def test_generation_is_reproducible_from_the_rng_seed():
    """An explicit seed reproduces every latent and observed array exactly."""
    config = baseline_config()
    first = generate_airm_lsrfm(
        np.random.default_rng(15),
        12,
        AIRM_GEOMETRY,
        config,
    )
    second = generate_airm_lsrfm(
        np.random.default_rng(15),
        12,
        AIRM_GEOMETRY,
        config,
    )

    for field in (
        "observations",
        "centres",
        "factors",
        "loadings",
        "tangent_noise",
        "time",
    ):
        np.testing.assert_array_equal(getattr(first, field), getattr(second, field))

    assert first.centre_path_length == second.centre_path_length
    assert first.centre_path_energy == second.centre_path_energy
