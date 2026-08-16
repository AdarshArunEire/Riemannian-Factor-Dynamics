# FRAME-DB — generic curved non-rigid frame debiasing team proof campaign

> **ARCHIVED RUN PROMPT — CAMPAIGN COMPLETED 2026-08-12.** The canonical result is FRAME-2P-U. This prompt is proof provenance, not a live obligation; the completed FRAME-DB and FRAME-IF dossiers are under `Archived/Proof workstreams`.

You are now the **lead mathematical researcher, estimator architect, adversarial auditor, and proof-record maintainer** for the FRAME-DB campaign in the Riemannian Factor Dynamics repository.

Your task is to decide whether a feasible, generic curved-manifold correction can remove the first-order non-rigid frame contamination from Paper 1's lag row. A successful campaign may produce:

1. a proved feasible generic debiasing estimator;
2. a proved estimator under explicit additional geometric/statistical structure;
3. an analytic impossibility or non-identifiability result, followed by the strongest corrected theorem;
4. one precisely isolated irreducible open lemma after all mandated constructions and attacks have been exhausted.

The desired optimistic result is not assumed true. The campaign succeeds when the strongest correct verdict is proved and recorded without leaving a provisional claim for the project lead to repair.

This campaign produces **noncanonical proof dossiers and a lead adjudication only**. Do not edit current canonical theorem files. Canonical reintegration and the subsequent notation freeze will be a separate project-lead action after this campaign.

Paper 2 is out of scope.

## 0. Read before proving

Read the repository instructions and these current canonical sources completely:

1. `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md`;
2. `Ideas/Paper 1 — Locally stationary Riemannian factor model.md`;
3. `Ideas/HD1 — growing-dimension Paper 1 proof dossier.md`;
4. `Ideas/G1 audit — resolution of the uniform local Fréchet rate.md`;
5. `Ideas/Application map — geometry, symmetry, and rate accelerators.md`;
6. `Ideas/OPEN OBLIGATIONS — current research actions.md`;
7. `Ideas/Time-varying Fréchet mean Riemannian factor model.md`.

Then read these archived proof sources completely:

- `Ideas/Archived/Proof workstreams/APP-B — cancellation and oracle-rate proof dossier.md` — governing four-term expansion, coefficient definitions, residual theorem, and counterexamples;
- `Ideas/Archived/Proof workstreams/HD1-B — lag operator signal and factor number proof dossier.md` — sharper route and non-rigid-frame interface;
- `Ideas/Archived/Proof workstreams/HD1-C — hostile counterexamples and assumption audit.md` — theorem boundaries and frame attacks;
- `Ideas/Archived/Proof workstreams/APP-A — geometry and differential application atlas.md` — ribbon/curvature and near-flat geometry;
- `Ideas/Archived/Proof workstreams/APP-C — dependence, dimension, and hostile application audit.md` — dimension-free Hilbert/HS concentration and the corrected frame-energy norm.

Archived status statements never override current canon. APP-B supplies the exact FRAME-DB starting algebra; it does not itself supply a feasible debiaser.

## 1. Fixed starting point

After one common anchor rotation has been removed, APP-B proves that the aligned feasible tangent vector has expansion

\[
U_t=Y_t-H_te_t+\Omega_tY_t+\xi_t^{(2)},
\]

where

\[
e_t=\log_{\mu_t}\widehat\mu_t,
\qquad
H_t=\tfrac12\operatorname{Hess}_{\mu_t}d(\mu_t,X_t)^2,
\qquad
\Omega_t^*=-\Omega_t,
\]

and

\[
\|\xi_t^{(2)}\|
\lesssim
\|e_t\|^2+\|e_t\|\|\Omega_t\|+\|Y_t\|\|\Omega_t\|^2.
\]

For lag \(h\), the four first-order terms are

\[
\begin{aligned}
L_{t,h}^{\rm mean}
&=-H_te_t\otimes Y_{t-h}-Y_t\otimes H_{t-h}e_{t-h},\\
L_{t,h}^{\rm fr}
&=\Omega_tY_t\otimes Y_{t-h}
+Y_t\otimes\Omega_{t-h}Y_{t-h}.
\end{aligned}
\tag{1.1}
\]

Under exact training/evaluation separation and lag-specific GLO, the mean terms are conditionally centred and contribute only their empirical fluctuation plus quadratic errors. The unresolved curved-frame population coefficient is

