---
type: paper-shape
title: Paper 1 shape — identification to application
status: current-spec
last-audited: 2026-08-25
---

# Paper 1 shape — identification to application

\[
\text{identification theorem}
\longrightarrow
\text{moving-centre estimator}
\longrightarrow
\text{controlled synthetic boundary}
\longrightarrow
\text{real APP-FIN illustration}
\longrightarrow
\text{freeze}.
\]

That is the whole first paper. Its central contribution is not a faster rate or
a universal forecasting victory. It identifies when centre drift and a
persistent factor can be separated, builds an estimator for the separated
objects, and shows where the distinction matters.

## 1. Identification theorem

Begin with the question the fixed-centre model assumes away: why study
fluctuations around one Fréchet mean without first asking whether the mean
moves? State the positive identification conditions and the impossibility
boundary. The claim is not that the parent's Factor 1 is spurious. It is that a
fixed-centre fit can superpose centre drift and persistent common movement and
cannot report their split without additional structure.

## 2. Moving-centre estimator

Introduce only the machinery needed to estimate the identified objects:

1. three-scale local Fréchet centres;
2. the shared polygonal centre path and transported frame;
3. common-reference tangent rows;
4. the nonzero-lag operator and minimum dynamic loading space;
5. fixed-rank reconstruction, with selector theory stated separately.

The robust theorem supplies the dimension-uniform bounded-energy rate and its
explicit assumptions. Long expansions and theorem-boundary ledgers belong in
the repository supplement, not the narrative spine.

## 3. Controlled synthetic boundary

The numerical evidence asks when the extra moving-centre machinery helps. The
literal paired BW comparison supplies the clean answer:

- all 576 draws completed without failures or fallbacks;
- parent RFM won all 288 home/fixed/aligned draws;
- RFD won all 288 mixed/orthogonal/curved draws;
- at \(n=8192\), RFD reduced median latent-signal error by 42.5%, 57.8%,
  and 55.8% in the mixed, orthogonal, and curved regimes;
- its home/fixed/aligned penalty shrank to about 1%;
- in the aligned cell, RFD reduced centre-path error by 60.5% while parent RFM
  retained a 1% reconstruction advantage.

The aligned result is central: a model may reconstruct the sum accurately while
misallocating it between centre drift and factor amplitude. The experiment is
known-rank reconstruction evidence, not forecasting or automatic rank
selection. The canonical adjudication is
`results/final/parent_rfd_bw_parity_adjudication/report.md` and the executed
figure lab is `notebooks/parent_rfd_bw_parity_plot_lab.ipynb`.

## 4. Real APP-FIN illustration

Use the parent's rebuilt 240-month, 12-stock realised-covariance panel under
Bures--Wasserstein geometry. Fit literal parent RFM and RFD at fixed \(r=2\),
matching the parent's published specification without calling it the true rank.
Report:

1. intrinsic centre-path motion and uncertainty;
2. the portion of that motion inside and outside the parent loading span;
3. loading-space and reconstruction sensitivity;
4. how the leading persistent direction and its VIX interpretation change;
5. BW numerical margins, convergence, and fallback diagnostics;
6. ranks \(1,\ldots,15\) only as a labelled sensitivity envelope.

APP-FIN has no ground-truth centre/factor split, factor amplitudes, or rank. It
can show that the fixed-centre assumption is empirically consequential; it
cannot establish that RFD predicts better or that either decomposition is
economically causal.

## 5. Freeze

After APP-FIN, stop adding scientific branches. Freeze the manuscript claims,
notation, configurations, generated tables, plots, environment, and public
supplement. Forecasting, score filtering, predictive rank, state-space/VAR
dynamics, future-centre estimation, continuous drift phase diagrams, and
streaming implementation form the next application paper.

## Proposed main-text allocation

| section | job | approximate length |
|---|---|---:|
| Introduction | the centre-drift/factor question and protected parent comparison | 2.5 pages |
| Model and identification | separability, quotient, and impossibility boundary | 3.5 pages |
| RFD estimator | centre, polygon/frame, lag row, loading space, reconstruction | 4 pages |
| Theory | robust theorem, rate, assumptions, and proof map | 3 pages |
| Synthetic evidence | rates, placebos, paired orientation boundary | 4.5 pages |
| APP-FIN and limitations | fixed-rank real-data sensitivity and honest nonclaims | 2.5 pages |

Target: roughly 20 pages before references, with detailed proofs and full
reproduction artifacts in the repository supplement.

## Scope lock

Paper 1 claims identification, estimation, and controlled reconstruction. It
does not claim automatic rank recovery on APP-FIN, structural recovery of
factor amplitudes, predictive dominance, or a finished forecasting model.

Related canonical sources: [[Paper 1 — Locally stationary Riemannian factor model]],
[[P1-ID — centre-drift and factor identification boundary]],
[[Numerical suite — theorem-driven design matrix]], and
[[Future application programme — factor scores, predictive rank, and online RFD]].
