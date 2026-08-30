"""Known-centre BW tournament with APP-FIN-like covariance proxies."""

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
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from analyze_appfin_centre_diagnostic import _geodesic_shrink  # noqa: E402
from run_appfin_centre_diagnostic import (  # noqa: E402
    _broad_positive_vertices,
    _stage_diagnostics,
)
from run_appfin_identification import effective_rfd_settings  # noqa: E402
from rfd.dgp.covariance_proxy import sample_covariance_proxies  # noqa: E402
from rfd.estimators.centre import estimate_centre_path  # noqa: E402
from rfd.estimators.centre_low_n import (  # noqa: E402
    anchored_tangent_trend,
    graph_smoothed_polygon,
    piecewise_frechet_path,
    segmented_frechet_polygon,
)
from rfd.estimators.frame import (  # noqa: E402
    PolygonalFrame,
    evaluate_polygon,
    regular_polygon_grid,
)
from rfd.eval.losses import bw_loss, frobenius_loss, qlike_loss  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "matched_centre_tournament.yaml"


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    if int(experiment["matrix_size"]) < 2:
        raise ValueError("matrix size must be at least two")
    retention = float(experiment["latent_global_retention"])
    if not 0.0 <= retention <= 1.0:
        raise ValueError("latent global retention must lie in [0, 1]")
    if float(experiment["student_degrees_of_freedom"]) <= 4.0:
        raise ValueError("Student degrees of freedom must exceed four")
    for name, profile in config["profiles"].items():
        if not profile["n_values"] or min(map(int, profile["n_values"])) < 48:
            raise ValueError(f"profile {name} has an invalid n value")
        if int(profile["replicates"]) < 1:
            raise ValueError(f"profile {name} needs a replicate")
        if set(profile["distributions"]) - {"gaussian", "student_t"}:
            raise ValueError(f"profile {name} has an unsupported distribution")
    if not 1 <= int(config["runtime"]["workers"]) <= 8:
        raise ValueError("workers must lie between one and eight")


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
        ROOT / config["experiment"]["centre_source"],
        Path(__file__),
        ROOT / "py" / "rfd" / "dgp" / "covariance_proxy.py",
        ROOT / "py" / "rfd" / "estimators" / "centre.py",
        ROOT / "py" / "rfd" / "estimators" / "centre_low_n.py",
    ]
    material = "\n".join(f"{p.resolve()}:{_sha256(p)}" for p in paths)
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    os.replace(temporary, path)


