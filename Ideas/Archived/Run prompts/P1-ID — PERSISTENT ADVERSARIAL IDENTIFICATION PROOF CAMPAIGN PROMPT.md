# P1-ID — persistent adversarial identification proof campaign

You are the **lead mathematical researcher, identification theorist, adversarial proof auditor, and repository maintainer** for the Riemannian Factor Dynamics project.

You have filesystem access to the repository. Use one lead and the available subagents as a hostile proof team. Work directly in the repository. This is a **persistent proof-completion campaign**, not a planning exercise, literature survey, numerical study, or request for promising partial progress.

The scientific question is:

> Why analyse serially persistent fluctuations around a fixed Fréchet mean without first asking whether the mean itself moves? Under what observational and model assumptions are centre drift and persistent tangent factors separately identified, and what exactly remains identifiable when they are not?

The parent RFM assumes in (P2) that every marginal law has the same Fréchet mean. Do not describe its empirical Factor 1 as spurious. The defensible starting claim is that, under fixed-centre misspecification, drift and persistent factor contributions can enter the same lag object and the fitted output does not itself report their split.

Your objective is to **close P1-ID**. Closure may be:

1. a proved necessary-and-sufficient identification theorem;
2. a proved classification of the complete observational-equivalence class;
3. a proved impossibility/non-identification theorem plus the strongest useful identified quotient or convention;
4. a rigorous counterexample disproving the intended generic claim, followed by a sharper theorem on a mathematically justified maximal or clearly natural restricted class.

A narrower counterexample is acceptable only when you prove why its restriction marks a real mathematical boundary and not merely a convenient example. A negative theorem is success. An unsupported open question is not.

Do not return until every in-scope node created by this campaign has one of the terminal statuses defined below and the canonical repository has been updated accordingly.

At the first opportunity, use the environment's persistent-goal mechanism to create or continue the objective:

> Close P1-ID by proving the sharp centre-drift/factor identification or non-identification theorem, closing every generated dependency, surviving hostile cross-audit, and integrating the terminal result canonically.

Do not assign an artificial token budget. Do not mark that goal complete for a wave, a partial theorem, or an interim dossier. A context compaction, agent return, or failed route is a checkpoint, not a terminal event.

---

## 0. Non-negotiable completion contract

This run must not end with:

- “the remaining step is technical”;
- “a Jacobi-field argument should work”;
- “necessity remains open”;
- “future work should classify”;
- a conjecture standing where the headline theorem needs a result;
- a numerical example presented as proof;
- a web search or citation presented as proof;
- a theorem whose primitives are merely renamed versions of its conclusion;
- a counterexample that violates the assumptions it purports to attack;
- a restriction added only because the proof became difficult;
- a list of tasks for another team.

Every claim introduced into the live dependency graph must terminate as exactly one of:

- **PROVED INTERNALLY** — complete proof recorded with every load-bearing lemma closed;
- **CITED EXTERNALLY AND APPLIED** — exact primary theorem, hypotheses, and line-by-line application recorded; project-specific scope proved internally;
- **DISPROVED** — analytic counterexample satisfies the stated assumptions and violates the conclusion;
- **SHARPLY REFORMULATED AND PROVED** — the original statement is false or ill-posed, its failure is proved, and a corrected useful theorem is proved;
- **SUPERSEDED/BYPASSED** — a complete theorem makes the node unnecessary, and the no-consumer dependency argument is proved;
- **OUT OF SCOPE BY PROVED SEPARATION** — only if a formal dependency argument proves that the node belongs to estimation, application verification, or Paper 2 and is not needed for P1-ID.

`OPEN`, `CONDITIONAL`, `PLAUSIBLE`, and `EXPECTED` are not terminal statuses for any in-scope node. If the broadest desired theorem is undecidable from the adopted assumptions, prove that insufficiency by constructing two observationally equivalent admissible models or by proving the assumptions fail to determine the target. Then state and prove the identified set, quotient, or repaired theorem. Do not merely label the issue open.

### Persistence rule

Do not stop at the first broken proof. For every failed route:

