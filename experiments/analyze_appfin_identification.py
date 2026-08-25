"""Analysis and plots for the APP-FIN fixed-rank identification run."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))

from rfd.estimators.lag import tangent_coordinates  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402


VIRIDIS = plt.colormaps["viridis"]
COLOURS = {
    "rfd": VIRIDIS(0.12),
    "parent_verified": VIRIDIS(0.55),
    "parent_budget": VIRIDIS(0.88),
    "vix": "#7f3c8d",
    "outside": "#d95f02",
}


def _load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as source:
        return {name: source[name].copy() for name in source.files}


def _bw_rms(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.sqrt(np.mean(BW_GEOMETRY.dist2(left, right))))


def _relative_frobenius_rms(estimate: np.ndarray, truth: np.ndarray) -> float:
    error = np.linalg.norm(estimate - truth, axis=(-2, -1))
    scale = np.linalg.norm(truth, axis=(-2, -1))
    return float(np.sqrt(np.mean(error**2)) / np.sqrt(np.mean(scale**2)))


def _parent_primary_reconstruction(
    parent: dict[str, np.ndarray], prefix: str, rank: int
) -> np.ndarray:
    tangent = (
        parent[f"{prefix}_row_mean_tangent"]
        + np.tensordot(
            parent[f"{prefix}_scores"][:, :rank],
            parent[f"{prefix}_loadings"][:rank],
            axes=(-1, 0),
        )
    )
    return BW_GEOMETRY.exp(parent[f"{prefix}_mean"], tangent)


def _rank_curve(rows: np.ndarray, scores: np.ndarray, max_rank: int) -> np.ndarray:
    centred = rows - rows.mean(axis=0, keepdims=True)
    total = float(np.sum(centred**2))
    if total <= 0.0:
        raise ValueError("rank sensitivity requires positive tangent variation")
    removed = np.cumsum(np.sum(scores[:, :max_rank] ** 2, axis=0))
    return np.clip((total - removed) / total, 0.0, 1.0)


def _orthonormal_columns(rows: np.ndarray) -> np.ndarray:
    rows = np.asarray(rows, dtype=float)
    if rows.ndim != 2 or rows.shape[0] < 1:
        raise ValueError("loading rows must be a nonempty matrix")
    q, r = np.linalg.qr(rows.T, mode="reduced")
    if np.min(np.abs(np.diag(r))) <= 1e-10:
        raise ValueError("loading rows are numerically rank deficient")
    return q


def _loading_comparison(
    parent: dict[str, np.ndarray], rfd: dict[str, np.ndarray], max_rank: int
) -> pd.DataFrame:
    transported = BW_GEOMETRY.transport(
        parent["converged_loadings"][:max_rank],
        parent["converged_mean"],
        rfd["reference_point"],
    )
    parent_rows = tangent_coordinates(
        transported,
        rfd["reference_point"],
        rfd["basis"],
        BW_GEOMETRY,
    )
    records = []
    for rank in range(1, max_rank + 1):
        parent_q = _orthonormal_columns(parent_rows[:rank])
        rfd_q = rfd["eigenvectors"][:, :rank]
        singular = np.linalg.svd(parent_q.T @ rfd_q, compute_uv=False)
        singular = np.clip(singular, 0.0, 1.0)
        angles = np.arccos(singular)
        records.append({
            "rank": rank,
            "largest_principal_angle_degrees": float(np.degrees(np.max(angles))),
            "projector_operator_distance": float(np.sin(np.max(angles))),
            "projector_frobenius_distance": float(
                np.linalg.norm(parent_q @ parent_q.T - rfd_q @ rfd_q.T, ord="fro")
            ),
        })
    return pd.DataFrame(records)


def _centre_decomposition(
    parent: dict[str, np.ndarray], rfd: dict[str, np.ndarray], rank: int
) -> tuple[pd.DataFrame, dict[str, float]]:
    mean = parent["converged_mean"]
    basis = BW_GEOMETRY.tangent_basis(mean)
    drift_vectors = BW_GEOMETRY.log(mean, rfd["local_centres"])
    drift_rows = tangent_coordinates(drift_vectors, mean, basis, BW_GEOMETRY)
    parent_loading_rows = tangent_coordinates(
        parent["converged_loadings"][:rank], mean, basis, BW_GEOMETRY
    )
    q = _orthonormal_columns(parent_loading_rows)
    inside_rows = drift_rows @ q @ q.T
    outside_rows = drift_rows - inside_rows
    inside = np.linalg.norm(inside_rows, axis=1)
    outside = np.linalg.norm(outside_rows, axis=1)
    total = np.linalg.norm(drift_rows, axis=1)
    total_energy = float(np.sum(total**2))
    inside_energy = float(np.sum(inside**2))
    outside_energy = float(np.sum(outside**2))
    summary = {
        "inside_parent_rank2_energy_percent": 100.0 * inside_energy / total_energy,
        "outside_parent_rank2_energy_percent": 100.0 * outside_energy / total_energy,
        "centre_displacement_rms": float(np.sqrt(np.mean(total**2))),
        "centre_displacement_max": float(np.max(total)),
    }
    return pd.DataFrame({
        "centre_displacement": total,
        "inside_parent_rank2": inside,
        "outside_parent_rank2": outside,
    }), summary


def _load_vix(path: Path, months: np.ndarray) -> np.ndarray:
    frame = pd.read_csv(path)
    frame["DATE"] = pd.to_datetime(frame["DATE"], errors="coerce")
    frame["VIXCLS"] = pd.to_numeric(frame["VIXCLS"], errors="coerce")
    frame = frame.dropna(subset=["DATE", "VIXCLS"])
    frame["month"] = frame["DATE"].dt.to_period("M").astype(str)
    monthly = frame.groupby("month")["VIXCLS"].mean()
    result = monthly.reindex(months.astype(str)).to_numpy(dtype=float)
    if not np.isfinite(result).all():
        missing = months[~np.isfinite(result)]
        raise ValueError(f"VIX is missing APP-FIN months: {missing.tolist()}")
    return result


def _standardize(value: np.ndarray) -> np.ndarray:
    value = np.asarray(value, dtype=float)
    scale = value.std(ddof=1)
    if not np.isfinite(scale) or scale <= 0.0:
        raise ValueError("cannot standardize a constant series")
    return (value - value.mean()) / scale


def _orient_to(reference: np.ndarray, value: np.ndarray) -> tuple[np.ndarray, float]:
    correlation = float(np.corrcoef(reference, value)[0, 1])
    sign = 1.0 if correlation >= 0.0 else -1.0
    return sign * value, abs(correlation)


def _path_length(vertices: np.ndarray) -> float:
    return float(np.sqrt(BW_GEOMETRY.dist2(vertices[:-1], vertices[1:])).sum())


def _minimum_eigenvalue(values: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(values).min())


def _style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 180,
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def _save(fig, output: Path, name: str) -> None:
    fig.tight_layout()
    fig.savefig(output / f"{name}.png", bbox_inches="tight")
    fig.savefig(output / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def _plots(
    output: Path,
    rank_table: pd.DataFrame,
    time_table: pd.DataFrame,
    loading_table: pd.DataFrame,
    primary_rank: int,
) -> None:
    _style()
    fig, ax = plt.subplots(figsize=(8, 4.6))
    for column, label, colour, style in (
        ("rfd_tangent_fvu_percent", "RFD", COLOURS["rfd"], "-"),
        ("parent_verified_tangent_fvu_percent", "parent, verified mean", COLOURS["parent_verified"], "--"),
        ("parent_budget_tangent_fvu_percent", "parent, published mean budget", COLOURS["parent_budget"], ":"),
    ):
        ax.plot(rank_table["rank"], rank_table[column], marker="o", color=colour, linestyle=style, label=label)
    ax.axvline(primary_rank, color="0.45", linewidth=1, linestyle="--")
    ax.set(xlabel="retained persistent directions", ylabel="tangent variation left (%)", title="Rank sensitivity, not rank selection")
    ax.set_xticks(rank_table["rank"])
    ax.legend(frameon=False)
    _save(fig, output, "rank_sensitivity")

    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(time_table["month"], time_table["inside_parent_rank2"], color=COLOURS["parent_verified"], label="inside parent rank-2 space")
    ax.plot(time_table["month"], time_table["outside_parent_rank2"], color=COLOURS["outside"], label="outside parent rank-2 space")
    ax.set(xlabel="month", ylabel="BW tangent magnitude", title="Where the estimated centre motion sits")
    ticks = np.linspace(0, len(time_table) - 1, 9, dtype=int)
    ax.set_xticks(ticks, time_table.loc[ticks, "month"], rotation=30, ha="right")
    ax.legend(frameon=False)
    _save(fig, output, "centre_motion_decomposition")

    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(time_table["month"], time_table["parent_factor1_z"], color=COLOURS["parent_verified"], alpha=0.85, label="parent Factor 1")
    ax.plot(time_table["month"], time_table["rfd_factor1_z"], color=COLOURS["rfd"], alpha=0.85, label="RFD Factor 1")
    ax.plot(time_table["month"], time_table["vix_z"], color=COLOURS["vix"], linewidth=1.5, label="VIX")
    ax.set(xlabel="month", ylabel="standard deviations", title="Factor 1 after orienting its arbitrary sign toward VIX")
    ticks = np.linspace(0, len(time_table) - 1, 9, dtype=int)
    ax.set_xticks(ticks, time_table.loc[ticks, "month"], rotation=30, ha="right")
    ax.legend(frameon=False, ncol=3)
    _save(fig, output, "factor1_vix")

    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(loading_table["rank"], loading_table["largest_principal_angle_degrees"], color=COLOURS["rfd"], marker="o")
    ax.axvline(primary_rank, color="0.45", linewidth=1, linestyle="--")
    ax.set(xlabel="compared rank", ylabel="largest principal angle (degrees)", title="Fixed-centre and moving-centre loading spaces")
    ax.set_xticks(loading_table["rank"])
    _save(fig, output, "loading_space_sensitivity")


def analyze(
    root: Path,
    config: dict[str, Any],
    panel: dict[str, np.ndarray],
    output: Path,
) -> None:
    parent = _load_npz(output / "parent_fit.npz")
    rfd = _load_npz(output / "rfd_fit.npz")
    observations = np.asarray(panel["panel"], dtype=float)
    months = panel["months"].astype(str)
    primary_rank = int(config["experiment"]["primary_rank"])
    max_rank = int(config["experiment"]["sensitivity_max_rank"])

    parent_budget_primary = _parent_primary_reconstruction(parent, "budget", primary_rank)
    parent_verified_primary = _parent_primary_reconstruction(parent, "converged", primary_rank)
    rfd_primary = rfd["primary_rank_reconstruction"]

    rank_table = pd.DataFrame({"rank": np.arange(1, max_rank + 1)})
    rank_table["rfd_tangent_fvu_percent"] = 100 * _rank_curve(rfd["tangent_rows"], rfd["scores"], max_rank)
    for prefix, label in (("budget", "parent_budget"), ("converged", "parent_verified")):
        rank_table[f"{label}_tangent_fvu_percent"] = 100 * _rank_curve(
            parent[f"{prefix}_log_rows"], parent[f"{prefix}_scores"], max_rank
        )

    loading_table = _loading_comparison(parent, rfd, max_rank)
    centre_table, centre_summary = _centre_decomposition(parent, rfd, primary_rank)
    vix = _load_vix(root / config["experiment"]["vix_path"], months)
    vix_z = _standardize(vix)
    parent_factor, parent_vix_correlation = _orient_to(vix_z, _standardize(parent["converged_scores"][:, 0]))
    rfd_factor, rfd_vix_correlation = _orient_to(vix_z, _standardize(rfd["scores"][:, 0]))
    centre_vix_correlation = float(np.corrcoef(vix_z, centre_table["centre_displacement"])[0, 1])

    time_table = pd.DataFrame({
        "month": months,
        "vix": vix,
        "vix_z": vix_z,
        "parent_factor1_z": parent_factor,
        "rfd_factor1_z": rfd_factor,
    })
    time_table = pd.concat([time_table, centre_table], axis=1)

    parent_fixed = np.broadcast_to(parent["converged_mean"], observations.shape)
    budget_fixed = np.broadcast_to(parent["budget_mean"], observations.shape)
    reconstructions = {
        "parent_budget_centre_only": budget_fixed,
        "parent_verified_centre_only": parent_fixed,
        "rfd_centre_only": rfd["local_centres"],
        "parent_budget_rank2": parent_budget_primary,
        "parent_verified_rank2": parent_verified_primary,
        "rfd_rank2": rfd_primary,
    }
    primary_rows = []
    for name, estimate in reconstructions.items():
        primary_rows.append({
            "representation": name,
            "bw_rms_to_observation": _bw_rms(estimate, observations),
            "relative_frobenius_rms": _relative_frobenius_rms(estimate, observations),
            "minimum_reconstruction_eigenvalue": _minimum_eigenvalue(estimate),
        })
    primary_table = pd.DataFrame(primary_rows)

    numerics = {
        **centre_summary,
        "rfd_centre_path_length": _path_length(rfd["vertices"]),
        "parent_budget_vs_verified_mean_bw_distance": float(np.sqrt(BW_GEOMETRY.dist2(parent["budget_mean"], parent["converged_mean"]))),
        "parent_factor1_absolute_vix_correlation": parent_vix_correlation,
        "rfd_factor1_absolute_vix_correlation": rfd_vix_correlation,
        "centre_displacement_vix_correlation": centre_vix_correlation,
        "observation_minimum_eigenvalue": _minimum_eigenvalue(observations),
        "rfd_vertex_minimum_eigenvalue": _minimum_eigenvalue(rfd["vertices"]),
        "rfd_local_centre_minimum_eigenvalue": _minimum_eigenvalue(rfd["local_centres"]),
        "parent_verified_mean_minimum_eigenvalue": _minimum_eigenvalue(parent["converged_mean"]),
        "primary_rank_loading_angle_degrees": float(loading_table.loc[loading_table["rank"].eq(primary_rank), "largest_principal_angle_degrees"].iloc[0]),
    }
    rfd_meta = json.loads((output / "rfd_fit.meta.json").read_text(encoding="utf-8"))
    numerics.update({f"rfd_{key}": value for key, value in rfd_meta["diagnostics"].items() if key != "fallback_reasons"})

    rank_table.to_csv(output / "rank_sensitivity.csv", index=False)
    loading_table.to_csv(output / "loading_space_sensitivity.csv", index=False)
    time_table.to_csv(output / "time_series.csv", index=False)
    primary_table.to_csv(output / "primary_reconstruction.csv", index=False)
    (output / "diagnostics.json").write_text(json.dumps(numerics, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _plots(output, rank_table, time_table, loading_table, primary_rank)

    lookup = primary_table.set_index("representation")
    rank2_parent = float(lookup.loc["parent_verified_rank2", "bw_rms_to_observation"])
    rank2_rfd = float(lookup.loc["rfd_rank2", "bw_rms_to_observation"])
    lines = [
        "# APP-FIN identification illustration",
        "",
        "## Scope",
        "",
        "This is a descriptive fixed-rank comparison on the same 240 monthly 12-stock covariance matrices. It is not forecasting, rank selection, or a test of latent factor-score truth. Rank two is supplied because it is the parent's published APP-FIN RFM forecast specification; ranks 1--15 are sensitivity only.",
        "",
        "Each monthly matrix is built from the sample covariance of that month's daily log returns. A 12 x 12 symmetric tangent matrix has 78 metric coordinates. The rank-two fits retain two persistent directions in that 78-dimensional tangent representation and map the resulting approximation back to a 12 x 12 SPD matrix.",
        "",
        "## Headline measurements",
        "",
        f"- verified-mean parent rank-2 BW reconstruction RMS: **{rank2_parent:.4g}**",
        f"- RFD rank-2 BW reconstruction RMS: **{rank2_rfd:.4g}**",
        f"- RFD relative change versus verified parent: **{100*(rank2_rfd/rank2_parent-1):+.1f}%** (negative favours RFD)",
        f"- estimated centre-motion energy inside the parent rank-2 loading space: **{centre_summary['inside_parent_rank2_energy_percent']:.1f}%**",
        f"- estimated centre-motion energy outside it: **{centre_summary['outside_parent_rank2_energy_percent']:.1f}%**",
        f"- parent/RFD rank-2 loading-space largest angle: **{numerics['primary_rank_loading_angle_degrees']:.1f} degrees**",
        f"- |correlation(Factor 1, VIX)|: parent **{parent_vix_correlation:.3f}**, RFD **{rfd_vix_correlation:.3f}**",
        "",
        "## Interpretation boundary",
        "",
        "A small loading-space angle means the two methods identify similar persistent directions after their tangent spaces are aligned. A small reconstruction error means those directions plus the fitted centre reproduce the observed matrices well. Neither statement proves that a projected score is the true structural factor amplitude: APP-FIN contains no observed latent factors, and contemporaneous noise lying inside the loading space survives projection.",
        "",
        "The centre decomposition answers the Paper 1 identification question empirically: it measures how much of RFD's estimated centre motion would sit inside the parent's rank-two fixed-centre loading space, where a fixed-centre analysis cannot label it separately as drift versus factor movement.",
        "",
        "## Numerical health",
        "",
        f"- RFD Richardson fallbacks: **{int(numerics['rfd_fallback_count'])}**",
        f"- nonconverged local means: **{int(numerics['rfd_nonconverged_stage_count'])}**",
        f"- local-mean support count range: **{int(numerics['rfd_support_count_min'])}--{int(numerics['rfd_support_count_max'])}** months",
        f"- local-mean effective sample-size range: **{numerics['rfd_effective_sample_size_min']:.1f}--{numerics['rfd_effective_sample_size_max']:.1f}**",
        f"- smallest observed matrix eigenvalue: **{numerics['observation_minimum_eigenvalue']:.4g}**",
        f"- smallest RFD local-centre eigenvalue: **{numerics['rfd_local_centre_minimum_eigenvalue']:.4g}**",
        "",
        "See `primary_reconstruction.csv`, `rank_sensitivity.csv`, `loading_space_sensitivity.csv`, `time_series.csv`, and the four plot files beside this report.",
    ]
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    import yaml

    from run_appfin_identification import load_configuration, load_panel

    configuration = load_configuration(ROOT / "config" / "appfin_identification.yaml")
    analyze(
        ROOT,
        configuration,
        load_panel(configuration),
        ROOT / configuration["output"]["directory"],
    )
