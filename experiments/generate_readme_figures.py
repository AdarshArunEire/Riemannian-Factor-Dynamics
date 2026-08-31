"""Generate the public README figures from small, tracked result extracts.

Run from any directory: python experiments/generate_readme_figures.py
No raw market data, R installation or intermediate experiment caches are needed.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "figures" / "readme"
GREEN = "#147D64"
NAVY = "#344A76"
RUST = "#B65D3C"
INK = "#232A2D"
GREY = "#7E898E"
GRID = "#E4E7E5"
METRICS = {
    "frobenius2": "Squared Frobenius error",
    "qlike": "QLIKE",
    "bw2": "Squared Bures–Wasserstein error",
    "gmv_realized_variance": "Portfolio realised variance",
}
METHODS = {
    "locf": "Last observation",
    "ewma": "EWMA",
    "loghar_spd": "Log-HAR",
    "parent_rfm": "Parent RFM",
    "rfd_piecewise6": "RFD",
}


def style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "text.color": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.edgecolor": GREY,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.titleweight": "bold",
        "svg.fonttype": "none",
        "svg.hashsalt": "rfd-readme",
        "savefig.facecolor": "white",
    })


def finish(fig, filename: str) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for suffix in ("png", "svg"):
        metadata = {"Date": None} if suffix == "svg" else {}
        fig.savefig(OUTPUT / f"{filename}.{suffix}", dpi=180,
                    bbox_inches="tight", metadata=metadata)
    plt.close(fig)
    print(f"Wrote {OUTPUT.relative_to(ROOT) / filename} (PNG + SVG)")


def arrow(axis, y: float, value: float, colour: str, *, label: str,
          offset: float = 7, linewidth: float = 2.5) -> None:
    """A zero-anchored comparison, with its endpoint labelled directly."""
    if abs(value) > 0.15:
        axis.annotate("", xy=(value, y), xytext=(0, y),
                      arrowprops={"arrowstyle": "-|>", "color": colour,
                                  "lw": linewidth, "mutation_scale": 13,
                                  "shrinkA": 0, "shrinkB": 0})
    else:
        axis.plot(value, y, "o", color=colour, ms=4)
    axis.annotate(label, (value, y), xytext=(offset if value >= 0 else -offset, 0),
                  textcoords="offset points", va="center",
                  ha="left" if value >= 0 else "right", color=colour,
                  fontsize=11, fontweight="bold")


def grid(axis) -> None:
    axis.set_axisbelow(True)
    axis.grid(axis="x", color=GRID, linewidth=0.8)
    axis.tick_params(axis="y", length=0, pad=9)
    axis.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))


def synthetic_boundary() -> None:
    source = ROOT / "results/final/parent_rfd_bw_parity_adjudication"
    headline = pd.read_csv(source / "headline_8192.csv").set_index("scenario")
    wins = pd.read_csv(source / "paired_win_counts.csv")
    order = ["parent home", "fixed control", "aligned", "mixed", "orthogonal", "curved"]
    labels = ["Fixed centre · identity", "Fixed centre · conditioned",
              "Drift inside factor space", "Drift partly outside",
              "Drift orthogonal to factors", "Curved centre path"]
    if set(headline.index) != set(order) or wins["paired draws"].sum() != 576:
        raise ValueError("The recorded synthetic comparison changed")
    values = headline.loc[order, "signal gain (%)"].to_numpy()
    if not np.isfinite(values).all():
        raise ValueError("Nonfinite synthetic gains")

    fig, axis = plt.subplots(figsize=(11.8, 5.8))
    fig.subplots_adjust(left=0.28, right=0.96, top=0.78, bottom=0.20)
    fig.text(0.03, 0.95, "The moving centre helps when drift escapes the factor space",
             fontsize=18, fontweight="bold", va="top")
    fig.text(0.03, 0.88, "Latent-signal reconstruction · paired synthetic covariance series",
             fontsize=11.5, color=GREY)
    axis.axvline(0, color=INK, lw=1)
    axis.axhspan(2.5, 5.5, color=GREEN, alpha=0.045)
    for y, value in enumerate(values):
        arrow(axis, y, value, GREEN if value > 0 else RUST, label=f"{value:+.1f}%")
    axis.set_yticks(range(6), labels)
    axis.set_ylim(5.6, -0.6)
    axis.set_xlim(-13, 70)
    axis.set_xticks([0, 20, 40, 60])
    axis.set_xlabel("Reduction in signal RMS versus parent RFM  →", labelpad=10)
    grid(axis)
    fig.text(0.03, 0.07,
             "Shown: median paired reduction at n = 8,192; known rank 2; 24 draws per regime.",
             fontsize=10, color=GREY)
    fig.text(0.03, 0.025,
             "Across all sample sizes: RFD wins 288/288 mixed, orthogonal and curved draws; parent wins 288/288 controls.",
             fontsize=10, color=INK)
    finish(fig, "synthetic_boundary")


def crypto_benchmarks() -> None:
    losses = pd.read_csv(ROOT / "results/final/crypto_forecast/headline_losses.csv").set_index("method")
    if set(losses.index) != set(METHODS) or not (losses["hours"] == 8760).all():
        raise ValueError("Expected the five frozen 8,760-hour headline rows")
    fig, axes = plt.subplots(2, 2, figsize=(13.2, 9.0))
    fig.subplots_adjust(left=0.15, right=0.95, top=0.80, bottom=0.13,
                        hspace=0.58, wspace=0.52)
    fig.text(0.035, 0.96, "RFD improves on parent RFM; classical baselines still lead",
             fontsize=19, fontweight="bold", va="top")
    fig.text(0.035, 0.895,
             "20 crypto assets · 8,760 next-hour forecasts · lower average loss is better",
             fontsize=12, color=GREY)
    for axis, (metric, title) in zip(axes.flat, METRICS.items()):
        excess = (100 * (losses[metric] / losses[metric].min() - 1)).sort_values()
        for y, (method, value) in enumerate(excess.items()):
            colour = GREEN if method == "rfd_piecewise6" else RUST if method == "parent_rfm" else GREY
            arrow(axis, y, value, colour,
                  label="best" if value < 1e-9 else f"+{value:.1f}%",
                  linewidth=3 if method == "rfd_piecewise6" else 1.9)
        axis.set_yticks(range(5), [METHODS[m] for m in excess.index])
        for tick in axis.get_yticklabels():
            if tick.get_text() == "RFD":
                tick.set_color(GREEN)
                tick.set_fontweight("bold")
        axis.set_ylim(4.6, -0.6)
        limit, ticks = {
            "frobenius2": (115, [0, 25, 50, 75, 100]),
            "qlike": (220, [0, 50, 100, 150, 200]),
            "bw2": (65, [0, 10, 20, 30, 40, 50, 60]),
            "gmv_realized_variance": (80, [0, 20, 40, 60, 80]),
        }[metric]
        axis.set_xlim(-0.01 * limit, limit)
        axis.set_xticks(ticks)
        axis.set_title(title, loc="left", pad=14, fontsize=12)
        axis.set_xlabel("Extra loss versus the best  →", fontsize=10, labelpad=8)
        grid(axis)
    fig.text(0.035, 0.058,
             "Matched rank-19 VAR(1); 2025 evaluation, with tuning on 2024. Each panel uses its own scale.",
             fontsize=10, color=GREY)
    fig.text(0.035, 0.022,
             "Primary RFD–parent loss intervals cross zero: the formal comparison is a tie.",
             fontsize=10, color=INK)
    finish(fig, "crypto_benchmarks")


def crypto_mean_median() -> None:
    contrast = pd.read_csv(ROOT / "results/final/crypto_forecast/rfd_vs_parent.csv").set_index("metric")
    fig, axis = plt.subplots(figsize=(12.6, 6.2))
    fig.subplots_adjust(left=0.29, right=0.96, top=0.74, bottom=0.22)
    fig.text(0.035, 0.95, "Lower average loss, despite higher median forecast error",
             fontsize=18, fontweight="bold", va="top")
    fig.text(0.035, 0.88, "RFD versus parent RFM · the mean and median tell different stories",
             fontsize=11.5, color=GREY)
    axis.axvline(0, color=INK, lw=1)
    for y, metric in enumerate(METRICS):
        for offset, column, colour in [(-0.17, "mean_reduction_percent", GREEN),
                                       (0.17, "median_reduction_percent", NAVY)]:
            value = float(contrast.loc[metric, column])
            arrow(axis, y + offset, value, colour, label=f"{value:+.2f}%")
    axis.set_yticks(range(4), list(METRICS.values()))
    axis.set_ylim(3.6, -0.6)
    axis.set_xlim(-9.5, 17)
    axis.set_xticks([-5, 0, 5, 10, 15])
    axis.set_xlabel("← Parent lower loss          RFD lower loss →", labelpad=10)
    grid(axis)
    fig.legend(handles=[Line2D([0], [0], color=GREEN, lw=2.5, label="Mean loss"),
                        Line2D([0], [0], color=NAVY, lw=2.5, label="Median loss")],
               loc="upper right", bbox_to_anchor=(0.97, 0.835), frameon=False, ncol=2)
    fig.text(0.035, 0.056,
             "Percent reductions compare the methods' separate means or medians; they are not median paired hourly gains.",
             fontsize=9.5, color=GREY)
    fig.text(0.035, 0.016,
             "The contrast suggests a contribution from large-error hours; it does not identify a market-stress mechanism.",
             fontsize=9.5, color=GREY)
    finish(fig, "crypto_mean_median")


if __name__ == "__main__":
    style()
    synthetic_boundary()
    crypto_benchmarks()
    crypto_mean_median()