1. isolate the exact failed implication;
2. attempt a genuinely different route;
3. test the statement with an exact analytic counterexample;
4. determine whether the problem is definition, information set, geometry, probability law, or regularity;
5. weaken the conclusion or strengthen assumptions only along a proved boundary;
6. prove the repaired result;
7. have a different workstream attack both the counterexample and the repair;
8. propagate the final status to all consumers.

If context, time, or a tool call ends, persist through the task/goal mechanism available in the environment and continue from the saved ledgers. Do not summarize and quit while an in-scope node lacks a terminal status. Do not mark the goal complete until the closure audit in §11 passes.

---

## 1. Read and preserve before proving

Read repository instructions and recursively inventory `Ideas/`. Read completely, at minimum:

1. `Ideas/P1-ID — centre-drift and factor identification boundary.md`;
2. `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md`;
3. `Ideas/Paper 1 — Locally stationary Riemannian factor model.md`;
4. `Ideas/Time-varying Fréchet mean Riemannian factor model.md`;
5. `Ideas/OPEN OBLIGATIONS — current research actions.md`;
6. `Ideas/HD1 — growing-dimension Paper 1 proof dossier.md`;
7. `Ideas/References and external claim audit.md`;
8. the archived historical identification material, especially the former Theorems A and B and the old P1-ID obligation;
9. the parent Huang–Chen–Chen paper, especially model equations (1)–(3), (P2), Remark 1, the lag estimator, and APP-FIN claims.

Use archived material as proof provenance, never as current status authority. Preserve all uncommitted user work. Inspect the worktree before editing; do not overwrite concurrent or unrelated changes. The current uncommitted P1-ID reframe is intentional and must be incorporated, not reverted.

Before proving anything, create:

- `Ideas/Working proof dossiers/P1-ID — lead definition and dependency ledger.md`;
- at most three workstream dossiers named `P1-ID-A`, `P1-ID-B`, and `P1-ID-C` under `Ideas/Working proof dossiers/`.

The lead ledger must list every claim, exact information set, model class, target, equivalence relation, norm/topology if any, producer, consumer, status, objection, and proof location. No theorem may use “same observed process” without specifying whether this means identical marginals, identical finite-dimensional distributions, identical full path law, contiguity/asymptotic equivalence, or recovery from one locally stationary triangular-array path.

---

## 2. First gate — determine whether the proposed problem is nontrivial

Do this before any long curved calculation.

Let \(Q_u\) denote a fully known marginal law. If \(Q_u\) has a unique Fréchet mean, then that mean is a functional of \(Q_u\). Therefore two representations of the **same marginal law** that both declare their centre to be its unique Fréchet mean must have the same centre. Prove this elementary proposition and use it as a scope gate.

Then adjudicate which genuinely nontrivial identification problem remains. Distinguish at least:

1. **Population marginal identification:** \(Q_u\) known for each \(u\). Decide what is immediate from unique Fréchet means and what factor-loading ambiguity remains.
2. **Full time-series-law identification:** all finite-dimensional distributions known. Determine whether factor/noise decompositions and zero-frequency components remain nonunique after the centre is fixed.
3. **Single-path/local-stationary recoverability:** only one triangular-array path is observed, so \(Q_u\) is inferred by local smoothing. Separate identifiability from consistency and rate.
4. **Fixed-centre misspecification:** the fitted model imposes one \(\mu\) although the true marginal centre is \(\mu(u)\). Characterise the exact population lag object and its drift/factor superposition.
5. **Weakened centring:** the model declares a reference curve not required to be the unique pointwise Fréchet mean. Characterise the resulting change-of-centre equivalence.

At Gate 1, write a formal adjudication:

- If “curved necessity” under identical known marginals and unique Fréchet means is trivial, say so and **do not manufacture a Jacobi-field theorem to solve a nonexistent ambiguity**.
- If the real theorem concerns single-path recoverability, fixed-centre misspecification, factor/noise decomposition, or weakened centring, restate P1-ID precisely and prove that this restatement captures the scientific question.
- If multiple distinct questions survive, order them and prove a theorem for each; do not collapse them into one ambiguous use of “identification.”

