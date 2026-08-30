"""APP-HF-3: materialise and diagnose frozen cross-fitted crypto scores.

The completed HF-2 caches contain each cross-fit polygon and its loading basis
transported to the identity.  Those objects are sufficient to recover held-out
projected scores without refitting centres or lag operators.  Fold gauges are
aligned by loading-space Procrustes at the identity.  VAR diagnostics use only
genuine within-week transitions, so alternating cross-fit gauges cannot create
fake training pairs.  No 2025 observation is loaded.
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
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "py"))

from experiments import run_hf2_representation as hf2  # noqa: E402
from rfd.estimators.frame import PolygonalFrame  # noqa: E402
from rfd.estimators.lag import (  # noqa: E402
    common_reference_tangent_rows,
    coordinate_tangents,
    tangent_coordinates,
)
from rfd.geometry import BW_GEOMETRY  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "hf3_score_diagnostic.yaml"
METHODS = ("parent_rfm", "rfd_piecewise6")
PHASES = ("tuning", "evaluation")


def load_configuration(path: Path = CONFIG_DEFAULT) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    source = config["source"]
    materialization = config["materialization"]
    policy = config["head_policy"]
    diagnostics = config["diagnostics"]
    if int(experiment["development_year"]) != 2024:
        raise ValueError("HF-3 is restricted to the frozen 2024 development year")
    if int(experiment["sealed_evaluation_year"]) != 2025:
        raise ValueError("HF-3 must keep the 2025 evaluation year sealed")
    if int(experiment["complete_weeks"]) != 52 or int(experiment["hours_per_block"]) != 168:
        raise ValueError("HF-3 requires 52 complete seven-day weeks")
    if tuple(source["methods"]) != METHODS:
        raise ValueError("HF-3 requires exact parent/RFD arm parity")
    ranks = {name: int(value) for name, value in source["frozen_ranks"].items()}
    if ranks != {"parent_rfm": 19, "rfd_piecewise6": 19}:
        raise ValueError("HF-3 must inherit frozen rank 19 in both arms")
    if int(source["mechanism_rank"]) != 1:
        raise ValueError("HF-3 retains rank 1 only as the frozen mechanism diagnostic")
    if int(source["max_lag"]) != 6 or list(map(int, diagnostics["ranks"])) != [1, 19]:
        raise ValueError("HF-3 diagnostics are frozen at ranks 1 and 19 with six lags")
    if materialization["anchor_phase"] != "tuning" or int(materialization["anchor_fold"]) != 0:
        raise ValueError("HF-3 gauge anchor must remain tuning fold 0")
    smoke_weeks = int(materialization["smoke_heldout_weeks_per_phase"])
    if not 1 <= smoke_weeks <= 6:
        raise ValueError("smoke held-out weeks must lie between one and six")
    if policy["primary"] != "parent_var1_with_intercept":
        raise ValueError("parent-style VAR(1) with intercept is the frozen primary head")
    if policy["kalman"] != "inherited_non_promoted_sensitivity":
        raise ValueError("HF-3 may not retune or promote the Kalman sensitivity")
    if not 1 <= int(config["runtime"]["workers"]) <= 8:
        raise ValueError("workers must lie between one and eight")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _atomic_json(path: Path, value: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
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


def load_frozen_source(config: dict[str, Any]) -> tuple[dict[str, Any], dict[str, np.ndarray], Path]:
    hf2_config = hf2.load_configuration(ROOT / config["source"]["hf2_config"])
    panel = hf2.load_panel(hf2_config)
    source = ROOT / config["source"]["hf2_output"]
    verdict_path = source / "verdict.json"
    design_path = source / "design.json"
    if not verdict_path.is_file() or not design_path.is_file():
        raise FileNotFoundError("the recorded HF-2 verdict/design is missing")
    verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
    design = json.loads(design_path.read_text(encoding="utf-8"))
    if verdict.get("profile") != "recorded":
        raise ValueError("HF-3 requires the recorded, not smoke, HF-2 source")
    inherited = {name: int(value) for name, value in verdict["selected_ranks"].items()}
    frozen = {name: int(value) for name, value in config["source"]["frozen_ranks"].items()}
    if inherited != frozen:
        raise ValueError(f"HF-2 selected ranks {inherited}, not frozen HF-3 ranks {frozen}")
    if int(design["sealed_evaluation_year"]) != int(config["experiment"]["sealed_evaluation_year"]):
        raise ValueError("HF-2 and HF-3 sealed-year contracts disagree")
    required = []
    for phase in PHASES:
        for fold in range(2):
            required.extend([
                source / phase / f"fold_{fold}.npz",
                source / phase / f"fold_{fold}.meta.json",
            ])
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"HF-2 source caches are missing: {missing}")
    years = panel["hours"].astype("datetime64[Y]").astype(int) + 1970
    if set(years.tolist()) != {2024}:
        raise ValueError("HF-3 panel loader exposed observations outside 2024")
    return hf2_config, panel, source


def experiment_digest(config: dict[str, Any], source: Path, *, smoke: bool) -> str:
    paths = [
        Path(config["config_path"]), Path(__file__),
        ROOT / config["source"]["hf2_config"],
        ROOT / "py" / "rfd" / "forecast.py",
        ROOT / "py" / "rfd" / "estimators" / "lag.py",
    ]
    for phase in PHASES:
        for fold in range(2):
            paths.extend([
                source / phase / f"fold_{fold}.npz",
                source / phase / f"fold_{fold}.meta.json",
            ])
    material = "\n".join(f"{path.resolve()}:{_sha256(path)}" for path in paths)
    material += f"\nprofile={'smoke' if smoke else 'recorded'}"
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def orthogonal_loading_alignment(
    anchor: np.ndarray, source: np.ndarray
) -> tuple[np.ndarray, dict[str, float]]:
    """Return Q with Q @ source closest to anchor and subspace diagnostics."""
    anchor = np.asarray(anchor, dtype=float)
    source = np.asarray(source, dtype=float)
    if anchor.ndim != 2 or source.shape != anchor.shape:
        raise ValueError("anchor and source loading arrays must have equal r-by-p shape")
    left, singular, right_t = np.linalg.svd(anchor @ source.T, full_matrices=False)
    rotation = left @ right_t
    cosines = np.clip(singular, 0.0, 1.0)
    angles = np.arccos(cosines)
    return rotation, {
        "minimum_canonical_correlation": float(cosines.min()),
        "mean_canonical_correlation": float(cosines.mean()),
        "largest_principal_angle_degrees": float(np.degrees(angles.max())),
        "grassmann_distance": float(np.linalg.norm(angles)),
        "aligned_loading_rms": float(np.linalg.norm(rotation @ source - anchor) / math.sqrt(anchor.shape[0])),
    }


def _loading_coordinates_at_reference(
    identity_loadings: np.ndarray, frame: PolygonalFrame
) -> np.ndarray:
    size = frame.reference_point.shape[0]
    identity = np.eye(size)
    identity_basis = BW_GEOMETRY.tangent_basis(identity)
    loading_vectors = coordinate_tangents(identity_loadings, identity_basis)
    reference_vectors = BW_GEOMETRY.transport(
        loading_vectors, identity, frame.reference_point
    )
    reference_basis = BW_GEOMETRY.tangent_basis(frame.reference_point)
    return tangent_coordinates(
        reference_vectors, frame.reference_point, reference_basis, BW_GEOMETRY
    )


def _selected_heldout(
    heldout: np.ndarray, blocks: np.ndarray, *, smoke: bool, smoke_weeks: int
) -> np.ndarray:
    if not smoke:
        return heldout.copy()
    available = np.unique(blocks[heldout])[:smoke_weeks]
    return heldout & np.isin(blocks, available)


def _materialize_fold(payload: tuple[Any, ...]) -> dict[str, Any]:
    phase, fold, observations, hours, hf2_config, config, source, smoke, anchors = payload
    block_hours = int(config["experiment"]["hours_per_block"])
    times = np.linspace(0.0, 1.0, observations.shape[0])
    training, heldout, blocks = hf2.blocked_fold_masks(
        observations.shape[0],
        block_hours=block_hours,
        validation_parity=int(fold),
        embargo_hours=int(hf2_config["crossfit"]["embargo_hours_each_training_edge"]),
    )
    selected = _selected_heldout(
        heldout, blocks, smoke=smoke,
        smoke_weeks=int(config["materialization"]["smoke_heldout_weeks_per_phase"]),
    )
    needed = training | selected
    needed_indices = np.flatnonzero(needed)
    selected_local = selected[needed]
    training_local = training[needed]
    global_week_offset = 0 if phase == "tuning" else 26
    cache_path = source / phase / f"fold_{fold}.npz"
    rank_frames: dict[int, list[pd.DataFrame]] = {1: [], 19: []}
    alignment_rows = []
    with np.load(cache_path, allow_pickle=False) as cache:
        for method in METHODS:
            frame = PolygonalFrame(
                cache[f"{method}_vertex_times"],
                cache[f"{method}_vertices"],
                BW_GEOMETRY,
            )
            tangent = common_reference_tangent_rows(
                observations[needed], times[needed], frame
            )
            row_mean = tangent.rows[training_local].mean(axis=0)
            centred = tangent.rows[selected_local] - row_mean
            identity_all = cache[f"{method}_identity_loadings"]
            common = {
                "hour": hours[needed][selected_local].astype("datetime64[h]").astype(str),
                "phase": phase,
                "week": blocks[needed][selected_local] + global_week_offset,
                "fold": int(fold),
                "method": method,
            }
            for rank in (1, 19):
                identity_loadings = identity_all[:rank]
                reference_loadings = _loading_coordinates_at_reference(
                    identity_loadings, frame
                )
                local_scores = centred @ reference_loadings.T
                rotation, diagnostics = orthogonal_loading_alignment(
                    anchors[method][rank], identity_loadings
                )
                aligned_scores = local_scores @ rotation.T
                frame_data: dict[str, Any] = dict(common)
                for component in range(rank):
                    frame_data[f"score_{component + 1:02d}"] = aligned_scores[:, component]
                rank_frames[rank].append(pd.DataFrame(frame_data))
                alignment_rows.append({
                    "phase": phase,
                    "fold": int(fold),
                    "method": method,
                    "rank": int(rank),
                    **diagnostics,
                })
    return {
        "phase": phase,
        "fold": int(fold),
        "rank1": pd.concat(rank_frames[1], ignore_index=True),
        "rank19": pd.concat(rank_frames[19], ignore_index=True),
        "alignment": pd.DataFrame(alignment_rows),
    }


def fit_blocked_var1(scores: np.ndarray, blocks: np.ndarray) -> dict[str, Any]:
    """Fit parent-style VAR(1) using only consecutive rows in one block."""
    scores = np.asarray(scores, dtype=float)
    blocks = np.asarray(blocks)
    if scores.ndim != 2 or scores.shape[0] < 3 or blocks.shape != (scores.shape[0],):
        raise ValueError("scores and blocks must be matching n-by-r and n arrays")
    if not np.isfinite(scores).all():
        raise ValueError("scores contain NaN or Inf")
    valid = blocks[1:] == blocks[:-1]
    if valid.sum() <= scores.shape[1] + 1:
        raise ValueError("too few genuine within-block transitions for VAR(1)")
    past = scores[:-1][valid]
    response = scores[1:][valid]
    design = np.column_stack((np.ones(past.shape[0]), past))
    gram = design.T @ design
    coefficients = np.linalg.solve(gram, design.T @ response)
    residuals = response - design @ coefficients
    transition = coefficients[1:].T
    radius = float(np.max(np.abs(np.linalg.eigvals(transition))))
    centred_response = response - response.mean(axis=0)
    denominator = float(np.sum(centred_response**2))
    r2 = 1.0 - float(np.sum(residuals**2)) / denominator if denominator > 0.0 else math.nan
    response_covariance = np.atleast_2d(np.cov(response, rowvar=False, bias=True))
    residual_covariance = np.atleast_2d(np.cov(residuals, rowvar=False, bias=True))
    return {
        "coefficients": coefficients,
        "residuals": residuals,
        "target_blocks": blocks[1:][valid],
        "transition_radius": radius,
        "gram_condition_number": float(np.linalg.cond(gram)),
        "var_r2": float(r2),
        "innovation_variance_fraction": float(
            np.trace(residual_covariance) / np.trace(response_covariance)
        ),
        "transition_count": int(valid.sum()),
    }


def residual_lag_dependence(
    residuals: np.ndarray, blocks: np.ndarray, max_lag: int
) -> pd.DataFrame:
    residuals = np.asarray(residuals, dtype=float)
    blocks = np.asarray(blocks)
    rows = []
    for lag in range(1, max_lag + 1):
        valid = blocks[lag:] == blocks[:-lag]
        current = residuals[lag:][valid]
        past = residuals[:-lag][valid]
        if current.shape[0] == 0:
            raise ValueError(f"no residual pairs at lag {lag}")
        current = current - current.mean(axis=0)
        past = past - past.mean(axis=0)
        cross = current.T @ past / current.shape[0]
        current_cov = current.T @ current / current.shape[0]
        past_cov = past.T @ past / past.shape[0]
        denominator = math.sqrt(
            float(np.linalg.norm(current_cov, ord="fro"))
            * float(np.linalg.norm(past_cov, ord="fro"))
        )
        rows.append({
            "lag": int(lag),
            "dependence_ratio": float(np.linalg.norm(cross, ord="fro") / denominator)
            if denominator > 0.0 else math.nan,
            "pair_count": int(current.shape[0]),
        })
    return pd.DataFrame(rows)


def _seam_ratio(scores: np.ndarray, blocks: np.ndarray) -> float:
    differences = np.linalg.norm(np.diff(scores, axis=0), axis=1)
    seams = blocks[1:] != blocks[:-1]
    within = differences[~seams]
    between = differences[seams]
    if within.size == 0 or between.size == 0:
        return math.nan
    denominator = float(np.median(within))
    return float(np.median(between) / denominator) if denominator > 0.0 else math.nan


def diagnose_scores(rank_frames: dict[int, pd.DataFrame], config: dict[str, Any]) -> tuple[pd.DataFrame, pd.DataFrame]:
    diagnostic_rows = []
    lag_rows = []
    for rank, frame in rank_frames.items():
        score_columns = [f"score_{index:02d}" for index in range(1, rank + 1)]
        for method in METHODS:
            selected = frame[frame["method"] == method].sort_values("hour")
            scores = selected[score_columns].to_numpy(dtype=float)
            blocks = selected["week"].to_numpy(dtype=int)
            fit = fit_blocked_var1(scores, blocks)
            lag = residual_lag_dependence(
                fit["residuals"], fit["target_blocks"],
                int(config["diagnostics"]["residual_lags"]),
            )
            lag.insert(0, "rank", rank)
            lag.insert(0, "method", method)
            lag_rows.append(lag)
            score_energy = np.mean(np.sum(scores**2, axis=1))
            diagnostic_rows.append({
                "method": method,
                "rank": int(rank),
                "score_rows": int(scores.shape[0]),
                "score_energy": float(score_energy),
                "transition_count": fit["transition_count"],
                "transition_radius": fit["transition_radius"],
                "gram_condition_number": fit["gram_condition_number"],
                "var_r2": fit["var_r2"],
                "innovation_variance_fraction": fit["innovation_variance_fraction"],
                "maximum_residual_lag_dependence": float(lag["dependence_ratio"].max()),
                "median_week_seam_ratio": _seam_ratio(scores, blocks),
            })
    return pd.DataFrame(diagnostic_rows), pd.concat(lag_rows, ignore_index=True)


def _plots(
    output: Path,
    rank_frames: dict[int, pd.DataFrame],
    diagnostics: pd.DataFrame,
    residual_lags: pd.DataFrame,
) -> None:
    colours = {"parent_rfm": "#440154", "rfd_piecewise6": "#22A884"}
    labels = {"parent_rfm": "global RFM", "rfd_piecewise6": "piecewise-6 RFD"}

    figure, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    for method in METHODS:
        row = diagnostics[(diagnostics["method"] == method) & (diagnostics["rank"] == 19)].iloc[0]
        axes[0].bar(labels[method], 100.0 * row["var_r2"], color=colours[method])
        axes[1].bar(labels[method], 100.0 * row["innovation_variance_fraction"], color=colours[method])
    axes[0].set(ylabel="one-step variance explained (%)", title="Blocked VAR(1) fit")
    axes[1].set(ylabel="innovation / score variance (%)", title="Unpredictable score share")
    for axis in axes:
        axis.grid(axis="y", alpha=0.2)
    figure.tight_layout()
    figure.savefig(output / "var_diagnostic.png", dpi=160)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(8.5, 4.5))
    for method in METHODS:
        selected = rank_frames[19][rank_frames[19]["method"] == method]
        columns = [f"score_{index:02d}" for index in range(1, 20)]
        variance = selected[columns].var(ddof=0).to_numpy(dtype=float)
        axis.plot(np.arange(1, 20), variance / variance.sum(), marker="o", label=labels[method], color=colours[method])
    axis.set(
        xlabel="score direction", ylabel="share of projected-score variance",
        title="Where the 19-dimensional score energy lives", xticks=np.arange(1, 20, 2),
    )
    axis.grid(alpha=0.2)
    axis.legend(frameon=False)
    figure.tight_layout()
    figure.savefig(output / "score_variance_profile.png", dpi=160)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(8.5, 4.5))
    for method in METHODS:
        selected = residual_lags[(residual_lags["method"] == method) & (residual_lags["rank"] == 19)]
        axis.plot(selected["lag"], selected["dependence_ratio"], marker="o", label=labels[method], color=colours[method])
    axis.set(
        xlabel="residual lag (hours)", ylabel="remaining dependence multiplier",
        title="What VAR(1) leaves behind", xticks=np.arange(1, 7),
    )
    axis.grid(alpha=0.2)
    axis.legend(frameon=False)
    figure.tight_layout()
    figure.savefig(output / "var_residual_dependence.png", dpi=160)
    plt.close(figure)


def build_design(
    config: dict[str, Any], panel: dict[str, np.ndarray], *, smoke: bool
) -> dict[str, Any]:
    years = panel["hours"].astype("datetime64[Y]").astype(int) + 1970
    return {
        "experiment_id": config["experiment"]["id"],
        "profile": "smoke" if smoke else "recorded",
        "development_years_loaded": sorted(set(years.tolist())),
        "sealed_evaluation_year": int(config["experiment"]["sealed_evaluation_year"]),
        "sealed_year_loaded": bool(np.any(years == int(config["experiment"]["sealed_evaluation_year"]))),
        "methods": list(METHODS),
        "frozen_ranks": config["source"]["frozen_ranks"],
        "mechanism_rank": int(config["source"]["mechanism_rank"]),
        "gauge_anchor": f"{config['materialization']['anchor_phase']} fold {config['materialization']['anchor_fold']}",
        "var_pairs": "within complete weeks only",
        "primary_head": config["head_policy"]["primary"],
        "kalman_status": config["head_policy"]["kalman"],
        "selects_or_tunes_any_choice": False,
        "observation_count": int(panel["covariances"].shape[0]),
    }


def _load_anchors(source: Path) -> dict[str, dict[int, np.ndarray]]:
    with np.load(source / "tuning" / "fold_0.npz", allow_pickle=False) as cache:
        return {
            method: {
                rank: cache[f"{method}_identity_loadings"][:rank].copy()
                for rank in (1, 19)
            }
            for method in METHODS
        }


def _fold_cache_paths(output: Path, phase: str, fold: int) -> dict[str, Path]:
    stem = output / "materialized" / f"{phase}_fold_{fold}"
    return {
        "rank1": stem.with_name(stem.name + "_rank1.csv"),
        "rank19": stem.with_name(stem.name + "_rank19.csv"),
        "alignment": stem.with_name(stem.name + "_alignment.csv"),
        "meta": stem.with_name(stem.name + ".meta.json"),
    }


def _write_fold_cache(output: Path, result: dict[str, Any], digest: str) -> None:
    directory = output / "materialized"
    directory.mkdir(parents=True, exist_ok=True)
    paths = _fold_cache_paths(output, result["phase"], result["fold"])
    _atomic_csv(paths["rank1"], result["rank1"])
    _atomic_csv(paths["rank19"], result["rank19"])
    _atomic_csv(paths["alignment"], result["alignment"])
    _atomic_json(paths["meta"], {"digest": digest})


def run(config: dict[str, Any], *, smoke: bool, force: bool) -> dict[str, Any]:
    hf2_config, panel, source = load_frozen_source(config)
    output_key = "smoke_directory" if smoke else "directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config, source, smoke=smoke)
    design = build_design(config, panel, smoke=smoke)
    design["digest"] = digest
    _atomic_json(output / "design.json", design)
    anchors = _load_anchors(source)

    jobs = []
    for phase in PHASES:
        data = hf2.phase_data(panel, hf2_config, phase, smoke=False)
        for fold in range(2):
            paths = _fold_cache_paths(output, phase, fold)
            fold_digest = f"{digest}:{phase}:{fold}"
            if force or not _cache_matches(paths["meta"], fold_digest) or not all(
                paths[name].is_file() for name in ("rank1", "rank19", "alignment")
            ):
                jobs.append((
                    phase, fold, data["covariances"], data["hours"], hf2_config,
                    config, source, smoke, anchors,
                ))
    if jobs:
        workers = min(int(config["runtime"]["workers"]), len(jobs))
        print(f"[scores] materialising {len(jobs)} phase/fold sources with {workers} workers", flush=True)
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_materialize_fold, job): (job[0], job[1]) for job in jobs}
            for future in as_completed(futures):
                phase, fold = futures[future]
                result = future.result()
                _write_fold_cache(output, result, f"{digest}:{phase}:{fold}")
                print(f"[scores] completed {phase} fold {fold}", flush=True)
    else:
        print("[scores] all digest-matched materialisations are cached", flush=True)

    rank_frames: dict[int, pd.DataFrame] = {}
    alignment = []
    for rank in (1, 19):
        rank_frames[rank] = pd.concat([
            pd.read_csv(_fold_cache_paths(output, phase, fold)[f"rank{rank}"])
            for phase in PHASES for fold in range(2)
        ], ignore_index=True).sort_values(["method", "hour"]).reset_index(drop=True)
    for phase in PHASES:
        for fold in range(2):
            alignment.append(pd.read_csv(_fold_cache_paths(output, phase, fold)["alignment"]))
    alignment_frame = pd.concat(alignment, ignore_index=True)
    diagnostics, residual_lags = diagnose_scores(rank_frames, config)

    _atomic_csv(output / "scores_rank1.csv", rank_frames[1])
    _atomic_csv(output / "scores_rank19.csv", rank_frames[19])
    _atomic_csv(output / "loading_alignment.csv", alignment_frame)
    _atomic_csv(output / "score_diagnostics.csv", diagnostics)
    _atomic_csv(output / "var_residual_lags.csv", residual_lags)
    _plots(output, rank_frames, diagnostics, residual_lags)

    report = [
        "# APP-HF-3 — projected-score observation diagnostic", "",
        f"**Profile:** {'smoke; non-scientific' if smoke else 'recorded'}  ",
        "**Status:** diagnostic only; no centre, rank, lag, or head was selected", "",
        "HF-3 reconstructed held-out score coordinates from the completed HF-2 polygons and loading bases. All fold gauges were aligned at the identity. VAR(1) diagnostics exclude every cross-week seam and use only genuine consecutive hourly pairs. Only 2024 was loaded; 2025 remains sealed.", "",
        "| arm | rank | VAR variance explained | innovation share | transition radius | max residual lag dependence | seam multiplier |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for method in METHODS:
        for rank in (1, 19):
            row = diagnostics[(diagnostics["method"] == method) & (diagnostics["rank"] == rank)].iloc[0]
            report.append(
                f"| {method} | {rank} | {100.0 * row['var_r2']:.2f}% | "
                f"{100.0 * row['innovation_variance_fraction']:.2f}% | "
                f"{row['transition_radius']:.4f} | "
                f"{row['maximum_residual_lag_dependence']:.4f} | "
                f"{row['median_week_seam_ratio']:.3f}x |"
            )
    report.extend([
        "", "## Interpretation boundary", "",
        "The scores are observable low-dimensional coordinates, not known structural amplitudes. Crypto provides no latent score truth, so HF-3 reports innovation and residual behaviour rather than a factor-score NRMSE. Rank 19 is the frozen reconstruction dimension; rank 1 is a mechanism diagnostic only.", "",
        "Kalman was not re-tuned here. Its status remains the inherited non-promoted sensitivity from the synthetic and monthly score-head audits. Parent-style VAR(1) with intercept remains the Paper 1 primary head, and HF-4 must apply every admitted head identically to parent RFM and RFD.", "",
        "All of 2025 remains sealed for APP-HF-4.", "",
    ])
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")
    result = {
        "profile": "smoke" if smoke else "recorded",
        "score_rows_rank19": int(len(rank_frames[19])),
        "only_2024_loaded": not design["sealed_year_loaded"] and design["development_years_loaded"] == [2024],
        "frozen_ranks": config["source"]["frozen_ranks"],
        "kalman_status": config["head_policy"]["kalman"],
        "report": str(output / "report.md"),
    }
    _atomic_json(output / "verdict.json", result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    config = load_configuration(args.config)
    _, panel, _ = load_frozen_source(config)
    design = build_design(config, panel, smoke=args.smoke)
    print(json.dumps(design, indent=2), flush=True)
    if args.dry_run:
        print("APP-HF-3 dry run passed; only 2024 was loaded and 2025 remains sealed.", flush=True)
        return
    result = run(config, smoke=args.smoke, force=args.force)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
