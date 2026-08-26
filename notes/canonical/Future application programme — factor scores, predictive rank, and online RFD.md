---
type: canonical-future-programme
title: Future application programme — factor scores, predictive rank, and online RFD
aliases:
  - Online RFD
  - Adaptive-rank RFD
  - Fixed-loading RFD application follow-up
status: parked-after-paper-1
verdict: Paper 1 stops before forecasting; a fixed-rank monthly VAR bridge precedes the declared hourly-crypto home, after which factor-score filtering, predictive rank, future-centre policy, state-space dynamics, and learned refit scheduling form one application programme
last-audited: 2026-08-25
area:
  - geometry
  - time-series
  - factor-models
  - online-learning
tags:
  - canonical-programme
  - future-application
  - forecasting
---

# Future application programme — factor scores, predictive rank, and online RFD

> **Scope boundary.** This is the canonical application follow-up on the same
> fixed-loading RFD branch as Paper 1. It is the current Paper 2 candidate, not a
> reserved publication label, and it is not the separate
> [[Parked programme — Intrinsically moving loading subspace]]. The expanded
> masked-learning brainstorm remains archived in
> [[Future programme ideation — identifiable geometric learning for RFD]].

## 1. What Paper 1 may claim

The parent RFM and RFD use nonzero-lag relationships to identify the tangent
subspace containing serially persistent dynamics. Paper 1 keeps the scientific
rank fixed within each synthetic series.

- Synthetic theorem and recovery tables use the **known DGP rank** where the
  purpose is to test centre estimation, polygon construction, transport, lag
  recovery, or loading recovery.
- The completed selector sweep is supporting evidence about detectability. It
  is not allowed to confound the fixed-rank BW closure or the literal
  parent/RFD comparison.
- Thresholding is the proved feasible selector when a selector conclusion is
  actually reported. The parent's raw eigenvalue ratio remains a comparator;
  it cannot return rank zero and its consistency does not follow from the
  displayed parent rates alone.
- Paper 1 makes no general claim of latent time-varying-rank recovery.
- Reconstruction is reported as reconstruction, not forecasting; loading-space
  accuracy alone is not an application result.

APP-FIN has no known true rank. Paper 1 therefore uses:

1. the parent's published \(r=2\) as a fixed comparison convention; and
2. ranks \(1,\ldots,15\) only as a labelled sensitivity envelope.

Forecasting and predictive rank are post-freeze. The first forecast bridge also
holds \(r=2\) fixed so it tests the centre and forecast plumbing rather than a
rank policy.

## 2. What the completed rank sweep established

On the equal-strength controlled DGP, centre estimation, polygon construction,
and transport created no visible additional rank-selection boundary:

| \(n\) | oracle threshold accuracy | full RFD threshold accuracy |
|---:|---:|---:|
| 512 | 78.4% | 79.4% |
| 2,048 | 92.0% | 92.5% |
| 8,192 | 100.0% | 100.0% |

The visible boundary was weak dynamic signal. At \(n=8192\), a final factor
with marginal amplitude \(0.2\) was missed almost universally by both oracle
and feasible threshold selectors. The feasible raw ratio missed it in 97.7% of
the relevant cells. Thresholding selected rank zero in every null cell; ratio
selectors cannot return zero.

The exact AR(1) calibration is

\[
\chi_j=s_j^4\sum_{h\in\mathcal H}\rho_j^{2h}.
\]

Thus a factor with one fifth the marginal amplitude has only
\(0.2^4=0.0016\) of the corresponding strong factor's lag-operator eigenvalue
before sampling or geometry error. This supports the interpretation that the
principal rank boundary in this experiment is factor detectability rather than
damage from RFD preprocessing. It is not a minimax impossibility claim.

Authoritative analytical source:
[[P1-RANK — AR1 signal strength and threshold boundary]].

## 3. Loading recovery is not score recovery

After centre removal and common-frame alignment, the tangent observation is
approximately

\[
z_t=Af_t+\delta_t.
\]

The lag operator can recover \(\operatorname{span}(A)\) because the declared
factor persists at nonzero lags while the declared residual noise does not.
Pointwise scores are then obtained by projection,

\[
\widehat f_t=\widehat A^\top\widehat z_t.
\]

Even with the true row and loading directions,

\[
A^\top z_t=f_t+A^\top\delta_t.
\]

Projection removes noise orthogonal to the loading space. It cannot distinguish
the factor from contemporaneous noise pointing inside that space.

At \(n=8192\), the completed AIRM baseline had:

- loading-projector error \(0.010\)–\(0.016\);
- largest loading angle \(0.59^\circ\)–\(0.91^\circ\); and
- factor-score NRMSE \(30\%\)–\(44\%\).

The paired low-sample attribution isolated the discrepancy:

| \(n\) | complete RFD median score NRMSE | oracle rows + true directions |
|---:|---:|---:|
| 240 | 0.962 | 0.276 |
| 512 | 0.747 | 0.279 |
| 2,048 | 0.476 | 0.278 |

The approximately \(28\%\) oracle error is the projected-noise floor on this
DGP. The additional low-\(n\) error came overwhelmingly from the combined
feasible-row bundle—local centre, base-Log recentering, polygon interpolation,
and non-rigid frame transport—not loading-direction estimation. The experiment
does not identify one of those four row subchannels as the cause. A single
scalar rescaling reduced some error but did not repair the trajectory shape.

These are synthetic RFD results. They do not measure latent-factor accuracy in
the parent's APP-FIN data.

Authoritative numerical sources:
results/final/b45_adjudication/ and
results/final/amplitude_diagnostic/report.md.

## 4. What the parent establishes

The parent RFM estimates scores by the same direct projection. Its analytical
results cover the global Fréchet mean, lag operator, loading space,
lag-operator eigenvalues, and factor-number selection. Its dimension-free
\(n^{-1/2}\) result is a loading-space rate, not a rate for

\[
\|\widehat f_t-Hf_t\|
\quad\text{or}\quad
\|\widehat A\widehat f_t-Af_t\|.
\]

The orthogonal \(H\) only resolves rotation, permutation, and sign gauge.

The projected scores are used in two different tasks:

1. **Held-out reconstruction/pseudo-prediction.** An observed tangent row is
   projected and reconstructed. Noise inside the loading space may improve
   reconstruction without implying accurate recovery of \(f_t\).
2. **Genuine forecasting.** Training scores are projected, a VAR(1) is fitted,
   and future scores are forecast. The VAR receives noisy projected scores; it
   does not replace projection with latent-state filtering.

If a latent factor is VAR(1) but its projected observation contains additive
measurement noise, the observed score process is generally VARMA-like. A
direct VAR can remain a useful reduced-form forecaster, but it is not an
explicit latent-state filter and may exhibit errors-in-variables effects.

The unresolved interpretation question is:

> Are projected scores intended as estimators of structural latent factors, or
> as observable low-dimensional coordinates containing persistent factors plus
> projected contemporaneous noise?

The structural interpretation needs an additional identification or
vanishing-noise condition. Without one, interpretation should concern
persistent co-movement rather than exact absolute amplitudes.

## 5. APP-FIN reproduction boundary

The parent pipeline has been reproduced closely enough to establish
implementation credibility:

| RFM statistic | published | reproduction | gap |
|---|---:|---:|---:|
| BW mean | 2.22 | 2.239 | 0.9% |
| BW median | 2.00 | 2.026 | 1.3% |
| Frobenius mean | 10.79 | 10.97 | 1.7% |
| Frobenius median | 7.14 | 7.077 | 0.9% |
| risk mean | 0.94 | 1.001 | 6.0% |
| risk median | 0.52 | 0.5785 | 10.1% |

All published RFM/LFM/LOCF/EWMA rankings were preserved, and the independent
evaluation implementations agreed on the rebuilt panel to roundoff. Exact
reproduction was impossible because the original realised-covariance panel was
not published; the reconstructed adjusted-close panel may differ through data
revisions and effective trading-day conventions.

There is no APP-FIN score-recovery truth because its latent financial factors
are unobserved. VIX co-movement is external interpretive evidence, not
ground-truth amplitude recovery.

Authoritative source: results/final/parent_reproduce.md.

## 6. Why evaluating every candidate rank is cheap

Let

\[
\widehat A_R=[\widehat a_1,\ldots,\widehat a_R].
\]

Rank \(r\) uses the first \(r\) columns. Centre estimation, manifold Log maps,
polygon transport, common-reference rows, lag covariances, and the lag-operator
eigendecomposition are shared. Maximum-rank scores are calculated once,

\[
F_R=Z\widehat A_R,
\]

and every smaller model uses a prefix. Only a small rank-specific forecasting
fit and reconstruction remain.

For APP-FIN, \(m=12\) and the symmetric tangent dimension is

\[
p=\frac{m(m+1)}2=78.
\]

Paper 1 evaluates \(r=0,\ldots,15\), adding the centre-only rank zero to the
parent's rank-1-to-15 sweep. This comparison is negligible relative to repeated
BW centre and matrix-geometric refits. The computational bottleneck is updating
the full geometric pipeline at new forecast origins, not comparing nested
ranks after one fit.

