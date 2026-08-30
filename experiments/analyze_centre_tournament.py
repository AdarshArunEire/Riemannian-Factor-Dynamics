"""Analyse the low-sample APP-FIN centre tournament."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from analyze_appfin_centre_diagnostic import _geodesic_shrink  # noqa: E402
from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402


VIRIDIS = plt.colormaps["viridis"]


def _load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as source:
        return {name: source[name].copy() for name in source.files}


def _key(prefix: str, value: float | int) -> str:
    return f"{prefix}_{str(value).replace('.', 'p')}"


def _spectral_health(points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    eigenvalues = np.linalg.eigvalsh(points)
    return eigenvalues[:, 0], eigenvalues[:, -1] / eigenvalues[:, 0]


def _rows_for_fold(
    panel: np.ndarray,
    months: np.ndarray,
    fold: int,
    arrays: dict[str, np.ndarray],
    tournament: dict[str, Any],
) -> list[dict[str, Any]]:
    indices = arrays["indices"].astype(int)
    truth = panel[indices]
    global_points = np.broadcast_to(arrays["global_centre"], truth.shape)
    candidates: list[tuple[str, str, float, np.ndarray]] = [
        ("global", "global", 0.0, global_points),
        ("positive_local", "positive_raw", 1.0, arrays["positive_centres"]),
        ("richardson", "richardson_raw", 1.0, arrays["richardson_centres"]),
        ("tangent_trend", "tangent_trend", 0.0, arrays["tangent_trend"]),
    ]
    for coefficient in tournament["shrinkage_lambdas"]:
        coefficient = float(coefficient)
        candidates.extend([
            (
                f"positive_shrink_{coefficient:.1f}",
                "positive_shrink",
                coefficient,
                _geodesic_shrink(
                    arrays["global_centre"], arrays["positive_centres"], coefficient
                ),
            ),
            (
                f"richardson_shrink_{coefficient:.1f}",
                "richardson_shrink",
                coefficient,
                _geodesic_shrink(
                    arrays["global_centre"], arrays["richardson_centres"], coefficient
                ),
            ),
        ])
    for strength in tournament["graph_strengths"]:
        value = float(strength)
        candidates.append((
            f"graph_smooth_{value:g}", "graph_smooth", value,
            arrays[_key("graph", value)],
        ))
    for segments in tournament["piecewise_segments"]:
        value = int(segments)
        candidates.append((
            f"piecewise_{value}", "piecewise", float(value),
            arrays[_key("piecewise", value)],
        ))
        candidates.append((
            f"segmented_polygon_{value}", "segmented_polygon", float(value),
            arrays[_key("segmented_polygon", value)],
        ))

    truth_scale = np.maximum(frobenius_loss(np.zeros_like(truth), truth), 1e-300)
    rows = []
    for method, family, parameter, points in candidates:
        bw2 = bw_loss(points, truth)
        qlike = qlike_loss(points, truth)
        relative_frobenius2 = frobenius_loss(points, truth) / truth_scale
        minimum_eigenvalue, condition = _spectral_health(points)
        for position, index in enumerate(indices):
            rows.append({
                "month_index": int(index),
                "month": str(months[index]),
                "fold": int(fold),
                "fold_parity": int(fold % 2),
                "method": method,
                "family": family,
                "parameter": float(parameter),
                "bw2": float(bw2[position]),
                "qlike": float(qlike[position]),
                "relative_frobenius2": float(relative_frobenius2[position]),
                "minimum_eigenvalue": float(minimum_eigenvalue[position]),
                "condition_number": float(condition[position]),
            })
    return rows


def _metrics(frame: pd.DataFrame) -> dict[str, float]:
    return {
        "bw_rms": float(np.sqrt(frame["bw2"].mean())),
        "mean_bw2": float(frame["bw2"].mean()),
        "mean_qlike": float(frame["qlike"].mean()),
        "relative_frobenius_rms": float(np.sqrt(frame["relative_frobenius2"].mean())),
        "minimum_eigenvalue": float(frame["minimum_eigenvalue"].min()),
        "median_condition_number": float(frame["condition_number"].median()),
        "maximum_condition_number": float(frame["condition_number"].max()),
    }


def _all_fold_summary(scores: pd.DataFrame) -> pd.DataFrame:
    records = []
    for (method, family, parameter), frame in scores.groupby(
        ["method", "family", "parameter"], sort=False
    ):
        records.append({
            "method": method,
            "family": family,
            "parameter": parameter,
            **_metrics(frame),
        })
    result = pd.DataFrame(records)
    global_bw2 = float(result.loc[result["method"].eq("global"), "mean_bw2"].iloc[0])
    result["bw_reduction_percent_vs_global"] = 100.0 * (1.0 - result["mean_bw2"] / global_bw2)
    return result.sort_values("mean_bw2").reset_index(drop=True)


def _selected_evaluations(scores: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    records = []
    selections: dict[str, Any] = {}
    tunable = [
        "positive_shrink", "graph_smooth", "piecewise",
        "segmented_polygon", "richardson_shrink",
    ]
    fixed = ["global", "positive_raw", "tangent_trend", "richardson_raw"]
    for assignment, tune_parity in (("A", 0), ("B", 1)):
        tuning = scores[scores["fold_parity"].eq(tune_parity)]
        evaluation = scores[scores["fold_parity"].eq(1 - tune_parity)]
        global_metrics = _metrics(evaluation[evaluation["family"].eq("global")])
        selected: dict[str, float] = {}
        candidates: list[tuple[str, str, float, pd.DataFrame]] = []
        for family in fixed:
            frame = evaluation[evaluation["family"].eq(family)]
            candidates.append((family, family, float(frame["parameter"].iloc[0]), frame))
        for family in tunable:
            means = tuning[tuning["family"].eq(family)].groupby("parameter")["bw2"].mean()
            parameter = float(means.idxmin())
            selected[family] = parameter
            frame = evaluation[
                evaluation["family"].eq(family)
                & np.isclose(evaluation["parameter"], parameter)
            ]
            candidates.append((f"selected_{family}", family, parameter, frame))
        for name, family, parameter, frame in candidates:
            values = _metrics(frame)
            records.append({
                "assignment": assignment,
                "tuning_fold_parity": tune_parity,
                "evaluation_fold_parity": 1 - tune_parity,
                "method": name,
                "family": family,
                "parameter": parameter,
                **values,
                "bw_reduction_percent_vs_global": 100.0 * (
                    1.0 - values["mean_bw2"] / global_metrics["mean_bw2"]
                ),
                "qlike_reduction_percent_vs_global": 100.0 * (
                    1.0 - values["mean_qlike"] / global_metrics["mean_qlike"]
                ),
            })
        selections[assignment] = selected
    return pd.DataFrame(records), selections


def _paired_bootstrap(
    scores: pd.DataFrame,
    evaluations: pd.DataFrame,
    selections: dict[str, Any],
    *,
    replicates: int,
    seed: int,
) -> pd.DataFrame:
    rows = []
    for assignment, tune_parity in (("A", 0), ("B", 1)):
        evaluation = scores[scores["fold_parity"].eq(1 - tune_parity)]
        global_fold = evaluation[evaluation["family"].eq("global")].groupby("fold")["bw2"].mean()
        chosen = evaluations[
            evaluations["assignment"].eq(assignment)
            & ~evaluations["family"].isin(["global", "richardson_raw"])
        ]
        for method_index, row in enumerate(chosen.itertuples()):
            frame = evaluation[evaluation["family"].eq(row.family)]
            if row.family in selections[assignment]:
                frame = frame[np.isclose(frame["parameter"], row.parameter)]
            candidate_fold = frame.groupby("fold")["bw2"].mean()
            common = global_fold.index.intersection(candidate_fold.index)
            differences = (global_fold.loc[common] - candidate_fold.loc[common]).to_numpy()
            rng = np.random.default_rng(seed + 1000 * (assignment == "B") + method_index)
            draws = rng.choice(differences, size=(replicates, differences.size), replace=True).mean(axis=1)
            rows.append({
                "assignment": assignment,
                "method": row.method,
                "family": row.family,
                "parameter": row.parameter,
                "evaluation_folds": int(differences.size),
                "improvement_percent": 100.0 * float(differences.mean()) / float(global_fold.loc[common].mean()),
                "ci95_lower_percent": 100.0 * float(np.quantile(draws, 0.025)) / float(global_fold.loc[common].mean()),
                "ci95_upper_percent": 100.0 * float(np.quantile(draws, 0.975)) / float(global_fold.loc[common].mean()),
                "probability_improvement": float(np.mean(draws > 0.0)),
            })
    return pd.DataFrame(rows)


def _plot(output: Path, evaluations: pd.DataFrame) -> None:
    display = evaluations[
        ~evaluations["family"].isin(["positive_raw", "richardson_raw", "richardson_shrink"])
    ].copy()
    methods = display["method"].drop_duplicates().tolist()
    fig, ax = plt.subplots(figsize=(10, 5.2))
    width = 0.36
    for offset, assignment, colour in (
        (-width / 2, "A", VIRIDIS(0.25)),
        (width / 2, "B", VIRIDIS(0.72)),
    ):
        values = display[display["assignment"].eq(assignment)].set_index("method")
        ax.bar(
            np.arange(len(methods)) + offset,
            values.loc[methods, "bw_reduction_percent_vs_global"],
            width=width,
            color=colour,
            label=f"calendar split {assignment}",
        )
    ax.axhline(0.0, color="0.3", linewidth=1)
    ax.set_xticks(
        np.arange(len(methods)),
        [name.replace("selected_", "").replace("_", " ") for name in methods],
        rotation=18,
        ha="right",
    )
    ax.set_ylabel("held-out BW error reduction vs global (%)")
    ax.set_title("Low-sample centre tournament")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output / "centre_tournament.png", dpi=180)
    fig.savefig(output / "centre_tournament.svg")
    plt.close(fig)


def analyze(
    config: dict[str, Any],
    panel: np.ndarray,
    output: Path,
    *,
    fold_count: int,
) -> None:
    with np.load(ROOT / config["experiment"]["panel_path"], allow_pickle=False) as source:
        months = source["months"].astype(str)
    rows = []
    diagnostics = []
    for fold in range(fold_count):
        arrays = _load_npz(output / f"fold_{fold:02d}.npz")
        rows.extend(_rows_for_fold(panel, months, fold, arrays, config["tournament"]))
        meta = json.loads((output / f"fold_{fold:02d}.meta.json").read_text(encoding="utf-8"))
        diagnostics.append({"fold": fold, "diagnostics": json.dumps(meta["diagnostics"], sort_keys=True)})
    scores = pd.DataFrame(rows).sort_values(["month_index", "method"]).reset_index(drop=True)
    if scores.isna().any().any():
        raise RuntimeError("centre tournament produced missing values")
    expected_rows = fold_count * int(config["tournament"]["holdout_block_months"]) * (
        4
        + 2 * len(config["tournament"]["shrinkage_lambdas"])
        + len(config["tournament"]["graph_strengths"])
        + 2 * len(config["tournament"]["piecewise_segments"])
    )
    if len(scores) != expected_rows:
        raise RuntimeError(f"expected {expected_rows} score rows, found {len(scores)}")

    summary = _all_fold_summary(scores)
    evaluations, selections = _selected_evaluations(scores)
    paired = _paired_bootstrap(
        scores,
        evaluations,
        selections,
        replicates=int(config["tournament"]["bootstrap_replicates"]),
        seed=int(config["tournament"]["bootstrap_seed"]),
    )
    scores.to_csv(output / "monthly_scores.csv", index=False)
    summary.to_csv(output / "method_summary.csv", index=False)
    evaluations.to_csv(output / "split_evaluation.csv", index=False)
    paired.to_csv(output / "paired_year_bootstrap.csv", index=False)
    pd.DataFrame(diagnostics).to_csv(output / "fold_diagnostics.csv", index=False)
    (output / "selections.json").write_text(
        json.dumps(selections, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    _plot(output, evaluations)

    lines = [
        "# APP-FIN low-sample centre tournament",
        "",
        "Twenty twelve-month blocks are omitted before every candidate is fitted. Each family is tuned on alternating calendar folds and evaluated on the opposite folds; the assignment is then reversed. Squared BW loss is primary.",
        "",
        "## Frozen split results",
        "",
        "| assignment | method | parameter | BW RMS | BW change vs global | mean QLIKE | max condition |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in evaluations.sort_values(["assignment", "mean_bw2"]).itertuples():
        lines.append(
            f"| {row.assignment} | {row.method} | {row.parameter:.3g} | {row.bw_rms:.4g} | {row.bw_reduction_percent_vs_global:+.1f}% | {row.mean_qlike:.4g} | {row.maximum_condition_number:.3g} |"
        )
    lines.extend([
        "",
        "## All-fold descriptive leaders",
        "",
        "| method | family | parameter | BW RMS | BW change vs global | min eigenvalue | max condition |",
        "|---|---|---:|---:|---:|---:|---:|",
    ])
    for row in summary.head(12).itertuples():
        lines.append(
            f"| {row.method} | {row.family} | {row.parameter:.3g} | {row.bw_rms:.4g} | {row.bw_reduction_percent_vs_global:+.1f}% | {row.minimum_eigenvalue:.3g} | {row.maximum_condition_number:.3g} |"
        )
    lines.extend([
        "",
        "## Interpretation rule",
        "",
        "A candidate is not promoted merely for the lowest pooled error. It must improve on the global centre in both frozen calendar assignments, avoid a materially worse spectral boundary, and have a paired block interval compatible with a real improvement. Full Richardson remains a negative control.",
        "",
        "See `monthly_scores.csv`, `method_summary.csv`, `split_evaluation.csv`, `paired_year_bootstrap.csv`, and `centre_tournament.png`.",
    ])
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    from run_centre_tournament import CONFIG_DEFAULT, _load_panel, load_configuration

    configuration = load_configuration(CONFIG_DEFAULT)
    data, _ = _load_panel(configuration)
    analyze(
        configuration,
        data,
        ROOT / configuration["output"]["directory"],
        fold_count=int(configuration["experiment"]["expected_months"])
        // int(configuration["tournament"]["holdout_block_months"]),
    )
