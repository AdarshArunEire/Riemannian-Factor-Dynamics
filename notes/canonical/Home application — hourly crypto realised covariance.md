---
type: canonical-application-spec
title: Home application — hourly crypto realised covariance
aliases:
  - APP-HF-CRYPTO
  - Hourly crypto RFD
status: paper-1-empirical-gate-frozen
verdict: The compact 20-asset one-hour-ahead study is complete; matched rank-19 VAR gives a formal RFD/RFM tie with lower RFD mean loss on all four reported metrics
last-audited: 2026-08-29
area:
  - finance
  - realised-covariance
  - forecasting
  - application
tags:
  - canonical-application
  - paper-1
  - crypto
  - causal-forecasting
---

# Home application — hourly crypto realised covariance

## 0. Decision

The completed home application and final empirical gate for Paper 1 is:

> Separate a slowly moving covariance baseline from lag-persistent co-movement
> in a liquid 20-asset crypto market, then forecast the next hour's covariance.

This result is not a claim that crypto verifies every theorem assumption.
Continuous trading supplied enough consecutive hourly matrices to estimate a
moving centre, and the matched rank-19 VAR comparison ended in a formal tie
with lower RFD mean loss on all four reported metrics. This is a compact
fixed-rank result, not the beginning of the broader adaptive or online
application programme.

### Paper 1 scope cut

Paper 1 includes APP-HF-0, APP-HF-1, APP-HF-2, and APP-HF-4. APP-HF-3 is a
diagnostic sensitivity: parent-style VAR(1) is primary and the existing Kalman
head may be reported without becoming a tuning branch. APP-HF-5, adaptive rank,
learned centre or score heads, streaming deployment, online experts, and the
full competitor zoo remain outside Paper 1. Any failed gate is itself the final
application result; it does not license a new estimator family.

## 1. Observation contract

The primary panel is fixed before evaluation:

- 20 liquid spot crypto assets from one venue and one quote currency;
- assets selected using a pre-sample liquidity rule;
- stablecoins, leveraged tokens, and wrapped duplicates excluded;
- no silent survivor replacements; delistings and missing intervals are
  recorded as data events;
- official one-minute spot klines, synchronized in UTC and converted to
  one-minute log returns;
- one non-overlapping \(20\times20\) realised-covariance matrix per hour,
  using up to \(60\) intrahour returns;
- a fixed, declared SPD regularisation rule applied before any model sees the
  matrix.

The frozen panel is 2024-01-01 through 2025-12-31, giving at most
\(n=17{,}544\) hourly observations before data-quality exclusions. The
symmetric tangent dimension is

\[
p=\frac{20(21)}2=210.
\]

The first data release targets those two complete calendar years: one for
burn-in, training, and validation, and one for a causal forecast evaluation.
The split, asset list, regulariser, and missing-data policy are frozen before
final losses are read.

Asset selection is causal and two-stage. Over 2023-Q4 only, retain the 30
eligible candidates with the highest median daily quote volume, then select the
20 with the highest daily log-return volatility inside that liquid pool. This
is a liquid-first, volatile-second rule; it seeks an informative application
without selecting on 2024--2025 centre motion. Volatility does not prove a
moving centre. APP-HF-1 may still reject the home hypothesis.

### Protocol amendment ledger

**2026-08-27 — raw frequency changed before data inspection.** The original
plan used official one-second bars aggregated to synchronized ten-second
returns, about 360 returns per hourly covariance. Before downloading or
inspecting the panel, that contract was replaced by official one-minute klines,
at most 60 returns per hourly covariance. The reason was data and computation
scale: the original two-year, 20-asset design implied roughly 1.26 billion raw
asset-second rows, while the minute contract implies roughly 21 million. The
scientific unit remains one non-overlapping hourly covariance and the primary
forecast horizon remains one hour; six- and 24-hour horizons are declared
sensitivities. Sub-hour covariance targets are excluded because 5- or 15-minute
windows cannot identify a full \(20\times20\) sample covariance without making
regularisation, rather than data, carry most directions.

This amendment changes proxy precision and therefore must remain visible in
the paper. It does not change the centre, rank, or forecast method after seeing
an outcome. The executable contract is `config/hf0_crypto.yaml`.

Every matrix records its minimum eigenvalue, condition number, ridge applied,
number of valid intrahour returns, missing-or-no-trade fraction,
unchanged-close fraction, and any BW domain or fallback event. Periodicity is
estimated using training data only; raw-data results remain as a robustness
view because removing clock effects changes the estimand.

