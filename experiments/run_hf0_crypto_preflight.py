"""APP-HF-0: construct and audit the frozen hourly crypto covariance panel.

The runner has three profiles:

``dry-run``
    Validate and print the immutable design without network access.
``pilot``
    Select assets from 2023-Q4 only, then build one declared 2024 month.
``full``
    Reuse the digest-matched selection and build calendar years 2024--2025.

Raw Binance archives and constructed matrices are gitignored.  The runner
verifies Binance's published SHA-256 files, writes downloads atomically, and
stores a manifest so every matrix can be traced to its source archives.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import time
from typing import Any, Iterable

import numpy as np
import pandas as pd
import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))

from rfd.data.crypto import (  # noqa: E402
    HourlyCovariancePanel,
    build_hourly_covariances,
    read_binance_kline_zip,
    select_crypto_symbols,
)


CONFIG_DEFAULT = ROOT / "config" / "hf0_crypto.yaml"


def load_configuration(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    config["config_path"] = path.resolve()
    validate_configuration(config)
    return config


def validate_configuration(config: dict[str, Any]) -> None:
    experiment = config["experiment"]
    selection = config["selection"]
    construction = config["construction"]
    if experiment["raw_interval"] != "1m":
        raise ValueError("APP-HF-0 protocol is frozen to one-minute klines")
    if experiment["timezone"] != "UTC":
        raise ValueError("APP-HF-0 timestamps must be UTC")
    candidates = tuple(selection["candidate_symbols"])
    if len(candidates) != len(set(candidates)):
        raise ValueError("candidate_symbols must be unique")
    if any(not symbol.endswith(experiment["quote_asset"]) for symbol in candidates):
        raise ValueError("every candidate must use the frozen quote asset")
    if int(selection["selected_assets"]) != 20:
        raise ValueError("Paper 1 APP-HF-0 is frozen to 20 assets")
    if not (
        int(selection["selected_assets"])
        <= int(selection["liquidity_pool_size"])
        <= len(candidates)
    ):
        raise ValueError("selection sizes must satisfy selected <= pool <= candidates")
    if int(construction["minutes_per_covariance"]) != 60:
        raise ValueError("Paper 1 APP-HF-0 is frozen to hourly covariance")
    if int(construction["minimum_complete_returns_per_hour"]) <= 20:
        raise ValueError("complete returns must exceed matrix dimension")
    if float(construction["relative_eigenvalue_floor"]) <= 0.0:
        raise ValueError("relative_eigenvalue_floor must be positive")
    dates = {
        key: pd.Timestamp(experiment[key])
        for key in ("selection_start", "selection_end", "panel_start", "panel_end")
    }
    if dates["selection_start"] > dates["selection_end"]:
        raise ValueError("selection period is reversed")
    if dates["panel_start"] > dates["panel_end"]:
        raise ValueError("panel period is reversed")
    if dates["selection_end"] >= dates["panel_start"]:
        raise ValueError("asset selection must end before the panel begins")
    pilot = pd.Period(config["acquisition"]["pilot_month"], freq="M")
    if not dates["panel_start"].to_period("M") <= pilot <= dates["panel_end"].to_period("M"):
        raise ValueError("pilot month must lie inside the declared panel")


def build_design(config: dict[str, Any], profile: str) -> dict[str, Any]:
    experiment = config["experiment"]
    selection = config["selection"]
    if profile == "pilot":
        panel_months = [config["acquisition"]["pilot_month"]]
    else:
        panel_months = month_labels(experiment["panel_start"], experiment["panel_end"])
    return {
        "experiment_id": experiment["id"],
        "profile": profile,
        "source": "Binance official public-data monthly spot kline archive",
        "quote_asset": experiment["quote_asset"],
        "raw_interval": experiment["raw_interval"],
        "selection_period": [experiment["selection_start"], experiment["selection_end"]],
        "panel_period": [panel_months[0], panel_months[-1]],
        "candidate_count": len(selection["candidate_symbols"]),
        "selected_assets": int(selection["selected_assets"]),
        "selection_rule": (
            f"top {selection['liquidity_pool_size']} by median daily quote volume, "
            f"then top {selection['selected_assets']} by daily volatility"
        ),
        "matrix_size": 20,
        "tangent_dimension": 210,
        "minutes_per_covariance": 60,
        "expected_hours": sum(pd.Period(month).days_in_month * 24 for month in panel_months),
        "primary_forecast_horizon_hours": experiment["primary_forecast_horizon_hours"],
        "sensitivity_horizons_hours": experiment["sensitivity_horizons_hours"],
        "scope": "data/proxy preflight only; no centre, factor, rank, or forecast fit",
    }


def month_labels(start: str, end: str) -> list[str]:
    first = pd.Timestamp(start).to_period("M")
    last = pd.Timestamp(end).to_period("M")
    return [str(period) for period in pd.period_range(first, last, freq="M")]


def _selection_digest(config: dict[str, Any]) -> str:
    material = json.dumps(
        {
            "experiment": {
                key: config["experiment"][key]
                for key in ("source", "market", "quote_asset", "selection_start", "selection_end")
            },
            "selection": config["selection"],
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def _atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    temporary.replace(path)


def _atomic_npz(path: Path, **arrays: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp.npz")
    np.savez_compressed(temporary, **arrays)
    temporary.replace(path)


def archive_url(config: dict[str, Any], symbol: str, interval: str, month: str) -> str:
    return (
        f"{config['source']['base_url'].rstrip('/')}/{symbol}/{interval}/"
        f"{symbol}-{interval}-{month}.zip"
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _request(url: str, *, timeout: int, retries: int) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout, stream=True)
            if response.status_code == 404:
                return response
            response.raise_for_status()
            return response
        except requests.RequestException as error:
            last_error = error
            if attempt < retries:
                time.sleep(float(attempt))
    assert last_error is not None
    raise last_error


def download_archive(
    config: dict[str, Any],
    symbol: str,
    interval: str,
    month: str,
    raw_directory: Path,
) -> dict[str, Any]:
    """Download one archive, verify its official checksum, and return manifest data."""
    url = archive_url(config, symbol, interval, month)
    relative = Path(interval) / symbol / f"{symbol}-{interval}-{month}.zip"
    destination = raw_directory / "archives" / relative
    checksum_url = url + str(config["source"]["checksum_suffix"])
    timeout = int(config["acquisition"]["timeout_seconds"])
    retries = int(config["acquisition"]["retries"])
    checksum_response = _request(checksum_url, timeout=timeout, retries=retries)
    if checksum_response.status_code == 404:
        return {
            "symbol": symbol, "interval": interval, "month": month,
            "url": url, "status": "missing", "path": "", "bytes": 0,
            "sha256": "", "expected_sha256": "",
        }
    checksum_text = checksum_response.content.decode("utf-8").strip()
    expected = checksum_text.split()[0].lower()
    if len(expected) != 64:
        raise ValueError(f"invalid checksum response for {url}: {checksum_text!r}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and _sha256(destination) == expected:
        return {
            "symbol": symbol, "interval": interval, "month": month,
            "url": url, "status": "cached", "path": str(destination.relative_to(ROOT)),
            "bytes": destination.stat().st_size, "sha256": expected,
            "expected_sha256": expected,
        }
    response = _request(url, timeout=timeout, retries=retries)
    if response.status_code == 404:
        return {
            "symbol": symbol, "interval": interval, "month": month,
            "url": url, "status": "missing", "path": "", "bytes": 0,
            "sha256": "", "expected_sha256": expected,
        }
    temporary = destination.with_suffix(destination.suffix + ".part")
    with temporary.open("wb") as handle:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                handle.write(chunk)
    actual = _sha256(temporary)
    if actual != expected:
        temporary.unlink(missing_ok=True)
        raise ValueError(f"checksum mismatch for {url}: {actual} != {expected}")
    temporary.replace(destination)
    return {
        "symbol": symbol, "interval": interval, "month": month,
        "url": url, "status": "downloaded", "path": str(destination.relative_to(ROOT)),
        "bytes": destination.stat().st_size, "sha256": actual,
        "expected_sha256": expected,
    }


def ensure_archives(
    config: dict[str, Any],
    requests_: Iterable[tuple[str, str, str]],
    raw_directory: Path,
) -> list[dict[str, Any]]:
    jobs = list(dict.fromkeys(requests_))
    records: list[dict[str, Any]] = []
    workers = int(config["acquisition"]["workers"])
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(download_archive, config, symbol, interval, month, raw_directory):
            (symbol, interval, month)
            for symbol, interval, month in jobs
        }
        for index, future in enumerate(as_completed(futures), start=1):
            record = future.result()
            records.append(record)
            print(
                f"[{index}/{len(jobs)}] {record['symbol']} {record['interval']} "
                f"{record['month']}: {record['status']}",
                flush=True,
            )
    return sorted(records, key=lambda row: (row["interval"], row["symbol"], row["month"]))


def _path_from_record(record: dict[str, Any]) -> Path | None:
    return ROOT / record["path"] if record["path"] else None


def build_selection(
    config: dict[str, Any], raw_directory: Path
) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    experiment = config["experiment"]
    candidates = list(config["selection"]["candidate_symbols"])
    months = month_labels(experiment["selection_start"], experiment["selection_end"])
    manifest = ensure_archives(
        config,
        ((symbol, "1d", month) for symbol in candidates for month in months),
        raw_directory,
    )
    lookup = {(row["symbol"], row["month"]): row for row in manifest}
    rows: list[dict[str, Any]] = []
    start = pd.Timestamp(experiment["selection_start"], tz="UTC")
    end = pd.Timestamp(experiment["selection_end"], tz="UTC") + pd.Timedelta(days=1)
    for symbol in candidates:
        times: list[pd.DatetimeIndex] = []
        closes: list[np.ndarray] = []
        quote_volumes: list[np.ndarray] = []
        for month in months:
            path = _path_from_record(lookup[(symbol, month)])
            if path is None:
                continue
            block = read_binance_kline_zip(path)
            times.append(block.time)
            closes.append(block.close)
            quote_volumes.append(block.quote_volume)
        if not times:
            rows.append({
                "symbol": symbol, "days": 0, "median_quote_volume": np.nan,
                "daily_volatility": np.nan,
            })
            continue
        time = times[0].append(times[1:]) if len(times) > 1 else times[0]
        close = np.concatenate(closes)
        quote_volume = np.concatenate(quote_volumes)
        keep = (time >= start) & (time < end)
        close = close[keep]
        quote_volume = quote_volume[keep]
        daily_returns = np.diff(np.log(close)) if close.size > 1 else np.array([])
        rows.append({
            "symbol": symbol,
            "days": int(close.size),
            "median_quote_volume": float(np.median(quote_volume)) if close.size else np.nan,
            "daily_volatility": float(np.std(daily_returns, ddof=1))
            if daily_returns.size > 1 else np.nan,
        })
    selected = select_crypto_symbols(
        pd.DataFrame(rows),
        minimum_days=int(config["selection"]["minimum_selection_days"]),
        liquidity_pool_size=int(config["selection"]["liquidity_pool_size"]),
        selected_assets=int(config["selection"]["selected_assets"]),
    )
    return selected, manifest


def freeze_or_load_selection(
    config: dict[str, Any], raw_directory: Path
) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    path = raw_directory / "selection.json"
    digest = _selection_digest(config)
    if path.exists():
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("digest") != digest:
            raise RuntimeError(
                "frozen asset selection does not match config; remove it only after "
                "declaring a new protocol amendment"
            )
        print("reusing digest-matched frozen asset selection", flush=True)
        return pd.DataFrame(payload["statistics"]), payload.get("manifest", [])
    statistics, manifest = build_selection(config, raw_directory)
    selected = statistics.loc[statistics["selected"], "symbol"].tolist()
    _atomic_json(path, {
        "digest": digest,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "selection_period": [
            config["experiment"]["selection_start"],
            config["experiment"]["selection_end"],
        ],
        "selected_symbols": selected,
        "statistics": json.loads(statistics.to_json(orient="records")),
        "manifest": manifest,
    })
    print(f"froze selected symbols: {', '.join(selected)}", flush=True)
    return statistics, manifest


def _month_bounds(month: str) -> tuple[pd.Timestamp, pd.Timestamp, pd.DatetimeIndex]:
    period = pd.Period(month, freq="M")
    start = period.start_time.tz_localize("UTC")
    stop = (period + 1).start_time.tz_localize("UTC")
    return start, stop, pd.date_range(start, stop, freq="1min", inclusive="left")


def _aligned_month(
    symbols: list[str],
    month: str,
    lookup: dict[tuple[str, str], dict[str, Any]],
) -> tuple[pd.DatetimeIndex, np.ndarray, np.ndarray, list[dict[str, Any]]]:
    _, _, index = _month_bounds(month)
    prices = np.full((len(index), len(symbols)), np.nan)
    trades = np.full_like(prices, np.nan)
    coverage: list[dict[str, Any]] = []
    for column, symbol in enumerate(symbols):
        record = lookup[(symbol, month)]
        path = _path_from_record(record)
        if path is None:
            coverage.append({"month": month, "symbol": symbol, "coverage": 0.0})
            continue
        block = read_binance_kline_zip(path)
        frame = pd.DataFrame(
            {"close": block.close, "trades": block.trades}, index=block.time
        ).reindex(index)
        prices[:, column] = frame["close"].to_numpy(float)
        trades[:, column] = frame["trades"].to_numpy(float)
        coverage.append({
            "month": month,
            "symbol": symbol,
            "coverage": float(frame["close"].notna().mean()),
        })
    return index, prices, trades, coverage


def _combine_panels(panels: list[HourlyCovariancePanel], m: int) -> HourlyCovariancePanel:
    if not panels:
        raise ValueError("no monthly panels were constructed")
    fields = HourlyCovariancePanel.__dataclass_fields__
    combined: dict[str, np.ndarray] = {}
    for name in fields:
        values = [getattr(panel, name) for panel in panels]
        if name == "covariances":
            combined[name] = np.concatenate(values, axis=0) if values else np.empty((0, m, m))
        else:
            combined[name] = np.concatenate(values)
    order = np.argsort(combined["hours"])
    return HourlyCovariancePanel(**{
        name: value[order] for name, value in combined.items()
    })


def construct_panel(
    config: dict[str, Any],
    symbols: list[str],
    months: list[str],
    raw_directory: Path,
) -> tuple[HourlyCovariancePanel, list[dict[str, Any]], list[dict[str, Any]]]:
    manifest = ensure_archives(
        config,
        ((symbol, "1m", month) for symbol in symbols for month in months),
        raw_directory,
    )
    lookup = {(row["symbol"], row["month"]): row for row in manifest}
    construction = config["construction"]
    panels: list[HourlyCovariancePanel] = []
    coverage: list[dict[str, Any]] = []
    previous_close = np.full(len(symbols), np.nan)
    for index_number, month in enumerate(months, start=1):
        index, prices, trades, month_coverage = _aligned_month(symbols, month, lookup)
        coverage.extend(month_coverage)
        prepend_time = index[0] - pd.Timedelta(minutes=1)
        extended_index = index.insert(0, prepend_time)
        extended_prices = np.vstack([previous_close, prices])
        extended_trades = np.vstack([np.full(len(symbols), np.nan), trades])
        panel = build_hourly_covariances(
            extended_index,
            extended_prices,
            extended_trades,
            returns_scale=float(construction["returns_scale"]),
            maximum_forward_fill_minutes=int(construction["maximum_forward_fill_minutes"]),
            minimum_complete_returns=int(construction["minimum_complete_returns_per_hour"]),
            relative_eigenvalue_floor=float(construction["relative_eigenvalue_floor"]),
        )
        keep = panel.hours >= np.datetime64(index[0].tz_localize(None), "ns")
        panels.append(HourlyCovariancePanel(**{
            name: getattr(panel, name)[keep]
            for name in HourlyCovariancePanel.__dataclass_fields__
        }))
        for column in range(len(symbols)):
            valid = prices[:, column][np.isfinite(prices[:, column])]
            if valid.size:
                previous_close[column] = valid[-1]
        print(
            f"[{index_number}/{len(months)}] built {month}: "
            f"{int(keep.sum())}/{pd.Period(month).days_in_month * 24} hours",
            flush=True,
        )
    return _combine_panels(panels, len(symbols)), coverage, manifest


def _autocorrelation(values: np.ndarray, lag: int) -> float:
    if len(values) <= lag or not np.isfinite(values).all():
        return np.nan
    left, right = values[:-lag], values[lag:]
    if np.std(left) == 0.0 or np.std(right) == 0.0:
        return np.nan
    return float(np.corrcoef(left, right)[0, 1])


def audit_panel(
    config: dict[str, Any],
    panel: HourlyCovariancePanel,
    coverage: pd.DataFrame,
    expected_hours: int,
) -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    covariances = panel.covariances
    traces = np.trace(covariances, axis1=1, axis2=2)
    logdet = np.linalg.slogdet(covariances)[1]
    hours = pd.to_datetime(panel.hours, utc=True)
    diagnostics = pd.DataFrame({
        "hour": hours,
        "complete_returns": panel.complete_returns,
        "missing_fraction": panel.missing_fraction,
        "missing_or_no_trade_fraction": panel.missing_or_no_trade_fraction,
        "unchanged_close_fraction": panel.unchanged_close_fraction,
        "ridge": panel.ridge,
        "minimum_eigenvalue": panel.minimum_eigenvalue,
        "maximum_eigenvalue": panel.maximum_eigenvalue,
        "condition_number": panel.condition_number,
        "trace": traces,
        "logdet": logdet,
        "split_half_relative_frobenius": panel.split_half_relative_frobenius,
    })
    seasonality = diagnostics.assign(
        utc_hour=hours.hour, utc_day_of_week=hours.dayofweek
    ).groupby(["utc_day_of_week", "utc_hour"], as_index=False).agg(
        median_trace=("trace", "median"),
        median_missing_or_no_trade_fraction=(
            "missing_or_no_trade_fraction", "median"
        ),
        median_unchanged_close_fraction=("unchanged_close_fraction", "median"),
        hours=("hour", "size"),
    )
    dependence_rows = []
    for lag in (1, 6, 24, 168):
        dependence_rows.append({
            "lag_hours": lag,
            "trace_autocorrelation": _autocorrelation(traces, lag),
            "logdet_autocorrelation": _autocorrelation(logdet, lag),
        })
    dependence = pd.DataFrame(dependence_rows)
    acceptance = config["acceptance"]
    has_hours = len(covariances) > 0
    selected_count = covariances.shape[1] if covariances.ndim == 3 else 0
    raw_minute_coverage = (
        float(coverage["coverage"].min()) if not coverage.empty else 0.0
    )
    constructible_fraction = float(len(covariances) / expected_hours)
    median_complete = float(np.median(panel.complete_returns)) if has_hours else 0.0
    p99_missing_or_no_trade = float(
        np.quantile(panel.missing_or_no_trade_fraction, 0.99)
    ) if has_hours else 1.0
    p99_unchanged_close = float(
        np.quantile(panel.unchanged_close_fraction, 0.99)
    ) if has_hours else 1.0
    maximum_condition = float(np.max(panel.condition_number)) if has_hours else None
    finite_spd = bool(
        covariances.size
        and np.isfinite(covariances).all()
        and np.all(panel.minimum_eigenvalue > 0.0)
    )
    gates = {
        "selected_assets": selected_count >= int(acceptance["minimum_selected_assets"]),
        "raw_minute_coverage": raw_minute_coverage >= float(acceptance["minimum_raw_minute_coverage"]),
        "constructible_hours": constructible_fraction >= float(acceptance["minimum_constructible_hour_fraction"]),
        "complete_returns": median_complete >= float(acceptance["minimum_median_complete_returns"]),
        "availability": p99_missing_or_no_trade <= float(
            acceptance["maximum_p99_missing_or_no_trade_fraction"]
        ),
        "finite_spd": finite_spd,
        "conditioning": bool(
            has_hours
            and maximum_condition is not None
            and maximum_condition
            <= float(acceptance["maximum_condition_number"]) * (1.0 + 1e-10)
        ),
    }
    finite_split = panel.split_half_relative_frobenius[
        np.isfinite(panel.split_half_relative_frobenius)
    ]
    summary = {
        "verdict": "PASS" if all(gates.values()) else "BOUNDARY",
        "gates": gates,
        "hours_constructed": int(len(covariances)),
        "expected_hours": int(expected_hours),
        "constructible_hour_fraction": constructible_fraction,
        "minimum_asset_month_coverage": raw_minute_coverage,
        "median_complete_returns": median_complete,
        "p99_missing_or_no_trade_fraction": p99_missing_or_no_trade,
        "p99_unchanged_close_fraction": p99_unchanged_close,
        "ridge_activation_fraction": float(np.mean(panel.ridge > 0.0)) if has_hours else 0.0,
        "minimum_eigenvalue": float(np.min(panel.minimum_eigenvalue)) if has_hours else None,
        "maximum_condition_number": maximum_condition,
        "median_condition_number": float(np.median(panel.condition_number))
        if has_hours else None,
        "median_split_half_relative_frobenius": float(np.median(finite_split))
        if finite_split.size else None,
        "trace_median": float(np.median(traces)) if has_hours else None,
    }
    return summary, diagnostics, seasonality, dependence


def write_outputs(
    config: dict[str, Any],
    profile: str,
    design: dict[str, Any],
    selection: pd.DataFrame,
    manifest: list[dict[str, Any]],
    coverage: list[dict[str, Any]],
    panel: HourlyCovariancePanel,
) -> Path:
    output_key = "pilot_directory" if profile == "pilot" else "full_directory"
    output = ROOT / config["output"][output_key]
    output.mkdir(parents=True, exist_ok=True)
    prior_summary = output / "summary.json"
    if prior_summary.exists():
        prior = json.loads(prior_summary.read_text(encoding="utf-8"))
        if prior.get("verdict") == "BOUNDARY" and "p99_stale_fraction" in prior:
            for name in ("report.md", "summary.json", "design.json"):
                source = output / name
                destination = output / f"{Path(name).stem}.pre-metric-correction-2026-08-27{Path(name).suffix}"
                if source.exists() and not destination.exists():
                    shutil.copy2(source, destination)
    coverage_frame = pd.DataFrame(coverage)
    summary, diagnostics, seasonality, dependence = audit_panel(
        config, panel, coverage_frame, int(design["expected_hours"])
    )
    _atomic_json(output / "design.json", design)
    _atomic_json(output / "summary.json", summary)
    selection.to_csv(output / "selection.csv", index=False)
    pd.DataFrame(manifest).to_csv(output / "manifest.csv", index=False)
    coverage_frame.to_csv(output / "coverage.csv", index=False)
    diagnostics.to_csv(output / "hourly_diagnostics.csv", index=False)
    seasonality.to_csv(output / "seasonality.csv", index=False)
    dependence.to_csv(output / "dependence.csv", index=False)
    selected_symbols = selection.loc[selection["selected"], "symbol"].to_numpy(str)
    _atomic_npz(
        output / "hourly_covariances.npz",
        covariances=panel.covariances,
        hours=panel.hours,
        symbols=selected_symbols,
        complete_returns=panel.complete_returns,
        missing_or_no_trade_fraction=panel.missing_or_no_trade_fraction,
        unchanged_close_fraction=panel.unchanged_close_fraction,
        ridge=panel.ridge,
        minimum_eigenvalue=panel.minimum_eigenvalue,
        condition_number=panel.condition_number,
    )
    def display(value: float | None, format_specification: str) -> str:
        return "not available" if value is None else format(value, format_specification)

    report = [
        "# APP-HF-0 crypto data/proxy preflight",
        "",
        f"- generated UTC: {datetime.now(timezone.utc).isoformat()}",
        f"- profile: {profile}",
        f"- verdict: **{summary['verdict']}**",
        f"- selected symbols: {', '.join(selected_symbols)}",
        f"- constructed hours: {summary['hours_constructed']}/{summary['expected_hours']} "
        f"({100 * summary['constructible_hour_fraction']:.2f}%)",
        f"- minimum asset-month raw coverage: {100 * summary['minimum_asset_month_coverage']:.2f}%",
        f"- median complete returns/hour: {summary['median_complete_returns']:.1f}/60",
        f"- 99th percentile missing-or-no-trade fraction: "
        f"{100 * summary['p99_missing_or_no_trade_fraction']:.2f}%",
        f"- 99th percentile unchanged-close fraction: "
        f"{100 * summary['p99_unchanged_close_fraction']:.2f}%",
        f"- median / maximum condition: "
        f"{display(summary['median_condition_number'], '.3g')} / "
        f"{display(summary['maximum_condition_number'], '.3g')}",
        f"- ridge activation: {100 * summary['ridge_activation_fraction']:.2f}%",
        f"- median split-half proxy disagreement: "
        f"{display(summary['median_split_half_relative_frobenius'], '.3f')}"
        f"× full-covariance Frobenius norm",
        "",
        "## Gate ledger",
        "",
        "| gate | result |",
        "|---|:---:|",
        *[
            f"| {name.replace('_', ' ')} | {'PASS' if passed else 'BOUNDARY'} |"
            for name, passed in summary["gates"].items()
        ],
        "",
        "A BOUNDARY verdict stops APP-HF-1 until its failed data contract is",
        "adjudicated. It does not authorise replacing assets or changing the",
        "period after inspecting centre or forecast results.",
    ]
    (output / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    parser.add_argument("--profile", choices=("dry-run", "selection", "pilot", "full"), default="dry-run")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_configuration(args.config.resolve())
    design_profile = "pilot" if args.profile == "pilot" else "full"
    design = build_design(config, design_profile)
    print(json.dumps(design, indent=2), flush=True)
    if args.profile == "dry-run":
        print("APP-HF-0 dry run passed; no network request was made.")
        return
    raw_directory = ROOT / config["output"]["raw_directory"]
    selection, selection_manifest = freeze_or_load_selection(config, raw_directory)
    selected_symbols = selection.loc[selection["selected"], "symbol"].tolist()
    if args.profile == "selection":
        print(f"selection frozen: {', '.join(selected_symbols)}")
        return
    months = (
        [config["acquisition"]["pilot_month"]]
        if args.profile == "pilot"
        else month_labels(config["experiment"]["panel_start"], config["experiment"]["panel_end"])
    )
    panel, coverage, panel_manifest = construct_panel(
        config, selected_symbols, months, raw_directory
    )
    output = write_outputs(
        config,
        args.profile,
        design,
        selection,
        selection_manifest + panel_manifest,
        coverage,
        panel,
    )
    print(f"APP-HF-0 report: {output / 'report.md'}")
    if json.loads((output / "summary.json").read_text(encoding="utf-8"))["verdict"] != "PASS":
        raise SystemExit("APP-HF-0 reached a declared data/proxy boundary")


if __name__ == "__main__":
    main()
