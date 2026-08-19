# Diagnostic -- the GMV risk-error gap

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-18 21:13 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.3
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- panel: adjusted, 240 months
- D1: 20 draws at 2.40% relative perturbation

D1 is the decisive one. If BW and Frobenius barely move under a
perturbation the size of our own disagreement with them, while the risk
error swings enough to cover their published value, then a 20% risk gap
is what a 2% panel gap looks like after inverting a matrix at this
conditioning -- and the risk statistic cannot verify a panel.

If the perturbed range does NOT cover their value, amplification is not
the whole story and something in the construction differs. The leading
candidate is the effective number of trading days: their notebook
downloads all ~500 constituents and selects twelve later, so if days
with any missing price were dropped across the full universe, their
monthly covariances rest on fewer observations -- worse conditioned,
more extreme weights, larger risk errors, and almost no effect on BW or
## Measured

| diagnostic | item | value | theirs | range | swing | covers |
|---|---|---|---|---|---|---|
| D1 sensitivity | LOCF BW | 2.679 | 2.66 | 2.669..2.695 | 1.0% | no |
| D1 sensitivity | EWMA BW | 2.360 | 2.36 | 2.357..2.371 | 0.6% | YES |
| D1 sensitivity | LOCF Frob | 12.814 | 12.51 | 12.710..13.022 | 2.4% | no |
| D1 sensitivity | EWMA Frob | 12.041 | 11.97 | 11.989..12.185 | 1.6% | no |
| D1 sensitivity | LOCF risk | 1.990 | 2.61 | 1.949..2.043 | 4.8% | no |
| D1 sensitivity | EWMA risk | 1.237 | 1.45 | 1.211..1.282 | 5.7% | no |
| D2 amplifier | kappa median | 3.906e+02 |  |  |  |  |
| D2 amplifier | kappa max | 1.430e+03 |  |  |  |  |
| D2 amplifier | gross leverage median | 3.12 |  |  |  |  |
| D2 amplifier | gross leverage max | 9.32 |  |  |  |  |
| D2 amplifier | corr(log kappa, risk err) | +0.169 |  |  |  |  |
| D3 shrinkage | alpha=0.00 | 1.990 | 23.7% | 1.237 | 14.7% |  |
| D3 shrinkage | alpha=0.01 | 1.385 | 46.9% | 0.970 | 33.1% |  |
| D3 shrinkage | alpha=0.05 | 0.833 | 68.1% | 0.755 | 47.9% |  |
| D3 shrinkage | alpha=0.10 | 0.684 | 73.8% | 0.711 | 50.9% |  |
| D3 shrinkage | alpha=0.20 | 0.660 | 74.7% | 0.711 | 51.0% |  |
| D3 shrinkage | alpha=0.50 | 0.646 | 75.3% | 0.734 | 49.4% |  |

Frobenius. That is the shape of what we see.