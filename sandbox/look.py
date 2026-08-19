"""Throwaway plots for every experiment that has produced a CSV.

Not evidence -- results/final/*.md is the record. These are for looking at.
Writes PNGs to sandbox/plots/, which is gitignored. Delete them whenever.

    python sandbox/look.py

Missing CSVs are skipped silently, so this is safe to run at any point.
Colours are the validated dark-mode categorical slots; a second factor is
always carried by linestyle rather than more colours, because four hues on
one axis stops being readable long before it stops being possible.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "results" / "final"
OUTDIR = ROOT / "sandbox" / "plots"

SURFACE, INK, MUTED, GRID = "#1a1a19", "#ffffff", "#c3c2b7", "#3a3a38"
SLOTS = ["#3987e5", "#d95926", "#199e70"]          # blue, orange, aqua
DASH = ["-", "--", ":"]

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "text.color": INK, "axes.labelcolor": MUTED, "axes.titlecolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.edgecolor": GRID, "grid.color": GRID, "grid.alpha": 0.4,
    "axes.grid": True, "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 10, "lines.linewidth": 2.0, "lines.markersize": 5,
    "legend.frameon": False, "figure.dpi": 130,
})


def _load(name):
    p = FINAL / f"{name}.csv"
    return pd.read_csv(p) if p.exists() else None


def _save(fig, name):
    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / f"{name}.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(ROOT)}")


def plot_e4():
    df = _load("bw_cost_model")
    if df is None:
        return
    df["per_1k"] = df["ms_per_iter"] / df["N"] * 1000.0
    colour = {m: SLOTS[i] for i, m in enumerate(sorted(df["m"].unique()))}
    dash = {c: DASH[i] for i, c in enumerate(sorted(df["cond"].unique()))}

    fig, (a, b, c) = plt.subplots(1, 3, figsize=(14.5, 4.3))
    for (m, cond), g in df.groupby(["m", "cond"], sort=True):
        g = g.sort_values("N")
        kw = dict(color=colour[m], linestyle=dash[cond], marker="o",
                  label=f"m={m}, $\\kappa$={cond:.0e}")
        a.plot(g["N"], g["seconds"], **kw)
        b.plot(g["N"], g["per_1k"], **kw)
        c.plot(g["N"], g["iters"], **kw)
    a.set(xscale="log", yscale="log", xlabel="N", ylabel="seconds",
          title="One barycentre")
    b.set(xscale="log", xlabel="N", ylabel="ms / iter / 1000 matrices",
          title="Linear in N?   (flat = yes)", ylim=(0, None))
    c.set(xscale="log", xlabel="N", ylabel="iterations",
          title="Iterations   (flat or falling = fine)", ylim=(0, None))
    a.legend(loc="upper left", fontsize=8)
    fig.suptitle("E4 - cost model", color=INK, x=0.01, ha="left")
    fig.tight_layout()
    _save(fig, "e4_cost")


def plot_e1():
    df = _load("e1_convergence_surface")
    if df is None:
        return
    shapes = list(df["shape"].unique())
    colour = {c: SLOTS[i] for i, c in enumerate(sorted(df["cond"].unique()))}
    dash = {m: DASH[i] for i, m in enumerate(sorted(df["m"].unique()))}

    fig, axes = plt.subplots(1, len(shapes), figsize=(4.9 * len(shapes), 4.3),
                             sharey=True)
    axes = list(axes) if len(shapes) > 1 else [axes]
    for ax, shape in zip(axes, shapes):
        sub = df[df["shape"] == shape]
        for (m, cond), g in sub.groupby(["m", "cond"], sort=True):
            g = g.sort_values("delta")
            ax.plot(g["delta"], g["iters"], color=colour[cond],
                    linestyle=dash[m], marker="o",
                    label=f"m={m}, $\\kappa$={cond:.0e}")
        ax.set(xlabel="$\\delta$  (dispersion of the family)",
               title=f"spectrum: {shape}", ylim=(0, None))
    axes[0].set_ylabel("iterations to converge")
    axes[-1].legend(fontsize=8, loc="upper left")
    fig.suptitle("E1 - does cost follow dispersion or conditioning?",
                 color=INK, x=0.01, ha="left")
    fig.tight_layout()
    _save(fig, "e1_surface")


def plot_e2():
    df = _load("e2_boundary")
    if df is None:
        return
    colour = {m: SLOTS[i] for i, m in enumerate(sorted(df["m"].unique()))}
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
    for m, g in df.groupby("m", sort=True):
        g = g.sort_values("cond")
        ok = g[g["iters"] > 0]
        a.plot(ok["cond"], ok["iters"], color=colour[m], marker="o", label=f"m={m}")
        dead = g[g["iters"] < 0]
        if len(dead):
            a.scatter(dead["cond"], [0] * len(dead), color=colour[m],
                      marker="x", s=70, zorder=3)
        res = ok[ok["residual"] != "nan"]
        b.plot(res["cond"], res["residual"].astype(float), color=colour[m],
               marker="o", label=f"m={m}")
    a.set(xscale="log", xlabel="$\\kappa$", ylabel="iterations",
          title="Iterations   (x on the floor = raised)", ylim=(0, None))
    b.set(xscale="log", yscale="log", xlabel="$\\kappa$",
          ylabel="final residual", title="Residual reached")
    b.axhline(1e-12, color=MUTED, linestyle=":", linewidth=1.2)
    a.legend(fontsize=8)
    fig.suptitle("E2 - where it stops working", color=INK, x=0.01, ha="left")
    fig.tight_layout()
    _save(fig, "e2_boundary")


def plot_e3():
    df = _load("e3_tol_accuracy")
    if df is None:
        return
    colour = {c: SLOTS[i] for i, c in enumerate(sorted(df["cond"].unique()))}
    dash = {m: DASH[i] for i, m in enumerate(sorted(df["m"].unique()))}
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
    for (m, cond), g in df.groupby(["m", "cond"], sort=True):
        g = g.sort_values("tol")
        kw = dict(color=colour[cond], linestyle=dash[m], marker="o",
                  label=f"m={m}, $\\kappa$={cond:.0e}")
        a.plot(g["tol"], g["err_vs_ref"].astype(float), **kw)
        b.plot(g["tol"], g["iters"], **kw)
    a.set(xscale="log", yscale="log", xlabel="requested tol",
          ylabel="actual error vs exact barycentre",
          title="What tol buys   (knee = stop paying)")
    b.set(xscale="log", xlabel="requested tol", ylabel="iterations",
          title="What tol costs", ylim=(0, None))
    a.legend(fontsize=8, loc="upper left")
    fig.suptitle("E3 - tol vs accuracy", color=INK, x=0.01, ha="left")
    fig.tight_layout()
    _save(fig, "e3_tol")


def plot_e5():
    df = _load("e5_airm_cost")
    if df is None:
        return
    colour = {m: SLOTS[i] for i, m in enumerate(sorted(df["m"].unique()))}
    dash = {c: DASH[i] for i, c in enumerate(sorted(df["cond"].unique()))}
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
    for (m, cond), g in df.groupby(["m", "cond"], sort=True):
        g = g.sort_values("N")
        lbl = f"m={m}, $\\kappa$={cond:.0e}"
        a.plot(g["N"], g["bw_seconds"], color=colour[m], linestyle=dash[cond],
               marker="o", label=f"BW  {lbl}")
        a.plot(g["N"], g["airm_seconds"], color=colour[m], linestyle=dash[cond],
               marker="s", alpha=0.55, label=f"AIRM {lbl}")
        b.plot(g["N"], g["ratio"], color=colour[m], linestyle=dash[cond], marker="o",
               label=lbl)
    a.set(xscale="log", yscale="log", xlabel="N", ylabel="seconds",
          title="One barycentre   (circle BW, square AIRM)")
    b.axhline(1.0, color=MUTED, linestyle=":", linewidth=1.2)
    b.axhline(2.0, color=MUTED, linestyle="--", linewidth=1.0)
    b.set(xscale="log", xlabel="N", ylabel="AIRM / BW",
          title="Cost ratio   (dashed = E4's assumed 2x)", ylim=(0, None))
    a.legend(fontsize=7, loc="upper left")
    fig.suptitle("E5 - AIRM vs BW cost", color=INK, x=0.01, ha="left")
    fig.tight_layout()
    _save(fig, "e5_airm_cost")


def plot_e6():
    df = _load("e6_airm_convergence")
    if df is None:
        return
    df = df[df["m"] == df["m"].max()]          # busiest m only; 12 lines is unreadable
    shapes = list(df["shape"].unique())
    colour = {c: SLOTS[i] for i, c in enumerate(sorted(df["cond"].unique()))}
    dash = {st: DASH[i] for i, st in enumerate(sorted(df["step"].unique(), reverse=True))}
    fig, axes = plt.subplots(1, len(shapes), figsize=(4.9 * len(shapes), 4.3), sharey=True)
    axes = list(axes) if len(shapes) > 1 else [axes]
    for ax, shape in zip(axes, shapes):
        sub = df[df["shape"] == shape]
        for (step, cond), g in sub.groupby(["step", "cond"], sort=True):
            g = g.sort_values("delta")
            ax.plot(g["delta"], g["iters"], color=colour[cond], linestyle=dash[step],
                    marker="o", label=f"step={step}, $\\kappa$={cond:.0e}")
        ax.set(xlabel="$\\delta$  (dispersion)", title=f"spectrum: {shape}", ylim=(0, None))
    axes[0].set_ylabel("iterations to converge")
    axes[-1].legend(fontsize=8, loc="upper left")
    fig.suptitle(f"E6 - AIRM convergence (m={df['m'].iloc[0]})", color=INK, x=0.01, ha="left")
    fig.tight_layout()
    _save(fig, "e6_airm_convergence")


def plot_e7():
    df = _load("e7_geometry_divergence")
    if df is None:
        return
    colour = {c: SLOTS[i] for i, c in enumerate(sorted(df["cond"].unique()))}
    dash = {m: DASH[i] for i, m in enumerate(sorted(df["m"].unique()))}
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3), sharey=True)
    for (m, cond), g in df.groupby(["m", "cond"], sort=True):
        g = g.sort_values("delta")
        kw = dict(color=colour[cond], linestyle=dash[m], marker="o",
                  label=f"m={m}, $\\kappa$={cond:.0e}")
        a.plot(g["delta"], g["d_bw_airm_rel"], **kw)
        b.plot(g["delta"], g["d_airm_frob_rel"], **kw)
    for ax, t in ((a, "BW centre vs AIRM centre"), (b, "AIRM centre vs arithmetic mean")):
        ax.set(xscale="log", yscale="log", xlabel="$\\delta$  (dispersion)", title=t)
    a.set_ylabel("distance between centres / spread of data")
    a.legend(fontsize=8, loc="upper left")
    fig.suptitle("E7 - does the choice of geometry move the centre?",
                 color=INK, x=0.01, ha="left")
    fig.tight_layout()
    _save(fig, "e7_divergence")


if __name__ == "__main__":
    plot_e4(); plot_e1(); plot_e2(); plot_e3()
    plot_e5(); plot_e6(); plot_e7()
    if not any(OUTDIR.glob("*.png")):
        sys.exit("no CSVs found in results/final -- run the experiments first")
