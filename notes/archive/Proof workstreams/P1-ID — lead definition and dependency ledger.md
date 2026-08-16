---
type: archived-proof-ledger
title: P1-ID — lead definition and dependency ledger
status: terminal-campaign-two-hostile-passes-integrated
last-audited: 2026-08-12
authority: common notation, dependency graph, objections, and adjudication during the P1-ID campaign
---

# P1-ID — lead definition and dependency ledger

> Archived campaign ledger. The A/B/C dossiers are producer and audit records. Every canonical P1-ID claim survived two hostile passes, repair rechecks, and lead adjudication before integration.

## 0. Preservation and source record

- Worktree at entry: `main` ahead of `origin/main` by one commit; nine intentional modified/untracked P1-ID and canonical files were present. They are user work and must not be reverted.
- No repository `AGENTS.md` exists.
- Read completely: the campaign brief, current P1-ID boundary, canonical analytical ledger, Paper 1 spec, programme note, live obligations, HD1 dossier, and external-claim audit.
- Read for identification provenance: the historical identification ledger (T09–T14, T01–T08, Theorems A/B) and the old P1-ID obligation.
- Checked at the primary source: Huang–Chen–Chen (2026), equations (1)–(3), (P2), Remark 1, the lag estimator, and APP-FIN claims.
- Historical material is provenance, never status authority.

## 1. Common primitives

Let \((M,d)\) be a complete separable Riemannian manifold whenever probability laws on path space are used. At local time \(u\), let \(Q_u\in\mathcal P_2(M)\) and
\[
F_{Q_u}(x)=\int_M d(x,z)^2\,Q_u(dz),\qquad
\mathfrak M(Q_u)=\operatorname*{argmin}_{x\in M}F_{Q_u}(x).
\]
When \(\mathfrak M(Q_u)=\{\mu(u)\}\), \(\mu(u)\) is the unique pointwise Fréchet centre. A *reference curve* \(c(u)\) is not called a centre unless it is required to equal this unique law-functional.

For a centre/reference curve \(c\), on a declared common normal domain define
\[
Y_t^c=\log_{c(u_t)}X_t,
\qquad
\Phi_{x\to y}(z)=\log_y(\operatorname{Exp}_x z).
\]
The map \(\Phi_{x\to y}\) is typed from an open subset of \(T_xM\) to \(T_yM\); its use requires unique Exp/Log branches and support inside their common domain. Parallel transport is inserted only when two tangent vectors or loading subspaces are compared in one fibre.

An affine dynamic-factor representation in a Hilbert fibre \(H\) is
\[
Y_t=m(u_t)+Af_t+\delta_t,
\]
where \(A:\mathbb R^r\to H\) is injective (isometric when stated), and every claim must state the factor centring, persistence, idiosyncratic lag covariance, factor–noise cross-lag covariance, rank, and stationarity/local-stationarity conditions.

## 2. Information sets and observational equivalence

| Label | Information set | Exact equivalence relation | Legitimate target |
|---|---|---|---|
| \(\mathcal I_M\) | all pointwise marginal laws \(\{Q_u:u\in[0,1]\}\) | equality of every \(Q_u\) | law-functionals such as unique Fréchet centres; no serial object |
| \(\mathcal I_J\) | full time-series law | equality of all finite-dimensional distributions, equivalently the path law on the declared cylinder sigma-field | marginals, lag laws/operators, dynamic subspace, and decomposition quotient under model restrictions |
| \(\mathcal I_1\) | one locally stationary triangular-array path \(\{X_{t,n}:1\le t\le n\}\) as \(n\to\infty\) | equality/contiguity/asymptotic equivalence of the sequence of experiments, stated case by case | recoverability/estimability of an already defined population target |
| \(\mathcal I_F(c_0)\) | population or sample output after imposing one fixed centre \(c_0\) | equality of the declared fixed-centre lag rows/operators (strictly weaker than equality of joint law) | contaminated lag object and its spectral quotient, not a unique drift/factor split |
| \(\mathcal I_R\) | weakened-centre/reference-curve model | equality of the observation law after the exact change of coordinates \(Y^{\tilde c}=\Phi_{c\to\tilde c}(Y^c)\) | the orbit of admissible representations under base-point change and internal factor gauge |

Never replace equality in one row by equality in another. In particular, identical marginals do not mean identical temporal law; one-path recoverability is not a definition of population identification; and equality of a lag operator is much weaker than equality of a path law.

