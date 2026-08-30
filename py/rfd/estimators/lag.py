"""Lag-operator estimation for common-reference RFD tangent rows.

This first B4.4 layer performs only the geometric-to-linear transition. It
logs each observation at its polygonal centre, transports that tangent vector
back to the first polygon vertex, and expresses it in an intrinsic
orthonormal basis. Lag products and spectral selection are added in the next
layers.
"""

from dataclasses import dataclass
from typing import Literal

import numpy as np

from rfd.estimators.frame import (
    PolygonalFrame,
    evaluate_polygon,
    transport_to_reference,
)
from rfd.geometry import GeometryOps


Array = np.ndarray
TailMode = Literal["common", "available"]
Normalization = Literal["row_size", "pair_count"]


@dataclass(frozen=True)
class TangentRowResult:
    """Observable tangent rows and the geometry needed to interpret them."""

    rows: Array
    reference_vectors: Array
    local_vectors: Array
    local_centres: Array
    basis: Array
    time: Array

    @property
    def tangent_dimension(self) -> int:
        return self.rows.shape[1]


@dataclass(frozen=True)
class LagRowResult:
    """The complete row of empirical lag cross-covariance matrices."""

    covariances: Array
    lags: Array
    centred_rows: Array
    row_mean: Array
    pair_counts: Array
    divisors: Array
    tail_mode: TailMode
    normalization: Normalization

    @property
    def stacked(self) -> Array:
        """Horizontal row operator [Gamma(1) ... Gamma(h_0)]."""
        return np.concatenate(tuple(self.covariances), axis=1)


@dataclass(frozen=True)
class LagOperatorResult:
    """Positive-semidefinite square of one empirical lag row."""

    matrix: Array
    stacked_row: Array
    lag_row: LagRowResult


@dataclass(frozen=True)
class LagSpectrum:
    """Descending spectrum and loading directions of the lag operator."""

    eigenvalues: Array
    eigenvectors: Array
    singular_values: Array
    lag_operator: LagOperatorResult


@dataclass(frozen=True)
class DynamicFactorFit:
    """Rank-r projection of the common-reference tangent rows."""

    rank: int
    loadings: Array
    factor_scores: Array
    fitted_centred_rows: Array
    residual_rows: Array
    reconstructed_rows: Array
    row_mean: Array
    spectrum: LagSpectrum


@dataclass(frozen=True)
class ThresholdRankResult:
    """Factor count obtained by thresholding lag-operator eigenvalues."""

    rank: int
    threshold: float
    considered_eigenvalues: Array


@dataclass(frozen=True)
class RatioRankResult:
    """Factor count and complete consecutive-ratio diagnostic."""

    rank: int
    candidate_ranks: Array
    ratios: Array
    ridge: float
    method: str


def tangent_coordinates(
    vectors: Array,
    point: Array,
    basis: Array,
    geometry: GeometryOps,
    *,
    batch_size: int = 64,
) -> Array:
    """Coordinates of tangent vectors in an intrinsic orthonormal basis.

    Coordinate rows are independent. Evaluate them in bounded sample batches
    so an ``n x p x m x m`` broadcast is never materialised for long SPD
    panels. Batching changes only workspace size, not the estimator.
    """
    vectors = np.asarray(vectors, dtype=float)
    basis = np.asarray(basis, dtype=float)
    point_shape = np.asarray(point).shape
    if vectors.shape[-len(point_shape) :] != point_shape:
        raise ValueError("vectors do not match the reference point shape")
    if basis.ndim != len(point_shape) + 1 or basis.shape[1:] != point_shape:
        raise ValueError("basis must contain tangent vectors at the point")
    if not np.isfinite(vectors).all() or not np.isfinite(basis).all():
        raise ValueError("vectors and basis must be finite")
    if not isinstance(batch_size, (int, np.integer)) or batch_size < 1:
        raise ValueError("batch_size must be a positive integer")

    vector_leading = vectors.shape[: -len(point_shape)]
    if not vector_leading:
        return geometry.inner(point, vectors, basis)

    flat_vectors = vectors.reshape((-1,) + point_shape)
    rows = np.empty((flat_vectors.shape[0], basis.shape[0]), dtype=float)
    expanded_basis = basis[None]
    for start in range(0, flat_vectors.shape[0], int(batch_size)):
        stop = min(start + int(batch_size), flat_vectors.shape[0])
        rows[start:stop] = geometry.inner(
            point,
            flat_vectors[start:stop, None],
            expanded_basis,
        )
    return rows.reshape(vector_leading + (basis.shape[0],))


