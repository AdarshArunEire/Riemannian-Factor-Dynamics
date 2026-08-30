"""Plain-language plots for the recorded APP-HF-4 forecast comparison."""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "py"))

from experiments.run_hf4_forecast import newey_west_mean_interval  # noqa: E402


OUTPUT = ROOT / "results" / "intermediate" / "hf4_crypto_forecast"
METHODS = ["locf", "ewma", "loghar_spd", "parent_rfm", "rfd_piecewise6"]
LABELS = {
    "locf": "Last observation",
    "ewma": "EWMA",
    "loghar_spd": "Log-HAR",
    "parent_rfm": "Parent RFM",
    "rfd_piecewise6": "RFD",
}
METRICS = {
    "frobenius2": "Frobenius error",
    "qlike": "QLIKE",
    "bw2": "Bures–Wasserstein error",
    "gmv_realized_variance": "Portfolio realised variance",
}


def _headline(raw: pd.DataFrame) -> pd.DataFrame:
    selected = raw[
        ((raw["rank"] == 0) & (raw["head"] == "native"))
        | ((raw["rank"] == 19) & (raw["head"] == "var1"))
    ].copy()
    if len(selected) != 8760 * len(METHODS):
        raise RuntimeError("HF-4 headline rows are incomplete")
    if set(selected["method"]) != set(METHODS):
        raise RuntimeError("HF-4 headline method set changed")
    return selected


def _finish(axis: plt.Axes) -> None:
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)
    axis.grid(axis="x", alpha=0.18)


def plot_scorecard(headline: pd.DataFrame) -> None:
    means = headline.groupby("method")[list(METRICS)].mean()
    colours = dict(zip(METHODS, plt.cm.viridis(np.linspace(0.08, 0.88, len(METHODS)))))
    figure, axes = plt.subplots(2, 2, figsize=(12, 8.2))
    for axis, (metric, title) in zip(axes.flat, METRICS.items()):
        values = means[metric]
        excess = 100.0 * (values / values.min() - 1.0)
        order = excess.sort_values().index
        bars = axis.barh(
            [LABELS[item] for item in order],
            excess.loc[order],
            color=[colours[item] for item in order],
        )
        axis.invert_yaxis()
        axis.set_title(title)
        axis.set_xlabel("more error than the best method (%)")
        axis.set_xlim(left=0.0)
        for bar, value in zip(bars, excess.loc[order]):
            axis.text(
                value + max(excess.max(), 1.0) * 0.015,
                bar.get_y() + bar.get_height() / 2,
                "best" if abs(value) < 1e-12 else f"+{value:.1f}%",
                va="center",
                fontsize=9,
            )
        _finish(axis)
    figure.suptitle("Classical methods lead; RFD still beats parent RFM", fontsize=16)
    figure.tight_layout()
    figure.savefig(OUTPUT / "simple_forecaster_scorecard.png", dpi=180, bbox_inches="tight")
    plt.close(figure)


def plot_rfd_vs_parent(headline: pd.DataFrame) -> pd.DataFrame:
    indexed = {
        method: headline[headline["method"] == method].set_index("target_hour")
        for method in ("parent_rfm", "rfd_piecewise6")
    }
    parent = indexed["parent_rfm"]
    rfd = indexed["rfd_piecewise6"].loc[parent.index]
    rows = []
    for metric, label in METRICS.items():
        interval = newey_west_mean_interval(
            (rfd[metric] - parent[metric]).to_numpy(dtype=float), 168
        )
        scale = float(parent[metric].mean())
        rows.append({
            "metric": metric,
            "label": label,
            "improvement_percent": 100.0 * (1.0 - rfd[metric].mean() / scale),
            "ci95_lower_percent": -100.0 * interval["ci95_upper"] / scale,
            "ci95_upper_percent": -100.0 * interval["ci95_lower"] / scale,
        })
    comparison = pd.DataFrame(rows)
    y = np.arange(len(comparison))
    value = comparison["improvement_percent"].to_numpy()
    lower = comparison["ci95_lower_percent"].to_numpy()
    upper = comparison["ci95_upper_percent"].to_numpy()
    figure, axis = plt.subplots(figsize=(10, 5.4))
    axis.errorbar(
        value,
        y,
        xerr=np.vstack((value - lower, upper - value)),
        fmt="o",
        markersize=9,
        color=plt.cm.viridis(0.62),
        ecolor="#777777",
        capsize=5,
        linewidth=2,
    )
    axis.axvline(0.0, color="black", linewidth=1)
    axis.set_yticks(y, comparison["label"])
    axis.invert_yaxis()
    axis.set_xlabel("RFD error reduction versus parent RFM (%)")
    axis.set_title("RFD averages are better; uncertainty still says tie")
    for index, point in enumerate(value):
        axis.text(point + 0.55, index, f"{point:+.1f}%", va="center", fontsize=10)
    _finish(axis)
    figure.tight_layout()
    figure.savefig(OUTPUT / "simple_rfd_vs_rfm.png", dpi=180, bbox_inches="tight")
    plt.close(figure)
    return comparison


