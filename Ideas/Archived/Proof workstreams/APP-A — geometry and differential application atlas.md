---
type: proof-dossier
title: APP-A — geometry and differential application atlas
status: noncanonical-workstream
authority: noncanonical-workstream
scope: Paper 1 application map; geometry and uniform differentials only
last-audited: 2026-08-08
---

# APP-A — geometry and differential application atlas

> **NONCANONICAL WORKSTREAM.** Proof evidence for the Paper 1 application-map run. It does not supersede [[HD1 — growing-dimension Paper 1 proof dossier]]. Paper 2 is out of scope. APP-B owns the final statistical oracle theorem.

## 0. Verdict

1. **T-APP-1 — PROVED UNDER EXPLICIT ASSUMPTIONS.** A Hilbert space, unconstrained symmetric matrices with the Frobenius metric, or one fixed common AIRM commuting SPD flat gives an exact Hilbert reduction when the centre, observations, loading/noise directions, barycentres, Richardson points, blend, connectors, and polygonal segments remain in that same convex flat. Exp, Log, PT, the observation Hessian, base-change error, connector error, and ribbon holonomy become Euclidean. Mean error remains exact additive recentering error and is first order pathwise. Flatness alone does not imply an oracle loading rate.
2. **T-APP-2 — PROVED.** On a fixed spectral band \(cI\preceq A\preceq CI\), every fixed-order (\(\le4\)) AIRM differential consumed by HD-G—Exp, Log, radial PT/connectors, Hessian and its derivatives, Richardson/base-point remainder, blend, and ruled-surface maps—has an operator bound independent of matrix size in the AIRM/Frobenius project norms. Direct matrix calculus is essential: a generic Jacobi estimate through AIRM distance can hide a spurious \(\sqrt m\).
3. The band does **not** imply bounded total tangent energy: \(d_{\rm AIRM}(I,eI)=\sqrt m\). HD-X total energy and mean-length assumptions remain separate.
4. Local symmetry \(\nabla R=0\) is a differential-control property, not a cancellation property. Full AIRM SPD is locally symmetric but retains curvature, holonomy, and random Hessians.

## 1. Term-level geometry ledger

With \(e_t=\log_{\mu_t}\hat\mu_t\), \(Y_t=\log_{\mu_t}X_t\), and radial connector \(\Phi_{e_t}\),

\[
\Phi_{e_t}^{-1}\log_{\hat\mu_t}X_t
=Y_t-H_te_t+\mathcal R_t,\qquad
H_t=\tfrac12\operatorname{Hess}_{\mu_t}d(\mu_t,X_t)^2,\quad
\|\mathcal R_t\|\le C\|e_t\|^2. \tag{1.1}
\]

| ID | Exact term | Flat/common-flat effect | \(\nabla R=0\) effect | Status / proof |
|---|---|---|---|---|
| MB1 | stage bias \(\pm cbA_1+c^2b^2A_2+O(b^3+n^{-a}+n^{-1})\) | smoothing terms remain | constants only | **PROVED**, HD1-A Lemma 5.1 |
| MB2 | Richardson base-change \(\mathcal C=O(r^3)\) | exactly zero | bounded, generally nonzero | **PROVED**, §§2,5 |
| MS | score fluctuation \((nb)^{-1/2}\) / sup \(\sqrt{\log n/(nb)}\) | unchanged | unchanged | **PROVED**, HD1-A §§4,6 |
| MD | derivative fluctuation \((nb^3)^{-1/2}\), defect \(n^{-a}/b\) | unchanged | unchanged | **PROVED**, HD1-A §7 |
| LOG1 | \(-H_te_t\) | exactly \(-e_t\), still linear | \(H_t\) remains random | **PROVED**, §2; HD1-B §4 |
| LOG2 | \(\mathcal R_t=O(\|e_t\|^2)\) | exactly zero | bounded, nonzero | **PROVED**, §§2,5 |
| CON | endpoint connector | identity in affine trivialisation | controlled, not identity | **PROVED**, §§2,5 |
| HOL | ribbon/polygon holonomy | zero on simply connected flat tube | generally nonzero | **PROVED**, §3; canonical T31/T54 |
| POLY | frame term \(\Lambda\{L_\mu\ell+M\ell^2+M^{-2}\}\) | zero as frame error | same order, uniform constants | **PROVED**, HD1 PF |
| LIN | \(-H_te_t\otimes Y_{t-h}-Y_t\otimes H_{t-h}e_{t-h}\) | \(H=I\), terms remain pathwise | no cancellation | **PROVED**, §2; HD1-B §4 |
| QUAD | two-error/Taylor lag terms | \(O(\ell^2)\) | \(O(\ell^2)\) | **PROVED**, HD1-B B5 |
| ROW/OP | \(d_n\), \(\eta_n=2A_{2,n}d_n+d_n^2\) | improves only if LIN centred | none | **PROVED**, HD1 §§3–4 |
| DK/EV | \(\sin\Theta/\Delta_n\), \(\hat\lambda_{r+1}\le d_n^2\) | only through \(d_n\) | unchanged | **PROVED**, HD1 §§3–4 |

