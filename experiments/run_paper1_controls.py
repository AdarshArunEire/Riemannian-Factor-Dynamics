"""Run the frozen Paper 1 null, identification, and violation matrix.

One task generates one AIRM sample and fits three estimators to that draw:
the known-centre noisy oracle, complete feasible RFD, and a one-global-centre
RFM-compatible ablation.  Component random streams are shared across regimes
whenever their component configuration agrees.  Output is append-only and
resumable; an exception becomes a recorded row.
"""

from __future__ import annotations

import argparse
import csv
import concurrent.futures
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
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_b45_comparators import (  # noqa: E402
    _projector_from_rows,
    _selector_ranks,
    evaluate_comparators,
)
from run_end_to_end import (  # noqa: E402
    GEOMETRIES,
    _base_and_direction,
    _direct_sum_operator_norm,
    _energy_radius,
    _intrinsic_rms,
    _model_config,
    _procrustes_nrmse,
    _stage_health,
)
from rfd.dgp.lsrfm import (  # noqa: E402
    AR1FactorConfig,
    LSRFMSample,
    LoadingConfig,
    NoiseConfig,
    centre_path_diagnostics,
    generate_factors,
    generate_loadings,
    generate_reference_tangent_noise,
    rescaled_time,
)
from rfd.estimators.frame import evaluate_polygon  # noqa: E402
from rfd.estimators.lag import (  # noqa: E402
    coordinate_tangents,
    lag_cross_covariances,
    tangent_coordinates,
)
from rfd.geometry import GeometryOps  # noqa: E402
from rfd.model import fit_rfd  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "paper1_controls.yaml"
RUNTIME_SECONDS = {128: 0.25, 512: 0.8, 2048: 3.4, 8192: 16.5}

RAW_COLUMNS = [
    "profile", "regime", "regime_label", "regime_class", "expected",
    "n", "matrix_size", "tangent_dimension", "replicate", "seed_key",
    "status", "error_type", "error_message", "path_kind", "drift_scale",
    "true_rank", "noise_scale", "noise_persistence", "loading_orientation",
    "declared_drift_overlap", "realised_drift_loading_overlap",
    "centre_path_length", "centre_path_energy", "empirical_energy_R",
    "noise_lag_row_size", "rfd_centre_path_rms", "rfd_loading_error",
    "rfd_loading_angle_degrees", "rfd_factor_nrmse",
    "rfd_observation_reconstruction_rms", "rfd_signal_reconstruction_rms",
    "rfd_threshold_rank", "rfd_raw_ratio_rank", "rfd_ridged_ratio_rank",
    "rfd_fallback_count", "rfd_fallback_rate", "rfd_minimum_effective_sample_size",
    "rfd_nonconverged_stages", "known_centre_loading_error",
    "known_centre_factor_nrmse", "known_centre_observation_reconstruction_rms",
    "known_centre_signal_reconstruction_rms", "known_centre_threshold_rank",
    "known_centre_raw_ratio_rank", "known_centre_ridged_ratio_rank",
    "fixed_centre_loading_error", "fixed_centre_factor_nrmse",
    "fixed_centre_observation_reconstruction_rms",
    "fixed_centre_signal_reconstruction_rms", "fixed_centre_threshold_rank",
    "fixed_centre_raw_ratio_rank", "fixed_centre_ridged_ratio_rank",
    "global_mean_centre_path_rms", "global_mean_converged",
    "global_mean_iterations", "global_mean_residual",
    "observation_min_eigenvalue", "observation_max_condition", "elapsed_seconds",
]


@dataclass(frozen=True)
class ControlTask:
    n: int
    replicate: int
    regime: str
    specification: dict[str, Any]