def plot_block_consistency(headline: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for metric in ("frobenius2", "qlike"):
        means = headline.groupby(["block", "method"])[metric].mean().unstack()
        improvement = 100.0 * (
            1.0 - means["rfd_piecewise6"] / means["parent_rfm"]
        )
        rows.extend(
            {"block": int(block), "metric": metric, "improvement_percent": float(value)}
            for block, value in improvement.items()
        )
    frame = pd.DataFrame(rows)
    figure, axes = plt.subplots(2, 1, figsize=(11, 6.8), sharex=True)
    for axis, metric in zip(axes, ("frobenius2", "qlike")):
        selected = frame[frame["metric"] == metric]
        values = selected["improvement_percent"].to_numpy()
        colours = np.where(values >= 0.0, "#2A9D8F", "#D95F59")
        axis.bar(selected["block"] + 1, values, color=colours, width=0.78)
        axis.axhline(0.0, color="black", linewidth=0.9)
        axis.set_ylabel("RFD improvement (%)")
        axis.set_title(METRICS[metric])
        axis.grid(axis="y", alpha=0.18)
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)
    axes[-1].set_xlabel("four-week evaluation block (block 14 contains 24 hours)")
    axes[-1].set_xticks(np.arange(1, 15))
    figure.suptitle("RFD versus parent RFM changes across the year", fontsize=15)
    figure.tight_layout()
    figure.savefig(OUTPUT / "simple_rfd_rfm_by_block.png", dpi=180, bbox_inches="tight")
    plt.close(figure)
    return frame


def plot_average_versus_typical(headline: pd.DataFrame) -> pd.DataFrame:
    parent = headline[headline["method"] == "parent_rfm"]
    rfd = headline[headline["method"] == "rfd_piecewise6"]
    rows = []
    for metric, label in METRICS.items():
        rows.append({
            "metric": metric,
            "label": label,
            "annual average": 100.0 * (1.0 - rfd[metric].mean() / parent[metric].mean()),
            "typical hour": 100.0 * (1.0 - rfd[metric].median() / parent[metric].median()),
        })
    frame = pd.DataFrame(rows)
    y = np.arange(len(frame))
    figure, axis = plt.subplots(figsize=(10.5, 5.4))
    width = 0.34
    axis.barh(
        y - width / 2,
        frame["annual average"],
        height=width,
        label="full-year average",
        color=plt.cm.viridis(0.68),
    )
    axis.barh(
        y + width / 2,
        frame["typical hour"],
        height=width,
        label="typical hour (median)",
        color=plt.cm.viridis(0.22),
    )
    axis.axvline(0.0, color="black", linewidth=0.9)
    axis.set_yticks(y, frame["label"])
    axis.invert_yaxis()
    axis.set_xlabel("RFD error reduction versus parent RFM (%)")
    axis.set_title("RFD's gain comes from difficult regimes, not the typical hour")
    axis.legend(frameon=False, ncol=2, loc="lower right")
    _finish(axis)
    figure.tight_layout()
    figure.savefig(OUTPUT / "simple_average_vs_typical.png", dpi=180, bbox_inches="tight")
    plt.close(figure)
    return frame


def plot_rank_curve() -> None:
    ranks = pd.read_csv(OUTPUT / "rank_sensitivity.csv")
    figure, axes = plt.subplots(1, 3, figsize=(17, 5.2), sharey=True)
    colours = plt.cm.viridis(np.linspace(0.15, 0.82, 3))
    for axis, head in zip(axes, ("var1", "har_ols", "vhar_ridge")):
        selected = ranks[ranks["head"] == head]
        for colour, (metric, label) in zip(
            colours,
            (("frobenius2", "Frobenius"), ("qlike", "QLIKE"), ("bw2", "Bures–Wasserstein")),
        ):
            axis.plot(
                selected["rank"],
                selected[f"rfd_reduction_percent_{metric}"],
                marker="o", linewidth=2, label=label, color=colour,
            )
        axis.axhline(0.0, color="black", linewidth=0.9)
        axis.set_xticks(selected["rank"])
        axis.set_xlabel("retained rank")
        axis.set_title(head.upper())
        axis.grid(alpha=0.18)
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)
    axes[0].set_ylabel("RFD error reduction versus same-rank RFM (%)")
    axes[0].legend(frameon=False, ncol=3, loc="upper left")
    figure.suptitle("The RFD advantage depends on rank, loss and score head")
    figure.tight_layout()
    figure.savefig(OUTPUT / "simple_rank_sensitivity.png", dpi=180, bbox_inches="tight")
    plt.close(figure)