## 7. Valid online rank choice

A historical backtest is genuinely online when every forecast is computed from
the prefix available at its issue time. It need not have been run live in
calendar time.

At forecast origin \(t\):

1. fit or update the common geometric pipeline using observations through
   \(t-1\);
2. issue and store forecasts \(\widehat X^{(r)}_t\) for every
   \(r=0,\ldots,15\);
3. choose the deployed rank or ensemble using losses observed only through
   \(t-1\);
4. observe \(X_t\);
5. score every forecast that was already issued; and
6. update the policy for \(t+1\).

Therefore:

> **The rank need not be frozen. The causal rank-selection policy must be
> frozen.**

Choosing the rank that minimises loss over the complete final 36-month block
and reporting that same loss is leakage. That path is a **retrospective oracle**
and must be labelled as such.

### Minimal later adaptive-rank protocol

When adaptive rank is eventually tested, keep it compact:

1. **Fixed baseline:** choose one rank on training-era rolling validation,
   refit through month 204, and keep that rank for the final 36 months.
2. **Online baseline:** predeclare a lagged follow-the-leader or exponentially
   weighted rank policy, including its loss, memory/discount, learning rate,
   switching rule, and deterministic tie-break. Seed it only with training-era
   validation losses. During the final block, update it only after each
   completed forecast.
3. **Retrospective diagnostic:** compute the best fixed test rank and the
   monthwise oracle-rank path, but never report either as a deployed forecast.

The primary losses remain squared Frobenius and multivariate QLIKE under
[[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]].
Geodesic losses require their induced target and recalibration warning.

An exponentially weighted policy has

\[
w_{r,t}\propto\exp\{-\eta C_{r,t-1}\},
\]

where \(C_{r,t-1}\) is a declared accumulated or discounted loss using only
completed forecasts. It may select the largest-weight rank or combine
rank-specific SPD forecasts. A positive linear convex combination of SPD
forecasts remains SPD. Any standard regret statement additionally requires the
loss boundedness/scaling and comparator class used by that theorem; QLIKE is
not silently treated as bounded.

With only 36 final observations, a complicated learned selector is not
credible. A fixed baseline and one simple frozen online policy are enough for
the first adaptive-rank study.

## 8. Retrospective diagnostics before a larger adaptive programme

On a longer or higher-frequency application, first measure:

- rank dwell times and switching frequency;
- improvement over the best fixed rank;
- uncertainty in that improvement;
- whether switches coincide with eigengap collapse, residual persistence,
  centre acceleration, conditioning deterioration, or market events; and
- whether the apparent switching survives a switching penalty.

Possible verdicts:

1. **one rank dominates:** retain a fixed rank;
2. **rank changes slowly:** periodic causal reselection is sufficient;
3. **rank changes frequently but predictably:** online experts or learned
   selection are justified;
4. **rank changes apparently randomly:** prefer an ensemble or switching
   penalty rather than chasing the latest winner.

These concern **predictive effective rank**. They do not identify a
time-varying population factor rank.

### 8.1 Fixed-rank monthly VAR implementation bridge

Before the high-frequency application, reproduce the parent's causal forecast
loop on the existing APP-FIN panel:

- 240 monthly covariance matrices, with months \(1{:}204\) supplying the
  initial fit and months \(205{:}240\) supplying 36 expanding one-step
  forecasts;
- fixed \(r=2\), lag horizon \(h=6\), and the same OLS VAR(1) with
  intercept for parent RFM and RFD;
- parent RFM estimates its global BW centre on the initial training window and
  holds it fixed, exactly as the published code does;
- RFD uses only observations available at each origin, reconstructs an
  expanding-prefix centre path, and carries its one-sided terminal centre one
  month ahead;
- identical forecast origins, covariance inputs, score-dynamics code, and
  losses in both arms.

This is **APP-MONTHLY-VAR**, an implementation and low-sample diagnostic. It is
not a rank experiment, factor-score truth experiment, or final application.
The authoritative protocol and its non-claims are in
[[Home application — hourly crypto realised covariance]].

The 36-origin run is complete. Parent RFM versus RFD produced mean
Frobenius-squared losses 206.48 versus 241.34 and mean QLIKE 11.12 versus
1717.40. RFD required two guarded decodes, reached a minimum forecast
eigenvalue \(4.16\times10^{-6}\), and accumulated 69 centre-stage fallbacks.
Its fitted VAR transition radii remained below one. The evidence therefore
localises the severe loss to noisy projected scores interacting with the
moving-centre/frame row and BW decoder, rather than an explosive VAR fit.

