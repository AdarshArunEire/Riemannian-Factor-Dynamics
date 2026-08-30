"""B4.5 / N-01 complete RFD factor-recovery experiment harness.

One task generates one bounded-energy moving-centre factor sample.  The same
sample is then fitted with two predeclared bandwidth rules:

``production``
    ``min(2.1, 0.95 * c_max(n))``, where the cap is fixed and therefore does
    not cancel bandwidth shrinkage asymptotically.

``reference``
    the completed rate-study multiplier 1.3.

The runner is serial, append-only and resumable.  Errors are rows, not deleted
replications.  It measures the complete chain from the centre through the lag
row and loading space to factor scores and intrinsic reconstruction.

Examples
--------
Inspect the recorded workload without writing::

    python experiments/run_end_to_end.py --profile factor_baseline --dry-run

Run the cheap integration smoke::

    python experiments/run_end_to_end.py --profile smoke

Run or resume the recorded baseline::

    python experiments/run_end_to_end.py --profile factor_baseline
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import shutil
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

for _thread_variable in (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ.setdefault(_thread_variable, "1")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))

from rfd.dgp.lsrfm import (  # noqa: E402
    AR1FactorConfig,
    CentrePathConfig,
    LSRFMConfig,
    LoadingConfig,
    NoiseConfig,
    generate_lsrfm,
)
from rfd.estimators.frame import evaluate_polygon, polygon_cell_count  # noqa: E402
from rfd.estimators.lag import (  # noqa: E402
    assemble_lag_operator,
    decompose_lag_operator,
    lag_cross_covariances,
    raw_ratio_rank,
    ridged_ratio_rank,
    tangent_coordinates,
    threshold_rank,
)
from rfd.geometry import AIRM_GEOMETRY, BW_GEOMETRY, GeometryOps  # noqa: E402
from rfd.model import RFDConfig, RFDFit, fit_rfd  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "end_to_end.yaml"
CONFIG_8192 = ROOT / "config" / "end_to_end_8192.yaml"
GEOMETRIES = {"airm": AIRM_GEOMETRY, "bw": BW_GEOMETRY}
VARIANTS = ("production", "reference")
RAW_COLUMNS = [
    "profile", "n", "matrix_size", "tangent_dimension", "replicate",
    "variant", "seed_spawn_key", "bandwidth_multiplier", "bandwidth",
    "n_cells", "status", "error_type", "error_message", "true_rank",
    "fixed_fit_rank", "threshold_rank", "ridged_ratio_rank", "raw_ratio_rank",
    "threshold", "centre_path_rms", "lag_row_error", "oracle_lag_row_size",
    "operator_error", "oracle_gap", "assembly_bound", "assembly_gap_ratio",
    "loading_subspace_error", "factor_score_nrmse", "null_eigenvalue",
    "null_bound_ratio", "observation_reconstruction_rms",
    "signal_reconstruction_rms", "row_residual_fraction", "empirical_energy_R",
    "centre_path_length", "centre_path_energy", "fallback_count",
    "fallback_rate", "minimum_effective_sample_size", "nonconverged_stages",
    "observation_min_eigenvalue", "observation_max_condition", "elapsed_seconds",
]


@dataclass(frozen=True)
class Task:
    n: int
    matrix_size: int
    replicate: int
    seed_sequence: np.random.SeedSequence


def cubic_profile(time_values: np.ndarray) -> np.ndarray:
    """The B4.2 smooth profile, retained so layers are compared coherently."""
    time_values = np.asarray(time_values, dtype=float)
    return time_values + 0.5 * time_values**3


def maximum_admissible_multiplier(
    n: int,
    *,
    bandwidth_constant: float,
    bandwidth_exponent: float,
    overlap_fractions: tuple[float, float],
) -> float:
    """Largest multiplier whose three scales fit the fixed boundary regions."""
    left, right = overlap_fractions
    boundary_width = min(left, 1.0 - right)
    return boundary_width / (bandwidth_constant * n ** (-bandwidth_exponent))


def production_multiplier(n: int, estimator: dict[str, Any]) -> float:
    """Predeclared clipped rule: small-sample feasibility plus a fixed cap."""
    maximum = maximum_admissible_multiplier(
        n,
        bandwidth_constant=float(estimator["bandwidth_constant"]),
        bandwidth_exponent=float(estimator["bandwidth_exponent"]),
        overlap_fractions=tuple(estimator["overlap_fractions"]),
    )
    return min(
        float(estimator["production_multiplier_cap"]),
        float(estimator["admissible_boundary_fraction"]) * maximum,
    )


def bandwidth_variants(n: int, estimator: dict[str, Any]) -> dict[str, float]:
    """Return the production and paired-reference multipliers for one n."""
    return {
        "production": production_multiplier(n, estimator),
        "reference": float(estimator["reference_multiplier"]),
    }


def load_configuration(path: Path, profile_name: str) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        source = yaml.safe_load(handle)
    if profile_name not in source.get("profiles", {}):
        raise ValueError(f"unknown profile: {profile_name}")
    resolved = {
        "profile_name": profile_name,
        "profile": dict(source["profiles"][profile_name]),
        "experiment": dict(source["experiment"]),
        "estimator": dict(source["estimator"]),
        "analysis": dict(source["analysis"]),
        "config_path": path.resolve(),
    }
    validate_configuration(resolved)
    return resolved


def validate_configuration(config: dict[str, Any]) -> None:
    profile = config["profile"]
    experiment = config["experiment"]
    estimator = config["estimator"]
    if experiment["geometry"] not in GEOMETRIES:
        raise ValueError("geometry must be 'airm' or 'bw'")
    rank = int(experiment["factor_rank"])
    if rank < 1:
        raise ValueError("the B4.5 factor baseline requires positive factor rank")
    persistence = np.asarray(experiment["factor_persistence"], dtype=float)
    scales = np.asarray(experiment["factor_scale"], dtype=float)
    if persistence.shape != (rank,) or scales.shape != (rank,):
        raise ValueError("factor persistence and scale must match factor_rank")
    if np.any(np.abs(persistence) >= 1.0) or np.any(scales <= 0.0):
        raise ValueError("factor persistence/scale are outside their valid domains")
    n_values = [int(value) for value in profile["n_values"]]
    matrix_sizes = [int(value) for value in profile["matrix_sizes"]]
    if not n_values or min(n_values) < 16 or len(set(n_values)) != len(n_values):
        raise ValueError("n_values must be unique and at least 16")
    if not matrix_sizes or min(matrix_sizes) < 2 or len(set(matrix_sizes)) != len(matrix_sizes):
        raise ValueError("matrix_sizes must be unique and at least two")
    if int(profile["replicates"]) < 1:
        raise ValueError("replicates must be positive")
    if any(m * (m + 1) // 2 <= rank for m in matrix_sizes):
        raise ValueError("each tangent dimension must exceed the factor rank")
    overlap = tuple(float(value) for value in estimator["overlap_fractions"])
    if len(overlap) != 2 or not 0.0 < overlap[0] < overlap[1] < 1.0:
        raise ValueError("overlap_fractions must be two increasing interior values")
    if not 0.0 < float(estimator["admissible_boundary_fraction"]) < 1.0:
        raise ValueError("admissible_boundary_fraction must lie in (0, 1)")
    if float(estimator["production_multiplier_cap"]) <= 0.0:
        raise ValueError("production_multiplier_cap must be positive")
    if int(estimator["max_lag"]) < 1 or int(estimator["max_lag"]) >= min(n_values):
        raise ValueError("max_lag must lie between one and the smallest n minus one")
    for n in n_values:
        maximum = maximum_admissible_multiplier(
            n,
            bandwidth_constant=float(estimator["bandwidth_constant"]),
            bandwidth_exponent=float(estimator["bandwidth_exponent"]),
            overlap_fractions=overlap,
        )
        variants = bandwidth_variants(n, estimator)
        if max(variants.values()) >= maximum:
            raise ValueError(f"a bandwidth variant violates the boundary at n={n}")


def build_tasks(config: dict[str, Any]) -> list[Task]:
    profile = config["profile"]
    bare = [
        (int(n), int(matrix_size), replicate)
        for n in profile["n_values"]
        for matrix_size in profile["matrix_sizes"]
        for replicate in range(int(profile["replicates"]))
    ]
    root = np.random.SeedSequence(
        [int(config["experiment"]["root_seed"]), int(profile["seed_namespace"])]
    )
    children = root.spawn(len(bare))
    return [
        Task(n, matrix_size, replicate, seed)
        for (n, matrix_size, replicate), seed in zip(bare, children)
    ]


def _base_and_direction(matrix_size: int, condition: float) -> tuple[np.ndarray, np.ndarray]:
    base = np.diag(np.geomspace(1.0, condition, matrix_size))
    diagonal = np.linspace(-1.0, 1.0, matrix_size)
    direction = np.diag(diagonal)
    if matrix_size > 1:
        direction[0, -1] = direction[-1, 0] = 0.35
    return base, direction


def _dgp_config(config: dict[str, Any], task: Task) -> LSRFMConfig:
    experiment = config["experiment"]
    base, direction = _base_and_direction(
        task.matrix_size, float(experiment["base_condition"])
    )
    return LSRFMConfig(
        centre=CentrePathConfig(
            base_centre=base,
            drift_direction=direction,
            drift_scale=float(experiment["drift_scale"]),
            profile=cubic_profile,
        ),
        factor=AR1FactorConfig(
            rank=int(experiment["factor_rank"]),
            persistence=np.asarray(experiment["factor_persistence"], dtype=float),
            scale=np.asarray(experiment["factor_scale"], dtype=float),
        ),
        loading=LoadingConfig(
            orientation=str(experiment["loading_orientation"]),
            structure=str(experiment["loading_structure"]),
        ),
        noise=NoiseConfig(
            scale=float(experiment["noise_scale"]),
            persistence=float(experiment["noise_persistence"]),
            constant_norm=bool(experiment["noise_constant_norm"]),
            structure="dense",
        ),
    )


def _model_config(
    config: dict[str, Any],
    task: Task,
    multiplier: float,
) -> RFDConfig:
    estimator = config["estimator"]
    bandwidth = (
        float(estimator["bandwidth_constant"])
        * task.n ** (-float(estimator["bandwidth_exponent"]))
        * multiplier
    )
    centre_rate = task.n ** (-float(estimator["polygon_rate_exponent"]))
    n_cells = polygon_cell_count(
        centre_rate, constant=float(estimator["polygon_cell_constant"])
    )
    return RFDConfig(
        bandwidth=bandwidth,
        n_cells=n_cells,
        max_lag=int(estimator["max_lag"]),
        rank_method="fixed",
        rank=int(config["experiment"]["factor_rank"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
        overlap_fractions=tuple(estimator["overlap_fractions"]),
        mean_tol=float(estimator["mean_tolerance"]),
        mean_max_iter=int(estimator["mean_max_iter"]),
    )


def _intrinsic_rms(geometry: GeometryOps, left: np.ndarray, right: np.ndarray) -> float:
    return float(np.sqrt(np.mean(geometry.dist2(left, right))))


def _direct_sum_operator_norm(covariances: np.ndarray) -> float:
    return float(np.sqrt(sum(np.linalg.norm(block, ord=2) ** 2 for block in covariances)))


def _procrustes_nrmse(estimated: np.ndarray, target: np.ndarray) -> float:
    if estimated.shape != target.shape or estimated.shape[1] == 0:
        return np.nan
    left, _, right = np.linalg.svd(estimated.T @ target, full_matrices=False)
    aligned = estimated @ (left @ right)
    denominator = np.linalg.norm(target)
    return float(np.linalg.norm(aligned - target) / denominator) if denominator > 0.0 else np.nan


def _stage_health(fit: RFDFit) -> tuple[float, int]:
    stages = []
    for estimate in fit.centre.estimates:
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is not None:
                stages.extend(one_sided.stages.stages)
    return (
        float(min(stage.effective_sample_size for stage in stages)),
        int(sum(not stage.converged for stage in stages)),
    )


def _energy_radius(sample, geometry: GeometryOps) -> float:
    total = sample.factor_effects + sample.tangent_noise
    squared = geometry.inner(sample.centres, total, total)
    return float(np.sqrt(np.max(np.maximum(squared, 0.0))))


def _diagnostics(sample, fit: RFDFit, geometry: GeometryOps, config: dict[str, Any]) -> dict[str, Any]:
    estimator = config["estimator"]
    rank = int(config["experiment"]["factor_rank"])
    base = config["_active_base"]
    base_basis = geometry.tangent_basis(base)

    reference_factor = geometry.transport(sample.factor_effects, sample.centres, base)
    oracle_factor_rows = tangent_coordinates(reference_factor, base, base_basis, geometry)
    oracle_lag = lag_cross_covariances(
        oracle_factor_rows,
        int(estimator["max_lag"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
    )
    oracle_operator = assemble_lag_operator(oracle_lag)
    oracle_spectrum = decompose_lag_operator(oracle_operator)

    estimated_reference = fit.centre.polygon.reference_point
    aligned_vectors = geometry.transport(
        fit.tangent_rows.reference_vectors, estimated_reference, base
    )
    aligned_rows = tangent_coordinates(aligned_vectors, base, base_basis, geometry)
    estimated_lag = lag_cross_covariances(
        aligned_rows,
        int(estimator["max_lag"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
    )
    estimated_operator = assemble_lag_operator(estimated_lag)
    estimated_spectrum = decompose_lag_operator(estimated_operator)

    lag_difference = estimated_lag.covariances - oracle_lag.covariances
    d_n = _direct_sum_operator_norm(lag_difference)
    a2_n = _direct_sum_operator_norm(oracle_lag.covariances)
    assembly_bound = 2.0 * a2_n * d_n + d_n**2
    operator_error = float(
        np.linalg.norm(estimated_operator.matrix - oracle_operator.matrix, ord=2)
    )
    gap = float(oracle_spectrum.eigenvalues[rank - 1])

    true_projector = (
        oracle_spectrum.eigenvectors[:, :rank]
        @ oracle_spectrum.eigenvectors[:, :rank].T
    )
    fitted_projector = (
        estimated_spectrum.eigenvectors[:, :rank]
        @ estimated_spectrum.eigenvectors[:, :rank].T
    )
    loading_error = float(np.linalg.norm(fitted_projector - true_projector, ord=2))
    target_scores = oracle_lag.centred_rows @ oracle_spectrum.eigenvectors[:, :rank]
    fitted_scores = estimated_lag.centred_rows @ estimated_spectrum.eigenvectors[:, :rank]

    threshold_value = (
        float(estimator["selector_constant"])
        * sample.time.size ** (-float(estimator["selector_exponent"]))
    )
    selector_cap = min(
        int(estimator["selector_max_rank"]),
        estimated_spectrum.eigenvalues.size - 1,
    )
    threshold_result = threshold_rank(
        estimated_spectrum.eigenvalues, threshold_value, max_rank=selector_cap
    )
    ridge_result = ridged_ratio_rank(
        estimated_spectrum.eigenvalues, threshold_value, max_rank=selector_cap
    )
    raw_result = raw_ratio_rank(
        estimated_spectrum.eigenvalues, max_rank=selector_cap
    )

    estimated_centres = evaluate_polygon(fit.centre.polygon, sample.time).points
    latent_signal = geometry.exp(sample.centres, sample.factor_effects)
    observation_eigenvalues = np.linalg.eigvalsh(sample.observations)
    minimum_ess, nonconverged = _stage_health(fit)
    null_eigenvalue = float(estimated_spectrum.eigenvalues[rank])
    row_norm = np.linalg.norm(estimated_lag.centred_rows)
    residual_norm = np.linalg.norm(fit.factors.residual_rows)
    return {
        "true_rank": rank,
        "fixed_fit_rank": fit.rank,
        "threshold_rank": threshold_result.rank,
        "ridged_ratio_rank": ridge_result.rank,
        "raw_ratio_rank": raw_result.rank,
        "threshold": threshold_value,
        "centre_path_rms": _intrinsic_rms(geometry, estimated_centres, sample.centres),
        "lag_row_error": d_n,
        "oracle_lag_row_size": a2_n,
        "operator_error": operator_error,
        "oracle_gap": gap,
        "assembly_bound": assembly_bound,
        "assembly_gap_ratio": assembly_bound / gap if gap > 0.0 else np.inf,
        "loading_subspace_error": loading_error,
        "factor_score_nrmse": _procrustes_nrmse(fitted_scores, target_scores),
        "null_eigenvalue": null_eigenvalue,
        "null_bound_ratio": null_eigenvalue / d_n**2 if d_n > 0.0 else np.nan,
        "observation_reconstruction_rms": _intrinsic_rms(
            geometry, fit.reconstructed_observations, sample.observations
        ),
        "signal_reconstruction_rms": _intrinsic_rms(
            geometry, fit.reconstructed_observations, latent_signal
        ),
        "row_residual_fraction": residual_norm / row_norm if row_norm > 0.0 else np.nan,
        "empirical_energy_R": _energy_radius(sample, geometry),
        "centre_path_length": sample.centre_path_length,
        "centre_path_energy": sample.centre_path_energy,
        "fallback_count": fit.centre.fallback_count,
        "fallback_rate": fit.centre.fallback_rate,
        "minimum_effective_sample_size": minimum_ess,
        "nonconverged_stages": nonconverged,
        "observation_min_eigenvalue": float(np.min(observation_eigenvalues)),
        "observation_max_condition": float(
            np.max(observation_eigenvalues[..., -1] / observation_eigenvalues[..., 0])
        ),
    }


def _error_row(
    config: dict[str, Any], task: Task, variant: str, multiplier: float,
    model_config: RFDConfig, error: Exception, elapsed: float,
) -> dict[str, Any]:
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": config["profile_name"], "n": task.n,
        "matrix_size": task.matrix_size,
        "tangent_dimension": task.matrix_size * (task.matrix_size + 1) // 2,
        "replicate": task.replicate, "variant": variant,
        "seed_spawn_key": ".".join(map(str, task.seed_sequence.spawn_key)),
        "bandwidth_multiplier": multiplier, "bandwidth": model_config.bandwidth,
        "n_cells": model_config.n_cells, "status": "error",
        "error_type": type(error).__name__,
        "error_message": str(error).replace("\n", " ")[:500],
        "elapsed_seconds": elapsed,
    })
    return row


def run_task(
    config: dict[str, Any], task: Task, geometry: GeometryOps | None = None
) -> list[dict[str, Any]]:
    """Generate one draw and fit both bandwidth variants to it."""
    geometry = geometry or GEOMETRIES[config["experiment"]["geometry"]]
    rng = np.random.default_rng(task.seed_sequence)
    dgp_config = _dgp_config(config, task)
    sample = generate_lsrfm(rng, task.n, geometry, dgp_config)
    config["_active_base"] = dgp_config.centre.base_centre
    rows = []
    for variant, multiplier in bandwidth_variants(task.n, config["estimator"]).items():
        model_config = _model_config(config, task, multiplier)
        started = time.perf_counter()
        try:
            fit = fit_rfd(sample.observations, sample.time, geometry, model_config)
            row = {
                "profile": config["profile_name"], "n": task.n,
                "matrix_size": task.matrix_size,
                "tangent_dimension": fit.tangent_rows.tangent_dimension,
                "replicate": task.replicate, "variant": variant,
                "seed_spawn_key": ".".join(map(str, task.seed_sequence.spawn_key)),
                "bandwidth_multiplier": multiplier,
                "bandwidth": model_config.bandwidth, "n_cells": model_config.n_cells,
                "status": "ok", "error_type": "", "error_message": "",
                **_diagnostics(sample, fit, geometry, config),
                "elapsed_seconds": time.perf_counter() - started,
            }
        except Exception as error:
            row = _error_row(
                config, task, variant, multiplier, model_config, error,
                time.perf_counter() - started,
            )
        rows.append(row)
    config.pop("_active_base", None)
    return rows


def _row_key(row: dict[str, Any] | pd.Series) -> tuple[Any, ...]:
    return (str(row["variant"]), int(row["n"]), int(row["matrix_size"]), int(row["replicate"]))


def read_existing_rows(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=RAW_COLUMNS)
    return pd.read_csv(path)


def analysis_rows(config: dict[str, Any], current_raw: pd.DataFrame) -> pd.DataFrame:
    """Combine declared earlier raw tables with this profile for reporting.

    The current profile remains the only table written by this run.  Included
    sources are read-only and may not overlap its (n, m, replicate, variant)
    identities; an overlap is an error rather than a silent overwrite.
    """
    frames = []
    for source in config["profile"].get("analysis_include_raw", []):
        path = (ROOT / source).resolve()
        if not path.is_file():
            print(f"analysis source not found; plotting extension only -> {source}")
            continue
        included = read_existing_rows(path)
        missing = set(RAW_COLUMNS) - set(included.columns)
        if missing:
            raise ValueError(
                f"analysis source {source} is missing columns: {sorted(missing)}"
            )
        frames.append(included[RAW_COLUMNS])
    frames.append(current_raw[RAW_COLUMNS])
    combined = pd.concat(frames, ignore_index=True)
    identity = ["n", "matrix_size", "replicate", "variant"]
    duplicated = combined.duplicated(identity, keep=False)
    if duplicated.any():
        examples = combined.loc[duplicated, identity].head(3).to_dict("records")
        raise ValueError(f"analysis inputs contain overlapping result rows: {examples}")
    return combined


def append_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RAW_COLUMNS, extrasaction="ignore")
        if write_header:
            writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, np.nan) for column in RAW_COLUMNS})
        handle.flush()
        os.fsync(handle.fileno())


def summarize(raw: pd.DataFrame) -> pd.DataFrame:
    ok = raw.loc[raw["status"] == "ok"].copy()
    if ok.empty:
        return pd.DataFrame()
    metrics = [
        "bandwidth_multiplier", "centre_path_rms", "lag_row_error",
        "oracle_lag_row_size", "operator_error", "oracle_gap",
        "assembly_gap_ratio", "loading_subspace_error", "factor_score_nrmse",
        "null_eigenvalue", "observation_reconstruction_rms",
        "signal_reconstruction_rms", "empirical_energy_R", "elapsed_seconds",
    ]
    records = []
    for keys, group in ok.groupby(["n", "matrix_size", "tangent_dimension", "variant"]):
        record = dict(zip(("n", "matrix_size", "tangent_dimension", "variant"), keys))
        record["completed"] = len(group)
        for metric in metrics:
            values = pd.to_numeric(group[metric], errors="coerce")
            record[f"{metric}_median"] = float(values.median())
            record[f"{metric}_q25"] = float(values.quantile(0.25))
            record[f"{metric}_q75"] = float(values.quantile(0.75))
        for selector in ("threshold_rank", "ridged_ratio_rank", "raw_ratio_rank"):
            record[f"{selector}_accuracy_percent"] = float(
                100.0 * (group[selector] == group["true_rank"]).mean()
            )
        records.append(record)
    return pd.DataFrame.from_records(records)


def paired_contrasts(raw: pd.DataFrame) -> pd.DataFrame:
    ok = raw.loc[raw["status"] == "ok"].copy()
    metrics = [
        "centre_path_rms", "loading_subspace_error", "factor_score_nrmse",
        "observation_reconstruction_rms", "signal_reconstruction_rms",
    ]
    records = []
    identity = ["n", "matrix_size", "replicate"]
    for (n, matrix_size), group in ok.groupby(["n", "matrix_size"]):
        wide = group.pivot(index=identity, columns="variant", values=metrics)
        record = {"n": int(n), "matrix_size": int(matrix_size)}
        for metric in metrics:
            if (metric, "production") not in wide or (metric, "reference") not in wide:
                continue
            production = wide[(metric, "production")]
            reference = wide[(metric, "reference")]
            valid = production.notna() & reference.notna() & (reference != 0.0)
            reductions = 100.0 * (reference[valid] - production[valid]) / reference[valid]
            record[f"{metric}_reduction_percent_median"] = float(reductions.median())
            record[f"{metric}_paired_count"] = int(valid.sum())
        records.append(record)
    return pd.DataFrame.from_records(records)


def _style(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.2)


def plot_results(summary: pd.DataFrame, contrasts: pd.DataFrame, output: Path) -> None:
    if summary.empty:
        return
    plot_dir = output / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)
    colors = {"production": "#0072B2", "reference": "#E69F00"}
    styles = {"production": "-", "reference": "--"}

    rate_metrics = [
        ("centre_path_rms_median", "centre path RMS"),
        ("lag_row_error_median", "lag-row error $d_n$"),
        ("loading_subspace_error_median", "loading projector error"),
        ("null_eigenvalue_median", "first beyond-rank eigenvalue"),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    for ax, (metric, label) in zip(axes.flat, rate_metrics):
        for (matrix_size, variant), line in summary.groupby(["matrix_size", "variant"]):
            line = line.sort_values("n")
            ax.plot(
                line["n"], line[metric], marker="o", color=colors[variant],
                linestyle=styles[variant],
                alpha=min(1.0, 0.55 + 0.12 * matrix_size),
                label=f"m={matrix_size}, {variant}",
            )
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xlabel("observations n")
        ax.set_ylabel(label)
        _style(ax)
    axes[0, 0].legend(fontsize=8, ncol=2)
    fig.suptitle("Complete RFD errors across sample size and SPD size", fontweight="bold")
    fig.tight_layout()
    fig.savefig(plot_dir / "01_end_to_end_rates.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    if not contrasts.empty:
        metric = "loading_subspace_error_reduction_percent_median"
        pivot = contrasts.pivot(index="matrix_size", columns="n", values=metric)
        fig, ax = plt.subplots(figsize=(9, 4.8))
        image = ax.imshow(pivot.to_numpy(), aspect="auto", cmap="RdBu", vmin=-50, vmax=50)
        ax.set_xticks(range(pivot.shape[1]), [f"{int(value):,}" for value in pivot.columns])
        ax.set_yticks(range(pivot.shape[0]), [str(int(value)) for value in pivot.index])
        ax.set_xlabel("observations n")
        ax.set_ylabel("SPD matrix size m")
        ax.set_title("Production bandwidth: loading-error reduction", fontweight="bold")
        colorbar = fig.colorbar(image, ax=ax)
        colorbar.set_label("improvement over fixed 1.3 (%)")
        fig.tight_layout()
        fig.savefig(plot_dir / "02_paired_loading_gain.png", dpi=180, bbox_inches="tight")
        plt.close(fig)

    rank = summary.loc[summary["variant"] == "production"]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    selector_columns = {
        "threshold_rank_accuracy_percent": "threshold",
        "ridged_ratio_rank_accuracy_percent": "ridged ratio",
        "raw_ratio_rank_accuracy_percent": "raw ratio (comparator)",
    }
    for index, (column, label) in enumerate(selector_columns.items()):
        grouped = rank.groupby("n")[column].mean().sort_index()
        ax.plot(grouped.index, grouped.values, marker="o", label=label,
                linestyle=("-", "--", ":")[index])
    ax.set_xscale("log", base=2)
    ax.set_ylim(-2, 102)
    ax.set_xlabel("observations n")
    ax.set_ylabel("correct factor count (%)")
    ax.set_title("Factor-number recovery on production fits", fontweight="bold")
    _style(ax)
    ax.legend()
    fig.tight_layout()
    fig.savefig(plot_dir / "03_rank_accuracy.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def initialize_output(config: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    metadata_path = output / "metadata.json"
    metadata = {
        "profile": config["profile_name"],
        "recorded": bool(config["profile"]["recorded"]),
        "config_sha256": _digest(config["config_path"]),
        "root_seed": int(config["experiment"]["root_seed"]),
        "seed_namespace": int(config["profile"]["seed_namespace"]),
        "numpy": np.__version__, "python": platform.python_version(),
        "platform": platform.platform(),
    }
    if metadata_path.exists():
        existing = json.loads(metadata_path.read_text(encoding="utf-8"))
        for key in ("profile", "config_sha256", "root_seed", "seed_namespace"):
            if existing.get(key) != metadata[key]:
                raise RuntimeError(f"existing output metadata disagrees on {key}")
    else:
        metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        shutil.copy2(config["config_path"], output / "end_to_end.yaml")


def summarize_and_plot(config: dict[str, Any], output: Path) -> None:
    raw = read_existing_rows(output / "raw.csv")
    if raw.empty:
        print("No rows available to summarize.")
        return
    combined = analysis_rows(config, raw)
    summary = summarize(combined)
    contrasts = paired_contrasts(combined)
    summary.to_csv(output / "summary.csv", index=False)
    contrasts.to_csv(output / "paired_contrasts.csv", index=False)
    plot_results(summary, contrasts, output)
    requested = len(build_tasks(config)) * len(VARIANTS)
    completed = int((raw["status"] == "ok").sum())
    errors = int((raw["status"] == "error").sum())
    report = [
        f"# {config['profile_name']} complete RFD experiment", "",
        "Numerical evidence only; it does not prove the analytical rates.", "",
        f"- requested rows: {requested}", f"- completed rows: {completed}",
        f"- recorded errors: {errors}",
        f"- completion: {100.0 * completed / requested:.1f}%", "",
        f"- rows used in combined analysis: {len(combined)}", "",
        "The production and reference fits are paired on every generated draw.",
        "Positive values in `paired_contrasts.csv` mean the capped production",
        "bandwidth reduced error relative to fixed multiplier 1.3.", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"summaries and plots -> {output.relative_to(ROOT)}")


def print_workload(config: dict[str, Any], tasks: list[Task]) -> None:
    profile = config["profile"]
    print(f"profile: {config['profile_name']}")
    print(f"recorded: {profile['recorded']}")
    print(f"output: {profile['output_dir']}")
    print(f"n values: {profile['n_values']}")
    print(f"matrix sizes: {profile['matrix_sizes']}")
    print(f"replicates: {profile['replicates']}")
    print(f"DGP tasks: {len(tasks)}")
    print(f"requested result rows: {len(tasks) * len(VARIANTS)}")
    print("bandwidth rules:")
    for n in profile["n_values"]:
        values = bandwidth_variants(int(n), config["estimator"])
        print(f"  n={int(n):,}: production={values['production']:.6g}, reference={values['reference']:.6g}")


def run(config: dict[str, Any], *, max_tasks: int | None = None, plot_only: bool = False) -> None:
    output = (ROOT / config["profile"]["output_dir"]).resolve()
    initialize_output(config, output)
    if plot_only:
        summarize_and_plot(config, output)
        return
    raw_path = output / "raw.csv"
    existing = read_existing_rows(raw_path)
    completed_keys = {_row_key(row) for _, row in existing.iterrows()}
    tasks = build_tasks(config)
    processed = 0
    for index, task in enumerate(tasks, start=1):
        missing = [
            variant for variant in VARIANTS
            if (variant, task.n, task.matrix_size, task.replicate) not in completed_keys
        ]
        if not missing:
            continue
        if max_tasks is not None and processed >= max_tasks:
            break
        print(f"[{index}/{len(tasks)}] n={task.n}, m={task.matrix_size}, rep={task.replicate}", flush=True)
        rows = run_task(config, task)
        rows = [row for row in rows if row["variant"] in missing]
        append_rows(raw_path, rows)
        completed_keys.update(_row_key(row) for row in rows)
        processed += 1
    summarize_and_plot(config, output)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument(
        "--profile",
        choices=("smoke", "factor_baseline", "factor_baseline_8192"),
        default="smoke",
    )
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument("--plot-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_configuration(args.config.resolve(), args.profile)
    tasks = build_tasks(config)
    print_workload(config, tasks)
    if args.dry_run:
        return 0
    if args.max_tasks is not None and args.max_tasks < 1:
        raise ValueError("max-tasks must be positive")
    try:
        run(config, max_tasks=args.max_tasks, plot_only=args.plot_only)
    except KeyboardInterrupt:
        print("\nInterrupted. Completed rows are on disk; rerun to resume.")
        summarize_and_plot(config, (ROOT / config["profile"]["output_dir"]).resolve())
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