Flatness kills HOL, not LIN.

## 2. T-APP-1 — exact flat reduction

### 2.1 Hilbert and symmetric-Frobenius cases

For a real Hilbert space,

\[
\operatorname{Exp}_qv=q+v,\quad \operatorname{Log}_qx=x-q,\quad
P=I,\quad H(q,x)=I,\quad R=0. \tag{2.1}
\]

Probability barycentres are arithmetic means, and if \(\sum\lambda_j=1\),
\[
\mathcal R(x_1,x_2,x_3)=\sum_j\lambda_jx_j. \tag{2.2}
\]
Thus all base-change derivatives above first order, connectors, and holonomy vanish. The vector space \({\rm Sym}(m)\) with Frobenius metric is exactly this case, of dimension \(m(m+1)/2\). The SPD cone with the *induced Frobenius* metric is only an incomplete open flat region; signed affine combinations require a spectral-interior event. **PROVED.**

### 2.2 One common commuting AIRM flat

Fix orthogonal \(Q\) and
\[
\mathcal F_Q=\{Q\operatorname{diag}(e^{z_1},\ldots,e^{z_m})Q^T:z\in\mathbb R^m\}. \tag{2.3}
\]
For \(A(z)\in\mathcal F_Q\) and
\(U=Q\operatorname{diag}(e^{z_i}u_i)Q^T\),
\[
\|U\|_{A(z)}^2=\operatorname{tr}(A^{-1}UA^{-1}U)=\sum_i u_i^2. \tag{2.4}
\]
The AIRM geodesic is \(A((1-t)z+tw)\), hence \(\mathcal F_Q\) is complete, flat, convex, and totally geodesic. Positive barycentres of supported laws lie in their closed convex hull; Richardson, the geodesic blend, and polygonal chords remain in \(\mathcal F_Q\). If the centre, observations, loadings/noise, and all estimator stages use this same \(Q\), Paper 1 is exactly the Hilbert factor problem in log-eigenvalue coordinates. **PROVED.**

### 2.3 What remains, and when cross-fitting helps

In one flat,
\[
\widehat Y_t=Y_t-e_t,\qquad
\widehat Y_t\otimes\widehat Y_{t-h}-Y_t\otimes Y_{t-h}
=-e_t\otimes Y_{t-h}-Y_t\otimes e_{t-h}+e_t\otimes e_{t-h}. \tag{2.5}
\]
The linear terms remain pathwise, so geometry alone retains the robust \(O_p(\ell_n)\) channel. If a valid leave-block-out construction makes the **whole error field** training-measurable and independent of retained evaluation innovations, with conditional mean zero, fixed memory gives
\[
d_{\rm mean}=O_p\!\left(\ell_n\sqrt{(m_0+h_0+1)/n}+\ell_n^2\right). \tag{2.6}
\]
This is conditional, not pathwise, cancellation (HD1-B B5 with \(H=I\)). At \(b=n^{-1/7}\), \(a\ge3/7\), \(\ell_n=n^{-3/7}\), both added terms are \(o(n^{-1/2})\). **PROVED UNDER THE EXPLICIT SPLIT.**

Flatness alone fails: let iid Rademacher \(Y_t\in\mathbb R\), \(h=1\), and \(e_t=\varepsilon Y_{t-1}\). Then the oracle lag covariance is zero but
\[
\mathbb E[(Y_t-e_t)(Y_{t-1}-e_{t-1})]=-\varepsilon. \tag{2.7}
\]
This attacks geometry plus an RMS error bound, not the correctly cross-fitted HD1 estimator. **DISPROVED: \(R=0\Rightarrow\) oracle recovery.**

## 3. Flatness, local symmetry, relevant planes, and law symmetry

### 3.1 Global/support-tube flatness

