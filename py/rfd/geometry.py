from dataclasses import dataclass
from typing import Callable

import numpy as np

from rfd.spd.airm import (
    airm_barycentre,
    airm_dist2,
    airm_exp,
    airm_log,
    airm_inner,
    airm_parallel_transport,
    airm_random_tangent,
)
from rfd.spd.bw import (
    bw_barycentre,
    bw_dist2,
    bw_exp,
    bw_log,
    bw_inner,
    bw_parallel_transport,
    bw_random_tangent,
)
from rfd.sphere import (
    sphere_barycentre,
    sphere_dist2,
    sphere_exp,
    sphere_log,
    sphere_inner,
    sphere_parallel_transport,
    sphere_random_tangent,
)


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
