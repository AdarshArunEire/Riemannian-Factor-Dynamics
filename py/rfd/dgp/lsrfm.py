"""Configurable locally stationary Riemannian factor-model generator.

The generator implements

    X_t = Exp_{mu(t)}(P_t[A f_t] + delta_t),

while keeping centre drift, loading orientation, factor dynamics and tangent
noise as separate experimental controls. Manifold-specific mathematics is
provided by :class:`rfd.geometry.GeometryOps`; this module contains no SPD or
sphere formula.
"""

from dataclasses import dataclass, field
from typing import Callable, Literal, TypeAlias

import numpy as np
from scipy.linalg import solve_discrete_lyapunov

from rfd.geometry import AIRM_GEOMETRY, GeometryOps


Array = np.ndarray
Orientation = Literal["random", "aligned", "orthogonal", "mixed"]
TangentStructure = Literal["dense", "commuting"]


@dataclass(frozen=True)
class CentrePathConfig:
    """One radial centre path ``Exp_base(drift_scale * profile(t) * V)``."""

    base_centre: Array
    drift_direction: Array
    drift_scale: float
    profile: Callable[[Array], Array]
    normalise_direction: bool = True


@dataclass(frozen=True)
class AR1FactorConfig:
    """Independent stationary AR(1) factors.

    ``persistence`` and ``scale`` may each be scalars or length-``rank``
    vectors. Thus factors can carry different lag strengths without needing
    a separate process class.
    """

    rank: int
    persistence: float | Array
    scale: float | Array


@dataclass(frozen=True)
class VAR1FactorConfig:
    """Stable cross-coupled VAR(1) factors for harder lag-operator tests."""

    transition: Array
    innovation_covariance: Array

    @property
    def rank(self) -> int:
        return int(np.asarray(self.transition).shape[0])


FactorConfig: TypeAlias = AR1FactorConfig | VAR1FactorConfig


@dataclass(frozen=True)
class LoadingConfig:
    """Geometry and drift relationship of the reference loading space.

    ``mixed`` makes the first loading have the requested absolute cosine with
    the drift direction. ``commuting`` is available on SPD geometries and
    produces exact common-flat controls; the sphere supports ``dense`` only.
    """

    orientation: Orientation = "random"
    drift_overlap: float = 0.5
    structure: TangentStructure = "dense"


@dataclass(frozen=True)
class NoiseConfig:
    """Reference-tangent noise controls.

    ``persistence`` creates a directional AR(1) stress process. With
    ``constant_norm=True`` every realised noise vector has exactly ``scale``
    intrinsic norm; this is useful for bounded-energy experiments, although
    the normalisation means its correlation is no longer exactly the scalar
    AR coefficient.
    """

    scale: float
    persistence: float = 0.0
    constant_norm: bool = True
    structure: TangentStructure = "dense"


@dataclass(frozen=True)
class LSRFMConfig:
    centre: CentrePathConfig
    factor: FactorConfig
    noise: NoiseConfig
    loading: LoadingConfig = field(default_factory=LoadingConfig)


@dataclass(frozen=True)
class LSRFMSample:
    observations: Array
    centres: Array
    factors: Array
    loadings: Array
    factor_effects: Array
    tangent_noise: Array
    time: Array
    centre_path_length: float
    centre_path_energy: float
    geometry_name: str


def rescaled_time(n: int) -> Array:
    """Observation times ``1/n, ..., 1``."""
    if n <= 0:
        raise ValueError("n must be positive")
    return np.arange(1, n + 1, dtype=float) / n


def _intrinsic_norm(vector: Array, base: Array, geometry: GeometryOps) -> float:
    squared = float(geometry.inner(base, vector, vector))
    if not np.isfinite(squared) or squared <= 1e-24:
        raise ValueError("tangent vector has zero or non-finite intrinsic norm")
    return float(np.sqrt(max(squared, 0.0)))


def _unit_tangent(vector: Array, base: Array, geometry: GeometryOps) -> Array:
    return np.asarray(vector, dtype=float) / _intrinsic_norm(vector, base, geometry)


def centre_path(
    time: Array,
    geometry: GeometryOps,
    config: CentrePathConfig,
) -> Array:
    """Evaluate the configured centre path at arbitrary rescaled times."""
    time = np.asarray(time, dtype=float)
    profile = np.asarray(config.profile(time), dtype=float)
    if profile.shape != time.shape:
        raise ValueError("centre profile must return one scalar per time")
    if not np.isfinite(profile).all():
        raise ValueError("centre profile returned NaN or Inf")
    if config.drift_scale < 0.0:
        raise ValueError("drift_scale must be nonnegative")

    direction = np.asarray(config.drift_direction, dtype=float)
    if config.normalise_direction:
        direction = _unit_tangent(direction, config.base_centre, geometry)

    amplitude = config.drift_scale * profile
    trailing_axes = (1,) * direction.ndim
    tangent_path = amplitude.reshape((-1,) + trailing_axes) * direction
    return geometry.exp(config.base_centre, tangent_path)


