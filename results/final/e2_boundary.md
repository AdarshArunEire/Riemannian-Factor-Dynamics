# E2 -- boundary of the working range

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-17 23:03 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.7
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- N per cell: 50, delta: 1.0, tol: 1e-12, max_iter: 500

iters = -1 means an exception was raised rather than a number returned.
That is not necessarily a bug: spd_eigh's strict guard firing means an
intermediate stopped being numerically positive definite, which is the
guard doing its job at the edge of what float64 can represent.

Three outcomes, in increasing severity: converged; ran to max_iter with
a finite residual (stalled at the noise floor); raised. Record where each
boundary sits -- the first is the working range, the second is the
degraded band, the third is off the map.

Sanity anchor for the real application: realised covariance of 12 assets
## Measured

| m | cond | iters | residual | converged | raised |
|---|---|---|---|---|---|
| 2 | 100 | 5 | 6.201e-15 | 1 | - |
| 2 | 10000 | 3 | 3.106e-15 | 1 | - |
| 2 | 1e+06 | 2 | 2.452e-13 | 1 | - |
| 2 | 1e+08 | 53 | 6.974e-13 | 1 | - |
| 2 | 1e+10 | 500 | nan | 0 | - |
| 2 | 1e+12 | 500 | nan | 0 | - |
| 3 | 100 | 6 | 1.907e-13 | 1 | - |
| 3 | 10000 | 4 | 5.342e-13 | 1 | - |
| 3 | 1e+06 | 4 | 5.577e-13 | 1 | - |
| 3 | 1e+08 | -1 | nan | 0 | LinAlgError |
| 3 | 1e+10 | -1 | nan | 0 | LinAlgError |
| 3 | 1e+12 | -1 | nan | 0 | LinAlgError |
| 12 | 100 | 5 | 4.868e-13 | 1 | - |
| 12 | 10000 | 5 | 8.234e-14 | 1 | - |
| 12 | 1e+06 | 500 | 6.948e-12 | 0 | - |
| 12 | 1e+08 | -1 | nan | 0 | LinAlgError |
| 12 | 1e+10 | -1 | nan | 0 | LinAlgError |
| 12 | 1e+12 | -1 | nan | 0 | LinAlgError |

from ~21 daily returns is expected around kappa ~ 1e3-1e4.