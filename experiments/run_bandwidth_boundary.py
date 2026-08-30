"""Extend the B4.2 bandwidth search up to its fixed-overlap boundary.

The completed tuning run remains immutable reference data.  This exploratory
follow-up uses new seed namespaces and respects the n-dependent admissibility
ceiling instead of changing the estimator's overlap rule.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from experiments.run_centre_rate import (
    ROOT,
    build_tasks,
    load_configuration,
    print_workload,
    run,
)


CONFIG_DEFAULT = ROOT / "config" / "centre_bandwidth_boundary.yaml"
REFERENCE_RAW = (
    ROOT / "results" / "intermediate" / "centre_bandwidth_tuning" / "raw.csv"
)
OUTPUT = ROOT / "results" / "intermediate" / "centre_bandwidth_boundary"
PROFILE_NAMES = ("boundary_4096", "boundary_8192")
REFERENCE_MULTIPLIERS = (1.9, 2.1)


def admissible_multiplier_ceiling(config: dict[str, Any], n: int) -> float:
    """Strict multiplier ceiling implied by the fixed overlap."""
    estimator = config["estimator"]
    left, right = map(float, estimator["overlap_fractions"])
    available = min(left, 1.0 - right)
    base = float(estimator["bandwidth_constant"]) * n ** (
        -float(estimator["bandwidth_exponent"])
    )
    return available / base


def complete_raw(config: dict[str, Any]) -> pd.DataFrame:
    raw_path = (ROOT / config["profile"]["output_dir"] / "raw.csv").resolve()
    if not raw_path.exists():
        raise RuntimeError(f"missing result table: {raw_path}")
    raw = pd.read_csv(raw_path)
    expected = len(build_tasks(config)) * len(
        config["profile"]["bandwidth_multipliers"]
    )
    if len(raw) != expected:
        raise RuntimeError(
            f"{config['profile_name']} is incomplete: {len(raw)}/{expected} rows"
        )
    bad = raw.loc[raw["status"] != "ok"]
    if not bad.empty:
        raise RuntimeError(
            f"{config['profile_name']} contains {len(bad)} failed rows"
        )
    return raw


def summarise(raw: pd.DataFrame, source: str) -> pd.DataFrame:
    """Cell medians and interquartile ranges for the zoomed plot."""
    summary = (
        raw.groupby(["n", "bandwidth_multiplier"], sort=True)["path_rms"]
        .agg(
            median="median",
            q25=lambda values: values.quantile(0.25),
            q75=lambda values: values.quantile(0.75),
            replicates="size",
        )
        .reset_index()
    )
    summary["source"] = source
    return summary


def reference_summary() -> pd.DataFrame:
    if not REFERENCE_RAW.exists():
        raise RuntimeError(f"missing completed reference table: {REFERENCE_RAW}")
    raw = pd.read_csv(REFERENCE_RAW)
    keep = raw["bandwidth_multiplier"].isin(REFERENCE_MULTIPLIERS)
    reference = raw.loc[keep & raw["n"].isin((4096, 8192))]
    if len(reference) != 2 * 2 * 32:
        raise RuntimeError("completed reference data do not have the expected shape")
    return summarise(reference, "original tuning (seed namespace 4201)")


def plot_zoom(
    reference: pd.DataFrame,
    extension: pd.DataFrame,
    configs: list[dict[str, Any]],
) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    colours = dict(
        zip((4096, 8192), plt.get_cmap("viridis")(np.linspace(0.2, 0.82, 2)))
    )
    figure, axis = plt.subplots(figsize=(8.2, 4.8))

    for n in (4096, 8192):
        colour = colours[n]
        old = reference.loc[reference["n"] == n].sort_values(
            "bandwidth_multiplier"
        )
        new = extension.loc[extension["n"] == n].sort_values(
            "bandwidth_multiplier"
        )
        axis.errorbar(
            old["bandwidth_multiplier"],
            old["median"],
            yerr=np.vstack((old["median"] - old["q25"], old["q75"] - old["median"])),
            marker="o",
            markerfacecolor="white",
            markeredgewidth=1.8,
            linestyle="-",
            capsize=3,
            color=colour,
            linewidth=1.7,
        )
        axis.errorbar(
            new["bandwidth_multiplier"],
            new["median"],
            yerr=np.vstack((new["median"] - new["q25"], new["q75"] - new["median"])),
            marker="s",
            linestyle="-",
            capsize=3,
            color=colour,
            linewidth=1.7,
        )
        axis.plot(
            [old["bandwidth_multiplier"].iloc[-1], new["bandwidth_multiplier"].iloc[0]],
            [old["median"].iloc[-1], new["median"].iloc[0]],
            linestyle=":",
            color=colour,
            linewidth=1.4,
        )

    for config in configs:
        n = int(config["profile"]["n_values"][0])
        ceiling = admissible_multiplier_ceiling(config, n)
        axis.axvline(
            ceiling,
            color=colours[n],
            linestyle="--",
            linewidth=1.1,
            alpha=0.75,
        )

    legend = [
        Line2D([0], [0], color=colours[4096], marker="s", label="n=4,096"),
        Line2D([0], [0], color=colours[8192], marker="s", label="n=8,192"),
        Line2D(
            [0],
            [0],
            color="#555555",
            marker="o",
            markerfacecolor="white",
            linestyle="-",
            label="original reference",
        ),
        Line2D(
            [0],
            [0],
            color="#555555",
            marker="s",
            linestyle="-",
            label="new extension",
        ),
        Line2D(
            [0],
            [0],
            color="#555555",
            linestyle="--",
            label="admissibility ceiling",
        ),
    ]
    axis.legend(handles=legend, frameon=False, ncol=2)
    axis.set_xlim(1.8, 2.5)
    axis.set_xticks(np.arange(1.8, 2.51, 0.1))
    axis.set(
        title="Bandwidth minimum: boundary extension",
        xlabel="bandwidth multiplier",
        ylabel="median centre error (bars show middle 50%)",
    )
    axis.grid(alpha=0.18)
    figure.tight_layout()
    figure.savefig(OUTPUT / "bandwidth_boundary_zoom.png", dpi=180)
    plt.close(figure)


def write_report(
    reference: pd.DataFrame,
    extension: pd.DataFrame,
    configs: list[dict[str, Any]],
) -> None:
    combined = pd.concat((reference, extension), ignore_index=True)
    combined.to_csv(OUTPUT / "bandwidth_boundary_summary.csv", index=False)
    rows = []
    verdicts = []
    for n, group in combined.groupby("n", sort=True):
        group = group.sort_values("bandwidth_multiplier")
        for item in group.itertuples(index=False):
            rows.append(
                f"| {int(n):,} | {item.bandwidth_multiplier:.2f} | "
                f"{item.median:.6f} | {item.q25:.6f}–{item.q75:.6f} | "
                f"{item.source} |"
            )
        winner = group.loc[group["median"].idxmin()]
        largest = float(group["bandwidth_multiplier"].max())
        verdict = (
            "still decreases at the largest tested admissible point"
            if np.isclose(float(winner["bandwidth_multiplier"]), largest)
            else f"has an observed interior minimum near {winner['bandwidth_multiplier']:.2f}"
        )
        verdicts.append(f"- n={int(n):,}: {verdict}.")

    ceilings = []
    for config in configs:
        n = int(config["profile"]["n_values"][0])
        ceilings.append(
            f"- n={n:,}: strict multiplier ceiling {admissible_multiplier_ceiling(config, n):.3f}."
        )
    report = "\n".join(
        [
            "# B4.2 bandwidth boundary extension",
            "",
            "This is an exploratory continuation, not a rewrite of the frozen 2.1 selection.",
            "The circular reference markers come from seed namespace 4201; square extension markers use independent namespaces 4204/4205. Dotted joins are visual guides only.",
            "",
            "## Fixed-overlap admissibility",
            "",
            *ceilings,
            "",
            "## Observed verdict",
            "",
            *verdicts,
            "",
            "## Cell summaries",
            "",
            "| n | multiplier | median error | middle 50% | source |",
            "|---:|---:|---:|---:|---|",
            *rows,
            "",
            "The minimum is descriptive until any replacement constant is frozen and checked on fresh paired validation data.",
            "",
        ]
    )
    (OUTPUT / "README.md").write_text(report, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configs = [
        load_configuration(args.config.resolve(), profile)
        for profile in PROFILE_NAMES
    ]
    for config in configs:
        n = int(config["profile"]["n_values"][0])
        ceiling = admissible_multiplier_ceiling(config, n)
        largest = max(map(float, config["profile"]["bandwidth_multipliers"]))
        if largest >= ceiling:
            raise RuntimeError(
                f"n={n} candidate {largest} reaches the strict ceiling {ceiling}"
            )

    if args.dry_run:
        for index, config in enumerate(configs, start=1):
            print(f"{index}/{len(configs)} {config['profile_name']}")
            print_workload(config, build_tasks(config))
        return 0

    if not args.report_only:
        for index, config in enumerate(configs, start=1):
            print(
                f"{index}/{len(configs)} {config['profile_name']}",
                flush=True,
            )
            run(config)

    extension = pd.concat(
        [summarise(complete_raw(config), f"extension ({config['profile_name']})") for config in configs],
        ignore_index=True,
    )
    reference = reference_summary()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    plot_zoom(reference, extension, configs)
    write_report(reference, extension, configs)
    print(f"boundary report -> {OUTPUT.relative_to(ROOT)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
