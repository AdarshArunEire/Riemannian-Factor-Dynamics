from __future__ import annotations

from pathlib import Path
import zipfile

import numpy as np
import pandas as pd
import pytest

from experiments.run_hf0_crypto_preflight import (
    CONFIG_DEFAULT,
    audit_panel,
    build_design,
    load_configuration,
    month_labels,
)
from rfd.data.crypto import (
    build_hourly_covariances,
    normalise_binance_timestamps,
    read_binance_kline_zip,
    select_crypto_symbols,
)


def test_frozen_hf0_contract_is_minute_hourly_and_causal() -> None:
    config = load_configuration(CONFIG_DEFAULT)
    pilot = build_design(config, "pilot")
    full = build_design(config, "full")

    assert pilot["raw_interval"] == "1m"
    assert pilot["minutes_per_covariance"] == 60
    assert pilot["matrix_size"] == 20
    assert pilot["tangent_dimension"] == 210
    assert pilot["primary_forecast_horizon_hours"] == 1
    assert pilot["panel_period"] == ["2024-01", "2024-01"]
    assert full["panel_period"] == ["2024-01", "2025-12"]
    assert full["expected_hours"] == 17_544
    assert pd.Timestamp(config["experiment"]["selection_end"]) < pd.Timestamp(
        config["experiment"]["panel_start"]
    )


def test_month_labels_include_both_declared_endpoints() -> None:
    assert month_labels("2024-11-15", "2025-02-01") == [
        "2024-11",
        "2024-12",
        "2025-01",
        "2025-02",
    ]


def test_binance_timestamp_normalisation_handles_2025_unit_switch() -> None:
    expected = pd.to_datetime(
        ["2024-12-31 23:59:00+00:00", "2025-01-01 00:00:00+00:00"]
    )
    mixed = np.array([
        int(expected[0].timestamp() * 1_000),
        int(expected[1].timestamp() * 1_000_000),
    ])

    actual = normalise_binance_timestamps(mixed)

    assert actual.equals(pd.DatetimeIndex(expected))


def test_kline_zip_parser_accepts_headerless_official_shape(tmp_path: Path) -> None:
    timestamps = [1_704_067_200_000, 1_704_067_260_000]
    rows = [
        [timestamps[0], 10, 11, 9, 10.5, 100, timestamps[0] + 59_999,
         1_050, 20, 50, 525, 0],
        [timestamps[1], 10.5, 12, 10, 11.0, 120, timestamps[1] + 59_999,
         1_320, 25, 60, 660, 0],
    ]
    payload = "\n".join(",".join(map(str, row)) for row in rows) + "\n"
    archive = tmp_path / "TESTUSDT-1m-2024-01.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr("TESTUSDT-1m-2024-01.csv", payload)

    block = read_binance_kline_zip(archive)

    assert block.close.tolist() == [10.5, 11.0]
    assert block.quote_volume.tolist() == [1_050.0, 1_320.0]
    assert block.trades.tolist() == [20, 25]
    assert block.time[1] - block.time[0] == pd.Timedelta(minutes=1)


def test_selection_is_liquid_first_then_volatile_and_deterministic() -> None:
    statistics = pd.DataFrame({
        "symbol": ["A", "B", "C", "D", "E"],
        "days": [92, 92, 92, 92, 92],
        "median_quote_volume": [500, 400, 300, 200, 10],
        "daily_volatility": [0.01, 0.02, 0.03, 0.04, 9.0],
    })

    result = select_crypto_symbols(
        statistics,
        minimum_days=80,
        liquidity_pool_size=4,
        selected_assets=2,
    )

    assert set(result.loc[result["selected"], "symbol"]) == {"C", "D"}
    assert not bool(result.set_index("symbol").loc["E", "selected"])
    assert np.isnan(result.set_index("symbol").loc["E", "liquidity_rank"])


