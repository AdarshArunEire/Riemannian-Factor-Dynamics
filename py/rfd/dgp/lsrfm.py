from dataclasses import dataclass
from typing import Callable
from rfd.spd.linalg import spd_sqrt
import numpy as np

@dataclass(frozen=True)
class CentrePathConfig:
    base_centre: np.ndarray
    drift_direction: np.ndarray
    drift_scale: float
    profile: Callable[[np.ndarray], np.ndarray]

@dataclass(frozen=True)
class AR1FactorConfig:
    rank: int
    persistence: float
    scale: float

'''
@dataclass(frozen=True)
class LoadingConfig:
    orientation: str
    structure: str
'''

@dataclass(frozen=True)
class NoiseConfig:
    scale: float
    ### persistence: float

@dataclass(frozen=True)
class LSRFMConfig:
    centre: CentrePathConfig
    factor: AR1FactorConfig
    ### loading: LoadingConfig
    noise: NoiseConfig


@dataclass(frozen=True)
class LSRFMSample:
    observations: np.ndarray
    centres: np.ndarray
    factors: np.ndarray
    loadings: np.ndarray
    tangent_noise: np.ndarray
    time: np.ndarray
    centre_path_length: float
    centre_path_energy: float


def rescaled_time(n: int) -> np.ndarray:
    return np.arange(1, n + 1, dtype=float) / n


def centre_path(time, geometry, config):
    amplitude = (
        config.drift_scale 
        * config.profile(time)
    )

    trailing_axes = (1,) * config.drift_direction.ndim
    tangent_path = amplitude.reshape((-1,) + trailing_axes)
    tangent_path = tangent_path * config.drift_direction

    return geometry.exp(
        config.base_centre,
        tangent_path,
    )


def generate_ar1_factors( # first-order autoregressive factors
    rng,
    n,
    config: AR1FactorConfig, 
) -> np.ndarray:

    rank = config.rank
    persistence = config.persistence
    scale = config.scale
    
    factors = np.empty((n, rank))

    factors[0] = scale * rng.standard_normal(rank)

    innovation_scale = scale * np.sqrt(1 - persistence**2)

    for t in range(1, n):
        factors[t] = (
            persistence * factors[t - 1]
            + innovation_scale * rng.standard_normal(rank)
        )

    return factors


def generate_airm_loadings(rng, base_centre, rank):
    m = base_centre.shape[-1]

    raw = rng.standard_normal((rank, m, m))
    raw = 0.5 * (raw + raw.mT)

    flat = raw.reshape(rank, m * m).T
    orthonormal, _ = np.linalg.qr(flat)

    normal_loadings = (
        orthonormal[:, :rank].T
        .reshape(rank, m, m)
    )

    root = spd_sqrt(base_centre)

    return root @ normal_loadings @ root


def generate_airm_tangent_noise(
    rng,
    n,
    base_centre,
    centres,
    geometry,
    config: NoiseConfig,
) -> np.ndarray:
    
    m = base_centre.shape[-1]

    raw = rng.standard_normal((n, m, m))
    symmetric = 0.5 * (raw + raw.mT)

    norms = np.linalg.norm(
        symmetric,
        axis=(-2, -1),
        keepdims=True,
    )
    unit_normal_noise = symmetric / norms

    root = spd_sqrt(base_centre)

    reference_noise = (
        config.scale
        * root
        @ unit_normal_noise
        @ root
    )

    return geometry.transport(
        reference_noise,
        base_centre,
        centres,
    )

def centre_path_diagnostics(
    path_time,
    path_centres,
    geometry,
):
    step_dist2 = geometry.dist2(
        path_centres[:-1],
        path_centres[1:],
    )

    delta_time = np.diff(path_time)

    length = np.sqrt(step_dist2).sum()
    energy = (step_dist2 / delta_time).sum()

    return float(length), float(energy)


def generate_airm_lsrfm(rng, n, geometry, config: LSRFMConfig) -> LSRFMSample:

    time = rescaled_time(n)
    path_time = np.concatenate([
        np.array([0.0]),
        time,
    ])

    path_centres = centre_path(
        path_time,
        geometry,
        config.centre,
    )
    centres = path_centres[1:]

    factors = generate_ar1_factors(rng, n, config.factor)
    
    loadings = generate_airm_loadings(
        rng,
        config.centre.base_centre,
        config.factor.rank
        )

    reference_effects = np.tensordot(
        factors,
        loadings,
        axes=([-1], [0]),
    )


    transported_effects = geometry.transport(
        reference_effects,
        config.centre.base_centre,
        centres
    )

    tangent_noise = generate_airm_tangent_noise(
        rng,
        n,
        config.centre.base_centre,
        centres,
        geometry,
        config.noise
    )


    total_tangent = transported_effects + tangent_noise
    observations = geometry.exp(centres, total_tangent)

    centre_path_length, centre_path_energy = centre_path_diagnostics(
        path_time,
        path_centres,
        geometry,
    )

    return LSRFMSample(
        observations=observations,
        centres=centres,
        factors=factors,
        loadings=loadings,
        tangent_noise=tangent_noise,
        time=time,
        centre_path_length=centre_path_length,
        centre_path_energy=centre_path_energy
    )
