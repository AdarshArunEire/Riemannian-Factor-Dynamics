"""Run the paired low-n factor-amplitude attribution diagnostic.

The four primary variants form a descriptive 2x2 crossing:

* oracle rows / true loadings (OT): pointwise-noise floor;
* oracle rows / feasible loadings (OF): loading-space cost on clean rows;
* feasible rows / true loadings (FT): centre/frame-row cost;
* feasible rows / feasible loadings (FF): complete RFD.

Oracle rows / oracle-estimated loadings (OO) and the fixed-centre estimator are
reported as contextual benchmarks.  Nothing is tuned or learned.  Output is
append-only and resumable, and only the parent process writes ``raw.csv``.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import platform
import shutil
import sys
import time
from pathlib import Path
from typing import Any

for _name in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[_name] = "1"

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_b45_comparators import _fit_rows, evaluate_comparators  # noqa: E402
from run_end_to_end import GEOMETRIES, _model_config  # noqa: E402
from run_paper1_controls import (  # noqa: E402
    ControlTask,
    _active_config,
    _production_multiplier,
    generate_control_sample,
    load_configuration as load_control_configuration,
)
from rfd.estimators.lag import (  # noqa: E402
    coordinate_tangents,
    tangent_coordinates,
)
from rfd.model import fit_rfd  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "amplitude_diagnostic.yaml"
VARIANTS = ("ot", "oo", "ft", "of", "ff")
METRICS = ("nrmse", "calibrated_nrmse", "norm_ratio", "cosine", "scale")
RAW_COLUMNS = [
    "profile", "n", "replicate", "seed_key", "status", "error_type",
    "error_message", "matrix_size", "tangent_dimension", "true_rank",
    "centre_path_rms", "loading_error", "fixed_nrmse", "elapsed_seconds",
] + [f"{variant}_{metric}" for variant in VARIANTS for metric in METRICS]


def load_configuration(path: Path, profile_name: str) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        own = yaml.safe_load(handle)
    profiles = own.get("profiles", {})
    if profile_name not in profiles:
        raise ValueError(f"unknown profile: {profile_name}")
    source_path = (ROOT / own["experiment"]["source_config"]).resolve()
    base = load_control_configuration(source_path, "control_core")
    regime = str(own["experiment"]["source_regime"])
    if regime not in base["core_regimes"]:
        raise ValueError(f"unknown source regime: {regime}")
    profile = dict(profiles[profile_name])
    n_values = [int(value) for value in profile.get("n_values", [])]
    if not n_values or min(n_values) < 16:
        raise ValueError("n_values must be nonempty and at least 16")
    if int(profile.get("replicates", 0)) < 1:
        raise ValueError("replicates must be positive")
    base.update({
        "profile_name": profile_name,
        "profile": profile,
        "analysis": dict(own["analysis"]),
        "config_path": path.resolve(),
        "source_config_path": source_path,
        "source_regime": regime,
    })
    return base


def build_tasks(config: dict[str, Any]) -> list[ControlTask]:
    regime = config["source_regime"]
    specification = dict(config["core_regimes"][regime])
    return [
        ControlTask(int(n), replicate, regime, specification)
        for n in config["profile"]["n_values"]
        for replicate in range(int(config["profile"]["replicates"]))
    ]


def aligned_score_metrics(
    estimated: np.ndarray, target: np.ndarray
) -> dict[str, float]:
    """Orthogonally align scores, then measure shape and scalar attenuation."""
    estimated = np.asarray(estimated, dtype=float)
    target = np.asarray(target, dtype=float)
    if estimated.shape != target.shape or estimated.ndim != 2:
        raise ValueError("estimated and target scores must be equal 2D arrays")
    target_norm = float(np.linalg.norm(target))
    if target_norm <= 0.0 or not np.isfinite(target_norm):
        raise ValueError("target factor norm must be finite and positive")
    left, _, right = np.linalg.svd(estimated.T @ target, full_matrices=False)
    aligned = estimated @ (left @ right)
    estimated_norm = float(np.linalg.norm(aligned))
    nrmse = float(np.linalg.norm(aligned - target) / target_norm)
    denominator = float(np.sum(aligned * aligned))
    scale = float(np.sum(aligned * target) / denominator) if denominator > 0 else np.nan
    calibrated = (
        float(np.linalg.norm(scale * aligned - target) / target_norm)
        if np.isfinite(scale) else np.nan
    )
    cosine = (
        float(np.sum(aligned * target) / (estimated_norm * target_norm))
        if estimated_norm > 0 else np.nan
    )
    return {
        "nrmse": nrmse,
        "calibrated_nrmse": calibrated,
        "norm_ratio": estimated_norm / target_norm,
        "cosine": cosine,
        "scale": scale,
    }


def _true_loading_coordinates(sample, point, basis, base, geometry) -> np.ndarray:
    loadings = (
        sample.loadings if np.array_equal(point, base)
        else geometry.transport(sample.loadings, base, point)
    )
    return tangent_coordinates(loadings, point, basis, geometry)


def evaluate_task(config: dict[str, Any], task: ControlTask) -> dict[str, float]:
    geometry = GEOMETRIES[config["experiment"]["geometry"]]
    sample, base, _ = generate_control_sample(config, task, geometry)
    active = _active_config(config, task)
    model_config = _model_config(
        active, task, multiplier=_production_multiplier(active, task.n)
    )
    fit = fit_rfd(sample.observations, sample.time, geometry, model_config)
    target = sample.factors - sample.factors.mean(axis=0)

    base_basis = geometry.tangent_basis(base)
    oracle_local = geometry.log(sample.centres, sample.observations)
    oracle_reference = geometry.transport(oracle_local, sample.centres, base)
    oracle_rows = tangent_coordinates(
        oracle_reference, base, base_basis, geometry
    )
    oracle_lag, _, oracle_factors = _fit_rows(oracle_rows, active)
    oracle_centred = oracle_lag.centred_rows
    true_base = _true_loading_coordinates(
        sample, base, base_basis, base, geometry
    )

    feasible_point = fit.centre.polygon.reference_point
    true_feasible = _true_loading_coordinates(
        sample, feasible_point, fit.tangent_rows.basis, base, geometry
    )
    feasible_vectors = coordinate_tangents(
        fit.loadings.T, fit.tangent_rows.basis
    )
    feasible_at_base = geometry.transport(
        feasible_vectors, feasible_point, base
    )
    feasible_base = tangent_coordinates(
        feasible_at_base, base, base_basis, geometry
    )

    scores = {
        "ot": oracle_centred @ true_base.T,
        "oo": oracle_factors.factor_scores,
        "ft": fit.lag_row.centred_rows @ true_feasible.T,
        "of": oracle_centred @ feasible_base.T,
        "ff": fit.factor_scores,
    }
    result: dict[str, float] = {}
    for variant, values in scores.items():
        for metric, value in aligned_score_metrics(values, target).items():
            result[f"{variant}_{metric}"] = value

    comparators = evaluate_comparators(sample, geometry, active, base)
    result["fixed_nrmse"] = float(comparators["fixed_centre_factor_nrmse"])
    result["centre_path_rms"] = float(comparators["global_mean_centre_path_rms"])
    truth_projector = true_base.T @ true_base
    feasible_projector = feasible_base.T @ feasible_base
    result["loading_error"] = float(
        np.linalg.norm(feasible_projector - truth_projector, ord=2)
    )
    return result


def run_task(config: dict[str, Any], task: ControlTask) -> dict[str, Any]:
    started = time.perf_counter()
    m = int(config["experiment"]["matrix_size"])
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": config["profile_name"], "n": task.n,
        "replicate": task.replicate,
        "seed_key": f"{config['profile']['seed_namespace']}.{task.n}.{task.replicate}",
        "matrix_size": m, "tangent_dimension": m * (m + 1) // 2,
        "true_rank": int(task.specification["rank"]),
    })
    try:
        row.update(evaluate_task(config, task))
        row.update({"status": "ok", "error_type": "", "error_message": ""})
    except Exception as error:
        row.update({
            "status": "error", "error_type": type(error).__name__,
            "error_message": str(error).replace("\n", " ")[:500],
        })
    row["elapsed_seconds"] = time.perf_counter() - started
    return row


def _row_key(row) -> tuple[int, int]:
    return int(row["n"]), int(row["replicate"])


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
        "source_config_sha256": _digest(config["source_config_path"]),
        "root_seed": int(config["experiment"]["root_seed"]),
        "seed_namespace": int(config["profile"]["seed_namespace"]),
        "python": platform.python_version(), "numpy": np.__version__,
        "platform": platform.platform(),
    }
    if metadata_path.exists():
        existing = json.loads(metadata_path.read_text(encoding="utf-8"))
        for key in (
            "profile", "config_sha256", "source_config_sha256",
            "root_seed", "seed_namespace",
        ):
            if existing.get(key) != metadata[key]:
                raise RuntimeError(f"existing output metadata disagrees on {key}")
    else:
        metadata_path.write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        shutil.copy2(config["config_path"], output / "amplitude_diagnostic.yaml")
        shutil.copy2(config["source_config_path"], output / "source_controls.yaml")


def write_run_summary(raw: pd.DataFrame, output: Path, requested: int) -> None:
    ok = raw.loc[raw["status"] == "ok"] if not raw.empty else raw
    report = [
        "# Amplitude diagnostic run", "",
        "Numerical diagnostic only; no estimator was tuned or changed.", "",
        f"- requested tasks: {requested}",
        f"- rows on disk: {len(raw)}",
        f"- completed rows: {len(ok)}",
        f"- recorded errors: {int((raw['status'] == 'error').sum()) if not raw.empty else 0}",
        f"- completion: {100 * len(raw) / requested:.1f}%", "",
    ]
    (output / "run_report.md").write_text("\n".join(report), encoding="utf-8")


def print_workload(config: dict[str, Any], tasks: list[ControlTask], workers: int) -> None:
    historical = {128: 0.20, 240: 0.31, 512: 0.67, 2048: 3.17}
    serial = sum(historical.get(task.n, 3.17 * task.n / 2048) for task in tasks)
    print(f"profile: {config['profile_name']}")
    print(f"recorded: {config['profile']['recorded']}")
    print(f"source: {config['source_regime']} in {config['source_config_path']}")
    print(f"n values: {config['profile']['n_values']}")
    print(f"replicates: {config['profile']['replicates']}")
    print(f"requested tasks: {len(tasks)}")
    print(f"{workers}-worker planning estimate: {serial / max(1, .7 * workers):.1f} seconds")


def run(config: dict[str, Any], *, workers: int, max_tasks: int | None = None) -> None:
    output = (ROOT / config["profile"]["output_dir"]).resolve()
    initialize_output(config, output)
    raw_path = output / "raw.csv"
    existing = read_rows(raw_path)
    completed = {_row_key(row) for _, row in existing.iterrows()}
    tasks = build_tasks(config)
    pending = [task for task in tasks if (task.n, task.replicate) not in completed]
    if max_tasks is not None:
        pending = pending[:max_tasks]
    if workers == 1:
        for index, task in enumerate(pending, start=1):
            print(f"[{index}/{len(pending)}] n={task.n}, rep={task.replicate}", flush=True)
            append_row(raw_path, run_task(config, task))
    elif pending:
        print(f"dispatching {len(pending)} tasks to {workers} workers", flush=True)
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(run_task, config, task): task for task in pending}
            for index, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                task = futures[future]
                row = future.result()
                append_row(raw_path, row)
                print(
                    f"[{index}/{len(pending)} complete] n={task.n}, "
                    f"rep={task.replicate}, status={row['status']}", flush=True,
                )
    write_run_summary(read_rows(raw_path), output, len(tasks))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument(
        "--profile", choices=("smoke", "calibration", "diagnostic"),
        default="smoke",
    )
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.workers < 1 or args.workers > 8:
        raise ValueError("workers must lie between one and eight")
    if args.max_tasks is not None and args.max_tasks < 1:
        raise ValueError("max-tasks must be positive")
    config = load_configuration(args.config.resolve(), args.profile)
    tasks = build_tasks(config)
    print_workload(config, tasks, args.workers)
    if args.dry_run:
        return 0
    try:
        run(config, workers=args.workers, max_tasks=args.max_tasks)
    except KeyboardInterrupt:
        print("\nInterrupted. Completed rows are on disk; rerun to resume.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
