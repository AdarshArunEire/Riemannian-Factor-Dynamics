---
type: proof-adjudication
title: FRAME-DB — lead adjudication ledger
status: noncanonical-workstream
scope: bounded-energy fixed-memory Paper 1 FRAME-DB campaign; Paper 2 excluded
adjudication: Gate D
---

# FRAME-DB — lead adjudication ledger

> This is the lead adjudication for the campaign specified by [[FRAME-DB — GENERIC CURVED FRAME DEBIASING TEAM PROOF PROMPT]]. It does not edit canon. All twelve required canonical and archived sources were read completely. The three companion dossiers are [[FRAME-DB-A — geometry gauge and influence]], [[FRAME-DB-B — feasible estimator and row theorem]], and [[FRAME-DB-C — hostile identifiability and counterexamples]].

## 0. Plain-language verdict

**Gate D — OPEN — EXACT LEMMA STATED.**

Generic curved non-rigid frame debiasing is not proved. Generic non-identifiability is also not proved and, under the retained unique-mean/fixed-connection assumptions, the obvious observational-equivalence attack is false: the population Fréchet path, its Levi–Civita transport, and the Paper 1 lag row modulo one common anchor rotation are functionals of the observable law.

The campaign seriously tested all four mandated constructions. Naive pointwise frame plug-in, fixed-fold jackknife/Richardson averaging, and invariant-only redesign fail on declared analytic classes. A complete one-step/Jacobi correction remains possible in principle, but it requires one unproved aggregate influence lemma for the actual polygonal estimator. The missing result is not “estimate the frame better.” It is an observable, common-gauge-equivariant, direct-sum Hilbert–Schmidt influence representation for the entire mean–log–transport–lag functional, with root-\(n\) empirical influence fluctuation and a sub-root-\(n\) nuisance remainder.

The robust canonical fallback remains

\[
d_n=O_p(n^{-1/2}+\ell_n),\qquad
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
=O_p\{(n^{-1/2}+\ell_n)/\Delta_n\},
\quad \ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
\tag{0.1}
\]

At \(b_n=n^{-1/7}\), this is the proved \(n^{-3/7}\) numerator. No canonical statement is changed by this campaign.

## 1. Fixed interface and the mean/frame distinction

After one common anchor rotation is removed, APP-B proves

\[
U_t=Y_t-H_te_t+\Omega_tY_t+\xi_t^{(2)},
\qquad
\|\xi_t^{(2)}\|\lesssim
\|e_t\|^2+\|e_t\|\|\Omega_t\|+\|Y_t\|\|\Omega_t\|^2.
\tag{1.1}
\]

The two channels are different:

\[
L_{t,h}^{\rm mean}=-H_te_t\otimes Y_{t-h}-Y_t\otimes H_{t-h}e_{t-h},
\tag{1.2}
\]

\[
L_{t,h}^{\rm fr}=\Omega_tY_t\otimes Y_{t-h}
+Y_t\otimes\Omega_{t-h}Y_{t-h}.
\tag{1.3}
\]

Exact training/evaluation separation and GLO conditionally centre (1.2). They do not centre (1.3), whose population coefficient is

\[
\Phi_{F,n}(h)=N_{n,h}^{-1}\sum_t
\{\Omega_t\Gamma_{t,h}-\Gamma_{t,h}\Omega_{t-h}\}.
\tag{1.4}
\]

One time-constant skew is the derivative of a common conjugation and is quotiented out. Only the time-varying residual belongs in (1.4). The frame coefficient is measured in direct-sum HS norm and is produced by the HS lag-energy budget \(G_{2,{\rm HS},n}\), not by operator row energy without a rank restriction.

## 2. What is observable

### Proposition L-ID — observable-law identification

Fix the manifold, Levi–Civita connection, path convention, and a class in which every time marginal has a unique Fréchet mean and these means form the unique admissible regular path. Then the common-conjugacy class

\[
\mathfrak T_n(P)=\left[
\left(N_{n,h}^{-1}\sum_tE_P\{Y_t(P)\otimes Y_{t-h}(P)\}\right)_{h\le h_0}
\right]
\tag{2.1}
\]

