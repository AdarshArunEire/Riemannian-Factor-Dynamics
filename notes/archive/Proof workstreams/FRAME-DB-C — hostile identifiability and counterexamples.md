---
type: proof-dossier
title: FRAME-DB-C — hostile identifiability and counterexamples
status: noncanonical-workstream
scope: FRAME-DB hostile audit only; Paper 2 excluded
---

# FRAME-DB-C — hostile identifiability and counterexamples

> This dossier is adversarial proof input, not canon. It distinguishes failures of a proposed construction from impossibility for the full observable-law problem. The current canon and every archived source required by the FRAME-DB brief were read completely before the claims below were made.

## 0. Executive verdict before the A/B cross-audits

The strongest negative conclusion currently justified is narrower than generic non-identifiability.

1. **The oracle target is identifiable from the observable law under the retained uniqueness assumptions.** If the Fréchet mean at every time is unique, the mean path is the uniquely selected regular path, the Levi–Civita connection and the path convention are fixed, and the target is taken modulo one anchor orthogonal conjugation, then the transported lag row is a functional of the observable marginal and lag-pair laws. In that class there is no pair with the same observable law and different oracle lag row modulo common conjugation. **PROVED.**
2. Consequently, an impossibility argument based on treating the true parallel frame or Ω as an extra latent DGP parameter is invalid. Ω is relative to a chosen feasible centre/frame estimator. This generic non-identifiability route is **DISPROVED**.
3. Simple plug-in frame subtraction, fixed-fold averaging, jackknife/Richardson cancellation of realised frame noise, and invariant-spectrum redesigns fail for the declared estimator classes, not generically. **DISPROVED.**
4. A full one-step/von-Mises correction is not defeated by the preceding attacks. In principle it may differentiate the complete observable-law functional—Fréchet mean, inverse Karcher map, path transport, endpoint connectors, logarithms, and lag expectation—so that the frame derivative is corrected without estimating Ω pointwise. No observational-equivalence counterexample survives uniqueness of the population mean path and the target modulo common conjugation. **OPEN — EXACT LEMMA STATED** in Section 7.
5. Until that lemma and its statistical implementation are proved, the robust (n^{-3/7}) numerator remains the only generic curved nonparametric conclusion. A root-(n) parametric centre or geometry with an observable finite-dimensional connection gives a restricted route but not generic first-order immunity. **PROVED UNDER EXPLICIT ASSUMPTIONS** by the existing APP-B interface.

## 1. Fixed targets and gauges

Let (H_0=T_{mu(u_0)}M), and let (P^mu_{t\to0}:T_{mu(u_t)}M\to H_0) be Levi–Civita parallel transport along the declared population mean path. Define

\[
Y_t=P^mu_{t\to0}\log_{mu(u_t)}X_t,
\qquad
\Gamma_n(h)=N_{n,h}^{-1}\sum_t E(Y_t\otimes Y_{t-h}).
\tag{1.1}
\]

The five targets that must not be conflated are:

| ID | Target | Gauge treatment | Identifiability |
|---|---|---|---|
| T0 | ((\Gamma_n(h))_{h\le h_0}) in one declared anchor frame | coordinate representative | identifiable after choosing the anchor isometry |
| T1 | common-conjugacy class ([\Gamma_n]=\{(Q\Gamma_n(h)Q^*)_h:Q^*Q=I\}) | one harmless rigid rotation quotiented out | intrinsic Paper 1 lag-row target |
| T2 | feasible row based on an estimated centre and estimated path frame | contains time-varying relative frame error | observable estimator, not the target |
| T3 | a corrected feasible row | must converge to T1 | FRAME-DB objective |
| T4 | spectra, singular values, Gram data, or another quotient summary | more gauge invariant than T1 | changed estimand unless it reconstructs T1 up to one common (Q) |

### Proposition C1 — no observational-equivalence attack under unique mean and fixed connection

Fix a known Riemannian manifold and its Levi–Civita connection. Suppose the observable law determines a unique Fréchet mean (mu(u)) for every (u), these means form the unique admissible regular path, and (1.1) uses the declared path transport. If two mechanisms have the same joint observable law of ((X_1,\ldots,X_n)), then they have the same (mu(u_t)), the same transports (P^mu_{t\to0}), and the same (Gamma_n(h)). Any two anchor orthonormal coordinates differ by one common orthogonal conjugation.

**Proof.** Equality of the observable law gives equality of every marginal Fréchet objective and every lag-pair law. Uniqueness gives the same minimiser at each time. The connection and the same mean path then uniquely solve the transport ODE. Hence the measurable integrands in (1.1) and their expectations agree. An anchor coordinate change is one common orthogonal map. \(\square\)

**Status: PROVED.**

This proposition rules out the requested Section 8(12) observational-equivalence pair within the retained identifiable class. Such pairs become possible only after deleting one of its hypotheses—nonunique means, unspecified path selection, arbitrary external connections, or a latent factor decomposition whose loading range is not tied to the lag row. Those are different model classes.

Under exact included-lag factorisation and (Q_n=\sum_hC_f(h)C_f(h)^*\succ0), (E=\operatorname{ran}\mathcal G) is itself fixed by the observable lag row. Alternative factor coordinates only rotate inside the same (E). Thus latent factor reparametrisation also fails to create the required pair.

## 2. Exact plug-in residual and the burden it creates

After common alignment, APP-B gives

\[
U_t=Y_t-H_te_t+\Omega_tY_t+\xi_t^{(2)}.
\tag{2.1}
\]

Consider a training-measurable plug-in Ω estimate (\widetilde\Omega_t) and a vector proxy (\widetilde Y_t=Y_t+a_t), all written in the same aligned anchor space. Put

\[
\delta_t=\widetilde\Omega_t-\Omega_t.
\]

Subtracting the proposed frame term leaves, before the APP-B quadratic remainder,

\[
\begin{aligned}
R^{\rm plug}_{t,h}
=&-\delta_tY_t\otimes Y_{t-h}-Y_t\otimes\delta_{t-h}Y_{t-h}\\
&-\widetilde\Omega_ta_t\otimes Y_{t-h}
-\widetilde\Omega_tY_t\otimes a_{t-h}\\
&-a_t\otimes\widetilde\Omega_{t-h}Y_{t-h}
-Y_t\otimes\widetilde\Omega_{t-h}a_{t-h}\\
&-\widetilde\Omega_ta_t\otimes a_{t-h}
-a_t\otimes\widetilde\Omega_{t-h}a_{t-h},
\end{aligned}
\tag{2.2}
\]

with the obvious regrouping if (\widetilde\Omega) is also applied to (a_t) inside the first slot. Conditional on exact training/evaluation separation, the population part of the first line is

