"""Compare direct VAR and latent-score Kalman heads on causal BW panels.

Each synthetic draw is split once into an 80% training prefix and a 20%
sequential holdout.  Oracle, fixed-centre RFM-compatible, and moving-centre
RFD score representations are built from the training prefix.  VAR and Kalman
parameters are then frozen; every holdout prediction precedes the score used
to update the next prediction.  The known factors test amplitude recovery,
while guarded BW reconstructions separately test numerical stability.
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
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

for _name in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[_name] = "1"

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
from rfd.estimators.frame import (  # noqa: E402
    PolygonalFrame,
    transport_from_reference,
    transport_to_reference,
)
from rfd.estimators.lag import (  # noqa: E402
    assemble_lag_operator,
    coordinate_tangents,
    decompose_lag_operator,
    extract_dynamic_factors,
    lag_cross_covariances,
    tangent_coordinates,
)
from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402
from rfd.forecast import (  # noqa: E402
    filter_score_state_space,
    fit_score_state_space,
    fit_var1,
)
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.model import fit_rfd  # noqa: E402
from rfd.spd.bw import bw_clip_exp_tangent  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "score_filter_bw.yaml"
REPRESENTATIONS = ("oracle", "rfm", "rfd")
HEADS = ("var", "kf")
SCORE_METRICS = (
    "observed_score_nrmse", "kf_filtered_nrmse",
    "var_forecast_nrmse", "kf_forecast_nrmse",
    "kf_over_var_forecast_nrmse", "var_radius", "kf_radius",
    "kf_measurement_fraction", "kf_converged", "kf_iterations",
)
MATRIX_METRICS = (
    "signal_frobenius2", "signal_bw2", "signal_qlike",
    "observation_frobenius2", "clip_rate", "clip_min_factor",
    "forecast_min_eigenvalue", "forecast_max_condition",
)
IDENTITY_COLUMNS = [
    "profile", "scenario", "scenario_label", "scenario_class", "n",
    "n_train", "n_test", "replicate", "seed_key", "status",
    "error_type", "error_message", "matrix_size", "true_rank",
    "noise_scale", "centre_path_length", "rfd_fallback_count",
    "rfd_nonconverged_stages", "elapsed_seconds",
]
RAW_COLUMNS = (
    IDENTITY_COLUMNS
    + [f"{rep}_{metric}" for rep in REPRESENTATIONS for metric in SCORE_METRICS]
    + [
        f"{rep}_{head}_{metric}"
        for rep in REPRESENTATIONS
        for head in HEADS
        for metric in MATRIX_METRICS
    ]
)


@dataclass(frozen=True)
class ScoreRepresentation:
    name: str
    train_scores: np.ndarray
    test_scores: np.ndarray
    row_mean: np.ndarray
    loadings: np.ndarray
    basis: np.ndarray
    source_point: np.ndarray
    forecast_centres: np.ndarray
    frame: PolygonalFrame | None = None


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
        "head": deepcopy(source["head"]),
        "scenarios": deepcopy(source["scenarios"]),
        "config_path": path.resolve(),
    }
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    profile = config["profile"]
    experiment = config["experiment"]
    head = config["head"]
    rank = int(experiment["factor_rank"])
    matrix_size = int(experiment["matrix_size"])
    if experiment["geometry"] != "bw":
        raise ValueError("score-filter experiment requires BW geometry")
    if rank < 1 or matrix_size * (matrix_size + 1) // 2 <= rank:
        raise ValueError("rank must be positive and below tangent dimension")
    if len(experiment["factor_persistence"]) != rank:
        raise ValueError("factor persistence must match rank")
    if len(experiment["factor_scale"]) != rank:
        raise ValueError("factor scale must match rank")
    fraction = float(head["train_fraction"])
    if not 0.5 < fraction < 0.95:
        raise ValueError("train_fraction must lie between 0.5 and 0.95")
    if not 0.0 < float(head["bw_step_margin"]) < 1.0:
        raise ValueError("bw_step_margin must lie inside (0, 1)")
    n_values = [int(value) for value in profile["n_values"]]
    if not n_values or min(n_values) < 32 or len(set(n_values)) != len(n_values):
        raise ValueError("n_values must be unique and at least 32")
    if int(profile["replicates"]) < 1:
        raise ValueError("replicates must be positive")
    for name in profile["scenarios"]:
        if name not in config["scenarios"]:
            raise ValueError(f"unknown scenario: {name}")
        specification = config["scenarios"][name]
        if int(specification["rank"]) != rank:
            raise ValueError("all score-filter scenarios must use the true rank")
        if specification["path"] not in ("commuting", "curved"):
            raise ValueError("only regular commuting or curved paths are allowed")


def build_tasks(config: dict[str, Any]) -> list[BWTask]:
    profile = config["profile"]
    return [
        BWTask(
            group="scientific", scenario=str(scenario), n=int(n),
            replicate=replicate,
            specification=deepcopy(config["scenarios"][scenario]),
        )
        for n in profile["n_values"]
        for scenario in profile["scenarios"]
        for replicate in range(int(profile["replicates"]))
    ]


def _training_size(config: dict[str, Any], n: int) -> int:
    size = int(np.floor(float(config["head"]["train_fraction"]) * n))
    return min(n - 8, max(16, size))


def _procrustes(train_scores: np.ndarray, target: np.ndarray) -> np.ndarray:
    left, _, right = np.linalg.svd(
        np.asarray(train_scores).T @ np.asarray(target), full_matrices=False
    )
    return left @ right


def _nrmse(estimate: np.ndarray, target: np.ndarray) -> float:
    denominator = float(np.linalg.norm(target))
    if denominator <= 0.0:
        raise ValueError("factor target has zero norm")
    return float(np.linalg.norm(estimate - target) / denominator)


def _fixed_representation(
    train_observations: np.ndarray,
    test_observations: np.ndarray,
    config: dict[str, Any],
) -> ScoreRepresentation:
    mean = BW_GEOMETRY.barycentre(
        train_observations,
        tol=float(config["estimator"]["mean_tolerance"]),
        max_iter=int(config["estimator"]["mean_max_iter"]),
    )
    if not mean.converged:
        raise RuntimeError("global BW mean did not converge")
    basis = BW_GEOMETRY.tangent_basis(mean.X)
    train_rows = tangent_coordinates(
        BW_GEOMETRY.log(mean.X, train_observations),
        mean.X, basis, BW_GEOMETRY,
    )
    test_rows = tangent_coordinates(
        BW_GEOMETRY.log(mean.X, test_observations),
        mean.X, basis, BW_GEOMETRY,
    )
    lag = lag_cross_covariances(
        train_rows, int(config["estimator"]["max_lag"]),
        tail_mode=str(config["estimator"]["tail_mode"]),
        normalization=str(config["estimator"]["normalization"]),
    )
    factors = extract_dynamic_factors(
        decompose_lag_operator(assemble_lag_operator(lag)),
        int(config["experiment"]["factor_rank"]),
    )
    test_scores = (test_rows - factors.row_mean) @ factors.loadings
    return ScoreRepresentation(
        name="rfm", train_scores=factors.factor_scores,
        test_scores=test_scores, row_mean=factors.row_mean,
        loadings=factors.loadings, basis=basis, source_point=mean.X,
        forecast_centres=np.broadcast_to(
            mean.X, (test_observations.shape[0],) + mean.X.shape
        ).copy(),
    )


def _rfd_representation(
    train_observations: np.ndarray,
    test_observations: np.ndarray,
    config: dict[str, Any],
    task: BWTask,
) -> tuple[ScoreRepresentation, Any]:
    n_train = train_observations.shape[0]
    train_task = BWTask(
        group=task.group, scenario=task.scenario, n=n_train,
        replicate=task.replicate, specification=deepcopy(task.specification),
    )
    train_time = np.arange(1, n_train + 1, dtype=float) / n_train
    fit = fit_rfd(
        train_observations, train_time, BW_GEOMETRY,
        _model_config(config, train_task),
    )
    frame = fit.centre.polygon
    terminal_time = float(frame.vertex_times[-1])
    terminal = frame.vertices[-1]
    local_test = BW_GEOMETRY.log(terminal, test_observations)
    reference_test = transport_to_reference(
        frame, local_test,
        np.full(test_observations.shape[0], terminal_time),
    )
    test_rows = tangent_coordinates(
        reference_test, frame.reference_point,
        fit.tangent_rows.basis, BW_GEOMETRY,
    )
    test_scores = (test_rows - fit.factors.row_mean) @ fit.loadings
    representation = ScoreRepresentation(
        name="rfd", train_scores=fit.factor_scores,
        test_scores=test_scores, row_mean=fit.factors.row_mean,
        loadings=fit.loadings, basis=fit.tangent_rows.basis,
        source_point=frame.reference_point,
        forecast_centres=np.broadcast_to(
            terminal, (test_observations.shape[0],) + terminal.shape
        ).copy(),
        frame=frame,
    )
    return representation, fit


def _oracle_representation(
    sample: Any,
    base: np.ndarray,
    n_train: int,
) -> ScoreRepresentation:
    basis = BW_GEOMETRY.tangent_basis(base)
    local = BW_GEOMETRY.log(sample.centres, sample.observations)
    reference = BW_GEOMETRY.transport(local, sample.centres, base)
    rows = tangent_coordinates(reference, base, basis, BW_GEOMETRY)
    loading_rows = tangent_coordinates(
        sample.loadings, base, basis, BW_GEOMETRY
    )
    row_mean = rows[:n_train].mean(axis=0)
    scores = (rows - row_mean) @ loading_rows.T
    return ScoreRepresentation(
        name="oracle", train_scores=scores[:n_train],
        test_scores=scores[n_train:], row_mean=row_mean,
        loadings=loading_rows.T, basis=basis, source_point=base,
        forecast_centres=sample.centres[n_train:].copy(),
    )


def _head_predictions(
    representation: ScoreRepresentation,
    config: dict[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, float]]:
    train = representation.train_scores
    test = representation.test_scores
    var = fit_var1(train)
    previous = np.vstack((train[-1], test[:-1]))
    var_predictions = np.stack([var.forecast(value) for value in previous])
    head = config["head"]
    state = fit_score_state_space(
        train,
        max_iter=int(head["state_max_iterations"]),
        tolerance=float(head["state_tolerance"]),
        covariance_floor=float(head["covariance_floor"]),
        maximum_radius=float(head["maximum_transition_radius"]),
    )
    causal = filter_score_state_space(np.vstack((train, test)), state)
    start = train.shape[0]
    variance = float(
        np.trace(state.process_covariance + state.measurement_covariance)
    )
    diagnostics = {
        "var_radius": float(np.max(np.abs(np.linalg.eigvals(
            var.coefficients[1:].T
        )))),
        "kf_radius": float(np.max(np.abs(np.linalg.eigvals(state.transition)))),
        "kf_measurement_fraction": float(
            np.trace(state.measurement_covariance) / variance
        ),
        "kf_converged": float(state.converged),
        "kf_iterations": float(state.n_iter),
    }
    predictions = {
        "var": var_predictions,
        "kf": causal.predicted_states[start:],
        "kf_filtered": causal.filtered_states[start:],
    }
    return predictions, diagnostics


def _decode(
    representation: ScoreRepresentation,
    scores: np.ndarray,
    config: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray]:
    rows = representation.row_mean + scores @ representation.loadings.T
    reference_vectors = coordinate_tangents(rows, representation.basis)
    if representation.frame is None:
        local_vectors = BW_GEOMETRY.transport(
            reference_vectors, representation.source_point,
            representation.forecast_centres,
        )
    else:
        local_vectors = transport_from_reference(
            representation.frame, reference_vectors,
            np.full(scores.shape[0], representation.frame.vertex_times[-1]),
        )
    clipped = bw_clip_exp_tangent(
        representation.forecast_centres, local_vectors,
        step_margin=float(config["head"]["bw_step_margin"]),
    )
    forecasts = BW_GEOMETRY.exp(
        representation.forecast_centres, clipped.tangent
    )
    return forecasts, clipped.factors


def _matrix_metrics(
    forecasts: np.ndarray,
    clip_factors: np.ndarray,
    latent_signal: np.ndarray,
    observations: np.ndarray,
) -> dict[str, float]:
    eigenvalues = np.linalg.eigvalsh(forecasts)
    return {
        "signal_frobenius2": float(np.mean(frobenius_loss(
            forecasts, latent_signal
        ))),
        "signal_bw2": float(np.mean(bw_loss(forecasts, latent_signal))),
        "signal_qlike": float(np.mean(qlike_loss(forecasts, latent_signal))),
        "observation_frobenius2": float(np.mean(frobenius_loss(
            forecasts, observations
        ))),
        "clip_rate": float(np.mean(clip_factors < 1.0 - 1e-12)),
        "clip_min_factor": float(np.min(clip_factors)),
        "forecast_min_eigenvalue": float(np.min(eigenvalues)),
        "forecast_max_condition": float(np.max(
            eigenvalues[:, -1] / eigenvalues[:, 0]
        )),
    }


def _nonconverged_stages(fit: Any) -> int:
    stages = []
    for estimate in fit.centre.estimates:
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is not None:
                stages.extend(one_sided.stages.stages)
    return int(sum(not stage.converged for stage in stages))


def evaluate_task(config: dict[str, Any], task: BWTask) -> dict[str, Any]:
    sample, base, _, _ = generate_fit_sample(config, task)
    n_train = _training_size(config, task.n)
    true_mean = sample.factors[:n_train].mean(axis=0)
    target_train = sample.factors[:n_train] - true_mean
    target_test = sample.factors[n_train:] - true_mean
    train_observations = sample.observations[:n_train]
    test_observations = sample.observations[n_train:]
    representations: dict[str, ScoreRepresentation] = {}
    representations["oracle"] = _oracle_representation(sample, base, n_train)
    representations["rfm"] = _fixed_representation(
        train_observations, test_observations, config
    )
    representations["rfd"], rfd_fit = _rfd_representation(
        train_observations, test_observations, config, task
    )
    latent_signal = BW_GEOMETRY.exp(
        sample.centres[n_train:], sample.factor_effects[n_train:]
    )
    result: dict[str, Any] = {
        "n_train": n_train,
        "n_test": task.n - n_train,
        "centre_path_length": float(sample.centre_path_length),
        "rfd_fallback_count": int(rfd_fit.centre.fallback_count),
        "rfd_nonconverged_stages": _nonconverged_stages(rfd_fit),
    }
    for name, representation in representations.items():
        alignment = _procrustes(representation.train_scores, target_train)
        predictions, diagnostics = _head_predictions(representation, config)
        result[f"{name}_observed_score_nrmse"] = _nrmse(
            representation.test_scores @ alignment, target_test
        )
        result[f"{name}_kf_filtered_nrmse"] = _nrmse(
            predictions["kf_filtered"] @ alignment, target_test
        )
        for key in ("var_radius", "kf_radius", "kf_measurement_fraction",
                    "kf_converged", "kf_iterations"):
            result[f"{name}_{key}"] = diagnostics[key]
        for head_name in HEADS:
            estimate = predictions[head_name] @ alignment
            result[f"{name}_{head_name}_forecast_nrmse"] = _nrmse(
                estimate, target_test
            )
            forecasts, factors = _decode(
                representation, predictions[head_name], config
            )
            for metric, value in _matrix_metrics(
                forecasts, factors, latent_signal, test_observations
            ).items():
                result[f"{name}_{head_name}_{metric}"] = value
        result[f"{name}_kf_over_var_forecast_nrmse"] = (
            result[f"{name}_kf_forecast_nrmse"]
            / result[f"{name}_var_forecast_nrmse"]
        )
    return result


def _seed_key(config: dict[str, Any], task: BWTask) -> str:
    return ".".join(map(str, (
        int(config["experiment"]["root_seed"]),
        int(config["profile"]["seed_namespace"]), task.scenario,
        task.n, task.replicate,
    )))


def run_task(config: dict[str, Any], task: BWTask) -> dict[str, Any]:
    started = time.perf_counter()
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": config["profile_name"], "scenario": task.scenario,
        "scenario_label": task.specification["label"],
        "scenario_class": task.specification["class"], "n": task.n,
        "replicate": task.replicate, "seed_key": _seed_key(config, task),
        "matrix_size": int(config["experiment"]["matrix_size"]),
        "true_rank": int(config["experiment"]["factor_rank"]),
        "noise_scale": float(task.specification["noise_scale"]),
    })
    try:
        row.update(evaluate_task(config, task))
        row.update({"status": "ok", "error_type": "", "error_message": ""})
    except Exception as error:
        row.update({
            "status": "error", "error_type": type(error).__name__,
            "error_message": str(error).replace("\n", " ")[:1000],
        })
    row["elapsed_seconds"] = time.perf_counter() - started
    return row


def _task_key(task: BWTask) -> tuple[str, int, int]:
    return task.scenario, task.n, task.replicate


def _row_key(row: pd.Series) -> tuple[str, int, int]:
    return str(row["scenario"]), int(row["n"]), int(row["replicate"])


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


def _initialize(config: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    metadata = {
        "experiment": config["experiment"]["id"],
        "profile": config["profile_name"],
        "recorded": bool(config["profile"]["recorded"]),
        "config_sha256": _digest(config["config_path"]),
        "root_seed": int(config["experiment"]["root_seed"]),
        "seed_namespace": int(config["profile"]["seed_namespace"]),
        "python": platform.python_version(), "numpy": np.__version__,
        "platform": platform.platform(),
        "rank_policy": "known DGP rank supplied to every representation",
        "split_policy": "one frozen prefix; heads fitted on prefix only",
    }
    path = output / "metadata.json"
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        for key in (
            "experiment", "profile", "config_sha256", "root_seed",
            "seed_namespace",
        ):
            if existing.get(key) != metadata[key]:
                raise RuntimeError(f"existing output metadata disagrees on {key}")
    else:
        path.write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        shutil.copy2(config["config_path"], output / "score_filter_bw.yaml")


def _write_plots(summary: pd.DataFrame, output: Path) -> None:
    scenarios = list(dict.fromkeys(summary["scenario"]))
    figure, axes = plt.subplots(2, 3, figsize=(13, 7), sharex=True)
    for axis, scenario in zip(axes.flat, scenarios):
        frame = summary.loc[summary["scenario"] == scenario].sort_values("n")
        for representation, colour in (("rfm", "#6A3D9A"), ("rfd", "#0072B2")):
            for head, style in (("var", "--"), ("kf", "-")):
                axis.plot(
                    frame["n"],
                    frame[f"{representation}_{head}_forecast_nrmse_median"],
                    marker="o", linestyle=style, color=colour,
                    label=f"{representation.upper()}–{head.upper()}",
                )
        axis.set_title(scenario)
        axis.set_xscale("log", base=2)
        axis.grid(alpha=0.2)
    axes[0, 0].legend(frameon=False, fontsize=8)
    for axis in axes[-1]:
        axis.set_xlabel("observations")
    for axis in axes[:, 0]:
        axis.set_ylabel("factor forecast NRMSE")
    figure.suptitle("Latent-amplitude forecast: VAR versus Kalman")
    figure.tight_layout()
    figure.savefig(output / "amplitude_forecast.png", dpi=180)
    plt.close(figure)

    figure, axes = plt.subplots(2, 3, figsize=(13, 7), sharex=True)
    for axis, scenario in zip(axes.flat, scenarios):
        frame = summary.loc[summary["scenario"] == scenario].sort_values("n")
        for head, colour in (("var", "#D55E00"), ("kf", "#009E73")):
            axis.plot(
                frame["n"], frame[f"rfd_{head}_signal_qlike_median"],
                marker="o", color=colour, label=head.upper(),
            )
        axis.set_title(scenario)
        axis.set_xscale("log", base=2)
        axis.set_yscale("log")
        axis.grid(alpha=0.2)
    axes[0, 0].legend(frameon=False, fontsize=8)
    for axis in axes[-1]:
        axis.set_xlabel("observations")
    for axis in axes[:, 0]:
        axis.set_ylabel("latent-signal QLIKE")
    figure.suptitle("RFD reconstruction stability")
    figure.tight_layout()
    figure.savefig(output / "rfd_stability.png", dpi=180)
    plt.close(figure)


def _summarize(raw: pd.DataFrame, output: Path) -> None:
    usable = raw.loc[raw["status"] == "ok"].copy()
    if usable.empty:
        return
    rows = []
    metric_columns = [column for column in RAW_COLUMNS if column not in IDENTITY_COLUMNS]
    for (scenario, n), group in usable.groupby(["scenario", "n"], sort=False):
        row: dict[str, Any] = {
            "scenario": scenario, "n": int(n), "completed": len(group),
        }
        for column in metric_columns:
            values = pd.to_numeric(group[column], errors="coerce")
            row[f"{column}_median"] = float(values.median())
            row[f"{column}_q25"] = float(values.quantile(0.25))
            row[f"{column}_q75"] = float(values.quantile(0.75))
        for representation in REPRESENTATIONS:
            left = pd.to_numeric(
                group[f"{representation}_kf_forecast_nrmse"], errors="coerce"
            )
            right = pd.to_numeric(
                group[f"{representation}_var_forecast_nrmse"], errors="coerce"
            )
            row[f"{representation}_kf_win_rate"] = float((left < right).mean())
        rows.append(row)
    summary = pd.DataFrame(rows)
    summary.to_csv(output / "summary.csv", index=False)
    _write_plots(summary, output)
    report = [
        "# BW latent-score filter gate", "",
        "Every draw uses one frozen training prefix and a sequential holdout.",
        "Known factors adjudicate amplitude recovery; guarded BW reconstructions",
        "adjudicate numerical stability separately.", "",
        f"- requested rows on disk: {len(raw)}",
        f"- successful rows: {len(usable)}",
        f"- recorded errors: {int((raw['status'] == 'error').sum())}",
        "- representations: oracle score channel, fixed-centre RFM-compatible, RFD",
        "- heads: frozen OLS VAR(1), frozen linear state-space/Kalman",
        "- true rank supplied to every representation",
        "- no holdout loss tunes either head", "",
        "The run is a causal score-head and decoder gate, not literal parent-code",
        "parity and not an APP-FIN result.", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")


def print_workload(config: dict[str, Any], tasks: list[BWTask], workers: int) -> None:
    print(f"profile: {config['profile_name']}")
    print(f"recorded: {config['profile']['recorded']}")
    print(f"n values: {config['profile']['n_values']}")
    print(f"scenarios: {config['profile']['scenarios']}")
    print(f"replicates: {config['profile']['replicates']}")
    print(f"requested tasks: {len(tasks)}")
    print(f"workers: {workers} (one BLAS thread each)")


def run(config: dict[str, Any], *, workers: int, max_tasks: int | None = None) -> None:
    output = (ROOT / str(config["profile"]["output_dir"])).resolve()
    _initialize(config, output)
    raw_path = output / "raw.csv"
    existing = _read_raw(raw_path)
    complete = {_row_key(row) for _, row in existing.iterrows()}
    tasks = [task for task in build_tasks(config) if _task_key(task) not in complete]
    if max_tasks is not None:
        tasks = tasks[:max_tasks]
    if workers == 1:
        for index, task in enumerate(tasks, start=1):
            print(f"[{index}/{len(tasks)}] {task.scenario}, n={task.n}, rep={task.replicate}", flush=True)
            _append_row(raw_path, run_task(config, task))
    elif tasks:
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(run_task, config, task): task for task in tasks}
            for index, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                task = futures[future]
                row = future.result()
                _append_row(raw_path, row)
                print(
                    f"[{index}/{len(tasks)} complete] {task.scenario}, n={task.n}, "
                    f"rep={task.replicate}, status={row['status']}", flush=True,
                )
    _summarize(_read_raw(raw_path), output)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument(
        "--profile", choices=("smoke", "calibration", "overnight"),
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