def _parameter_vector(value, rank: int, name: str) -> Array:
    result = np.asarray(value, dtype=float)
    if result.ndim == 0:
        result = np.full(rank, float(result))
    if result.shape != (rank,):
        raise ValueError(f"{name} must be scalar or have shape ({rank},)")
    if not np.isfinite(result).all():
        raise ValueError(f"{name} contains NaN or Inf")
    return result


def generate_ar1_factors(
    rng: np.random.Generator,
    n: int,
    config: AR1FactorConfig,
) -> Array:
    """Generate exactly stationary, component-wise AR(1) factors."""
    if n <= 0:
        raise ValueError("n must be positive")
    if config.rank < 0:
        raise ValueError("factor rank must be nonnegative")
    if config.rank == 0:
        return np.empty((n, 0))

    persistence = _parameter_vector(config.persistence, config.rank, "persistence")
    scale = _parameter_vector(config.scale, config.rank, "scale")
    if np.any(np.abs(persistence) >= 1.0):
        raise ValueError("AR(1) persistence must lie strictly between -1 and 1")
    if np.any(scale < 0.0):
        raise ValueError("factor scale must be nonnegative")

    factors = np.empty((n, config.rank))
    factors[0] = scale * rng.standard_normal(config.rank)
    innovation_scale = scale * np.sqrt(1.0 - persistence**2)
    for t in range(1, n):
        factors[t] = (
            persistence * factors[t - 1]
            + innovation_scale * rng.standard_normal(config.rank)
        )
    return factors


def _psd_gaussian(rng: np.random.Generator, covariance: Array) -> Array:
    covariance = 0.5 * (covariance + covariance.T)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    tolerance = 1e-10 * max(1.0, float(np.max(np.abs(eigenvalues))))
    if np.min(eigenvalues) < -tolerance:
        raise ValueError("covariance must be positive semidefinite")
    root = eigenvectors * np.sqrt(np.clip(eigenvalues, 0.0, None))
    return root @ rng.standard_normal(covariance.shape[0])


def generate_var1_factors(
    rng: np.random.Generator,
    n: int,
    config: VAR1FactorConfig,
) -> Array:
    """Generate a stationary Gaussian VAR(1) process."""
    if n <= 0:
        raise ValueError("n must be positive")
    transition = np.asarray(config.transition, dtype=float)
    innovation = np.asarray(config.innovation_covariance, dtype=float)
    if transition.ndim != 2 or transition.shape[0] != transition.shape[1]:
        raise ValueError("VAR transition must be square")
    if innovation.shape != transition.shape:
        raise ValueError("innovation covariance must match the transition")
    if not np.isfinite(transition).all() or not np.isfinite(innovation).all():
        raise ValueError("VAR configuration contains NaN or Inf")
    if np.max(np.abs(np.linalg.eigvals(transition))) >= 1.0:
        raise ValueError("VAR transition must be stable")

    stationary = solve_discrete_lyapunov(transition, innovation)
    factors = np.empty((n, transition.shape[0]))
    factors[0] = _psd_gaussian(rng, stationary)
    for t in range(1, n):
        factors[t] = transition @ factors[t - 1] + _psd_gaussian(rng, innovation)
    return factors


def generate_factors(
    rng: np.random.Generator,
    n: int,
    config: FactorConfig,
) -> Array:
    """Dispatch the explicitly supported factor-process families."""
    if isinstance(config, AR1FactorConfig):
        return generate_ar1_factors(rng, n, config)
    if isinstance(config, VAR1FactorConfig):
        return generate_var1_factors(rng, n, config)
    raise TypeError(f"unsupported factor configuration: {type(config).__name__}")


def _orthogonalise(
    candidate: Array,
    basis: list[Array],
    base: Array,
    geometry: GeometryOps,
) -> Array:
    result = np.array(candidate, dtype=float, copy=True)
    for _ in range(2):
        for vector in basis:
            result -= float(geometry.inner(base, result, vector)) * vector
    return result


def _new_orthogonal_unit(
    rng: np.random.Generator,
    base: Array,
    geometry: GeometryOps,
    structure: TangentStructure,
    exclusions: list[Array],
) -> Array:
    for _ in range(256):
        candidate = geometry.random_tangent(rng, base, 1, structure)[0]
        candidate = _orthogonalise(candidate, exclusions, base, geometry)
        squared = float(geometry.inner(base, candidate, candidate))
        if np.isfinite(squared) and squared > 1e-18:
            return candidate / np.sqrt(squared)
    raise ValueError("requested loading rank exceeds the available tangent subspace")


