"""Analysis and plots for the APP-FIN centre-detectability diagnostic."""

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

from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402


VIRIDIS = plt.colormaps["viridis"]
COLOURS = {
    "global": "#525252",
    "positive": VIRIDIS(0.28),
    "richardson": VIRIDIS(0.72),
    "stability": "#d95f02",
}


def _load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as source:
        return {name: source[name].copy() for name in source.files}


def _geodesic_shrink(
    global_centre: np.ndarray,
    local_centres: np.ndarray,
    coefficient: float,
) -> np.ndarray:
    if coefficient == 0.0:
        return np.broadcast_to(global_centre, local_centres.shape).copy()
    if coefficient == 1.0:
        return local_centres.copy()
    displacement = BW_GEOMETRY.log(global_centre, local_centres)
    return BW_GEOMETRY.exp(global_centre, coefficient * displacement)


def _loss_rows(
    observations: np.ndarray,
    months: np.ndarray,
    fold: int,
    indices: np.ndarray,
    global_centre: np.ndarray,
    positive: np.ndarray,
    richardson: np.ndarray,
    full: dict[str, np.ndarray],
    lambdas: np.ndarray,
) -> list[dict[str, Any]]:
    truth = observations[indices]
    global_values = np.broadcast_to(global_centre, truth.shape)
    estimates: list[tuple[str, str, str, float, np.ndarray]] = [
        ("global", "global", "base", 0.0, global_values),
        ("positive_local", "positive", "base", 1.0, positive),
        ("richardson", "richardson", "base", 1.0, richardson),
    ]
    for family, local in (("positive", positive), ("richardson", richardson)):
        for coefficient in lambdas:
            estimates.append((
                f"{family}_shrink_{coefficient:.1f}",
                family,
                "shrink",
                float(coefficient),
                _geodesic_shrink(global_centre, local, float(coefficient)),
            ))

    full_global = np.broadcast_to(full["global_centre"], truth.shape)
    stability = {
        "global": BW_GEOMETRY.dist2(global_values, full_global),
        "positive": BW_GEOMETRY.dist2(positive, full["positive_centres"][indices]),
        "richardson": BW_GEOMETRY.dist2(
            richardson, full["richardson_centres"][indices]
        ),
    }
    rows = []
    truth_scale = np.maximum(frobenius_loss(np.zeros_like(truth), truth), 1e-300)
    for method, family, kind, coefficient, estimate in estimates:
        bw2 = bw_loss(estimate, truth)
        qlike = qlike_loss(estimate, truth)
        relative_frobenius2 = frobenius_loss(estimate, truth) / truth_scale
        displacement2 = (
            np.zeros(indices.size)
            if family == "global"
            else BW_GEOMETRY.dist2(global_values, estimate)
        )
        family_stability = stability.get(family, np.zeros(indices.size))
        for position, index in enumerate(indices):
            rows.append({
                "month_index": int(index),
                "month": str(months[index]),
                "fold": int(fold),
                "fold_parity": int(fold % 2),
                "method": method,
                "family": family,
                "kind": kind,
                "lambda": coefficient,
                "bw2": float(bw2[position]),
                "qlike": float(qlike[position]),
                "relative_frobenius2": float(relative_frobenius2[position]),
                "displacement_from_fold_global2": float(displacement2[position]),
                "crossfit_to_full_path2": float(family_stability[position]),
            })
    return rows


def _metrics(frame: pd.DataFrame) -> dict[str, float]:
    return {
        "bw_rms": float(np.sqrt(frame["bw2"].mean())),
        "mean_bw2": float(frame["bw2"].mean()),
        "mean_qlike": float(frame["qlike"].mean()),
        "relative_frobenius_rms": float(
            np.sqrt(frame["relative_frobenius2"].mean())
        ),
        "centre_displacement_rms": float(
            np.sqrt(frame["displacement_from_fold_global2"].mean())
        ),
        "crossfit_stability_rms": float(
            np.sqrt(frame["crossfit_to_full_path2"].mean())
        ),
    }


