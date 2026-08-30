"""Binance minute-bar construction for APP-HF-0.

The functions in this module are deliberately source-agnostic after parsing:
they accept aligned minute prices/trade counts and return non-overlapping
hourly sample covariances plus the data-quality quantities consumed by the
APP-HF-0 gate.  Network access, caching, and checksums live in the experiment
runner so unit tests never depend on an exchange endpoint.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import zipfile

import numpy as np
import pandas as pd


Array = np.ndarray
KLINE_COLUMNS = (
    "open_time", "open", "high", "low", "close", "volume", "close_time",
    "quote_volume", "trades", "taker_base", "taker_quote", "ignore",
)


@dataclass(frozen=True)
class KlineBlock:
    """One symbol's parsed Binance kline block."""

    time: pd.DatetimeIndex
    close: Array
    quote_volume: Array
    trades: Array


@dataclass(frozen=True)
class HourlyCovariancePanel:
    """Hourly realised covariances and their construction diagnostics."""

    covariances: Array
    hours: Array
    complete_returns: Array
    missing_fraction: Array
    missing_or_no_trade_fraction: Array
    unchanged_close_fraction: Array
    ridge: Array
    minimum_eigenvalue: Array
    maximum_eigenvalue: Array
    condition_number: Array
    split_half_relative_frobenius: Array


def normalise_binance_timestamps(values: Array) -> pd.DatetimeIndex:
    """Convert Binance millisecond or microsecond epochs to UTC timestamps.

    Binance spot archive timestamps changed from milliseconds to microseconds
    on 2025-01-01.  Mixed-unit input is supported row by row so a concatenated
    panel cannot silently jump by a factor of one thousand.
    """
    raw = np.asarray(values, dtype=np.int64)
    milliseconds = raw < 100_000_000_000_000
    nanoseconds = np.empty_like(raw)
    nanoseconds[milliseconds] = raw[milliseconds] * 1_000_000
    nanoseconds[~milliseconds] = raw[~milliseconds] * 1_000
    return pd.to_datetime(nanoseconds, unit="ns", utc=True)


def read_binance_kline_zip(path: str | Path) -> KlineBlock:
    """Read one official Binance monthly kline zip with strict columns."""
    archive = Path(path)
    with zipfile.ZipFile(archive) as handle:
        members = [name for name in handle.namelist() if not name.endswith("/")]
        if len(members) != 1:
            raise ValueError(f"expected one CSV member in {archive}, found {members}")
        with handle.open(members[0]) as stream:
            frame = pd.read_csv(stream, header=None, names=KLINE_COLUMNS)
    if frame.empty:
        raise ValueError(f"empty kline archive: {archive}")
    # Some recent archive files include a header row despite the historical
    # files being headerless.  Coercion and this mask support both formats.
    open_time = pd.to_numeric(frame["open_time"], errors="coerce")
    keep = open_time.notna()
    frame = frame.loc[keep]
    open_time = open_time.loc[keep].astype(np.int64)
    if frame.empty:
        raise ValueError(f"no numeric kline rows in {archive}")
    result = KlineBlock(
        time=normalise_binance_timestamps(open_time.to_numpy()),
        close=pd.to_numeric(frame["close"], errors="raise").to_numpy(float),
        quote_volume=pd.to_numeric(
            frame["quote_volume"], errors="raise"
        ).to_numpy(float),
        trades=pd.to_numeric(frame["trades"], errors="raise").to_numpy(np.int64),
    )
    if not result.time.is_monotonic_increasing or result.time.has_duplicates:
        raise ValueError(f"kline timestamps are not unique and increasing: {archive}")
    if np.any(result.close <= 0.0) or not np.isfinite(result.close).all():
        raise ValueError(f"nonpositive or nonfinite close in {archive}")
    return result


