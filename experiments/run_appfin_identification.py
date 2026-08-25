"""Run the final Paper 1 APP-FIN identification illustration.

The same rebuilt 240-month, 12-stock BW covariance panel is fitted by:

* the cloned parent's fixed-global-centre RFM implementation; and
* RFD's three-scale moving centre, polygon frame, and lag factor model.

Rank two is supplied to both for the headline comparison.  A single rank-15
decomposition also supplies a rank-sensitivity curve without selecting rank
from the evaluation data.  There is no forecasting and no latent-score truth.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
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

from run_end_to_end import production_multiplier  # noqa: E402
from rfd.estimators.frame import polygon_cell_count  # noqa: E402
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.model import RFDConfig, fit_rfd  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "appfin_identification.yaml"
R_WORKER = ROOT / "experiments" / "parent_rfm_bw_worker.R"
PARENT_SOURCE = ROOT / "reference" / "Riemannian_factor_model-main" / "BWS_util.R"


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    rfd = config["rfd"]
    parent = config["parent"]
    if int(experiment["expected_months"]) < 24:
        raise ValueError("APP-FIN requires at least 24 monthly matrices")
    if len(experiment["expected_tickers"]) != 12:
        raise ValueError("APP-FIN contract requires the twelve declared stocks")
    primary = int(experiment["primary_rank"])
    maximum = int(experiment["sensitivity_max_rank"])
    if not 1 <= primary <= maximum < 78:
        raise ValueError("rank contract must satisfy 1 <= primary <= max < 78")
    if not 1 <= int(experiment["max_lag"]) < int(experiment["expected_months"]):
        raise ValueError("max_lag must lie inside the monthly sample")
    overlap = tuple(float(value) for value in rfd["overlap_fractions"])
    if len(overlap) != 2 or not 0 < overlap[0] < overlap[1] < 1:
        raise ValueError("overlap fractions must be increasing and interior")
    if not 0 < float(rfd["admissible_boundary_fraction"]) < 1:
        raise ValueError("admissible boundary fraction must lie in (0, 1)")
    if min(
        float(rfd["bandwidth_constant"]),
        float(rfd["production_multiplier_cap"]),
        float(rfd["mean_tolerance"]),
        int(rfd["mean_max_iterations"]),
        int(parent["batch_size"]),
        int(parent["budget_iterations"]),
        float(parent["verified_mean_tolerance"]),
        int(parent["verified_mean_max_iterations"]),
    ) <= 0:
        raise ValueError("all numerical controls must be positive")


def load_panel(config: dict[str, Any]) -> dict[str, np.ndarray]:
    experiment = config["experiment"]
    path = ROOT / experiment["panel_path"]
    if not path.is_file():
        raise FileNotFoundError(f"rebuilt APP-FIN panel is missing: {path}")
    with np.load(path, allow_pickle=False) as source:
        required = {"panel", "months", "ndays", "tickers", "rets", "ret_month"}
        if not required.issubset(source.files):
            raise ValueError(f"panel archive is missing {sorted(required - set(source.files))}")
        data = {name: source[name].copy() for name in required}

    panel = np.asarray(data["panel"], dtype=float)
    months = data["months"].astype(str)
    tickers = data["tickers"].astype(str)
    expected_n = int(experiment["expected_months"])
    if panel.shape != (expected_n, 12, 12):
        raise ValueError(f"panel shape is {panel.shape}; expected {(expected_n, 12, 12)}")
    if months.shape != (expected_n,) or months[0] != experiment["expected_first_month"] or months[-1] != experiment["expected_last_month"]:
        raise ValueError("panel month range does not match the frozen APP-FIN contract")
    if tickers.tolist() != list(experiment["expected_tickers"]):
        raise ValueError("panel ticker order does not match the frozen contract")
    if not np.isfinite(panel).all():
        raise ValueError("panel contains NaN or Inf")
    if not np.allclose(panel, panel.swapaxes(-1, -2), rtol=0.0, atol=1e-10):
        raise ValueError("panel contains a nonsymmetric covariance matrix")
    eigenvalues = np.linalg.eigvalsh(panel)
    if np.any(eigenvalues <= 0.0):
        raise ValueError("APP-FIN BW experiment requires strictly positive matrices")
    if np.any((data["ndays"] < 2) | ~np.isfinite(data["ndays"])):
        raise ValueError("monthly daily-return counts are invalid")
    return data


def effective_rfd_settings(config: dict[str, Any], n: int) -> dict[str, Any]:
    source = config["rfd"]
    estimator = {
        "bandwidth_constant": float(source["bandwidth_constant"]),
        "bandwidth_exponent": float(source["bandwidth_exponent"]),
        "production_multiplier_cap": float(source["production_multiplier_cap"]),
        "admissible_boundary_fraction": float(source["admissible_boundary_fraction"]),
        "overlap_fractions": tuple(source["overlap_fractions"]),
    }
    multiplier = production_multiplier(n, estimator)
    bandwidth = (
        estimator["bandwidth_constant"]
        * n ** (-estimator["bandwidth_exponent"])
        * multiplier
    )
    centre_rate = n ** (-float(source["polygon_rate_exponent"]))
    n_cells = polygon_cell_count(
        centre_rate, constant=float(source["polygon_cell_constant"])
    )
    return {
        "bandwidth_multiplier": float(multiplier),
        "bandwidth": float(bandwidth),
        "n_cells": int(n_cells),
        "vertex_count": int(n_cells + 1),
        "broad_window_months": float(n * bandwidth),
        "half_window_months": float(n * bandwidth / 2.0),
        "quarter_window_months": float(n * bandwidth / 4.0),
    }


def build_design(config: dict[str, Any], panel: dict[str, np.ndarray]) -> dict[str, Any]:
    observations = panel["panel"]
    eigenvalues = np.linalg.eigvalsh(observations)
    settings = effective_rfd_settings(config, observations.shape[0])
    return {
        "experiment_id": config["experiment"]["id"],
        "panel": str((ROOT / config["experiment"]["panel_path"]).resolve()),
        "months": [str(panel["months"][0]), str(panel["months"][-1])],
        "n_months": int(observations.shape[0]),
        "matrix_size": int(observations.shape[1]),
        "tangent_dimension": int(observations.shape[1] * (observations.shape[1] + 1) // 2),
        "tickers": panel["tickers"].astype(str).tolist(),
        "daily_returns_per_month": {
            "minimum": int(np.min(panel["ndays"])),
            "median": float(np.median(panel["ndays"])),
            "maximum": int(np.max(panel["ndays"])),
        },
        "primary_rank": int(config["experiment"]["primary_rank"]),
        "sensitivity_ranks": [1, int(config["experiment"]["sensitivity_max_rank"])],
        "lags_months": [1, int(config["experiment"]["max_lag"])],
        "minimum_matrix_eigenvalue": float(eigenvalues.min()),
        "maximum_matrix_eigenvalue": float(eigenvalues.max()),
        "maximum_condition_number": float(np.max(eigenvalues[:, -1] / eigenvalues[:, 0])),
        "rfd": settings,
        "scope": "descriptive identification and reconstruction; no forecasting or rank selection",
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def experiment_digest(config: dict[str, Any]) -> str:
    paths = [
        Path(config["config_path"]), ROOT / config["experiment"]["panel_path"],
        R_WORKER, PARENT_SOURCE, ROOT / "py" / "rfd" / "model.py",
    ]
    joined = "\n".join(f"{path.resolve()}:{_sha256(path)}" for path in paths)
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()


def _atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def _atomic_npz(path: Path, **arrays: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("wb") as handle:
        np.savez_compressed(handle, **arrays)
    os.replace(temporary, path)


def _resolve_project_r_library() -> Path | None:
    declared = os.environ.get("R_LIBS_USER")
    if declared and Path(declared).is_dir():
        return Path(declared)
    root = ROOT / "renv" / "library" / "windows"
    candidates = [path.parents[1] for path in root.glob("*/*/renv/DESCRIPTION")] if root.is_dir() else []
    return candidates[0] if len(candidates) == 1 else None


def check_r_environment(rscript: Path) -> None:
    if not rscript.is_file() or not R_WORKER.is_file() or not PARENT_SOURCE.is_file():
        raise FileNotFoundError("Rscript, parent worker, or cloned BWS_util.R is missing")
    env = os.environ.copy()
    library = _resolve_project_r_library()
    if library is not None:
        env["R_LIBS_USER"] = str(library)
    env["RENV_CONFIG_AUTOLOADER_ENABLED"] = "FALSE"
    completed = subprocess.run(
        [str(rscript), "--vanilla", "-e",
         "stopifnot(requireNamespace('maotai',quietly=TRUE),requireNamespace('expm',quietly=TRUE),requireNamespace('deSolve',quietly=TRUE));cat('APP-FIN parent R ready\\n')"],
        cwd=ROOT, env=env, capture_output=True, text=True, timeout=90, check=False,
    )
    if completed.returncode:
        raise RuntimeError((completed.stderr or completed.stdout).strip())


def _read_matrix(path: Path, shape: tuple[int, ...]) -> np.ndarray:
    value = np.loadtxt(path, delimiter=",", ndmin=2)
    if value.size != int(np.prod(shape)):
        raise ValueError(f"{path.name} has {value.size} values; expected {np.prod(shape)}")
    value = value.reshape(shape)
    if not np.isfinite(value).all():
        raise FloatingPointError(f"{path.name} contains NaN or Inf")
    return value


def run_parent_stage(
    observations: np.ndarray,
    config: dict[str, Any],
    rscript: Path,
) -> dict[str, np.ndarray]:
    n, m, _ = observations.shape
    rank = int(config["experiment"]["sensitivity_max_rank"])
    parent = config["parent"]
    print("[parent] computing a verified full-data BW mean", flush=True)
    mean_started = time.perf_counter()
    mean_result = BW_GEOMETRY.barycentre(
        observations,
        tol=float(parent["verified_mean_tolerance"]),
        max_iter=int(parent["verified_mean_max_iterations"]),
    )
    if not mean_result.converged:
        raise RuntimeError("verified parent BW mean did not converge")
    print(f"[parent] verified mean complete in {time.perf_counter()-mean_started:.1f}s", flush=True)

    env = os.environ.copy()
    library = _resolve_project_r_library()
    if library is not None:
        env["R_LIBS_USER"] = str(library)
    env["RENV_CONFIG_AUTOLOADER_ENABLED"] = "FALSE"
    with tempfile.TemporaryDirectory(prefix="rfd_appfin_parent_") as temporary:
        directory = Path(temporary)
        input_path = directory / "panel.csv"
        mean_path = directory / "verified_mean.csv"
        output_path = directory / "output"
        np.savetxt(input_path, observations.reshape(n, -1), delimiter=",", fmt="%.17g")
        np.savetxt(mean_path, np.asarray(mean_result.X).reshape(1, -1), delimiter=",", fmt="%.17g")
        command = [
            str(rscript), "--vanilla", str(R_WORKER), str(input_path), str(mean_path),
            str(output_path), str(n), str(m), str(rank),
            str(int(config["experiment"]["max_lag"])), str(int(parent["seed"])),
            str(int(parent["batch_size"])), str(int(parent["budget_iterations"])),
        ]
        print("[parent] running the literal cloned RFM at maximum sensitivity rank", flush=True)
        started = time.perf_counter()
        completed = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, check=False)
        if completed.returncode:
            raise RuntimeError(f"parent worker failed: {(completed.stderr or completed.stdout).strip()}")
        print(f"[parent] R worker complete in {time.perf_counter()-started:.1f}s", flush=True)

        result: dict[str, np.ndarray] = {
            "verified_mean_iterations": np.array(mean_result.n_iter),
            "verified_mean_residual": np.array(mean_result.residual),
        }
        tangent_dimension = m * (m + 1) // 2
        for prefix in ("budget", "converged"):
            status_path = output_path / f"{prefix}_status.txt"
            status = status_path.read_text(encoding="utf-8").splitlines()
            if not status or status[0].strip() != "ok":
                raise RuntimeError(f"parent {prefix} fit failed: {' '.join(status[1:])}")
            result[f"{prefix}_mean"] = _read_matrix(output_path / f"{prefix}_mean.csv", (m, m))
            result[f"{prefix}_log_rows"] = _read_matrix(output_path / f"{prefix}_log_rows.csv", (n, tangent_dimension))
            result[f"{prefix}_scores"] = _read_matrix(output_path / f"{prefix}_scores.csv", (n, rank))
            result[f"{prefix}_loadings"] = _read_matrix(output_path / f"{prefix}_loadings.csv", (rank, m, m))
            result[f"{prefix}_row_mean_tangent"] = _read_matrix(output_path / f"{prefix}_row_mean_tangent.csv", (m, m))
            result[f"{prefix}_rank_max_reconstruction"] = _read_matrix(output_path / f"{prefix}_reconstruction.csv", (n, m, m))
        return result


def _stage_diagnostics(fit) -> dict[str, Any]:
    stages = []
    reasons: list[str] = []
    for estimate in fit.centre.estimates:
        reasons.extend(estimate.fallback_reasons)
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is not None:
                stages.extend(one_sided.stages.stages)
    return {
        "fallback_count": int(fit.centre.fallback_count),
        "fallback_reasons": reasons,
        "nonconverged_stage_count": int(sum(not stage.converged for stage in stages)),
        "support_count_min": int(min(stage.support_count for stage in stages)),
        "support_count_max": int(max(stage.support_count for stage in stages)),
        "effective_sample_size_min": float(min(stage.effective_sample_size for stage in stages)),
        "effective_sample_size_max": float(max(stage.effective_sample_size for stage in stages)),
        "stage_iterations_max": int(max(stage.n_iter for stage in stages)),
        "stage_residual_max": float(max(stage.residual for stage in stages)),
    }


def run_rfd_stage(observations: np.ndarray, config: dict[str, Any]) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    n = observations.shape[0]
    settings = effective_rfd_settings(config, n)
    source = config["rfd"]
    model_config = RFDConfig(
        bandwidth=float(settings["bandwidth"]),
        n_cells=int(settings["n_cells"]),
        max_lag=int(config["experiment"]["max_lag"]),
        rank_method="fixed",
        # Fit only the declared primary rank.  The complete spectrum below
        # still supplies ranks 1..15 for tangent-energy sensitivity, without
        # forcing a high-rank BW Exp that is not part of the headline model.
        rank=int(config["experiment"]["primary_rank"]),
        tail_mode=str(source["tail_mode"]),
        normalization=str(source["normalization"]),
        overlap_fractions=tuple(source["overlap_fractions"]),
        mean_tol=float(source["mean_tolerance"]),
        mean_max_iter=int(source["mean_max_iterations"]),
    )
    time_values = np.arange(1, n + 1, dtype=float) / n
    print(
        "[RFD] fitting moving centres: "
        f"{settings['vertex_count']} vertices; nominal one-sided windows "
        f"{settings['broad_window_months']:.1f}/{settings['half_window_months']:.1f}/"
        f"{settings['quarter_window_months']:.1f} months",
        flush=True,
    )
    started = time.perf_counter()
    fit = fit_rfd(observations, time_values, BW_GEOMETRY, model_config)
    max_rank = int(config["experiment"]["sensitivity_max_rank"])
    centred_rows = fit.lag_operator.lag_row.centred_rows
    sensitivity_scores = centred_rows @ fit.spectrum.eigenvectors[:, :max_rank]
    elapsed = time.perf_counter() - started
    print(f"[RFD] complete in {elapsed:.1f}s", flush=True)
    diagnostics = _stage_diagnostics(fit)
    diagnostics["elapsed_seconds"] = elapsed
    diagnostics.update(settings)
    arrays = {
        "time": time_values,
        "vertex_times": fit.centre.vertex_times,
        "vertices": fit.centre.vertices,
        "local_centres": fit.tangent_rows.local_centres,
        "tangent_rows": fit.tangent_rows.rows,
        "basis": fit.tangent_rows.basis,
        "reference_point": fit.centre.polygon.reference_point,
        "eigenvalues": fit.spectrum.eigenvalues,
        "eigenvectors": fit.spectrum.eigenvectors,
        "scores": sensitivity_scores,
        "row_mean": fit.factors.row_mean,
        "primary_rank_reconstruction": fit.reconstructed_observations,
    }
    return arrays, diagnostics


def _cache_matches(meta_path: Path, digest: str) -> bool:
    if not meta_path.is_file():
        return False
    try:
        return json.loads(meta_path.read_text(encoding="utf-8")).get("digest") == digest
    except (OSError, json.JSONDecodeError):
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check-r", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config = load_configuration(args.config)
    panel = load_panel(config)
    design = build_design(config, panel)
    print(json.dumps(design, indent=2), flush=True)
    rscript_string = shutil.which("Rscript")
    if rscript_string is None:
        raise FileNotFoundError("Rscript is not on PATH")
    rscript = Path(rscript_string)
    if args.check_r or not args.dry_run:
        check_r_environment(rscript)
    if args.dry_run:
        print("APP-FIN dry run passed; no estimators were fitted.", flush=True)
        return

    output = ROOT / config["output"]["directory"]
    output.mkdir(parents=True, exist_ok=True)
    digest = experiment_digest(config)
    design["digest"] = digest
    _atomic_json(output / "design.json", design)

    parent_cache = output / "parent_fit.npz"
    parent_meta = output / "parent_fit.meta.json"
    if args.force or not parent_cache.is_file() or not _cache_matches(parent_meta, digest):
        parent_arrays = run_parent_stage(panel["panel"], config, rscript)
        _atomic_npz(parent_cache, **parent_arrays)
        _atomic_json(parent_meta, {"digest": digest, "completed": time.strftime("%Y-%m-%dT%H:%M:%S%z")})
    else:
        print("[parent] reusing digest-matched stage cache", flush=True)

    rfd_cache = output / "rfd_fit.npz"
    rfd_meta = output / "rfd_fit.meta.json"
    if args.force or not rfd_cache.is_file() or not _cache_matches(rfd_meta, digest):
        rfd_arrays, diagnostics = run_rfd_stage(panel["panel"], config)
        _atomic_npz(rfd_cache, **rfd_arrays)
        _atomic_json(rfd_meta, {"digest": digest, "completed": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "diagnostics": diagnostics})
    else:
        print("[RFD] reusing digest-matched stage cache", flush=True)

    from analyze_appfin_identification import analyze

    analyze(ROOT, config, panel, output)
    print(f"APP-FIN identification report: {output / 'report.md'}", flush=True)


if __name__ == "__main__":
    main()
