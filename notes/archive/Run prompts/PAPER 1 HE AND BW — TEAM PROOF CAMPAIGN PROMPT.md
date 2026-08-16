> **ARCHIVED RUN PROMPT — CAMPAIGN COMPLETED 2026-08-08.** This prompt is proof-run provenance. It does not create live obligations or override the canonical analytical ledger.

# Paper 1 HE + BW — persistent team proof campaign

You are now the **maintainer, lead proof architect, and adversarial auditor** for the Riemannian Factor Dynamics research repository.

Your task is to run one persistent analytical campaign containing two independent proof programmes:

1. **HE:** a growing-total-energy/pervasive-factor extension of Paper 1;
2. **BW:** a full moving-centre Bures–Wasserstein extension, fixed matrix size first and growing matrix size second.

This is a proof-completion campaign, not a literature summary, brainstorming session, or numerical experiment. Continue through derivations, counterexamples, repairs, hostile review, and canonical integration until every in-scope claim has an honest final status.

## 0. Governing repository sources

Read the repository instructions and every canonical source completely before changing theorem status. The current canonical hierarchy is:

1. `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md` — programme-wide source of truth;
2. `Ideas/Paper 1 — Locally stationary Riemannian factor model.md` — concise Paper 1 theorem/specification;
3. `Ideas/HD1 — growing-dimension Paper 1 proof dossier.md` — complete robust bounded-energy proof;
4. `Ideas/G1 audit — resolution of the uniform local Fréchet rate.md` — mean-estimation proof source;
5. `Ideas/Application map — geometry, symmetry, and rate accelerators.md` — property/rate/application map;
6. `Ideas/OPEN OBLIGATIONS — current research actions.md` — only live queue;
7. `Ideas/Time-varying Fréchet mean Riemannian factor model.md` — scientific overview;
8. `Ideas/Paper 2 — Moving loading subbundle.md` — standalone Paper 2, out of scope except for preventing accidental claim transfer.

Then read only the archived proof records needed for the active obligations:

- `Ideas/Archived/Proof workstreams/APP-C — dependence, dimension, and hostile application audit.md` for the existing (R_n), product-moment, physical-dependence, normalisation, and signal-defect calculations;
- APP-A for AIRM/BW geometry warnings and the diagonal BW special case;
- APP-B for the four first-order nuisance terms and oracle cancellation package;
- HD1-A/B/C for the exact mean, lag-row, signal, and hostile counterexample proofs consumed by the new programmes;
- the historical ledger only when provenance for a named lemma is missing from the current canon.

Archived status labels never override the current canonical files.

## 1. Team structure

Use one lead and exactly three parallel subagents, subject to available concurrency:

### Agent HE — growing energy and pervasive signal

Own the complete HE derivation: assumptions, mean/frame rates, lag-row concentration, feasible comparison, operator assembly, signal phase diagram, examples, and counterexamples.

### Agent BW — Bures–Wasserstein geometry

Own the complete BW derivation: domain, metric, uniqueness, fixed-size differential calculus, estimator maps, feasible frame or replacement, lag identification, boundary attacks, and only then the growing-size constant audit.

### Agent X — hostile auditor and dependency checker

Maintain an independent error ledger. Attack HE and BW for hidden dimension factors, invalid norm transfers, unjustified conditioning, nonunique maps, wrong eigengap powers, incomplete-domain failures, and claims whose assumptions do not reach their consumers.

### Lead

The lead maintains the canonical dependency graph, performs independent derivations where the workstreams leave gaps, forces cross-audits, adjudicates conflicts, and integrates only claims that survive hostile review.

Agents may produce temporary work dossiers under `Ideas/Working proof dossiers/`. These are noncanonical. At completion, integrate accepted results into the canonical sources and move the temporary dossiers to `Ideas/Archived/Proof workstreams/`. Do not leave a second live theorem ledger on the surface.

## 2. Non-negotiable proof rules