def coordinate_tangents(rows: Array, basis: Array) -> Array:
    """Reconstruct tangent vectors from orthonormal coordinates."""
    rows = np.asarray(rows, dtype=float)
    basis = np.asarray(basis, dtype=float)
    if rows.ndim < 1 or basis.ndim < 2:
        raise ValueError("rows and basis must have coordinate axes")
    if rows.shape[-1] != basis.shape[0]:
        raise ValueError("row width must equal the basis size")
    if not np.isfinite(rows).all() or not np.isfinite(basis).all():
        raise ValueError("rows and basis must be finite")
    return np.tensordot(rows, basis, axes=(-1, 0))


def common_reference_tangent_rows(
    observations: Array,
    time: Array,
    frame: PolygonalFrame,
) -> TangentRowResult:
    """Map manifold observations to metric-correct common-reference rows."""
    observations = np.asarray(observations, dtype=float)
    time = np.asarray(time, dtype=float)
    point_shape = frame.vertices.shape[1:]

    if time.ndim != 1 or time.size == 0:
        raise ValueError("time must be a nonempty one-dimensional array")
    if observations.ndim != len(point_shape) + 1:
        raise ValueError("observations must have one leading sample axis")
    if observations.shape[0] != time.size:
        raise ValueError("observations and time must have matching lengths")
    if observations.shape[1:] != point_shape:
        raise ValueError("observations do not match the polygon point shape")
    if not np.isfinite(observations).all() or not np.isfinite(time).all():
        raise ValueError("observations and time must be finite")

    evaluation = evaluate_polygon(frame, time)
    local_vectors = frame.geometry.log(evaluation.points, observations)
    reference_vectors = transport_to_reference(frame, local_vectors, time)
    basis = frame.geometry.tangent_basis(frame.reference_point)
    rows = tangent_coordinates(
        reference_vectors,
        frame.reference_point,
        basis,
        frame.geometry,
    )

    if rows.shape != (time.size, basis.shape[0]):
        raise RuntimeError("geometry produced an invalid tangent-row shape")
    if not np.isfinite(rows).all():
        raise FloatingPointError("common-reference tangent rows are nonfinite")

    return TangentRowResult(
        rows=rows,
        reference_vectors=reference_vectors,
        local_vectors=local_vectors,
        local_centres=evaluation.points,
        basis=basis,
        time=time.copy(),
    )


