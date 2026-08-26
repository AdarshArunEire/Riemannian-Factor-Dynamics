"""Run the causal APP-FIN centre-construction x score-head tournament.

The literal parent RFM global-centre representation and four RFD centre paths
compete on the same 36 expanding one-month-ahead origins.  Every representation
uses supplied rank two and lags 1:6, then branches to either the parent's OLS
VAR(1) head or the guarded latent-score Kalman head.

The RFD centre paths are:

* broad positive local means on the theorem grid;
* six positive segment means joined by a continuous BW polygon;
* twelve positive segment means joined by a continuous BW polygon; and
* the three-scale Richardson path.

No target month estimates its own centre, loading space, scores, or head.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
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
import run_appfin_score_filter as heads  # noqa: E402
from run_appfin_centre_diagnostic import _broad_positive_vertices  # noqa: E402
from run_appfin_identification import (  # noqa: E402
    _atomic_json,
    _atomic_npz,
    check_r_environment,
    load_panel,
)
from rfd.estimators.centre import estimate_centre_path  # noqa: E402
from rfd.estimators.centre_low_n import segmented_frechet_polygon  # noqa: E402
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
from rfd.forecast import forecast_score_state_space, forecast_var1  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "appfin_centre_head_tournament.yaml"
CENTRE_LABELS = {
    "broad_positive": "RFD broad-positive",
    "segmented_6": "RFD piecewise-6 polygon",
    "segmented_12": "RFD piecewise-12 polygon",
    "richardson": "RFD Richardson",
}
HEAD_LABELS = {"var": "VAR", "kf": "KF"}


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    source_path = (ROOT / config["experiment"]["source_score_filter_config"]).resolve()
    config["source_filter"] = heads.load_configuration(source_path)
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    methods = tuple(config["experiment"]["centre_methods"])
    if not methods or len(set(methods)) != len(methods):
        raise ValueError("centre_methods must be nonempty and unique")
    unknown = set(methods) - set(CENTRE_LABELS)
    if unknown:
        raise ValueError(f"unknown centre methods: {sorted(unknown)}")
    if int(config["experiment"]["workers"]) < 1:
        raise ValueError("workers must be positive")
    acceptance = config["acceptance"]
    if float(acceptance["maximum_qlike_multiple_of_parent_var"]) <= 1.0:
        raise ValueError("QLIKE multiplier boundary must exceed one")
    if float(acceptance["maximum_forecast_condition_number"]) <= 1.0:
        raise ValueError("condition-number boundary must exceed one")


def build_design(
    config: dict[str, Any],
    panel: dict[str, np.ndarray],
    forecast_months: int,
) -> dict[str, Any]:
    source = config["source_filter"]["source"]
    initial = int(source["experiment"]["initial_train_months"])
    centre_methods = list(config["experiment"]["centre_methods"])
    methods = ["Parent RFM global–VAR", "Parent RFM global–KF"]
    methods.extend(
        f"{CENTRE_LABELS[centre]}–{HEAD_LABELS[head]}"
        for centre in centre_methods
        for head in ("var", "kf")
    )
    return {
        "experiment_id": config["experiment"]["id"],
        "panel": str((ROOT / source["experiment"]["panel_path"]).resolve()),
        "initial_train_months": initial,
        "forecast_months": int(forecast_months),
        "first_target_month": str(panel["months"][initial]),
        "last_target_month": str(panel["months"][initial + forecast_months - 1]),
        "rank": int(source["experiment"]["rank"]),
        "max_lag": int(source["experiment"]["max_lag"]),
        "methods": methods,
        "future_centre_policy": "carry the terminal fitted centre one month",
        "causality": "every arm is refitted on the expanding prefix only",
        "scope": "APP-FIN forecast stability closure; no rank selection or latent-score truth",
    }


def _digest(config: dict[str, Any], forecast_months: int) -> str:
    paths = [
        Path(config["config_path"]),
        Path(config["source_filter"]["config_path"]),
        Path(config["source_filter"]["source"]["config_path"]),
        Path(__file__),
        ROOT / "py" / "rfd" / "estimators" / "centre.py",
        ROOT / "py" / "rfd" / "estimators" / "centre_low_n.py",
        ROOT / "py" / "rfd" / "estimators" / "frame.py",
        ROOT / "py" / "rfd" / "estimators" / "lag.py",
        ROOT / "py" / "rfd" / "forecast.py",
    ]
    material = json.dumps(
        {
            "forecast_months": forecast_months,
            "experiment": config["experiment"],
            "acceptance": config["acceptance"],
            "source": heads._jsonable_config(config["source_filter"]),
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    for path in paths:
        material += f"\n{path.resolve()}:{heads._sha256(path)}"
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _frame_bundle(
    training: np.ndarray,
    config: dict[str, Any],
) -> tuple[dict[str, PolygonalFrame], dict[str, dict[str, Any]]]:
    """Fit every RFD centre path once on a common expanding prefix."""
    source_config = config["source_filter"]["source"]
    source = source_config["rfd"]
    n = training.shape[0]
    time_values = np.arange(1, n + 1, dtype=float) / n
    settings = bridge.effective_rfd_settings(source_config, n)
    vertex_times = regular_polygon_grid(
        settings["n_cells"],
        start=float(time_values[0]),
        stop=float(time_values[-1]),
    )
    started = time.perf_counter()
    richardson = estimate_centre_path(
        observations=training,
        time=time_values,
        vertex_times=vertex_times,
        bandwidth=settings["bandwidth"],
        geometry=BW_GEOMETRY,
        overlap_fractions=tuple(source["overlap_fractions"]),
        mean_tol=float(source["mean_tolerance"]),
        max_iter=int(source["mean_max_iterations"]),
    )
    positive = PolygonalFrame(
        vertex_times,
        _broad_positive_vertices(richardson),
        BW_GEOMETRY,
    )
    frames: dict[str, PolygonalFrame] = {
        "broad_positive": positive,
        "richardson": richardson.polygon,
    }
    diagnostics: dict[str, dict[str, Any]] = {
        "broad_positive": {
            **settings,
            "centre_fit_seconds": float(time.perf_counter() - started),
            "centre_fallback_count": 0,
        },
        "richardson": {
            **settings,
            "centre_fit_seconds": float(time.perf_counter() - started),
            "centre_fallback_count": int(richardson.fallback_count),
        },
    }
    for segments in (6, 12):
        key = f"segmented_{segments}"
        if key not in config["experiment"]["centre_methods"]:
            continue
        segment_started = time.perf_counter()
        result = segmented_frechet_polygon(
            training,
            time_values,
            time_values,
            segments,
            BW_GEOMETRY,
            mean_tol=float(source["mean_tolerance"]),
            max_iter=int(source["mean_max_iterations"]),
        )
        frames[key] = result.frame
        diagnostics[key] = {
            **result.diagnostics,
            "centre_fit_seconds": float(time.perf_counter() - segment_started),
            "centre_fallback_count": 0,
        }
    requested = tuple(config["experiment"]["centre_methods"])
    return {key: frames[key] for key in requested}, {
        key: diagnostics[key] for key in requested
    }


def _representation_heads(
    training: np.ndarray,
    time_values: np.ndarray,
    frame: PolygonalFrame,
    config: dict[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, Any], dict[str, np.ndarray]]:
    source_config = config["source_filter"]["source"]
    source = source_config["rfd"]
    tangent_rows = common_reference_tangent_rows(training, time_values, frame)
    lag_row = lag_cross_covariances(
        tangent_rows,
        int(source_config["experiment"]["max_lag"]),
        demean=True,
        tail_mode=str(source["tail_mode"]),
        normalization=str(source["normalization"]),
    )
    spectrum = decompose_lag_operator(assemble_lag_operator(lag_row))
    factors = extract_dynamic_factors(
        spectrum, int(source_config["experiment"]["rank"])
    )
    scores = factors.factor_scores
    var_score, var_fit = forecast_var1(scores)
    state_fit = heads._state_fit(scores, config["source_filter"])
    kf_score, _ = forecast_score_state_space(scores, state_fit)
    terminal_time = np.array([time_values[-1]])
    terminal_centre = frame.vertices[-1]
    diagnostics = heads._head_diagnostics(var_fit, state_fit)
    forecasts: dict[str, np.ndarray] = {}
    arrays: dict[str, np.ndarray] = {
        "scores": scores,
        "lag_eigenvalues": spectrum.eigenvalues,
        "terminal_centre": terminal_centre,
        "var_score": var_score,
        "kf_score": kf_score,
    }
    for head, score in (("var", var_score), ("kf", kf_score)):
        row = factors.row_mean + factors.loadings @ score
        reference = coordinate_tangents(row[None, :], tangent_rows.basis)
        local = transport_from_reference(frame, reference, terminal_time)[0]
        forecast, health = heads._decode(
            terminal_centre,
            local,
            float(config["source_filter"]["head"]["bw_step_margin"]),
        )
        forecasts[head] = forecast
        arrays[head] = forecast
        diagnostics.update({f"{head}_{key}": value for key, value in health.items()})
    return forecasts, diagnostics, arrays


def run_rfd_origin(
    training: np.ndarray,
    config: dict[str, Any],
) -> tuple[dict[str, dict[str, np.ndarray]], list[dict[str, Any]], dict[str, np.ndarray]]:
    n = training.shape[0]
    time_values = np.arange(1, n + 1, dtype=float) / n
    frames, centre_health = _frame_bundle(training, config)
    forecasts: dict[str, dict[str, np.ndarray]] = {}
    diagnostics = []
    arrays: dict[str, np.ndarray] = {}
    for centre_method, frame in frames.items():
        started = time.perf_counter()
        result, health, stored = _representation_heads(
            training, time_values, frame, config
        )
        health.update(centre_health[centre_method])
        health.update({
            "centre_method": centre_method,
            "n_train": int(n),
            "representation_seconds": float(time.perf_counter() - started),
        })
        forecasts[centre_method] = result
        diagnostics.append(health)
        for key, value in stored.items():
            arrays[f"{centre_method}__{key}"] = value
    return forecasts, diagnostics, arrays


def _origin_worker(payload: tuple[Any, ...]) -> tuple[Any, ...]:
    """Fit one independent origin inside a spawn-safe worker process."""
    target, train_stop, training, config = payload
    started = time.perf_counter()
    result, health, arrays = run_rfd_origin(training, config)
    elapsed = float(time.perf_counter() - started)
    for row in health:
        row.update({
            "target_index": int(target),
            "origin_seconds": elapsed,
        })
    return int(target), int(train_stop), result, health, arrays


def _run_rfd_origins(
    observations: np.ndarray,
    config: dict[str, Any],
    forecast_months: int,
    output: Path,
    digest: str,
    *,
    force: bool,
) -> tuple[dict[str, dict[str, np.ndarray]], list[dict[str, Any]]]:
    source = config["source_filter"]["source"]
    initial = int(source["experiment"]["initial_train_months"])
    methods = tuple(config["experiment"]["centre_methods"])
    forecasts = {method: {"var": [], "kf": []} for method in methods}
    diagnostics: list[dict[str, Any]] = []
    directory = output / "rfd_origins"
    directory.mkdir(parents=True, exist_ok=True)
    origins = bridge.expanding_origins(initial, forecast_months)
    completed: dict[int, tuple[dict[str, dict[str, np.ndarray]], list[dict[str, Any]]]] = {}
    pending = []
    for train_stop, target in origins:
        cache = directory / f"target_{target:03d}.npz"
        meta = directory / f"target_{target:03d}.json"
        origin_digest = hashlib.sha256(f"{digest}:target={target}".encode()).hexdigest()
        if not force and cache.is_file() and bridge._cache_matches(meta, origin_digest):
            with np.load(cache, allow_pickle=False) as stored:
                result = {
                    method: {
                        head: stored[f"{method}__{head}"].copy()
                        for head in ("var", "kf")
                    }
                    for method in methods
                }
            health = json.loads(meta.read_text(encoding="utf-8"))["diagnostics"]
            completed[target] = (result, health)
        else:
            pending.append((target, train_stop, observations[:train_stop].copy(), config))

    if pending:
        workers = min(int(config["experiment"]["workers"]), len(pending))
        print(
            f"[RFD] fitting {len(pending)} uncached origins with {workers} workers",
            flush=True,
        )
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_origin_worker, payload): payload[:2] for payload in pending}
            for count, future in enumerate(as_completed(futures), start=1):
                target, train_stop, result, health, arrays = future.result()
                cache = directory / f"target_{target:03d}.npz"
                meta = directory / f"target_{target:03d}.json"
                origin_digest = hashlib.sha256(
                    f"{digest}:target={target}".encode()
                ).hexdigest()
                _atomic_npz(cache, **arrays)
                _atomic_json(meta, {"digest": origin_digest, "diagnostics": health})
                completed[target] = (result, health)
                worst = max(
                    float(row[f"{head}_forecast_condition_number"])
                    for row in health for head in ("var", "kf")
                )
                print(
                    f"[RFD {count:02d}/{len(pending):02d}] target={target}, "
                    f"train={train_stop}, worst condition={worst:.3g}",
                    flush=True,
                )

    for train_stop, target in origins:
        result, health = completed[target]
        for method in methods:
            for head in ("var", "kf"):
                forecasts[method][head].append(result[method][head])
        diagnostics.extend(health)
    stacked = {
        method: {head: np.stack(values) for head, values in by_head.items()}
        for method, by_head in forecasts.items()
    }
    return stacked, diagnostics


def _atomic_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    frame.to_csv(temporary, index=False)
    os.replace(temporary, path)


def _augment_summary(summary: pd.DataFrame) -> pd.DataFrame:
    summary = summary.copy()
    parent = summary.loc[summary["method"] == "Parent RFM global–VAR"].iloc[0]
    summary["qlike_multiple_of_parent_var"] = summary["mean_qlike"] / parent["mean_qlike"]
    summary["frobenius_change_percent"] = 100.0 * (
        summary["mean_frobenius2"] / parent["mean_frobenius2"] - 1.0
    )
    summary["bw_change_percent"] = 100.0 * (
        summary["mean_bw2"] / parent["mean_bw2"] - 1.0
    )
    return summary


def _plot(summary: pd.DataFrame, output: Path) -> None:
    labels = summary["method"].str.replace("RFD ", "", regex=False)
    colours = plt.colormaps["viridis"](np.linspace(0.08, 0.92, len(summary)))
    figure, axes = plt.subplots(2, 2, figsize=(14, 10), constrained_layout=True)
    panels = [
        ("qlike_multiple_of_parent_var", "Mean QLIKE", "× parent RFM–VAR", True),
        ("maximum_forecast_condition_number", "Worst forecast conditioning", "condition number", True),
        ("bw_change_percent", "Mean BW² change", "% versus parent RFM–VAR", False),
        ("frobenius_change_percent", "Mean Frobenius² change", "% versus parent RFM–VAR", False),
    ]
    for axis, (column, title, xlabel, logarithmic) in zip(axes.flat, panels):
        values = summary[column].to_numpy()
        axis.barh(labels, values, color=colours)
        axis.set(title=title, xlabel=xlabel)
        if logarithmic:
            axis.set_xscale("log")
            axis.axvline(1.0, color="0.35", linestyle="--", linewidth=1)
            formatter = lambda value: f"{value:.2g}×" if column.startswith("qlike") else f"{value:.2g}"
        else:
            axis.axvline(0.0, color="0.35", linewidth=1)
            formatter = lambda value: f"{value:+.1f}%"
        for index, value in enumerate(values):
            axis.annotate(
                formatter(value), (value, index), xytext=(4, 0),
                textcoords="offset points", va="center", fontsize=8,
            )
        axis.grid(axis="x", alpha=0.2)
    figure.suptitle("APP-FIN centre construction × score head")
    figure.savefig(output / "centre_head_tournament.png", dpi=180)
    plt.close(figure)


def _write_report(
    output: Path,
    design: dict[str, Any],
    summary: pd.DataFrame,
    diagnostics: pd.DataFrame,
    acceptance: dict[str, Any],
) -> None:
    q_limit = float(acceptance["maximum_qlike_multiple_of_parent_var"])
    c_limit = float(acceptance["maximum_forecast_condition_number"])
    summary = summary.copy()
    summary["stability_pass"] = (
        (summary["qlike_multiple_of_parent_var"] <= q_limit)
        & (summary["maximum_forecast_condition_number"] <= c_limit)
    )
    stable_rfd = summary.loc[
        summary["method"].str.startswith("RFD ") & summary["stability_pass"]
    ]
    best_qlike = stable_rfd.loc[stable_rfd["mean_qlike"].idxmin()]
    best_bw = stable_rfd.loc[stable_rfd["mean_bw2"].idxmin()]
    kf_fit_count = int(
        diagnostics.loc[
            (diagnostics["representation"] != "Parent RFM global")
            & (diagnostics["head"] == "kf")
        ].shape[0]
    )
    lines = [
        "# APP-FIN centre construction × score-head closure", "",
        "All results are causal one-month forecasts over the same 36 expanding",
        "origins. Rank two and lags 1:6 are supplied to every representation.", "",
        "| method | mean Frobenius² | mean QLIKE | QLIKE × parent | mean BW² | max condition | stable? |",
        "|---|---:|---:|---:|---:|---:|:---:|",
    ]
    for row in summary.itertuples(index=False):
        lines.append(
            f"| {row.method} | {row.mean_frobenius2:.6g} | {row.mean_qlike:.6g} | "
            f"{row.qlike_multiple_of_parent_var:.3g}× | {row.mean_bw2:.6g} | "
            f"{row.maximum_forecast_condition_number:.6g} | "
            f"{'yes' if row.stability_pass else 'no'} |"
        )
    rfd = diagnostics.loc[diagnostics["representation"] != "Parent RFM global"]
    lines.extend([
        "", "## Declared stability reading", "",
        f"An arm passes the operational no-blow-up check when mean QLIKE is at most {q_limit:g}×",
        f"parent RFM–VAR and its worst forecast condition number is at most {c_limit:g}.",
        "These limits classify numerical closure; they do not define statistical dominance.", "",
        f"- RFD forecasts requiring BW step clipping: {int((rfd['clip_factor'] < 1.0).sum())}/{len(rfd)}",
        f"- non-converged RFD Kalman fits: {int((~rfd.loc[rfd['head'] == 'kf', 'kf_converged'].astype(bool)).sum())}/{kf_fit_count} representation-origins",
        f"- best stable RFD QLIKE: {best_qlike['method']} at {best_qlike['qlike_multiple_of_parent_var']:.3g}× parent RFM–VAR",
        f"- best stable RFD intrinsic BW²: {best_bw['method']} at {best_bw['bw_change_percent']:+.1f}% versus parent RFM–VAR",
        "", "## Scope", "",
        "Piecewise-6 and piecewise-12 are continuous geodesic polygons, not step",
        "functions. Every observation is logged at its interpolated centre and",
        "recursively transported to the common reference frame. The future centre",
        "is the terminal training-prefix centre carried forward one month.", "",
        "The parent arm is the literal cloned RFM representation. APP-FIN provides",
        "no ground-truth factor amplitudes, so this adjudicates forecast loss and",
        "decoder stability only.", "",
        "See summary.csv, loss_by_month.csv, diagnostics.csv, forecasts.npz, and",
        "centre_head_tournament.png.",
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
    source_filter = config["source_filter"]
    source = source_filter["source"]
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
        print("APP-FIN centre-head dry run passed; no estimators were fitted.", flush=True)
        return

    output_key = "smoke_directory" if args.smoke_months else "directory"
    output = (ROOT / config["output"][output_key]).resolve()
    output.mkdir(parents=True, exist_ok=True)
    digest = _digest(config, forecast_months)
    design["digest"] = digest
    _atomic_json(output / "design.json", design)

    # Reuse the literal parent cache under its original, unchanged experiment
    # digest.  --force intentionally refits only the new RFD tournament.
    parent_output_key = "smoke_directory" if args.smoke_months else "directory"
    parent_output = (ROOT / source_filter["output"][parent_output_key]).resolve()
    parent_experiment_digest = heads.experiment_digest(source_filter, forecast_months)
    parent_digest = hashlib.sha256(
        f"{parent_experiment_digest}:parent".encode()
    ).hexdigest()
    parent_stage = heads.run_parent_stage(
        panel["panel"], source_filter, forecast_months, rscript,
        parent_output, parent_digest, force=False,
    )
    parent, parent_health = heads._run_parent_origins(
        parent_stage, source_filter, forecast_months
    )
    rfd, rfd_health = _run_rfd_origins(
        panel["panel"], config, forecast_months, output, digest, force=args.force
    )

    initial = int(source["experiment"]["initial_train_months"])
    truth = panel["panel"][initial : initial + forecast_months]
    lagged = panel["panel"][initial - 1 : initial + forecast_months - 1]
    months = panel["months"][initial : initial + forecast_months]
    keyed: dict[str, np.ndarray] = {
        "parent_var": parent["var"], "parent_kf": parent["kf"]
    }
    methods: dict[str, np.ndarray] = {
        "Parent RFM global–VAR": parent["var"],
        "Parent RFM global–KF": parent["kf"],
    }
    for centre_method in config["experiment"]["centre_methods"]:
        for head in ("var", "kf"):
            key = f"{centre_method}_{head}"
            keyed[key] = rfd[centre_method][head]
            methods[f"{CENTRE_LABELS[centre_method]}–{HEAD_LABELS[head]}"] = keyed[key]
    long, summary = bridge.score_forecasts(methods, truth, lagged, months)
    summary = _augment_summary(summary)

    parent_rows = []
    for health in parent_health:
        for head in ("var", "kf"):
            parent_rows.append({
                "representation": "Parent RFM global",
                "centre_method": "global",
                "head": head,
                "target_index": health["target_index"],
                "clip_factor": health[f"{head}_clip_factor"],
                "forecast_min_eigenvalue": health[f"{head}_forecast_min_eigenvalue"],
                "forecast_condition_number": health[f"{head}_forecast_condition_number"],
                "kf_converged": health["kf_converged"],
            })
    rfd_rows = []
    for health in rfd_health:
        for head in ("var", "kf"):
            rfd_rows.append({
                **health,
                "representation": CENTRE_LABELS[health["centre_method"]],
                "head": head,
                "clip_factor": health[f"{head}_clip_factor"],
                "forecast_min_eigenvalue": health[f"{head}_forecast_min_eigenvalue"],
                "forecast_condition_number": health[f"{head}_forecast_condition_number"],
            })
    diagnostics = pd.DataFrame(parent_rows + rfd_rows)
    _atomic_csv(output / "loss_by_month.csv", long)
    _atomic_csv(output / "summary.csv", summary)
    _atomic_csv(output / "diagnostics.csv", diagnostics)
    _atomic_npz(output / "forecasts.npz", truth=truth, months=months, **keyed)
    _plot(summary, output)
    _write_report(output, design, summary, diagnostics, config["acceptance"])
    print(f"APP-FIN centre-head report: {output / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