\[
\mathcal B_h(\delta)
=N_{n,h}^{-1}\sum_t
\{\delta_t\Gamma_{t,h}-\Gamma_{t,h}\delta_{t-h}\}.
\tag{2.3}
\]

The centred fluctuation of that line is at best (O_p(r_\delta n^{-1/2})) under the retained bounded-energy/fixed-memory package. The binding requirement is not pointwise recovery of every (\Omega_t), but

\[
\left\{\sum_h\|\mathcal B_h(\delta)\|_{\rm HS}^2\right\}^{1/2}
=o_p(n^{-1/2}),
\tag{2.4}
\]

plus direct-sum HS control of every (a\)-product in (2.2). A theorem demanding (\sup_t\|\delta_t\|=o_p(n^{-1/2})) is sufficient but unnecessarily strong; a theorem that gives only (r_\delta=O_p(\ell_n)) does not imply (2.4).

One common skew field must be removed before defining δ. Its commutator with Γ is the derivative of a harmless common conjugation and must not be inserted into (2.4) or Davis–Kahan.

**Status: PROVED.** This is direct expansion and conditional expectation.

### Counterexample C2 — frame-output-only identification is impossible

Consider the restricted class of corrections whose only training input is (K) reported infinitesimal frames

\[
W_k(t)=\Omega(t)+Z_k(t),\qquad k\le K,
\tag{2.5}
\]

where the joint law of the errors (Z_k) is unrestricted apart from a norm bound. For any nonconstant skew field (D(t)), the parameter/error pairs

\[
(\Omega,Z_k)
\quad\text{and}\quad
(\Omega+D,Z_k-D)
\]

have the same law of the complete reported input (W=(W_1,\ldots,W_K)) and different coefficients whenever

\[
N_h^{-1}\sum_t\{D_t\Gamma_{t,h}-\Gamma_{t,h}D_{t-h}\}\ne0.
\]

Therefore no estimator using only noisy frame outputs, with no model for their errors and no raw observations/geometry, identifies the desired correction.

The scope is the frame-output-only class. **Status: DISPROVED.** This is not a generic FRAME-DB impossibility theorem because the full raw law and geometry remove the equivalence by Proposition C1.

### Proposition C2b — a narrow pointwise root-\(n\) information ceiling

This proposition applies only to pointwise recovery from a local noisy-frame experiment; it does not rule out estimating the averaged coefficient (2.3) by an orthogonal score. At a fixed interior time \(u\), suppose the correction receives \(m_n\asymp nb_n\) independent local coordinates

\[
Z_i=\theta(u)+\varepsilon_i,\qquad \varepsilon_i\sim N(0,1),
\]

for one scalar projection of the infinitesimal frame, with no information about \(\theta(u)\) outside the bandwidth window. For \(\theta_0=0\) and \(\theta_1=c/\sqrt{m_n}\), the Kullback--Leibler divergence is \(c^2/2\). Le Cam's two-point inequality therefore gives, for every estimator \(\widehat\theta\),

\[
\sup_{j\in\{0,1\}}E_{\theta_j}|\widehat\theta-\theta_j|
\ge c_0m_n^{-1/2}=c_0(nb_n)^{-1/2}.
\tag{2.6}
\]

Because \(b_n\to0\), this is slower than \(n^{-1/2}\). Thus a theorem requiring pointwise \(o_p(n^{-1/2})\) recovery of an unrestricted locally estimated frame is impossible even in this favourable Gaussian subexperiment.

The scope is pointwise local-frame estimation in the stated Gaussian experiment. **Status: DISPROVED.** The conclusion does not apply to coefficient-level estimation, finite-dimensional parametric paths, pooling across time under smoothness, or the one-step functional in Section 7.

### Proposition C2c — correction-only root-\(n\) ceiling for a regular coefficient

This is a distinct, coefficient-level lower bound, but its scope is deliberately narrow. Conditional on a pilot curve, consider a correction stage with \(n\) independent observations from the regular Gaussian submodel

\[
Z_i\sim N(\vartheta,1),\qquad i=1,\ldots,n,
\]

and suppose one scalar projection of the non-rigid frame coefficient is \(B(\vartheta)=\beta\vartheta\), \(\beta\ne0\). For every estimator \(\widehat B_n\), there are constants \(c,c_0>0\) such that

\[
\max_{\vartheta\in\{0,c/\sqrt n\}}
P_\vartheta\left{
|\widehat B_n-B(\vartheta)|
>\frac{|\beta|c}{3\sqrt n}
\right}\ge c_0.
\tag{2.7}
\]

**Proof.** The two product laws have Kullback--Leibler divergence \(c^2/2\), independent of \(n\). Choose \(c\) small enough that their total variation is bounded strictly below one. If the displayed error event had probability tending to zero under both laws, thresholding \(\widehat B_n\) at \(\beta c/(2\sqrt n)\), with the inequality reversed when \(\beta<0\), would distinguish the two laws with total error tending to zero, contradicting the total-variation testing bound. \(\square\)

Hence an architecture that first fixes a pilot and then uses only \(O(n)\) fresh correction observations to estimate a regular nonzero frame coefficient cannot demand that the correction estimate itself have uniform error \(o_p(n^{-1/2})\). This is an information ceiling, not non-identifiability.

It also does not rule out a one-step estimator. In a regular one-step expansion, the unavoidable \(O_p(n^{-1/2})\) influence fluctuation is part of the estimator's leading empirical row, while the nuisance-induced remainder can be \(o_p(n^{-1/2})\). FRAME-DB must state which convention it uses: if “frame residual” includes the correction coefficient's own regular estimation noise, requirement (2.1) is generically too strong for this submodel; if that noise is incorporated into the corrected row's root-\(n\) influence term and only the post-linearisation nuisance remainder is called \(d_{F,{\rm db},n}\), Proposition C2c does not obstruct the objective.

The scope is correction-only estimators whose declared frame residual includes all regular coefficient-estimation noise. **Status: DISPROVED.**

## 3. Fixed-fold averaging, jackknife, Richardson, and nominal orthogonality

### Proposition C3 — fixed-fold linear combinations do not cancel realised nuisance noise

Let (T(\eta)) be a scalar projection of a lag-row functional with derivative (DT_\eta[v]=c(v)\ne0) in some admissible centre/frame direction. Suppose (K<\infty) independent fold estimators obey

\[
\widehat\eta_k=\eta+r_nZ_k+o_p(r_n),
\qquad EZ_k=0,quad \operatorname{Var}\{c(Z_k)\}=\sigma^2>0.
\]

For deterministic weights preserving the target, (\sum_kw_k=1),

\[
\sum_kw_kT(\widehat\eta_k)-T(\eta)
=r_n\sum_kw_kc(Z_k)+o_p(r_n),
\]

whose variance is at least (r_n^2\sigma^2/K). At (r_n=\ell_n=n^{-3/7}), this is not (o(n^{-1/2})). Negative jackknife weights do not change the lower bound (\sum_kw_k^2\ge1/K).

