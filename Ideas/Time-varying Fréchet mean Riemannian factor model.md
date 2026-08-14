---
type: idea
title: Time-varying Fréchet mean Riemannian factor model
aliases:
  - Moving-centre RFM
  - Locally stationary Riemannian factor model
status: current-programme
verdict: P1-ID is closed by exact quotients and impossibility boundaries; Paper 1 has scoped estimation branches and Paper 2 remains separate and parked
last-audited: 2026-08-12
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

The parent Riemannian factor model assumes in (P2) that every marginal law has the same Fréchet mean. The moving-centre programme asks the prior identification question: if the baseline can move, when can that centre drift be separated from a serially persistent tangent factor?

$$
X_{t,n}=\operatorname{Exp}_{\mu(u_t)}[A(u_t)f_{t,n}+\delta_{t,n}],
\qquad u_t=t/n.
$$

The fixed-centre lag operator can receive both contributions. Its leading direction may therefore be a superposition of baseline drift and factor persistence, without the fitted model reporting the split. This does **not** establish that the leading factor is spurious or that drift dominates it. [[P1-ID — centre-drift and factor identification boundary]] proves the exact identified quotients: unique marginal centres, the minimum dynamic loading quotient, pointwise but non-uniform one-path recovery, the weakened-reference orbit with curved rank failure, and the complete contaminated lag row.

The next distinction is geometric: after centre drift and factor variation have been made distinct estimands, is an apparent change in factor loadings induced merely by re-expressing one loading space along that moving centre, or does the loading subspace itself genuinely move?

### What the model is for

RFM is primarily geometry-aware dynamic dimension reduction. Lagged covariance identifies a few tangent directions that carry serial persistence, rather than directions that merely have large contemporaneous variance. The factor scores may be interpreted or used to reconstruct observations. For genuine forecasting, a separate time-series model is fitted to the factors and its forecast is mapped back with Exp. Covariance construction is scientifically justified only when covariance dynamics are the estimand; it is not a lossless replacement for modelling the raw multivariate distribution.

Paper 1 adds a slowly moving baseline. In applications such as covariance dynamics, it aims to separate structural drift in the baseline matrix from recurrent low-rank dynamic departures. Its rate and geometry theorems estimate that decomposition under explicit identifying assumptions; they do not by themselves prove that every observed law admits a unique scientific split.

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
| Centre-drift versus factor identification (P1-ID) | CLOSED — ID-0 through ID-6 terminal | exact quotients, curved rank-inflation boundary, one-path non-uniformity, and complete contamination theorem |
| Moving-centre identification under pointwise local-mean ergodicity | PROVED INTERNALLY; mean-square ergodic step CITED EXTERNALLY | fixed $p$; Doob (1953), Chapter X §7; see [[References and external claim audit]] |
| Positive-weight growing-$p_n$ G1 route | PROVED UNDER EXPLICIT ASSUMPTIONS | arbitrary $p_n$, bounded total energy/fixed memory |
| Integrated mean and corrected derivative rates | PROVED UNDER EXPLICIT ASSUMPTIONS | dimension-free; derivative carries $n^{-a}/b_n$ under level-only local stationarity |
| Ribbon holonomy and rotational decomposition | PROVED INTERNALLY; curvature/holonomy expansions CITED EXTERNALLY | fixed-$p$ stochastic theorem; Hunger Proposition 2.7 and Ambrose–Singer; see [[References and external claim audit]] |
| Paper 1 feasible lag/loading theorem | PROVED UNDER EXPLICIT ASSUMPTIONS | arbitrary $p_n$, polygonal Route R |
| Factor-number threshold/ridged selector | PROVED | arbitrary $p_n$; raw-ratio consistency is not implied by the displayed signal/null rates alone |
| Flat/common-flat exact-split oracle loading | PROVED UNDER EXPLICIT ASSUMPTIONS | arbitrary \(p_n\), bounded total energy |
| FRAME-2P-U two-path loading | CONDITIONAL IMPLICATION PROVED | root-\(n\) rate order under U2P; current growing-\(p_n\) witness has one fixed curved active block plus flat padding; growing-curvature/AIRM/BW verification is open |
| Known/root-\(n\) parametric centre loading | PROVED | oracle order; parametric branch is not immunity |
| Hilbert physical-dependence robust extension | PROVED | arbitrary \(p_n\) under uniform coefficients |
| Full AIRM fixed-band higher differentials | PROVED | matrix-size uniform in project norms; no cancellation |
| Structured signed growing-\(p_n\) mean | PROVED UNDER EXPLICIT ASSUMPTIONS | full AIRM signed branch remains open |
| Growing-energy/pervasive-factor theorem | PROVED UNDER EXPLICIT ASSUMPTIONS | bounded-tail and expanding-domain truncation chains; see [[HE — canonical growing-energy theorem boundary]] |
| Full moving-centre Bures–Wasserstein theorem | PROVED UNDER EXPLICIT ASSUMPTIONS — FIXED SIZE | safeguarded full-rank estimator; see [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]]; global/rank-changing PSD theorem disproved |
| Noncommuting BW fixed-margin growing-size geometry | PROVED UNDER EXPLICIT COMPATIBLE GENERATED-DOMAIN ASSUMPTIONS | dimension-free quotient/G1/PF producer with application-supplied statistics; see [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]] |
| BW shrinking-margin statistical propagation | PROVED UNDER RESTRICTED FRACTIONAL-NORMAL ASSUMPTIONS | sufficient \(x<3/(5A)\) corollary; see [[BW-SHRINKING-MARGIN — canonical restricted theorem boundary]] |
| Fixed-basis diagonal HE–BW | PROVED UNDER EXPLICIT ASSUMPTIONS | positive-root flat DGP; moving eigenvectors excluded |
| Paper 2 frame/subbundle identities | PROVED | dimension-free algebra |
| Paper 2 cross-tangent estimator and bootstrap | OPEN | fixed $p$ first, then growing $p$ |

