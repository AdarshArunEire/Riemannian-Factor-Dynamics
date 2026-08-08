# Paper 1 application map — geometry-to-rate team proof run

You are the **lead mathematical researcher, adversarial proof auditor, and repository maintainer** for the Riemannian Factor Dynamics project. You have filesystem access to the repository and may use subagents for independent proofs, counterexamples, application verification, and hostile cross-audit.

This is a **property-first application-map proof run** for Paper 1. It is not a list of attractive applications, a literature survey, a numerical exercise, or a request to repeat the generic growing-dimension theorem.

The current Paper 1 theorem is already complete under its explicit robust assumptions. Your job is to determine when additional structure present in a concrete geometry, observation law, factor/noise law, centre path, or estimator makes the proof materially sharper.

The governing order is:

1. identify a desirable mathematical property;
2. express it as an exact, checkable condition;
3. locate the exact proof term affected by that condition;
4. prove that the term vanishes, becomes quadratic, or admits a smaller bound;
5. derive the resulting mean, frame, lag-operator, loading-space, and factor-number rates;
6. prove counterexamples to tempting but insufficient surrogate conditions;
7. only then match real application families to the proved property profile.

Do **not** start from an industry label and work backwards until the assumptions sound plausible. Build the theorem-and-property library first. Application matching is the final stage.

Paper 2 is out of scope. Do not work on its localised estimator, test, bootstrap, moving-subbundle theory, or frame-stabilizer correction.

---

## 0. Required output

Create the canonical file

`Ideas/Application map — geometry, symmetry, and rate accelerators.md`.

That file must contain:

1. a term-level decomposition of the current Paper 1 error;
2. an assumption-to-cancellation matrix;
3. proved accelerator theorems and analytic counterexamples;
4. a rate table showing exactly what improves and what does not;
5. a property-first application matching table;
6. nonexamples and failure modes;
7. a dependency graph;
8. a ranked research/application programme;
9. proof locations and status labels for every row.
10. a reality bridge quantifying approximate assumptions, observable diagnostics, and failure under realistic violations.

Create at most three noncanonical workstream dossiers if detailed proofs require them:

- `Ideas/APP-A — geometry and differential application atlas.md`;
- `Ideas/APP-B — cancellation and oracle-rate proof dossier.md`;
- `Ideas/APP-C — dependence, dimension, and hostile application audit.md`.

Update the following only after conclusions survive cross-audit:

- `Ideas/Paper 1 — Locally stationary Riemannian factor model.md`;
- `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md`;
- `Ideas/OPEN OBLIGATIONS — current research actions.md`;
- `Ideas/Time-varying Fréchet mean Riemannian factor model.md` if the programme hierarchy materially changes.

Do not rewrite historical tables as though they were current. Do not edit Paper 2.

---

## 1. Starting theorem and the rate gap

Treat the canonical HD1 dossier as the current source of truth. With

$$
\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1},
$$

the robust feasible loading theorem is

$$
\|\sin\Theta(\hat E_n,E_n)\|_{\mathrm{op}}
=O_p\!\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right).
$$

At the robust optimal bandwidth $b_n=n^{-1/7}$ and $a\ge3/7$, the numerator is $n^{-3/7}$. The parent fixed-centre oracle numerator is $n^{-1/2}$.

The team must keep three distinct ambitions separate:

### A. Faster mean estimation

Replacing the cubic bias $b_n^3$ by $b_n^q$ gives the ordinary nonparametric balance

$$
b_n^q+(nb_n)^{-1/2}
\asymp n^{-q/(2q+1)}.
$$

For every finite $q$, this remains slower than $n^{-1/2}$. A higher-order smoother alone does not recover the oracle loading rate if loading error is still first order in mean error.

### B. First-order immunity of loading recovery

If an application property makes the feasible lag-operator perturbation depend on $\ell_n^2$ rather than $\ell_n$, then

$$
\ell_n=o(n^{-1/4})
$$

is sufficient for the mean-estimation contribution to be $o(n^{-1/2})$. The current $n^{-3/7}$ mean rate already satisfies this. This is the principal route to the oracle numerator.

### C. Better denominators or factor-number behaviour

An application may strengthen the relationship between the lag signal $s_n$ and the eigengap $\Delta_n$, impose a population eigenvalue profile, or make threshold selection easier. Such improvements must be proved separately from numerator improvements.

