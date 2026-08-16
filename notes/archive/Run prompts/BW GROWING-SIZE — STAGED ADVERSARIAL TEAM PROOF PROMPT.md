> **ARCHIVED RUN PROMPT — CAMPAIGN COMPLETED 2026-08-09.** This file preserves the staged fixed-/shrinking-margin proof specification. It creates no live obligation and does not override the current canonical ledgers.

# BW growing-size — staged adversarial team proof campaign

You are now the **maintainer, lead proof architect, and adversarial auditor** for the Riemannian Factor Dynamics repository.

Run this as a proof-completion campaign with one lead and three mathematical subagents. Work directly in the repository. The campaign has a strict sequential gate:

1. attack **BW-SIZE-FIXED-MARGIN** first;
2. adjudicate it completely;
3. start **BW-SIZE-SHRINKING-MARGIN** as a fresh campaign only if the fixed-margin theorem is genuinely proved.

Do not work on the shrinking-margin lemma speculatively or in parallel with Stage 1.

This is not a literature review, numerical investigation, or request for a plausible proof sketch. Web searches may locate exact primary theorems, and computation may diagnose algebra, but neither has proof status. The acceptable mathematical outputs are a complete proof, an analytic counterexample, or an exact irreducible open lemma after all prescribed attacks have been exhausted.

## 0. Read before acting

Read the repository instructions and these current canonical sources completely:

1. `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md`;
2. `Ideas/Paper 1 — Locally stationary Riemannian factor model.md`;
3. `Ideas/HD1 — growing-dimension Paper 1 proof dossier.md`;
4. `Ideas/G1 audit — resolution of the uniform local Fréchet rate.md`;
5. `Ideas/Application map — geometry, symmetry, and rate accelerators.md`;
6. `Ideas/OPEN OBLIGATIONS — current research actions.md` — the only live queue;
7. `Ideas/Time-varying Fréchet mean Riemannian factor model.md`.

Then read the relevant proof provenance:

- `Ideas/Archived/Proof workstreams/BW — moving-centre Bures-Wasserstein working dossier.md`, especially Sections 9–10;
- `Ideas/Archived/Proof workstreams/Joint HE-BW error ledger and hostile audit.md`;
- `Ideas/Archived/Incomplete proof sketches/BW-SIZE-FIXED-MARGIN — dimension-uniform quotient calculus.md`;
- `Ideas/Archived/Run prompts/PAPER 1 HE AND BW — TEAM PROOF CAMPAIGN PROMPT.md` for proof hygiene only.

The incomplete fixed-margin sketch is a **noncanonical conjectural seed**. Every formula in it must be independently rederived. Its `CLAIMED; UNVERIFIED` rows and proposed constant are not evidence. Archived status labels never override the current canon.

Paper 2 is out of scope.

## 1. Absolute proof and status rules

1. Keep every norm typed: lift Frobenius norm, matrix operator norm, BW tangent norm, multilinear operator norm, path-speed norm, and any direct-sum norm.
2. At every matrix multiplication use an inequality that shows which factor is paid in operator norm and which in Frobenius norm. Never silently use Frobenius-by-Frobenius bounds if they introduce matrix size.
3. Never pass through \(\|L\|_F\asymp\sqrt m\), a coordinate count, fixed-dimensional compactness, or an untyped curve length.
4. Repeated positive eigenvalues are not a forbidden margin. Do not introduce an eigenvector eigengap when invariant square-root, polar, or Sylvester calculus avoids one.
5. Spectral bands, polar/Exp margins, normal radius, generated-set closure, total BW energy, and statistical signal are separate assumptions. Proving one does not prove another.
6. A cited theorem is usable only after its full hypotheses, norms, and parameter uniformity are checked against the exact repository consumer.
7. Numerical agreement, symbolic simplification, and finite-dimensional examples have zero theorem status.
8. A proof-technique failure is not a counterexample. A counterexample must satisfy every retained hypothesis and violate the claimed conclusion.
9. Do not label a claim `PROVED` because its originating agent says so. It must survive independent hostile review and lead verification.
10. Do not edit canonical theorem status until the relevant stage has passed its gate.

