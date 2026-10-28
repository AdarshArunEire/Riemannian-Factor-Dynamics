"""Manifold operations used by the model: the sphere and the geometry interface."""

from dataclasses import dataclass
from typing import Callable, NamedTuple

import numpy as np

from rfd._maths.spd import airm_barycentre, airm_dist2, airm_exp, airm_inner, airm_log, airm_parallel_transport, airm_random_tangent, bw_barycentre, bw_dist2, bw_exp, bw_inner, bw_log, bw_parallel_transport, bw_random_tangent

# Geometry of the unit sphere used by the RFD simulation controls.
#
# Points and tangent vectors are ordinary arrays with trailing shape ``(d,)``.
# All operations support NumPy broadcasting over leading sample dimensions.
# The antipode is deliberately rejected by Log/transport because the connecting
# minimising geodesic is not unique there.

def _unit_points(X):
    X = np.asarray(X, dtype=float)
    norms = np.linalg.norm(X, axis=-1, keepdims=True)
    if np.any(norms == 0.0):
        raise ValueError("sphere point cannot be the zero vector")
    return X / norms


def sphere_inner(A, U, V):
    """Euclidean inner product restricted to the tangent plane at ``A``."""
    return np.sum(np.asarray(U) * np.asarray(V), axis=-1)


def sphere_dist2(A, B):
    """Squared great-circle distance on the unit sphere."""
    A, B = _unit_points(A), _unit_points(B)
    cosine = np.sum(A * B, axis=-1)
    return np.arccos(np.clip(cosine, -1.0, 1.0)) ** 2


def sphere_exp(A, V, strict=True):
    """Riemannian exponential on the unit sphere."""
    A, V = _unit_points(A), np.asarray(V, dtype=float)
    tangency = np.sum(A * V, axis=-1)
    if strict and np.any(np.abs(tangency) > 1e-9 * (1.0 + np.linalg.norm(V, axis=-1))):
        raise ValueError("V is not tangent at A")

    norm = np.linalg.norm(V, axis=-1, keepdims=True)
    coefficient = np.divide(
        np.sin(norm),
        norm,
        out=np.ones_like(norm),
        where=norm > 0.0,
    )
    point = np.cos(norm) * A + coefficient * V
    return _unit_points(point)


def sphere_log(A, B, strict=True):
    """Riemannian logarithm on the unique non-antipodal branch."""
    A, B = _unit_points(A), _unit_points(B)
    cosine = np.clip(np.sum(A * B, axis=-1, keepdims=True), -1.0, 1.0)
    if strict and np.any(cosine <= -1.0 + 1e-10):
        raise ValueError("sphere logarithm is non-unique at the antipode")
    angle = np.arccos(cosine)
    direction = B - cosine * A
    norm = np.linalg.norm(direction, axis=-1, keepdims=True)
    return np.divide(
        angle * direction,
        norm,
        out=np.zeros_like(direction),
        where=norm > 1e-15,
    )


def sphere_parallel_transport(V, A, B, strict=True):
    """Parallel transport along the unique short great-circle arc."""
    A, B, V = _unit_points(A), _unit_points(B), np.asarray(V, dtype=float)
    tangency = np.sum(A * V, axis=-1)
    if strict and np.any(np.abs(tangency) > 1e-9 * (1.0 + np.linalg.norm(V, axis=-1))):
        raise ValueError("V is not tangent at A")

    cosine = np.sum(A * B, axis=-1, keepdims=True)
    denominator = 1.0 + cosine
    if strict and np.any(denominator <= 1e-10):
        raise ValueError("sphere transport is non-unique at the antipode")

    transported = V - (
        np.sum(V * B, axis=-1, keepdims=True) / denominator
    ) * (A + B)
    # Clear the final few ulps in the normal direction without changing the
    # mathematical map.
    return transported - np.sum(transported * B, axis=-1, keepdims=True) * B


def sphere_random_tangent(rng, A, count=1, structure="dense"):
    """Draw unnormalised tangent vectors at one sphere point."""
    if structure != "dense":
        raise ValueError("sphere tangent structure must be 'dense'")
    A = _unit_points(A)
    if A.ndim != 1:
        raise ValueError("A must be one sphere point")
    if count < 0:
        raise ValueError("count must be nonnegative")
    raw = rng.standard_normal((count, A.shape[0]))
    return raw - np.sum(raw * A, axis=-1, keepdims=True) * A


class SphereMeanResult(NamedTuple):
    """Weighted spherical Karcher-mean result and convergence diagnostics."""

    X: np.ndarray
    n_iter: int
    residual: float
    converged: bool


