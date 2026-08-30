from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments"))

from run_centre_k_curve import load_configuration  # noqa: E402


def test_dense_k_curve_is_consecutive_and_stops_before_empty_regions() -> None:
    config = load_configuration(ROOT / "config" / "centre_k_curve_n240.yaml")
    assert config["selection"]["k_values"] == list(range(1, 20))
    assert config["selection"]["holdout_block_months"] == 12
