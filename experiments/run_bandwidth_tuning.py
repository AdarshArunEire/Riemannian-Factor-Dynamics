"""Tune and freshly validate the B4.2 finite-sample bandwidth constant.

The tuning and validation stages use distinct SeedSequence namespaces. The
tuning winner is frozen, together with a digest of the complete tuning table,
before validation is run. Repeating the command resumes either stage without
recomputing completed cells.

Run the complete two-stage experiment::

    python experiments/run_bandwidth_tuning.py

Inspect the workloads without writing anything::

    python experiments/run_bandwidth_tuning.py --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from experiments.run_centre_rate import (
    ROOT,
    build_tasks,
    load_configuration,
    print_workload,
    run,
    validate_configuration,
)


CONFIG_DEFAULT = ROOT / "config" / "centre_bandwidth.yaml"
SELECTION_PATH = ROOT / "results" / "intermediate" / "centre_bandwidth_selection.json"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_document(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _output_path(config: dict[str, Any]) -> Path:
    return (ROOT / config["profile"]["output_dir"]).resolve()


def _complete_raw(config: dict[str, Any]) -> pd.DataFrame:
    raw_path = _output_path(config) / "raw.csv"
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


def score_candidates(
    raw: pd.DataFrame,
    candidates: list[float],
) -> pd.DataFrame:
    """Apply the predeclared mean-log-of-cell-medians selection rule."""
    cell = (
        raw.groupby(["bandwidth_multiplier", "n"], sort=True)["path_rms"]
        .median()
        .rename("path_rms_median")
        .reset_index()
    )
    seen = sorted(cell["bandwidth_multiplier"].unique().tolist())
    expected = sorted(float(value) for value in candidates)
    if not np.allclose(seen, expected, rtol=0.0, atol=1e-12):
        raise RuntimeError(
            f"tuning candidates disagree: observed {seen}, expected {expected}"
        )
    if (cell["path_rms_median"] <= 0.0).any():
        raise RuntimeError("path RMS must be positive for mean-log selection")

    scores = (
        cell.assign(log_error=np.log(cell["path_rms_median"]))
        .groupby("bandwidth_multiplier", sort=True)["log_error"]
        .mean()
        .rename("mean_log_median_error")
        .reset_index()
        .sort_values(
            ["mean_log_median_error", "bandwidth_multiplier"],
            kind="stable",
        )
        .reset_index(drop=True)
    )
    best = float(scores.loc[0, "mean_log_median_error"])
    scores["error_above_best_percent"] = 100.0 * (
        np.exp(scores["mean_log_median_error"] - best) - 1.0
    )
    return scores


def freeze_selection(
    config_path: Path,
    tuning_config: dict[str, Any],
) -> dict[str, Any]:
    document = _load_document(config_path)
    candidates = [
        float(value)
        for value in tuning_config["profile"]["bandwidth_multipliers"]
    ]
    raw_path = _output_path(tuning_config) / "raw.csv"
    raw = _complete_raw(tuning_config)
    scores = score_candidates(raw, candidates)
    scores.to_csv(_output_path(tuning_config) / "candidate_scores.csv", index=False)

    winner = float(scores.loc[0, "bandwidth_multiplier"])
    payload = {
        "schema_version": 1,
        "config_sha256": _sha256(config_path),
        "tuning_raw_sha256": _sha256(raw_path),
        "selection_rule": document["selection"],
        "candidates": candidates,
        "winner": winner,
        "winner_at_upper_boundary": bool(np.isclose(winner, max(candidates))),
        "scores": scores.to_dict(orient="records"),
    }

    SELECTION_PATH.parent.mkdir(parents=True, exist_ok=True)
    if SELECTION_PATH.exists():
        existing = json.loads(SELECTION_PATH.read_text(encoding="utf-8"))
        if existing != payload:
            raise RuntimeError(
                "the frozen bandwidth selection disagrees with current tuning "
                f"results; preserve {SELECTION_PATH} and investigate"
            )
    else:
        SELECTION_PATH.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return payload


def validation_configuration(
    config_path: Path,
    winner: float,
) -> dict[str, Any]:
    config = deepcopy(
        load_configuration(config_path, "bandwidth_validate")
    )
    baseline = float(_load_document(config_path)["selection"]["baseline_multiplier"])
    config["profile"]["bandwidth_multipliers"] = sorted({baseline, float(winner)})
    validate_configuration(config)
    return config


def _bootstrap_median_interval(
    values: np.ndarray,
    *,
    seed: int,
    draws: int = 2000,
) -> tuple[float, float]:
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(values), size=(draws, len(values)))
    medians = np.median(values[indices], axis=1)
    return tuple(float(item) for item in np.quantile(medians, [0.025, 0.975]))


def validation_contrasts(
    raw: pd.DataFrame,
    *,
    baseline: float,
    winner: float,
) -> pd.DataFrame:
    records: list[dict[str, float | int]] = []
    for n, group in raw.groupby("n", sort=True):
        errors = group.pivot(
            index="replicate",
            columns="bandwidth_multiplier",
            values="path_rms",
        )
        if baseline not in errors or winner not in errors:
            raise RuntimeError(f"validation cell n={n} lacks a paired multiplier")
        paired_gain = 100.0 * (1.0 - errors[winner] / errors[baseline])
        chosen = group.loc[np.isclose(group["bandwidth_multiplier"], winner)]
        richardson_gain = 100.0 * (
            1.0 - chosen["path_rms"].to_numpy() / chosen["broad_path_rms"].to_numpy()
        )
        low, high = _bootstrap_median_interval(
            paired_gain.to_numpy(),
            seed=420300 + int(n),
        )
        records.append(
            {
                "n": int(n),
                "baseline_multiplier": baseline,
                "winner_multiplier": winner,
                "baseline_path_rms_median": float(errors[baseline].median()),
                "winner_path_rms_median": float(errors[winner].median()),
                "paired_error_reduction_percent_median": float(paired_gain.median()),
                "paired_error_reduction_percent_q025": low,
                "paired_error_reduction_percent_q975": high,
                "winner_richardson_reduction_percent_median": float(
                    np.median(richardson_gain)
                ),
            }
        )
    return pd.DataFrame.from_records(records)


def _plot_tuning(raw: pd.DataFrame, output: Path) -> None:
    cell = (
        raw.groupby(["n", "bandwidth_multiplier"], sort=True)["path_rms"]
        .median()
        .reset_index()
    )
    figure, axis = plt.subplots(figsize=(7.2, 4.4))
    colours = plt.get_cmap("viridis")(
        np.linspace(0.2, 0.82, cell["n"].nunique())
    )
    for colour, (n, group) in zip(colours, cell.groupby("n", sort=True)):
        axis.plot(
            group["bandwidth_multiplier"],
            group["path_rms"],
            marker="o",
            color=colour,
            label=f"n={int(n):,}",
        )
    axis.set(
        title="Bandwidth tuning",
        xlabel="bandwidth multiplier",
        ylabel="median centre error",
    )
    axis.legend(frameon=False)
    axis.grid(alpha=0.2)
    figure.tight_layout()
    figure.savefig(output / "bandwidth_tuning.png", dpi=180)
    plt.close(figure)


def _plot_validation(contrasts: pd.DataFrame, output: Path) -> None:
    x = np.arange(len(contrasts))
    centre = contrasts["paired_error_reduction_percent_median"].to_numpy()
    low = contrasts["paired_error_reduction_percent_q025"].to_numpy()
    high = contrasts["paired_error_reduction_percent_q975"].to_numpy()
    colours = ["#2E8B57" if value >= 0.0 else "#B22222" for value in centre]

    figure, axis = plt.subplots(figsize=(6.8, 4.4))
    axis.bar(x, centre, color=colours, width=0.62)
    axis.errorbar(
        x,
        centre,
        yerr=np.vstack((centre - low, high - centre)),
        fmt="none",
        ecolor="#222222",
        capsize=4,
        linewidth=1.2,
    )
    axis.axhline(0.0, color="#222222", linewidth=1.0)
    axis.set_xticks(x, [f"{int(n):,}" for n in contrasts["n"]])
    axis.set(
        title="Fresh validation: error reduction",
        xlabel="observations",
        ylabel="error reduction versus multiplier 1.0 (%)",
    )
    axis.grid(axis="y", alpha=0.2)
    figure.tight_layout()
    figure.savefig(output / "bandwidth_validation.png", dpi=180)
    plt.close(figure)


def write_adjudication(
    tuning_config: dict[str, Any],
    validation_config: dict[str, Any],
    selection: dict[str, Any],
) -> None:
    tuning_raw = _complete_raw(tuning_config)
    validation_raw = _complete_raw(validation_config)
    winner = float(selection["winner"])
    baseline = float(
        _load_document(validation_config["config_path"])["selection"][
            "baseline_multiplier"
        ]
    )
    contrasts = validation_contrasts(
        validation_raw,
        baseline=baseline,
        winner=winner,
    )
    output = _output_path(validation_config)
    contrasts.to_csv(output / "validation_contrasts.csv", index=False)
    _plot_tuning(tuning_raw, output)
    _plot_validation(contrasts, output)

    score_rows = [
        (
            f"| {float(row['bandwidth_multiplier']):.1f} | "
            f"{float(row['error_above_best_percent']):.2f}% |"
        )
        for row in selection["scores"]
    ]
    contrast_rows = [
        (
            f"| {int(row.n):,} | {row.baseline_path_rms_median:.6f} | "
            f"{row.winner_path_rms_median:.6f} | "
            f"{row.paired_error_reduction_percent_median:+.2f}% "
            f"[{row.paired_error_reduction_percent_q025:+.2f}%, "
            f"{row.paired_error_reduction_percent_q975:+.2f}%] | "
            f"{row.winner_richardson_reduction_percent_median:+.2f}% |"
        )
        for row in contrasts.itertuples(index=False)
    ]
    boundary = (
        "The winner is the largest admissible candidate, so it is a "
        "**constrained winner**, not a bracketed interior optimum."
        if selection["winner_at_upper_boundary"]
        else "The winner is not the upper edge of the candidate grid."
    )
    report = "\n".join(
        [
            "# B4.2 bandwidth constant — frozen validation",
            "",
            f"- frozen winner: **{winner:.1f}×**",
            f"- baseline: **{baseline:.1f}×**",
            f"- tuning rows: {len(tuning_raw)}",
            f"- fresh validation rows: {len(validation_raw)}",
            f"- tuning seed namespace: {tuning_config['profile']['seed_namespace']}",
            (
                "- validation seed namespace: "
                f"{validation_config['profile']['seed_namespace']}"
            ),
            f"- verdict: {boundary}",
            "",
            "## Tuning score",
            "",
            "Lower is better; percentages are geometric error above the winner.",
            "",
            "| multiplier | error above winner |",
            "|---:|---:|",
            *score_rows,
            "",
            "## Fresh paired validation",
            "",
            (
                "Positive error reduction means the frozen winner improves on "
                "multiplier 1.0. Intervals bootstrap the paired median."
            ),
            "",
            (
                "| n | baseline median error | winner median error | "
                "paired reduction [95% interval] | Richardson reduction |"
            ),
            "|---:|---:|---:|---:|---:|",
            *contrast_rows,
            "",
            "This tuning changes only a finite-sample constant. It does not "
            "change the proved or observed n^(-3/7) rate.",
            "",
        ]
    )
    (output / "adjudication.md").write_text(report, encoding="utf-8")
    print(f"frozen bandwidth adjudication -> {output.relative_to(ROOT)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=CONFIG_DEFAULT,
        help="bandwidth tuning YAML",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and print both workloads without writing",
    )
    parser.add_argument(
        "--tune-only",
        action="store_true",
        help="run tuning and freeze the winner, but do not validate",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="rebuild the final report and plots from completed outputs",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    tuning = load_configuration(config_path, "bandwidth_tune")
    validation_placeholder = load_configuration(
        config_path, "bandwidth_validate"
    )

    if args.dry_run:
        print("1/2 independent tuning")
        print_workload(tuning, build_tasks(tuning))
        print("\n2/2 fresh validation")
        print_workload(
            validation_placeholder,
            build_tasks(validation_placeholder),
        )
        print("validation adds the frozen winner to baseline multiplier 1.0")
        return 0

    if not args.report_only:
        print("1/2 independent bandwidth tuning", flush=True)
        run(tuning)
    selection = freeze_selection(config_path, tuning)
    print(
        f"frozen winner: {float(selection['winner']):.1f}× "
        f"(upper boundary: {selection['winner_at_upper_boundary']})",
        flush=True,
    )
    validation = validation_configuration(
        config_path,
        float(selection["winner"]),
    )
    if args.tune_only:
        return 0
    if not args.report_only:
        print("2/2 fresh paired validation", flush=True)
        run(validation)
    write_adjudication(tuning, validation, selection)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
