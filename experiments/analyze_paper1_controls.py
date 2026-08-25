"""Summarise and plot the frozen Paper 1 control-matrix outputs."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config/paper1_controls.yaml"
CORE_RAW = ROOT / "results/intermediate/paper1_control_core/raw.csv"
PHASE_RAW = ROOT / "results/intermediate/paper1_phase_curve/raw.csv"
OUTPUT = ROOT / "results/final/paper1_control_matrix"
METHOD_COLORS = {
    "known centre + noise": "#3B0F70",
    "full RFD": "#21918C",
    "fixed-centre ablation": "#A0DA39",
}


def load_config(path: Path = CONFIG) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _read(path: Path) -> pd.DataFrame:
    if not path.is_file() or path.stat().st_size == 0:
        return pd.DataFrame()
    return pd.read_csv(path)


def load_results() -> tuple[pd.DataFrame, pd.DataFrame]:
    return _read(CORE_RAW), _read(PHASE_RAW)


def _bootstrap_median(
    values: np.ndarray, *, repeats: int, rng: np.random.Generator
) -> tuple[float, float]:
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if values.size == 0:
        return np.nan, np.nan
    sampled = values[rng.integers(0, values.size, size=(repeats, values.size))]
    medians = np.median(sampled, axis=1)
    return float(np.quantile(medians, 0.025)), float(np.quantile(medians, 0.975))


def paired_effects(
    raw: pd.DataFrame, *, repeats: int, seed: int
) -> pd.DataFrame:
    metrics = {
        "loading projector": ("rfd_loading_error", "fixed_centre_loading_error"),
        "factor scores": ("rfd_factor_nrmse", "fixed_centre_factor_nrmse"),
        "observation reconstruction": (
            "rfd_observation_reconstruction_rms",
            "fixed_centre_observation_reconstruction_rms",
        ),
        "latent-signal reconstruction": (
            "rfd_signal_reconstruction_rms",
            "fixed_centre_signal_reconstruction_rms",
        ),
    }
    rng = np.random.default_rng(seed)
    records = []
    ok = raw.loc[raw["status"] == "ok"]
    for (regime, n), group in ok.groupby(["regime", "n"]):
        for metric, (rfd_column, fixed_column) in metrics.items():
            rfd = pd.to_numeric(group[rfd_column], errors="coerce")
            fixed = pd.to_numeric(group[fixed_column], errors="coerce")
            valid = rfd.notna() & fixed.notna() & (fixed > 0.0)
            gains = 100 * (fixed[valid] - rfd[valid]) / fixed[valid]
            lower, upper = _bootstrap_median(
                gains.to_numpy(), repeats=repeats, rng=rng
            )
            records.append({
                "regime": regime, "n": int(n), "metric": metric,
                "paired_draws": int(valid.sum()),
                "mean_improvement_percent": float(gains.mean()),
                "median_improvement_percent": float(gains.median()),
                "improvement_q25": float(gains.quantile(0.25)),
                "improvement_q75": float(gains.quantile(0.75)),
                "median_ci025": lower, "median_ci975": upper,
                "rfd_win_percent": float(100 * (gains > 0.0).mean()),
            })
    return pd.DataFrame(records)


def core_summary(raw: pd.DataFrame) -> pd.DataFrame:
    if raw.empty:
        return pd.DataFrame()
    records = []
    ok = raw.loc[raw["status"] == "ok"]
    numeric_metrics = [
        "rfd_centre_path_rms", "rfd_loading_angle_degrees",
        "rfd_factor_nrmse", "rfd_observation_reconstruction_rms",
        "known_centre_loading_error", "fixed_centre_loading_error",
        "noise_lag_row_size", "rfd_fallback_rate",
    ]
    for (regime, n), group in ok.groupby(["regime", "n"]):
        record = {
            "regime": regime, "regime_label": group["regime_label"].iloc[0],
            "regime_class": group["regime_class"].iloc[0], "n": int(n),
            "completed": len(group),
            "rfd_threshold_accuracy_percent": float(
                100 * (group["rfd_threshold_rank"] == group["true_rank"]).mean()
            ),
            "known_threshold_accuracy_percent": float(
                100 * (group["known_centre_threshold_rank"] == group["true_rank"]).mean()
            ),
            "fixed_threshold_accuracy_percent": float(
                100 * (group["fixed_centre_threshold_rank"] == group["true_rank"]).mean()
            ),
            "recorded_error_percent": 0.0,
            "nonconverged_stage_total": int(group["rfd_nonconverged_stages"].sum()),
            "fallback_total": int(group["rfd_fallback_count"].sum()),
        }
        for metric in numeric_metrics:
            values = pd.to_numeric(group[metric], errors="coerce")
            record[f"{metric}_mean"] = float(values.mean())
            record[f"{metric}_median"] = float(values.median())
            record[f"{metric}_q25"] = float(values.quantile(0.25))
            record[f"{metric}_q75"] = float(values.quantile(0.75))
        records.append(record)
    return pd.DataFrame(records)


def _style(ax: plt.Axes) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(True, alpha=0.18, axis="y")


def plot_core_loading(core: pd.DataFrame, output: Path) -> None:
    if core.empty:
        return
    final = core.loc[
        (core["status"] == "ok")
        & (core["n"] == core["n"].max())
        & (core["true_rank"] > 0)
    ].copy()
    methods = {
        "known centre + noise": "known_centre_loading_error",
        "full RFD": "rfd_loading_error",
        "fixed-centre ablation": "fixed_centre_loading_error",
    }
    regimes = list(dict.fromkeys(final["regime"]))
    positions = np.arange(len(regimes))
    width = 0.25
    fig, ax = plt.subplots(figsize=(12.5, 5.2))
    for index, (method, column) in enumerate(methods.items()):
        medians = []
        for regime in regimes:
            value = final.loc[final["regime"] == regime, column].median()
            medians.append(np.degrees(np.arcsin(np.clip(value, 0.0, 1.0))))
        ax.bar(
            positions + (index - 1) * width, medians, width=width,
            label=method, color=METHOD_COLORS[method],
        )
    ax.set_xticks(positions, regimes)
    ax.set_ylabel("largest loading angle (degrees)")
    ax.set_title(f"Paper 1 controls at n = {int(final['n'].max()):,}")
    ax.legend(frameon=False, ncol=3)
    _style(ax)
    fig.tight_layout()
    fig.savefig(output / "01_core_loading_controls.png", dpi=190, bbox_inches="tight")
    plt.close(fig)


def plot_rank_nulls(core: pd.DataFrame, output: Path) -> None:
    if core.empty:
        return
    nulls = core.loc[
        (core["status"] == "ok") & core["regime"].isin(["C1", "C3"])
    ]
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), sharey=True)
    methods = {
        "known centre + noise": "known_centre_threshold_rank",
        "full RFD": "rfd_threshold_rank",
        "fixed-centre ablation": "fixed_centre_threshold_rank",
    }
    for ax, (regime, group) in zip(axes, nulls.groupby("regime")):
        for method, column in methods.items():
            accuracy = 100 * group.groupby("n")[column].apply(lambda x: (x == 0).mean())
            ax.plot(
                accuracy.index, accuracy.values, marker="o", label=method,
                color=METHOD_COLORS[method],
            )
        ax.set_xscale("log", base=2)
        ax.set_ylim(-3, 103)
        ax.set_title(f"{regime}: {group['regime_label'].iloc[0]}")
        ax.set_xlabel("observations n")
        _style(ax)
    axes[0].set_ylabel("rank zero selected (%)")
    axes[0].legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(output / "02_rank_zero_nulls.png", dpi=190, bbox_inches="tight")
    plt.close(fig)


def plot_phase(phase: pd.DataFrame, effects: pd.DataFrame, output: Path) -> None:
    if phase.empty or effects.empty:
        return
    orientation_labels = {
        "aligned": "aligned", "mixed": "mixed", "orthogonal": "orthogonal"
    }
    colors = dict(zip(orientation_labels, plt.cm.viridis(np.linspace(0.12, 0.88, 3))))
    metrics = ["loading projector", "observation reconstruction"]
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.7))
    phase_keys = phase[["regime", "drift_scale", "loading_orientation"]].drop_duplicates()
    joined = effects.merge(phase_keys, on="regime", how="inner")
    for ax, metric in zip(axes, metrics):
        selected = joined.loc[joined["metric"] == metric]
        for orientation, group in selected.groupby("loading_orientation"):
            group = group.sort_values("drift_scale")
            ax.plot(
                group["drift_scale"], group["median_improvement_percent"],
                marker="o", color=colors[orientation], label=orientation_labels[orientation],
            )
            ax.fill_between(
                group["drift_scale"], group["median_ci025"], group["median_ci975"],
                color=colors[orientation], alpha=0.14,
            )
        ax.axhline(0.0, color="#555555", linestyle="--", linewidth=1.1)
        ax.set_xlabel("centre-drift scale ν")
        ax.set_ylabel("RFD error reduction vs fixed centre (%)")
        ax.set_title(metric)
        _style(ax)
    axes[0].legend(frameon=False)
    fig.suptitle("Where moving-centre modelling helps")
    fig.tight_layout()
    fig.savefig(output / "03_drift_orientation_phase.png", dpi=190, bbox_inches="tight")
    plt.close(fig)


def plot_violation_diagnostics(core: pd.DataFrame, output: Path) -> None:
    if core.empty:
        return
    selected = core.loc[
        (core["status"] == "ok") & core["regime"].isin(["B0", "V-L", "V-R"])
    ]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.4))
    colors = dict(zip(["B0", "V-L", "V-R"], plt.cm.viridis([0.15, 0.5, 0.85])))
    for regime, group in selected.groupby("regime"):
        noise = group.groupby("n")["noise_lag_row_size"].median()
        centre = group.groupby("n")["rfd_centre_path_rms"].median()
        axes[0].plot(noise.index, noise.values, marker="o", color=colors[regime], label=regime)
        axes[1].plot(centre.index, centre.values, marker="o", color=colors[regime])
    for ax, ylabel in zip(
        axes, ("noise lag-row size", "RFD centre-path RMS")
    ):
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xlabel("observations n")
        ax.set_ylabel(ylabel)
        _style(ax)
    axes[0].legend(frameon=False)
    fig.suptitle("Assumption-violation diagnostics")
    fig.tight_layout()
    fig.savefig(output / "04_violation_diagnostics.png", dpi=190, bbox_inches="tight")
    plt.close(fig)


def write_report(
    config: dict, core: pd.DataFrame, phase: pd.DataFrame,
    summary: pd.DataFrame, effects: pd.DataFrame, output: Path,
) -> None:
    core_requested = (
        len(config["core_regimes"])
        * len(config["profiles"]["control_core"]["n_values"])
        * int(config["profiles"]["control_core"]["replicates"])
    )
    phase_requested = (
        len(config["phase_curve"]["drift_scales"])
        * len(config["phase_curve"]["orientations"])
        * len(config["profiles"]["phase_curve"]["n_values"])
        * int(config["profiles"]["phase_curve"]["replicates"])
    )
    lines = [
        "# Paper 1 control matrix", "",
        "Numerical evidence only. A violation cell passes when it fails in the",
        "declared measurable way; attractive performance is not required.", "",
        "## Completion", "",
        f"- core: {len(core)}/{core_requested} rows",
        f"- phase: {len(phase)}/{phase_requested} rows",
        f"- core recorded errors: {(core['status'] == 'error').sum() if not core.empty else 0}",
        f"- phase recorded errors: {(phase['status'] == 'error').sum() if not phase.empty else 0}", "",
    ]
    complete = len(core) == core_requested and len(phase) == phase_requested
    if not complete:
        lines.extend([
            "**Status: incomplete.** The analysis products are provisional and no",
            "paper claim is adjudicated until both profiles are complete.", "",
        ])
    else:
        largest_n = int(core["n"].max())
        final_summary = summary.loc[summary["n"] == largest_n]
        final_effects = effects.loc[
            (effects["n"] == largest_n)
            & (effects["metric"].isin(["loading projector", "observation reconstruction"]))
        ]
        lines.extend([
            f"**Status: complete at n up to {largest_n:,}.** Interpretations below",
            "remain conditional on the predeclared DGPs.", "", "## Core decisions", "",
            "| regime | threshold accuracy | RFD loading angle | fallback total |",
            "|---|---:|---:|---:|",
        ])
        for _, row in final_summary.sort_values("regime").iterrows():
            angle = row["rfd_loading_angle_degrees_median"]
            angle_text = "n/a" if not np.isfinite(angle) else f"{angle:.2f}°"
            lines.append(
                f"| {row['regime']} | {row['rfd_threshold_accuracy_percent']:.1f}% | "
                f"{angle_text} | {int(row['fallback_total'])} |"
            )
        lines.extend([
            "", "## Paired headline effects", "",
            "Positive values mean RFD reduces error relative to the fixed-centre ablation.", "",
            "| regime | metric | median improvement | 95% paired-bootstrap interval | RFD wins |",
            "|---|---|---:|---:|---:|",
        ])
        for _, row in final_effects.sort_values(["regime", "metric"]).iterrows():
            lines.append(
                f"| {row['regime']} | {row['metric']} | "
                f"{row['median_improvement_percent']:.1f}% | "
                f"[{row['median_ci025']:.1f}%, {row['median_ci975']:.1f}%] | "
                f"{row['rfd_win_percent']:.1f}% |"
            )
        lines.extend([
            "", "The fixed-centre placebo, rank-zero nulls, identification ordering,",
            "curved-path health, and violation boundaries require scientific",
            "adjudication together; no single favourable row closes the matrix.", "",
        ])
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")


def run(output: Path = OUTPUT) -> None:
    output.mkdir(parents=True, exist_ok=True)
    config = load_config()
    core, phase = load_results()
    combined = pd.concat([frame for frame in (core, phase) if not frame.empty], ignore_index=True) \
        if not core.empty or not phase.empty else pd.DataFrame()
    summary = core_summary(core)
    effects = paired_effects(
        combined,
        repeats=int(config["analysis"]["bootstrap_replicates"]),
        seed=int(config["analysis"]["bootstrap_seed"]),
    ) if not combined.empty else pd.DataFrame()
    summary.to_csv(output / "core_summary.csv", index=False)
    effects.to_csv(output / "paired_effects.csv", index=False)
    plot_core_loading(core, output)
    plot_rank_nulls(core, output)
    plot_phase(phase, effects, output)
    plot_violation_diagnostics(core, output)
    write_report(config, core, phase, summary, effects, output)
    print(f"Paper 1 control analysis -> {output.relative_to(ROOT)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args(argv)
    run(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
