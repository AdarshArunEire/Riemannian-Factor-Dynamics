"""Geometry of the unit sphere used by the RFD simulation controls.

Points and tangent vectors are ordinary arrays with trailing shape ``(d,)``.
All operations support NumPy broadcasting over leading sample dimensions.
The antipode is deliberately rejected by Log/transport because the connecting
minimising geodesic is not unique there.
"""

from typing import NamedTuple

import numpy as np


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
