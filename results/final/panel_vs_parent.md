# B3.4a step 3 -- panel verified against the published numbers

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-18 21:00 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.3
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- test window: last 36 months (2017-01 .. 2019-12)
- EWMA lambda: 0.94, Sigma_hat_1 = 0 (paper section 5)
- anchors: arXiv:2607.28385v1 Figures 3 and 4

LOCF and EWMA involve no model fitting, no Frechet mean, no seeds and no
convergence. Every gap below is therefore about the DATA and nothing
else -- which is what makes this a panel check rather than a whole-
pipeline check.

**Closer variant: `adjusted` Close, worst gap 23.9%** (other variant 27.5%).

### Proposed acceptance tolerance

Set it at the worst gap achieved here, **23.9%**, rounded up.
It is the closest this panel can get to theirs, so nothing downstream can
be held to a tighter standard. Two floors sit underneath it and cannot be
removed: their figures print to 2 decimals, which is +-0.5% on a value of
1.0 and less on larger ones; and Yahoo revises history, so a 2026 pull is
not byte-identical to theirs whatever we do.

**Fix this number before running our own estimator.** Chosen from LOCF and
EWMA, which cannot be tuned, it is an honest band. Chosen after seeing an
RFM comparison, it would not be.

### Not yet checkable

RFM and LFM are also published (BW 2.22/2.00 and 3.57/3.63; Frobenius
10.79/7.14 and 17.25/17.01; risk 0.94/0.52 and 3.66/2.29) but depend on
their estimator, so they test the pipeline rather than the data. They are
## Measured

| variant | model | statistic | published_mean | ours_mean | gap_mean | published_median | ours_median | gap_median |
|---|---|---|---|---|---|---|---|---|
| adjusted | LOCF | BW distance | 2.66 | 2.68 | 0.7% | 2.33 | 2.39 | 2.5% |
| adjusted | EWMA | BW distance | 2.36 | 2.36 | 0.0% | 2.28 | 2.23 | 2.0% |
| adjusted | LOCF | Frobenius distance | 12.51 | 12.81 | 2.4% | 8.02 | 8.25 | 2.8% |
| adjusted | EWMA | Frobenius distance | 11.97 | 12.04 | 0.6% | 9.81 | 9.81 | 0.0% |
| adjusted | LOCF | risk prediction error | 2.61 | 1.99 | 23.7% | 0.91 | 1.13 | 23.9% |
| adjusted | EWMA | risk prediction error | 1.45 | 1.24 | 14.7% | 0.89 | 0.88 | 1.1% |
| raw | LOCF | BW distance | 2.66 | 2.69 | 1.0% | 2.33 | 2.39 | 2.4% |
| raw | EWMA | BW distance | 2.36 | 2.37 | 0.2% | 2.28 | 2.23 | 2.1% |
| raw | LOCF | Frobenius distance | 12.51 | 12.80 | 2.3% | 8.02 | 8.38 | 4.5% |
| raw | EWMA | Frobenius distance | 11.97 | 12.04 | 0.6% | 9.81 | 9.86 | 0.5% |
| raw | LOCF | risk prediction error | 2.61 | 1.89 | 27.5% | 0.91 | 0.93 | 2.7% |
| raw | EWMA | risk prediction error | 1.45 | 1.16 | 20.2% | 0.89 | 0.80 | 10.4% |

the B3.4b targets.