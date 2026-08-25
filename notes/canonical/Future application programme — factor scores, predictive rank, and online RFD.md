---
type: canonical-future-programme
title: Future application programme — factor scores, predictive rank, and online RFD
aliases:
  - Online RFD
  - Adaptive-rank RFD
  - Fixed-loading RFD application follow-up
status: parked-after-paper-1
verdict: Paper 1 stops before forecasting; factor-score filtering, predictive rank, future-centre policy, state-space/VAR dynamics, and learned refit scheduling form one later application programme
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
- Reconstruction and genuine out-of-sample forecast losses are reported;
  loading-space accuracy alone is not an application result.

APP-FIN has no known true rank. Paper 1 therefore reports both:

1. a rank fixed by training-era validation; and
2. one **frozen causal online rank policy** that may change its predictive rank
   after observing completed forecast losses.

The second item is online forecast-model selection, not a theorem that the
latent scientific rank changed.

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

### Minimal Paper 1 protocol

Paper 1 keeps this compact:

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
credible. The fixed baseline and one simple frozen online policy are enough for
Paper 1.

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

1. finish Paper 1 with fixed-rank synthetic recovery, completed literal parent
   parity, and the non-forecasting APP-FIN identification illustration;
2. diagnose projected-score noise, construct the future-centre policy, and compare direct VAR with latent
   state-space filtering;
3. construct retrospective rank paths on longer or higher-frequency data;
4. compare fixed, rolling, switching-penalised, and online-expert policies;
5. measure when full geometric refitting is useful;
6. develop a causal event-triggered refit policy; and
7. only then test supervised or learned refit scheduling.

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

This note adds no theorem. It does not claim time-varying latent-rank
identification, APP-FIN factor-score truth, general selector optimality, or a
regret guarantee without its own online-learning assumptions.
