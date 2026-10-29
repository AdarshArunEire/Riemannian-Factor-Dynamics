"""Draw the README figures from the tracked result tables in results/.

python experiments/figures.py

Colours are two viridis steps: teal for RFD, purple for the parent RFM, grey for
the classical baselines. Explanations live in the README captions.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "figures"
RFD = "#20a386"      # viridis 0.58
PARENT = "#3e4c8a"   # viridis 0.23
BASELINE = "#a7afb2"
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
                  ha="left" if value >= 0 else "right", color=INK,
                  fontsize=10.5)


def grid(axis) -> None:
    axis.set_axisbelow(True)
    axis.grid(axis="x", color=GRID, linewidth=0.8)
    axis.tick_params(axis="y", length=0, pad=9)
    axis.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))


def title(fig, text: str) -> None:
    fig.text(0.03, 0.96, text, fontsize=15, fontweight="bold", va="top")


def synthetic_boundary() -> None:
    source = ROOT / "results/synthetic"
    headline = pd.read_csv(source / "headline_8192.csv").set_index("scenario")
    wins = pd.read_csv(source / "paired_win_counts.csv")
    order = ["parent home", "fixed control", "aligned", "mixed", "orthogonal", "curved"]
    labels = ["Fixed centre", "Fixed centre, conditioned",
              "Drift inside factor space", "Drift partly outside",
              "Drift orthogonal to factors", "Curved drift"]
    if set(headline.index) != set(order) or wins["paired draws"].sum() != 576:
        raise ValueError("The recorded synthetic comparison changed")
    values = headline.loc[order, "signal gain (%)"].to_numpy()
    if not np.isfinite(values).all():
        raise ValueError("Nonfinite synthetic gains")

    fig, axis = plt.subplots(figsize=(10.5, 4.8))
    fig.subplots_adjust(left=0.25, right=0.96, top=0.84, bottom=0.15)
    title(fig, "Signal error reduction versus parent RFM")
    axis.axvline(0, color=INK, lw=1)
    axis.axhspan(2.5, 5.5, color=RFD, alpha=0.06)
    for y, value in enumerate(values):
        arrow(axis, y, value, RFD if value > 0 else PARENT, label=f"{value:+.1f}%")
    axis.set_yticks(range(6), labels)
    axis.set_ylim(5.6, -0.6)
    axis.set_xlim(-13, 70)
    axis.set_xticks([0, 20, 40, 60])
    axis.set_xlabel("Reduction in signal error  →", labelpad=8)
    grid(axis)
    fig.legend(handles=[Patch(color=RFD, label="RFD better"),
                        Patch(color=PARENT, label="Parent RFM better")],
               loc="upper right", bbox_to_anchor=(0.97, 0.97), frameon=False, ncol=2)
    finish(fig, "synthetic_boundary")


def crypto_benchmarks() -> None:
    losses = pd.read_csv(ROOT / "results/crypto/headline_losses.csv").set_index("method")
    if set(losses.index) != set(METHODS) or not (losses["hours"] == 8760).all():
        raise ValueError("Expected the five frozen 8,760-hour headline rows")
    colours = {"rfd_piecewise6": RFD, "parent_rfm": PARENT}
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.6))
    fig.subplots_adjust(left=0.14, right=0.96, top=0.82, bottom=0.07,
                        hspace=0.55, wspace=0.5)
    title(fig, "Next-hour forecast loss above the best method")
    for axis, (metric, name) in zip(axes.flat, METRICS.items()):
        excess = (100 * (losses[metric] / losses[metric].min() - 1)).sort_values()
        for y, (method, value) in enumerate(excess.items()):
            arrow(axis, y, value, colours.get(method, BASELINE),
                  label="best" if value < 1e-9 else f"+{value:.1f}%",
                  linewidth=3 if method in colours else 2)
        axis.set_yticks(range(5), [METHODS[m] for m in excess.index])
        axis.set_ylim(4.6, -0.6)
        limit, ticks = {
            "frobenius2": (115, [0, 25, 50, 75, 100]),
            "qlike": (220, [0, 50, 100, 150, 200]),
            "bw2": (65, [0, 20, 40, 60]),
            "gmv_realized_variance": (80, [0, 20, 40, 60, 80]),
        }[metric]
        axis.set_xlim(-0.01 * limit, limit)
        axis.set_xticks(ticks)
        axis.set_title(name, loc="left", pad=10, fontsize=11.5)
        grid(axis)
    fig.legend(handles=[Patch(color=RFD, label="RFD"), Patch(color=PARENT, label="Parent RFM"),
                        Patch(color=BASELINE, label="Classical baselines")],
               loc="upper left", bbox_to_anchor=(0.022, 0.935), frameon=False, ncol=3)
    finish(fig, "crypto_benchmarks")


def crypto_mean_median() -> None:
    contrast = pd.read_csv(ROOT / "results/crypto/rfd_vs_parent.csv").set_index("metric")
    names = {"frobenius2": "Frobenius", "qlike": "QLIKE", "bw2": "Bures–Wasserstein",
             "gmv_realized_variance": "Portfolio variance"}
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
    fig.subplots_adjust(left=0.17, right=0.97, top=0.76, bottom=0.17, wspace=0.12)
    title(fig, "RFD versus parent RFM: average hour and typical hour")
    for axis, column, name in [(axes[0], "mean_reduction_percent", "Average (mean) loss"),
                               (axes[1], "median_reduction_percent", "Typical (median) loss")]:
        axis.axvline(0, color=INK, lw=1)
        for y, metric in enumerate(names):
            value = float(contrast.loc[metric, column])
            arrow(axis, y, value, RFD if value > 0 else PARENT, label=f"{value:+.1f}%")
        axis.set_yticks(range(4), list(names.values()))
        axis.set_ylim(3.6, -0.6)
        axis.set_xlim(-10, 18)
        axis.set_xticks([-5, 0, 5, 10, 15])
        axis.set_title(name, loc="left", pad=10, fontsize=11.5)
        grid(axis)
    fig.supxlabel("← Parent lower loss      RFD lower loss →", fontsize=10.5, y=0.03)
    fig.legend(handles=[Patch(color=RFD, label="RFD better"),
                        Patch(color=PARENT, label="Parent RFM better")],
               loc="upper right", bbox_to_anchor=(0.97, 0.965), frameon=False, ncol=2)
    finish(fig, "crypto_mean_median")


if __name__ == "__main__":
    style()
    synthetic_boundary()
    crypto_benchmarks()
    crypto_mean_median()
