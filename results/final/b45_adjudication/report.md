# B4.5 / N-01 adjudication

## Verdict

**Qualified pass.** The complete bounded-energy RFD implementation is
numerically healthy, recovers the generated loading space accurately,
shows decreasing centre/row/operator/loading errors, satisfies the null
eigenvalue square bound on every recorded production draw, and selects
the declared rank by thresholding on every draw. It has not uniformly
entered the sufficient operator-error-below-eigengap regime by n=8,192,
so these experiments do not justify a stronger finite-sample claim.

This is numerical evidence, not a proof of the analytical theorem.

## Data integrity

- result CSV files parsed: 61
- result rows parsed: 130,488
- parse failures: 0
- recorded scientific status errors: 0
- B4.5 rows: 960 (480 paired DGP draws; production and reference)
- B4.5 fallback count: 0
- B4.5 nonconverged local-mean stages: 0
- null eigenvalue <= lag-row error squared on every production draw: True

The infinite cells listed in `csv_audit.csv` are the declared `a=∞`
sentinel in the discrepancy experiment, not failed numerical outputs.

## Recovery at n = 8,192

| SPD size m | centre error / path | loading projector error | largest loading angle | factor NRMSE | operator error < gap | threshold rank correct |
|---|---|---|---|---|---|---|
| 2 | 17.8% | 0.0102 | 0.59° | 44.1% | 46.9% | 100.0% |
| 3 | 18.7% | 0.0115 | 0.66° | 35.3% | 68.8% | 100.0% |
| 4 | 18.4% | 0.0158 | 0.91° | 30.4% | 59.4% | 100.0% |

The loading target is not merely another fitted oracle: the noiseless
factor lag row lies in the generated loading span, and its positive
rank-two gap makes its projector equal to the DGP loading projector on
these draws. Thus the 1–1.6% projector errors are absolute synthetic-truth
errors. Factor-score recovery is materially weaker and reconstruction has
a per-observation noise/projection floor, so neither should be described as
vanishing from these plots.

## Empirical exponents

Positive `a` below means the median error follows approximately n^(-a)
over n=512,...,8192. These are descriptive finite-grid slopes.

| metric | m=2 | m=3 | m=4 |
|---|---:|---:|---:|
| centre path | 0.438 | 0.482 | 0.465 |
| first null eigenvalue | 1.096 | 1.065 | 1.126 |
| lag operator | 0.893 | 1.228 | 1.057 |
| lag row | 0.804 | 1.080 | 0.985 |
| loading projector | 0.639 | 0.670 | 0.603 |

## Paired production-bandwidth effect

| metric | median improvement over c=1.3 | pairs improved |
|---|---:|---:|
| centre path | 17.0% | 82.9% |
| lag row | 41.5% | 78.5% |
| lag operator | 46.8% | 77.7% |
| loading projector | 9.3% | 64.4% |
| first null eigenvalue | 9.0% | 67.1% |
| factor scores | 10.2% | 79.4% |
| observation reconstruction | 0.4% | 88.5% |
| signal reconstruction | 0.6% | 86.9% |

The bandwidth rule helps the centre and theorem intermediates
substantially, but changes final reconstruction by less than 1% because
reconstruction is dominated by the score/noise floor.

## What comparison is still required?

The completed B4.5 table compares RFD to the exact generated loading
target. Practical model comparison needs the same DGP draw fitted at four
levels: truth, true moving centre with noisy observations, feasible RFD,
and one global-centre RFM-compatible estimation. The replay harness
`experiments/run_b45_comparators.py` implements the two missing levels
without changing seeds. Literal parent-code parity belongs on the later BW
control cells because the present B4.5 DGP uses AIRM.

**Status:** all 480 same-draw comparator tasks completed without a
recorded error. At n=8,192:

| SPD m | method | loading angle | factor NRMSE | observation reconstruction RMS |
|---:|---|---:|---:|---:|
| 2 | known centre + noise | 0.47° | 38.3% | 0.1132 |
| 2 | full RFD | 0.59° | 44.1% | 0.1133 |
| 2 | one-centre RFM-compatible | 7.48° | 50.9% | 0.1281 |
| 3 | known centre + noise | 0.70° | 27.3% | 0.1630 |
| 3 | full RFD | 0.66° | 35.3% | 0.1632 |
| 3 | one-centre RFM-compatible | 17.26° | 38.0% | 0.2080 |
| 4 | known centre + noise | 0.93° | 21.4% | 0.1786 |
| 4 | full RFD | 0.91° | 30.4% | 0.1788 |
| 4 | one-centre RFM-compatible | 17.28° | 32.9% | 0.2223 |

Paired RFD improvement over the one-centre fit at n=8,192:

| SPD m | target | median error reduction | RFD wins |
|---:|---|---:|---:|
| 2 | loading projector | 93.1% | 100.0% |
| 2 | factor scores | 12.5% | 93.8% |
| 2 | observation reconstruction | 9.9% | 93.8% |
| 2 | latent-signal reconstruction | 5.5% | 90.6% |
| 3 | loading projector | 96.2% | 100.0% |
| 3 | factor scores | 8.7% | 84.4% |
| 3 | observation reconstruction | 20.8% | 100.0% |
| 3 | latent-signal reconstruction | 32.6% | 100.0% |
| 4 | loading projector | 94.6% | 100.0% |
| 4 | factor scores | 5.7% | 68.8% |
| 4 | observation reconstruction | 19.9% | 100.0% |
| 4 | latent-signal reconstruction | 42.9% | 100.0% |

This is a paper-eligible positive control, not a general empirical
dominance claim. The DGP deliberately satisfies the moving-centre
model with one cubic drift path, rank two, AR(1) factors, white
constant-norm tangent noise, and small AIRM matrices. A fixed-centre
placebo is still required to show that the gain disappears when drift
is absent; literal parent-code comparison belongs on the BW cells.