Allowed final labels are:

- `PROVED`;
- `PROVED UNDER EXPLICIT ASSUMPTIONS`;
- `DISPROVED`;
- `RETRACTED`;
- `SUPERSEDED`;
- `OPEN — EXACT LEMMA STATED`;
- `BLOCKED BY BW-SIZE-FIXED-MARGIN` for the untouched downstream shrinking-margin node when Stage 1 does not prove its prerequisite.

Do not use “plausible”, “standard”, “expected”, “routine”, or “should follow” as load-bearing language.

## 2. Repository editing discipline

At the start, inspect the current filesystem and preserve unrelated work.

Each subagent may write at most one clearly named noncanonical dossier under `Ideas/Working proof dossiers/`. Subagents must not concurrently edit canonical files. The lead alone integrates results after the stage gate and hostile passes.

Keep one common claim ledger containing:

| ID | Exact claim | Domain and margins | Input/output norms | Producer | Direct consumer | Dimension dependence | Objection | Resolution | Status |
|---|---|---|---|---|---|---|---|---|---|

At completion, move useful workstream dossiers to `Ideas/Archived/Proof workstreams/`, move failed but informative sketches to `Ideas/Archived/Incomplete proof sketches/`, and leave no second live status ledger on the surface.

## 3. Stage 1 — BW-SIZE-FIXED-MARGIN only

### 3.1 Exact target

Fix

\[
0<\alpha<\beta<\infty,\qquad \chi>0,\qquad r_0>0,\qquad k_0<\infty.
\]

On the exact full-rank local/regularized BW generated domain, prove or disprove that every fixed-order geometric constant consumed by G1 and the polygonal-frame theorem is bounded independently of matrix size \(m\) by one explicit finite function

\[
C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0).
\]

The target must cover, with exact formulas and typed norms:

1. derivatives through order \(k_0\) of the horizontal projector;
2. quotient connection derivatives;
3. the O'Neill tensor/curvature operator and the derivatives actually used by connection variation;
4. parameter derivatives of radial, connector, polygonal, and ruled-surface parallel transport from a typed variational ODE;
5. squared-distance score, observation Hessian, and every consumed base-point/observation derivative;
6. Exp, Log, polar alignment, Richardson, blend, chord, and ruled-surface derivatives;
7. base-varying BW tangent-norm equivalences;
8. a positive-Hessian and normal-radius theorem uniform in \(m\) on every generated pair;
9. finite polygonal accumulation with the exact dependence on path length, segment count if any, and \(r_0\).

The proof must state the precise generated-domain hypotheses. It may strengthen the current package only when the strengthened assumption is explicit, checkable, propagated to all consumers, and shown nonempty.

### 3.2 Team structure

Use exactly three subagents, subject to available concurrency.

#### Agent A — quotient and invariant matrix calculus

Independently derive:

- full-rank BW quotient/horizontal-lift definitions;
- tangent/lift norm equivalences;
- Sylvester inverses and horizontal projector derivatives;
- quotient connection and O'Neill formulas;
- fixed-order operator-by-Frobenius bounds without coordinate or multiplicity gaps.

Agent A must explicitly type every multilinear map and identify every use of \(\alpha,\beta,\chi\).

#### Agent B — transport, Hessian, and estimator-generated geometry

Independently derive:

- radial and polygonal PT ODEs and their parameter variations;
- connection-variation and ruled-surface bounds;
- Exp/Log and squared-distance Hessian derivatives;
- the dimension-uniform positive-Hessian/normal-radius step;
- Richardson/blend/chord closure and finite polygonal accumulation on the exact generated set.

Agent B must show that every path speed and length is typed and that no hidden segment-count or \(\sqrt m\) factor enters.

#### Agent C — hostile counterexamples and dependency audit

Do not help complete the optimistic proof initially. Attack it independently for:

- a hidden \(\|L\|_F\) or trace factor;
- an invalid horizontal/vertical identification;
- incorrect quotient connection or O'Neill signs/types;
- differentiation of gauge choices that are not smooth;
- nonunique polar alignment or missing singular-value margin;
- a PT Gronwall coefficient that grows with dimension or polygon length;
- a local Hessian argument that assumes the desired radius;
- generated endpoints or Richardson images leaving the declared domain;
- fixed-dimensional compactness disguised as a uniform derivative bound;
- a claimed constant that does not actually reach G1 or PF.

Construct analytic matrix families whenever possible. A valid disproof must retain fixed \(\alpha,\beta,\chi,r_0,k_0\).

#### Lead

The lead owns the ledger and canonical dependency graph. Independently rederive all headline formulas, compare A and B at their shared connection/transport boundary, and force every objection from C to receive a proof repair, theorem restriction, or counterexample verdict.

### 3.3 Mandatory two-pass cross-audit

After the first dossiers:

1. Agent A attacks B's use of quotient formulas and norm conversion.
2. Agent B attacks A's claim that primitive derivative bounds survive ODE composition and generated polygons.
3. Agent C attacks both complete chains and the proposed common constant.
4. The lead checks scalar \(m=1\), commuting diagonal, repeated-eigenvalue, identity-base, zero-path, many-segment, and high-dimensional fixed-band edge cases.
5. A and B repair or reject every objection.
6. Agent C performs a second hostile pass on the repaired theorem.

Maintain an objection table:

| Claim | Attack | Repair or counterexample | Independent checker | Final status | Canonical consequence |
|---|---|---|---|---|---|

## 4. Stage 1 adjudication gate

The lead must choose exactly one verdict.

### Gate A — fixed-margin proved

Use this only if every target in Section 3.1 is proved under one compatible assumption package, the constant is independent of \(m\), all direct G1/PF consumers are checked, and the result survives both hostile passes.

Actions:

1. integrate BW-SIZE-FIXED-MARGIN into every affected canonical source;
2. mark only that node proved;
3. archive the Stage 1 dossiers and objection ledger;
4. terminate the Stage 1 subagents;
5. start Stage 2 with fresh subagents and a fresh ledger. Do not let Stage 1 agents simply relabel coarse bounds as sharp shrinking-margin powers.

### Gate B — fixed-margin disproved

Use this only if there is a complete analytic counterexample satisfying fixed \(\alpha,\beta,\chi,r_0,k_0\) and the exact retained generated-domain assumptions while violating a necessary uniform consumer bound.

Actions:

1. integrate the counterexample and the strongest corrected theorem, if one survives;
2. mark BW-SIZE-FIXED-MARGIN `DISPROVED` or `SUPERSEDED` with exact scope;
3. do **not** start Stage 2;
4. mark the proposed shrinking-margin theorem impossible **for the same theorem class**, because constant margins are a special case of margin sequences;
5. distinguish this from the possibility of a redesigned estimator, a smaller geometry class, or additional structural assumptions.

### Gate C — fixed-margin unresolved

Use this when the team has neither a complete proof nor a valid counterexample after the two hostile passes and the prescribed alternative formulations.

Actions:

1. keep BW-SIZE-FIXED-MARGIN as `OPEN — EXACT LEMMA STATED`, narrowed to the irreducible missing equations;
2. stop the campaign;
3. do **not** start Stage 2;
4. label BW-SIZE-SHRINKING-MARGIN `BLOCKED BY BW-SIZE-FIXED-MARGIN`, not disproved and not impossible;
5. archive all incomplete work with prominent noncanonical/unverified banners.

Failure to prove something is not evidence that it is false.

## 5. Stage 2 — fresh BW-SIZE-SHRINKING-MARGIN campaign

Enter this section only after Gate A.

Start three fresh subagents. They must read the proved fixed-margin theorem and its proof, but treat every coarse exponent from Stage 1 as non-sharp until rederived.

### Fresh Agent D — primitive sharp-margin exponents

For every primitive and composed derivative, derive the smallest justified powers of the lower spectral margin \(\alpha_n\), upper bound \(\beta_n\), polar/Exp margin \(\chi_n\), normal radius, and any path/segment quantity. Separate genuine singular blow-up from artifacts of repeated chain-rule bounds.

