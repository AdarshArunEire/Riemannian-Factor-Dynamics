"""Summarise the APP-FIN-matched known-centre tournament."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


VIRIDIS = plt.colormaps["viridis"]


def _markdown_table(frame: pd.DataFrame) -> str:
    """Render a compact Markdown table without pandas' optional tabulate extra."""
    printable = frame.copy()
    for column in printable.select_dtypes(include=[np.number]).columns:
        printable[column] = printable[column].map(lambda value: f"{value:.5g}")
    columns = printable.columns.astype(str).tolist()
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    lines.extend(
        "| " + " | ".join(map(str, row)) + " |"
        for row in printable.itertuples(index=False, name=None)
    )
    return "\n".join(lines)


def analyze(output: Path) -> None:
    scores = pd.read_csv(output / "scores.csv")
    required = {
        "method", "n", "distribution", "replicate", "centre_bw_rms",
        "proxy_bw_rms", "mean_qlike_to_truth", "minimum_eigenvalue",
        "maximum_condition_number",
    }
    if required - set(scores):
        raise RuntimeError(f"score table is missing {sorted(required - set(scores))}")
    if scores[list(required - {"method", "distribution"})].isna().any().any():
        raise RuntimeError("score table contains missing numerical values")

    summary = (
        scores.groupby(["n", "distribution", "method"], sort=True)
        .agg(
            replicates=("replicate", "nunique"),
            median_centre_bw_rms=("centre_bw_rms", "median"),
            q25_centre_bw_rms=("centre_bw_rms", lambda x: x.quantile(0.25)),
            q75_centre_bw_rms=("centre_bw_rms", lambda x: x.quantile(0.75)),
            median_qlike=("mean_qlike_to_truth", "median"),
            median_proxy_fit=("proxy_bw_rms", "median"),
            minimum_eigenvalue=("minimum_eigenvalue", "min"),
            maximum_condition_number=("maximum_condition_number", "max"),
        )
        .reset_index()
    )
    baseline = summary[summary["method"].eq("global")][
        ["n", "distribution", "median_centre_bw_rms"]
    ].rename(columns={"median_centre_bw_rms": "global_bw_rms"})
    summary = summary.merge(baseline, on=["n", "distribution"], how="left")
    summary["bw_error_reduction_percent_vs_global"] = 100.0 * (
        1.0 - summary["median_centre_bw_rms"] ** 2 / summary["global_bw_rms"] ** 2
    )
    summary.to_csv(output / "summary.csv", index=False)

    methods = [
        "global", "positive_local", "positive_shrink_0.6",
        "richardson", "richardson_shrink_0.2", "graph_smooth_1",
        "piecewise_6", "tangent_trend",
        "segmented_polygon_6",
    ]
    display_names = {
        "global": "global", "positive_local": "positive local",
        "positive_shrink_0.6": "positive shrink", "richardson": "Richardson",
        "richardson_shrink_0.2": "Richardson shrink", "graph_smooth_1": "graph smooth",
        "piecewise_6": "piecewise 6", "tangent_trend": "tangent trend",
        "segmented_polygon_6": "six-centre polygon",
    }
    scenarios = summary[["n", "distribution"]].drop_duplicates().itertuples(index=False)
    scenarios = list(scenarios)
    fig, axes = plt.subplots(1, len(scenarios), figsize=(6.2 * len(scenarios), 5.2), squeeze=False)
    for axis, scenario in zip(axes[0], scenarios, strict=True):
        selected = summary[
            summary["n"].eq(scenario.n) & summary["distribution"].eq(scenario.distribution)
        ].set_index("method")
        available = [method for method in methods if method in selected.index]
        values = selected.loc[available, "bw_error_reduction_percent_vs_global"]
        colours = [VIRIDIS(index / max(1, len(available) - 1)) for index in range(len(available))]
        axis.barh(range(len(available)), values, color=colours)
        axis.axvline(0.0, color="0.3", linewidth=1)
        axis.set_yticks(range(len(available)), [display_names[x] for x in available])
        axis.set_xlabel("known-centre BW error reduction vs global (%)")
        axis.set_title(f"{scenario.distribution.replace('_', ' ')}, n={scenario.n:,}")
    fig.suptitle("APP-FIN-matched centre tournament")
    fig.tight_layout()
    fig.savefig(output / "matched_centre_tournament.png", dpi=180)
    fig.savefig(output / "matched_centre_tournament.svg")
    plt.close(fig)

    diagnostics = json.loads((output / "diagnostics.json").read_text(encoding="utf-8"))
    health = pd.DataFrame([
        {"n": item["n"], "distribution": item["distribution"], **item["data_health"]}
        for item in diagnostics
    ])
    health_summary = health.groupby(["n", "distribution"]).agg(
        truth_minimum_eigenvalue=("truth_minimum_eigenvalue", "min"),
        truth_maximum_condition_number=("truth_maximum_condition_number", "max"),
        proxy_minimum_eigenvalue=("proxy_minimum_eigenvalue", "min"),
        proxy_maximum_condition_number=("proxy_maximum_condition_number", "max"),
    ).reset_index()
    health_summary.to_csv(output / "data_health.csv", index=False)

    lines = [
        "# APP-FIN-matched known-centre tournament", "",
        "This experiment gives every method the same finite-window covariance proxies and scores it against the known conditional BW centre. It contains no factors, rank selection, or forecasting.", "",
        "## Verdict", "",
    ]
    for (n, distribution), group in summary.groupby(["n", "distribution"]):
        ranked = group.sort_values("median_centre_bw_rms")
        winner = ranked.iloc[0]
        rich = group[group["method"].eq("richardson")].iloc[0]
        lines.extend([
            f"- **{distribution.replace('_', ' ')}, n={int(n):,}:** {display_names.get(winner.method, winner.method)} wins with median known-centre BW RMS {winner.median_centre_bw_rms:.4g} ({winner.bw_error_reduction_percent_vs_global:+.1f}% squared-error change versus global). Raw Richardson gives {rich.median_centre_bw_rms:.4g} ({rich.bw_error_reduction_percent_vs_global:+.1f}%).",
        ])
    lines.extend(["", "## Method table", "", _markdown_table(summary), "", "## Data health", "", _markdown_table(health_summary), ""])
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {output / 'report.md'}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    analyze(parser.parse_args().output)