This gate must end with a theorem statement matrix, not prose alone.

---

## 3. Team structure and wave discipline

Use one lead plus three parallel workstreams when concurrency permits. Agents may spawn narrower helpers only if the lead ledger remains the common authority.

### Workstream A — definitions, flat classification, and spectral persistence

Own:

- exact observational-equivalence definitions for all five information regimes in §2;
- the unique-marginal-mean gate;
- the Euclidean/Hilbert change-of-centre classification;
- deterministic, zero-frequency, spectral-atom, and ordinary short-memory components;
- pointwise local-mean ergodicity and its exact relationship to spectral mass at frequency zero;
- factor rotation, loading-span ambiguity, factor/noise reallocations, and minimum-dynamic-rank conventions;
- exact examples with drift inside, outside, and partly inside the loading space.

The flat result must be necessary and sufficient on its stated class, or include a sharp counterexample and corrected classification. “The shift can be absorbed into a factor” is not enough: specify admissibility, centring, stationarity/local stationarity, whiteness, rank, and equality of laws.

### Workstream B — curved change of centre and local equivalence

Own:

- the exact map
  \[
  \Phi_{x\to y}(z)=\log_y(\operatorname{Exp}_x z),
  \]
  with domains, injectivity/cut-locus restrictions, and correct parallel-transport typing;
- exact common-geodesic/totally geodesic reductions;
- first and, only where consumed, higher variations through Jacobi fields or double-exponential identities;
- whether an affine factor-plus-white-noise structure survives nonlinear base-point change;
- local rigidity or non-rigidity of two admissible curved representations;
- analytic curved counterexamples where curvature creates interactions absent in the flat classification.

Do not infer global uniqueness from a local Taylor series. Do not use an \(O(\|v\|^2)\) remainder to establish equality of laws. If exact classification is impossible generically, prove impossibility and identify the strongest exact restricted geometry: for example one common geodesic/flat, a symmetric model with an exact group action, or a declared local infinitesimal identification theorem. Prove why the restriction is load-bearing.

### Workstream C — hostile counterexamples, information boundaries, and theorem audit

Independently attack A and B. Own:

- examples with identical marginals but different temporal laws and vice versa;
- nonunique Fréchet means, cut loci, mixtures, deterministic trends, zero-frequency atoms, near-zero-frequency factors, and rank changes;
- factor/noise reallocations compatible with or violating the exact white-noise conditions;
- drift aligned and orthogonal to factor loadings;
- fixed-centre lag contamination and factor-number consequences;
- observational equivalence versus merely asymptotic indistinguishability;
- whether proposed assumptions are checkable or simply encode the conclusion;
- maximality attacks on every restricted theorem.

C must try to destroy every headline claim with examples satisfying all displayed assumptions. It must also attack every counterexample for hidden assumption violations.

### Lead

The lead:

- fixes notation and the information-set hierarchy;
- proves missing bridge lemmas rather than waiting;
- prevents estimation rates from being confused with identification;
- assigns every claim to a consumer;
- forces A to audit B, B to audit C, and C to audit A in each wave;
- adjudicates disagreements with written proofs;
- maintains the canonical boundary and completion ledger;
- integrates only claims that survive two hostile passes.

---

## 4. Wave 1 — exact flat/Hilbert theorem

Prove the complete flat benchmark first. At minimum resolve:

1. Given a Euclidean or Hilbert process
   \[
   X_t=m(u_t)+Af_t+\delta_t,
   \]
   classify all alternative decompositions satisfying the same declared mean, persistence, white-noise, rank, and local-stationarity conditions.
2. Determine exactly when a change \(m\mapsto m+Ag\) can be absorbed into \(f\mapsto f-g\), and whether \(g\) must be deterministic, zero-frequency, locally deterministic, or merely non-ergodic.
3. Prove what pointwise local-mean ergodicity identifies and whether it is necessary under the adopted class.
4. Separate uniqueness of the centre, uniqueness of the loading span, uniqueness of factor scores, and uniqueness only up to an invertible/orthogonal factor transformation.
5. Treat drift components in \(\operatorname{ran}A\), in its orthogonal complement, and in both.
6. Derive the exact fixed-centre lag moment and prove when drift adds rank, changes only eigenvalues, or is invisible to the loading span.

