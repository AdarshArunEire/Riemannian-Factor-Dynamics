"""Polygonal centre paths and their derivative-free transported frames.

B4.3 replaces a derivative estimate of the moving centre by a finite chain:
join estimated centre vertices with geodesic chords and compose ordinary
parallel transports along those chords. The result gives every local tangent
vector a reversible route to one common reference fibre.
"""

from dataclasses import dataclass

import numpy as np

from rfd.geometry import GeometryOps


Array = np.ndarray


@dataclass(frozen=True)
class PolygonEvaluation:
    """Points on a polygon together with their containing cells."""

    points: Array
    cell_indices: Array
    fractions: Array


@dataclass(frozen=True)
class PolygonalFrame:
    """A piecewise-geodesic centre path with a declared reference vertex."""

    vertex_times: Array
    vertices: Array
    geometry: GeometryOps

    def __post_init__(self) -> None:
        vertex_times = np.asarray(self.vertex_times, dtype=float)
        vertices = np.asarray(self.vertices, dtype=float)

        if vertex_times.ndim != 1 or vertex_times.size < 2:
            raise ValueError("vertex_times must contain at least two times")
        if not np.isfinite(vertex_times).all():
            raise ValueError("vertex_times contain NaN or Inf")
        if np.any(np.diff(vertex_times) <= 0.0):
            raise ValueError("vertex_times must be strictly increasing")
        if vertices.ndim < 2 or vertices.shape[0] != vertex_times.size:
            raise ValueError(
                "vertices must have one point for every vertex time"
            )
        if not np.isfinite(vertices).all():
            raise ValueError("vertices contain NaN or Inf")

        # Own immutable copies: mutating a caller's input later must not alter
        # the path whose transports are being interpreted.
        vertex_times = vertex_times.copy()
        vertices = vertices.copy()
        vertex_times.flags.writeable = False
        vertices.flags.writeable = False
        object.__setattr__(self, "vertex_times", vertex_times)
        object.__setattr__(self, "vertices", vertices)

    @property
    def n_cells(self) -> int:
        return self.vertex_times.size - 1

    @property
    def reference_point(self) -> Array:
        return self.vertices[0]


def polygon_cell_count(
    centre_rate: float,
    *,
    constant: float = 1.0,
    minimum: int = 1,
) -> int:
    """Choose ceil(constant * centre_rate**(-2/3)) polygon cells."""
    if not np.isfinite(centre_rate) or centre_rate <= 0.0:
        raise ValueError("centre_rate must be finite and positive")
    if not np.isfinite(constant) or constant <= 0.0:
        raise ValueError("constant must be finite and positive")
    if not isinstance(minimum, (int, np.integer)) or minimum < 1:
        raise ValueError("minimum must be a positive integer")
    return max(int(minimum), int(np.ceil(constant * centre_rate ** (-2.0 / 3.0))))


def regular_polygon_grid(
    n_cells: int,
    *,
    start: float = 0.0,
    stop: float = 1.0,
) -> Array:
    """Return the n_cells + 1 deterministic vertex times."""
    if not isinstance(n_cells, (int, np.integer)) or n_cells < 1:
        raise ValueError("n_cells must be a positive integer")
    if not np.isfinite(start) or not np.isfinite(stop) or stop <= start:
        raise ValueError("start and stop must be finite with stop > start")
    return np.linspace(start, stop, int(n_cells) + 1)


def evaluate_polygon(
    frame: PolygonalFrame,
    target_times: Array,
) -> PolygonEvaluation:
    """Evaluate the piecewise-geodesic centre path at requested times."""
    target_times = np.asarray(target_times, dtype=float)
    if target_times.ndim != 1 or target_times.size == 0:
        raise ValueError("target_times must be a nonempty one-dimensional array")
    if not np.isfinite(target_times).all():
        raise ValueError("target_times contain NaN or Inf")

    lower = frame.vertex_times[0]
    upper = frame.vertex_times[-1]
    if np.any(target_times < lower) or np.any(target_times > upper):
        raise ValueError("target_times must lie inside the polygon time range")

    cells = np.searchsorted(frame.vertex_times, target_times, side="right") - 1
    cells = np.clip(cells, 0, frame.n_cells - 1)
    left_times = frame.vertex_times[cells]
    right_times = frame.vertex_times[cells + 1]
    fractions = (target_times - left_times) / (right_times - left_times)

    points = []
    for cell, fraction in zip(cells, fractions):
        left = frame.vertices[cell]
        if fraction == 0.0:
            point = left
        elif fraction == 1.0:
            point = frame.vertices[cell + 1]
        else:
            chord = frame.geometry.log(left, frame.vertices[cell + 1])
            point = frame.geometry.exp(left, fraction * chord)
        points.append(point)

    return PolygonEvaluation(
        points=np.stack(points),
        cell_indices=cells,
        fractions=fractions,
    )


