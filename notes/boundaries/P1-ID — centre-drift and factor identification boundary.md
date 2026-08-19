---
type: canonical-research-boundary
title: P1-ID — centre-drift and factor identification boundary
status: closed-theorem-package
verdict: unique marginal Fréchet centres are law-functionals on the deterministic-centre class; on the latent-stochastic-centre class the centre/factor split is a declared convention, not an identified object; reference-dependent rank inflation is universal in curvature; separation is recovered exactly by a declared frequency-band restriction that the three-scale estimator attains
last-audited: 2026-08-14
area:
  - identification
  - geometry
  - time-series
  - factor-models
---

# P1-ID — centre-drift and factor identification boundary

> **Canonical closed theorem boundary.** ID-0 through ID-10 are terminal, and the five ID-9 escape routes R1–R5 are individually terminal. Detailed proofs and hostile passes are archived under `Archived/Proof workstreams` in the P1-ID and P1-ID-CLOSE lead, A, B, and C dossiers. [[Analytical reconstruction — proof ledger and rebuilt spec]] governs programme-wide status.

> **Reading order for the two halves.** §§3–9 are the impossibility package (ID-0–ID-6). §§12–15 are the closure package (ID-7–ID-10): a constructive separation theorem, the curvature class of rank inflation, the sharpness verdict on the ID-1 gate, and the persistence window. The two halves meet at one place: **ID-3 says frequency zero is the failure locus; ID-7 says a declared band away from frequency zero is exactly what restores separation; ID-9 route R3 says such a declaration is unavoidable; ID-10 says how much persistence the estimator can absorb.** The scope locks in §4.1 and §5.1 are the corrections that the closure package forces on the impossibility package.

## 1. Gate 1 verdict

Part of the former curved question was misformulated. If a known marginal law \(Q_u\) has a unique Fréchet mean, that centre is a functional of \(Q_u\). Two representations of the same marginal cannot declare different points to be its unique Fréchet mean. Curvature affects existence, uniqueness, Log domains, and reference changes; it cannot create two unique minimizers of one fixed objective.

The nontrivial questions are:

1. the factor/loading/noise quotient after the centre is fixed;
2. recovery from one locally stationary path and its near-zero-frequency boundary;
3. the lag object produced by fixed-centre misspecification;
4. base-point changes when a reference is not required to be the unique marginal mean.

## 2. Information sets

| Label | Information | Equivalence | Identified target |
|---|---|---|---|
| \(\mathcal I_M\) | every marginal \(Q_u\) | equality of each \(Q_u\) | unique mean or minimizer set |
| \(\mathcal I_J\) | full time-series law | equality of every FDD | marginal functionals and a declared latent quotient |
| \(\mathcal I_1\) | one triangular-array path | equality/contiguity of experiments when stated | recoverability of a prior population target |
| \(\mathcal I_F(c_0)\) | fixed-anchor lag row/operator | equality of the declared lag functional | contaminated row/operator only |
| \(\mathcal I_R\) | weakened reference model | compatible-chart change plus factor gauge | orbit of reference representations |

## 3. ID-0 — information-set separation

**Theorem ID-0.** When lag functionals are measurable and integrable and each Log is single-valued on its declared almost-sure support:

- \(\mathcal I_J\) determines \(\mathcal I_M\) and every such lag functional.
- \(\mathcal I_M\not\Rightarrow\mathcal I_J\): an iid \(Q\)-process and a time-constant \(Z\sim Q\) process have equal marginals and different two-time laws.
- A lag row determines neither marginals nor FDDs. Deterministic fixed-anchor drift and an invariant random factor can have the same uncentred lag row but different laws.
- Even all marginals and covariance lags do not determine non-Gaussian FDDs. The archived stationary Rademacher three-block process matches iid Rademachers at every covariance lag but has a different consecutive third moment.
- One-path recovery is a statistical experiment, not another population equivalence. Weakened-reference equivalence is an orbit inside one observation law.

**Status: PROVED INTERNALLY.**

## 4. ID-1 — unique marginal centre

For \(Q\in\mathcal P_2(M)\), let

\[
F_Q(x)=\int d(x,z)^2Q(dz),\qquad
\mathfrak M(Q)=\operatorname*{argmin}_xF_Q(x).
\]

**Theorem ID-1.** If \(\mathfrak M(Q)\) is nonempty, the law identifies that set. If it is \(\{m_Q\}\), every admissible representation whose centre must be the unique Fréchet mean has centre \(m_Q\). A nonempty nonsingleton set needs a selection convention. An empty argmin means no centre exists in this class.

**Proof.** Equal laws give the same objective and argmin. A singleton forces equality; a nonsingleton objective contains no selector. \(\square\)

The antipodal two-point law on \(S^1\) proves the nonunique boundary. Existence, selection, and continuity are separate hypotheses or theorems.

**Status: PROVED INTERNALLY; the former curved necessity target is SHARPLY REFORMULATED.**

### 4.1 Scope lock ID-1-L (forced by ID-9 route R3)

ID-1 is **true as stated and non-binding outside the deterministic-centre class**. Let \(\mathrm D\) be the class of models whose declared centre is a deterministic function of rescaled time, and let \(\mathrm{LC}\) be the latent-stochastic-centre class \(X_t=\operatorname{Exp}_{C_t}[\cdots]\) with \(C_t\) random and adapted.

A centre convention binds a model only if it is a **functional of the declared information set**. A random \(C_u\) is not a functional of any of \(\mathcal I_M,\mathcal I_J,\mathcal I_1,\mathcal I_F,\mathcal I_R\): every \(M\)-valued functional of a law is a fixed point, hence deterministic. Therefore no model in \(\mathrm{LC}\setminus\mathrm D\) satisfies ID-1's antecedent, and ID-1 constrains nothing there. The gate contains no false theorem; its reach is smaller than the project needs. §14 states the sharpness verdict and §14.3 the exact replacement over \(\mathrm{LC}\).

Two consequences are recorded here because they are easy to misread:

1. Even on \(\mathrm D\), what ID-1 pins in a mixture model is \(\mathbb EC_u\), not the realised centre path. In a Hilbert space with \(\mathbb E[\xi\mid C]=0\), \(\mathfrak M(Q_u)=\{\mathbb EC_u\}\), which equals \(C_u\) only when \(C_u\) is a.s. constant.
2. In curvature the marginal Fréchet mean of a mixture is not even the Fréchet mean of the mixing-centre law. §14.3 records the exact \(H^2\) counterexample and its flat vanishing.

**Status of the lock: PROVED INTERNALLY.**

## 5. ID-2 — flat/Hilbert equivalence class

Let \(X_t=Af_t+\delta_t\) be centred and weakly stationary in a real separable Hilbert space \(H\). Assume finite \(r\), injective \(A:\mathbb R^r\to H\), temporally uncorrelated \(\delta\), and both factor–noise cross-lag directions zero for every nonzero integer lag. Define

\[
\mathcal S_X=\overline{\operatorname{span}}
\{\operatorname{ran}\Gamma_X(h):h\in\mathbb Z\setminus\{0\}\}.
\]

**Theorem ID-2.** If \(q=\dim\mathcal S_X<\infty\):

1. every admissible loading contains \(\mathcal S_X\);
2. minimum dynamic rank is \(q\), and every minimum loading range equals \(\mathcal S_X\);
3. minimum loading maps differ by \(R\in GL(q)\), or orthogonal \(R\) after isometric normalization;
4. dynamically white variation in the loading span remains reallocable between factor and noise.

This follows from

