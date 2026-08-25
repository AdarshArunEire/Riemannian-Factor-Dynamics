from pathlib import Path

import numpy as np
import pytest

from experiments.analyze_appfin_identification import _load_vix, _rank_curve
from experiments.run_appfin_identification import (
    CONFIG_DEFAULT,
    ROOT,
    build_design,
    effective_rfd_settings,
    load_configuration,
    load_panel,
    validate_configuration,
)


def test_frozen_appfin_panel_contract_is_exact():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_panel(config)
    design = build_design(config, panel)

    assert panel["panel"].shape == (240, 12, 12)
    assert panel["months"][[0, -1]].tolist() == ["2000-01", "2019-12"]
    assert panel["tickers"].tolist() == [
        "MSFT", "AAPL", "ORCL", "CSCO",
        "JPM", "BAC", "WFC", "GS",
        "XOM", "CVX", "COP", "EOG",
    ]
    assert design["tangent_dimension"] == 78
    assert design["primary_rank"] == 2
    assert design["lags_months"] == [1, 6]


def test_effective_windows_are_predeclared_not_data_tuned():
    config = load_configuration(CONFIG_DEFAULT)
    settings = effective_rfd_settings(config, 240)

    assert settings["n_cells"] == 5
    assert settings["vertex_count"] == 6
    assert settings["bandwidth"] == pytest.approx(0.95 / 3.0)
    assert settings["broad_window_months"] == pytest.approx(76.0)
    assert settings["half_window_months"] == pytest.approx(38.0)
    assert settings["quarter_window_months"] == pytest.approx(19.0)


def test_configuration_rejects_rank_selection_disguised_as_sensitivity():
    config = load_configuration(CONFIG_DEFAULT)
    config["experiment"]["primary_rank"] = 16

    with pytest.raises(ValueError, match="rank contract"):
        validate_configuration(config)


def test_rank_curve_measures_residual_energy_without_selecting_rank():
    rows = np.array([
        [1.0, 1.0, 0.0],
        [-1.0, 1.0, 0.0],
        [1.0, -1.0, 0.0],
        [-1.0, -1.0, 0.0],
    ])
    scores = rows[:, :2]

    curve = _rank_curve(rows, scores, 2)

    assert curve[0] == pytest.approx(0.5)
    assert curve[1] == pytest.approx(0.0)


def test_vix_monthly_overlay_aligns_to_every_panel_month():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_panel(config)
    vix = _load_vix(ROOT / config["experiment"]["vix_path"], panel["months"])

    assert vix.shape == (240,)
    assert np.isfinite(vix).all()
    assert np.all(vix > 0.0)


def test_parent_worker_exports_every_prefix_reconstruction_producer():
    source = (ROOT / "experiments" / "parent_rfm_bw_worker.R").read_text(
        encoding="utf-8"
    )

    assert "_log_rows.csv" in source
    assert "_scores.csv" in source
    assert "_loadings.csv" in source
    assert "_row_mean_tangent.csv" in source