## 3. Gate 1 — theorem statement matrix

| Slot | Precise statement to close | Gate adjudication | Status | Producer | Consumer | Proof location / objection |
|---|---|---|---|---|---|---|
| G1-0 | If \(Q=\widetilde Q\in\mathcal P_2(M)\) and both representations require their declared centre to be the unique Fréchet mean, then their centres coincide. If the minimizer set is not a singleton, only \(\mathfrak M(Q)\) is identified. | The old curved “same marginal law, distinct unique centres” necessity problem is misformulated and needs no Jacobi-field proof. | PROVED INTERNALLY | Lead/A | ID-0, ID-1, ID-4 scope | §4.1; hostile attack must target existence, uniqueness, or a changed information set. |
| G1-1 | \(\mathcal I_J\Rightarrow\mathcal I_M\), while \(\mathcal I_M\not\Rightarrow\mathcal I_J\); neither a fixed-centre lag row nor finitely many lag rows determine \(\mathcal I_J\). | Nontrivial temporal identification survives after the centre is fixed. | proof and exact examples required | A/C | ID-0, ID-2 | Wave 1. |
| G1-2 | Given \(\mathcal I_J\) and a unique centre, classify all factor/loading/noise representations. The dynamic lag subspace is identified; factor coordinates and dynamically silent reallocations generally are not. | This, not centre ambiguity, is the full-law problem. | classification required | A, audited by C/B | ID-2 | Wave 1. |
| G1-3 | Under \(\mathcal I_1\), state when local empirical laws/means converge pointwise, and distinguish pointwise identification from uniform recovery over near-zero spectra. | This is an estimation/information-boundary theorem, not curved population identification. | theorem and counterexample required | A/C | ID-3, Paper 1 interpretation | Wave 3. |
| G1-4 | Under \(\mathcal I_F(c_0)\), expand the exact fixed-centre lag row into drift, factor, both cross terms, idiosyncratic lag, local-stationarity/end, and sample terms. | Historical additive formula is usable only when its cross terms are proved zero. | repaired theorem required | C/Lead | ID-5, ID-6 | Wave 4. |
| G1-5 | Under \(\mathcal I_R\), every alternative reference representation is related by the exact nonlinear map \(\Phi_{c\to\tilde c}\). Determine when the pushed-forward law still lies in the affine-factor-plus-white-noise model class. | This is the genuinely geometric base-point question. | rigidity/non-identification classification required | B, audited by A/C | ID-4 | Wave 2. |

## 4. Gate proofs and formal adjudication

### 4.1 Proposition G1-0 — unique marginal centres are law-functionals

**Statement.** Let \(Q\in\mathcal P_2(M)\). Suppose two admissible representations of the same marginal law \(Q\) declare \(c\) and \(\tilde c\) to be its unique Fréchet mean. Then \(c=\tilde c\). Without uniqueness, the identified object is exactly the minimizer set \(\mathfrak M(Q)\), and a selected centre requires an additional convention.

**Proof.** Equality of the marginal laws gives the same objective
\(F_Q(x)=\int d(x,z)^2Q(dz)\) for both representations. Hence
\(c,\tilde c\in\operatorname{argmin}F_Q\). If the argmin is the singleton \(\{m_Q\}\), then \(c=m_Q=\tilde c\). If it has multiple elements, the law determines the objective and therefore its full argmin set, but does not select one element absent a selection rule. \(\square\)

**Scope consequence.** Curvature affects whether existence/uniqueness and a usable Log domain hold, but it cannot create two different *unique* minimizers of the same objective. Therefore ID-4 must concern weakened centring/reference curves and preservation of the affine factor/noise class under \(\Phi\), not uniqueness of a law-functional centre under identical known marginals.

### 4.2 Proposition G1-1a — marginal law does not determine temporal law

Let \(Q\) be any non-degenerate law. An iid process \(X_t\sim Q\) and the constant process \(\widetilde X_t=Z\) for one \(Z\sim Q\) have identical marginals and different two-time laws. Thus \(\mathcal I_M\not\Rightarrow\mathcal I_J\). Conversely, equality of all finite-dimensional distributions includes equality of every one-dimensional marginal, so \(\mathcal I_J\Rightarrow\mathcal I_M\). \(\square\)

### 4.3 Formal Gate 1 verdict