def load_configuration(path: Path, profile_name: str) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        source = yaml.safe_load(handle)
    if profile_name not in source.get("profiles", {}):
        raise ValueError(f"unknown profile: {profile_name}")
    config = {
        "profile_name": profile_name,
        "profile": dict(source["profiles"][profile_name]),
        "experiment": dict(source["experiment"]),
        "estimator": dict(source["estimator"]),
        "analysis": dict(source["analysis"]),
        "core_regimes": dict(source["core_regimes"]),
        "phase_curve": dict(source["phase_curve"]),
        "config_path": path.resolve(),
    }
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    profile = config["profile"]
    experiment = config["experiment"]
    if experiment["geometry"] not in GEOMETRIES:
        raise ValueError("unsupported geometry")
    if int(experiment["matrix_size"]) < 2:
        raise ValueError("matrix_size must be at least two")
    if int(profile["replicates"]) < 1:
        raise ValueError("replicates must be positive")
    if profile["regime_group"] not in {"core", "phase"}:
        raise ValueError("regime_group must be core or phase")
    n_values = [int(value) for value in profile["n_values"]]
    if not n_values or min(n_values) < 16:
        raise ValueError("n_values must be nonempty and at least 16")
    for regime, specification in config["core_regimes"].items():
        if specification["path"] not in {"radial", "curved", "rough"}:
            raise ValueError(f"unknown path for {regime}")
        if specification["loading_orientation"] not in {
            "random", "aligned", "mixed", "orthogonal"
        }:
            raise ValueError(f"unknown loading orientation for {regime}")
        if int(specification["rank"]) < 0:
            raise ValueError(f"negative rank for {regime}")
        if not 0.0 <= float(specification.get("drift_overlap", 0.5)) <= 1.0:
            raise ValueError(f"invalid drift overlap for {regime}")


