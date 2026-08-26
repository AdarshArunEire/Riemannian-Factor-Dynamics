"""Dense blocked-validation curve for the APP-FIN polygon vertex count."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import json
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

from rfd.estimators.centre_low_n import segmented_frechet_polygon  # noqa: E402
from rfd.eval.losses import bw_loss, qlike_loss  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "centre_k_curve_n240.yaml"
VIRIDIS = plt.colormaps["viridis"]


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    selection = config["selection"]
    values = list(map(int, selection["k_values"]))
    if values != list(range(1, max(values) + 1)):
        raise ValueError("k_values must be every integer from one to K_max")
    n = int(config["experiment"]["expected_months"])
    block = int(selection["holdout_block_months"])
    if n % block:
        raise ValueError("holdout block must divide the sample")
    if not 1 <= int(selection["workers"]) <= 8:
        raise ValueError("workers must lie between one and eight")
    return config


def _load_inputs(config: dict[str, Any]) -> tuple[np.ndarray, np.ndarray, list[np.ndarray]]:
    with np.load(ROOT / config["experiment"]["panel_path"], allow_pickle=False) as source:
        panel = np.asarray(source["panel"], dtype=float)
        months = source["months"].astype(str)
    expected = config["experiment"]
    m = int(expected["expected_matrix_size"])
    if panel.shape != (int(expected["expected_months"]), m, m):
        raise ValueError(f"unexpected panel shape {panel.shape}")
    source_directory = ROOT / expected["source_directory"] / "folds"
    folds = []
    for fold in range(panel.shape[0] // int(config["selection"]["holdout_block_months"])):
        with np.load(source_directory / f"fold_{fold:02d}.npz", allow_pickle=False) as source:
            folds.append(source["indices"].astype(int).copy())
    return panel, months, folds


def _minimum_occupancy(times: np.ndarray, folds: list[np.ndarray], k: int) -> int:
    edges = np.linspace(float(times.min()), float(times.max()), k + 1)
    bins = np.clip(np.searchsorted(edges, times, side="right") - 1, 0, k - 1)
    all_indices = np.arange(times.size)
    return min(
        int(np.bincount(bins[np.setdiff1d(all_indices, heldout)], minlength=k).min())
        for heldout in folds
    )


def _worker(payload: tuple[Any, ...]) -> list[dict[str, Any]]:
    fold, heldout, panel, months, times, selection = payload
    keep = np.ones(times.size, dtype=bool)
    keep[heldout] = False
    training = panel[keep]
    training_times = times[keep]
    target_times = times[heldout]
    truth = panel[heldout]
    rows = []
    for k in map(int, selection["k_values"]):
        started = time.perf_counter()
        if k == 1:
            result = BW_GEOMETRY.barycentre(
                training,
                tol=float(selection["mean_tolerance"]),
                max_iter=int(selection["mean_max_iterations"]),
            )
            if not result.converged:
                raise RuntimeError("fold global centre did not converge")
            points = np.broadcast_to(result.X, truth.shape)
        else:
            polygon = segmented_frechet_polygon(
                training,
                training_times,
                target_times,
                k,
                BW_GEOMETRY,
                mean_tol=float(selection["mean_tolerance"]),
                max_iter=int(selection["mean_max_iterations"]),
            )
            points = polygon.points
        bw2 = bw_loss(points, truth)
        qlike = qlike_loss(points, truth)
        eigenvalues = np.linalg.eigvalsh(points)
        for position, index in enumerate(heldout):
            rows.append({
                "fold": int(fold),
                "month_index": int(index),
                "month": str(months[index]),
                "k": k,
                "bw2": float(bw2[position]),
                "qlike": float(qlike[position]),
                "minimum_eigenvalue": float(eigenvalues[position, 0]),
                "condition_number": float(eigenvalues[position, -1] / eigenvalues[position, 0]),
                "fit_seconds": float(time.perf_counter() - started),
            })
    return rows


def _analyse(frame: pd.DataFrame, output: Path, occupancy: dict[int, int]) -> None:
    fold_scores = frame.groupby(["k", "fold"], sort=True).agg(
        mean_bw2=("bw2", "mean"), mean_qlike=("qlike", "mean")
    ).reset_index()
    summary = frame.groupby("k", sort=True).agg(
        bw_rms=("bw2", lambda x: float(np.sqrt(x.mean()))),
        mean_bw2=("bw2", "mean"),
        mean_qlike=("qlike", "mean"),
        minimum_eigenvalue=("minimum_eigenvalue", "min"),
        maximum_condition_number=("condition_number", "max"),
        total_fit_seconds=("fit_seconds", "sum"),
    ).reset_index()
    fold_se = fold_scores.groupby("k")["mean_bw2"].sem().rename("fold_se_bw2")
    summary = summary.merge(fold_se, on="k")
    summary["minimum_training_observations_per_region"] = summary["k"].map(occupancy)
    global_loss = float(summary.loc[summary["k"].eq(1), "mean_bw2"].iloc[0])
    summary["bw_reduction_percent_vs_k1"] = 100.0 * (1.0 - summary["mean_bw2"] / global_loss)
    best_row = summary.loc[summary["mean_bw2"].idxmin()]
    threshold = float(best_row["mean_bw2"] + best_row["fold_se_bw2"])
    one_se_k = int(summary.loc[summary["mean_bw2"].le(threshold), "k"].min())
    summary["inside_one_se_of_best"] = summary["mean_bw2"].le(threshold)
    summary.to_csv(output / "k_curve_summary.csv", index=False)
    fold_scores.to_csv(output / "k_curve_fold_scores.csv", index=False)

    fig, axis = plt.subplots(figsize=(9.2, 5.4))
    axis.plot(summary["k"], summary["bw_rms"], marker="o", color=VIRIDIS(0.35))
    axis.axvline(int(best_row["k"]), color=VIRIDIS(0.75), linestyle="--", label=f"minimum K={int(best_row['k'])}")
    axis.axvline(one_se_k, color="0.35", linestyle=":", label=f"one-SE K={one_se_k}")
    axis.set_xticks(summary["k"])
    axis.set_xlabel("number of positive centre regions K")
    axis.set_ylabel("held-out BW centre error (RMS)")
    axis.set_title("APP-FIN centre complexity curve")
    axis.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output / "centre_k_curve.png", dpi=180)
    fig.savefig(output / "centre_k_curve.svg")
    plt.close(fig)

    lines = [
        "# APP-FIN dense centre-complexity curve", "",
        "Every consecutive integer K is evaluated with the same twenty leave-one-year-out folds. K=1 is the fold-specific global BW centre; K>=2 uses positive segment means joined by one continuous BW geodesic polygon. Held-out months never estimate their candidate path.", "",
        "## Verdict", "",
        f"- Raw validation minimum: **K={int(best_row['k'])}**, BW RMS {best_row['bw_rms']:.4f}, {best_row['bw_reduction_percent_vs_k1']:+.1f}% squared-error change versus K=1.",
        f"- One-standard-error choice: **K={one_se_k}**.",
        f"- At the largest feasible K={int(summary['k'].max())}, the worst fold leaves only {int(summary.iloc[-1]['minimum_training_observations_per_region'])} training observation(s) in one region.", "",
        "The curve is descriptive for this panel and blocking rule. It is not a universal K theorem and is not a forecasting-valid selection rule.", "",
    ]
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = load_configuration(args.config.resolve())
    panel, months, folds = _load_inputs(config)
    times = np.arange(1, panel.shape[0] + 1, dtype=float) / panel.shape[0]
    occupancy = {k: _minimum_occupancy(times, folds, k) for k in config["selection"]["k_values"]}
    design = {
        "experiment_id": config["experiment"]["id"],
        "k_values": config["selection"]["k_values"],
        "folds": len(folds),
        "holdout_months": int(config["selection"]["holdout_block_months"]),
        "minimum_occupancy_by_k": occupancy,
        "maximum_feasible_k": max(k for k, count in occupancy.items() if count > 0),
    }
    print(json.dumps(design, indent=2))
    if args.dry_run:
        return
    output = ROOT / config["output"]["directory"]
    output.mkdir(parents=True, exist_ok=True)
    (output / "design.json").write_text(json.dumps(design, indent=2), encoding="utf-8")
    jobs = [
        (fold, heldout, panel, months, times, config["selection"])
        for fold, heldout in enumerate(folds)
    ]
    rows = []
    started = time.perf_counter()
    with ProcessPoolExecutor(max_workers=int(config["selection"]["workers"])) as executor:
        futures = [executor.submit(_worker, job) for job in jobs]
        for done, future in enumerate(as_completed(futures), start=1):
            rows.extend(future.result())
            print(f"[{done}/{len(jobs)}] held-out folds complete", flush=True)
    frame = pd.DataFrame(rows).sort_values(["k", "fold", "month_index"])
    expected = len(folds) * len(config["selection"]["k_values"]) * int(config["selection"]["holdout_block_months"])
    if len(frame) != expected or frame.isna().any().any():
        raise RuntimeError(f"expected {expected} complete rows, found {len(frame)}")
    frame.to_csv(output / "monthly_scores.csv", index=False)
    _analyse(frame, output, occupancy)
    print(f"Completed in {time.perf_counter() - started:.1f}s")


if __name__ == "__main__":
    main()