1. **Population marginal centre:** immediate under a unique Fréchet mean; the former curved necessity target is sharply reformulated.
2. **Full-law decomposition:** nontrivial even after the centre is fixed; it concerns dynamic loading spans, factor gauge, and factor/noise reallocation.
3. **One path:** concerns recovery and uniform estimability of population law-functionals, with zero and near-zero frequency as the boundary.
4. **Fixed-centre misspecification:** concerns the exact contaminated lag functional; it never by itself identifies the drift/factor split.
5. **Weakened centring:** is the sole base-point-change problem requiring exact curved geometry.

This hierarchy is the scientific replacement for the ambiguous phrase “same observed process.”

## 5. Required theorem slots and dependency ledger

| ID | Claim / target | Information set | Model class | Equivalence / quotient | Norm or topology | Producer | Consumers | Current status | Main objection |
|---|---|---|---|---|---|---|---|---|---|
| ID-0 | information-set implications and non-implications | all five | metric laws / experiments | as in §2 | weak/FDD equality; experiment topology when used | Lead+A+C | all | **PROVED INTERNALLY; TWO HOSTILE PASSES COMPLETE** | avoid treating one-path limits as law equality |
| ID-1 | unique marginal-centre theorem and nonunique boundary | \(\mathcal I_M\) | \(\mathcal P_2(M)\) | singleton or argmin-set quotient | Wasserstein-2 only when continuity is claimed | Lead+A | ID-4 scope, interpretation | **PROVED INTERNALLY; TWO HOSTILE PASSES COMPLETE** | existence and measurability must not be smuggled in |
| ID-2 | flat/Hilbert decomposition equivalence class | \(\mathcal I_J\) | affine factor plus declared white noise | rotation/isometry plus dynamically silent reallocation; minimum dynamic rank | operator/HS on lag rows; equality of FDDs | A | ID-3, ID-5, Paper 1 | **PROVED INTERNALLY ON THE STATED SECOND-ORDER AND GAUSSIAN-FDD CLASSES** | lag covariance may identify less than full law; exact white-noise conditions matter |
| ID-3 | zero-frequency and local-mean recovery theorem | \(\mathcal I_J,\mathcal I_1\) | stationary/local stationary Hilbert processes | invariant-component quotient | \(L^2\), pointwise probability, and uniform risk separated | A+C | Paper 1 recovery interpretation | **CITED EXTERNALLY AND APPLIED / PROJECT-SPECIFIC PARTS PROVED INTERNALLY** | no-atom is pointwise, not a uniform rate class |
| ID-4 | exact curved reference-change rigidity/non-identification | \(\mathcal I_R\) | common normal domain; affine factor/noise before and after \(\Phi\) | base-point orbit plus internal factor gauge | exact equality of law; derivative results separately labelled | B | scientific boundary | **SHARPLY REFORMULATED AND PROVED; GENERIC RIGIDITY DISPROVED** | Taylor remainder cannot prove exact equality; restriction needs boundary proof |
| ID-5 | fixed-centre contamination with all cross/noise terms | \(\mathcal I_F(c_0)\) | moving unique centre truth, fixed-centre fit | identified contaminated row/operator only | direct-sum operator/HS | C+Lead | ID-6, N-18 language | **SHARPLY REFORMULATED AND PROVED** | historical formula suppressed cross terms and mixed population/sample notation |
| ID-6 | scientific interpretation of Factor 1 | conclusions of ID-0–ID-5 | parent (P2) and misspecified alternatives | sensitivity or identified quotient only | qualitative corollary tied to proved operators | Lead, audited by all | canonical Paper 1/programme | **PROVED INTERNALLY; TWO HOSTILE PASSES COMPLETE** | no dominance/spurious claim without dataset-specific identification |

## 6. Objection ledger

