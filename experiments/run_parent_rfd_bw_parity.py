"""Run literal parent RFM and RFD on identical regular BW synthetic draws.

The parent arm calls the cloned R function ``rfm_bws``.  Both estimators are
given the known DGP rank and the same lag count, so this is a paired test of
fixed-global-centre RFM against RFD's moving centre, polygon, and transport
chain.  It is reconstruction/recovery work, not forecasting or rank selection.

Rows are appended and flushed by the parent Python process as worker tasks
finish.  Rerunning the same immutable profile resumes missing task keys.
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
import subprocess
import sys
import tempfile
import time
from copy import deepcopy
from pathlib import Path
from typing import Any

for _thread_variable in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_bw_closure import BWTask, _model_config, generate_fit_sample  # noqa: E402
from run_end_to_end import _intrinsic_rms, _procrustes_nrmse  # noqa: E402
from run_b45_comparators import _projector_from_rows  # noqa: E402
from rfd.estimators.lag import coordinate_tangents, tangent_coordinates  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.model import fit_rfd  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "parent_rfd_bw_parity.yaml"
R_WORKER = ROOT / "experiments" / "parent_rfm_bw_worker.R"
PARENT_SOURCE = ROOT / "reference" / "Riemannian_factor_model-main" / "BWS_util.R"

IDENTITY_COLUMNS = [
    "profile", "scenario", "scenario_label", "scenario_class", "n",
    "matrix_size", "replicate", "seed_key", "true_rank", "status",
    "error_type", "error_message",
]
METHOD_METRICS = [
    "centre_path_rms", "loading_error", "factor_nrmse",
    "observation_reconstruction_rms", "signal_reconstruction_rms",
]
METHODS = ("rfd", "parent_budget", "parent_converged")
RAW_COLUMNS = IDENTITY_COLUMNS + [
    "centre_path_length", "centre_path_energy", "true_centre_observation_rms",
    "true_centre_signal_rms", "observation_min_eigenvalue",
    "observation_max_eigenvalue", "rfd_fallback_count",
    "rfd_nonconverged_stages", "parent_budget_status",
    "parent_budget_message", "parent_converged_status",
    "parent_converged_message", "parent_sensitivity_mean_converged",
    "parent_sensitivity_mean_iterations", "parent_sensitivity_mean_residual",
] + [
    f"{method}_{metric}" for method in METHODS for metric in METHOD_METRICS
] + [
    "rfd_over_parent_budget_signal_rms",
    "rfd_over_parent_converged_signal_rms",
    "generation_seconds", "rfd_seconds", "parent_seconds", "elapsed_seconds",
]


def load_configuration(path: Path, profile_name: str) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        source = yaml.safe_load(handle)
    if profile_name not in source.get("profiles", {}):
        raise ValueError(f"unknown profile: {profile_name}")
    config = {
        "profile_name": profile_name,
        "profile": deepcopy(source["profiles"][profile_name]),
        "experiment": deepcopy(source["experiment"]),
        "estimator": deepcopy(source["estimator"]),
        "parent": deepcopy(source["parent"]),
        "regimes": deepcopy(source["regimes"]),
        "config_path": path.resolve(),
    }
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    profile = config["profile"]
    estimator = config["estimator"]
    rank = int(experiment["factor_rank"])
    matrix_size = int(experiment["matrix_size"])
    if experiment["geometry"] != "bw":
        raise ValueError("parent/RFD parity requires geometry='bw'")
    if matrix_size < 2 or rank < 1:
        raise ValueError("matrix size must be at least two and rank positive")
    if matrix_size * (matrix_size + 1) // 2 <= rank:
        raise ValueError("tangent dimension must exceed the supplied rank")
    persistence = np.asarray(experiment["factor_persistence"], dtype=float)
    scales = np.asarray(experiment["factor_scale"], dtype=float)
    if persistence.shape != (rank,) or scales.shape != (rank,):
        raise ValueError("factor persistence and scales must match factor_rank")
    if np.any(np.abs(persistence) >= 1.0) or np.any(scales <= 0.0):
        raise ValueError("invalid factor persistence or scale")
    n_values = [int(value) for value in profile["n_values"]]
    if not n_values or min(n_values) < 32 or len(set(n_values)) != len(n_values):
        raise ValueError("n_values must be unique and at least 32")
    if int(profile["replicates"]) < 1:
        raise ValueError("replicates must be positive")
    lag = int(estimator["max_lag"])
    if lag < 1 or lag >= min(n_values):
        raise ValueError("max_lag must lie inside every sample")
    overlap = tuple(float(value) for value in estimator["overlap_fractions"])
    if len(overlap) != 2 or not 0.0 < overlap[0] < overlap[1] < 1.0:
        raise ValueError("overlap fractions must be increasing and interior")
    for name in profile["regimes"]:
        if name not in config["regimes"]:
            raise ValueError(f"unknown regime: {name}")
        spec = config["regimes"][name]
        if int(spec["rank"]) != rank:
            raise ValueError("every parity regime must use the supplied true rank")
        if spec["path"] not in ("commuting", "curved"):
            raise ValueError(f"unsupported regular path in {name}")
    parent = config["parent"]
    if min(int(parent["batch_size"]), int(parent["budget_iterations"])) < 1:
        raise ValueError("parent computational controls must be positive")
    if (
        float(parent["sensitivity_mean_tolerance"]) <= 0.0
        or int(parent["sensitivity_mean_max_iterations"]) < 1
    ):
        raise ValueError("parent sensitivity mean controls must be positive")


def build_tasks(config: dict[str, Any]) -> list[BWTask]:
    profile = config["profile"]
    return [
        BWTask(
            group="scientific", scenario=str(scenario), n=int(n),
            replicate=replicate,
            specification=deepcopy(config["regimes"][scenario]),
        )
        for n in profile["n_values"]
        for scenario in profile["regimes"]
        for replicate in range(int(profile["replicates"]))
    ]


def _task_key(task: BWTask) -> tuple[str, int, int]:
    return task.scenario, task.n, task.replicate


def _row_key(row: pd.Series) -> tuple[str, int, int]:
    return str(row["scenario"]), int(row["n"]), int(row["replicate"])


def _seed_key(config: dict[str, Any], task: BWTask) -> str:
    return ".".join(map(str, (
        int(config["experiment"]["root_seed"]),
        int(config["profile"]["seed_namespace"]),
        task.n, task.replicate,
    )))


def _parent_seed(config: dict[str, Any], task: BWTask) -> int:
    digest = hashlib.sha256(
        f"{_seed_key(config, task)}:{task.scenario}".encode("utf-8")
    ).digest()
    return 1 + int.from_bytes(digest[:4], "little") % (2**31 - 2)


def _resolve_project_r_library() -> Path | None:
    declared = os.environ.get("R_LIBS_USER")
    if declared:
        path = Path(declared)
        if path.is_dir():
            return path
    root = ROOT / "renv" / "library" / "windows"
    if not root.is_dir():
        return None
    candidates = [
        path.parents[1] for path in root.glob("*/*/renv/DESCRIPTION")
    ]
    return candidates[0] if len(candidates) == 1 else None


def check_r_environment(rscript: Path) -> None:
    if not rscript.is_file():
        raise FileNotFoundError(f"Rscript does not exist: {rscript}")
    if not R_WORKER.is_file() or not PARENT_SOURCE.is_file():
        raise FileNotFoundError("parent R worker or cloned BWS_util.R is missing")
    env = os.environ.copy()
    library = _resolve_project_r_library()
    if library is not None:
        env["R_LIBS_USER"] = str(library)
    env["RENV_CONFIG_AUTOLOADER_ENABLED"] = "FALSE"
    command = [
        str(rscript), "--vanilla", "-e",
        "stopifnot(requireNamespace('maotai',quietly=TRUE),"
        "requireNamespace('expm',quietly=TRUE),"
        "requireNamespace('deSolve',quietly=TRUE));cat('parent R ready\\n')",
    ]
    completed = subprocess.run(
        command, cwd=ROOT, env=env, capture_output=True, text=True, timeout=90,
        check=False,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip()
        raise RuntimeError(f"parent R preflight failed: {detail}")


def _write_panel(path: Path, observations: np.ndarray) -> None:
    flat = np.asarray(observations, dtype=float).reshape(observations.shape[0], -1)
    np.savetxt(path, flat, delimiter=",", fmt="%.17g")


def _read_status(directory: Path, prefix: str) -> tuple[str, str]:
    path = directory / f"{prefix}_status.txt"
    if not path.is_file():
        return "error", "parent worker did not write a status file"
    lines = path.read_text(encoding="utf-8").splitlines()
    return lines[0].strip(), " ".join(lines[1:]).strip()


def _read_matrix(path: Path, shape: tuple[int, ...]) -> np.ndarray:
    value = np.loadtxt(path, delimiter=",", ndmin=2)
    expected = int(np.prod(shape))
    if value.size != expected:
        raise ValueError(f"{path.name} has {value.size} values; expected {expected}")
    value = value.reshape(shape)
    if not np.isfinite(value).all():
        raise FloatingPointError(f"{path.name} contains NaN or Inf")
    return value


def _run_parent(
    observations: np.ndarray,
    config: dict[str, Any],
    task: BWTask,
    rscript: Path,
) -> dict[str, Any]:
    n, m, _ = observations.shape
    rank = int(config["experiment"]["factor_rank"])
    parent = config["parent"]
    env = os.environ.copy()
    library = _resolve_project_r_library()
    if library is not None:
        env["R_LIBS_USER"] = str(library)
    env["RENV_CONFIG_AUTOLOADER_ENABLED"] = "FALSE"
    with tempfile.TemporaryDirectory(prefix="rfd_parent_bw_") as temporary:
        directory = Path(temporary)
        input_path = directory / "observations.csv"
        mean_path = directory / "verified_mean.csv"
        output_path = directory / "output"
        _write_panel(input_path, observations)
        mean_result = BW_GEOMETRY.barycentre(
            observations, tol=float(parent["sensitivity_mean_tolerance"]),
            max_iter=int(parent["sensitivity_mean_max_iterations"]),
        )
        np.savetxt(
            mean_path, np.asarray(mean_result.X).reshape(1, -1),
            delimiter=",", fmt="%.17g",
        )
        command = [
            str(rscript), "--vanilla", str(R_WORKER), str(input_path),
            str(mean_path), str(output_path), str(n), str(m), str(rank),
            str(int(config["estimator"]["max_lag"])),
            str(_parent_seed(config, task)), str(int(parent["batch_size"])),
            str(int(parent["budget_iterations"])),
        ]
        completed = subprocess.run(
            command, cwd=ROOT, env=env, capture_output=True, text=True,
            check=False,
        )
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip()
            raise RuntimeError(f"parent R worker exited {completed.returncode}: {detail}")
        result: dict[str, Any] = {
            "sensitivity_mean_converged": bool(mean_result.converged),
            "sensitivity_mean_iterations": int(mean_result.n_iter),
            "sensitivity_mean_residual": float(mean_result.residual),
        }
        for prefix in ("budget", "converged"):
            status, message = _read_status(output_path, prefix)
            result[f"{prefix}_status"] = status
            result[f"{prefix}_message"] = message
            if status != "ok":
                continue
            result[f"{prefix}_mean"] = _read_matrix(
                output_path / f"{prefix}_mean.csv", (m, m)
            )
            result[f"{prefix}_scores"] = _read_matrix(
                output_path / f"{prefix}_scores.csv", (n, rank)
            )
            result[f"{prefix}_loadings"] = _read_matrix(
                output_path / f"{prefix}_loadings.csv", (rank, m, m)
            )
            result[f"{prefix}_reconstruction"] = _read_matrix(
                output_path / f"{prefix}_reconstruction.csv", (n, m, m)
            )
        return result


def _projector_error(
    loading_tangents: np.ndarray,
    source: np.ndarray,
    base: np.ndarray,
    truth_projector: np.ndarray,
) -> float:
    transported = BW_GEOMETRY.transport(loading_tangents, source, base)
    coordinates = tangent_coordinates(
        transported, base, BW_GEOMETRY.tangent_basis(base), BW_GEOMETRY
    )
    estimate = _projector_from_rows(coordinates)
    return float(np.linalg.norm(estimate - truth_projector, ord=2))


def _rfd_metrics(sample, base: np.ndarray, fit) -> dict[str, float]:
    basis = BW_GEOMETRY.tangent_basis(base)
    truth_coordinates = tangent_coordinates(
        sample.loadings, base, basis, BW_GEOMETRY
    )
    truth_projector = _projector_from_rows(truth_coordinates)
    loading_tangents = coordinate_tangents(
        fit.loadings.T, fit.tangent_rows.basis
    )
    target_scores = sample.factors - sample.factors.mean(axis=0)
    latent_signal = BW_GEOMETRY.exp(sample.centres, sample.factor_effects)
    return {
        "centre_path_rms": _intrinsic_rms(
            BW_GEOMETRY, fit.tangent_rows.local_centres, sample.centres
        ),
        "loading_error": _projector_error(
            loading_tangents, fit.centre.polygon.reference_point,
            base, truth_projector,
        ),
        "factor_nrmse": _procrustes_nrmse(fit.factor_scores, target_scores),
        "observation_reconstruction_rms": _intrinsic_rms(
            BW_GEOMETRY, fit.reconstructed_observations, sample.observations
        ),
        "signal_reconstruction_rms": _intrinsic_rms(
            BW_GEOMETRY, fit.reconstructed_observations, latent_signal
        ),
    }


def _parent_metrics(
    sample,
    base: np.ndarray,
    parent: dict[str, Any],
    prefix: str,
) -> dict[str, float]:
    basis = BW_GEOMETRY.tangent_basis(base)
    truth_coordinates = tangent_coordinates(
        sample.loadings, base, basis, BW_GEOMETRY
    )
    truth_projector = _projector_from_rows(truth_coordinates)
    mean = parent[f"{prefix}_mean"]
    reconstruction = parent[f"{prefix}_reconstruction"]
    latent_signal = BW_GEOMETRY.exp(sample.centres, sample.factor_effects)
    target_scores = sample.factors - sample.factors.mean(axis=0)
    return {
        "centre_path_rms": _intrinsic_rms(BW_GEOMETRY, mean, sample.centres),
        "loading_error": _projector_error(
            parent[f"{prefix}_loadings"], mean, base, truth_projector
        ),
        "factor_nrmse": _procrustes_nrmse(
            parent[f"{prefix}_scores"], target_scores
        ),
        "observation_reconstruction_rms": _intrinsic_rms(
            BW_GEOMETRY, reconstruction, sample.observations
        ),
        "signal_reconstruction_rms": _intrinsic_rms(
            BW_GEOMETRY, reconstruction, latent_signal
        ),
    }


def _nonconverged_stages(fit) -> int:
    stages = []
    for estimate in fit.centre.estimates:
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is not None:
                stages.extend(one_sided.stages.stages)
    return int(sum(not stage.converged for stage in stages))


def run_task(
    config: dict[str, Any], task: BWTask, rscript: Path
) -> dict[str, Any]:
    started = time.perf_counter()
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": config["profile_name"], "scenario": task.scenario,
        "scenario_label": task.specification["label"],
        "scenario_class": task.specification["class"], "n": task.n,
        "matrix_size": int(config["experiment"]["matrix_size"]),
        "replicate": task.replicate, "seed_key": _seed_key(config, task),
        "true_rank": int(config["experiment"]["factor_rank"]),
    })
    try:
        stage = time.perf_counter()
        sample, base, _, _ = generate_fit_sample(config, task)
        row["generation_seconds"] = time.perf_counter() - stage
        spectra = np.linalg.eigvalsh(sample.observations)
        row.update({
            "centre_path_length": sample.centre_path_length,
            "centre_path_energy": sample.centre_path_energy,
            "true_centre_observation_rms": _intrinsic_rms(
                BW_GEOMETRY, sample.centres, sample.observations
            ),
            "true_centre_signal_rms": _intrinsic_rms(
                BW_GEOMETRY, sample.centres,
                BW_GEOMETRY.exp(sample.centres, sample.factor_effects),
            ),
            "observation_min_eigenvalue": float(np.min(spectra)),
            "observation_max_eigenvalue": float(np.max(spectra)),
        })

        stage = time.perf_counter()
        fit = fit_rfd(
            sample.observations, sample.time, BW_GEOMETRY,
            _model_config(config, task),
        )
        row["rfd_seconds"] = time.perf_counter() - stage
        row["rfd_fallback_count"] = int(fit.centre.fallback_count)
        row["rfd_nonconverged_stages"] = _nonconverged_stages(fit)
        for metric, value in _rfd_metrics(sample, base, fit).items():
            row[f"rfd_{metric}"] = value

        stage = time.perf_counter()
        parent = _run_parent(sample.observations, config, task, rscript)
        row["parent_seconds"] = time.perf_counter() - stage
        row["parent_sensitivity_mean_converged"] = parent["sensitivity_mean_converged"]
        row["parent_sensitivity_mean_iterations"] = parent["sensitivity_mean_iterations"]
        row["parent_sensitivity_mean_residual"] = parent["sensitivity_mean_residual"]
        for prefix in ("budget", "converged"):
            row[f"parent_{prefix}_status"] = parent[f"{prefix}_status"]
            row[f"parent_{prefix}_message"] = parent[f"{prefix}_message"]
            if parent[f"{prefix}_status"] == "ok":
                metrics = _parent_metrics(sample, base, parent, prefix)
                for metric, value in metrics.items():
                    row[f"parent_{prefix}_{metric}"] = value

        budget = row["parent_budget_signal_reconstruction_rms"]
        converged = row["parent_converged_signal_reconstruction_rms"]
        rfd = row["rfd_signal_reconstruction_rms"]
        if np.isfinite(budget) and budget > 0.0:
            row["rfd_over_parent_budget_signal_rms"] = rfd / budget
        if np.isfinite(converged) and converged > 0.0:
            row["rfd_over_parent_converged_signal_rms"] = rfd / converged
        parent_ok = all(
            row[f"parent_{prefix}_status"] == "ok"
            for prefix in ("budget", "converged")
        )
        row.update({
            "status": "ok" if parent_ok else "partial",
            "error_type": "", "error_message": "",
        })
    except Exception as error:
        row.update({
            "status": "error", "error_type": type(error).__name__,
            "error_message": str(error).replace("\n", " ")[:1000],
        })
    row["elapsed_seconds"] = time.perf_counter() - started
    return row


def _default_output(config: dict[str, Any]) -> Path:
    return ROOT / str(config["profile"]["output_dir"])


def _read_raw(path: Path) -> pd.DataFrame:
    if not path.is_file() or path.stat().st_size == 0:
        return pd.DataFrame(columns=RAW_COLUMNS)
    return pd.read_csv(path)


def _append_row(path: Path, row: dict[str, Any]) -> None:
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


def _initialize(config: dict[str, Any], output: Path, rscript: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    metadata = {
        "experiment": config["experiment"]["id"],
        "profile": config["profile_name"],
        "config_sha256": _digest(config["config_path"]),
        "parent_source_sha256": _digest(PARENT_SOURCE),
        "r_worker_sha256": _digest(R_WORKER),
        "root_seed": int(config["experiment"]["root_seed"]),
        "seed_namespace": int(config["profile"]["seed_namespace"]),
        "python": platform.python_version(), "numpy": np.__version__,
        "rscript": str(rscript), "platform": platform.platform(),
        "rank_policy": "known DGP rank supplied to every method",
    }
    path = output / "metadata.json"
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        for key in (
            "experiment", "profile", "config_sha256", "parent_source_sha256",
            "r_worker_sha256", "root_seed", "seed_namespace",
        ):
            if existing.get(key) != metadata[key]:
                raise RuntimeError(f"existing output metadata disagrees on {key}")
    else:
        path.write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        shutil.copy2(config["config_path"], output / "source_config.yaml")


def _summarize(raw: pd.DataFrame, output: Path) -> None:
    usable = raw.loc[raw["status"].isin(("ok", "partial"))].copy()
    if usable.empty:
        return
    rows: list[dict[str, Any]] = []
    for (scenario, n), group in usable.groupby(["scenario", "n"], sort=False):
        summary: dict[str, Any] = {
            "scenario": scenario, "n": int(n), "completed": len(group),
            "fully_successful": int((group["status"] == "ok").sum()),
        }
        for method in METHODS:
            for metric in METHOD_METRICS:
                values = pd.to_numeric(group[f"{method}_{metric}"], errors="coerce")
                summary[f"{method}_{metric}_median"] = float(values.median())
                summary[f"{method}_{metric}_q25"] = float(values.quantile(0.25))
                summary[f"{method}_{metric}_q75"] = float(values.quantile(0.75))
        for parent in ("parent_budget", "parent_converged"):
            left = pd.to_numeric(group["rfd_signal_reconstruction_rms"], errors="coerce")
            right = pd.to_numeric(
                group[f"{parent}_signal_reconstruction_rms"], errors="coerce"
            )
            valid = left.notna() & right.notna()
            summary[f"rfd_win_rate_vs_{parent}"] = float(
                (left[valid] < right[valid]).mean()
            ) if valid.any() else np.nan
            summary[f"rfd_over_{parent}_signal_rms_median"] = float(
                (left[valid] / right[valid]).median()
            ) if valid.any() else np.nan
        rows.append(summary)
    summary_frame = pd.DataFrame(rows)
    summary_frame.to_csv(output / "summary.csv", index=False)
    _write_plots(summary_frame, output)
    report = [
        "# Parent RFM versus RFD on paired regular BW draws", "",
        "Both methods receive each identical generated panel, the known DGP rank,",
        "and the same nonzero lags. This isolates geometric preprocessing; it is",
        "not a forecasting or rank-selection experiment.", "",
        f"- requested/recorded rows: {len(raw)}",
        f"- fully successful rows: {(raw['status'] == 'ok').sum()}",
        f"- partial parent rows: {(raw['status'] == 'partial').sum()}",
        f"- fatal rows: {(raw['status'] == 'error').sum()}",
        "- parent variants: published simulation budget and verified deterministic global mean",
        "- primary paired outcome: intrinsic RMS to the latent signal", "",
        "See `summary.csv` for medians, interquartile ranges, paired win rates,",
        "and direct error multipliers. Do not interpret these in-sample recovery",
        "numbers as forecasts.", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")


def _write_plots(summary: pd.DataFrame, output: Path) -> None:
    scenarios = list(dict.fromkeys(summary["scenario"]))
    figure, axes = plt.subplots(2, 3, figsize=(13, 7), sharex=True)
    for axis, scenario in zip(axes.flat, scenarios):
        frame = summary.loc[summary["scenario"] == scenario].sort_values("n")
        for method, label, colour, style in (
            ("rfd", "RFD", "#0072B2", "-"),
            ("parent_budget", "parent budget", "#D55E00", "--"),
            ("parent_converged", "parent verified mean", "#009E73", ":"),
        ):
            axis.plot(
                frame["n"], frame[f"{method}_signal_reconstruction_rms_median"],
                marker="o", color=colour, linestyle=style, label=label,
            )
        axis.set_title(scenario)
        axis.set_xscale("log", base=2)
        axis.set_yscale("log")
        axis.grid(alpha=0.2)
    axes[0, 0].legend(frameon=False, fontsize=8)
    figure.supxlabel("observations")
    figure.supylabel("latent-signal reconstruction RMS")
    figure.tight_layout()
    figure.savefig(output / "signal_reconstruction.png", dpi=180)
    plt.close(figure)

    pivot = summary.pivot(
        index="scenario", columns="n",
        values="rfd_over_parent_converged_signal_rms_median",
    ).reindex(scenarios)
    figure, axis = plt.subplots(figsize=(7.5, 4.5))
    image = axis.imshow(pivot.to_numpy(), aspect="auto", cmap="RdYlGn_r", vmin=0.5, vmax=1.5)
    axis.set_xticks(range(len(pivot.columns)), [f"{int(value):,}" for value in pivot.columns])
    axis.set_yticks(range(len(pivot.index)), pivot.index)
    axis.set_xlabel("observations")
    axis.set_title("RFD error relative to parent verified-mean RFM")
    for row_index in range(pivot.shape[0]):
        for column_index in range(pivot.shape[1]):
            value = pivot.iloc[row_index, column_index]
            if np.isfinite(value):
                axis.text(column_index, row_index, f"{value:.2f}×", ha="center", va="center", fontsize=8)
    colourbar = figure.colorbar(image, ax=axis)
    colourbar.set_label("error multiplier (below 1 favours RFD)")
    figure.tight_layout()
    figure.savefig(output / "paired_signal_multiplier.png", dpi=180)
    plt.close(figure)


def run(
    config: dict[str, Any], output: Path, rscript: Path, *, workers: int,
    max_tasks: int | None = None,
) -> None:
    _initialize(config, output, rscript)
    raw_path = output / "raw.csv"
    raw = _read_raw(raw_path)
    completed = {_row_key(row) for _, row in raw.iterrows()}
    pending = [task for task in build_tasks(config) if _task_key(task) not in completed]
    if max_tasks is not None:
        pending = pending[:max_tasks]
    if not pending:
        _summarize(raw, output)
        print("No pending rows; summaries refreshed.", flush=True)
        return
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(run_task, config, task, rscript): task
            for task in pending
        }
        completed_now = 0
        for future in concurrent.futures.as_completed(futures):
            row = future.result()
            _append_row(raw_path, row)
            completed_now += 1
            print(
                f"[{completed_now}/{len(pending)}] {row['scenario']} "
                f"n={row['n']} rep={row['replicate']} status={row['status']} "
                f"elapsed={float(row['elapsed_seconds']):.1f}s",
                flush=True,
            )
    _summarize(_read_raw(raw_path), output)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--profile", choices=("smoke", "overnight"), default="smoke")
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument("--rscript", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check-r", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.workers < 1 or args.workers > 8:
        raise ValueError("workers must lie between one and eight")
    if args.max_tasks is not None and args.max_tasks < 1:
        raise ValueError("max-tasks must be positive")
    rscript_value = args.rscript if args.rscript is not None else shutil.which("Rscript")
    if rscript_value is None:
        raise FileNotFoundError("Rscript was not found")
    rscript = Path(rscript_value).resolve()
    config = load_configuration(args.config.resolve(), args.profile)
    tasks = build_tasks(config)
    output = args.output.resolve() if args.output else _default_output(config)
    print(f"profile: {config['profile_name']}")
    print(f"output: {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}")
    print(f"paired DGP tasks: {len(tasks)}")
    print(f"method fits per task: 3 (RFD + 2 parent mean budgets)")
    print(f"total estimator fits: {3 * len(tasks)}")
    print(f"workers: {args.workers} (one BLAS thread each)")
    print("rank: known DGP rank supplied to every method")
    if args.check_r or not args.dry_run:
        check_r_environment(rscript)
    if args.dry_run or args.check_r:
        return 0
    try:
        run(
            config, output, rscript, workers=args.workers,
            max_tasks=args.max_tasks,
        )
    except KeyboardInterrupt:
        print("\nInterrupted. Finished rows are durable; rerun to resume.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