def select_crypto_symbols(
    statistics: pd.DataFrame,
    *,
    minimum_days: int,
    liquidity_pool_size: int,
    selected_assets: int,
) -> pd.DataFrame:
    """Apply the frozen liquid-first, volatile-second pre-sample rule."""
    required = {"symbol", "days", "median_quote_volume", "daily_volatility"}
    missing = required - set(statistics.columns)
    if missing:
        raise ValueError(f"selection statistics missing columns: {sorted(missing)}")
    if not 0 < selected_assets <= liquidity_pool_size:
        raise ValueError("selected_assets must be positive and no larger than pool")
    frame = statistics.copy()
    frame["eligible"] = (
        (frame["days"] >= int(minimum_days))
        & np.isfinite(frame["median_quote_volume"])
        & (frame["median_quote_volume"] > 0.0)
        & np.isfinite(frame["daily_volatility"])
        & (frame["daily_volatility"] > 0.0)
    )
    eligible = frame.loc[frame["eligible"]].sort_values(
        ["median_quote_volume", "symbol"], ascending=[False, True]
    )
    if len(eligible) < selected_assets:
        raise ValueError(
            f"only {len(eligible)} eligible symbols for {selected_assets} slots"
        )
    pool = eligible.head(min(int(liquidity_pool_size), len(eligible))).copy()
    pool["liquidity_rank"] = np.arange(1, len(pool) + 1)
    pool = pool.sort_values(
        ["daily_volatility", "median_quote_volume", "symbol"],
        ascending=[False, False, True],
    )
    selected_symbols = set(pool.head(int(selected_assets))["symbol"])
    frame["liquidity_rank"] = frame["symbol"].map(
        pool.set_index("symbol")["liquidity_rank"]
    )
    frame["selected"] = frame["symbol"].isin(selected_symbols)
    return frame.sort_values(
        ["selected", "daily_volatility", "median_quote_volume", "symbol"],
        ascending=[False, False, False, True],
    ).reset_index(drop=True)


def _regularise_covariance(covariance: Array, relative_floor: float) -> tuple[Array, float]:
    covariance = 0.5 * (covariance + covariance.T)
    eigenvalues = np.linalg.eigvalsh(covariance)
    scale = float(np.trace(covariance) / covariance.shape[0])
    target = float(relative_floor) * max(scale, np.finfo(float).tiny)
    ridge = max(0.0, target - float(eigenvalues[0]))
    return covariance + ridge * np.eye(covariance.shape[0]), ridge