def resolved_regimes(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if config["profile"]["regime_group"] == "core":
        return {key: dict(value) for key, value in config["core_regimes"].items()}
    experiment = config["experiment"]
    result = {}
    for orientation, orientation_spec in config["phase_curve"]["orientations"].items():
        for drift_scale in config["phase_curve"]["drift_scales"]:
            code = str(orientation_spec["code"])
            scale_code = f"{int(round(100 * float(drift_scale))):03d}"
            regime = f"P-{code}-{scale_code}"
            result[regime] = {
                "label": f"phase {orientation}, nu={float(drift_scale):.2f}",
                "class": "phase",
                "path": "radial",
                "drift_scale": float(drift_scale),
                "rank": int(experiment["factor_rank"]),
                "noise_scale": float(experiment["noise_scale"]),
                "noise_persistence": 0.0,
                "loading_orientation": orientation,
                "drift_overlap": float(orientation_spec["drift_overlap"]),
                "expected": "map fixed-minus-moving risk without assuming monotonicity",
            }
    return result


def build_tasks(config: dict[str, Any]) -> list[ControlTask]:
    regimes = resolved_regimes(config)
    return [
        ControlTask(int(n), replicate, regime, specification)
        for n in config["profile"]["n_values"]
        for regime, specification in regimes.items()
        for replicate in range(int(config["profile"]["replicates"]))
    ]


def _unit(vector: np.ndarray, base: np.ndarray, geometry: GeometryOps) -> np.ndarray:
    squared = float(geometry.inner(base, vector, vector))
    if not np.isfinite(squared) or squared <= 1e-18:
        raise ValueError("control direction has zero or nonfinite intrinsic norm")
    return np.asarray(vector, dtype=float) / np.sqrt(squared)


def _control_directions(
    matrix_size: int, condition: float, geometry: GeometryOps
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    base, first_raw = _base_and_direction(matrix_size, condition)
    first = _unit(first_raw, base, geometry)
    second_raw = np.zeros_like(base)
    for index in range(matrix_size - 1):
        second_raw[index, index + 1] = 1.0
        second_raw[index + 1, index] = 1.0
    second_raw -= float(geometry.inner(base, second_raw, first)) * first
    second = _unit(second_raw, base, geometry)
    return base, first, second


def _path_centres(
    time_values: np.ndarray,
    base: np.ndarray,
    first: np.ndarray,
    second: np.ndarray,
    geometry: GeometryOps,
    path_kind: str,
    drift_scale: float,
) -> np.ndarray:
    time_values = np.asarray(time_values, dtype=float)
    if path_kind == "rough":
        first_profile = (
            1.5 * time_values
            + 0.35 * (np.abs(time_values - 0.5) - 0.5)
        )
        second_profile = np.zeros_like(time_values)
    else:
        first_profile = time_values + 0.5 * time_values**3
        second_profile = (
            0.60 * np.sin(np.pi * time_values)
            if path_kind == "curved" else np.zeros_like(time_values)
        )
    tangents = drift_scale * (
        first_profile[:, None, None] * first
        + second_profile[:, None, None] * second
    )
    return geometry.exp(base, tangents)


def _component_rng(
    config: dict[str, Any], task: ControlTask, component: int
) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence([
        int(config["experiment"]["root_seed"]),
        int(config["profile"]["seed_namespace"]),
        int(task.n), int(task.replicate), int(component),
    ]))


def _new_excluded_unit(
    rng: np.random.Generator,
    base: np.ndarray,
    geometry: GeometryOps,
    exclusions: list[np.ndarray],
    structure: str,
) -> np.ndarray:
    for _ in range(256):
        candidate = geometry.random_tangent(rng, base, 1, structure)[0]
        if exclusions:
            gram = np.asarray([
                [float(geometry.inner(base, left, right)) for right in exclusions]
                for left in exclusions
            ])
            inner = np.asarray([
                float(geometry.inner(base, vector, candidate))
                for vector in exclusions
            ])
            coefficients = np.linalg.lstsq(gram, inner, rcond=None)[0]
            candidate = candidate - np.tensordot(
                coefficients, np.stack(exclusions), axes=(0, 0)
            )
        squared = float(geometry.inner(base, candidate, candidate))
        if np.isfinite(squared) and squared > 1e-18:
            return candidate / np.sqrt(squared)
    raise ValueError("could not construct the declared loading orientation")


def _control_loadings(
    rng: np.random.Generator,
    base: np.ndarray,
    rank: int,
    drift: np.ndarray,
    geometry: GeometryOps,
    config: LoadingConfig,
) -> np.ndarray:
    """Make the complete loading-span/drift overlap exact for controls."""
    if config.orientation == "random" or rank == 0:
        return generate_loadings(
            rng, base, rank, drift, geometry, config
        )
    loadings: list[np.ndarray] = []
    if config.orientation == "aligned":
        loadings.append(drift)
    elif config.orientation == "mixed":
        orthogonal = _new_excluded_unit(
            rng, base, geometry, [drift], config.structure
        )
        overlap = float(config.drift_overlap)
        loadings.append(
            overlap * drift + np.sqrt(1.0 - overlap**2) * orthogonal
        )
    while len(loadings) < rank:
        exclusions = [drift, *loadings]
        loadings.append(
            _new_excluded_unit(rng, base, geometry, exclusions, config.structure)
        )
    return np.stack(loadings)


def generate_control_sample(
    config: dict[str, Any], task: ControlTask, geometry: GeometryOps
) -> tuple[LSRFMSample, np.ndarray, np.ndarray]:
    experiment = config["experiment"]
    spec = task.specification
    matrix_size = int(experiment["matrix_size"])
    base, first, second = _control_directions(
        matrix_size, float(experiment["base_condition"]), geometry
    )
    time_values = rescaled_time(task.n)
    path_time = np.concatenate(([0.0], time_values))
    path_centres = _path_centres(
        path_time, base, first, second, geometry,
        str(spec["path"]), float(spec["drift_scale"]),
    )
    centres = path_centres[1:]
    rank = int(spec["rank"])
    persistence = np.asarray(experiment["factor_persistence"], dtype=float)[:rank]
    scales = np.asarray(experiment["factor_scale"], dtype=float)[:rank]
    factors = generate_factors(
        _component_rng(config, task, 1), task.n,
        AR1FactorConfig(rank=rank, persistence=persistence, scale=scales),
    )
    loading_config = LoadingConfig(
        orientation=str(spec["loading_orientation"]),
        drift_overlap=float(spec.get("drift_overlap", 0.5)),
        structure=str(experiment["loading_structure"]),
    )
    loadings = _control_loadings(
        _component_rng(config, task, 2), base, rank, first, geometry,
        loading_config,
    )
    reference_effects = np.tensordot(factors, loadings, axes=([-1], [0]))
    reference_noise = generate_reference_tangent_noise(
        _component_rng(config, task, 3), task.n, base, geometry,
        NoiseConfig(
            scale=float(spec["noise_scale"]),
            persistence=float(spec["noise_persistence"]),
            constant_norm=bool(experiment["noise_constant_norm"]),
            structure=str(experiment["loading_structure"]),
        ),
    )
    factor_effects = geometry.transport(reference_effects, base, centres)
    tangent_noise = geometry.transport(reference_noise, base, centres)
    observations = geometry.exp(centres, factor_effects + tangent_noise)
    path_length, path_energy = centre_path_diagnostics(
        path_time, path_centres, geometry
    )
    sample = LSRFMSample(
        observations=observations,
        centres=centres,
        factors=factors,
        loadings=loadings,
        factor_effects=factor_effects,
        tangent_noise=tangent_noise,
        time=time_values,
        centre_path_length=path_length,
        centre_path_energy=path_energy,
        geometry_name=geometry.name,
    )
    return sample, base, first


def _active_config(
    config: dict[str, Any], task: ControlTask
) -> dict[str, Any]:
    active = {
        "profile_name": config["profile_name"],
        "profile": config["profile"],
        "experiment": dict(config["experiment"]),
        "estimator": config["estimator"],
    }
    active["experiment"]["factor_rank"] = int(task.specification["rank"])
    return active


def _loading_error(
    fit, sample: LSRFMSample, base: np.ndarray, geometry: GeometryOps
) -> tuple[float, float]:
    rank = sample.factors.shape[1]
    if rank == 0:
        return np.nan, np.nan
    base_basis = geometry.tangent_basis(base)
    truth_coordinates = tangent_coordinates(
        sample.loadings, base, base_basis, geometry
    )
    truth_projector = _projector_from_rows(truth_coordinates)
    estimated_vectors = coordinate_tangents(
        fit.loadings.T, fit.tangent_rows.basis
    )
    estimated_at_base = geometry.transport(
        estimated_vectors, fit.centre.polygon.reference_point, base
    )
    estimated_coordinates = tangent_coordinates(
        estimated_at_base, base, base_basis, geometry
    )
    estimated_projector = _projector_from_rows(estimated_coordinates)
    error = float(np.linalg.norm(estimated_projector - truth_projector, ord=2))
    angle = float(np.degrees(np.arcsin(np.clip(error, 0.0, 1.0))))
    return error, angle


def _noise_lag_size(
    sample: LSRFMSample, base: np.ndarray, geometry: GeometryOps,
    config: dict[str, Any],
) -> float:
    basis = geometry.tangent_basis(base)
    reference = geometry.transport(sample.tangent_noise, sample.centres, base)
    rows = tangent_coordinates(reference, base, basis, geometry)
    lag = lag_cross_covariances(
        rows, int(config["estimator"]["max_lag"]),
        tail_mode=str(config["estimator"]["tail_mode"]),
        normalization=str(config["estimator"]["normalization"]),
    )
    return _direct_sum_operator_norm(lag.covariances)


def evaluate_task(
    config: dict[str, Any], task: ControlTask, geometry: GeometryOps
) -> dict[str, Any]:
    sample, base, first = generate_control_sample(config, task, geometry)
    active = _active_config(config, task)
    model_config = _model_config(active, task, multiplier=_production_multiplier(active, task.n))
    fit = fit_rfd(sample.observations, sample.time, geometry, model_config)
    comparators = evaluate_comparators(sample, geometry, active, base)
    rank = int(task.specification["rank"])
    loading_error, loading_angle = _loading_error(fit, sample, base, geometry)
    target_factors = sample.factors - sample.factors.mean(axis=0)
    estimated_centres = evaluate_polygon(fit.centre.polygon, sample.time).points
    latent_signal = geometry.exp(sample.centres, sample.factor_effects)
    threshold, raw_ratio, ridged_ratio = _selector_ranks(
        fit.spectrum.eigenvalues, active, task.n
    )
    minimum_ess, nonconverged = _stage_health(fit)
    observation_eigenvalues = np.linalg.eigvalsh(sample.observations)
    overlaps = [
        float(geometry.inner(base, loading, first))
        for loading in sample.loadings
    ]
    realised_overlap = float(np.linalg.norm(overlaps)) if overlaps else np.nan
    result = {
        "centre_path_length": sample.centre_path_length,
        "centre_path_energy": sample.centre_path_energy,
        "empirical_energy_R": _energy_radius(sample, geometry),
        "noise_lag_row_size": _noise_lag_size(sample, base, geometry, config),
        "realised_drift_loading_overlap": realised_overlap,
        "rfd_centre_path_rms": _intrinsic_rms(
            geometry, estimated_centres, sample.centres
        ),
        "rfd_loading_error": loading_error,
        "rfd_loading_angle_degrees": loading_angle,
        "rfd_factor_nrmse": _procrustes_nrmse(
            fit.factor_scores, target_factors
        ),
        "rfd_observation_reconstruction_rms": _intrinsic_rms(
            geometry, fit.reconstructed_observations, sample.observations
        ),
        "rfd_signal_reconstruction_rms": _intrinsic_rms(
            geometry, fit.reconstructed_observations, latent_signal
        ),
        "rfd_threshold_rank": threshold,
        "rfd_raw_ratio_rank": raw_ratio,
        "rfd_ridged_ratio_rank": ridged_ratio,
        "rfd_fallback_count": fit.centre.fallback_count,
        "rfd_fallback_rate": fit.centre.fallback_rate,
        "rfd_minimum_effective_sample_size": minimum_ess,
        "rfd_nonconverged_stages": nonconverged,
        "observation_min_eigenvalue": float(np.min(observation_eigenvalues)),
        "observation_max_condition": float(np.max(
            observation_eigenvalues[..., -1] / observation_eigenvalues[..., 0]
        )),
    }
    for column in (
        "known_centre_loading_error", "fixed_centre_loading_error",
        "known_centre_factor_nrmse", "fixed_centre_factor_nrmse",
        "known_centre_observation_reconstruction_rms",
        "fixed_centre_observation_reconstruction_rms",
        "known_centre_signal_reconstruction_rms",
        "fixed_centre_signal_reconstruction_rms",
        "known_centre_threshold_rank", "fixed_centre_threshold_rank",
        "known_centre_raw_ratio_rank", "fixed_centre_raw_ratio_rank",
        "known_centre_ridged_ratio_rank", "fixed_centre_ridged_ratio_rank",
        "global_mean_centre_path_rms", "global_mean_converged",
        "global_mean_iterations", "global_mean_residual",
    ):
        result[column] = comparators[column]
    if rank == 0:
        for column in (
            "known_centre_loading_error", "fixed_centre_loading_error",
            "known_centre_factor_nrmse", "fixed_centre_factor_nrmse",
        ):
            result[column] = np.nan
    return result


def _production_multiplier(config: dict[str, Any], n: int) -> float:
    estimator = config["estimator"]
    left, right = map(float, estimator["overlap_fractions"])
    maximum = min(left, 1.0 - right) / (
        float(estimator["bandwidth_constant"])
        * n ** (-float(estimator["bandwidth_exponent"]))
    )
    return min(
        float(estimator["production_multiplier_cap"]),
        float(estimator["admissible_boundary_fraction"]) * maximum,
    )


def run_task(config: dict[str, Any], task: ControlTask) -> dict[str, Any]:
    started = time.perf_counter()
    spec = task.specification
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": config["profile_name"], "regime": task.regime,
        "regime_label": spec["label"], "regime_class": spec["class"],
        "expected": spec["expected"], "n": task.n,
        "matrix_size": int(config["experiment"]["matrix_size"]),
        "tangent_dimension": int(config["experiment"]["matrix_size"])
        * (int(config["experiment"]["matrix_size"]) + 1) // 2,
        "replicate": task.replicate,
        "seed_key": (
            f"{config['profile']['seed_namespace']}.{task.n}.{task.replicate}"
        ),
        "path_kind": spec["path"], "drift_scale": spec["drift_scale"],
        "true_rank": spec["rank"], "noise_scale": spec["noise_scale"],
        "noise_persistence": spec["noise_persistence"],
        "loading_orientation": spec["loading_orientation"],
        "declared_drift_overlap": spec.get("drift_overlap", np.nan),
    })
    try:
        geometry = GEOMETRIES[config["experiment"]["geometry"]]
        row.update(evaluate_task(config, task, geometry))
        row.update({"status": "ok", "error_type": "", "error_message": ""})
    except Exception as error:
        row.update({
            "status": "error", "error_type": type(error).__name__,
            "error_message": str(error).replace("\n", " ")[:500],
        })
    row["elapsed_seconds"] = time.perf_counter() - started
    return row


