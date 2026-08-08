---
type: archived-action-board
title: OPEN OBLIGATIONS — pre-reconstruction 2026-08-08
status: archived-superseded
last-audited: 2026-08-08
---

# OPEN OBLIGATIONS — current research actions

> **ARCHIVED 2026-08-08.** This queue is not live. It is preserved to retain the completed proof specifications. The only current queue is [[OPEN OBLIGATIONS — current research actions]].

> **Historical wording:** this file formerly served as the only live queue. It was superseded by the canonical reconstruction.

## 0. Current programme status

Paper 1 has a complete robust **growing-\(p_n\) theorem under explicit assumptions** and a dependency-checked application library in [[Application map — geometry, symmetry, and rate accelerators]]. The robust rate is nonparametric. A flat/common-commuting exact-split branch has a genuine oracle \(n^{-1/2}\) numerator; known and root-\(n\) parametric centres give oracle order, with the latter not first-order immune. Fixed-band AIRM higher differentials, a Hilbert physical-dependence robust extension, and a structured signed growing-\(p_n\) mean route are also proved. Paper 2 remains separate and unchanged.

## 0A. Application-map obligations closed or sharply replaced

- **APP-LEDGER — PROVED.** The two mean/Hessian and two non-rigid-frame linear lag terms are explicit in the canonical map.
- **APP-FLAT — PROVED UNDER EXPLICIT ASSUMPTIONS.** One simply connected convex flat plus exact innovation separation yields quadratic feasible recentering and the oracle loading numerator.
- **APP-PAR — PROVED.** Known, constant-pooled, and finite-dimensional root-\(n\) centre branches are separated. Root-\(n\) parametric fitting gives oracle order but is not negligible first order.
- **APP-AIRM — PROVED.** Fixed absolute generated spectral bands give all fixed-order HD-G AIRM differentials in the project norms, uniformly in matrix size. Energy and signal remain separate.
- **APP-PD — PROVED.** Summable causal Hilbert physical dependence replaces fixed finite memory in the robust G1/oracle-row chain.
- **APP-SIGNED — PROVED UNDER STRUCTURAL HESSIAN ASSUMPTIONS.** Deterministic, scalar-plus-HS, and controlled block-scalar Hessians permit signed growing-\(p_n\) G1. Unrestricted full AIRM remains open.
- **APP-SHORTCUT WARNINGS — DISPROVED.** Local symmetry, flatness alone, marginal sign symmetry, isotropic expected Hessian, nominal cross-fitting, time-local commutation, coordinatewise energy, higher smoothing alone, and root-\(n\) centre estimation alone do not imply first-order immunity.
- **APP-REALITY — PROVED/CLASSIFIED.** Approximate GLO/algebra/frame, dependence, lag-contamination, energy, band-escape, lag-tail, and signal defects have explicit penalties and feasibility labels.

## 0B. Paper 1 obligations closed by HD1

- **HD1 — PROVED UNDER EXPLICIT ASSUMPTIONS.** See [[HD1 — growing-dimension Paper 1 proof dossier]].
- **P1-OP — PROVED.** Dimension-free oracle HS concentration, pathwise feasible-versus-oracle control, and deterministic row assembly are internal.
- **P1-CF — SUPERSEDED for the final theorem.** The robust Route R needs no cross-fitting. The sharper cross-fitted quadratic route is not consumed because cross-fitting alone fails to remove the curved random-Hessian term.
- **Signal/eigengap repair — PROVED.** Davis–Kahan uses $\Delta_n^{-1}$; $s_n^{-2}$ is only a corollary of $\Delta_n\ge s_n^2$.
- **Factor number — PROVED after replacement.** The beyond-rank square is proved from row-operator singular values. The raw ratio is disproved; threshold and ridged selectors are consistent.
- **G1′ repair — PROVED.** Level local stationarity pays $n^{-a}/b_n$, sharply. The final loading theorem bypasses G1′ by a proved polygonal-frame theorem.

The P0 entries immediately below are retained as the pre-run closure specifications; they are not live blockers.

## 1. Historical P0 closure specifications — all Paper 1 items closed

### [P1-OP — CLOSED] Self-contained lag-operator theorem

**Why it matters**

Theorem E currently assumes the $O_p(n^{-1/2})$ lag-operator input and an internal eigengap. The former Lam–Yao rate attribution was audited as unsupported.

