"""B4.2 centre-rate and N-LS-A discrepancy experiment harness.

The recorded scientific choices live in ``config/predeclaration.yaml`` and
the concrete operational values live in ``config/centre_rate.yaml``.

Examples
--------
Inspect the resolved workload without computing anything::

    python experiments/run_centre_rate.py --profile centre_rate --dry-run

Run the unrecorded smoke profile::

    python experiments/run_centre_rate.py --profile smoke

Run or resume a recorded profile::

    python experiments/run_centre_rate.py --profile centre_rate
    python experiments/run_centre_rate.py --profile discrepancy

The process is serial and append-only.  A repeated command skips completed
rows and regenerates summaries and plots from all rows already present.
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
from typing import Any, Iterable

# Keep one serial experiment from turning each tiny SPD operation into a
# competing BLAS thread team.  Explicit user environment settings still win.
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
    centre_path,
    generate_lsrfm,
)
from rfd.estimators.centre import (  # noqa: E402
    CentrePathEstimate,
    geodesic_blend,
    estimate_centre_path,
)
from rfd.estimators.frame import (  # noqa: E402
    PolygonalFrame,
    evaluate_polygon,
    polygon_cell_count,
    regular_polygon_grid,
)
from rfd.geometry import AIRM_GEOMETRY, GeometryOps  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "centre_rate.yaml"
RAW_COLUMNS = [
    "profile",
    "regime",
    "a_label",
    "a_value",
    "n",
    "replicate",
    "bandwidth_multiplier",
    "bandwidth",
    "n_cells",
    "seed_spawn_key",
    "status",
    "error_type",
    "error_message",
    "path_rms",
    "vertex_rms",
    "path_sup",
    "broad_path_rms",
    "richardson_gain",
    "actual_centre_rms",
    "paired_discrepancy_rms",
    "fallback_count",
    "fallback_rate",
    "fallback_reasons",
    "minimum_ess",
    "minimum_support",
    "maximum_iterations",
    "maximum_residual",
    "nonconverged_stages",
    "observation_min_eigenvalue",
    "observation_max_condition",
    "estimated_min_eigenvalue",
    "elapsed_seconds",
]

PALETTE = [
    "#0072B2",
    "#E69F00",
    "#009E73",
    "#CC79A7",
    "#D55E00",
    "#56B4E9",
    "#F0E442",
    "#000000",
]
LINE_STYLES = ["-", "--", ":", "-."]


@dataclass(frozen=True)
class Scenario:
    regime: str
    a_value: float | None

    @property
    def a_label(self) -> str:
        if self.a_value is None:
            return "none"
        if np.isinf(self.a_value):
            return "infinity"
        return f"{self.a_value:.12g}"

    @property
    def label(self) -> str:
        if self.regime != "discrepancy_coherent":
            return self.regime
        return f"a={self.a_label}"


@dataclass(frozen=True)
class Task:
    scenario: Scenario
    n: int
    replicate: int
    seed_sequence: np.random.SeedSequence


def cubic_profile(time_values: np.ndarray) -> np.ndarray:
    """Smooth path with a nonzero third derivative: g(u)=u+u^3/2."""
    time_values = np.asarray(time_values, dtype=float)
    return time_values + 0.5 * time_values**3


def discrepancy_profile(time_values: np.ndarray) -> np.ndarray:
    """Coherent bounded perturbation h(u)=1+sin(2*pi*u)/4."""
    time_values = np.asarray(time_values, dtype=float)
    return 1.0 + 0.25 * np.sin(2.0 * np.pi * time_values)


def load_configuration(path: Path, profile_name: str) -> dict[str, Any]:
    """Load and validate one resolved runtime profile."""
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if profile_name not in config.get("profiles", {}):
        raise ValueError(f"unknown profile: {profile_name}")

    profile = dict(config["profiles"][profile_name])
    experiment = dict(config["experiment"])
    estimator = dict(config["estimator"])
    analysis = dict(config["analysis"])
    discrepancy = dict(config["discrepancy"])
    resolved = {
        "profile_name": profile_name,
        "profile": profile,
        "experiment": experiment,
        "estimator": estimator,
        "analysis": analysis,
        "discrepancy": discrepancy,
        "config_path": path.resolve(),
    }
    validate_configuration(resolved)
    return resolved


def _parse_a(value: Any) -> float:
    if isinstance(value, str) and value.lower() in {"inf", "infinity"}:
        return float("inf")
    result = float(value)
    if result <= 0.0 or not np.isfinite(result):
        raise ValueError("finite discrepancy exponents must be positive")
    return result


def scenarios_from_configuration(config: dict[str, Any]) -> list[Scenario]:
    """Expand named regimes and discrepancy exponents into scenarios."""
    scenarios: list[Scenario] = []
    for regime in config["profile"]["regimes"]:
        if regime == "discrepancy_coherent":
            exponents = config["profile"].get("discrepancy_exponents", [])
            if not exponents:
                raise ValueError("discrepancy regime requires discrepancy_exponents")
            scenarios.extend(Scenario(regime, _parse_a(value)) for value in exponents)
        else:
            scenarios.append(Scenario(regime, None))
    return scenarios


def validate_configuration(config: dict[str, Any]) -> None:
    profile = config["profile"]
    experiment = config["experiment"]
    estimator = config["estimator"]
    analysis = config["analysis"]

    if experiment["geometry"] != "airm":
        raise ValueError("the first recorded centre-rate harness is AIRM-only")
    matrix_size = int(experiment["matrix_size"])
    if matrix_size < 2:
        raise ValueError("matrix_size must be at least two")
    if len(experiment["base_eigenvalues"]) != matrix_size:
        raise ValueError("base_eigenvalues must match matrix_size")
    if len(experiment["drift_direction_diagonal"]) != matrix_size:
        raise ValueError("drift_direction_diagonal must match matrix_size")
    if np.min(experiment["base_eigenvalues"]) <= 0.0:
        raise ValueError("base_eigenvalues must be positive")
    if experiment["centre_profile"] != "cubic":
        raise ValueError("unknown centre profile")
    if int(experiment["factor_rank"]) != 0:
        raise ValueError("B4.2 isolates centre estimation with factor_rank=0")

    n_values = [int(value) for value in profile["n_values"]]
    if len(n_values) < 1 or any(value < 8 for value in n_values):
        raise ValueError("n_values must contain positive usable sample sizes")
    if len(set(n_values)) != len(n_values):
        raise ValueError("n_values must be unique")
    if int(profile["replicates"]) < 1:
        raise ValueError("replicates must be positive")
    multipliers = np.asarray(profile["bandwidth_multipliers"], dtype=float)
    if multipliers.size == 0 or np.any(multipliers <= 0.0):
        raise ValueError("bandwidth multipliers must be positive")

    allowed_regimes = {
        "bias_only",
        "variance_only",
        "full",
        "discrepancy_coherent",
    }
    unknown = set(profile["regimes"]) - allowed_regimes
    if unknown:
        raise ValueError(f"unknown regimes: {sorted(unknown)}")

    overlap = np.asarray(estimator["overlap_fractions"], dtype=float)
    if overlap.shape != (2,) or not 0.0 < overlap[0] < overlap[1] < 1.0:
        raise ValueError("overlap_fractions must be two increasing interior values")
    largest_bandwidth = (
        float(estimator["bandwidth_constant"])
        * min(n_values) ** (-float(estimator["bandwidth_exponent"]))
        * float(np.max(multipliers))
    )
    boundary_width = min(float(overlap[0]), 1.0 - float(overlap[1]))
    if largest_bandwidth >= boundary_width:
        raise ValueError(
            "largest requested bandwidth violates the fixed-overlap boundary regions"
        )
    if int(profile["bootstrap_replicates"]) < 1:
        raise ValueError("bootstrap_replicates must be positive")
    band = np.asarray(analysis["compatibility_band"], dtype=float)
    if band.shape != (2,) or band[0] >= band[1]:
        raise ValueError("compatibility_band must be increasing")
    scenarios_from_configuration(config)


def build_tasks(config: dict[str, Any]) -> list[Task]:
    """Build stable, independently spawned DGP tasks."""
    profile = config["profile"]
    scenario_specs = scenarios_from_configuration(config)
    bare_tasks = [
        (scenario, int(n), replicate)
        for n in profile["n_values"]
        for replicate in range(int(profile["replicates"]))
        for scenario in scenario_specs
    ]
    seed_namespace = profile.get("seed_namespace")
    if seed_namespace is None:
        # Preserve the completed B4.2/N-LS-A seed map byte-for-byte.
        root_entropy: int | list[int] = int(config["experiment"]["root_seed"])
    else:
        root_entropy = [
            int(config["experiment"]["root_seed"]),
            int(seed_namespace),
        ]
    root = np.random.SeedSequence(root_entropy)
    data_root, _ = root.spawn(2)
    children = data_root.spawn(len(bare_tasks))
    return [
        Task(scenario, n, replicate, seed)
        for (scenario, n, replicate), seed in zip(bare_tasks, children)
    ]


def _base_and_direction(config: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    experiment = config["experiment"]
    base = np.diag(np.asarray(experiment["base_eigenvalues"], dtype=float))
    direction = np.diag(
        np.asarray(experiment["drift_direction_diagonal"], dtype=float)
    )
    return base, direction


def _target_and_actual_centre_configs(
    config: dict[str, Any],
    scenario: Scenario,
    n: int,
) -> tuple[CentrePathConfig, CentrePathConfig]:
    experiment = config["experiment"]
    base, direction = _base_and_direction(config)
    drift_scale = 0.0 if scenario.regime == "variance_only" else float(
        experiment["drift_scale"]
    )
    target = CentrePathConfig(
        base_centre=base,
        drift_direction=direction,
        drift_scale=drift_scale,
        profile=cubic_profile,
    )
    if scenario.regime != "discrepancy_coherent" or np.isinf(scenario.a_value):
        return target, target

    discrepancy_size = (
        float(config["discrepancy"]["amplitude"])
        * n ** (-float(scenario.a_value))
    )

    def actual_profile(time_values: np.ndarray) -> np.ndarray:
        return (
            drift_scale * cubic_profile(time_values)
            + discrepancy_size * discrepancy_profile(time_values)
        )

    actual = CentrePathConfig(
        base_centre=base,
        drift_direction=direction,
        drift_scale=1.0,
        profile=actual_profile,
    )
    return target, actual


def _dgp_config(
    config: dict[str, Any],
    scenario: Scenario,
    n: int,
) -> tuple[LSRFMConfig, CentrePathConfig]:
    experiment = config["experiment"]
    target_centre, actual_centre = _target_and_actual_centre_configs(
        config, scenario, n
    )
    noise_scale = 0.0 if scenario.regime == "bias_only" else float(
        experiment["noise_scale"]
    )
    result = LSRFMConfig(
        centre=actual_centre,
        factor=AR1FactorConfig(rank=0, persistence=0.0, scale=0.0),
        loading=LoadingConfig(orientation="random", structure="dense"),
        noise=NoiseConfig(
            scale=noise_scale,
            persistence=float(experiment["noise_persistence"]),
            constant_norm=bool(experiment["noise_constant_norm"]),
            structure="dense",
        ),
    )
    return result, target_centre


def _intrinsic_rms(
    geometry: GeometryOps,
    estimates: np.ndarray,
    targets: np.ndarray,
) -> float:
    return float(np.sqrt(np.mean(geometry.dist2(estimates, targets))))


def _broad_vertices(result: CentrePathEstimate, geometry: GeometryOps) -> np.ndarray:
    vertices = []
    for estimate in result.estimates:
        forward = estimate.forward
        backward = estimate.backward
        if forward is None:
            point = backward.stages.stages[0].point
        elif backward is None:
            point = forward.stages.stages[0].point
        else:
            point = geodesic_blend(
                forward.stages.stages[0].point,
                backward.stages.stages[0].point,
                estimate.blend_weight,
                geometry,
            )
        vertices.append(point)
    return np.stack(vertices)


def _stage_diagnostics(result: CentrePathEstimate) -> dict[str, Any]:
    stages = []
    reasons: list[str] = []
    for estimate in result.estimates:
        reasons.extend(estimate.fallback_reasons)
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is not None:
                stages.extend(one_sided.stages.stages)
    reason_counts: dict[str, int] = {}
    for reason in reasons:
        key = reason.split(":", 1)[0]
        reason_counts[key] = reason_counts.get(key, 0) + 1
    return {
        "fallback_reasons": json.dumps(reason_counts, sort_keys=True),
        "minimum_ess": min(stage.effective_sample_size for stage in stages),
        "minimum_support": min(stage.support_count for stage in stages),
        "maximum_iterations": max(stage.n_iter for stage in stages),
        "maximum_residual": max(stage.residual for stage in stages),
        "nonconverged_stages": sum(not stage.converged for stage in stages),
    }


def _spectral_diagnostics(
    observations: np.ndarray,
    estimates: np.ndarray,
) -> dict[str, float]:
    observation_eigenvalues = np.linalg.eigvalsh(observations)
    estimated_eigenvalues = np.linalg.eigvalsh(estimates)
    return {
        "observation_min_eigenvalue": float(np.min(observation_eigenvalues)),
        "observation_max_condition": float(
            np.max(
                observation_eigenvalues[..., -1]
                / observation_eigenvalues[..., 0]
            )
        ),
        "estimated_min_eigenvalue": float(np.min(estimated_eigenvalues)),
    }


def _paired_frozen_observations(
    sample,
    target_centres: np.ndarray,
    geometry: GeometryOps,
    base: np.ndarray,
) -> np.ndarray:
    reference_factor = geometry.transport(
        sample.factor_effects, sample.centres, base
    )
    reference_noise = geometry.transport(sample.tangent_noise, sample.centres, base)
    frozen_tangent = geometry.transport(
        reference_factor + reference_noise,
        base,
        target_centres,
    )
    return geometry.exp(target_centres, frozen_tangent)


def _empty_error_row(
    config: dict[str, Any],
    task: Task,
    bandwidth_multiplier: float,
    bandwidth: float,
    n_cells: int,
    error: Exception,
) -> dict[str, Any]:
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update(
        {
            "profile": config["profile_name"],
            "regime": task.scenario.regime,
            "a_label": task.scenario.a_label,
            "a_value": task.scenario.a_value,
            "n": task.n,
            "replicate": task.replicate,
            "bandwidth_multiplier": bandwidth_multiplier,
            "bandwidth": bandwidth,
            "n_cells": n_cells,
            "seed_spawn_key": ".".join(map(str, task.seed_sequence.spawn_key)),
            "status": "error",
            "error_type": type(error).__name__,
            "error_message": str(error).replace("\n", " ")[:500],
        }
    )
    return row


def run_task(
    config: dict[str, Any],
    task: Task,
    geometry: GeometryOps,
    requested_multipliers: Iterable[float],
    example_dir: Path,
) -> list[dict[str, Any]]:
    """Generate one common draw and evaluate all missing bandwidths."""
    estimator = config["estimator"]
    rng = np.random.default_rng(task.seed_sequence)
    dgp_config, target_centre_config = _dgp_config(
        config, task.scenario, task.n
    )
    sample = generate_lsrfm(rng, task.n, geometry, dgp_config)
    target_centres = centre_path(
        sample.time, geometry, target_centre_config
    )
    base = target_centre_config.base_centre
    frozen_observations = _paired_frozen_observations(
        sample, target_centres, geometry, base
    )
    paired_discrepancy_rms = _intrinsic_rms(
        geometry, sample.observations, frozen_observations
    )
    actual_centre_rms = _intrinsic_rms(
        geometry, sample.centres, target_centres
    )

    centre_rate = task.n ** (-float(estimator["polygon_rate_exponent"]))
    n_cells = polygon_cell_count(
        centre_rate,
        constant=float(estimator["polygon_cell_constant"]),
    )
    vertex_times = regular_polygon_grid(n_cells)
    true_vertices = centre_path(vertex_times, geometry, target_centre_config)
    rows = []
    for bandwidth_multiplier in requested_multipliers:
        bandwidth = (
            float(estimator["bandwidth_constant"])
            * task.n ** (-float(estimator["bandwidth_exponent"]))
            * float(bandwidth_multiplier)
        )
        started = time.perf_counter()
        try:
            result = estimate_centre_path(
                observations=sample.observations,
                time=sample.time,
                vertex_times=vertex_times,
                bandwidth=bandwidth,
                geometry=geometry,
                overlap_fractions=tuple(estimator["overlap_fractions"]),
                mean_tol=float(estimator["mean_tolerance"]),
                max_iter=int(estimator["mean_max_iter"]),
            )
            corrected_path = evaluate_polygon(result.polygon, sample.time).points
            broad_vertices = _broad_vertices(result, geometry)
            broad_frame = PolygonalFrame(vertex_times, broad_vertices, geometry)
            broad_path = evaluate_polygon(broad_frame, sample.time).points

            path_distances = np.sqrt(
                geometry.dist2(corrected_path, target_centres)
            )
            path_rms = float(np.sqrt(np.mean(path_distances**2)))
            broad_path_rms = _intrinsic_rms(
                geometry, broad_path, target_centres
            )
            diagnostics = _stage_diagnostics(result)
            row = {
                "profile": config["profile_name"],
                "regime": task.scenario.regime,
                "a_label": task.scenario.a_label,
                "a_value": task.scenario.a_value,
                "n": task.n,
                "replicate": task.replicate,
                "bandwidth_multiplier": float(bandwidth_multiplier),
                "bandwidth": bandwidth,
                "n_cells": n_cells,
                "seed_spawn_key": ".".join(map(str, task.seed_sequence.spawn_key)),
                "status": "ok",
                "error_type": "",
                "error_message": "",
                "path_rms": path_rms,
                "vertex_rms": _intrinsic_rms(
                    geometry, result.vertices, true_vertices
                ),
                "path_sup": float(np.max(path_distances)),
                "broad_path_rms": broad_path_rms,
                "richardson_gain": broad_path_rms / path_rms
                if path_rms > 0.0
                else np.inf,
                "actual_centre_rms": actual_centre_rms,
                "paired_discrepancy_rms": paired_discrepancy_rms,
                "fallback_count": result.fallback_count,
                "fallback_rate": result.fallback_rate,
                **diagnostics,
                **_spectral_diagnostics(sample.observations, result.vertices),
                "elapsed_seconds": time.perf_counter() - started,
            }
            rows.append(row)

            is_example = (
                task.replicate == 0
                and task.n == max(config["profile"]["n_values"])
                and np.isclose(float(bandwidth_multiplier), 1.0)
            )
            if is_example:
                example_dir.mkdir(parents=True, exist_ok=True)
                example_path = example_dir / (
                    f"{task.scenario.label.replace('=', '_')}_n{task.n}.npz"
                )
                np.savez_compressed(
                    example_path,
                    time=sample.time,
                    corrected_error=path_distances,
                    broad_error=np.sqrt(
                        geometry.dist2(broad_path, target_centres)
                    ),
                    vertex_times=vertex_times,
                    vertex_error=np.sqrt(
                        geometry.dist2(result.vertices, true_vertices)
                    ),
                )
        except Exception as error:  # recorded as data; never silently dropped
            rows.append(
                _empty_error_row(
                    config,
                    task,
                    float(bandwidth_multiplier),
                    bandwidth,
                    n_cells,
                    error,
                )
            )
    return rows


def _row_key(row: dict[str, Any] | pd.Series) -> tuple[Any, ...]:
    return (
        str(row["regime"]),
        str(row["a_label"]),
        int(row["n"]),
        int(row["replicate"]),
        round(float(row["bandwidth_multiplier"]), 12),
    )


def read_existing_rows(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=RAW_COLUMNS)
    return pd.read_csv(path, keep_default_na=False, na_values=["nan", "NaN"])


def append_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=RAW_COLUMNS)
        if write_header:
            writer.writeheader()
        writer.writerows(rows)
        handle.flush()


def _cell_summary(raw: pd.DataFrame) -> pd.DataFrame:
    ok = raw.loc[raw["status"] == "ok"].copy()
    if ok.empty:
        return pd.DataFrame()
    group_columns = ["regime", "a_label", "bandwidth_multiplier", "n"]
    metrics = [
        "path_rms",
        "vertex_rms",
        "path_sup",
        "broad_path_rms",
        "richardson_gain",
        "actual_centre_rms",
        "paired_discrepancy_rms",
        "fallback_rate",
        "minimum_ess",
        "maximum_iterations",
        "elapsed_seconds",
    ]
    records = []
    for keys, group in ok.groupby(group_columns, sort=True, dropna=False):
        record = dict(zip(group_columns, keys))
        record["completed"] = len(group)
        for metric in metrics:
            values = pd.to_numeric(group[metric], errors="coerce").dropna().to_numpy()
            if values.size == 0:
                continue
            record[f"{metric}_mean"] = float(np.mean(values))
            record[f"{metric}_median"] = float(np.median(values))
            record[f"{metric}_sd"] = float(np.std(values, ddof=1)) if values.size > 1 else 0.0
            for quantile, label in (
                (0.05, "q05"),
                (0.25, "q25"),
                (0.75, "q75"),
                (0.95, "q95"),
            ):
                record[f"{metric}_{label}"] = float(np.quantile(values, quantile))
        records.append(record)
    return pd.DataFrame.from_records(records)


def _fit_log_slope(n_values: np.ndarray, values: np.ndarray) -> float:
    usable = np.isfinite(values) & (values > 0.0) & np.isfinite(n_values)
    if np.count_nonzero(usable) < 2:
        return np.nan
    return float(np.polyfit(np.log(n_values[usable]), np.log(values[usable]), 1)[0])


def _bootstrap_slopes(
    raw: pd.DataFrame,
    config: dict[str, Any],
) -> pd.DataFrame:
    ok = raw.loc[raw["status"] == "ok"].copy()
    if ok.empty:
        return pd.DataFrame()
    profile = config["profile"]
    root = np.random.SeedSequence(int(config["experiment"]["root_seed"]))
    _, bootstrap_root = root.spawn(2)
    rng = np.random.default_rng(bootstrap_root)
    fit_min = int(profile["slope_fit_n_min"])
    n_bootstrap = int(profile["bootstrap_replicates"])
    group_columns = ["regime", "a_label", "bandwidth_multiplier"]
    metrics = ["path_rms", "broad_path_rms", "paired_discrepancy_rms"]
    records = []
    for keys, group in ok.groupby(group_columns, sort=True, dropna=False):
        group = group.loc[group["n"] >= fit_min]
        n_values = np.asarray(sorted(group["n"].unique()), dtype=float)
        if n_values.size < 2:
            continue
        for metric in metrics:
            if metric == "paired_discrepancy_rms" and keys[0] != "discrepancy_coherent":
                continue
            arrays = [
                pd.to_numeric(
                    group.loc[group["n"] == n, metric], errors="coerce"
                ).dropna().to_numpy(dtype=float)
                for n in n_values
            ]
            if any(values.size == 0 for values in arrays):
                continue
            cell_medians = np.asarray([np.median(values) for values in arrays])
            if metric == "paired_discrepancy_rms" and np.max(cell_medians) < 1e-14:
                continue
            point = _fit_log_slope(n_values, cell_medians)
            if not np.isfinite(point):
                continue
            bootstrap = np.empty(n_bootstrap)
            for index in range(n_bootstrap):
                resampled_medians = np.asarray(
                    [
                        np.median(rng.choice(values, size=values.size, replace=True))
                        for values in arrays
                    ]
                )
                bootstrap[index] = _fit_log_slope(n_values, resampled_medians)
            record = dict(zip(group_columns, keys))
            record.update(
                {
                    "metric": metric,
                    "n_min": int(np.min(n_values)),
                    "n_max": int(np.max(n_values)),
                    "n_scales": int(n_values.size),
                    "slope": point,
                    "slope_q025": float(np.nanquantile(bootstrap, 0.025)),
                    "slope_q50": float(np.nanquantile(bootstrap, 0.5)),
                    "slope_q975": float(np.nanquantile(bootstrap, 0.975)),
                }
            )
            records.append(record)
    return pd.DataFrame.from_records(records)


def _local_slopes(summary: pd.DataFrame) -> pd.DataFrame:
    if summary.empty:
        return pd.DataFrame()
    records = []
    for keys, group in summary.groupby(
        ["regime", "a_label", "bandwidth_multiplier"],
        sort=True,
        dropna=False,
    ):
        group = group.sort_values("n")
        n_values = group["n"].to_numpy(dtype=float)
        values = group["path_rms_median"].to_numpy(dtype=float)
        for left in range(len(group) - 1):
            slope = np.log(values[left + 1] / values[left]) / np.log(
                n_values[left + 1] / n_values[left]
            )
            records.append(
                {
                    "regime": keys[0],
                    "a_label": keys[1],
                    "bandwidth_multiplier": keys[2],
                    "n_left": int(n_values[left]),
                    "n_right": int(n_values[left + 1]),
                    "local_slope": float(slope),
                }
            )
    return pd.DataFrame.from_records(records)


def _scenario_label(regime: str, a_label: str) -> str:
    return f"a={a_label}" if regime == "discrepancy_coherent" else regime


def _style_axes(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.22)


def _plot_rate_panels(summary: pd.DataFrame, output: Path) -> None:
    if summary.empty:
        return
    groups = list(summary.groupby(["regime", "a_label"], sort=True, dropna=False))
    n_columns = min(3, len(groups))
    n_rows = int(np.ceil(len(groups) / n_columns))
    fig, axes = plt.subplots(
        n_rows,
        n_columns,
        figsize=(5.2 * n_columns, 4.2 * n_rows),
        squeeze=False,
    )
    reference_slope = -3.0 / 7.0
    for panel, ((regime, a_label), group) in enumerate(groups):
        ax = axes.flat[panel]
        for line_index, (multiplier, line) in enumerate(
            group.groupby("bandwidth_multiplier", sort=True)
        ):
            line = line.sort_values("n")
            color = PALETTE[line_index % len(PALETTE)]
            style = LINE_STYLES[line_index % len(LINE_STYLES)]
            ax.plot(
                line["n"],
                line["path_rms_median"],
                marker="o",
                linestyle=style,
                color=color,
                label=f"{multiplier:g}× bandwidth",
            )
            ax.fill_between(
                line["n"].to_numpy(dtype=float),
                line["path_rms_q25"].to_numpy(dtype=float),
                line["path_rms_q75"].to_numpy(dtype=float),
                color=color,
                alpha=0.14,
            )
        anchor = group.loc[
            np.isclose(group["bandwidth_multiplier"], 1.0)
        ].sort_values("n")
        if anchor.empty:
            anchor = group.sort_values("n")
        first = anchor.iloc[0]
        n_reference = np.asarray(sorted(group["n"].unique()), dtype=float)
        reference = float(first["path_rms_median"]) * (
            n_reference / float(first["n"])
        ) ** reference_slope
        ax.plot(
            n_reference,
            reference,
            color="#555555",
            linestyle=(0, (5, 3)),
            linewidth=1.4,
            label="−3/7 reference",
        )
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_title(_scenario_label(str(regime), str(a_label)))
        ax.set_xlabel("observations n")
        ax.set_ylabel("intrinsic path RMS")
        _style_axes(ax)
        ax.legend(fontsize=8)
    for panel in range(len(groups), axes.size):
        axes.flat[panel].set_visible(False)
    fig.suptitle("Moving-centre RMS against the n⁻³ᐟ⁷ reference", fontweight="bold")
    fig.tight_layout()
    fig.savefig(output / "01_rate_rms.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _plot_scaled_rate(summary: pd.DataFrame, output: Path) -> None:
    if summary.empty:
        return
    central = summary.loc[np.isclose(summary["bandwidth_multiplier"], 1.0)].copy()
    if central.empty:
        return
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    for index, ((regime, a_label), group) in enumerate(
        central.groupby(["regime", "a_label"], sort=True, dropna=False)
    ):
        group = group.sort_values("n")
        scaled = group["path_rms_median"] * group["n"] ** (3.0 / 7.0)
        ax.plot(
            group["n"],
            scaled,
            marker="o",
            color=PALETTE[index % len(PALETTE)],
            linestyle=LINE_STYLES[index % len(LINE_STYLES)],
            label=_scenario_label(str(regime), str(a_label)),
        )
    ax.set_xscale("log", base=2)
    ax.set_xlabel("observations n")
    ax.set_ylabel("scaled RMS  n³ᐟ⁷ Eₙ")
    ax.set_title("A horizontal curve is compatible with the headline rate", fontweight="bold")
    _style_axes(ax)
    ax.legend(fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(output / "02_scaled_rms.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _plot_correction_gain(summary: pd.DataFrame, output: Path) -> None:
    if summary.empty:
        return
    central = summary.loc[np.isclose(summary["bandwidth_multiplier"], 1.0)].copy()
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    for index, ((regime, a_label), group) in enumerate(
        central.groupby(["regime", "a_label"], sort=True, dropna=False)
    ):
        group = group.sort_values("n")
        ax.plot(
            group["n"],
            group["richardson_gain_median"],
            marker="o",
            color=PALETTE[index % len(PALETTE)],
            linestyle=LINE_STYLES[index % len(LINE_STYLES)],
            label=_scenario_label(str(regime), str(a_label)),
        )
    ax.axhline(1.0, color="#555555", linestyle="--", linewidth=1.2)
    ax.set_xscale("log", base=2)
    ax.set_xlabel("observations n")
    ax.set_ylabel("broad-stage RMS / corrected RMS")
    ax.set_title("Values above one mean Richardson improved RMS", fontweight="bold")
    _style_axes(ax)
    ax.legend(fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(output / "03_richardson_gain.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _plot_health(summary: pd.DataFrame, output: Path) -> None:
    if summary.empty:
        return
    central = summary.loc[np.isclose(summary["bandwidth_multiplier"], 1.0)].copy()
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    for index, ((regime, a_label), group) in enumerate(
        central.groupby(["regime", "a_label"], sort=True, dropna=False)
    ):
        group = group.sort_values("n")
        label = _scenario_label(str(regime), str(a_label))
        color = PALETTE[index % len(PALETTE)]
        style = LINE_STYLES[index % len(LINE_STYLES)]
        axes[0].plot(
            group["n"], group["fallback_rate_mean"], marker="o",
            color=color, linestyle=style, label=label,
        )
        axes[1].plot(
            group["n"], group["minimum_ess_median"], marker="o",
            color=color, linestyle=style, label=label,
        )
    axes[0].set_title("Observable fallback rate")
    axes[0].set_ylabel("fraction of vertices")
    axes[1].set_title("Smallest three-scale effective sample size")
    axes[1].set_ylabel("effective observations")
    for ax in axes:
        ax.set_xscale("log", base=2)
        ax.set_xlabel("observations n")
        _style_axes(ax)
    axes[1].legend(fontsize=8)
    fig.suptitle("Estimator health is reported, never filtered away", fontweight="bold")
    fig.tight_layout()
    fig.savefig(output / "04_health.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _plot_pointwise_examples(example_dir: Path, output: Path) -> None:
    paths = sorted(example_dir.glob("*.npz")) if example_dir.exists() else []
    if not paths:
        return
    n_columns = min(3, len(paths))
    n_rows = int(np.ceil(len(paths) / n_columns))
    fig, axes = plt.subplots(
        n_rows, n_columns, figsize=(5.2 * n_columns, 3.8 * n_rows), squeeze=False
    )
    for index, path in enumerate(paths):
        with np.load(path) as data:
            ax = axes.flat[index]
            ax.plot(data["time"], data["broad_error"], color="#999999", label="broad")
            ax.plot(data["time"], data["corrected_error"], color=PALETTE[0], label="corrected")
            ax.scatter(
                data["vertex_times"], data["vertex_error"], s=14,
                color=PALETTE[1], label="vertices", zorder=3,
            )
            ax.set_title(path.stem.replace("_", " "))
            ax.set_xlabel("rescaled time u")
            ax.set_ylabel("intrinsic error")
            _style_axes(ax)
            ax.legend(fontsize=8)
    for index in range(len(paths), axes.size):
        axes.flat[index].set_visible(False)
    fig.suptitle("Where along the path the centre error occurs", fontweight="bold")
    fig.tight_layout()
    fig.savefig(output / "05_pointwise_examples.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _plot_discrepancy(summary: pd.DataFrame, output: Path) -> None:
    subset = summary.loc[
        (summary["regime"] == "discrepancy_coherent")
        & np.isclose(summary["bandwidth_multiplier"], 1.0)
    ].copy()
    if subset.empty:
        return
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    for index, (a_label, group) in enumerate(subset.groupby("a_label", sort=True)):
        group = group.sort_values("n")
        color = PALETTE[index % len(PALETTE)]
        style = LINE_STYLES[index % len(LINE_STYLES)]
        axes[0].plot(
            group["n"], group["paired_discrepancy_rms_median"],
            marker="o", color=color, linestyle=style, label=f"a={a_label}",
        )
        axes[1].plot(
            group["n"], group["path_rms_median"],
            marker="o", color=color, linestyle=style, label=f"a={a_label}",
        )
    for ax in axes:
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xlabel("observations n")
        _style_axes(ax)
    axes[0].set_title("Paired actual/frozen discrepancy")
    axes[0].set_ylabel("paired intrinsic RMS")
    axes[1].set_title("Resulting moving-centre error")
    axes[1].set_ylabel("intrinsic path RMS")
    axes[1].legend(fontsize=8, ncol=2)
    fig.suptitle("The controlled n⁻ᵃ channel and its 3/7 transition", fontweight="bold")
    fig.tight_layout()
    fig.savefig(output / "06_discrepancy_phase.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _write_report(
    raw: pd.DataFrame,
    summary: pd.DataFrame,
    slopes: pd.DataFrame,
    output: Path,
    config: dict[str, Any],
) -> None:
    requested = (
        len(scenarios_from_configuration(config))
        * len(config["profile"]["n_values"])
        * int(config["profile"]["replicates"])
        * len(config["profile"]["bandwidth_multipliers"])
    )
    completed = int((raw["status"] == "ok").sum()) if not raw.empty else 0
    errors = int((raw["status"] == "error").sum()) if not raw.empty else 0
    lines = [
        f"# {config['profile_name']} centre experiment",
        "",
        "Numerical diagnostic only: these results cannot prove an analytical theorem.",
        "",
        f"- requested rows: {requested}",
        f"- completed rows: {completed}",
        f"- recorded errors: {errors}",
        f"- completion fraction: {completed / requested:.3f}" if requested else "- completion fraction: n/a",
        f"- root seed: {config['experiment']['root_seed']}",
        f"- numpy: {np.__version__}",
        f"- python: {platform.python_version()}",
        "",
        "## Fitted slopes",
        "",
    ]
    if slopes.empty:
        lines.append("Not enough completed sample-size scales to fit slopes yet.")
    else:
        display_columns = [
            "regime", "a_label", "bandwidth_multiplier", "metric",
            "slope", "slope_q025", "slope_q975", "n_min", "n_max",
        ]
        lines.extend(
            [
                "| " + " | ".join(display_columns) + " |",
                "|" + "---|" * len(display_columns),
            ]
        )
        for _, row in slopes.iterrows():
            values = []
            for column in display_columns:
                value = row[column]
                if column.startswith("slope"):
                    values.append(f"{float(value):.4f}")
                else:
                    values.append(str(value))
            lines.append("| " + " | ".join(values) + " |")
    lines += [
        "",
        "## Files",
        "",
        "- `raw.csv`: one row per replication and bandwidth; errors are retained.",
        "- `summary.csv`: means, medians, spread and quantiles by cell.",
        "- `slopes.csv`: fitted slopes and within-cell bootstrap intervals.",
        "- `local_slopes.csv`: adjacent-sample-size slopes.",
        "- `plots/`: rate, scaled-rate, correction, health and path figures.",
        "",
    ]
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")


def summarize_and_plot(config: dict[str, Any], output: Path) -> None:
    raw_path = output / "raw.csv"
    raw = read_existing_rows(raw_path)
    if raw.empty:
        print("No rows available to summarize.")
        return
    summary = _cell_summary(raw)
    slopes = _bootstrap_slopes(raw, config)
    local_slopes = _local_slopes(summary)
    summary.to_csv(output / "summary.csv", index=False)
    slopes.to_csv(output / "slopes.csv", index=False)
    local_slopes.to_csv(output / "local_slopes.csv", index=False)

    plot_dir = output / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)
    _plot_rate_panels(summary, plot_dir)
    _plot_scaled_rate(summary, plot_dir)
    _plot_correction_gain(summary, plot_dir)
    _plot_health(summary, plot_dir)
    _plot_pointwise_examples(output / "examples", plot_dir)
    _plot_discrepancy(summary, plot_dir)
    _write_report(raw, summary, slopes, output, config)
    print(f"summaries and plots -> {output.relative_to(ROOT)}")


def _configuration_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _resolved_profile_digest(profile: dict[str, Any]) -> str:
    encoded = json.dumps(profile, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


def initialize_output(config: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    metadata_path = output / "metadata.json"
    metadata = {
        "profile": config["profile_name"],
        "recorded": bool(config["profile"]["recorded"]),
        "config_sha256": _configuration_digest(config["config_path"]),
        "resolved_profile_sha256": _resolved_profile_digest(config["profile"]),
        "root_seed": int(config["experiment"]["root_seed"]),
        "numpy": np.__version__,
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    if config["profile"].get("seed_namespace") is not None:
        metadata["seed_namespace"] = int(config["profile"]["seed_namespace"])
    if metadata_path.exists():
        existing = json.loads(metadata_path.read_text(encoding="utf-8"))
        for key in ("profile", "config_sha256", "root_seed"):
            if existing.get(key) != metadata[key]:
                raise RuntimeError(
                    f"existing output metadata disagrees on {key}; use a new output directory"
                )
        # Older completed outputs predate the resolved-profile lock. New
        # outputs carry it and therefore reject silent runtime-profile changes.
        for key in ("resolved_profile_sha256", "seed_namespace"):
            if key in existing and existing.get(key) != metadata.get(key):
                raise RuntimeError(
                    f"existing output metadata disagrees on {key}; use a new output directory"
                )
    else:
        metadata_path.write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        shutil.copy2(config["config_path"], output / "centre_rate.yaml")


def print_workload(config: dict[str, Any], tasks: list[Task]) -> None:
    profile = config["profile"]
    rows = len(tasks) * len(profile["bandwidth_multipliers"])
    print(f"profile: {config['profile_name']}")
    print(f"recorded: {profile['recorded']}")
    print(f"output: {profile['output_dir']}")
    print(f"scenarios: {', '.join(s.label for s in scenarios_from_configuration(config))}")
    print(f"n values: {profile['n_values']}")
    print(f"replicates: {profile['replicates']}")
    print(f"bandwidth multipliers: {profile['bandwidth_multipliers']}")
    print(f"DGP tasks: {len(tasks)}")
    print(f"requested result rows: {rows}")


def run(
    config: dict[str, Any],
    *,
    max_tasks: int | None = None,
    plot_only: bool = False,
) -> None:
    profile = config["profile"]
    output = (ROOT / profile["output_dir"]).resolve()
    initialize_output(config, output)
    if plot_only:
        summarize_and_plot(config, output)
        return

    raw_path = output / "raw.csv"
    existing = read_existing_rows(raw_path)
    completed_keys = {_row_key(row) for _, row in existing.iterrows()}
    tasks = build_tasks(config)
    task_limit = len(tasks) if max_tasks is None else min(max_tasks, len(tasks))
    processed_tasks = 0
    for task_index, task in enumerate(tasks, start=1):
        missing = [
            float(multiplier)
            for multiplier in profile["bandwidth_multipliers"]
            if (
                task.scenario.regime,
                task.scenario.a_label,
                task.n,
                task.replicate,
                round(float(multiplier), 12),
            )
            not in completed_keys
        ]
        if not missing:
            continue
        if processed_tasks >= task_limit:
            break
        print(
            f"[{task_index}/{len(tasks)}] {task.scenario.label}, "
            f"n={task.n}, rep={task.replicate}, bandwidth_multipliers={missing}",
            flush=True,
        )
        try:
            rows = run_task(
                config,
                task,
                AIRM_GEOMETRY,
                missing,
                output / "examples",
            )
        except Exception as error:
            estimator = config["estimator"]
            centre_rate = task.n ** (-float(estimator["polygon_rate_exponent"]))
            n_cells = polygon_cell_count(
                centre_rate,
                constant=float(estimator["polygon_cell_constant"]),
            )
            rows = []
            for multiplier in missing:
                bandwidth = (
                    float(estimator["bandwidth_constant"])
                    * task.n ** (-float(estimator["bandwidth_exponent"]))
                    * multiplier
                )
                rows.append(
                    _empty_error_row(
                        config, task, multiplier, bandwidth, n_cells, error
                    )
                )
        append_rows(raw_path, rows)
        completed_keys.update(_row_key(row) for row in rows)
        processed_tasks += 1

    summarize_and_plot(config, output)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=CONFIG_DEFAULT,
        help="operational YAML configuration",
    )
    parser.add_argument(
        "--profile",
        choices=("smoke", "centre_rate", "discrepancy"),
        default="smoke",
    )
    parser.add_argument(
        "--max-tasks",
        type=int,
        default=None,
        help="run at most this many unfinished DGP tasks before summarizing",
    )
    parser.add_argument(
        "--plot-only",
        action="store_true",
        help="regenerate summaries and plots without simulation",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and print the workload without writing outputs",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config_path = args.config.resolve()
    config = load_configuration(config_path, args.profile)
    tasks = build_tasks(config)
    print_workload(config, tasks)
    if args.dry_run:
        return 0
    if args.max_tasks is not None and args.max_tasks < 1:
        raise ValueError("max-tasks must be positive")
    try:
        run(config, max_tasks=args.max_tasks, plot_only=args.plot_only)
    except KeyboardInterrupt:
        print("\nInterrupted. Completed rows are already on disk; rerun to resume.")
        output = (ROOT / config["profile"]["output_dir"]).resolve()
        summarize_and_plot(config, output)
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