\[
\Gamma_X(h)=A\Gamma_f(h)A^*,\quad h\ne0,\qquad
\mathcal S_X=A\operatorname{span}_{h\ne0}\operatorname{ran}\Gamma_f(h).
\]

On the centred jointly Gaussian *minimum-representation* class with iid Gaussian noise independent of the complete factor process, the exact FDD quotient is the loading gauge plus every feasible lag-zero allocation:

\[
\Gamma_g(h)=R^{-1}\Gamma_f(h)R^{-*},\quad h\ne0,
\]
\[
\Gamma_g(0)=R^{-1}\Gamma_f(0)R^{-*}+K,\qquad
D_\varepsilon=D_\delta-ARKR^*A^*,
\]

where the proposed factor covariance sequence is positive definite and \(D_\varepsilon\) is positive trace class. Outside Gaussianity this classifies second order only.

A deterministic reference shift is absorbable with fixed \(A\) exactly when it lies in \(\operatorname{ran}A\), subject to the declared factor centring/stationarity. If both references must be the unique marginal mean, ID-1 makes the shift zero. A random invariant component cannot become a deterministic centre.

Complementary deficient lags show one full-rank lag is not necessary. An iid loaded coordinate proves why minimum rank is load-bearing. Colored idiosyncratic noise destroys persistent factor/noise separation.

**Status: PROVED INTERNALLY** on the displayed second-order and Gaussian-FDD classes.

### 5.1 Scope lock ID-2-L — what "loading" means (forced by ID-9 route R3)

ID-2's \(A\) is the **total dynamic loading**, not a factor-only loading. ID-2 assumes \(\delta\) is temporally uncorrelated. A serially dependent latent centre cannot be placed in \(\delta\) without violating that hypothesis, so in ID-2's own vocabulary such a centre must be absorbed into \(A\). ID-2 is therefore **true on its declared class and non-binding on \(\mathrm{LC}\)**, exactly as ID-1 is; it is not contradicted by any latent-centre construction.

The decisive test, on the archived \(\mathbb R^3\) witness: three independent AR(1) coordinates \(z_1,z_2,z_3\). Model 1 declares centre \(z_1e_1\) and loading range \(\operatorname{span}\{e_2,e_3\}\); Model 2 declares centre \(z_3e_3\) and loading range \(\operatorname{span}\{e_1,e_2\}\). The two loading ranges are incomparable, the centre processes differ, and the two models generate the **same process**, hence share every finite-dimensional distribution. Neither declared \(\delta\) is temporally uncorrelated, so neither is an ID-2 representation; the common ID-2 representation is \(A=I_3\), \(f=(z_1,z_2,z_3)\), \(\delta=0\), for which \(\operatorname{ran}A=\mathbb R^3\supseteq\mathcal S_X\) and ID-2 holds.

What fails is one level down and it is the load-bearing fact:

> **The decomposition of ID-2's identified total dynamic loading into a centre part and a factor part is not identified, even from \(\mathcal I_J\).**

This is continuous with ID-0, which already separates deterministic fixed-anchor drift from an invariant random factor sharing one lag row. §14.3 gives the exact surviving quotient and §12 the restriction that removes the ambiguity.

**Status of the lock: PROVED INTERNALLY.**

## 6. ID-3 — spectral persistence and one-path recovery

**Theorem ID-3.** For a centred square-integrable weakly stationary Hilbert process \(Z_t\), ordinary averages converge in \(L^2\) to the invariant projection \(Z^{\rm inv}\), with

\[
\mathbb E\|Z^{\rm inv}\|^2=\operatorname{tr}F_Z(\{0\}).
\]

Hence the averages converge to zero exactly when \(F_Z(\{0\})=0\). A local triangular-array window has the same pointwise conclusion under the shrinking-window, mean-continuity, and \(L^2\) frozen-process coupling in P1-ID-A §7.

This is not uniform over the qualitative no-atom class. For Gaussian AR(1) observations with unknown mean, unit marginal variance, and \(\rho_n=1-n^{-2}\),

\[
\mathbf1^T\Sigma_{\rho_n}^{-1}\mathbf1
=\frac{n(1-\rho_n)+2\rho_n}{1+\rho_n}\le\frac32.
\]

A two-point KL/Pinsker argument gives fixed positive minimax risk. A sequence of nonzero-frequency atoms moving toward zero at \(o(1/n)\) likewise leaves ordinary-average variance order one although no fixed law has an atom at zero.

**Status:** mean-square ergodic producer **CITED EXTERNALLY AND APPLIED** from Doob (1953), Chapter X §7; spectral application, local transfer, AR(1) impossibility, and near-zero example **PROVED INTERNALLY**. Exact hypothesis mapping is in [[References and external claim audit]].

## 7. ID-4 — curved reference orbit

On compatible normal branches and \(U\subset N_x\cap N_y\), define

\[
D_{x\to y}=\operatorname{Exp}_x^{-1}(U),\qquad
\Phi_{x\to y}(v)=\log_y(\operatorname{Exp}_xv).
\]

Three-chart composition is asserted only on a displayed \(U_{xyz}\), with source \(D_x^{xyz}=\log_x(U_{xyz})\). Parallel transport is inserted before fibre comparisons.

**Theorem ID-4.** A weakened-reference model identifies the compatible-chart orbit

\[
\mathcal L_y=((\Phi_{x\to y})^{\mathbb Z})_\#\mathcal L_x,
\]

not a preferred reference. If the complete score/observation support and both references lie on one injective geodesic, or in one simply connected totally geodesic flat, \(\Phi\) is exact translation after typed parallel identification and preserves the affine factor/noise representation.

Generic fixed-rank preservation is false. On finite reset probes, dynamic rank equals the affine dimension of the support configuration before and after \(\Phi\). Universal probe-rank preservation is therefore equivalent to finite-subset affine-dimension preservation, which is weaker than ordinary affinity.

On \(S^2\), a bounded geometrically mixing three-state process has unique marginal mean \(x=(0,0,1)\), minimum rank one at \(x\), and minimum rank two at \(y=(1,0,0)\), because

\[
\Phi_{x\to y}(te_2)=\frac\pi2\{-\cos(t)E_1+\sin(t)E_2\}
\]

maps \(-b,0,b\) to non-collinear points. All Logs are unique, persistence is ordinary, and noise is zero. Curvature-induced nonlinearity causes the failure. An antipodal example proves the normal-branch boundary.

Higher Jacobi expansions are **SUPERSEDED/BYPASSED** because no exact consumer needs them.

**Status: SHARPLY REFORMULATED AND PROVED; generic rigidity and fixed-rank invariance DISPROVED.**

## 8. ID-5 — fixed-centre contamination

Fix an anchor \(c_0\) and a common unique Log branch. Put

\[
Z_{t,n}=\log_{c_0}X_{t,n},\quad
b_{t,n}=\mathbb EZ_{t,n},\quad
U_{t,n}=Z_{t,n}-b_{t,n}.
\]

Universally,

\[
S_n(h)=D_{b,n}(h)+R_{U,n}(h),
\]

while the empirical row also contains both drift–residual cross products and centred residual-product sampling error. The score mean \(b_{t,n}\) is not automatically \(\log_{c_0}\mu(u_t)\) in curvature.

If an exact one-fibre model \(Z=d+Af+e\) is declared, multiplication gives all nine population terms:

\[
dd,\ df,\ de,\ fd,\ ff,\ fe,\ ed,\ ef,\ ee.
\]

