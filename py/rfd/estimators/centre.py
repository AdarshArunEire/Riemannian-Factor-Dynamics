"""Positive three-scale estimation of the moving RFD centre path.

This first layer contains only temporal kernels and local weight construction.
Geometry, Fréchet means and Richardson extrapolation are added in subsequent
layers so each contract remains independently understandable and testable.
"""

from dataclasses import dataclass
from typing import Callable, Literal

import numpy as np

from rfd.estimators.frame import PolygonalFrame
from rfd.geometry import GeometryOps


Side = Literal["forward", "backward"]
Kernel = Callable[[np.ndarray], np.ndarray]
THREE_SCALE_MULTIPLIERS = (1.0, 0.5, 0.25)
RICHARDSON_COEFFICIENTS = (1.0 / 3.0, -2.0, 8.0 / 3.0)


@dataclass(frozen=True)
class LocalWeights:
    """Normalized temporal weights and their finite-sample diagnostics."""

    weights: np.ndarray
    support_count: int
    effective_sample_size: float


@dataclass(frozen=True)
class LocalMeanResult:
    """One positive local Fréchet mean and its complete diagnostics."""

    point: np.ndarray
    weights: np.ndarray
    target: float
    bandwidth: float
    side: Side
    support_count: int
    effective_sample_size: float
    n_iter: int
    residual: float
    converged: bool


@dataclass(frozen=True)
class ThreeScaleMeanResult:
    """The three positive stage means for one target and one direction."""

    target: float
    base_bandwidth: float
    side: Side
    stages: tuple[LocalMeanResult, LocalMeanResult, LocalMeanResult]

    @property
    def points(self) -> np.ndarray:
        """Stage points ordered as ``b``, ``b/2`` and ``b/4``."""
        return np.stack([stage.point for stage in self.stages])

    @property
    def all_converged(self) -> bool:
        return all(stage.converged for stage in self.stages)


@dataclass(frozen=True)
class RichardsonResult:
    """One-sided signed correction, or an explicit finite-sample failure."""

    point: np.ndarray | None
    correction_tangent: np.ndarray | None
    anchor: np.ndarray
    stages: ThreeScaleMeanResult
    succeeded: bool
    failure_reason: str | None


@dataclass(frozen=True)
class OneSidedCentreEstimate:
    """Resolved one-sided estimate with an observable fallback record."""

    point: np.ndarray
    stages: ThreeScaleMeanResult
    richardson: RichardsonResult
    used_fallback: bool
    fallback_reason: str | None


@dataclass(frozen=True)
class CentreVertexEstimate:
    """One final centre vertex after one-sided estimation and blending."""

    point: np.ndarray
    target: float
    forward: OneSidedCentreEstimate | None
    backward: OneSidedCentreEstimate | None
    blend_weight: float
    used_fallback: bool
    fallback_reasons: tuple[str, ...]


@dataclass(frozen=True)
class CentrePathEstimate:
    """Complete estimated centre grid and its polygonal frame."""

    vertex_times: np.ndarray
    vertices: np.ndarray
    estimates: tuple[CentreVertexEstimate, ...]
    bandwidth: float
    overlap: tuple[float, float]
    polygon: PolygonalFrame

    @property
    def fallback_count(self) -> int:
        return sum(estimate.used_fallback for estimate in self.estimates)

    @property
    def fallback_rate(self) -> float:
        return self.fallback_count / len(self.estimates)

    @property
    def minimum_effective_sample_size(self) -> float:
        values = []
        for estimate in self.estimates:
            for one_sided in (estimate.forward, estimate.backward):
                if one_sided is not None:
                    values.extend(
                        stage.effective_sample_size
                        for stage in one_sided.stages.stages
                    )
        return float(min(values))


def endpoint_flat_kernel(v: np.ndarray) -> np.ndarray:
    """Default positive unit-mass kernel supported on ``[0, 1]``.

    This is the Beta(3, 3) density ``30 v²(1-v)²``. Both its value and first
    derivative vanish at the support endpoints, so observations enter and
    leave a moving one-sided window smoothly.
    """
    v = np.asarray(v, dtype=float)
    inside = (v >= 0.0) & (v <= 1.0)
    return np.where(inside, 30.0 * v**2 * (1.0 - v) ** 2, 0.0)