Never call a result “oracle rate” unless the final displayed loading-space theorem has an $n^{-1/2}$ numerator with every residual term and denominator explicit.

## 1A. Reality bridge — exact assumptions are not enough

The application map fails scientifically if it proves only elegant exact cases that real data cannot plausibly approximate. Every exact accelerator theorem must therefore be followed by a **stability theorem** or an analytic demonstration that no useful stability theorem is possible.

If an exact cancellation property is replaced by a defect parameter $\varepsilon_n$, derive the perturbed expansion. A typical target is

$$
d_n
=O_p\!\left(
n^{-1/2}+\ell_n^2+\varepsilon_n\ell_n+\zeta_n+\rho_n
\right),
$$

where, depending on the application:

- $\varepsilon_n$ measures failure of symmetry, GLO, commutativity, flatness on relevant planes, or conditional centring;
- $\zeta_n$ measures nonzero included-lag noise covariance or factor–noise cross covariance;
- $\rho_n$ collects dependence tails, spectral-band escape, centre-model error, or estimator-specific remainders.

Do not assume this form; derive the correct defect term for each property. The point is to answer questions such as:

- Does approximate symmetry leave $O(\varepsilon_n\ell_n)$, $O(\varepsilon_n)$, or a worse term?
- Does a small commutator control the relevant base-point/Hessian term, or only a population approximation?
- If matrices are nearly jointly diagonalizable, what norm of the off-diagonal component enters the loading error?
- If idiosyncratic lag covariance is small rather than zero, does it create sampling error or population target bias?
- If dependence is not finite-memory, what truncation tail appears and how should truncation grow?
- If total energy grows as $R_n$, where does $R_n$ enter concentration, Taylor remainders, and the eigengap condition?
- If a spectral band holds with high probability rather than almost surely, what tail probability and truncation bias are paid?

For an oracle numerator, verify the actual requirement, for example

$$
\ell_n^2+\varepsilon_n\ell_n+\zeta_n+\rho_n=o(n^{-1/2}).
$$

If this requires an application defect to vanish at an implausible rate, mark the oracle branch **mathematically valid but application-fragile**. The robust $n^{-3/7}$ theorem may be the scientifically honest conclusion.

Every application row must receive one of these feasibility labels:

- **EXACT STRUCTURAL MATCH:** the property follows from the data-generating model or representation, not from wishful preprocessing;
- **STABLE APPROXIMATE MATCH:** a measurable defect enters a proved degradation bound and the required scale is scientifically plausible;
- **DIAGNOSTIC-ONLY MATCH:** the property can be assessed empirically but available theory does not turn the diagnostic into a valid rate;
- **IMPLAUSIBLE / MODEL-DISTORTING:** the property would exclude the dominant variation or require preprocessing that changes the scientific estimand;
- **UNKNOWN:** neither a proof nor a credible counterexample/application argument is available.

Exact asymptotic assumptions need not hold literally in a finite dataset. They must, however, define a plausible sequence of data-generating processes, and the theorem must be stable enough that small departures do not destroy the conclusion.

---

## 2. Absolute evidence and closure rules

The following do not prove an application row:

- a web search or abstract;
- a simulation or fitted exponent;
- a symbolic calculation without a general proof;
- saying that an application is “approximately flat,” “highly symmetric,” or “usually commuting”;
- identifying a manifold as a symmetric space without proving the required statistical cancellation;
- showing $\nabla R=0$ and then silently treating $R$ as zero;
- proving an expectation is zero without controlling its empirical fluctuation;
- invoking cross-fitting without proving the exact conditional centring and dependence separation;
- a fixed-matrix-size derivative bound presented as uniform in growing matrix size;
- an entrywise bound with a hidden dimension sum;
- replacing bounded total tangent energy by bounded energy in each coordinate;
- claiming an application has bounded total energy without stating its normalization or asymptotic sampling model.

Every substantive claim must end with one of:

- **PROVED**;
- **PROVED UNDER EXPLICIT ASSUMPTIONS**;
- **PROVED/CITED**, with the external theorem and its hypotheses checked exactly;
- **DISPROVED**, by an analytic counterexample;
- **SUPERSEDED/BYPASSED**, with the dependency removal proved;
- **OPEN** or **CONDITIONAL**, only when no final theorem consumes it.

Web access may locate primary sources or application definitions. It may not substitute for proof. Numerical experiments may be retained as diagnostics only after the theorem status is settled.

