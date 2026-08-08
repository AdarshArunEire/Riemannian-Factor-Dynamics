---
type: canonical-research-queue
title: OPEN OBLIGATIONS — current research actions
status: active
last-audited: 2026-08-08
---

# OPEN OBLIGATIONS — current research actions

> **Only live queue.** Closed proof-run specifications and superseded TODO lists are archived. A task may enter a proved theorem only after its assumptions, producer lemmas, consumer lemmas, counterexamples, and rate substitutions are all explicit. Web references and numerical experiments may support application selection but cannot close a proof obligation.

## 0. Current programme state

Paper 1’s robust arbitrary-\(p_n\), bounded-total-energy theorem is closed under its displayed assumptions. The flat/common-commuting exact-split oracle branch, root-\(n\) parametric-centre order, Hilbert physical-dependence extension, fixed-band AIRM differential calculus, structured signed mean branch, and corrected factor-number selectors are also closed under their explicit packages.

The two primary next programmes are:

1. **HE — growing energy and pervasive factor signal**;
2. **BW — moving-centre Bures–Wasserstein covariance dynamics**.

They are independent. HE changes statistical scaling and signal balance. BW changes the geometry and estimator calculus. Their intersection is a later corollary, not the starting point.

## 1. P0 — HE: growing-energy/pervasive-factor theorem

### Objective

Replace the uniform bound \(\|Y_{t,n}\|\le R\) by a controlled sequence \(R_n\to\infty\), and prove loading consistency in regimes where signal strength can also grow with dimension.

### Required outputs

#### HE-1 — typed assumption ledger

Separate and minimise the quantities actually consumed by:

- mean-score concentration;
- local empirical Hessian and tube localisation;
- lag-product concentration;
- feasible-versus-oracle comparison;
- frame/holonomy control;
- lag target and eigengap.

Do not replace all of these by one unnecessarily strong almost-sure norm assumption if moment/product conditions suffice.

#### HE-2 — rederive mean and frame errors

Prove the positive three-scale mean, grid, and polygonal-frame results with displayed \(R_n\), tail, dependence, and generated-tube constants. Define the resulting feasible observation error \(q_{R,n}\); do not reuse \(\ell_n\) by assertion.

#### HE-3 — oracle lag-row theorem

For each included lag, prove the Hilbert–Schmidt row concentration under the chosen product-moment and dependence conditions. The bounded-envelope benchmark is

\[
O_p(R_n^2n^{-1/2}),
\]

but sharper variance-sensitive bounds should be retained when proved.

#### HE-4 — feasible row and operator assembly

Prove a typed bound of the form

\[
d_n\lesssim \text{oracle row}+2R_nq_{R,n}+q_{R,n}^2
+\text{frame, target, and dependence defects},
\]

then use

\[
\eta_n=2A_{2,n}d_n+d_n^2.
\]

No factor of \(R_n\), \(A_{2,n}\), lag count, or dependence budget may be hidden in \(O(1)\).

#### HE-5 — signal phase diagram

State consistency in terms of \(\eta_n=o(\Delta_n)\). Work out separate corollaries for:

- localised factors with bounded signal;
- pervasive factors whose lag signal grows with dimension;
- normalised observations with signal preserved;
- normalised observations with signal dilution;
- matrix observations, distinguishing matrix size \(m_n\) from tangent dimension \(p_n=m_n(m_n+1)/2\).

#### HE-6 — hostile lower bounds and counterexamples

At minimum, attack:

- coordinatewise moments without a total/product budget;
- growing energy with a fixed eigengap;
- normalisation of a localised factor;
- pervasive signal with weak idiosyncratic lag contamination;
- growing rank under bounded or slowly growing energy.

For every proposed growth window, either prove attainability or give a counterexample. Numerical plots do not establish sharpness.

### Completion gate

HE closes only when one theorem states all rates in \((n,b_n,R_n,A_{2,n},\Delta_n)\) and the dependence/tube budgets, proves a nonempty consistency regime, and supplies at least one pervasive application model satisfying it without scientifically arbitrary rescaling.

## 2. P0 — BW: moving-centre Bures–Wasserstein theorem

### Objective

Build a full Paper 1 geometry-and-statistics route for covariance matrices under the same Bures–Wasserstein estimand used by the parent application.

### Required outputs

#### BW-1 — domain and metric specification

Choose whether the theorem lives on strictly positive-definite matrices, a fixed-rank PSD stratum, or a quotient representation. State the BW metric, tangent norm, Exp/Log convention, horizontal alignment, and every uniqueness condition. Quantify distance from rank loss and nonunique alignment.

#### BW-2 — generated-set closure

Prove that population means, empirical local means, Richardson/blend images, connectors, chords, and reconstructed observations stay in one explicitly controlled domain with probability tending to one. A bound on the raw observations alone is insufficient.

