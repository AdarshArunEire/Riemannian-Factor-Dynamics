"""Run the compact fixed-size Bures--Wasserstein Paper 1 closure matrix.

Safe cells fit the complete RFD estimator and expose every quantity in the
robust chain ``d_n -> 2 A_2 d_n + d_n^2 -> Delta_n``.  Hostile cells isolate
one BW theorem boundary at a time.  Expected rejection and the declared
positive-stage Richardson fallback are recorded as scientific outcomes, not
silently converted into successful fits.

Rows are append-only and parent-written, so an interrupted parallel run is
resumed by invoking the same command again.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import platform
import shutil
import sys
import time
import warnings
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

for _thread_variable in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))
sys.path.insert(0, str(ROOT / "experiments"))

from run_end_to_end import (  # noqa: E402
    _direct_sum_operator_norm,
    _intrinsic_rms,
    _procrustes_nrmse,
)
from run_paper1_controls import _control_loadings  # noqa: E402
from rfd.dgp.lsrfm import (  # noqa: E402
    AR1FactorConfig,
    LSRFMSample,
    LoadingConfig,
    NoiseConfig,
    centre_path_diagnostics,
    generate_factors,
    generate_reference_tangent_noise,
    rescaled_time,
)
from rfd.estimators.centre import (  # noqa: E402
    LocalMeanResult,
    ThreeScaleMeanResult,
    resolve_one_sided_centre,
)
from rfd.estimators.frame import (  # noqa: E402
    PolygonalFrame,
    evaluate_polygon,
    polygon_cell_count,
)
from rfd.estimators.lag import (  # noqa: E402
    assemble_lag_operator,
    coordinate_tangents,
    decompose_lag_operator,
    lag_cross_covariances,
    raw_ratio_rank,
    ridged_ratio_rank,
    tangent_coordinates,
    threshold_rank,
)
from rfd.geometry import BW_GEOMETRY  # noqa: E402
from rfd.model import RFDConfig, fit_rfd  # noqa: E402
from rfd.spd.bw import (  # noqa: E402
    bw_barycentre,
    bw_dist2,
    bw_exp,
    bw_log,
    bw_optimal_map,
)
from rfd.spd.linalg import spd_sqrt, sym  # noqa: E402


CONFIG_DEFAULT = ROOT / "config" / "bw_closure.yaml"
SCRIPT_PATH = Path(__file__).resolve()

IDENTITY_COLUMNS = [
    "profile", "group", "scenario", "scenario_label", "scenario_class",
    "mode", "expected", "n", "matrix_size", "replicate", "seed_key",
    "status", "boundary_verdict", "error_type", "error_message",
    "elapsed_seconds",
]

DIAGNOSTIC_COLUMNS = [
    # Estimator and robust statistical chain.
    "true_rank", "bandwidth", "n_cells", "grid_vertex_count", "max_lag",
    "pair_count_min", "generated_object_count", "mask_missing_fraction",
    "local_law_exponent", "dependence_producer", "factor_persistence_max",
    "noise_persistence",
    "centre_path_rms", "polygon_approximation_rms", "lag_row_error",
    "lag_row_error_scaled_n_3_7", "oracle_lag_row_size", "operator_error",
    "assembly_bound", "oracle_gap", "assembly_gap_ratio", "eta_gap_pass",
    "loading_subspace_error", "factor_score_nrmse", "null_eigenvalue",
    "null_bound_ratio", "threshold", "threshold_rank", "raw_ratio_rank",
    "ridged_ratio_rank", "selector_window_pass", "noise_lag_row_size",
    "population_lag_defect_declared", "observation_reconstruction_rms",
    "signal_reconstruction_rms", "row_residual_fraction",
    # Primitive domain and localization producers.
    "empirical_energy_R", "centre_path_length", "centre_path_energy",
    "estimated_polygon_length", "maximum_polygon_chord",
    "minimum_effective_sample_size", "minimum_support_count",
    "maximum_stage_iterations", "maximum_stage_residual",
    "nonconverged_stages", "fallback_count", "fallback_rate",
    "fallback_reason", "generated_min_eigenvalue", "generated_max_eigenvalue",
    "polar_singular_margin", "exp_factor_singular_margin",
    "score_radius_max", "domain_spectral_pass", "domain_polar_pass",
    "domain_exp_pass", "domain_score_pass", "domain_path_pass",
    "generated_membership_pass", "all_finite", "maximum_imaginary_part",
    # Standalone hostile-probe diagnostics.
    "probe_value", "probe_secondary", "probe_iterations", "probe_residual",
    "probe_converged", "probe_rejected", "probe_fallback_activated",
]

RAW_COLUMNS = IDENTITY_COLUMNS + DIAGNOSTIC_COLUMNS


@dataclass(frozen=True)
class BWTask:
    group: str
    scenario: str
    n: int
    replicate: int
    specification: dict[str, Any]


def load_configuration(path: Path, profile_name: str) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        source = yaml.safe_load(handle)
    profiles = source.get("profiles", {})
    if profile_name not in profiles:
        raise ValueError(f"unknown profile: {profile_name}")
    config = {
        "profile_name": profile_name,
        "profile": deepcopy(profiles[profile_name]),
        "experiment": deepcopy(source["experiment"]),
        "estimator": deepcopy(source["estimator"]),
        "domain": deepcopy(source["domain"]),
        "regime_groups": {
            "rate": deepcopy(source["rate_regimes"]),
            "scientific": deepcopy(source["scientific_regimes"]),
            "hostile": deepcopy(source["hostile_regimes"]),
        },
        "config_path": path.resolve(),
    }
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    if config["experiment"]["geometry"] != "bw":
        raise ValueError("the BW closure campaign requires geometry='bw'")
    if int(config["experiment"]["matrix_size"]) < 2:
        raise ValueError("matrix_size must be at least two")
    if int(config["estimator"]["max_lag"]) < 1:
        raise ValueError("max_lag must be positive")
    domain = config["domain"]
    if not 0.0 < float(domain["spectral_lower"]) < float(domain["spectral_upper"]):
        raise ValueError("spectral domain must have positive ordered bounds")
    known_modes = {
        "fit", "signed_exit", "near_identical", "rank_loss", "exp_exit",
        "dispersion",
    }
    for group, workload in config["profile"]["workloads"].items():
        if group not in config["regime_groups"]:
            raise ValueError(f"unknown workload group: {group}")
        n_values = [int(value) for value in workload["n_values"]]
        if not n_values or min(n_values) < 16:
            raise ValueError(f"{group} n_values must be nonempty and at least 16")
        if int(workload["replicates"]) < 1:
            raise ValueError(f"{group} replicates must be positive")
        for scenario in workload["regimes"]:
            if scenario not in config["regime_groups"][group]:
                raise ValueError(f"unknown {group} scenario: {scenario}")
            mode = config["regime_groups"][group][scenario]["mode"]
            if mode not in known_modes:
                raise ValueError(f"unknown mode for {scenario}: {mode}")


def build_tasks(config: dict[str, Any]) -> list[BWTask]:
    tasks: list[BWTask] = []
    for group, workload in config["profile"]["workloads"].items():
        regimes = config["regime_groups"][group]
        for n in workload["n_values"]:
            for scenario in workload["regimes"]:
                for replicate in range(int(workload["replicates"])):
                    tasks.append(BWTask(
                        group=group,
                        scenario=str(scenario),
                        n=int(n),
                        replicate=replicate,
                        specification=deepcopy(regimes[scenario]),
                    ))
    return tasks


def _component_rng(config: dict[str, Any], task: BWTask, component: int) -> np.random.Generator:
    group_code = {"rate": 1, "scientific": 2, "hostile": 3}[task.group]
    scenario_code = int.from_bytes(
        hashlib.sha256(task.scenario.encode("utf-8")).digest()[:4], "little"
    )
    return np.random.default_rng(np.random.SeedSequence([
        int(config["experiment"]["root_seed"]),
        int(config["profile"]["seed_namespace"]), group_code, scenario_code,
        task.n, task.replicate, component,
    ]))


def _unit(vector: np.ndarray, base: np.ndarray) -> np.ndarray:
    squared = float(BW_GEOMETRY.inner(base, vector, vector))
    if not np.isfinite(squared) or squared <= 1e-18:
        raise ValueError("BW control direction has zero or nonfinite norm")
    return sym(vector) / np.sqrt(squared)


def _base_and_directions(
    matrix_size: int, condition: float, path_kind: str
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not np.isfinite(condition) or condition < 1.0:
        raise ValueError("base condition must be finite and at least one")
    base = np.diag(np.geomspace(1.0 / condition, 1.0, matrix_size))
    diagonal = np.linspace(-1.0, 1.0, matrix_size)
    first = np.diag(diagonal)
    second = np.diag(np.linspace(1.0, -1.0, matrix_size) ** 2)
    if path_kind != "commuting":
        first = first.copy()
        first[0, -1] = first[-1, 0] = 0.25
        second = np.zeros_like(base)
        for index in range(matrix_size - 1):
            second[index, index + 1] = second[index + 1, index] = 1.0
    first = _unit(first, base)
    second = second - float(BW_GEOMETRY.inner(base, second, first)) * first
    second = _unit(second, base)
    return base, first, second


def _path_centres(
    time_values: np.ndarray,
    base: np.ndarray,
    first: np.ndarray,
    second: np.ndarray,
    path_kind: str,
    drift_scale: float,
) -> np.ndarray:
    time_values = np.asarray(time_values, dtype=float)
    first_profile = time_values + 0.5 * time_values**3
    second_profile = (
        np.zeros_like(time_values)
        if path_kind == "commuting"
        else 0.55 * np.sin(np.pi * time_values)
    )
    tangent = drift_scale * (
        first_profile[:, None, None] * first
        + second_profile[:, None, None] * second
    )
    return BW_GEOMETRY.exp(base, tangent)


def _active_experiment(config: dict[str, Any], task: BWTask) -> dict[str, Any]:
    active = deepcopy(config["experiment"])
    spec = task.specification
    active["base_condition"] = float(spec.get("base_condition", active["base_condition"]))
    active["factor_rank"] = int(spec.get("rank", active["factor_rank"]))
    active["factor_scale"] = deepcopy(spec.get("factor_scale", active["factor_scale"]))
    active["noise_scale"] = float(spec.get("noise_scale", active["noise_scale"]))
    active["loading_structure"] = str(
        spec.get("loading_structure", active["loading_structure"])
    )
    return active


def generate_fit_sample(
    config: dict[str, Any], task: BWTask
) -> tuple[LSRFMSample, np.ndarray, np.ndarray, np.ndarray]:
    spec = task.specification
    experiment = _active_experiment(config, task)
    base, first, second = _base_and_directions(
        int(experiment["matrix_size"]), float(experiment["base_condition"]),
        str(spec["path"]),
    )
    time_values = rescaled_time(task.n)
    path_time = np.concatenate(([0.0], time_values))
    path_centres = _path_centres(
        path_time, base, first, second, str(spec["path"]),
        float(spec["drift_scale"]),
    )
    centres = path_centres[1:]
    rank = int(spec["rank"])
    persistence = np.asarray(experiment["factor_persistence"], dtype=float)[:rank]
    scales = np.asarray(experiment["factor_scale"], dtype=float)[:rank]
    factors = generate_factors(
        _component_rng(config, task, 1), task.n,
        AR1FactorConfig(rank=rank, persistence=persistence, scale=scales),
    )
    loading_config = LoadingConfig(
        orientation=str(spec["loading_orientation"]),
        drift_overlap=float(spec.get("drift_overlap", 0.5)),
        structure=str(spec["loading_structure"]),
    )
    loadings = _control_loadings(
        _component_rng(config, task, 2), base, rank, first, BW_GEOMETRY,
        loading_config,
    )
    reference_effects = np.tensordot(factors, loadings, axes=([-1], [0]))
    reference_noise = generate_reference_tangent_noise(
        _component_rng(config, task, 3), task.n, base, BW_GEOMETRY,
        NoiseConfig(
            scale=float(spec["noise_scale"]),
            persistence=float(spec["noise_persistence"]),
            constant_norm=bool(experiment["noise_constant_norm"]),
            structure=str(spec["loading_structure"]),
        ),
    )
    factor_effects = BW_GEOMETRY.transport(reference_effects, base, centres)
    tangent_noise = BW_GEOMETRY.transport(reference_noise, base, centres)
    observations = BW_GEOMETRY.exp(centres, factor_effects + tangent_noise)
    path_length, path_energy = centre_path_diagnostics(
        path_time, path_centres, BW_GEOMETRY
    )
    return LSRFMSample(
        observations=observations,
        centres=centres,
        factors=factors,
        loadings=loadings,
        factor_effects=factor_effects,
        tangent_noise=tangent_noise,
        time=time_values,
        centre_path_length=path_length,
        centre_path_energy=path_energy,
        geometry_name="bw",
    ), base, first, second


def _model_config(config: dict[str, Any], task: BWTask) -> RFDConfig:
    estimator = config["estimator"]
    bandwidth = (
        float(estimator["bandwidth_constant"])
        * float(estimator["bandwidth_multiplier"])
        * task.n ** (-float(estimator["bandwidth_exponent"]))
    )
    n_cells = polygon_cell_count(
        task.n ** (-float(estimator["polygon_rate_exponent"])),
        constant=float(estimator["polygon_cell_constant"]),
    )
    return RFDConfig(
        bandwidth=bandwidth,
        n_cells=n_cells,
        max_lag=int(estimator["max_lag"]),
        rank_method="fixed",
        rank=int(task.specification["rank"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
        overlap_fractions=tuple(estimator["overlap_fractions"]),
        mean_tol=float(estimator["mean_tolerance"]),
        mean_max_iter=int(estimator["mean_max_iter"]),
    )


def _stage_diagnostics(fit) -> dict[str, Any]:
    stages = []
    reasons = []
    for estimate in fit.centre.estimates:
        reasons.extend(estimate.fallback_reasons)
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is not None:
                stages.extend(one_sided.stages.stages)
    return {
        "minimum_effective_sample_size": float(min(s.effective_sample_size for s in stages)),
        "minimum_support_count": int(min(s.support_count for s in stages)),
        "maximum_stage_iterations": int(max(s.n_iter for s in stages)),
        "maximum_stage_residual": float(max(s.residual for s in stages)),
        "nonconverged_stages": int(sum(not s.converged for s in stages)),
        "fallback_count": int(fit.centre.fallback_count),
        "fallback_rate": float(fit.centre.fallback_rate),
        "fallback_reason": "; ".join(sorted(set(reasons))),
    }


def _generated_points(fit) -> np.ndarray:
    points = []
    for estimate in fit.centre.estimates:
        points.append(estimate.point)
        for one_sided in (estimate.forward, estimate.backward):
            if one_sided is None:
                continue
            points.extend(stage.point for stage in one_sided.stages.stages)
            if one_sided.richardson.point is not None:
                points.append(one_sided.richardson.point)
    return np.stack(points)


def _pair_margin(left: np.ndarray, right: np.ndarray) -> tuple[float, float]:
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    left_root = spd_sqrt(left)
    right_root = spd_sqrt(right)
    polar = np.linalg.svd(left_root.mT @ right_root, compute_uv=False)[..., -1]
    exp_factor = np.linalg.svd(
        bw_optimal_map(left, right), compute_uv=False
    )[..., -1]
    return float(np.min(polar)), float(np.min(exp_factor))


def _domain_diagnostics(sample, fit, config: dict[str, Any]) -> dict[str, Any]:
    evaluation = evaluate_polygon(fit.centre.polygon, sample.time)
    reconstructed = fit.reconstructed_observations
    generated = _generated_points(fit)
    spectra = [
        np.linalg.eigvalsh(sample.centres),
        np.linalg.eigvalsh(sample.observations),
        np.linalg.eigvalsh(reconstructed),
        np.linalg.eigvalsh(generated),
    ]
    minimum = float(min(np.min(value) for value in spectra))
    maximum = float(max(np.max(value) for value in spectra))

    margins = [
        _pair_margin(evaluation.points, sample.observations),
        _pair_margin(evaluation.points, reconstructed),
        _pair_margin(fit.centre.vertices[:-1], fit.centre.vertices[1:]),
    ]
    polar_margin = min(value[0] for value in margins)
    exp_margin = min(value[1] for value in margins)
    score_radius = float(np.sqrt(np.max(BW_GEOMETRY.dist2(
        evaluation.points, sample.observations
    ))))
    chord_lengths = np.sqrt(BW_GEOMETRY.dist2(
        fit.centre.vertices[:-1], fit.centre.vertices[1:]
    ))
    polygon_length = float(np.sum(chord_lengths))
    maximum_chord = float(np.max(chord_lengths))
    domain = config["domain"]
    spectral_pass = (
        minimum >= float(domain["spectral_lower"])
        and maximum <= float(domain["spectral_upper"])
    )
    polar_pass = polar_margin >= float(domain["polar_singular_lower"])
    exp_pass = exp_margin >= float(domain["exp_factor_singular_lower"])
    score_pass = score_radius <= float(domain["score_radius_upper"])
    path_pass = polygon_length <= float(domain["path_length_upper"])
    all_values = [sample.observations, reconstructed, generated]
    all_finite = all(np.isfinite(value).all() for value in all_values)
    maximum_imaginary = max(
        float(np.max(np.abs(np.imag(value)))) if np.iscomplexobj(value) else 0.0
        for value in all_values
    )
    return {
        "generated_min_eigenvalue": minimum,
        "generated_max_eigenvalue": maximum,
        "polar_singular_margin": polar_margin,
        "exp_factor_singular_margin": exp_margin,
        "score_radius_max": score_radius,
        "estimated_polygon_length": polygon_length,
        "maximum_polygon_chord": maximum_chord,
        "generated_object_count": int(generated.shape[0]),
        "domain_spectral_pass": bool(spectral_pass),
        "domain_polar_pass": bool(polar_pass),
        "domain_exp_pass": bool(exp_pass),
        "domain_score_pass": bool(score_pass),
        "domain_path_pass": bool(path_pass),
        "generated_membership_pass": bool(
            spectral_pass and polar_pass and exp_pass and score_pass and path_pass
        ),
        "all_finite": bool(all_finite),
        "maximum_imaginary_part": maximum_imaginary,
    }


def _projector(vectors: np.ndarray, rank: int) -> np.ndarray:
    if rank == 0:
        return np.zeros((vectors.shape[0], vectors.shape[0]))
    return vectors[:, :rank] @ vectors[:, :rank].T


def _statistical_diagnostics(sample, fit, base: np.ndarray, config: dict[str, Any]) -> dict[str, Any]:
    estimator = config["estimator"]
    rank = sample.factors.shape[1]
    basis = BW_GEOMETRY.tangent_basis(base)
    oracle_vectors = np.tensordot(sample.factors, sample.loadings, axes=([-1], [0]))
    oracle_rows = tangent_coordinates(oracle_vectors, base, basis, BW_GEOMETRY)
    oracle_lag = lag_cross_covariances(
        oracle_rows, int(estimator["max_lag"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
    )
    oracle_operator = assemble_lag_operator(oracle_lag)
    oracle_spectrum = decompose_lag_operator(oracle_operator)

    aligned_vectors = BW_GEOMETRY.transport(
        fit.tangent_rows.reference_vectors,
        fit.centre.polygon.reference_point,
        base,
    )
    estimated_rows = tangent_coordinates(aligned_vectors, base, basis, BW_GEOMETRY)
    estimated_lag = lag_cross_covariances(
        estimated_rows, int(estimator["max_lag"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
    )
    estimated_operator = assemble_lag_operator(estimated_lag)
    estimated_spectrum = decompose_lag_operator(estimated_operator)

    lag_error = _direct_sum_operator_norm(
        estimated_lag.covariances - oracle_lag.covariances
    )
    a2 = _direct_sum_operator_norm(oracle_lag.covariances)
    assembly_bound = 2.0 * a2 * lag_error + lag_error**2
    operator_error = float(np.linalg.norm(
        estimated_operator.matrix - oracle_operator.matrix, ord=2
    ))
    if rank > 0:
        next_value = float(oracle_spectrum.eigenvalues[rank]) if (
            rank < oracle_spectrum.eigenvalues.size
        ) else 0.0
        gap = float(oracle_spectrum.eigenvalues[rank - 1] - next_value)
        loading_error = float(np.linalg.norm(
            _projector(estimated_spectrum.eigenvectors, rank)
            - _projector(oracle_spectrum.eigenvectors, rank), ord=2
        ))
        target_scores = oracle_lag.centred_rows @ oracle_spectrum.eigenvectors[:, :rank]
        fitted_scores = estimated_lag.centred_rows @ estimated_spectrum.eigenvectors[:, :rank]
        score_error = _procrustes_nrmse(fitted_scores, target_scores)
    else:
        gap = np.nan
        loading_error = np.nan
        score_error = np.nan
    null_index = min(rank, estimated_spectrum.eigenvalues.size - 1)
    null_eigenvalue = float(estimated_spectrum.eigenvalues[null_index])
    threshold_value = (
        float(estimator["selector_constant"])
        * sample.time.size ** (-float(estimator["selector_exponent"]))
    )
    selector_cap = min(
        int(estimator["selector_max_rank"]), estimated_spectrum.eigenvalues.size - 1
    )
    threshold_result = threshold_rank(
        estimated_spectrum.eigenvalues, threshold_value, max_rank=selector_cap
    )
    raw_result = raw_ratio_rank(
        estimated_spectrum.eigenvalues, max_rank=selector_cap
    )
    ridge_result = ridged_ratio_rank(
        estimated_spectrum.eigenvalues, threshold_value, max_rank=selector_cap
    )
    if rank == 0:
        selector_window = threshold_value > float(estimated_spectrum.eigenvalues[0])
    else:
        selector_window = (
            null_eigenvalue < threshold_value
            < float(estimated_spectrum.eigenvalues[rank - 1])
        )

    reference_noise = BW_GEOMETRY.transport(sample.tangent_noise, sample.centres, base)
    noise_rows = tangent_coordinates(reference_noise, base, basis, BW_GEOMETRY)
    noise_lag = lag_cross_covariances(
        noise_rows, int(estimator["max_lag"]),
        tail_mode=str(estimator["tail_mode"]),
        normalization=str(estimator["normalization"]),
    )
    energy = sample.factor_effects + sample.tangent_noise
    energy_squared = BW_GEOMETRY.inner(sample.centres, energy, energy)
    latent_signal = BW_GEOMETRY.exp(sample.centres, sample.factor_effects)
    row_norm = np.linalg.norm(estimated_lag.centred_rows)
    residual_norm = np.linalg.norm(fit.factors.residual_rows)
    eta_gap = bool(assembly_bound < gap) if np.isfinite(gap) and gap > 0.0 else False
    return {
        "true_rank": rank,
        "grid_vertex_count": int(fit.centre.vertex_times.size),
        "max_lag": int(estimator["max_lag"]),
        "pair_count_min": int(np.min(estimated_lag.pair_counts)),
        "mask_missing_fraction": 0.0,
        "lag_row_error": lag_error,
        "lag_row_error_scaled_n_3_7": lag_error * sample.time.size ** (3.0 / 7.0),
        "oracle_lag_row_size": a2,
        "operator_error": operator_error,
        "assembly_bound": assembly_bound,
        "oracle_gap": gap,
        "assembly_gap_ratio": assembly_bound / gap if np.isfinite(gap) and gap > 0.0 else np.nan,
        "eta_gap_pass": eta_gap,
        "loading_subspace_error": loading_error,
        "factor_score_nrmse": score_error,
        "null_eigenvalue": null_eigenvalue,
        "null_bound_ratio": null_eigenvalue / lag_error**2 if lag_error > 0.0 else np.nan,
        "threshold": threshold_value,
        "threshold_rank": int(threshold_result.rank),
        "raw_ratio_rank": int(raw_result.rank),
        "ridged_ratio_rank": int(ridge_result.rank),
        "selector_window_pass": bool(selector_window),
        "noise_lag_row_size": _direct_sum_operator_norm(noise_lag.covariances),
        "population_lag_defect_declared": 0.0 if (
            float(sample.time.size) > 0.0
        ) else np.nan,
        "observation_reconstruction_rms": _intrinsic_rms(
            BW_GEOMETRY, fit.reconstructed_observations, sample.observations
        ),
        "signal_reconstruction_rms": _intrinsic_rms(
            BW_GEOMETRY, fit.reconstructed_observations, latent_signal
        ),
        "row_residual_fraction": residual_norm / row_norm if row_norm > 0.0 else np.nan,
        "empirical_energy_R": float(np.sqrt(np.max(np.maximum(energy_squared, 0.0)))),
        "centre_path_length": sample.centre_path_length,
        "centre_path_energy": sample.centre_path_energy,
    }


def evaluate_fit_task(config: dict[str, Any], task: BWTask) -> dict[str, Any]:
    sample, base, first, second = generate_fit_sample(config, task)
    model_config = _model_config(config, task)
    fit = fit_rfd(sample.observations, sample.time, BW_GEOMETRY, model_config)
    estimated_centres = evaluate_polygon(fit.centre.polygon, sample.time).points
    true_vertices = _path_centres(
        fit.centre.vertex_times, base, first, second,
        str(task.specification["path"]), float(task.specification["drift_scale"]),
    )
    true_polygon = PolygonalFrame(fit.centre.vertex_times, true_vertices, BW_GEOMETRY)
    true_polygon_centres = evaluate_polygon(true_polygon, sample.time).points
    result = {
        "bandwidth": model_config.bandwidth,
        "n_cells": model_config.n_cells,
        "local_law_exponent": np.inf,
        "dependence_producer": "geometric-AR1 physical dependence; iid tangent noise",
        "factor_persistence_max": float(np.max(np.abs(
            np.asarray(_active_experiment(config, task)["factor_persistence"], dtype=float)
            [: int(task.specification["rank"])]
        ))) if int(task.specification["rank"]) > 0 else 0.0,
        "noise_persistence": float(task.specification["noise_persistence"]),
        "centre_path_rms": _intrinsic_rms(
            BW_GEOMETRY, estimated_centres, sample.centres
        ),
        "polygon_approximation_rms": _intrinsic_rms(
            BW_GEOMETRY, true_polygon_centres, sample.centres
        ),
        **_statistical_diagnostics(sample, fit, base, config),
        **_stage_diagnostics(fit),
        **_domain_diagnostics(sample, fit, config),
    }
    return result


def _local_stage(point: np.ndarray, bandwidth: float) -> LocalMeanResult:
    return LocalMeanResult(
        point=point, weights=np.ones(1), target=0.5, bandwidth=bandwidth,
        side="forward", support_count=1, effective_sample_size=1.0,
        n_iter=1, residual=0.0, converged=True,
    )


def _probe_signed_exit(matrix_size: int) -> dict[str, Any]:
    points = tuple((root**2) * np.eye(matrix_size) for root in (3.0, 2.0, 0.1))
    stages = ThreeScaleMeanResult(
        target=0.5, base_bandwidth=0.2, side="forward",
        stages=tuple(_local_stage(point, bandwidth) for point, bandwidth in zip(
            points, (0.2, 0.1, 0.05)
        )),
    )
    resolved = resolve_one_sided_centre(stages, BW_GEOMETRY)
    return {
        "probe_fallback_activated": bool(resolved.used_fallback),
        "fallback_count": int(resolved.used_fallback),
        "fallback_rate": float(resolved.used_fallback),
        "fallback_reason": resolved.fallback_reason or "",
        "probe_rejected": False,
        "all_finite": bool(np.isfinite(resolved.point).all()),
        "generated_min_eigenvalue": float(np.min(np.linalg.eigvalsh(resolved.point))),
    }


def _probe_near_identical(matrix_size: int, rng: np.random.Generator) -> dict[str, Any]:
    base = np.diag(np.linspace(0.8, 1.2, matrix_size))
    perturbation = sym(rng.standard_normal((matrix_size, matrix_size)))
    perturbation /= np.linalg.norm(perturbation)
    nearby = base + 1e-12 * perturbation
    value = float(bw_dist2(base, nearby))
    return {
        "probe_value": value,
        "probe_rejected": False,
        "all_finite": bool(np.isfinite(value)),
        "maximum_imaginary_part": 0.0,
    }


def _probe_rank_loss(matrix_size: int) -> dict[str, Any]:
    rank_deficient = np.eye(matrix_size)
    rank_deficient[-1, -1] = 0.0
    rejected = False
    finite = False
    message = ""
    try:
        with warnings.catch_warnings(), np.errstate(all="raise"):
            warnings.simplefilter("error")
            value = bw_log(rank_deficient, np.eye(matrix_size))
        finite = bool(np.isfinite(value).all())
        rejected = not finite
    except (ValueError, FloatingPointError, RuntimeWarning, np.linalg.LinAlgError) as error:
        rejected = True
        message = f"{type(error).__name__}: {error}"
    return {
        "probe_rejected": rejected,
        "all_finite": finite,
        "fallback_reason": message,
        "generated_min_eigenvalue": 0.0,
    }


def _probe_exp_exit(matrix_size: int) -> dict[str, Any]:
    rejected = False
    message = ""
    try:
        bw_exp(np.eye(matrix_size), -3.0 * np.eye(matrix_size))
    except (ValueError, FloatingPointError, np.linalg.LinAlgError) as error:
        rejected = True
        message = f"{type(error).__name__}: {error}"
    return {
        "probe_rejected": rejected,
        "fallback_reason": message,
        "exp_factor_singular_margin": -0.5,
        "all_finite": True,
    }


def _rotation(matrix_size: int, angle: float) -> np.ndarray:
    rotation = np.eye(matrix_size)
    cosine, sine = np.cos(angle), np.sin(angle)
    rotation[:2, :2] = [[cosine, -sine], [sine, cosine]]
    return rotation


def _probe_dispersion(matrix_size: int, task: BWTask) -> dict[str, Any]:
    level = 0.35 if task.n <= 512 else 1.0
    spectrum = np.linspace(1.0, 3.0, matrix_size)
    matrices = np.stack([
        _rotation(matrix_size, sign * level) @ np.diag(spectrum)
        @ _rotation(matrix_size, sign * level).T
        for sign in (-1.0, -0.35, 0.35, 1.0)
    ])
    result = bw_barycentre(matrices, tol=1e-12, max_iter=300)
    spread = float(np.sqrt(np.max(bw_dist2(result.X, matrices))))
    return {
        "probe_value": level,
        "probe_secondary": spread,
        "probe_iterations": result.n_iter,
        "probe_residual": result.residual,
        "probe_converged": result.converged,
        "probe_rejected": False,
        "all_finite": bool(np.isfinite(result.X).all()),
        "generated_min_eigenvalue": float(np.min(np.linalg.eigvalsh(matrices))),
        "generated_max_eigenvalue": float(np.max(np.linalg.eigvalsh(matrices))),
    }


def evaluate_probe_task(config: dict[str, Any], task: BWTask) -> dict[str, Any]:
    mode = task.specification["mode"]
    matrix_size = int(config["experiment"]["matrix_size"])
    rng = _component_rng(config, task, 9)
    if mode == "signed_exit":
        return _probe_signed_exit(matrix_size)
    if mode == "near_identical":
        return _probe_near_identical(matrix_size, rng)
    if mode == "rank_loss":
        return _probe_rank_loss(matrix_size)
    if mode == "exp_exit":
        return _probe_exp_exit(matrix_size)
    if mode == "dispersion":
        return _probe_dispersion(matrix_size, task)
    raise ValueError(f"unknown probe mode: {mode}")


def _base_row(config: dict[str, Any], task: BWTask) -> dict[str, Any]:
    row = {column: np.nan for column in RAW_COLUMNS}
    row.update({
        "profile": config["profile_name"],
        "group": task.group,
        "scenario": task.scenario,
        "scenario_label": task.specification["label"],
        "scenario_class": task.specification["class"],
        "mode": task.specification["mode"],
        "expected": task.specification["expected"],
        "n": task.n,
        "matrix_size": int(config["experiment"]["matrix_size"]),
        "replicate": task.replicate,
        "seed_key": (
            f"{config['profile']['seed_namespace']}.{task.group}."
            f"{task.scenario}.{task.n}.{task.replicate}"
        ),
        "error_type": "",
        "error_message": "",
        "fallback_reason": "",
    })
    return row


def _verdict(task: BWTask, result: dict[str, Any]) -> str:
    expected = task.specification["expected"]
    if task.specification["mode"] == "fit":
        membership = bool(result.get("generated_membership_pass", False))
        finite = bool(result.get("all_finite", False))
        if expected == "safe":
            return "pass" if membership and finite else "fail"
        return "boundary_exposed" if (not membership or not finite) else "boundary_not_reached"
    if expected == "fallback":
        return "pass" if result.get("probe_fallback_activated") else "fail"
    if expected == "reject":
        return "pass" if result.get("probe_rejected") else "fail"
    if expected == "finite":
        return "pass" if result.get("all_finite") else "fail"
    return "unknown"


def run_task(config: dict[str, Any], task: BWTask) -> dict[str, Any]:
    started = time.perf_counter()
    row = _base_row(config, task)
    try:
        if task.specification["mode"] == "fit":
            result = evaluate_fit_task(config, task)
        else:
            result = evaluate_probe_task(config, task)
        row.update(result)
        row["status"] = "ok"
        row["boundary_verdict"] = _verdict(task, result)
    except Exception as error:
        row.update({
            "status": "error",
            "boundary_verdict": (
                "honest_rejection" if task.specification["expected"] in {
                    "reject", "boundary"
                } else "fail"
            ),
            "error_type": type(error).__name__,
            "error_message": str(error).replace("\n", " ")[:500],
        })
    row["elapsed_seconds"] = time.perf_counter() - started
    return row


def _row_key(row: dict[str, Any] | pd.Series) -> tuple[str, str, int, int]:
    return (
        str(row["group"]), str(row["scenario"]), int(row["n"]),
        int(row["replicate"]),
    )


def read_rows(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=RAW_COLUMNS)
    return pd.read_csv(path)


def append_row(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RAW_COLUMNS)
        if write_header:
            writer.writeheader()
        writer.writerow({column: row.get(column, np.nan) for column in RAW_COLUMNS})
        handle.flush()
        os.fsync(handle.fileno())


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def initialize_output(config: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    metadata_path = output / "metadata.json"
    metadata = {
        "profile": config["profile_name"],
        "recorded": bool(config["profile"]["recorded"]),
        "config_sha256": _digest(config["config_path"]),
        "script_sha256": _digest(SCRIPT_PATH),
        "root_seed": int(config["experiment"]["root_seed"]),
        "seed_namespace": int(config["profile"]["seed_namespace"]),
        "numpy": np.__version__,
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    if metadata_path.exists():
        existing = json.loads(metadata_path.read_text(encoding="utf-8"))
        for key in (
            "profile", "config_sha256", "script_sha256", "root_seed",
            "seed_namespace",
        ):
            if existing.get(key) != metadata[key]:
                raise RuntimeError(f"existing output metadata disagrees on {key}")
    else:
        metadata_path.write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        shutil.copy2(config["config_path"], output / "bw_closure.yaml")


def summarize(raw: pd.DataFrame, output: Path, requested: int) -> None:
    if raw.empty:
        summary = pd.DataFrame()
    else:
        rows = []
        for (group, scenario, n), cell in raw.groupby(["group", "scenario", "n"]):
            rows.append({
                "group": group,
                "scenario": scenario,
                "n": int(n),
                "rows": len(cell),
                "ok": int((cell["status"] == "ok").sum()),
                "pass_or_boundary_percent": float(100.0 * cell["boundary_verdict"].isin([
                    "pass", "boundary_exposed", "honest_rejection"
                ]).mean()),
                "median_centre_error": float(pd.to_numeric(
                    cell["centre_path_rms"], errors="coerce"
                ).median()),
                "median_lag_row_error": float(pd.to_numeric(
                    cell["lag_row_error"], errors="coerce"
                ).median()),
                "median_loading_error": float(pd.to_numeric(
                    cell["loading_subspace_error"], errors="coerce"
                ).median()),
                "domain_pass_percent": float(100.0 * pd.to_numeric(
                    cell["generated_membership_pass"], errors="coerce"
                ).mean()),
            })
        summary = pd.DataFrame(rows)
    summary.to_csv(output / "summary.csv", index=False)
    failures = raw.loc[raw["boundary_verdict"] == "fail"] if not raw.empty else raw
    lines = [
        "# P1-BW-CLOSE run", "",
        "Numerical evidence only. Safe interiors must complete inside the declared",
        "generated domain; hostile cells pass through explicit rejection, fallback,",
        "or a recorded boundary exposure.", "",
        f"- requested tasks: {requested}",
        f"- rows on disk: {len(raw)}",
        f"- ordinary errors: {int((raw['status'] == 'error').sum()) if not raw.empty else 0}",
        f"- failed verdicts: {len(failures)}", "",
        "The raw file retains every primitive margin and the complete robust-rate chain.",
    ]
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_workload(config: dict[str, Any], tasks: list[BWTask], workers: int) -> None:
    print(f"profile: {config['profile_name']}")
    print(f"recorded: {config['profile']['recorded']}")
    print(f"output: {config['profile']['output_dir']}")
    for group in ("rate", "scientific", "hostile"):
        group_tasks = [task for task in tasks if task.group == group]
        if group_tasks:
            print(f"{group}: {len(group_tasks)} tasks")
    print(f"requested tasks: {len(tasks)}")
    print(f"workers: {workers} (one BLAS thread per worker)")


def run(config: dict[str, Any], *, workers: int = 1, max_tasks: int | None = None) -> None:
    output = (ROOT / config["profile"]["output_dir"]).resolve()
    initialize_output(config, output)
    raw_path = output / "raw.csv"
    existing = read_rows(raw_path)
    completed = {_row_key(row) for _, row in existing.iterrows()}
    tasks = build_tasks(config)
    pending = [task for task in tasks if _row_key({
        "group": task.group, "scenario": task.scenario, "n": task.n,
        "replicate": task.replicate,
    }) not in completed]
    if max_tasks is not None:
        pending = pending[:max_tasks]
    if workers == 1:
        for index, task in enumerate(pending, start=1):
            print(
                f"[{index}/{len(pending)}] {task.scenario}, n={task.n}, "
                f"rep={task.replicate}", flush=True,
            )
            append_row(raw_path, run_task(config, task))
    elif pending:
        print(
            f"dispatching {len(pending)} tasks to {workers} worker processes; "
            "the parent alone writes rows", flush=True,
        )
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(run_task, config, task): task for task in pending}
            for count, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                task = futures[future]
                row = future.result()
                append_row(raw_path, row)
                print(
                    f"[{count}/{len(pending)} complete] {task.scenario}, n={task.n}, "
                    f"rep={task.replicate}, status={row['status']}, "
                    f"verdict={row['boundary_verdict']}", flush=True,
                )
    summarize(read_rows(raw_path), output, len(tasks))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--profile", choices=("smoke", "bw_closure"), default="smoke")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.workers < 1 or args.workers > 8:
        raise ValueError("workers must lie between one and eight")
    if args.max_tasks is not None and args.max_tasks < 1:
        raise ValueError("max-tasks must be positive")
    config = load_configuration(args.config.resolve(), args.profile)
    tasks = build_tasks(config)
    print_workload(config, tasks, args.workers)
    if args.dry_run:
        return 0
    try:
        run(config, workers=args.workers, max_tasks=args.max_tasks)
    except KeyboardInterrupt:
        print("\nInterrupted. Completed rows are on disk; rerun to resume.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