**Exact mathematical obligation**

Under the Paper 1 transported, cross-fitted model, prove an operator-norm bound for $\hat{\mathbb L}-\mathbb L$ with every $h_0$, moment, mixing, bias, and mean-estimation term explicit; then derive the loading-space rate by Davis–Kahan with $\kappa$ defined as the population eigengap.

**Current assumptions**

Fixed $p$; finite fourth or stronger moments; stated mixing/summable lag conditions; serially uncorrelated idiosyncratic noise; cross-fitting; chosen G1 route; positive eigengap.

**What it blocks**

The self-contained fixed-$p$ headline Theorem E and any claim that the paper no longer relies on the unsupported Lam–Yao rate attribution.

**Known partial results**

T17–T25 give the additive and rotational perturbations. The algebraic Davis–Kahan step is dimension-free. The missing piece is a single complete sampling/operator theorem with the same estimator and assumptions.

**What would count as closure**

A theorem and proof yielding the displayed Paper 1 rate from the stated model, with no placeholder citation and no hidden dependence on $n$, $h_0$, or $p$.

**What would NOT count as closure**

Citing Lam–Yao's $\kappa_n$, assuming the final loading-space rate, or proving only entrywise covariance convergence.

**Suggested next attack**

Write $\hat S(h)-S(h)$ as oracle sampling error plus the already-audited mean/frame terms; sum over fixed $h_0$; bound $\hat{\mathbb L}-\mathbb L$ directly; apply Davis–Kahan once.

**Estimated scope**
- Paper 1

### [P1-CF — SUPERSEDED] Formal cross-fitted estimator and coupling proof

**Why it matters**

Without cross-fitting, the stochastic frame error and the lag moments use the same observations; T20's commutator collapse is not proved for that coupling.

**Exact mathematical obligation**

Define leave-block-out mean/frame estimates for every lagged product, choose block length exceeding the largest lag and the dependence buffer, and prove that the construction preserves G1$_{L^2}$/G1′$_{L^2}$ while removing the first-order feasible-moment defect and delivering the conditional independence/decoupling used in T20.

**Current assumptions**

Fixed $p$; maximum lag $h_0$; mixing; local bandwidth $b$; one of the two canonical mean estimators.

**What it blocks**

The general stochastic rotational part of Theorem E for the estimator actually written in Paper 1.

**Known partial results**

T15 shows leave-block-out removes the $O((nb)^{-1})$ overlap defect. T20–T25 are proved when the rotation is deterministic or decoupled.

**What would count as closure**

A fully specified estimator plus a coupling/conditioning proof whose remainder is included in Theorem E.

**What would NOT count as closure**

Saying cross-fitting is standard, splitting the sample without checking the local mean rate, or treating zero covariance as independence.

**Suggested next attack**

Use alternating blocks with a gap larger than $h_0$ and the mixing truncation length; condition on the training blocks; rerun the integrated score and ribbon bounds on evaluation blocks.

**Estimated scope**
- Paper 1

### [HD1 — CLOSED UNDER EXPLICIT ASSUMPTIONS] Retain a growing-dimensional scope

**Why it matters**

The parent RFM's locally recorded headline permits $p=p_n\to\infty$. The moving-centre project currently proves only fixed $p$. Calling it an extension without this qualification would drop a central parent regime.

**Exact mathematical obligation**

Produce one triangular-array theorem closing, under a common assumption set: support/tube probability, score concentration, signed-Hessian concentration or positive-route alternative, G1$_{L^2}$ dimension budget, transport error, lag-covariance operator estimation, idiosyncratic covariance, factor-strength/eigengap scaling, Davis–Kahan input, and factor-number selection.

**Current assumptions**

Affine-invariant SPD with uniformly bounded tube gives dimension-free geometry. The current concentration proofs use finite-dimensional nets and a fixed polynomial-mixing threshold. T44–T46 give support budgets but not the full operator theorem.

**What it blocks**

Any statement that Paper 1 matches or extends the parent's $p_n\to\infty$ theorem; any high-dimensional factor-number claim.

**Known partial results**

The Hessian net has been corrected from $O(p^2)$ to $O(p)$ entropy. H-LIP-SYM is dimension-free on bounded SPD tubes. Davis–Kahan itself is dimension-free. Every unresolved component is itemised in the HD1 table of the analytical reconstruction.

