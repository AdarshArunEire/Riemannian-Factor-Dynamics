"""N-RANK fixed-rank selector and loading-space stress-test harness.

The broad ``rank_oracle`` profile removes centre/frame estimation error but
retains tangent noise, so it cheaply identifies intrinsic selector boundaries
over many tangent dimensions, ranks, signal shapes, and sample sizes.  The
``rank_feasible`` profile runs the complete moving-centre RFD fit on a smaller
predeclared grid, including n=8192.  Every time series has one constant rank;
this experiment does not introduce a time-varying-rank model.

Examples
--------
Inspect workloads::

    python experiments/run_rank_sweep.py --profile rank_oracle --dry-run
    python experiments/run_rank_sweep.py --profile rank_feasible --dry-run

Run or resume::

    python experiments/run_rank_sweep.py --profile rank_oracle
    python experiments/run_rank_sweep.py --profile rank_feasible
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
    generate_ar1_factors,
    generate_lsrfm,
)
from rfd.estimators.frame import polygon_cell_count  # noqa: E402
from rfd.estimators.lag import (  # noqa: E402
    assemble_lag_operator,
    decompose_lag_operator,
    lag_cross_covariances,
    raw_ratio_rank,
    ridged_ratio_rank,
    threshold_rank,
)
from rfd.geometry import AIRM_GEOMETRY, BW_GEOMETRY  # noqa: E402
from rfd.model import RFDConfig, fit_rfd  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "rank_sweep.yaml"
GEOMETRIES = {"airm": AIRM_GEOMETRY, "bw": BW_GEOMETRY}
MODES = {"oracle", "feasible"}
RAW_COLUMNS = [
    "profile", "mode", "n", "matrix_size", "tangent_dimension",
    "true_rank", "signal_profile", "replicate", "seed_spawn_key",
    "method", "ridge_multiplier", "selected_rank", "correct",
    "rank_error", "status", "error_type", "error_message", "threshold",
    "ridge", "lambda_1", "lambda_r", "lambda_r_plus_1", "eigengap",
    "signal_to_threshold", "null_to_threshold", "elapsed_seconds",
]


@dataclass(frozen=True)
class Task:
    n: int
    matrix_size: int
    rank: int
    signal_profile: str
    replicate: int
    seed_sequence: np.random.SeedSequence

    @property
    def tangent_dimension(self) -> int:
        return self.matrix_size * (self.matrix_size + 1) // 2


def cubic_profile(time_values: np.ndarray) -> np.ndarray:
    time_values = np.asarray(time_values, dtype=float)
    return time_values + 0.5 * time_values**3


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
        "config_path": path.resolve(),
    }
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    profile = config["profile"]
    experiment = config["experiment"]
    estimator = config["estimator"]
    if profile.get("mode") not in MODES:
        raise ValueError("mode must be 'oracle' or 'feasible'")
    if experiment.get("geometry") not in GEOMETRIES:
        raise ValueError("geometry must be 'airm' or 'bw'")
    n_values = [int(value) for value in profile.get("n_values", [])]
    matrix_sizes = [int(value) for value in profile.get("matrix_sizes", [])]
    rank_values = [int(value) for value in profile.get("rank_values", [])]
    signal_profiles = list(profile.get("signal_profiles", []))
    if not n_values or min(n_values) < 16 or len(set(n_values)) != len(n_values):
        raise ValueError("n_values must be unique and at least 16")
    if not matrix_sizes or min(matrix_sizes) < 2 or len(set(matrix_sizes)) != len(matrix_sizes):
        raise ValueError("matrix_sizes must be unique and at least two")
    if not rank_values or min(rank_values) < 0 or len(set(rank_values)) != len(rank_values):
        raise ValueError("rank_values must be unique and nonnegative")
    known_profiles = experiment.get("signal_profiles", {})
    if not signal_profiles or any(name not in known_profiles for name in signal_profiles):
        raise ValueError("every requested signal profile must be declared")
    if int(profile.get("replicates", 0)) < 1:
        raise ValueError("replicates must be positive")
    if not any(rank < m * (m + 1) // 2 for m in matrix_sizes for rank in rank_values):
        raise ValueError("the rank grid contains no admissible rank/tangent pair")
    if float(experiment["total_factor_scale"]) <= 0.0:
        raise ValueError("total_factor_scale must be positive")
    if float(experiment["noise_scale"]) < 0.0:
        raise ValueError("noise_scale must be nonnegative")
    ridge_multipliers = np.asarray(estimator.get("ridge_multipliers", []), dtype=float)
    if ridge_multipliers.size == 0 or np.any(~np.isfinite(ridge_multipliers)):
        raise ValueError("ridge_multipliers must be finite and nonempty")
    if np.any(ridge_multipliers <= 0.0) or len(set(ridge_multipliers)) != len(ridge_multipliers):
        raise ValueError("ridge_multipliers must be unique and positive")
    if int(estimator["selector_max_rank"]) < 1:
        raise ValueError("selector_max_rank must be positive")
    if int(estimator["max_lag"]) < 1 or int(estimator["max_lag"]) >= min(n_values):
        raise ValueError("max_lag must lie below every sample size")


def build_tasks(config: dict[str, Any]) -> list[Task]:
    profile = config["profile"]
    first_signal = str(profile["signal_profiles"][0])
    bare = []
    for n in profile["n_values"]:
        for matrix_size in profile["matrix_sizes"]:
            dimension = int(matrix_size) * (int(matrix_size) + 1) // 2
            for rank in profile["rank_values"]:
                rank = int(rank)
                if rank >= dimension:
                    continue
                for signal_profile in profile["signal_profiles"]:
                    # Rank zero has no signal shape; record it exactly once.
                    if rank == 0 and signal_profile != first_signal:
                        continue
                    for replicate in range(int(profile["replicates"])):
                        bare.append(
                            (int(n), int(matrix_size), rank, str(signal_profile), replicate)
                        )
    root = np.random.SeedSequence(
        [int(config["experiment"]["root_seed"]), int(profile["seed_namespace"])]
    )
    return [
        Task(*values, seed)
        for values, seed in zip(bare, root.spawn(len(bare)))
    ]


def _base_and_direction(matrix_size: int, condition: float) -> tuple[np.ndarray, np.ndarray]:
    base = np.diag(np.geomspace(1.0, condition, matrix_size))
    diagonal = np.linspace(-1.0, 1.0, matrix_size)
    direction = np.diag(diagonal)
    if matrix_size > 1:
        direction[0, -1] = direction[-1, 0] = 0.35
    return base, direction


def signal_parameters(config: dict[str, Any], rank: int, name: str) -> tuple[np.ndarray, np.ndarray]:
    if rank == 0:
        return np.empty(0), np.empty(0)
    declared = config["experiment"]["signal_profiles"][name]
    if declared["scale_weights"] == "equal":
        weights = np.ones(rank)
    elif declared["scale_weights"] == "geometric":
        weights = np.geomspace(1.0, 0.35, rank)
    else:
        raise ValueError(f"unknown scale_weights: {declared['scale_weights']}")
    weights[-1] *= float(declared["weak_tail_multiplier"])
    weights /= np.linalg.norm(weights)
    scales = float(config["experiment"]["total_factor_scale"]) * weights
    persistence = np.linspace(
        float(declared["persistence_high"]),
        float(declared["persistence_low"]),
        rank,
    )
    return persistence, scales


def _dgp_config(config: dict[str, Any], task: Task) -> LSRFMConfig:
    experiment = config["experiment"]
    base, direction = _base_and_direction(
        task.matrix_size, float(experiment["base_condition"])
    )
    persistence, scales = signal_parameters(config, task.rank, task.signal_profile)
    return LSRFMConfig(
        centre=CentrePathConfig(
            base_centre=base,
            drift_direction=direction,
            drift_scale=float(experiment["drift_scale"]),
            profile=cubic_profile,
        ),
        factor=AR1FactorConfig(
            rank=task.rank,
            persistence=persistence,
            scale=scales,
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


def _production_multiplier(n: int, estimator: dict[str, Any]) -> float:
    left, right = (float(value) for value in estimator["overlap_fractions"])
    base_bandwidth = float(estimator["bandwidth_constant"]) * n ** (
        -float(estimator["bandwidth_exponent"])
    )
    maximum = min(left, 1.0 - right) / base_bandwidth
    return min(
        float(estimator["production_multiplier_cap"]),
        float(estimator["admissible_boundary_fraction"]) * maximum,
    )


def _model_config(config: dict[str, Any], task: Task) -> RFDConfig:
    estimator = config["estimator"]
    bandwidth = (
        float(estimator["bandwidth_constant"])
        * task.n ** (-float(estimator["bandwidth_exponent"]))
        * _production_multiplier(task.n, estimator)
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
        rank=task.rank,
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
        overlap_fractions=tuple(float(v) for v in estimator["overlap_fractions"]),
        mean_tol=float(estimator["mean_tolerance"]),
        mean_max_iter=int(estimator["mean_max_iter"]),
    )


def _spectrum(config: dict[str, Any], task: Task, rng: np.random.Generator):
    if config["profile"]["mode"] == "oracle":
        persistence, scales = signal_parameters(config, task.rank, task.signal_profile)
        factors = generate_ar1_factors(
            rng,
            task.n,
            AR1FactorConfig(task.rank, persistence, scales),
        )
        if task.rank:
            raw_loadings = rng.standard_normal((task.tangent_dimension, task.rank))
            loadings, _ = np.linalg.qr(raw_loadings, mode="reduced")
            factor_rows = factors @ loadings.T
        else:
            factor_rows = np.zeros((task.n, task.tangent_dimension))
        raw_noise = rng.standard_normal((task.n, task.tangent_dimension))
        noise_norms = np.linalg.norm(raw_noise, axis=1, keepdims=True)
        noise_rows = (
            float(config["experiment"]["noise_scale"])
            * raw_noise
            / noise_norms
        )
        rows = factor_rows + noise_rows
    else:
        geometry = GEOMETRIES[config["experiment"]["geometry"]]
        dgp = _dgp_config(config, task)
        sample = generate_lsrfm(rng, task.n, geometry, dgp)
        return fit_rfd(
            sample.observations,
            sample.time,
            geometry,
            _model_config(config, task),
        ).spectrum

    lag_row = lag_cross_covariances(
        rows,
        int(config["estimator"]["max_lag"]),
        tail_mode=str(config["estimator"]["tail_mode"]),
        normalization=str(config["estimator"]["normalization"]),
    )
    return decompose_lag_operator(assemble_lag_operator(lag_row))


def _selector_specs(config: dict[str, Any]) -> list[tuple[str, float]]:
    return [
        ("threshold", np.nan),
        ("raw_ratio", 0.0),
        *[("ridged_ratio", float(value)) for value in config["estimator"]["ridge_multipliers"]],
    ]


def _base_row(config: dict[str, Any], task: Task) -> dict[str, Any]:
    return {
        "profile": config["profile_name"],
        "mode": config["profile"]["mode"],
        "n": task.n,
        "matrix_size": task.matrix_size,
        "tangent_dimension": task.tangent_dimension,
        "true_rank": task.rank,
        "signal_profile": task.signal_profile if task.rank > 0 else "rank_zero",
        "replicate": task.replicate,
        "seed_spawn_key": ".".join(map(str, task.seed_sequence.spawn_key)),
    }


def run_task(config: dict[str, Any], task: Task) -> list[dict[str, Any]]:
    started = time.perf_counter()
    threshold = float(config["estimator"]["threshold_constant"]) * task.n ** (
        -float(config["estimator"]["threshold_exponent"])
    )
    specs = _selector_specs(config)
    try:
        spectrum = _spectrum(config, task, np.random.default_rng(task.seed_sequence))
        eigenvalues = spectrum.eigenvalues
        cap = min(int(config["estimator"]["selector_max_rank"]), eigenvalues.size - 1)
        if cap < 1:
            raise ValueError("selector requires at least two tangent eigenvalues")
        lambda_r = float(eigenvalues[task.rank - 1]) if task.rank > 0 else np.nan
        lambda_next = float(eigenvalues[task.rank])
        gap = lambda_r - lambda_next if task.rank > 0 else np.nan
        common = {
            **_base_row(config, task),
            "status": "ok",
            "error_type": "",
            "error_message": "",
            "threshold": threshold,
            "lambda_1": float(eigenvalues[0]),
            "lambda_r": lambda_r,
            "lambda_r_plus_1": lambda_next,
            "eigengap": gap,
            "signal_to_threshold": lambda_r / threshold if task.rank > 0 else np.nan,
            "null_to_threshold": lambda_next / threshold,
        }
        rows = []
        for method, multiplier in specs:
            if method == "threshold":
                result = threshold_rank(eigenvalues, threshold, max_rank=cap)
                ridge = np.nan
            elif method == "raw_ratio":
                result = raw_ratio_rank(eigenvalues, max_rank=cap)
                ridge = 0.0
            else:
                ridge = threshold * multiplier
                result = ridged_ratio_rank(eigenvalues, ridge, max_rank=cap)
            rows.append({
                **common,
                "method": method,
                "ridge_multiplier": multiplier,
                "ridge": ridge,
                "selected_rank": int(result.rank),
                "correct": int(result.rank == task.rank),
                "rank_error": int(result.rank - task.rank),
                "elapsed_seconds": time.perf_counter() - started,
            })
        return rows
    except Exception as error:
        return [
            {
                **_base_row(config, task),
                "method": method,
                "ridge_multiplier": multiplier,
                "status": "error",
                "error_type": type(error).__name__,
                "error_message": str(error).replace("\n", " ")[:500],
                "threshold": threshold,
                "ridge": 0.0 if method == "raw_ratio" else (
                    threshold * multiplier if method == "ridged_ratio" else np.nan
                ),
                "elapsed_seconds": time.perf_counter() - started,
            }
            for method, multiplier in specs
        ]


def _row_key(row: dict[str, Any] | pd.Series) -> tuple[Any, ...]:
    multiplier = row["ridge_multiplier"]
    multiplier = "nan" if pd.isna(multiplier) else float(multiplier)
    return (
        int(row["n"]), int(row["matrix_size"]), int(row["true_rank"]),
        str(row["signal_profile"]), int(row["replicate"]),
        str(row["method"]), multiplier,
    )


def read_existing_rows(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=RAW_COLUMNS)
    return pd.read_csv(path)


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
    groups = [
        "mode", "n", "matrix_size", "tangent_dimension", "true_rank",
        "signal_profile", "method", "ridge_multiplier",
    ]
    records = []
    for keys, group in ok.groupby(groups, dropna=False):
        record = dict(zip(groups, keys))
        record.update({
            "completed": len(group),
            "accuracy_percent": 100.0 * float(group["correct"].mean()),
            "underselect_percent": 100.0 * float((group["rank_error"] < 0).mean()),
            "overselect_percent": 100.0 * float((group["rank_error"] > 0).mean()),
            "median_selected_rank": float(group["selected_rank"].median()),
            "lambda_r_median": float(pd.to_numeric(group["lambda_r"], errors="coerce").median()),
            "lambda_r_plus_1_median": float(
                pd.to_numeric(group["lambda_r_plus_1"], errors="coerce").median()
            ),
            "signal_to_threshold_median": float(
                pd.to_numeric(group["signal_to_threshold"], errors="coerce").median()
            ),
            "null_to_threshold_median": float(
                pd.to_numeric(group["null_to_threshold"], errors="coerce").median()
            ),
        })
        records.append(record)
    return pd.DataFrame.from_records(records)


def _method_label(method: str, multiplier: float) -> str:
    if method != "ridged_ratio":
        return method.replace("_", " ")
    return f"ridge {multiplier:g}x"


def plot_results(summary: pd.DataFrame, output: Path) -> None:
    if summary.empty:
        return
    plot_dir = output / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)

    aggregated = (
        summary.groupby(["true_rank", "method", "ridge_multiplier"], dropna=False)[
            "accuracy_percent"
        ].mean().reset_index()
    )
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for (method, multiplier), line in aggregated.groupby(
        ["method", "ridge_multiplier"], dropna=False
    ):
        line = line.sort_values("true_rank")
        label = _method_label(str(method), float(multiplier))
        ax.plot(line["true_rank"], line["accuracy_percent"], marker="o", label=label)
    ax.set_xlabel("true persistent rank")
    ax.set_ylabel("correct rank (%)")
    ax.set_ylim(-2, 102)
    ax.set_title("Rank recovery across the complete fixed-rank screen", fontweight="bold")
    ax.grid(True, alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(plot_dir / "01_selector_accuracy_by_rank.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    threshold = summary.loc[summary["method"] == "threshold"].copy()
    profiles = list(dict.fromkeys(threshold["signal_profile"]))
    n_values = sorted(threshold["n"].unique())
    fig, axes = plt.subplots(
        len(profiles), len(n_values),
        figsize=(4.0 * len(n_values), 3.2 * len(profiles)),
        squeeze=False,
    )
    image = None
    for row, signal_profile in enumerate(profiles):
        for column, n in enumerate(n_values):
            ax = axes[row, column]
            cell = threshold.loc[
                (threshold["signal_profile"] == signal_profile) & (threshold["n"] == n)
            ]
            pivot = cell.pivot_table(
                index="tangent_dimension", columns="true_rank",
                values="accuracy_percent", aggfunc="mean",
            ).sort_index()
            image = ax.imshow(pivot.to_numpy(), aspect="auto", vmin=0, vmax=100, cmap="viridis")
            ax.set_xticks(range(len(pivot.columns)), [str(int(v)) for v in pivot.columns])
            ax.set_yticks(range(len(pivot.index)), [str(int(v)) for v in pivot.index])
            ax.set_title(f"{signal_profile}, n={int(n):,}")
            ax.set_xlabel("true rank")
            ax.set_ylabel("tangent dimension p")
    if image is not None:
        colorbar = fig.colorbar(image, ax=axes.ravel().tolist(), shrink=0.8)
        colorbar.set_label("correct rank (%)")
    fig.suptitle("Threshold-selector phase map", fontweight="bold")
    fig.subplots_adjust(top=0.90, right=0.90, hspace=0.45, wspace=0.35)
    fig.savefig(plot_dir / "02_threshold_phase_map.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def initialize_output(config: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    metadata_path = output / "metadata.json"
    metadata = {
        "profile": config["profile_name"],
        "mode": config["profile"]["mode"],
        "recorded": bool(config["profile"]["recorded"]),
        "config_sha256": _digest(config["config_path"]),
        "root_seed": int(config["experiment"]["root_seed"]),
        "seed_namespace": int(config["profile"]["seed_namespace"]),
        "numpy": np.__version__,
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    if metadata_path.exists():
        existing = json.loads(metadata_path.read_text(encoding="utf-8"))
        for key in ("profile", "mode", "config_sha256", "root_seed", "seed_namespace"):
            if existing.get(key) != metadata[key]:
                raise RuntimeError(f"existing output metadata disagrees on {key}")
    else:
        metadata_path.write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        shutil.copy2(config["config_path"], output / "rank_sweep.yaml")


def summarize_and_plot(config: dict[str, Any], output: Path) -> None:
    raw = read_existing_rows(output / "raw.csv")
    if raw.empty:
        print("No rows available to summarize.")
        return
    summary = summarize(raw)
    summary.to_csv(output / "summary.csv", index=False)
    plot_results(summary, output)
    requested = len(build_tasks(config)) * len(_selector_specs(config))
    completed = int((raw["status"] == "ok").sum())
    errors = int((raw["status"] == "error").sum())
    report = [
        f"# {config['profile_name']} fixed-rank sweep", "",
        "Numerical evidence only; every time series has one constant rank.", "",
        f"- requested selector rows: {requested}",
        f"- completed selector rows: {completed}",
        f"- recorded errors: {errors}",
        f"- completion: {100.0 * completed / requested:.1f}%", "",
        "Rank zero is a legitimate target for the threshold selector. Ratio",
        "selectors cannot return zero and are expected to fail on that null.", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")


def print_workload(config: dict[str, Any], tasks: list[Task]) -> None:
    profile = config["profile"]
    valid_pairs = sorted({(task.tangent_dimension, task.rank) for task in tasks})
    print(f"profile: {config['profile_name']}")
    print(f"mode: {profile['mode']}")
    print(f"recorded: {profile['recorded']}")
    print(f"output: {profile['output_dir']}")
    print(f"n values: {profile['n_values']}")
    print(f"matrix sizes: {profile['matrix_sizes']}")
    print(f"requested ranks: {profile['rank_values']}")
    print(f"valid (p, r) pairs: {valid_pairs}")
    print(f"signal profiles: {profile['signal_profiles']}")
    print(f"replicates: {profile['replicates']}")
    print(f"DGP tasks: {len(tasks)}")
    print(f"selector rows: {len(tasks) * len(_selector_specs(config))}")
    print("n=8192 included: " + str(8192 in [int(v) for v in profile["n_values"]]))


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
        expected = []
        for method, multiplier in _selector_specs(config):
            key_multiplier = "nan" if np.isnan(multiplier) else float(multiplier)
            expected.append((
                task.n, task.matrix_size, task.rank,
                task.signal_profile if task.rank > 0 else "rank_zero",
                task.replicate, method, key_multiplier,
            ))
        missing_keys = {key for key in expected if key not in completed_keys}
        if not missing_keys:
            continue
        if max_tasks is not None and processed >= max_tasks:
            break
        task_rows = run_task(config, task)
        missing = [row for row in task_rows if _row_key(row) in missing_keys]
        print(
            f"[{index}/{len(tasks)}] n={task.n}, m={task.matrix_size}, "
            f"p={task.tangent_dimension}, r={task.rank}, "
            f"signal={task.signal_profile}, rep={task.replicate}",
            flush=True,
        )
        append_rows(raw_path, missing)
        completed_keys.update(_row_key(row) for row in missing)
        processed += 1
    summarize_and_plot(config, output)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--profile", default="smoke")
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
        print("\nInterrupted. Completed selector rows are on disk; rerun to resume.")
        summarize_and_plot(config, (ROOT / config["profile"]["output_dir"]).resolve())
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