is a functional of the observable law. Equal observable laws give the same mean path, transport ODE, lag-pair integrands, and lag row. Anchor coordinates differ by one common orthogonal conjugation. **Status: PROVED.**

This does not make (2.1) easy to estimate. It rules out treating \(\Omega_t\) as a freely varying latent DGP parameter after the observable law is fixed.

| Object | Used by computation? | Status |
|---|---:|---|
| raw observations and split/mask | yes | observed |
| fitted positive vertex means and polygon | yes | observed estimator |
| manifold Exp, Log, PT, curvature/Jacobi operations when geometry is known | yes | observed/known operation |
| true centre/path/frame | no | proof comparison only |
| true anchor alignment | no | quotient comparison only |
| \(e_t,\Omega_t,\Gamma_{t,h}\) | no | proof comparison/population target |
| unobserved true ribbon | no | forbidden computational input |
| fitted Karcher inverse and polygon derivative | potentially | rates not proved generically |

## 3. The four estimator strategies

### 3.1 Plug-in infinitesimal-frame subtraction

Write \(\widetilde Y_t=Y_t+a_t\) and \(\widetilde\Omega_t=\Omega_t+\delta_t\) after proof alignment and removal of the best common skew. The first residual population coefficient is

\[
\mathcal B_h(\delta)=N_h^{-1}\sum_t
\{\delta_t\Gamma_{t,h}-\Gamma_{t,h}\delta_{t-h}\}.
\tag{3.1}
\]

Products involving \(a_t\) and \(\widetilde\Omega_t\) remain, as displayed in the B/C dossiers. With the required shifted/action RMS and envelope assumptions, the coefficient-conditional bound is

\[
d_{F,{\rm plug},n}
\lesssim \|\oplus_h\mathcal B_h(\delta)\|_{\rm HS}
+r_\delta n^{-1/2}
+\widetilde r_F r_a+\text{typed higher products}.
\tag{3.2}
\]

Differences of noisy fitted frames do not identify either truth-relative error without a synchronization or influence identity. An \(O_p(\ell_n)\) frame rate does not imply (3.1) is \(o_p(n^{-1/2})\). **Status: DISPROVED** for naive noisy-frame-output plug-in; the broader aggregate influence construction is covered by the exact lemma in Section 7.

### 3.2 Influence-function/Jacobi correction

For a \(C^2\) path variation \(S(\epsilon,s)\), put \(T=\partial_sS\), \(V=\partial_\epsilon S\), and use connector generators \(E_a,E_b\). Under the A-dossier curvature convention,

\[
\mathcal P'_0W=-E_bP_{b\leftarrow a}W+P_{b\leftarrow a}E_aW
+\int_a^bP_{b\leftarrow s}R(T,V)P_{s\leftarrow a}W\,ds.
\tag{3.3}
\]

Radial connector generators vanish at first order. The actual polygon derivative is the ordered sum of differentiated cell transports, including the current partial cell and matched shared-vertex terms. The canonical polygon retains

\[
C_{{\rm geo},n}\{M_nr_N^2+M_n^{-2}\}.
\tag{3.4}
\]

At \(M_n\asymp\ell_n^{-2/3}\) and dimension-uniform \(C_{{\rm geo},n}=O(1)\), (3.4) is \(O_p(\ell_n^{4/3})=o(n^{-1/2})\) for \(\ell_n=n^{-3/7}\). The full observable-law derivative must also include inverse Karcher influence, base-log Hessians, endpoint terms, and the lag-law score. **Status: OPEN — EXACT LEMMA STATED.**

### 3.3 Multi-fold, jackknife, Richardson, and orthogonal score

For fixed \(K\), target-preserving weights applied to nuisance estimates \(\eta+r_nZ_k\) leave variance at least a constant multiple of \(r_n^2/K\) in any nonzero derivative direction. Thus fold averaging does not cancel realised \(n^{-3/7}\) nuisance noise. **Status: DISPROVED** for fixed-fold linear combinations without an evaluation influence score.

For \(\Psi(\mu)=E\log_\mu X\), \(D_\mu\Psi[v]=-Av\). If \(K=D_\mu T\), the sign-correct orthogonal template is