def _row_key(row) -> tuple[str, int, int]:
    return str(row["regime"]), int(row["n"]), int(row["replicate"])


def read_rows(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=RAW_COLUMNS)
    return pd.read_csv(path)


def append_row(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RAW_COLUMNS)
        if write_header:
            writer.writeheader()
        writer.writerow({column: row.get(column, np.nan) for column in RAW_COLUMNS})
        handle.flush()
        os.fsync(handle.fileno())


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
        metadata_path.write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        shutil.copy2(config["config_path"], output / "paper1_controls.yaml")


def summarize(raw: pd.DataFrame, output: Path, requested: int) -> None:
    ok = raw.loc[raw["status"] == "ok"].copy()
    summary_rows = []
    metrics = [
        "rfd_centre_path_rms", "rfd_loading_error", "rfd_factor_nrmse",
        "rfd_observation_reconstruction_rms", "rfd_signal_reconstruction_rms",
        "known_centre_loading_error", "fixed_centre_loading_error",
        "known_centre_factor_nrmse", "fixed_centre_factor_nrmse",
        "known_centre_observation_reconstruction_rms",
        "fixed_centre_observation_reconstruction_rms", "noise_lag_row_size",
    ]
    for (regime, n), group in ok.groupby(["regime", "n"]):
        row = {"regime": regime, "n": int(n), "completed": len(group)}
        for metric in metrics:
            values = pd.to_numeric(group[metric], errors="coerce")
            row[f"{metric}_mean"] = float(values.mean())
            row[f"{metric}_median"] = float(values.median())
            row[f"{metric}_q25"] = float(values.quantile(0.25))
            row[f"{metric}_q75"] = float(values.quantile(0.75))
        row["rfd_threshold_accuracy_percent"] = float(
            100 * (group["rfd_threshold_rank"] == group["true_rank"]).mean()
        )
        summary_rows.append(row)
    pd.DataFrame(summary_rows).to_csv(output / "summary.csv", index=False)
    report = [
        f"# {raw['profile'].iloc[0] if not raw.empty else 'control'} run", "",
        "Numerical evidence only; violations are expected to fail honestly.", "",
        f"- requested tasks: {requested}",
        f"- rows on disk: {len(raw)}",
        f"- completed rows: {len(ok)}",
        f"- recorded errors: {(raw['status'] == 'error').sum() if not raw.empty else 0}",
        f"- completion: {100 * len(raw) / requested:.1f}%", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")


def estimate_seconds(tasks: list[ControlTask]) -> float:
    return float(sum(RUNTIME_SECONDS.get(task.n, 16.5 * task.n / 8192) for task in tasks))


def print_workload(
    config: dict[str, Any], tasks: list[ControlTask], workers: int
) -> None:
    seconds = estimate_seconds(tasks)
    print(f"profile: {config['profile_name']}")
    print(f"recorded: {config['profile']['recorded']}")
    print(f"output: {config['profile']['output_dir']}")
    print(f"regimes: {len(resolved_regimes(config))}")
    print(f"n values: {config['profile']['n_values']}")
    print(f"replicates: {config['profile']['replicates']}")
    print(f"requested tasks: {len(tasks)}")
    print(f"historical serial estimate: {seconds / 3600:.2f} hours")
    parallel_seconds = seconds / max(1.0, 0.75 * workers)
    print(f"{workers}-worker planning estimate: {parallel_seconds / 3600:.2f} hours")


def run(
    config: dict[str, Any], *, max_tasks: int | None = None, workers: int = 1
) -> None:
    output = (ROOT / config["profile"]["output_dir"]).resolve()
    initialize_output(config, output)
    raw_path = output / "raw.csv"
    existing = read_rows(raw_path)
    completed = {_row_key(row) for _, row in existing.iterrows()}
    tasks = build_tasks(config)
    pending = [
        task for task in tasks
        if (task.regime, task.n, task.replicate) not in completed
    ]
    if max_tasks is not None:
        pending = pending[:max_tasks]
    if workers == 1:
        for index, task in enumerate(pending, start=1):
            print(
                f"[{index}/{len(pending)}] {task.regime}, n={task.n}, "
                f"rep={task.replicate}", flush=True,
            )
            append_row(raw_path, run_task(config, task))
    elif pending:
        print(
            f"dispatching {len(pending)} tasks to {workers} worker processes; "
            "the parent alone writes result rows", flush=True,
        )
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
            future_tasks = {
                executor.submit(run_task, config, task): task for task in pending
            }
            for completed_count, future in enumerate(
                concurrent.futures.as_completed(future_tasks), start=1
            ):
                task = future_tasks[future]
                row = future.result()
                append_row(raw_path, row)
                print(
                    f"[{completed_count}/{len(pending)} complete] "
                    f"{task.regime}, n={task.n}, rep={task.replicate}, "
                    f"status={row['status']}", flush=True,
                )
    summarize(read_rows(raw_path), output, len(tasks))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument(
        "--profile",
        choices=("smoke", "phase_smoke", "control_core", "phase_curve"),
        default="smoke",
    )
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_configuration(args.config.resolve(), args.profile)
    tasks = build_tasks(config)
    if args.workers < 1 or args.workers > 8:
        raise ValueError("workers must lie between one and eight")
    print_workload(config, tasks, args.workers)
    if args.dry_run:
        return 0
    if args.max_tasks is not None and args.max_tasks < 1:
        raise ValueError("max-tasks must be positive")
    try:
        run(config, max_tasks=args.max_tasks, workers=args.workers)
    except KeyboardInterrupt:
        print("\nInterrupted. Completed rows are on disk; rerun to resume.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