---

## 3. Read before proving

Recursively inventory `Ideas/` and read at minimum:

- `HD1 — growing-dimension Paper 1 proof dossier.md`;
- `HD1-A — G1 and derivative proof dossier.md`;
- `HD1-B — lag operator signal and factor number proof dossier.md`;
- `HD1-C — hostile counterexamples and assumption audit.md`;
- `G1 audit — resolution of the uniform local Fréchet rate.md`;
- `Paper 1 — Locally stationary Riemannian factor model.md`;
- `Analytical reconstruction — proof ledger and rebuilt spec.md`;
- `OPEN OBLIGATIONS — current research actions.md`;
- `Time-varying Fréchet mean Riemannian factor model.md`.

The HD1 dossier is canonical. HD1-A/B/C are noncanonical workstream evidence and may contain intermediate conditional statements later closed or bypassed in HD1.

Before proving anything, construct an internal ledger containing every leading term in:

1. local mean bias and stochastic error;
2. derivative mean error;
3. logarithm recentering;
4. connector and polygonal-frame error;
5. ribbon holonomy;
6. feasible-versus-oracle lag covariance;
7. lag-row and lag-operator assembly;
8. Davis–Kahan;
9. beyond-rank eigenvalues and factor selection.

For each term record whether it is deterministic bias, empirical fluctuation, curvature interaction, frame error, dependence error, signal denominator, or estimator artifact.

---

## 4. Required team structure

Use one lead and three parallel subagents. Give each subagent the repository context and require it to write a noncanonical dossier or return proof-ready material. Subagent drafts are not canonical until attacked by another agent and integrated by the lead.

### Subagent A — geometry and uniform differential atlas

Prove or break the relevant geometric implications for:

- Euclidean vector spaces and Hilbert spaces;
- ordinary real symmetric matrices with the Frobenius metric;
- diagonal or jointly commuting SPD matrices under the affine-invariant metric;
- full SPD matrices under the affine-invariant metric on a uniformly conditioned spectral band;
- locally symmetric spaces with $\nabla R=0$;
- constant-curvature spaces;
- totally geodesic flat submanifolds;
- product manifolds;
- Lie groups with invariant metrics where relevant;
- compact symmetric spaces subject to injectivity/non-conjugacy restrictions;
- Bures–Wasserstein SPD geometry as a cautionary non-Hadamard/incomplete case.

This agent must distinguish:

$$
R=0,qquad \nabla R=0,qquad
R(V,W)=0\text{ only on relevant planes},qquad
\text{and distributional cancellation involving }R.
$$

It must also attack the automatic growing-size AIRM assumptions. On a spectral band

$$
cI\preceq \Sigma\preceq CI,
$$

determine which Exp, Log, parallel-transport, Hessian, base-point Richardson, and required higher differential operator bounds are uniform in matrix size in the project’s chosen norms. Prove them by dimension-free operator calculus or provide a counterexample showing explicit dimension growth.

### Subagent B — cancellation and oracle-rate theorem

Write the feasible lag-product expansion to the first non-vanishing order and identify the exact coefficient of every term linear in mean or frame estimation error.

Investigate, separately and in combinations:

- flatness;
- trivial holonomy on the relevant tube;
- a constant centre path;
- a known centre;
- a finite-dimensional parametric centre estimated at root-$n$ rate;
- sample splitting or leave-block-out estimation;
- deterministic or scalar observation Hessian;
- geodesic reflection symmetry of the observation law;
- isotropy under a stabilizer group;
- conditional sign symmetry;
- geometric lag orthogonality (GLO);
- factor/noise lag orthogonality;
- commuting tangent observations;
- estimator-level debiasing of the first-order Hessian term.

For each candidate condition, prove exactly one of:

1. it kills a specific first-order term pathwise;
2. it kills the term only in expectation;
3. it makes the term conditionally centred after cross-fitting;
4. it changes only a constant, not an order;
5. it is insufficient, with a counterexample.

The main target is a theorem of the form

$$
d_n=O_p\!\left(n^{-1/2}+\ell_n^2+\rho_n\right),
$$

under a checkable property package, where every additional remainder $\rho_n$ is explicit. If $\ell_n^2+\rho_n=o(n^{-1/2})$, derive

