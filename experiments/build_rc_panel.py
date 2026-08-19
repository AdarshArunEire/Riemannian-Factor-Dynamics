"""B3.4a -- rebuild the 12-asset monthly realised-covariance panel.

Every choice below is taken from the parent's own code, not invented. Sources
in reference/AUDIT.md sections 2 and 9.

    stock_price_extract.ipynb   yf.download(tickers, start="2000-01-01",
                                            end="2024-12-31"); data["Close"]
    Huang, email 2026-08-17     "compute the log returns. Then compute the
                                sample covariance of the log returns in each
                                month."
    sp500_analysis.R:150        dta = dta * 10000   # percentage points
    sp500_analysis.R:146-147    dta = dta[1:240,,]  # 2000-01 .. 2019-12

ONE ASSUMPTION, recorded rather than hidden: `Close` is taken to be the
AUTO-ADJUSTED series. yfinance changed its default and their notebook pins no
version, so which one they got depends on when they ran it. For a 2026 paper
the modern default is the reasonable reading. If a later mismatch looks
dividend-shaped, this is the line to revisit.

Writes the panel to results/raw/ (gitignored -- it is data) and the
measurements to results/final/ (committed -- they are evidence).

    python experiments/build_rc_panel.py
"""

from _common import header, write, ROOT, FINAL

import sys

import numpy as np

from rfd.spd.airm import airm_barycentre, airm_dist2

# Table 3 of arXiv:2607.28385, read DOWN the columns -- i.e. grouped by sector,
# which is what the parent's data file name (sp500_12bySector.RData) says the
# ordering is. Order is not load-bearing for any scalar we compute: BW,
# Frobenius, EWMA and LOCF are all equivariant under a common permutation, so a
# wrong guess here changes heat-map labels and nothing else.
TICKERS = [
    "MSFT", "AAPL", "ORCL", "CSCO",     # technology
    "JPM", "BAC", "WFC", "GS",          # financials
    "XOM", "CVX", "COP", "EOG",         # energy
]

START, END = "2000-01-01", "2024-12-31"     # their download window
N_MONTHS = 240                               # their analysis window: 2000-01..2019-12
SCALE = 10000.0                              # sp500_analysis.R:150
RAW = ROOT / "results" / "raw"


def fetch_prices():
    """One download, BOTH price series.

    auto_adjust=False makes yfinance return `Close` (raw) and `Adj Close`
    (split- and dividend-adjusted) side by side, so we build both panels from
    one call and let the published numbers decide which they used.

    The DOWNLOAD END DATE IS IRRELEVANT and is left at their 2024-12-31 only
    for fidelity. Adjustment applies a constant multiplicative factor per
    ticker across the whole history, and a constant factor cancels exactly in
    log returns -- log(cP_t / cP_{t-1}) = log(P_t / P_{t-1}). A 2026 download
    and a 2024 download give identical returns over 2000-2019. Only raw-vs-
    adjusted moves the numbers, because dividends INSIDE the window are real
    return events.
    """
    try:
        import yfinance as yf
    except ImportError:
        sys.exit("yfinance not installed:  pip install yfinance")

    print(f"yfinance {yf.__version__}", flush=True)
    print(f"downloading {len(TICKERS)} tickers {START} .. {END}", flush=True)
    data = yf.download(TICKERS, start=START, end=END,
                       auto_adjust=False, progress=False)

    fields = set(data.columns.get_level_values(0))
    print(f"fields returned: {sorted(fields)}", flush=True)
    if "Adj Close" not in fields:
        sys.exit("no 'Adj Close' column -- auto_adjust did not stay off; "
                 "check the yfinance version")

    out = {}
    for name, col in (("adjusted", "Adj Close"), ("raw", "Close")):
        px = data[col][TICKERS].dropna(how="all")
        out[name] = px
        print(f"  {name:<9} {px.shape[0]} rows, "
              f"{px.index[0].date()} .. {px.index[-1].date()}", flush=True)
    return out


def monthly_rc(px):
    """Daily log returns -> per-month sample covariance -> x 10000.

    Also returns the daily returns themselves, so a later diagnostic can
    re-slice them (e.g. the day-count sweep in diag_day_count.py) without
    hitting the network again.
    """
    logret = np.log(px).diff().dropna(how="all")

    panel, months, ndays = [], [], []
    ret_rows, ret_month = [], []
    for period, block in logret.groupby(logret.index.to_period("M")):
        r = block.dropna(how="any").to_numpy()
        if r.shape[0] < 2:
            continue
        # np.cov defaults to ddof=1 and demeans -- identical to R's cov()
        panel.append(np.cov(r, rowvar=False) * SCALE)
        months.append(str(period))
        ndays.append(r.shape[0])
        ret_rows.append(r)
        ret_month += [str(period)] * r.shape[0]

    return (np.stack(panel), months, np.array(ndays),
            np.concatenate(ret_rows), np.array(ret_month))