def propagate_vertex_frame(
    frame: PolygonalFrame,
    initial_vectors: Array,
) -> Array:
    """Transport one vector or a vector frame through every polygon chord."""
    initial_vectors = _validate_tangent_shape(
        initial_vectors,
        frame.vertices.shape[1:],
        name="initial_vectors",
    )
    transported = [initial_vectors]
    current = initial_vectors
    for left, right in zip(frame.vertices[:-1], frame.vertices[1:]):
        current = frame.geometry.transport(current, left, right)
        transported.append(current)
    return np.stack(transported)


def transport_from_reference(
    frame: PolygonalFrame,
    reference_vectors: Array,
    target_times: Array,
) -> Array:
    """Transport paired vectors from the first vertex to polygon points.

    reference_vectors[i] is transported to target_times[i]. Each item may
    itself be a stack of vectors, which lets a complete basis travel without
    requiring another geometry-specific implementation.
    """
    target_times = _validate_target_times(target_times)
    reference_vectors = _validate_paired_vectors(
        reference_vectors,
        target_times.size,
        frame.vertices.shape[1:],
        name="reference_vectors",
    )
    evaluation = evaluate_polygon(frame, target_times)

    result = []
    for vector, cell, point in zip(
        reference_vectors,
        evaluation.cell_indices,
        evaluation.points,
    ):
        current = vector
        for step in range(int(cell)):
            current = frame.geometry.transport(
                current,
                frame.vertices[step],
                frame.vertices[step + 1],
            )
        current = frame.geometry.transport(
            current,
            frame.vertices[cell],
            point,
        )
        result.append(current)
    return np.stack(result)


def transport_to_reference(
    frame: PolygonalFrame,
    local_vectors: Array,
    source_times: Array,
) -> Array:
    """Transport paired local vectors backwards to the first vertex."""
    source_times = _validate_target_times(source_times, name="source_times")
    local_vectors = _validate_paired_vectors(
        local_vectors,
        source_times.size,
        frame.vertices.shape[1:],
        name="local_vectors",
    )
    evaluation = evaluate_polygon(frame, source_times)

    result = []
    for vector, cell, point in zip(
        local_vectors,
        evaluation.cell_indices,
        evaluation.points,
    ):
        current = frame.geometry.transport(
            vector,
            point,
            frame.vertices[cell],
        )
        for step in range(int(cell), 0, -1):
            current = frame.geometry.transport(
                current,
                frame.vertices[step],
                frame.vertices[step - 1],
            )
        result.append(current)
    return np.stack(result)


def _validate_target_times(target_times: Array, *, name: str = "target_times") -> Array:
    target_times = np.asarray(target_times, dtype=float)
    if target_times.ndim != 1 or target_times.size == 0:
        raise ValueError(f"{name} must be a nonempty one-dimensional array")
    if not np.isfinite(target_times).all():
        raise ValueError(f"{name} contain NaN or Inf")
    return target_times


def _validate_tangent_shape(
    vectors: Array,
    point_shape: tuple[int, ...],
    *,
    name: str,
) -> Array:
    vectors = np.asarray(vectors, dtype=float)
    if vectors.ndim < len(point_shape):
        raise ValueError(f"{name} do not have the geometry's tangent shape")
    if vectors.shape[-len(point_shape) :] != point_shape:
        raise ValueError(f"{name} do not match the geometry's point shape")
    if not np.isfinite(vectors).all():
        raise ValueError(f"{name} contain NaN or Inf")
    return vectors


def _validate_paired_vectors(
    vectors: Array,
    count: int,
    point_shape: tuple[int, ...],
    *,
    name: str,
) -> Array:
    vectors = _validate_tangent_shape(vectors, point_shape, name=name)
    if vectors.ndim == len(point_shape) or vectors.shape[0] != count:
        raise ValueError(f"{name} must have one leading item per time")
    return vectors
