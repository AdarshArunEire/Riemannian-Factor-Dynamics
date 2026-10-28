from pathlib import Path

import pytest

PANEL = Path(__file__).resolve().parents[2] / "results/intermediate/hf0_crypto/hourly_covariances.npz"
NEEDS_PANEL = {
    "test_hf1_frozen_design_and_sealed_year_boundary",
    "test_hf2_design_separates_rank_tuning_from_representation_evaluation",
    "test_recorded_protocol_covers_every_2025_hour_without_leakage",
    "test_smoke_protocol_is_small_but_still_strictly_causal",
    "test_representation_digest_ignores_rank_grid_and_forecast_head",
}


def pytest_collection_modifyitems(items):
    if PANEL.is_file():
        return
    skip = pytest.mark.skip(reason="needs the hourly crypto panel: python experiments/crypto/data.py --profile full")
    for item in items:
        if item.originalname in NEEDS_PANEL:
            item.add_marker(skip)