| Objection | Raised by | Target | Required disposition | Status |
|---|---|---|---|---|
| Historical T13 shifts a random constant factor into a random “centre”; that shifted object is not the unique marginal Fréchet mean and therefore cannot attack G1-0. | Lead | old Theorem B / ID-1 | reclassify as weakened-centre or latent-random-intercept non-identification | **REPAIRED, RECHECKED, AND INTEGRATED** |
| Equality of lag covariances is not equality of full path laws. | Lead | ID-2/ID-5 | state quotient relative to the declared information set | **REPAIRED, RECHECKED, AND INTEGRATED** |
| “White noise” must specify temporal uncorrelatedness versus independence and both cross-lag directions. | Lead | ID-2/ID-5 | theorem assumptions and counterexamples must use the exact version | **REPAIRED, RECHECKED, AND INTEGRATED** |
| The historical \(M_\mu+A\Gamma_f(h)A^*\) formula is false without zero drift–factor cross moments. | Brief/Lead | ID-5 | retain both cross terms and derive conditions for their disappearance | **REPAIRED, RECHECKED, AND INTEGRATED** |
| Absence of an atom at zero cannot yield a uniform rate over spectra concentrating arbitrarily near zero. | Lead | ID-3 | pointwise theorem plus explicit non-uniformity construction | **REPAIRED, RECHECKED, AND INTEGRATED BY THE UNIFORM IMPOSSIBILITY THEOREM** |

## 7. Review protocol

- Wave author table → one foreign workstream audit → author repair → same auditor recheck → lead check.
- After all four waves, Hostile Pass I attacks every ID statement and counterexample assumption.
- Hostile Pass II starts from the repaired package and attacks maximality, hidden conclusion-like assumptions, and canonical propagation.
- Only then may canonical integration and archival cleanup start.

## 8. Lead theorem synthesis after producer pass

This section is the candidate ID-0--ID-6 package submitted to hostile review. “Identified” always means relative to the displayed information set and class.

### ID-0 — information-set separation theorem

**Statement.** When the required moments exist and every Log used by a lag functional is single-valued on its declared branch, equality of all FDDs implies equality of every marginal and every such population lag functional. Equality of marginals does not imply equality of FDDs. Equality of a lag row does not imply equality of FDDs or equality of marginals. Even joint equality of all one-time marginals and all covariance lags does not determine non-Gaussian FDDs. A fixed-centre lag row is therefore a quotient of the two-time laws, not an observation-law identifier. One-path recovery is a sequence-of-experiments question downstream of a population target; weakened-reference equivalence is an orbit of representations of one law and is not another level of observed information.

**Proof.** G1-1a gives the marginal/joint strictness. A's randomized three-block construction has Rademacher marginals and zero covariance at every nonzero lag, like iid Rademachers, but a nonzero consecutive third moment. C-3 gives identical fixed-anchor lag rows with different laws and physical descriptions. The final two assertions follow from the definitions in §2. **Status: PROVED INTERNALLY.**

### ID-1 — unique marginal-centre theorem

**Statement.** For (Q\in\mathcal P_2(M)), the law identifies the complete Fréchet minimizer set \(\mathfrak M(Q)\). If that set is a singleton, every admissible representation whose declared centre must be the unique Fréchet mean has that same centre. If the set is not a singleton, selecting one element needs an additional convention. Existence, uniqueness, and measurable/continuous dependence are separate hypotheses or theorems; completeness alone is not being used to supply them.

**Proof.** Proposition G1-0. The antipodal circle mixture in A/C supplies a nonunique boundary. **Status: PROVED INTERNALLY.**

### ID-2 — flat/Hilbert identified quotient

Let (X_t=Af_t+\delta_t) be centred and weakly stationary in a separable Hilbert space, with finite (r), injective (A), temporally uncorrelated \(\delta\), and both factor--noise cross-lag directions zero at every nonzero integer lag. Define
\[
\mathcal S_X=\overline{\operatorname{span}}
\{\operatorname{ran}\Gamma_X(h):h\in\mathbb Z\setminus\{0\}\}.
\]

**Statement.** Every admissible loading contains \(\mathcal S_X\). If (q=\dim\mathcal S_X<\infty), the minimum dynamic rank is (q), and every minimum representation has loading range exactly \(\mathcal S_X\). Two minimum loading maps differ by (R\in GL(q)), or by an orthogonal (R) after isometric normalization. Dynamically silent white variation in the loading span remains reallocable between factor and noise. On the declared centred jointly Gaussian minimum-representation class with iid Gaussian noise independent of the complete factor process, the complete observed-FDD quotient is exactly the loading gauge plus every lag-zero covariance reallocation (K) recorded in A (3.3)--(3.4) for which the complete proposed factor covariance sequence is positive definite and the residual noise covariance is positive trace class. Outside Gaussianity, those equations classify only second order.

