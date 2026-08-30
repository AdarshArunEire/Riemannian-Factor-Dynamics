---
type: idea
title: Time-varying Fréchet mean Riemannian factor model
aliases:
  - Moving-centre RFM
  - Locally stationary Riemannian factor model
status: current-programme
verdict: P1-ID is closed by exact quotients and impossibility boundaries; Paper 1 has scoped estimation branches and the moving-loading programme remains separate, unnumbered, and parked
last-audited: 2026-08-25 (parent/RFD BW parity and narrowed non-forecast Paper 1 application scope integrated)
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

### M2 — moving centre, genuinely moving loading subbundle (parked programme)

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
| Centre-drift versus factor identification (P1-ID) | CLOSED — ID-0 through ID-10 terminal | exact quotients, constructive separation and persistence windows, curved rank-inflation boundary, one-path non-uniformity, and complete contamination theorem |
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
| Moving-loading frame/subbundle identities | PROVED | dimension-free algebra |
| Moving-loading cross-tangent estimator and bootstrap | OPEN | fixed $p$ first, then growing $p$ |

## High-dimensional scope

The affine-invariant SPD geometry is not the high-dimensional blocker: on fixed absolute generated spectral bands, every fixed-order differential consumed by HD-G is now proved uniform in matrix size in the project norms. Spectral bands do not bound total tangent energy. Local symmetry does not cancel the random-Hessian or ribbon terms. The structured signed route avoids a sphere net only for deterministic, scalar-plus-HS, or controlled block Hessians; this structure remains unverified for full AIRM.

The robust chain is closed in [[HD1 — growing-dimension Paper 1 proof dossier]]. The sharper oracle chain still requires control of both linear mean terms and both non-rigid-frame terms. In a flat this follows from exact splitting plus GLO/frame rigidity. Under the explicit U2P package, FRAME-2P-U supplies an entirely observable three-colour correction: an independent undersmoothed validation path estimates the training path's realised displacement, and the evaluation polygon derivative corrects both base-log/Hessian and Jacobi/connector/frame actions. The implication is proved, but no genuinely growing-curvature family has been verified. Signal \(s_n\) and eigengap \(\Delta_n\) remain distinct; Davis–Kahan pays \(\Delta_n^{-1}\), with \(s_n^{-2}\) only after proving \(\Delta_n\ge s_n^2\). No branch covers pervasive energy by assertion, and every normalization must recheck the gap.

The high-energy theorem exposes score/product budgets, generated-domain constants, centre and frame error separately, and the exact assembly ratio
\[
\{2A_{2,n}d_n+d_n^2\}/\Delta_n.
\]
It proves nonempty localised, pervasive, matrix, and growing-rank regimes under bounded-tail assumptions. Its expanding-domain truncation theorem adds explicit score/product tail integrals, no-clipping escape probability, and a sub-Weibull corollary for unbounded observations. For BW, fixed-size full-rank local geometry, the noncommuting fixed-margin calculus, and a restricted fractional-normal shrinking-margin chain are closed. The latter requires support/energy \(O(\sqrt{\alpha_n})\) and therefore is not a pervasive-energy theorem. Unrestricted nonlocal sharp exponent minimisation is optional and open.

## Paper split

Paper 1 and the parked moving-loading programme answer different questions.

- **Paper 1:** when are centre drift and persistent factors separately identified, and—under that split—can the moving centre be removed without losing the fixed loading space and its lag-factor interpretation?
- **Moving-loading programme:** after removing the moving centre, does the loading subspace itself move intrinsically?

The stale instruction to fold the moving-loading programme into Paper 1 has been withdrawn. Its publication status remains conditional on its open estimator/bootstrap nodes; it is neither dismissed nor declared complete, and it does not reserve the number of the next paper.

### Parked same-programme application follow-up — current Paper 2 candidate

The natural application paper after Paper 1 stays on the **same fixed-loading RFD branch**. It is not the moving-loading-subbundle programme. Paper 1 first installs a minimal causal forecasting policy and a compact fixed-versus-online predictive-rank comparison. The later application programme preserves the interpretable extraction pipeline while developing score filtering, online rank experts, and event-triggered geometric refitting:

$$
(\widehat\mu_{1:t},\widehat f_{1:t})
\longmapsto
(\widehat\mu_{t+1:t+h},\widehat f_{t+1:t+h})
\longmapsto
\widehat X_{t+1:t+h},
$$

where reconstruction still uses the fitted fixed loading space, polygon transport, and Exp map. Masked or future-block prediction supplies self-supervision; a real application may add a supervised task loss. The learner must remain common-gauge equivariant and cannot claim to separate centre drift from persistent factors beyond the P1-ID quotient.