Wave 1 cannot close with only a sufficient condition if a necessity claim is retained. Either prove necessity, disprove it, or state and prove the exact identified equivalence class.

Required hostile checks:

- constant random factors;
- deterministic smooth factors;
- processes with a spectral atom at zero;
- processes with continuous spectrum concentrated near zero but no atom;
- white and coloured idiosyncratic components;
- complementary rank-deficient lag matrices;
- a centre path aligned with one loading direction;
- a centre path outside the loading span.

Only after Wave 1 survives cross-audit may it enter the lead theorem.

---

## 5. Wave 2 — curved exactness gate

Use Wave 1 to decide which curved question actually needs geometry.

### 5.1 Exact law-functional result

Prove that unique pointwise Fréchet means fix the centre when identical marginal laws are assumed. Record all required existence/uniqueness/support conditions and the failure under nonunique means. This may dispose of part of the former “curved necessity” question.

### 5.2 Exact base-point-change result

For weakened centring or reference-curve models, analyse \(\Phi_{x\to y}\) exactly. Determine when it maps an admissible affine factor/noise law at \(x\) to another admissible affine factor/noise law at \(y\).

You must distinguish:

- one common geodesic;
- one common totally geodesic flat;
- constant-curvature spaces;
- general controlled normal neighbourhoods;
- global statements where cut loci or nonunique logs occur.

A local derivative calculation may prove infinitesimal identification but not an exact finite-displacement theorem. Label it accordingly and prove whether the infinitesimal result has an exact consumer. If not, either upgrade it or bypass it.

### 5.3 Rigidity versus impossibility

Attempt a local rigidity theorem under explicit nondegeneracy assumptions on the distributional support and factor/noise law. Candidate tools include:

- equality of Karcher score equations;
- differentiability and invertibility of the Karcher map;
- Jacobi fields for \(D\Phi_{x\to y}\);
- preservation or failure of affine subspaces under \(\Phi\);
- higher cumulants or conditional moments that distinguish a nonlinear transformed factor law;
- curvature-induced mixed terms.

If generic exact rigidity is false, construct an admissible curved pair with the same declared observation law and distinct decompositions. Then prove the identified equivalence class or a sharp restricted rigidity theorem. Do not stop at the example.

### 5.4 Boundary justification

Every restriction must come with one of:

- a counterexample immediately outside it;
- a theorem showing the proof invariant is equivalent to it;
- a maximality statement within a declared class;
- a geometric obstruction, such as loss of unique Log, loss of flat preservation, or a nonzero curvature term that cannot be represented in the allowed factor/noise class.

“We could only prove the flat case” is not a boundary justification.

---

## 6. Wave 3 — single-path recoverability is not population identification

Once the population targets are settled, state separately what one locally stationary path can recover.

Prove or sharply classify:

1. when local windows consistently recover \(Q_u\) or its Fréchet mean;
2. why deterministic/zero-frequency components obstruct local averaging;
3. whether absence of a zero-frequency atom is sufficient and necessary for the precise averaging target;
4. which triangular-array local-stationarity errors preserve the population split;
5. what happens for near-zero-frequency mass: identification may hold while finite-sample separation becomes arbitrarily ill-conditioned;
6. the distinction between an identified target and a uniformly estimable target.

Reuse existing G1/HD1 concentration only after proving its hypotheses match the newly identified target. Do not re-prove rate machinery unless P1-ID actually consumes it. If uniform recovery requires a quantitative spectral gap away from zero, state and prove it; if no uniform rate exists over the qualitative no-atom class, give a minimax/two-point or explicit slow-ergodic counterexample and state the pointwise result honestly.

This wave must not turn P1-ID into another bandwidth-optimisation project. Its purpose is to connect the population theorem to what a single dependent path can logically reveal.

---

## 7. Wave 4 — fixed-centre misspecification and the Factor 1 claim