\[
\Phi_{F,n}(h)
=N_{n,h}^{-1}\sum_t
\{\Omega_t\Gamma_{t,h}-\Gamma_{t,h}\Omega_{t-h}\},
\tag{1.2}
\]

with direct-sum Hilbert--Schmidt size

\[
\phi_{F,n}^2=\sum_{h=1}^{h_0}\|\Phi_{F,n}(h)\|_{\rm HS}^2.
\tag{1.3}
\]

Cross-fitting and GLO do not remove (1.2). APP-B CE-B5 proves this. If \(\Omega_t\) is one common rigid skew operator, its effect is an exact common conjugation and must be absorbed into the anchor rotation rather than treated as additive error. FRAME-DB concerns only the remaining time-varying non-rigid component.

The corrected oracle row theorem already proves

\[
d_n=O_p\!\left[
n^{-1/2}+(r_e+r_F)n^{-1/2}
+\varepsilon_{G,n}r_e+\phi_{F,n}
+r_e^2+r_er_F+r_F^2+\rho_n
\right].
\tag{1.4}
\]

At the canonical \(b_n=n^{-1/7}\), \(r_e,r_F=O_p(\ell_n)\), the quadratic terms are already \(o(n^{-1/2})\). The binding issue is first-order frame contamination, not a need for higher-order smoothing.

## 2. Exact primary objective

Assume the existing bounded-total-energy Paper 1 package, fixed retained lag count and memory, exact training/evaluation separation, and GLO for the mean channel. Construct a **feasible** corrected lag row or a feasible alternative estimator for which the residual frame contribution satisfies

\[
d_{F,{\rm db},n}=o_p(n^{-1/2})
\tag{2.1}
\]

in direct-sum Hilbert--Schmidt norm, under explicit dimension-uniform assumptions on the generic curved geometry and data law.

A stronger and especially useful sufficient result is a second-order residual

\[
d_{F,{\rm db},n}
=O_p(r_e^2+r_er_F+r_F^2)+o_p(n^{-1/2}).
\tag{2.2}
\]

The resulting theorem must reach

\[
d_n^{\rm db}
=O_p\!\left(n^{-1/2}+\ell_n^2
+\varepsilon_{G,n}\ell_n+d_{F,{\rm db},n}+\rho_n\right),
\tag{2.3}
\]

and, under the existing signal conditions,

\[
\|\sin\Theta(\widehat E_n^{\rm db},E_n)\|_{\rm op}
=O_p(n^{-1/2}/\Delta_n),
\qquad
\widehat\lambda_{r+1,n}^{\rm db}=O_p(n^{-1}).
\tag{2.4}
\]

If (2.1) is impossible generically, prove that fact analytically and identify the weakest additional information or structure that restores it.

## 3. Feasibility and observability requirements

A proposed correction is not feasible if it uses, without an estimable replacement:

- the true centre \(\mu_t\);
- the true parallel frame;
- the true anchor alignment \(Q\);
- the true errors \(e_t\) or \(\Omega_t\);
- the population lag row \(\Gamma_{t,h}\);
- an unobserved curvature ribbon or Jacobi field;
- an oracle Hessian evaluated at an unknown population pair.

Every candidate must list exactly what is observed, what is trained on an independent fold, what is estimated, and what population quantity remains in its residual.

The definition of \(\Omega_t\) is gauge-relative. The correction must be equivariant under a common anchor rotation. It may estimate only the time-varying residual modulo one common rigid conjugation; it must not pay a Davis--Kahan penalty for a harmless common change of coordinates.

## 4. Candidate estimator classes that must be tested

The team must seriously investigate all four classes before declaring the problem irreducible.

### 4.1 Plug-in infinitesimal-frame correction

Construct an estimator \(\widetilde\Omega_t\) and subtract

\[
N_{n,h}^{-1}\sum_t
\{\widetilde\Omega_t\widetilde Y_t\otimes\widetilde Y_{t-h}
+\widetilde Y_t\otimes
\widetilde\Omega_{t-h}\widetilde Y_{t-h}\}
\tag{4.1}
\]

from the feasible lag covariance. Derive the exact direct-sum HS residual, including estimation noise, dependence, common-gauge alignment, and products involving \(\widetilde Y-Y\).

Do not assume that the difference of two noisy frames estimates either frame's error relative to truth. Prove the relevant influence or synchronization identity.

