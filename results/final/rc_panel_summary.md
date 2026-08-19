# B3.4a -- the realised-covariance panel, both price variants

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-18 21:33 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.3
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- tickers: MSFT AAPL ORCL CSCO JPM BAC WFC GS XOM CVX COP EOG
- analysis window: 2000-01 .. 2019-12 (paper section 5: 'January 1, 2000 to December 31, 2019')
- scaling: x10000

Two panels are built, from `Adj Close` and from raw `Close`. Their
notebook pins no yfinance version, so which one they used is unknown --
and rather than guess, both are carried forward and the published LOCF
and EWMA numbers decide. See experiments/check_panel_vs_parent.py.

The download end date does NOT matter and was not swept: adjustment is a
constant multiplicative factor per ticker over the whole history, and a
constant factor cancels in log returns. Only raw-vs-adjusted moves the
numbers, because dividends inside 2000-2019 are real return events.

Read kappa against E2 (working range ends near 1e6) and delta against E7
(BW and AIRM centres sit ~0.075*delta apart at m=12, as a fraction of the
data's own spread).

## Measured

| variant | quantity | value |
|---|---|---|
| adjusted | kappa median | 4.2805e+02 |
| adjusted | kappa min | 6.4403e+01 |
| adjusted | kappa max | 1.4838e+04 |
| adjusted | delta | 5.2279 |
| adjusted | months | 240 |
| adjusted | trading days min/max | 15/23 |
| adjusted | check: shape is (240, 12, 12) | PASS |
| adjusted | check: first month is 2000-01 | PASS |
| adjusted | check: last month is 2019-12 | PASS |
| adjusted | check: every RC is positive definite | PASS |
| adjusted | check: trading days per month in 15..25 | PASS |
| adjusted | check: no NaN or inf | PASS |
| adjusted | check: AIRM centre converged | PASS |
| raw | kappa median | 4.0165e+02 |
| raw | kappa min | 6.4115e+01 |
| raw | kappa max | 1.0237e+04 |
| raw | delta | 5.2106 |
| raw | months | 240 |
| raw | trading days min/max | 15/23 |
| raw | check: shape is (240, 12, 12) | PASS |
| raw | check: first month is 2000-01 | PASS |
| raw | check: last month is 2019-12 | PASS |
| raw | check: every RC is positive definite | PASS |
| raw | check: trading days per month in 15..25 | PASS |
| raw | check: no NaN or inf | PASS |
| raw | check: AIRM centre converged | PASS |

Panels are in results/raw/rc_panel_{adjusted,raw}.npz -- gitignored, data.