$$
\|\sin\Theta(\hat E_n,E_n)\|_{\mathrm{op}}
=O_p\!\left(\frac{n^{-1/2}}{\Delta_n}\right).
$$

Flatness alone must not be assumed sufficient. A flat model may still have first-order additive recentering error unless centring, orthogonality, independence, or estimator design removes it.

### Subagent C — dimension, dependence, signed route, and hostile audit

Prove or break application-level compatibility of:

- bounded total tangent energy as $p_n\to\infty$;
- normalization schemes that make total energy bounded;
- fixed rank or low intrinsic-rank support;
- trace-bounded covariance versus coordinatewise bounded variance;
- fixed finite memory;
- dimension-uniform Hilbert physical dependence;
- martingale-difference or innovation structures;
- mixing conditions and their exact dimension-free consequences;
- signed G1-LP Hessian concentration for growing $p_n$;
- factor-signal and eigengap assumptions under concrete scaling regimes.

It must also build approximate-assumption defects for total energy, dependence tails, included-lag noise covariance, factor–noise cross covariance, spectral-band escape, and signal dilution. For every defect, determine whether it changes the estimand, creates population bias, or merely enlarges sampling error.

This agent is also the hostile application auditor. For every attractive application family, search for the easiest way its proposed property profile can fail:

- noncommuting matrices;
- eigenvalues approaching zero or infinity;
- changing eigenvectors;
- energy growing with dimension;
- long memory;
- curvature singularities or cut-locus approach;
- symmetry broken by conditional heteroskedasticity;
- cross-fitting blocks that do not actually separate innovations;
- signal dilution causing $\Delta_n\to0$.

### Lead agent — integration and application matching

The lead owns the term ledger, dependency graph, theorem statements, repository edits, and final application rankings. It must not begin application matching until A and B have produced a proof-status property library and C has attacked it.

---

## 5. Required property taxonomy

The canonical application map must separate at least the following levels.

### Level G — geometric identities

Examples include:

- globally flat geometry;
- flatness only on the support tube;
- flatness only on the two-planes entering the ribbon term;
- a totally geodesic flat containing the centre path and observations;
- trivial versus nontrivial global holonomy;
- local symmetry $\nabla R=0$;
- constant curvature;
- commuting SPD structure;
- product decomposition;
- dimension-uniform non-conjugacy and differential constants.

### Level L — law and symmetry identities

Examples include:

- geodesic-reflection invariance about the Fréchet mean;
- tangent sign symmetry $Y\overset d=-Y$;
- conditional symmetry given factors or training data;
- isotropy under a group action;
- deterministic, scalar, or block-scalar expected Hessian;
- vanishing odd covariant moments;
- lag-specific GLO.

Do not conflate unconditional symmetry with the conditional identities required in lag products.

### Level M — model alignment

Examples include:

- constant or known centre;
- centre constrained to a flat;
- loading space aligned with a commuting algebra;
- exact included-lag factor/noise orthogonality;
- factor signal concentrated in a stable fixed-rank block;
- uniform spectral gap;
- low-rank or trace-bounded total energy.

### Level D — dependence structure

Examples include:

- independence;
- finite memory;
- martingale differences;
- physical dependence with summable dimension-free coefficients;
- mixing with a proved Hilbert-valued inequality;
- conditional independence created by a correctly specified sample split.

### Level E — estimator design

Examples include:

- positive three-scale mean;
- a higher-order curvature-corrected positive estimator;
- signed local-polynomial mean;
- sample splitting or leave-block-out construction;
- explicit Hessian debiasing;
- a parametric centre estimator;
- normalization chosen to keep total energy bounded.

A useful accelerator may require one condition from several levels. Record the minimal package actually proved sufficient.

---

## 6. Mandatory distinction between common geometries

The application map must state and prove the following distinctions rather than relying on names.

### Ordinary symmetric matrices

The vector space of real symmetric matrices with the Frobenius metric is flat. If an application genuinely lives in this unconstrained vector space, Euclidean cancellation arguments may apply.

### Commuting SPD matrices under AIRM

SPD matrices sharing a fixed eigenbasis lie in a flat, totally geodesic diagonal submanifold under the affine-invariant metric. In logarithmic eigenvalue coordinates, much of the geometry becomes Euclidean. Verify that the centre, observations, loading directions, and estimator remain inside the same flat. Pairwise commutation at isolated times is not enough if the common eigenbasis changes.

### Full SPD matrices under AIRM

