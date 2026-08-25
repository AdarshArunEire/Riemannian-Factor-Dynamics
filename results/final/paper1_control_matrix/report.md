# Paper 1 control matrix

Numerical evidence only. A violation cell passes when it fails in the
declared measurable way; attractive performance is not required.

## Completion

- core: 1056/1056 rows
- phase: 480/480 rows
- core recorded errors: 0
- phase recorded errors: 0

**Status: complete at n up to 8,192.** Interpretations below
remain conditional on the predeclared DGPs.

## Core decisions

| regime | threshold accuracy | RFD loading angle | fallback total |
|---|---:|---:|---:|
| B0 | 100.0% | 0.77° | 0 |
| C0 | 100.0% | 0.77° | 0 |
| C1 | 100.0% | n/a | 0 |
| C2 | 100.0% | 0.05° | 0 |
| C3 | 100.0% | n/a | 0 |
| G-C | 100.0% | 0.85° | 0 |
| I-A | 100.0% | 0.69° | 0 |
| I-M | 100.0% | 0.77° | 0 |
| I-O | 100.0% | 0.82° | 0 |
| V-L | 100.0% | 1.46° | 0 |
| V-R | 100.0% | 0.77° | 0 |

## Paired headline effects

Positive values mean RFD reduces error relative to the fixed-centre ablation.

| regime | metric | median improvement | 95% paired-bootstrap interval | RFD wins |
|---|---|---:|---:|---:|
| B0 | loading projector | 95.5% | [94.1%, 96.8%] | 100.0% |
| B0 | observation reconstruction | 21.4% | [17.7%, 23.8%] | 100.0% |
| C0 | loading projector | -7.2% | [-18.9%, 2.2%] | 37.5% |
| C0 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| C1 | loading projector | nan% | [nan%, nan%] | nan% |
| C1 | observation reconstruction | 19.5% | [19.4%, 19.6%] | 100.0% |
| C2 | loading projector | 99.7% | [99.6%, 99.8%] | 100.0% |
| C2 | observation reconstruction | 99.4% | [99.4%, 99.5%] | 100.0% |
| C3 | loading projector | nan% | [nan%, nan%] | nan% |
| C3 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| G-C | loading projector | 95.5% | [93.8%, 96.0%] | 100.0% |
| G-C | observation reconstruction | 24.0% | [20.6%, 26.2%] | 100.0% |
| I-A | loading projector | -14.5% | [-22.4%, -0.7%] | 31.2% |
| I-A | observation reconstruction | -0.2% | [-0.2%, -0.1%] | 0.0% |
| I-M | loading projector | 89.7% | [87.9%, 91.6%] | 100.0% |
| I-M | observation reconstruction | 14.9% | [14.7%, 15.2%] | 100.0% |
| I-O | loading projector | 84.3% | [79.6%, 90.0%] | 96.9% |
| I-O | observation reconstruction | 26.3% | [26.0%, 26.5%] | 100.0% |
| P-A-000 | loading projector | -3.8% | [-8.0%, 6.7%] | 46.9% |
| P-A-000 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| P-A-010 | loading projector | -3.8% | [-7.6%, 5.6%] | 46.9% |
| P-A-010 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| P-A-020 | loading projector | -3.8% | [-8.4%, 4.8%] | 40.6% |
| P-A-020 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| P-A-035 | loading projector | -4.3% | [-8.8%, 2.9%] | 40.6% |
| P-A-035 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| P-A-050 | loading projector | -4.2% | [-8.1%, 2.3%] | 43.8% |
| P-A-050 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| P-M-000 | loading projector | -2.3% | [-6.9%, 4.0%] | 43.8% |
| P-M-000 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| P-M-010 | loading projector | 17.7% | [14.7%, 23.5%] | 90.6% |
| P-M-010 | observation reconstruction | 1.5% | [1.5%, 1.6%] | 100.0% |
| P-M-020 | loading projector | 67.6% | [63.9%, 73.5%] | 100.0% |
| P-M-020 | observation reconstruction | 6.0% | [5.8%, 6.2%] | 100.0% |
| P-M-035 | loading projector | 89.0% | [87.7%, 91.0%] | 100.0% |
| P-M-035 | observation reconstruction | 15.0% | [14.7%, 15.3%] | 100.0% |
| P-M-050 | loading projector | 94.3% | [93.7%, 95.2%] | 100.0% |
| P-M-050 | observation reconstruction | 23.7% | [23.4%, 24.2%] | 100.0% |
| P-O-000 | loading projector | -3.7% | [-8.4%, 3.6%] | 37.5% |
| P-O-000 | observation reconstruction | -0.1% | [-0.2%, -0.1%] | 0.0% |
| P-O-010 | loading projector | 17.9% | [6.8%, 20.9%] | 84.4% |
| P-O-010 | observation reconstruction | 3.1% | [3.0%, 3.2%] | 100.0% |
| P-O-020 | loading projector | 44.8% | [33.0%, 50.1%] | 93.8% |
| P-O-020 | observation reconstruction | 11.2% | [11.0%, 11.3%] | 100.0% |
| P-O-035 | loading projector | 87.0% | [82.5%, 89.9%] | 100.0% |
| P-O-035 | observation reconstruction | 26.2% | [26.0%, 26.4%] | 100.0% |
| P-O-050 | loading projector | 98.6% | [98.5%, 98.7%] | 100.0% |
| P-O-050 | observation reconstruction | 44.5% | [44.3%, 44.7%] | 100.0% |
| V-L | loading projector | 92.4% | [89.9%, 93.4%] | 100.0% |
| V-L | observation reconstruction | 21.8% | [17.6%, 23.8%] | 100.0% |
| V-R | loading projector | 95.9% | [94.7%, 97.0%] | 100.0% |
| V-R | observation reconstruction | 22.4% | [18.5%, 25.0%] | 100.0% |

The fixed-centre placebo, rank-zero nulls, identification ordering,
curved-path health, and violation boundaries require scientific
adjudication together; no single favourable row closes the matrix.