def _source_arrays(config: dict[str, Any]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    source_path = ROOT / config["experiment"]["centre_source"]
    with np.load(source_path, allow_pickle=False) as source:
        global_centre = source["global_centre"].copy()
        positive_vertices = source["positive_vertices"].copy()
        vertex_times = source["vertex_times"].copy()
    graph = graph_smoothed_polygon(
        vertex_times,
        positive_vertices,
        vertex_times,
        float(config["experiment"]["latent_graph_strength"]),
        BW_GEOMETRY,
    )
    local_weight = 1.0 - float(config["experiment"]["latent_global_retention"])
    latent_vertices = _geodesic_shrink(global_centre, graph.points, local_weight)
    return global_centre, vertex_times, latent_vertices


def _window_cycle(config: dict[str, Any]) -> np.ndarray:
    with np.load(ROOT / config["experiment"]["panel_path"], allow_pickle=False) as panel:
        return np.asarray(panel["ndays"], dtype=int).copy()


def build_design(config: dict[str, Any], profile: str, *, smoke: bool) -> dict[str, Any]:
    source = config["profiles"][profile]
    n_values = [min(96, int(source["n_values"][0]))] if smoke else list(map(int, source["n_values"]))
    replicates = 1 if smoke else int(source["replicates"])
    distributions = [source["distributions"][0]] if smoke else list(source["distributions"])
    settings = {str(n): effective_rfd_settings(config, n) for n in n_values}
    return {
        "experiment_id": config["experiment"]["id"],
        "profile": profile,
        "smoke": smoke,
        "n_values": n_values,
        "replicates": replicates,
        "distributions": distributions,
        "tasks": len(n_values) * replicates * len(distributions),
        "matrix_size": int(config["experiment"]["matrix_size"]),
        "covariance_window_counts": "the observed APP-FIN 15--23 day sequence, tiled",
        "latent_path": "smoothed APP-FIN positive path, shrunk 40% toward its global centre",
        "truth": "known conditional covariance at every time",
        "settings": settings,
        "scope": "matched centre identification only; no factors or forecasting",
    }


def _fit_methods(
    observations: np.ndarray,
    truth: np.ndarray,
    times: np.ndarray,
    config: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rfd = config["rfd"]
    candidates = config["candidates"]
    settings = effective_rfd_settings(config, observations.shape[0])
    vertex_times = regular_polygon_grid(int(settings["n_cells"]))
    global_result = BW_GEOMETRY.barycentre(
        observations,
        tol=float(rfd["mean_tolerance"]),
        max_iter=int(rfd["mean_max_iterations"]),
    )
    if not global_result.converged:
        raise RuntimeError("global BW mean did not converge")
    centre = estimate_centre_path(
        observations=observations,
        time=times,
        vertex_times=vertex_times,
        bandwidth=float(settings["bandwidth"]),
        geometry=BW_GEOMETRY,
        overlap_fractions=tuple(map(float, rfd["overlap_fractions"])),
        mean_tol=float(rfd["mean_tolerance"]),
        max_iter=int(rfd["mean_max_iterations"]),
    )
    positive_vertices = _broad_positive_vertices(centre)
    positive = evaluate_polygon(
        PolygonalFrame(vertex_times, positive_vertices, BW_GEOMETRY), times
    ).points
    richardson = evaluate_polygon(centre.polygon, times).points
    global_points = np.broadcast_to(global_result.X, truth.shape)
    trend = anchored_tangent_trend(
        observations, times, times, global_result.X, BW_GEOMETRY,
        bw_step_margin=float(candidates["bw_step_margin"]),
    )
    graph = graph_smoothed_polygon(
        vertex_times, positive_vertices, times,
        float(candidates["graph_strength"]), BW_GEOMETRY,
        mean_tol=float(rfd["mean_tolerance"]),
        max_iter=int(rfd["mean_max_iterations"]),
    )
    piecewise = piecewise_frechet_path(
        observations, times, times, int(candidates["piecewise_segments"]),
        BW_GEOMETRY, mean_tol=float(rfd["mean_tolerance"]),
        max_iter=int(rfd["mean_max_iterations"]),
    )
    segmented = segmented_frechet_polygon(
        observations, times, times, int(candidates["piecewise_segments"]),
        BW_GEOMETRY, mean_tol=float(rfd["mean_tolerance"]),
        max_iter=int(rfd["mean_max_iterations"]),
    )
    methods = {
        "global": global_points,
        "positive_local": positive,
        "positive_shrink_0.6": _geodesic_shrink(
            global_result.X, positive, float(candidates["positive_shrinkage"])
        ),
        "richardson": richardson,
        "richardson_shrink_0.2": _geodesic_shrink(
            global_result.X, richardson, float(candidates["richardson_shrinkage"])
        ),
        "tangent_trend": trend.points,
        "graph_smooth_1": graph.points,
        "piecewise_6": piecewise.points,
        "segmented_polygon_6": segmented.points,
    }
    truth_scale = np.maximum(frobenius_loss(np.zeros_like(truth), truth), 1e-300)
    rows = []
    for name, points in methods.items():
        eigenvalues = np.linalg.eigvalsh(points)
        rows.append({
            "method": name,
            "centre_bw_rms": float(np.sqrt(np.mean(bw_loss(points, truth)))),
            "proxy_bw_rms": float(np.sqrt(np.mean(bw_loss(points, observations)))),
            "mean_qlike_to_truth": float(np.mean(qlike_loss(points, truth))),
            "relative_frobenius_rms": float(np.sqrt(np.mean(frobenius_loss(points, truth) / truth_scale))),
            "minimum_eigenvalue": float(eigenvalues[:, 0].min()),
            "maximum_condition_number": float(np.max(eigenvalues[:, -1] / eigenvalues[:, 0])),
        })
    diagnostics = _stage_diagnostics(centre)
    diagnostics.update({
        "global_iterations": int(global_result.n_iter),
        "global_residual": float(global_result.residual),
        "trend": trend.diagnostics,
        "graph": graph.diagnostics,
        "piecewise": piecewise.diagnostics,
        "segmented_polygon": segmented.diagnostics,
    })
    return rows, diagnostics


def _worker(payload: tuple[Any, ...]) -> dict[str, Any]:
    n, distribution, replicate, config, digest, output = payload
    output = Path(output)
    task_path = output / "tasks" / f"n{n}_{distribution}_rep{replicate:03d}.json"
    if task_path.is_file():
        try:
            cached = json.loads(task_path.read_text(encoding="utf-8"))
            if cached.get("digest") == digest:
                return cached
        except (OSError, json.JSONDecodeError):
            pass
    started = time.perf_counter()
    global_centre, source_times, source_vertices = _source_arrays(config)
    times = np.arange(1, n + 1, dtype=float) / n
    latent_times = np.linspace(float(source_times[0]), float(source_times[-1]), n)
    truth = evaluate_polygon(
        PolygonalFrame(source_times, source_vertices, BW_GEOMETRY), latent_times
    ).points
    counts = np.resize(_window_cycle(config), n)
    seed = int(config["experiment"]["base_seed"]) + 100000 * int(replicate) + (distribution == "student_t") * 10000 + n
    rng = np.random.default_rng(seed)
    observations = sample_covariance_proxies(
        rng, truth, counts, distribution=distribution,
        student_degrees_of_freedom=float(config["experiment"]["student_degrees_of_freedom"]),
    )
    rows, diagnostics = _fit_methods(observations, truth, times, config)
    proxy_eigenvalues = np.linalg.eigvalsh(observations)
    truth_eigenvalues = np.linalg.eigvalsh(truth)
    for row in rows:
        row.update({"n": n, "distribution": distribution, "replicate": replicate})
    result = {
        "digest": digest,
        "n": n,
        "distribution": distribution,
        "replicate": replicate,
        "rows": rows,
        "diagnostics": diagnostics,
        "data_health": {
            "window_count_min": int(counts.min()),
            "window_count_median": float(np.median(counts)),
            "window_count_max": int(counts.max()),
            "truth_minimum_eigenvalue": float(truth_eigenvalues[:, 0].min()),
            "truth_maximum_condition_number": float(np.max(truth_eigenvalues[:, -1] / truth_eigenvalues[:, 0])),
            "proxy_minimum_eigenvalue": float(proxy_eigenvalues[:, 0].min()),
            "proxy_maximum_condition_number": float(np.max(proxy_eigenvalues[:, -1] / proxy_eigenvalues[:, 0])),
        },
        "elapsed_seconds": float(time.perf_counter() - started),
    }
    _atomic_json(task_path, result)
    return result


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--profile", choices=("n240", "n8192"), required=True)
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    config = load_configuration(args.config.resolve())
    design = build_design(config, args.profile, smoke=args.smoke)
    output = ROOT / config["output"]["root"] / (args.profile + ("_smoke" if args.smoke else ""))
    output.mkdir(parents=True, exist_ok=True)
    print(json.dumps(design, indent=2))
    if args.dry_run:
        return
    digest = experiment_digest(config)
    _atomic_json(output / "design.json", {**design, "digest": digest})
    if args.force:
        for path in (output / "tasks").glob("*.json") if (output / "tasks").is_dir() else []:
            path.unlink()
    jobs = [
        (n, distribution, replicate, config, digest, str(output))
        for n in design["n_values"]
        for distribution in design["distributions"]
        for replicate in range(design["replicates"])
    ]
    workers = min(int(config["runtime"]["workers"]), len(jobs))
    results = []
    started = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(_worker, job): job[:3] for job in jobs}
        for done, future in enumerate(as_completed(futures), start=1):
            result = future.result()
            results.append(result)
            print(
                f"[{done}/{len(jobs)}] n={result['n']}, {result['distribution']}, "
                f"rep={result['replicate']} ({result['elapsed_seconds']:.1f}s)",
                flush=True,
            )
    rows = [row for result in results for row in result["rows"]]
    frame = pd.DataFrame(rows).sort_values(["n", "distribution", "replicate", "method"])
    frame.to_csv(output / "scores.csv", index=False)
    _atomic_json(output / "diagnostics.json", [
        {key: value for key, value in result.items() if key != "rows"}
        for result in results
    ])
    print(f"Completed {len(jobs)} tasks in {time.perf_counter() - started:.1f}s")
    from analyze_matched_centre_tournament import analyze
    analyze(output)


if __name__ == "__main__":
    main()