If \(R=0\) on a simply connected convex tube containing every curve, connector, and ribbon, PT is path-independent and the Hilbert reduction holds. Topology is separate: a flat Klein bottle has nontrivial linear holonomy; a flat torus has cut loci and can have multiple Fréchet means (canonical analytical reconstruction §4.3). **PROVED / analytic counterexamples.**

### 3.2 Relevant-plane flatness

The connection-variation identity contains the endomorphism
\[
R(\partial_sS,\partial_\tau S). \tag{3.1}
\]
The exact local condition killing ribbon holonomy is that (3.1) is zero everywhere, not merely that one sectional-curvature scalar is zero. For AIRM,
\[
R_I(U,V)W=-\tfrac14[[U,V],W], \tag{3.2}
\]
so \([U,V]=0\) kills the entire curvature operator. A common commuting flat enforces this. **PROVED.**

### 3.3 Local symmetry and constant curvature

Local symmetry deletes \(\nabla R\) forcing from differentiated Jacobi equations but does not delete (3.1). At \(I\in\mathcal P(2)\), take
\[
U=2^{-1/2}\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
V=2^{-1/2}\begin{pmatrix}0&1\\1&0\end{pmatrix}. \tag{3.3}
\]
Then \([U,V]\ne0\), so a small \(U,V\) geodesic rectangle has holonomy
\(I+{\rm area}\,R(U,V)+o({\rm area})\ne I\), although AIRM SPD has \(\nabla R=0\). HD1-B B4 gives a separate locally symmetric hyperbolic law with nonzero first-order recentering. **DISPROVED: \(\nabla R=0\) implies cancellation.**

For constant \(K\ne0\),
\[
R(U,V)W=K\{\langle V,W\rangle U-\langle U,W\rangle V\}, \tag{3.4}
\]
and the squared-distance Hessian has radial eigenvalue \(1\), transverse eigenvalue \(r\sqrt K\cot(r\sqrt K)\) for \(K>0\) or \(r\sqrt{-K}\coth(r\sqrt{-K})\) for \(K<0\). These are explicit, not zero. Compact cases require quantitative conjugacy/cut and Hessian margins. **PROVED/CITED**, canonical G1 §7 and T38.

### 3.4 Distributional cancellation

On a locally symmetric space, geodesic symmetry \(s_q\) gives
\[
H(q,s_qx)=H(q,x),\qquad ds_q=-I. \tag{3.5}
\]
Joint transported sign symmetry at every consumed lag makes the GLO integrands odd, hence zero in expectation. Summands do not vanish pathwise; cross-fitting/dependence separation is still needed for the \(O_p(\ell/\sqrt n)\) fluctuation. **PROVED**, HD1-B §4.

## 4. Commutation and defects

Global pairwise commutation of a family of real symmetric matrices implies simultaneous diagonalisation. “Commuting at each time” does not. Let
\[
A_1=\operatorname{diag}(2,1),\quad A_2=I,\quad
A_3=R_\theta\operatorname{diag}(2,1)R_\theta^T,\quad
\theta\notin\tfrac\pi2\mathbb Z. \tag{4.1}
\]
Adjacent pairs commute, but \(A_1,A_3\) do not. A repeated-eigenvalue time can hide a basis change. **DISPROVED: time-local commutation implies one fixed flat.**

For a proved approximate statement, whiten at the base and write \(Y=D+N\), with \(D,e\) in one diagonal algebra and \(\|Y\|_{\rm op}\le L\). The AIRM Hessian is an even analytic function \(f({\rm ad}_Y)\), so
\[
\|(H_Y-I)e\|_F\le C_L\|N\|_F\|e\|_F. \tag{4.2}
\]
Indeed \({\rm ad}_Y\) and \({\rm ad}_D\) are self-adjoint on the Frobenius matrix Hilbert space, their spectra lie in a fixed real interval depending only on \(L\), and \(f(s)=(s/2)\coth(s/2)\) is analytic on a complex neighbourhood of that interval. Cauchy functional calculus gives
\[
\|f({\rm ad}_Y)-f({\rm ad}_D)\|_{F\to F}
\le C_L\|{\rm ad}_N\|_{F\to F}
\le2C_L\|N\|_{\rm op}.
\]
Since \([D,e]=0\), \(f({\rm ad}_D)e=e\), and \(\|N\|_{\rm op}\le\|N\|_F\), this proves (4.2). This replaces the former power-series justification, whose Taylor radius need not cover an arbitrarily wide fixed spectral interval. Thus a fixed-algebra defect \(\|N_t\|_F\le\varepsilon_n\) yields \(O(\varepsilon_n\ell_n)\) linear Hessian mismatch. This requires centre/loading alignment with the same algebra; a small selected commutator alone is diagnostic only. **PROVED UNDER DISPLAYED ASSUMPTIONS.**

