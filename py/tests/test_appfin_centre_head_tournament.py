from pathlib import Path

import numpy as np
import pytest

from experiments.run_appfin_centre_head_tournament import (
    CENTRE_LABELS,
    CONFIG_DEFAULT,
    _augment_summary,
    _frame_bundle,
    build_design,
    load_configuration,
    validate_configuration,
)
from experiments.run_appfin_identification import load_panel


def test_tournament_contract_has_global_parent_and_all_positive_rfd_paths():
    config = load_configuration(CONFIG_DEFAULT)
    panel = load_panel(config["source_filter"]["source"])
    design = build_design(config, panel, 36)

    assert design["initial_train_months"] == 204
    assert design["forecast_months"] == 36
    assert design["rank"] == 2
    assert design["max_lag"] == 6
    assert len(design["methods"]) == 10
    assert set(config["experiment"]["centre_methods"]) == set(CENTRE_LABELS)
    assert "prefix only" in design["causality"]


def test_configuration_rejects_unknown_or_duplicate_centre_methods():
    config = load_configuration(CONFIG_DEFAULT)
    config["experiment"]["centre_methods"].append("mystery")
    with pytest.raises(ValueError, match="unknown centre"):
        validate_configuration(config)

    config = load_configuration(CONFIG_DEFAULT)
    config["experiment"]["centre_methods"].append("segmented_6")
    with pytest.raises(ValueError, match="unique"):
        validate_configuration(config)

    config = load_configuration(CONFIG_DEFAULT)
    config["experiment"]["workers"] = 0
    with pytest.raises(ValueError, match="workers"):
        validate_configuration(config)


def test_frame_bundle_returns_continuous_frames_with_shared_domain():
    config = load_configuration(CONFIG_DEFAULT)
    config["source_filter"]["source"]["rfd"]["mean_max_iterations"] = 80
    n = 36
    angle = np.linspace(0.0, 0.25, n)
    observations = np.stack([
        np.array([[1.3 + value, 0.04 * np.sin(value)],
                  [0.04 * np.sin(value), 0.8 + 0.3 * value]])
        for value in angle
    ])
    frames, diagnostics = _frame_bundle(observations, config)

    assert set(frames) == set(CENTRE_LABELS)
    assert set(diagnostics) == set(CENTRE_LABELS)
    for frame in frames.values():
        assert frame.vertex_times[0] == pytest.approx(1.0 / n)
        assert frame.vertex_times[-1] == pytest.approx(1.0)
        assert np.all(np.linalg.eigvalsh(frame.vertices) > 0.0)
    assert frames["segmented_6"].vertices.shape[0] == 8
    assert frames["segmented_12"].vertices.shape[0] == 14


def test_summary_uses_explicit_parent_multipliers_and_percent_changes():
    summary = np.array([
        ("Parent RFM global–VAR", 20.0, 10.0, 5.0),
        ("RFD piecewise-6 polygon–VAR", 15.0, 25.0, 4.0),
    ], dtype=[("method", "U40"), ("mean_frobenius2", float),
              ("mean_qlike", float), ("mean_bw2", float)])
    import pandas as pd

    result = _augment_summary(pd.DataFrame.from_records(summary))
    assert result.loc[1, "qlike_multiple_of_parent_var"] == pytest.approx(2.5)
    assert result.loc[1, "frobenius_change_percent"] == pytest.approx(-25.0)
    assert result.loc[1, "bw_change_percent"] == pytest.approx(-20.0)