\[
S(\mu,P)=T(\mu,P)+KA^{-1}\Psi_P(\mu),
\qquad D_\mu S[v]=Kv+KA^{-1}(-Av)=0.
\tag{3.5}
\]

One fold must estimate \(\mu,K,A^{-1}\), one identically masked fold must evaluate the Karcher score, and one must form the base lag row. This template is not a theorem until the aggregate polygon/grid HS influence and all split products are controlled. **Status: OPEN — EXACT LEMMA STATED.**

### 3.4 Frame-avoiding or gauge-invariant redesign

Spectra and singular values do not determine the Paper 1 loading space; invariant-only estimation changes the estimand. Direct endpoint-geodesic transport changes the target by holonomy. Pairwise transports could recover (2.1) only after cycle-consistent synchronization up to one common \(Q\), with second-order centre sensitivity and a direct-sum HS concentration theorem. **Status: DISPROVED** for invariant-only redesign; cycle-synchronized recovery is subsumed by the exact lemma in Section 7.

## 4. Information bound and the residual convention

Conditional on a pilot, consider the regular submodel \(Z_i\sim N(\theta,1)\) and a scalar frame coefficient \(B(\theta)=\beta\theta\), \(\beta\ne0\). Testing \(\theta=0\) against \(c/\sqrt n\) gives a Le Cam root-\(n\) lower bound. No estimator based on \(O(n)\) correction observations can estimate \(B(\theta)\) uniformly with \(o_p(n^{-1/2})\) error. **Status: PROVED** for this declared correction-only class.

Therefore two conventions must be separated:

1. If \(d_{F,{\rm db},n}\) includes every stochastic fluctuation of the estimated correction, the requested \(o_p(n^{-1/2})\) bound is impossible on that regular submodel.
2. In a one-step expansion, the unavoidable correction influence fluctuation belongs to the leading root-\(n\) empirical row. The FRAME-DB residual is then the nuisance remainder after that influence term. This is the only convention under which the optimistic objective is coherent.

No claim of oracle-equivalent limiting law is made: the corrected row's influence function may differ from the known-centre/frame oracle influence.

## 5. Target ledger

| ID | Target | Gauge | Verdict |
|---|---|---|---|
| T0 | oracle lag row in selected anchor coordinates | coordinate representative | identifiable after anchor choice |
| T1 | T0 modulo one common conjugation; identifiable from the law | intrinsic Paper 1 target | PROVED |
| T2 | feasible polygonal row | time-varying frame contamination retained | observed estimator |
| T3 | one-step/debiased feasible row | must estimate T1 | OPEN — EXACT LEMMA STATED |
| T4 | spectra/Gram/quotient summary | more invariant than T1 | changed estimand unless T1 reconstructs |

## 6. Claim and nuisance ledgers

### Claim ledger

| ID | Exact claim | Observable inputs | Unobservable comparison | Norm | Producer | Consumer | Rate | Objection | Resolution | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| L1 | four-term APP-B expansion | feasible vectors | \(e,\Omega,Y\) | row HS | APP-B | all strategies | first/quadratic | mean/frame conflation | equations (1.1)–(1.4) | PROVED |
| L2 | target is law-functional modulo common \(Q\) | observable law, known geometry | anchor coordinates | quotient row | L-ID | identifiability | exact | latent-gauge attack | uniqueness/path ODE | PROVED |
| L3 | naive plug-in residual contains (3.1) | fitted frame/vector | truth-relative errors | direct-sum HS | B/C | plug-in | first order | noisy frames | exact expansion | PROVED |
| L4 | fixed-fold weights retain nuisance noise | fold outputs | true nuisance | scalar projection | C | jackknife | \(r_n\) | deterministic bias cancellation | variance lower bound | DISPROVED |
| L5 | invariant spectra recover loading | invariant lag summaries | anchor loading | loading space | C | redesign | none | changed estimand | rotation example | DISPROVED |
| L6 | full polygon influence closes root-\(n\) | all observable fitted nuisances | full functional derivative | direct-sum HS | FRAME-IF-POLY | row theorem | root-\(n\)+small remainder | aggregation/grid/HS gap | exact lemma Section 7 | OPEN — EXACT LEMMA STATED |
| L7 | downstream loading/null result | corrected row | target row | operator/gap | APP-B/HD1 | loading/selector | root-\(n\) | actual gap/assembly | Section 8 | PROVED UNDER EXPLICIT ASSUMPTIONS |