The clean formula \(S_n(h)=D_{d,n}(h)+A\Gamma_{f,n}(h)A^*\) holds only under pointwise factor/noise centring, both factor–noise cross-lag zeros, and idiosyncratic whiteness at each included lag.

For a curved moving-centre truth, let \(P_t:T_{\mu(u_t)}M\to T_{c_0}M\) be transport along the declared unique connector and \(V_{t,n}=\log_{\mu(u_t)}X_{t,n}\). The exact remainder

\[
g_{t,n}=\Phi_{\mu(u_t)\to c_0}(V_{t,n})
-\log_{c_0}\mu(u_t)-P_tV_{t,n}
\]

and its three lag products must be retained. It vanishes on a common flat but is not generically white. Lipschitz drift gives a lag-invariant \(M_d\) plus explicit \(O((h+1)/n)\) end error. Local stationarity uses a process-level same-freeze coupling or direct pair-moment approximation; sampling error has no rate without a dependence theorem.

For clean finite-dimensional \(S_h=M+B_h\):

- aligned drift adds no outside direction but can change rank/eigenstructure;
- orthogonal drift yields \(h_0M^2\oplus\mathbb L_f\);
- under factor-complete lag contrasts, partial drift has range \(E+D\) and adds \(\dim P_{E^\perp}D\) directions;
- otherwise cancellation is possible.

In a general Hilbert space,

\[
\overline{\operatorname{ran}\mathbb L}
=\overline{\operatorname{ran}\mathcal G}
=\overline{\operatorname{span}}_h\operatorname{ran}S_h.
\]

Dimension formulas require finite-dimensional \(E+D\). For stacked contamination \(\mathcal K\),

\[
\|\mathbb L-\mathbb L_0\|
\le2\|\mathcal G_0\|\,\|\mathcal K\|+\|\mathcal K\|^2.
\]

Eigenspace claims require the actual eigengap; exact rank claims require exact zeros or a threshold. Summable factor lags saturate while repeated drift contributes \(h_0M_d^2\), but near-zero factors can appear lag-invariant over finite lags.

**Status: SHARPLY REFORMULATED AND PROVED.** The old additive formula without cross/geometry conditions is superseded.

## 9. ID-6 — scientific interpretation

The parent (P2) requires the Fréchet mean of each marginal law to exist and equal the same \(\mu\); the surrounding definition treats the Fréchet mean as a unique minimizer.

> Under fixed-centre misspecification, the fitted lag row can superpose fixed-score drift, persistent factors, cross/noise terms, end/local-stationarity error, and nonlinear geometry. It does not report their split.

A moving-centre refit that changes the leading direction is sensitivity evidence unless the application justifies ID-2 through ID-5. Nothing here implies that the parent's empirical Factor 1 is spurious, drift-dominated, or erroneous. Dataset-specific dominance needs an identified decomposition plus estimation and uncertainty analysis.

**Status: PROVED INTERNALLY.**

## 10. What existing Paper 1 machinery estimates

HD1, HE, FRAME-2P-U, and the scoped BW packages retain their separately adjudicated estimation rates and assumption packages. They estimate the moving-centre/loading target after the centre convention and included-lag target have been fixed:

- unique pointwise Fréchet means define the population centre path — here **by construction**, since \(\mu_n(u)\) is defined as the Fréchet mean of the marginal \(Q_u\) and no minimisation over centre *paths* is ever posed. (In the flow-datum setting, where the objective **is** posed over whole paths, the corresponding reduction to pointwise barycentres is a theorem: Santoro & Panaretos, arXiv:2310.13764v2, Lemma 1. It is cited here as a **comparison**, not consumed as a producer. Their object, the *Fréchet mean flow*, is estimated from i.i.d. replicate flows; this file's centre path is estimated from a single dependent path — see [[Literature review — external positioning and prior art]] §2.2.) The existence and uniqueness of each pointwise mean is **now split by geometry**. On Bures–Wasserstein it is automatic for every law charging the full-rank cone (§14.2 R1, R2). On spheres and sphere products it can fail, and where it fails no continuous selection exists and any single-valued convention injects the lag-invariant contamination of §14.2. On the latent-stochastic-centre class the phrase has no referent at all (§4.1);
- exact included-lag orthogonal-white factorisation plus minimum rank defines the selected-lag dynamic span up to gauge — with "loading" meaning the **total dynamic loading** (§5.1); the centre/factor sub-split additionally requires the declared band separation of §14.3(v);
- weakened references are reference-dependent unless ID-4's boundary is justified — and by §13 that boundary is *flatness*, so in AIRM, BW and spheres a reference change generically changes dynamic rank;
- a fixed-centre fit targets the contaminated row unless ID-5 terms are removed or budgeted;
- the persistence the estimator can absorb is bounded by §15: \(d=0\) for the headline rate, \(d<\tfrac12\) for consistency, \(\theta<1\) in the near-unit-root parameterisation.

P1-ID changes interpretation, not the established rate algebra — with one exception now recorded: ID-10 replaces \(\ell_n\)'s stochastic term by \(\psi^+(nb_n)\), which is an identity under HD-M and a strictly slower rate outside it.

## 11. Failure boundaries and closure evidence

The analytic suite covers equal marginals/different laws; equal marginals and all covariance lags/different FDDs; nonunique means; cut loci; invariant and near-zero persistence; white factor/noise reallocation; one-sided cross-lag failure; complementary lag ranks; selected-lag cancellation; and exact curved rank inflation. Each construction verifies its manifold, metric, law, centre, support, loading/noise, dependence, observational equality, and failure mechanism in the archived dossiers.

Workstream A proved ID-0–ID-3, B proved ID-4, and C proved ID-5–ID-6 and eleven hostile examples. A audited B and C; B audited A and C; C attacked the complete package. Every sustained objection was repaired and rechecked. Hostile Pass II attacked the integrated package and all final scope locks appear above.

Proof and adjudication provenance is archived in [[P1-ID — lead definition and dependency ledger]], [[P1-ID-A — flat classification and spectral persistence]], [[P1-ID-B — curved reference change and rigidity]], and [[P1-ID-C — hostile counterexamples and contamination audit]]. These are proof records, not parallel status authorities.

Every ID-0–ID-6 node has a terminal proved, sharply reformulated, disproved, superseded, or cited-and-applied disposition; none is deferred. §15 records the closure evidence for ID-7–ID-10 and the complete external-producer list.

## 12. ID-7 — constructive separation

ID-0–ID-6 is an impossibility package. ID-7 is its constructive companion, and it lives exactly where ID-3 says it must: away from frequency zero.

### 12.1 The modulus

For the frozen tangent process \(\{Z^{(u)}_t\}\) at rescaled time \(u\) — centred, square-integrable, weakly stationary in the tangent Hilbert space — define the **ergodic-average modulus** and its one-sided majorant

\[
\psi_u(N)=\Big\|\tfrac1N\sum_{t=1}^NZ^{(u)}_t\Big\|_{L^2},
\qquad
\psi^+(N)=\sup_u\Big\{N^{-2}\sum_{s,t\le N}\big|\operatorname{tr}\Gamma_u(s-t)\big|\Big\}^{1/2}.
\]

\(\psi_u(N)^2=\int\|D_N\|^2d\nu_u\) exactly, so ID-3's dichotomy reads \(\psi_u(N)\to0\iff\nu_u(\{0\})=0\), pointwise and not uniformly. The exact evaluations are:

| Frozen factor law | \(\psi(N)\) |
|---|---|
| Hilbert AR(1), coefficient \(\rho\), unit marginal variance | \(\psi(N)^2=N^{-2}\big[N\frac{1+\rho}{1-\rho}-\frac{2\rho(1-\rho^N)}{(1-\rho)^2}\big]\) |
| the same, in the near-unit-root limit \(x=N(1-\rho)\) fixed | \(\psi(N)^2\to\Psi(x)=\dfrac{2(x-1+e^{-x})}{x^2}\), \(\Psi(0^+)=1\), \(\Psi(x)\sim2/x\) |
| \(m_0\)-dependent (HD-M baseline) | \(\psi(N)\le\sqrt{(2m_0+1)R^2/N}\); two-sided \(\asymp N^{-1/2}\) **iff** \(\Lambda_u=\sum_h\operatorname{tr}\Gamma_u(h)>0\) |
| summable Hilbert physical dependence (HD-L, T-APP-4) | \(\psi(N)\le\Delta_2N^{-1/2}\) |
| long memory, \(\operatorname{tr}\Gamma_u(h)\asymp c_\gamma|h|^{2d-1}\), \(d\in(0,\tfrac12)\) | \(\psi_u(N)^2=\dfrac{c_\gamma(u)}{d(2d+1)}N^{-(1-2d)}\{1+o(1)\}\) |

The unconditional claim \(\psi(N)\asymp N^{-1/2}\) under \(m_0\)-dependence is **false**: \(Z_t=e_t-e_{t-1}\) has \(\Lambda=0\) and \(\psi(N)=\sqrt2/N\). The upper bound always holds, which is the direction every consumer uses.

### 12.2 Where the modulus enters the estimator

This is the load-bearing step, and it is about the project's own three-scale estimator, not an abstract smoother.

**Lemma ID-7-W.** For nonnegative weights with \(\sum_tw_t=1\) and \(\max_tw_t\le C_2/N\) supported on a window of length \(N\), \(\|\sum_tw_t\xi_t\|_{L^2}\le C_2\,\psi^+(N)\), with a matching lower bound of order \(\psi(N)\) when \(\operatorname{tr}\Gamma\ge0\) and is regularly varying. The three kernel scales \(c=(1,\tfrac12,\tfrac14)\) have different effective windows and the narrowest, \(c_3=\tfrac14\), sets the modulus.

**Consequence.** Replacing HD1's stochastic term by the modulus gives

\[
\ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1},
\]