### Fresh Agent E — statistical propagation and growth windows

Propagate the proved sharp constants through:

- mean localisation and G1;
- the complete generated-set event;
- polygonal framing;
- feasible tangent observations;
- oracle and feasible lag rows;
- \(d_n\), \(A_{2,n}\), and
  \[
  \eta_n=2A_{2,n}d_n+d_n^2;
  \]
- Davis–Kahan with the actual \(\Delta_n\);
- beyond-rank eigenvalues and the selector window.

State explicit nonempty \(m_n\)-versus-\(n\) regimes. If matrix size enters only through margins, energy, signal, or the number of generated objects, say so rather than inventing a direct dimension factor.

### Fresh Agent F — sharpness and impossibility auditor

Attack every exponent and growth window. Construct scalar, diagonal, rank-near-loss, polar-near-singular, and moving-eigenvector families to prove necessary blow-up powers or disprove overoptimistic windows. Check that no union bound, path discretisation, energy term, or eigengap denominator is omitted.

### Stage 2 lead duties

Build a new dependency ledger, independently check the exponent algebra, force two hostile passes, and classify separately:

1. geometry-constant blow-up;
2. generated-domain failure;
3. total-energy growth;
4. lag sampling and dependence;
5. signal/eigengap dilution;
6. factor-number selection.

Do not claim a full growing-\(m_n\) statistical theorem merely because the geometry constants are controlled.

## 6. Stage 2 verdicts

Accept one of:

- a proved sharp or explicitly sufficient shrinking-margin theorem with nonempty growth windows;
- a proved restricted window plus analytic impossibility beyond a boundary;
- a counterexample disproving the proposed shrinking-margin scope, followed by the strongest corrected theorem;
- `OPEN — EXACT LEMMA STATED` only for a precisely isolated exponent or consumer after proof and counterexample routes are exhausted.

There is no requirement that the optimistic shrinking-margin theorem be true. There is a requirement that no coarse Stage 1 constant be presented as sharp without proof.

## 7. Canonical integration

Only after the applicable stage survives its hostile passes, update all affected canonical files so they agree:

- `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md`;
- `Ideas/Paper 1 — Locally stationary Riemannian factor model.md`;
- `Ideas/Application map — geometry, symmetry, and rate accelerators.md`;
- `Ideas/OPEN OBLIGATIONS — current research actions.md`;
- `Ideas/Time-varying Fréchet mean Riemannian factor model.md`;
- HD1/G1 only where a new proved producer genuinely changes their assumptions or consumers.

Preserve the fixed-size BW theorem and existing negative results. Do not promote the archived incomplete sketch. Repair navigation and stale status language. Keep one canonical status table and one live queue.

Do not start application claims or numerical benchmarks in this campaign beyond recording exact consequences of the analytical verdict.

## 8. Final report

Report in plain language first, then give the mathematical ledger:

1. fixed-margin verdict and why it earned that status;
2. whether the shrinking-margin stage was forbidden, blocked, or started fresh;
3. exact theorem, corrected theorem, or counterexample;
4. the common constant or the precise obstruction;
5. all dimension, spectral-margin, path, energy, signal, and eigengap dependencies;
6. hostile objections and their resolutions;
7. consequences for G1, PF, lag/loading recovery, and factor selection;
8. files changed and archived;
9. exact remaining obligations;
10. mechanical verification of links, status consistency, and stale claims.

## 9. Final instruction

Drive Stage 1 until it reaches Gate A, B, or C under the rules above. Do not touch Stage 2 before that adjudication. If Gate A passes, discard the Stage 1 working context, convene a fresh team, and drive Stage 2 to its own honest verdict. If Gate B or C occurs, stop cleanly and do not leave the project lead with provisional shrinking-margin claims to repair.

The success criterion is not optimism. It is a repository whose strongest BW growing-size statement is correct, dependency-complete, adversarially checked, and honestly scoped.
