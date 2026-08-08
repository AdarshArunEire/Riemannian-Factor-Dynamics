---
type: idea
title: Time-varying Fréchet mean Riemannian factor model
aliases:
  - Moving-centre RFM
  - Locally stationary Riemannian factor model
status: current-programme
verdict: Paper 1 has a closed bounded-energy growing-p theorem and explicit accelerators; growing-energy/pervasive factors and full moving-centre Bures–Wasserstein covariance dynamics are the two primary next programmes; Paper 2 remains separate and parked
last-audited: 2026-08-08
area:
  - geometry
  - time-series
  - factor-models
tags:
  - idea
  - programme
---

# Time-varying Fréchet mean Riemannian factor model

> **Programme note only.** [[Analytical reconstruction — proof ledger and rebuilt spec]] is the primary source of mathematical truth. [[G1 audit — resolution of the uniform local Fréchet rate]] is the canonical proof source for mean estimation. This note explains the scientific hierarchy and paper split; it does not maintain independent theorem statuses.

## Scientific question

The parent Riemannian factor model uses a fixed Fréchet mean. The moving-centre programme asks what happens when the centre itself drifts along a smooth trajectory and whether lagged factor structure can still be separated from that drift.

$$
X_{t,n}=\operatorname{Exp}_{\mu(u_t)}[A(u_t)f_{t,n}+\delta_{t,n}],
\qquad u_t=t/n.
$$

The central scientific distinction is not merely that tangent spaces change. It is whether an apparent change in factor loadings is induced by re-expressing the same loading space along a moving centre, or reflects a genuinely moving loading subspace.

### What the model is for

RFM is primarily geometry-aware dynamic dimension reduction. Lagged covariance identifies a few tangent directions that carry serial persistence, rather than directions that merely have large contemporaneous variance. The factor scores may be interpreted or used to reconstruct observations. For genuine forecasting, a separate time-series model is fitted to the factors and its forecast is mapped back with Exp. Covariance construction is scientifically justified only when covariance dynamics are the estimand; it is not a lossless replacement for modelling the raw multivariate distribution.

Paper 1 adds a slowly moving baseline. In applications such as covariance dynamics, it aims to separate structural drift in the baseline matrix from recurrent low-rank dynamic departures.

## Current model hierarchy

### M0 — fixed centre, fixed loading space

This is the parent RFM reference model. The primary source permits a high-dimensional triangular array with (p=p(n)) diverging and reports a fixed-centre dimension-free oracle rate under its short-memory/strong-signal assumptions.

### M1 / Paper 1 — moving centre, covariantly constant loading space

$$
X_{t,n}=\operatorname{Exp}_{\mu(u_t)}
\left[\mathcal P^\mu_{u_0\to u_t}Af_{t,n}+\delta_{t,n}\right].
$$

After parallel transport to $T_{\mu(u_0)}M$, the loading map $A$ is constant. The robust theorem permits arbitrary $p_n\to\infty$ under bounded total tangent energy, explicit uniform geometry, exact included-lag noise orthogonality, and the polygonal estimator. [[Application map — geometry, symmetry, and rate accelerators]] adds an exact flat/common-commuting split-oracle branch, oracle-order known/parametric-centre branches, a Hilbert physical-dependence extension, fixed-band AIRM differential verification, and a structured signed growing-\(p_n\) mean route.

### M2 / Paper 2 — moving centre, genuinely moving loading subbundle

$$
X_{t,n}=\operatorname{Exp}_{\mu(u_t)}[A(u_t)f_{t,n}+\delta_{t,n}],
\qquad \frac D{du}\Pi(u)\ne0.
$$

In a parallel frame this becomes a Euclidean time-varying-loading problem, but the frame is estimated from $\hat\mu$. The induced ribbon holonomy can manufacture the alternative being tested. The frame/subbundle geometry is proved; cross-tangent identification, localised concentration, and estimated-frame bootstrap validity remain open.

## Flat pullback and where geometry remains

The pullback connection $\mu^*\nabla$ over an interval is flat because its curvature is a two-form on a one-dimensional base. A global parallel frame therefore turns the oracle model into a vector model in one fixed $\mathbb R^p$.

