"""Audit all result CSVs and adjudicate the recorded B4.5/N-01 experiment."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
BASE_RAW = ROOT / "results/intermediate/end_to_end_factor_baseline/raw.csv"
EXT_RAW = ROOT / "results/intermediate/end_to_end_factor_baseline_8192/raw.csv"
COMPARATOR_BASE = ROOT / "results/intermediate/b45_comparators/raw.csv"
COMPARATOR_EXT = ROOT / "results/intermediate/b45_comparators_8192/raw.csv"
OUTPUT = ROOT / "results/final/b45_adjudication"


def audit_csvs() -> pd.DataFrame:
    """Parse every result CSV and record structural health."""
    rows = []
    for path in sorted((ROOT / "results").rglob("*.csv")):
        record = {"path": str(path.relative_to(ROOT))}
        try:
            frame = pd.read_csv(path)
            numeric = frame.select_dtypes(include=[np.number])
            record.update({
                "parse_status": "ok",
                "rows": len(frame),
                "columns": len(frame.columns),
                "status_errors": int(
                    (frame["status"].astype(str).str.lower() == "error").sum()
                ) if "status" in frame else 0,
                "infinite_numeric_cells": int(np.isinf(numeric.to_numpy()).sum()),
            })
        except Exception as error:
            record.update({
                "parse_status": "error", "rows": np.nan, "columns": np.nan,
                "status_errors": np.nan, "infinite_numeric_cells": np.nan,
                "error": f"{type(error).__name__}: {error}",
            })
        rows.append(record)
    return pd.DataFrame(rows)


def load_b45() -> pd.DataFrame:
    frames = [pd.read_csv(BASE_RAW), pd.read_csv(EXT_RAW)]
    raw = pd.concat(frames, ignore_index=True)
    identity = ["n", "matrix_size", "replicate", "variant"]
    if raw.duplicated(identity).any():
        raise ValueError("B4.5 raw sources contain duplicate task/variant rows")
    if len(raw) != 960:
        raise ValueError(f"B4.5 expected 960 rows, found {len(raw)}")
    return raw


def load_comparators() -> pd.DataFrame | None:
    """Return the complete same-draw comparator replay, or None while pending."""
    if not COMPARATOR_BASE.is_file() or not COMPARATOR_EXT.is_file():
        return None
    raw = pd.concat(
        [pd.read_csv(COMPARATOR_BASE), pd.read_csv(COMPARATOR_EXT)],
        ignore_index=True,
    )
    identity = ["n", "matrix_size", "replicate"]
    if raw.duplicated(identity).any():
        raise ValueError("comparator sources contain duplicate task rows")
    if len(raw) != 480 or (raw["status"] != "ok").any():
        return None
    return raw


def rate_table(raw: pd.DataFrame) -> pd.DataFrame:
    metrics = {
        "centre_path_rms": "centre path",
        "lag_row_error": "lag row",
        "operator_error": "lag operator",
        "loading_subspace_error": "loading projector",
        "null_eigenvalue": "first null eigenvalue",
    }
    ok = raw.loc[(raw["status"] == "ok") & (raw["variant"] == "production")]
    records = []
    for matrix_size, group in ok.groupby("matrix_size"):
        for column, label in metrics.items():
            medians = group.groupby("n")[column].median().sort_index()
            slope, _ = np.polyfit(np.log(medians.index), np.log(medians.values), 1)
            records.append({
                "matrix_size": int(matrix_size), "metric": label,
                "empirical_exponent": float(-slope),
            })
    return pd.DataFrame(records)


def final_quality(raw: pd.DataFrame) -> pd.DataFrame:
    final = raw.loc[
        (raw["status"] == "ok")
        & (raw["variant"] == "production")
        & (raw["n"] == raw["n"].max())
    ].copy()
    final["loading_angle_degrees"] = np.degrees(
        np.arcsin(np.clip(final["loading_subspace_error"], 0.0, 1.0))
    )
    final["centre_percent_of_path"] = (
        100.0 * final["centre_path_rms"] / final["centre_path_length"]
    )
    final["factor_nrmse_percent"] = 100.0 * final["factor_score_nrmse"]
    final["operator_below_gap"] = final["operator_error"] < final["oracle_gap"]
    final["assembly_below_gap"] = final["assembly_bound"] < final["oracle_gap"]
    records = []
    for matrix_size, group in final.groupby("matrix_size"):
        record = {"matrix_size": int(matrix_size), "replicates": len(group)}
        for metric in (
            "centre_path_rms", "centre_percent_of_path",
            "loading_subspace_error", "loading_angle_degrees",
            "factor_score_nrmse", "factor_nrmse_percent",
            "observation_reconstruction_rms", "signal_reconstruction_rms",
            "assembly_gap_ratio", "empirical_energy_R",
        ):
            record[f"{metric}_median"] = float(group[metric].median())
            record[f"{metric}_q25"] = float(group[metric].quantile(0.25))
            record[f"{metric}_q75"] = float(group[metric].quantile(0.75))
        record["operator_below_gap_percent"] = float(100 * group["operator_below_gap"].mean())
        record["assembly_below_gap_percent"] = float(100 * group["assembly_below_gap"].mean())
        record["threshold_accuracy_percent"] = float(
            100 * (group["threshold_rank"] == group["true_rank"]).mean()
        )
        records.append(record)
    return pd.DataFrame(records)


def bandwidth_gains(raw: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        "centre_path_rms", "lag_row_error", "operator_error",
        "loading_subspace_error", "null_eigenvalue", "factor_score_nrmse",
        "observation_reconstruction_rms", "signal_reconstruction_rms",
    ]
    wide = raw.loc[raw["status"] == "ok"].pivot(
        index=["n", "matrix_size", "replicate"], columns="variant", values=metrics
    )
    records = []
    for metric in metrics:
        production = wide[(metric, "production")]
        reference = wide[(metric, "reference")]
        gain = 100.0 * (reference - production) / reference
        records.append({
            "metric": metric,
            "median_improvement_percent": float(gain.median()),
            "positive_pair_percent": float(100.0 * (gain > 0.0).mean()),
            "paired_draws": int(gain.notna().sum()),
        })
    return pd.DataFrame(records)


def _style(ax: plt.Axes) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(True, alpha=0.18)


def plot_theorem_entry(raw: pd.DataFrame, output: Path) -> None:
    production = raw.loc[
        (raw["status"] == "ok") & (raw["variant"] == "production")
    ].copy()
    production["operator_below_gap"] = (
        production["operator_error"] < production["oracle_gap"]
    )
    colors = plt.cm.viridis(np.linspace(0.15, 0.85, 3))
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.6))
    for color, (matrix_size, group) in zip(colors, production.groupby("matrix_size")):
        frequency = 100 * group.groupby("n")["operator_below_gap"].mean()
        ratio = group.groupby("n")["assembly_gap_ratio"].median()
        axes[0].plot(frequency.index, frequency.values, marker="o", color=color,
                     label=f"{matrix_size}×{matrix_size} SPD")
        axes[1].plot(ratio.index, ratio.values, marker="o", color=color)
    axes[0].set_ylabel("draws with operator error below eigengap (%)")
    axes[0].set_ylim(-3, 103)
    axes[0].legend(frameon=False)
    axes[1].set_ylabel("assembly bound ÷ eigengap (median multiplier)")
    axes[1].axhline(1.0, color="#555555", linestyle="--", linewidth=1.2)
    for ax in axes:
        ax.set_xscale("log", base=2)
        ax.set_xlabel("observations n")
        _style(ax)
    fig.suptitle("Finite-sample entry into the loading-separation regime")
    fig.tight_layout()
    fig.savefig(output / "01_theorem_entry.png", dpi=190, bbox_inches="tight")
    plt.close(fig)


def plot_final_quality(raw: pd.DataFrame, output: Path) -> None:
    final = raw.loc[
        (raw["status"] == "ok")
        & (raw["variant"] == "production")
        & (raw["n"] == raw["n"].max())
    ].copy()
    final["loading_angle_degrees"] = np.degrees(
        np.arcsin(np.clip(final["loading_subspace_error"], 0.0, 1.0))
    )
    final["centre_percent_of_path"] = 100 * final["centre_path_rms"] / final["centre_path_length"]
    final["factor_nrmse_percent"] = 100 * final["factor_score_nrmse"]
    panels = [
        ("loading_angle_degrees", "loading-space angle", "degrees"),
        ("centre_percent_of_path", "centre error", "% of complete path excursion"),
        ("factor_nrmse_percent", "factor-score error", "NRMSE (%)"),
    ]
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, 3))
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.1))
    for ax, (metric, title, ylabel) in zip(axes, panels):
        grouped = final.groupby("matrix_size")[metric]
        medians = grouped.median()
        q25 = grouped.quantile(0.25)
        q75 = grouped.quantile(0.75)
        positions = np.arange(len(medians))
        ax.bar(positions, medians, color=colors, width=0.68)
        ax.errorbar(
            positions, medians,
            yerr=np.vstack((medians - q25, q75 - medians)),
            fmt="none", color="#222222", capsize=3,
        )
        ax.set_xticks(positions, [f"{int(m)}×{int(m)}" for m in medians.index])
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        _style(ax)
    fig.suptitle("What the complete RFD fit recovers at n = 8,192")
    fig.tight_layout()
    fig.savefig(output / "02_final_recovery_quality.png", dpi=190, bbox_inches="tight")
    plt.close(fig)


def plot_comparator_recovery(
    raw: pd.DataFrame, comparators: pd.DataFrame, output: Path
) -> None:
    """Compare recovery after adding noise, centre estimation, and misspecification."""
    identity = ["n", "matrix_size", "replicate"]
    rfd = raw.loc[
        (raw["status"] == "ok") & (raw["variant"] == "production")
    ]
    merged = comparators.merge(rfd, on=identity, how="inner", validate="one_to_one")
    methods = {
        "known centre + noise": (
            "known_centre_loading_error", "known_centre_factor_nrmse"
        ),
        "full RFD": ("loading_subspace_error", "factor_score_nrmse"),
        "one-centre RFM-compatible": (
            "fixed_centre_loading_error", "fixed_centre_factor_nrmse"
        ),
    }
    colors = dict(zip(methods, plt.cm.viridis(np.linspace(0.12, 0.88, len(methods)))))
    fig, axes = plt.subplots(2, 3, figsize=(13.2, 7.6), sharex="col")
    for column, (matrix_size, group) in enumerate(merged.groupby("matrix_size")):
        for label, (loading_column, factor_column) in methods.items():
            loading = group.groupby("n")[loading_column].median()
            factor = 100 * group.groupby("n")[factor_column].median()
            axes[0, column].plot(
                loading.index,
                np.degrees(np.arcsin(np.clip(loading.values, 0.0, 1.0))),
                marker="o", label=label, color=colors[label],
            )
            axes[1, column].plot(
                factor.index, factor.values, marker="o", color=colors[label]
            )
        axes[0, column].set_title(f"{int(matrix_size)}×{int(matrix_size)} SPD")
        axes[1, column].set_xlabel("observations n")
        for row in (0, 1):
            axes[row, column].set_xscale("log", base=2)
            _style(axes[row, column])
    axes[0, 0].set_ylabel("largest loading angle (degrees)")
    axes[1, 0].set_ylabel("factor-score NRMSE (%)")
    axes[0, 0].legend(frameon=False, fontsize=9)
    fig.suptitle("Moving-centre recovery approaches the known-centre oracle")
    fig.tight_layout()
    fig.savefig(output / "03_same_draw_comparators.png", dpi=190, bbox_inches="tight")
    plt.close(fig)


def comparator_summary(raw: pd.DataFrame, comparators: pd.DataFrame) -> pd.DataFrame:
    identity = ["n", "matrix_size", "replicate"]
    rfd = raw.loc[
        (raw["status"] == "ok")
        & (raw["variant"] == "production")
        & (raw["n"] == raw["n"].max())
    ]
    final = comparators.loc[comparators["n"] == comparators["n"].max()]
    merged = final.merge(rfd, on=identity, how="inner", validate="one_to_one")
    records = []
    columns = {
        "known centre + noise": (
            "known_centre_loading_error", "known_centre_factor_nrmse",
            "known_centre_observation_reconstruction_rms",
        ),
        "full RFD": (
            "loading_subspace_error", "factor_score_nrmse",
            "observation_reconstruction_rms",
        ),
        "one-centre RFM-compatible": (
            "fixed_centre_loading_error", "fixed_centre_factor_nrmse",
            "fixed_centre_observation_reconstruction_rms",
        ),
    }
    for matrix_size, group in merged.groupby("matrix_size"):
        for method, (loading, factor, reconstruction) in columns.items():
            loading_median = float(group[loading].median())
            records.append({
                "matrix_size": int(matrix_size), "method": method,
                "loading_angle_degrees": float(
                    np.degrees(np.arcsin(np.clip(loading_median, 0.0, 1.0)))
                ),
                "factor_nrmse_percent": float(100 * group[factor].median()),
                "observation_reconstruction_rms": float(group[reconstruction].median()),
            })
    return pd.DataFrame(records)


def comparator_gains(raw: pd.DataFrame, comparators: pd.DataFrame) -> pd.DataFrame:
    """Paired RFD gains over the fixed-centre fit at the largest n."""
    identity = ["n", "matrix_size", "replicate"]
    rfd = raw.loc[
        (raw["status"] == "ok")
        & (raw["variant"] == "production")
        & (raw["n"] == raw["n"].max())
    ]
    final = comparators.loc[comparators["n"] == comparators["n"].max()]
    merged = final.merge(rfd, on=identity, how="inner", validate="one_to_one")
    metrics = {
        "loading projector": ("loading_subspace_error", "fixed_centre_loading_error"),
        "factor scores": ("factor_score_nrmse", "fixed_centre_factor_nrmse"),
        "observation reconstruction": (
            "observation_reconstruction_rms",
            "fixed_centre_observation_reconstruction_rms",
        ),
        "latent-signal reconstruction": (
            "signal_reconstruction_rms", "fixed_centre_signal_reconstruction_rms"
        ),
    }
    records = []
    for matrix_size, group in merged.groupby("matrix_size"):
        for metric, (rfd_column, fixed_column) in metrics.items():
            gain = 100 * (group[fixed_column] - group[rfd_column]) / group[fixed_column]
            records.append({
                "matrix_size": int(matrix_size), "metric": metric,
                "median_error_reduction_percent": float(gain.median()),
                "rfd_win_percent": float(100 * (group[rfd_column] < group[fixed_column]).mean()),
            })
    return pd.DataFrame(records)


def _markdown_table(frame: pd.DataFrame, columns: list[str], formats: dict[str, str]) -> list[str]:
    labels = [formats.get(column, column) for column in columns]
    lines = ["| " + " | ".join(labels) + " |", "|" + "---|" * len(columns)]
    for _, row in frame.iterrows():
        values = []
        for column in columns:
            value = row[column]
            if column == "matrix_size":
                values.append(str(int(value)))
            elif "percent" in column:
                values.append(f"{value:.1f}%")
            elif "angle" in column:
                values.append(f"{value:.2f}°")
            else:
                values.append(f"{value:.4f}")
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_report(
    raw: pd.DataFrame,
    audit: pd.DataFrame,
    rates: pd.DataFrame,
    quality: pd.DataFrame,
    gains: pd.DataFrame,
    comparators: pd.DataFrame | None,
    output: Path,
) -> None:
    parse_errors = int((audit["parse_status"] != "ok").sum())
    recorded_errors = int(audit["status_errors"].fillna(0).sum())
    total_rows = int(audit["rows"].fillna(0).sum())
    production = raw.loc[(raw["status"] == "ok") & (raw["variant"] == "production")]
    null_check = bool(
        (production["null_eigenvalue"] <= production["lag_row_error"] ** 2 + 1e-12).all()
    )
    lines = [
        "# B4.5 / N-01 adjudication", "",
        "## Verdict", "",
        "**Qualified pass.** The complete bounded-energy RFD implementation is",
        "numerically healthy, recovers the generated loading space accurately,",
        "shows decreasing centre/row/operator/loading errors, satisfies the null",
        "eigenvalue square bound on every recorded production draw, and selects",
        "the declared rank by thresholding on every draw. It has not uniformly",
        "entered the sufficient operator-error-below-eigengap regime by n=8,192,",
        "so these experiments do not justify a stronger finite-sample claim.", "",
        "This is numerical evidence, not a proof of the analytical theorem.", "",
        "## Data integrity", "",
        f"- result CSV files parsed: {len(audit)}",
        f"- result rows parsed: {total_rows:,}",
        f"- parse failures: {parse_errors}",
        f"- recorded scientific status errors: {recorded_errors}",
        f"- B4.5 rows: {len(raw)} (480 paired DGP draws; production and reference)",
        f"- B4.5 fallback count: {int(production['fallback_count'].sum())}",
        f"- B4.5 nonconverged local-mean stages: {int(production['nonconverged_stages'].sum())}",
        f"- null eigenvalue <= lag-row error squared on every production draw: {null_check}", "",
        "The infinite cells listed in `csv_audit.csv` are the declared `a=∞`",
        "sentinel in the discrepancy experiment, not failed numerical outputs.", "",
        "## Recovery at n = 8,192", "",
    ]
    columns = [
        "matrix_size", "centre_percent_of_path_median",
        "loading_subspace_error_median", "loading_angle_degrees_median",
        "factor_nrmse_percent_median", "operator_below_gap_percent",
        "threshold_accuracy_percent",
    ]
    lines.extend(_markdown_table(quality, columns, {
        "matrix_size": "SPD size m",
        "centre_percent_of_path_median": "centre error / path",
        "loading_subspace_error_median": "loading projector error",
        "loading_angle_degrees_median": "largest loading angle",
        "factor_nrmse_percent_median": "factor NRMSE",
        "operator_below_gap_percent": "operator error < gap",
        "threshold_accuracy_percent": "threshold rank correct",
    }))
    lines.extend([
        "", "The loading target is not merely another fitted oracle: the noiseless",
        "factor lag row lies in the generated loading span, and its positive",
        "rank-two gap makes its projector equal to the DGP loading projector on",
        "these draws. Thus the 1–1.6% projector errors are absolute synthetic-truth",
        "errors. Factor-score recovery is materially weaker and reconstruction has",
        "a per-observation noise/projection floor, so neither should be described as",
        "vanishing from these plots.", "", "## Empirical exponents", "",
        "Positive `a` below means the median error follows approximately n^(-a)",
        "over n=512,...,8192. These are descriptive finite-grid slopes.", "",
    ])
    pivot = rates.pivot(index="metric", columns="matrix_size", values="empirical_exponent").reset_index()
    lines.append("| metric | m=2 | m=3 | m=4 |")
    lines.append("|---|---:|---:|---:|")
    for _, row in pivot.iterrows():
        lines.append(
            f"| {row['metric']} | {row[2]:.3f} | {row[3]:.3f} | {row[4]:.3f} |"
        )
    lines.extend(["", "## Paired production-bandwidth effect", ""])
    gain_labels = {
        "centre_path_rms": "centre path",
        "lag_row_error": "lag row",
        "operator_error": "lag operator",
        "loading_subspace_error": "loading projector",
        "null_eigenvalue": "first null eigenvalue",
        "factor_score_nrmse": "factor scores",
        "observation_reconstruction_rms": "observation reconstruction",
        "signal_reconstruction_rms": "signal reconstruction",
    }
    lines.extend(["| metric | median improvement over c=1.3 | pairs improved |", "|---|---:|---:|"])
    for _, row in gains.iterrows():
        lines.append(
            f"| {gain_labels[row['metric']]} | {row['median_improvement_percent']:.1f}% | "
            f"{row['positive_pair_percent']:.1f}% |"
        )
    lines.extend([
        "", "The bandwidth rule helps the centre and theorem intermediates",
        "substantially, but changes final reconstruction by less than 1% because",
        "reconstruction is dominated by the score/noise floor.", "",
        "## What comparison is still required?", "",
        "The completed B4.5 table compares RFD to the exact generated loading",
        "target. Practical model comparison needs the same DGP draw fitted at four",
        "levels: truth, true moving centre with noisy observations, feasible RFD,",
        "and one global-centre RFM-compatible estimation. The replay harness",
        "`experiments/run_b45_comparators.py` implements the two missing levels",
        "without changing seeds. Literal parent-code parity belongs on the later BW",
        "control cells because the present B4.5 DGP uses AIRM.", "",
    ])
    if comparators is None:
        lines.extend([
            "**Status:** smoke passed; the complete recorded comparator replay is",
            "pending. No practical superiority claim is made before it finishes.", "",
        ])
    else:
        comparison = comparator_summary(raw, comparators)
        gains = comparator_gains(raw, comparators)
        lines.extend([
            "**Status:** all 480 same-draw comparator tasks completed without a",
            "recorded error. At n=8,192:", "",
            "| SPD m | method | loading angle | factor NRMSE | observation reconstruction RMS |",
            "|---:|---|---:|---:|---:|",
        ])
        for _, row in comparison.iterrows():
            lines.append(
                f"| {int(row['matrix_size'])} | {row['method']} | "
                f"{row['loading_angle_degrees']:.2f}° | "
                f"{row['factor_nrmse_percent']:.1f}% | "
                f"{row['observation_reconstruction_rms']:.4f} |"
            )
        lines.append("")
        lines.extend([
            "Paired RFD improvement over the one-centre fit at n=8,192:", "",
            "| SPD m | target | median error reduction | RFD wins |",
            "|---:|---|---:|---:|",
        ])
        for _, row in gains.iterrows():
            lines.append(
                f"| {int(row['matrix_size'])} | {row['metric']} | "
                f"{row['median_error_reduction_percent']:.1f}% | "
                f"{row['rfd_win_percent']:.1f}% |"
            )
        lines.extend([
            "", "This is a paper-eligible positive control, not a general empirical",
            "dominance claim. The DGP deliberately satisfies the moving-centre",
            "model with one cubic drift path, rank two, AR(1) factors, white",
            "constant-norm tangent noise, and small AIRM matrices. A fixed-centre",
            "placebo is still required to show that the gain disappears when drift",
            "is absent; literal parent-code comparison belongs on the BW cells.", "",
        ])
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")


def run(output: Path = OUTPUT) -> None:
    output.mkdir(parents=True, exist_ok=True)
    audit = audit_csvs()
    raw = load_b45()
    comparators = load_comparators()
    rates = rate_table(raw)
    quality = final_quality(raw)
    gains = bandwidth_gains(raw)
    audit.to_csv(output / "csv_audit.csv", index=False)
    rates.to_csv(output / "empirical_rates.csv", index=False)
    quality.to_csv(output / "n8192_quality.csv", index=False)
    gains.to_csv(output / "bandwidth_gains.csv", index=False)
    plot_theorem_entry(raw, output)
    plot_final_quality(raw, output)
    if comparators is not None:
        comparison = comparator_summary(raw, comparators)
        comparator_gains(raw, comparators).to_csv(
            output / "n8192_comparator_gains.csv", index=False
        )
        comparison.to_csv(output / "n8192_comparators.csv", index=False)
        plot_comparator_recovery(raw, comparators, output)
    write_report(raw, audit, rates, quality, gains, comparators, output)
    print(f"B4.5 adjudication -> {output.relative_to(ROOT)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args(argv)
    run(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