**2026-08-27 — availability metric corrected after the first full preflight,
before APP-HF-1.** The original implementation called the union of missing
bars, no-trade bars, and unchanged consecutive closes “staleness” and compared
its 99th percentile with the frozen 25% limit. It returned 38.21%. A hostile
decomposition showed 100% raw coverage and 60/60 complete returns; the
missing-or-no-trade fraction had 8.63% at its 99th percentile and 16.33% at its
maximum, whereas unchanged closes alone reproduced the 38.21% tail. An
unchanged close with positive trades is an observed zero close-to-close return,
not an unavailable bar. The 25% threshold is therefore unchanged but now gates
missing-or-no-trade minutes. Unchanged-close frequency remains separately
reported as a proxy-resolution diagnostic. The original boundary report and
summary are preserved with `pre-metric-correction-2026-08-27` filenames on the
first corrected rerun. This is a metric-definition repair, not a threshold
relaxation or model-result retuning.

## 2. What is being estimated

The centre path is a slowly evolving geometric covariance baseline. The lag
operator seeks a low-dimensional tangent subspace of co-movements that persist
at nonzero lags around that baseline. The centre/factor split is not identified
by the observed path alone: it inherits the convention and separation
conditions of [[P1-ID — centre-drift and factor identification boundary]].

The one-hour forecast target is the next conditional covariance, observed
through the next hour's realised covariance proxy. Loading directions are
interpreted as persistent co-movement directions. Projected scores are noisy
coordinates, not automatically structural factor amplitudes.

## 3. The causal programme

### APP-MONTHLY-VAR — implementation bridge

Before the high-frequency study, run a compact forecasting bridge on the
existing 240-month, 12-stock APP-FIN panel:

- initial training months \(1{:}204\), followed by 36 one-step expanding
  forecasts;
- fixed rank \(r=2\) and lag horizon \(h=6\), matching the parent;
- the same OLS VAR(1) with intercept in both arms, refitted at every origin;
- literal parent RFM holds its first-training-window global BW centre fixed, as
  the published code does;
- RFD estimates its centre path using observations available at that origin
  only and carries the terminal causal centre forward one month;
- both arms use identical forecast origins, covariance inputs, factor-dynamics
  code, and losses.

This is a low-power, \(n=240\) implementation bridge. It can reveal leakage,
convention, or centre-policy effects. It cannot identify the true rank,
structural factor amplitudes, or a population forecasting advantage.

The bridge is complete. Across all 36 causal origins, positive broad,
piecewise-6, and piecewise-12 polygon paths remained SPD without clipping.
Piecewise-6/VAR and piecewise-12/VAR lowered squared BW loss relative to
parent/VAR by 6.3% and 5.7%, but neither dominated under Frobenius or QLIKE.
Full Richardson was catastrophically unstable under both heads. Kalman
filtering produced no consistent loss improvement and did not rescue the signed
centre. The predeclared one-standard-error practical choice is piecewise-6;
piecewise-12 is sensitivity only. This is the low-sample boundary that motivates
the hourly gate, not evidence of forecast dominance. See
`results/intermediate/appfin_centre_head_tournament/report.md`.

### APP-HF-0 — data and proxy preflight

Construct the frozen panel and audit synchronization, missingness, microstructure
noise, covariance regularisation, spectral margins, seasonality, dependence,
and effective intrahour sample size. Failure stops the application or changes
the declared observation process before evaluation begins.

### APP-HF-1 — centre gate

On blocked training/validation periods compare:

1. one global BW centre;
2. one broad positive local BW path;
3. continuous piecewise-6 and piecewise-12 BW polygon paths;
4. the full three-scale Richardson path as a negative-control candidate.

Use held-out proxy-robust covariance losses, path stability, effective local
sample size, compatibility/fallback diagnostics, and a dependence-preserving
constant-centre null. If global wins, reject moving-centre RFD for this panel.
Freeze the winning positive rule on training/validation data only; use
piecewise-6 as the predeclared lower-complexity choice when it lies within one
standard error of the best candidate. If a positive local path wins but
Richardson loses, retain the winning positive estimator and report that the
theorem-valid full correction is finite-sample inefficient. If global wins or
jumps dominate, reject smooth moving-centre RFD for this panel.