def plot_absolute_rank_curves() -> None:
    summary = pd.read_csv(OUTPUT / "performance.csv")
    represented = summary[summary["method"].isin(("parent_rfm", "rfd_piecewise6"))]
    colours = {"var1": "#31688E", "har_ols": "#35B779", "vhar_ridge": "#E69F00"}
    labels = {"var1": "VAR(1)", "har_ols": "coordinate OLS HAR", "vhar_ridge": "ridge VHAR"}
    figure, axes = plt.subplots(1, 2, figsize=(13.5, 5.2))
    for axis, metric, title, baseline_method in (
        (axes[0], "mean_frobenius2", "Frobenius error", "loghar_spd"),
        (axes[1], "mean_qlike", "QLIKE", "ewma"),
    ):
        for head in ("var1", "har_ols", "vhar_ridge"):
            for method, linestyle, suffix in (
                ("parent_rfm", "--", "parent"),
                ("rfd_piecewise6", "-", "RFD"),
            ):
                selected = represented[
                    (represented["method"] == method) & (represented["head"] == head)
                ].sort_values("rank")
                axis.plot(
                    selected["rank"], selected[metric], color=colours[head],
                    linestyle=linestyle, linewidth=2,
                    label=f"{labels[head]} — {suffix}",
                )
        baseline = float(summary[summary["method"] == baseline_method][metric].iloc[0])
        axis.axhline(baseline, color="black", linewidth=1.4, label=baseline_method.replace("_", " "))
        axis.set(xlabel="retained rank", ylabel=title, title=title, xticks=range(1, 20, 2))
        axis.grid(alpha=0.18)
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)
    axes[0].legend(frameon=False, fontsize=8, ncol=2)
    figure.suptitle("HAR improves magnitude error; extra rank can damage QLIKE", fontsize=15)
    figure.tight_layout()
    figure.savefig(OUTPUT / "simple_absolute_rank_heads.png", dpi=180, bbox_inches="tight")
    plt.close(figure)


def plot_rank1_scorecard() -> None:
    summary = pd.read_csv(OUTPUT / "performance.csv")
    selected = summary[
        (summary["rank"] == 0)
        | ((summary["rank"] == 1) & summary["method"].isin(("parent_rfm", "rfd_piecewise6")))
    ].copy()
    selected["label"] = np.where(
        selected["rank"] == 0,
        selected["method"].replace(LABELS),
        np.where(selected["method"] == "rfd_piecewise6", "RFD — ", "Parent — ")
        + selected["head"].replace({
            "var1": "VAR(1)", "har_ols": "scalar OLS HAR", "vhar_ridge": "scalar ridge HAR"
        }),
    )
    figure, axes = plt.subplots(1, 2, figsize=(13.5, 6.2))
    for axis, metric, title in (
        (axes[0], "mean_frobenius2", "Frobenius error"),
        (axes[1], "mean_qlike", "QLIKE"),
    ):
        ordered = selected.sort_values(metric, ascending=True)
        best = float(ordered[metric].iloc[0])
        excess = 100.0 * (ordered[metric] / best - 1.0)
        bars = axis.barh(ordered["label"], excess, color=plt.cm.viridis(np.linspace(0.2, 0.85, len(ordered))))
        axis.invert_yaxis()
        axis.set(xlabel="more error than the best method (%)", title=title, xlim=(0, None))
        for bar, value in zip(bars, excess):
            axis.text(value + 0.25, bar.get_y() + bar.get_height() / 2, "best" if value < 1e-10 else f"+{value:.1f}%", va="center", fontsize=8)
        axis.grid(axis="x", alpha=0.18)
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)
    figure.suptitle("One persistent score is already competitive", fontsize=15)
    figure.tight_layout()
    figure.savefig(OUTPUT / "simple_rank1_scorecard.png", dpi=180, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    raw = pd.read_csv(OUTPUT / "hourly_losses.csv")
    headline = _headline(raw)
    plot_scorecard(headline)
    comparison = plot_rfd_vs_parent(headline)
    blocks = plot_block_consistency(headline)
    typical = plot_average_versus_typical(headline)
    plot_rank_curve()
    plot_absolute_rank_curves()
    plot_rank1_scorecard()
    comparison.to_csv(OUTPUT / "simple_rfd_vs_rfm.csv", index=False)
    blocks.to_csv(OUTPUT / "simple_rfd_rfm_by_block.csv", index=False)
    typical.to_csv(OUTPUT / "simple_average_vs_typical.csv", index=False)
    print(f"Wrote simple HF-4 plots to {OUTPUT}")


if __name__ == "__main__":
    main()