A deterministic reference shift (d(u)) is absorbable with fixed (A) exactly when (d(u)\in\operatorname{ran}A), but the shifted factor must separately satisfy the declared centring/stationarity rules. If both reference curves are required to be the unique marginal mean, ID-1 forces the shift to vanish.

**Proof.** A2--A4. Complementary rank-deficient lags prove that one full-rank lag is not necessary; a dynamically silent iid coordinate proves the minimum-rank boundary is load-bearing. **Status: PROVED INTERNALLY on the stated second-order and Gaussian-FDD classes.**

### ID-3 — spectral persistence and single-path recovery theorem

**Statement.** For a centred square-integrable weakly stationary Hilbert process (Z_t), ordinary averages converge in (L^2) to the time-invariant projection (Z^{\rm inv}), whose squared (L^2) norm is the trace of the spectral atom at zero. Hence the mean is recovered pointwise in (L^2) if and only if (F_Z(\{0\})=0). For a local triangular-array window, the same statement holds under the explicit continuity, shrinking-window, and (L^2) frozen-process coupling in A6. The qualitative no-atom class admits no uniform consistent mean estimator: the Gaussian AR(1) two-point sequence with \(\rho_n=1-n^{-2}\) has bounded information for the mean. A sequence of nonzero-frequency atoms moving toward zero can also keep the ordinary average variance order one when its frequency is (o(1/n)), even though each fixed law has no atom at exactly zero.

**Proof.** A5--A7. The fixed-law convergence is the Hilbert mean-ergodic theorem, with the project application recorded exactly in the references ledger; the spectral dominated-convergence calculation and triangular-array transfer are internal. The AR(1) precision/KL/Pinsker argument proves non-uniformity. **Status: CITED EXTERNALLY AND APPLIED for the mean-ergodic producer; project-specific equivalence, transfer, and non-uniformity PROVED INTERNALLY.**

### ID-4 — curved base-point non-identification and exact repaired boundary

On compatible normal branches define \(\Phi_{x\to y}=\log_y\circ\operatorname{Exp}_x\), with domain \(D_{x\to y}=\operatorname{Exp}_x^{-1}(U)\). Three-chart composition is asserted only on a displayed triple overlap \(U_{xyz}\), with source domain \(D_x^{xyz}=\log_x(U_{xyz})\).

**Statement.** Under weakened centring, exact observation-law equality identifies the compatible-chart orbit
\[
\mathcal L_y=((\Phi_{x\to y})^{\mathbb Z})_\#\mathcal L_x,
\]
not a preferred reference. On one injective geodesic or one simply connected totally geodesic flat, \(\Phi\) is exact translation after the typed parallel identification and preserves an affine factor/noise representation. Generic fixed-rank preservation is false. On the finite reset-probe class, rank before and after reference change is the affine dimension of each finite support configuration and its image; therefore two-sided preservation for all probes is equivalent exactly to preservation of finite-subset affine dimension, not to ordinary affinity of \(\Phi\). B's bounded geometrically mixing (S^2) construction has a unique marginal Fréchet mean, common unique Log branches, rank one at the true centre, and rank two at an off-centre weakened reference. A cut-locus example proves the normal-branch restriction.

**Proof.** B1--B6, after A's foreign-audit repairs. Higher Jacobi expansions are bypassed because no exact consumer needs them. **Status: SHARPLY REFORMULATED AND PROVED; generic rigidity/fixed-rank preservation DISPROVED.**

### ID-5 — fixed-centre contamination theorem

Fix an anchor (c_0) and put (Z_{t,n}=\log_{c_0}X_{t,n}) on a declared common unique Log branch. Universally let (b_{t,n}=E Z_{t,n}) and (U_{t,n}=Z_{t,n}-b_{t,n}). In the moving-centre comparison below, (P_t:T_{\mu(u_t)}M\to T_{c_0}M) is parallel transport along the declared unique connector used by that same common branch.

**Statement.** The population fixed-anchor lag splits exactly as
\[
S_n(h)=D_{b,n}(h)+R_{U,n}(h),
\]
while the empirical row additionally contains both drift--residual cross products and centred residual-product sampling error. The score mean (b_{t,n}) is not automatically \(\log_{c_0}\mu(u_t)\).

