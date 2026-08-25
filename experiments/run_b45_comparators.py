"""Replay B4.5 draws through fair centre and factor-recovery comparators.

The recorded end-to-end run already measures feasible RFD against the
noiseless dynamic loading target.  This companion runner replays the exact
same deterministic DGP draws and adds two interpretable baselines:

``known_centre_noisy``
    Uses the true moving centre but retains the generated observation noise.
    Its gap from truth is sampling/noise error; its gap from RFD is the cost of
    estimating and polygonally transporting the centre path.

``fixed_centre_rfm``
    Uses one global Fréchet mean, then the same lag operator and fixed true
    rank as RFD.  This is an RFM-compatible AIRM baseline on the same draws,
    not a claim that the parent's published BW implementation was run.

The script is serial, append-only, resumable, and does not alter the completed
B4.5 raw tables.  Full recorded runs are intended to be launched by the user.
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
from pathlib import Path
from typing import Any

for _thread_variable in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS",
):
    os.environ.setdefault(_thread_variable, "1")

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_end_to_end import (  # noqa: E402
    CONFIG_DEFAULT,
    GEOMETRIES,
    Task,
    _dgp_config,
    _intrinsic_rms,
    _procrustes_nrmse,
    build_tasks,
    load_configuration,
)
from rfd.dgp.lsrfm import generate_lsrfm  # noqa: E402
from rfd.estimators.lag import (  # noqa: E402
    assemble_lag_operator,
    coordinate_tangents,
    decompose_lag_operator,
    extract_dynamic_factors,
    lag_cross_covariances,
    raw_ratio_rank,
    ridged_ratio_rank,
    tangent_coordinates,
    threshold_rank,
)
from rfd.geometry import GeometryOps  # noqa: E402


RAW_COLUMNS = [
    "profile", "n", "matrix_size", "tangent_dimension", "replicate",
    "seed_spawn_key", "status", "error_type", "error_message", "true_rank",
    "known_centre_loading_error", "fixed_centre_loading_error",
    "known_centre_factor_nrmse", "fixed_centre_factor_nrmse",
    "known_centre_observation_reconstruction_rms",
    "fixed_centre_observation_reconstruction_rms",
    "known_centre_signal_reconstruction_rms",
    "fixed_centre_signal_reconstruction_rms",
    "true_centre_observation_rms", "true_centre_signal_rms",
    "global_mean_observation_rms", "global_mean_signal_rms",
    "global_mean_centre_path_rms", "known_centre_threshold_rank",
    "fixed_centre_threshold_rank", "known_centre_raw_ratio_rank",
    "fixed_centre_raw_ratio_rank", "known_centre_ridged_ratio_rank",
    "fixed_centre_ridged_ratio_rank", "global_mean_converged",
    "global_mean_iterations", "global_mean_residual", "elapsed_seconds",
]


def _default_output(config: dict[str, Any]) -> Path:
    name = config["profile_name"]
    if name == "smoke":
        return ROOT / "tmp" / "b45_comparators_smoke"
    suffix = "_8192" if name.endswith("8192") else ""
    return ROOT / "results" / "intermediate" / f"b45_comparators{suffix}"


def _projector_from_rows(rows: np.ndarray) -> np.ndarray:
    """Orthogonal projector onto the row span of coordinate vectors."""
    rows = np.asarray(rows, dtype=float)
    _, singular_values, right = np.linalg.svd(rows, full_matrices=False)
    if rows.shape[0] == 0 or singular_values[0] <= 0.0:
        return np.zeros((rows.shape[1], rows.shape[1]))
    keep = singular_values > 1e-12 * singular_values[0]
    basis = right[keep].T
    return basis @ basis.T


def _fit_rows(rows: np.ndarray, config: dict[str, Any]):
    estimator = config["estimator"]
    lag = lag_cross_covariances(
        rows,
        int(estimator["max_lag"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
    )
    spectrum = decompose_lag_operator(assemble_lag_operator(lag))
    factors = extract_dynamic_factors(
        spectrum, int(config["experiment"]["factor_rank"])
    )
    return lag, spectrum, factors


def _selector_ranks(
    eigenvalues: np.ndarray, config: dict[str, Any], n: int
) -> tuple[float, float, float]:
    estimator = config["estimator"]
    threshold = (
        float(estimator["selector_constant"])
        * n ** (-float(estimator["selector_exponent"]))
    )
    cap = min(int(estimator["selector_max_rank"]), eigenvalues.size - 1)
    threshold_value = threshold_rank(eigenvalues, threshold, max_rank=cap).rank
    ridged_value = ridged_ratio_rank(eigenvalues, threshold, max_rank=cap).rank
    try:
        raw_value = raw_ratio_rank(eigenvalues, max_rank=cap).rank
    except ValueError:
        raw_value = np.nan
    return float(threshold_value), float(raw_value), float(ridged_value)


def _reconstruct(
    factors,
    basis: np.ndarray,
    source_point: np.ndarray,
    target_centres: np.ndarray,
    geometry: GeometryOps,
) -> np.ndarray:
    reference_vectors = coordinate_tangents(factors.reconstructed_rows, basis)
    if target_centres.ndim == source_point.ndim:
        local_vectors = reference_vectors
    else:
        local_vectors = geometry.transport(
            reference_vectors, source_point, target_centres
        )
    return geometry.exp(target_centres, local_vectors)


def evaluate_comparators(
    sample,
    geometry: GeometryOps,
    config: dict[str, Any],
    base: np.ndarray,
) -> dict[str, Any]:
    """Evaluate truth-centred noisy and global-centre fits on one draw."""
    rank = int(config["experiment"]["factor_rank"])
    mean_tol = float(config["estimator"]["mean_tolerance"])
    mean_max_iter = int(config["estimator"]["mean_max_iter"])
    latent_signal = geometry.exp(sample.centres, sample.factor_effects)
    target_factors = sample.factors - sample.factors.mean(axis=0)

    base_basis = geometry.tangent_basis(base)
    truth_coordinates = tangent_coordinates(
        sample.loadings, base, base_basis, geometry
    )
    truth_projector = _projector_from_rows(truth_coordinates)

    known_local = geometry.log(sample.centres, sample.observations)
    known_reference = geometry.transport(
        known_local, sample.centres, base
    )
    known_rows = tangent_coordinates(
        known_reference, base, base_basis, geometry
    )
    _, known_spectrum, known_factors = _fit_rows(known_rows, config)
    known_projector = (
        known_spectrum.eigenvectors[:, :rank]
        @ known_spectrum.eigenvectors[:, :rank].T
    )
    known_reconstruction = _reconstruct(
        known_factors, base_basis, base, sample.centres, geometry
    )

    mean_result = geometry.barycentre(
        sample.observations, tol=mean_tol, max_iter=mean_max_iter
    )
    global_mean = mean_result.X
    global_basis = geometry.tangent_basis(global_mean)
    fixed_vectors = geometry.log(global_mean, sample.observations)
    fixed_rows = tangent_coordinates(
        fixed_vectors, global_mean, global_basis, geometry
    )
    _, fixed_spectrum, fixed_factors = _fit_rows(fixed_rows, config)
    fixed_loading_vectors = coordinate_tangents(
        fixed_spectrum.eigenvectors[:, :rank].T, global_basis
    )
    fixed_loading_at_base = geometry.transport(
        fixed_loading_vectors, global_mean, base
    )
    fixed_loading_coordinates = tangent_coordinates(
        fixed_loading_at_base, base, base_basis, geometry
    )
    fixed_projector = _projector_from_rows(fixed_loading_coordinates)
    fixed_reconstruction = _reconstruct(
        fixed_factors, global_basis, global_mean, global_mean, geometry
    )

    known_threshold, known_raw, known_ridged = _selector_ranks(
        known_spectrum.eigenvalues, config, sample.time.size
    )
    fixed_threshold, fixed_raw, fixed_ridged = _selector_ranks(
        fixed_spectrum.eigenvalues, config, sample.time.size
    )
    return {
        "true_rank": rank,
        "known_centre_loading_error": float(
            np.linalg.norm(known_projector - truth_projector, ord=2)
        ),
        "fixed_centre_loading_error": float(
            np.linalg.norm(fixed_projector - truth_projector, ord=2)
        ),
        "known_centre_factor_nrmse": _procrustes_nrmse(
            known_factors.factor_scores, target_factors
        ),
        "fixed_centre_factor_nrmse": _procrustes_nrmse(
            fixed_factors.factor_scores, target_factors
        ),
        "known_centre_observation_reconstruction_rms": _intrinsic_rms(
            geometry, known_reconstruction, sample.observations
        ),
        "fixed_centre_observation_reconstruction_rms": _intrinsic_rms(
            geometry, fixed_reconstruction, sample.observations
        ),
        "known_centre_signal_reconstruction_rms": _intrinsic_rms(
            geometry, known_reconstruction, latent_signal
        ),
        "fixed_centre_signal_reconstruction_rms": _intrinsic_rms(
            geometry, fixed_reconstruction, latent_signal
        ),
        "true_centre_observation_rms": _intrinsic_rms(
            geometry, sample.centres, sample.observations
        ),
        "true_centre_signal_rms": _intrinsic_rms(
            geometry, sample.centres, latent_signal
        ),
        "global_mean_observation_rms": _intrinsic_rms(
            geometry, global_mean, sample.observations
        ),
        "global_mean_signal_rms": _intrinsic_rms(
            geometry, global_mean, latent_signal
        ),
        "global_mean_centre_path_rms": _intrinsic_rms(
            geometry, global_mean, sample.centres
        ),
        "known_centre_threshold_rank": known_threshold,
        "fixed_centre_threshold_rank": fixed_threshold,
        "known_centre_raw_ratio_rank": known_raw,
        "fixed_centre_raw_ratio_rank": fixed_raw,
        "known_centre_ridged_ratio_rank": known_ridged,
        "fixed_centre_ridged_ratio_rank": fixed_ridged,
        "global_mean_converged": bool(mean_result.converged),
        "global_mean_iterations": int(mean_result.n_iter),
        "global_mean_residual": float(mean_result.residual),
    }


def run_task(config: dict[str, Any], task: Task) -> dict[str, Any]:
    started = time.perf_counter()
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": config["profile_name"], "n": task.n,
        "matrix_size": task.matrix_size,
        "tangent_dimension": task.matrix_size * (task.matrix_size + 1) // 2,
        "replicate": task.replicate,
        "seed_spawn_key": ".".join(map(str, task.seed_sequence.spawn_key)),
    })
    try:
        geometry = GEOMETRIES[config["experiment"]["geometry"]]
        dgp_config = _dgp_config(config, task)
        sample = generate_lsrfm(
            np.random.default_rng(task.seed_sequence),
            task.n,
            geometry,
            dgp_config,
        )
        row.update(evaluate_comparators(
            sample, geometry, config, dgp_config.centre.base_centre
        ))
        row.update({"status": "ok", "error_type": "", "error_message": ""})
    except Exception as error:
        row.update({
            "status": "error", "error_type": type(error).__name__,
            "error_message": str(error).replace("\n", " ")[:500],
        })
    row["elapsed_seconds"] = time.perf_counter() - started
    return row


def _key(row) -> tuple[int, int, int]:
    return int(row["n"]), int(row["matrix_size"]), int(row["replicate"])


def _read(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=RAW_COLUMNS)
    return pd.read_csv(path)


def _append(path: Path, row: dict[str, Any]) -> None:
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


def _initialize(config: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    metadata_path = output / "metadata.json"
    metadata = {
        "profile": config["profile_name"],
        "config_sha256": _digest(config["config_path"]),
        "root_seed": int(config["experiment"]["root_seed"]),
        "seed_namespace": int(config["profile"]["seed_namespace"]),
        "numpy": np.__version__, "python": platform.python_version(),
        "platform": platform.platform(),
        "comparators": ["known_centre_noisy", "fixed_centre_rfm"],
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
        shutil.copy2(config["config_path"], output / "source_end_to_end.yaml")


def _summarize(raw: pd.DataFrame, output: Path) -> None:
    ok = raw.loc[raw["status"] == "ok"].copy()
    if ok.empty:
        return
    metrics = [
        column for column in RAW_COLUMNS
        if column.endswith(("_error", "_nrmse", "_rms"))
    ]
    rows = []
    for (n, matrix_size), group in ok.groupby(["n", "matrix_size"]):
        row = {"n": int(n), "matrix_size": int(matrix_size), "completed": len(group)}
        for metric in metrics:
            values = pd.to_numeric(group[metric], errors="coerce")
            row[f"{metric}_median"] = float(values.median())
            row[f"{metric}_q25"] = float(values.quantile(0.25))
            row[f"{metric}_q75"] = float(values.quantile(0.75))
        rows.append(row)
    pd.DataFrame(rows).to_csv(output / "summary.csv", index=False)
    report = [
        "# B4.5 comparator replay", "",
        "These rows replay the exact B4.5 DGP namespaces. The fixed-centre",
        "fit is RFM-compatible on AIRM, not the parent's literal BW code.", "",
        f"- requested tasks: {len(raw)}",
        f"- completed tasks: {len(ok)}",
        f"- recorded errors: {(raw['status'] == 'error').sum()}",
        f"- nonconverged global means: {(~ok['global_mean_converged'].astype(bool)).sum()}", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")


def run(
    config: dict[str, Any], output: Path, *, max_tasks: int | None = None
) -> None:
    _initialize(config, output)
    raw_path = output / "raw.csv"
    raw = _read(raw_path)
    completed = {_key(row) for _, row in raw.iterrows()}
    tasks = build_tasks(config)
    processed = 0
    for index, task in enumerate(tasks, start=1):
        if (task.n, task.matrix_size, task.replicate) in completed:
            continue
        if max_tasks is not None and processed >= max_tasks:
            break
        print(
            f"[{index}/{len(tasks)}] n={task.n}, m={task.matrix_size}, "
            f"rep={task.replicate}", flush=True,
        )
        _append(raw_path, run_task(config, task))
        processed += 1
    _summarize(_read(raw_path), output)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument(
        "--profile", choices=("smoke", "factor_baseline", "factor_baseline_8192"),
        default="smoke",
    )
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_configuration(args.config.resolve(), args.profile)
    tasks = build_tasks(config)
    output = args.output.resolve() if args.output else _default_output(config)
    print(f"profile: {config['profile_name']}")
    print(f"output: {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}")
    print(f"DGP tasks: {len(tasks)}")
    print("comparators: known-centre noisy; fixed-centre RFM-compatible")
    if args.dry_run:
        return 0
    if args.max_tasks is not None and args.max_tasks < 1:
        raise ValueError("max-tasks must be positive")
    try:
        run(config, output, max_tasks=args.max_tasks)
    except KeyboardInterrupt:
        print("\nInterrupted. Completed rows are on disk; rerun to resume.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