**What would count as closure**

A proved admissible region for $(p_n,b_n,h_0,\kappa_n)$ and dependence/moment parameters, ending in a uniform loading-space rate and a separately justified factor-number statement.

**What would NOT count as closure**

Proving only dimension-free curvature constants, writing the pointwise rate with $p$ inserted, or saying a sphere net “allows high dimension” without closing the union-bound and operator chain.

**Suggested next attack**

Start with the positive-weight $q=3$ route to avoid signed Hessian concentration. Derive a triangular-array score bound and lag-operator bound under the same dependence regime; only then compare with the signed route.

**Estimated scope**
- high-dimensional extension only

## 2. P1 — important but bypassable

### [P2-XT] Cross-tangent loading-operator algebra

**Why it matters**

It is the identification backbone of Paper 2.

**Exact mathematical obligation**

Type and prove $\Gamma_t(h)=A_tC_t(h)A_{t-h}^*$, include factor–noise cross terms, define the local loading operator, and prove when its image equals $\operatorname{Im}A_t$.

**Current assumptions**

Smooth moving isometric loading path, locally stationary factors, serial conditions on noise, connector/parallel-frame machinery T50–T54.

**What it blocks**

Paper 2 identification and every local estimator theorem.

**Known partial results**

The pullback frame identities and covariant smoothness equalities are proved.

**What would count as closure**

A fibre-correct operator identity and image theorem with explicit rank/eigengap conditions.

**What would NOT count as closure**

Writing Euclidean matrices in different tangent spaces or assuming every lagged isometry cancels without proof.

**Suggested next attack**

Work entirely in the true parallel frame first, prove the Euclidean operator identity there, then push it back covariantly.

**Estimated scope**
- Paper 2

### [P2-LOC] Localised operator concentration

**Why it matters**

Paper 2 uses effective sample size $nh$ and cannot inherit Paper 1's global factor step.

**Exact mathematical obligation**

Prove uniform local score and lag-operator concentration with explicit $n,h,p$, mixing, block, lag-count, and eigengap dependence.

**Current assumptions**

P2-XT; fixed $p$ first; locally stationary dependence; bounded/moment-controlled transported observations.

**What it blocks**

The Paper 2 loading-space estimator, its rate, and all high-dimensional Paper 2 claims.

**Known partial results**

Paper 1 supplies mean/frame inputs and T55-A supplies conditional bandwidth algebra once P2-LOC provides the internal uniform benchmark.

**What would count as closure**

A uniform operator theorem at effective sample size $nh$ and its Davis–Kahan consequence.

**What would NOT count as closure**

Replacing $n$ by $nh$ in a global theorem without rechecking dependence, entropy, and bias.

**Suggested next attack**

Close fixed $p$ after P2-XT; defer $p_n$ until the local theorem is correct.

**Estimated scope**
- Paper 2

### [P2-BOOT] Estimated-frame multiplier bootstrap

**Why it matters**

Frame error manufactures the same non-constant projector alternative that the test targets.

**Exact mathematical obligation**

Prove that the bootstrap either re-estimates and reproduces the frame channel or that the channel is negligible in the exact supremum topology and anti-concentration scale of the statistic.

**Current assumptions**

P2-LOC; T50–T55-A; one canonical mean estimator; block multiplier scheme.

**What it blocks**

Paper 2 test size, bootstrap validity, and local power.

**Known partial results**

The conditional frame-error algebra is available. The old external quantity $\varrho_n$ was a citation error and has been removed; P2-LOC must supply the internal uniform benchmark.

**What would count as closure**

A conditional weak-approximation/bootstrap theorem with the estimated-frame remainder explicitly controlled.

**What would NOT count as closure**

Substituting G1$_{L^2}$ into a uniform theorem, citing the Euclidean bootstrap unchanged, or simulation agreement.

**Suggested next attack**

Formulate a bootstrap that recomputes $\hat\mu$ and the frame inside each draw; compare it with an oracle-frame process through the typed ribbon bound.

**Estimated scope**
- Paper 2

### [P1-ID] Curved-space necessity in mean/factor identification

**Why it matters**

The current pointwise local-mean condition is sufficient. The exact nonlinear ambiguity on curved manifolds is characterised only partially.

**Exact mathematical obligation**