The executable gate is frozen in `config/hf1_centre_gate.yaml` and
`experiments/run_hf1_centre_gate.py`. It uses the first 52 complete UTC weeks
of 2024 only; the final 48 hours of leap-year 2024 are unused and all of 2025
remains sealed. Two complementary folds hold out every week exactly once, with
a 24-hour edge removed from every adjacent training week. A moving method is
eligible only if its paired weekly improvement exceeds one standard error
under both squared Frobenius loss and QLIKE. Among eligible methods, a minimax
two-loss rule applies, with the declared piecewise-6 lower-complexity
preference when it lies within one standard error. Squared BW loss is
descriptive and cannot select the method.

The constant-centre null permutes complete 168-hour weeks. It therefore
preserves within-week dependence and hour-of-week structure while destroying
slow calendar order. It uses 49 predeclared permutations. A null p-value above
0.05, a global one-standard-error verdict, or a selected path whose largest
edge supplies more than half of total edge energy stops the smooth
moving-centre branch. Richardson is computed and diagnosed but never
selectable. The 16-week, three-permutation smoke profile passed its executable
tests; its provisional numbers are explicitly non-scientific.

**Recorded APP-HF-1 adjudication, 2026-08-27.** Both piecewise paths beat the
global centre out of block: piecewise-6 reduced Frobenius/QLIKE/BW loss by
2.22%/16.06%/21.20%, and piecewise-12 by 2.42%/18.61%/22.65%. The complete-week
null distinguished the piecewise-6 movement at the smallest attainable
(p=0.02). The executable nevertheless emitted
`REJECT_SMOOTH_MOVING_CENTRE__JUMP_DOMINATED` because 57.35% of the selected
piecewise-6 edge energy lay in one coarse chord, above the exploratory 50%
guard.

The project lead does not consume that edge-share guard as a model gate. It is
not a theorem condition, the polygon remains continuous along the chord, and a
post-run mechanism audit found that PEPE supplied approximately 88% of the
large January--March edge. Its fixed price tick was about 86 basis points at
the median 2023-Q4 price, so the one-minute covariance proxy carried a declared
microstructure-resolution pathology. The original output remains preserved as
an audit record; edge concentration is descriptive only. Piecewise-6 is frozen
for APP-HF-2 by the predeclared lower-complexity rule. This decision does not
claim smoothness, remove PEPE, or retroactively alter the HF-1 losses.

### APP-HF-2 — matched representation

Fit parent RFM and piecewise-6 RFD on identical matrices. The first 26 complete
weeks of 2024 choose rank independently for each arm under the same rank-
1-through-21 one-standard-error rule; those two ranks are frozen on the final
26 complete weeks. Within each half, complementary weekly folds keep every
scored observation out of its centre and lag-space fit, and six hourly lags use
only genuine within-block pairs. Compare centre diagnostics, loading stability,
reconstruction, lag spectra, residual dependence, and numerical margins. The
complete rank-1-through-21 same-rank curve is mandatory: the independently tuned headline is a
fair operational contest, while the curve isolates centre preprocessing from
retained dimension. This stage is not a forecast contest and therefore has no
VAR or Kalman head. All of 2025 remains sealed.

The executable contract is frozen in `config/hf2_representation.yaml`,
`experiments/run_hf2_representation.py`, and
`sandbox/run_hf2_representation.ps1`. Its 8-week-per-half smoke profile is
non-scientific; it exists only to verify the full BW, cache, report, and plot
path before the recorded run.

**Recorded verdict (2026-08-28).** The full 52-week 2024 experiment completed:
26 weeks selected rank and 26 disjoint weeks evaluated it. Both arms selected
rank 19. At that operational rank, piecewise-6 RFD had 3.74% higher mean
Frobenius loss, 4.18% higher mean QLIKE, and 0.26% higher mean BW loss than
global RFM. The blockwise reading is narrower than the automatic
`PARENT_RFM_REPRESENTATION_WINS` label: parent RFM won Frobenius in 20 of 26
weeks, while the paired QLIKE and BW differences were unresolved. The terminal
claim is therefore **no selected-rank representation gain**, with a modest and
week-consistent parent Frobenius advantage—not universal parent dominance.

The same-rank mechanism curve contains the scientifically useful positive
result. At rank 1, RFD reduced mean Frobenius, QLIKE, and BW loss by 12.12%,
6.74%, and 8.16%, respectively, and won 23/26, 18/26, and 22/26 weekly blocks.
The first loading direction was also slightly more stable under RFD across the
two evaluation folds: largest angle 11.56 degrees versus 14.01 degrees for the
parent. Both arms found almost the same leading direction, with cross-arm
canonical correlations 0.991 and 0.984. Hence RFD improves **aggressive
one-direction compression**, not the validation-selected high-rank
reconstruction.