def lag_cross_covariances(
    rows: Array | TangentRowResult,
    max_lag: int,
    *,
    demean: bool = True,
    tail_mode: TailMode = "common",
    normalization: Normalization = "row_size",
) -> LagRowResult:
    """Estimate Gamma(h) with an explicit tail and denominator convention.

    The orientation is current outer past:

        Gamma(h) = divisor^(-1) sum_t z_t z_(t-h)^T.

    Parent parity uses one common tail beginning at max_lag and divides every
    lag sum by the full row count n. The pair-count option implements the
    finite-array normalization used in the proof dossiers.
    """
    if isinstance(rows, TangentRowResult):
        rows = rows.rows
    rows = np.asarray(rows, dtype=float)
    if rows.ndim != 2 or rows.shape[0] < 2 or rows.shape[1] < 1:
        raise ValueError("rows must be a two-dimensional n by p array")
    if not np.isfinite(rows).all():
        raise ValueError("rows contain NaN or Inf")
    if not isinstance(max_lag, (int, np.integer)):
        raise ValueError("max_lag must be an integer")

    n = rows.shape[0]
    if max_lag < 1 or max_lag >= n:
        raise ValueError("max_lag must lie between 1 and n - 1")
    if tail_mode not in ("common", "available"):
        raise ValueError("tail_mode must be 'common' or 'available'")
    if normalization not in ("row_size", "pair_count"):
        raise ValueError("normalization must be 'row_size' or 'pair_count'")

    row_mean = rows.mean(axis=0) if demean else np.zeros(rows.shape[1])
    centred = rows - row_mean
    lags = np.arange(1, max_lag + 1)
    covariances = []
    pair_counts = []
    divisors = []

    for lag in lags:
        start = max_lag if tail_mode == "common" else int(lag)
        current = centred[start:]
        past = centred[start - lag : n - lag]
        pair_count = current.shape[0]
        divisor = n if normalization == "row_size" else pair_count

        covariances.append((current.T @ past) / divisor)
        pair_counts.append(pair_count)
        divisors.append(divisor)

    return LagRowResult(
        covariances=np.stack(covariances),
        lags=lags,
        centred_rows=centred,
        row_mean=row_mean,
        pair_counts=np.asarray(pair_counts),
        divisors=np.asarray(divisors),
        tail_mode=tail_mode,
        normalization=normalization,
    )


def assemble_lag_operator(lag_row: LagRowResult) -> LagOperatorResult:
    """Form L = G G^T = sum_h Gamma(h) Gamma(h)^T."""
    if not isinstance(lag_row, LagRowResult):
        raise TypeError("lag_row must be a LagRowResult")
    stacked = lag_row.stacked
    matrix = stacked @ stacked.T
    matrix = 0.5 * (matrix + matrix.T)
    return LagOperatorResult(
        matrix=matrix,
        stacked_row=stacked,
        lag_row=lag_row,
    )


def decompose_lag_operator(lag_operator: LagOperatorResult) -> LagSpectrum:
    """Recover loading directions through the lag row's singular vectors.

    Using the SVD of G rather than an eigendecomposition of G G^T produces
    the same ordered eigenvectors and eigenvalues, while preserving exact
    nonnegativity of the reported spectrum at floating-point precision.
    """
    if not isinstance(lag_operator, LagOperatorResult):
        raise TypeError("lag_operator must be a LagOperatorResult")
    eigenvectors, singular_values, _ = np.linalg.svd(
        lag_operator.stacked_row,
        full_matrices=True,
    )
    eigenvalues = singular_values**2
    if eigenvalues.size < eigenvectors.shape[1]:
        eigenvalues = np.pad(
            eigenvalues,
            (0, eigenvectors.shape[1] - eigenvalues.size),
        )
    return LagSpectrum(
        eigenvalues=eigenvalues,
        eigenvectors=eigenvectors,
        singular_values=singular_values,
        lag_operator=lag_operator,
    )


def extract_dynamic_factors(
    spectrum: LagSpectrum,
    rank: int,
) -> DynamicFactorFit:
    """Project centred tangent rows onto the requested leading lag space."""
    if not isinstance(spectrum, LagSpectrum):
        raise TypeError("spectrum must be a LagSpectrum")
    if not isinstance(rank, (int, np.integer)):
        raise ValueError("rank must be an integer")
    dimension = spectrum.eigenvectors.shape[0]
    if rank < 0 or rank > dimension:
        raise ValueError("rank must lie between zero and the tangent dimension")

    centred_rows = spectrum.lag_operator.lag_row.centred_rows
    row_mean = spectrum.lag_operator.lag_row.row_mean
    loadings = spectrum.eigenvectors[:, :rank]
    factor_scores = centred_rows @ loadings
    fitted_centred = factor_scores @ loadings.T
    residual = centred_rows - fitted_centred
    reconstructed = fitted_centred + row_mean

    return DynamicFactorFit(
        rank=int(rank),
        loadings=loadings,
        factor_scores=factor_scores,
        fitted_centred_rows=fitted_centred,
        residual_rows=residual,
        reconstructed_rows=reconstructed,
        row_mean=row_mean,
        spectrum=spectrum,
    )