The scope is fixed-(K) target-preserving linear combinations without an evaluation-score correction. **Status: DISPROVED.**

Richardson weights can cancel deterministic powers of a bandwidth when the derivative errors share known scale coefficients. They do not cancel the realised stochastic (Z_k) above. Increasing (K) enough to average this term changes training sizes, dependence, masks, and computation and still does not cancel a nonzero conditional bias coefficient.

### Gateaux audit for any claimed orthogonal score

Let a proposed score be (\psi_h(O;\eta)), where η includes the mean path, connectors, and frame. Neyman orthogonality requires

\[
\left.\frac d{d\epsilon}E\psi_h(O;\eta+\epsilon v)\right|_{\epsilon=0}=0
\tag{3.1}
\]

for every admissible path perturbation (v), modulo one common rigid gauge. Cancelling only the base-log derivative (-H_tv_t) leaves the connection derivative

\[
(D P^\mu[v])\log_{mu_t}X_t,
\tag{3.2}
\]

which is exactly the frame channel. Conversely, subtracting a ribbon term while ignoring the derivative of the Fréchet equation, the endpoint logarithm, or endpoint connectors is not (3.1). A label such as “double machine learning” has no proof status until the sum of all typed terms vanishes.

## 4. Frame-avoiding redesigns and target changes

1. **Intrinsic lag-pair morphisms.** One may define an operator between (T_{\mu_{t-h}}M) and (T_{\mu_t}M) using pairwise transport. To recover the fixed Paper 1 anchor loading space, those morphisms must still be synchronized along a declared path. Estimated-centre synchronization reintroduces the derivative of transport. **PROVED.**
2. **Conjugacy-invariant spectra.** Singular values or spectra of lag operators are invariant, but do not determine the loading subspace. For (0<a<1), (\Gamma=\operatorname{diag}(a,0)) and (Q\Gamma Q^*) have the same invariants and different coordinate loading lines. Invariant-only loading recovery is **DISPROVED**.
3. **Gram/synchronization methods.** A complete collection of pairwise inner products may recover a configuration up to one common orthogonal map. This is not ruled out. It must prove that estimated pairwise transports are cycle-consistent to second order after shared centre errors and that its output equals T1 rather than merely T4. **OPEN — EXACT LEMMA STATED** jointly with Section 7.
4. **Endpoint-geodesic replacement.** Transport along the direct geodesic from (mu_{t-h}) to (mu_t) generally differs from transport along the population mean path by holonomy. Automatic debiasing by this substitution is **DISPROVED**.

## 5. HS/operator, dependence, mask, and propagation attacks

### Counterexample C4 — operator lag energy cannot replace HS lag energy

Let (k\) be even and in (\mathbb R^k) set

\[
D_k=k^{-1}\operatorname{diag}(I_{k/2},-I_{k/2}).
\]

There are bounded unit-norm finite-state lag processes with lag covariance (D_k): select a coordinate uniformly and let its sign have lag correlation (+1) on the first half and (-1) on the second half. Thus (\|D_k\|_* =1), compatible with bounded total energy, while

\[
\|D_k\|_{\rm op}=k^{-1},
\qquad
\|D_k\|_{\rm HS}=k^{-1/2}.
\]

Choose a unit-norm skew operator (B_k) that swaps the two half-spaces. Then

\[
\|B_kD_k-D_kB_k\|_{\rm HS}\asymp k^{-1/2},
\]

whereas (\|D_k\|_{\rm op}\|B_k\|\asymp k^{-1}). Hence an (A_{2,n}r_F) bound based on operator lag energy can miss a factor (\sqrt{k}). The valid generic producer is (G_{2,{\rm HS},n}r_F).

**Status: DISPROVED.**

### Dependence and splitting

Exact finite-memory innovation separation makes trained nuisances conditionally fixed and supports HS fluctuation bounds. A finite gap under infinite memory does not. Any approximate branch must include both a joint retained-row coupling/conditional physical-dependence bound and stability of the trained nuisance. Pairwise conditional total variation controls a conditional coefficient but not the empirical row. **PROVED.**

### Mask and target

Alternating training/evaluation blocks alter local design moments by first-order terms such as (L_n/n), and comparison of masked and unmasked lag targets is itself first order. A claimed quadratic nuisance theorem cannot square the target-mask discrepancy. The score, its population target, and every lag normalisation must use the same mask, or the mismatch enters (d_n^{\rm db}) additively.

### Actual loading propagation

If the corrected direct-sum HS row error is (d_n^{\rm db}), then only

\[
\|\widehat{\mathbb L}^{\rm db}-\mathbb L\|_{\rm op}
\le 2A_{2,n}d_n^{\rm db}+(d_n^{\rm db})^2
\tag{5.1}
\]

is automatic, with (A_{2,n}) the operator row energy used for assembly. Davis–Kahan requires the actual (\Delta_n) and (2A_2d+d^2=o_p(\Delta_n)). The null-spectrum square is obtained from the row-operator singular-value argument:

\[
\widehat\lambda_{r+1,n}^{\rm db}\le(d_n^{\rm db})^2.
\tag{5.2}
\]

Neither a small commutator, a factor lag singular value, nor a frame rate replaces these steps. Replacing (\Delta_n) by (s_n^2) requires the proved full-rank-lag comparison.

## 6. Mandatory edge-case results

