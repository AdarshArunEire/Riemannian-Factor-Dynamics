"""Run APP-MONTHLY-VAR on the frozen 240-month APP-FIN panel.

The cloned parent RFM and RFD both use fixed rank two, lags 1:6, and the same
OLS VAR(1) score forecast. The parent retains its published fixed global centre.
RFD is refitted on each expanding prefix and carries its terminal causal centre
one month ahead. No forecast uses its target month.
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
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

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_appfin_identification import (  # noqa: E402
    _atomic_json,
    _atomic_npz,
    _resolve_project_r_library,
    _sha256,
    _stage_diagnostics,
    check_r_environment,
    load_panel,
)
from run_end_to_end import production_multiplier  # noqa: E402
from rfd.estimators.centre import estimate_centre_path  # noqa: E402
from rfd.estimators.frame import (  # noqa: E402
    PolygonalFrame,
    polygon_cell_count,
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
from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402
from rfd.forecast import forecast_var1  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.spd.bw import bw_clip_exp_tangent  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "appfin_forecast.yaml"
R_WORKER = ROOT / "experiments" / "parent_rfm_forecast_worker.R"
PARENT_SOURCE = (
    ROOT / "reference" / "Riemannian_factor_model-main" / "BWS_util.R"
)
PARENT_MAIN = (
    ROOT / "reference" / "Riemannian_factor_model-main" / "main_func.R"
)


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    rfd = config["rfd"]
    parent = config["parent"]
    expected = int(experiment["expected_months"])
    initial = int(experiment["initial_train_months"])
    forecasts = int(experiment["forecast_months"])
    rank = int(experiment["rank"])
    lag = int(experiment["max_lag"])
    if expected != initial + forecasts:
        raise ValueError("initial_train_months + forecast_months must equal expected_months")
    if initial < 24 or forecasts < 1:
        raise ValueError("forecast design requires a substantial training set and a test block")
    if not 1 <= rank < 78:
        raise ValueError("fixed rank must lie inside the APP-FIN tangent dimension")
    if not 1 <= lag < initial:
        raise ValueError("max_lag must lie inside the initial training sample")
    if str(rfd["future_centre_policy"]) != "carry_terminal":
        raise ValueError("the first bridge fixes future_centre_policy=carry_terminal")
    overlap = tuple(float(value) for value in rfd["overlap_fractions"])
    if len(overlap) != 2 or not 0 < overlap[0] < overlap[1] < 1:
        raise ValueError("overlap fractions must be increasing and interior")
    positive = (
        float(rfd["bandwidth_constant"]),
        float(rfd["production_multiplier_cap"]),
        float(rfd["mean_tolerance"]),
        int(rfd["mean_max_iterations"]),
        float(rfd["forecast_step_margin"]),
        int(parent["batch_size"]),
        int(parent["max_iterations"]),
        float(config["baselines"]["ewma_lambda"]),
    )
    if min(positive) <= 0:
        raise ValueError("numerical controls must be positive")
    if float(rfd["forecast_step_margin"]) >= 1:
        raise ValueError("forecast_step_margin must lie in (0, 1)")
    if float(config["baselines"]["ewma_lambda"]) >= 1:
        raise ValueError("EWMA lambda must lie in (0, 1)")


def expanding_origins(
    initial_train_months: int,
    forecast_months: int,
) -> list[tuple[int, int]]:
    """Return (exclusive train stop, target index) without future leakage."""
    if initial_train_months < 3 or forecast_months < 1:
        raise ValueError("invalid expanding forecast dimensions")
    return [
        (initial_train_months + offset, initial_train_months + offset)
        for offset in range(forecast_months)
    ]


def effective_rfd_settings(config: dict[str, Any], n: int) -> dict[str, Any]:
    source = config["rfd"]
    multiplier = production_multiplier(
        n,
        {
            "bandwidth_constant": float(source["bandwidth_constant"]),
            "bandwidth_exponent": float(source["bandwidth_exponent"]),
            "production_multiplier_cap": float(source["production_multiplier_cap"]),
            "admissible_boundary_fraction": float(source["admissible_boundary_fraction"]),
            "overlap_fractions": tuple(source["overlap_fractions"]),
        },
    )
    bandwidth = (
        float(source["bandwidth_constant"])
        * n ** (-float(source["bandwidth_exponent"]))
        * multiplier
    )
    centre_rate = n ** (-float(source["polygon_rate_exponent"]))
    n_cells = polygon_cell_count(
        centre_rate,
        constant=float(source["polygon_cell_constant"]),
    )
    return {
        "bandwidth_multiplier": float(multiplier),
        "bandwidth": float(bandwidth),
        "n_cells": int(n_cells),
        "vertex_count": int(n_cells + 1),
    }


def build_design(
    config: dict[str, Any],
    panel: dict[str, np.ndarray],
    forecast_months: int,
) -> dict[str, Any]:
    experiment = config["experiment"]
    initial = int(experiment["initial_train_months"])
    last_target = initial + forecast_months - 1
    return {
        "experiment_id": experiment["id"],
        "panel": str((ROOT / experiment["panel_path"]).resolve()),
        "n_months": int(panel["panel"].shape[0]),
        "matrix_size": int(panel["panel"].shape[1]),
        "initial_train_months": initial,
        "forecast_months": int(forecast_months),
        "first_target_month": str(panel["months"][initial]),
        "last_target_month": str(panel["months"][last_target]),
        "rank": int(experiment["rank"]),
        "max_lag": int(experiment["max_lag"]),
        "score_model": "OLS VAR(1) with intercept, refitted at every origin",
        "parent_centre_policy": "initial global BW centre held fixed",
        "rfd_centre_policy": "expanding-prefix path; one-sided terminal centre carried one month",
        "primary_losses": ["squared_frobenius", "multivariate_qlike"],
        "scope": "causal implementation bridge; no rank, latent-score, or dominance claim",
    }


def experiment_digest(config: dict[str, Any], forecast_months: int) -> str:
    paths = [
        Path(config["config_path"]),
        ROOT / config["experiment"]["panel_path"],
        Path(__file__),
        R_WORKER,
        PARENT_MAIN,
        PARENT_SOURCE,
        ROOT / "py" / "rfd" / "forecast.py",
        ROOT / "py" / "rfd" / "estimators" / "centre.py",
        ROOT / "py" / "rfd" / "estimators" / "frame.py",
        ROOT / "py" / "rfd" / "estimators" / "lag.py",
    ]
    material = json.dumps(
        {"forecast_months": forecast_months, "config": _jsonable_config(config)},
        sort_keys=True,
        separators=(",", ":"),
    )
    material += "\n" + "\n".join(
        f"{path.resolve()}:{_sha256(path)}" for path in paths
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _component_digest(payload: Any, paths: list[Path]) -> str:
    material = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    material += "\n" + "\n".join(
        f"{path.resolve()}:{_sha256(path)}" for path in paths
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def parent_stage_digest(config: dict[str, Any], forecast_months: int) -> str:
    experiment = config["experiment"]
    return _component_digest(
        {
            "panel_path": experiment["panel_path"],
            "initial_train_months": experiment["initial_train_months"],
            "forecast_months": forecast_months,
            "rank": experiment["rank"],
            "max_lag": experiment["max_lag"],
            "parent": config["parent"],
            "orchestrator": inspect.getsource(run_parent_forecasts),
        },
        [
            ROOT / experiment["panel_path"],
            R_WORKER,
            PARENT_MAIN,
            PARENT_SOURCE,
        ],
    )


def rfd_stage_digest(config: dict[str, Any], forecast_months: int) -> str:
    experiment = config["experiment"]
    return _component_digest(
        {
            "panel_path": experiment["panel_path"],
            "initial_train_months": experiment["initial_train_months"],
            "forecast_months": forecast_months,
            "rank": experiment["rank"],
            "max_lag": experiment["max_lag"],
            "rfd": config["rfd"],
            "orchestrator": (
                inspect.getsource(run_rfd_origin)
                + inspect.getsource(run_rfd_forecasts)
            ),
        },
        [
            ROOT / experiment["panel_path"],
            ROOT / "py" / "rfd" / "forecast.py",
            ROOT / "py" / "rfd" / "estimators" / "centre.py",
            ROOT / "py" / "rfd" / "estimators" / "frame.py",
            ROOT / "py" / "rfd" / "estimators" / "lag.py",
            ROOT / "py" / "rfd" / "spd" / "bw.py",
        ],
    )


def _jsonable_config(config: dict[str, Any]) -> dict[str, Any]:
    value = dict(config)
    value["config_path"] = str(value["config_path"])
    return value


def run_parent_forecasts(
    observations: np.ndarray,
    config: dict[str, Any],
    forecast_months: int,
    rscript: Path,
) -> np.ndarray:
    initial = int(config["experiment"]["initial_train_months"])
    n = initial + forecast_months
    m = observations.shape[1]
    source = observations[:n]
    with tempfile.TemporaryDirectory(prefix="rfd_appfin_forecast_parent_") as temporary:
        directory = Path(temporary)
        input_path = directory / "panel.csv"
        output_path = directory / "forecasts.csv"
        np.savetxt(input_path, source.reshape(n, -1), delimiter=",", fmt="%.17g")
        command = [
            str(rscript), "--vanilla", str(R_WORKER), str(input_path),
            str(output_path), str(n), str(m),
            str(int(config["experiment"]["rank"])),
            str(int(config["experiment"]["max_lag"])),
            str(forecast_months), str(int(config["parent"]["seed"])),
            str(int(config["parent"]["batch_size"])),
            str(int(config["parent"]["max_iterations"])),
            str(PARENT_SOURCE),
        ]
        env = os.environ.copy()
        library = _resolve_project_r_library()
        if library is not None:
            env["R_LIBS_USER"] = str(library)
        env["RENV_CONFIG_AUTOLOADER_ENABLED"] = "FALSE"
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode:
            status = output_path.with_suffix(output_path.suffix + ".status")
            detail = status.read_text(encoding="utf-8") if status.is_file() else ""
            raise RuntimeError(
                "parent forecast worker failed: "
                + (detail or completed.stderr or completed.stdout).strip()
            )
        flat = np.loadtxt(output_path, delimiter=",", ndmin=2)
    expected = (forecast_months, m * m)
    if flat.shape != expected or not np.isfinite(flat).all():
        raise ValueError(f"parent forecast output has shape {flat.shape}; expected {expected}")
    return flat.reshape(forecast_months, m, m)


def run_rfd_origin(
    training_observations: np.ndarray,
    config: dict[str, Any],
) -> tuple[np.ndarray, dict[str, Any], dict[str, np.ndarray]]:
    """Fit one causal RFD prefix and issue its next-month covariance forecast."""
    n = training_observations.shape[0]
    source = config["rfd"]
    settings = effective_rfd_settings(config, n)
    time_values = np.arange(1, n + 1, dtype=float) / n
    vertex_times = regular_polygon_grid(
        settings["n_cells"],
        start=float(time_values[0]),
        stop=float(time_values[-1]),
    )
    centre = estimate_centre_path(
        observations=training_observations,
        time=time_values,
        vertex_times=vertex_times,
        bandwidth=settings["bandwidth"],
        geometry=BW_GEOMETRY,
        overlap_fractions=tuple(source["overlap_fractions"]),
        mean_tol=float(source["mean_tolerance"]),
        max_iter=int(source["mean_max_iterations"]),
    )
    tangent_rows = common_reference_tangent_rows(
        training_observations,
        time_values,
        centre.polygon,
    )
    lag_row = lag_cross_covariances(
        tangent_rows,
        int(config["experiment"]["max_lag"]),
        demean=True,
        tail_mode=str(source["tail_mode"]),
        normalization=str(source["normalization"]),
    )
    spectrum = decompose_lag_operator(assemble_lag_operator(lag_row))
    factors = extract_dynamic_factors(
        spectrum,
        int(config["experiment"]["rank"]),
    )
    forecast_score, var_fit = forecast_var1(factors.factor_scores)
    forecast_row = factors.row_mean + factors.loadings @ forecast_score
    reference_vector = coordinate_tangents(
        forecast_row[None, :],
        tangent_rows.basis,
    )
    frame = PolygonalFrame(centre.vertex_times, centre.vertices, BW_GEOMETRY)
    local_vector = transport_from_reference(
        frame,
        reference_vector,
        np.array([time_values[-1]]),
    )
    target_centre = centre.vertices[-1][None, :, :]
    clipped = bw_clip_exp_tangent(
        target_centre,
        local_vector,
        step_margin=float(source["forecast_step_margin"]),
    )
    forecast = BW_GEOMETRY.exp(target_centre, clipped.tangent)[0]
    diagnostics = _stage_diagnostics(centre)
    diagnostics.update(settings)
    diagnostics.update({
        "n_train": int(n),
        "forecast_clip_factor": float(clipped.factors[0]),
        "forecast_raw_step_min_eigenvalue": float(
            clipped.raw_step_min_eigenvalues[0]
        ),
        "forecast_min_eigenvalue": float(np.linalg.eigvalsh(forecast)[0]),
        "var_residual_rms": float(np.sqrt(np.mean(var_fit.residuals**2))),
        "lag_eigenvalue_rank": float(
            spectrum.eigenvalues[int(config["experiment"]["rank"]) - 1]
        ),
        "lag_eigengap": float(
            spectrum.eigenvalues[int(config["experiment"]["rank"]) - 1]
            - spectrum.eigenvalues[int(config["experiment"]["rank"])]
        ),
    })
    arrays = {
        "forecast": forecast,
        "terminal_centre": centre.vertices[-1],
        "forecast_score": forecast_score,
        "var_coefficients": var_fit.coefficients,
        "lag_eigenvalues": spectrum.eigenvalues,
    }
    return forecast, diagnostics, arrays


def _cache_matches(path: Path, digest: str) -> bool:
    if not path.is_file():
        return False
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("digest") == digest
    except (OSError, json.JSONDecodeError):
        return False


def run_rfd_forecasts(
    observations: np.ndarray,
    config: dict[str, Any],
    forecast_months: int,
    output: Path,
    digest: str,
    *,
    force: bool,
) -> tuple[np.ndarray, list[dict[str, Any]]]:
    initial = int(config["experiment"]["initial_train_months"])
    m = observations.shape[1]
    forecasts = []
    diagnostics = []
    origin_dir = output / "rfd_origins"
    origin_dir.mkdir(parents=True, exist_ok=True)
    for offset, (train_stop, target_index) in enumerate(
        expanding_origins(initial, forecast_months),
        start=1,
    ):
        cache = origin_dir / f"target_{target_index:03d}.npz"
        meta = origin_dir / f"target_{target_index:03d}.json"
        origin_digest = hashlib.sha256(
            f"{digest}:target={target_index}".encode("utf-8")
        ).hexdigest()
        if force or not cache.is_file() or not _cache_matches(meta, origin_digest):
            started = time.perf_counter()
            forecast, health, arrays = run_rfd_origin(
                observations[:train_stop],
                config,
            )
            health["elapsed_seconds"] = time.perf_counter() - started
            health["target_index"] = int(target_index)
            _atomic_npz(cache, **arrays)
            _atomic_json(meta, {"digest": origin_digest, "diagnostics": health})
        else:
            with np.load(cache, allow_pickle=False) as source:
                forecast = source["forecast"].copy()
            health = json.loads(meta.read_text(encoding="utf-8"))["diagnostics"]
        if forecast.shape != (m, m) or not np.isfinite(forecast).all():
            raise ValueError("cached RFD forecast violates its matrix contract")
        forecasts.append(forecast)
        diagnostics.append(health)
        print(
            f"[RFD {offset:02d}/{forecast_months:02d}] "
            f"train={train_stop}, target={target_index}, "
            f"clip={float(health['forecast_clip_factor']):.3f}",
            flush=True,
        )
    return np.stack(forecasts), diagnostics


def baseline_forecasts(
    observations: np.ndarray,
    initial_train_months: int,
    forecast_months: int,
    ewma_lambda: float,
) -> dict[str, np.ndarray]:
    targets = range(initial_train_months, initial_train_months + forecast_months)
    locf = np.stack([observations[index - 1] for index in targets])
    ewma = np.zeros_like(observations)
    state = np.zeros_like(observations[0])
    for index in range(1, observations.shape[0]):
        state = ewma_lambda * state + (1.0 - ewma_lambda) * observations[index - 1]
        ewma[index] = state
    return {
        "LOCF": locf,
        "EWMA": ewma[initial_train_months : initial_train_months + forecast_months],
    }


def _risk_error(forecast: np.ndarray, truth: np.ndarray, lagged: np.ndarray) -> float:
    ones = np.ones(lagged.shape[0])
    weights = np.linalg.solve(lagged, ones)
    weights /= np.sum(weights)
    predicted = float(weights @ forecast @ weights)
    realised = float(weights @ truth @ weights)
    return abs(predicted - realised)


def score_forecasts(
    methods: dict[str, np.ndarray],
    truth: np.ndarray,
    lagged: np.ndarray,
    months: np.ndarray,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    for method, forecasts in methods.items():
        if forecasts.shape != truth.shape:
            raise ValueError(f"{method} forecasts do not match the truth shape")
        eigenvalues = np.linalg.eigvalsh(forecasts)
        if not np.isfinite(forecasts).all() or np.any(eigenvalues <= 0):
            raise ValueError(f"{method} produced a nonfinite or non-SPD forecast")
        for index in range(truth.shape[0]):
            frobenius2 = float(frobenius_loss(forecasts[index], truth[index]))
            bw2 = float(bw_loss(forecasts[index], truth[index]))
            rows.append({
                "month": str(months[index]),
                "method": method,
                "frobenius2": frobenius2,
                "frobenius": float(np.sqrt(frobenius2)),
                "qlike": float(qlike_loss(forecasts[index], truth[index])),
                "bw2": bw2,
                "bw": float(np.sqrt(bw2)),
                "risk_absolute_error": _risk_error(
                    forecasts[index], truth[index], lagged[index]
                ),
                "forecast_min_eigenvalue": float(eigenvalues[index, 0]),
                "forecast_condition_number": float(
                    eigenvalues[index, -1] / eigenvalues[index, 0]
                ),
            })
    long = pd.DataFrame(rows)
    summary = (
        long.groupby("method", sort=False)
        .agg(
            mean_frobenius2=("frobenius2", "mean"),
            median_frobenius=("frobenius", "median"),
            mean_qlike=("qlike", "mean"),
            median_qlike=("qlike", "median"),
            mean_bw2=("bw2", "mean"),
            median_bw=("bw", "median"),
            mean_risk_absolute_error=("risk_absolute_error", "mean"),
            median_risk_absolute_error=("risk_absolute_error", "median"),
            minimum_forecast_eigenvalue=("forecast_min_eigenvalue", "min"),
            maximum_forecast_condition_number=("forecast_condition_number", "max"),
        )
        .reset_index()
    )
    return long, summary


def _atomic_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    frame.to_csv(temporary, index=False)
    os.replace(temporary, path)


def plot_losses(long: pd.DataFrame, output: Path) -> None:
    methods = list(dict.fromkeys(long["method"]))
    colours = plt.colormaps["viridis"](np.linspace(0.08, 0.9, len(methods)))
    figure, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
    for method, colour in zip(methods, colours):
        frame = long.loc[long["method"] == method].reset_index(drop=True)
        x = np.arange(1, frame.shape[0] + 1)
        axes[0].plot(x, frame["frobenius"].expanding().mean(), label=method, color=colour)
        axes[1].plot(x, frame["qlike"].expanding().mean(), label=method, color=colour)
    axes[0].set(title="Cumulative Frobenius error", xlabel="forecast month", ylabel="mean error")
    axes[1].set(title="Cumulative QLIKE", xlabel="forecast month", ylabel="mean loss")
    axes[0].legend(frameon=False)
    for axis in axes:
        axis.grid(alpha=0.2)
    figure.savefig(output / "forecast_loss_paths.png", dpi=180)
    plt.close(figure)


def write_report(
    output: Path,
    design: dict[str, Any],
    summary: pd.DataFrame,
    rfd_diagnostics: list[dict[str, Any]],
) -> None:
    table = [
        "| method | mean Frobenius² | mean QLIKE | mean BW² | mean risk abs. error |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in summary.itertuples(index=False):
        table.append(
            f"| {row.method} | {row.mean_frobenius2:.6g} | "
            f"{row.mean_qlike:.6g} | {row.mean_bw2:.6g} | "
            f"{row.mean_risk_absolute_error:.6g} |"
        )
    clip_count = sum(float(item["forecast_clip_factor"]) < 1.0 for item in rfd_diagnostics)
    fallback_count = sum(int(item["fallback_count"]) for item in rfd_diagnostics)
    lines = [
        "# APP-MONTHLY-VAR — first causal forecasting bridge",
        "",
        f"- targets: {design['first_target_month']} through {design['last_target_month']}",
        f"- initial training months: {design['initial_train_months']}",
        f"- forecasts: {design['forecast_months']}",
        f"- fixed rank / lag horizon: {design['rank']} / {design['max_lag']}",
        "- both factor arms: OLS VAR(1) with intercept, refitted at each origin",
        "- parent centre: first training-window global BW centre held fixed",
        "- RFD centre: expanding causal path with terminal-centre carry",
        "",
        "## Loss summary",
        "",
        *table,
        "",
        "Squared Frobenius and multivariate QLIKE are the primary forecast losses. "
        "BW and the parent's portfolio-risk statistic are descriptive bridges.",
        "",
        "## Numerical health",
        "",
        f"- RFD forecast clips: {clip_count}/{design['forecast_months']}",
        f"- total RFD centre fallbacks across origins: {fallback_count}",
        f"- minimum RFD forecast eigenvalue: "
        f"{min(float(item['forecast_min_eigenvalue']) for item in rfd_diagnostics):.6g}",
        "",
        "## Scope",
        "",
        "This is a low-power implementation bridge; the production run contains "
        "one predeclared 36-month evaluation block. "
        "Rank two is inherited from the parent, not estimated truth. The comparison "
        "does not identify structural factor amplitudes, and projected-score VAR(1) "
        "is not a latent-state filter.",
        "",
        "See loss_by_month.csv, summary.csv, rfd_origin_diagnostics.csv, "
        "forecasts.npz, and forecast_loss_paths.png.",
    ]
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

    config = load_configuration(args.config)
    panel = load_panel(config)
    full_count = int(config["experiment"]["forecast_months"])
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
        print("APP-MONTHLY-VAR dry run passed; no forecasts were fitted.", flush=True)
        return

    output_key = "smoke_directory" if args.smoke_months else "directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config, forecast_months)
    design["digest"] = digest
    _atomic_json(output / "design.json", design)

    parent_cache = output / "parent_forecasts.npz"
    parent_meta = output / "parent_forecasts.json"
    parent_digest = parent_stage_digest(config, forecast_months)
    if args.force or not parent_cache.is_file() or not _cache_matches(parent_meta, parent_digest):
        print("[parent] running cloned dyn_RFM forecast loop", flush=True)
        started = time.perf_counter()
        parent = run_parent_forecasts(
            panel["panel"], config, forecast_months, rscript
        )
        _atomic_npz(parent_cache, forecasts=parent)
        _atomic_json(parent_meta, {
            "digest": parent_digest,
            "elapsed_seconds": time.perf_counter() - started,
        })
    else:
        print("[parent] reusing digest-matched forecasts", flush=True)
        with np.load(parent_cache, allow_pickle=False) as source:
            parent = source["forecasts"].copy()

    rfd_digest = rfd_stage_digest(config, forecast_months)
    rfd, rfd_health = run_rfd_forecasts(
        panel["panel"],
        config,
        forecast_months,
        output,
        rfd_digest,
        force=args.force,
    )
    initial = int(config["experiment"]["initial_train_months"])
    truth = panel["panel"][initial : initial + forecast_months]
    lagged = panel["panel"][initial - 1 : initial + forecast_months - 1]
    months = panel["months"][initial : initial + forecast_months]
    baselines = baseline_forecasts(
        panel["panel"],
        initial,
        forecast_months,
        float(config["baselines"]["ewma_lambda"]),
    )
    methods = {"Parent RFM": parent, "RFD": rfd, **baselines}
    long, summary = score_forecasts(methods, truth, lagged, months)
    _atomic_csv(output / "loss_by_month.csv", long)
    _atomic_csv(output / "summary.csv", summary)
    _atomic_csv(output / "rfd_origin_diagnostics.csv", pd.DataFrame(rfd_health))
    _atomic_npz(
        output / "forecasts.npz",
        truth=truth,
        months=months,
        parent_rfm=parent,
        rfd=rfd,
        locf=baselines["LOCF"],
        ewma=baselines["EWMA"],
    )
    plot_losses(long, output)
    write_report(output, design, summary, rfd_health)
    print(f"APP-MONTHLY-VAR report: {output / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
