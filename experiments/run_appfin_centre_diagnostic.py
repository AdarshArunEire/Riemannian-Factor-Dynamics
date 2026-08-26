"""Cross-fitted APP-FIN diagnostic for detectable BW centre motion.

The experiment separates four questions which a full RFD fit alone cannot:

* does a local centre beat one global centre out of block;
* does Richardson improve on the ordinary positive local mean;
* is partial global/local shrinkage preferable to either endpoint; and
* is observed local-centre motion larger than a constant-centre block null.

This is a descriptive interpolation diagnostic, not a causal forecast.  Every
held-out year is omitted before its centres and polygon are constructed.
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

import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_appfin_identification import (  # noqa: E402
    _atomic_json,
    _atomic_npz,
    effective_rfd_settings,
    load_panel,
)
from rfd.estimators.centre import (  # noqa: E402
    estimate_centre_path,
    fixed_overlap_weight,
    geodesic_blend,
    positive_local_frechet_mean,
)
from rfd.estimators.frame import (  # noqa: E402
    PolygonalFrame,
    evaluate_polygon,
    regular_polygon_grid,
)
from rfd.geometry import BW_GEOMETRY  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "appfin_centre_diagnostic.yaml"


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    rfd = config["rfd"]
    diagnostic = config["diagnostic"]
    n = int(experiment["expected_months"])
    block = int(diagnostic["holdout_block_months"])
    bootstrap_block = int(diagnostic["bootstrap_block_months"])
    if n < 48 or block < 2 or n % block:
        raise ValueError("holdout blocks must divide an APP-FIN sample of at least 48 months")
    if not 1 <= bootstrap_block <= n:
        raise ValueError("bootstrap block length must lie inside the sample")
    lambdas = np.asarray(diagnostic["shrinkage_lambdas"], dtype=float)
    if (
        lambdas.ndim != 1
        or lambdas.size < 3
        or not np.isfinite(lambdas).all()
        or np.any(np.diff(lambdas) <= 0.0)
        or lambdas[0] != 0.0
        or lambdas[-1] != 1.0
    ):
        raise ValueError("shrinkage lambdas must increase from exactly zero to one")
    if int(diagnostic["bootstrap_replicates"]) < 19:
        raise ValueError("at least 19 bootstrap replicates are required")
    if not 1 <= int(diagnostic["workers"]) <= 8:
        raise ValueError("workers must lie between one and eight")
    overlap = np.asarray(rfd["overlap_fractions"], dtype=float)
    if overlap.shape != (2,) or not 0.0 < overlap[0] < overlap[1] < 1.0:
        raise ValueError("overlap fractions must be increasing and interior")
    positive_controls = (
        "bandwidth_exponent", "bandwidth_constant", "production_multiplier_cap",
        "admissible_boundary_fraction", "polygon_rate_exponent",
        "polygon_cell_constant", "mean_tolerance", "mean_max_iterations",
    )
    if any(float(rfd[name]) <= 0.0 for name in positive_controls):
        raise ValueError("all RFD numerical controls must be positive")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def experiment_digest(config: dict[str, Any]) -> str:
    paths = [
        Path(config["config_path"]),
        ROOT / config["experiment"]["panel_path"],
        Path(__file__),
        ROOT / "py" / "rfd" / "estimators" / "centre.py",
        ROOT / "py" / "rfd" / "estimators" / "frame.py",
        ROOT / "py" / "rfd" / "spd" / "bw.py",
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


def _fit_controls(config: dict[str, Any], n: int) -> dict[str, Any]:
    settings = effective_rfd_settings(config, n)
    rfd = config["rfd"]
    return {
        "bandwidth": float(settings["bandwidth"]),
        "n_cells": int(settings["n_cells"]),
        "overlap_fractions": tuple(float(x) for x in rfd["overlap_fractions"]),
        "mean_tolerance": float(rfd["mean_tolerance"]),
        "mean_max_iterations": int(rfd["mean_max_iterations"]),
    }


def build_design(config: dict[str, Any], panel: dict[str, np.ndarray]) -> dict[str, Any]:
    n, m, _ = panel["panel"].shape
    block = int(config["diagnostic"]["holdout_block_months"])
    settings = effective_rfd_settings(config, n)
    return {
        "experiment_id": config["experiment"]["id"],
        "panel": str((ROOT / config["experiment"]["panel_path"]).resolve()),
        "months": [str(panel["months"][0]), str(panel["months"][-1])],
        "n_months": n,
        "matrix_size": m,
        "tangent_dimension": m * (m + 1) // 2,
        "holdout_block_months": block,
        "holdout_folds": n // block,
        "alternating_assignments": {
            "A": "even folds tune shrinkage; odd folds evaluate",
            "B": "odd folds tune shrinkage; even folds evaluate",
        },
        "methods": [
            "global BW centre", "positive local BW polygon",
            "three-scale Richardson polygon", "global/local geodesic shrinkage",
        ],
        "shrinkage_lambdas": [float(x) for x in config["diagnostic"]["shrinkage_lambdas"]],
        "constant_centre_null": {
            "block_months": int(config["diagnostic"]["bootstrap_block_months"]),
            "replicates": int(config["diagnostic"]["bootstrap_replicates"]),
            "statistic": "positive-local displacement energy from its fitted global centre",
        },
        "rfd": settings,
        "scope": "blocked descriptive interpolation; not forecasting or a structural centre/factor verdict",
    }


def _stage_diagnostics(centre: Any) -> dict[str, Any]:
    stages = []
    reasons: list[str] = []
    for estimate in centre.estimates:
        reasons.extend(estimate.fallback_reasons)
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is not None:
                stages.extend(one_sided.stages.stages)
    return {
        "fallback_count": int(centre.fallback_count),
        "fallback_reasons": reasons,
        "nonconverged_stage_count": int(sum(not stage.converged for stage in stages)),
        "support_count_min": int(min(stage.support_count for stage in stages)),
        "support_count_max": int(max(stage.support_count for stage in stages)),
        "effective_sample_size_min": float(min(stage.effective_sample_size for stage in stages)),
        "effective_sample_size_max": float(max(stage.effective_sample_size for stage in stages)),
        "stage_iterations_max": int(max(stage.n_iter for stage in stages)),
        "stage_residual_max": float(max(stage.residual for stage in stages)),
    }


def _broad_positive_vertices(centre: Any) -> np.ndarray:
    """Recover the broad positive stage path already computed by Richardson."""
    vertices = []
    for estimate in centre.estimates:
        forward = (
            None if estimate.forward is None else estimate.forward.stages.stages[0].point
        )
        backward = (
            None if estimate.backward is None else estimate.backward.stages.stages[0].point
        )
        if forward is None:
            point = backward
        elif backward is None:
            point = forward
        else:
            point = geodesic_blend(
                forward, backward, estimate.blend_weight, BW_GEOMETRY
            )
        vertices.append(np.asarray(point, dtype=float))
    return np.stack(vertices)


def _fit_centre_bundle(
    observations: np.ndarray,
    observation_times: np.ndarray,
    target_times: np.ndarray,
    vertex_times: np.ndarray,
    controls: dict[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    started = time.perf_counter()
    global_result = BW_GEOMETRY.barycentre(
        observations,
        tol=controls["mean_tolerance"],
        max_iter=controls["mean_max_iterations"],
    )
    if not global_result.converged:
        raise RuntimeError("cross-fitted global BW centre did not converge")
    centre = estimate_centre_path(
        observations=observations,
        time=observation_times,
        vertex_times=vertex_times,
        bandwidth=controls["bandwidth"],
        geometry=BW_GEOMETRY,
        overlap_fractions=controls["overlap_fractions"],
        mean_tol=controls["mean_tolerance"],
        max_iter=controls["mean_max_iterations"],
    )
    positive_vertices = _broad_positive_vertices(centre)
    positive_frame = PolygonalFrame(vertex_times, positive_vertices, BW_GEOMETRY)
    arrays = {
        "global_centre": np.asarray(global_result.X),
        "positive_vertices": positive_vertices,
        "richardson_vertices": centre.vertices,
        "positive_centres": evaluate_polygon(positive_frame, target_times).points,
        "richardson_centres": evaluate_polygon(centre.polygon, target_times).points,
    }
    diagnostics = _stage_diagnostics(centre)
    diagnostics.update({
        "global_iterations": int(global_result.n_iter),
        "global_residual": float(global_result.residual),
        "elapsed_seconds": float(time.perf_counter() - started),
    })
    return arrays, diagnostics


def _fold_worker(payload: tuple[Any, ...]) -> tuple[int, dict[str, np.ndarray], dict[str, Any]]:
    fold, observations, times, holdout, vertex_times, controls = payload
    keep = np.ones(observations.shape[0], dtype=bool)
    keep[holdout] = False
    arrays, diagnostics = _fit_centre_bundle(
        observations[keep], times[keep], times[holdout], vertex_times, controls
    )
    arrays["indices"] = holdout
    return int(fold), arrays, diagnostics


def _fit_positive_path(
    observations: np.ndarray,
    times: np.ndarray,
    vertex_times: np.ndarray,
    controls: dict[str, Any],
) -> tuple[PolygonalFrame, dict[str, Any]]:
    start = float(vertex_times[0])
    stop = float(vertex_times[-1])
    span = stop - start
    left = start + controls["overlap_fractions"][0] * span
    right = start + controls["overlap_fractions"][1] * span
    vertices = []
    stages = []
    for target in vertex_times:
        forward = backward = None
        if target < right:
            forward = positive_local_frechet_mean(
                observations, times, float(target), controls["bandwidth"],
                "forward", BW_GEOMETRY,
                mean_tol=controls["mean_tolerance"],
                max_iter=controls["mean_max_iterations"],
            )
            stages.append(forward)
        if target > left:
            backward = positive_local_frechet_mean(
                observations, times, float(target), controls["bandwidth"],
                "backward", BW_GEOMETRY,
                mean_tol=controls["mean_tolerance"],
                max_iter=controls["mean_max_iterations"],
            )
            stages.append(backward)
        if forward is None:
            point = backward.point
        elif backward is None:
            point = forward.point
        else:
            point = geodesic_blend(
                forward.point,
                backward.point,
                fixed_overlap_weight(float(target), left=left, right=right),
                BW_GEOMETRY,
            )
        vertices.append(point)
    if any(not stage.converged for stage in stages):
        raise RuntimeError("positive-local null-bootstrap mean did not converge")
    return PolygonalFrame(vertex_times, np.stack(vertices), BW_GEOMETRY), {
        "support_count_min": int(min(stage.support_count for stage in stages)),
        "effective_sample_size_min": float(min(stage.effective_sample_size for stage in stages)),
        "stage_iterations_max": int(max(stage.n_iter for stage in stages)),
        "stage_residual_max": float(max(stage.residual for stage in stages)),
    }


def _circular_block_indices(rng: np.random.Generator, n: int, block: int) -> np.ndarray:
    count = math.ceil(n / block)
    starts = rng.integers(0, n, size=count)
    indices = np.concatenate(
        [(start + np.arange(block, dtype=int)) % n for start in starts]
    )
    return indices[:n]


def _bootstrap_worker(payload: tuple[Any, ...]) -> tuple[int, dict[str, Any]]:
    replicate, residuals, reference, times, vertex_times, controls, block, seed = payload
    started = time.perf_counter()
    rng = np.random.default_rng(int(seed) + int(replicate))
    indices = _circular_block_indices(rng, residuals.shape[0], int(block))
    observations = BW_GEOMETRY.exp(reference, residuals[indices])
    global_result = BW_GEOMETRY.barycentre(
        observations,
        tol=controls["mean_tolerance"],
        max_iter=controls["mean_max_iterations"],
    )
    if not global_result.converged:
        raise RuntimeError("constant-centre bootstrap global mean did not converge")
    frame, diagnostics = _fit_positive_path(
        observations, times, vertex_times, controls
    )
    local = evaluate_polygon(frame, times).points
    global_centres = np.broadcast_to(global_result.X, local.shape)
    movement = float(np.mean(BW_GEOMETRY.dist2(global_centres, local)))
    residual = float(np.mean(BW_GEOMETRY.dist2(local, observations)))
    return int(replicate), {
        "movement_energy": movement,
        "residual_energy": residual,
        "movement_to_residual": movement / residual if residual > 0.0 else float("inf"),
        "global_iterations": int(global_result.n_iter),
        "global_residual": float(global_result.residual),
        "elapsed_seconds": float(time.perf_counter() - started),
        **diagnostics,
    }


def _run_jobs(
    jobs: list[tuple[Any, ...]],
    worker: Any,
    workers: int,
) -> list[Any]:
    if workers == 1:
        return [worker(job) for job in jobs]
    results = []
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, job): job[0] for job in jobs}
        for completed, future in enumerate(as_completed(futures), start=1):
            result = future.result()
            results.append(result)
            print(
                f"[parallel] completed {completed}/{len(futures)}; item={futures[future]}",
                flush=True,
            )
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--skip-bootstrap", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config = load_configuration(args.config)
    panel = load_panel(config)
    design = build_design(config, panel)
    if args.smoke:
        design["smoke"] = True
        design["holdout_folds_executed"] = 2
        design["bootstrap_replicates_executed"] = 7
    print(json.dumps(design, indent=2), flush=True)
    if args.dry_run:
        print("APP-FIN centre diagnostic dry run passed; no centres were fitted.", flush=True)
        return

    output_key = "smoke_directory" if args.smoke else "directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config) + (":smoke" if args.smoke else ":full")
    design["digest"] = digest
    _atomic_json(output / "design.json", design)

    observations = np.asarray(panel["panel"], dtype=float)
    n = observations.shape[0]
    times = np.arange(1, n + 1, dtype=float) / n
    controls = _fit_controls(config, n)
    vertex_times = regular_polygon_grid(
        controls["n_cells"], start=float(times[0]), stop=float(times[-1])
    )

    full_path = output / "full_fit.npz"
    full_meta = output / "full_fit.meta.json"
    if args.force or not full_path.is_file() or not _cache_matches(full_meta, digest):
        print("[full] fitting global, positive-local, and Richardson paths", flush=True)
        arrays, diagnostics = _fit_centre_bundle(
            observations, times, times, vertex_times, controls
        )
        arrays.update({"time": times, "vertex_times": vertex_times})
        _atomic_npz(full_path, **arrays)
        _atomic_json(full_meta, {
            "digest": digest,
            "completed": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "diagnostics": diagnostics,
        })
    else:
        print("[full] reusing digest-matched fit", flush=True)

    block = int(config["diagnostic"]["holdout_block_months"])
    all_folds = list(range(n // block))
    selected_folds = all_folds[:2] if args.smoke else all_folds
    fold_directory = output / "folds"
    fold_directory.mkdir(parents=True, exist_ok=True)
    fold_jobs = []
    for fold in selected_folds:
        path = fold_directory / f"fold_{fold:02d}.npz"
        meta = fold_directory / f"fold_{fold:02d}.meta.json"
        fold_digest = f"{digest}:fold:{fold}"
        if args.force or not path.is_file() or not _cache_matches(meta, fold_digest):
            holdout = np.arange(fold * block, (fold + 1) * block, dtype=int)
            fold_jobs.append((fold, observations, times, holdout, vertex_times, controls))
    if fold_jobs:
        print(f"[cross-fit] fitting {len(fold_jobs)} missing annual folds", flush=True)
        results = _run_jobs(
            fold_jobs,
            _fold_worker,
            min(int(config["diagnostic"]["workers"]), len(fold_jobs)),
        )
        for fold, arrays, diagnostics in results:
            _atomic_npz(fold_directory / f"fold_{fold:02d}.npz", **arrays)
            _atomic_json(fold_directory / f"fold_{fold:02d}.meta.json", {
                "digest": f"{digest}:fold:{fold}",
                "completed": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "diagnostics": diagnostics,
            })
    else:
        print("[cross-fit] all requested annual folds are cached", flush=True)

    bootstrap_replicates = 7 if args.smoke else int(config["diagnostic"]["bootstrap_replicates"])
    if not args.skip_bootstrap:
        with np.load(full_path, allow_pickle=False) as full:
            reference = full["global_centre"].copy()
        residuals = BW_GEOMETRY.log(reference, observations)
        bootstrap_directory = output / "constant_centre_bootstrap"
        bootstrap_directory.mkdir(parents=True, exist_ok=True)
        bootstrap_jobs = []
        for replicate in range(bootstrap_replicates):
            path = bootstrap_directory / f"replicate_{replicate:03d}.json"
            replicate_digest = f"{digest}:null:{replicate}"
            if args.force or not _cache_matches(path, replicate_digest):
                bootstrap_jobs.append((
                    replicate, residuals, reference, times, vertex_times, controls,
                    int(config["diagnostic"]["bootstrap_block_months"]),
                    int(config["diagnostic"]["bootstrap_seed"]),
                ))
        if bootstrap_jobs:
            print(
                f"[constant-centre null] fitting {len(bootstrap_jobs)} missing replicates",
                flush=True,
            )
            results = _run_jobs(
                bootstrap_jobs,
                _bootstrap_worker,
                min(int(config["diagnostic"]["workers"]), len(bootstrap_jobs)),
            )
            for replicate, values in results:
                _atomic_json(
                    bootstrap_directory / f"replicate_{replicate:03d}.json",
                    {
                        "digest": f"{digest}:null:{replicate}",
                        "replicate": replicate,
                        **values,
                    },
                )
        else:
            print("[constant-centre null] all requested replicates are cached", flush=True)

    from analyze_appfin_centre_diagnostic import analyze

    analyze(
        ROOT,
        config,
        panel,
        output,
        require_bootstrap=not args.skip_bootstrap,
        fold_count=2 if args.smoke else None,
        bootstrap_replicates=7 if args.smoke else None,
    )
    if args.smoke:
        print(f"Centre diagnostic smoke completed: {output}", flush=True)
        return
    print(f"Centre diagnostic report: {output / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
