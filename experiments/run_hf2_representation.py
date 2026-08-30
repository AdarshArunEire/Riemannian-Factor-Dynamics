"""APP-HF-2: head-free RFM versus piecewise-6 RFD representation.

The first 26 complete weeks of 2024 select rank independently for each arm.
The selected ranks are frozen and evaluated on the final 26 complete weeks.
Within each phase, complementary weekly folds fit centres and lag spaces without
using the week being scored.  The expensive geometric fit is shared across all
candidate ranks.  No forecasting head is present and all of 2025 stays sealed.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
from typing import Any

for _name in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[_name] = "1"

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))

from rfd.estimators.centre_low_n import segmented_frechet_polygon  # noqa: E402
from rfd.estimators.frame import PolygonalFrame, transport_from_reference  # noqa: E402
from rfd.estimators.lag import (  # noqa: E402
    LagRowResult,
    assemble_lag_operator,
    common_reference_tangent_rows,
    coordinate_tangents,
    decompose_lag_operator,
    tangent_coordinates,
)
from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.spd.bw import bw_clip_exp_tangent  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "hf2_representation.yaml"
METHODS = ("parent_rfm", "rfd_piecewise6")
PRIMARY_LOSSES = ("frobenius2", "qlike")


def load_configuration(path: Path = CONFIG_DEFAULT) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    crossfit = config["crossfit"]
    representation = config["representation"]
    selection = config["rank_selection"]
    if int(experiment["complete_weeks"]) != 52:
        raise ValueError("HF-2 requires the 52 complete 2024 weeks")
    if int(experiment["rank_tuning_weeks"]) != 26 or int(
        experiment["representation_evaluation_weeks"]
    ) != 26:
        raise ValueError("HF-2 freezes a 26-week tuning and 26-week evaluation split")
    if int(experiment["hours_per_block"]) != 168:
        raise ValueError("HF-2 blocks must be complete seven-day weeks")
    if int(crossfit["folds"]) != 2:
        raise ValueError("HF-2 uses two complementary folds inside each phase")
    embargo = int(crossfit["embargo_hours_each_training_edge"])
    if not 0 <= embargo < 84:
        raise ValueError("the weekly training-edge embargo must lie in [0, 84)")
    if list(representation["methods"]) != list(METHODS):
        raise ValueError("the only HF-2 arms are parent RFM and piecewise-6 RFD")
    if int(representation["piecewise_segments"]) != 6:
        raise ValueError("the HF-1 decision freezes piecewise-6 for HF-2")
    if not 1 <= int(representation["max_lag"]) < 168 - 2 * embargo:
        raise ValueError("max_lag must fit inside every embargoed training week")
    if representation["tail_mode"] != "common" or representation["normalization"] != "row_size":
        raise ValueError("HF-2 freezes the parent-compatible common-tail row-size convention")
    candidates = list(map(int, selection["candidates"]))
    if candidates != list(range(1, 22)):
        raise ValueError("HF-2 rank candidates must be exactly 1 through 21")
    if selection["primary_losses"] != ["frobenius2", "qlike"]:
        raise ValueError("rank selection uses Frobenius and QLIKE only")
    if selection["rule"] != "arm_specific_one_standard_error":
        raise ValueError("each arm must use the frozen one-standard-error rank rule")
    if not 1 <= int(config["runtime"]["workers"]) <= 8:
        raise ValueError("workers must lie between one and eight")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def experiment_digest(config: dict[str, Any], *, smoke: bool) -> str:
    paths = [
        Path(config["config_path"]), ROOT / config["experiment"]["panel_path"],
        Path(__file__), ROOT / "py" / "rfd" / "estimators" / "centre_low_n.py",
        ROOT / "py" / "rfd" / "estimators" / "frame.py",
        ROOT / "py" / "rfd" / "estimators" / "lag.py",
        ROOT / "py" / "rfd" / "spd" / "bw.py",
    ]
    material = "\n".join(f"{path.resolve()}:{_sha256(path)}" for path in paths)
    material += f"\nprofile={'smoke' if smoke else 'recorded'}"
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _atomic_json(path: Path, value: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _atomic_npz(path: Path, **arrays: Any) -> None:
    temporary = path.with_name(path.name + ".tmp.npz")
    np.savez_compressed(temporary, **arrays)
    temporary.replace(path)


def _atomic_csv(path: Path, frame: pd.DataFrame) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    frame.to_csv(temporary, index=False)
    temporary.replace(path)


def _cache_matches(path: Path, digest: str) -> bool:
    if not path.is_file():
        return False
    try:
        return json.loads(path.read_text(encoding="utf-8"))["digest"] == digest
    except (KeyError, OSError, ValueError):
        return False


def load_panel(config: dict[str, Any]) -> dict[str, np.ndarray]:
    path = ROOT / config["experiment"]["panel_path"]
    if not path.is_file():
        raise FileNotFoundError(f"APP-HF-0 panel is missing: {path}")
    with np.load(path, allow_pickle=False) as source:
        required = {"covariances", "hours", "symbols"}
        if not required.issubset(source.files):
            raise ValueError(f"HF-0 archive is missing {sorted(required - set(source.files))}")
        hours = source["hours"].copy()
        years = hours.astype("datetime64[Y]").astype(int) + 1970
        selected = np.flatnonzero(years == int(config["experiment"]["development_year"]))
        observations = source["covariances"][selected].copy()
        hours = hours[selected].copy()
        symbols = source["symbols"].astype(str)
    expected = int(config["experiment"]["complete_weeks"]) * 168
    observations = observations[:expected]
    hours = hours[:expected]
    m = int(config["experiment"]["expected_matrix_size"])
    if observations.shape != (expected, m, m):
        raise ValueError(f"HF-2 panel shape is {observations.shape}; expected {(expected, m, m)}")
    if symbols.size != int(config["experiment"]["expected_assets"]):
        raise ValueError("HF-2 asset count does not match the frozen panel")
    if np.any(np.diff(hours) != np.timedelta64(1, "h")):
        raise ValueError("HF-2 requires a contiguous hourly panel")
    if not np.isfinite(observations).all() or np.any(np.linalg.eigvalsh(observations) <= 0.0):
        raise ValueError("HF-2 requires finite full-rank covariance observations")
    return {"covariances": observations, "hours": hours, "symbols": symbols}


def phase_data(
    panel: dict[str, np.ndarray], config: dict[str, Any], phase: str, *, smoke: bool
) -> dict[str, np.ndarray]:
    block = int(config["experiment"]["hours_per_block"])
    if phase == "tuning":
        start_week = 0
        weeks = int(config["experiment"]["rank_tuning_weeks"])
    elif phase == "evaluation":
        start_week = int(config["experiment"]["rank_tuning_weeks"])
        weeks = int(config["experiment"]["representation_evaluation_weeks"])
    else:
        raise ValueError("phase must be tuning or evaluation")
    if smoke:
        weeks = int(config["crossfit"]["smoke_weeks_per_phase"])
    start = start_week * block
    stop = start + weeks * block
    observations = panel["covariances"][start:stop].copy()
    hours = panel["hours"][start:stop].copy()
    return {
        "covariances": observations,
        "hours": hours,
        "indices": np.arange(observations.shape[0], dtype=int),
        "week_ids": np.arange(observations.shape[0], dtype=int) // block,
    }


def blocked_fold_masks(
    n: int, *, block_hours: int, validation_parity: int, embargo_hours: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if n % block_hours:
        raise ValueError("cross-fit phases must contain complete weeks")
    index = np.arange(n)
    blocks = index // block_hours
    within = index % block_hours
    heldout = blocks % 2 == int(validation_parity)
    training = (~heldout) & (within >= embargo_hours) & (
        within < block_hours - embargo_hours
    )
    if not training.any() or not heldout.any() or np.any(training & heldout):
        raise RuntimeError("invalid complementary weekly fold")
    return training, heldout, blocks


def indexed_lag_cross_covariances(
    rows: np.ndarray,
    indices: np.ndarray,
    max_lag: int,
    *,
    demean: bool = True,
) -> LagRowResult:
    """Lag products using only pairs whose original indices differ by h.

    This prevents the end of one retained week from being treated as adjacent
    to the start of the next retained week after blocked cross-fitting.
    """
    rows = np.asarray(rows, dtype=float)
    indices = np.asarray(indices, dtype=int)
    if rows.ndim != 2 or indices.shape != (rows.shape[0],):
        raise ValueError("rows and indices must have matching sample axes")
    if rows.shape[0] < 2 or np.any(np.diff(indices) <= 0):
        raise ValueError("indices must be strictly increasing")
    if not 1 <= max_lag < rows.shape[0]:
        raise ValueError("max_lag must lie inside the retained row sample")
    row_mean = rows.mean(axis=0) if demean else np.zeros(rows.shape[1])
    centred = rows - row_mean
    covariances: list[np.ndarray] = []
    pair_counts: list[int] = []
    for lag in range(1, max_lag + 1):
        wanted = indices - lag
        positions = np.searchsorted(indices, wanted)
        valid = positions < indices.size
        exact = np.zeros(indices.size, dtype=bool)
        exact[valid] = indices[positions[valid]] == wanted[valid]
        current = centred[exact]
        past = centred[positions[exact]]
        if current.shape[0] == 0:
            raise ValueError(f"no retained pairs exist at lag {lag}")
        covariances.append((current.T @ past) / rows.shape[0])
        pair_counts.append(int(current.shape[0]))
    return LagRowResult(
        covariances=np.stack(covariances),
        lags=np.arange(1, max_lag + 1),
        centred_rows=centred,
        row_mean=row_mean,
        pair_counts=np.asarray(pair_counts),
        divisors=np.full(max_lag, rows.shape[0], dtype=int),
        tail_mode="common",
        normalization="row_size",
    )


def _constant_frame(point: np.ndarray, start: float, stop: float) -> PolygonalFrame:
    return PolygonalFrame(
        np.asarray([start, stop], dtype=float),
        np.stack([point, point]),
        BW_GEOMETRY,
    )


def _fit_arm(
    observations: np.ndarray,
    times: np.ndarray,
    training: np.ndarray,
    method: str,
    config: dict[str, Any],
) -> dict[str, Any]:
    source = config["representation"]
    train_observations = observations[training]
    train_times = times[training]
    if method == "parent_rfm":
        result = BW_GEOMETRY.barycentre(
            train_observations,
            tol=float(source["mean_tolerance"]),
            max_iter=int(source["mean_max_iterations"]),
        )
        if not result.converged:
            raise RuntimeError("parent global BW mean did not converge")
        frame = _constant_frame(result.X, float(times[0]), float(times[-1]))
        centre_diagnostics = {
            "segments": 1,
            "vertex_count": 2,
            "minimum_segment_count": int(train_observations.shape[0]),
            "maximum_iterations": int(result.n_iter),
            "maximum_residual": float(result.residual),
        }
    elif method == "rfd_piecewise6":
        result = segmented_frechet_polygon(
            train_observations,
            train_times,
            times,
            int(source["piecewise_segments"]),
            BW_GEOMETRY,
            mean_tol=float(source["mean_tolerance"]),
            max_iter=int(source["mean_max_iterations"]),
        )
        frame = result.frame
        centre_diagnostics = dict(result.diagnostics)
    else:
        raise ValueError(f"unknown representation method: {method}")
    tangent_rows = common_reference_tangent_rows(observations, times, frame)
    train_indices = np.flatnonzero(training)
    lag_row = indexed_lag_cross_covariances(
        tangent_rows.rows[training],
        train_indices,
        int(source["max_lag"]),
    )
    spectrum = decompose_lag_operator(assemble_lag_operator(lag_row))
    return {
        "method": method,
        "frame": frame,
        "tangent_rows": tangent_rows,
        "lag_row": lag_row,
        "spectrum": spectrum,
        "centre_diagnostics": centre_diagnostics,
    }


def _reconstruct(
    fit: dict[str, Any],
    mask: np.ndarray,
    rank: int,
    config: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray, dict[str, float]]:
    tangent_rows = fit["tangent_rows"]
    rows = tangent_rows.rows[mask]
    row_mean = fit["lag_row"].row_mean
    centred = rows - row_mean
    if rank == 0:
        reconstructed = tangent_rows.local_centres[mask].copy()
        residual = centred
        return reconstructed, residual, {
            "clip_fraction": 0.0,
            "minimum_clip_factor": 1.0,
            "minimum_raw_step_eigenvalue": math.nan,
            "minimum_reconstruction_eigenvalue": float(
                np.min(np.linalg.eigvalsh(reconstructed))
            ),
        }
    loadings = fit["spectrum"].eigenvectors[:, :rank]
    fitted_rows = (centred @ loadings) @ loadings.T + row_mean
    residual = centred - (centred @ loadings) @ loadings.T
    reference_vectors = coordinate_tangents(fitted_rows, tangent_rows.basis)
    local_vectors = transport_from_reference(
        fit["frame"], reference_vectors, tangent_rows.time[mask]
    )
    local_centres = tangent_rows.local_centres[mask]
    clipped = bw_clip_exp_tangent(
        local_centres,
        local_vectors,
        step_margin=float(config["representation"]["reconstruction_step_margin"]),
    )
    reconstructed = BW_GEOMETRY.exp(local_centres, clipped.tangent)
    return reconstructed, residual, {
        "clip_fraction": float(np.mean(clipped.factors < 1.0)),
        "minimum_clip_factor": float(np.min(clipped.factors)),
        "minimum_raw_step_eigenvalue": float(np.min(clipped.raw_step_min_eigenvalues)),
        "minimum_reconstruction_eigenvalue": float(
            np.min(np.linalg.eigvalsh(reconstructed))
        ),
    }


def _residual_lag_ratio(
    full_rows: np.ndarray,
    residual_rows: np.ndarray,
    indices: np.ndarray,
    max_lag: int,
) -> float:
    full = indexed_lag_cross_covariances(full_rows, indices, max_lag)
    residual = indexed_lag_cross_covariances(residual_rows, indices, max_lag)
    denominator = float(np.linalg.norm(full.stacked, ord="fro"))
    numerator = float(np.linalg.norm(residual.stacked, ord="fro"))
    return numerator / denominator if denominator > 0.0 else math.nan


def _score_arm(
    fit: dict[str, Any],
    observations: np.ndarray,
    heldout: np.ndarray,
    blocks: np.ndarray,
    ranks: list[int],
    phase: str,
    fold: int,
    config: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    indices = np.flatnonzero(heldout)
    target = observations[heldout]
    block_values = blocks[heldout]
    score_rows: list[dict[str, Any]] = []
    diagnostic_rows: list[dict[str, Any]] = []
    for rank in [0, *ranks]:
        reconstruction, residual, diagnostics = _reconstruct(
            fit, heldout, rank, config
        )
        losses = {
            "frobenius2": frobenius_loss(reconstruction, target),
            "qlike": qlike_loss(reconstruction, target),
            "bw2": bw_loss(reconstruction, target),
        }
        for block in np.unique(block_values):
            selected = block_values == block
            score_rows.append({
                "phase": phase,
                "fold": int(fold),
                "block": int(block),
                "method": fit["method"],
                "rank": int(rank),
                **{name: float(values[selected].mean()) for name, values in losses.items()},
            })
        ratio = _residual_lag_ratio(
            fit["tangent_rows"].rows[heldout],
            residual,
            indices,
            int(config["representation"]["max_lag"]),
        )
        diagnostic_rows.append({
            "phase": phase,
            "fold": int(fold),
            "method": fit["method"],
            "rank": int(rank),
            "residual_lag_ratio": ratio,
            **diagnostics,
        })
    return pd.DataFrame(score_rows), pd.DataFrame(diagnostic_rows)


def _identity_loading_coordinates(fit: dict[str, Any], max_rank: int) -> np.ndarray:
    tangent_rows = fit["tangent_rows"]
    loading_vectors = coordinate_tangents(
        fit["spectrum"].eigenvectors[:, :max_rank].T,
        tangent_rows.basis,
    )
    identity = np.eye(fit["frame"].reference_point.shape[0])
    transported = BW_GEOMETRY.transport(
        loading_vectors,
        fit["frame"].reference_point,
        identity,
    )
    return tangent_coordinates(
        transported,
        identity,
        BW_GEOMETRY.tangent_basis(identity),
        BW_GEOMETRY,
    )


def _fold_worker(payload: tuple[Any, ...]) -> dict[str, Any]:
    phase, fold, observations, times, config = payload
    started = time.perf_counter()
    block_hours = int(config["experiment"]["hours_per_block"])
    training, heldout, blocks = blocked_fold_masks(
        observations.shape[0],
        block_hours=block_hours,
        validation_parity=fold,
        embargo_hours=int(config["crossfit"]["embargo_hours_each_training_edge"]),
    )
    ranks = list(map(int, config["rank_selection"]["candidates"]))
    scores = []
    diagnostics = []
    arrays: dict[str, np.ndarray] = {}
    metadata: dict[str, Any] = {
        "phase": phase,
        "fold": int(fold),
        "training_hours": int(training.sum()),
        "heldout_hours": int(heldout.sum()),
    }
    for method in METHODS:
        fit = _fit_arm(observations, times, training, method, config)
        arm_scores, arm_diagnostics = _score_arm(
            fit, observations, heldout, blocks, ranks, phase, fold, config
        )
        scores.append(arm_scores)
        diagnostics.append(arm_diagnostics)
        arrays[f"{method}_eigenvalues"] = fit["spectrum"].eigenvalues
        arrays[f"{method}_identity_loadings"] = _identity_loading_coordinates(
            fit, max(ranks)
        )
        arrays[f"{method}_vertex_times"] = fit["frame"].vertex_times
        arrays[f"{method}_vertices"] = fit["frame"].vertices
        metadata[method] = fit["centre_diagnostics"]
        metadata[method]["minimum_lag_pair_count"] = int(
            np.min(fit["lag_row"].pair_counts)
        )
    metadata["elapsed_seconds"] = float(time.perf_counter() - started)
    return {
        "phase": phase,
        "fold": int(fold),
        "scores": pd.concat(scores, ignore_index=True),
        "diagnostics": pd.concat(diagnostics, ignore_index=True),
        "arrays": arrays,
        "metadata": metadata,
    }


def select_arm_rank(
    tuning_scores: pd.DataFrame,
    method: str,
    candidates: list[int],
) -> tuple[int, pd.DataFrame]:
    arm = tuning_scores[tuning_scores["method"] == method].copy()
    baseline = arm[arm["rank"] == 0].set_index(["fold", "block"])
    rows = []
    for rank in candidates:
        ranked = arm[arm["rank"] == rank].set_index(["fold", "block"])
        ratios = []
        for loss in PRIMARY_LOSSES:
            values = (ranked[loss] / baseline[loss]).to_numpy(dtype=float)
            ratios.extend(values.tolist())
        values = np.asarray(ratios)
        rows.append({
            "method": method,
            "rank": int(rank),
            "mean_relative_primary_loss": float(values.mean()),
            "se_relative_primary_loss": float(values.std(ddof=1) / np.sqrt(values.size)),
        })
    curve = pd.DataFrame(rows)
    best = curve.loc[curve["mean_relative_primary_loss"].idxmin()]
    threshold = float(best["mean_relative_primary_loss"] + best["se_relative_primary_loss"])
    eligible = curve[curve["mean_relative_primary_loss"] <= threshold]
    selected = int(eligible["rank"].min())
    curve["selected"] = curve["rank"] == selected
    curve["one_se_threshold"] = threshold
    return selected, curve


def _subspace_diagnostics(
    output: Path, selected_ranks: dict[str, int]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    projectors: dict[tuple[int, str], np.ndarray] = {}
    bases: dict[tuple[int, str], np.ndarray] = {}
    for fold in range(2):
        with np.load(output / "evaluation" / f"fold_{fold}.npz") as source:
            for method in METHODS:
                rank = selected_ranks[method]
                coordinates = source[f"{method}_identity_loadings"][:rank]
                basis, _ = np.linalg.qr(coordinates.T)
                bases[(fold, method)] = basis[:, :rank]
                projectors[(fold, method)] = basis[:, :rank] @ basis[:, :rank].T
    stability = []
    for method in METHODS:
        left = bases[(0, method)]
        right = bases[(1, method)]
        singular = np.linalg.svd(left.T @ right, compute_uv=False)
        singular = np.clip(singular, 0.0, 1.0)
        stability.append({
            "method": method,
            "rank": selected_ranks[method],
            "fold_projector_distance": float(
                np.linalg.norm(projectors[(0, method)] - projectors[(1, method)], ord="fro")
            ),
            "largest_principal_angle_degrees": float(
                np.degrees(np.arccos(np.min(singular)))
            ),
        })
    overlap = []
    for fold in range(2):
        left = bases[(fold, "parent_rfm")]
        right = bases[(fold, "rfd_piecewise6")]
        singular = np.linalg.svd(left.T @ right, compute_uv=False)
        overlap.append({
            "fold": fold,
            "minimum_cross_arm_canonical_correlation": float(np.min(singular)),
            "largest_cross_arm_principal_angle_degrees": float(
                np.degrees(np.arccos(np.clip(np.min(singular), 0.0, 1.0)))
            ),
        })
    return pd.DataFrame(stability), pd.DataFrame(overlap)


def _performance_table(
    evaluation_scores: pd.DataFrame,
    selected_ranks: dict[str, int],
) -> pd.DataFrame:
    rows = []
    for method in METHODS:
        rank = selected_ranks[method]
        arm = evaluation_scores[
            (evaluation_scores["method"] == method)
            & (evaluation_scores["rank"] == rank)
        ]
        rows.append({
            "method": method,
            "rank": rank,
            **{f"mean_{loss}": float(arm[loss].mean()) for loss in ("frobenius2", "qlike", "bw2")},
            **{f"se_{loss}": float(arm[loss].std(ddof=1) / np.sqrt(arm.shape[0])) for loss in ("frobenius2", "qlike", "bw2")},
        })
    result = pd.DataFrame(rows)
    parent = result[result["method"] == "parent_rfm"].iloc[0]
    for loss in ("frobenius2", "qlike", "bw2"):
        result[f"reduction_percent_vs_parent_{loss}"] = 100.0 * (
            1.0 - result[f"mean_{loss}"] / float(parent[f"mean_{loss}"])
        )
    return result


def _centre_table(evaluation_scores: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for method in METHODS:
        arm = evaluation_scores[
            (evaluation_scores["method"] == method)
            & (evaluation_scores["rank"] == 0)
        ]
        rows.append({
            "method": method,
            **{
                f"mean_{loss}": float(arm[loss].mean())
                for loss in ("frobenius2", "qlike", "bw2")
            },
        })
    result = pd.DataFrame(rows)
    parent = result[result["method"] == "parent_rfm"].iloc[0]
    for loss in ("frobenius2", "qlike", "bw2"):
        result[f"reduction_percent_vs_parent_{loss}"] = 100.0 * (
            1.0 - result[f"mean_{loss}"] / float(parent[f"mean_{loss}"])
        )
    return result


def _centre_movement_table(output: Path) -> pd.DataFrame:
    rows = []
    for fold in range(2):
        with np.load(output / "evaluation" / f"fold_{fold}.npz") as source:
            global_centre = source["parent_rfm_vertices"][0]
            vertices = source["rfd_piecewise6_vertices"]
            reference = np.broadcast_to(global_centre, vertices.shape)
            displacement2 = BW_GEOMETRY.dist2(reference, vertices)
            edge2 = BW_GEOMETRY.dist2(vertices[:-1], vertices[1:])
            total = float(edge2.sum())
            rows.append({
                "fold": fold,
                "vertex_bw_rms_from_global": float(np.sqrt(displacement2.mean())),
                "maximum_vertex_bw_distance_from_global": float(np.sqrt(displacement2.max())),
                "total_polygon_edge_energy": total,
                "maximum_edge_energy_share": float(edge2.max() / total) if total > 0.0 else 0.0,
            })
    return pd.DataFrame(rows)


def _matched_rank_table(evaluation_scores: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for rank in sorted(set(evaluation_scores["rank"]) - {0}):
        selected = evaluation_scores[evaluation_scores["rank"] == rank]
        values = {method: selected[selected["method"] == method] for method in METHODS}
        row: dict[str, Any] = {"rank": int(rank)}
        for loss in ("frobenius2", "qlike", "bw2"):
            parent = float(values["parent_rfm"][loss].mean())
            rfd = float(values["rfd_piecewise6"][loss].mean())
            row[f"rfd_reduction_percent_{loss}"] = 100.0 * (1.0 - rfd / parent)
        rows.append(row)
    return pd.DataFrame(rows)


def _terminal_verdict(
    performance: pd.DataFrame,
    selected_diagnostics: pd.DataFrame,
    config: dict[str, Any],
) -> str:
    if float(selected_diagnostics["clip_fraction"].max()) > float(
        config["acceptance"]["maximum_reconstruction_clip_fraction"]
    ):
        return "NUMERICAL_RECONSTRUCTION_BOUNDARY"
    if float(selected_diagnostics["residual_lag_ratio"].max()) > float(
        config["acceptance"]["maximum_residual_lag_ratio"]
    ):
        return "RESIDUAL_LAG_REPRESENTATION_FAILURE"
    rfd = performance[performance["method"] == "rfd_piecewise6"].iloc[0]
    changes = np.asarray([
        rfd["reduction_percent_vs_parent_frobenius2"],
        rfd["reduction_percent_vs_parent_qlike"],
    ], dtype=float)
    tie = float(config["acceptance"]["practical_tie_percent"])
    if np.all(changes > tie):
        return "SUPPORT_RFD_REPRESENTATION"
    if np.all(changes < -tie):
        return "PARENT_RFM_REPRESENTATION_WINS"
    if np.all(np.abs(changes) <= tie):
        return "PRACTICAL_TIE"
    return "MIXED_REPRESENTATION_RESULT"


def _stability_markdown(stability: pd.DataFrame) -> list[str]:
    lines = [
        "| arm | rank | fold projector distance | largest angle |",
        "|---|---:|---:|---:|",
    ]
    labels = {"parent_rfm": "global RFM", "rfd_piecewise6": "piecewise-6 RFD"}
    for row in stability.itertuples(index=False):
        lines.append(
            f"| {labels[row.method]} | {int(row.rank)} | "
            f"{row.fold_projector_distance:.4g} | "
            f"{row.largest_principal_angle_degrees:.2f}° |"
        )
    return lines


def _plots(
    output: Path,
    rank_curves: pd.DataFrame,
    performance: pd.DataFrame,
    matched: pd.DataFrame,
    spectra: pd.DataFrame,
) -> None:
    colours = {"parent_rfm": "#440154", "rfd_piecewise6": "#35b779"}
    labels = {"parent_rfm": "global RFM", "rfd_piecewise6": "piecewise-6 RFD"}
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    for method in METHODS:
        frame = rank_curves[rank_curves["method"] == method]
        ax.plot(frame["rank"], 100.0 * (frame["mean_relative_primary_loss"] - 1.0), marker="o", color=colours[method], label=labels[method])
        chosen = frame[frame["selected"]].iloc[0]
        ax.scatter([chosen["rank"]], [100.0 * (chosen["mean_relative_primary_loss"] - 1.0)], s=100, facecolors="none", edgecolors=colours[method], linewidths=2)
    ax.axhline(0.0, color="#777777", linewidth=1)
    ax.set(xlabel="retained lag-factor directions", ylabel="validation loss change vs centre only (%)", title="Each arm chooses rank before evaluation")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output / "rank_validation.png", dpi=180)
    plt.close(fig)

    rfd = performance[performance["method"] == "rfd_piecewise6"].iloc[0]
    names = ["Frobenius", "QLIKE", "BW"]
    values = [rfd[f"reduction_percent_vs_parent_{loss}"] for loss in ("frobenius2", "qlike", "bw2")]
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    bars = ax.bar(names, values, color=plt.colormaps["viridis"](np.linspace(0.2, 0.8, 3)))
    ax.axhline(0.0, color="#333333", linewidth=1)
    ax.bar_label(bars, fmt="%+.1f%%", padding=3)
    ax.set(ylabel="RFD error reduction vs global RFM (%)", title="Held-out representation")
    fig.tight_layout()
    fig.savefig(output / "heldout_representation.png", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0), sharex=True)
    for ax, loss, label in zip(axes, ("frobenius2", "qlike"), ("Frobenius", "QLIKE")):
        ax.plot(matched["rank"], matched[f"rfd_reduction_percent_{loss}"], marker="o", color="#31688e")
        ax.axhline(0.0, color="#777777", linewidth=1)
        ax.set(xlabel="same retained rank in both arms", ylabel="RFD reduction vs RFM (%)", title=label)
    fig.suptitle("Does the centre change help at the same dimension?")
    fig.tight_layout()
    fig.savefig(output / "matched_rank_curve.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    for method in METHODS:
        frame = spectra[spectra["method"] == method].groupby("index", as_index=False)["relative_eigenvalue"].mean()
        ax.plot(frame["index"] + 1, frame["relative_eigenvalue"], marker="o", color=colours[method], label=labels[method])
    ax.set_yscale("log")
    ax.set(xlabel="lag-operator eigenvalue index", ylabel="multiplier of leading eigenvalue (log scale)", title="Evaluation-fold lag spectra")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output / "lag_spectrum.png", dpi=180)
    plt.close(fig)

def analyze(output: Path, config: dict[str, Any], *, smoke: bool) -> dict[str, Any]:
    tuning_scores = pd.concat([
        pd.read_csv(output / "tuning" / f"fold_{fold}_scores.csv") for fold in range(2)
    ], ignore_index=True)
    evaluation_scores = pd.concat([
        pd.read_csv(output / "evaluation" / f"fold_{fold}_scores.csv") for fold in range(2)
    ], ignore_index=True)
    evaluation_diagnostics = pd.concat([
        pd.read_csv(output / "evaluation" / f"fold_{fold}_diagnostics.csv") for fold in range(2)
    ], ignore_index=True)
    candidates = list(map(int, config["rank_selection"]["candidates"]))
    selected_ranks: dict[str, int] = {}
    curves = []
    for method in METHODS:
        selected_ranks[method], curve = select_arm_rank(tuning_scores, method, candidates)
        curves.append(curve)
    rank_curves = pd.concat(curves, ignore_index=True)
    performance = _performance_table(evaluation_scores, selected_ranks)
    centres = _centre_table(evaluation_scores)
    movement = _centre_movement_table(output)
    matched = _matched_rank_table(evaluation_scores)
    stability, overlap = _subspace_diagnostics(output, selected_ranks)
    selected_diagnostics = pd.concat([
        evaluation_diagnostics[
            (evaluation_diagnostics["method"] == method)
            & (evaluation_diagnostics["rank"] == rank)
        ] for method, rank in selected_ranks.items()
    ], ignore_index=True)
    spectra_rows = []
    for fold in range(2):
        with np.load(output / "evaluation" / f"fold_{fold}.npz") as source:
            for method in METHODS:
                eigenvalues = source[f"{method}_eigenvalues"][:15]
                leading = float(eigenvalues[0])
                for index, value in enumerate(eigenvalues):
                    spectra_rows.append({
                        "fold": fold, "method": method, "index": index,
                        "eigenvalue": float(value),
                        "relative_eigenvalue": float(value / leading) if leading > 0.0 else math.nan,
                    })
    spectra = pd.DataFrame(spectra_rows)
    verdict = _terminal_verdict(performance, selected_diagnostics, config)
    _atomic_csv(output / "rank_validation.csv", rank_curves)
    _atomic_csv(output / "evaluation_scores.csv", evaluation_scores)
    _atomic_csv(output / "performance.csv", performance)
    _atomic_csv(output / "centre_only_performance.csv", centres)
    _atomic_csv(output / "centre_movement.csv", movement)
    _atomic_csv(output / "matched_rank.csv", matched)
    _atomic_csv(output / "selected_numerical_diagnostics.csv", selected_diagnostics)
    _atomic_csv(output / "loading_stability.csv", stability)
    _atomic_csv(output / "cross_arm_loading_overlap.csv", overlap)
    _atomic_csv(output / "lag_spectra.csv", spectra)
    _plots(output, rank_curves, performance, matched, spectra)

    parent = performance[performance["method"] == "parent_rfm"].iloc[0]
    rfd = performance[performance["method"] == "rfd_piecewise6"].iloc[0]
    rfd_centre = centres[centres["method"] == "rfd_piecewise6"].iloc[0]
    phase_weeks = int(config["crossfit"]["smoke_weeks_per_phase"] if smoke else 26)
    report = [
        "# APP-HF-2 — matched representation", "",
        f"**Profile:** {'smoke; non-scientific' if smoke else 'recorded'}  ",
        f"**Verdict:** `{verdict}`", "",
        "## Frozen comparison", "",
        f"The first {phase_weeks} {'smoke-profile ' if smoke else ''}weeks choose rank independently for each arm; the subsequent {phase_weeks} weeks evaluate those frozen ranks. Inside each phase, complementary weekly folds keep every scored covariance out of its centre and lag-space fit. Both arms use the same observations, six hourly lags, coordinate convention, reconstruction guard, and losses. There is no VAR or Kalman head. The complete same-rank curve is retained so rank flexibility cannot masquerade as a centre effect.", "",
        "| arm | selected rank | Frobenius | QLIKE | BW |", "|---|---:|---:|---:|---:|",
        f"| global RFM | {int(parent['rank'])} | {parent['mean_frobenius2']:.6g} | {parent['mean_qlike']:.6g} | {parent['mean_bw2']:.6g} |",
        f"| piecewise-6 RFD | {int(rfd['rank'])} | {rfd['mean_frobenius2']:.6g} | {rfd['mean_qlike']:.6g} | {rfd['mean_bw2']:.6g} |", "",
        "RFD change versus parent (positive means lower error):", "",
        f"- Frobenius: **{rfd['reduction_percent_vs_parent_frobenius2']:+.2f}%**",
        f"- QLIKE: **{rfd['reduction_percent_vs_parent_qlike']:+.2f}%**",
        f"- BW (descriptive): **{rfd['reduction_percent_vs_parent_bw2']:+.2f}%**", "",
        "The piecewise-6 centre by itself changed held-out Frobenius/QLIKE/BW error versus the global centre by "
        f"**{rfd_centre['reduction_percent_vs_parent_frobenius2']:+.2f}% / "
        f"{rfd_centre['reduction_percent_vs_parent_qlike']:+.2f}% / "
        f"{rfd_centre['reduction_percent_vs_parent_bw2']:+.2f}%**. This separates the centre contribution from the retained lag space.", "",
        "## Diagnostics", "",
        *_stability_markdown(stability), "",
        f"- maximum selected-rank reconstruction clip fraction: {selected_diagnostics['clip_fraction'].max():.3%}",
        f"- maximum selected-rank residual/full lag-row ratio: {selected_diagnostics['residual_lag_ratio'].max():.3f}",
        f"- mean piecewise-6 vertex displacement from the fold global centre: {movement['vertex_bw_rms_from_global'].mean():.4g} BW units", "",
        "Projected scores remain noisy coordinates. HF-2 evaluates dimension reduction and reconstruction, not structural factor-amplitude recovery and not forecasting.", "",
        "All of 2025 remains sealed for APP-HF-4.", "",
    ]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")
    result = {
        "verdict": verdict,
        "selected_ranks": selected_ranks,
        "rfd_reduction_percent": {
            loss: float(rfd[f"reduction_percent_vs_parent_{loss}"])
            for loss in ("frobenius2", "qlike", "bw2")
        },
        "maximum_clip_fraction": float(selected_diagnostics["clip_fraction"].max()),
        "maximum_residual_lag_ratio": float(selected_diagnostics["residual_lag_ratio"].max()),
        "profile": "smoke" if smoke else "recorded",
    }
    _atomic_json(output / "verdict.json", result)
    return result


def build_design(config: dict[str, Any], panel: dict[str, np.ndarray], *, smoke: bool) -> dict[str, Any]:
    weeks = int(config["crossfit"]["smoke_weeks_per_phase"] if smoke else 26)
    n = weeks * int(config["experiment"]["hours_per_block"])
    train, heldout, _ = blocked_fold_masks(
        n,
        block_hours=int(config["experiment"]["hours_per_block"]),
        validation_parity=0,
        embargo_hours=int(config["crossfit"]["embargo_hours_each_training_edge"]),
    )
    return {
        "experiment_id": config["experiment"]["id"],
        "profile": "smoke" if smoke else "recorded",
        "matrix_size": int(panel["covariances"].shape[1]),
        "tangent_dimension": int(panel["covariances"].shape[1] * (panel["covariances"].shape[1] + 1) // 2),
        "assets": panel["symbols"].tolist(),
        "rank_tuning_weeks": weeks,
        "representation_evaluation_weeks": weeks,
        "crossfit_training_hours_per_fold": int(train.sum()),
        "crossfit_heldout_hours_per_fold": int(heldout.sum()),
        "rank_candidates": config["rank_selection"]["candidates"],
        "rank_policy": "independent arm-specific validation rank, then frozen",
        "matched_rank_diagnostic": True,
        "max_lag_hours": int(config["representation"]["max_lag"]),
        "forecast_head": None,
        "sealed_evaluation_year": int(config["experiment"]["sealed_evaluation_year"]),
    }


def _write_fold(output: Path, result: dict[str, Any], digest: str) -> None:
    phase = result["phase"]
    fold = int(result["fold"])
    directory = output / phase
    directory.mkdir(parents=True, exist_ok=True)
    _atomic_csv(directory / f"fold_{fold}_scores.csv", result["scores"])
    _atomic_csv(directory / f"fold_{fold}_diagnostics.csv", result["diagnostics"])
    _atomic_npz(directory / f"fold_{fold}.npz", **result["arrays"])
    _atomic_json(directory / f"fold_{fold}.meta.json", {
        "digest": f"{digest}:{phase}:{fold}",
        "metadata": result["metadata"],
    })


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    config = load_configuration(args.config)
    panel = load_panel(config)
    design = build_design(config, panel, smoke=args.smoke)
    print(json.dumps(design, indent=2), flush=True)
    if args.dry_run:
        print("APP-HF-2 dry run passed; 2025 was not evaluated.", flush=True)
        return
    output_key = "smoke_directory" if args.smoke else "directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config, smoke=args.smoke)
    design["digest"] = digest
    _atomic_json(output / "design.json", design)
    jobs = []
    for phase in ("tuning", "evaluation"):
        data = phase_data(panel, config, phase, smoke=args.smoke)
        observations = data["covariances"]
        times = np.linspace(0.0, 1.0, observations.shape[0])
        for fold in range(2):
            meta = output / phase / f"fold_{fold}.meta.json"
            fold_digest = f"{digest}:{phase}:{fold}"
            required = [
                output / phase / f"fold_{fold}.npz",
                output / phase / f"fold_{fold}_scores.csv",
                output / phase / f"fold_{fold}_diagnostics.csv",
            ]
            if args.force or not _cache_matches(meta, fold_digest) or not all(path.is_file() for path in required):
                jobs.append((phase, fold, observations, times, config))
    if jobs:
        workers = min(int(config["runtime"]["workers"]), len(jobs))
        print(f"[fits] running {len(jobs)} missing phase/fold fits with {workers} workers", flush=True)
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_fold_worker, job): (job[0], job[1]) for job in jobs}
            for future in as_completed(futures):
                phase, fold = futures[future]
                result = future.result()
                _write_fold(output, result, digest)
                print(f"[fits] completed {phase} fold {fold}", flush=True)
    else:
        print("[fits] all digest-matched phase/fold fits are cached", flush=True)
    result = analyze(output, config, smoke=args.smoke)
    print(json.dumps(result, indent=2), flush=True)
    print(f"APP-HF-2 report: {output / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