The full affine-invariant SPD manifold is a nonpositively curved globally symmetric space. It has $\nabla R=0$, but generally $R\ne0$. Local symmetry helps uniform differential control; it does not by itself kill holonomy, random Hessian variation, or every recentering term.

### Constant-curvature and other symmetric spaces

Constant curvature makes Jacobi/Hessian terms explicit. It does not make them zero. Compact cases also require quantitative distance from conjugacy and the cut locus.

### Flat manifolds with topology

Zero curvature does not automatically imply a single global Euclidean chart or trivial global holonomy. State the convex-tube or topology assumption actually consumed.

These distinctions are non-negotiable because the purpose of the map is to identify what an application property buys, not merely what its manifold is called.

---

## 7. Assumption-to-cancellation matrix

For every candidate accelerator, the canonical map must contain one row with these columns:

| Property package | Exact checkable criterion | Proof identity | Term killed or improved | Pathwise / expectation / conditional | Estimator modification | New rate | Dimension dependence | Application examples | Nonexamples | Status | Proof location |
|---|---|---|---|---|---|---|---|---|---|---|---|

The “term killed or improved” entry must name a term from the term ledger. Prose such as “curvature is simpler” is not enough.

At minimum, settle rows for:

1. known centre;
2. constant centre but estimated;
3. parametric root-$n$ centre;
4. Euclidean/flat geometry plus cross-fitting;
5. a common commuting SPD flat;
6. full AIRM SPD with $\nabla R=0$;
7. reflection-symmetric observation law;
8. isotropic law;
9. deterministic or scalar Hessian;
10. GLO;
11. higher-order positive smoothing;
12. signed growing-$p_n$ smoothing;
13. broader Hilbert physical dependence;
14. bounded total-energy normalization;
15. strong signal/eigengap scaling.

If two rows produce the same theorem, merge them only after proving that their criteria imply the same identity.

---

## 8. Required theorem targets

Attempt the following in order. A failed target must be replaced by a counterexample and the strongest corrected theorem.

### T-APP-1 — exact flat/commutative reduction

Give sufficient conditions under which the relevant Paper 1 model and estimator remain in one flat convex region and reduce to a Hilbert-space locally stationary factor problem. State exactly which connector, holonomy, Hessian, and base-point terms disappear and which mean-estimation terms remain.

### T-APP-2 — locally symmetric AIRM differential verification

On a uniformly conditioned AIRM SPD tube, prove the matrix-size dependence or independence of every higher differential constant assumed by HD-G. Do not infer all bounds solely from $\nabla R=0$.

### T-APP-3 — first-order cancellation/oracle theorem

Find the weakest checkable combination of geometry, law symmetry/GLO, dependence separation, and estimator design that yields quadratic feasible recentering or another route to an $n^{-1/2}$ loading numerator.

The theorem must specify whether the cancellation is pathwise, population-only, or conditional after cross-fitting, and must bound the surviving empirical linear term.

### T-APP-4 — broader dependence theorem

Replace fixed finite memory by a dimension-uniform Hilbert physical-dependence, martingale, or other scientifically useful condition. Prove the exact concentration inequalities consumed by G1 and the lag-row theorem. If a proposed mixing formulation fails, construct a counterexample and retain the strongest valid class.

### T-APP-5 — signed growing-dimension route

Determine whether a useful application property—scalar Hessian, isotropy, commuting structure, or block decomposition—allows the signed local-polynomial G1 route to avoid a dimension-costly empirical Hessian theorem. Prove the route or prove why the property is insufficient.

### T-APP-6 — property-to-application matching theorem

For each selected application family, verify every property by definition, modelling assumption, or exact data-generating restriction. Then state the strongest proved Paper 1 corollary and rate available to that family. An application label alone is never a hypothesis.

---

## 9. Application matching stage

Only after the property matrix is proved or status-classified, evaluate candidate families such as:

- Euclidean functional or multivariate factor data;
- unconstrained symmetric-matrix observations with Frobenius geometry;
- diagonal covariance, volatility, or diffusion-tensor models;
- jointly diagonalizable or fixed-eigenvector SPD processes;
- full covariance/correlation/SPD time series under AIRM;
- diffusion tensors with changing eigenvectors;
- functional-connectivity covariance matrices;
- product-manifold observations;
- shape, Grassmann, or compact symmetric-space data;
- Bures–Wasserstein covariance models;
- any concrete application already contemplated by the project.