The current DGP evidence supports **keeping lag extraction fixed in the first learned application model**. In the completed 768-row bounded-energy evaluation, the feasible lag-row error decreases across every tested sample size. At $n=4096$ its median is about $0.01$ for $m\in\{2,3,4\}$, roughly $7$–$9\%$ of the oracle-row magnitude, and median loading-projector error is about $0.01$–$0.02$. The broader selector sweep found no visible extra geometry-induced detectability boundary on equal-strength cells; weak signal was the boundary. Synthetic structural headlines nevertheless use known rank, and APP-FIN online rank is treated as predictive model selection rather than latent-rank recovery. These are simulation results, not a real-data guarantee.

#### Parked amplitude bottleneck and two separate adaptive modules

The completed core-control stage exposes a forecasting-relevant finite-sample
bottleneck that loading recovery alone hides. On the smooth moving-centre B0
control at $n=512$, feasible RFD has a $4.44$-degree loading angle versus
$15.50$ degrees for the one-centre ablation and reduces reconstruction error
by a paired median $17.5\%$, yet its factor-score NRMSE is $0.777$ versus
$0.364$ for the one-centre fit. The factor-score disadvantage remains about
$23\%$ at $n=2048$ and reverses only at $n=8192$, where RFD is about $10\%$
better. Thus the persistent subspace can be structurally accurate while its
time-specific amplitudes remain too noisy for efficient forecasting. This is
recorded as a **Paper 2 forecasting bottleneck**, not a reason to change the
Paper 1 loading theorem.

The same-draw attribution is now complete on 192 B0 draws at
$n\in\{240,512,2048\}$. It crosses oracle/feasible rows with true/feasible
loading directions and retains an oracle-estimated-loading benchmark. Median
complete RFD factor-score NRMSE is respectively $0.962$, $0.747$, and $0.476$,
against oracle noisy-row floors $0.276$, $0.279$, and $0.278$. Replacing only
the oracle rows by feasible centre/frame rows adds $0.683$, $0.465$, and
$0.204$ NRMSE. Replacing only the true loading directions by RFD directions
adds essentially zero at every sample size, with all paired-bootstrap
intervals containing zero; the row/loading interaction is also negligible.

Thus the finite-sample bottleneck is localized to the **feasible-row bundle**:
local-centre estimation, base-Log recentering, polygon interpolation, and
non-rigid frame transport. This experiment does not separate those four
subchannels and therefore must not be shortened to “the centre estimator is
the cause.” Loading-space and lag-eigenspace estimation are exonerated on this
declared DGP only. One scalar rescaling removes some error but leaves NRMSE
$0.736$, $0.624$, and $0.440$; the estimated score norms are inflated rather
than uniformly damped. Scalar calibration is not a remedy for the remaining
trajectory error. The authoritative numerical artifacts are
`results/final/amplitude_diagnostic/`.

With that attribution complete, the application follow-up may compare two
different adaptive modules:

- **fixed-to-moving centre shrinkage:** interpolate between a global centre
  and the feasible moving path with a validation-selected coefficient
  $0\le\lambda\le1$. This learns how much dynamic centring improves untouched
  forecast loss; it does not identify how much the true centre moves and is
  not, by itself, an amplitude correction;
- **dynamic amplitude filtering:** condition on the extracted loading space
  and estimate the score trajectory jointly with a linear state-space,
  Kalman/Wiener, or later gauge-equivariant learned transition model. This
  directly trades the noisy pointwise projection against temporal
  persistence and is the first candidate remedy if the four-way decomposition
  places the loss in score extraction rather than centre estimation.

Both modules require causal training/validation/evaluation separation. A
scalar score damping coefficient is only a calibration baseline: it cannot
repair factor-specific persistence, phase delay, leakage, or correlated
noise. The first learned experiment should therefore benchmark an explicit
linear state-space amplitude filter before a deeper forecasting head.

APP-FIN can already use one much smaller adaptive component without importing
this full future programme. All ranks \(0,\ldots,15\) share the expensive
geometric fit. If every rank-specific forecast is issued before the next
outcome, a frozen online policy may update its predictive rank from completed
losses. The rank path is allowed to move; the update rule is frozen. With only
36 test months, Paper 1 compares a validation-selected fixed rank with one
simple online policy and labels the whole-block best path a retrospective
oracle. Structural score filtering, time-varying population-rank inference,
and learned refit scheduling remain later work. The authoritative scope is
[[Future application programme — factor scores, predictive rank, and online RFD]].

