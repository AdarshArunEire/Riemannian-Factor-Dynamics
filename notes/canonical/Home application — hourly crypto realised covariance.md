---
type: canonical-application-spec
title: Home application — hourly crypto realised covariance
aliases:
  - APP-HF-CRYPTO
  - Hourly crypto RFD
status: gated-post-paper-1
verdict: A 20-asset, one-hour-ahead realised-covariance study is the declared home application for fixed-loading RFD; it proceeds only through predeclared data, centre, representation, score, and forecast gates
last-audited: 2026-08-25
area:
  - finance
  - realised-covariance
  - forecasting
  - application
tags:
  - canonical-application
  - post-paper-1
  - crypto
  - causal-forecasting
---

# Home application — hourly crypto realised covariance

## 0. Decision

The declared home application for the fixed-loading RFD follow-up is:

> Separate a slowly moving covariance baseline from lag-persistent co-movement
> in a liquid 20-asset crypto market, then forecast the next hour's covariance.

This choice is not a claim that crypto satisfies the theory. It is a gated
application hypothesis. Continuous trading supplies enough consecutive hourly
matrices to make moving-centre estimation plausible, one hour is operationally
meaningful, and realised-covariance forecasting has serious statistical and
geometric competitors. Paper 1 remains frozen before forecasting.

## 1. Observation contract

The primary panel is fixed before evaluation:

- 20 liquid spot crypto assets from one venue and one quote currency;
- assets selected using a pre-sample liquidity rule;
- stablecoins, leveraged tokens, and wrapped duplicates excluded;
- no silent survivor replacements; delistings and missing intervals are
  recorded as data events;
- official one-second bars, aggregated to synchronized ten-second log returns;
- one non-overlapping \(20\times20\) realised-covariance matrix per hour,
  using approximately \(360\) intrahour returns;
- a fixed, declared SPD regularisation rule applied before any model sees the
  matrix.

Thus one year supplies roughly \(n=8{,}760\) hourly observations and the
symmetric tangent dimension is

\[
p=\frac{20(21)}2=210.
\]

The first data release should target two complete years: one for burn-in,
training, and validation, and one for a causal forecast evaluation. The split,
asset list, regulariser, and missing-data policy are frozen before final losses
are read.

Every matrix records its minimum eigenvalue, condition number, ridge applied,
number of valid intrahour returns, stale-price fraction, and any BW domain or
fallback event. Periodicity is estimated using training data only; raw-data
results remain as a robustness view because removing clock effects changes the
estimand.

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

### APP-HF-0 — data and proxy preflight

Construct the frozen panel and audit synchronization, missingness, microstructure
noise, covariance regularisation, spectral margins, seasonality, dependence,
and effective intrahour sample size. Failure stops the application or changes
the declared observation process before evaluation begins.

### APP-HF-1 — centre gate

On blocked training/validation periods compare:

1. one global BW centre;
2. positive local BW centres;
3. the full three-scale Richardson path;
4. a predeclared global/local geodesic shrinkage family.

Use held-out proxy-robust covariance losses, path stability, effective local
sample size, compatibility/fallback diagnostics, and a dependence-preserving
constant-centre null. If global wins, reject moving-centre RFD for this panel.
If positive local or shrinkage wins but Richardson loses, retain the winning
regularised centre and report that the theorem-valid full correction is
finite-sample inefficient. If jumps dominate, reject the smooth-path model.

### APP-HF-2 — matched representation

Fit literal parent RFM and RFD on identical matrices with one fixed,
validation-chosen rank. Compare centre diagnostics, loading stability,
reconstruction, lag spectra, residual dependence, and numerical margins. This
stage asks whether moving-centre preprocessing adds useful representation; it
is not yet a forecast contest.

### APP-HF-3 — score observation model

Quantify projected-score noise and compare direct projection with a declared
linear state-space/Kalman filter. The parent-style VAR(1) on projected scores
remains the required baseline. This stage must distinguish loading-space
recovery from factor-amplitude recovery.

### APP-HF-4 — one-hour causal forecast

Freeze the centre rule, rank, score filter, refit schedule, and all tuning on
training/validation data. Issue one-hour-ahead forecasts sequentially. No
evaluation-period outcome may influence a forecast already issued. Start with
a fixed rank; adaptive rank and learned refit scheduling are later extensions.

### APP-HF-5 — external validation

Repeat the frozen protocol on a 20-stock high-frequency US-equity panel after
explicit market-hours, intraday-seasonality, asynchronous-trading, and overnight
policies. This tests whether the result is crypto-specific; it is not used to
retune the crypto headline.

## 4. Competitors and losses

The minimum benchmark set is:

- LOCF and EWMA;
- HAR-style covariance forecasting in a declared SPD parameterisation;
- conditional autoregressive Wishart or F-Riesz dynamics;
- a conventional factor/state-space covariance model;
- parent fixed-centre RFM with projected-score VAR(1);
- at least one modern geometric or SPD-network benchmark if its causal protocol
  can be reproduced without changing the target.

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
\text{APP-HF-2 representation gain or honest tie}\\
\downarrow\\
\text{APP-HF-3 score-noise treatment}\\
\downarrow\\
\text{APP-HF-4 one-hour forecast}\\
\downarrow\\
\text{APP-HF-5 external validation.}
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

The downstream score, rank, future-centre, and online-update questions remain
in [[Future application programme — factor scores, predictive rank, and online RFD]].