def main():
    series = fetch_prices()
    RAW.mkdir(parents=True, exist_ok=True)

    summary_rows = []
    for variant, px in series.items():
        panel, months, ndays, rets, ret_month = monthly_rc(px)
        print(f"\n[{variant}] built {panel.shape[0]} months, keeping first {N_MONTHS}",
              flush=True)
        panel = panel[:N_MONTHS]
        months = months[:N_MONTHS]
        ndays = ndays[:N_MONTHS]

        eig = np.linalg.eigvalsh(panel)
        kappa = eig[:, -1] / eig[:, 0]

        centre = airm_barycentre(panel, tol=1e-10, max_iter=500)
        delta = float(np.sqrt(airm_dist2(
            np.broadcast_to(centre.X, panel.shape), panel).mean()))

        checks = [
            ("shape is (240, 12, 12)", panel.shape == (N_MONTHS, 12, 12)),
            ("first month is 2000-01", months[0] == "2000-01"),
            ("last month is 2019-12", months[-1] == "2019-12"),
            ("every RC is positive definite", bool((eig[:, 0] > 0).all())),
            ("trading days per month in 15..25",
             bool(((ndays >= 15) & (ndays <= 25)).all())),
            ("no NaN or inf", bool(np.isfinite(panel).all())),
            ("AIRM centre converged", bool(centre.converged)),
        ]

        keep = np.isin(ret_month, months)          # daily rows for the kept months
        np.savez_compressed(RAW / f"rc_panel_{variant}.npz", panel=panel,
                            months=np.array(months), ndays=ndays,
                            tickers=np.array(TICKERS),
                            rets=rets[keep], ret_month=ret_month[keep])

        summary_rows += [
            (variant, "kappa median", f"{np.median(kappa):.4e}"),
            (variant, "kappa min", f"{kappa.min():.4e}"),
            (variant, "kappa max", f"{kappa.max():.4e}"),
            (variant, "delta", f"{delta:.4f}"),
            (variant, "months", str(panel.shape[0])),
            (variant, "trading days min/max", f"{ndays.min()}/{ndays.max()}"),
            *[(variant, f"check: {name}", "PASS" if ok else "FAIL")
              for name, ok in checks],
        ]

        print(f"[{variant}] kappa median {np.median(kappa):.3e} "
              f"({kappa.min():.2e} .. {kappa.max():.2e})   delta {delta:.4f}", flush=True)
        for name, ok in checks:
            print(f"    {'PASS' if ok else 'FAIL'}  {name}")

    lines = header("B3.4a -- the realised-covariance panel, both price variants",
                   extra=[f"tickers: {' '.join(TICKERS)}",
                          f"analysis window: 2000-01 .. 2019-12 "
                          f"(paper section 5: 'January 1, 2000 to December 31, 2019')",
                          f"scaling: x{SCALE:.0f}"])
    lines += [
        "Two panels are built, from `Adj Close` and from raw `Close`. Their",
        "notebook pins no yfinance version, so which one they used is unknown --",
        "and rather than guess, both are carried forward and the published LOCF",
        "and EWMA numbers decide. See experiments/check_panel_vs_parent.py.",
        "",
        "The download end date does NOT matter and was not swept: adjustment is a",
        "constant multiplicative factor per ticker over the whole history, and a",
        "constant factor cancels in log returns. Only raw-vs-adjusted moves the",
        "numbers, because dividends inside 2000-2019 are real return events.",
        "",
        "Read kappa against E2 (working range ends near 1e6) and delta against E7",
        "(BW and AIRM centres sit ~0.075*delta apart at m=12, as a fraction of the",
        "data's own spread).",
        "",
        "Panels are in results/raw/rc_panel_{adjusted,raw}.npz -- gitignored, data.",
    ]
    write("rc_panel_summary", lines, ["variant", "quantity", "value"], summary_rows)

    if any(v == "FAIL" for _, k, v in summary_rows if k.startswith("check")):
        sys.exit("one or more checks FAILED -- see results/final/rc_panel_summary.md")


if __name__ == "__main__":
    main()