Richardson centre extraction is now an evidence-backed application follow-up rather than a generic replacement idea. On monthly APP-FIN, full Richardson raised cross-fitted squared BW loss by 183.8%; the narrowest held-out stage reached effective sample size about 4.5, and both alternating tuning halves preferred only 0.2 of the global-to-Richardson displacement. Positive local was stable but modest. This does not disprove exact asymptotic bias cancellation: the signed weights have absolute mass five, amplify the joint stage-noise/curvature remainder, and operate here with very small local samples. The follow-up must first compare predeclared scale ratios, kernels, extra-scale covariance-aware weights, and causal regularisation; only later compare a learned **causal** centre head using identical masks and untouched future blocks. Every alternative must preserve SPD/generated-domain validity and smoothness and be hostile-tested on P1-ID-equivalent laws; apparent recovery of an impossible centre/factor split is leakage or an undeclared convention. See [[Future application programme — factor scores, predictive rank, and online RFD]].

The parked order is therefore

$$
\text{fixed Paper 1 RFD extraction and causal APP-FIN rank policy}
\rightarrow
\text{latent-score filtering and online predictive rank}
\rightarrow
\text{event-triggered geometric refitting}
\rightarrow
\text{optional learned centre extraction}.
$$

This is the current **Paper 2 candidate**, not a reserved publication label.
Its canonical scope is
[[Future application programme — factor scores, predictive rank, and online RFD]].
The expanded masked-learning brainstorm remains archived at
`notes/archive/Future programme ideation — identifiable geometric learning for RFD.md`
and is not a separate canonical programme.

## Main current risks

- P1-ID proves generic weakened-reference rigidity false and identifies the compatible-chart orbit, with an exact curved rank-inflation boundary. Its fixed-centre theorem supports superposition/non-separation, not claims that Factor 1 is spurious or drift-dominated.
- The robust growing-\(p_n\) rate remains slower than the parent fixed-centre oracle rate. FRAME-2P-U matches the oracle numerator's root-\(n\) **order** only under U2P; its added validation influence changes the limit variance, and no genuinely growing-curvature application has yet been verified.
- Cross-fitting alone does not restore quadratic curved recentering. Same-band score correction is disproved; the successful route needs an independently undersmoothed validation path with \(1/6<\gamma<3/14\), exact local law or \(a>1/2\), and dimension-uniform composed-action/replacement control.
- The moving-loading programme cannot inherit a Euclidean bootstrap merely by changing frame or substituting an $L^2$ mean rate.
- Bures–Wasserstein boundary distance and rank loss require the proved local/regularized estimator; the global PSD theorem is false.
- The parent’s covariance demonstration can consume the fixed-size BW theorem only after its covariance-estimation measurement layer and generated-domain margins are checked.
- Growing energy can be offset by growing signal only through the proved assembly/gap phase conditions; rescaling can erase localised factors.
- The raw factor-number ratio is disproved as a consequence of the available eigenvalue rates; threshold and ridged selectors are proved internally.

## Live work

P1-ID is closed and supplies the interpretation boundary. The AIRM centre,
bounded-energy, selector, scientific-control, orientation-phase, amplitude, and
compact fixed-size BW diagnostics are complete. Paper 1 now closes through
two empirical steps: the now-completed literal parent parity on common BW
synthetic draws, followed by a fixed-rank non-forecasting APP-FIN identification
illustration. The exact order and terminal conditions are in
[[OPEN OBLIGATIONS — current research actions]], [[Numerical suite — theorem-driven design matrix]]
§3F, and [[Paper 1 shape — identification to application]].

The full N-10 shrinking-margin, N-15 growing-size, FRAME-2P-U application,
exhaustive N-18 phase, learned forecasting, infinite-memory conditional
splitting, unrestricted full-AIRM signed Hessian, higher positive smoothing,
and unrestricted BW exponent-sharpness programmes are secondary rather than
Paper 1 gates. The unattended parent simulations may finish independently.
The moving-loading programme is parked, standalone, and unnumbered.

## Related notes

- [[Analytical reconstruction — proof ledger and rebuilt spec]]
- [[P1-ID — centre-drift and factor identification boundary]]
- [[G1 audit — resolution of the uniform local Fréchet rate]]
- [[Paper 1 — Locally stationary Riemannian factor model]]
- [[Parked programme — Intrinsically moving loading subspace]]
- [[Application map — geometry, symmetry, and rate accelerators]]
- [[Future application programme — factor scores, predictive rank, and online RFD]]
- [[Numerical suite — theorem-driven design matrix]]
- [[OPEN OBLIGATIONS — current research actions]]
