"""Validate and summarize the paired low-n amplitude diagnostic."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments"))

from run_amplitude_diagnostic import (  # noqa: E402
    CONFIG_DEFAULT,
    VARIANTS,
    build_tasks,
    load_configuration,
)


LABELS = {
    "ot": "oracle rows + true directions",
    "oo": "oracle rows + oracle-fit directions",
    "ft": "RFD rows + true directions",
    "of": "oracle rows + RFD directions",
    "ff": "complete RFD",
    "fixed": "fixed-centre comparator",
}


def validate_raw(raw: pd.DataFrame, config: dict[str, Any], allow_incomplete: bool) -> None:
    required = {(task.n, task.replicate) for task in build_tasks(config)}
    keys = list(zip(raw["n"].astype(int), raw["replicate"].astype(int)))
    if len(keys) != len(set(keys)):
        raise ValueError("raw diagnostic contains duplicate (n, replicate) rows")
    unexpected = set(keys) - required
    if unexpected:
        raise ValueError(f"raw diagnostic contains unexpected keys: {sorted(unexpected)[:3]}")
    missing = required - set(keys)
    if missing and not allow_incomplete:
        raise ValueError(f"diagnostic is incomplete: {len(missing)} rows missing")
    errors = raw.loc[raw["status"] != "ok"]
    if not errors.empty:
        raise ValueError(f"diagnostic contains {len(errors)} error rows")


def bootstrap_median_ci(
    values: np.ndarray, *, draws: int, seed: int
) -> tuple[float, float]:
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if values.size == 0:
        return np.nan, np.nan
    rng = np.random.default_rng(seed)
    sampled = rng.choice(values, size=(draws, values.size), replace=True)
    medians = np.median(sampled, axis=1)
    return float(np.quantile(medians, .025)), float(np.quantile(medians, .975))


def make_long(raw: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, source in raw.iterrows():
        for variant in VARIANTS:
            rows.append({
                "n": int(source["n"]), "replicate": int(source["replicate"]),
                "variant": variant, "label": LABELS[variant],
                "nrmse": float(source[f"{variant}_nrmse"]),
                "calibrated_nrmse": float(source[f"{variant}_calibrated_nrmse"]),
                "norm_ratio": float(source[f"{variant}_norm_ratio"]),
                "cosine": float(source[f"{variant}_cosine"]),
                "scale": float(source[f"{variant}_scale"]),
            })
        rows.append({
            "n": int(source["n"]), "replicate": int(source["replicate"]),
            "variant": "fixed", "label": LABELS["fixed"],
            "nrmse": float(source["fixed_nrmse"]),
            "calibrated_nrmse": np.nan, "norm_ratio": np.nan,
            "cosine": np.nan, "scale": np.nan,
        })
    return pd.DataFrame(rows)


def summarize(long: pd.DataFrame) -> pd.DataFrame:
    records = []
    for (n, variant, label), group in long.groupby(["n", "variant", "label"]):
        record: dict[str, Any] = {
            "n": int(n), "variant": variant, "label": label,
            "replicates": len(group),
        }
        for metric in ("nrmse", "calibrated_nrmse", "norm_ratio", "cosine", "scale"):
            values = pd.to_numeric(group[metric], errors="coerce")
            record[f"{metric}_mean"] = float(values.mean())
            record[f"{metric}_median"] = float(values.median())
            record[f"{metric}_q25"] = float(values.quantile(.25))
            record[f"{metric}_q75"] = float(values.quantile(.75))
        records.append(record)
    return pd.DataFrame(records).sort_values(["n", "variant"])


def paired_attribution(raw: pd.DataFrame, config: dict[str, Any]) -> pd.DataFrame:
    draws = int(config["analysis"]["bootstrap_replicates"])
    root_seed = int(config["analysis"]["bootstrap_seed"])
    records = []
    contrasts = {
        "row cost at true directions": lambda g: g["ft_nrmse"] - g["ot_nrmse"],
        "RFD-direction cost on oracle rows": lambda g: g["of_nrmse"] - g["ot_nrmse"],
        "row-direction interaction": lambda g: (
            g["ff_nrmse"] - g["ft_nrmse"] - g["of_nrmse"] + g["ot_nrmse"]
        ),
        "complete excess over noise floor": lambda g: g["ff_nrmse"] - g["ot_nrmse"],
        "oracle direction-estimation cost": lambda g: g["oo_nrmse"] - g["ot_nrmse"],
        "RFD scalar-calibration gain": lambda g: (
            g["ff_nrmse"] - g["ff_calibrated_nrmse"]
        ),
    }
    for n, group in raw.groupby("n"):
        for offset, (name, function) in enumerate(contrasts.items()):
            values = np.asarray(function(group), dtype=float)
            low, high = bootstrap_median_ci(
                values, draws=draws, seed=root_seed + 100 * int(n) + offset
            )
            records.append({
                "n": int(n), "contrast": name, "replicates": values.size,
                "median": float(np.median(values)), "mean": float(np.mean(values)),
                "ci_low": low, "ci_high": high,
            })
    return pd.DataFrame(records)


def _style_axis(axis) -> None:
    axis.spines[["top", "right"]].set_visible(False)
    axis.grid(alpha=.18)


def plot_nrmse(summary: pd.DataFrame, output: Path) -> None:
    order = ["ot", "oo", "ft", "of", "ff", "fixed"]
    colours = plt.cm.viridis(np.linspace(.08, .92, len(order)))
    figure, axis = plt.subplots(figsize=(9.4, 5.4))
    for colour, variant in zip(colours, order):
        subset = summary.loc[summary["variant"] == variant].sort_values("n")
        axis.plot(
            subset["n"], subset["nrmse_median"], marker="o", linewidth=2,
            color=colour, label=LABELS[variant],
        )
        axis.fill_between(
            subset["n"], subset["nrmse_q25"], subset["nrmse_q75"],
            color=colour, alpha=.10,
        )
    axis.set_xscale("log", base=2)
    axis.set_xticks(sorted(summary["n"].unique()))
    axis.set_xticklabels([f"{int(n):,}" for n in sorted(summary["n"].unique())])
    axis.set_xlabel("observations")
    axis.set_ylabel("factor-score error (NRMSE)")
    axis.set_title("Where low-sample factor-score error enters")
    axis.legend(frameon=False, fontsize=8, ncol=2)
    _style_axis(axis)
    figure.tight_layout()
    figure.savefig(output / "factor_score_attribution.png", dpi=180)
    plt.close(figure)


def plot_attribution(attribution: pd.DataFrame, output: Path) -> None:
    names = [
        "row cost at true directions",
        "RFD-direction cost on oracle rows",
        "row-direction interaction",
    ]
    labels = ["centre/frame rows", "loading directions", "interaction"]
    colours = plt.cm.viridis([.20, .52, .84])
    n_values = sorted(attribution["n"].unique())
    x = np.arange(len(n_values), dtype=float)
    width = .24
    figure, axis = plt.subplots(figsize=(8.8, 5.2))
    for index, (name, label, colour) in enumerate(zip(names, labels, colours)):
        subset = attribution.loc[attribution["contrast"] == name].set_index("n").loc[n_values]
        positions = x + (index - 1) * width
        values = subset["median"].to_numpy()
        errors = np.vstack((values - subset["ci_low"], subset["ci_high"] - values))
        axis.bar(positions, values, width, color=colour, label=label)
        axis.errorbar(positions, values, yerr=errors, fmt="none", color="black", capsize=3)
    axis.axhline(0, color="black", linewidth=.8)
    axis.set_xticks(x, [f"{int(n):,}" for n in n_values])
    axis.set_xlabel("observations")
    axis.set_ylabel("paired change in NRMSE")
    axis.set_title("Descriptive 2×2 attribution")
    axis.legend(frameon=False)
    _style_axis(axis)
    figure.tight_layout()
    figure.savefig(output / "paired_error_attribution.png", dpi=180)
    plt.close(figure)


def plot_calibration(summary: pd.DataFrame, output: Path) -> None:
    subset = summary.loc[summary["variant"] == "ff"].sort_values("n")
    x = np.arange(len(subset), dtype=float)
    figure, axis = plt.subplots(figsize=(8.2, 4.9))
    colours = plt.cm.viridis([.25, .75])
    axis.bar(x - .18, subset["nrmse_median"], .36, color=colours[0], label="as estimated")
    axis.bar(
        x + .18, subset["calibrated_nrmse_median"], .36,
        color=colours[1], label="after one best scalar",
    )
    axis.set_xticks(x, [f"{int(n):,}" for n in subset["n"]])
    axis.set_xlabel("observations")
    axis.set_ylabel("factor-score error (NRMSE)")
    axis.set_title("Is the amplitude error mostly uniform damping?")
    axis.legend(frameon=False)
    _style_axis(axis)
    figure.tight_layout()
    figure.savefig(output / "scalar_damping_diagnostic.png", dpi=180)
    plt.close(figure)


def verdict(attribution: pd.DataFrame, summary: pd.DataFrame) -> list[str]:
    lines = []
    for n in sorted(attribution["n"].unique()):
        table = attribution.loc[attribution["n"] == n].set_index("contrast")
        candidates = {
            "centre/frame rows": float(table.loc["row cost at true directions", "median"]),
            "loading directions": float(table.loc["RFD-direction cost on oracle rows", "median"]),
            "row-loading interaction": float(table.loc["row-direction interaction", "median"]),
        }
        largest = max(candidates, key=lambda key: abs(candidates[key]))
        ff = summary.loc[(summary["n"] == n) & (summary["variant"] == "ff")].iloc[0]
        gain = float(ff["nrmse_median"] - ff["calibrated_nrmse_median"])
        lines.append(
            f"- n={int(n):,}: largest descriptive contrast is **{largest}** "
            f"({candidates[largest]:+.3f} NRMSE); one scalar removes {gain:.3f} NRMSE."
        )
    return lines


def write_report(
    raw: pd.DataFrame, summary: pd.DataFrame, attribution: pd.DataFrame,
    output: Path, complete: bool,
) -> None:
    report = [
        "# Low-n factor-amplitude diagnosis", "",
        ("**Complete paired diagnostic.**" if complete else "**Provisional: incomplete run.**"),
        "", "## Reading the experiment", "",
        "OT is the irreducible noisy-oracle floor. FT changes only the centre/frame rows; "
        "OF changes only the loading directions; FF changes both and is complete RFD. "
        "OO estimates loading directions from oracle rows. Contrasts are paired on identical draws.",
        "",
        "The 2×2 numbers are descriptive contrasts of a nonlinear error metric, not "
        "variance shares and not a proof of causality.", "", "## Automated read", "",
        *verdict(attribution, summary), "", "## Scalar-damping test", "",
        "The calibrated score permits only one post-hoc scalar after the usual orthogonal "
        "gauge alignment. A large reduction means uniform attenuation is important; a "
        "large remaining error means trajectory shape is also wrong. This diagnostic does "
        "not install or tune a correction.", "", "## Outputs", "",
        "- `summary.csv`: mean, median, and interquartile range by estimator variant.",
        "- `paired_attribution.csv`: paired medians and bootstrap 95% intervals.",
        "- `factor_score_attribution.png`: all estimator paths.",
        "- `paired_error_attribution.png`: row/loading/interaction contrasts.",
        "- `scalar_damping_diagnostic.png`: raw versus scalar-calibrated RFD.", "",
        f"Rows analysed: {len(raw)}.",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")


def analyze(config: dict[str, Any], *, allow_incomplete: bool = False) -> Path:
    input_dir = (ROOT / config["profile"]["output_dir"]).resolve()
    raw_path = input_dir / "raw.csv"
    if not raw_path.exists():
        raise FileNotFoundError(raw_path)
    raw = pd.read_csv(raw_path)
    validate_raw(raw, config, allow_incomplete)
    output = (
        ROOT / "results" / "final" / "amplitude_diagnostic"
        if config["profile_name"] == "diagnostic"
        else ROOT / "tmp" / f"amplitude_diagnostic_{config['profile_name']}_analysis"
    )
    output.mkdir(parents=True, exist_ok=True)
    long = make_long(raw)
    table = summarize(long)
    attribution = paired_attribution(raw, config)
    long.to_csv(output / "long_metrics.csv", index=False)
    table.to_csv(output / "summary.csv", index=False)
    attribution.to_csv(output / "paired_attribution.csv", index=False)
    plot_nrmse(table, output)
    plot_attribution(attribution, output)
    plot_calibration(table, output)
    complete = len(raw) == len(build_tasks(config))
    write_report(raw, table, attribution, output, complete)
    print(f"analysed {len(raw)} paired draws")
    print(f"output: {output}")
    return output


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--profile", choices=("smoke", "calibration", "diagnostic"), default="diagnostic")
    parser.add_argument("--allow-incomplete", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_configuration(args.config.resolve(), args.profile)
    analyze(config, allow_incomplete=args.allow_incomplete)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