Reconstruct and independently prove the fixed-centre contamination result in the exact notation ultimately used by P1-ID. Do not merely cite the historical theorem if its assumptions or target differ.

For every included lag \(h\), decompose the population and sample lag rows into:

- centre-drift contribution;
- factor contribution;
- drift–factor cross terms;
- idiosyncratic lag contamination;
- local-stationarity/end effects;
- sampling error.

Determine precisely when a lag-invariant drift term enters all lags, when the factor contribution saturates or varies with \(h\), and when rank/eigendirection conclusions follow. Retain the actual eigengap and factor-number conditions.

The final scientific language must distinguish:

- **proved:** the fixed-centre operator can superpose drift and persistent factor structure under the displayed misspecification;
- **identified under additional assumptions:** a stated decomposition or quotient;
- **empirical sensitivity only:** the leading factor changes under a moving-centre refit;
- **not claimed:** the parent's reported Factor 1 is spurious or drift-dominated.

If the historical formula \(S(h)=M_\mu+A\Gamma_f(h)A^*+\cdots\) omitted cross terms under assumptions no longer adopted, repair the theorem and propagate the correction. Do not preserve a rhetorically convenient but false additive decomposition.

---

## 8. Required theorem package

The final campaign must deliver the sharpest true version of the following package. Titles may change after Gate 1, but no conceptual slot may be silently dropped.

### ID-0 — information-set separation theorem

Classify what “identification” means under known marginals, full joint law, one locally stationary path, fixed-centre misspecification, and weakened centring. Prove implications and non-implications among them.

### ID-1 — unique marginal-centre theorem

Prove the exact result and failure boundary for unique Fréchet means as law-functionals.

### ID-2 — flat/Hilbert equivalence-class theorem

Give necessary and sufficient conditions or the exact identified quotient for centre, loading space, factors, and noise.

### ID-3 — spectral persistence theorem

Settle the role of zero-frequency atoms/local-mean ergodicity and the distinction between qualitative identification and uniform recoverability near frequency zero.

### ID-4 — curved base-point rigidity or non-identification theorem

Either prove exact curved rigidity on the broadest justified class, or prove its failure and the strongest corrected restricted theorem/equivalence class.

### ID-5 — fixed-centre contamination theorem

State the complete drift/factor/cross/noise lag decomposition and its loading/rank consequences.

### ID-6 — scientific interpretation corollary

State exactly what may be said about a leading fitted factor under (P2), what additional assumptions identify a split, and what remains only sensitivity analysis.

If any item is shown redundant or trivial, mark it **SUPERSEDED/BYPASSED** only after proving why and replacing its intended scientific content elsewhere. The package must contain no `OPEN` node at completion.

---

## 9. Counterexample standards

Every disproof must include:

1. the manifold and metric;
2. the complete stochastic construction;
3. existence and uniqueness or deliberate nonuniqueness of every Fréchet mean used;
4. support/normal-neighbourhood conditions;
5. factor rank, loading map, factor law, and noise law;
6. temporal dependence and spectral properties;
7. verification of every assumption in the attacked theorem;
8. equality of the claimed observational object;
9. explicit violation of the conclusion;
10. the mathematical feature responsible for failure.

After a counterexample, determine whether it is:

- universal;
- curvature-specific;
- topology/cut-locus-specific;
- caused by weak centring;
- caused by zero-frequency persistence;
- caused by insufficient temporal information;
- caused by factor/noise non-identification.

Then prove the strongest corrected theorem that removes exactly the responsible feature, or prove that no nontrivial correction exists on that class.

Use computation only to discover or sanity-check an example. Convert it into an exact analytic construction before assigning `DISPROVED`.

---

## 10. Cross-audit waves and escalation

At the end of each wave:

1. each workstream writes a claim table with assumptions, conclusion, proof location, and known weak point;
2. a different workstream performs a line-by-line hostile audit;
3. the lead records every objection in the dependency ledger;
4. the originating workstream repairs or concedes each objection;
5. the hostile auditor rechecks the repair;
6. the lead performs an independent final check.

No claim enters the canonical P1-ID file after only its author's review.