def endpoint_flat_kernel_derivative(v: np.ndarray) -> np.ndarray:
    """Derivative of :func:`endpoint_flat_kernel`."""
    v = np.asarray(v, dtype=float)
    inside = (v >= 0.0) & (v <= 1.0)
    return np.where(
        inside,
        60.0 * v * (1.0 - v) * (1.0 - 2.0 * v),
        0.0,
    )


def local_kernel_weights(
    time: np.ndarray,
    target: float,
    bandwidth: float,
    side: Side,
    kernel: Kernel = endpoint_flat_kernel,
) -> LocalWeights:
    """Construct normalized forward or backward local-kernel weights.

    ``forward`` uses rescaled offsets ``(time-target)/bandwidth``;
    ``backward`` reflects them. The kernel controls the relative weights, so
    the usual common ``1/bandwidth`` factor cancels during normalization.
    """
    time = np.asarray(time, dtype=float)
    if time.ndim != 1 or time.size == 0:
        raise ValueError("time must be a nonempty one-dimensional array")
    if not np.isfinite(time).all() or not np.isfinite(target):
        raise ValueError("time and target must be finite")
    if np.any(np.diff(time) <= 0.0):
        raise ValueError("time must be strictly increasing")
    if not np.isfinite(bandwidth) or bandwidth <= 0.0:
        raise ValueError("bandwidth must be finite and positive")
    if side == "forward":
        scaled_offset = (time - target) / bandwidth
    elif side == "backward":
        scaled_offset = (target - time) / bandwidth
    else:
        raise ValueError("side must be 'forward' or 'backward'")

    raw_weights = np.asarray(kernel(scaled_offset), dtype=float)
    if raw_weights.shape != time.shape:
        raise ValueError("kernel must return one weight per observation time")
    if not np.isfinite(raw_weights).all():
        raise ValueError("kernel returned NaN or Inf")
    if np.any(raw_weights < 0.0):
        raise ValueError("local Fréchet means require a nonnegative kernel")

    total = raw_weights.sum()
    if total <= 0.0:
        raise ValueError("no observations receive positive kernel weight")
    weights = raw_weights / total
    support_count = int(np.count_nonzero(weights > 0.0))
    effective_sample_size = min(
        float(1.0 / np.sum(weights**2)),
        float(support_count),
    )
    return LocalWeights(weights, support_count, effective_sample_size)


def positive_local_frechet_mean(
    observations: np.ndarray,
    time: np.ndarray,
    target: float,
    bandwidth: float,
    side: Side,
    geometry: GeometryOps,
    kernel: Kernel = endpoint_flat_kernel,
    mean_tol: float | None = None,
    max_iter: int = 200,
) -> LocalMeanResult:
    """Estimate one local centre using only nonnegative kernel weights.

    Zero-weight observations are removed before the geometry sees them. This
    is both cheaper and mathematically important: a point outside the local
    window must not trigger an SPD-domain or spherical-antipode failure.
    """
    observations = np.asarray(observations)
    time = np.asarray(time, dtype=float)
    if observations.ndim < 2:
        raise ValueError("observations must have a leading sample axis")
    if observations.shape[0] != time.shape[0]:
        raise ValueError("observations and time must have matching lengths")
    if max_iter <= 0:
        raise ValueError("max_iter must be positive")
    if mean_tol is not None and (not np.isfinite(mean_tol) or mean_tol <= 0.0):
        raise ValueError("mean_tol must be finite and positive")

    local = local_kernel_weights(time, target, bandwidth, side, kernel)
    included = local.weights > 0.0
    included_observations = observations[included]
    included_weights = local.weights[included]

    barycentre_kwargs = {
        "weights": included_weights,
        "max_iter": max_iter,
    }
    if mean_tol is not None:
        barycentre_kwargs["tol"] = mean_tol
    result = geometry.barycentre(included_observations, **barycentre_kwargs)

    return LocalMeanResult(
        point=result.X,
        weights=local.weights,
        target=float(target),
        bandwidth=float(bandwidth),
        side=side,
        support_count=local.support_count,
        effective_sample_size=local.effective_sample_size,
        n_iter=result.n_iter,
        residual=result.residual,
        converged=result.converged,
    )