#### BW-3 — dimension-uniform differential calculus

Prove or disprove matrix-size-uniform bounds for every fixed-order map consumed by G1 and the polygonal-frame proof:

- squared-distance score and Hessian;
- Exp and Log;
- optimal alignment/horizontal lift;
- connector and comparison maps;
- Richardson and blend maps;
- ruled-surface/frame variation.

Track the dependence on lower eigenvalue, upper eigenvalue, rank, and spectral multiplicity margins. Do not import the AIRM proof.

#### BW-4 — mean and feasible-frame theorem

Either reproduce the positive three-scale and polygonal route under BW or design a replacement estimator with fewer geometric consumers. Prove its level, grid, and frame error bounds.

#### BW-5 — lag identification

Show that the transported BW tangent observations yield the intended loading space under explicit included-lag noise/cross-covariance conditions. Define \(A_{2,n}\), \(\Delta_n\), and the target in the BW tangent norm.

#### BW-6 — fixed-size theorem first

Close the complete moving-centre theorem for fixed matrix size before making a growing-size claim. Then audit every constant for matrix-size uniformity.

#### BW-7 — boundary and nonuniqueness attacks

Construct or cite explicit failures caused by:

- eigenvalues approaching zero;
- rank changes;
- nonunique Procrustes alignment;
- nonunique Fréchet means;
- generated estimator images leaving the controlled stratum.

### Completion gate

BW closes only when the estimator is well-defined on a proved high-probability event, every consumed differential is bounded in the stated norm, and the final lag/loading theorem has no AIRM-only lemma hidden in its dependency chain.

## 3. P1 — application verification after HE/BW

Application matching begins from proved property packages, not labels.

### APP-FIN — realised covariance dynamics

- specify raw return sampling, covariance estimator, regularisation, and monthly/rolling overlap;
- identify whether covariance dynamics—not the full return distribution—is the estimand;
- quantify covariance-estimation noise and its included-lag contamination;
- test whether signal is pervasive or localised as the asset universe grows;
- compare AIRM, BW, log-Euclidean, and direct covariance baselines under the same forecast protocol.

### APP-NEURO — functional connectivity and diffusion data

- separate raw time series, estimated connectivity matrices, and the scientific target;
- model overlapping-window dependence and regularisation bias;
- check energy and signal under increasing parcellation;
- distinguish moving eigenvectors from approximately fixed anatomical axes;
- reject dimension refinement that changes the estimand without an explicit continuum interpretation.

### APP-SENSOR/GENE — expanding panels

- distinguish adding genuinely new noisy variables from refining a fixed-energy latent object;
- formulate a pervasive-factor DGP with checkable product dependence;
- verify whether the eigengap strengthens fast enough to pay the HE numerator;
- retain raw-variable benchmarks that do not require a covariance aggregation.

### Numerical role

The later numerical suite should compare reconstruction, factor stability, factor-number selection, and genuine out-of-sample forecasting. It validates usefulness and diagnostics; it does not close HE or BW proof nodes.

## 4. P2 — secondary analytical backlog

These do not block the robust theorem or the two primary programmes unless explicitly imported:

- **CF-PD:** conditional Hilbert/HS physical-dependence inequality or joint retained-row coupling for infinite-memory oracle cancellation;
- **AIRM-SIGNED:** prove or disprove a matrix-size-uniform scalar-plus-HS or controlled-block representation for the full AIRM random Hessian;
- **FRAME-DB:** generic curved non-rigid frame debiasing with a proved first-order coefficient;
- **G1-Q4:** positive-weight bias order at least four with all Exp/Log/Richardson derivatives verified;
- **GEO-N/GEO-AV:** necessity and averaged variants of curvature-derivative control;
- **MIX-SHARP:** sharpness of sufficient polynomial-mixing thresholds;
- **P1-ID:** necessity side of the curved mean/factor identification ambiguity.

Paper 2’s cross-tangent algebra, localised concentration, and estimated-frame bootstrap remain in [[Paper 2 — Moving loading subbundle]] and are parked while Paper 1 applications are prioritised.

## 5. Execution order

1. Run HE-1/HE-2 and BW-1/BW-2 in parallel as independent analytical scoping tasks.
2. Close HE-3/HE-4; only then derive the HE phase diagram.
3. Close BW-3; choose between reusing and replacing the current feasible-frame estimator.
4. Obtain a complete fixed-size BW theorem before its growing-size audit.
5. Match finance, neuro, and expanding-panel applications only to assumption packages that have survived the hostile pass.
6. Design the numerical suite from the final theorem regimes and declared failure modes.

## 6. Repository rule

Canonical theorem status appears only in this queue, [[Analytical reconstruction — proof ledger and rebuilt spec]], and the named canonical theorem/application files. Documents under `Ideas/Archived` are evidence and history. Their old status labels do not override the canon.