and \(\psi^+(nb_n)\) sits **exactly where \((nb_n)^{-1/2}\) sits in \(\ell_n\), and nowhere else in the mean channel**. Under HD-M this reduces to HD1's \(\ell_n\) verbatim. G1-HD-L2, GRID, Theorem PF, OBS, P1-ROW, P1-OP, EV and the Davis–Kahan step all propagate with \(\ell_n\mapsto\ell_n(\psi)\); the bias channel \(b_n^3\) is untouched.

Two honest costs are recorded rather than hidden. First, HD1's weighted Hilbert inequality splits an \(m_0\)-dependent row into \(m_0+1\) independent residue classes; that device has **no long-memory analogue** and is DISPROVED as available for \(d>0\). Second, the optional sup-norm results G1-HD and HD-Minf do not survive long memory. Neither is consumed by Theorem HD-E, so both are SEPARATED with the no-consumer argument, but the separation is displayed, not assumed. Under a Gaussian factor with \(|\gamma_f(h)|\le C(1+|h|)^{2d-1}\) the oracle row degrades to \(d_{\mathrm{or},n}=O_p(n^{-1/2}+n^{-(1-2d)})\), with the classical \(n^{-1/2}\sqrt{\log n}\) boundary at \(d=\tfrac14\); it remains strictly dominated by \(\ell_n(\psi)\) at every re-optimised bandwidth.

### 12.3 The theorem

> **Theorem ID-7 (constructive separation).** Assume
> **(S1)** the declared centre path is a deterministic \(C^3\) function of rescaled time with uniformly bounded derivatives;
> **(S2)** the frozen tangent factor is weakly stationary with modulus \(\psi^+\), and **(S2b)** its frozen law is Hölder in \(u\);
> **(S3)** HD-M2 local stationarity with exponent \(a\);
> **(S4)** ID-2's conditions hold at each frozen \(u\) — temporally white \(\delta\), both factor–noise cross-lag directions zero at every included nonzero lag, and minimum dynamic rank;
> **(S5)** HD-K together with \(\psi^+(nb_n)=o(1)\).
> Then the centre path and the loading space are **separately identified from \(\mathcal I_J\)** and **separately estimable**, with mean error \(\ell_n(\psi)\) and loading error \(O_p\big((d_{\mathrm{or},n}+\ell_n(\psi))/\Delta_n\big)\).

(S2b) is more than HD1 assumes as written and is declared as new, with its boundary reason: without Hölder continuity of the frozen law the same-freeze coupling in ID-3's local transfer has no modulus and the window average has no target.

**What ID-7 buys.** Identification alone follows from ID-1 plus ID-2 given (S1) and is nearly vacuous. The content is the **quantitative, sample-size-indexed** replacement for ID-3's non-uniform predicate: ID-3 says recovery holds pointwise in \(u\) and fails uniformly; ID-7 says the exact price of persistence is \(\psi^+(nb_n)\) in the estimator the project actually uses.

### 12.4 Sharpness — the positive theorem and the impossibility meet with no gap

Both sides are functions of the **same scalar** \(x_n=(1-\rho_n)nb_n\):

\[
\text{achievable: }\psi^2\to\Psi(x)=\frac{2(x-1+e^{-x})}{x^2},
\qquad
\text{information: }\mathbf1^\top\Sigma_{\rho}^{-1}\mathbf1=\frac{x+2\rho}{1+\rho}.
\]

ID-7 holds iff \(x_n\to\infty\); ID-3's floor bites iff \(x_n=O(1)\). There is no intermediate regime. ID-3's construction \(\rho_n=1-n^{-2}\) has \(x_n=b_n/n\to0\), missing the separation boundary by a factor \(n^{8/7}\) at \(b_n=n^{-1/7}\) — far outside, and far outside HD-M/HD-K/HD-L as well.

**Status: PROVED INTERNALLY.** The mean-ergodic producer is Doob, cited and mapped in [[References and external claim audit]]; the local-stationarity mode is Dahlhaus–Richter–Wu Assumption 2.1; every rate and every modulus evaluation is internal.

## 13. ID-8 — reference-dependent rank is a curvature phenomenon, not a cut-locus artefact

ID-4 disproved generic fixed-rank preservation with an \(S^2\) construction. \(S^2\) is positively curved with a cut locus, and the project's applications are AIRM (Hadamard, no cut locus) and Bures–Wasserstein (nonnegatively curved, no cut locus between full-rank points). ID-8 settles every geometry the project uses.

### 13.1 The universal criterion

Let \(w=\log_yx\), let \(P:T_xM\to T_yM\) be parallel transport along the connecting geodesic, and let \(c(t)=\log_y\operatorname{Exp}_x(tV)\). The Gavrilov–Pennec expansion — Pennec (2019), Theorem 2, recorded as C-AUDIT-5 and confirmed verbatim against the primary source, with \(O(4)\) meaning total order jointly in both arguments — gives

\[
c(t)=w+t\Big[PV+\tfrac16R(PV,w)w\Big]+t^2\cdot\tfrac13R(PV,w)PV+O(t^3).
\]

The three probe points \(t=-b,0,b\) satisfy

\[
\big(c(b)-c(0)\big)\wedge\big(c(-b)-c(0)\big)=b^3\,c'(0)\wedge c''(0)+O(b^4),
\]