If an exact one-fibre affine score model (Z=d+Af+e) is declared, multiplication gives nine population terms: (dd,df,de,fd,ff,fe,ed,ef,ee). The historical clean formula (D_d+A\Gamma_f(h)A^*) holds only under pointwise factor/noise centring, both factor--noise cross-lag zeros, and idiosyncratic whiteness at included lags. On a generic curved model recentered from \(\mu(u_t)\), the exact nonlinear remainder
\[
g_{t,n}=\Phi_{\mu(u_t)\to c_0}(V_{t,n})
-\log_{c_0}\mu(u_t)-P_tV_{t,n}
\]
and its three lag products must be retained; it vanishes on the common-flat exact reduction. Lipschitz drift yields a lag-invariant \(M_d\) plus the explicit \(O((h+1)/n)\) end term. The frozen-array coupling gives the displayed local-stationarity error, and no sampling rate is asserted without a dependence theorem.

For the clean finite-dimensional population row \(S_h=M+B_h\): aligned drift adds no outside direction but can change rank/eigenstructure; orthogonal drift produces the exact block sum \(h_0M^2\oplus\mathbb L_f\); under factor-complete lag contrasts, partial drift has row range \(E+D\) and adds exactly \(\dim P_{E^\perp}D\) dimensions. In a general Hilbert space the universal statement is the closed-range identity \(\overline{\operatorname{ran}\mathbb L}=\overline{\operatorname{ran}\mathcal G}\); the dimension formula is asserted only when \(E+D\) is finite-dimensional, and without contrast completeness cancellation is possible. The local-stationarity term uses C's process-level same-freeze coupling (or a direct pair-moment approximation), not merely separate own-time couplings. General cross/noise/geometry contamination perturbs the assembled operator by at most \(2\|\mathcal G_0\|\|\mathcal K\|+\|\mathcal K\|^2\), so subspace conclusions require the actual eigengap and exact rank conclusions require exact zeros or a declared threshold.

**Proof.** C §§4--5, subject to the foreign-audit closed-range/finite-dimensional repair. **Status: SHARPLY REFORMULATED AND PROVED.**

### ID-6 — scientific interpretation corollary

**Statement.** The parent (P2) uses one common marginal Fréchet mean and a factor model for its tangent residual; the surrounding definition treats the mean as unique when the minimizer is a singleton. Under a moving-centre truth fitted at one anchor, the lag output can superpose fixed-score drift, factor persistence, cross/noise terms, and nonlinear geometric remainder; it does not label their split. A moving-centre refit that changes the leading factor is sensitivity evidence unless the ID-2/ID-3/ID-4/ID-5 identifying assumptions are justified for that application. Nothing in P1-ID proves that the parent's empirical Factor 1 is spurious, drift-dominated, or erroneous. Dataset-specific dominance needs an identified decomposition plus estimation and uncertainty analysis.

**Proof.** Immediate from ID-0--ID-5 and the parent model equations/(P2). **Status: PROVED INTERNALLY.**

## 9. Two hostile passes and terminal adjudication

| Slot | Producer | Hostile Pass I | Hostile Pass II | Terminal disposition |
|---|---|---|---|---|
| ID-0/ID-1 | lead/A/C | information labels, Log/integrability scope, unique/nonunique/empty argmin split | all non-implications enumerated and source scopes locked | repaired, rechecked, and integrated |
| ID-2 | A | Gaussian scope, full-process independence, trace-class feasibility, signed-lag scope | minimum-representation qualifier and covariance-feasibility locks | repaired, rechecked, and integrated |
| ID-3 | A | pointwise versus uniform and absence of a rate | exact Doob hypothesis map, same-freeze transfer, and moving nonzero-frequency mass wording | repaired, rechecked, and integrated |
| ID-4 | B | triple-overlap typing and finite-subset dimension versus ordinary affinity | full score/observation support required on the geodesic/flat | repaired, rechecked, and integrated |
| ID-5 | C | closed-range/finite-rank scope and local-stationarity double-count risk | declared connector branch, two-index coupling, and range closure retained | repaired, rechecked, and integrated |
| ID-6 | C/lead | protection against component-dominance claims | parent-source wording narrowed to the common-mean specification and surrounding uniqueness convention | repaired, rechecked, and integrated |

No hostile counterexample defeated the terminal package. Generic curved reference rigidity and generic dynamic-rank invariance were instead disproved and replaced by the exact compatible-chart orbit plus the geodesic/flat and finite-subset boundaries. All seven theorem slots are terminal, every sustained objection has a recorded repair and foreign recheck, and the canonical result is [[P1-ID — centre-drift and factor identification boundary]].
