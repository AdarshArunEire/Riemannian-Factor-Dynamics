# D4 -- day-count sweep

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-18 21:34 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.3
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- published targets: BW 2.66/2.36, Frobenius 12.51/11.97, risk 2.61/1.45
- days removed evenly spaced, not from the end

`bulk` is the worst gap among the BW and Frobenius statistics -- the ones
dominated by the LARGEST eigenvalues. `tail` is the worst gap among the
GMV risk errors, which run through 1/(1' Sigma^-1 1) and are dominated by
the SMALLEST eigenvalues. They are different claims about the panel and
the whole point of this sweep is that they may be minimised at different K.

If one K minimises both, day count is the mechanism and that K is their
effective M. If bulk is flat while tail moves sharply, the day count is
changing only the spectrum tail -- which is still informative, but means
our bulk agreement was never evidence about the tail.

K cannot go below 13: np.cov uses ddof=1, so the rank is at most K-1 and
a 12x12 covariance is singular at K <= 12. Their own solve(truth_lag)
would fail there, so their effective M is at least 13 whatever else is
true. That bounds the search from below before any number is computed.

If no K brings the tail close, day count is not it. The next suspects, in
order: whether they demean within the month; whether returns are computed
across month boundaries or reset each month; and whether any winsorising
## Measured

| K | mean_days | kappa_median | lambda_min_median | LOCF_BW | EWMA_BW | LOCF_Frob | EWMA_Frob | LOCF_risk | EWMA_risk | worst_bulk_gap | worst_tail_gap |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | 13.0 | 1.203e+04 | 1.425e-03 | 3.012 | 2.769 | 14.638 | 13.930 | 69.025 | 46.697 | 17.3% | 3120.5% |
| 14 | 14.0 | 3.872e+03 | 5.189e-03 | 3.085 | 2.614 | 15.154 | 12.471 | 17.887 | 6.599 | 21.1% | 585.3% |
| 15 | 15.0 | 1.813e+03 | 1.055e-02 | 2.957 | 2.610 | 14.310 | 12.812 | 4.542 | 2.199 | 14.4% | 74.0% |
| 16 | 16.0 | 1.130e+03 | 1.601e-02 | 2.838 | 2.456 | 11.721 | 10.792 | 3.581 | 1.537 | 9.8% | 37.2% |
| 17 | 17.0 | 8.305e+02 | 2.371e-02 | 2.805 | 2.461 | 13.537 | 12.018 | 2.767 | 1.578 | 8.2% | 8.8% |
| 18 | 18.0 | 6.169e+02 | 2.866e-02 | 2.826 | 2.459 | 13.731 | 12.258 | 3.319 | 1.633 | 9.8% | 27.2% |
| 20 | 19.9 | 4.702e+02 | 3.814e-02 | 2.691 | 2.357 | 12.702 | 11.796 | 2.550 | 1.373 | 1.5% | 5.3% |
| all | 21.0 | 4.281e+02 | 4.149e-02 | 2.679 | 2.360 | 12.814 | 12.041 | 1.990 | 1.237 | 2.4% | 23.7% |

or missing-data fill was applied before the covariance.