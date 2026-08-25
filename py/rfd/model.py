"""End-to-end fitting and reconstruction for Riemannian Factor Dynamics.

The component modules remain the mathematical sources of truth.  This module
only composes them into one observable fit while retaining every intermediate
object needed by theorem-driven diagnostics.
"""

from dataclasses import dataclass
from typing import Literal

import numpy as np

from rfd.estimators.centre import CentrePathEstimate, estimate_centre_path
from rfd.estimators.frame import regular_polygon_grid, transport_from_reference
from rfd.estimators.lag import (
    DynamicFactorFit,
    LagOperatorResult,
    LagRowResult,
    LagSpectrum,
    Normalization,
    RatioRankResult,
    TailMode,
    TangentRowResult,
    ThresholdRankResult,
    assemble_lag_operator,
    common_reference_tangent_rows,
    coordinate_tangents,
    decompose_lag_operator,
    extract_dynamic_factors,
    lag_cross_covariances,
    ridged_ratio_rank,
    threshold_rank,
)
from rfd.geometry import GeometryOps


Array = np.ndarray
RankMethod = Literal["fixed", "threshold", "ridged_ratio"]


@dataclass(frozen=True)
class FixedRankResult:
    """A user-declared rank, represented beside the data-driven selectors."""

    rank: int
    method: str = "fixed"


RankSelection = FixedRankResult | ThresholdRankResult | RatioRankResult


@dataclass(frozen=True)
class RFDConfig:
    """All finite-sample choices required by one RFD fit.

    The theory supplies rates for these quantities; a concrete experiment
    supplies their constants.  Nothing is inferred silently here.
    """

    bandwidth: float
    n_cells: int
    max_lag: int
    rank_method: RankMethod = "ridged_ratio"
    rank: int | None = None
    threshold: float | None = None
    ridge: float | None = None
    max_rank: int | None = None
    demean: bool = True
    tail_mode: TailMode = "common"
    normalization: Normalization = "row_size"
    overlap_fractions: tuple[float, float] = (1.0 / 3.0, 2.0 / 3.0)
    mean_tol: float | None = None
    mean_max_iter: int = 200

    def __post_init__(self) -> None:
        if not np.isfinite(self.bandwidth) or self.bandwidth <= 0.0:
            raise ValueError("bandwidth must be finite and positive")
        if not isinstance(self.n_cells, (int, np.integer)) or self.n_cells < 1:
            raise ValueError("n_cells must be a positive integer")
        if not isinstance(self.max_lag, (int, np.integer)) or self.max_lag < 1:
            raise ValueError("max_lag must be a positive integer")
        if self.rank_method not in ("fixed", "threshold", "ridged_ratio"):
            raise ValueError(
                "rank_method must be 'fixed', 'threshold', or 'ridged_ratio'"
            )
        if self.rank_method == "fixed" and self.rank is None:
            raise ValueError("rank is required when rank_method='fixed'")
        if self.rank_method == "threshold" and self.threshold is None:
            raise ValueError(
                "threshold is required when rank_method='threshold'"
            )
        if self.rank_method == "ridged_ratio" and self.ridge is None:
            raise ValueError("ridge is required when rank_method='ridged_ratio'")
        if self.rank is not None and (
            not isinstance(self.rank, (int, np.integer)) or self.rank < 0
        ):
            raise ValueError("rank must be a nonnegative integer")
        if self.threshold is not None and (
            not np.isfinite(self.threshold) or self.threshold <= 0.0
        ):
            raise ValueError("threshold must be finite and positive")
        if self.ridge is not None and (
            not np.isfinite(self.ridge) or self.ridge <= 0.0
        ):
            raise ValueError("ridge must be finite and positive")
        if self.max_rank is not None and (
            not isinstance(self.max_rank, (int, np.integer))
            or self.max_rank < 1
        ):
            raise ValueError("max_rank must be a positive integer")
        if self.tail_mode not in ("common", "available"):
            raise ValueError("tail_mode must be 'common' or 'available'")
        if self.normalization not in ("row_size", "pair_count"):
            raise ValueError(
                "normalization must be 'row_size' or 'pair_count'"
            )
        if (
            len(self.overlap_fractions) != 2
            or not np.isfinite(self.overlap_fractions).all()
            or not 0.0
            < self.overlap_fractions[0]
            < self.overlap_fractions[1]
            < 1.0
        ):
            raise ValueError(
                "overlap_fractions must be two increasing values inside (0, 1)"
            )
        if self.mean_tol is not None and (
            not np.isfinite(self.mean_tol) or self.mean_tol <= 0.0
        ):
            raise ValueError("mean_tol must be finite and positive")
        if (
            not isinstance(self.mean_max_iter, (int, np.integer))
            or self.mean_max_iter < 1
        ):
            raise ValueError("mean_max_iter must be a positive integer")


@dataclass(frozen=True)
class RFDFit:
    """A complete fitted RFD decomposition and its intrinsic reconstruction."""

    config: RFDConfig
    geometry: GeometryOps
    centre: CentrePathEstimate
    tangent_rows: TangentRowResult
    lag_row: LagRowResult
    lag_operator: LagOperatorResult
    spectrum: LagSpectrum
    rank_selection: RankSelection
    factors: DynamicFactorFit
    reconstructed_reference_vectors: Array
    reconstructed_local_vectors: Array
    reconstructed_observations: Array

    @property
    def rank(self) -> int:
        return self.factors.rank

    @property
    def loadings(self) -> Array:
        return self.factors.loadings

    @property
    def factor_scores(self) -> Array:
        return self.factors.factor_scores

    @property
    def residual_rows(self) -> Array:
        return self.factors.residual_rows