### Nuisance ledger

| Nuisance | First-order coefficient | Proposed estimate/cancellation | Training fold | Evaluation fold | Residual | Required rate | Identifiability status |
|---|---|---|---|---|---|---|---|
| mean error | GLO maps applied to \(e_t\) | inverse Karcher score, sign (3.5) | fitted \(A^{-1}\), mean | masked score | quadratic plus IF estimation | sub-root-\(n\) remainder | functional identified; rate open |
| non-rigid frame | (1.4) | polygon Jacobi derivative inside \(K\) | fitted polygon/geometry | aggregate influence row | (3.4) plus producer errors | sub-root-\(n\) remainder | functional identified; rate open |
| common rigid gauge | common conjugation | quotient/synchronization | observable anchor convention | same convention | zero intrinsically | exact | identified modulo \(Q\) |
| lag-law sampling | direct lag influence | empirical base row | none | lag-pair row | root-\(n\) influence | \(O_p(n^{-1/2})\) | identified |
| mask/coupling | target and conditional-law defects | exact common mask/split | disjoint innovations | retained cores | additive defect | \(o(n^{-1/2})\) for oracle order | not removed by orthogonality |

## 7. Exact irreducible lemma

> **Lemma FRAME-IF-POLY — aggregate gauge-equivariant polygon influence.** Under the canonical bounded-total-energy, fixed-rank/lag/memory, exact finite-memory split, GLO, unique-mean, generated-tube, and dimension-uniform fixed-order geometry package, with deterministic \(M_n\asymp\bar\ell_n^{-2/3}\), construct an entirely observable three-fold estimator of (2.1) satisfying all five properties below.

1. **Typed derivative and gauge.** In a declared observable anchor convention, derive the derivative of the complete finite-array masked lag functional with respect to every admissible mean-path law perturbation. It must contain the inverse Karcher map, base-log Hessians, every ordered polygon-cell and partial-cell Jacobi derivative from (3.3), matched endpoint connectors, and the lag-law score. Under a common anchor rotation \(Q\), the estimator and influence row must conjugate by \(Q\); one common skew is projected out.
2. **Feasibility and folds.** Fold T estimates the positive vertex means, polygon, \(A^{-1}\), and the aggregate nuisance derivative \(K\); fold V evaluates the identically masked weighted Karcher score; fold E evaluates the base lag row. No true centre/frame/anchor, \(e,\Omega,\Gamma\), or true ribbon is used. Innovation sets are disjoint and every fold targets the same masked finite-array row.
3. **Asymptotic linearity.** For an observable influence summand \(\varphi_{n,P}\in\oplus_{h\le h_0}\mathcal S_2(H_0)\),
   \[
   \widehat{\mathfrak T}_n^{1s}-\mathfrak T_n(P)
   =(P_n-P)\varphi_{n,P}+R_n,
   \tag{7.1}
   \]
   where the empirical term includes both ordinary lag sampling and correction-score influence, rather than placing correction noise in \(d_{F,{\rm db},n}\).
4. **Direct-sum HS rate.** Prove dimension-uniformly
   \[
   \|(P_n-P)\varphi_{n,P}\|_{\oplus{\rm HS}}=O_p(n^{-1/2}),
   \tag{7.2}
   \]
   exposing the vertex weights, \(\ell^2_M\to\oplus\mathcal S_2\) norm of \(KA^{-1}\), memory, mask, curvature/path/grid constants, and every product or U-statistic term created by the folds.
5. **Nuisance remainder.** With a proved vertex maximum tube event,
   \[
   \|R_n\|_{\oplus{\rm HS}}
   =O_p\{M_n\ell_n^2+M_n^{-2}+r_e^2+r_er_F+r_F^2\}
   +o_p(n^{-1/2})+\rho_n,
   \tag{7.3}
   \]
   including fitted \(A^{-1}\), fitted \(K\), synchronization, mask, coupling, and target errors in their producer norms. At \(M_n\asymp\ell_n^{-2/3}\), the polygon part is \(O_p(\ell_n^{4/3})\).