### 4.2 Influence-function/Jacobi correction

Differentiate parallel transport or the polygonal frame with respect to centre-path perturbations. Determine whether the first variation can be written as an observable curvature/Jacobi functional applied to a feasible influence estimate of \(e_t\). If so:

- derive the typed first-variation formula;
- state endpoint and connector terms;
- prove the estimator approximates \(\Omega_t\) at the required rate;
- retain curvature, path length, grid count, derivative order, and dimension constants explicitly.

An asserted “holonomy equals curvature times area” slogan is insufficient; the actual ribbon, endpoint fibres, and orientation must be specified.

### 4.3 Multi-fold, jackknife, Richardson, or orthogonal-score correction

Test whether independent centre/frame estimates can be combined so their first-order frame errors cancel while preserving the target lag row. Candidate weights must cancel the actual derivative of the frame functional, not merely the mean bias.

If an estimating equation can be made Neyman-orthogonal to centre/frame nuisance perturbations, write its Gateaux derivative and prove it vanishes in all admissible nuisance directions. An orthogonality label without the derivative calculation has no status.

### 4.4 Frame-avoiding or gauge-invariant estimator redesign

Determine whether loading information can be recovered from intrinsic lag-pair objects that do not require one estimated global frame, for example through pairwise transport, synchronized transports, conjugacy-invariant operators, or a quotient target. The redesigned estimator must still estimate the Paper 1 loading space or must explicitly declare and justify a changed estimand.

Changing the estimand silently is not debiasing.

## 5. Team structure

Use one lead and exactly three parallel subagents, subject to available concurrency. Each subagent writes one noncanonical dossier under `Ideas/Working proof dossiers/`. Do not edit canonical files.

### Agent A — geometry, gauge, and frame influence

Own:

- the exact first variation of radial and polygonal parallel transport under centre-path perturbation;
- the relationship between ribbon holonomy, the estimated mean error, and \(\Omega_t\);
- common-gauge removal and synchronization;
- endpoint connector and boundary terms;
- fixed-order dimension-uniform curvature/Jacobi assumptions;
- candidate influence-function and frame-avoiding constructions.

Agent A must separate identities valid for a smooth path, the actual polygonal estimator, and an arbitrary external frame. It must verify scalar, flat, constant-curvature, AIRM, and generic curved edge cases.

### Agent B — feasible estimator and statistical rate

Own:

- construction of plug-in, multi-fold, orthogonal-score, or redesigned corrected lag rows;
- training/evaluation/sample-split architecture;
- direct-sum HS concentration of every correction term;
- exact residual \(d_{F,{\rm db},n}\);
- propagation through row assembly, Davis--Kahan, null spectrum, and factor selection;
- bandwidth, grid, mask, and dependence conditions;
- fixed-\(p\) closure first, followed by dimension-uniform growing-\(p_n\) closure if the producer norms permit it.

Agent B must not use \(A_{2,n}\), which is based on operator norms, to bound a Hilbert--Schmidt frame coefficient without a proved rank restriction. The valid general envelope uses

\[
G_{2,{\rm HS},n}^2
=\sum_{h=1}^{h_0}\sup_t\|\Gamma_{t,h}\|_{\rm HS}^2.
\]

### Agent C — hostile identifiability and counterexample audit

Initially do not help the optimistic proof. Attack every candidate for:

- use of the unknown true centre/frame/anchor;
- gauge non-identifiability;
- a common rigid rotation incorrectly treated as additive error;
- same-sample leakage or invalid conditional independence;
- failure to estimate \(\Omega_t\) more accurately than the original frame;
- a hidden derivative of the Hessian or connection;
- an HS/operator norm switch hiding rank or dimension;
- untyped path length, polygon count, or ribbon area;
- target change under a frame-avoiding construction;
- lag contamination or weak gap mistaken for frame error;
- numerical evidence presented as proof.

Construct analytic pairs of data-generating mechanisms with the same observable law but different frame corrections whenever possible. A valid impossibility theorem must state the estimator class and retained assumptions precisely; failure of one construction is not generic impossibility.

### Lead

The lead owns the common claim ledger, observability ledger, dependency graph, and final adjudication. It must independently rederive the four-term expansion interface and verify every proposed correction against APP-B CE-B1--CE-B8.

## 6. Common ledgers

Maintain a claim ledger:

| ID | Exact claim | Observable inputs | Unobservable target | Norm | Producer | Consumer | Rate | Objection | Resolution | Status |
|---|---|---|---|---|---|---|---|---|---|---|

Maintain a nuisance ledger:

| Nuisance | First-order coefficient | Proposed estimate/cancellation | Training fold | Evaluation fold | Residual | Required rate | Identifiability status |
|---|---|---|---|---|---|---|---|

Maintain a target ledger distinguishing:

1. oracle lag row in the true anchor frame;
2. the same row under one harmless common conjugation;
3. feasible row with time-varying frame contamination;
4. debiased feasible row;
5. any redesigned gauge-invariant target.

No two targets may be conflated.

## 7. Non-negotiable proof rules

1. Web searches and citations do not prove a FRAME-DB claim. An external theorem may be used only after its complete hypotheses, norms, and parameter uniformity are verified against the exact consumer.
2. Numerical experiments may diagnose algebra or suggest a counterexample but have zero proof status.
3. Every tangent fibre, connector, transport, adjoint, and tensor product must be typed.
4. Every rate must distinguish pathwise identity, population expectation, conditional expectation, and empirical fluctuation.
5. Keep mean/Hessian and frame channels separate. Solving GLO again does not solve FRAME-DB.
6. Cross-fitting makes trained nuisances conditionally fixed; it does not centre the signal-carrying frame coefficient.
7. Small sectional curvature, local symmetry, isotropy, a small matrix commutator, or moving along a geodesic is not frame debiasing unless linked to the exact coefficient (1.2).
8. Do not hide factor rank, ambient dimension, path/grid size, energy, or signal in constants.
9. The actual loading denominator is \(\Delta_n\). Replace it by \(s_n^2\) only after proving the required factorisation/gap inequality.
10. A negative result counts as completion only when it is an analytic counterexample or impossibility theorem satisfying every retained hypothesis.
11. A restricted theorem must propagate its new assumption only to its direct consumers; do not weaken the robust HD1 fallback.
12. Preserve unrelated user changes. Subagents edit only their named dossiers; the lead writes one adjudication ledger.

Allowed statuses are:

- `PROVED`;
- `PROVED UNDER EXPLICIT ASSUMPTIONS`;
- `DISPROVED`;
- `SUPERSEDED`;
- `OPEN — EXACT LEMMA STATED`.

Do not use “plausible”, “standard”, “natural”, “expected”, or “should follow” as load-bearing status language.

## 8. Mandatory edge cases and counterexample programme

Every proposed theorem must be tested on:

1. a flat Hilbert space, where true non-rigid frame error must vanish after common alignment;
2. one fixed commuting SPD flat;
3. a common rigid rotation \(\Omega_t\equiv\bar\Omega\), which must be absorbed rather than debiased additively;
4. APP-B CE-B5 with \([B,\Gamma(1)]\ne0\), which defeats GLO-only claims;
5. zero signal \(\Gamma_h=0\), where frame contamination of the population row vanishes but loading identification also fails;
6. zero idiosyncratic noise with an estimated moving centre, where frame error can remain;
7. constant curvature with a genuinely moving mean;
8. high-dimensional bounded-total-energy directions, to expose HS/operator or net costs;
9. concentrated grid error at one vertex;
10. high-frequency small-amplitude paths with bounded length but large acceleration;
11. nearly commuting matrices with a changing eigenbasis;
12. identical observable laws with different latent frame/centre decompositions, if such a construction is possible under the model.

## 9. First hostile pass

After Agents A and B produce complete first dossiers:

1. Agent C audits both from observables to final loading theorem.
2. Agent A attacks B's use of geometric derivatives, gauges, and connector comparisons.
3. Agent B attacks A's observability, sample-split architecture, and claimed rates.
4. The lead checks every correction term by expanding it back to (1.1).
5. Each objection receives a proof repair, theorem restriction, analytic counterexample, or explicit rejection.

Maintain:

| Claim | Attack | Repair/counterexample | Independent checker | Final status | Consequence |
|---|---|---|---|---|---|

## 10. Second hostile pass

Freeze the repaired dossiers. Agent C then performs a fresh complete-chain audit, including:

- exact gauge equivariance;
- feasibility without population quantities;
- all empirical correction fluctuations;
- the direct-sum HS residual;
- quadratic cross terms;
- dimension and rank dependence;
- mask/coupling/target defects;
- row assembly and actual eigengap;
- factor-number consequences;
- every edge family in Section 8.

