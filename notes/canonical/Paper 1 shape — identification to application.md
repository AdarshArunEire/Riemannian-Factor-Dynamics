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

The completed centre-detectability adjudication supplies the application
boundary rather than a real-data victory. Across 20 leave-one-year-out folds,
the global, positive-local, and full Richardson BW RMS errors were 5.033,
4.954, and 8.479. Thus the ordinary local path lowered squared BW loss by
3.1%, but won only 10 of 20 years and had approximately zero median annual
improvement. Full Richardson increased squared BW loss by 183.8%, with severe
losses concentrated around 2004--2010. This was not merely a solver failure:
five annual fits invoked the declared domain fallback, no positive stage was
nonconvergent, and catastrophic losses also occurred in no-fallback folds.

The fixed-centre block null was suggestive but not rejected at 5%: observed
motion energy 2.984, null median 1.058, null 95th percentile 3.630, and
\(p=0.07\) from 99 replicates. Both alternating tuning halves selected 0.2
retention of the global-to-Richardson displacement. The corresponding
opposite-half BW improvements were 6.3% and 15.7%, but paired year-block
intervals crossed zero. Therefore Paper 1 says:

> On monthly APP-FIN, centre movement is plausible and modestly useful after
> regularisation, but the sample does not decisively distinguish it from a
> dependent fixed-centre null and the full signed correction is
> finite-sample variance dominated.

This does not retract the assumption-to-conclusion Richardson theorem or the
controlled large-\(n\) synthetic evidence. It bounds the flagship application
claim at \(n=240\). Exact scale/coefficient redesign, causal regularisation,
and higher-frequency panels belong to [[Future application programme — factor
scores, predictive rank, and online RFD]]. Executed report:
`results/intermediate/appfin_centre_diagnostic/report.md`.

## 5. Freeze

After this APP-FIN boundary, stop adding scientific branches. Freeze the manuscript claims,
notation, configurations, generated tables, plots, environment, and public
supplement. Forecasting, score filtering, predictive rank, state-space/VAR
dynamics, future-centre estimation, continuous drift phase diagrams, and
streaming implementation form the next application paper.

The first post-freeze experiment is intentionally small: APP-MONTHLY-VAR
reuses the parent's 240-month panel and exact 204/36 expanding VAR(1) forecast
protocol at fixed \(r=2\), adding only a causal one-sided RFD centre path and a
one-month terminal-centre carry. It validates the forecasting bridge without
being imported back into Paper 1. The declared application home after that is
the gated 20-asset hourly crypto study in
[[Home application — hourly crypto realised covariance]].

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