**Status: OPEN — EXACT LEMMA STATED.**

This lemma is irreducible relative to the completed campaign: it combines the only surviving construction with the exact rate and observability properties attacked in both hostile passes. Proving merely a smooth-path identity, a pointwise \(\Omega\) estimate, or an \(O_p(\ell_n)\) frame bound does not prove it.

## 8. What FRAME-IF-POLY would unlock

At \(b_n=n^{-1/7}\), \(a\ge3/7\), \(\ell_n=n^{-3/7}\) and

\[
\ell_n^{4/3}=n^{-4/7}=o(n^{-1/2}),\qquad \ell_n^2=n^{-6/7}=o(n^{-1/2}).
\]

If FRAME-IF-POLY holds and \(\varepsilon_{G,n}\ell_n+\rho_n=o(n^{-1/2})\), then

\[
d_n^{\rm db}=O_p(n^{-1/2}+\ell_n^{4/3}+\ell_n^2
+\varepsilon_{G,n}\ell_n+\rho_n)=O_p(n^{-1/2}).
\tag{8.1}
\]

With \(A_{2,n}\) retained explicitly and

\[
2A_{2,n}d_n^{\rm db}+(d_n^{\rm db})^2=o_p(\Delta_n),
\tag{8.2}
\]

the existing row assembly and Davis–Kahan results give

\[
\|\sin\Theta(\widehat E_n^{\rm db},E_n)\|_{\rm op}
=O_p(n^{-1/2}/\Delta_n),
\qquad
\widehat\lambda_{r+1,n}^{\rm db}=O_p(n^{-1}).
\tag{8.3}
\]

Replacing \(\Delta_n\) by \(s_n^2\) requires the existing factorisation/full-rank-lag comparison. The empirical influence in (7.1) can change the limiting law; (8.3) is a rate conclusion.

## 9. Mandatory edge-family adjudication

| Edge family | Campaign result | Status |
|---|---|---|
| flat Hilbert | non-rigid frame vanishes after common alignment; mean channel remains | PROVED |
| fixed commuting SPD flat | exact flat reduction only when every estimator object stays in one fixed algebra | PROVED |
| common rigid \(\Omega_t\) | common conjugation; no additive/gap penalty | PROVED |
| CE-B5 | noncommuting alternating frame survives GLO and splitting, defeating the GLO-only route | DISPROVED |
| zero signal | frame coefficient zero but \(\Delta_n=0\); loading unidentified | PROVED |
| zero idiosyncratic noise | moving-centre ribbon can remain because signal supplies \(Y_t\), defeating noise-free immunity | DISPROVED |
| constant curvature/moving mean | curvature integral (3.3) is generally nonzero | PROVED |
| high-dimensional bounded energy | HS/operator counterexample defeats operator-energy substitution and requires \(G_{2,{\rm HS}}\) | DISPROVED |
| one bad grid vertex | retain maximum tube and \(M_nr_N^2\) | PROVED |
| high-frequency path | bounded length does not bound acceleration/chord lens | DISPROVED |
| near-commuting changing basis | raw commutators do not control one fixed algebra or ribbon | DISPROVED |
| identical laws/different decompositions | no different T1 survives unique mean/fixed connection/exact lag-range target | DISPROVED |

## 10. Two hostile cross-audits

### Pass 1

The first pass found and repaired:

- reversed/undefined endpoint connector signs and curvature orientation;
- double counting between fixed-observation geometric derivative and lag-law score;
- an impossible demand that correction coefficient noise itself be \(o_p(n^{-1/2})\);
- the wrong one-step sign;
- suppression of \(M_nr_N^2+M_n^{-2}\);
- an invalid triple-product conclusion from RMS inputs without an envelope/action norm;
- unproved fold sigma-fields, mask identity, synchronization, and aggregate HS concentration;
- promotion of an algebraic parametric template without a fully instantiated nonempty curved DGP;
- nonallowed status labels.

