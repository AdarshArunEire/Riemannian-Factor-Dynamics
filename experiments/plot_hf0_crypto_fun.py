"""Build an exploratory visual gallery from the frozen APP-HF-0 panel.

These are deliberately reader-friendly exploration plots, not inferential
APP-HF-1 results.  They use only the already frozen selected universe and
2024--2025 raw/panel data.  No chart output changes a model or gate.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import leaves_list, linkage
from scipy.spatial.distance import squareform


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))

from rfd.data.crypto import read_binance_kline_zip  # noqa: E402


PANEL = ROOT / "results" / "intermediate" / "hf0_crypto" / "hourly_covariances.npz"
RAW = ROOT / "results" / "raw" / "hf0_crypto" / "archives" / "1m"
OUTPUT = ROOT / "results" / "intermediate" / "hf0_crypto_fun"
VIRIDIS = plt.colormaps["viridis"]


def set_style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 180,
        "font.size": 10,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "grid.alpha": 0.20,
    })


def short(symbol: str) -> str:
    return symbol.removesuffix("USDT")


def load_hourly() -> tuple[pd.DataFrame, np.ndarray, list[str]]:
    if not PANEL.exists():
        raise FileNotFoundError(f"run APP-HF-0 first: {PANEL}")
    with np.load(PANEL) as stored:
        covariances = stored["covariances"]
        hours = pd.to_datetime(stored["hours"], utc=True)
        symbols = [str(value) for value in stored["symbols"]]
        unavailable = stored["missing_or_no_trade_fraction"]
        unchanged = stored["unchanged_close_fraction"]
    diagonal = np.diagonal(covariances, axis1=1, axis2=2)
    standard_deviation = np.sqrt(np.maximum(diagonal, np.finfo(float).tiny))
    denominator = standard_deviation[:, :, None] * standard_deviation[:, None, :]
    correlations = covariances / denominator
    upper = np.triu_indices(covariances.shape[1], k=1)
    eigenvalues = np.linalg.eigvalsh(covariances)
    trace = diagonal.sum(axis=1)
    hourly = pd.DataFrame({
        "hour": hours,
        "date": hours.floor("D"),
        "utc_hour": hours.hour,
        "trace": trace,
        "mean_correlation": correlations[:, upper[0], upper[1]].mean(axis=1),
        "leading_share": eigenvalues[:, -1] / np.maximum(trace, np.finfo(float).tiny),
        "missing_or_no_trade": unavailable,
        "unchanged_close": unchanged,
    })
    return hourly, covariances, symbols


def build_daily(symbols: list[str], *, refresh: bool) -> pd.DataFrame:
    cache = OUTPUT / "asset_daily.csv"
    if cache.exists() and not refresh:
        daily = pd.read_csv(cache, parse_dates=["date"])
        if set(daily["symbol"]) == set(symbols):
            return daily
    rows: list[pd.DataFrame] = []
    for number, symbol in enumerate(symbols, start=1):
        previous_close: float | None = None
        symbol_rows: list[pd.DataFrame] = []
        archives = sorted((RAW / symbol).glob("*.zip"))
        if len(archives) != 24:
            raise ValueError(f"expected 24 monthly archives for {symbol}, found {len(archives)}")
        for archive in archives:
            block = read_binance_kline_zip(archive)
            unchanged = np.zeros(len(block.close), dtype=bool)
            unchanged[1:] = block.close[1:] == block.close[:-1]
            if previous_close is not None:
                unchanged[0] = block.close[0] == previous_close
            previous_close = float(block.close[-1])
            frame = pd.DataFrame({
                "date": block.time.floor("D"),
                "close": block.close,
                "quote_volume": block.quote_volume,
                "trades": block.trades,
                "unchanged": unchanged.astype(int),
                "no_trade": (block.trades <= 0).astype(int),
            })
            grouped = frame.groupby("date", as_index=False).agg(
                close=("close", "last"),
                quote_volume=("quote_volume", "sum"),
                trades=("trades", "sum"),
                unchanged_minutes=("unchanged", "sum"),
                no_trade_minutes=("no_trade", "sum"),
                minutes=("close", "size"),
            )
            symbol_rows.append(grouped)
        combined = pd.concat(symbol_rows, ignore_index=True)
        combined["symbol"] = symbol
        combined["unchanged_fraction"] = combined["unchanged_minutes"] / combined["minutes"]
        combined["no_trade_fraction"] = combined["no_trade_minutes"] / combined["minutes"]
        rows.append(combined)
        print(f"[{number}/{len(symbols)}] summarized {symbol}", flush=True)
    daily = pd.concat(rows, ignore_index=True).sort_values(["symbol", "date"])
    daily["log_return"] = daily.groupby("symbol")["close"].transform(
        lambda values: np.log(values).diff()
    )
    daily["normalized_price"] = daily.groupby("symbol")["close"].transform(
        lambda values: 100.0 * values / values.iloc[0]
    )
    OUTPUT.mkdir(parents=True, exist_ok=True)
    daily.to_csv(cache, index=False)
    return daily


def summarize_assets(daily: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for symbol, group in daily.groupby("symbol", sort=False):
        returns = group["log_return"].dropna()
        rows.append({
            "symbol": symbol,
            "annualized_volatility_percent": 100 * np.sqrt(365) * returns.std(ddof=1),
            "total_return_percent": 100 * (group["close"].iloc[-1] / group["close"].iloc[0] - 1),
            "median_daily_quote_volume": group["quote_volume"].median(),
            "unchanged_minute_percent": 100 * group["unchanged_fraction"].mean(),
            "no_trade_minute_percent": 100 * group["no_trade_fraction"].mean(),
        })
    return pd.DataFrame(rows)


def save(fig: plt.Figure, name: str) -> Path:
    path = OUTPUT / name
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def plot_rollercoaster(daily: pd.DataFrame) -> Path:
    fig, ax = plt.subplots(figsize=(13, 7))
    symbols = list(daily["symbol"].drop_duplicates())
    for index, symbol in enumerate(symbols):
        group = daily.loc[daily["symbol"] == symbol]
        ax.plot(
            group["date"], group["normalized_price"],
            color=VIRIDIS((index + 1) / (len(symbols) + 1)),
            linewidth=1.0, alpha=0.78, label=short(symbol),
        )
    basket = daily.groupby("date", as_index=False)["normalized_price"].mean()
    ax.plot(
        basket["date"], basket["normalized_price"],
        color="#111111", linewidth=3.0, label="equal-weight basket",
    )
    ax.axhline(100, color="#777777", linestyle=":", linewidth=1)
    ax.set_yscale("log")
    ax.set_title("Twenty coins enter. Nobody stays at 100.")
    ax.set_ylabel("value of 100 at the start (log scale)")
    ax.set_xlabel("")
    ax.legend(ncol=7, fontsize=7.5, loc="upper center", bbox_to_anchor=(0.5, -0.10))
    fig.autofmt_xdate()
    return save(fig, "01_twenty_coin_rollercoaster.png")


def plot_volatility_race(summary: pd.DataFrame) -> Path:
    ordered = summary.sort_values("annualized_volatility_percent")
    colors = VIRIDIS(np.linspace(0.15, 0.95, len(ordered)))
    y = np.arange(len(ordered))
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.hlines(y, 0, ordered["annualized_volatility_percent"], color=colors, linewidth=3)
    ax.scatter(ordered["annualized_volatility_percent"], y, color=colors, s=65, zorder=3)
    ax.set_yticks(y, [short(value) for value in ordered["symbol"]])
    ax.set_xlim(left=0)
    ax.set_xlabel("annualized volatility of daily log returns")
    ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
    ax.set_title("The volatility Olympics")
    return save(fig, "02_volatility_olympics.png")


def plot_market_heartbeat(hourly: pd.DataFrame) -> Path:
    pivot = hourly.pivot(index="utc_hour", columns="date", values="trace")
    values = np.log10(np.maximum(pivot.to_numpy(), np.finfo(float).tiny))
    dates = pd.DatetimeIndex(pivot.columns)
    fig, ax = plt.subplots(figsize=(15, 5.5))
    image = ax.imshow(values, aspect="auto", origin="lower", cmap="viridis")
    tick_locations = np.linspace(0, len(dates) - 1, 9).astype(int)
    ax.set_xticks(tick_locations, [dates[index].strftime("%b %Y") for index in tick_locations])
    ax.set_yticks([0, 4, 8, 12, 16, 20, 23])
    ax.set_ylabel("UTC hour")
    ax.set_xlabel("")
    ax.set_title("The market never sleeps, but it definitely has moods")
    colorbar = fig.colorbar(image, ax=ax, pad=0.012)
    colorbar.set_label("log10 hourly covariance trace")
    return save(fig, "03_market_heartbeat.png")


def plot_correlation_weather(hourly: pd.DataFrame) -> Path:
    daily = hourly.groupby("date", as_index=False).agg(
        mean_correlation=("mean_correlation", "median"),
        leading_share=("leading_share", "median"),
    )
    smooth_correlation = daily["mean_correlation"].rolling(14, center=True, min_periods=5).median()
    smooth_share = daily["leading_share"].rolling(14, center=True, min_periods=5).median()
    fig, axes = plt.subplots(2, 1, figsize=(13, 7), sharex=True)
    axes[0].plot(daily["date"], daily["mean_correlation"], color="#9e9e9e", alpha=0.35, linewidth=0.7)
    axes[0].plot(daily["date"], smooth_correlation, color=VIRIDIS(0.25), linewidth=2.2)
    axes[0].axhline(0, color="#555555", linewidth=0.8)
    axes[0].set_ylabel("average correlation")
    axes[0].set_title("When twenty coins become one big trade")
    axes[1].plot(daily["date"], daily["leading_share"], color="#9e9e9e", alpha=0.35, linewidth=0.7)
    axes[1].plot(daily["date"], smooth_share, color=VIRIDIS(0.78), linewidth=2.2)
    axes[1].set_ylabel("largest eigenvalue / trace")
    axes[1].yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    axes[1].set_xlabel("")
    fig.autofmt_xdate()
    return save(fig, "04_correlation_weather.png")


def plot_correlation_family(daily: pd.DataFrame) -> Path:
    returns = daily.pivot(index="date", columns="symbol", values="log_return").dropna()
    correlation = returns.corr()
    distance = np.clip(1.0 - correlation.to_numpy(), 0.0, 2.0)
    np.fill_diagonal(distance, 0.0)
    order = leaves_list(linkage(squareform(distance, checks=False), method="average"))
    ordered = correlation.iloc[order, order]
    labels = [short(value) for value in ordered.columns]
    fig, ax = plt.subplots(figsize=(10, 9))
    image = ax.imshow(ordered, vmin=-1, vmax=1, cmap="RdBu_r")
    ax.set_xticks(np.arange(len(labels)), labels, rotation=55, ha="right")
    ax.set_yticks(np.arange(len(labels)), labels)
    ax.grid(False)
    ax.set_title("The crypto family photo: who actually moves together?")
    colorbar = fig.colorbar(image, ax=ax, shrink=0.82)
    colorbar.set_label("daily-return correlation")
    return save(fig, "05_crypto_family_photo.png")


def plot_stillness_chaos(summary: pd.DataFrame) -> Path:
    volume = np.log10(summary["median_daily_quote_volume"])
    sizes = 80 + 360 * (volume - volume.min()) / max(volume.max() - volume.min(), 1e-12)
    returns = summary["total_return_percent"].to_numpy()
    maximum = max(abs(float(returns.min())), abs(float(returns.max())), 1.0)
    norm = TwoSlopeNorm(vmin=-maximum, vcenter=0.0, vmax=maximum)
    fig, ax = plt.subplots(figsize=(11, 8))
    points = ax.scatter(
        summary["annualized_volatility_percent"],
        summary["unchanged_minute_percent"],
        s=sizes, c=returns, cmap="PiYG", norm=norm,
        alpha=0.82, edgecolor="white", linewidth=0.8,
    )
    for row in summary.itertuples():
        ax.annotate(
            short(row.symbol),
            (row.annualized_volatility_percent, row.unchanged_minute_percent),
            xytext=(4, 4), textcoords="offset points", fontsize=8,
        )
    ax.set_xlabel("annualized daily volatility")
    ax.set_ylabel("minutes with an unchanged close")
    ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
    ax.set_title("Chaos versus stillness (bubble size = trading volume)")
    colorbar = fig.colorbar(points, ax=ax, pad=0.02)
    colorbar.set_label("two-year price return (%)")
    return save(fig, "06_chaos_versus_stillness.png")


def plot_money_river(daily: pd.DataFrame, hourly: pd.DataFrame) -> Path:
    turnover = daily.groupby("date", as_index=False)["quote_volume"].sum()
    covariance = hourly.groupby("date", as_index=False)["trace"].median()
    turnover["smooth"] = turnover["quote_volume"].rolling(14, center=True, min_periods=5).median()
    covariance["smooth"] = covariance["trace"].rolling(14, center=True, min_periods=5).median()
    fig, axes = plt.subplots(2, 1, figsize=(13, 7), sharex=True)
    axes[0].fill_between(
        turnover["date"], turnover["quote_volume"] / 1e9,
        color=VIRIDIS(0.75), alpha=0.20,
    )
    axes[0].plot(turnover["date"], turnover["smooth"] / 1e9, color=VIRIDIS(0.75), linewidth=2)
    axes[0].set_ylabel("daily turnover (billion USDT)")
    axes[0].set_title("Money arrives; covariance wakes up")
    axes[1].plot(covariance["date"], covariance["trace"], color="#9e9e9e", alpha=0.30, linewidth=0.7)
    axes[1].plot(covariance["date"], covariance["smooth"], color=VIRIDIS(0.25), linewidth=2)
    axes[1].set_ylabel("median hourly covariance trace")
    axes[1].set_xlabel("")
    fig.autofmt_xdate()
    return save(fig, "07_money_and_covariance.png")


def build_gallery(paths: list[Path]) -> Path:
    chosen = paths[:6]
    fig, axes = plt.subplots(3, 2, figsize=(18, 17))
    for ax, path in zip(axes.flat, chosen, strict=True):
        ax.imshow(plt.imread(path))
        ax.axis("off")
    fig.suptitle("APP-HF-0: an unserious gallery of a serious dataset", fontsize=22, fontweight="bold")
    fig.subplots_adjust(wspace=0.02, hspace=0.07, top=0.96)
    return save(fig, "00_crypto_fun_gallery.png")


def write_fun_facts(daily: pd.DataFrame, hourly: pd.DataFrame, summary: pd.DataFrame) -> None:
    best = summary.loc[summary["total_return_percent"].idxmax()]
    worst = summary.loc[summary["total_return_percent"].idxmin()]
    wildest = summary.loc[summary["annualized_volatility_percent"].idxmax()]
    stillest = summary.loc[summary["unchanged_minute_percent"].idxmax()]
    panic = hourly.loc[hourly["mean_correlation"].idxmax()]
    fire = hourly.loc[hourly["trace"].idxmax()]
    lines = [
        "# APP-HF-0 fun facts",
        "",
        "Exploratory descriptions only; none is an APP-HF-1 model result.",
        "",
        f"- largest two-year price return: **{short(best.symbol)}**, {best.total_return_percent:+.1f}%",
        f"- smallest two-year price return: **{short(worst.symbol)}**, {worst.total_return_percent:+.1f}%",
        f"- highest annualized daily volatility: **{short(wildest.symbol)}**, {wildest.annualized_volatility_percent:.1f}%",
        f"- most unchanged minute closes: **{short(stillest.symbol)}**, {stillest.unchanged_minute_percent:.1f}%",
        f"- highest hourly average correlation: **{panic['mean_correlation']:.3f}** at {panic['hour']}",
        f"- highest hourly covariance trace: **{fire['trace']:.3g}** at {fire['hour']}",
        f"- selected assets: {daily['symbol'].nunique()}",
        f"- calendar days: {daily['date'].nunique()}",
        f"- hourly covariance matrices: {len(hourly):,}",
    ]
    (OUTPUT / "fun_facts.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="rebuild the daily raw-data cache")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    set_style()
    hourly, _, symbols = load_hourly()
    daily = build_daily(symbols, refresh=args.refresh)
    summary = summarize_assets(daily)
    summary.to_csv(OUTPUT / "asset_summary.csv", index=False)
    paths = [
        plot_rollercoaster(daily),
        plot_volatility_race(summary),
        plot_market_heartbeat(hourly),
        plot_correlation_weather(hourly),
        plot_correlation_family(daily),
        plot_stillness_chaos(summary),
        plot_money_river(daily, hourly),
    ]
    gallery = build_gallery(paths)
    write_fun_facts(daily, hourly, summary)
    print(f"Gallery: {gallery}")
    print(f"Individual plots and data: {OUTPUT}")


if __name__ == "__main__":
    main()