When stuck, escalate in this order:

1. simplify to the exact flat benchmark;
2. isolate a one-dimensional/common-geodesic curved model;
3. derive the exact obstruction;
4. construct a counterexample on constant curvature or a symmetric space;
5. prove a restricted theorem with the obstruction excluded;
6. test maximality or give a counterexample outside the restriction;
7. classify the identified quotient if uniqueness remains impossible.

Do not respond to difficulty by adding opaque assumptions such as “identifiability holds.” Any new assumption must be expressed in primitive geometric/probabilistic terms and must be shown to reach the consumer.

---

## 11. Canonical integration and closure audit

Only after the theorem package survives two hostile passes:

1. rewrite `Ideas/P1-ID — centre-drift and factor identification boundary.md` as the complete canonical theorem boundary, with primitive assumptions, derived producers, equivalence relation, conclusions, counterexamples, and proof links;
2. update `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md`;
3. update `Ideas/Paper 1 — Locally stationary Riemannian factor model.md`;
4. update `Ideas/Time-varying Fréchet mean Riemannian factor model.md`;
5. update `Ideas/OPEN OBLIGATIONS — current research actions.md` so P1-ID is removed from the live queue only if every in-scope node is terminal;
6. update `Ideas/Application map — geometry, symmetry, and rate accelerators.md` with the identification preconditions applications must justify;
7. update `Ideas/References and external claim audit.md` for every consumed external theorem;
8. update `Ideas/Numerical suite — theorem-driven design matrix.md` only to align N-18 with the theorem; simulations remain diagnostics, not proof;
9. archive all P1-ID workstream dossiers under `Ideas/Archived/Proof workstreams/` and leave no duplicate surface-level status source;
10. preserve the parent N-00 baseline and all existing HD1, HE, FRAME, BW, selector, and rate results unless a proved dependency contradiction requires an explicit correction.

Run a project-wide closure scan. Completion requires all of:

- every ID-0–ID-6 slot has a terminal status;
- every lemma introduced by their proofs has a terminal status or a proved no-consumer disposition;
- no canonical file still calls P1-ID open, optional, conditional, future work, or unresolved unless the final proved theorem itself establishes an irreducible identified set—in that case the **mathematical non-identification is proved**, not left open;
- all theorem statements use one consistent information-set vocabulary;
- marginal-law, joint-law, and single-path claims are never conflated;
- no claim labels Factor 1 spurious without a dataset-specific identified decomposition;
- all restrictions have proved boundary reasons;
- all external citations have exact theorem and scope records;
- all Markdown links resolve uniquely;
- LaTeX delimiters, control characters, patch artifacts, stale statuses, and duplicate live ledgers are clean;
- the worktree preserves unrelated pre-existing changes;
- the final dependency graph has no unadjudicated node.

If any check fails, continue the campaign. Do not issue the final report.

---

## 12. Final report format

Return only after closure. The final report must state, in plain language for a mathematically intuitive project lead:

1. **What the identification problem turned out to be.** Say if part of the original question was trivial, ill-posed, or aimed at the wrong information set.
2. **The final theorem.** State what is uniquely identified, under which assumptions, and up to which rotation/gauge/equivalence.
3. **The failure boundary.** Give the sharp counterexample or impossibility result and explain why the restriction is mathematically necessary.
4. **What this says about the parent's Factor 1.** Use only the proved non-separation or identified conclusions; do not infer dominance.
5. **What existing Paper 1 machinery now estimates.** Connect identification to HD1/HE/FRAME/BW without rewriting their rates.
6. **What changed canonically.** List files and proof dossiers.
7. **Closure evidence.** Report hostile passes, terminal-node counts, scans, and any exact external theorems consumed.

Do not end with suggested future analytical work on P1-ID. If a broader class remains outside the theorem, it must be outside because the campaign proved a boundary or impossibility, and the final theorem must already be complete on its declared class.

Begin now by reading the repository, creating the lead definition/dependency ledger, dispatching the three workstreams, and executing Gate 1. Do not begin from a presumed Jacobi-field solution; first prove what the actual identification problem is.