def fit_rfd(
    observations: Array,
    time: Array,
    geometry: GeometryOps,
    config: RFDConfig,
) -> RFDFit:
    """Fit the complete moving-centre RFD model and reconstruct the sample."""
    observations, time = _validate_sample(observations, time)
    _validate_config(config, sample_size=time.size)

    vertex_times = regular_polygon_grid(
        config.n_cells,
        start=float(time[0]),
        stop=float(time[-1]),
    )
    centre = estimate_centre_path(
        observations=observations,
        time=time,
        vertex_times=vertex_times,
        bandwidth=config.bandwidth,
        geometry=geometry,
        overlap_fractions=config.overlap_fractions,
        mean_tol=config.mean_tol,
        max_iter=config.mean_max_iter,
    )
    tangent_rows = common_reference_tangent_rows(
        observations,
        time,
        centre.polygon,
    )
    lag_row = lag_cross_covariances(
        tangent_rows,
        config.max_lag,
        demean=config.demean,
        tail_mode=config.tail_mode,
        normalization=config.normalization,
    )
    lag_operator = assemble_lag_operator(lag_row)
    spectrum = decompose_lag_operator(lag_operator)
    rank_selection = _select_rank(spectrum, config)
    factors = extract_dynamic_factors(spectrum, rank_selection.rank)

    reconstructed_reference_vectors = coordinate_tangents(
        factors.reconstructed_rows,
        tangent_rows.basis,
    )
    reconstructed_local_vectors = transport_from_reference(
        centre.polygon,
        reconstructed_reference_vectors,
        time,
    )
    reconstructed_observations = geometry.exp(
        tangent_rows.local_centres,
        reconstructed_local_vectors,
    )
    if reconstructed_observations.shape != observations.shape:
        raise RuntimeError("geometry produced an invalid reconstruction shape")
    if not np.isfinite(reconstructed_observations).all():
        raise FloatingPointError("RFD reconstruction contains NaN or Inf")

    return RFDFit(
        config=config,
        geometry=geometry,
        centre=centre,
        tangent_rows=tangent_rows,
        lag_row=lag_row,
        lag_operator=lag_operator,
        spectrum=spectrum,
        rank_selection=rank_selection,
        factors=factors,
        reconstructed_reference_vectors=reconstructed_reference_vectors,
        reconstructed_local_vectors=reconstructed_local_vectors,
        reconstructed_observations=reconstructed_observations,
    )


def _select_rank(spectrum: LagSpectrum, config: RFDConfig) -> RankSelection:
    dimension = spectrum.eigenvalues.size
    if config.rank_method == "fixed":
        if config.rank is None:
            raise ValueError("rank is required when rank_method='fixed'")
        if not isinstance(config.rank, (int, np.integer)):
            raise ValueError("rank must be an integer")
        if config.rank < 0 or config.rank > dimension:
            raise ValueError("rank must lie between zero and tangent dimension")
        return FixedRankResult(rank=int(config.rank))
    if config.rank_method == "threshold":
        if config.threshold is None:
            raise ValueError(
                "threshold is required when rank_method='threshold'"
            )
        return threshold_rank(
            spectrum.eigenvalues,
            config.threshold,
            max_rank=config.max_rank,
        )
    if config.rank_method == "ridged_ratio":
        if config.ridge is None:
            raise ValueError("ridge is required when rank_method='ridged_ratio'")
        return ridged_ratio_rank(
            spectrum.eigenvalues,
            config.ridge,
            max_rank=config.max_rank,
        )
    raise ValueError(
        "rank_method must be 'fixed', 'threshold', or 'ridged_ratio'"
    )


def _validate_sample(observations: Array, time: Array) -> tuple[Array, Array]:
    observations = np.asarray(observations, dtype=float)
    time = np.asarray(time, dtype=float)
    if time.ndim != 1 or time.size < 2:
        raise ValueError("time must be a one-dimensional array of length at least two")
    if observations.ndim < 2 or observations.shape[0] != time.size:
        raise ValueError("observations and time must have matching sample axes")
    if not np.isfinite(observations).all() or not np.isfinite(time).all():
        raise ValueError("observations and time must be finite")
    if np.any(np.diff(time) <= 0.0):
        raise ValueError("time must be strictly increasing")
    return observations, time


def _validate_config(config: RFDConfig, *, sample_size: int) -> None:
    if not isinstance(config, RFDConfig):
        raise TypeError("config must be an RFDConfig")
    if not np.isfinite(config.bandwidth) or config.bandwidth <= 0.0:
        raise ValueError("bandwidth must be finite and positive")
    if not isinstance(config.n_cells, (int, np.integer)) or config.n_cells < 1:
        raise ValueError("n_cells must be a positive integer")
    if (
        not isinstance(config.max_lag, (int, np.integer))
        or config.max_lag < 1
        or config.max_lag >= sample_size
    ):
        raise ValueError("max_lag must lie between one and sample size minus one")
    if (
        not isinstance(config.mean_max_iter, (int, np.integer))
        or config.mean_max_iter < 1
    ):
        raise ValueError("mean_max_iter must be a positive integer")
