"""Low-sample centre-path estimators built only from positive BW operations.

These estimators are finite-sample application candidates.  They do not
replace the three-scale Richardson theorem without separate rate analysis.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from rfd.estimators.frame import PolygonalFrame, evaluate_polygon
from rfd.geometry import GeometryOps
from rfd.spd.bw import bw_clip_exp_tangent


Array = np.ndarray


@dataclass(frozen=True)
class LowSamplePathResult:
    points: Array
    diagnostics: dict[str, float | int | bool]


@dataclass(frozen=True)
class LowSamplePolygonResult:
    """A low-sample centre path whose geometry remains explicitly available."""

    points: Array
    frame: PolygonalFrame
    diagnostics: dict[str, float | int | bool]


def _validate_times(time: Array, target_times: Array, n: int) -> tuple[Array, Array]:
    time = np.asarray(time, dtype=float)
    target_times = np.asarray(target_times, dtype=float)
    if time.shape != (n,) or target_times.ndim != 1:
        raise ValueError("time and target_times must be one-dimensional")
    if not np.isfinite(time).all() or not np.isfinite(target_times).all():
        raise ValueError("times must be finite")
    if np.any(np.diff(time) <= 0.0):
        raise ValueError("training times must be strictly increasing")
    return time, target_times


def anchored_tangent_trend(
    observations: Array,
    time: Array,
    target_times: Array,
    anchor: Array,
    geometry: GeometryOps,
    *,
    bw_step_margin: float = 0.05,
) -> LowSamplePathResult:
    """Fit one tangent-linear trend through a supplied global centre.

    All observations estimate one slope, so this is deliberately much lower
    variance than independently estimated local vertices.  For BW, radial
    clipping is reported if a target leaves the compatible Exp branch.
    """
    observations = np.asarray(observations, dtype=float)
    anchor = np.asarray(anchor, dtype=float)
    if observations.ndim < 2 or observations.shape[1:] != anchor.shape:
        raise ValueError("observations and anchor have incompatible shapes")
    time, target_times = _validate_times(time, target_times, observations.shape[0])

    centred = time - float(time.mean())
    denominator = float(np.dot(centred, centred))
    if denominator <= 0.0:
        raise ValueError("at least two distinct training times are required")
    tangent_rows = geometry.log(anchor, observations)
    slope = np.tensordot(centred, tangent_rows, axes=(0, 0)) / denominator
    targets = (target_times - float(time.mean()))[:, None, None] * slope

    clipped = 0
    minimum_factor = 1.0
    if geometry.name == "bw":
        anchors = np.broadcast_to(anchor, targets.shape)
        guarded = bw_clip_exp_tangent(
            anchors, targets, step_margin=bw_step_margin
        )
        targets = guarded.tangent
        clipped = int(np.count_nonzero(guarded.factors < 1.0))
        minimum_factor = float(np.min(guarded.factors))
    points = geometry.exp(np.broadcast_to(anchor, targets.shape), targets)
    return LowSamplePathResult(
        points=np.asarray(points),
        diagnostics={
            "clipped_targets": clipped,
            "minimum_clip_factor": minimum_factor,
            "slope_norm_frobenius": float(np.linalg.norm(slope)),
        },
    )


def piecewise_frechet_path(
    observations: Array,
    time: Array,
    target_times: Array,
    segments: int,
    geometry: GeometryOps,
    *,
    mean_tol: float = 1e-10,
    max_iter: int = 200,
) -> LowSamplePathResult:
    """Fit equally spaced, positive-weight Fréchet centres by segment."""
    observations = np.asarray(observations, dtype=float)
    if observations.ndim < 3:
        raise ValueError("observations must be a stack of manifold points")
    time, target_times = _validate_times(time, target_times, observations.shape[0])
    if segments < 1:
        raise ValueError("segments must be positive")

    start = min(float(time.min()), float(target_times.min()))
    stop = max(float(time.max()), float(target_times.max()))
    if stop <= start:
        raise ValueError("the time domain must have positive length")
    edges = np.linspace(start, stop, segments + 1)
    training_bins = np.clip(np.searchsorted(edges, time, side="right") - 1, 0, segments - 1)
    target_bins = np.clip(
        np.searchsorted(edges, target_times, side="right") - 1, 0, segments - 1
    )

    centres = []
    counts = []
    iterations = []
    residuals = []
    for segment in range(segments):
        selected = observations[training_bins == segment]
        if selected.shape[0] == 0:
            raise ValueError(f"segment {segment} has no training observations")
        result = geometry.barycentre(selected, tol=mean_tol, max_iter=max_iter)
        if not result.converged:
            raise RuntimeError(f"segment {segment} Fréchet mean did not converge")
        centres.append(np.asarray(result.X))
        counts.append(int(selected.shape[0]))
        iterations.append(int(result.n_iter))
        residuals.append(float(result.residual))
    centres = np.stack(centres)
    return LowSamplePathResult(
        points=centres[target_bins],
        diagnostics={
            "segments": int(segments),
            "minimum_segment_count": int(min(counts)),
            "maximum_iterations": int(max(iterations)),
            "maximum_residual": float(max(residuals)),
        },
    )


def segmented_frechet_polygon(
    observations: Array,
    time: Array,
    target_times: Array,
    segments: int,
    geometry: GeometryOps,
    *,
    mean_tol: float = 1e-10,
    max_iter: int = 200,
) -> LowSamplePolygonResult:
    """Join positive equal-duration segment means by geodesic chords.

    This is the stable polygonal analogue of ``piecewise_frechet_path``.
    It estimates the same ``segments`` positive means, places them at segment
    midpoints, extends the endpoint regimes flat to the observed boundary,
    and evaluates the continuous geodesic polygon between them.  The frame is
    returned so downstream Log maps and parallel transport use the exact path
    that produced the reported centres.
    """
    observations = np.asarray(observations, dtype=float)
    if observations.ndim < 3:
        raise ValueError("observations must be a stack of manifold points")
    time, target_times = _validate_times(time, target_times, observations.shape[0])
    if segments < 2:
        raise ValueError("segments must be at least two")

    start = min(float(time.min()), float(target_times.min()))
    stop = max(float(time.max()), float(target_times.max()))
    if stop <= start:
        raise ValueError("the time domain must have positive length")
    edges = np.linspace(start, stop, segments + 1)
    midpoints = 0.5 * (edges[:-1] + edges[1:])
    bins = np.clip(np.searchsorted(edges, time, side="right") - 1, 0, segments - 1)

    centres = []
    counts = []
    iterations = []
    residuals = []
    for segment in range(segments):
        selected = observations[bins == segment]
        if selected.shape[0] == 0:
            raise ValueError(f"segment {segment} has no training observations")
        result = geometry.barycentre(selected, tol=mean_tol, max_iter=max_iter)
        if not result.converged:
            raise RuntimeError(f"segment {segment} Fréchet mean did not converge")
        centres.append(np.asarray(result.X))
        counts.append(int(selected.shape[0]))
        iterations.append(int(result.n_iter))
        residuals.append(float(result.residual))
    centres = np.stack(centres)
    vertex_times = np.concatenate(([start], midpoints, [stop]))
    vertices = np.concatenate((centres[:1], centres, centres[-1:]), axis=0)
    frame = PolygonalFrame(vertex_times, vertices, geometry)
    points = evaluate_polygon(frame, target_times).points
    return LowSamplePolygonResult(
        points=np.asarray(points),
        frame=frame,
        diagnostics={
            "segments": int(segments),
            "vertex_count": int(vertex_times.size),
            "minimum_segment_count": int(min(counts)),
            "maximum_iterations": int(max(iterations)),
            "maximum_residual": float(max(residuals)),
        },
    )


def graph_smoothed_polygon(
    vertex_times: Array,
    positive_vertices: Array,
    target_times: Array,
    strength: float,
    geometry: GeometryOps,
    *,
    mean_tol: float = 1e-10,
    max_iter: int = 200,
    smoothing_iterations: int = 12,
    smoothing_tol: float = 1e-8,
) -> LowSamplePathResult:
    """Smooth neighbouring positive vertices with positive BW barycentres.

    Each update balances the original local vertex (weight one) against its
    current graph neighbours (weight ``strength`` each).  No signed weights
    or tangent extrapolation are used.
    """
    vertex_times = np.asarray(vertex_times, dtype=float)
    vertices = np.asarray(positive_vertices, dtype=float)
    target_times = np.asarray(target_times, dtype=float)
    if vertices.shape[0] != vertex_times.size or vertex_times.size < 2:
        raise ValueError("vertex_times and positive_vertices are incompatible")
    if not np.isfinite(strength) or strength < 0.0:
        raise ValueError("strength must be finite and nonnegative")
    if smoothing_iterations < 1:
        raise ValueError("smoothing_iterations must be positive")

    original = vertices.copy()
    current = vertices.copy()
    converged = strength == 0.0
    maximum_update = 0.0
    iterations_used = 0
    for iteration in range(1, smoothing_iterations + 1):
        if strength == 0.0:
            break
        updated = []
        for index in range(vertex_times.size):
            points = [original[index]]
            weights = [1.0]
            if index > 0:
                points.append(current[index - 1])
                weights.append(strength)
            if index + 1 < vertex_times.size:
                points.append(current[index + 1])
                weights.append(strength)
            result = geometry.barycentre(
                np.stack(points),
                weights=np.asarray(weights),
                tol=mean_tol,
                max_iter=max_iter,
                X0=current[index],
            )
            if not result.converged:
                raise RuntimeError("graph-smoothed vertex mean did not converge")
            updated.append(np.asarray(result.X))
        updated = np.stack(updated)
        maximum_update = float(np.sqrt(np.max(geometry.dist2(current, updated))))
        current = updated
        iterations_used = iteration
        if maximum_update <= smoothing_tol:
            converged = True
            break

    frame = PolygonalFrame(vertex_times, current, geometry)
    points = evaluate_polygon(frame, target_times).points
    return LowSamplePathResult(
        points=np.asarray(points),
        diagnostics={
            "strength": float(strength),
            "smoothing_iterations": int(iterations_used),
            "smoothing_converged": bool(converged),
            "maximum_final_update": maximum_update,
        },
    )