1. **Web searches and citations do not prove repository claims.** External sources may supply a named theorem only when its complete hypotheses are checked against the exact consumer. Otherwise derive the result internally or mark the node open.
2. **Numerical evidence is not proof.** Do not run the future benchmark suite as a substitute for analytical closure. Computation may sanity-check algebra or locate counterexamples, but the final status must rest on proof or an analytic counterexample.
3. **Negative results count as completion.** If the proposed strong result is false, give the sharpest counterexample possible, identify the failed implication, and prove the strongest corrected theorem that survives.
4. **Do not hide growth in constants.** Every occurrence of (R_n), matrix size (m_n), tangent dimension (p_n), lag count, factor rank, dependence budget, spectral margin, (A_{2,n}), and (Delta_n) must remain visible unless a displayed assumption proves it uniformly bounded.
5. **Keep norms typed.** Distinguish tangent norm, Frobenius/Hilbert–Schmidt norm, matrix operator norm, lag-row direct-sum norm, and loading-subspace operator norm. Do not transfer a bound between them without proof.
6. **Keep target, sampling error, and geometry separate.** Lag contamination, mean estimation, frame error, and oracle lag sampling are different channels.
7. **No false cancellation.** Flatness, local symmetry, marginal sign symmetry, cross-fitting, a scalar expected Hessian, or root-(n) centre estimation alone do not remove all four first-order nuisance terms.
8. **Use the actual gap.** Davis–Kahan consumes (Delta_n^{-1}). Replace it by (s_n^{-2}) only after proving (Delta_nge s_n^2) under the exact included-lag factorisation.
9. **Do not modify Paper 2 mathematics.** Only update its scope/navigation wording if the Paper 1 reconstruction requires it.
10. **Preserve user work.** Inspect the current filesystem state before editing. Do not discard unrelated changes. Use focused patches and verify the resulting Markdown and links.

Allowed final statuses are:

- `PROVED`;
- `PROVED UNDER EXPLICIT ASSUMPTIONS`;
- `DISPROVED`;
- `RETRACTED`;
- `SUPERSEDED`;
- `OPEN — EXACT LEMMA STATED`.

Do not use “plausible”, “standard”, “expected”, or “should follow” as a load-bearing status.

## 3. Phase 0 — reconstruct the joint error ledger

Before attempting either headline theorem, create one shared ledger with rows for:

- mean bias;
- mean score fluctuation;
- local-stationarity approximation;
- generated-tube localisation;
- derivative or polygonal-frame input;
- Log/base-point recentering;
- endpoint connectors;
- non-rigid frame and ribbon holonomy;
- oracle lag-product concentration;
- feasible-versus-oracle lag comparison;
- included-lag population contamination;
- lag-operator assembly;
- Davis–Kahan;
- beyond-rank eigenvalues and factor selection.

For each row record:

- exact mathematical quantity;
- norm;
- producer lemma;
- consumer theorem;
- bounded-energy rate;
- proposed HE rate;
- proposed BW replacement;
- status;
- counterexample or failure if false.

The HE and BW teams must use this same ledger. Do not permit two incompatible notational systems.

## 4. Programme HE — growing total energy and pervasive factors

### HE objective

Replace the bounded-total-energy assumption by a controlled sequence

\[
R_n:=\sup_t\|Y_{t,n}\|\to\infty
\]

or by weaker typed moment/product assumptions where possible. Prove the sharpest loading and factor-number result available when factor signal may also grow with dimension.

The existing benchmark identities are only a starting point:

\[
\text{score fluctuation}\sim R_n(nb_n)^{-1/2},
\]

\[
\text{oracle lag fluctuation}\sim R_n^2n^{-1/2},
\]

\[
\text{feasible comparison}\lesssim 2R_nq_{R,n}+q_{R,n}^2,
\]

\[
\eta_n=2A_{2,n}d_n+d_n^2,
\qquad
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
\lesssim \eta_n/\Delta_n.
\]

Do not call these a theorem until every input and remainder has been rederived.

### HE-1 — minimal typed assumptions

Determine separately what is required for:

- score second moments and tails;
- empirical localisation and strong convexity;
- lag-product second moments and tails;
- causal Hilbert/HS physical-dependence inequalities;
- frame/holonomy bounds on a potentially growing tube;
- exact or approximate included-lag target factorisation.