The lag spectrum has one dominant persistent direction: the second eigenvalue
is only about 2.0--3.3% of the first. Directions beyond the first are much less
stable—the rank-2 fold comparison already has an approximately 82--84 degree
largest angle, and the rank-19 loading spaces are nearly orthogonal across
folds. Rank 19 is therefore an operational reconstruction dimension, not a
claim that the panel contains nineteen stable structural factors. The recorded
run was numerically safe and left all of 2025 sealed. Authoritative generated
outputs are `results/intermediate/hf2_crypto_representation/report.md` and the
retained block rows in `evaluation_scores.csv`.

### APP-HF-3 — score observation model

APP-HF-3 is a compact 2024-only diagnostic and score-materialisation step, not
a new estimator-selection gate. Its prerequisites are now frozen:

1. reuse the global parent centre and piecewise-6 RFD centre selected before
   HF-2; neither centre rule may be retuned;
2. use rank 19 in both arms for the operational HF-4 forecast, while retaining
   rank 1 only as a labelled compression/mechanism diagnostic;
3. construct out-of-fold 2024 projected-score rows for both arms under the same
   coordinates, six genuine within-block lags, masks, and origins used by HF-2;
   HF-2 stores the polygons and identity-coordinate loadings, so HF-3 recreates
   the scores without refitting any centre or lag operator;
4. quantify only observable diagnostics—VAR innovation covariance and serial
   dependence, fitted transition radius, score/reconstruction residuals, and
   forecast-origin state uncertainty. With no latent truth in crypto, this
   stage cannot report a structural factor-amplitude error or noise floor;
5. retain parent-style VAR(1) with intercept as the Paper 1 primary head. The
   already implemented linear state-space/Kalman filter is a frozen, labelled
   sensitivity only because the synthetic and monthly audits did not show a
   consistent forecast improvement; and
6. preserve strict arm parity. Parent RFM and RFD receive the same head code,
   information, hyperparameters, and origins. No 2025 outcome is opened or used.

APP-HF-3 may diagnose whether projected scores look hostile to VAR, but it may
not reselect rank, centres, lags, or heads and cannot delay or expand Paper 1.
Loading-space recovery remains distinct from factor-amplitude recovery.

The executable contract is `config/hf3_score_diagnostic.yaml`,
`experiments/run_hf3_score_diagnostic.py`, and
`sandbox/run_hf3_score_diagnostic.ps1`. The recorded run completed on
2026-08-28: all four phase/fold sources materialised, the arm/gauge and
within-week transition guards passed, and only 2024 was loaded. At rank 19,
the parent/RFD blocked-VAR variance explained was 52.36%/40.65%, innovation
share was 47.64%/59.35%, and transition radius was 0.942/0.836. Maximum
residual lag dependence was small and nearly equal at 0.0547/0.0569. Thus both
score processes support a finite stable VAR diagnostic, but the parent scores
are materially more one-step predictable in 2024. This is not a forecast-loss
comparison and does not reopen the frozen head policy. Authoritative output:
`results/intermediate/hf3_crypto_scores/report.md`.

### APP-HF-4 — one-hour causal forecast

The executable contract is now frozen in `config/hf4_forecast.yaml` and
`experiments/run_hf4_forecast.py`. The 2024 panel is development-only. It
selects the EWMA decay from the declared grid; no 2025 loss selects any method,
rank, centre rule, lag, or refit frequency.

The recorded comparison covers all 8,760 hours of 2025. Parent RFM and
piecewise-6 RFD refit every 672 hours on the trailing 4,368 hours (26 weeks),
use the same six-lag operator and the same OLS VAR(1) head, and carry the final
fitted centre through the next four-week forecast block. Revealed hour (t)
updates the projected score used to forecast hour (t+1); it never enters its
own forecast. Up to eight workers evaluate the 14 independent refit blocks, with one
atomic digest-checked cache per block.

Rank 19 with VAR(1) is the sole original operational headline inherited from
HF-2. All ranks 1--18 are same-rank compression sensitivities: they may show
where RFD and the parent differ, but cannot retrospectively select a winner.
The non-geometric baselines are LOCF, development-tuned EWMA, and a
coordinatewise HAR model in matrix-log coordinates mapped back to SPD. Primary
losses are squared Frobenius and QLIKE, with paired rank-19 differences given
168-lag Bartlett Newey--West intervals; BW and GMV realised-variance/calibration
are descriptive.

