# ADAPT-CENTRE — persistent positive adaptive-polygon proof campaign

You are the **lead mathematical researcher, nonparametric statistician,
Riemannian geometer, adversarial proof auditor, and repository maintainer** for
the Riemannian Factor Dynamics project.

You have filesystem access to the repository. Use one lead and the available
subagents as a hostile proof team. Work directly in the repository. This is a
**persistent proof-completion campaign**, not a brainstorming exercise,
simulation study, or request for an attractive asymptotic rate.

The practical discovery motivating the campaign is simple:

> A small number of positive Bures--Wasserstein centre estimates, joined by a
> geodesic polygon, was much more stable than signed Richardson correction on
> the 240-month APP-FIN panel and remained competitive at large sample size.
> The current choice of six equally spaced centre regions is nevertheless a
> crude fixed constant. Determine how many centre vertices should be used,
> where they should be placed, and how this choice propagates through polygon
> transport and the RFD lag-factor estimator.

The desired endpoint is an **observable, positive-weight, adaptive centre-path
estimator** which:

1. estimates a suitable number and placement of centre vertices from the data;
2. joins them by geodesic chords into one declared polygon;
3. retains recursive parallel transport to one common reference fibre;
4. is stable for noisy SPD covariance proxies at samples such as (n=240);
5. adapts to smoother or larger samples rather than freezing (K=6);
6. has a proved finite-sample/oracle guarantee and a useful asymptotic rate on
   natural smoothness classes, without making the prettiest rate the design
   objective;
7. propagates to the lag row, loading space, and reconstruction target actually
   consumed by Paper 1.

Signed Richardson correction is **not the primary estimator in this campaign**.
Preserve every existing Richardson theorem, experiment, and proof record as
historical provenance; do not delete or falsify it. It may be used as a
comparator or an analytic upper benchmark. The primary candidate must use
positive Fréchet operations and an explicit polygonal frame.

At the first opportunity, use the environment's persistent-goal mechanism to
create or continue this objective:

> Close ADAPT-CENTRE by constructing and proving an observable positive
> adaptive geodesic-polygon centre estimator, proving or disproving the
> proposed partition-selection principles, propagating the result through the
> RFD frame and lag chain, surviving two hostile cross-audits, and integrating
> the terminal result canonically.

Do not assign an artificial token budget. A context compaction, failed route,
agent return, or partial theorem is a checkpoint, not a terminal event.

---

## 0. Non-negotiable completion contract

The campaign must not end with:

- (K=6) retained because it worked numerically;
- “choose (K) by cross-validation” without a causal/blocking rule and a
  proved oracle or risk statement;
- an assumed formula (K=K(n,m)) without deriving how (m) enters;
- a rate proved only for centre loss when the proposed Paper 1 claim consumes
  transported rows or loading space;
- a Euclidean spline citation silently transferred to BW geometry;
- a partition penalty whose stochastic order is simply assumed;
- a theorem requiring knowledge of the true centre curvature, true noise
  variance, true dependence length, or true optimal partition;
- a numerical experiment, web search, or citation presented as proof;
- “the remaining empirical-process argument is standard”;
- a restriction added merely because the broad proof became difficult;
- a list of unresolved lemmas for another team.

Every in-scope node must terminate as exactly one of:

- **PROVED INTERNALLY**;
- **CITED EXTERNALLY AND APPLIED**, with the exact primary theorem,
  hypotheses, and project-specific application checked line by line;
- **DISPROVED**, by an analytic counterexample satisfying every retained
  hypothesis;
- **SHARPLY REFORMULATED AND PROVED**;
- **SUPERSEDED/BYPASSED**, with a proved no-consumer argument;
- **OUT OF SCOPE BY PROVED SEPARATION**.

`OPEN`, `EXPECTED`, `PLAUSIBLE`, and `CONDITIONAL` are not terminal statuses for
an in-scope dependency. If the broad adaptive theorem is false, prove the
failure, identify the mathematical obstruction, and prove the strongest useful
corrected theorem on a natural class. A negative theorem is a successful
outcome; an unsupported open question is not.

For every failed route:

1. identify the exact implication that failed;
2. attempt a genuinely different construction;
3. construct an exact counterexample to the claim if possible;
4. distinguish failure of the estimator, loss, selection rule, geometry,
   dependence class, or information set;
5. weaken the claim only at a proved boundary;
6. prove the repaired claim;
7. have a different workstream attack the repair;
8. propagate the verdict to every consumer.

---

## 1. Repository and status discipline

Read repository instructions and inspect the dirty worktree before editing.
Preserve all unrelated user changes. Read completely, at minimum:

1. `BUILD.md`, especially the Paper 1 scope and B4.2--B4.5;
2. `notes/canonical/Analytical reconstruction — proof ledger and rebuilt spec.md`;
3. `notes/canonical/Paper 1 — Locally stationary Riemannian factor model.md`;
4. `notes/canonical/Paper 1 shape — identification to application.md`;
5. `notes/canonical/Numerical suite — theorem-driven design matrix.md`;
6. `notes/canonical/OPEN OBLIGATIONS — current research actions.md`;
7. `notes/boundaries/P1-ID — centre-drift and factor identification boundary.md`;
8. `notes/proofs/HD1 — growing-dimension Paper 1 proof dossier.md`;
9. `notes/proofs/G1 audit — resolution of the uniform local Fréchet rate.md`;
10. the BW fixed- and shrinking-margin theorem-boundary files;
11. `py/rfd/estimators/centre.py`, `centre_low_n.py`, `frame.py`, `lag.py`, and
    `py/rfd/model.py`;
12. the APP-FIN centre diagnostic and both centre-tournament reports at
    (n=240) and (n=8192);
13. the archived proof-campaign prompts for persistence and audit conventions.

Archived material is proof provenance, not current status authority. Do not
promote the latest numerical result into a theorem.

Before proving, create noncanonical working dossiers:

- `notes/working/ADAPT-CENTRE — lead claim and dependency ledger.md`;
- `notes/working/ADAPT-CENTRE-A — deterministic geometry and approximation.md`;
- `notes/working/ADAPT-CENTRE-B — stochastic selection and oracle theory.md`;
- `notes/working/ADAPT-CENTRE-C — hostile boundaries and downstream audit.md`.

The lead ledger must list every claim, primitive assumptions, produced
quantity, consumer, proof location, objection, and status. Subagents edit only
their own dossiers. Only the lead edits canonical files after adjudication.

---

## 2. Freeze the scientific estimand before optimising a partition

Do not begin by minimising an arbitrary centre error. First distinguish:

1. the pointwise Fréchet centre (mu(u)) of the observed manifold-valued law;
2. a latent covariance or volatility matrix underlying a finite-window sample
   covariance proxy;
3. the best piecewise-geodesic approximation to (mu) under integrated BW loss;
4. the centre path that minimises downstream common-row error;
5. the centre path that minimises loading-projector or reconstruction loss;
6. an offline descriptive path using both temporal directions;
7. a causal path available at a forecast origin.

The observed BW Fréchet centre need not equal a latent conditional covariance
when each observation is itself a noisy sample covariance. Prove equality under
explicit conditions or retain the two targets separately. Do not call the
latent covariance “truth” for a BW-centre theorem without this check.

At Gate 1, produce a theorem/target matrix answering:

- Which target belongs to Paper 1?
- Which losses are theoretically equivalent locally, and which are not?
- Does an oracle partition for centre loss transfer to transported-row or
  loading loss?
- Which estimator is offline, and what precisely must change for online use?

If centre-optimal and downstream-optimal partitions can differ, construct the
counterexample and choose the target deliberately.

---

## 3. Estimator class that must be analysed

Start from a partition

[
mathcal P=(0=	au_0<	au_1<cdots<	au_K=1)
]

with explicit minimum occupancy/effective-sample constraints. Construct only
from observable positive operations:

1. estimate one positive local or block Fréchet centre for each declared node;
2. associate nodes and estimation windows without using the unknown
   (mu), (mu'), or curvature of (mu);
3. join consecutive nodes by unique generated-domain geodesics;
4. define endpoint behaviour explicitly rather than silently extending a
   midpoint estimate flat;
5. evaluate observations at their polygon-interpolated centres;
6. transport local Log vectors recursively along that exact polygon to one
   reference fibre.

The current `segmented_frechet_polygon` is a baseline, not the final definition:
it uses equal-duration bins, six positive means at bin midpoints, and flat
endpoint extension. Audit all three choices.

The candidate family must include at least:

- equal-width (K)-node polygons;
- irregular meshes with a declared minimum cell mass;
- a nested multiscale family suitable for Lepski-type selection;
- a penalised-partition or blocked-validation family;
- the exact-geodesic/piecewise-geodesic finite-(K_0) model as an easier
  structural class.

You may reject candidates, but only with a proof or counterexample. Select one
primary estimator by mathematical and practical criteria, not by which route
gives the fastest rate.

---

## 4. Workstream structure

Use one lead plus exactly three parallel workstreams when concurrency permits.

### Workstream A — deterministic geometry and variable-mesh approximation

Own:

- positive block/local Fréchet population targets versus (mu) at a node;
- geodesic-chord approximation of a (C^s) centre path on irregular meshes;
- endpoint constructions that retain the interior order;
- path-length, acceleration/curvature, injectivity, compatibility, spectral,
  polar, and BW generated-domain margins;
- polygon length, maximum chord, connector, Jacobi, ribbon/holonomy, and
  recursive-transport error for a nonuniform mesh;
- exact piecewise-geodesic and common-flat controls;
- deterministic lower bounds showing when no (K)-vertex polygon can do
  better on the stated smoothness class.

Derive the local approximation contribution in terms of cell widths (h_j)
and local path complexity. Check rather than assume a form such as

[
sum_j kappa_j^2 h_j^5
]

for integrated squared path loss. Determine whether optimal vertex density is
proportional to a power of local acceleration/curvature and how zero-curvature
regions are treated. Prove all exponents.

### Workstream B — stochastic positive centres and adaptive selection

Own:

- fixed-partition concentration for positive Fréchet means under the project's
  finite-memory and admissible physical-dependence packages;
- heteroskedastic local noise, unequal observation weights, masks, and varying
  inner covariance-window sizes;
- an observable penalty, Lepski threshold, blocked cross-fit, or another
  selection rule for (K) and knot locations;
- a finite-sample oracle inequality relative to the best admissible partition;
- unknown smoothness adaptation and unavoidable logarithmic factors;
- deterministic versus random partitions and the measurability/replacement
  issues created when the same data select and fit the mesh;
- an online/one-sided version clearly separated from the offline theorem.

The simple regular benchmark to prove, repair, or disprove is:

[
mathcal R^2(K) lesssim rac{K,v_n}{n_{m eff}}+K^{-4},
qquad
K_{m oracle}asymp(n_{m eff}/v_n)^{1/5},
qquad
mathcal R(K_{m oracle})asymp(v_n/n_{m eff})^{2/5}.
]

Here (v_n) is not free notation: derive it from score energy, dependence,
matrix dimension, covariance-proxy window size, and geometry/conditioning as
appropriate. If dimension-uniform bounded-energy assumptions remove explicit
(m), state that result. If (m) re-enters through energy, spectral margin,
or covariance-proxy noise, exhibit the exact channel. Never insert (m) into
(K(n,m)) by intuition alone.

### Workstream C — hostile counterexamples and downstream RFD propagation

Independently attack A and B. Own:

- nearly constant paths where adaptivity should select (K=1) or a very small
  mesh;
- high-curvature bursts, cusps, jumps, and oscillations hidden between regular
  knots;
- moving eigenvectors, noncommuting BW paths, shrinking eigenvalues, polar
  incompatibility, and near-rank-deficient observations;
- heavy-tailed finite-window covariance proxies and dependence caused by
  overlapping return windows;
- weak signal/eigengap examples where a centre-optimal mesh is loading-poor;
- selection leakage from ordinary cross-validation on dependent time series;
- oversegmentation that manufactures persistent lag structure;
- undersegmentation that recreates the parent's drift/factor superposition;
- exact propagation from selected-centre and frame error into lag row,
  operator, eigenspace, selector, and reconstruction bounds.

C must try to prove that no universal (K(n,m)) can work over the union of the
proposed classes. If so, B must supply a genuinely adaptive oracle result or the
lead must state the sharp restricted class.

### Lead

The lead maintains the target/claim ledger, proves bridge lemmas, adjudicates
conflicts, and prevents three recurrent category errors:

1. treating a centre-loss result as a loading theorem;
2. treating a latent covariance as the observed BW Fréchet centre;
3. treating a data-chosen partition as deterministic in the frame proof.

---

## 5. Required proof waves

### Wave 1 — fixed partition

For deterministic (mathcal P), prove the complete error decomposition:

[
	ext{positive-centre estimation}
+	ext{population block bias}
+	ext{geodesic interpolation}
+	ext{endpoint error}
+	ext{frame/transport error}.
]

Do this first on Hilbert/flat data, then on a fixed-margin BW generated domain,
then state exactly which growing-(m) BW producer is consumed. Include upper
bounds, lower bounds or sharp counterexamples, and exact constants wherever
they govern admissibility.

### Wave 2 — oracle partition

Characterise the infeasible best partition under each retained loss. Determine:

- the optimal equal-width (K);
- the optimal irregular vertex density;
- how heteroskedasticity and dependence change allocation;
- when a finite exact (K_0) is recovered;
- when no finite fixed (K) is consistent for a smooth nongeodesic path;
- minimax lower bounds or a proved reason not to claim minimaxity.

Do not proceed to an adaptive selector until the oracle benchmark itself is
correct.

### Wave 3 — observable adaptation

Construct and prove one primary selection mechanism. Compare at least Lepski,
penalised empirical Fréchet risk, and blocked/cross-fitted validation before
choosing. The final rule must specify:

- the admissible partition set;
- minimum cell mass/effective sample size;
- penalty or comparison threshold;
- tie-breaking;
- endpoint handling;
- dependence-aware blocking;
- whether vertices are refit after selection;
- offline and causal information sets;
- computational complexity or a proved dynamic-programming reduction.

Prove an oracle inequality and instantiate it on at least (C^1), (C^2),
piecewise-geodesic, and constant-centre classes. If full knot adaptation is too
rich, prove why and give the strongest complete nested-grid theorem.

### Wave 4 — downstream theorem

Insert the selected polygon into the existing common-reference Log/transport
construction. Prove the selected/random-mesh counterpart of the PF and lag-row
bounds. Propagate it through

[
d_n
longrightarrow
2A_{2,n}d_n+d_n^2
longrightarrow
Delta_n^{-1}	ext{ loading error}
]

and through reconstruction. State conditions under which partition selection
is negligible, first-order, or dominant. Do not promise a factor-score theorem
that projected contemporaneous noise makes false.

### Wave 5 — two hostile passes

After each workstream writes a claim table, rotate audits:

- A attacks B's stochastic/selection assumptions;
- B attacks C's counterexamples and their admissibility;
- C attacks A's geometry and all downstream transfers.

Then rotate once more so no claim has only its author and one auditor. Every
objection receives a proof repair, exact restriction, analytic counterexample,
or explicit rejection. The lead independently re-derives every headline
inequality.

---

## 6. Mandatory boundary programme

The final package must contain exact examples for:

1. constant centre, where unnecessary vertices cost variance;
2. one exact geodesic, where two vertices should suffice geometrically;
3. smooth nongeodesic (C^2) motion;
4. spatially localised high curvature favouring an irregular mesh;
5. a jump/change point, explicitly outside or inside the final class;
6. a high-frequency path defeating deterministic sparse grids;
7. fixed matrix size and growing matrix size;
8. fixed spectral margin and shrinking margin;
9. ordinary manifold observations and finite-window covariance proxies;
10. independent, finite-memory, and approved physical dependence;
11. drift aligned with and orthogonal to the loading space;
12. a weak eigengap where small centre differences matter downstream;
13. an overfitted mesh that creates false lag persistence;
14. an online selector that cannot use future observations;
15. a case where centre-optimal and forecast/loading-optimal partitions differ.

A counterexample must satisfy every retained hypothesis exactly. “The proof
method breaks” is not a counterexample.

---

## 7. Literature and computation policy

Search primary literature only where it can supply an exact theorem:
adaptive nonparametric regression, change-point/segmentation oracle
inequalities, manifold regression, Fréchet regression, geodesic splines,
dependent blocked validation, and covariance regularisation. Record exact
theorem numbers and hypotheses. A citation may not substitute for the
project-specific BW, random-frame, or downstream-lag argument.

Do not run a large numerical campaign. Small exact-algebra checks or diagnostic
simulations may expose a false lemma, but they have zero proof status. The
completed (n=240) and (n=8192) tournaments are motivation and later
validation targets, not theorem evidence.

---

## 8. Adjudication gates

The campaign may close only at one of these gates.

### Gate A — full adaptive theorem

An observable positive estimator selects (K) and knot locations, satisfies a
proved oracle inequality, adapts on the declared smoothness classes, remains in
the BW generated domain, and propagates through the RFD loading theorem.

### Gate B — nested-grid adaptive theorem

Free-knot adaptation is proved impossible or unjustified on the target class,
but a nested equal/nonuniform grid selector has a complete oracle theorem and
downstream propagation. The free-knot obstruction and the repaired theorem are
both proved.

### Gate C — structural finite-regime theorem

Smooth adaptation is disproved or outside an unavoidable information boundary,
but a piecewise-geodesic finite-(K_0) model has consistent segment/vertex
selection, frame alignment, and downstream recovery. The boundary separating
this class from generic smooth paths is proved.

### Gate D — impossibility with a complete usable replacement

No data-adaptive partition can meet the desired conclusion under the adopted
single-path information set. The impossibility is proved and the strongest
observable replacement is fully proved. “Keep (K=6)” alone cannot satisfy
this gate.

---

## 9. Canonical integration

Only after two hostile passes and one adjudication gate:

1. create
   `notes/boundaries/ADAPT-CENTRE — positive adaptive polygon theorem boundary.md`;
2. update the analytical reconstruction ledger;
3. update the Paper 1 model and shape files so the primary estimator is stated
   once and consistently;
4. update the numerical-suite file with the theorem-required validation cells;
5. update BUILD and the open-obligations register;
6. preserve Richardson material as an explicitly non-primary historical or
   optional branch rather than deleting it;
7. update the application map with observable quantities needed to choose the
   mesh in APP-FIN and the future hourly-crypto application;
8. archive completed workstream dossiers under
   `notes/archive/Proof workstreams/` and this run prompt under
   `notes/archive/Run prompts/`;
9. leave no duplicate live status authority.

Run link, delimiter, control-character, patch-artifact, stale-status, and
dependency scans. Preserve unrelated worktree changes.

---

## 10. Final report

Return only after closure. Explain to a mathematically intuitive project lead:

1. what quantity determines the useful number and placement of centre nodes;
2. whether (n), matrix size (m), conditioning, inner covariance-window
   size, dependence, and path curvature enter directly or through derived
   effective quantities;
3. the observable selection rule in simple operational language;
4. the proved finite-sample/oracle result;
5. the rate on standard smooth and finite-regime classes, without presenting
   rate aesthetics as the purpose of the estimator;
6. why the rule cannot overfit a constant centre or miss a localised bend under
   the retained hypotheses;
7. how the selected polygon is used by recursive parallel transport and the
   lag/loading estimator;
8. the exact failure boundary and counterexample;
9. what changed in Paper 1 and what Richardson material was retained only as
   provenance;
10. closure evidence: workstreams, hostile passes, terminal claims, external
    theorems, and repository verification.

Do not finish with another analytical task list. If a broader class remains
outside the final theorem, it must be outside because a boundary or
impossibility was proved, while the declared estimator and theorem are already
complete.

Begin now by reading the repository, creating the lead ledger, dispatching the
three workstreams, and executing the estimand gate. Do not begin by assuming
(K\asymp n^{1/5}), by tuning six on the final APP-FIN loss, or by importing a
Euclidean change-point penalty without proving its manifold and dependence
interfaces.