Determine whether the geodesic-in-loading-space ambiguity is necessary, or give a counterexample.

**Current assumptions**

Smooth Hadamard geometry and the Paper 1 model class.

**What it blocks**

Only a sharp identification theorem; the current fixed-$p$ paper can proceed with the sufficient condition.

**Known partial results**

The Euclidean ambiguity and its pointwise LME repair are proved; curved sufficiency along common geodesics is proved.

**What would count as closure**

A necessity theorem or explicit nonlinear counterexample within the stated model class.

**What would NOT count as closure**

Repeating the Euclidean reparametrisation in different tangent spaces.

**Suggested next attack**

Analyse equality of two exponential representations via Jacobi fields along the candidate centre displacement.

**Estimated scope**
- Paper 1

## 3. P2 — optional generalisations / sharpness

### [GEO-N] Necessity of curvature-derivative control

**Why it matters**

It determines the minimal quantitative primitive for H-LIP outside compact fixed-$p$ settings.

**Exact mathematical obligation**

Decide whether $(K_0,\rho^*,\Theta)$ alone controls $\nabla H$, or construct a non-conjugate counterexample.

**Current assumptions**

Uniform curvature, tube radius, and quantitative non-conjugacy.

**What it blocks**

No current fixed-$p$ or SPD theorem; sharpness/general geometry only.

**Known partial results**

$|\nabla R|$ and $K_1^{\rm av}$ are sufficient. The sphere shows failure only as $\Theta\to\infty$.

**What would count as closure**

A theorem using only $(K_0,\rho^*,\Theta)$ or a counterexample with these uniformly bounded and $\|\nabla H\|\to\infty$.

**What would NOT count as closure**

Approaching a conjugate point, or observing $\nabla R$ in one proof route.

**Suggested next attack**

Study the Green-kernel integral in H-LIP rather than the sup norm of $\nabla R$.

**Estimated scope**
- optional generalisation

### [GEO-AV] Separate $K_1^{\rm av}$ from $\|\nabla R\|_\infty$

**Why it matters**

Without an example, “strictly weaker” is unsupported.

**Exact mathematical obligation**

Construct a geodesic tube with finite uniform $K_1^{\rm av}$ and unbounded $\|\nabla R\|_\infty$, while retaining the other H-LIP primitives.

**Current assumptions**

As in H-LIP′.

**What it blocks**

Only the logical strictness claim.

**Known partial results**

$K_1^{\rm av}\le C K_1$; oscillatory cancellation is a heuristic, not a proved separating example.

**What would count as closure**

One complete analytic example.

**What would NOT count as closure**

A formal inequality or an unverified oscillatory ansatz.

**Suggested next attack**

Use an explicit two-dimensional warped metric where the Jacobi Green kernel is computable.

**Estimated scope**
- optional generalisation

### [G1-Q4] Positive-weight bias order at least four

**Why it matters**

It would give a higher-order positive route without signed objectives.

**Exact mathematical obligation**

Add and analyse the third-order change-of-base-point curvature correction so the tangent combination has remainder $O(b^4)$.

**Current assumptions**

$C^4$ law/mean smoothness and positive scale-family barycentres.

**What it blocks**

Nothing current; $q=3$ already makes the certified bandwidth window nonempty.

**Known partial results**

Scale-family Richardson cancels polynomial bias, but the uncorrected tangent-base change is cubic.

**What would count as closure**

An explicit corrected estimator and uniform $O_p(b^4+\sqrt{\log n/(nb)}+n^{-a})$ theorem.

**What would NOT count as closure**

Adding a fourth scale without correcting the cubic geometry.

**Suggested next attack**

Use the existing Gavrilov/Pennec base-point expansion to subtract the cubic term.

**Estimated scope**
- Paper 1

### [STAT-MIX] Sharpness of the polynomial-mixing threshold

**Why it matters**

The current exponent is sufficient and may be conservative.

**Exact mathematical obligation**

Either improve the blocking/union-bound proof or construct a lower bound showing failure below a stated exponent.

**Current assumptions**

Fixed $p$, bounded summands, $b=n^{-\alpha}$, polynomial $\alpha$-mixing.

**What it blocks**

No current theorem; only assumption sharpness.

**Known partial results**

The Liebscher/Rio route gives $\beta>1+2\gamma/(1-\alpha)$.

**What would count as closure**