Test whether an almost-sure (R_n) envelope can be weakened to trace, fourth/product moment, Orlicz, or truncation conditions without losing the desired rate. State every truncation bias.

### HE-2 — mean and frame theorem

Rederive the positive three-scale level, grid, and polygonal-frame results with explicit energy, dependence, tail, and geometry constants. Define the resulting feasible observation error (q_{R,n}).

The proof must decide whether deterministic bias constants also grow with (R_n) or tube radius; it may not scale only the stochastic term by inspection.

Give the bandwidth optimisation after all (R_n)-dependent terms are known. If no universal optimum exists, provide a regime table.

### HE-3 — oracle lag-row concentration

Prove a dimension-explicit Hilbert–Schmidt concentration theorem for

\[
Y_{t,n}\otimes Y_{t-h,n}-E(Y_{t,n}\otimes Y_{t-h,n})
\]

under the selected dependence assumptions. Retain variance-sensitive improvements over (R_n^2/sqrt n) when valid. Track lag aggregation and growing physical-dependence budgets.

### HE-4 — feasible row and loading theorem

Derive the full feasible lag-row error term by term. A schematic target is

\[
d_n\lesssim
\text{oracle sampling}
+2R_nq_{R,n}+q_{R,n}^2
+\text{frame}
+\text{dependence}
+\text{target contamination},
\]

but replace it by the exact proved expression.

Then prove operator assembly, the loading theorem, the beyond-rank square, and any valid threshold/ridged factor-number selector. State every condition relative to the actual (Delta_n).

### HE-5 — phase diagram

Derive explicit nonempty consistency regimes for:

1. bounded/localised factor signal with growing background energy;
2. pervasive factor signal strengthening with (p_n);
3. normalisation that preserves signal;
4. normalisation that dilutes signal;
5. matrix observations, carefully distinguishing (m_n) from (p_n=m_n(m_n+1)/2);
6. growing factor rank if any nontrivial regime survives.

For each regime state:

- allowed dimension/energy growth;
- required sample size and bandwidth;
- signal/eigengap behaviour;
- dependence and product-moment conditions;
- loading rate;
- factor-number window;
- application interpretation.

### HE-6 — hostile attacks

Construct analytic counterexamples for every shortcut that fails, including at least:

- coordinatewise control without total/product control;
- growing energy with fixed gap;
- global normalisation of a localised factor;
- pervasive signal plus coloured idiosyncratic lag contamination;
- hidden dimension cost in coordinatewise physical dependence;
- growing rank with insufficient total lag energy.

### HE acceptable verdicts

The programme must end in one of these forms:

- a broad growing-energy theorem with a pervasive-factor corollary;
- a conditional theorem with a sharp nonempty phase region;
- an impossibility boundary plus the strongest corrected estimator/theorem;
- `OPEN — EXACT LEMMA STATED` only after the team has attempted proof, counterexample, truncation, normalisation, and alternative estimator routes and can identify one irreducible missing lemma.

## 5. Programme BW — moving-centre Bures–Wasserstein geometry

### BW objective

Build a complete fixed-matrix-size Paper 1 theorem under the same Bures–Wasserstein estimand used by the parent covariance application. Only after fixed-size closure may the team audit growing matrix size.

Do not import AIRM results by analogy. Diagonal fixed-basis BW in square-root coordinates is a valid special case, not evidence for full noncommuting BW.

### BW-1 — domain and definitions

Choose and state the precise domain:

- strictly positive-definite matrices;
- a fixed-rank PSD stratum;
- or a quotient/horizontal-lift representation.

Define the BW metric, tangent norm, Exp, Log, geodesic, optimal alignment, connection/transport or its replacement, and Fréchet objective. State quantitative margins from:

- eigenvalues reaching zero;
- rank changes;
- nonunique optimal alignments;
- nonunique logarithms or means;
- singular quotient coordinates.

### BW-2 — generated-set closure

Prove that every object generated by the Paper 1 estimator stays in a common controlled domain with probability tending to one:

- population centre path;
- local empirical means;
- one-sided scale means;
- Richardson/blend images;
- connectors and chords;
- frame/transport comparison objects;
- reconstructed observations.

A raw-data spectral bound is not automatically a generated-set bound.

### BW-3 — fixed-size differential calculus

For fixed matrix size, prove every differential consumed by G1 and the feasible-frame theorem:

- squared-distance score and observation Hessian;
- Exp and Log base-point and vector derivatives;
- alignment/horizontal-lift derivatives;
- connector/comparison maps;
- Richardson and blend derivatives;
- ruled-surface, frame, or holonomy comparison.

If BW lacks the exact transport structure used by HD1, determine whether:

1. an equivalent horizontal-lift comparison proves the same estimator bound;
2. a different canonical frame avoids the missing map;
3. the current estimator must be replaced.

Prove the chosen route rather than declaring it natural.

### BW-4 — fixed-size statistical theorem

Using the fixed-size geometry, close:

- mean existence/localisation and rate;
- feasible tangent observations;
- oracle and feasible lag rows;
- included-lag factorisation;
- loading-space perturbation;
- factor-number selection.

Explicitly distinguish the covariance matrix as the scientific observation from any preliminary covariance estimator built from raw returns or signals. The latter creates an additional measurement-error/dependence layer and is not part of the geometric theorem unless modelled.

### BW-5 — hostile boundary attacks

Give analytic examples or precise arguments showing what fails under:

- eigenvalue collapse;
- rank change;
- repeated or crossing spectral/alignment structures;
- nonunique means;
- generated estimator images leaving the controlled set;
- moving eigenvectors versus a fixed diagonal algebra.

Use these attacks to determine whether the theorem is global, local, stratified, regularised, or flat-submodel only.

### BW-6 — growing-size audit

Only after BW-1 through BW-4 are closed, expose every fixed-size constant as a function of:

- matrix size (m_n);
- tangent dimension;
- lower and upper eigenvalue bounds;
- spectral multiplicity/alignment margins;
- rank;
- generated-set radius.

The possible outcomes are:

- matrix-size-uniform calculus;
- a polynomial dimension cost and an explicit (m_n)-versus-(n) regime;
- a spectral-margin rather than dimension cost;
- unavoidable blow-up requiring a redesigned estimator or fixed-size-only theorem.

### BW-7 — intersection with HE

Do not merge BW and HE prematurely. After both independent ledgers are closed, state exactly what additional assumptions would be required for a growing-energy, growing-matrix BW corollary. If the intersection is empty under current rates, prove that fact or display the conflicting inequalities.

### BW acceptable verdicts

The programme must end in one of these forms:

- complete fixed-size and dimension-uniform growing-size BW theorem;
- complete fixed-size theorem plus a restricted growing-size window;
- a local/regularised/stratified theorem with explicit boundary margins;
- a proved flat diagonal/fixed-basis theorem plus a counterexample to the proposed full route;
- `OPEN — EXACT LEMMA STATED` only after alternative alignment, lift, frame, and estimator constructions have been seriously attempted.

## 6. Required hostile cross-audit

Do not integrate provisional results immediately.

After HE and BW write their first complete dossiers:

1. Agent X audits both dossiers from first definitions to final consumers.
2. Agent HE attacks BW’s statistical concentration, signal, energy, and norm bookkeeping.
3. Agent BW attacks HE’s geometry, tube, Hessian, frame, and matrix-scaling assumptions.
4. The lead independently checks every headline display and constructs at least one zero-signal, zero-noise, fixed-dimension, and high-dimension edge case.
5. Each originating agent must repair or explicitly reject every objection.
6. Agent X performs a second pass on the repaired dossiers.

Maintain an objection table with columns:

| Claim | Attack | Resolution | Final status | Canonical consequence |
|---|---|---|---|---|

No claim enters the canon merely because all agents agree informally.

## 7. Application matching after proof closure

Only after the HE and BW verdicts are fixed, update the application map for:

- realised covariance and correlation dynamics in finance;
- functional-connectivity matrices and diffusion data;
- expanding sensor arrays;
- gene-expression panels;
- functional/Hilbert data;
- fixed-axis diagonal covariance/volatility models.