def _selected_evaluations(scores: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    records = []
    selections: dict[str, Any] = {}
    for assignment, tune_parity in (("A", 0), ("B", 1)):
        evaluation_parity = 1 - tune_parity
        tuning = scores[scores["fold_parity"].eq(tune_parity)]
        evaluation = scores[scores["fold_parity"].eq(evaluation_parity)]
        global_metrics = _metrics(
            evaluation[evaluation["method"].eq("global")]
        )
        assignment_selections = {}
        candidates = [
            ("global", evaluation[evaluation["method"].eq("global")], 0.0),
            (
                "positive_local",
                evaluation[evaluation["method"].eq("positive_local")],
                1.0,
            ),
            (
                "richardson",
                evaluation[evaluation["method"].eq("richardson")],
                1.0,
            ),
        ]
        for family in ("positive", "richardson"):
            tuning_family = tuning[
                tuning["family"].eq(family) & tuning["kind"].eq("shrink")
            ]
            means = tuning_family.groupby("lambda", sort=True)["bw2"].mean()
            selected_lambda = float(means.idxmin())
            chosen = evaluation[
                evaluation["family"].eq(family)
                & evaluation["kind"].eq("shrink")
                & np.isclose(evaluation["lambda"], selected_lambda)
            ]
            name = f"selected_{family}_shrink"
            assignment_selections[family] = selected_lambda
            candidates.append((name, chosen, selected_lambda))

        for name, frame, coefficient in candidates:
            values = _metrics(frame)
            records.append({
                "assignment": assignment,
                "tuning_fold_parity": tune_parity,
                "evaluation_fold_parity": evaluation_parity,
                "method": name,
                "lambda": coefficient,
                **values,
                "bw_error_reduction_percent_vs_global": 100.0 * (
                    1.0 - values["mean_bw2"] / global_metrics["mean_bw2"]
                ),
                "qlike_reduction_percent_vs_global": 100.0 * (
                    1.0 - values["mean_qlike"] / global_metrics["mean_qlike"]
                ),
            })
        selections[assignment] = assignment_selections
    return pd.DataFrame(records), selections


def _paired_fold_bootstrap(
    scores: pd.DataFrame,
    evaluations: pd.DataFrame,
    selections: dict[str, Any],
    *,
    replicates: int = 20000,
    seed: int = 20260826,
) -> pd.DataFrame:
    records = []
    for assignment, tune_parity in (("A", 0), ("B", 1)):
        evaluation = scores[scores["fold_parity"].eq(1 - tune_parity)]
        method_specs = [
            ("positive_local", "positive", "base", 1.0),
            ("richardson", "richardson", "base", 1.0),
            (
                "selected_positive_shrink",
                "positive",
                "shrink",
                selections[assignment]["positive"],
            ),
            (
                "selected_richardson_shrink",
                "richardson",
                "shrink",
                selections[assignment]["richardson"],
            ),
        ]
        global_rows = evaluation[evaluation["method"].eq("global")]
        for method_index, (name, family, kind, coefficient) in enumerate(method_specs):
            candidate = evaluation[
                evaluation["family"].eq(family)
                & evaluation["kind"].eq(kind)
                & np.isclose(evaluation["lambda"], coefficient)
            ]
            for metric in ("bw2", "qlike"):
                global_fold = global_rows.groupby("fold")[metric].mean()
                candidate_fold = candidate.groupby("fold")[metric].mean()
                common = global_fold.index.intersection(candidate_fold.index)
                differences = (
                    global_fold.loc[common] - candidate_fold.loc[common]
                ).to_numpy()
                rng = np.random.default_rng(
                    seed + 1000 * (assignment == "B") + 10 * method_index + (metric == "qlike")
                )
                draws = rng.choice(
                    differences, size=(replicates, differences.size), replace=True
                ).mean(axis=1)
                global_mean = float(global_fold.loc[common].mean())
                records.append({
                    "assignment": assignment,
                    "method": name,
                    "lambda": coefficient,
                    "metric": metric,
                    "evaluation_folds": int(differences.size),
                    "mean_improvement": float(differences.mean()),
                    "improvement_percent": 100.0 * float(differences.mean()) / global_mean,
                    "ci95_lower": float(np.quantile(draws, 0.025)),
                    "ci95_upper": float(np.quantile(draws, 0.975)),
                    "bootstrap_probability_improvement": float(np.mean(draws > 0.0)),
                })
    return pd.DataFrame(records)


def _constant_centre_null(
    full: dict[str, np.ndarray],
    observations: np.ndarray,
    output: Path,
    expected_replicates: int,
    required: bool,
) -> tuple[pd.DataFrame, dict[str, float]]:
    reference = np.broadcast_to(full["global_centre"], observations.shape)
    observed_movement = float(
        np.mean(BW_GEOMETRY.dist2(reference, full["positive_centres"]))
    )
    observed_residual = float(
        np.mean(BW_GEOMETRY.dist2(full["positive_centres"], observations))
    )
    records = []
    directory = output / "constant_centre_bootstrap"
    for path in sorted(directory.glob("replicate_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        records.append({
            key: value for key, value in payload.items()
            if key not in {"digest"}
        })
    if required and len(records) != expected_replicates:
        raise RuntimeError(
            f"constant-centre bootstrap has {len(records)} rows; expected {expected_replicates}"
        )
    table = pd.DataFrame(records)
    if table.empty:
        return table, {
            "observed_movement_energy": observed_movement,
            "observed_residual_energy": observed_residual,
            "observed_movement_to_residual": observed_movement / observed_residual,
        }
    null_values = table["movement_energy"].to_numpy(dtype=float)
    return table, {
        "observed_movement_energy": observed_movement,
        "observed_residual_energy": observed_residual,
        "observed_movement_to_residual": observed_movement / observed_residual,
        "null_movement_median": float(np.median(null_values)),
        "null_movement_p95": float(np.quantile(null_values, 0.95)),
        "constant_centre_p_value": float(
            (1 + np.sum(null_values >= observed_movement)) / (1 + null_values.size)
        ),
        "constant_centre_replicates": int(null_values.size),
    }


def _method_summary(scores: pd.DataFrame) -> pd.DataFrame:
    records = []
    global_metrics = _metrics(scores[scores["method"].eq("global")])
    for (method, family, kind, coefficient), frame in scores.groupby(
        ["method", "family", "kind", "lambda"], sort=False
    ):
        values = _metrics(frame)
        records.append({
            "method": method,
            "family": family,
            "kind": kind,
            "lambda": coefficient,
            **values,
            "bw_error_reduction_percent_vs_global": 100.0 * (
                1.0 - values["mean_bw2"] / global_metrics["mean_bw2"]
            ),
            "qlike_reduction_percent_vs_global": 100.0 * (
                1.0 - values["mean_qlike"] / global_metrics["mean_qlike"]
            ),
        })
    return pd.DataFrame(records)


def _fold_summary(scores: pd.DataFrame) -> pd.DataFrame:
    base = scores[scores["method"].isin(["global", "positive_local", "richardson"])]
    grouped = base.groupby(["fold", "method"], sort=True)["bw2"].mean().unstack()
    result = grouped.reset_index()
    for method in ("positive_local", "richardson"):
        result[f"{method}_error_reduction_percent"] = 100.0 * (
            1.0 - result[method] / result["global"]
        )
    return result


def _style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 180,
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def _save(fig: Any, output: Path, name: str) -> None:
    fig.tight_layout()
    fig.savefig(output / f"{name}.png", bbox_inches="tight")
    fig.savefig(output / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def _plots(
    output: Path,
    scores: pd.DataFrame,
    summary: pd.DataFrame,
    folds: pd.DataFrame,
    evaluations: pd.DataFrame,
    full: dict[str, np.ndarray],
    months: np.ndarray,
) -> None:
    _style()
    fig, ax = plt.subplots(figsize=(8, 4.8))
    shrink = summary[summary["kind"].eq("shrink")]
    for family, colour, label in (
        ("positive", COLOURS["positive"], "positive local"),
        ("richardson", COLOURS["richardson"], "Richardson"),
    ):
        values = shrink[shrink["family"].eq(family)].sort_values("lambda")
        ax.plot(
            values["lambda"], values["bw_error_reduction_percent_vs_global"],
            marker="o", color=colour, label=label,
        )
    ax.axhline(0.0, color="0.4", linewidth=1)
    ax.set(
        xlabel="fraction of local movement retained",
        ylabel="held-out BW error reduction vs global (%)",
        title="How much centre movement should survive?",
    )
    ax.legend(frameon=False)
    _save(fig, output, "shrinkage_curve")

    fig, ax = plt.subplots(figsize=(10, 4.8))
    x = np.arange(len(folds))
    ax.plot(
        x, folds["positive_local_error_reduction_percent"], marker="o",
        color=COLOURS["positive"], label="positive local",
    )
    ax.plot(
        x, folds["richardson_error_reduction_percent"], marker="o",
        color=COLOURS["richardson"], label="Richardson",
    )
    ax.axhline(0.0, color="0.35", linewidth=1)
    ax.set(
        xlabel="held-out year (chronological)",
        ylabel="BW error reduction vs global (%)",
        title="Does the moving centre help consistently?",
    )
    first_month_by_fold = (
        scores[scores["method"].eq("global")]
        .groupby("fold", sort=True)["month"]
        .min()
    )
    year_labels = [
        str(first_month_by_fold.loc[int(fold)])[:4]
        for fold in folds["fold"]
    ]
    ax.set_xticks(x, year_labels, rotation=45)
    ax.legend(frameon=False)
    _save(fig, output, "annual_holdout_effects")

    global_values = np.broadcast_to(full["global_centre"], full["positive_centres"].shape)
    positive_motion = np.sqrt(BW_GEOMETRY.dist2(global_values, full["positive_centres"]))
    richardson_motion = np.sqrt(BW_GEOMETRY.dist2(global_values, full["richardson_centres"]))
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(months, positive_motion, color=COLOURS["positive"], label="positive local")
    ax.plot(months, richardson_motion, color=COLOURS["richardson"], label="Richardson")
    ticks = np.linspace(0, len(months) - 1, 9, dtype=int)
    ax.set_xticks(ticks, months[ticks], rotation=30, ha="right")
    ax.set(
        xlabel="month", ylabel="BW distance from global centre",
        title="Full-sample centre movement",
    )
    ax.legend(frameon=False)
    _save(fig, output, "centre_motion_paths")

    display = evaluations[
        evaluations["method"].isin([
            "positive_local", "richardson", "selected_positive_shrink",
            "selected_richardson_shrink",
        ])
    ].copy()
    fig, ax = plt.subplots(figsize=(9, 4.8))
    methods = display["method"].drop_duplicates().tolist()
    width = 0.36
    for offset, assignment in ((-width / 2, "A"), (width / 2, "B")):
        values = display[display["assignment"].eq(assignment)].set_index("method")
        ax.bar(
            np.arange(len(methods)) + offset,
            values.loc[methods, "bw_error_reduction_percent_vs_global"],
            width=width,
            label=f"calendar split {assignment}",
            color=VIRIDIS(0.30 if assignment == "A" else 0.72),
        )
    ax.axhline(0.0, color="0.35", linewidth=1)
    ax.set_xticks(
        np.arange(len(methods)),
        [name.replace("selected_", "").replace("_", " ") for name in methods],
        rotation=18,
        ha="right",
    )
    ax.set(
        ylabel="evaluation BW error reduction vs global (%)",
        title="Frozen shrinkage on the opposite calendar years",
    )
    ax.legend(frameon=False)
    _save(fig, output, "evaluation_verdict")


def _verdict(evaluations: pd.DataFrame, null_summary: dict[str, float]) -> str:
    best = {}
    for assignment in ("A", "B"):
        subset = evaluations[evaluations["assignment"].eq(assignment)]
        row = subset.loc[subset["mean_bw2"].idxmin()]
        best[assignment] = (str(row["method"]), float(row["lambda"]), float(row["bw_error_reduction_percent_vs_global"]))
    null_p = null_summary.get("constant_centre_p_value")
    if best["A"][0] == "global" and best["B"][0] == "global":
        return "No held-out evidence that a moving centre improves on one global BW centre."
    def conceptual_family(method: str) -> str:
        if method in {"positive_local", "selected_positive_shrink"}:
            return "positive"
        if method in {"richardson", "selected_richardson_shrink"}:
            return "richardson"
        return method

    family_a = conceptual_family(best["A"][0])
    family_b = conceptual_family(best["B"][0])
    if family_a != family_b or min(best["A"][2], best["B"][2]) <= 0.0:
        return "The preferred centre construction is calendar-sensitive; no stable moving-centre verdict is available."
    null_clause = (
        "The constant-centre block null is also rejected."
        if null_p is not None and null_p <= 0.05
        else "The constant-centre block null is not rejected at 5%, so this remains predictive sensitivity rather than detected structural motion."
    )
    if best["A"][0] == "positive_local" and best["B"][0] == "positive_local":
        return "Positive local centres are stable winners; movement is useful but Richardson adds excess variance. " + null_clause
    if best["A"][0] == "richardson" and best["B"][0] == "richardson":
        return "The full Richardson centre is the stable held-out winner. " + null_clause
    return "A partially shrunk moving centre is the stable held-out winner; detectable movement should not be used at full strength. " + null_clause


def analyze(
    root: Path,
    config: dict[str, Any],
    panel: dict[str, np.ndarray],
    output: Path,
    *,
    require_bootstrap: bool = True,
    fold_count: int | None = None,
    bootstrap_replicates: int | None = None,
) -> None:
    observations = np.asarray(panel["panel"], dtype=float)
    months = panel["months"].astype(str)
    full = _load_npz(output / "full_fit.npz")
    lambdas = np.asarray(config["diagnostic"]["shrinkage_lambdas"], dtype=float)
    block = int(config["diagnostic"]["holdout_block_months"])
    expected_folds = (
        observations.shape[0] // block if fold_count is None else int(fold_count)
    )
    rows = []
    fold_diagnostics = []
    for fold in range(expected_folds):
        path = output / "folds" / f"fold_{fold:02d}.npz"
        meta_path = output / "folds" / f"fold_{fold:02d}.meta.json"
        if not path.is_file() or not meta_path.is_file():
            raise RuntimeError(f"missing completed centre diagnostic fold {fold}")
        values = _load_npz(path)
        rows.extend(_loss_rows(
            observations,
            months,
            fold,
            values["indices"].astype(int),
            values["global_centre"],
            values["positive_centres"],
            values["richardson_centres"],
            full,
            lambdas,
        ))
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        fold_diagnostics.append({"fold": fold, **meta["diagnostics"]})
    scores = pd.DataFrame(rows).sort_values(["month_index", "method"]).reset_index(drop=True)
    summary = _method_summary(scores)
    folds = _fold_summary(scores)
    evaluations, selections = _selected_evaluations(scores)
    paired = _paired_fold_bootstrap(scores, evaluations, selections)
    null_table, null_summary = _constant_centre_null(
        full,
        observations,
        output,
        (
            int(config["diagnostic"]["bootstrap_replicates"])
            if bootstrap_replicates is None
            else int(bootstrap_replicates)
        ),
        require_bootstrap,
    )
    diagnostics = pd.DataFrame(fold_diagnostics)

    scores.to_csv(output / "monthly_scores.csv", index=False)
    summary.to_csv(output / "method_summary.csv", index=False)
    folds.to_csv(output / "annual_holdout_effects.csv", index=False)
    evaluations.to_csv(output / "split_evaluation.csv", index=False)
    paired.to_csv(output / "paired_year_bootstrap.csv", index=False)
    diagnostics.to_csv(output / "fold_diagnostics.csv", index=False)
    if not null_table.empty:
        null_table.to_csv(output / "constant_centre_bootstrap.csv", index=False)
    (output / "diagnostics.json").write_text(
        json.dumps({"selections": selections, "constant_centre_null": null_summary}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    _plots(output, scores, summary, folds, evaluations, full, months)

    global_all = summary[summary["method"].eq("global")].iloc[0]
    positive_all = summary[summary["method"].eq("positive_local")].iloc[0]
    richardson_all = summary[summary["method"].eq("richardson")].iloc[0]
    verdict = _verdict(evaluations, null_summary)
    lines = [
        "# APP-FIN centre-detectability diagnostic",
        "",
        "## Scope",
        "",
        "Each twelve-month block is omitted before its global centre, positive-local vertices, Richardson vertices, and polygon are fitted. The omitted months are then interpolated from that cross-fitted polygon. This is a centre-estimation diagnostic, not a causal forecast: observations on both sides of a held-out year remain available.",
        "",
        "Shrinkage is protected from same-sample tuning by alternating calendar years. Split A tunes on even-numbered folds and evaluates on odd folds; split B reverses the assignment. QLIKE and relative Frobenius losses are sensitivity analyses with different conditional-mean targets; squared BW is the primary loss for the BW Fréchet centre.",
        "",
        "## Automatic verdict",
        "",
        f"**{verdict}**",
        "",
        "## All-fold cross-fitted description",
        "",
        f"- global-centre BW RMS: **{global_all['bw_rms']:.4g}**",
        f"- positive-local BW RMS: **{positive_all['bw_rms']:.4g}**; error change **{positive_all['bw_error_reduction_percent_vs_global']:+.1f}%** (positive is better)",
        f"- Richardson BW RMS: **{richardson_all['bw_rms']:.4g}**; error change **{richardson_all['bw_error_reduction_percent_vs_global']:+.1f}%**",
        f"- positive-local cross-fit/full-path discrepancy RMS: **{positive_all['crossfit_stability_rms']:.4g}**",
        f"- Richardson cross-fit/full-path discrepancy RMS: **{richardson_all['crossfit_stability_rms']:.4g}**",
        "",
        "## Frozen alternating-split results",
        "",
    ]
    for assignment in ("A", "B"):
        selected = evaluations[
            evaluations["assignment"].eq(assignment)
            & evaluations["method"].str.startswith("selected_")
        ]
        lines.append(
            f"- split {assignment}: positive-family lambda **{selections[assignment]['positive']:.1f}**, Richardson-family lambda **{selections[assignment]['richardson']:.1f}**; evaluation BW changes "
            + ", ".join(
                f"{row.method.replace('selected_', '')} **{row.bw_error_reduction_percent_vs_global:+.1f}%**"
                for row in selected.itertuples()
            )
        )
    lines.extend([
        "",
        "## Constant-centre null",
        "",
        f"- observed positive-local movement energy: **{null_summary['observed_movement_energy']:.4g}**",
        f"- movement/residual-energy ratio: **{null_summary['observed_movement_to_residual']:.3f}**",
    ])
    if "constant_centre_p_value" in null_summary:
        lines.extend([
            f"- null median and 95th percentile: **{null_summary['null_movement_median']:.4g}**, **{null_summary['null_movement_p95']:.4g}**",
            f"- fixed-block bootstrap p-value: **{null_summary['constant_centre_p_value']:.3f}** from **{int(null_summary['constant_centre_replicates'])}** replicates",
        ])
    else:
        lines.append("- bootstrap was skipped; no constant-centre test is reported")
    lines.extend([
        "",
        "The null resamples twelve-month blocks of global-centre BW residuals and maps them back at one fixed centre. It preserves within-block dependence while deliberately destroying deterministic centre motion. It is an application diagnostic, not a theorem-level test under every form of long memory or covariance-proxy error.",
        "",
        "## Why full Richardson can overcorrect",
        "",
        "The weights `(1/3, -2, 8/3)` exactly cancel the first two formal bandwidth-bias powers, but their absolute mass is five. They therefore extrapolate rather than average: noise and disagreement among the nested stages are amplified, and the largest coefficient multiplies the narrowest, noisiest stage. The annual holdouts reduce the minimum effective local sample size to the value reported below. BW curvature and noncommutation can add anchor/Log/Exp disagreement even when every positive mean converges.",
        "",
        "With three scales and two exact cancellation constraints plus preservation of the centre, the coefficients are unique once the scale ratio is fixed. Different coefficients are not a free repair. Changing the scale ratio moves the trade-off between extrapolation conditioning and the smallest window; using four or more scales permits minimum-variance weights under the same constraints. Damping or positive-local estimation lowers variance but restores some lower-order bias and therefore requires a new rate statement before replacing the proved estimator.",
        "",
        "Paper 1 records this as a finite-sample APP-FIN scope boundary, not a disproof of the asymptotic theorem. Scale/kernel/extra-scale design, causal regularisation, and higher-frequency panels are routed to the fixed-loading application follow-up.",
        "",
        "## Numerical health",
        "",
        f"- Richardson fallbacks across annual fits: **{int(diagnostics['fallback_count'].sum())}**",
        f"- nonconverged three-scale means: **{int(diagnostics['nonconverged_stage_count'].sum())}**",
        f"- effective local sample-size range: **{diagnostics['effective_sample_size_min'].min():.1f}--{diagnostics['effective_sample_size_max'].max():.1f}**",
        "",
        "See `method_summary.csv`, `split_evaluation.csv`, `paired_year_bootstrap.csv`, `annual_holdout_effects.csv`, `constant_centre_bootstrap.csv`, and the four figures beside this report.",
    ])
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    from run_appfin_centre_diagnostic import load_configuration
    from run_appfin_identification import load_panel

    configuration = load_configuration(ROOT / "config" / "appfin_centre_diagnostic.yaml")
    analyze(
        ROOT,
        configuration,
        load_panel(configuration),
        ROOT / configuration["output"]["directory"],
    )