## High-dimensional scope

The affine-invariant SPD geometry is not the high-dimensional blocker: on fixed absolute generated spectral bands, every fixed-order differential consumed by HD-G is now proved uniform in matrix size in the project norms. Spectral bands do not bound total tangent energy. Local symmetry does not cancel the random-Hessian or ribbon terms. The structured signed route avoids a sphere net only for deterministic, scalar-plus-HS, or controlled block Hessians; this structure remains unverified for full AIRM.

The robust chain is closed in [[HD1 — growing-dimension Paper 1 proof dossier]]. The sharper oracle chain still requires control of both linear mean terms and both non-rigid-frame terms. In a flat this follows from exact splitting plus GLO/frame rigidity. Under the explicit U2P package, FRAME-2P-U supplies an entirely observable three-colour correction: an independent undersmoothed validation path estimates the training path's realised displacement, and the evaluation polygon derivative corrects both base-log/Hessian and Jacobi/connector/frame actions. The implication is proved, but no genuinely growing-curvature family has been verified. Signal \(s_n\) and eigengap \(\Delta_n\) remain distinct; Davis–Kahan pays \(\Delta_n^{-1}\), with \(s_n^{-2}\) only after proving \(\Delta_n\ge s_n^2\). No branch covers pervasive energy by assertion, and every normalization must recheck the gap.

The high-energy theorem exposes score/product budgets, generated-domain constants, centre and frame error separately, and the exact assembly ratio
\[
\{2A_{2,n}d_n+d_n^2\}/\Delta_n.
\]
It proves nonempty localised, pervasive, matrix, and growing-rank regimes under bounded-tail assumptions. Its expanding-domain truncation theorem adds explicit score/product tail integrals, no-clipping escape probability, and a sub-Weibull corollary for unbounded observations. For BW, fixed-size full-rank local geometry, the noncommuting fixed-margin calculus, and a restricted fractional-normal shrinking-margin chain are closed. The latter requires support/energy \(O(\sqrt{\alpha_n})\) and therefore is not a pervasive-energy theorem. Unrestricted nonlocal sharp exponent minimisation is optional and open.

## Paper split

Paper 1 and Paper 2 answer different questions.

- **Paper 1:** when are centre drift and persistent factors separately identified, and—under that split—can the moving centre be removed without losing the fixed loading space and its lag-factor interpretation?
- **Paper 2:** after removing the moving centre, does the loading subspace itself move intrinsically?

The stale instruction to fold Paper 2 into Paper 1 has been withdrawn. Paper 2's publication status remains conditional on its open estimator/bootstrap nodes; it is neither dismissed nor declared complete.

## Main current risks

- P1-ID proves generic weakened-reference rigidity false and identifies the compatible-chart orbit, with an exact curved rank-inflation boundary. Its fixed-centre theorem supports superposition/non-separation, not claims that Factor 1 is spurious or drift-dominated.
- The robust growing-\(p_n\) rate remains slower than the parent fixed-centre oracle rate. FRAME-2P-U matches the oracle numerator's root-\(n\) **order** only under U2P; its added validation influence changes the limit variance, and no genuinely growing-curvature application has yet been verified.
- Cross-fitting alone does not restore quadratic curved recentering. Same-band score correction is disproved; the successful route needs an independently undersmoothed validation path with \(1/6<\gamma<3/14\), exact local law or \(a>1/2\), and dimension-uniform composed-action/replacement control.
- Paper 2 cannot inherit a Euclidean bootstrap merely by changing frame or substituting an $L^2$ mean rate.
- Bures–Wasserstein boundary distance and rank loss require the proved local/regularized estimator; the global PSD theorem is false.
- The parent’s covariance demonstration can consume the fixed-size BW theorem only after its covariance-estimation measurement layer and generated-domain margins are checked.
- Growing energy can be offset by growing signal only through the proved assembly/gap phase conditions; rescaling can erase localised factors.
- The raw factor-number ratio is disproved as a consequence of the available eigenvalue rates; threshold and ridged selectors are proved internally.

## Live work

P1-ID is closed and supplies the interpretation boundary. N-18 is a sensitivity diagnostic rather than proof.

All live work is in [[OPEN OBLIGATIONS — current research actions]]. N-00 remains the first computational task. FRAME-2P-U application verification beyond fixed-active-curvature padding remains open. Infinite-memory conditional splitting, unrestricted full-AIRM signed Hessians, higher positive smoothing, and optional unrestricted BW exponent sharpness remain secondary. Paper 2 is parked and standalone.

## Related notes

- [[Analytical reconstruction — proof ledger and rebuilt spec]]
- [[P1-ID — centre-drift and factor identification boundary]]
- [[G1 audit — resolution of the uniform local Fréchet rate]]
- [[Paper 1 — Locally stationary Riemannian factor model]]
- [[Paper 2 — Moving loading subbundle]]
- [[Application map — geometry, symmetry, and rate accelerators]]
- [[Numerical suite — theorem-driven design matrix]]
- [[OPEN OBLIGATIONS — current research actions]]