def positive_three_scale_means(
    observations: np.ndarray,
    time: np.ndarray,
    target: float,
    bandwidth: float,
    side: Side,
    geometry: GeometryOps,
    kernel: Kernel = endpoint_flat_kernel,
    mean_tol: float | None = None,
    max_iter: int = 200,
) -> ThreeScaleMeanResult:
    """Compute the positive stage means at ``b``, ``b/2`` and ``b/4``.

    The scale ladder is deliberately fixed because the later Richardson
    coefficients are its unique matching cancellation weights. Every stage
    is still an ordinary positive-weight Fréchet minimisation.
    """
    stages = tuple(
        positive_local_frechet_mean(
            observations=observations,
            time=time,
            target=target,
            bandwidth=bandwidth * multiplier,
            side=side,
            geometry=geometry,
            kernel=kernel,
            mean_tol=mean_tol,
            max_iter=max_iter,
        )
        for multiplier in THREE_SCALE_MULTIPLIERS
    )
    return ThreeScaleMeanResult(
        target=float(target),
        base_bandwidth=float(bandwidth),
        side=side,
        stages=stages,
    )


def richardson_correct_three_scale(
    stages: ThreeScaleMeanResult,
    geometry: GeometryOps,
) -> RichardsonResult:
    """Cancel first- and second-order bias in one common tangent space.

    The broadest positive stage mean is the anchor required by the proof.
    Signed coefficients act only on its tangent vectors; no signed Fréchet
    objective is ever minimized. A failed extrapolation is reported rather
    than clipped or replaced here—the deterministic fallback belongs to the
    next estimator layer.
    """
    anchor = stages.stages[0].point
    if not stages.all_converged:
        return RichardsonResult(
            point=None,
            correction_tangent=None,
            anchor=anchor,
            stages=stages,
            succeeded=False,
            failure_reason="stage_mean_nonconvergence",
        )

    try:
        tangent_vectors = np.stack(
            [geometry.log(anchor, stage.point) for stage in stages.stages]
        )
    except (ValueError, np.linalg.LinAlgError, FloatingPointError) as error:
        return RichardsonResult(
            point=None,
            correction_tangent=None,
            anchor=anchor,
            stages=stages,
            succeeded=False,
            failure_reason=f"log_failure: {error}",
        )

    coefficients = np.asarray(RICHARDSON_COEFFICIENTS)
    correction_tangent = np.tensordot(
        coefficients,
        tangent_vectors,
        axes=(0, 0),
    )
    if not np.isfinite(correction_tangent).all():
        return RichardsonResult(
            point=None,
            correction_tangent=correction_tangent,
            anchor=anchor,
            stages=stages,
            succeeded=False,
            failure_reason="nonfinite_correction_tangent",
        )

    try:
        point = geometry.exp(anchor, correction_tangent)
    except (ValueError, np.linalg.LinAlgError, FloatingPointError) as error:
        return RichardsonResult(
            point=None,
            correction_tangent=correction_tangent,
            anchor=anchor,
            stages=stages,
            succeeded=False,
            failure_reason=f"exp_failure: {error}",
        )
    if not np.isfinite(point).all():
        return RichardsonResult(
            point=None,
            correction_tangent=correction_tangent,
            anchor=anchor,
            stages=stages,
            succeeded=False,
            failure_reason="nonfinite_corrected_point",
        )

    return RichardsonResult(
        point=point,
        correction_tangent=correction_tangent,
        anchor=anchor,
        stages=stages,
        succeeded=True,
        failure_reason=None,
    )


