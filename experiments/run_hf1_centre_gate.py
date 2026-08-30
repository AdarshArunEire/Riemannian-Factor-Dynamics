"""APP-HF-1: blocked moving-centre gate on the frozen hourly crypto panel.

The gate uses only 52 complete weeks from 2024.  Two complementary blocked
folds hold out every week exactly once and remove a 24-hour edge from each
adjacent training week.  Global, broad-positive, piecewise-6 and piecewise-12
centres are selectable; Richardson is reported only as a negative control.
The final 48 hours of 2024 and all of 2025 are untouched by selection.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
import math
import os
from pathlib import Path
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

from run_appfin_centre_diagnostic import _fit_centre_bundle  # noqa: E402
from run_appfin_identification import _atomic_json, _atomic_npz  # noqa: E402
from run_end_to_end import production_multiplier  # noqa: E402
from rfd.estimators.centre_low_n import segmented_frechet_polygon  # noqa: E402
from rfd.estimators.frame import regular_polygon_grid  # noqa: E402
from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "hf1_centre_gate.yaml"
METHODS = ("global", "broad_positive", "piecewise6", "piecewise12", "richardson")
POSITIVE_METHODS = ("broad_positive", "piecewise6", "piecewise12")


def load_configuration(path: Path = CONFIG_DEFAULT) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    crossfit = config["crossfit"]
    candidates = config["candidates"]
    selection = config["selection"]
    null = config["dependent_null"]
    if int(experiment["complete_weeks"]) != 52 or int(experiment["hours_per_block"]) != 168:
        raise ValueError("HF-1 requires exactly 52 complete seven-day blocks")
    if int(crossfit["folds"]) != 2:
        raise ValueError("HF-1 uses exactly two complementary folds")
    embargo = int(crossfit["embargo_hours_each_training_edge"])
    if not 0 <= embargo < int(experiment["hours_per_block"]) // 2:
        raise ValueError("embargo must be less than half a validation block")
    if candidates["selectable"] != ["global", "broad_positive", "piecewise6", "piecewise12"]:
        raise ValueError("the frozen selectable centre candidates changed")
    if candidates["negative_control"] != "richardson":
        raise ValueError("Richardson must remain a nonselectable negative control")
    if list(map(int, candidates["piecewise_segments"])) != [6, 12]:
        raise ValueError("the frozen piecewise candidates are 6 and 12")
    if selection["primary_losses"] != ["frobenius2", "qlike"]:
        raise ValueError("Frobenius and QLIKE are the two primary losses")
    if not 0.0 < float(selection["maximum_single_edge_energy_share"]) < 1.0:
        raise ValueError("edge-energy share must lie in (0, 1)")
    if int(null["block_hours"]) != 168 or int(null["replicates"]) < 19:
        raise ValueError("dependent null requires weekly blocks and at least 19 replicates")
    if not 1 <= int(null["workers"]) <= 8:
        raise ValueError("workers must lie between one and eight")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def experiment_digest(config: dict[str, Any], *, smoke: bool) -> str:
    paths = [
        Path(config["config_path"]), ROOT / config["experiment"]["panel_path"],
        Path(__file__), ROOT / "py" / "rfd" / "estimators" / "centre.py",
        ROOT / "py" / "rfd" / "estimators" / "centre_low_n.py",
        ROOT / "py" / "rfd" / "spd" / "bw.py",
    ]
    material = "\n".join(f"{path.resolve()}:{_sha256(path)}" for path in paths)
    material += f"\nprofile={'smoke' if smoke else 'recorded'}"
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _cache_matches(path: Path, digest: str) -> bool:
    if not path.is_file():
        return False
    try:
        return json.loads(path.read_text(encoding="utf-8"))["digest"] == digest
    except (KeyError, ValueError, OSError):
        return False


def load_development_panel(config: dict[str, Any], *, smoke: bool = False) -> dict[str, np.ndarray]:
    path = ROOT / config["experiment"]["panel_path"]
    if not path.is_file():
        raise FileNotFoundError(f"APP-HF-0 panel is missing: {path}")
    with np.load(path, allow_pickle=False) as source:
        required = {"covariances", "hours", "symbols"}
        if not required.issubset(source.files):
            raise ValueError(f"HF-0 archive is missing {sorted(required - set(source.files))}")
        hours = source["hours"].copy()
        symbols = source["symbols"].astype(str)
        all_covariances = source["covariances"]
        years = hours.astype("datetime64[Y]").astype(int) + 1970
        development_indices = np.flatnonzero(years == int(config["experiment"]["development_year"]))
        covariances = all_covariances[development_indices].copy()
        development_hours = hours[development_indices].copy()

    expected = int(config["experiment"]["complete_weeks"]) * int(config["experiment"]["hours_per_block"])
    if covariances.shape[0] < expected:
        raise ValueError(f"2024 contains {covariances.shape[0]} hours; {expected} are required")
    covariances = covariances[:expected]
    development_hours = development_hours[:expected]
    if smoke:
        smoke_n = int(config["crossfit"]["smoke_complete_weeks"]) * int(config["experiment"]["hours_per_block"])
        covariances = covariances[:smoke_n]
        development_hours = development_hours[:smoke_n]
    if symbols.size != int(config["experiment"]["expected_assets"]):
        raise ValueError("HF-0 asset count does not match the HF-1 contract")
    expected_shape = (covariances.shape[0], int(config["experiment"]["expected_matrix_size"]), int(config["experiment"]["expected_matrix_size"]))
    if covariances.shape != expected_shape:
        raise ValueError(f"development panel shape is {covariances.shape}; expected {expected_shape}")
    if not np.isfinite(covariances).all() or np.any(np.linalg.eigvalsh(covariances) <= 0.0):
        raise ValueError("HF-1 requires finite strictly positive covariance matrices")
    expected_step = np.timedelta64(1, "h")
    if np.any(np.diff(development_hours) != expected_step):
        raise ValueError("development hours are not a contiguous hourly panel")
    return {"covariances": covariances, "hours": development_hours, "symbols": symbols}


def blocked_fold_masks(
    n: int,
    *,
    block_hours: int,
    validation_parity: int,
    embargo_hours: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if n % block_hours:
        raise ValueError("complete blocked folds require n divisible by block_hours")
    index = np.arange(n)
    block = index // block_hours
    within = index % block_hours
    validation = block % 2 == int(validation_parity)
    training_block = ~validation
    training = training_block & (within >= embargo_hours) & (within < block_hours - embargo_hours)
    if np.any(training & validation) or not training.any() or not validation.any():
        raise RuntimeError("invalid blocked cross-fit masks")
    return training, validation, block


def _fit_controls(config: dict[str, Any], n_train: int) -> dict[str, Any]:
    source = config["rfd"]
    estimator = {
        "bandwidth_constant": float(source["bandwidth_constant"]),
        "bandwidth_exponent": float(source["bandwidth_exponent"]),
        "production_multiplier_cap": float(source["production_multiplier_cap"]),
        "admissible_boundary_fraction": float(source["admissible_boundary_fraction"]),
        "overlap_fractions": tuple(source["overlap_fractions"]),
    }
    multiplier = production_multiplier(n_train, estimator)
    bandwidth = estimator["bandwidth_constant"] * n_train ** (-estimator["bandwidth_exponent"]) * multiplier
    n_cells = max(1, int(math.ceil(
        float(source["polygon_cell_constant"])
        * (n_train ** (-float(source["polygon_rate_exponent"]))) ** (-2.0 / 3.0)
    )))
    return {
        "bandwidth": float(bandwidth),
        "bandwidth_multiplier": float(multiplier),
        "n_cells": int(n_cells),
        "overlap_fractions": tuple(source["overlap_fractions"]),
        "mean_tolerance": float(source["mean_tolerance"]),
        "mean_max_iterations": int(source["mean_max_iterations"]),
    }


def _fit_methods(
    observations: np.ndarray,
    observation_times: np.ndarray,
    target_times: np.ndarray,
    config: dict[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    controls = _fit_controls(config, observations.shape[0])
    domain_start = float(min(observation_times.min(), target_times.min()))
    domain_stop = float(max(observation_times.max(), target_times.max()))
    vertex_times = regular_polygon_grid(
        controls["n_cells"], start=domain_start, stop=domain_stop
    )
    bundle, diagnostics = _fit_centre_bundle(
        observations, observation_times, target_times, vertex_times, controls
    )
    estimates = {
        "global": np.broadcast_to(bundle["global_centre"], (target_times.size,) + bundle["global_centre"].shape).copy(),
        "broad_positive": bundle["positive_centres"],
        "richardson": bundle["richardson_centres"],
    }
    metadata: dict[str, Any] = {
        "controls": controls,
        "richardson": diagnostics,
        "global_centre": bundle["global_centre"],
        "broad_positive_vertices": bundle["positive_vertices"],
        "richardson_vertices": bundle["richardson_vertices"],
        "richardson_vertex_times": vertex_times,
    }
    for segments in map(int, config["candidates"]["piecewise_segments"]):
        result = segmented_frechet_polygon(
            observations, observation_times, target_times, segments, BW_GEOMETRY,
            mean_tol=controls["mean_tolerance"], max_iter=controls["mean_max_iterations"],
        )
        name = f"piecewise{segments}"
        estimates[name] = result.points
        metadata[name] = result.diagnostics
        metadata[f"{name}_vertices"] = result.frame.vertices
        metadata[f"{name}_vertex_times"] = result.frame.vertex_times
    return estimates, metadata


def _fold_worker(payload: tuple[Any, ...]) -> tuple[int, dict[str, np.ndarray], dict[str, Any]]:
    fold, observations, times, train, validation, block_ids, config = payload
    started = time.perf_counter()
    estimates, metadata = _fit_methods(observations[train], times[train], times[validation], config)
    arrays = {"indices": np.flatnonzero(validation), "block_ids": block_ids[validation]}
    arrays.update({f"centre_{name}": value for name, value in estimates.items()})
    serializable = _json_metadata(metadata)
    serializable["elapsed_seconds"] = float(time.perf_counter() - started)
    serializable["training_hours"] = int(train.sum())
    serializable["validation_hours"] = int(validation.sum())
    return int(fold), arrays, serializable


def _json_metadata(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _json_metadata(item) for key, item in value.items() if not isinstance(item, np.ndarray)}
    if isinstance(value, (list, tuple)):
        return [_json_metadata(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    return value


def permute_complete_blocks(
    observations: np.ndarray,
    *,
    block_hours: int,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    if observations.shape[0] % block_hours:
        raise ValueError("block permutation requires complete blocks")
    blocks = observations.reshape(-1, block_hours, *observations.shape[1:])
    order = rng.permutation(blocks.shape[0])
    return blocks[order].reshape(observations.shape), order


def _movement_statistic(global_centre: np.ndarray, path: np.ndarray) -> float:
    reference = np.broadcast_to(global_centre, path.shape)
    return float(np.mean(BW_GEOMETRY.dist2(reference, path)))


def _null_worker(payload: tuple[Any, ...]) -> tuple[int, dict[str, Any]]:
    replicate, observations, times, config, seed = payload
    started = time.perf_counter()
    shuffled, order = permute_complete_blocks(
        observations,
        block_hours=int(config["dependent_null"]["block_hours"]),
        rng=np.random.default_rng(int(seed) + int(replicate)),
    )
    controls = _fit_controls(config, shuffled.shape[0])
    global_result = BW_GEOMETRY.barycentre(
        shuffled, tol=controls["mean_tolerance"], max_iter=controls["mean_max_iterations"]
    )
    if not global_result.converged:
        raise RuntimeError("null global BW centre did not converge")
    result = segmented_frechet_polygon(
        shuffled, times, times, 6, BW_GEOMETRY,
        mean_tol=controls["mean_tolerance"], max_iter=controls["mean_max_iterations"],
    )
    return int(replicate), {
        "movement_energy": _movement_statistic(global_result.X, result.points),
        "elapsed_seconds": float(time.perf_counter() - started),
        "block_order_sha256": hashlib.sha256(order.tobytes()).hexdigest(),
    }


def _run_jobs(jobs: list[tuple[Any, ...]], worker: Any, workers: int) -> list[Any]:
    if workers == 1:
        return [worker(job) for job in jobs]
    results = []
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, job): job[0] for job in jobs}
        for completed, future in enumerate(as_completed(futures), start=1):
            result = future.result()
            results.append(result)
            print(f"[parallel] completed {completed}/{len(futures)}; item={futures[future]}", flush=True)
    return results


def _score_folds(
    observations: np.ndarray,
    hours: np.ndarray,
    output: Path,
    fold_count: int,
) -> pd.DataFrame:
    records: list[dict[str, Any]] = []
    for fold in range(fold_count):
        with np.load(output / "folds" / f"fold_{fold}.npz", allow_pickle=False) as source:
            indices = source["indices"].copy()
            blocks = source["block_ids"].copy()
            truth = observations[indices]
            for method in METHODS:
                centre = source[f"centre_{method}"].copy()
                frobenius2 = frobenius_loss(centre, truth)
                qlike = qlike_loss(centre, truth)
                bw2 = bw_loss(centre, truth)
                for position, index in enumerate(indices):
                    records.append({
                        "fold": fold,
                        "block": int(blocks[position]),
                        "index": int(index),
                        "hour": str(hours[index]),
                        "method": method,
                        "frobenius2": float(frobenius2[position]),
                        "qlike": float(qlike[position]),
                        "bw2": float(bw2[position]),
                    })
    return pd.DataFrame(records)


def paired_method_table(scores: pd.DataFrame) -> pd.DataFrame:
    weekly = scores.groupby(["block", "method"], sort=True)[["frobenius2", "qlike", "bw2"]].mean()
    records = []
    for method in METHODS:
        row: dict[str, Any] = {"method": method, "weeks": int(weekly.xs(method, level="method").shape[0])}
        candidate = weekly.xs(method, level="method")
        global_values = weekly.xs("global", level="method")
        for metric in ("frobenius2", "qlike", "bw2"):
            values = candidate[metric]
            difference = global_values[metric] - values
            se = float(difference.std(ddof=1) / math.sqrt(difference.size)) if difference.size > 1 else float("inf")
            row[f"mean_{metric}"] = float(values.mean())
            row[f"se_mean_{metric}"] = float(values.std(ddof=1) / math.sqrt(values.size)) if values.size > 1 else float("inf")
            row[f"improvement_{metric}"] = float(difference.mean())
            row[f"se_improvement_{metric}"] = se
            row[f"reduction_percent_{metric}"] = 100.0 * float(difference.mean()) / float(global_values[metric].mean())
        records.append(row)
    return pd.DataFrame(records)


def select_centre_method(summary: pd.DataFrame, config: dict[str, Any]) -> dict[str, Any]:
    standard_errors = float(config["selection"]["require_improvement_beyond_standard_errors"])
    eligible = []
    for method in POSITIVE_METHODS:
        row = summary.set_index("method").loc[method]
        if all(
            row[f"improvement_{metric}"] > standard_errors * row[f"se_improvement_{metric}"]
            for metric in config["selection"]["primary_losses"]
        ):
            eligible.append(method)
    if not eligible:
        return {"selected_method": "global", "eligible_positive_methods": [], "reason": "no moving method beat global beyond one weekly SE on both primary losses"}

    indexed = summary.set_index("method")
    best_means = {
        metric: min(float(indexed.loc[method, f"mean_{metric}"]) for method in eligible)
        for metric in config["selection"]["primary_losses"]
    }
    minimax = min(
        eligible,
        key=lambda method: max(
            float(indexed.loc[method, f"mean_{metric}"]) / best_means[metric]
            for metric in config["selection"]["primary_losses"]
        ),
    )
    selected = minimax
    if "piecewise6" in eligible and minimax != "piecewise6":
        weekly_se = float(config["selection"]["prefer_piecewise6_within_standard_errors"])
        within = all(
            float(indexed.loc["piecewise6", f"mean_{metric}"])
            <= float(indexed.loc[minimax, f"mean_{metric}"])
            + weekly_se * math.sqrt(
                float(indexed.loc["piecewise6", f"se_mean_{metric}"]) ** 2
                + float(indexed.loc[minimax, f"se_mean_{metric}"]) ** 2
            )
            for metric in config["selection"]["primary_losses"]
        )
        if within:
            selected = "piecewise6"
    return {
        "selected_method": selected,
        "minimax_winner": minimax,
        "eligible_positive_methods": eligible,
        "reason": "conservative two-loss one-SE rule; piecewise6 receives the declared lower-complexity preference",
    }


def _edge_energy_share(vertices: np.ndarray) -> float:
    if vertices.shape[0] < 2:
        return 0.0
    energies = np.asarray(BW_GEOMETRY.dist2(vertices[:-1], vertices[1:]), dtype=float)
    total = float(energies.sum())
    return float(energies.max() / total) if total > 0.0 else 0.0


def _load_null(output: Path, replicates: int) -> pd.DataFrame:
    rows = []
    for replicate in range(replicates):
        path = output / "dependent_null" / f"replicate_{replicate:03d}.json"
        if path.is_file():
            payload = json.loads(path.read_text(encoding="utf-8"))
            rows.append({key: value for key, value in payload.items() if key != "digest"})
    return pd.DataFrame(rows)


def _plots(
    output: Path,
    scores: pd.DataFrame,
    summary: pd.DataFrame,
    full: dict[str, np.ndarray],
    null: pd.DataFrame,
    observed_movement: float,
    *,
    smoke: bool,
) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    colours = {method: plt.colormaps["viridis"](value) for method, value in zip(METHODS, np.linspace(0.08, 0.92, len(METHODS)))}
    base = summary.set_index("method")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, metric, label in zip(axes, ("frobenius2", "qlike"), ("Frobenius", "QLIKE")):
        methods = list(METHODS)
        values = [base.loc[method, f"reduction_percent_{metric}"] for method in methods]
        ax.barh(methods, values, color=[colours[m] for m in methods])
        ax.axvline(0.0, color="0.3", linewidth=1)
        ax.set(xlabel="error reduction versus global centre (%)", title=label)
    fig.suptitle("HF-1 smoke only — held-out centre performance" if smoke else "Held-out 2024 centre performance")
    fig.tight_layout()
    fig.savefig(output / "heldout_error_reduction.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    global_centre = full["global_centre"]
    fig, ax = plt.subplots(figsize=(11, 4.5))
    for method in POSITIVE_METHODS + ("richardson",):
        path = full[f"centre_{method}"]
        distance = np.sqrt(BW_GEOMETRY.dist2(np.broadcast_to(global_centre, path.shape), path))
        ax.plot(full["times"], distance, color=colours[method], label=method.replace("_", " "), alpha=0.9)
    ax.set(xlabel="rescaled 2024 time", ylabel="BW distance from global centre", title="How much centre motion does each method infer?")
    ax.legend(frameon=False, ncol=2)
    fig.tight_layout()
    fig.savefig(output / "centre_motion.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    if not null.empty:
        fig, ax = plt.subplots(figsize=(7.5, 4.5))
        ax.hist(null["movement_energy"], bins=min(12, max(3, null.shape[0] // 3)), color=plt.colormaps["viridis"](0.42), alpha=0.85)
        ax.axvline(observed_movement, color="#d95f02", linewidth=2, label="observed piecewise-6")
        ax.set(xlabel="mean squared BW movement from global centre", ylabel="permuted weekly panels", title="Dependence-preserving fixed-centre null")
        ax.legend(frameon=False)
        fig.tight_layout()
        fig.savefig(output / "dependent_null.png", dpi=180, bbox_inches="tight")
        plt.close(fig)


def _summary_markdown(summary: pd.DataFrame) -> str:
    columns = (
        "method", "mean_frobenius2", "reduction_percent_frobenius2",
        "mean_qlike", "reduction_percent_qlike", "mean_bw2",
        "reduction_percent_bw2",
    )
    labels = (
        "method", "Frobenius²", "Frob. reduction %", "QLIKE",
        "QLIKE reduction %", "BW²", "BW reduction %",
    )
    lines = [
        "| " + " | ".join(labels) + " |",
        "|" + "|".join(["---"] + ["---:"] * (len(labels) - 1)) + "|",
    ]
    for _, row in summary.loc[:, columns].iterrows():
        values = [str(row["method"])] + [f"{float(row[column]):.6g}" for column in columns[1:]]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def analyze(
    output: Path,
    config: dict[str, Any],
    panel: dict[str, np.ndarray],
    *,
    fold_count: int,
    null_replicates: int,
    require_null: bool,
    smoke: bool,
) -> dict[str, Any]:
    scores = _score_folds(panel["covariances"], panel["hours"], output, fold_count)
    scores.to_csv(output / "heldout_scores.csv", index=False)
    summary = paired_method_table(scores)
    summary.to_csv(output / "method_summary.csv", index=False)
    selection = select_centre_method(summary, config)
    with np.load(output / "full_fit.npz", allow_pickle=False) as source:
        full = {name: source[name].copy() for name in source.files}
    observed_movement = _movement_statistic(full["global_centre"], full["centre_piecewise6"])
    null = _load_null(output, null_replicates)
    if require_null and null.shape[0] != null_replicates:
        raise RuntimeError(f"dependent null has {null.shape[0]} replicates; expected {null_replicates}")
    p_value = None if null.empty else float((1 + np.sum(null["movement_energy"] >= observed_movement)) / (1 + null.shape[0]))
    selected = selection["selected_method"]
    edge_share = 0.0 if selected == "global" else _edge_energy_share(full[f"vertices_{selected}"])
    if selected == "global":
        verdict = "REJECT_MOVING_CENTRE__GLOBAL_WITHIN_ONE_SE"
    elif p_value is not None and p_value > float(config["dependent_null"]["significance_level"]):
        verdict = "REJECT_MOVING_CENTRE__MOVEMENT_NOT_DISTINGUISHED_FROM_DEPENDENT_NULL"
    elif edge_share > float(config["selection"]["maximum_single_edge_energy_share"]):
        verdict = "REJECT_SMOOTH_MOVING_CENTRE__JUMP_DOMINATED"
    else:
        verdict = f"PASS_MOVING_CENTRE__{selected.upper()}"
    scientific_verdict = verdict
    if smoke:
        verdict = f"SMOKE_ONLY__{verdict}"
    result = {
        **selection,
        "verdict": verdict,
        "scientific_verdict_if_recorded_design_agreed": scientific_verdict,
        "dependent_null_p_value": p_value,
        "observed_piecewise6_movement_energy": observed_movement,
        "selected_path_maximum_edge_energy_share": edge_share,
        "sealed_evaluation_year": int(config["experiment"]["sealed_evaluation_year"]),
    }
    _atomic_json(output / "verdict.json", result)
    _plots(output, scores, summary, full, null, observed_movement, smoke=smoke)
    report = [
        "# APP-HF-1 hourly crypto centre gate", "",
        f"**Verdict: `{verdict}`.**", "",
        (
            "This is a **non-scientific 16-week smoke profile** used only to validate the executable pipeline. It cannot pass or reject the centre hypothesis."
            if smoke else
            "This decision used only the first 52 complete UTC weeks of 2024. The final 48 hours of 2024 and every 2025 covariance remain outside centre selection."
        ), "",
        "## Frozen decision rule", "",
        "A moving method had to beat the global centre by more than one paired weekly standard error under **both** squared Frobenius loss and multivariate QLIKE. Richardson was never selectable. Piecewise-6 received the declared lower-complexity preference when statistically tied.", "",
        "## Held-out results", "",
        _summary_markdown(summary), "",
        f"Selected method: **{selected}**. Eligible positive methods: {', '.join(selection['eligible_positive_methods']) or 'none'}.", "",
        f"Piecewise-6 movement energy: `{observed_movement:.6g}`. Dependent weekly-block null p-value: `{p_value if p_value is not None else 'not run'}`.", "",
        f"Selected path maximum single-edge energy share: `{edge_share:.3%}`.", "",
        "Squared BW loss is reported as a geometric description but did not choose the winner. The fixed-centre null permutes complete weeks, preserving within-week dependence and hour-of-week structure while destroying slow calendar order.", "",
        "## Scope", "",
        "This is a centre-identification gate, not a factor, reconstruction, or forecasting result. Passing authorises APP-HF-2; rejection is itself the predeclared terminal Paper 1 result for smooth moving-centre RFD on this panel.", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")
    return result


def build_design(config: dict[str, Any], panel: dict[str, np.ndarray], *, smoke: bool) -> dict[str, Any]:
    hours_per_block = int(config["experiment"]["hours_per_block"])
    complete_weeks = panel["covariances"].shape[0] // hours_per_block
    embargo = int(config["crossfit"]["embargo_hours_each_training_edge"])
    train, validation, _ = blocked_fold_masks(
        panel["covariances"].shape[0], block_hours=hours_per_block,
        validation_parity=0, embargo_hours=embargo,
    )
    return {
        "experiment_id": config["experiment"]["id"],
        "profile": "smoke" if smoke else "recorded",
        "development_hours": int(panel["covariances"].shape[0]),
        "complete_weeks": int(complete_weeks),
        "matrix_size": int(panel["covariances"].shape[1]),
        "assets": panel["symbols"].tolist(),
        "folds": 2,
        "training_hours_per_fold_after_embargo": int(train.sum()),
        "validation_hours_per_fold": int(validation.sum()),
        "embargo_hours_each_training_edge": embargo,
        "selectable_methods": config["candidates"]["selectable"],
        "negative_control": config["candidates"]["negative_control"],
        "primary_losses": config["selection"]["primary_losses"],
        "dependent_null_replicates": int(config["dependent_null"]["smoke_replicates"] if smoke else config["dependent_null"]["replicates"]),
        "unused_2024_remainder_hours_recorded_profile": 48,
        "sealed_evaluation_year": int(config["experiment"]["sealed_evaluation_year"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--skip-null", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    config = load_configuration(args.config)
    panel = load_development_panel(config, smoke=args.smoke)
    design = build_design(config, panel, smoke=args.smoke)
    print(json.dumps(design, indent=2), flush=True)
    if args.dry_run:
        print("APP-HF-1 dry run passed; 2025 was not evaluated.", flush=True)
        return

    output_key = "smoke_directory" if args.smoke else "directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config, smoke=args.smoke)
    design["digest"] = digest
    _atomic_json(output / "design.json", design)
    observations = panel["covariances"]
    n = observations.shape[0]
    times = np.linspace(0.0, 1.0, n)
    hours_per_block = int(config["experiment"]["hours_per_block"])
    embargo = int(config["crossfit"]["embargo_hours_each_training_edge"])

    fold_directory = output / "folds"
    fold_directory.mkdir(parents=True, exist_ok=True)
    fold_jobs = []
    for fold in range(2):
        fold_digest = f"{digest}:fold:{fold}"
        path = fold_directory / f"fold_{fold}.npz"
        meta = fold_directory / f"fold_{fold}.meta.json"
        if args.force or not path.is_file() or not _cache_matches(meta, fold_digest):
            train, validation, blocks = blocked_fold_masks(
                n, block_hours=hours_per_block, validation_parity=fold,
                embargo_hours=embargo,
            )
            fold_jobs.append((fold, observations, times, train, validation, blocks, config))
    if fold_jobs:
        print(f"[cross-fit] fitting {len(fold_jobs)} missing complementary folds", flush=True)
        results = _run_jobs(fold_jobs, _fold_worker, len(fold_jobs))
        for fold, arrays, metadata in results:
            _atomic_npz(fold_directory / f"fold_{fold}.npz", **arrays)
            _atomic_json(fold_directory / f"fold_{fold}.meta.json", {"digest": f"{digest}:fold:{fold}", "diagnostics": metadata})
    else:
        print("[cross-fit] both complementary folds are cached", flush=True)

    full_path = output / "full_fit.npz"
    full_meta = output / "full_fit.meta.json"
    if args.force or not full_path.is_file() or not _cache_matches(full_meta, f"{digest}:full"):
        print("[full] fitting all candidate paths on the complete development panel", flush=True)
        estimates, metadata = _fit_methods(observations, times, times, config)
        arrays: dict[str, np.ndarray] = {"times": times, "global_centre": metadata["global_centre"]}
        arrays.update({f"centre_{name}": value for name, value in estimates.items()})
        arrays.update({
            "vertices_broad_positive": metadata["broad_positive_vertices"],
            "vertices_richardson": metadata["richardson_vertices"],
            "vertices_piecewise6": metadata["piecewise6_vertices"],
            "vertices_piecewise12": metadata["piecewise12_vertices"],
        })
        _atomic_npz(full_path, **arrays)
        _atomic_json(full_meta, {"digest": f"{digest}:full", "diagnostics": _json_metadata(metadata)})
    else:
        print("[full] reusing digest-matched fit", flush=True)

    null_replicates = int(config["dependent_null"]["smoke_replicates"] if args.smoke else config["dependent_null"]["replicates"])
    if not args.skip_null:
        directory = output / "dependent_null"
        directory.mkdir(parents=True, exist_ok=True)
        jobs = []
        for replicate in range(null_replicates):
            path = directory / f"replicate_{replicate:03d}.json"
            replicate_digest = f"{digest}:null:{replicate}"
            if args.force or not _cache_matches(path, replicate_digest):
                jobs.append((replicate, observations, times, config, int(config["dependent_null"]["seed"])))
        if jobs:
            print(f"[dependent null] fitting {len(jobs)} missing weekly-block permutations", flush=True)
            results = _run_jobs(jobs, _null_worker, min(int(config["dependent_null"]["workers"]), len(jobs)))
            for replicate, values in results:
                _atomic_json(directory / f"replicate_{replicate:03d}.json", {"digest": f"{digest}:null:{replicate}", "replicate": replicate, **values})
        else:
            print("[dependent null] all requested permutations are cached", flush=True)

    result = analyze(
        output, config, panel, fold_count=2, null_replicates=null_replicates,
        require_null=not args.skip_null,
        smoke=args.smoke,
    )
    print(json.dumps(result, indent=2), flush=True)
    print(f"APP-HF-1 report: {output / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
