# B3.4b step 1 -- inputs handed to the parent's own script

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-18 22:00 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.3
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- variant: adjusted
- window: 2000-01 .. 2019-12
- tickers: MSFT AAPL ORCL CSCO JPM BAC WFC GS XOM CVX COP EOG
- written into reference/.../sp500_covariance/ (gitignored)

`sp500_covariance/` is ABSENT from the clone at commit c07d49c, and no
file in their repo builds the RC panel from prices. The panel is an
input to their code, so reproduction requires supplying it. No upstream
file is modified; deleting this directory restores the clone exactly.

The panel is written UNSCALED. build_rc_panel.py applies their x10000
(sp500_analysis.R:150) and sp500_reproduce.R:148 applies it again, so
exactly one of the two must be undone and this is the one we control.

## Measured

| quantity | value |
|---|---|
| variant | adjusted |
| months | 240 |
| scale applied on export | 1/10000 |
| max |Sigma| after unscaling | 2.8719e-02 |
|   where | 2000-09 -- AAPL, the -52% day of 2000-09-29 |
| median diagonal, unscaled | 2.2512e-04 |
|   as annualised vol | 23.8% |
| median diagonal x 10000 | 2.2512 |
| vix rows | 5217 |
| vix missing blanked | 185 |
| check: the CSV bitwise round-trips the unscaled panel | PASS |
| check: median asset-month annualises to equity-like vol (5%-100%) | PASS |
| check: their aperm+reshape returns chronological order | PASS |
| check: 240 months, 12 assets | PASS |
| check: every RC still positive definite | PASS |
| check: VIX fetched | PASS |

Next: Rscript R/make_panel_rdata.R, then Rscript R/run_parent_reproduce.R.