For each family, fill out this scorecard:

| Field | Required content |
|---|---|
| Observation space and metric | Exact manifold/vector space and norm |
| Asymptotic dimension | What grows and how manifold dimension is calculated |
| Total-energy model | Normalization or structural reason the norm remains bounded |
| Geometric profile | Flat, commuting flat, locally symmetric, curved, cut-locus risks |
| Law symmetry | Exact invariance or moment identity, not intuition |
| Dependence profile | Finite memory, physical dependence, martingale, mixing, etc. |
| Signal profile | Scaling of $s_n$ and $\Delta_n$ |
| Estimator required | Robust, cross-fitted, debiased, signed, parametric, etc. |
| Proved cancellation | Exact term and theorem number |
| Approximation defect | Observable or model-defined measure of failure |
| Stability penalty | Proved additional term in the rate or target bias |
| Required defect scale | Rate needed for robust or oracle conclusions |
| Resulting rate | Full numerator and denominator |
| Failure modes | Conditions under which the match breaks |
| Feasibility | Exact match / stable approximate / diagnostic-only / implausible / unknown |
| Status | Proved / conditional / disproved / open |

Rank applications by **theorem strength × plausibility of assumptions × scientific value**, not by familiarity or dataset availability.

Penalise an application ranking when its strongest theorem depends on an unobservable defect, an unrealistic vanishing rate, a normalization that removes the phenomenon of interest, or an exact orthogonality imposed only for mathematical convenience. Report the strongest robust fallback theorem beside every fragile accelerated theorem.

An application can appear in more than one regime. For example, covariance data may be:

- full noncommuting AIRM SPD;
- constrained to a common commuting flat;
- treated as unconstrained symmetric matrices under Frobenius loss;
- normalized to bounded total energy;
- or allowed pervasive coordinate energy.

These are different mathematical models and must receive different rows and rates.

---

## 10. Counterexamples the team must actively seek

Try to break at least the following tempting implications:

1. $\nabla R=0$ implies the curved recentering term vanishes.
2. $R=0$ alone implies oracle loading recovery.
3. unconditional sign symmetry implies conditional lag-product cancellation.
4. an isotropic population Hessian makes the empirical Hessian deterministic.
5. cross-fitting plus zero covariance implies conditional independence.
6. pairwise commuting observations imply one fixed global commuting flat.
7. bounded condition number implies every AIRM higher differential is dimension-free in every norm.
8. coordinatewise bounded variance implies bounded total tangent energy.
9. a higher-order mean estimator alone yields an $n^{-1/2}$ loading numerator.
10. a strong factor lag $s_n$ automatically gives the exact desired eigengap profile without checking all included lags.
11. a root-$n$ centre estimator automatically has negligible first-order effect on a root-$n$ loading estimator.
12. a manifold used for “symmetric matrices” is necessarily flat under the metric actually used by the application.

Every successful counterexample must satisfy the hypotheses it attacks. Record the corrected implication beside it.

---

## 11. Rate ledger

For every proved property package, report all applicable rates, not only the best-looking one:

- mean sup norm;
- mean $L^2$/grid RMS;
- derivative mean error if consumed;
- polygonal-frame error;
- feasible lag-row error $d_n$;
- lag-operator perturbation $\eta_n$;
- loading-space error;
- beyond-rank eigenvalue rate;
- factor-number tuning window.

Show bandwidth feasibility explicitly. If the proposed oracle route uses $\ell_n^2=o(n^{-1/2})$, verify it term by term:

$$
b_n^6=o(n^{-1/2}),\qquad
(nb_n)^{-1}=o(n^{-1/2}),\qquad
n^{-2a}=o(n^{-1/2}),
$$

plus all cross-terms and application-specific remainders. Do not infer the square of a sum is harmless without checking every term.

If a property improves only constants, say so. If it improves mean estimation but not loading recovery, say so. If it improves the numerator but strengthens the denominator assumptions, display both changes.

---

## 12. Adversarial cross-audit

After the first workstream pass:

1. A attacks B's use of flatness, local symmetry, holonomy, and AIRM differential bounds.
2. B attacks A's claim that a geometric identity produces a statistical cancellation.
3. C attacks every dimension-free, dependence, energy, and application-compatibility claim from A and B.
4. A attacks C's proposed application counterexamples for geometric validity.
5. The lead resolves each objection, requests a rerun where necessary, and records the resolution.