No theorem status is earned before this pass and independent lead verification.

## 11. Adjudication gates

The lead must choose exactly one outcome.

### Gate A — generic curved debiaser proved

Use only if one feasible estimator achieves (2.1) on a genuinely nonflat, non-rigid class under explicit dimension-uniform assumptions and reaches (2.3)--(2.4) after both hostile passes.

Record:

- estimator definition;
- observability proof;
- exact residual theorem;
- rate and bandwidth conditions;
- geometry/dependence/signal package;
- nonempty DGP;
- loading and selector consequences.

### Gate B — restricted debiaser proved

Use if debiasing works only under additional structure such as known curvature, parametric mean dynamics, observable connection coefficients, a finite-dimensional nuisance model, special homogeneous geometry, or a restricted gauge. Prove the class is nonempty and state exactly which applications qualify.

Do not call this generic.

### Gate C — generic FRAME-DB disproved

Use only if an analytic impossibility or non-identifiability result covers the declared generic estimator/model class. Then prove the strongest surviving restricted theorem or estimator redesign. Preserve the robust \(n^{-3/7}\) Paper 1 theorem as the fallback.

### Gate D — exact irreducible open lemma

Use only after all four candidate classes in Section 4, the counterexample programme, and both hostile passes have been attempted. State the smallest missing observable approximation or concentration lemma and every theorem it would unlock. Do not leave a generic “estimate the frame better” instruction.

## 12. Scope expansion gate

The primary campaign is the bounded-energy, fixed-memory Paper 1 oracle branch. Do not begin growing-energy, infinite-memory, shrinking-margin BW, or application-specific propagation until the baseline FRAME-DB verdict is fixed.

If Gate A or B closes the baseline, the lead may state—but not prove by inspection—the additional ledgers required for:

- growing energy, where frame error is multiplied by the appropriate energy and HS lag budget;
- causal physical dependence;
- AIRM or BW application geometry;
- growing factor rank;
- shrinking spectral margins.

These are downstream campaigns unless the baseline proof already supplies every needed uniform constant.

## 13. Repository outputs

Create at most four noncanonical files:

1. `Ideas/Working proof dossiers/FRAME-DB-A — geometry gauge and influence.md`;
2. `Ideas/Working proof dossiers/FRAME-DB-B — feasible estimator and row theorem.md`;
3. `Ideas/Working proof dossiers/FRAME-DB-C — hostile identifiability and counterexamples.md`;
4. `Ideas/Working proof dossiers/FRAME-DB — lead adjudication ledger.md`.

At completion, move them to:

- `Ideas/Archived/Proof workstreams/` if they are complete proof/adjudication records;
- `Ideas/Archived/Incomplete proof sketches/` if they remain unverified or incomplete.

Do not modify:

- the analytical reconstruction;
- Paper 1;
- HD1 or G1;
- the application map;
- OPEN OBLIGATIONS;
- the numerical suite.

Instead, the lead adjudication must provide an exact proposed canonical migration table:

| Canonical file | Current statement | Proposed replacement | Proven producer | Status effect |
|---|---|---|---|---|

The project lead will perform canonical reintegration and the notation freeze separately.

## 14. Final report

Report in plain language first, then give the mathematical ledger:

1. whether generic curved frame debiasing is proved, restricted, disproved, or exactly open;
2. what is and is not observable;
3. the selected estimator or impossibility construction;
4. the residual \(d_{F,{\rm db},n}\) and its norm;
5. whether the oracle \(n^{-1/2}\) numerator is earned;
6. required geometry, splitting, dependence, energy, lag-target, and gap conditions;
7. application classes newly enabled or still excluded;
8. hostile objections and their resolutions;
9. files created and archived;
10. exact proposed canonical migrations;
11. exact remaining obligations;
12. mechanical verification of links, status labels, delimiters, and stale claims inside the new dossiers.

## 15. Final instruction

Drive the campaign until one adjudication gate is honestly reached. Do not stop at a candidate formula, literature reference, numerical check, or first failed proof. For every obstruction, attempt a direct proof, a counterexample, the weakest natural repair, and an estimator redesign.

The success criterion is not that a generic debiaser must exist. It is that the repository receives a complete, adversarially tested answer about whether the time-varying curved-frame coefficient can be feasibly removed, under what information and assumptions, and with what exact consequence for Paper 1's oracle loading rate.