Each application must receive one of:

- `EXACT MATCH`;
- `CONDITIONAL MATCH — CHECKS LISTED`;
- `APPROXIMATE MATCH — DEFECT PENALTY DISPLAYED`;
- `REJECTED MATCH — ESTIMAND OR ASSUMPTIONS NOT DEFENSIBLE`.

For covariance data, distinguish:

1. raw multivariate observations;
2. an estimated covariance matrix time series;
3. the RFM/BW model on those matrices;
4. the separate factor forecasting model.

Do not claim that covariance aggregation is lossless. It is justified only when covariance dynamics are the target. Do not claim universal forecasting superiority; record the direct matrix and alternative-geometry baselines required by the later numerical suite.

## 8. Canonical integration

After the second hostile pass, update all affected canonical files so that theorem scope, notation, dependencies, application verdicts, and live obligations agree.

At minimum update:

- `Analytical reconstruction — proof ledger and rebuilt spec.md`;
- `Paper 1 — Locally stationary Riemannian factor model.md`;
- `Application map — geometry, symmetry, and rate accelerators.md`;
- `OPEN OBLIGATIONS — current research actions.md`;
- `Time-varying Fréchet mean Riemannian factor model.md`;
- HD1 and G1 only where a new proved theorem genuinely changes their assumptions or consumers.

Rules:

- retain one canonical status table and one live queue;
- archive temporary dossiers after integration;
- preserve counterexamples and rejected routes;
- mark historical files clearly as archived;
- repair wiki links and navigation;
- do not duplicate the same theorem in incompatible notation;
- do not leave provisional language in a canonical headline.

## 9. Numerical-suite boundary

Do not implement the complete numerical suite in this campaign. Produce only its theorem-driven design matrix after the analytical verdicts are known:

- regimes to simulate;
- parameters to vary;
- predicted rates and failure boundaries;
- reconstruction and genuine forecasting targets;
- factor-number diagnostics;
- direct covariance, linear-factor, AIRM, BW, and log-Euclidean baselines as scientifically appropriate;
- reproducibility requirements, seeds, and output structure.

Label every numerical item `PLANNED`, not `PROVED`.

## 10. Persistence and stopping rule

Do not stop after a first failed proof attempt, a literature search, or a provisional lemma. For each obstruction:

1. isolate the exact failed implication;
2. attempt a direct proof under the current assumptions;
3. attempt a counterexample;
4. test the weakest natural repair;
5. determine whether an estimator modification removes the obstruction;
6. propagate the result through every downstream rate and application claim.

The campaign is complete only when:

- HE has a proved theorem, proved boundary/counterexample, or one exact irreducible open lemma after all prescribed alternatives;
- BW has a complete fixed-size verdict and a completed growing-size audit or exact obstruction;
- both have survived two hostile passes;
- the intersection of HE and BW is classified rather than assumed;
- applications are remapped to the surviving packages;
- canonical files agree;
- temporary work is archived;
- the remaining queue contains only genuinely unresolved, precisely stated obligations.

## 11. Final report format

Report to the project lead in plain language first, then give the mathematical ledger.

The final report must contain:

1. **Bottom line:** what was proved, disproved, narrowed, or left exactly open.
2. **HE verdict:** theorem, rate, phase regions, and counterexamples.
3. **BW verdict:** fixed-size theorem, growing-size audit, and boundary failures.
4. **Intersection verdict:** whether growing-energy BW is currently nonempty and under what inequalities.
5. **Application consequences:** which major application families were reopened, narrowed, or rejected.
6. **Estimator consequences:** whether the original Paper 1 construction survived or changed.
7. **Dependency chart:** proved nodes only in solid arrows; open nodes in dashed arrows.
8. **Files changed and archived.**
9. **Exact remaining obligations**, if any, with no vague “future work”.
10. **Numerical-suite design**, clearly separated from analytical proof.

The standard is not that the desired optimistic theorem must be true. The standard is that after this campaign the repository states the strongest correct result, contains the proof or counterexample supporting it, and leaves no hidden dependency or false application promise for the project lead to clean up.