def sphere_barycentre(
    S,
    weights=None,
    tol=1e-11,
    max_iter=200,
    step=1.0,
    X0=None,
    strict=True,
):
    """Weighted Karcher mean of points contained in one open hemisphere.

    The local centre estimator supplies positive kernel weights and operates
    inside a controlled normal neighbourhood. Globally, a spherical mean can
    be non-unique; a vanishing weighted Euclidean initializer therefore raises
    instead of pretending to select a canonical answer.

    ``weights=None`` gives equal weights. Supplied weights are normalized, so
    only their relative sizes matter.
    """
    S = np.asarray(S, dtype=float)
    if S.ndim != 2 or S.shape[0] == 0:
        raise ValueError("S must contain at least one sphere point")
    S = _unit_points(S)

    if weights is None:
        weights = np.full(S.shape[0], 1.0 / S.shape[0])
    else:
        weights = np.asarray(weights, dtype=float)
        if weights.shape != (S.shape[0],):
            raise ValueError(f"weights must have shape ({S.shape[0]},)")
        if not np.isfinite(weights).all():
            raise ValueError("weights contain NaN or Inf")
        if np.any(weights < 0.0):
            raise ValueError("weights must be nonnegative")
        total = weights.sum()
        if total <= 0.0:
            raise ValueError("weights must have positive total mass")
        weights = weights / total

    if X0 is None:
        initializer = np.tensordot(weights, S, axes=(0, 0))
        initializer_norm = np.linalg.norm(initializer)
        if initializer_norm <= 1e-12:
            raise ValueError("weighted sphere mean has no stable hemisphere initializer")
        X = initializer / initializer_norm
    else:
        X = _unit_points(np.asarray(X0, dtype=float))

    residual = np.inf
    for n_iter in range(1, max_iter + 1):
        logs = sphere_log(X, S, strict=strict)
        gradient = np.tensordot(weights, logs, axes=(0, 0))
        residual = np.linalg.norm(gradient)
        if residual < tol:
            return SphereMeanResult(X, n_iter, float(residual), True)
        X = sphere_exp(X, step * gradient, strict=strict)

    return SphereMeanResult(X, max_iter, float(residual), False)


@dataclass(frozen=True)
class GeometryOps:
    name: str
    exp: Callable
    log: Callable
    barycentre: Callable
    transport: Callable
    dist2: Callable
    inner: Callable
    random_tangent: Callable
    tangent_basis: Callable


def _symmetric_tangent_candidates(point):
    """Canonical Frobenius basis of the ambient symmetric-matrix space."""
    point = np.asarray(point, dtype=float)
    if point.ndim != 2 or point.shape[0] != point.shape[1]:
        raise ValueError("SPD tangent basis requires one square matrix")

    m = point.shape[0]
    candidates = []
    for row in range(m):
        diagonal = np.zeros((m, m))
        diagonal[row, row] = 1.0
        candidates.append(diagonal)
    for row in range(m):
        for column in range(row + 1, m):
            off_diagonal = np.zeros((m, m))
            off_diagonal[row, column] = 1.0 / np.sqrt(2.0)
            off_diagonal[column, row] = 1.0 / np.sqrt(2.0)
            candidates.append(off_diagonal)
    return np.stack(candidates)


def _sphere_tangent_candidates(point):
    """Projected ambient axes spanning the tangent plane of one sphere."""
    point = np.asarray(point, dtype=float)
    if point.ndim != 1:
        raise ValueError("sphere tangent basis requires one point")
    norm = np.linalg.norm(point)
    if not np.isfinite(norm) or norm <= 1e-15:
        raise ValueError("sphere point must be finite and nonzero")
    unit = point / norm
    return np.eye(unit.size) - np.outer(unit, unit)


def _orthonormal_tangent_basis(point, candidates, inner):
    """Turn a spanning family into an intrinsic orthonormal tangent basis."""
    candidates = np.asarray(candidates, dtype=float)
    gram = inner(
        point,
        candidates[:, None, ...],
        candidates[None, ...],
    )
    gram = 0.5 * (gram + gram.T)
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    largest = float(np.max(eigenvalues))
    if not np.isfinite(largest) or largest <= 0.0:
        raise ValueError("tangent metric is not positive on the candidates")

    keep = eigenvalues > 1e-12 * largest
    transform = (
        eigenvectors[:, keep]
        / np.sqrt(eigenvalues[keep])[None, :]
    )
    basis = np.tensordot(transform.T, candidates, axes=(1, 0))

    check = inner(point, basis[:, None, ...], basis[None, ...])
    if not np.allclose(check, np.eye(basis.shape[0]), rtol=2e-10, atol=2e-11):
        raise FloatingPointError("failed to construct an orthonormal tangent basis")
    return basis


def _airm_tangent_basis(point):
    return _orthonormal_tangent_basis(
        point,
        _symmetric_tangent_candidates(point),
        airm_inner,
    )


def _bw_tangent_basis(point):
    return _orthonormal_tangent_basis(
        point,
        _symmetric_tangent_candidates(point),
        bw_inner,
    )


def _sphere_tangent_basis(point):
    return _orthonormal_tangent_basis(
        point,
        _sphere_tangent_candidates(point),
        sphere_inner,
    )


AIRM_GEOMETRY = GeometryOps(
    name="airm",
    exp=airm_exp,
    log=airm_log,
    barycentre=airm_barycentre,
    transport=airm_parallel_transport,
    dist2=airm_dist2,
    inner=airm_inner,
    random_tangent=airm_random_tangent,
    tangent_basis=_airm_tangent_basis,
)

BW_GEOMETRY = GeometryOps(
    name="bw",
    exp=bw_exp,
    log=bw_log,
    barycentre=bw_barycentre,
    transport=bw_parallel_transport,
    dist2=bw_dist2,
    inner=bw_inner,
    random_tangent=bw_random_tangent,
    tangent_basis=_bw_tangent_basis,
)

SPHERE_GEOMETRY = GeometryOps(
    name="sphere",
    exp=sphere_exp,
    log=sphere_log,
    barycentre=sphere_barycentre,
    transport=sphere_parallel_transport,
    dist2=sphere_dist2,
    inner=sphere_inner,
    random_tangent=sphere_random_tangent,
    tangent_basis=_sphere_tangent_basis,
)