def _synthetic_minute_prices(n: int, m: int) -> tuple[pd.DatetimeIndex, np.ndarray, np.ndarray]:
    index = pd.date_range("2024-01-01", periods=n, freq="1min", tz="UTC")
    time = np.arange(n, dtype=float)[:, None]
    asset = np.arange(1, m + 1, dtype=float)[None, :]
    log_price = np.log(100.0 + asset) + 0.0002 * time * asset
    log_price += 0.0001 * np.sin(time / (2.0 + asset))
    prices = np.exp(log_price)
    trades = np.full((n, m), 12.0)
    return index, prices, trades


def test_hourly_covariance_builder_returns_finite_spd_blocks() -> None:
    index, prices, trades = _synthetic_minute_prices(120, 3)

    panel = build_hourly_covariances(
        index,
        prices,
        trades,
        minimum_complete_returns=40,
        relative_eigenvalue_floor=2e-5,
    )

    assert panel.covariances.shape == (2, 3, 3)
    assert panel.complete_returns.tolist() == [59, 60]
    assert np.isfinite(panel.covariances).all()
    assert np.all(panel.minimum_eigenvalue > 0.0)
    assert np.all(panel.condition_number <= 1e6 * (1.0 + 1e-10))
    assert np.all(panel.missing_or_no_trade_fraction == 0.0)
    np.testing.assert_allclose(
        panel.covariances,
        panel.covariances.transpose(0, 2, 1),
        atol=1e-14,
    )


def test_unusable_hour_is_excluded_instead_of_silently_imputed() -> None:
    index, prices, trades = _synthetic_minute_prices(120, 3)
    prices[60:] = np.nan
    trades[60:] = 0.0

    panel = build_hourly_covariances(
        index,
        prices,
        trades,
        maximum_forward_fill_minutes=1,
        minimum_complete_returns=40,
    )

    assert panel.covariances.shape == (1, 3, 3)
    assert panel.hours[0] == np.datetime64("2024-01-01T00:00:00", "ns")


def test_unchanged_traded_close_is_diagnostic_not_missing_data() -> None:
    index, prices, trades = _synthetic_minute_prices(120, 20)
    prices[:, 0] = prices[0, 0]
    panel = build_hourly_covariances(
        index,
        prices,
        trades,
        minimum_complete_returns=40,
        relative_eigenvalue_floor=2e-5,
    )

    assert np.all(panel.missing_or_no_trade_fraction == 0.0)
    assert np.all(panel.unchanged_close_fraction > 0.04)

    config = load_configuration(CONFIG_DEFAULT)
    summary, _, _, _ = audit_panel(
        config,
        panel,
        pd.DataFrame({"coverage": [1.0] * 20}),
        expected_hours=2,
    )
    assert summary["gates"]["availability"]
    assert summary["p99_missing_or_no_trade_fraction"] == 0.0
    assert summary["p99_unchanged_close_fraction"] > 0.04


def test_hourly_builder_rejects_rank_deficient_return_count_contract() -> None:
    index, prices, trades = _synthetic_minute_prices(60, 3)

    with pytest.raises(ValueError, match="must exceed asset count"):
        build_hourly_covariances(
            index,
            prices,
            trades,
            minimum_complete_returns=3,
        )


def test_zero_constructible_hours_produce_boundary_instead_of_crash() -> None:
    config = load_configuration(CONFIG_DEFAULT)
    index, prices, trades = _synthetic_minute_prices(60, 20)
    prices[:] = np.nan
    trades[:] = 0.0
    panel = build_hourly_covariances(
        index,
        prices,
        trades,
        minimum_complete_returns=40,
    )

    summary, diagnostics, _, _ = audit_panel(
        config,
        panel,
        pd.DataFrame({"coverage": [0.0] * 20}),
        expected_hours=1,
    )

    assert summary["verdict"] == "BOUNDARY"
    assert summary["hours_constructed"] == 0
    assert summary["maximum_condition_number"] is None
    assert not summary["gates"]["finite_spd"]
    assert diagnostics.empty
