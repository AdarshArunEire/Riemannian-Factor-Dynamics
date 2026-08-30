"""APP-HF-4: final causal one-hour covariance forecast on 2025 crypto.

Every refit uses the trailing 26 weeks available at that origin. Geometry and
loading spaces are then held fixed for four weeks while revealed hourly scores
update matched VAR(1), coordinatewise OLS HAR, and ridge-VHAR heads. Rank 19
with VAR(1) is the frozen Paper 1 comparison; ranks 1--18 are sensitivities and
both score-HAR heads are retained post-freeze diagnostics excluded from the
paper. LOCF,
development-tuned EWMA and
log-SPD HAR use the same origins and targets.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
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
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "py"))

from experiments import run_hf2_representation as hf2  # noqa: E402
from rfd.estimators.frame import PolygonalFrame, transport_from_reference  # noqa: E402
from rfd.estimators.lag import (  # noqa: E402
    common_reference_tangent_rows,
    coordinate_tangents,
)
from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402
from rfd.forecast import (  # noqa: E402
    fit_coordinate_har,
    fit_ridge_vhar,
    fit_var1,
    forecast_coordinate_har,
    forecast_ridge_vhar,
)
from rfd.forecast_baselines import (  # noqa: E402
    ewma_forecasts,
    fit_log_har,
    forecast_log_har,
    locf_forecasts,
)
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.spd.bw import bw_clip_exp_tangent  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "hf4_forecast.yaml"
REPRESENTATION_METHODS = ("parent_rfm", "rfd_piecewise6")
BASELINE_METHODS = ("locf", "ewma", "loghar_spd")
REPRESENTATION_HEADS = ("var1", "har_ols", "vhar_ridge")
REPRESENTATION_CACHE_SCHEMA = 1


def load_configuration(path: Path = CONFIG_DEFAULT) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    representation = config["representation"]
    baselines = config["baselines"]
    score_heads = config["score_heads"]
    if int(experiment["development_year"]) != 2024 or int(experiment["evaluation_year"]) != 2025:
        raise ValueError("HF-4 freezes 2024 development and 2025 evaluation")
    if int(experiment["forecast_horizon_hours"]) != 1:
        raise ValueError("HF-4 primary horizon is exactly one hour")
    if int(experiment["training_weeks"]) != 26:
        raise ValueError("HF-4 uses a trailing 26-week representation window")
    if int(experiment["refit_every_hours"]) != 4 * 168:
        raise ValueError("HF-4 geometric refits are frozen every four weeks")
    if int(experiment["max_lag"]) != 6 or int(representation["max_lag"]) != 6:
        raise ValueError("both representation arms use six hourly lags")
    if tuple(representation["methods"]) != REPRESENTATION_METHODS:
        raise ValueError("HF-4 requires exact parent/RFD arm parity")
    if int(representation["piecewise_segments"]) != 6:
        raise ValueError("HF-1 freezes the RFD centre at piecewise-6")
    if int(representation["primary_rank"]) != 19:
        raise ValueError("rank 19 is the frozen operational headline")
    expected_sensitivities = list(range(1, int(representation["primary_rank"])))
    if list(map(int, representation["sensitivity_ranks"])) != expected_sensitivities:
        raise ValueError("HF-4 exploratory sensitivities must contain every rank 1 through 18")
    if representation["future_centre_policy"] != "carry_terminal_until_refit":
        raise ValueError("HF-4 carries the terminal centre until the next refit")
    if tuple(score_heads["methods"]) != REPRESENTATION_HEADS:
        raise ValueError("HF-4 requires matched VAR, OLS-HAR and ridge-VHAR heads")
    if (
        int(score_heads["har_daily_hours"]) != 24
        or int(score_heads["har_weekly_hours"]) != 168
    ):
        raise ValueError("HF-4 score HAR windows are frozen at 24 and 168 hours")
    if (
        not np.isfinite(float(score_heads["vhar_ridge"]))
        or float(score_heads["vhar_ridge"]) < 0.0
    ):
        raise ValueError("HF-4 ridge-VHAR penalty must be finite and nonnegative")
    if score_heads["vhar_feature_scaling"] != "training_standard_deviation":
        raise ValueError("HF-4 ridge VHAR must use training-only feature scaling")
    if tuple(baselines["methods"]) != BASELINE_METHODS:
        raise ValueError("HF-4 requires LOCF, EWMA, and log-SPD HAR baselines")
    candidates = list(map(float, baselines["ewma_candidates"]))
    if candidates != sorted(set(candidates)) or any(not 0.0 < value < 1.0 for value in candidates):
        raise ValueError("EWMA candidates must be unique, increasing, and interior")
    if int(baselines["har_daily_hours"]) != 24 or int(baselines["har_weekly_hours"]) != 168:
        raise ValueError("HF-4 HAR windows are frozen at 24 and 168 hours")
    if baselines["har_parameterization"] != "coordinatewise_log_euclidean":
        raise ValueError("HF-4 HAR must remain SPD through the log-Euclidean parameterisation")
    if config["evaluation"]["primary_losses"] != ["frobenius2", "qlike"]:
        raise ValueError("HF-4 primary losses are Frobenius and QLIKE")
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


def _atomic_npz(path: Path, **arrays: np.ndarray) -> None:
    temporary = path.with_suffix(".tmp.npz")
    np.savez(temporary, **arrays)
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
        raise FileNotFoundError(f"HF-0 panel is missing: {path}")
    with np.load(path, allow_pickle=False) as source:
        observations = source["covariances"].copy()
        hours = source["hours"].copy()
        symbols = source["symbols"].astype(str)
    size = int(config["experiment"]["matrix_size"])
    if observations.ndim != 3 or observations.shape[1:] != (size, size):
        raise ValueError("HF-4 panel matrix size disagrees with the frozen contract")
    if np.any(np.diff(hours) != np.timedelta64(1, "h")):
        raise ValueError("HF-4 requires a contiguous hourly panel")
    if not np.isfinite(observations).all() or np.any(np.linalg.eigvalsh(observations) <= 0.0):
        raise ValueError("HF-4 requires finite full-rank covariance observations")
    years = hours.astype("datetime64[Y]").astype(int) + 1970
    if set(years.tolist()) != {2024, 2025}:
        raise ValueError("HF-4 panel must contain exactly the frozen 2024--2025 years")
    return {"covariances": observations, "hours": hours, "symbols": symbols, "years": years}


def forecast_blocks(
    panel: dict[str, np.ndarray], config: dict[str, Any], *, smoke: bool
) -> list[dict[str, int]]:
    years = panel["years"]
    if smoke:
        interval = int(config["smoke"]["hours_per_block"])
        count = int(config["smoke"]["refit_blocks"])
        training_hours = int(config["smoke"]["training_weeks"]) * 168
        development = np.flatnonzero(
            years == int(config["experiment"]["development_year"])
        )
        end = int(development[-1] + 1)
        start = end - count * interval
        starts = [start + index * interval for index in range(count)]
    else:
        evaluation = np.flatnonzero(
            years == int(config["experiment"]["evaluation_year"])
        )
        start = int(evaluation[0])
        end = int(evaluation[-1] + 1)
        interval = int(config["experiment"]["refit_every_hours"])
        training_hours = int(config["experiment"]["training_weeks"]) * 168
        starts = list(range(start, end, interval))
    blocks = []
    for index, target_start in enumerate(starts):
        target_stop = min(target_start + interval, end)
        training_start = target_start - training_hours
        if training_start < 0:
            raise ValueError("HF-4 lacks the declared trailing training window")
        blocks.append({
            "block": int(index),
            "training_start": int(training_start),
            "training_stop": int(target_start),
            "target_start": int(target_start),
            "target_stop": int(target_stop),
        })
    return blocks


def tune_ewma(development: np.ndarray, config: dict[str, Any]) -> tuple[float, pd.DataFrame]:
    burn = int(config["baselines"]["ewma_tuning_burn_hours"])
    training = development[:burn]
    targets = development[burn:]
    rows = []
    for decay in map(float, config["baselines"]["ewma_candidates"]):
        forecasts = ewma_forecasts(training, targets, decay)
        rows.append({
            "decay": decay,
            "mean_frobenius2": float(frobenius_loss(forecasts, targets).mean()),
            "mean_qlike": float(qlike_loss(forecasts, targets).mean()),
        })
    table = pd.DataFrame(rows)
    table["joint_log_relative_loss"] = (
        np.log(table["mean_frobenius2"] / table["mean_frobenius2"].min())
        + np.log(table["mean_qlike"] / table["mean_qlike"].min())
    )
    selected = float(table.sort_values(["joint_log_relative_loss", "decay"]).iloc[0]["decay"])
    table["selected"] = table["decay"] == selected
    return selected, table


def _extended_frame(frame: PolygonalFrame, stop: float) -> PolygonalFrame:
    if stop <= float(frame.vertex_times[-1]):
        return frame
    return PolygonalFrame(
        np.append(frame.vertex_times, stop),
        np.concatenate((frame.vertices, frame.vertices[-1][None]), axis=0),
        frame.geometry,
    )


def representation_cache_base_digest(config: dict[str, Any], *, smoke: bool) -> str:
    """Digest only inputs that determine the reusable geometric representation.

    Rank grids and forecast-head choices are deliberately excluded. A cache
    remains valid when a VAR head is replaced by HAR or when another prefix of
    the same maximum-rank loading basis is requested.
    """
    experiment = config["experiment"]
    representation = config["representation"]
    producer_paths = [
        ROOT / experiment["panel_path"],
        ROOT / "experiments" / "run_hf2_representation.py",
        ROOT / "py" / "rfd" / "estimators" / "centre_low_n.py",
        ROOT / "py" / "rfd" / "estimators" / "frame.py",
        ROOT / "py" / "rfd" / "estimators" / "lag.py",
        ROOT / "py" / "rfd" / "geometry.py",
        ROOT / "py" / "rfd" / "spd" / "bw.py",
    ]
    payload = {
        "schema": REPRESENTATION_CACHE_SCHEMA,
        "profile": "smoke" if smoke else "recorded",
        "matrix_size": int(experiment["matrix_size"]),
        "training_weeks": int(
            config["smoke"]["training_weeks"] if smoke else experiment["training_weeks"]
        ),
        "max_lag": int(representation["max_lag"]),
        "piecewise_segments": int(representation["piecewise_segments"]),
        "mean_tolerance": float(representation["mean_tolerance"]),
        "mean_max_iterations": int(representation["mean_max_iterations"]),
        "tail_mode": str(representation["tail_mode"]),
        "normalization": str(representation["normalization"]),
        "future_centre_policy": str(representation["future_centre_policy"]),
        "maximum_cached_rank": int(representation["primary_rank"]),
        "producer_sha256": {
            str(path.relative_to(ROOT)): _sha256(path) for path in producer_paths
        },
    }
    material = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _representation_cache_paths(
    output: Path, block: int, method: str,
) -> tuple[Path, Path]:
    directory = output / "representation_cache" / f"block_{block:02d}"
    directory.mkdir(parents=True, exist_ok=True)
    return directory / f"{method}.npz", directory / f"{method}.meta.json"


def _representation_stage_digest(
    base_digest: str, block: dict[str, int], method: str,
) -> str:
    boundaries = ":".join(
        str(block[key])
        for key in ("block", "training_start", "training_stop", "target_start", "target_stop")
    )
    return hashlib.sha256(
        f"{base_digest}:{method}:{boundaries}".encode("utf-8")
    ).hexdigest()


def _fit_representation_stage(
    method: str,
    training: np.ndarray,
    targets: np.ndarray,
    config: dict[str, Any],
) -> dict[str, np.ndarray]:
    representation = config["representation"]
    n = training.shape[0]
    training_times = np.linspace(0.0, 1.0, n)
    started = time.perf_counter()
    fit = hf2._fit_arm(
        training, training_times, np.ones(n, dtype=bool), method, config
    )
    fit_seconds = float(time.perf_counter() - started)
    future_times = 1.0 + np.arange(1, targets.shape[0] + 1, dtype=float) / n
    frame = _extended_frame(fit["frame"], float(future_times[-1]))
    future = common_reference_tangent_rows(targets, future_times, frame)
    row_mean = fit["lag_row"].row_mean
    maximum_rank = int(representation["primary_rank"])
    loadings = fit["spectrum"].eigenvectors[:, :maximum_rank]
    return {
        "training_scores": (fit["tangent_rows"].rows - row_mean) @ loadings,
        "revealed_scores": (future.rows - row_mean) @ loadings,
        "loadings": loadings,
        "row_mean": row_mean,
        "basis": future.basis,
        "future_times": future_times,
        "future_local_centres": future.local_centres,
        "frame_vertex_times": frame.vertex_times,
        "frame_vertices": frame.vertices,
        "fit_seconds": np.asarray(fit_seconds),
    }


def _validate_representation_stage(stage: dict[str, np.ndarray]) -> None:
    required = {
        "training_scores", "revealed_scores", "loadings", "row_mean", "basis",
        "future_times", "future_local_centres", "frame_vertex_times",
        "frame_vertices", "fit_seconds",
    }
    if set(stage) != required:
        raise ValueError("representation cache has an invalid array contract")
    if not all(np.isfinite(np.asarray(value)).all() for value in stage.values()):
        raise ValueError("representation cache contains NaN or Inf")
    training_scores = np.asarray(stage["training_scores"])
    revealed_scores = np.asarray(stage["revealed_scores"])
    loadings = np.asarray(stage["loadings"])
    row_mean = np.asarray(stage["row_mean"])
    basis = np.asarray(stage["basis"])
    future_times = np.asarray(stage["future_times"])
    future_centres = np.asarray(stage["future_local_centres"])
    if training_scores.ndim != 2 or revealed_scores.ndim != 2:
        raise ValueError("cached score arrays must be matrices")
    if training_scores.shape[1] != revealed_scores.shape[1]:
        raise ValueError("cached score arrays disagree on maximum rank")
    if loadings.shape != (row_mean.size, training_scores.shape[1]):
        raise ValueError("cached loading matrix has an invalid shape")
    if basis.shape[0] != row_mean.size:
        raise ValueError("cached tangent basis disagrees with row dimension")
    if future_times.shape != (revealed_scores.shape[0],):
        raise ValueError("cached future times disagree with revealed scores")
    if future_centres.shape[0] != revealed_scores.shape[0]:
        raise ValueError("cached future centres disagree with revealed scores")
    PolygonalFrame(
        stage["frame_vertex_times"], stage["frame_vertices"], BW_GEOMETRY
    )


def _load_or_fit_representation_stage(
    method: str,
    training: np.ndarray,
    targets: np.ndarray,
    config: dict[str, Any],
    output: Path,
    block: dict[str, int],
    base_digest: str,
) -> tuple[dict[str, np.ndarray], bool]:
    cache, meta = _representation_cache_paths(output, block["block"], method)
    digest = _representation_stage_digest(base_digest, block, method)
    if cache.is_file() and _cache_matches(meta, digest):
        with np.load(cache, allow_pickle=False) as source:
            stage = {name: source[name].copy() for name in source.files}
        _validate_representation_stage(stage)
        return stage, True

    stage = _fit_representation_stage(method, training, targets, config)
    _validate_representation_stage(stage)
    _atomic_npz(cache, **stage)
    _atomic_json(meta, {
        "digest": digest,
        "schema": REPRESENTATION_CACHE_SCHEMA,
        "maximum_rank": int(stage["training_scores"].shape[1]),
        "training_rows": int(stage["training_scores"].shape[0]),
        "revealed_rows": int(stage["revealed_scores"].shape[0]),
    })
    return stage, False


def _representation_forecasts_from_stage(
    stage: dict[str, np.ndarray],
    config: dict[str, Any],
    *,
    heads: tuple[str, ...] = REPRESENTATION_HEADS,
) -> tuple[
    dict[tuple[str, int], np.ndarray],
    dict[tuple[str, int], dict[str, float]],
]:
    representation = config["representation"]
    if not heads or any(head not in REPRESENTATION_HEADS for head in heads):
        raise ValueError("requested an unknown or empty representation-head set")
    _validate_representation_stage(stage)
    frame = PolygonalFrame(
        stage["frame_vertex_times"], stage["frame_vertices"], BW_GEOMETRY
    )
    ranks = [int(representation["primary_rank"]), *map(int, representation["sensitivity_ranks"])]
    ranks = sorted(set(ranks))
    if max(ranks) > stage["training_scores"].shape[1]:
        raise ValueError("requested rank exceeds the cached maximum rank")
    forecasts: dict[tuple[str, int], np.ndarray] = {}
    diagnostics: dict[tuple[str, int], dict[str, float]] = {}
    for rank in ranks:
        loadings = stage["loadings"][:, :rank]
        training_scores = stage["training_scores"][:, :rank]
        revealed_scores = stage["revealed_scores"][:, :rank]
        head_outputs = {}
        if "var1" in heads:
            latest = _causal_latest_scores(training_scores, revealed_scores)
            head_started = time.perf_counter()
            var = fit_var1(training_scores)
            var_scores = np.asarray([var.forecast(score) for score in latest])
            head_outputs["var1"] = (
                var_scores,
                float(np.max(np.abs(np.linalg.eigvals(var.coefficients[1:].T)))),
                float(time.perf_counter() - head_started),
            )
        if "har_ols" in heads:
            head_started = time.perf_counter()
            har = fit_coordinate_har(
                training_scores,
                daily_window=int(config["score_heads"]["har_daily_hours"]),
                weekly_window=int(config["score_heads"]["har_weekly_hours"]),
            )
            har_scores = forecast_coordinate_har(
                har, training_scores, revealed_scores
            )
            head_outputs["har_ols"] = (
                har_scores,
                float(np.max(np.abs(np.linalg.eigvals(har.hourly_transition)))),
                float(time.perf_counter() - head_started),
            )
        if "vhar_ridge" in heads:
            head_started = time.perf_counter()
            vhar = fit_ridge_vhar(
                training_scores,
                daily_window=int(config["score_heads"]["har_daily_hours"]),
                weekly_window=int(config["score_heads"]["har_weekly_hours"]),
                ridge=float(config["score_heads"]["vhar_ridge"]),
            )
            vhar_scores = forecast_ridge_vhar(
                vhar, training_scores, revealed_scores
            )
            head_outputs["vhar_ridge"] = (
                vhar_scores,
                float(np.max(np.abs(np.linalg.eigvals(vhar.hourly_transition)))),
                float(time.perf_counter() - head_started),
            )
        for head in heads:
            forecast_scores, radius, head_seconds = head_outputs[head]
            forecast_rows = stage["row_mean"] + forecast_scores @ loadings.T
            reference_vectors = coordinate_tangents(forecast_rows, stage["basis"])
            local_vectors = transport_from_reference(
                frame, reference_vectors, stage["future_times"]
            )
            clipped = bw_clip_exp_tangent(
                stage["future_local_centres"],
                local_vectors,
                step_margin=float(representation["forecast_step_margin"]),
            )
            matrices = BW_GEOMETRY.exp(
                stage["future_local_centres"], clipped.tangent
            )
            key = (head, rank)
            forecasts[key] = matrices
            diagnostics[key] = {
                "transition_radius": radius,
                "clip_fraction": float(np.mean(clipped.factors < 1.0)),
                "minimum_clip_factor": float(np.min(clipped.factors)),
                "representation_fit_seconds": float(stage["fit_seconds"]),
                "head_fit_seconds": head_seconds,
            }
    return forecasts, diagnostics


def _causal_latest_scores(
    training_scores: np.ndarray, revealed_scores: np.ndarray,
) -> np.ndarray:
    """State available immediately before each forecast target.

    The first forecast uses the last training score. Thereafter target t's
    observed score is revealed only for forecasting target t+1.
    """
    training_scores = np.asarray(training_scores, dtype=float)
    revealed_scores = np.asarray(revealed_scores, dtype=float)
    if training_scores.ndim != 2 or revealed_scores.ndim != 2:
        raise ValueError("training and revealed scores must be matrices")
    if training_scores.shape[0] == 0 or revealed_scores.shape[0] == 0:
        raise ValueError("training and revealed scores must be nonempty")
    if training_scores.shape[1] != revealed_scores.shape[1]:
        raise ValueError("training and revealed scores must have equal width")
    if not np.isfinite(training_scores).all() or not np.isfinite(revealed_scores).all():
        raise ValueError("training and revealed scores must be finite")
    return np.vstack((training_scores[-1], revealed_scores[:-1]))


def _representation_forecasts(
    method: str,
    training: np.ndarray,
    targets: np.ndarray,
    config: dict[str, Any],
) -> tuple[
    dict[tuple[str, int], np.ndarray],
    dict[tuple[str, int], dict[str, float]],
]:
    """Uncached compatibility wrapper used by focused unit tests."""
    stage = _fit_representation_stage(method, training, targets, config)
    return _representation_forecasts_from_stage(stage, config)


def _gmv_metrics(forecasts: np.ndarray, targets: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    size = forecasts.shape[1]
    ones = np.ones(size)
    realised = np.empty(forecasts.shape[0])
    calibration = np.empty(forecasts.shape[0])
    for index, (forecast, target) in enumerate(zip(forecasts, targets)):
        raw = np.linalg.solve(forecast, ones)
        weights = raw / float(ones @ raw)
        predicted_variance = float(weights @ forecast @ weights)
        realised[index] = float(weights @ target @ weights)
        calibration[index] = abs(realised[index] - predicted_variance)
    return realised, calibration


def _score_forecasts(
    method: str,
    head: str,
    rank: int,
    role: str,
    forecasts: np.ndarray,
    targets: np.ndarray,
    hours: np.ndarray,
    block: int,
    diagnostics: dict[str, float] | None = None,
) -> pd.DataFrame:
    gmv, calibration = _gmv_metrics(forecasts, targets)
    eigenvalues = np.linalg.eigvalsh(forecasts)
    diagnostics = diagnostics or {}
    return pd.DataFrame({
        "block": int(block),
        "target_hour": hours.astype("datetime64[h]").astype(str),
        "method": method,
        "head": head,
        "rank": int(rank),
        "rank_role": role,
        "frobenius2": frobenius_loss(forecasts, targets),
        "qlike": qlike_loss(forecasts, targets),
        "bw2": bw_loss(forecasts, targets),
        "gmv_realized_variance": gmv,
        "gmv_variance_calibration": calibration,
        "forecast_minimum_eigenvalue": eigenvalues[:, 0],
        "forecast_condition_number": eigenvalues[:, -1] / eigenvalues[:, 0],
        "transition_radius": float(diagnostics.get("transition_radius", math.nan)),
        "clip_fraction": float(diagnostics.get("clip_fraction", 0.0)),
        "minimum_clip_factor": float(diagnostics.get("minimum_clip_factor", 1.0)),
        "representation_fit_seconds": float(
            diagnostics.get("representation_fit_seconds", 0.0)
        ),
        "head_fit_seconds": float(diagnostics.get("head_fit_seconds", 0.0)),
    })


def _frozen_original_path(output: Path, block: int) -> Path:
    return output / "frozen_original_var" / f"block_{block:02d}.csv"


def _normalise_frozen_original_rows(
    frame: pd.DataFrame,
    *,
    block: dict[str, int],
    target_hours: np.ndarray,
) -> pd.DataFrame:
    """Validate and label already-recorded baseline/VAR rows for reuse."""
    frame = frame.copy()
    if "head" not in frame:
        frame["head"] = np.where(frame["rank"].astype(int) == 0, "native", "var1")
    frame = frame[
        (frame["head"] == "native") | (frame["head"] == "var1")
    ].copy()
    if "fit_seconds" in frame and "representation_fit_seconds" not in frame:
        frame = frame.rename(columns={"fit_seconds": "representation_fit_seconds"})
    if "representation_fit_seconds" not in frame:
        frame["representation_fit_seconds"] = 0.0
    if "head_fit_seconds" not in frame:
        frame["head_fit_seconds"] = 0.0

    expected_hours = target_hours.astype("datetime64[h]").astype(str)
    expected_rows_per_hour = len(BASELINE_METHODS) + len(REPRESENTATION_METHODS) * 19
    if len(frame) != len(expected_hours) * expected_rows_per_hour:
        raise RuntimeError("frozen HF-4 original block has an unexpected row count")
    if frame.duplicated(["target_hour", "method", "head", "rank"]).any():
        raise RuntimeError("frozen HF-4 original block has duplicate forecast keys")
    if set(frame["target_hour"].astype(str)) != set(expected_hours.tolist()):
        raise RuntimeError("frozen HF-4 original block has the wrong target hours")
    counts = frame.groupby("target_hour").size().to_numpy()
    if not np.all(counts == expected_rows_per_hour):
        raise RuntimeError("frozen HF-4 original block is incomplete by hour")
    baselines = frame[frame["head"] == "native"]
    if set(baselines["method"]) != set(BASELINE_METHODS) or set(baselines["rank"]) != {0}:
        raise RuntimeError("frozen HF-4 baseline contract changed")
    original = frame[frame["head"] == "var1"]
    if set(original["method"]) != set(REPRESENTATION_METHODS):
        raise RuntimeError("frozen HF-4 VAR representation contract changed")
    if set(original["rank"].astype(int)) != set(range(1, 20)):
        raise RuntimeError("frozen HF-4 VAR rank grid changed")
    required = [
        "frobenius2", "qlike", "bw2", "gmv_realized_variance",
        "forecast_minimum_eigenvalue",
    ]
    if not np.isfinite(frame[required].to_numpy(dtype=float)).all():
        raise RuntimeError("frozen HF-4 original rows contain NaN or Inf")
    if (frame["forecast_minimum_eigenvalue"] <= 0.0).any():
        raise RuntimeError("frozen HF-4 original rows contain a non-SPD forecast")
    if set(frame["block"].astype(int)) != {int(block["block"])}:
        raise RuntimeError("frozen HF-4 original rows have the wrong block id")
    return frame


def _load_frozen_original_rows(
    output: Path,
    block: dict[str, int],
    target_hours: np.ndarray,
) -> pd.DataFrame | None:
    frozen = _frozen_original_path(output, block["block"])
    current, _ = _block_paths(output, block["block"])
    source = frozen if frozen.is_file() else current
    if not source.is_file():
        return None
    return _normalise_frozen_original_rows(
        pd.read_csv(source), block=block, target_hours=target_hours
    )


def _archive_recorded_original_blocks(
    output: Path,
    blocks: list[dict[str, int]],
) -> int:
    """Preserve exact pre-augmentation block CSVs before combined rewrites."""
    archived = 0
    directory = output / "frozen_original_var"
    for block in blocks:
        current, _ = _block_paths(output, block["block"])
        frozen = _frozen_original_path(output, block["block"])
        if frozen.is_file() or not current.is_file():
            continue
        columns = pd.read_csv(current, nrows=0).columns
        if "head" in columns:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        temporary = frozen.with_suffix(".tmp.csv")
        shutil.copyfile(current, temporary)
        temporary.replace(frozen)
        archived += 1
    return archived


def _block_worker(
    payload: tuple[int, dict[str, int], dict[str, Any], float, bool, str]
) -> pd.DataFrame:
    block_index, block, config, ewma_decay, smoke, base_digest = payload
    panel = load_panel(config)
    observations = panel["covariances"]
    hours = panel["hours"]
    training = observations[block["training_start"]:block["training_stop"]]
    targets = observations[block["target_start"]:block["target_stop"]]
    target_hours = hours[block["target_start"]:block["target_stop"]]
    output_key = "smoke_directory" if smoke else "directory"
    output = ROOT / config["output"][output_key]
    rows = []
    frozen_original = _load_frozen_original_rows(output, block, target_hours)
    if frozen_original is not None:
        rows.append(frozen_original)
        requested_heads = ("har_ols", "vhar_ridge")
        print(f"[frozen original] block {block_index + 1}", flush=True)
    else:
        requested_heads = REPRESENTATION_HEADS
        baseline_forecasts = {
            "locf": locf_forecasts(training[-1], targets),
            "ewma": ewma_forecasts(training, targets, ewma_decay),
        }
        har = fit_log_har(
            training,
            daily_window=int(config["baselines"]["har_daily_hours"]),
            weekly_window=int(config["baselines"]["har_weekly_hours"]),
        )
        baseline_forecasts["loghar_spd"] = forecast_log_har(har, training, targets)
        for method in BASELINE_METHODS:
            rows.append(_score_forecasts(
                method, "native", 0, "baseline", baseline_forecasts[method], targets,
                target_hours, block_index,
            ))

    for method in REPRESENTATION_METHODS:
        stage, cache_hit = _load_or_fit_representation_stage(
            method, training, targets, config, output, block, base_digest
        )
        forecasts, diagnostics = _representation_forecasts_from_stage(
            stage, config, heads=requested_heads
        )
        if cache_hit:
            print(
                f"[representation cache] block {block_index + 1} {method}",
                flush=True,
            )
        for (head, rank), matrices in forecasts.items():
            if head != "var1":
                role = "internal_diagnostic"
            else:
                role = (
                    "headline"
                    if rank == int(config["representation"]["primary_rank"])
                    else "sensitivity"
                )
            rows.append(_score_forecasts(
                method, head, rank, role, matrices, targets, target_hours,
                block_index, diagnostics[(head, rank)],
            ))
    return pd.concat(rows, ignore_index=True)


def experiment_digest(config: dict[str, Any], ewma_decay: float, *, smoke: bool) -> str:
    paths = [
        Path(config["config_path"]), ROOT / config["experiment"]["panel_path"],
        Path(__file__), ROOT / "py" / "rfd" / "forecast_baselines.py",
        ROOT / "py" / "rfd" / "forecast.py",
        ROOT / "py" / "rfd" / "estimators" / "centre_low_n.py",
        ROOT / "py" / "rfd" / "estimators" / "frame.py",
        ROOT / "py" / "rfd" / "estimators" / "lag.py",
    ]
    material = "\n".join(f"{path.resolve()}:{_sha256(path)}" for path in paths)
    material += f"\newma={ewma_decay}\nprofile={'smoke' if smoke else 'recorded'}"
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def build_design(
    config: dict[str, Any], panel: dict[str, np.ndarray], blocks: list[dict[str, int]],
    ewma_decay: float, *, smoke: bool,
) -> dict[str, Any]:
    first = blocks[0]
    last = blocks[-1]
    return {
        "experiment_id": config["experiment"]["id"],
        "profile": "smoke" if smoke else "recorded",
        "development_year": 2024,
        "target_year": int(panel["years"][first["target_start"]]),
        "scientific_evaluation": not smoke,
        "first_target": str(panel["hours"][first["target_start"]]),
        "last_target": str(panel["hours"][last["target_stop"] - 1]),
        "forecast_hours": int(sum(block["target_stop"] - block["target_start"] for block in blocks)),
        "refit_blocks": int(len(blocks)),
        "training_hours_per_refit": int(first["training_stop"] - first["training_start"]),
        "refit_every_hours": int(config["smoke"]["hours_per_block"] if smoke else config["experiment"]["refit_every_hours"]),
        "primary_rank": int(config["representation"]["primary_rank"]),
        "sensitivity_ranks": list(map(int, config["representation"]["sensitivity_ranks"])),
        "representation_heads": list(REPRESENTATION_HEADS),
        "score_har": {
            "daily_hours": int(config["score_heads"]["har_daily_hours"]),
            "weekly_hours": int(config["score_heads"]["har_weekly_hours"]),
            "publication_scope": "internal_diagnostic_only",
            "vhar_ridge": float(config["score_heads"]["vhar_ridge"]),
            "vhar_feature_scaling": str(config["score_heads"]["vhar_feature_scaling"]),
        },
        "baselines": list(BASELINE_METHODS),
        "selected_ewma_decay_from_2024": float(ewma_decay),
        "primary_losses": ["frobenius2", "qlike"],
        "future_centre_policy": "carry terminal centre until four-week refit",
        "rank_curve_scope": "exploratory discovery; rank 19 VAR(1) remains the original headline",
        "head_scope": "Paper 1 publishes matched VAR(1) only; coordinatewise OLS HAR and ridge VHAR are retained internal diagnostics",
    }


def _block_paths(output: Path, block: int) -> tuple[Path, Path]:
    directory = output / "blocks"
    return directory / f"block_{block:02d}.csv", directory / f"block_{block:02d}.meta.json"


def _summary(raw: pd.DataFrame) -> pd.DataFrame:
    metrics = ["frobenius2", "qlike", "bw2", "gmv_realized_variance", "gmv_variance_calibration"]
    rows = []
    for (method, head, rank, role), frame in raw.groupby(
        ["method", "head", "rank", "rank_role"], sort=False
    ):
        row = {
            "method": method, "head": head, "rank": int(rank),
            "rank_role": role, "hours": int(len(frame)),
        }
        for metric in metrics:
            row[f"mean_{metric}"] = float(frame[metric].mean())
            row[f"se_{metric}"] = float(frame[metric].std(ddof=1) / math.sqrt(len(frame)))
        row["maximum_condition_number"] = float(frame["forecast_condition_number"].max())
        row["minimum_eigenvalue"] = float(frame["forecast_minimum_eigenvalue"].min())
        row["maximum_clip_fraction"] = float(frame["clip_fraction"].max())
        rows.append(row)
    return pd.DataFrame(rows)


def _rank_comparison(summary: pd.DataFrame) -> pd.DataFrame:
    rows = []
    available = summary[summary["method"].isin(REPRESENTATION_METHODS)]
    ranks = sorted(available["rank"].astype(int).unique().tolist())
    for head in REPRESENTATION_HEADS:
        for rank in ranks:
            parent = summary[
                (summary["method"] == "parent_rfm")
                & (summary["head"] == head)
                & (summary["rank"] == rank)
            ].iloc[0]
            rfd = summary[
                (summary["method"] == "rfd_piecewise6")
                & (summary["head"] == head)
                & (summary["rank"] == rank)
            ].iloc[0]
            rows.append({
                "head": head,
                "rank": rank,
                **{
                    f"rfd_reduction_percent_{metric}": 100.0 * (
                        1.0 - float(rfd[f"mean_{metric}"])
                        / float(parent[f"mean_{metric}"])
                    )
                    for metric in (
                        "frobenius2", "qlike", "bw2",
                        "gmv_realized_variance",
                    )
                },
            })
    return pd.DataFrame(rows)


def newey_west_mean_interval(values: np.ndarray, max_lag: int = 168) -> dict[str, float]:
    """Mean and 95% interval using a Bartlett Newey--West long-run variance."""
    values = np.asarray(values, dtype=float)
    if values.ndim != 1 or values.size < 2 or not np.isfinite(values).all():
        raise ValueError("values must be a finite vector with at least two entries")
    centred = values - values.mean()
    lag = min(int(max_lag), values.size - 1)
    long_run = float(centred @ centred / values.size)
    for offset in range(1, lag + 1):
        covariance = float(centred[offset:] @ centred[:-offset] / values.size)
        long_run += 2.0 * (1.0 - offset / (lag + 1.0)) * covariance
    standard_error = math.sqrt(max(long_run, 0.0) / values.size)
    mean = float(values.mean())
    return {
        "mean_difference_rfd_minus_parent": mean,
        "newey_west_se": standard_error,
        "ci95_lower": mean - 1.96 * standard_error,
        "ci95_upper": mean + 1.96 * standard_error,
        "max_lag": int(lag),
    }


def _paired_rank19_inference(raw: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for head in REPRESENTATION_HEADS:
        selected = raw[
            (raw["rank"] == 19)
            & (raw["head"] == head)
            & raw["method"].isin(REPRESENTATION_METHODS)
        ]
        for metric in ("frobenius2", "qlike"):
            pivot = selected.pivot(
                index="target_hour", columns="method", values=metric
            )
            difference = (
                pivot["rfd_piecewise6"] - pivot["parent_rfm"]
            ).to_numpy(dtype=float)
            rows.append({
                "head": head,
                "metric": metric,
                **newey_west_mean_interval(difference),
            })
    return pd.DataFrame(rows)


def _paired_rank19_head_inference(raw: pd.DataFrame) -> pd.DataFrame:
    """Test optional ridge VHAR against the main coordinatewise OLS HAR."""
    rows = []
    selected = raw[raw["rank"] == 19]
    for method in REPRESENTATION_METHODS:
        method_rows = selected[selected["method"] == method]
        for metric in ("frobenius2", "qlike"):
            pivot = method_rows.pivot(
                index="target_hour", columns="head", values=metric
            )
            difference = (
                pivot["vhar_ridge"] - pivot["har_ols"]
            ).to_numpy(dtype=float)
            interval = newey_west_mean_interval(difference)
            rows.append({
                "method": method,
                "metric": metric,
                "comparison": "vhar_ridge_minus_har_ols",
                "mean_difference_vhar_minus_har": interval[
                    "mean_difference_rfd_minus_parent"
                ],
                "newey_west_se": interval["newey_west_se"],
                "ci95_lower": interval["ci95_lower"],
                "ci95_upper": interval["ci95_upper"],
                "max_lag": interval["max_lag"],
            })
    return pd.DataFrame(rows)


def _plots(output: Path, raw: pd.DataFrame, summary: pd.DataFrame, ranks: pd.DataFrame) -> None:
    colours = {
        "locf": "#9E9E9E", "ewma": "#FDE725", "loghar_spd": "#35B779",
        "parent_rfm": "#440154", "rfd_piecewise6": "#31688E",
    }
    headline = summary[
        (summary["rank_role"] == "baseline")
        | ((summary["rank_role"] == "headline") & (summary["head"] == "var1"))
    ].copy()
    labels = []
    values = {"frobenius2": [], "qlike": []}
    locf = headline[headline["method"] == "locf"].iloc[0]
    for _, row in headline.iterrows():
        labels.append(row["method"].replace("_", " "))
        for metric in values:
            values[metric].append(100.0 * (1.0 - row[f"mean_{metric}"] / locf[f"mean_{metric}"]))
    figure, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    for axis, metric, title in zip(axes, values, ("Frobenius", "QLIKE")):
        axis.bar(labels, values[metric], color=[colours[m] for m in headline["method"]])
        axis.axhline(0.0, color="black", linewidth=0.8)
        axis.set(ylabel="error reduction versus LOCF (%)", title=title)
        axis.tick_params(axis="x", rotation=25)
        axis.grid(axis="y", alpha=0.2)
    figure.suptitle("One-hour covariance forecast")
    figure.tight_layout()
    figure.savefig(output / "headline_forecast.png", dpi=160)
    plt.close(figure)

    figure, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    head_colours = {
        "var1": "#31688E", "har_ols": "#35B779", "vhar_ridge": "#FDE725"
    }
    for axis, metric, title in zip(axes, ("frobenius2", "qlike"), ("Frobenius", "QLIKE")):
        for head in REPRESENTATION_HEADS:
            selected_ranks = ranks[ranks["head"] == head]
            axis.plot(
                selected_ranks["rank"],
                selected_ranks[f"rfd_reduction_percent_{metric}"],
                marker="o", color=head_colours[head], label=head.upper(),
            )
        axis.axhline(0.0, color="black", linewidth=0.8)
        axis.set(
            xlabel="retained rank", ylabel="RFD reduction versus parent (%)",
            title=title, xticks=sorted(ranks["rank"].unique()),
        )
        axis.grid(alpha=0.2)
        axis.legend(frameon=False)
    figure.suptitle("Does moving-centre preprocessing help prediction at the same rank?")
    figure.tight_layout()
    figure.savefig(output / "rank_forecast_curve.png", dpi=160)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(10, 4.2))
    for head in REPRESENTATION_HEADS:
        selected = raw[
            (raw["rank"] == 19) & (raw["head"] == head)
            & raw["method"].isin(REPRESENTATION_METHODS)
        ].copy()
        pivot = selected.pivot(
            index="target_hour", columns="method", values="frobenius2"
        ).sort_index()
        cumulative = (pivot["rfd_piecewise6"] - pivot["parent_rfm"]).cumsum()
        axis.plot(
            np.arange(len(cumulative)), cumulative,
            color=head_colours[head], label=head.upper(),
        )
    axis.axhline(0.0, color="black", linewidth=0.8)
    axis.set(xlabel="forecast hour", ylabel="cumulative RFD minus parent Frobenius loss", title="Where the rank-19 forecast difference accumulates")
    axis.grid(alpha=0.2)
    axis.legend(frameon=False)
    figure.tight_layout()
    figure.savefig(output / "cumulative_rank19_difference.png", dpi=160)
    plt.close(figure)


def analyze(output: Path, config: dict[str, Any], blocks: list[dict[str, int]], *, smoke: bool) -> dict[str, Any]:
    raw = pd.concat([
        pd.read_csv(_block_paths(output, block["block"])[0]) for block in blocks
    ], ignore_index=True)
    # Early augmented caches labelled every rank-19 score head as ``headline``.
    # Publication scope is narrower: only matched rank-19 VAR(1) is a headline.
    diagnostic_heads = raw["head"].isin(["har_ols", "vhar_ridge"])
    raw.loc[diagnostic_heads, "rank_role"] = "internal_diagnostic"
    rank_count = 1 + len(config["representation"]["sensitivity_ranks"])
    expected_methods = (
        len(BASELINE_METHODS)
        + len(REPRESENTATION_METHODS) * len(REPRESENTATION_HEADS) * rank_count
    )
    expected_hours = sum(block["target_stop"] - block["target_start"] for block in blocks)
    expected_rows = expected_methods * expected_hours
    if len(raw) != expected_rows:
        raise RuntimeError(f"HF-4 produced {len(raw)} rows; expected {expected_rows}")
    if raw.duplicated(["target_hour", "method", "head", "rank"]).any():
        raise RuntimeError("HF-4 produced duplicate forecast keys")
    required = ["frobenius2", "qlike", "bw2", "gmv_realized_variance", "forecast_minimum_eigenvalue"]
    if not np.isfinite(raw[required].to_numpy(dtype=float)).all():
        raise RuntimeError("HF-4 primary output contains NaN or Inf")
    if (raw["forecast_minimum_eigenvalue"] <= 0.0).any():
        raise RuntimeError("HF-4 produced a non-SPD forecast")
    summary = _summary(raw)
    ranks = _rank_comparison(summary)
    paired = _paired_rank19_inference(raw)
    head_paired = _paired_rank19_head_inference(raw)
    _atomic_csv(output / "hourly_losses.csv", raw)
    _atomic_csv(output / "performance.csv", summary)
    _atomic_csv(output / "rank_sensitivity.csv", ranks)
    _atomic_csv(output / "paired_rank19_inference.csv", paired)
    _atomic_csv(output / "paired_rank19_head_inference.csv", head_paired)
    _plots(output, raw, summary, ranks)

    headline = summary[summary["rank_role"].isin(["baseline", "headline"])]
    publication_headline = headline[headline["head"].isin(["native", "var1"])]
    vhar_promoted = bool((head_paired["ci95_upper"] < 0.0).all())
    best_f = publication_headline.sort_values("mean_frobenius2").iloc[0]
    best_q = publication_headline.sort_values("mean_qlike").iloc[0]
    rank19_var = ranks[(ranks["rank"] == 19) & (ranks["head"] == "var1")].iloc[0]
    rank19_har = ranks[(ranks["rank"] == 19) & (ranks["head"] == "har_ols")].iloc[0]
    rank19_vhar = ranks[(ranks["rank"] == 19) & (ranks["head"] == "vhar_ridge")].iloc[0]
    original_paired = paired[paired["head"] == "var1"]
    intervals = original_paired.set_index("metric")
    if (intervals["ci95_upper"] < 0.0).all():
        verdict = "RFD_RANK19_PRIMARY_PASS"
    elif (intervals["ci95_lower"] > 0.0).all():
        verdict = "PARENT_RANK19_PRIMARY_PASS"
    elif (
        (intervals["ci95_lower"] <= 0.0)
        & (intervals["ci95_upper"] >= 0.0)
    ).all():
        verdict = "RANK19_PRIMARY_TIE"
    else:
        verdict = "RANK19_MIXED_OR_UNRESOLVED"

    report = [
        "# APP-HF-4 — one-hour crypto covariance forecast", "",
        f"**Profile:** {'smoke; non-scientific' if smoke else 'recorded'}  ",
        f"**Original VAR rank-19 verdict:** `{verdict}`", "",
        "Every forecast is issued before its target is used. Representations refit every four weeks on the trailing 26 weeks; score-head coefficients then remain fixed inside the block while newly revealed scores update the one-step state. EWMA was selected on 2024 only. Rank-19 VAR(1) is the frozen Paper 1 RFD/RFM headline; ranks 1--18 are labelled sensitivities.", "",
        "Coordinatewise OLS HAR and ridge VHAR score heads were run later and are retained only as internal post-freeze diagnostics. They are excluded from Paper 1 tables, figures and claims. Log-SPD HAR remains an external classical baseline.", "",
        "| method | head | rank | role | Frobenius | QLIKE | BW | GMV realised variance |", "|---|---|---:|---|---:|---:|---:|---:|",
    ]
    for _, row in publication_headline.iterrows():
        report.append(
            f"| {row['method']} | {row['head']} | {int(row['rank'])} | {row['rank_role']} | "
            f"{row['mean_frobenius2']:.6g} | {row['mean_qlike']:.6g} | "
            f"{row['mean_bw2']:.6g} | {row['mean_gmv_realized_variance']:.6g} |"
        )
    report.extend([
        "", "Published rank-19 RFD reduction versus parent (positive means lower loss):", "",
        "| head | Frobenius | QLIKE | BW | GMV realised variance |",
        "|---|---:|---:|---:|---:|",
        f"| VAR(1) | {rank19_var['rfd_reduction_percent_frobenius2']:+.2f}% | {rank19_var['rfd_reduction_percent_qlike']:+.2f}% | {rank19_var['rfd_reduction_percent_bw2']:+.2f}% | {rank19_var['rfd_reduction_percent_gmv_realized_variance']:+.2f}% |", "",
        "Internal score-head diagnostic (not a Paper 1 result):", "",
        "| head | Frobenius | QLIKE | BW | GMV realised variance |",
        "|---|---:|---:|---:|---:|",
        f"| coordinate OLS HAR | {rank19_har['rfd_reduction_percent_frobenius2']:+.2f}% | {rank19_har['rfd_reduction_percent_qlike']:+.2f}% | {rank19_har['rfd_reduction_percent_bw2']:+.2f}% | {rank19_har['rfd_reduction_percent_gmv_realized_variance']:+.2f}% |",
        f"| ridge VHAR (sensitivity) | {rank19_vhar['rfd_reduction_percent_frobenius2']:+.2f}% | {rank19_vhar['rfd_reduction_percent_qlike']:+.2f}% | {rank19_vhar['rfd_reduction_percent_bw2']:+.2f}% | {rank19_vhar['rfd_reduction_percent_gmv_realized_variance']:+.2f}% |", "",
        "Paired rank-19 RFD-minus-parent differences use a Bartlett Newey--West 95% interval with at most 168 hourly lags:", "",
    ])
    for _, row in paired.iterrows():
        report.append(
            f"- {row['head']} / {row['metric']}: **{row['mean_difference_rfd_minus_parent']:+.6g}** "
            f"[{row['ci95_lower']:+.6g}, {row['ci95_upper']:+.6g}]"
        )
    report.extend([
        "", f"Ridge-VHAR promotion gate: **{'PASS' if vhar_promoted else 'NOT PROMOTED'}**.",
        "The gate requires the 95% upper bound for ridge-VHAR-minus-coordinate-HAR loss to be below zero for both primary losses and both representations.", "",
    ])
    for _, row in head_paired.iterrows():
        report.append(
            f"- {row['method']} / {row['metric']}: **{row['mean_difference_vhar_minus_har']:+.6g}** "
            f"[{row['ci95_lower']:+.6g}, {row['ci95_upper']:+.6g}]"
        )
    report.extend(["",
        f"Best rank-19/baseline Frobenius cell: **{best_f['method']} / {best_f['head']}**.  ",
        f"Best rank-19/baseline QLIKE cell: **{best_q['method']} / {best_q['head']}**.", "",
        "Projected scores remain observable coordinates, not structural latent amplitudes. The complete rank curve describes the discovered compression/forecast trade-off; a later confirmatory application can validate any selected operating rank.", "",
    ])
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")
    result = {
        "profile": "smoke" if smoke else "recorded",
        "verdict": verdict,
        "forecast_hours": int(expected_hours),
        "forecast_rows": int(len(raw)),
        "best_frobenius": f"{best_f['method']}:{best_f['head']}",
        "best_qlike": f"{best_q['method']}:{best_q['head']}",
        "rank19_rfd_reduction_percent_by_head": {
            head: {
                metric: float(
                    ranks[(ranks["rank"] == 19) & (ranks["head"] == head)].iloc[0][
                        f"rfd_reduction_percent_{metric}"
                    ]
                )
                for metric in (
                    "frobenius2", "qlike", "bw2", "gmv_realized_variance"
                )
            }
            for head in REPRESENTATION_HEADS
        },
        "rank19_paired_inference_by_head": paired.to_dict(orient="records"),
        "vhar_promoted": vhar_promoted,
        "rank19_vhar_minus_har_inference": head_paired.to_dict(orient="records"),
    }
    _atomic_json(output / "verdict.json", result)
    return result


def run(config: dict[str, Any], *, smoke: bool, force: bool) -> dict[str, Any]:
    panel = load_panel(config)
    development = panel["covariances"][panel["years"] == 2024]
    ewma_decay, ewma_table = tune_ewma(development, config)
    blocks = forecast_blocks(panel, config, smoke=smoke)
    output_key = "smoke_directory" if smoke else "directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    archived_original_blocks = _archive_recorded_original_blocks(output, blocks)
    if archived_original_blocks:
        print(
            f"[frozen original] archived {archived_original_blocks} pre-augmentation blocks",
            flush=True,
        )
    _atomic_csv(output / "ewma_tuning.csv", ewma_table)
    digest = experiment_digest(config, ewma_decay, smoke=smoke)
    design = build_design(config, panel, blocks, ewma_decay, smoke=smoke)
    design["digest"] = digest
    representation_digest = representation_cache_base_digest(config, smoke=smoke)
    design["representation_cache_digest"] = representation_digest
    design["frozen_original_blocks"] = int(sum(
        _frozen_original_path(output, block["block"]).is_file()
        for block in blocks
    ))
    design["augmentation_policy"] = (
        "reuse validated native-baseline and VAR rows; compute only missing HAR heads"
    )
    _atomic_json(output / "design.json", design)
    (output / "blocks").mkdir(parents=True, exist_ok=True)

    jobs = []
    for block in blocks:
        csv_path, meta_path = _block_paths(output, block["block"])
        block_digest = f"{digest}:{block['block']}"
        if force or not csv_path.is_file() or not _cache_matches(meta_path, block_digest):
            jobs.append((
                block["block"], block, config, ewma_decay, smoke,
                representation_digest,
            ))
    completed_at_start = len(blocks) - len(jobs)
    _atomic_json(output / "run_status.json", {
        "digest": digest,
        "state": "running" if jobs else "cached",
        "completed_blocks": completed_at_start,
        "total_blocks": len(blocks),
        "representation_heads": list(REPRESENTATION_HEADS),
    })
    if jobs:
        workers = min(int(config["runtime"]["workers"]), len(jobs))
        print(f"[forecast] running {len(jobs)} refit blocks with {workers} workers", flush=True)
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_block_worker, job): job[0] for job in jobs}
            for future in as_completed(futures):
                block_index = futures[future]
                frame = future.result()
                csv_path, meta_path = _block_paths(output, block_index)
                _atomic_csv(csv_path, frame)
                _atomic_json(meta_path, {"digest": f"{digest}:{block_index}", "rows": int(len(frame))})
                completed_at_start += 1
                _atomic_json(output / "run_status.json", {
                    "digest": digest,
                    "state": "running",
                    "completed_blocks": completed_at_start,
                    "total_blocks": len(blocks),
                    "last_completed_block": int(block_index),
                    "representation_heads": list(REPRESENTATION_HEADS),
                })
                print(f"[forecast] completed block {block_index + 1}/{len(blocks)}", flush=True)
    else:
        print("[forecast] all digest-matched refit blocks are cached", flush=True)
    result = analyze(output, config, blocks, smoke=smoke)
    _atomic_json(output / "run_status.json", {
        "digest": digest,
        "state": "complete",
        "completed_blocks": len(blocks),
        "total_blocks": len(blocks),
        "representation_heads": list(REPRESENTATION_HEADS),
    })
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    config = load_configuration(args.config)
    panel = load_panel(config)
    development = panel["covariances"][panel["years"] == 2024]
    decay, _ = tune_ewma(development, config)
    blocks = forecast_blocks(panel, config, smoke=args.smoke)
    design = build_design(config, panel, blocks, decay, smoke=args.smoke)
    print(json.dumps(design, indent=2), flush=True)
    if args.dry_run:
        print("APP-HF-4 dry run passed; all choices are frozen before scoring 2025.", flush=True)
        return
    result = run(config, smoke=args.smoke, force=args.force)
    print(json.dumps(result, indent=2), flush=True)
    output_key = "smoke_directory" if args.smoke else "directory"
    print(f"APP-HF-4 report: {ROOT / config['output'][output_key] / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