def build_hourly_covariances(
    minute_index: pd.DatetimeIndex,
    close_prices: Array,
    trade_counts: Array,
    *,
    returns_scale: float = 100.0,
    maximum_forward_fill_minutes: int = 5,
    minimum_complete_returns: int = 40,
    relative_eigenvalue_floor: float = 1e-6,
) -> HourlyCovariancePanel:
    """Build non-overlapping hourly covariance proxies from minute closes.

    Prices are reindexed before this function.  Missing prices may be carried
    forward for at most ``maximum_forward_fill_minutes``.  An intrahour return
    is used only when all assets are finite. Missing/no-trade bars and unchanged
    consecutive closes are recorded separately: the former is the availability
    gate, while the latter is a zero-return/proxy-resolution diagnostic.
    """
    index = pd.DatetimeIndex(minute_index)
    prices = np.asarray(close_prices, dtype=float)
    trades = np.asarray(trade_counts, dtype=float)
    if index.tz is None:
        raise ValueError("minute_index must be timezone-aware")
    if prices.ndim != 2 or prices.shape != trades.shape:
        raise ValueError("close_prices and trade_counts must share shape (n, m)")
    if prices.shape[0] != len(index) or prices.shape[1] < 2:
        raise ValueError("minute array shape does not match index")
    if not index.is_monotonic_increasing or index.has_duplicates:
        raise ValueError("minute_index must be unique and increasing")
    if minimum_complete_returns <= prices.shape[1]:
        raise ValueError("minimum_complete_returns must exceed asset count")
    if relative_eigenvalue_floor <= 0.0:
        raise ValueError("relative_eigenvalue_floor must be positive")

    price_frame = pd.DataFrame(prices, index=index)
    filled = price_frame.ffill(limit=int(maximum_forward_fill_minutes))
    filled_values = filled.to_numpy(float)
    log_prices = np.log(filled_values)
    returns = np.empty_like(log_prices)
    returns[0] = np.nan
    returns[1:] = float(returns_scale) * np.diff(log_prices, axis=0)

    raw_missing = ~np.isfinite(prices)
    unchanged = np.zeros_like(raw_missing)
    unchanged[1:] = np.isclose(filled_values[1:], filled_values[:-1], rtol=0.0, atol=0.0)
    missing_or_no_trade = raw_missing | (trades <= 0.0)

    hour_keys = index.floor("h")
    unique_hours = hour_keys.unique()
    covariances: list[Array] = []
    hours: list[np.datetime64] = []
    complete_counts: list[int] = []
    missing_fractions: list[float] = []
    missing_or_no_trade_fractions: list[float] = []
    unchanged_close_fractions: list[float] = []
    ridges: list[float] = []
    min_eigenvalues: list[float] = []
    max_eigenvalues: list[float] = []
    conditions: list[float] = []
    split_errors: list[float] = []

    for hour in unique_hours:
        mask = np.asarray(hour_keys == hour)
        block = returns[mask]
        complete = np.isfinite(block).all(axis=1)
        used = block[complete]
        if used.shape[0] < int(minimum_complete_returns):
            continue
        covariance = np.cov(used, rowvar=False, ddof=1)
        covariance, ridge = _regularise_covariance(
            covariance, float(relative_eigenvalue_floor)
        )
        eigenvalues = np.linalg.eigvalsh(covariance)
        half = used.shape[0] // 2
        if half > prices.shape[1] and used.shape[0] - half > prices.shape[1]:
            first = np.cov(used[:half], rowvar=False, ddof=1)
            second = np.cov(used[half:], rowvar=False, ddof=1)
            denom = max(float(np.linalg.norm(covariance, ord="fro")), np.finfo(float).tiny)
            split_error = float(np.linalg.norm(first - second, ord="fro") / denom)
        else:
            split_error = np.nan
        covariances.append(covariance)
        hours.append(hour.to_datetime64())
        complete_counts.append(int(used.shape[0]))
        missing_fractions.append(float(raw_missing[mask].mean()))
        missing_or_no_trade_fractions.append(
            float(missing_or_no_trade[mask].mean())
        )
        unchanged_close_fractions.append(float(unchanged[mask].mean()))
        ridges.append(float(ridge))
        min_eigenvalues.append(float(eigenvalues[0]))
        max_eigenvalues.append(float(eigenvalues[-1]))
        conditions.append(float(eigenvalues[-1] / eigenvalues[0]))
        split_errors.append(split_error)

    m = prices.shape[1]
    covariance_array = (
        np.stack(covariances) if covariances else np.empty((0, m, m), dtype=float)
    )
    return HourlyCovariancePanel(
        covariances=covariance_array,
        hours=np.asarray(hours, dtype="datetime64[ns]"),
        complete_returns=np.asarray(complete_counts, dtype=int),
        missing_fraction=np.asarray(missing_fractions, dtype=float),
        missing_or_no_trade_fraction=np.asarray(
            missing_or_no_trade_fractions, dtype=float
        ),
        unchanged_close_fraction=np.asarray(unchanged_close_fractions, dtype=float),
        ridge=np.asarray(ridges, dtype=float),
        minimum_eigenvalue=np.asarray(min_eigenvalues, dtype=float),
        maximum_eigenvalue=np.asarray(max_eigenvalues, dtype=float),
        condition_number=np.asarray(conditions, dtype=float),
        split_half_relative_frobenius=np.asarray(split_errors, dtype=float),
    )