This does not eliminate geometry from the feasible estimator. Comparing the frame along $\hat\mu$ with the frame along $\mu$ creates a ribbon. The correctly typed transport error is controlled by
$$
\int\left|e\wedge\left(\mu'+\tfrac12\nabla_se\right)\right|du,
\qquad e=\log_\mu\hat\mu,
$$
with connector maps inserted before subtracting transports. The channel vanishes in flat simply connected geometry, not merely when $\mu$ is geodesic.

## Current mean-estimation choices

Paper 1 can use either:

- a signed degree-$d\ge2$ local-polynomial Fréchet criterion with a **localised argmin** and SW-AS; or
- three positive-weight scale-family barycentres combined in one tangent space, certified at bias order $q=3$.

The signed route can reach $q=d+1$ but needs empirical Hessian control. The positive route avoids the signed criterion and its SW-AS geometry, but is presently certified only at $q=3$. Both raw rates carry the local-stationarity remainder $n^{-a}$.

CE-9 is retained with corrected scope: arbitrary signed Fréchet criteria may have several minimisers, so localisation is required; it does not disprove the structured local-polynomial rate.

For the final growing-$p_n$ theorem, the live mean inputs are level/grid RMS G1 and the typed polygonal-frame theorem. G1′ is proved with its corrected $n^{-a}/b_n$ term but bypassed by the final loading theorem.

## Current programme status

| Component | Current status | Scope |
|---|---|---|
| Moving-centre identification under pointwise local-mean ergodicity | PROVED/CITED | fixed $p$; algebraic condition not inherently dimensional |
| Positive-weight growing-$p_n$ G1 route | PROVED UNDER EXPLICIT ASSUMPTIONS | arbitrary $p_n$, bounded total energy/fixed memory |
| Integrated mean and corrected derivative rates | PROVED UNDER EXPLICIT ASSUMPTIONS | dimension-free; derivative carries $n^{-a}/b_n$ under level-only local stationarity |
| Ribbon holonomy and rotational decomposition | PROVED/CITED | fixed-$p$ stochastic theorem; geometric constants can be dimension-free |
| Paper 1 feasible lag/loading theorem | PROVED UNDER EXPLICIT ASSUMPTIONS | arbitrary $p_n$, polygonal Route R |
| Factor-number threshold/ridged selector | PROVED | arbitrary $p_n$; raw ratio disproved |
| Flat/common-flat exact-split oracle loading | PROVED UNDER EXPLICIT ASSUMPTIONS | arbitrary \(p_n\), bounded total energy |
| Known/root-\(n\) parametric centre loading | PROVED | oracle order; parametric branch is not immunity |
| Hilbert physical-dependence robust extension | PROVED | arbitrary \(p_n\) under uniform coefficients |
| Full AIRM fixed-band higher differentials | PROVED | matrix-size uniform in project norms; no cancellation |
| Structured signed growing-\(p_n\) mean | PROVED UNDER EXPLICIT ASSUMPTIONS | full AIRM signed branch remains open |
| Growing-energy/pervasive-factor theorem | OPEN PROGRAMME | component \(R_n\)-scalings proved; joint phase diagram not closed |
| Full moving-centre Bures–Wasserstein theorem | OPEN PROGRAMME | diagonal fixed-basis flat special case only |
| Paper 2 frame/subbundle identities | PROVED | dimension-free algebra |
| Paper 2 cross-tangent estimator and bootstrap | OPEN | fixed $p$ first, then growing $p$ |

## High-dimensional scope

The affine-invariant SPD geometry is not the high-dimensional blocker: on fixed absolute generated spectral bands, every fixed-order differential consumed by HD-G is now proved uniform in matrix size in the project norms. Spectral bands do not bound total tangent energy. Local symmetry does not cancel the random-Hessian or ribbon terms. The structured signed route avoids a sphere net only for deterministic, scalar-plus-HS, or controlled block Hessians; this structure remains unverified for full AIRM.

The robust chain is closed in [[HD1 — growing-dimension Paper 1 proof dossier]]. The application-specific oracle chain separately requires cancellation of both linear mean terms and both non-rigid-frame terms. Signal \(s_n\) and eigengap \(\Delta_n\) remain distinct; Davis–Kahan pays \(\Delta_n^{-1}\), with \(s_n^{-2}\) only after proving \(\Delta_n\ge s_n^2\). No branch covers pervasive energy by assertion, and every normalization must recheck the gap.

The high-energy frontier must expose \(R_n\) in mean, lag-product, and feasible-comparison errors while allowing \(A_{2,n}\) and \(\Delta_n\) to strengthen. This is the correct route for expanding panels; the bounded-energy theorem remains the correct route for fixed-energy or trace-class refinement.

## Paper split

Paper 1 and Paper 2 answer different questions.

- **Paper 1:** can a moving centre be removed without losing the fixed loading space and its lag-factor interpretation?
- **Paper 2:** after removing the moving centre, does the loading subspace itself move intrinsically?

The stale instruction to fold Paper 2 into Paper 1 has been withdrawn. Paper 2's publication status remains conditional on its open estimator/bootstrap nodes; it is neither dismissed nor declared complete.

## Main current risks

- The robust growing-\(p_n\) rate is slower than the parent fixed-centre oracle rate; the flat exact-split and root-\(n\) centre branches are sharper but structurally narrower.
- Cross-fitting alone does not restore quadratic curved recentering. The oracle branch separately needs GLO and a negligible non-rigid frame coefficient.
- Paper 2 cannot inherit a Euclidean bootstrap merely by changing frame or substituting an $L^2$ mean rate.
- Bures–Wasserstein incompleteness and boundary distance must not be hidden by affine-invariant SPD simplifications.
- The parent’s covariance demonstration uses Bures–Wasserstein geometry, so AIRM verification alone does not connect Paper 1 to that exact application.
- Growing energy can be offset by growing signal only through a proved joint phase condition; rescaling can erase localised factors.
- The raw factor-number ratio is disproved as a consequence of the available eigenvalue rates; threshold and ridged selectors are proved internally.

## Live work

All live work is in [[OPEN OBLIGATIONS — current research actions]]. The next priorities are the growing-energy/pervasive-factor theorem and the full moving-centre Bures–Wasserstein theorem. After those proof gates, the application suite should test realised covariance, functional connectivity, and expanding sensor/gene panels against direct non-factor and alternative-geometry baselines. Infinite-memory conditional splitting, generic curved frame debiasing, unrestricted full-AIRM signed Hessians, and higher positive smoothing remain secondary. Paper 2 is parked and remains standalone.

## Related notes

- [[Analytical reconstruction — proof ledger and rebuilt spec]]
- [[G1 audit — resolution of the uniform local Fréchet rate]]
- [[Paper 1 — Locally stationary Riemannian factor model]]
- [[Paper 2 — Moving loading subbundle]]
- [[OPEN OBLIGATIONS — current research actions]]