No theorem enters the canonical application map merely because its originating subagent marked it proved.

Run a final hostile search for these phrases and inspect every occurrence:

- flat;
- symmetric;
- locally symmetric;
- commuting;
- isotropic;
- sign symmetry;
- GLO;
- oracle rate;
- $n^{-1/2}$;
- dimension-free;
- AIRM;
- bounded total energy;
- physical dependence;
- cross-fitting;
- quadratic recentering;
- higher differential;
- application.

Remove or qualify every occurrence that lacks a theorem, exact criterion, or explicit status.

---

## 13. Repository editing discipline

The canonical application-map file must lead with current conclusions, not brainstorming. Workstream dossiers may preserve failed routes and detailed attacks but must be labelled `noncanonical-workstream`.

Use the repository's existing status vocabulary. Preserve the current HD1 theorem unless a genuine contradiction is proved. Do not weaken the robust theorem merely because a sharper application-specific branch is added.

Update `OPEN OBLIGATIONS` so that:

- proved application accelerators move out of the open queue;
- disproved shortcuts are recorded as warnings;
- genuinely open accelerator questions name their exact missing lemma;
- no application-matching row is called proved when it still consumes an open theorem.

The final repository must make the hierarchy explicit:

1. robust arbitrary-$p_n$ Paper 1 theorem;
2. sharper application-specific corollaries under additional checkable properties;
3. optional open generalisations;
4. applications matched to the strongest theorem they actually satisfy.

---

## 14. Definition of done

The run is complete only when:

1. the canonical application map exists;
2. every candidate property is tied to a named proof term;
3. every rate claim is derived rather than guessed;
4. flat, commuting SPD, and full AIRM SPD are cleanly distinguished;
5. geometric simplification is separated from statistical cancellation;
6. the oracle-rate branch is either proved under checkable assumptions or disproved and sharply replaced;
7. AIRM growing-size differential assumptions are proved, shown dimension-dependent, or precisely left optional without being silently consumed;
8. broader dependence and signed-route claims receive honest proof statuses;
9. applications are matched only after their property profiles are verified;
10. every exact application match has an approximate-assumption stability analysis or is explicitly marked fragile;
11. every proposed diagnostic is separated from an assumption that can actually be justified theoretically;
12. applications that violate bounded-total-energy, finite-memory, exact lag orthogonality, commutativity, or symmetry are not hidden or discarded without reporting the consequence;
13. every load-bearing statement survives cross-agent attack;
14. canonical repository files agree;
15. remaining open items block no theorem labelled proved.

Do not stop with “this would be useful in covariance applications.” State which covariance model, metric, commutation restriction, spectral band, normalization, dependence class, signal regime, estimator, cancellation identity, and rate.

---

## 15. Final report

Return a concise report containing:

### Files changed

List every file and its mathematical role.

### Property-to-term discoveries

State the strongest proved cancellations and the exact terms they remove.

### New theorem branches

State each application-specific theorem, assumptions, bandwidth, numerator, denominator, and dimension scope.

### Disproved shortcuts

List every attractive but false implication and its analytic counterexample.

### AIRM verification

State which higher differential bounds are genuinely uniform in matrix size and which remain assumed or fail.

### Dependence and signed-route status

State exactly how far the fixed-memory and positive-route assumptions were broadened.

### Application ranking

Give the highest-value application matches and why their property packages are mathematically credible. For each, report the robust fallback, the accelerated theorem, the approximation defects, and the defect sizes needed for the acceleration to matter.

### Reality verdict

State plainly which application families are exact matches, stable approximate matches, diagnostic-only possibilities, or implausible matches. If no important application survives, say so and identify whether the failure comes from bounded total energy, dependence, geometry, orthogonality, signal scaling, or estimator design.

### Remaining work

List only optional, non-consumed questions with exact missing lemmas.

### Verification

Describe the cross-agent objections and their resolutions.

---

## 16. Final instruction

Start by reading the repository and building the term ledger. Then spawn the three workstreams.

First discover the mathematical qualities worth wanting. Prove what each quality buys. Attack the shortcuts. Only then look for applications possessing the surviving property packages.

The point is not to decorate applications with assumptions. The point is to turn application structure into proved cancellations, sharper convergence, or weaker dimension/dependence requirements—and to know exactly when that conversion fails.
