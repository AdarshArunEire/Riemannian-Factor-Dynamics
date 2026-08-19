# E5 -- AIRM vs BW barycentre cost

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-18 11:12 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.3
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- common tol: 1e-11, max_iter: 500

The ratio column is the number this experiment exists for. E4's
budget assumed ~2x for AIRM; anything materially above that is a
reason to revisit N-19's allocation BEFORE any result is seen.

Both methods are timed at a COMMON tolerance. Comparing them at
their own defaults would be rigged, since AIRM's measured floor
(~6e-12) is looser than BW's (~1e-14) and it would be charged for
chasing a precision it cannot reach.

Projected over the N-19 grid (9 cells per m, 20 streams, 50000 draws):
  BW    43.8 min
  AIRM  105.3 min
  both  149.1 min (2.49 h)

Still excluded: proxy generation, the Frobenius barycentre (free),
## Measured

| m | cond | N | bw_seconds | bw_iters | bw_converged | airm_seconds | airm_iters | airm_converged | ratio |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 10 | 100 | 0.0025 | 10 | 1 | 0.0031 | 12 | 1 | 1.27 |
| 3 | 10 | 1000 | 0.0147 | 9 | 1 | 0.0201 | 12 | 1 | 1.37 |
| 3 | 10 | 10000 | 0.1539 | 9 | 1 | 0.1884 | 11 | 1 | 1.22 |
| 3 | 10 | 50000 | 0.7364 | 9 | 1 | 0.9209 | 11 | 1 | 1.25 |
| 3 | 1000 | 100 | 0.0074 | 30 | 1 | 0.1042 | 401 | 1 | 14.13 |
| 3 | 1000 | 1000 | 0.0389 | 24 | 1 | 0.2319 | 138 | 1 | 5.96 |
| 3 | 1000 | 10000 | 0.3869 | 23 | 1 | 2.0199 | 120 | 1 | 5.22 |
| 3 | 1000 | 50000 | 1.8751 | 23 | 1 | 8.9612 | 111 | 1 | 4.78 |
| 12 | 10 | 100 | 0.0126 | 9 | 1 | 0.0162 | 11 | 1 | 1.29 |
| 12 | 10 | 1000 | 0.1189 | 8 | 1 | 0.1494 | 10 | 1 | 1.26 |
| 12 | 10 | 10000 | 1.1824 | 8 | 1 | 1.3399 | 9 | 1 | 1.13 |
| 12 | 10 | 50000 | 5.1566 | 7 | 1 | 6.6457 | 9 | 1 | 1.29 |
| 12 | 1000 | 100 | 0.0307 | 24 | 1 | 0.0832 | 64 | 1 | 2.71 |
| 12 | 1000 | 1000 | 0.2838 | 21 | 1 | 0.6348 | 47 | 1 | 2.24 |
| 12 | 1000 | 10000 | 2.5476 | 19 | 1 | 5.5037 | 41 | 1 | 2.16 |
| 12 | 1000 | 50000 | 12.7268 | 19 | 1 | 26.1467 | 39 | 1 | 2.05 |

and C5's non-Wishart proxy.