so collinearity fails iff \(c'(0)\wedge c''(0)\ne0\). By the curvature symmetry \(R(X,Y,Z,W)=-R(X,Y,W,Z)\) we have \(\langle R(PV,w)PV,PV\rangle=0\) **exactly**, so the quadratic coefficient is exactly transverse to \(PV\), while \(c'(0)=PV+O(\|w\|^2)\).

> **Theorem ID-8.** For \(\|w\|\) small and nonzero, the affine dimension of a three-point geodesic probe configuration is \(1\) at base \(x\) and \(2\) at base \(y\) whenever \(R(PV,w)PV\ne0\). Nonzero sectional curvature of \(\operatorname{span}\{PV,w\}\) is **sufficient** for this and is not necessary. Conversely, preservation of affine dimension for all small probes forces \(R(PV,w)PV=0\) for every \(V\), i.e. vanishing sectional curvature on every plane containing \(w\).

Rank inflation is therefore **curvature-specific and universal in curvature** — not cut-locus-specific, not compactness-specific, not sign-specific. ID-4's hedge that the failure was curvature-specific "in that construction" is retired.

### 13.2 Verdict by geometry, each with its own exact construction

| Geometry | Verdict | Exact witness |
|---|---|---|
| general Riemannian, nonzero curvature | **rank inflates** | Theorem ID-8 |
| Hadamard, \(H^2\) | **rank inflates, globally and exactly** | \(x,y\) at distance \(d\), \(\gamma\perp xy\) at \(x\): collinearity requires \(\rho\cos\theta=d\), but \(\cosh\rho=\cosh d\cosh b\) and \(\cos\theta=\tanh d/\tanh\rho\) give \(\rho\cos\theta-d=\tanh d\,(\rho/\tanh\rho)-d>0\) for every \(d>0,b\ne0\); \(\frac{d}{d\rho}\big[\rho\tanh d/\tanh\rho\big]_{\rho=d}=1-2d/\sinh2d>0\). No cut locus, no restriction on \(b\) |
| AIRM \({\rm SPD}(m)\), \(m\ge2\) | **rank inflates** | direct \({\rm SPD}(2)\) computation, and independently the totally geodesic \(H^2\hookrightarrow({\rm SPD}(2),\text{AIRM})\) with curvature \(-1/2\) derived rather than cited; block embedding lifts it to every \(m\ge2\) |
| Bures–Wasserstein \({\rm SPD}(m)\), full rank, noncommuting | **rank inflates, exactly in \(b\)** | \(y=I\), \(x=\operatorname{diag}(a,1)\), \(V=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\). Since \(\operatorname{Log}_I(B)=2(B^{1/2}-I)\) is affine in \(B^{1/2}\), collinearity \(\iff W=Y^2\) where \(\gamma(t)=x+tV+t^2W\), \(W=LxL\), \(Lx+xL=V\), and \(Yx^{1/2}+x^{1/2}Y=V\). Exactly, \(L=\frac{V}{1+a}\), \(W=\frac{\operatorname{diag}(1,a)}{(1+a)^2}\), \(Y=\frac{V}{1+\sqrt a}\), \(Y^2=\frac{I}{(1+\sqrt a)^2}\), so \(W\ne Y^2\) for every \(a\ne1\). Admissible range \(0<|b|<1+a\) from \(I+bL\succ0\) |
| BW, diagonal / fixed common eigenbasis | **rigid — rank preserved exactly** | \(Vx=xV\) gives \(\gamma(t)^{1/2}=x^{1/2}+\tfrac12tVx^{-1/2}\) exactly, so \(\operatorname{Log}_I\gamma(t)\) is exactly affine. The subcone is isometric to a Euclidean orthant under \(A\mapsto A^{1/2}\) |
| sphere and sphere products (parent's simulations) | **rank inflates** | ID-4's \(S^2\) construction |

The only rigid branches are the flat ones: a common injective geodesic, a totally geodesic flat, and the fixed-eigenbasis BW orthant. This exactly matches — and now explains — ID-4's positive statement.

### 13.3 What it means for the applications

Any moving-reference or changed-convention refit changes dynamic rank **by theorem** in every geometry the project uses. APP-FIN's realised covariance matrices are noncommuting and therefore squarely in the non-rigid class. A refit that reports a different factor count is not evidence about the data; it may be pure geometry. This is the precise sense in which a reference change is not a robustness check.

**Status: PROVED INTERNALLY**, with the Gavrilov–Pennec expansion **CITED EXTERNALLY AND APPLIED**.

## 14. ID-9 — the assault on the ID-1 gate

### 14.1 Verdict

**The gate stands as a theorem and fails as a closure of the identification question.** It is true, elementary, and correct; it is also non-binding on the class the flagship application most plausibly inhabits. Four of the five escape routes close in the gate's favour, exactly and with proof. The fifth — the latent stochastic centre — is a genuine crack, and it is the one that changes what the paper claims.

The classification that organises the routes is a trichotomy, and it is exhaustive by construction. A centre convention \(c\) either factors through the information map \(\iota\) or it does not. If it factors and is single-valued, it is pinned — this is pure set theory, and measurability is irrelevant to *pinning* (only to usability). If it factors but the defining argmin is empty or nonsingleton, that is escape **E1**. If it does not factor at all, that is escape **E2**. Routes R1 and R2 probe E1; R3 is E2; R4 proves it is not an escape; R5 is estimation. **There is no sixth route.** The content of ID-9 is entirely in the case analysis below, not in the trichotomy.

### 14.2 Routes R1, R2 — existence and uniqueness

**R1 — existence. The predicted counterexample does not exist. DISPROVED (as a failure mode).**

\(F_Q(A)=\int d_{\rm BW}(A,\Sigma)^2Q(d\Sigma)\) is continuous and coercive on \({\rm PSD}(m)\), which is proper under \(d_{\rm BW}\), so the argmin is nonempty whenever \(\int\operatorname{tr}\Sigma\,dQ<\infty\). No minimiser is rank-deficient when \(Q\) charges the full-rank cone. Writing \(G(A)=\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}=\|A^{1/2}\Sigma^{1/2}\|_*\) and taking \(\bar\Sigma\) singular, \(v\in\ker\bar\Sigma\) a unit vector, \(A_\varepsilon=\bar\Sigma+\varepsilon vv^\top\) (so \(A_\varepsilon^{1/2}=\bar\Sigma^{1/2}+\sqrt\varepsilon\,vv^\top\) exactly), a nuclear-norm dual certificate \(Z=Z_0+v\hat n^\top\) gives the **exact one-sided bound**

\[
G(A_\varepsilon)-G(\bar\Sigma)\ \ge\ \sqrt{\varepsilon\,s(\Sigma)},
\qquad
s(\Sigma)=\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12},
\]

the Schur complement in the \(\operatorname{ran}\bar\Sigma\oplus\ker\bar\Sigma\) splitting. The certificate has operator norm exactly one because \(v\perp\operatorname{ran}X_0\) automatically and \(\hat n\perp\operatorname{ran}X_0^\top\) by construction. Hence \(F_Q(A_\varepsilon)-F_Q(\bar\Sigma)\le\varepsilon-2\sqrt\varepsilon\int\sqrt s\,dQ<0\): no remainder, no integrability side condition, arbitrary corank.

**Consequence for the flagship geometry.** The BW Fréchet mean of any law charging the open cone exists **in the open cone**. ID-1's nonemptiness hypothesis is automatic on BW, and BW's genuine boundary remains rank loss for geodesics and logarithms, not mean existence.

