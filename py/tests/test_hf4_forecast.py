from copy import deepcopy
from pathlib import Path
import sys

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from experiments import run_hf4_forecast as hf4


def test_recorded_protocol_covers_every_2025_hour_without_leakage():
    config = hf4.load_configuration()
    panel = hf4.load_panel(config)
    blocks = hf4.forecast_blocks(panel, config, smoke=False)

    assert len(blocks) == 14
    assert sum(block["target_stop"] - block["target_start"] for block in blocks) == 8760
    assert blocks[0]["training_stop"] == blocks[0]["target_start"]
    assert blocks[-1]["target_stop"] == panel["covariances"].shape[0]
    assert all(block["training_stop"] <= block["target_start"] for block in blocks)
    assert all(
        block["training_stop"] - block["training_start"] == 26 * 168
        for block in blocks
    )


def test_rank_grid_and_evaluation_year_are_frozen():
    config = hf4.load_configuration()

    assert config["representation"]["sensitivity_ranks"] == list(range(1, 19))
    assert config["score_heads"]["methods"] == ["var1", "har_ols", "vhar_ridge"]

    bad_rank = deepcopy(config)
    bad_rank["representation"]["sensitivity_ranks"] = list(range(1, 18))
    with pytest.raises(ValueError, match="sensitivities"):
        hf4.validate_configuration(bad_rank)

    bad_year = deepcopy(config)
    bad_year["experiment"]["evaluation_year"] = 2024
    with pytest.raises(ValueError, match="2024 development and 2025 evaluation"):
        hf4.validate_configuration(bad_year)


def test_smoke_protocol_is_small_but_still_strictly_causal():
    config = hf4.load_configuration()
    panel = hf4.load_panel(config)
    blocks = hf4.forecast_blocks(panel, config, smoke=True)

    assert len(blocks) == 2
    assert sum(block["target_stop"] - block["target_start"] for block in blocks) == 48
    assert np.all(
        panel["years"][blocks[0]["target_start"]:blocks[-1]["target_stop"]] == 2024
    )
    assert all(block["training_stop"] == block["target_start"] for block in blocks)
    assert all(
        block["training_stop"] - block["training_start"] == 4 * 168
        for block in blocks
    )


def test_terminal_centre_extension_is_constant_and_does_not_mutate_frame():
    vertices = np.stack((np.eye(2), 2.0 * np.eye(2)))
    frame = hf4.PolygonalFrame(
        np.array([0.0, 1.0]), vertices, hf4.BW_GEOMETRY
    )
    extended = hf4._extended_frame(frame, 1.5)

    assert np.array_equal(frame.vertex_times, np.array([0.0, 1.0]))
    assert np.array_equal(extended.vertex_times, np.array([0.0, 1.0, 1.5]))
    assert np.array_equal(extended.vertices[-1], extended.vertices[-2])


def test_newey_west_interval_preserves_constant_paired_difference():
    result = hf4.newey_west_mean_interval(np.full(200, -0.25))

    assert result["mean_difference_rfd_minus_parent"] == pytest.approx(-0.25)
    assert result["newey_west_se"] == pytest.approx(0.0)
    assert result["ci95_lower"] == pytest.approx(-0.25)
    assert result["ci95_upper"] == pytest.approx(-0.25)


def _dummy_representation_stage():
    return {
        "training_scores": np.arange(15, dtype=float).reshape(5, 3),
        "revealed_scores": np.arange(12, dtype=float).reshape(4, 3),
        "loadings": np.eye(3),
        "row_mean": np.zeros(3),
        "basis": np.asarray([
            [[1.0, 0.0], [0.0, 0.0]],
            [[0.0, 1.0 / np.sqrt(2.0)], [1.0 / np.sqrt(2.0), 0.0]],
            [[0.0, 0.0], [0.0, 1.0]],
        ]),
        "future_times": np.linspace(1.1, 1.4, 4),
        "future_local_centres": np.repeat(np.eye(2)[None], 4, axis=0),
        "frame_vertex_times": np.array([0.0, 1.4]),
        "frame_vertices": np.repeat(np.eye(2)[None], 2, axis=0),
        "fit_seconds": np.asarray(2.5),
    }