The repaired A/B dossiers downgraded every unclosed theorem to FRAME-IF-POLY and retained the root-\(n\) influence fluctuation separately from the nuisance residual.

### Pass 2

The fresh pass-2 record is in the C dossier. Its final objections and resolutions govern this ledger. No Gate A, B, or C conclusion is used unless pass 2 accepts every link from observables through (8.3).

## 11. Application boundary

No new generic curved application is enabled. Flat Hilbert and one fixed commuting SPD flat retain the existing exact-split oracle branch. Known/root-\(n\) parametric centre branches retain oracle order but not first-order immunity or oracle-equivalent law. Full AIRM, noncommuting BW, constant-curvature moving means, and changing-eigenbasis covariance applications remain on the robust theorem unless an application proves FRAME-IF-POLY or supplies a separate complete finite-dimensional observable derivative theorem.

Growing energy, infinite memory, shrinking BW margins, growing rank, and shrinking eigengap are outside this baseline adjudication.

## 12. Proposed canonical migration table

| Canonical file | Current statement | Proposed replacement | Proven producer | Status effect |
|---|---|---|---|---|
| `Analytical reconstruction — proof ledger and rebuilt spec.md` | generic curved frame debiasing remains open | record Gate D; link the exact FRAME-IF-POLY lemma; retain robust fallback | this ledger + A/B/C | replaces broad open phrase by exact open node; no theorem upgrade |
| `Application map — geometry, symmetry, and rate accelerators.md` | curved GLO branch conditional on small \(\phi_F\) | retain T-APP-3; add that naive plug-in/fixed-fold/invariant-only routes fail and full one-step closure is FRAME-IF-POLY | APP-B + this campaign | no application promoted |
| `OPEN OBLIGATIONS — current research actions.md` | `FRAME-DB: generic curved non-rigid frame debiasing` | replace with the five properties of FRAME-IF-POLY in Section 7 | this ledger | narrows the obligation exactly |
| `Paper 1 — Locally stationary Riemannian factor model.md` | generic curved oracle branch unavailable | add Gate D synopsis and correction-noise convention; retain \(n^{-3/7}\) fallback | this ledger | no proved rate changed |
| `Time-varying Fréchet mean Riemannian factor model.md` | generic curved debiasing open | link exact Gate D result and clarify law-identifiability versus feasible rate | L-ID + FRAME-IF-POLY | sharper research boundary only |

No edit is proposed to G1, HD1's proved robust theorem, the numerical suite, or Paper 2.

## 13. Remaining obligations

The sole baseline mathematical obligation is FRAME-IF-POLY. Its producer work decomposes into inseparable proof components, not separate theorem claims:

1. construct the aggregate polygon derivative \(K\) and fitted inverse Karcher action in observable folds;
2. prove common-gauge synchronization and identical masked targets;
3. prove the \(\ell^2_M\to\oplus\mathcal S_2\) influence norm and root-\(n\) concentration without hidden dimension/rank/grid cost;
4. prove the complete remainder (7.3), including \(M_n\ell_n^2+M_n^{-2}\), inverse-Hessian/derivative estimation, products, masks, and coupling;
5. verify (8.2) with the actual \(\Delta_n\).

Failure of any one component must yield either a theorem restriction or an analytic impossibility result for its declared estimator/model class. Failure of pointwise \(\Omega\) recovery alone is not generic impossibility.

## 14. Mechanical verification checklist

- Four and only four FRAME-DB campaign dossiers exist.
- No canonical file was edited by the campaign.
- Paper 2 is not consumed.
- All theorem statuses use the allowed vocabulary.
- Mean and frame channels are separately displayed.
- All tensor products and row norms use the APP-B orientation.
- Common conjugation is not sent through Davis–Kahan.
- Frame coefficients use HS lag energy; row assembly uses operator row energy.
- Polygon count, maximum tube, acceleration, mask, dependence, rank, energy, and actual gap are explicit.
- The exact one-step sign is fixed by \(D\Psi=-A\).
- Correction influence fluctuation and nuisance remainder are not conflated.
- Every proposed canonical change is in the migration table rather than applied.

Final status: **OPEN — EXACT LEMMA STATED.**