def fixed_overlap_weight(
    target: float,
    *,
    left: float = 1.0 / 3.0,
    right: float = 2.0 / 3.0,
) -> float:
    """Canonical fixed-width C2 transition from forward to backward.

    Between the declared endpoints this is the quintic smoothstep
    6x^5 - 15x^4 + 10x^3. Its first two derivatives vanish at both ends,
    so extending it by zero and one gives a globally C2 blend weight.
    """
    if not np.isfinite(target):
        raise ValueError("target must be finite")
    if not np.isfinite(left) or not np.isfinite(right) or right <= left:
        raise ValueError("overlap endpoints must be finite with right > left")
    if target <= left:
        return 0.0
    if target >= right:
        return 1.0
    scaled = (target - left) / (right - left)
    return float(
        6.0 * scaled**5 - 15.0 * scaled**4 + 10.0 * scaled**3
    )


def resolve_one_sided_centre(
    stages: ThreeScaleMeanResult,
    geometry: GeometryOps,
) -> OneSidedCentreEstimate:
    """Apply Richardson correction or the declared broad-stage fallback."""
    richardson = richardson_correct_three_scale(stages, geometry)
    if richardson.succeeded:
        return OneSidedCentreEstimate(
            point=richardson.point,
            stages=stages,
            richardson=richardson,
            used_fallback=False,
            fallback_reason=None,
        )

    broad_stage = stages.stages[0]
    if not broad_stage.converged:
        raise RuntimeError(
            "Richardson correction failed and its broad positive stage "
            "did not converge"
        )
    if not np.isfinite(broad_stage.point).all():
        raise FloatingPointError(
            "Richardson correction failed and its broad positive stage "
            "is nonfinite"
        )
    return OneSidedCentreEstimate(
        point=broad_stage.point,
        stages=stages,
        richardson=richardson,
        used_fallback=True,
        fallback_reason=richardson.failure_reason,
    )


def estimate_one_sided_centre(
    observations: np.ndarray,
    time: np.ndarray,
    target: float,
    bandwidth: float,
    side: Side,
    geometry: GeometryOps,
    kernel: Kernel = endpoint_flat_kernel,
    mean_tol: float | None = None,
    max_iter: int = 200,
) -> OneSidedCentreEstimate:
    """Compute and resolve all three positive stages on one side."""
    stages = positive_three_scale_means(
        observations=observations,
        time=time,
        target=target,
        bandwidth=bandwidth,
        side=side,
        geometry=geometry,
        kernel=kernel,
        mean_tol=mean_tol,
        max_iter=max_iter,
    )
    return resolve_one_sided_centre(stages, geometry)


def geodesic_blend(
    forward_point: np.ndarray,
    backward_point: np.ndarray,
    weight: float,
    geometry: GeometryOps,
) -> np.ndarray:
    """Interpolate from the forward to backward estimate by one geodesic."""
    if not np.isfinite(weight) or weight < 0.0 or weight > 1.0:
        raise ValueError("blend weight must lie in [0, 1]")
    if weight == 0.0:
        return np.array(forward_point, copy=True)
    if weight == 1.0:
        return np.array(backward_point, copy=True)
    displacement = geometry.log(forward_point, backward_point)
    point = geometry.exp(forward_point, weight * displacement)
    if not np.isfinite(point).all():
        raise FloatingPointError("geodesic blend produced NaN or Inf")
    return point