The original recorded VAR run is complete. Across all 8,760 target hours, RFD
reduced rank-19 mean loss relative to the parent by 2.48% Frobenius, 13.26%
QLIKE, 2.18% BW, and 7.69% GMV realised variance. The paired Newey--West
intervals for the two primary losses crossed zero, so the formal original
rank-19 verdict is a tie rather than RFD dominance. Log-SPD HAR had the best
mean Frobenius loss and EWMA the best mean QLIKE. These are compatible with a
modest RFD advantage concentrated in difficult periods, not a claim that RFD
dominates classical covariance forecasters.

The later matched coordinatewise OLS HAR and ridge-VHAR score-head augmentation
is excluded from Paper 1. It is retained under the same HF-4 result directory
as internal diagnostic fuel for the follow-up application programme, but it is
not a manuscript result, figure, table, freeze gate, or alternative headline.
This retcon does not remove log-SPD HAR as a classical external baseline. The
published RFD/RFM comparison uses the matched VAR(1) head only.

Focused tests and a 48-hour development-only smoke pass. An earlier disposable
smoke was mistakenly pointed at the first 48 hours of 2025; the design and all
choices had already been frozen, none was changed after viewing it, its outputs
were overwritten, and no scientific claim uses it. The final run is therefore
fully predetermined, although not represented as pristine blinded evaluation.
The same one-line runner, `sandbox/run_hf4_forecast.ps1`, preserves the cached
geometric representations and all diagnostic rows. Publication code must
select only the native classical baselines and matched VAR(1) RFD/RFM rows.

The first recorded launch failed before completing any refit block because the
coordinate map materialised a (4368\times210\times20\times20) BW broadcast,
requesting 2.73 GiB per worker. This was a computational workspace defect, not
a model or data failure. `tangent_coordinates` now evaluates independent sample
rows in exact batches of at most 64. The batched output equals rowwise output,
and an isolated test of the original (4368\times210) target completed with a
7 MiB output and no large broadcast. No partial scientific block survived the
failed launch; the digest includes the repaired code.

### APP-HF-5 — external validation

Repeat the frozen protocol on a 20-stock high-frequency US-equity panel after
explicit market-hours, intraday-seasonality, asynchronous-trading, and overnight
policies. This tests whether the result is crypto-specific; it is not used to
retune the crypto headline.

## 4. Competitors and losses

The compact Paper 1 benchmark set is:

- LOCF and EWMA;
- HAR-style covariance forecasting in a declared SPD parameterisation;
- parent fixed-centre RFM with projected-score VAR(1);
- RFD with the frozen positive polygon centre and the same VAR(1) head.

Conditional Wishart/F-Riesz dynamics, broader factor/state-space models, and
modern SPD networks remain valuable follow-up competitors. They enter Paper 1
only if an already reproducible implementation fits the frozen target and split;
their absence does not trigger new engineering before the scope lock.

Primary forecast losses are squared Frobenius and multivariate QLIKE because
their target/proxy relationship is admissible under
[[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]]. BW,
AIRM, or log-Euclidean scores are descriptive unless their induced target and
recalibration are stated. Secondary economic diagnostics may include
minimum-variance portfolio realised variance, variance calibration, and VaR,
but they do not replace covariance losses.

## 5. Decision graph

\[
\begin{array}{c}
\text{APP-MONTHLY-VAR code bridge}\\
\downarrow\\
\text{APP-HF-0 data/proxy pass}\\
\downarrow\\
\text{APP-HF-1 moving-centre pass}\\
\downarrow\\
\text{APP-HF-2 qualified cost plus rank-1 compression gain}\\
\downarrow\\
\text{APP-HF-3 diagnostic sensitivity (non-gating)}\\
\downarrow\\
\text{APP-HF-4 one-hour forecast}\\
\downarrow\\
\text{Paper 1 freeze.}
\end{array}
\]

Any failed gate is a scientific result. It narrows or rejects the application
instead of authorising post-hoc retuning.

## 6. Non-claims

This specification does not claim that:

- the empirical centre/factor split is unique without the P1-ID convention;
- rank \(r=2\) is correct outside the monthly parent bridge;
- projected scores equal latent factor amplitudes;
- hourly realised covariance is noise-free;
- full Richardson correction must beat a positive or shrunk local centre;
- a BW forecast loss targets the conditional arithmetic covariance mean; or
- success on crypto implies success on equities.

APP-HF-5 equity transfer and the downstream structural-score, predictive-rank,
future-centre, learned-head, and online-update questions remain in [[Future application programme — factor scores, predictive rank, and online RFD]].