def test_representation_cache_round_trip_avoids_refit(tmp_path, monkeypatch):
    stage = _dummy_representation_stage()
    block = {
        "block": 0, "training_start": 0, "training_stop": 5,
        "target_start": 5, "target_stop": 9,
    }
    base_digest = "base"
    digest = hf4._representation_stage_digest(base_digest, block, "parent_rfm")
    cache, meta = hf4._representation_cache_paths(tmp_path, 0, "parent_rfm")
    hf4._atomic_npz(cache, **stage)
    hf4._atomic_json(meta, {"digest": digest})

    def fail_refit(*args, **kwargs):
        raise AssertionError("digest-matched representation should not refit")

    monkeypatch.setattr(hf4, "_fit_representation_stage", fail_refit)
    loaded, hit = hf4._load_or_fit_representation_stage(
        "parent_rfm", np.empty((5, 2, 2)), np.empty((4, 2, 2)),
        {}, tmp_path, block, base_digest,
    )

    assert hit
    assert set(loaded) == set(stage)
    for name in stage:
        assert np.array_equal(loaded[name], stage[name])


def test_representation_digest_ignores_rank_grid_and_forecast_head():
    config = hf4.load_configuration()
    baseline = hf4.representation_cache_base_digest(config, smoke=True)

    changed_head = deepcopy(config)
    changed_head["representation"]["sensitivity_ranks"] = [1]
    changed_head["baselines"]["har_daily_hours"] = 12
    changed_head["score_heads"]["methods"] = ["har_ols"]
    changed_head["score_heads"]["vhar_ridge"] = 100.0
    assert hf4.representation_cache_base_digest(changed_head, smoke=True) == baseline

    changed_geometry = deepcopy(config)
    changed_geometry["representation"]["piecewise_segments"] = 5
    assert hf4.representation_cache_base_digest(changed_geometry, smoke=True) != baseline


def test_cached_revealed_scores_are_shifted_causally():
    training = np.array([[1.0, 10.0], [2.0, 20.0]])
    revealed = np.array([[3.0, 30.0], [4.0, 40.0], [5.0, 50.0]])

    latest = hf4._causal_latest_scores(training, revealed)

    assert np.array_equal(latest, np.array([
        [2.0, 20.0],
        [3.0, 30.0],
        [4.0, 40.0],
    ]))


def test_scored_rows_distinguish_native_var_and_har_heads():
    targets = np.repeat(np.eye(2)[None], 2, axis=0)
    hours = np.asarray(["2025-01-01T00", "2025-01-01T01"], dtype="datetime64[h]")

    native = hf4._score_forecasts(
        "locf", "native", 0, "baseline", targets, targets, hours, 0
    )
    har = hf4._score_forecasts(
        "rfd_piecewise6", "har", 1, "sensitivity",
        targets, targets, hours, 0,
    )

    assert set(native["head"]) == {"native"}
    assert set(har["head"]) == {"har"}
    assert not hf4.pd.concat((native, har)).duplicated(
        ["target_hour", "method", "head", "rank"]
    ).any()


def test_legacy_original_rows_are_validated_and_labelled_without_recomputation():
    targets = np.repeat(np.eye(2)[None], 2, axis=0)
    hours = np.asarray(["2025-01-01T00", "2025-01-01T01"], dtype="datetime64[h]")
    rows = []
    for method in hf4.BASELINE_METHODS:
        rows.append(hf4._score_forecasts(
            method, "native", 0, "baseline", targets, targets, hours, 0
        ))
    for method in hf4.REPRESENTATION_METHODS:
        for rank in range(1, 20):
            role = "headline" if rank == 19 else "sensitivity"
            rows.append(hf4._score_forecasts(
                method, "var1", rank, role, targets, targets, hours, 0
            ))
    legacy = hf4.pd.concat(rows, ignore_index=True).drop(columns="head")
    legacy = legacy.rename(columns={"representation_fit_seconds": "fit_seconds"})
    legacy = legacy.drop(columns="head_fit_seconds")
    block = {
        "block": 0, "training_start": 0, "training_stop": 2,
        "target_start": 2, "target_stop": 4,
    }

    adopted = hf4._normalise_frozen_original_rows(
        legacy, block=block, target_hours=hours
    )

    assert len(adopted) == 82
    assert set(adopted[adopted["rank"] == 0]["head"]) == {"native"}
    assert set(adopted[adopted["rank"] > 0]["head"]) == {"var1"}
    assert "representation_fit_seconds" in adopted
    assert "head_fit_seconds" in adopted