### 8.1.1 Frozen VAR-versus-Kalman score-head gates

The next experiment changes one component at a time. Within either the parent
or RFD representation, the centre, tangent rows, loading directions, rank,
forecast origins, and BW decoder are identical. Only the score head changes:

\[
\text{projected scores}\longrightarrow
\begin{cases}
\text{OLS VAR(1)},\\
\text{identity-observation linear state space/Kalman filter}.
\end{cases}
\]

APP-BW-SCORE-FILTER runs first because its factors are known. It uses regular
BW draws at \(n=240,512,2048,8192\), true rank two, six fixed/moving and
noise controls, an 80/20 causal split, and oracle, fixed-centre, and feasible
RFD score representations. It measures filtered-amplitude and one-step factor
forecast NRMSE separately from guarded matrix reconstruction.

APP-MONTHLY-HEADS then replays all 36 APP-FIN origins with four arms:
parent–VAR, parent–Kalman, RFD–VAR, and RFD–Kalman. APP-FIN has no latent-score
truth, so its verdict is forecast loss and numerical stability only. The
literal parent one-origin smoke is exact: Python reproduces the R VAR score to
\(1.83\times10^{-15}\) and the parent forecast to \(5.18\times10^{-14}\).
Both Kalman fits converged and no smoke arm clipped. These are integrity facts,
not evidence that Kalman wins.

The decision rule is predeclared. Filtering advances only if it lowers known
synthetic factor-forecast error and then improves or materially stabilises the
APP-FIN replay without systematic compatibility clipping. Failure on either
gate is a useful terminal verdict: the in-span noise is not repaired by this
linear state model, so the hourly application must retain VAR as a baseline
and investigate a different observation/dynamics model on validation data.

### 8.2 Declared high-frequency home and external validation

The declared home uses **20 observed markets**, hence \(p=210\) symmetric
tangent coordinates. Twenty is a computational and covariance-sampling
compromise, not a model constant.

Two panels are ordered as follows:

1. **Continuous crypto panel:** 20 liquid, predeclared assets on one venue,
   one quote currency, synchronized ten-second returns aggregated from official
   one-second bars, and non-overlapping hourly realised covariances. Each matrix
   then uses about 360 intrahour returns; one year supplies about 8,760 matrices.
   Asset inclusion, venue, quote currency, delistings, stablecoins, missing
   bars, regularisation, and survivorship handling must be frozen before the
   evaluation panel is read. Hour/day/week periodicity must be estimated using
   training data only and removed, modelled, or retained in a labelled raw
   robustness run.
2. **Six-year US-equity panel:** 20 predeclared S&P names, regular-session
   minute returns, with equal non-overlapping intraday blocks. Raw clock-time
   seasonality and overnight discontinuities make this the less clean RFD
   design; stratification or a frozen deseasonalisation is mandatory. Daily
   realised covariances are the literature-standard alternative but produce
   only about 1,500 observations in six years, not the desired \(n\approx8192\).

Before forecasting or adaptive rank enters, both panels receive the
centre-detectability package recorded in [[Literature review — external
positioning and prior art]] §2.10: global, positive-local, Richardson, and
global/local-shrunk centre paths on blocked holdouts. Only after that gate do
literal parent RFM and RFD receive the same fixed-rank representation task.
LOCF and EWMA enter only when the task becomes causal forecasting.

The crypto sequence is APP-HF-0 data/proxy preflight, APP-HF-1 centre gate,
APP-HF-2 matched representation, APP-HF-3 projected-score filtering, and
APP-HF-4 one-hour causal forecasting. APP-HF-5 transfers the frozen protocol
to US equities. See [[Home application — hourly crypto realised covariance]]
for the observation contract, competitors, losses, stop rules, and non-claims.

### 8.3 Finite-sample centre extraction after the monthly APP-FIN boundary

The monthly \(n=240\) diagnostic established the problem, not its solution.
Full Richardson raised cross-fitted squared BW loss by 183.8%, whereas positive
local lowered it by 3.1%. Both alternating tuning halves selected 0.2 retention
of the global-to-Richardson displacement. The constant-centre block null gave
\(p=0.07\). This is evidence of a bias--variance boundary: possible centre
motion, insufficient evidence for a structural split, and an unusably noisy
full extrapolation at this resolution.

For scale ratio \(q\in(0,1)\), exact cancellation at bandwidths
\(b,qb,q^2b\) fixes the three coefficients uniquely:

\[
\lambda_1=\frac{q^3}{(1-q)^2(1+q)},\qquad
\lambda_2=-\frac{q}{(1-q)^2},\qquad
\lambda_3=\frac{1}{(1-q)^2(1+q)}.
\]

At \(q=1/2\) these are \((1/3,-2,8/3)\), with absolute mass five. They
remove the first two formal bias powers but amplify stage noise and stage
disagreement; the smallest window is also the noisiest. Moving \(q\) towards
one makes the extrapolation system ill-conditioned. Moving it towards zero
reduces coefficient mass but makes the smallest window drastically shorter.
Therefore ``choose different coefficients'' is not a free repair.

The Paper 2 investigation is ordered:

1. derive the joint bias and covariance expansion of the nested positive
   stages, including the BW Log/Exp anchor and noncommuting curvature terms;
2. map admissible \(q\), bandwidth, kernel, and minimum-effective-sample-size
   regions before looking at predictive outcomes;
3. add at least four scales and solve the covariance-aware minimum-variance
   weights under the same three moment constraints; keep data-dependent weight
   estimation on a separate training colour;
4. compare exact two-bias cancellation with a two-scale/positive-local route
   that accepts more bias for much less variance;
5. study causal damping of the correction and global/local shrinkage. A fixed
   damping below one generally restores lower-order bias, so it needs its own
   rate theorem; a sequence tending to one may preserve the asymptotic rate
   only under an explicit speed condition;
6. rerun the frozen centre gate on the 20-market high-frequency crypto and
   equity panels, reporting BW, QLIKE, and Frobenius targets separately; and
7. only after those analytical baselines compare a state-space or learned
   causal centre head.

Possible verdicts are equally useful: a minimum-variance exact-cancellation
design survives; positive-local dominates throughout and Richardson is only a
theoretical device; regularisation is essential but prediction improves; or
high-frequency data restores the full correction by increasing every local
effective sample size. No branch is preselected.

## 9. Score filtering and learned refit scheduling

The first substantive follow-up should diagnose projected-score noise and
compare direct VAR forecasting with a linear latent state-space or
Kalman/Wiener filter. This directly addresses the factor-amplitude bottleneck
before adding a neural model.

Brute-force rank evaluation is already cheap. The more useful learned decision
is

\[
\boxed{\text{When is the geometric model stale enough to justify a full refit?}}
\]

Candidate trigger features include recent forecast loss, centre velocity or
acceleration, residual nonzero-lag correlation, leading lag eigenvalues,
eigengap shrinkage, threshold decisions, conditioning/margin deterioration,
and disagreement among rank-specific forecasts.

A budget-aware rule targets

\[
\text{refit if expected forecast improvement}
>
\lambda\times\text{computational cost}.
\]

This is event-triggered RFD, not ordinary rank classification. A supervised
trigger should predict whether refitting now improves the next \(H\) forecasts
enough to justify its cost.

## 10. Future programme order

1. freeze Paper 1 with its completed synthetic recovery, literal parent parity,
   and qualified non-forecasting APP-FIN boundary;
2. run APP-MONTHLY-VAR, the fixed-\(r=2\) 204/36 parent-protocol forecast
   bridge, with a causal RFD centre path;
3. close APP-HF-0 and APP-HF-1: the frozen hourly crypto data/proxy audit and
   moving-centre gate;
4. derive and test the finite-sample centre-extraction alternatives in §8.3
   only if that gate supports a moving centre;
5. run APP-HF-2, the matched fixed-rank representation comparison;
6. diagnose projected-score noise, construct the future-centre policy, and
   compare direct VAR with latent state-space filtering;
7. run the frozen one-hour forecast and external equity validation;
8. construct retrospective predictive-rank paths and compare fixed, rolling,
   switching-penalised, and online-expert policies;
9. measure when full geometric refitting is useful and develop a causal
   event-triggered policy; and
10. only then test supervised or learned refit scheduling.

The strongest later-paper theme is:

> **Online RFD under computational constraints: latent-score filtering,
> adaptive predictive rank, and event-triggered geometric refitting.**

## 11. Provenance and non-claims

- Parent reproduction: results/final/parent_reproduce.md
- Loading and score baseline: results/final/b45_adjudication/
- Low-sample attribution: results/final/amplitude_diagnostic/report.md
- Fixed-rank signal boundary:
  [[P1-RANK — AR1 signal strength and threshold boundary]]
- Paper 1 scope and order: BUILD.md
- Declared application contract:
  [[Home application — hourly crypto realised covariance]]

This note adds no theorem. It does not claim time-varying latent-rank
identification, APP-FIN factor-score truth, general selector optimality, or a
regret guarantee without its own online-learning assumptions.