| Edge family | Hostile result | Status |
|---|---|---|
| Flat Hilbert space | after common alignment (\Omega=0); any nonzero claimed geometric frame correction is spurious; mean recentering can still be first order | PROVED |
| One fixed commuting SPD flat | exact log-coordinate reduction; same verdict as flat Hilbert when every estimator object stays in the one flat | PROVED |
| Common rigid (\Omega_t\equiv\bar\Omega) | exact common conjugation; additive subtraction followed by Davis–Kahan over-penalises a gauge change | PROVED |
| APP-B CE-B5 | alternating non-rigid (c_nB) with ([B,\Gamma(1)]\ne0) survives GLO and splitting at order (c_n), disproving GLO-only debiasing | DISPROVED |
| Zero signal (\Gamma_h=0) | frame population coefficient is zero, but (\Delta_n=0) and the loading space is unidentified | PROVED |
| Zero idiosyncratic noise, estimated moving centre | curvature ribbon can remain because the signal itself supplies (Y_t\), disproving noise-free frame immunity | DISPROVED |
| Constant nonzero curvature, moving mean | a typed small-ribbon expansion has leading holonomy (R(v,\mu')\) times oriented area | PROVED UNDER EXPLICIT ASSUMPTIONS |
| High-dimensional bounded total energy | Counterexample C4 disproves an operator-energy substitute for the HS coefficient | DISPROVED |
| Error concentrated at one grid vertex | RMS (\ell_n) allows (e_j\asymp\sqrt{M_n}\ell_n); the cell quadratic area is (M_n\ell_n^2), so synchronization proofs must retain the grid maximum/tube and (M_n\ell_n^2) terms | PROVED |
| High-frequency, small-amplitude path | the construction disproves bounded length as sufficient for (M^{-2}) discretisation | DISPROVED |
| Nearly commuting matrices with changing eigenbasis | the construction disproves raw near-commutation as sufficient | DISPROVED |
| Same observable law, different latent decomposition | no counterexample survives in the retained class | DISPROVED |

## 7. One-step/von-Mises escape route: exact unresolved lemma

Let (\mathcal P\) be a class of observable time-indexed laws with unique Fréchet path, uniform Karcher coercivity, fixed connection, retained lag laws, and the canonical smoothness/tube package. Define the intrinsic common-gauge lag-row functional

\[
\mathfrak T_n(P)
=\left[
\left(
N_{n,h}^{-1}\sum_t
E_P\{Y_t(P)\otimes Y_{t-h}(P)\}
\right)_{h\le h_0}
\right],
\tag{7.1}
\]

where (Y_t(P)=P^{\mu(P)}_{t\to0}\log_{\mu_t(P)}X_t) and brackets denote one common anchor conjugacy class.

> **Lemma FRAME-IF (smallest current missing lemma).** Construct a gauge-equivariant influence map
> \[
> \varphi_{n,P}:O\longmapsto\bigoplus_{h\le h_0}\mathcal S_2(H_0)
> \]
> and a feasible cross-fitted estimator (\widehat\varphi_{n,-k}) such that:
>
> 1. for every regular observable-law path (P_\epsilon) with score (s),
>    \[
>    \left.\frac d{d\epsilon}\mathfrak T_n(P_\epsilon)\right|_0
>    =E_P\{\varphi_{n,P}(O)s(O)\}
>    \]
>    in direct-sum HS norm, after projecting out the one common skew gauge;
> 2. the derivative includes the inverse Karcher influence for every (\mu_t), the base-log Hessian derivative, the full Jacobi/connection variation of path transport, endpoint connector terms, and the derivative of the lag-pair expectation, with all fibres typed;
> 3. the cross-fitted one-step row
>    \[
>    \widehat{\mathfrak T}_n^{\rm 1step}
>    =\mathfrak T_n(\widehat P_{-k})
>    +P_{n,k}\widehat\varphi_{n,-k}
>    \]
>    is computable without the true centre, frame, anchor, (e_t), Ω, population Γ, or an unobserved ribbon;
> 4. uniformly over the retained class,
>    \[
>    \left\|
>    \widehat{\mathfrak T}_n^{\rm 1step}-\mathfrak T_n(P)
>    -(P_n-P)\varphi_{n,P}
>    \right\|_{\oplus {\rm HS}}
>    =O_p(r_e^2+r_er_F+r_F^2)+o_p(n^{-1/2});
>    \]
> 5. the empirical influence row has a dimension-uniform (O_p(n^{-1/2})) direct-sum HS bound under the exact finite-memory split (or an explicitly proved conditional physical-dependence replacement), including masks and lag overlap.

**Status: OPEN — EXACT LEMMA STATED.**

## 7A. First hostile cross-audit of frozen A and B — SUPERSEDED as a current objection list

This pass audited the pre-repair A/B drafts from observables through the final loading claim. It is retained as audit history; its objections are **SUPERSEDED** as current claims wherever the repaired dossiers and Section 12 implement the resolution. Gate D survives.

| Claim | Attack | Required repair or counterexample | Independent checker | Final status | Consequence |
|---|---|---|---|---|---|
| A (A.1), endpoint connector variation | (E_a,E_b) are called derivatives of the connectors, but differentiation of ((C_b^\epsilon)^{-1}P^\epsilon C_a^\epsilon) gives the inverse-connector term with the opposite sign from the connector generator. The displayed (+E_bP-PE_a) cannot be checked until (E_a,E_b) are defined as left/right logarithmic derivatives of (C) or (C^{-1}). | Define (E_a=(C_a^0)^{-1}\nabla_\epsilon C_a^\epsilon|_0) and (E_b=(C_b^0)^{-1}\nabla_\epsilon C_b^\epsilon|_0), or define the inverse generators, then rederive every sign. State the special radial/parallel connector convention that makes an endpoint generator zero. | C | OPEN — EXACT LEMMA STATED | A.1 is not yet a reusable typed influence identity with fixed signs. |
| A (A.1), curvature sign and orientation | The curvature-integral sign depends jointly on the stated (R) convention, the order (R(V,T)), and whether transport is (P_{b\leftarrow a}) or its inverse. Naming the (R) convention alone does not verify the displayed sign. | Derive the commutator identity (\nabla_\epsilon\nabla_s-\nabla_s\nabla_\epsilon=R(V,T)) for a transported test vector with the exact boundary conditions. | C | OPEN — EXACT LEMMA STATED | The sign must match B's subtraction and the Karcher sign. |
| A (A.4), Karcher influence | With (Psi(q,P)=E_P\log_qX) and (A=EH), (D_q\Psi[v]=-Av), so (\dot\mu=A^{-1}E(\log_\mu X,s)) is correct. | Preserve this convention explicitly in B's score and one-step formula. | C | PROVED | This fixes the only acceptable sign convention for the repair below. |
| A (A.5), “direct observation-law term” | For a fixed observation (x), differentiating (F(\mu(P))\log_{\mu(P)}x) has the frame and base-log terms only. The law derivative enters when differentiating the expectation through the score (s). Adding an unspecified direct term in (dot Y_t) and then adding the lag-law derivative risks double counting. | Separate (i) the derivative of the integrand at fixed (x), and (ii) (E{(Y_t\otimes Y_{t-h})s_{t,h}}). If a structural coupling also moves (x), define that different statistical path separately. | C | OPEN — EXACT LEMMA STATED | The full observable-law influence function is not yet derived. |
| A (A.2), common gauge | (DF_t[V]F_t^{-1}) is skew only after the varying source fibre has been connector-identified and the family is an isometry on one fixed Hilbert space. A time-constant (B) is a first-order common left rotation, not an arbitrary addition at finite error. | State the connector identification and first-order gauge action. Quotient only the common component before the coefficient norm. | C | PROVED UNDER EXPLICIT ASSUMPTIONS | No Davis–Kahan cost is paid for the repaired common component. |
| A polygon derivative (A.3) | The product rule is correct, but it is not a feasible rate theorem. Shared-vertex endpoint generators telescope only for exactly matched connector conventions; a single bad vertex and the true-chord lens remain. | Keep every (M r_N^2), (M^{-2}), acceleration, and tube-maximum term. Prove matching before telescoping. | C | PROVED | The high-frequency and concentrated-grid attacks are correctly survived only with those terms. |
| A Lemma A-IF, property 3 | It asks the estimated aggregate coefficient itself to differ from truth by (o_p(n^{-1/2})), apart from quadratic pilot terms. On a regular nonzero-derivative correction submodel, Proposition C2c forbids this if the difference includes the correction sample's estimation noise. | Replace property 3 by an asymptotic-linear representation: estimated correction minus target equals an empirical influence row plus (O_p(r_e^2+r_er_F+r_F^2)+o_p(n^{-1/2})). Count the root-(n) influence row in the leading corrected-row fluctuation, not in (d_{F,{\rm db},n}). | C | DISPROVED | A-IF as written is too strong under the all-correction-noise residual convention; the broader full-functional version remains open. |
| B plug-in expansion (B.2)–(B.4) | The pathwise algebra is substantially correct, and it uses coefficient-level HS control rather than pointwise recovery. However (r_\delta) appears in (B.4) without definition, while (r_a) denotes vector-proxy error rather than frame error. Constants also hide the bounded oracle norm (R). | Define (r_\delta^2=N^{-1}\sum_t\|\delta_t\|_{\rm op}^2); retain (R) in the cross-product envelope; specify the shifted-index RMS convention. | C | PROVED UNDER EXPLICIT ASSUMPTIONS | The conditional plug-in residual is usable only after notation repair and an observable producer. |
| B plug-in feasibility | “Best common skew” and proof-aligned anchor space are not computational inputs. The theorem correctly calls them proof comparisons, but no observable synchronization rate is supplied. | State a gauge-equivariant observable synchronization rule or leave the result strictly coefficient-conditional. Add its non-rigid residual to (B.4). | C | OPEN — EXACT LEMMA STATED | No generic feasible plug-in theorem is earned. |
| B fixed-fold lower bound | The fixed-(K), target-preserving linear-combination subexperiment is valid and does not overclaim generic impossibility. | Retain its exact estimator-class scope. | C | DISPROVED | Jackknife/Richardson alone cannot supply FRAME-DB. |
| B finite-dimensional one-step, signs | B.6 omits the actual score formula. Under A's convention, if a pilot displacement is (e), then (Psi(\widehat\mu)=-Ae+o(\|e\|)), (widehat e=-A^{-1}\Psi), and the corrected functional is (T(\widehat\mu)-K\widehat e=T(\widehat\mu)+KA^{-1}\Psi). The derivative is (Kv+KA^{-1}(-Av)=0). Any formula (T-KA^{-1}\Psi) has the wrong sign. | Write the estimator and this derivative explicitly, including the parameter influence sign and whether training/evaluation influence is added or subtracted. | C | OPEN — EXACT LEMMA STATED | The restricted theorem is not independently reproducible until its convention is fixed. |
| B finite-dimensional one-step, theorem content | “Subtracting the fitted derivative applied to the training influence and adding its evaluation influence score” is not an estimator definition, and “standard Taylor expansion” is prohibited as load-bearing status language. The assumptions nearly contain the conclusion unless the influence row and sample masks are written. | Give one displayed estimator; define its training and evaluation sigma-fields, influence summand, mask, and target. Prove B.6 by expansion. Exhibit one nonempty curved DGP with computable derivative, rather than relying on finite-dimensional compactness. | C | OPEN — EXACT LEMMA STATED | Gate B is not yet earned by B.6 as written, although the parametric route remains viable. |
| B correction-noise convention | B correctly states that uniform (o_p(n^{-1/2})) is impossible if every correction fluctuation is called frame residual. This is exactly Proposition C2c's distinction. | Define (d_{F,{\rm db},n}) as the post-influence nuisance remainder. Put the empirical influence fluctuation in the leading root-(n) row. | C | PROVED | The objective is coherent only under this convention. |
| B FRAME-IF | The revised lemma correctly asks for a one-step remainder and a root-(n) empirical influence row, avoiding the impossible direct (o_p(n^{-1/2})) coefficient estimate. It still lacks the typed derivative, observable nuisance producer, grid aggregation, and concentration proof. | Merge A.1–A.5 after sign repair with B.7. Specify the direct-sum HS influence summand and its finite-array/mask law. | C | OPEN — EXACT LEMMA STATED | This is the correct Gate D node. |
| B validation/evaluation aggregation | Per-vertex local scores fluctuate at ((nb_n)^{-1/2}), not (n^{-1/2}). Root-(n) is possible only after a proved aggregate influence weighting; no (M)-normalisation or operator norm is displayed. Reusing evaluation data to fit derivative objects would also create product/U-statistic terms. | Define which fold estimates (A,K), which fold evaluates the influence, the weighted (ell^2)-to-direct-sum-HS operator, and prove its root-(n) concentration. | C | OPEN — EXACT LEMMA STATED | Dimension-free local G1 does not itself prove FRAME-IF. |
| HS/operator separation | A/B retain (G_{2,{\rm HS},n}) for the frame coefficient and (A_{2,n}) only for final operator assembly. | Keep this separation; no rank-free switch is allowed. | C | PROVED | Counterexample C4 is survived. |
| Mask and dependence | B requires a common mask and exact finite-memory split but supplies no calculation of retained mass, local moment defects, or masked-to-unmasked target error. FRAME-IF merely says to include them. | Target the exact masked finite-array row or add the first-order mask discrepancy. State retained (N_h\asymp n) and disjoint innovation sets. | C | OPEN — EXACT LEMMA STATED | A mask defect cannot be squared as a nuisance remainder. |
| Final row assembly and gap | Conditional on a genuine direct-sum row error, (2A_2d+d^2), the actual (\Delta_n), Davis–Kahan, and the row singular-value square are correct. | Require (A_{2,n}=O(1)) or retain it explicitly, require (2A_2d+d^2=o_p(\Delta_n)), and use (s_n^2) only after the factorisation comparison. | C | PROVED UNDER EXPLICIT ASSUMPTIONS | The oracle loading and (O_p(n^{-1})) null spectrum are only downstream implications of FRAME-IF. |
| Same-law counterexample | A and B correctly reject generic observational non-identifiability under a unique Fréchet path and fixed connection. Their phrase “different target under the same law is not identifiable” must not be read as an existing pair inside that class. | Cite Proposition C1; any contrary pair must relax uniqueness, path selection, connection, or lag-range identification. | C | PROVED | Gate C remains unavailable. |
| Status discipline | A uses “OPEN beyond naive plug-in” and “OPEN; invariant-only target change DISPROVED”; B uses “PROVED CONDITIONALLY” and qualified combined status cells. These are not among the five allowed labels. | Replace each with exactly `PROVED`, `PROVED UNDER EXPLICIT ASSUMPTIONS`, `DISPROVED`, `SUPERSEDED`, or `OPEN — EXACT LEMMA STATED`, moving scope qualifications into prose. | C | DISPROVED | Mechanical status verification currently fails. |

### First-pass edge audit

| Edge family | A/B result after attack | Status |
|---|---|---|
| flat Hilbert and one fixed commuting SPD flat | A.1 curvature integral vanishes; B must not estimate or subtract a non-rigid frame term | PROVED |
| common rigid skew | correctly quotiented; finite-error gauge wording needs first-order qualification | PROVED UNDER EXPLICIT ASSUMPTIONS |
| CE-B5 | GLO-only and fixed-fold claims fail; FRAME-IF would have to subtract the full commutator influence | OPEN — EXACT LEMMA STATED |
| zero signal | frame coefficient vanishes and loading gap vanishes | PROVED |
| zero idiosyncratic noise, moving estimated centre | A.1 retains curvature transport derivative; noise-free data do not remove it | PROVED |
| constant curvature, moving mean | geometric derivative is explicit, but no feasible statistical producer/rate is supplied | OPEN — EXACT LEMMA STATED |
| high-dimensional bounded total energy | HS concentration is available, full inverse-Hessian/derivative operator estimation is not | OPEN — EXACT LEMMA STATED |
| one bad grid vertex | A retains the cell quadratic and tube maximum; B's aggregate operator must show its vertex weighting | OPEN — EXACT LEMMA STATED |
| high-frequency small-amplitude path | A correctly rejects bounded length as a replacement for acceleration | DISPROVED |
| nearly commuting, changing eigenbasis | both reject raw commutators; direct ribbon/derivative defect is still missing | DISPROVED |
| identical observable law, different target | no valid pair survives Proposition C1's retained class | DISPROVED |

### Concise mandatory repairs after pass 1

1. Re-derive A.1 with explicit endpoint-generator definitions, curvature orientation, and fixed signs.
2. Split A.5 into fixed-integrand geometric derivative and lag-law score derivative; remove double counting.
3. Replace A-IF's impossible direct (o_p(n^{-1/2})) coefficient-estimation requirement by B's asymptotic-linear FRAME-IF convention.
4. Define (r_\delta) and repair the plug-in envelopes and observable synchronization scope.
5. Write the finite-dimensional one-step estimator and orthogonality derivative with (Psi'=-A), exact signs, folds, masks, and an explicit nonempty curved DGP.
6. Prove aggregate validation/evaluation influence concentration from local vertex scores, including (M)-weights, dependence, and direct-sum HS norms.
7. Keep mask/target error first order, retain (G_{2,{\rm HS},n}) for frame coefficients, and propagate only through (2A_2d+d^2) and the actual (\Delta_n).
8. Replace every nonallowed status label mechanically.

**First hostile-pass verdict: OPEN — EXACT LEMMA STATED.** Gate A and Gate C remain unavailable. Gate B is not yet earned because the restricted one-step estimator is not written/proved with fixed signs and a nonempty example. Gate D is the honest current result, with B's FRAME-IF as the correct statistical form after A's geometric sign and derivative repairs.

If Lemma FRAME-IF is proved with (r_e,r_F=O_p(\ell_n)), then (\ell_n^2=o(n^{-1/2})) at (b_n=n^{-1/7}), the FRAME-DB residual requirement follows, and APP-B plus (5.1)–(5.2) yields the oracle row, loading, and null-spectrum conclusions under the actual gap conditions. If it fails, the failure must identify which of pathwise differentiability, feasibility, second-order remainder, or HS concentration is impossible; a failed pointwise Ω estimator is not enough.

### Hostile conditions the lemma must not hide

- The Fréchet influence is (\bar H_t^{-1}\log_{\mu_t}X) only after specifying the observation-law perturbation, signs, local smoothing design, and inverse population Karcher Hessian. The random observation Hessian (H_t) in APP-B is a different object.
- The derivative of parallel transport is an integral curvature/Jacobi operator along the actual mean-path ribbon, with endpoint terms. “Curvature times area” is not an influence formula.
- A nonparametric estimate of the derivative operator may require curvature/connection derivatives and path acceleration. Their constants and estimation rates must be uniform in dimension and grid count.
- Local stationarity creates a triangular-array functional, not iid copies from one fixed (P). The influence row must match the finite-array target and split mask.
- The correction may need nuisance estimates of conditional lag laws. If so, their products and rates must be displayed; using population Γ inside the score is infeasible.
- Gauge projection must be defined from observables and must be equivariant. A Procrustes alignment to the true frame is only a proof comparison.

## 8. Candidate-class verdict ledger

| Class | Exact hostile verdict | Weakest repair | Status |
|---|---|---|---|
| Plug-in pointwise Ω | residual is (2.2)–(2.4); noisy-frame differences alone are unidentified and an (O_p(\ell_n)) Ω rate is insufficient | broader synchronized coefficient estimation remains in FRAME-IF | DISPROVED |
| Influence/Jacobi | no valid observational-equivalence impossibility under C1; all endpoint, Karcher, path, and lag-law derivatives are required | Lemma FRAME-IF | OPEN — EXACT LEMMA STATED |
| Multi-fold/jackknife/Richardson | fixed-fold target-preserving linear weights cannot cancel realised (n^{-3/7}) nuisance noise | a genuinely orthogonal evaluation score, not fold averaging alone | DISPROVED |
| Frame-avoiding/gauge-invariant | invariant spectra change the estimand; pairwise transports reintroduce synchronization unless they reconstruct T1 | prove cycle-consistent reconstruction of T1 up to one common (Q) with second-order centre sensitivity | invariant-only class DISPROVED; synchronization class OPEN |

## 9. First hostile-pass checklist for A and B

The following objections will be applied from observables to the final loading theorem.

| Claim attacked | Required evidence | Consequence if absent |
|---|---|---|
| Ω or frame influence is estimated | observable formula and common-gauge equivariance; no truth alignment in computation | correction infeasible |
| a Jacobi ribbon is evaluated | endpoints, fibres, orientation, path, grid, curvature and connector terms typed | derivative incomplete |
| fold averaging cancels first order | Gateaux derivative in every nuisance direction, not mean-zero fold noise | first-order term retained |
| conditional centring | disjoint finite-memory innovations or full conditional dependence/coupling theorem | leakage retained |
| HS frame coefficient | (G_{2,{\rm HS}}) or a proved rank restriction | dimension/rank gap |
| pairwise/invariant redesign estimates loading | equality to T1 up to one common (Q) | changed estimand |
| oracle loading rate | direct-sum row residual, (5.1), actual (\Delta_n), and (o_p(\Delta_n)) | no Davis–Kahan conclusion |
| (O_p(n^{-1})) null spectrum | corrected row-operator square (5.2) | Weyl is insufficient |

## 10. Claim ledger

| ID | Exact claim | Observable inputs | Unobservable comparison | Norm | Producer | Consumer | Rate | Objection | Resolution | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | T1 is a functional of the observable law under unique means/fixed connection | marginal and lag laws, known geometry | chosen anchor coordinates | common-gauge row | Section 1 | impossibility audit | exact | latent frame confused with estimator frame | Proposition C1 | PROVED |
| C2 | noisy frame outputs alone do not identify Ω | reported frames only | true relative frame | coefficient HS | Section 2 | naive plug-in | none | class omits raw law | scope stated exactly | DISPROVED |
| C3 | fixed-​K linear folds retain (r_n) noise | fold nuisance estimates | true nuisance | scalar row projection | Section 3 | jackknife audit | (r_n) | deterministic bias may cancel | stochastic subexperiment | DISPROVED |
| C4 | operator lag energy cannot bound HS commutator dimension-uniformly | bounded-energy lag law | none | HS versus operator | Section 5 | frame rate | factor (\sqrt k) | realisability | finite-state construction | DISPROVED |
| C5 | one-step route reduces to FRAME-IF | raw observations, geometry, trained laws | true functional derivative | direct-sum HS | Section 7 | possible Gate A/B | second order required | no full derivative/rate theorem yet | exact lemma isolated | OPEN — EXACT LEMMA STATED |

## 11. Nuisance ledger

| Nuisance | First-order coefficient | Proposed estimate/cancellation | Training fold | Evaluation fold | Residual | Required rate | Identifiability status |
|---|---|---|---|---|---|---|---|
| mean error (e_t) | APP-B GLO maps | inverse Karcher influence/orthogonal score | exact independent training | lag rows | mean second order plus IF error | (o(n^{-1/2})) in row HS | functional identified; estimator lemma open |
| non-rigid frame | (\Omega_t\Gamma_{t,h}-\Gamma_{t,h}\Omega_{t-h}) | full transport derivative or synchronized coefficient estimate | exact independent training | lag rows | (2.3) plus products | (o(n^{-1/2})) direct-sum HS | pointwise Ω unnecessary; functional derivative open |
| common rigid gauge | common conjugation | observable equivariant synchronization | either | either | zero intrinsically | exact quotient | identified only modulo common (Q), as desired |
| lag target law | direct lag expectation and derivative terms | empirical influence row | trained nuisance only | retained lag products | oracle fluctuation | (O_p(n^{-1/2})) | identified under target/mask convention |
| mask/dependence | target mismatch/coupling | exact common mask and finite-memory split | disjoint innovations | retained cores | explicit additive defect | (o(n^{-1/2})) for oracle equivalence | not removed by orthogonality |

## 12. Second hostile cross-audit of repaired dossiers

This is a fresh audit of the frozen repaired A and B dossiers. The complete chain remains open at one aggregate influence lemma; the repaired pathwise geometry and downstream row algebra do not close its feasibility or concentration producers.

### 12.1 Complete-chain audit

| Required link | Fresh attack | Surviving conclusion | Status |
|---|---|---|---|
| Exact gauge | A (A.6) combines coordinate conjugation and a separately chosen common left generator. Pure coordinate change gives \(Q\Omega Q^*\); changing common anchor alignment adds one time-constant skew at first order. | Split the two actions, quotient only the constant skew, and conjugate raw row and correction together. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Smooth derivative | A (A.1) defines connector generators, gives signs \((-E_b,+E_a)\), and derives \(R(T,V)\). | The smooth fixed-observation identity is typed and sign-consistent under its curvature convention. | PROVED |
| Polygon | A retains completed and partial cells, endpoint matching, \(Mr_N^2\), \(M^{-2}\), maximum/tube, and acceleration. | For deterministic \(M\asymp\bar\ell^{-2/3}\) and uniform geometry, the remainder is \(O_p(\ell^{4/3})=o_p(n^{-1/2})\). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Law derivative | A separates fixed-\(x\) geometry (A.8) from the lag-pair score (A.9). B retains direct lag-law influence in the base row. | No double count remains; \(D\Psi=-A\), \(\widehat e=-\widehat A^{-1}\widehat\Psi\), and \(T+KA^{-1}\Psi\) have the correct sign. | PROVED |
| Identifiability | Unique Fréchet path and fixed connection/path determine the target modulo common conjugation. Fitted-frame differences and arbitrary external frames do not identify a truth-relative error. | Gate C is unavailable; identification supplies no rate. | PROVED |
| Plug-in | B gives a coefficient-conditional direct-sum HS inequality with shifted action norms and \(G_{2,{\rm HS}}\), but \(\delta\), truth alignment, and synchronization are not observable producers. | The inequality survives; no generic feasible plug-in theorem is earned. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Correction fluctuations | B retains \(\beta_\delta\), \(R^2r_\delta n^{-1/2}\), every \(\widetilde\Omega a\) and \(\widetilde\Omega Y\otimes a\) product, and triple products via action/sup norms. | No RMS-only triple-product shortcut remains. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Correction noise | A/B put unavoidable root-\(n\) correction-score noise in the leading influence row and reserve \(d_{F,{\rm db}}\) for the remainder. | Proposition C2c no longer contradicts FRAME-IF. | PROVED |
| One-step feasibility | B (B.7) is observable conditional on fitted \(K,A^{-1}\), validation score, evaluation row, and synchronization. None is jointly constructed at the required rate on a curved nonparametric class. | Architecture is specified; feasibility is open. | OPEN — EXACT LEMMA STATED |
| Aggregate concentration | Vertex local scores are not root-\(n\). B asks for \(M\), weight norms, and \(\lVert KA^{-1}\rVert_{\ell_M^2\to\oplus {\rm HS}}\), but proves no aggregate concentration or nuisance-product theorem. | G1 and oracle HS concentration do not imply FRAME-IF. | OPEN — EXACT LEMMA STATED |
| HS residual | A (A.10)–(A.11) and B FRAME-IF have the right asymptotic-linear form and retain polygon, quadratic, \(o_p(n^{-1/2})\), and mask terms. | The desired residual follows only if the observable producers and concentration are proved. | OPEN — EXACT LEMMA STATED |
| Dimension/rank | Bounded energy does not estimate \(A^{-1}\) or \(K\) in operator norm. Frame coefficients use HS lag energy and no rank is hidden. | Generic growing-\(p_n\) closure remains open. | OPEN — EXACT LEMMA STATED |
| Mask/coupling/target | A/B target one masked finite-array row and require exact finite-memory colour separation, but do not prove retained mass, local moment, synchronization, or approximate-coupling bounds. | No unmasked or infinite-memory shortcut is earned. | OPEN — EXACT LEMMA STATED |
| Mean/frame separation | B conservatively retains \(\varepsilon_G\ell\) under the brief's GLO package; frame and direct lag-law channels remain distinct. | No mean error is relabelled frame error. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Assembly/gap | Given a genuine row error, \(2A_2d+d^2\), actual \(\Delta_n^{-1}\), and the row singular-value square are correct. | Require assembly \(o_p(\Delta_n)\); use \(s_n^2\) only after factorisation. | PROVED |
| Null spectrum | \(\widehat\lambda_{r+1}\le d^2\) uses row singular values, not Weyl. | \(O_p(n^{-1})\) is downstream of a root-\(n\) corrected row. | PROVED UNDER EXPLICIT ASSUMPTIONS |

### 12.2 All mandatory edge families

| Edge | Fresh verdict | Status |
|---|---|---|
| Flat Hilbert | Non-rigid frame influence is zero; mean terms stay separate. | PROVED |
| Fixed commuting SPD flat | Exact log-coordinate reduction only when all estimator objects stay in the flat. | PROVED |
| Common rigid skew | Quotient conjugation; no additive residual or gap cost. | PROVED |
| CE-B5 | GLO/splitting leave the commutator; no feasible FRAME-IF producer is proved. | OPEN — EXACT LEMMA STATED |
| Zero signal | Frame coefficient and loading gap both vanish. | PROVED |
| Zero idiosyncratic noise | Moving-centre curvature influence can remain through signal vectors. | PROVED |
| Constant curvature/moving mean | Geometry is explicit; fitted aggregate Hessian/score/mask theorem is not. | OPEN — EXACT LEMMA STATED |
| High-dimensional bounded energy | HS concentration survives; inverse-Hessian/derivative estimation does not follow. | OPEN — EXACT LEMMA STATED |
| One bad vertex | A retains the maximum, \(Mr_N^2\), and tube event; B leaves aggregate grid production open. | OPEN — EXACT LEMMA STATED |
| High-frequency small amplitude | Length cannot replace acceleration. | DISPROVED |
| Nearly commuting/changing basis | Raw commutators do not imply one flat or the ribbon defect. | DISPROVED |
| Same observable law/different decomposition | No different Paper 1 target survives the retained uniqueness, path, connection, and lag-range assumptions. | DISPROVED |

### 12.3 Invalid labels and stale claims found during pass 2 — SUPERSEDED after lead repair

The numbered items below record defects as found during pass 2. The lead repaired them after this audit; they are not current objections. **Status: SUPERSEDED.**

1. B Section 3 still uses `PROVED CONDITIONALLY`, which is not allowed; replace it by `PROVED UNDER EXPLICIT ASSUMPTIONS`.
2. B Section 5 combines “DISPROVED” and plain “OPEN”; split it and use `OPEN — EXACT LEMMA STATED`.
3. B Section 9 uses qualified status strings (“DISPROVED without coefficient producer,” “PROVED existing branch,” “DISPROVED GLO-only claim,” “PROVED distinction,” “PROVED boundary”). Move qualifications into the verdict column.
4. B Section 10 is stale pass-1 text keyed to pre-repair A numbering: its references to A.4, A.5, and A-IF(3) no longer match repaired A. Mark that section `SUPERSEDED` or rewrite it against A (A.7)–(A.12).
5. B Section 10 also combines multiple status labels in cells; split the claims.
6. A labels use the permitted set. A (A.6) should still split coordinate conjugation from common-anchor generator addition.
7. The former C Section 12 recommendation is retained below as historical pre-audit text and is superseded by this section.

### 12.4 Exact smallest remaining lemma

> **FRAME-IF — aggregate gauge-equivariant one-step row lemma.** Under the canonical bounded-total-energy, fixed-rank/lag/memory, exact finite-memory three-colour split, GLO, unique Fréchet path, fixed Levi–Civita/path convention, and dimension-uniform generated-tube assumptions, with deterministic \(M_n\asymp\bar\ell_n^{-2/3}\), construct from observable folds a common-gauge-equivariant corrected row \(\widehat{\mathfrak T}^{db}_n\) and direct-sum HS influence row \(\varphi_{n,P}\) such that:
>
> 1. computation uses no true centre/frame/anchor, \(e,\Omega,\Gamma\), or unobserved ribbon;
> 2. the nuisance derivative contains inverse Karcher influence and every base-log, smooth/polygon transport, radial endpoint, completed-cell, partial-cell, and synchronization derivative, while direct lag-law influence remains in the base row;
> 3. vertex weights, \(M_n\), geometry, inverse-Hessian, lag-energy, synchronization, mask, and dependence producer norms are explicit and dimension-uniform, with \(G_{2,{\rm HS}}\) for frame coefficients;
> 4. for the exact masked finite-array target,
> \[
> \widehat{\mathfrak T}^{db}_n-\mathfrak T_n(P)=(P_n-P)\varphi_{n,P}+\mathcal R_n,
> \qquad \lVert(P_n-P)\varphi_{n,P}\rVert_{\oplus {\rm HS}}=O_p(n^{-1/2}),
> \]
> and
> \[
> \lVert\mathcal R_n\rVert_{\oplus {\rm HS}}
> =O_p\{M_n\ell_n^2+M_n^{-2}+r_e^2+r_er_F+r_F^2\}
> +o_p(n^{-1/2})+\rho_{mask,n}+\rho_{CF,n};
> \]
> 5. the vertex maximum is \(o_p(1)\), geometry constants are \(O(1)\), and all nonexact mask/coupling terms are \(o_p(n^{-1/2})\).

At \(b_n=n^{-1/7}\), the polygon term is \(\ell_n^{4/3}=n^{-4/7}=o(n^{-1/2})\). This lemma would unlock the root-\(n\) row, \(n^{-1/2}/\Delta_n\) loading rate, and \(O_p(n^{-1})\) null spectrum through proved deterministic consumers.

**Status: OPEN — EXACT LEMMA STATED.**

### 12.5 Final gate recommendation

**Gate D — exact irreducible open lemma.** Gate A lacks the observable generic producer and aggregate HS theorem. Gate B lacks a fully instantiated nonempty curved class closing derivative, synchronization, mask, and concentration inputs. Gate C is blocked by Proposition C1 under the retained identifiable model. The robust \(n^{-3/7}\) theorem remains the fallback.

## 12H. Historical pre-audit recommendation

Before the A/B drafts are audited, Gate C is not earned: Proposition C1 blocks the obvious generic observational-equivalence theorem. Gate A is also not earned: no feasible correction has yet proved Lemma FRAME-IF or an equivalent synchronized coefficient theorem. The honest present position is Gate D with the exact lemma in Section 7, subject to the two mandatory hostile passes and any repair supplied by A or B.

The surviving robust fallback is unchanged:

\[
d_n=O_p(n^{-1/2}+\ell_n),
\qquad
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
=O_p\{(n^{-1/2}+\ell_n)/\Delta_n\}.
\]

**Status: OPEN — EXACT LEMMA STATED.**
