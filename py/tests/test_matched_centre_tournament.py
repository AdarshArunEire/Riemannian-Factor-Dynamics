from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments"))

from run_matched_centre_tournament import build_design, load_configuration  # noqa: E402


def test_matched_tournament_design_counts() -> None:
    config = load_configuration(ROOT / "config" / "matched_centre_tournament.yaml")
    design = build_design(config, "n240", smoke=False)
    assert design["tasks"] == 32
    assert design["n_values"] == [240]
    assert design["matrix_size"] == 12


def test_smoke_design_is_small() -> None:
    config = load_configuration(ROOT / "config" / "matched_centre_tournament.yaml")
    design = build_design(config, "n8192", smoke=True)
    assert design["tasks"] == 1
    assert design["n_values"] == [96]