Define the curvature density on the ribbon planes by
\[
\varepsilon_{R,n}
=\sup_{s,\tau}
\frac{\|R(\partial_sS,\partial_\tau S)\|_{\rm op}}
{\|\partial_sS\wedge\partial_\tau S\|},
\tag{4.3}
\]
with ratio zero when the wedge vanishes. Connection variation gives
\(\|{\rm Hol}-I\|\le C\varepsilon_{R,n}{\rm Area}(S)\); in AIRM, (3.2) converts this to a normalised whitened-commutator bound. Equivalently, if the defect is defined without the denominator as \(\sup\|R(\partial_sS,\partial_\tau S)\|_{\rm op}\), its integral is over parameter area and must not be multiplied by geometric area again. **PROVED after typing correction.**

## 5. T-APP-2 — dimension-free AIRM finite-order calculus

### 5.1 Theorem in the project norms

Let
\[
\mathcal B_m(c,C)=\{A\in\mathcal P(m):cI\preceq A\preceq CI\},\qquad
\|U\|_A=\|A^{-1/2}UA^{-1/2}\|_F. \tag{5.1}
\]

> **Theorem AIRM-HD-G — PROVED.** Fix \(k_0<\infty\) (HD1 uses \(k_0=4\)) and the fixed Richardson coefficients. On band inputs and the fixed expanded bands containing Richardson/blend images, the covariant differentials through order \(k_0\) of
> \[
> \operatorname{Exp}_A(U),\quad \operatorname{Log}_A(B),\quad
> \Phi_{A\to B}U,\quad H(A,B),\quad
> \mathcal R(A_1,A_2,A_3) \tag{5.2}
> \]
> and the consumed ruled-surface maps have induced multilinear norms bounded by \(C_k(c,C,\|\lambda\|_1)\), independent of \(m\). Exp arguments are logs between band points or their fixed Richardson combinations. These are exactly the AIRM/Frobenius Hilbert norms used by HD1, not arbitrary mixed matrix norms.

### 5.2 Dimension-free matrix calculus

Band metric equivalence and the only product inequality needed are
\[
C^{-1}\|U\|_F\le\|U\|_A\le c^{-1}\|U\|_F,\qquad
\|XYZ\|_F\le\|X\|_{\rm op}\|Y\|_F\|Z\|_{\rm op}. \tag{5.3}
\]
Inverse derivatives are finite words in \(A^{-1}\) and perturbations. For \(S=A^{1/2}\), \(X=D(A^{1/2})[H]\) solves
\[
SX+XS=H. \tag{5.4}
\]
In an eigenbasis, \(X_{ij}=H_{ij}/(s_i+s_j)\), so the inverse Sylvester map has Frobenius norm at most \((2\sqrt c)^{-1}\). Repeated differentiation of \(S^2=A\), followed by induction using (5.3), proves dimension-free fixed-order derivatives of \(A^{1/2}\), hence also \(A^{-1/2}\).

For symmetric \(Z\), time-ordered integrals give
\[
\|D^k\exp_Z[H_1,\ldots,H_k]\|_F
\le k!e^{\|Z\|_{\rm op}}\prod_i\|H_i\|_F. \tag{5.5}
\]
For \(X\succeq aI\), the resolvent formula gives
\[
D^k\log_X[H_1,\ldots,H_k]
=(-1)^{k-1}\sum_\pi\int_0^\infty
R_tH_{\pi(1)}R_t\cdots H_{\pi(k)}R_t\,dt,\qquad
R_t=(X+tI)^{-1},
\]
\[
\|D^k\log_X[H_1,\ldots,H_k]\|_F
\le (k-1)!a^{-k}\prod_i\|H_i\|_F. \tag{5.6}
\]
If \(A,B\in\mathcal B_m(c,C)\), with \(\kappa=C/c\),
\[
\kappa^{-1}I\preceq A^{-1/2}BA^{-1/2}\preceq\kappa I,\qquad
\|\log(A^{-1/2}BA^{-1/2})\|_{\rm op}\le L:=\log\kappa. \tag{5.7}
\]
Chain rule, (5.3)–(5.7), and the explicit AIRM formulas prove all fixed-order Exp/Log bounds. The Frobenius norm of the unperturbed log may grow as \(\sqrt mL\), but it is used as an operator-norm factor in every product; no eigenvalue sum appears.