A better proved sufficient region or a matching failure construction.

**What would NOT count as closure**

Simulation or calling the current threshold necessary.

**Suggested next attack**

Optimise block length and the time/spatial nets before attempting a lower bound.

**Estimated scope**
- optional generalisation

### [SW-FS] Finite-sample SW-AS constants

**Why it matters**

It would quantify the localisation event and permit finite-$n$ guarantees for the signed route.

**Exact mathematical obligation**

Track the probability, localisation radius, weight mass, Hessian bound, moduli, and mixing constants in SW-AS.

**Current assumptions**

S1–S5 or quantitative H-LIP/SW-L assumptions.

**What it blocks**

No asymptotic headline; only finite-sample statements and an unlocalised comparison.

**Known partial results**

The asymptotic $O_p$ perturbation and the separate finite-sample convexity safeguard are proved.

**What would count as closure**

A non-asymptotic probability bound guaranteeing a unique interior local minimiser.

**What would NOT count as closure**

Restating $o_p(1)$ or imposing the old global signed convexity condition without quantifying it.

**Suggested next attack**

Expose constants in the scalarised Hessian Bernstein and net argument.

**Estimated scope**
- optional generalisation

### [BW-SHARP] Sharpness of the bandwidth-window endpoint

**Why it matters**

The current $\alpha<1/4$ endpoint is sufficient; cancellation could widen it.

**Exact mathematical obligation**

Determine whether $\mathbb E[e\wedge\nabla_se]$ cancels at the relevant order, or give a lower-bound construction showing it does not.

**Current assumptions**

Paper 1 fixed-$p$ mean/frame model and one canonical estimator.

**What it blocks**

No current recommended bandwidth; only the width and necessity claim.

**Known partial results**

The certified window $1/(2q)<\alpha<1/4$ is sufficient and contains $\alpha=1/5$ at $q=3$.

**What would count as closure**

A proved cancellation theorem or matching lower bound.

**What would NOT count as closure**

Pointwise numerics or an argument that ignores the integrated ribbon term.

**Suggested next attack**

Compute the leading expectation under cross-fitting in the flat and constant-curvature cases first.

**Estimated scope**
- optional generalisation

## 4. Citation / external-verification queue

- **CIT-LYB:** no longer load-bearing; P1-OP is internal. Do not cite Lam–Yao (2012) for the old display.
- **CIT-HCC — VERIFIED FROM PRIMARY SOURCE:** the parent defines its (kappa) as a factor-lag singular value, states (lambda_r\ge\kappa^2), reports the fixed-centre dimension-free (n^{-1/2}/\kappa^2) rate, and states the signal/null eigenvalue rates. These statements do not broaden HD1 automatically.
- **CIT-HESS:** preserve the locally recorded general upper Hessian comparison citation $H\preceq\zeta(d)I$; the repository derives only the constant-curvature equality case.
- **CIT-ER:** verify any finite-sample or growing-$p$ eigenvalue-ratio claim before using it. The locally recorded Lam–Yao remark does not prove behaviour beyond the true rank.

## 5. Repository / writing cleanup

- Convert the detailed historical ledger's remaining `CONJECTURE` vocabulary to `OPEN` if it is ever promoted back into a current table.
- Keep numerical tables out of theorem evidence; they may be retained only as historical diagnostics.
- Paper 1 now references the internal P1-OP/HD1 theorem and records the parent comparison without broadening the result.

## 6. Optional next Paper 1 run

No open item blocks the robust theorem or any application branch labelled proved. The remaining optional Paper 1 questions are exact and non-consumed:

1. **APP-CF-PD:** prove estimator-stable joint retained-row coupling or a conditional Hilbert/HS physical-dependence inequality for oracle cancellation under infinite memory.
2. **APP-FR-DEB:** construct a generic curved estimator that makes the non-rigid frame coefficient \(\phi_{F,n}=o(n^{-1/2})\); GLO alone is disproved as sufficient.
3. **APP-AIRM-SIGNED:** prove or disprove a matrix-size-uniform scalar-plus-HS/fixed-block representation for the full AIRM random Hessian.
4. **G1-Q4:** construct the already-listed curvature-corrected positive estimator of certified order at least four.
5. **APP-BW:** develop the full growing-size Bures–Wasserstein tube/differential theory.

See the canonical application map §10 for statuses and exact dependencies.
