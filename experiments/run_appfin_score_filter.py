"""Compare VAR and Kalman score heads on the frozen APP-FIN bridge.

At every expanding forecast origin the literal parent RFM representation and
the feasible RFD representation are each fitted once.  Their projected score
rows are then held fixed while two heads issue a one-month forecast:

* the parent's OLS VAR(1) with intercept; and
* an identity-observation linear Gaussian latent-score model fitted by EM.

Every score forecast is decoded through the same guarded BW exponential.  The
experiment therefore isolates score filtering and forecast stability; it does
not estimate rank, reveal latent financial factors, or tune on the test block.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
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

import run_appfin_forecast as bridge  # noqa: E402
from run_appfin_identification import (  # noqa: E402
    _atomic_json,
    _atomic_npz,
    _resolve_project_r_library,
    _sha256,
    _stage_diagnostics,
    check_r_environment,
    load_panel,
)
from rfd.estimators.centre import estimate_centre_path  # noqa: E402
from rfd.estimators.frame import (  # noqa: E402
    PolygonalFrame,
    regular_polygon_grid,
    transport_from_reference,
)
from rfd.estimators.lag import (  # noqa: E402
    assemble_lag_operator,
    common_reference_tangent_rows,
    coordinate_tangents,
    decompose_lag_operator,
    extract_dynamic_factors,
    lag_cross_covariances,
)
from rfd.forecast import (  # noqa: E402
    fit_score_state_space,
    forecast_score_state_space,
    forecast_var1,
)
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.spd.bw import bw_clip_exp_tangent  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "appfin_score_filter.yaml"
R_WORKER = ROOT / "experiments" / "parent_rfm_score_heads_worker.R"
PARENT_MAIN = ROOT / "reference" / "Riemannian_factor_model-main" / "main_func.R"
PARENT_BW = ROOT / "reference" / "Riemannian_factor_model-main" / "BWS_util.R"
METHOD_KEYS = ("parent_var", "parent_kf", "rfd_var", "rfd_kf")
METHOD_LABELS = {
    "parent_var": "Parent RFM–VAR",
    "parent_kf": "Parent RFM–KF",
    "rfd_var": "RFD–VAR",
    "rfd_kf": "RFD–KF",
}


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    source_path = (ROOT / config["experiment"]["source_config"]).resolve()
    config["source"] = bridge.load_configuration(source_path)
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    head = config["head"]
    if int(head["state_max_iterations"]) < 1:
        raise ValueError("state_max_iterations must be positive")
    if float(head["state_tolerance"]) <= 0.0:
        raise ValueError("state_tolerance must be positive")
    if float(head["covariance_floor"]) <= 0.0:
        raise ValueError("covariance_floor must be positive")
    if not 0.0 < float(head["maximum_transition_radius"]) < 1.0:
        raise ValueError("maximum_transition_radius must lie inside (0, 1)")
    if not 0.0 < float(head["bw_step_margin"]) < 1.0:
        raise ValueError("bw_step_margin must lie inside (0, 1)")
    source = config["source"]
    if int(source["experiment"]["rank"]) < 1:
        raise ValueError("source bridge rank must be positive")
    if str(source["rfd"]["future_centre_policy"]) != "carry_terminal":
        raise ValueError("score-head replay requires terminal-centre carry")


def _jsonable_config(config: dict[str, Any]) -> dict[str, Any]:
    return {
        "experiment": config["experiment"],
        "head": config["head"],
        "output": config["output"],
        "source": bridge._jsonable_config(config["source"]),
        "config_path": str(config["config_path"]),
    }


def experiment_digest(config: dict[str, Any], forecast_months: int) -> str:
    paths = [
        Path(config["config_path"]),
        Path(config["source"]["config_path"]),
        ROOT / config["source"]["experiment"]["panel_path"],
        Path(__file__), R_WORKER, PARENT_MAIN, PARENT_BW,
        ROOT / "py" / "rfd" / "forecast.py",
        ROOT / "py" / "rfd" / "estimators" / "centre.py",
        ROOT / "py" / "rfd" / "estimators" / "frame.py",
        ROOT / "py" / "rfd" / "estimators" / "lag.py",
        ROOT / "py" / "rfd" / "spd" / "bw.py",
    ]
    material = json.dumps(
        {"forecast_months": forecast_months, "config": _jsonable_config(config)},
        sort_keys=True, separators=(",", ":"),
    )
    material += "\n" + "\n".join(
        f"{path.resolve()}:{_sha256(path)}" for path in paths
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def build_design(
    config: dict[str, Any],
    panel: dict[str, np.ndarray],
    forecast_months: int,
) -> dict[str, Any]:
    source = config["source"]
    initial = int(source["experiment"]["initial_train_months"])
    return {
        "experiment_id": config["experiment"]["id"],
        "source_experiment": source["experiment"]["id"],
        "panel": str((ROOT / source["experiment"]["panel_path"]).resolve()),
        "initial_train_months": initial,
        "forecast_months": forecast_months,
        "first_target_month": str(panel["months"][initial]),
        "last_target_month": str(panel["months"][initial + forecast_months - 1]),
        "rank": int(source["experiment"]["rank"]),
        "max_lag": int(source["experiment"]["max_lag"]),
        "methods": list(METHOD_LABELS.values()),
        "causality": "each origin fits on its expanding prefix only",
        "rank_policy": "parent rank two supplied to all four arms",
        "scope": "score-head and BW decoder stability; no latent-score truth",
    }


def _state_fit(scores: np.ndarray, config: dict[str, Any]):
    head = config["head"]
    return fit_score_state_space(
        scores,
        max_iter=int(head["state_max_iterations"]),
        tolerance=float(head["state_tolerance"]),
        covariance_floor=float(head["covariance_floor"]),
        maximum_radius=float(head["maximum_transition_radius"]),
    )


def _head_diagnostics(var_fit, state_fit) -> dict[str, Any]:
    var_radius = float(np.max(np.abs(np.linalg.eigvals(var_fit.coefficients[1:].T))))
    state_radius = float(np.max(np.abs(np.linalg.eigvals(state_fit.transition))))
    process = float(np.trace(state_fit.process_covariance))
    measurement = float(np.trace(state_fit.measurement_covariance))
    return {
        "var_transition_radius": var_radius,
        "kf_transition_radius": state_radius,
        "kf_measurement_fraction": measurement / (measurement + process),
        "kf_converged": bool(state_fit.converged),
        "kf_iterations": int(state_fit.n_iter),
        "kf_log_likelihood": float(state_fit.log_likelihood),
    }


def _decode(
    centre: np.ndarray,
    tangent: np.ndarray,
    step_margin: float,
) -> tuple[np.ndarray, dict[str, float]]:
    clipped = bw_clip_exp_tangent(
        centre[None, :, :], tangent[None, :, :], step_margin=step_margin
    )
    forecast = BW_GEOMETRY.exp(
        centre[None, :, :], clipped.tangent
    )[0]
    eigenvalues = np.linalg.eigvalsh(forecast)
    return forecast, {
        "clip_factor": float(clipped.factors[0]),
        "raw_step_min_eigenvalue": float(clipped.raw_step_min_eigenvalues[0]),
        "forecast_min_eigenvalue": float(eigenvalues[0]),
        "forecast_condition_number": float(eigenvalues[-1] / eigenvalues[0]),
    }


def _read_matrix(path: Path, shape: tuple[int, ...]) -> np.ndarray:
    value = np.loadtxt(path, delimiter=",", ndmin=2)
    if value.size != int(np.prod(shape)) or not np.isfinite(value).all():
        raise ValueError(f"invalid parent representation file: {path}")
    return value.reshape(shape)


def run_parent_stage(
    observations: np.ndarray,
    config: dict[str, Any],
    forecast_months: int,
    rscript: Path,
    output: Path,
    digest: str,
    *,
    force: bool,
) -> Path:
    source = config["source"]
    initial = int(source["experiment"]["initial_train_months"])
    n = initial + forecast_months
    stage = output / "parent_representations"
    meta = stage / "metadata.json"
    partial = stage / "partial.json"
    if not force and bridge._cache_matches(meta, digest):
        print("[parent] reusing digest-matched score representations", flush=True)
        return stage
    stage.mkdir(parents=True, exist_ok=True)
    resume = not force and bridge._cache_matches(partial, digest)
    _atomic_json(partial, {"digest": digest, "forecast_months": forecast_months})
    with tempfile.TemporaryDirectory(prefix="rfd_appfin_score_parent_") as temporary:
        input_path = Path(temporary) / "panel.csv"
        np.savetxt(
            input_path, observations[:n].reshape(n, -1),
            delimiter=",", fmt="%.17g",
        )
        command = [
            str(rscript), "--vanilla", str(R_WORKER), str(input_path), str(stage),
            str(n), str(observations.shape[1]),
            str(int(source["experiment"]["rank"])),
            str(int(source["experiment"]["max_lag"])), str(forecast_months),
            str(int(source["parent"]["seed"])),
            str(int(source["parent"]["batch_size"])),
            str(int(source["parent"]["max_iterations"])),
            "TRUE" if resume else "FALSE",
        ]
        env = os.environ.copy()
        library = _resolve_project_r_library()
        if library is not None:
            env["R_LIBS_USER"] = str(library)
        env["RENV_CONFIG_AUTOLOADER_ENABLED"] = "FALSE"
        completed = subprocess.run(
            command, cwd=ROOT, env=env, capture_output=True, text=True,
            check=False,
        )
    if completed.returncode:
        raise RuntimeError(
            "parent score worker failed: "
            + (completed.stderr or completed.stdout).strip()
        )
    expected = [
        stage / f"target_{target:03d}" / "status.txt"
        for target in range(initial, initial + forecast_months)
    ]
    if not all(path.is_file() and path.read_text(encoding="utf-8").startswith("ok") for path in expected):
        raise RuntimeError("parent score worker did not complete every origin")
    _atomic_json(meta, {"digest": digest, "forecast_months": forecast_months})
    if completed.stdout.strip():
        print(completed.stdout.strip(), flush=True)
    return stage


def parent_origin(
    directory: Path,
    rank: int,
    matrix_size: int,
    config: dict[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    scores = np.loadtxt(directory / "scores.csv", delimiter=",", ndmin=2)
    loadings = _read_matrix(
        directory / "loadings.csv", (rank, matrix_size, matrix_size)
    )
    row_mean = _read_matrix(directory / "row_mean_tangent.csv", (matrix_size, matrix_size))
    centre = _read_matrix(directory / "mean.csv", (matrix_size, matrix_size))
    r_var_score = _read_matrix(directory / "var_score.csv", (rank,))
    r_var_forecast = _read_matrix(directory / "var_forecast.csv", (matrix_size, matrix_size))
    var_score, var_fit = forecast_var1(scores)
    state_fit = _state_fit(scores, config)
    kf_score, _ = forecast_score_state_space(scores, state_fit)
    margin = float(config["head"]["bw_step_margin"])
    results: dict[str, np.ndarray] = {}
    diagnostics = _head_diagnostics(var_fit, state_fit)
    diagnostics["var_score_r_parity_error"] = float(np.linalg.norm(var_score - r_var_score))
    for name, score in (("var", var_score), ("kf", kf_score)):
        tangent = row_mean + np.tensordot(score, loadings, axes=([-1], [0]))
        forecast, health = _decode(centre, tangent, margin)
        results[name] = forecast
        diagnostics.update({f"{name}_{key}": value for key, value in health.items()})
    diagnostics["var_forecast_r_parity_error"] = float(
        np.linalg.norm(BW_GEOMETRY.exp(centre, row_mean + np.tensordot(
            var_score, loadings, axes=([-1], [0])
        )) - r_var_forecast)
    )
    return results, diagnostics


def rfd_origin(
    training: np.ndarray,
    config: dict[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, Any], dict[str, np.ndarray]]:
    source_config = config["source"]
    source = source_config["rfd"]
    n = training.shape[0]
    settings = bridge.effective_rfd_settings(source_config, n)
    time_values = np.arange(1, n + 1, dtype=float) / n
    vertex_times = regular_polygon_grid(
        settings["n_cells"], start=float(time_values[0]), stop=float(time_values[-1])
    )
    centre = estimate_centre_path(
        observations=training, time=time_values, vertex_times=vertex_times,
        bandwidth=settings["bandwidth"], geometry=BW_GEOMETRY,
        overlap_fractions=tuple(source["overlap_fractions"]),
        mean_tol=float(source["mean_tolerance"]),
        max_iter=int(source["mean_max_iterations"]),
    )
    tangent_rows = common_reference_tangent_rows(training, time_values, centre.polygon)
    lag_row = lag_cross_covariances(
        tangent_rows, int(source_config["experiment"]["max_lag"]),
        demean=True, tail_mode=str(source["tail_mode"]),
        normalization=str(source["normalization"]),
    )
    spectrum = decompose_lag_operator(assemble_lag_operator(lag_row))
    factors = extract_dynamic_factors(
        spectrum, int(source_config["experiment"]["rank"])
    )
    scores = factors.factor_scores
    var_score, var_fit = forecast_var1(scores)
    state_fit = _state_fit(scores, config)
    kf_score, _ = forecast_score_state_space(scores, state_fit)
    frame = PolygonalFrame(centre.vertex_times, centre.vertices, BW_GEOMETRY)
    target_time = np.array([time_values[-1]])
    terminal = centre.vertices[-1]
    margin = float(config["head"]["bw_step_margin"])
    results: dict[str, np.ndarray] = {}
    diagnostics = _stage_diagnostics(centre)
    diagnostics.update(settings)
    diagnostics.update(_head_diagnostics(var_fit, state_fit))
    for name, score in (("var", var_score), ("kf", kf_score)):
        row = factors.row_mean + factors.loadings @ score
        reference = coordinate_tangents(row[None, :], tangent_rows.basis)
        local = transport_from_reference(frame, reference, target_time)[0]
        forecast, health = _decode(terminal, local, margin)
        results[name] = forecast
        diagnostics.update({f"{name}_{key}": value for key, value in health.items()})
    arrays = {
        "var": results["var"], "kf": results["kf"], "scores": scores,
        "var_score": var_score, "kf_score": kf_score,
        "lag_eigenvalues": spectrum.eigenvalues,
    }
    return results, diagnostics, arrays


def _atomic_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    frame.to_csv(temporary, index=False)
    os.replace(temporary, path)


def _run_rfd_origins(
    observations: np.ndarray,
    config: dict[str, Any],
    forecast_months: int,
    output: Path,
    digest: str,
    *,
    force: bool,
) -> tuple[dict[str, np.ndarray], list[dict[str, Any]]]:
    source = config["source"]
    initial = int(source["experiment"]["initial_train_months"])
    directory = output / "rfd_origins"
    directory.mkdir(parents=True, exist_ok=True)
    forecasts = {"var": [], "kf": []}
    diagnostics: list[dict[str, Any]] = []
    for offset, (train_stop, target) in enumerate(
        bridge.expanding_origins(initial, forecast_months), start=1
    ):
        cache = directory / f"target_{target:03d}.npz"
        meta = directory / f"target_{target:03d}.json"
        origin_digest = hashlib.sha256(f"{digest}:target={target}".encode()).hexdigest()
        if force or not cache.is_file() or not bridge._cache_matches(meta, origin_digest):
            started = time.perf_counter()
            result, health, arrays = rfd_origin(observations[:train_stop], config)
            health.update({
                "target_index": target,
                "n_train": train_stop,
                "elapsed_seconds": time.perf_counter() - started,
            })
            _atomic_npz(cache, **arrays)
            _atomic_json(meta, {"digest": origin_digest, "diagnostics": health})
        else:
            with np.load(cache, allow_pickle=False) as stored:
                result = {"var": stored["var"].copy(), "kf": stored["kf"].copy()}
            health = json.loads(meta.read_text(encoding="utf-8"))["diagnostics"]
        for head in ("var", "kf"):
            forecasts[head].append(result[head])
        diagnostics.append(health)
        print(
            f"[RFD {offset:02d}/{forecast_months:02d}] train={train_stop}, "
            f"VAR clip={float(health['var_clip_factor']):.3f}, "
            f"KF clip={float(health['kf_clip_factor']):.3f}", flush=True,
        )
    return {key: np.stack(value) for key, value in forecasts.items()}, diagnostics


def _run_parent_origins(
    stage: Path,
    config: dict[str, Any],
    forecast_months: int,
) -> tuple[dict[str, np.ndarray], list[dict[str, Any]]]:
    source = config["source"]
    initial = int(source["experiment"]["initial_train_months"])
    rank = int(source["experiment"]["rank"])
    matrix_size = len(source["experiment"]["expected_tickers"])
    forecasts = {"var": [], "kf": []}
    diagnostics = []
    for target in range(initial, initial + forecast_months):
        result, health = parent_origin(
            stage / f"target_{target:03d}", rank, matrix_size, config
        )
        for head in ("var", "kf"):
            forecasts[head].append(result[head])
        health["target_index"] = target
        diagnostics.append(health)
    return {key: np.stack(value) for key, value in forecasts.items()}, diagnostics


def _plot(long: pd.DataFrame, diagnostics: pd.DataFrame, output: Path) -> None:
    methods = list(dict.fromkeys(long["method"]))
    colours = plt.colormaps["viridis"](np.linspace(0.08, 0.92, len(methods)))
    figure, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
    for method, colour in zip(methods, colours):
        frame = long.loc[long["method"] == method].reset_index(drop=True)
        x = np.arange(1, len(frame) + 1)
        axes[0].plot(x, frame["frobenius"].expanding().mean(), label=method, color=colour)
        axes[1].plot(x, frame["qlike"].expanding().mean(), label=method, color=colour)
    axes[0].set(title="Cumulative Frobenius error", xlabel="forecast month", ylabel="mean error")
    axes[1].set(title="Cumulative QLIKE", xlabel="forecast month", ylabel="mean loss")
    axes[0].legend(frameon=False, fontsize=8)
    for axis in axes:
        axis.grid(alpha=0.2)
    figure.savefig(output / "forecast_loss_paths.png", dpi=180)
    plt.close(figure)

    rfd = diagnostics.loc[diagnostics["representation"] == "RFD"].reset_index(drop=True)
    figure, axes = plt.subplots(1, 2, figsize=(12, 4.2), constrained_layout=True)
    x = np.arange(1, len(rfd) + 1)
    axes[0].plot(x, rfd["var_forecast_min_eigenvalue"], label="VAR", color=colours[2])
    axes[0].plot(x, rfd["kf_forecast_min_eigenvalue"], label="KF", color=colours[3])
    axes[0].set_yscale("log")
    axes[0].set(title="RFD forecast SPD margin", xlabel="forecast month", ylabel="minimum eigenvalue")
    axes[1].plot(x, rfd["var_forecast_condition_number"], label="VAR", color=colours[2])
    axes[1].plot(x, rfd["kf_forecast_condition_number"], label="KF", color=colours[3])
    axes[1].set_yscale("log")
    axes[1].set(title="RFD forecast conditioning", xlabel="forecast month", ylabel="condition number")
    axes[0].legend(frameon=False)
    for axis in axes:
        axis.grid(alpha=0.2)
    figure.savefig(output / "rfd_decoder_stability.png", dpi=180)
    plt.close(figure)


def _write_report(
    output: Path,
    design: dict[str, Any],
    summary: pd.DataFrame,
    diagnostics: pd.DataFrame,
) -> None:
    lines = [
        "# APP-FIN score-head adjudication", "",
        "The geometric representation is fixed within each pair. Only the score",
        "forecast head changes from direct OLS VAR(1) to a fitted latent-state",
        "Kalman filter. Every target is forecast before it is observed.", "",
        "| method | mean Frobenius² | mean QLIKE | mean BW² | min eigenvalue | max condition |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary.itertuples(index=False):
        lines.append(
            f"| {row.method} | {row.mean_frobenius2:.6g} | {row.mean_qlike:.6g} | "
            f"{row.mean_bw2:.6g} | {row.minimum_forecast_eigenvalue:.6g} | "
            f"{row.maximum_forecast_condition_number:.6g} |"
        )
    parent = diagnostics.loc[diagnostics["representation"] == "Parent RFM"]
    rfd = diagnostics.loc[diagnostics["representation"] == "RFD"]
    lines.extend([
        "", "## Integrity and numerical health", "",
        f"- parent VAR score parity max error: {parent['var_score_r_parity_error'].max():.3g}",
        f"- parent VAR forecast parity max error: {parent['var_forecast_r_parity_error'].max():.3g}",
        f"- RFD VAR clips: {int((rfd['var_clip_factor'] < 1.0).sum())}/{len(rfd)}",
        f"- RFD KF clips: {int((rfd['kf_clip_factor'] < 1.0).sum())}/{len(rfd)}",
        f"- RFD KF convergence: {int(rfd['kf_converged'].sum())}/{len(rfd)} origins",
        "", "## Scope", "",
        "APP-FIN has no known latent factor amplitudes, so this run adjudicates",
        "one-step forecast loss and BW decoder stability—not structural score",
        "recovery. Rank two, the head controls, and all 36 origins were frozen",
        "before the evaluation outcomes were scored.", "",
        "See loss_by_month.csv, summary.csv, head_diagnostics.csv, forecasts.npz,",
        "forecast_loss_paths.png, and rfd_decoder_stability.png.",
    ])
    temporary = output / "report.md.tmp"
    temporary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    os.replace(temporary, output / "report.md")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check-r", action="store_true")
    parser.add_argument("--smoke-months", type=int, default=0)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config = load_configuration(args.config.resolve())
    source = config["source"]
    panel = load_panel(source)
    full_count = int(source["experiment"]["forecast_months"])
    forecast_months = full_count if args.smoke_months == 0 else args.smoke_months
    if not 1 <= forecast_months <= full_count:
        raise ValueError("smoke-months must lie between 1 and forecast_months")
    design = build_design(config, panel, forecast_months)
    print(json.dumps(design, indent=2), flush=True)

    rscript_string = shutil.which("Rscript")
    if rscript_string is None:
        raise FileNotFoundError("Rscript is not on PATH")
    rscript = Path(rscript_string)
    if args.check_r or not args.dry_run:
        check_r_environment(rscript)
    if args.dry_run:
        print("APP-FIN score-filter dry run passed; no estimators were fitted.", flush=True)
        return

    output_key = "smoke_directory" if args.smoke_months else "directory"
    output = (ROOT / config["output"][output_key]).resolve()
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config, forecast_months)
    design["digest"] = digest
    _atomic_json(output / "design.json", design)

    parent_digest = hashlib.sha256(f"{digest}:parent".encode()).hexdigest()
    parent_stage = run_parent_stage(
        panel["panel"], config, forecast_months, rscript, output,
        parent_digest, force=args.force,
    )
    parent, parent_health = _run_parent_origins(parent_stage, config, forecast_months)
    rfd_digest = hashlib.sha256(f"{digest}:rfd".encode()).hexdigest()
    rfd, rfd_health = _run_rfd_origins(
        panel["panel"], config, forecast_months, output, rfd_digest,
        force=args.force,
    )

    initial = int(source["experiment"]["initial_train_months"])
    truth = panel["panel"][initial : initial + forecast_months]
    lagged = panel["panel"][initial - 1 : initial + forecast_months - 1]
    months = panel["months"][initial : initial + forecast_months]
    keyed = {
        "parent_var": parent["var"], "parent_kf": parent["kf"],
        "rfd_var": rfd["var"], "rfd_kf": rfd["kf"],
    }
    methods = {METHOD_LABELS[key]: keyed[key] for key in METHOD_KEYS}
    long, summary = bridge.score_forecasts(methods, truth, lagged, months)
    diagnostics = pd.concat([
        pd.DataFrame(parent_health).assign(representation="Parent RFM"),
        pd.DataFrame(rfd_health).assign(representation="RFD"),
    ], ignore_index=True, sort=False)
    _atomic_csv(output / "loss_by_month.csv", long)
    _atomic_csv(output / "summary.csv", summary)
    _atomic_csv(output / "head_diagnostics.csv", diagnostics)
    _atomic_npz(
        output / "forecasts.npz", truth=truth, months=months,
        **keyed,
    )
    _plot(long, diagnostics, output)
    _write_report(output, design, summary, diagnostics)
    print(f"APP-FIN score-head report: {output / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