**R2 — uniqueness. Splits by geometry; the selector is the crack. CITED EXTERNALLY on BW (see the boxed attribution below); the selector cost is PROVED INTERNALLY.**

> **Attribution (C-AUDIT-11).** The BW uniqueness conclusion below is **not internal**. It is established by **Kroshnin, Spokoiny & Suvorikova, *Ann. Appl. Probab.* 31(3) (2021), 1264–1298, Theorem 2.1** (finite-dimensional population case, minimal conditions) and by **Santoro & Panaretos, arXiv:2305.15592v3, Theorem 1**, which proves on a general separable Hilbert space that a BW Fréchet mean exists **iff** \(\mathbb E\|\Sigma\|_1<\infty\) and is unique under \(\mathbb P\{\Sigma\succ0\}>0\) — the same regularity hypothesis used here, on a strictly larger space, with the existence half proved as an equivalence. The empirical case is **Masarotto, Panaretos & Zemel, *Sankhya A* 81(1) (2019), Corollary 9 and Proposition 10**, the latter supplying the linear-structure convexity inequality. Santoro–Panaretos further note the regularity hypothesis is **not necessary**, with the counterexample \(\Sigma=\operatorname{diag}(W,0)\), \(W\sim\chi^2_1\) on \(\mathbb R^2\). The former claim of a strict extension was benchmarked against Agueh–Carlier, which was never the state of the art for the BW population barycentre; that benchmark, not the derivation, was the error. **The argument retained below is correct and is kept as an appendix remark: a self-contained elementary derivation of the one convexity step Santoro–Panaretos import from MPZ Proposition 10. It is an alternative route, not a new result.** Nothing downstream changes — R2's load-bearing content in this file is the selector cost, and R3, R5, ID-7 and ID-8 are untouched.

*On BW the gate applies — appendix remark, elementary route to a cited result.* \(F_Q\) is convex in the **ordinary linear structure** on \({\rm PSD}(m)\), despite BW being nonnegatively curved, because

\[
\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}
=\tfrac12\inf_{T\succ0}\big[\operatorname{tr}TA+\operatorname{tr}T^{-1}\Sigma\big]
\]

exhibits \(G\) as an infimum of functions affine in \(A\), hence concave; the identity reduces to \(\operatorname{tr}S+\operatorname{tr}(S^{-1}N^2)-2\operatorname{tr}N=\operatorname{tr}(S^{-1}(S-N)^2)\ge0\) with equality iff \(S=N\). Strictness follows because the optimiser \(T^\star(A)=A^{-1/2}(A^{1/2}\Sigma A^{1/2})^{1/2}A^{-1/2}\) is constant along \(A_0+tH\) only if \(THT=0\), i.e. \(H=0\). Therefore the BW Fréchet mean is **unique** for every \(Q\) charging the full-rank cone — a conclusion that is **cited, not claimed as new**; see the attribution box above and C-AUDIT-11 in [[References and external claim audit]].

*On spheres the gate is vacuous, and the argmin is large.* The antipodal law on \(S^{p-1}\) has \(\mathfrak M(Q)=S^{p-2}\) exactly — positive-dimensional for \(p\ge3\); the uniform law has \(\mathfrak M=S^{p-1}\); the uniform law on the equator has \(\mathfrak M=\{\pm\text{poles}\}\); on products the argmin sets multiply and their dimensions add.

*The cost of a selector — the sharpest crack, and it is answered.* A measurable selector exists (Kuratowski–Ryll-Nardzewski, closed-valued measurable multifunction into a Polish space). **No continuous selector exists** through a nonsingleton stratum: for the rotating two-point family on \(S^1\) with \(\psi(u)=\pi+\kappa(u-u_0)\), the one-sided limits of the unique mean are antipodal and the jump is exactly \(\pi\), independent of \(\kappa\). A jump of size \(\Delta\) at sample fraction \(\lambda\) injects into the ID-5 drift row

\[
D_{d,n}(h)=\lambda(1-\lambda)\Delta^2+O(h/n)\quad\text{at \emph{every} lag }h,
\]

with \(\Delta=\pi\) in the antipodal case. The contamination is rank one, **lag-invariant**, and bandwidth-insensitive for \(h=o(nb_n)\), whereas a genuine mixing factor decays geometrically. It dominates an AR(1) factor at every \(h\ge1\) whenever \(\lambda(1-\lambda)>\rho/4\) — in particular for every \(\rho<1\) at \(\lambda=\tfrac12\) — and fails to dominate only when the jump sits near an endpoint of the sample.

So the answer to "does a discontinuous selector manufacture spurious drift?" is **yes, quantifiably, and no single-valued convention avoids it**: the obstruction is the topology of the argmin correspondence, not the choice of rule.

### 14.3 Route R3 — the latent stochastic centre. The crack.

**(i) Mixture means.** In a Hilbert space with \(\mathbb E[\xi\mid C]=0\), \(\mathfrak M(Q_u)=\{\mathbb EC_u\}\): ID-1 pins the *mean of the mixing centres*, never the realised centre. In curvature it does not even pin that. On \(H^2\) — Hadamard, so every Fréchet mean is unique and every Log single-valued — take \(C\in\{c_1,c_2\}\) with equal probability, \(X=c_1\) given \(C=c_1\), and \(X\) the equal-weight two-point law \(\{p,q\}\) at geodesic distance \(s\) either side of \(c_2\) along \(\ell\), whose conditional Fréchet mean is exactly \(c_2\). With \(c_1\) off \(\ell\), the mixture mean satisfies \(m(s)=m_0+s^2m_2+O(s^4)\) with

\[
m_2=\tfrac14\,\frac{\sinh\beta\cosh\beta-\beta}{\sinh^2\beta}\,\hat w\ \ne\ 0,
\]

whereas in a flat space \(m(s)\equiv m_0\) **exactly**. The general attribution is \(m_2=-\tfrac K6H^{-1}w^\perp+O(\|w\|^3)\): the effect is curvature-induced and vanishes iff \(c_1\in\ell\). Equality of the mixture mean with the mixing-centre mean holds on the equivariance class — \(Q\) invariant under an isometry subgroup whose fixed-point set is the single point — and that sufficient condition is not necessary, the exact characterisation being \(\int\Delta(m_C,c)\,\nu(dc)=0\).

**(ii)–(iii) Marginal and FDD equivalence.** Both hold, and (iii) holds non-trivially. The \(\mathbb R^3\) witness of §5.1 gives two latent-centre models with **incomparable** loading ranges and different serially dependent centre processes sharing every finite-dimensional distribution. A curved certificate on \(H^2\times H^2\) gives orthogonal loading ranges with both centres random and \(M\)-valued, with covariant constancy exact, so the mechanism is not an artefact of flatness. And with \(\delta\equiv0\) the class imposes **no constraint whatever** on the centre process: for any subspace \(V\) and any \(r\), some admissible representation has \(\operatorname{ran}A=V\).

**(iv) What survives.** Over the latent-centre class under \(\mathcal I_J\), the identified object is the observed law itself. Its second-order shadow is the **sum**

\[
\Gamma_X(h)=\Gamma_C(h)+A\Gamma_f(h)A^*,
\]

and no nontrivial corrected theorem exists on that class — the split is not partially identified, it is entirely undetermined. This is the honest replacement statement.

**(v) What restores identification.** A **declared frequency-band separation**, and nothing weaker. Declare a centre-free band \(B_H\) and a factor-free band \(B_L\), with white \(\delta\), zero cross-spectra, and band-contrast completeness. Then