def threshold_rank(
    eigenvalues: Array,
    threshold: float,
    *,
    max_rank: int | None = None,
) -> ThresholdRankResult:
    """Count eigenvalues above a positive declared threshold."""
    eigenvalues = _validate_eigenvalues(eigenvalues)
    if not np.isfinite(threshold) or threshold <= 0.0:
        raise ValueError("threshold must be finite and positive")
    cap = eigenvalues.size if max_rank is None else max_rank
    if not isinstance(cap, (int, np.integer)) or cap < 1 or cap > eigenvalues.size:
        raise ValueError("max_rank must lie between one and the spectrum size")
    considered = eigenvalues[:cap]
    return ThresholdRankResult(
        rank=int(np.count_nonzero(considered > threshold)),
        threshold=float(threshold),
        considered_eigenvalues=considered.copy(),
    )


def ridged_ratio_rank(
    eigenvalues: Array,
    ridge: float,
    *,
    max_rank: int | None = None,
) -> RatioRankResult:
    """Minimize (lambda_(j+1)+ridge)/(lambda_j+ridge)."""
    if not np.isfinite(ridge) or ridge <= 0.0:
        raise ValueError("ridge must be finite and positive")
    return _ratio_rank(
        eigenvalues,
        ridge=float(ridge),
        max_rank=max_rank,
        method="ridged_ratio",
    )


def raw_ratio_rank(
    eigenvalues: Array,
    *,
    max_rank: int | None = None,
) -> RatioRankResult:
    """Parent-style unregularized ratio, retained as a negative control.

    Ratios with a zero denominator are undefined and stored as NaN. Selection
    is over the remaining finite ratios with the smallest-index tie rule.
    """
    return _ratio_rank(
        eigenvalues,
        ridge=0.0,
        max_rank=max_rank,
        method="raw_ratio",
    )


def _validate_eigenvalues(eigenvalues: Array) -> Array:
    eigenvalues = np.asarray(eigenvalues, dtype=float)
    if eigenvalues.ndim != 1 or eigenvalues.size == 0:
        raise ValueError("eigenvalues must be a nonempty one-dimensional array")
    if not np.isfinite(eigenvalues).all():
        raise ValueError("eigenvalues contain NaN or Inf")
    if np.any(eigenvalues < 0.0):
        raise ValueError("eigenvalues must be nonnegative")
    if np.any(np.diff(eigenvalues) > 1e-12 * max(1.0, eigenvalues[0])):
        raise ValueError("eigenvalues must be sorted in nonincreasing order")
    return eigenvalues


def _ratio_rank(
    eigenvalues: Array,
    *,
    ridge: float,
    max_rank: int | None,
    method: str,
) -> RatioRankResult:
    eigenvalues = _validate_eigenvalues(eigenvalues)
    if eigenvalues.size < 2:
        raise ValueError("ratio selection requires at least two eigenvalues")
    cap = eigenvalues.size - 1 if max_rank is None else max_rank
    if not isinstance(cap, (int, np.integer)) or cap < 1 or cap >= eigenvalues.size:
        raise ValueError(
            "max_rank must leave one following eigenvalue for every ratio"
        )

    denominator = eigenvalues[:cap] + ridge
    numerator = eigenvalues[1 : cap + 1] + ridge
    ratios = np.divide(
        numerator,
        denominator,
        out=np.full(cap, np.nan),
        where=denominator > 0.0,
    )
    finite = np.isfinite(ratios)
    if not np.any(finite):
        raise ValueError("every candidate eigenvalue ratio is undefined")
    finite_indices = np.flatnonzero(finite)
    winner = finite_indices[np.argmin(ratios[finite])]
    candidates = np.arange(1, cap + 1)
    return RatioRankResult(
        rank=int(candidates[winner]),
        candidate_ranks=candidates,
        ratios=ratios,
        ridge=float(ridge),
        method=method,
    )
