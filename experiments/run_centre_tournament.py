"""Run the low-sample APP-FIN centre tournament from cached cross-fits."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
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

import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_appfin_identification import _atomic_json, _atomic_npz  # noqa: E402
from rfd.estimators.centre_low_n import (  # noqa: E402
    anchored_tangent_trend,
    graph_smoothed_polygon,
    piecewise_frechet_path,
    segmented_frechet_polygon,
)
from rfd.geometry import BW_GEOMETRY  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "centre_tournament_n240.yaml"


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    tournament = config["tournament"]
    n = int(config["experiment"]["expected_months"])
    block = int(tournament["holdout_block_months"])
    if n < 48 or block < 2 or n % block:
        raise ValueError("holdout blocks must divide the sample")
    lambdas = np.asarray(tournament["shrinkage_lambdas"], dtype=float)
    if (
        lambdas.ndim != 1 or lambdas.size < 3
        or lambdas[0] != 0.0 or lambdas[-1] != 1.0
        or np.any(np.diff(lambdas) <= 0.0)
    ):
        raise ValueError("shrinkage lambdas must increase from zero to one")
    strengths = np.asarray(tournament["graph_strengths"], dtype=float)
    if strengths.ndim != 1 or strengths.size == 0 or np.any(strengths <= 0.0):
        raise ValueError("graph strengths must be positive")
    segments = np.asarray(tournament["piecewise_segments"], dtype=int)
    if segments.ndim != 1 or segments.size == 0 or np.any(segments < 2):
        raise ValueError("piecewise segment counts must be at least two")
    if int(tournament["workers"]) not in range(1, 9):
        raise ValueError("workers must lie between one and eight")
    if not 0.0 < float(tournament["bw_step_margin"]) < 1.0:
        raise ValueError("BW step margin must lie between zero and one")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def experiment_digest(config: dict[str, Any]) -> str:
    source = ROOT / config["experiment"]["source_directory"]
    paths = [
        Path(config["config_path"]),
        ROOT / config["experiment"]["panel_path"],
        source / "design.json",
        source / "full_fit.npz",
        Path(__file__),
        ROOT / "py" / "rfd" / "estimators" / "centre_low_n.py",
    ]
    material = "\n".join(f"{path.resolve()}:{_sha256(path)}" for path in paths)
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _cache_matches(path: Path, digest: str) -> bool:
    if not path.is_file():
        return False
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("digest") == digest
    except (OSError, json.JSONDecodeError):
        return False


def _load_panel(config: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    path = ROOT / config["experiment"]["panel_path"]
    with np.load(path, allow_pickle=False) as source:
        panel = np.asarray(source["panel"], dtype=float)
        months = source["months"].astype(str)
    expected = config["experiment"]
    if panel.shape != (
        int(expected["expected_months"]),
        int(expected["expected_matrix_size"]),
        int(expected["expected_matrix_size"]),
    ):
        raise ValueError(f"unexpected APP-FIN panel shape: {panel.shape}")
    return panel, months


def build_design(config: dict[str, Any]) -> dict[str, Any]:
    experiment = config["experiment"]
    tournament = config["tournament"]
    n = int(experiment["expected_months"])
    block = int(tournament["holdout_block_months"])
    return {
        "experiment_id": experiment["id"],
        "sample_size": n,
        "matrix_size": int(experiment["expected_matrix_size"]),
        "holdout_block_months": block,
        "holdout_folds": n // block,
        "source_directory": str((ROOT / experiment["source_directory"]).resolve()),
        "families": {
            "global": "one BW centre",
            "positive_shrink": "positive local polygon geodesically shrunk to global",
            "tangent_trend": "one global-anchor tangent-linear trend",
            "graph_smooth": "positive neighbouring-vertex BW smoothing",
            "piecewise": "equal-duration positive BW segment centres",
            "segmented_polygon": "the same positive segment means joined by BW geodesics",
            "richardson_shrink": "Richardson/global sensitivity; full Richardson is a negative control",
        },
        "shrinkage_lambdas": [float(x) for x in tournament["shrinkage_lambdas"]],
        "graph_strengths": [float(x) for x in tournament["graph_strengths"]],
        "piecewise_segments": [int(x) for x in tournament["piecewise_segments"]],
        "selection": "alternating annual folds tune each family and evaluate on the opposite folds",
        "primary_loss": "squared Bures-Wasserstein distance",
    }


def _load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as source:
        return {name: source[name].copy() for name in source.files}


def _key(prefix: str, value: float | int) -> str:
    return f"{prefix}_{str(value).replace('.', 'p')}"


def _fold_worker(payload: tuple[Any, ...]) -> tuple[int, dict[str, np.ndarray], dict[str, Any]]:
    fold, panel, times, source_arrays, vertex_times, tournament = payload
    indices = source_arrays["indices"].astype(int)
    keep = np.ones(panel.shape[0], dtype=bool)
    keep[indices] = False
    training = panel[keep]
    training_times = times[keep]
    target_times = times[indices]
    global_centre = source_arrays["global_centre"]

    arrays: dict[str, np.ndarray] = {
        "indices": indices,
        "global_centre": global_centre,
        "positive_centres": source_arrays["positive_centres"],
        "richardson_centres": source_arrays["richardson_centres"],
    }
    diagnostics: dict[str, Any] = {}

    trend = anchored_tangent_trend(
        training,
        training_times,
        target_times,
        global_centre,
        BW_GEOMETRY,
        bw_step_margin=float(tournament["bw_step_margin"]),
    )
    arrays["tangent_trend"] = trend.points
    diagnostics["tangent_trend"] = trend.diagnostics

    for strength in tournament["graph_strengths"]:
        result = graph_smoothed_polygon(
            vertex_times,
            source_arrays["positive_vertices"],
            target_times,
            float(strength),
            BW_GEOMETRY,
            mean_tol=float(tournament["mean_tolerance"]),
            max_iter=int(tournament["mean_max_iterations"]),
            smoothing_iterations=int(tournament["graph_iterations"]),
            smoothing_tol=float(tournament["graph_tolerance"]),
        )
        name = _key("graph", float(strength))
        arrays[name] = result.points
        diagnostics[name] = result.diagnostics

    for segments in tournament["piecewise_segments"]:
        result = piecewise_frechet_path(
            training,
            training_times,
            target_times,
            int(segments),
            BW_GEOMETRY,
            mean_tol=float(tournament["mean_tolerance"]),
            max_iter=int(tournament["mean_max_iterations"]),
        )
        name = _key("piecewise", int(segments))
        arrays[name] = result.points
        diagnostics[name] = result.diagnostics
        polygon = segmented_frechet_polygon(
            training,
            training_times,
            target_times,
            int(segments),
            BW_GEOMETRY,
            mean_tol=float(tournament["mean_tolerance"]),
            max_iter=int(tournament["mean_max_iterations"]),
        )
        polygon_name = _key("segmented_polygon", int(segments))
        arrays[polygon_name] = polygon.points
        diagnostics[polygon_name] = polygon.diagnostics
    return int(fold), arrays, diagnostics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config = load_configuration(args.config)
    design = build_design(config)
    print(json.dumps(design, indent=2), flush=True)
    if args.dry_run:
        print("Centre tournament dry run passed; no candidates were fitted.", flush=True)
        return

    panel, _ = _load_panel(config)
    source = ROOT / config["experiment"]["source_directory"]
    if not (source / "full_fit.npz").is_file():
        raise FileNotFoundError("completed APP-FIN centre diagnostic is required")
    full = _load_npz(source / "full_fit.npz")
    vertex_times = full["vertex_times"]
    times = np.arange(1, panel.shape[0] + 1, dtype=float) / panel.shape[0]

    output_key = "smoke_directory" if args.smoke else "directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config) + (":smoke" if args.smoke else ":full")
    design["digest"] = digest
    _atomic_json(output / "design.json", design)

    folds = list(range(design["holdout_folds"]))
    if args.smoke:
        folds = folds[:2]
    jobs = []
    for fold in folds:
        source_path = source / "folds" / f"fold_{fold:02d}.npz"
        if not source_path.is_file():
            raise FileNotFoundError(f"missing upstream fold {fold}: {source_path}")
        fold_digest = f"{digest}:fold:{fold}"
        meta_path = output / f"fold_{fold:02d}.meta.json"
        if args.force or not _cache_matches(meta_path, fold_digest):
            jobs.append((
                fold,
                panel,
                times,
                _load_npz(source_path),
                vertex_times,
                config["tournament"],
            ))

    started = time.perf_counter()
    if jobs:
        workers = min(int(config["tournament"]["workers"]), len(jobs))
        print(f"[tournament] fitting {len(jobs)} folds with {workers} workers", flush=True)
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_fold_worker, job): job[0] for job in jobs}
            for completed, future in enumerate(as_completed(futures), start=1):
                fold, arrays, diagnostics = future.result()
                _atomic_npz(output / f"fold_{fold:02d}.npz", **arrays)
                _atomic_json(output / f"fold_{fold:02d}.meta.json", {
                    "digest": f"{digest}:fold:{fold}",
                    "completed": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                    "diagnostics": diagnostics,
                })
                print(f"[tournament] completed {completed}/{len(jobs)}; fold={fold}", flush=True)
    else:
        print("[tournament] all requested folds are cached", flush=True)

    from analyze_centre_tournament import analyze  # noqa: E402

    analyze(
        config,
        panel,
        output,
        fold_count=len(folds),
    )
    print(f"Completed in {time.perf_counter() - started:.1f}s", flush=True)
    print(f"Report: {(output / 'report.md').resolve()}", flush=True)


if __name__ == "__main__":
    main()