def generate_loadings(
    rng: np.random.Generator,
    base: Array,
    rank: int,
    drift_direction: Array,
    geometry: GeometryOps,
    config: LoadingConfig,
) -> Array:
    """Generate an intrinsically orthonormal reference loading frame."""
    if rank < 0:
        raise ValueError("loading rank must be nonnegative")
    if config.orientation not in {"random", "aligned", "orthogonal", "mixed"}:
        raise ValueError(f"unknown loading orientation: {config.orientation}")
    if not 0.0 <= config.drift_overlap <= 1.0:
        raise ValueError("drift_overlap must lie in [0, 1]")
    if rank == 0:
        return np.empty((0,) + np.asarray(base).shape)

    drift = _unit_tangent(drift_direction, base, geometry)
    loadings: list[Array] = []
    exclusions: list[Array] = []
    if config.orientation == "aligned":
        loadings.append(drift)
    elif config.orientation == "orthogonal":
        exclusions.append(drift)
    elif config.orientation == "mixed":
        orthogonal = _new_orthogonal_unit(
            rng, base, geometry, config.structure, [drift]
        )
        overlap = config.drift_overlap
        first = overlap * drift + np.sqrt(1.0 - overlap**2) * orthogonal
        loadings.append(_unit_tangent(first, base, geometry))

    while len(loadings) < rank:
        loadings.append(
            _new_orthogonal_unit(
                rng,
                base,
                geometry,
                config.structure,
                exclusions + loadings,
            )
        )
    return np.stack(loadings)


def generate_reference_tangent_noise(
    rng: np.random.Generator,
    n: int,
    base: Array,
    geometry: GeometryOps,
    config: NoiseConfig,
) -> Array:
    """Generate tangent noise in the reference fibre before transport."""
    if n <= 0:
        raise ValueError("n must be positive")
    if config.scale < 0.0:
        raise ValueError("noise scale must be nonnegative")
    if abs(config.persistence) >= 1.0:
        raise ValueError("noise persistence must lie strictly between -1 and 1")
    if config.scale == 0.0:
        return np.zeros((n,) + np.asarray(base).shape)

    draws = geometry.random_tangent(rng, base, n, config.structure)
    units = np.stack([_unit_tangent(draw, base, geometry) for draw in draws])
    states = np.empty_like(units)
    states[0] = config.scale * units[0]
    innovation_weight = np.sqrt(1.0 - config.persistence**2)
    for t in range(1, n):
        states[t] = (
            config.persistence * states[t - 1]
            + config.scale * innovation_weight * units[t]
        )
        if config.constant_norm:
            states[t] = config.scale * _unit_tangent(states[t], base, geometry)
    return states


def centre_path_diagnostics(
    path_time: Array,
    path_centres: Array,
    geometry: GeometryOps,
) -> tuple[float, float]:
    """Discrete intrinsic length and piecewise-geodesic path energy."""
    path_time = np.asarray(path_time, dtype=float)
    if path_time.ndim != 1 or path_time.shape[0] != path_centres.shape[0]:
        raise ValueError("path_time and path_centres must have matching lengths")
    delta_time = np.diff(path_time)
    if np.any(delta_time <= 0.0):
        raise ValueError("path_time must be strictly increasing")
    step_dist2 = geometry.dist2(path_centres[:-1], path_centres[1:])
    length = np.sqrt(step_dist2).sum()
    energy = (step_dist2 / delta_time).sum()
    return float(length), float(energy)


def generate_lsrfm(
    rng: np.random.Generator,
    n: int,
    geometry: GeometryOps,
    config: LSRFMConfig,
) -> LSRFMSample:
    """Generate one complete LSRFM sample on the selected geometry."""
    time = rescaled_time(n)
    path_time = np.concatenate(([0.0], time))
    path_centres = centre_path(path_time, geometry, config.centre)
    centres = path_centres[1:]

    factors = generate_factors(rng, n, config.factor)
    rank = factors.shape[1]
    loadings = generate_loadings(
        rng,
        config.centre.base_centre,
        rank,
        config.centre.drift_direction,
        geometry,
        config.loading,
    )
    reference_effects = np.tensordot(factors, loadings, axes=([-1], [0]))
    reference_noise = generate_reference_tangent_noise(
        rng,
        n,
        config.centre.base_centre,
        geometry,
        config.noise,
    )

    factor_effects = geometry.transport(
        reference_effects,
        config.centre.base_centre,
        centres,
    )
    tangent_noise = geometry.transport(
        reference_noise,
        config.centre.base_centre,
        centres,
    )
    observations = geometry.exp(centres, factor_effects + tangent_noise)
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
        factor_effects=factor_effects,
        tangent_noise=tangent_noise,
        time=time,
        centre_path_length=centre_path_length,
        centre_path_energy=centre_path_energy,
        geometry_name=geometry.name,
    )


def generate_airm_lsrfm(
    rng: np.random.Generator,
    n: int,
    geometry: GeometryOps,
    config: LSRFMConfig,
) -> LSRFMSample:
    """Checked compatibility entry point for the original AIRM-only API."""
    if geometry.name != AIRM_GEOMETRY.name:
        raise ValueError("generate_airm_lsrfm requires AIRM_GEOMETRY")
    return generate_lsrfm(rng, n, geometry, config)