### 5.3 PT, Hessian, and Richardson

Set
\[
E(A,B)=A^{1/2}(A^{-1/2}BA^{-1/2})^{1/2}A^{-1/2}.
\]
Then \(EAE^T=B\) and
\[
\Phi_{A\to B}(U)=EUE^T \tag{5.8}
\]
is radial AIRM parallel transport. Its endpoint derivatives are dimension-free by §5.2.

The typed Hessian identity and connection formula are
\[
H(A,B)=-\nabla_A\operatorname{Log}_A(B),\qquad
(\nabla_XY)_A=DY_A[X]-\tfrac12(XA^{-1}Y_A+Y_AA^{-1}X). \tag{5.9}
\]
Iterating (5.9) produces finite sums of the derivatives already bounded, inverse factors, and products, proving the Hessian/higher-covariant-differential claim. More explicitly, with \(Z=\log(A^{-1/2}BA^{-1/2})\), \(H\) is the even functional calculus \(f({\rm ad}_Z)\), \(f(s)=(s/2)\coth(s/2)\), hence
\[
I\preceq H(A,B)\preceq L\coth(L)I. \tag{5.10}
\]

For
\[
\mathcal R(A_1,A_2,A_3)
=\operatorname{Exp}_{A_1}\!\left(\sum_j\lambda_j\operatorname{Log}_{A_1}A_j\right),
\]
the whitened exponent obeys \(\|Z_R\|_{\rm op}\le\|\lambda\|_1L\), so
\[
ce^{-\|\lambda\|_1L}I\preceq\mathcal R\preceq
Ce^{\|\lambda\|_1L}I. \tag{5.11}
\]
Thus the first four differentials are dimension-free on a fixed expanded band. Taylor in normal coordinates supplies, uniformly in \(m\),
\[
\|\mathcal C(x_1,x_2,x_3)\|\le Cr^3,\qquad
\|\nabla_u\mathcal C\|\le Cr^2\{\max_j\|\nabla_ux_j\|+r\|\mu'\|\}. \tag{5.12}
\]
Here the first differential at the diagonal is the affine combination and the second differential vanishes because normal-coordinate Christoffel symbols vanish at the base point and the connection is torsion-free; the uniformly bounded third/fourth differentials above control the cubic remainder and its covariant derivative.
The fixed-width blend is another Exp/Log composition. **This closes the previously explicit HD-G Richardson primitive.**

### 5.4 Ruled/Jacobi constants and the distance trap

At any base point after whitening,
\[
R(U,V)W=-\tfrac14[[U,V],W],\qquad \nabla R=0. \tag{5.13}
\]
Consequently \(\|R(U,V)W\|_F\le\|U\|_F\|V\|_F\|W\|_F\). Along a band geodesic of whitened velocity \(Z\), the sharper bound
\[
\|R(J,Z)Z\|_F\le\|Z\|_{\rm op}^2\|J\|_F\le L^2\|J\|_F \tag{5.14}
\]
makes the Jacobi equation dimension-free. Fixed differentiated variations contain no \(\nabla R\) terms and only finitely many commutator products, bounded by (5.3). Equivalently, the ruled surface is an Exp composition already covered by §5.2. AIRM is Hadamard, so the endpoint Jacobi map is nonsingular. **PROVED.**

A generic comparison using only \(|R|\le1\) and geodesic length \(\|Z\|_F\) could produce a constant depending on \(\sqrt mL\). Equations (5.5) and (5.14) show that this is an artifact of losing the matrix commutator structure.

### 5.5 What conditioning does not buy

For \(A=I\), \(B=eI\), both matrices lie in a fixed band and have condition number one, but
\[
d_{\rm AIRM}(A,B)=\sqrt m. \tag{5.15}
\]
So the band verifies differential constants, not HD-X total energy, trace-class scaling, or bounded mean length. Condition number without absolute \(c,C\) does not even give (5.3). “Every norm” is also false: \(\|I_m\|_*=m\) while \(\|I_m\|_{\rm op}=1\). **DISPROVED: bounded conditioning verifies all HD assumptions/all norms.**

## 6. Other geometry classes

- **Totally geodesic flat — PROVED.** If one complete flat contains centre, support, loading/noise directions, and estimator images, ambient normal curvature is irrelevant and §2 applies.
- **Products — PROVED.** Exp, Log, PT, Hessian, and curvature act componentwise under the \(\ell^2\) product metric. Uniform factor constants give a factor-count-free multilinear bound by Hölder. A product is flat only if every active factor is flat; growing products still require bounded total \(\ell^2\) energy.
- **Bi-invariant Lie groups — PROVED/CONDITIONAL FOR APPLICATIONS.** They are locally symmetric with bracket curvature; fixed Abelian subgroups are totally geodesic flats. Non-Abelian support is curved. Merely left-invariant metrics need not have \(\nabla R=0\). Invariance alone gives no statistical cancellation.
- **Compact symmetric/Grassmann/shape spaces — CONDITIONAL.** Local symmetry controls derivatives but does not remove curvature. A common convex normal tube, quantitative distance from conjugacy/cut loci, positive population Hessian, and dimension-uniform constants remain necessary. On a unit sphere \(r\cot r\to0\) at \(\pi/2\), and its derivative diverges near \(\pi\).
- **Bures–Wasserstein SPD — CAUTION/OPEN for full growing size.** BW is nonnegatively curved and incomplete toward singular PSD matrices; AIRM Hadamard/Sturm/global-Log conclusions do not transfer. Full BW needs its own convex-tube and differential proof. On a fixed diagonal algebra,
\[
d_{\rm BW}^2(\operatorname{diag}a,\operatorname{diag}b)
=\sum_i(\sqrt{a_i}-\sqrt{b_i})^2, \tag{6.1}
\]
so square-root coordinates give an exact flat positive orthant, conditional on a positive boundary margin and diagonal-preserving estimator. **Diagonal BW flat: PROVED; full BW HD-G: OPEN here.**

## 7. Assumption-to-cancellation matrix

| Package | Criterion | Term affected | Mode | Result | Status / location |
|---|---|---|---|---|---|
| Hilbert / symmetric Frobenius | global vector space | MB2, LOG2, CON, HOL, POLY | pathwise | zero geometric error | **PROVED**, §2.1 |
| Common AIRM flat | one fixed \(Q\), all model/estimator objects in \(\mathcal F_Q\) | same | pathwise | exact log-eigenvalue reduction | **PROVED**, §2.2 |
| Flat + valid split | preceding + innovation separation + conditional mean zero | LIN | conditional | \(O_p(\ell/\sqrt n+\ell^2)\) | **PROVED UNDER ASSUMPTIONS**, §2.3 |
| Relevant-plane flat | (3.1) zero on ribbon | HOL | pathwise | zero holonomy | **PROVED**, §3.2 |
| Locally symmetric | \(\nabla R=0\), controlled tube | differential constants | bound | no rate cancellation | **PROVED**, §§3.3,5 |
| Reflection law | local symmetry + simultaneous lag-vector sign invariance | population LIN/GLO | expectation | empirical fluctuation remains | **PROVED**, §3.4 |
| Approximate fixed algebra | \(Y=D+N\), aligned \(D,e\), \(\|N\|\le\varepsilon\) | Hessian part of LIN | bound | \(O(\varepsilon\ell)\) | **PROVED UNDER ASSUMPTIONS**, §4 |
| Full AIRM band | fixed \(c,C\), generated expanded bands | all HD-G differentials | bound | constants only | **PROVED**, §5 |
| Compact symmetric | local symmetry + quantitative tube | differential constants | bound | no cancellation | **CONDITIONAL**, §6 |
| Full BW | separately proved BW tube/calculus | none automatically | — | unknown | **OPEN here**, §6 |

## 8. Geometry-first application matching

| Family | Profile | Feasibility | Geometry conclusion |
|---|---|---|---|
| Euclidean multivariate/functional | Hilbert, total energy separately bounded | **EXACT STRUCTURAL MATCH** | T-APP-1; oracle still needs cancellation design |
| Unconstrained symmetric Frobenius | flat vector space | **EXACT STRUCTURAL MATCH** | T-APP-1 |
| Diagonal covariance/volatility/diffusion AIRM | structural fixed basis | **EXACT STRUCTURAL MATCH** | common flat |
| Jointly diagonalizable SPD | one fixed \(Q\) for centre/support/loadings/noise/estimator | **EXACT STRUCTURAL MATCH** | common flat |
| Nearly fixed-basis SPD | off-algebra defect in project norm, aligned error | **STABLE APPROXIMATE MATCH** | \(O(\varepsilon\ell)\) plus curvature defect |
| Full covariance/correlation SPD AIRM | noncommuting fixed band | **EXACT GEOMETRIC MATCH, NO CANCELLATION** | T-APP-2 + robust HD1 |
| Diffusion tensors with changing eigenvectors | full noncommuting SPD | **DIAGNOSTIC-ONLY for flatness** | T-APP-2 only |
| Functional-connectivity covariance | often noncommuting, small eigenvalues/pervasive energy | **DIAGNOSTIC-ONLY / MODEL-FRAGILE** | band/energy must be justified |
| Product observations | componentwise, total \(\ell^2\) energy | **EXACT STRUCTURAL MATCH** if factors verified | product theorem |
| Sphere/Grassmann/compact shapes | curved locally symmetric examples | **STABLE ONLY WITH TUBE MARGIN** | constants, no cancellation |
| Diagonal BW covariance | fixed diagonal algebra, lower spectral margin | **EXACT STRUCTURAL MATCH** | flat square-root coordinates |
| Full BW covariance | incomplete curved geometry | **UNKNOWN / DIAGNOSTIC-ONLY** | no AIRM transfer |

## 9. Counterexample ledger

| False shortcut | Analytic attack | Correct repair | Status |
|---|---|---|---|
| \(\nabla R=0\) kills recentering/holonomy | noncommuting AIRM \(\mathcal P(2)\); HD1-B B4 | relevant-plane \(R=0\) or GLO | **DISPROVED** |
| \(R=0\) gives oracle loading | (2.7) | conditional centring/independence/debiasing | **DISPROVED** |
| time-local commuting gives fixed flat | (4.1) | one fixed algebra/global pairwise commutation | **DISPROVED** |
| spectral band gives total energy | (5.15) | HD-X total energy separately | **DISPROVED** |
| condition number gives every norm | scale/mixed-norm examples §5.5 | fixed \(c,C\), project norms | **DISPROVED** |
| flat means global Euclidean chart | torus/Klein bottle | simply connected convex tube | **DISPROVED** |
| compact/symmetric means safe Log/Hessian | sphere at \(\pi/2,\pi\) | quantitative margins | **DISPROVED** |
| “symmetric matrices” means flat | full SPD AIRM has (5.13) | state actual metric | **DISPROVED** |
| BW inherits AIRM Hadamard geometry | finite-distance PSD boundary | separate BW proof/diagonal restriction | **DISPROVED** |

## 10. Dependency map and integration conclusions

Dependency chain: fixed band \(\to\) matrix calculus §5.2 \(\to\) PT/Hessian/Richardson §5.3; AIRM symmetry/bracket curvature \(\to\) ruled/Jacobi §5.4; together these verify HD-G. Separately, one convex fixed flat \(\to\) zero base-change/frame/holonomy, but additive mean error remains; a valid conditional split centres it and APP-B may then derive an oracle numerator.

Canonical dependencies: HD1 §§1–4 (current theorem/PF); HD1-A §§2,5–7 (mean/Richardson); HD1-B §§4–8 (recentring/GLO/lag row); HD1-C §§5,13 (geometry/energy); canonical G1 §7 (H-LIP/local symmetry); analytical reconstruction T31, T38–T40, T47–T49 (ribbon/topology/compact/BW).

Proof-ready conclusions:

1. For fixed spectral-band AIRM, replace the previously explicit higher-differential HD-G primitive by Theorem AIRM-HD-G. Retain total energy, mean length, and generated-band containment separately.
2. Euclidean/Hilbert, unconstrained symmetric Frobenius, and fixed-common-eigenbasis AIRM are exact flat reductions. Their mean rate remains \(\ell_n\); an oracle numerator additionally needs APP-B's conditional-cancellation package.
3. Full AIRM SPD is “locally symmetric, curved”: dimension-free differential constants, no automatic immunity.
4. Use \(R(\partial_sS,\partial_\tau S)=0\) as the exact ribbon property. In AIRM, whitened commutators control its defect.
5. Near diagonalisation is stable only with an off-algebra bound in the project norm and alignment to the same algebra; otherwise it is diagnostic.
6. Compact symmetric and full BW rows remain conditional. Full growing-size BW calculus is not consumed by T-APP-1 or T-APP-2.

## 11. Cross-audit of APP-B and APP-C

This audit checked every use of flatness, holonomy, local/reflection symmetry, constant curvature, commuting SPD structure, and AIRM differential control in the two companion dossiers.

| Claim attacked | Objection | Resolution | Final status |
|---|---|---|---|
| APP-B: flat tube gives \(H=I\) and no non-rigid frame after anchor alignment | \(R=0\) alone is insufficient on a topologically nontrivial region, and observations alone being flat would not constrain estimator ribbons | APP-B's exact row requires one convex tube, path-independent transports, and every estimator stage in the same flat; this is the sufficient §2 package. The remaining anchor change is one rigid \(Q\) | **ACCEPT** |
| APP-B: “trivial holonomy” removes the frame coefficient | The manifold label is weaker than the consumed identity | Its table defines the criterion directly as one common rigid \(Q\) for every \(t\), which is exactly what removes the residual after alignment | **ACCEPT AS DIRECT COEFFICIENT CONDITION** |
| APP-B: local symmetry gives \(H(Y)=H(-Y)\) | A merely small symmetric-looking chart is not enough; the geodesic symmetry must be an isometry on the support tube | On a locally symmetric tube where both \(\operatorname{Exp}_q(\pm Y)\) lie in the symmetry domain, isometry equivariance proves the parity. APP-B does not infer GLO or holonomy from it | **ACCEPT WITH TUBE INTERPRETATION** |
| APP-B: simultaneous reflection symmetry implies GLO | Marginal symmetry would be insufficient | The stated hypothesis is joint lag-pair invariance (conditional when required); Hessian parity makes the GLO integrands odd. The dossier separately disproves marginal symmetry | **ACCEPT** |
| APP-B: approximate curvature yields \(\varepsilon_R\ell\) frame degradation | A small sectional-curvature scalar does not control the curvature endomorphism in the connection-variation formula | APP-B §7.2 was patched to define \(\varepsilon_R\) as the normalized operator norm of \(R(\partial_sS,\partial_\tau S)\) on the actually consumed ribbons. With bounded Jacobi constants, its displayed frame bound follows | **REPAIRED, THEN ACCEPT** |
| APP-B: a small matrix commutator is insufficient | For AIRM, a commutator can control relevant curvature if all vectors are correctly whitened and typed | APP-B claims only insufficiency of an untyped raw diagnostic; APP-A §§3–4 supply the stronger typed fixed-algebra/whitened-commutator route | **ACCEPT** |
| APP-B: full AIRM/local symmetry is not an oracle package | T-APP-2 now proves its higher differentials, possibly suggesting more | Differential verification changes constants only. Noncommuting AIRM retains \(R\ne0\), random \(H\), and a non-rigid frame coefficient | **ACCEPT** |
| APP-C: common commuting AIRM flat has restricted \(H=I\) | This fails if the eigenbasis changes or the minimisation leaves the flat | APP-C explicitly requires one fixed flat and a constrained estimator and rejects changing bases | **ACCEPT** |
| APP-C: constant curvature \(-\kappa^2\) satisfies scalar-plus-HS (SH) | The radial vector \(v\) is undefined at \(r=0\), so the claimed Lipschitz remainder was not proved by the displayed form alone | APP-C §4.2 was patched to write the remainder as \(\beta_\kappa(r)\log_qx\otimes\log_qx\), with \(\beta_\kappa(0)=-\kappa^2/3\). It is smooth through zero, rank one, and uniformly HS-bounded on a bounded tube | **REPAIRED, THEN PROVED UNDER ITS PHYSICAL-DEPENDENCE ASSUMPTIONS** |
| APP-C: constant-curvature SH avoids an operator net | Rank one at each observation does not by itself control temporal concentration | APP-C separately assumes dimension-uniform physical dependence for the scalar and \(\mathcal S_2\)-valued remainder; Hilbert concentration plus \(\|\cdot\|_{\rm op}\le\|\cdot\|_{\rm HS}\) is valid | **ACCEPT** |
| APP-C: full AIRM signed route remains open | APP-A proves all band differential constants, so “geometry open” would be stale | APP-C was patched: band differentials are now credited to T-APP-2, while the missing scalar-plus-HS/fixed-block structure of the random Hessian remains open. These are distinct obligations | **REPAIRED SCOPE; SIGNED ROUTE STILL OPEN** |
| APP-C application rows for full SPD, compact symmetric spaces, and BW | Manifold names can conceal energy, cut-locus, or incompleteness failures | The rows retain fixed-band/energy cautions for AIRM, local-tube status for compact spaces, and no AIRM transfer for BW | **ACCEPT** |

No APP-B theorem was invalidated. APP-C's constant-negative-curvature signed-Hessian theorem survives after the zero-radius smoothness repair. Neither companion dossier now consumes an unproved statement that local symmetry kills curvature, that time-local commutation yields one flat, or that a spectral band supplies bounded total energy.
