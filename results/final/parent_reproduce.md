# B3.4b -- their estimator, our panel

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-18 23:00 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.3
- machine: Intel64 Family 6 Model 165 Stepping 5, GenuineIntel / Windows-11-10.0.22631-SP0
- eps: 2.220446e-16
- their code sourced verbatim; no upstream file modified
- bands: bulk 2%, tail 6% (predeclaration, 2026-08-18)
- anchors: arXiv:2607.28385v1 Figures 3 and 4

**Stage 1, harness agreement: worst 3.31e-14 (gate 1e-08).** Their R and our Python compute LOCF and
EWMA from the same panel, at full precision on both sides. A failure
here is OUR evaluation code, and every Stage 2 number below would be
uninterpretable until it were fixed.

**Stage 2: 13 of 24 published figures inside the
predeclared band.** LOCF and EWMA are not evidence here -- the band was
set from them. RFM and LFM are the reproduction.

**Stage 3 is the one to read.** The paper's claim is an ordering, not a
set of decimals. A number outside the band with the ranking intact is a
data difference; a ranking that flips is a reproduction failure.

## Measured

| stage | model | statistic | moment | published/ours | theirs-on-our-panel | gap | verdict |
|---|---|---|---|---|---|---|---|
| 1 harness | LOCF | BW distance | mean | 2.67861114425 | 2.67861114425 | 7.96e-15 |  |
| 1 harness | LOCF | BW distance | median | 2.38853733795 | 2.38853733795 | 3.31e-14 |  |
| 1 harness | LOCF | Frobenius | mean | 12.8139289462 | 12.8139289462 | 4.16e-16 |  |
| 1 harness | LOCF | Frobenius | median | 8.24603670144 | 8.24603670144 | 2.15e-16 |  |
| 1 harness | LOCF | risk error | mean | 1.99027098908 | 1.99027098908 | 4.02e-15 |  |
| 1 harness | LOCF | risk error | median | 1.1271313066 | 1.1271313066 | 1.97e-16 |  |
| 1 harness | EWMA | BW distance | mean | 2.36018504483 | 2.36018504483 | 5.08e-15 |  |
| 1 harness | EWMA | BW distance | median | 2.23440148599 | 2.23440148599 | 8.94e-15 |  |
| 1 harness | EWMA | Frobenius | mean | 12.0414058028 | 12.0414058028 | 2.80e-15 |  |
| 1 harness | EWMA | Frobenius | median | 9.80945237654 | 9.80945237654 | 0.00e+00 |  |
| 1 harness | EWMA | risk error | mean | 1.23732692228 | 1.23732692228 | 1.08e-15 |  |
| 1 harness | EWMA | risk error | median | 0.880199883638 | 0.880199883638 | 1.40e-14 |  |
| 2 bulk | RFM | BW distance | mean | 2.22 | 2.239 | 0.9% | in band |
| 2 bulk | RFM | BW distance | median | 2 | 2.026 | 1.3% | in band |
| 2 bulk | RFM | Frobenius | mean | 10.79 | 10.97 | 1.7% | in band |
| 2 bulk | RFM | Frobenius | median | 7.14 | 7.077 | 0.9% | in band |
| 2 tail | RFM | risk error | mean | 0.94 | 1.001 | 6.0% | OUT (band 6%) |
| 2 tail | RFM | risk error | median | 0.52 | 0.5785 | 10.1% | OUT (band 6%) |
| 2 bulk | LFM | BW distance | mean | 3.57 | 3.564 | 0.2% | in band |
| 2 bulk | LFM | BW distance | median | 3.63 | 3.653 | 0.6% | in band |
| 2 bulk | LFM | Frobenius | mean | 17.25 | 17.11 | 0.8% | in band |
| 2 bulk | LFM | Frobenius | median | 17.01 | 16.09 | 5.4% | OUT (band 2%) |
| 2 tail | LFM | risk error | mean | 3.66 | 3.238 | 11.5% | OUT (band 6%) |
| 2 tail | LFM | risk error | median | 2.29 | 2.023 | 11.6% | OUT (band 6%) |
| 2 bulk | LOCF | BW distance | mean | 2.66 | 2.679 | 0.7% | in band |
| 2 bulk | LOCF | BW distance | median | 2.33 | 2.389 | 2.5% | OUT (band 2%) |
| 2 bulk | LOCF | Frobenius | mean | 12.51 | 12.81 | 2.4% | OUT (band 2%) |
| 2 bulk | LOCF | Frobenius | median | 8.02 | 8.246 | 2.7% | OUT (band 2%) |
| 2 tail | LOCF | risk error | mean | 2.61 | 1.99 | 23.7% | OUT (band 6%) |
| 2 tail | LOCF | risk error | median | 0.91 | 1.127 | 19.3% | OUT (band 6%) |
| 2 bulk | EWMA | BW distance | mean | 2.36 | 2.36 | 0.0% | in band |
| 2 bulk | EWMA | BW distance | median | 2.28 | 2.234 | 2.0% | in band |
| 2 bulk | EWMA | Frobenius | mean | 11.97 | 12.04 | 0.6% | in band |
| 2 bulk | EWMA | Frobenius | median | 9.81 | 9.809 | 0.0% | in band |
| 2 tail | EWMA | risk error | mean | 1.45 | 1.237 | 14.7% | OUT (band 6%) |
| 2 tail | EWMA | risk error | median | 0.89 | 0.8802 | 1.1% | in band |
| 3 ranking | - | BW distance | mean | RFM < EWMA < LOCF < LFM | RFM < EWMA < LOCF < LFM |  | same |
| 3 ranking | - | BW distance | median | RFM < EWMA < LOCF < LFM | RFM < EWMA < LOCF < LFM |  | same |
| 3 ranking | - | Frobenius | mean | RFM < EWMA < LOCF < LFM | RFM < EWMA < LOCF < LFM |  | same |
| 3 ranking | - | Frobenius | median | RFM < LOCF < EWMA < LFM | RFM < LOCF < EWMA < LFM |  | same |
| 3 ranking | - | risk error | mean | RFM < EWMA < LOCF < LFM | RFM < EWMA < LOCF < LFM |  | same |
| 3 ranking | - | risk error | median | RFM < EWMA < LOCF < LFM | RFM < EWMA < LOCF < LFM |  | same |

Not corrected for: the ~20-vs-21 trading-day difference of AUDIT 2b.