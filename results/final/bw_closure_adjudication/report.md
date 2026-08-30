# P1-BW-CLOSE — final adjudication

**Verdict:** complete; qualified fixed-rank pass.

This is numerical evidence for the fixed-size, full-rank, safeguarded
Bures–Wasserstein implementation. It is not a proof of the analytical theorem
and it does not extend the shrinking-margin or growing-matrix-size theorems.

## Integrity

- frozen tasks requested: 496
- unique rows recorded: 496
- duplicate tasks: 0
- ordinary errors: 0
- failed or unknown verdicts: 0
- safe fit rows: 400
- hostile probes: 80
- lower-margin boundary fits: 16

The immutable configuration is
[`config/bw_closure.yaml`](../../../config/bw_closure.yaml). The raw evidence,
summary, metadata and machine report are in
[`results/intermediate/bw_closure`](../../intermediate/bw_closure).

## Rate-spine evidence

The fitted log–log exponents are finite-grid diagnostics. They are compared with
the robust centre/loading ceiling \(3/7\approx0.429\), polygon design exponent
\(4/7\approx0.571\), and the squared null-spectrum scale \(6/7\approx0.857\).

| path | centre | polygon | lag row | operator | loading | first null eigenvalue |
|---|---:|---:|---:|---:|---:|---:|
| commuting BW-flat | 0.41 | 0.58 | 0.68 | 0.72 | 0.55 | 1.01 |
| noncommuting curved | 0.42 | 0.58 | 0.75 | 0.82 | 0.57 | 1.17 |

The centre and polygon exponents closely track their analytical design rates.
The other quantities decline at least as fast on this grid; this is compatible
with, but cannot prove, their asymptotic upper bounds.

Selected medians from \(n=512\) to \(n=8192\):

| path | centre error | lag-row error | loading-projector error |
|---|---:|---:|---:|
| commuting, \(n=512\) | 0.1036 | 0.00655 | 0.0700 |
| commuting, \(n=8192\) | 0.0362 | 0.000948 | 0.0125 |
| curved, \(n=512\) | 0.1148 | 0.00668 | 0.0847 |
| curved, \(n=8192\) | 0.0369 | 0.000898 | 0.0191 |

At \(n=8192\), the median loading-projector errors over the regular scientific
cells range from 0.0105 to 0.0191. These are small subspace-angle errors in the
declared DGPs.

## Rank scope

Every rank-positive synthetic recovery result uses the DGP's **known true
rank**. The rank-zero control likewise uses the known null rank. Selector
columns remain in the raw data as diagnostics, but they are not adjudicated as
a Paper 1 result. This campaign therefore supports loading recovery conditional
on rank and makes no automatic-rank-selection claim.

This choice isolates the scientific question under test: whether moving-centre
estimation, polygon construction, BW transport and lag-operator recovery work
when the target dimension is known. It does not conceal rank choice in APP-FIN:
that real-data bridge reports a training-validation-fixed rank and one frozen
causal online policy over the parent-matched candidates \(0,\ldots,15\). The
policy may update its realised rank only from completed forecasts.

## Generated-domain and theorem-input checks

Across the 400 safe fit rows:

- domain pass: 400/400
- fallback: 0
- nonconvergence: 0
- generated-domain failure: 0
- operator assembly inequality violations: 0
- beyond-rank null-bound violations: 0

Observed safe-domain extrema remained away from the configured gates:

| quantity | observed safe extreme | configured gate |
|---|---:|---:|
| minimum eigenvalue | 0.0311 | 0.005 lower bound |
| maximum eigenvalue | 2.389 | 12 upper bound |
| minimum polar singular margin | 0.0941 | 0.01 lower bound |
| minimum Exp-factor margin | 0.311 | 0.01 lower bound |
| maximum score-radius ratio | 0.697 | 2 upper bound |
| maximum path length | 0.384 | 3 upper bound |

## Finite-sample qualification

The sufficient condition that empirical operator error be below the oracle
eigengap did not hold uniformly. Median assembly/gap ratios at \(n=8192\) were
approximately 1.45–1.82, and only a minority of positive cells satisfied the
literal sufficient inequality.

This does not contradict the small observed projector errors: Davis–Kahan is a
worst-case sufficient bound and may be conservative. It does mean the paper
must report the strong empirical recovery and the failed finite-sample
certificate side by side. The experiment does not numerically certify the
asymptotic theorem at every finite cell.

## Hostile and boundary verdicts

- signed Richardson exit: declared positive fallback activated in all 16 probes;
- rank-deficient input: honestly rejected in all 16 probes;
- incompatible Exp input: honestly rejected in all 16 probes;
- near-identical matrices: squared BW distance stayed finite and nonnegative,
  with maximum numerical residue \(1.78\times10^{-15}\);
- increasing dispersion at fixed conditioning: barycentres converged, with
  maximum residual \(2.89\times10^{-14}\);
- shrinking lower margin: all 16 fits remained numerically finite but correctly
  exposed that they were outside the fixed-margin theorem.

The lower-margin cells are boundary diagnostics only. Their good-looking
finite errors cannot be promoted into evidence for the separate shrinking-
margin theorem.

## Consequence

P1-BW-CLOSE is closed. The next Paper 1 experiment is literal parent RFM versus
RFD on common regular BW draws, with known synthetic rank supplied to both so
that rank selection cannot confound the moving-centre comparison. After the
minimal causal forecast policy is frozen, APP-FIN compares a
training-validation-fixed rank with one predeclared online policy over nested
ranks \(0,\ldots,15\). Every candidate forecast is issued before its outcome,
and the online update uses completed losses only. A whole-test best-rank curve
or monthwise best-rank path, if shown, is a retrospective oracle and cannot be
the headline result.
