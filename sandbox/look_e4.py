"""Throwaway plots of the E4 cost model. Not evidence -- just for looking.

Reads results/final/bw_cost_model.csv, writes PNGs to sandbox/plots/, which
is gitignored. Delete them whenever; re-run in a second.

    python sandbox/look_e4.py

Encoding: colour = m, linestyle = cond. Two factors, two channels -- rather
than four colours, which would put orange and yellow on screen together and
stop being readable. Dark surface because that is what you look at.

One panel per question:
  1. how long does one barycentre actually take
  2. is the cost linear in N        (flat line = yes)
  3. is the iteration count stable  (flat or falling = yes)
Panel 2 divides out N rather than drawing a slope-1 guide: a horizontal line
is far easier to read than "is this parallel to that dotted thing".
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")           # write files, never try to open a window
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "results" / "final" / "bw_cost_model.csv"
OUTDIR = ROOT / "sandbox" / "plots"

SURFACE = "#1a1a19"
INK = "#ffffff"
MUTED = "#c3c2b7"
GRID = "#3a3a38"
SERIES = {3: "#3987e5", 12: "#d95926"}     # validated dark-mode slots 1 and 2
STYLE = {10.0: "-", 1000.0: "--"}

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "text.color": INK, "axes.labelcolor": MUTED, "axes.titlecolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.edgecolor": GRID, "grid.color": GRID, "grid.alpha": 0.4,
    "axes.grid": True, "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 10, "lines.linewidth": 2.0, "lines.markersize": 6,
    "legend.frameon": False, "figure.dpi": 130,
})


def main():
    if not CSV.exists():
        sys.exit(f"no {CSV} -- run experiments/e4_bw_cost.py first")
    df = pd.read_csv(CSV)
    df["ms_per_iter_per_1k"] = df["ms_per_iter"] / df["N"] * 1000.0

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14.5, 4.3))

    for (m, cond), g in df.groupby(["m", "cond"], sort=True):
        g = g.sort_values("N")
        kw = dict(color=SERIES[m], linestyle=STYLE[float(cond)], marker="o",
                  label=f"m={m}, $\\kappa$={cond:.0e}")
        ax1.plot(g["N"], g["seconds"], **kw)
        ax2.plot(g["N"], g["ms_per_iter_per_1k"], **kw)
        ax3.plot(g["N"], g["iters"], **kw)

    ax1.set(xscale="log", yscale="log", xlabel="N",
            ylabel="seconds", title="One barycentre")
    ax2.set(xscale="log", xlabel="N", ylabel="ms / iteration / 1000 matrices",
            title="Linear in N?   (flat = yes)")
    ax2.set_ylim(bottom=0)
    ax3.set(xscale="log", xlabel="N", ylabel="iterations",
            title="Iterations   (flat or falling = fine)")
    ax3.set_ylim(bottom=0)

    ax1.legend(loc="upper left", fontsize=8)
    fig.suptitle("E4 - BW barycentre cost model", color=INK, x=0.01, ha="left")
    fig.tight_layout()

    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / "e4_cost.png"
    fig.savefig(out, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
