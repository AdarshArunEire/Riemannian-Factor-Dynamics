# B3.4b -- their estimator, our panel

Measurement only: no assertions, no pass/fail. Re-run and append a
dated section rather than editing.

- generated: 2026-08-19 12:23 UTC
- seed: 20260816
- numpy 2.5.2, python 3.14.7
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

Not corrected for: the ~20-vs-21 trading-day difference of AUDIT 2b.

**Stage 4: RFM has lower held-out FVU at 15/15 ranks under BW
and 10/15 under Frobenius. The winners differ at
5/15 ranks: 2, 3, 11, 14, 15.**
The mean relative RFM advantage is 35.55% under BW
and 4.13% under Frobenius.

Stage 4 is a matched-rank held-out reconstruction comparison, not a
forecasting test and not a factor-count selector. LYB predictions are
projected to SPD before BW scoring but not before Frobenius scoring, so
the five reversals combine loss geometry with that asymmetric repair.

Provenance correction (2026-08-19): the completed shared-mean run first
stored prefix means. The rank-specific curves here were recovered exactly
as v_r = r*mean_r - (r-1)*mean_(r-1). Legacy CSV SHA-256:
5353c10b887e45eaa6c7572643af25d54db564bf3acf0063f6f091aaf3e367db.
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
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=1 | 0.532488 / 1.188170 | 0.152508 / 0.327593 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=2 | 0.368458 / 0.516332 | 0.130046 / 0.115519 |  | DIFFERENT: BW RFM; Frob LYB |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=3 | 0.305767 / 0.432077 | 0.074726 / 0.072743 |  | DIFFERENT: BW RFM; Frob LYB |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=4 | 0.286611 / 0.424781 | 0.068257 / 0.071215 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=5 | 0.263131 / 0.368438 | 0.060904 / 0.063905 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=6 | 0.249981 / 0.358864 | 0.059400 / 0.061523 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=7 | 0.241519 / 0.345939 | 0.057628 / 0.060153 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=8 | 0.228694 / 0.344851 | 0.055079 / 0.056214 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=9 | 0.221511 / 0.341780 | 0.052214 / 0.054726 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=10 | 0.216782 / 0.337696 | 0.050733 / 0.051105 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=11 | 0.211440 / 0.333670 | 0.048718 / 0.048351 |  | DIFFERENT: BW RFM; Frob LYB |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=12 | 0.208200 / 0.329950 | 0.046980 / 0.047284 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=13 | 0.201413 / 0.329171 | 0.045649 / 0.046190 |  | same winner |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=14 | 0.196714 / 0.327652 | 0.044852 / 0.044617 |  | DIFFERENT: BW RFM; Frob LYB |
| 4 matched-rank FVU | RFM vs LYB | BW / Frobenius | r=15 | 0.190177 / 0.325916 | 0.041645 / 0.041433 |  | DIFFERENT: BW RFM; Frob LYB |

The corrected victory-lap runner now emits the returned curves directly.