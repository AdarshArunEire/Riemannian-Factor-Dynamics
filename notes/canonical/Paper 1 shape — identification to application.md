---
type: paper-shape
title: Paper 1 shape — identification to application
status: current-spec
last-audited: 2026-08-29
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
\text{compact hourly-crypto gate}
\longrightarrow
\text{freeze}.
\]

That is the whole first paper. Its central contribution is not a faster rate or
a universal forecasting victory. It identifies when centre drift and a
persistent factor can be separated, builds an estimator for the separated
objects, shows where the distinction matters, and ends with one compact causal
application gate. The application may pass, tie, or fail; every outcome closes
the paper without authorising post-hoc retuning.

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
claim at \(n=240\). Exact scale/coefficient redesign and learned or adaptive
centre rules belong to [[Future application programme — factor scores, predictive rank, and online RFD]]. Executed report:
`results/intermediate/appfin_centre_diagnostic/report.md`.

The completed 36-origin causal tournament adds a deliberately narrow forecast
boundary. The literal parent global centre, broad positive RFD, continuous
piecewise-6 and piecewise-12 polygon paths, and full Richardson path were each
paired with the same VAR(1) and Kalman score heads at fixed \(r=2\). Positive
polygon paths remained SPD without clipping. Piecewise-6/VAR and
piecewise-12/VAR improved squared BW loss over parent/VAR by 6.3% and 5.7%, and
piecewise-12/VAR had the best median realised minimum-variance portfolio ratio;
neither dominated the parent under Frobenius or QLIKE. Richardson/VAR was
numerically unstable (QLIKE 1717.4 versus 11.12 for parent/VAR), while Kalman
filtering neither consistently improved losses nor rescued Richardson. Hence
monthly APP-FIN is a low-\(n\) boundary, not the claimed home domain. The
predeclared one-standard-error choice is piecewise-6; piecewise-12 is a labelled
sensitivity. Executed report:
`results/intermediate/appfin_centre_head_tournament/report.md`.

## 5. Compact hourly-crypto gate

Paper 1 now includes one final empirical sequence on a frozen 20-asset hourly
crypto realised-covariance panel:

1. **APP-HF-0:** construct and audit the proxy, synchronization, missingness,
   regularisation, spectral margins, seasonality, and dependence;
2. **APP-HF-1:** select the centre rule on training/validation only, with global,
   broad-positive, piecewise-6, piecewise-12, and Richardson negative-control
   candidates;
3. **APP-HF-2:** compare parent RFM and the frozen piecewise-6 RFD on identical
   matrices. Each arm chooses rank 1--21 on the first 26 weeks and freezes it
   for the last 26; the complete same-rank curve remains the mechanism check.
   **Complete:** both chose rank 19. Parent had a modest, week-consistent
   Frobenius advantage there, with QLIKE/BW unresolved; RFD instead won the
   rank-1 compression comparison by 6.74--12.12%. The result is no operational
   representation gain plus a genuine aggressive-compression benefit. Rank 19
   is not interpreted as nineteen stable factors. This stage has no forecast
   head and leaves 2025 sealed;
4. **APP-HF-4:** the frozen one-hour-ahead causal forecast comparison is
   complete over all 8,760 hours of 2025. Rank-19 VAR(1) is the sole RFD/RFM
   score head in Paper 1 and all ranks 1--18 are labelled sensitivities only.
   Both geometric arms refit every four weeks on the trailing 26 weeks with the
   same six-lag OLS VAR(1). LOCF, 2024-tuned EWMA, and log-SPD HAR supply the
   classical baselines. Squared Frobenius and QLIKE adjudicate the result; BW
   and GMV diagnostics describe it. RFD's mean rank-19 losses were lower than
   the parent's by 2.48%, 13.26%, 2.18%, and 7.69%, respectively, but the
   paired primary-loss intervals crossed zero, giving a formal tie. The
   mean-versus-median contrast is retained as descriptive evidence that the
   gain is concentrated in large-error hours, not as a proved stress-regime
   effect.

Before HF-4, APP-HF-3 materialised matched out-of-fold 2024 scores at frozen
rank 19 and recorded their observable innovation and residual diagnostics. It
did not retune centres, ranks, lags, or heads and did not open 2025. VAR(1) is
the primary score head. The already implemented Kalman head is a diagnostic
sensitivity only and APP-HF-3 is not an independent paper gate.
Every forecast head has strict arm parity: the same implementation,
information, tuning, and origins are used for parent RFM and RFD. A Kalman or
other head cannot be added to only one arm.
Primary losses are squared Frobenius and multivariate QLIKE; intrinsic losses
and portfolio diagnostics remain secondary and are interpreted under
[[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]]. A
failed data, centre, representation, or forecast gate is a publishable scope
boundary and ends the application without tuning on the evaluation period.
The complete frozen specification is [[Home application — hourly crypto realised covariance]].

## 6. Freeze

APP-HF-4 is adjudicated and the scientific layer is now frozen. No further
experiment is on the Paper 1 critical path. Remaining work is manuscript and
release engineering: notation, reader-facing documentation, packaging, figure
regeneration, citation completion, and an immutable tag. Adaptive or
time-varying rank, learned centre/score heads, online experts and refit
scheduling, streaming deployment, the full competitor zoo, and the US-equity
transfer form the follow-up application programme.

## Proposed main-text allocation

| section | job | approximate length |
|---|---|---:|
| Introduction | the centre-drift/factor question and protected parent comparison | 2.5 pages |
| Model and identification | separability, quotient, and impossibility boundary | 3.5 pages |
| RFD estimator | centre, polygon/frame, lag row, loading space, reconstruction | 4 pages |
| Theory | robust theorem, rate, assumptions, and proof map | 3 pages |
| Synthetic evidence | rates, placebos, paired orientation boundary | 4.5 pages |
| APP-FIN and limitations | fixed-rank sensitivity, low-\(n\) forecast boundary, and honest nonclaims | 3 pages |
| Hourly crypto gate | frozen data/centre/representation/one-hour forecast sequence | 3 pages |

Target: roughly 22 pages before references, with detailed proofs and full
reproduction artifacts in the repository supplement.

## Scope lock — authoritative from 2026-08-27

This section supersedes every older statement that Paper 1 freezes before
forecasting. Paper 1 includes identification, estimation theory, controlled
known-rank reconstruction, the fixed-rank monthly APP-FIN boundary, and one
compact fixed-rank hourly-crypto forecast gate. It does **not** claim automatic
or time-varying rank recovery, structural factor-amplitude recovery, universal
predictive dominance, learned centre or score heads, online model selection,
streaming deployment, exhaustive competitor coverage, or cross-market external
validity. APP-HF-5 equity transfer is outside Paper 1.

Related canonical sources: [[Paper 1 — Locally stationary Riemannian factor model]],
[[P1-ID — centre-drift and factor identification boundary]],
[[Numerical suite — theorem-driven design matrix]], and
[[Future application programme — factor scores, predictive rank, and online RFD]].
The authoritative frozen result hierarchy is [[Paper 1 final result ledger]].