\[
\operatorname{ran}A=\operatorname{span}\big\{\operatorname{ran}\big(f_X(\lambda)-f_X(\lambda')\big):\lambda,\lambda'\in B_H\big\}
\]

exactly, with residual ambiguity reduced to ID-2(4)'s white-at-zero reallocation. The declaration is **necessary** as well as sufficient on the uniformly positive-definite class. It is a modelling convention and it is **untestable from the observed law** — which is precisely why it must be declared in the paper rather than derived.

This is where ID-9 hands off to ID-7: R3 proves a band declaration is unavoidable; ID-7 proves a specific one is sufficient *and attainable by the project's estimator*; ID-10 says how much persistence it tolerates.

**Status: the gate is TRUE AND NON-BINDING on \(\mathrm{LC}\setminus\mathrm D\); the replacement quotient and the restoring declaration are PROVED INTERNALLY.**

### 14.4 Route R4 — declared conventions. Not an escape. PROVED.

Any centre convention that is a functional of the marginal law and equivariant under \(\operatorname{Isom}(M)\) agrees with the Fréchet mean on the class where the stabiliser has the candidate as unique fixed point. Off that class the conventions genuinely differ, and their **failure geometries differ too**: for the antipodal two-point law on \(S^2\), the \(L^2\) argmin is the equator (dimension 1) while the \(L^1\) argmin is all of \(S^2\) (dimension 2), because \(F_{L^1}\equiv\pi/2\) identically.

A smoothness-regularised centre is **not** a functional of each marginal — so ID-1 does not apply to it pointwise — but the family \(\{Q_u\}\) *is* \(\mathcal I_M\), so it remains pinned at the family level. This yields the sharp form of the gate, of which ID-1 is a corollary:

> **any single-valued centre convention that is a measurable functional of the declared information set is pinned by that information set.**

Exactly three chart classes exist: \(\mathcal L^{\rm fix}\subsetneq\mathcal L^{\rm tv}\), with \(\mathcal L^{\rm rand}\cap\mathcal L^{\rm tv}=\emptyset\). Median, trimmed and regularised centres all fall in \(\mathcal L^{\rm tv}\), one new deterministic class beyond ID-4's orbit; conditional centres fall in \(\mathcal L^{\rm rand}\), which is R3's class. The regularised convention changes the estimand and Paper 1 as declared is incompatible with it, via HD-M, pointwise centring, and ID-5's \(d\otimes d\) term.

By ID-8, a median- or trimmed-centred refit is **not** a robustness check: it can report a different factor count for purely geometric reasons.

### 14.5 Route R5 — sample-level non-uniqueness. Separated on the geometries used; an identification node on spheres.

On Hadamard manifolds, and on any compact strongly geodesically convex domain with \(\operatorname{Hess}\tfrac12d^2\succeq\lambda I\), the empirical objective is strongly convex **pathwise**, so the empirical argmin is a singleton with probability one and the estimator's localisation never selects a branch. On BW the same conclusion follows from R2's linear-structure convexity applied to the empirical measure, whose atoms are full-rank almost surely on the declared domain. On these geometries R5 is **OUT OF SCOPE BY PROVED SEPARATION**, with the formal dependency argument that no consumer of ID-0–ID-6 quantifies over any estimator convention; the dependency runs only the other way, through one displayed population containment condition.

The separation genuinely needs a margin, and the witnesses show why. On \(S^1\) a law with singleton population argmin can have a non-singleton empirical argmin with probability \(\ge(1-w)^n\binom{n}{n/2}2^{-n}>0\); and for a triangular array whose margin shrinks at \(\delta_n=o(n^{-1/2})\), the empirical branch is decided by a coin flip, \(\mathbb P(\text{wrong branch})\to\tfrac12\), with the error not vanishing. On such strata the data-dependent localisation is a **randomised selector** with no population estimand, and R5 becomes an identification node — confined to sphere and sphere-product geometry, where it merges with R2's manufactured-drift cost.

## 15. ID-10 — the persistence window

ID-3 proves a fixed positive minimax risk at \(\rho_n=1-n^{-2}\). ID-10 connects that floor to the estimator's own regularity conditions.

### 15.1 The two windows

**Memory exponent.** With \(\psi^+(N)\asymp N^{-(1/2-d)}\), balancing \(b_n^3\) against \(\psi^+(nb_n)\) gives

\[
b_n=n^{-\alpha(d)},\quad \alpha(d)=\frac{1-2d}{7-2d},
\qquad
\ell_n(\psi)=n^{-3(1-2d)/(7-2d)}.
\]

The window is \(d\in[0,\tfrac12)\): \(\alpha(d)>0\iff d<\tfrac12\), and \(b_n\to0\) fails at \(d=\tfrac12\). HD-K's \(nb_n/\log n\to\infty\) never binds, and \(n^{-a}=O(b_n)\) holds throughout. **The advertised \(n^{-3/7}\) requires \(d=0\) exactly** — genuine short memory. Any long memory degrades the headline rate, continuously, to zero as \(d\uparrow\tfrac12\).

**Near-unit-root.** With \(\rho_n=1-n^{-\theta}\):

- if persistence is *constant* in rescaled time, the array is stationary, HD-M2 is vacuous, and the window is \(x_n=n^{1-\alpha-\theta}\to\infty\);
- if persistence *varies* in rescaled time, \(\rho(u)=1-n^{-\theta}g(u)\) with \(g\in C^2\) bounded away from zero and \(g'\not\equiv0\), then the induced local-stationarity exponent is **\(a=1-\theta\), exactly and sharply**. The multiplicative distortion of the MA coefficients is \(\exp(n^{-\theta-1}g'k^2/2)\), which at the effective memory \(k\asymp n^\theta\) is \(1+O(n^{\theta-1})\), and the unit-marginal-variance normalisation \(\sigma=\sqrt{1-\rho^2}\) contributes the same order without compounding.

Re-optimising gives \(\alpha=(1-\theta)/7\), rate \(n^{-3(1-\theta)/7}\), and \(x_n=n^{6(1-\theta)/7}\to\infty\iff\theta<1\). So the window is \(\theta\in[0,1)\).

**A correction to how the constraint was previously read.** \(a\ge3/7\) is a *design constant* tied to \(b_n=n^{-1/7}\), not a primitive. The primitive clause is \(a\ge3\alpha\) (HD-K separately needs only \(a\ge\alpha\)), and the induced \(a=1-\theta\) satisfies it automatically at the re-optimised bandwidth. The reading "\(\theta\le4/7\)" survives only as the corollary obtained by holding \(b_n=n^{-1/7}\) and \(a\ge3/7\) fixed.

**No contradiction with ID-3.** \(\rho_n=1-n^{-2}\) is \(\theta=2\), outside \(\theta<1\) by a full unit of exponent, and outside HD-M/HD-K/HD-L. But the margin is thinner than it looks: the headline rate needs \(d=0\), not merely \(d<\tfrac12\).

### 15.2 Where monthly realised covariance sits

**Inside the window, and — on the available evidence — on its degenerate edge.**

The analytic statement is unconditional: the application is inside iff its memory exponent satisfies \(d<\tfrac12\), which holds for any stationary specification, and it attains \(n^{-3/7}\) only if \(d=0\).

The empirical exponent is an **assumption under test, not a result, and no theorem consumes it.** The long-memory literature reports \(d\approx0.4\) for realised volatility, but those estimates are for *daily* realised volatility of *exchange rates*. Temporal aggregation preserves \(d\), but the asset class and the object — a covariance matrix rather than a univariate volatility — differ, and \(d\) is not separately estimated in the parent's 240-month panel. The transfer is therefore flagged unverified and routed to N-18/APP-FIN.

Read as a diagnostic and labelled as one: at \(n=240\), \(b_n=n^{-1/7}\) gives \(nb_n\approx110\) and \(b_n^3\approx0.096\); a memory exponent \(d\approx0.40\) gives \(\psi^+\approx0.60\), a stochastic-to-bias ratio near \(6\), and roughly \(2.7\) effective independent factor draws per smoothing window. If that exponent is the right one for this object, drift and factor are **not empirically separable at this sample size**, and \(n^{-3(1-2d)/(7-2d)}=n^{-0.10}\) is not a usable rate. That is a statement about resolution, not about the parent's estimator being wrong, and it must not be reported as evidence that the parent's Factor 1 is drift.

**Status: PROVED INTERNALLY** for both windows and the induced exponent; the Dahlhaus–Richter–Wu local-stationarity mode is **CITED EXTERNALLY AND APPLIED**; the empirical memory exponent is **OUT OF SCOPE BY PROVED SEPARATION** to application verification, with the no-consumer argument displayed above.

## 16. Closure evidence for ID-7–ID-10

Workstream A proved ID-7, ID-10 and route R4; B proved ID-8 and routes R1, R2; C proved routes R3 and R5. Wave 3's hostile cross-audit was interrupted by a credit limit and was re-executed by the lead, which authored none of the three dossiers; every load-bearing claim was re-derived analytically from scratch with numerical corroboration. Seven objections were raised and all seven closed: two lead conjectures were overturned by workstreams (the unconditional \(N^{-1/2}\) modulus; the \(\theta\le4/7\) window), one workstream claim was retitled rather than accepted (ID-2 "false" \(\to\) ID-2 non-binding), one was overruled (the \(\psi\) impossibility), one cross-workstream conflict was resolved (R5 on BW), and two were corrected in detail (the wedge constant \(2\to1\); the manufactured-drift domination now carries its \(\lambda\) condition). One claim was deflated to its true content (R3-D), one was scoped to what canon consumes (the global \(H^2\) monotonicity), and one citation transfer was refused (the empirical memory exponent).

External producers consumed by the closure package, each with exact theorem and scope in [[References and external claim audit]]: Doob's mean-square ergodic theorem (ID-3, ID-7); Gavrilov/Pennec's neighbouring-log expansion (ID-8); Dahlhaus–Richter–Wu Assumption 2.1 (ID-10); Kroshnin–Spokoiny–Suvorikova Theorem 2.1 and Santoro–Panaretos (arXiv:2305.15592) Theorem 1, with Masarotto–Panaretos–Zemel Corollary 9 / Proposition 10 (ID-9 R1 and R2 — **cited, not internal**; the former internal-novelty claim is retracted per C-AUDIT-11, and Agueh–Carlier is retained as historical context only); Kuratowski–Ryll-Nardzewski measurable selection (ID-9 R2).

Proof provenance for the closure package is archived in [[P1-ID-CLOSE — lead ledger]], [[P1-ID-CLOSE-A — constructive separation, persistence window, and centre conventions]], [[P1-ID-CLOSE-B — curved geometry, existence and uniqueness]], and [[P1-ID-CLOSE-C — latent stochastic centre and sample-level non-uniqueness]]. These are proof records, not parallel status authorities.

## 17. Downstream \(\nu\)-phase boundary — what the closed theorem does and does not imply

This section introduces no new identification node. It turns ID-5, ID-6, ID-10 and Corollary P-DRIFT into a controlled downstream experiment.

Let

\[
\mu_\nu(u)=\operatorname{Exp}_{\mu_0}\{\nu g(u)V\}
\]

on a declared injective radial domain, with \(V\in T_{\mu_0}M\) and \(g\) fixed. Then \(\nu=0\) is an exactly static centre and increasing \(|\nu|\) increases one declared mode of centre motion. Along this radial geodesic family,

\[
\mathcal L_{\mu_\nu}
=|\nu|\,\|V\|\int_0^1|g'(u)|\,du,
\qquad
\mathcal V_{\mu_\nu}^2
=\nu^2\|V\|^2\int_0^1|g'(u)|^2\,du.
\]

Thus \(\nu\) is a useful experimental coordinate, while path length and path energy are the intrinsic quantities to report. The formulas need not hold for a non-radial parameterisation; in that case compute the intrinsic motion directly.

For a target \(T\), estimator pair \((\widehat T^{\rm stat},\widehat T^{\rm mov})\), sample size \(n\), and fully declared risk \(R_T\), define the moving-centre advantage set

\[
\mathcal C_T
=\{\nu\ge0:
R_T(\widehat T^{\rm mov};\nu)
<
R_T(\widehat T^{\rm stat};\nu)\}.
\]

The first crossover \(\nu_T^\star=\inf\mathcal C_T\) is called a **static-centre breakdown threshold** only after the risk, target, horizon, tuning rule, loss, proxy and DGP are fixed. The set \(\mathcal C_T\) need not be nonempty or an upper interval, so neither existence nor uniqueness of a crossover is automatic. Estimation and forecasting use different risks and may have different—or no—thresholds.

ID-5 determines the local power of the structural contamination. Write its stacked fixed-centre defect as

\[
\mathcal K_\nu
=\nu\mathcal K_1+\nu^2\mathcal K_2+o(\nu^2)
\]

whenever that expansion is justified on the declared family. The linear coefficient contains any surviving drift–factor, drift–noise, or nonlinear curved base-change contribution. Only when centring/orthogonality kills \(\mathcal K_1\), and the clean drift row satisfies \(\mathcal K_\nu=\nu^2\mathcal K_2\), does balancing against a row-resolution scale \(e_n\) give

\[
\nu_{\rm est}^\star\asymp e_n^{1/2}.
\]

With \(e_n=n^{-1/2}+\ell_n\), short memory, and \(\ell_n\asymp n^{-3/7}\), this yields the **conditional candidate**

\[
\nu_{\rm est}^\star\asymp n^{-3/14}.
\]

It is not a generic theorem. If \(\mathcal K_1\ne0\), the first candidate scale is \(e_n\), not \(e_n^{1/2}\). If drift is aligned with the identified dynamic span, there may be no loading-span breakdown at any small \(\nu\), although within-span eigenvalue ordering and factor interpretation can change. Orthogonal clean drift gives the exact added directions of Corollary P-DRIFT; partial drift can rotate or cancel; nonzero curvature can change rank through ID-8 even when a flat quadratic intuition suggests otherwise. Long memory replaces \(\ell_n\)'s stochastic term by \(\psi^+(nb_n)\) under ID-10.

A forecasting threshold is further downstream. It depends on the score model, horizon, reconstruction, parameter tuning, and an evaluation loss admissible under [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]]. Squared Frobenius and multivariate QLIKE are the primary covariance risks. A geodesic-loss crossover is a crossover for that loss's induced proxy barycentre unless the induced target and recalibration are stated; it is not automatically evidence about latent conditional-mean forecasting.

**Canonical status.** The decomposition and boundary reasons above are consequences of proved ID-5/ID-8/ID-10 results. The numerical location and shape of \(\mathcal C_T\), including the \(n^{-3/14}\) clean-case candidate, are **PREDECLARED DIAGNOSTIC TARGETS, NOT THEOREMS**. They are implemented by N-18c in [[Numerical suite — theorem-driven design matrix]]. The originating research note is archived as [[Why ν matters — the static-centre breakdown threshold]].