def estimate_centre_vertex(
    observations: np.ndarray,
    time: np.ndarray,
    target: float,
    bandwidth: float,
    geometry: GeometryOps,
    *,
    overlap: tuple[float, float] = (1.0 / 3.0, 2.0 / 3.0),
    kernel: Kernel = endpoint_flat_kernel,
    mean_tol: float | None = None,
    max_iter: int = 200,
) -> CentreVertexEstimate:
    """Estimate one final centre vertex under the fixed-overlap contract."""
    left, right = overlap
    if not np.isfinite(left) or not np.isfinite(right) or right <= left:
        raise ValueError("overlap must contain finite increasing endpoints")

    forward = None
    backward = None
    if target < right:
        forward = estimate_one_sided_centre(
            observations,
            time,
            target,
            bandwidth,
            "forward",
            geometry,
            kernel,
            mean_tol,
            max_iter,
        )
    if target > left:
        backward = estimate_one_sided_centre(
            observations,
            time,
            target,
            bandwidth,
            "backward",
            geometry,
            kernel,
            mean_tol,
            max_iter,
        )

    weight = fixed_overlap_weight(target, left=left, right=right)
    reasons = []
    for estimate in (forward, backward):
        if estimate is not None and estimate.used_fallback:
            reasons.append(estimate.fallback_reason or "one_sided_fallback")

    if forward is None:
        point = backward.point
    elif backward is None:
        point = forward.point
    else:
        try:
            point = geodesic_blend(
                forward.point,
                backward.point,
                weight,
                geometry,
            )
        except (ValueError, np.linalg.LinAlgError, FloatingPointError) as error:
            reasons.append(f"blend_failure: {error}")
            broad_forward = forward.stages.stages[0].point
            broad_backward = backward.stages.stages[0].point
            try:
                point = geodesic_blend(
                    broad_forward,
                    broad_backward,
                    weight,
                    geometry,
                )
            except (
                ValueError,
                np.linalg.LinAlgError,
                FloatingPointError,
            ) as broad_error:
                reasons.append(f"broad_blend_failure: {broad_error}")
                point = (
                    np.array(broad_forward, copy=True)
                    if weight <= 0.5
                    else np.array(broad_backward, copy=True)
                )

    if not np.isfinite(point).all():
        raise FloatingPointError("final centre vertex is nonfinite")
    return CentreVertexEstimate(
        point=point,
        target=float(target),
        forward=forward,
        backward=backward,
        blend_weight=weight,
        used_fallback=bool(reasons),
        fallback_reasons=tuple(reasons),
    )


def estimate_centre_path(
    observations: np.ndarray,
    time: np.ndarray,
    vertex_times: np.ndarray,
    bandwidth: float,
    geometry: GeometryOps,
    *,
    overlap_fractions: tuple[float, float] = (1.0 / 3.0, 2.0 / 3.0),
    kernel: Kernel = endpoint_flat_kernel,
    mean_tol: float | None = None,
    max_iter: int = 200,
) -> CentrePathEstimate:
    """Estimate every centre vertex and return the shared polygon."""
    observations = np.asarray(observations)
    time = np.asarray(time, dtype=float)
    vertex_times = np.asarray(vertex_times, dtype=float)

    if time.ndim != 1 or time.size == 0 or observations.shape[0] != time.size:
        raise ValueError("observations and time must have matching sample axes")
    if vertex_times.ndim != 1 or vertex_times.size < 2:
        raise ValueError("vertex_times must contain at least two points")
    if not np.isfinite(vertex_times).all() or np.any(np.diff(vertex_times) <= 0.0):
        raise ValueError("vertex_times must be finite and strictly increasing")
    if not np.isfinite(bandwidth) or bandwidth <= 0.0:
        raise ValueError("bandwidth must be finite and positive")
    if not np.isfinite(overlap_fractions).all():
        raise ValueError("overlap fractions must be finite")
    fraction_left, fraction_right = overlap_fractions
    if not 0.0 < fraction_left < fraction_right < 1.0:
        raise ValueError("overlap fractions must lie strictly inside (0, 1)")

    start = float(vertex_times[0])
    stop = float(vertex_times[-1])
    span = stop - start
    if bandwidth >= min(fraction_left, 1.0 - fraction_right) * span:
        raise ValueError(
            "bandwidth must be smaller than both fixed boundary regions"
        )
    if time[0] < start or time[-1] > stop:
        raise ValueError("observation times must lie inside the path interval")

    overlap = (
        start + fraction_left * span,
        start + fraction_right * span,
    )
    estimates = tuple(
        estimate_centre_vertex(
            observations=observations,
            time=time,
            target=float(target),
            bandwidth=bandwidth,
            geometry=geometry,
            overlap=overlap,
            kernel=kernel,
            mean_tol=mean_tol,
            max_iter=max_iter,
        )
        for target in vertex_times
    )
    vertices = np.stack([estimate.point for estimate in estimates])
    polygon = PolygonalFrame(vertex_times, vertices, geometry)
    return CentrePathEstimate(
        vertex_times=vertex_times.copy(),
        vertices=vertices,
        estimates=estimates,
        bandwidth=float(bandwidth),
        overlap=overlap,
        polygon=polygon,
    )
