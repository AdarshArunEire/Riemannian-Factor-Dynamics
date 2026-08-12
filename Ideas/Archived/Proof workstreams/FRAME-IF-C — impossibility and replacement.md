---
type: proof-dossier
title: FRAME-IF-C — impossibility and restricted replacement
status: noncanonical-workstream
scope: FRAME-IF hostile lower bounds and an explicit curved replacement; Paper 2 excluded
---

# FRAME-IF-C — impossibility and restricted replacement

> This is adversarial proof input, not canon. The FRAME-DB brief and all four archived FRAME-DB dossiers were reread completely. The dossier does not promote a failed generic attack into an impossibility theorem.

## 0. Verdict

**Completion-audit notice.** Sections 0--12 preserve the chronological restricted-result and hostile-audit record. Section 13 supersedes the earlier Gate-B-only classification: together with the uniform geometric and statistical producers proved in A §10 and B §11, it certifies the dimension-uniform Gate-A theorem FRAME-2P-U. The restrictions below remain an independently proved fallback and counterexample record.

The broad FRAME-IF-POLY statement is not generically disproved by pointwise frame lower bounds, high dimension, or inverse-Hessian operator entropy. Those attacks confuse estimation of a complete operator with estimation of its action on an independent root-​(n) score. Under coercivity, that action can concentrate dimension-free.

A nontrivial restricted replacement is proved here on the known curved symmetric space

\[
\mathcal M=\mathbb H^2_{-1}\times\mathbb R.
\]

The centre path belongs to a known one-dimensional curved family, its scalar parameter is observed with bounded additive noise in the Euclidean product coordinate, and the lag signal is a bounded one-dependent rank-one process in the hyperbolic tangent factor. An entirely observable three-colour estimator differentiates its own evaluation row and removes the pilot's first-order mean/frame error. It has the finite-array expansion

\[
\widehat\Gamma^{\rm db}_n-\Gamma_n
=\frac1{N_E}\sum_{j\in E}\{g_j(\theta)-Eg_j(\theta)\}
+K_{n,\theta}\frac1{N_V}\sum_{j\in V}\eta_j+R_n,
\qquad \|R_n\|_{\rm HS}=O_p(n^{-1}).
\tag{0.1}
\]

The second term is unavoidable correction-score noise and belongs to the leading root-​(n) influence row. The post-linearisation nuisance residual is (O_p(n^{-1})=o_p(n^{-1/2})). The curvature/frame part of (K_{n,\theta}) is nonzero for an explicit choice of the path family, so this is not a flat or rigid-frame example.

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.** This is a Gate-B replacement, not a proof of generic FRAME-IF-POLY.

## 1. What the hostile attacks do and do not prove

### 1.1 Identification still survives

With unique population Fréchet means, a fixed Levi-Civita connection and path convention, and the target modulo one common anchor conjugation, the lag row is a functional of the observable law. Therefore no same-law/different-target pair exists in that retained class. Treating the truth-relative frame error as a free latent parameter is invalid.

**Status: PROVED.**

### 1.2 The correction-only information ceiling is narrow

In the Gaussian correction experiment (Z_i\sim N(\vartheta,1)), (B(\vartheta)=\beta\vartheta\), local alternatives (0,c/\sqrt n) give a Le Cam lower bound of order (n^{-1/2}). Hence the estimated correction itself cannot have uniform (o_p(n^{-1/2})) error when all of its sampling noise is called residual. This does not obstruct (0.1), where that noise is an influence term and only (R_n) is the nuisance residual.

**Status: PROVED.**

### 1.3 Full operator estimation can be impossible in high dimension

The following subexperiment states the scope exactly. Let (p=p_n\ge 4). In each of (n) repetitions observe all diagonal entries of

\[
J_i=2I_p+\operatorname{diag}(B_{i1},\ldots,B_{ip}),
\qquad B_{ij}\in\{-1,1\},
\]

independently, with (E B_{ij}=\vartheta_j). The target is

\[
A_\vartheta=EJ_i=2I_p+\operatorname{diag}(\vartheta_1,\ldots,\vartheta_p).
\]

Take the null (\vartheta=0) and alternatives (\vartheta^{(j)}=a_ne_j), where

\[
a_n=c\sqrt{\frac{\log p}{n}}\le\frac12.
\]

For a Rademacher variable of mean (a_n), its KL divergence from the mean-zero Rademacher law is at most (C a_n^2). Thus the (n)-sample KL divergence of every alternative from the null is at most (Cc^2\log p). Choosing (c) small, Fano's inequality shows that no test identifies the active coordinate with error tending to zero. If an estimator satisfied

\[
\|\widehat A-A_\vartheta\|_{op}<a_n/3
\]

under every null/alternative law, the largest diagonal departure of \(\widehat A\) would identify the active coordinate, a contradiction. Hence for universal constants (c_0,c_1>0),

\[
\inf_{\widehat A}\sup_{\vartheta\in\{0,a_ne_1,\ldots,a_ne_p\}}
P_\vartheta\!\left\{
\|\widehat A-A_\vartheta\|_{op}\ge
c_0\sqrt{\frac{\log p}{n}}
\right\}\ge c_1.
\tag{1.1}
\]

For \(\log p\asymp n\), even operator consistency fails. This rigorously disproves any FRAME-IF producer that demands uniform operator-norm estimation of an otherwise unrestricted high-dimensional Hessian law from (O(n)) observations.

The class in (1.1) is an abstract bounded coercive operator experiment. No claim is made that every member is a Riemannian distance Hessian. Therefore (1.1) is not a generic manifold impossibility theorem.

**Status: DISPROVED** for the stated unrestricted full-operator producer class.

### 1.4 Why (1.1) does not defeat an inverse-Hessian action

Let random self-adjoint operators satisfy (mI\preceq H_i\preceq LI), put (A=EH_i), and let \(\widehat A=N^{-1}\sum_iH_i\). For a vector (z) independent of the (H_i),

\[
\|(\widehat A^{-1}-A^{-1})z\|
\le m^{-1}\|(\widehat A-A)A^{-1}z\|.
\]

Conditioning on (v=A^{-1}z) and using Hilbert-space variance gives

\[
E\{\|(\widehat A-A)v\|^2\mid v\}
\le \frac{4L^2}{N}\|v\|^2,
\]

so

\[
\|(\widehat A^{-1}-A^{-1})z\|
=O_p\!\left(\frac{\|z\|}{\sqrt N}\right)
\tag{1.2}
\]

dimension-uniformly. If (z=O_p(n^{-1/2})) and (N\asymp n), the inverse-action error is (O_p(n^{-1})). Likewise, if random maps (K_i:H\to\mathcal S_2(H_0)^{\oplus h_0}) obey \(\|K_i v\|_{\oplus HS}\le C\|v\|\), their empirical action on an independent fixed (v) has (O_p(\|v\|/\sqrt N)) error without estimating the full operator in operator norm.

Thus missing global entropy for (A) or (K) is a valid objection only when the proposed estimator actually requires uniform operator recovery. It is not by itself a lower bound against a cross-fitted action estimator.

**Status: PROVED.**

### 1.5 Remaining generic quantifier hazards

Any generic proof still has to expose, rather than assume implicitly:

- a conditional action envelope for every fitted Hessian/Jacobi map;
- uniform second derivatives of the complete finite-array row on the generated tube;
- a vertex maximum event, not merely a grid RMS rate;
- the exact weighted map from local vertex scores to the row, including its (M_n)-normalisation;
- observable fold synchronization and one common gauge;
- a triangular-array influence sum rather than iid notation (P_n-P);
- one identical mask and target in the base row, score, derivative and population comparison;
- (G_{2,\mathrm{HS},n}) for frame coefficients and (A_{2,n}) only for row assembly.

Absence of these items is a failure of proof, not an analytic counterexample. The replacement below removes each issue by restriction and direct calculation.

### 1.6 Two-bandwidth validation escape: exact rate audit

Consider a pilot bandwidth (b=n^{-1/7}), a validation bandwidth (c=n^{-\gamma}), and (M=n^{2/7}) vertices. Suppose, in a common set of typed vertex fibres, the independent validation displacement has the uniform expansion

\[
v_j=\operatorname{Bias}_j(c)
+\frac1{nc}\sum_iK_{ji}\psi_i+r_j,
\qquad \sup_j\|\operatorname{Bias}_j(c)\|\lesssim c^3,
\tag{1.3}
\]

and the row derivative decomposes as \(D T[v]=\sum_{j=0}^M D_jv_j\) with

\[
\|D_jz\|_{\oplus HS}\le \frac C M\|z\|.
\tag{1.4}
\]

Assume compactly supported bounded kernels, a quasi-uniform grid, (Mc\to\infty), fixed memory, exact fold separation, and a remainder in (1.3) whose aggregate action is (o_p(n^{-1/2})). Swapping the vertex and observation sums shows that one validation observation has aggregate coefficient

\[
\sum_j\frac C M\frac{|K_{ji}|}{nc}
\lesssim \frac C M\frac{Mc}{nc}=\frac Cn.
\]

Therefore the aggregate stochastic term is a root-​(n) Hilbert-Schmidt influence sum; it is not of pointwise order \((nc)^{-1/2}\). The first-order smoothing bias is sub-root-​(n) precisely when

\[
c^3=o(n^{-1/2})
\quad\Longleftrightarrow\quad \gamma>\frac16.
\tag{1.5}
\]

The polygon/Taylor sum of validation variances is

\[
\frac{M}{nc}=n^{-5/7+\gamma},
\]

which is (o(n^{-1/2})) precisely when

\[
\gamma<\frac3{14}.
\tag{1.6}
\]

On this window, (Mc\to\infty), (Mc^6=o(n^{-1/2})), and the pilot-validation cross term

\[
M n^{-3/7}(nc)^{-1/2}
=n^{-9/14+\gamma/2}=o(n^{-1/2})
\]

also holds. Thus

\[
\boxed{\frac16<\gamma<\frac3{14}}
\tag{1.7}
\]

is a genuine nonempty rate window under (1.3)-(1.4). There is no information-theoretic counterexample to this aggregation calculation.

There is, however, a missing canonical term. The G1 vertex error is not merely (c^3+(nc)^{-1/2}); it also contains the triangular-law defect (n^{-a}) and design/mask terms. The correction cancels the pilot error and leaves the validation error at first order, so an uncentred (n^{-a}) contribution remains (O(n^{-a})), not (O(n^{-2a})). Under the retained baseline (a\ge3/7), this need not be (o(n^{-1/2})). Consequently the window (1.7) certifies the escape only under at least one of:

1. exact local stationarity for the validation law;
2. (a>1/2);
3. a proved aggregate centring or separate correction making the validation triangular-law and mask bias (o(n^{-1/2})).

The original FRAME-IF-POLY wording does not explicitly require the validation bandwidth to equal the pilot bandwidth. It therefore does not forbid a second bandwidth. Its displayed remainder (M\ell_n^2), however, does not account for a validation rate slower than the pilot rate. A valid two-bandwidth version must replace that shorthand by the separate terms

\[
M r_T^2+M r_V^2+M r_Tr_V+c^3+n^{-a}
+\rho_{\rm mask,V}+\rho_{\rm lin,V},
\tag{1.8}
\]

with the first-order biases outside the squared terms, and must state (1.3)-(1.4). Under exact local stationarity and exact masks, (1.7) makes every term in (1.8), apart from the leading root-​(n) influence row, sub-root-​(n).

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.** The unqualified claim under only (a\ge3/7) is **DISPROVED** because it omits a retained first-order (n^{-a}) term.

## 2. Explicit curved model

### 2.1 Geometry and mean family

Use the hyperboloid model

\[
\mathbb H^2_{-1}
=\{x\in\mathbb R^{1,2}:x_0^2-x_1^2-x_2^2=1,\ x_0>0\}
\]

with its known constant curvature (-1), and the product manifold
\(\mathcal M=\mathbb H^2_{-1}\times\mathbb R\). Fix (r_0>0), a sufficiently small (\omega>0), and (\Theta=[-\theta_0,\theta_0]). For (u\in[0,1]), define

\[
r_\alpha(u)=r_0+\alpha u,
\]

\[
\gamma_\alpha(u)=
(\cosh r_\alpha(u),
\sinh r_\alpha(u)\cos(\omega u),
\sinh r_\alpha(u)\sin(\omega u)),
\]

\[
\mu_\alpha(u)=(\gamma_\alpha(u),\alpha).
\tag{2.1}
\]

The hyperbolic anchor (\gamma_\alpha(0)) is independent of (\alpha), and tangent spaces in the Euclidean product coordinate have a canonical translation identification. Hence all anchor tangent spaces in this family have one observable common identification. The curve (\gamma_0) is a non-geodesic hyperbolic circle arc when (\omega\ne0).

Let (a) be the outward radial unit vector at the hyperbolic anchor, embedded in (T_{\mu_\alpha(0)}\mathcal M), and let

\[
a_\alpha(u)=P^{\mu_\alpha}_{u\leftarrow0}a.
\tag{2.2}
\]

Let (e_R) denote the global Euclidean unit tangent vector.

### 2.2 Bounded finite-memory observations

Let \((\xi_t)\) and \((\zeta_t)\) be independent iid Rademacher sequences. Fix (0<|\kappa|<1), (c>0), and (\sigma>0), and put

\[
f_t=\xi_t+\kappa\xi_{t-1},
\qquad \eta_t=\sigma\zeta_t,
\]

\[
Z_t=c f_t a_\theta(u_t)+\eta_t e_R,
\qquad X_t=\operatorname{Exp}_{\mu_\theta(u_t)}Z_t,
\qquad u_t=t/n.
\tag{2.3}
\]

The energy is bounded by

\[
\|Z_t\|\le R:=c(1+|\kappa|)+\sigma.
\]

The innovations are one-dependent through (f_t). Since (EZ_t=0), and squared distance is strongly geodesically convex on the Hadamard manifold (\mathcal M), (\mu_\theta(u_t)) is the unique Fréchet mean. The product is a symmetric space, so the distance Hessian at the centre is even under (Z_t\mapsto-Z_t). Global sign reversal of all relevant \(\xi\)'s and \(\zeta\)'s gives the retained GLO symmetry.

The Euclidean coordinate is directly observed as

\[
(X_t)_R=\theta+\eta_t.
\tag{2.4}
\]

The oracle anchor vector is

\[
Y_t=P^{\mu_\theta}_{0\leftarrow u_t}Z_t
=c f_t a+\eta_t e_R.
\tag{2.5}
\]

Therefore, at lag one,

\[
\Gamma_1=E(Y_t\otimes Y_{t-1})
=c^2\kappa\,a\otimes a,
\tag{2.6}
\]

because (E(f_tf_{t-1})=\kappa), while the Euclidean noise is serially white and orthogonal. This is the exact rank-one Paper-1 factorisation with signal singular value (s=|\kappa|c^2>0), bounded total energy, fixed lag and fixed memory. Coupling the same innovations at nearby (u)'s gives the required smooth local-stationarity bound because (2.1)-(2.3) have uniformly bounded derivatives on a compact parameter tube.

**Status: PROVED.**

## 3. Observable folds, mask and estimator

Partition time into superblocks of length (12). Ignoring (O(1)) boundary indices, use

\[
T=\{12j+1\},\qquad V=\{12j+5\},\qquad
E=\{t=12j+10\},
\tag{3.1}
\]

where an evaluation row at (t\in E) uses the lag pair \((t,t-1)\). The innovation sets used by the three colours are disjoint, and rows from different superblocks are independent. Their cardinalities satisfy (N_T,N_V,N_E\asymp n). Stationarity of (2.5) makes the exact masked target equal to (2.6), so there is no masked-to-unmasked target defect.

Let \(\chi\) be a fixed smooth clipping map that equals the identity on a neighbourhood of \(\Theta\), and define

\[
\widehat\theta_T
=\chi\!\left(N_T^{-1}\sum_{t\in T}(X_t)_R\right),
\qquad
\widehat\theta_V
=\chi\!\left(N_V^{-1}\sum_{t\in V}(X_t)_R\right).
\tag{3.2}
\]

For any candidate (\alpha), every evaluation quantity below is observable:

\[
y_t(\alpha)
=P^{\mu_\alpha}_{0\leftarrow u_t}
\log_{\mu_\alpha(u_t)}X_t,
\]

\[
g_t(\alpha)=y_t(\alpha)\otimes y_{t-1}(\alpha),
\qquad
\widehat T_E(\alpha)=N_E^{-1}\sum_{t\in E}g_t(\alpha).
\tag{3.3}
\]

The derivative \(\dot g_t(\alpha)\) is computed from the known log/Jacobi and path-transport derivative. In typed form,

\[
\dot y_t(\alpha)
=\Omega_{t,\alpha}(V_\alpha)y_t(\alpha)
-P^{\mu_\alpha}_{0\leftarrow u_t}
H(\mu_\alpha(u_t),X_t)V_\alpha(u_t),
\tag{3.4}
\]

with the radial endpoint connectors and the curvature integral along the known path (2.1). No true centre, true frame, truth alignment, population lag row or unobserved ribbon enters the computation.

Define the corrected row

\[
\boxed{
\widehat\Gamma^{\rm db}_n
=\widehat T_E(\widehat\theta_T)
-\dot{\widehat T}_E(\widehat\theta_T)
(\widehat\theta_T-\widehat\theta_V).}
\tag{3.5}
\]

The sign is forced: (\widehat\theta_T-\widehat\theta_V) estimates the pilot error (\widehat\theta_T-\theta), so the derivative applied to that error is subtracted. Equivalently, the validation score is (\widehat\theta_V-\widehat\theta_T), giving the plus-score convention of FRAME-DB.

Under any common anchor orthogonal coordinate change (Q), (y_t,\dot y_t\) transform by (Q), and every row in (3.5) transforms by (A\mapsto QAQ^*). Thus the estimator is exactly common-gauge equivariant.

**Status: PROVED.**

## 4. Restricted one-step theorem

### Theorem IF-C1

Assume the model in Section 2, the exact colours in Section 3, and that the true (\theta) lies in the interior region on which \(\chi\) is the identity. Then, with

\[
K_{n,\theta}=N_E^{-1}\sum_{t\in E}E_\theta\dot g_t(\theta),
\tag{4.1}
\]

the feasible estimator (3.5) satisfies

\[
\widehat\Gamma^{\rm db}_n-\Gamma_1
=N_E^{-1}\sum_{t\in E}\{g_t(\theta)-Eg_t(\theta)\}
+K_{n,\theta}N_V^{-1}\sum_{t\in V}\eta_t+R_n,
\tag{4.2}
\]

where

\[
\|R_n\|_{HS}=O_p(n^{-1}).
\tag{4.3}
\]

Consequently,

\[
\|\widehat\Gamma^{\rm db}_n-\Gamma_1\|_{HS}=O_p(n^{-1/2}),
\qquad d_{F,{\rm db},n}=O_p(n^{-1})=o_p(n^{-1/2}),
\tag{4.4}
\]

where (d_{F,{\rm db},n}) denotes the post-influence nuisance residual and does not include the second summand in (4.2).

#### Proof

On the compact set of candidate paths and the bounded observation tube, the hyperbolic product has no cut locus and the log, parallel-transport and Jacobi maps have uniformly bounded derivatives through order two. Hence, for a deterministic (C<\infty),

\[
\sup_{t,\alpha}\{\|g_t(\alpha)\|_{HS}
+\|\dot g_t(\alpha)\|_{HS}
+\|\ddot g_t(\alpha)\|_{HS}\}\le C.
\tag{4.5}
\]

Put (\delta_T=\widehat\theta_T-\theta) and (\delta_V=\widehat\theta_V-\theta). Bounded independent noises and (3.1) give

\[
\delta_T=O_p(n^{-1/2}),\qquad
\delta_V=O_p(n^{-1/2}),
\tag{4.6}
\]

and clipping differs from the identity with exponentially small probability. Taylor's formula applied pathwise to the evaluation average yields

\[
\widehat T_E(\theta+\delta_T)
=\widehat T_E(\theta)
+\dot{\widehat T}_E(\theta)\delta_T+O_p(\delta_T^2),
\]

\[
\dot{\widehat T}_E(\theta+\delta_T)
=\dot{\widehat T}_E(\theta)+O_p(|\delta_T|).
\]

Substitution into (3.5) gives

\[
\widehat\Gamma^{\rm db}_n
=\widehat T_E(\theta)
+\dot{\widehat T}_E(\theta)\delta_V
+O_p(\delta_T^2+|\delta_T\delta_V|).
\tag{4.7}
\]

The independent superblock rows and (4.5) imply

\[
\|\dot{\widehat T}_E(\theta)-K_{n,\theta}\|_{HS}
=O_p(n^{-1/2}).
\tag{4.8}
\]

Multiplying (4.8) by \(\delta_V=O_p(n^{-1/2})\), and using
\(\delta_V=N_V^{-1}\sum_{t\in V}\eta_t\) off the exponentially small clipping event, proves (4.2)-(4.3). Each leading sum in (4.2) is a bounded, independent, finite-array Hilbert-Schmidt sum of order (n^{-1/2}). This proves (4.4). \(\square\)

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 5. The correction is genuinely curved and non-rigid

At (\theta=0), the base curve has tangent

\[
T(u)=\omega\sinh(r_0)e_\phi(u),
\]

while the hyperbolic part of the parameter variation is

\[
V(u)=u e_r(u).
\]

For the convention used in FRAME-DB-A, constant curvature gives

\[
R(T,V)W
=-\{\langle V,W\rangle T-\langle T,W\rangle V\}.
\]

Let (b) be the angular anchor unit vector. Expanding the path transport uniformly for small (\omega), the radial loading vector obeys

\[
\Omega_u(V)a
=-\frac12\omega\sinh(r_0)u^2b+O(\omega^2),
\tag{5.1}
\]

uniformly on (u\in[0,1]). The distance-Hessian mean terms in (E\dot g_t(0)) vanish by the joint sign symmetry and the evenness of the symmetric-space Hessian. Therefore

\[
K_{n,0}
=c^2\kappa N_E^{-1}\sum_{t\in E}
\{\Omega_{u_t}(V)a\otimes a
+a\otimes\Omega_{u_{t-1}}(V)a\}.
\tag{5.2}
\]

Its inner product with (b\otimes a+a\otimes b) is a nonzero constant times

\[
-\omega\kappa c^2\sinh(r_0)
N_E^{-1}\sum_{t\in E}(u_t^2+u_{t-1}^2)+O(\omega^2).
\]

For sufficiently small nonzero (\omega), this is nonzero. Also (\Omega_0=0) and (5.1) varies as (u^2), so it is not one common rigid skew. The correction in (3.5) therefore removes a genuine non-rigid curvature-frame derivative.

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 6. Loading and null-spectrum propagation

Let (\mathbb L=\Gamma_1\Gamma_1^*=s^2a\otimes a), where (s=|\kappa|c^2), and let

\[
\widehat{\mathbb L}^{\rm db}
=\widehat\Gamma^{\rm db}_n(\widehat\Gamma^{\rm db}_n)^*.
\]

Writing (d_n=\|\widehat\Gamma^{\rm db}_n-\Gamma_1\|_{HS}),

\[
\|\widehat{\mathbb L}^{\rm db}-\mathbb L\|_{op}
\le 2s d_n+d_n^2.
\tag{6.1}
\]

The actual eigengap is (\Delta=s^2). Hence

\[
\|\sin\Theta(\widehat E_n^{\rm db},\operatorname{span}\{a\})\|_{op}
=O_p\!\left(\frac{n^{-1/2}}{s}\right),
\tag{6.2}
\]

and, by the row singular-value square,

\[
\widehat\lambda_{2,n}^{\rm db}\le d_n^2=O_p(n^{-1}).
\tag{6.3}
\]

For fixed (s>0), this earns the oracle root-​(n) numerator, root-​(n) loading rate, and (n^{-1}) null spectrum. No operator/HS switch or replacement of the actual gap is used.

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 7. Adversarial family audit

| Family | Result for the replacement |
|---|---|
| Flat Hilbert limit | Setting curvature to zero makes (5.1) vanish; (3.5) remains a mean-path one-step estimator and does not invent a frame term. |
| Fixed commuting SPD flat | Not claimed by this theorem; it belongs to the existing exact-flat branch. |
| Common rigid skew | A common anchor change conjugates (3.5) exactly and is not subtracted as additive error. |
| CE-B5 type non-rigid commutator | Equation (5.2) is the continuous curved analogue and is explicitly corrected. |
| Zero signal | If (\kappa=0), (5.2) and the gap vanish; the loading conclusion is not asserted. |
| Zero idiosyncratic noise | If (\sigma=0), the auxiliary coordinate reveals (\theta) exactly and the nuisance disappears; curvature frame sensitivity (5.1) still exists for a perturbed pilot. |
| Constant curvature, moving mean | This is the theorem's principal nonflat case. |
| High-dimensional bounded energy | Excluded: the theorem is fixed three-dimensional tangent geometry. Section 1 states the exact high-dimensional producer lower bound and the action escape. |
| One bad grid vertex | No estimated vertex grid is used; the known parametric path is evaluated directly. |
| High-frequency small amplitude | Excluded by fixed (\omega) and the uniform derivative bound (4.5); no length-only claim is made. |
| Nearly commuting changing basis | Not an assumption and not used as a surrogate for (5.2). |
| Same law, different decomposition | Impossible here because the Euclidean marginal identifies (\theta), the mean is unique, and the connection/path family is fixed. |

The hostile perturbations for any attempted extension are: let (\omega_n\) grow to break (4.5); remove the Euclidean coordinate to make the parametric producer nonexplicit; let (p_n\) grow while requiring full operator recovery to invoke (1.1); reuse colours to create a first-order product; replace the stationary exact mask by a locally weighted mask; or let (s_n\downarrow0) so (6.2), not the row theorem, becomes binding.

## 8. Claim ledger

| ID | Claim | Observable producer | Norm/rate | Status |
|---|---|---|---|---|
| IF-C-LB | unrestricted full Hessian operator recovery pays \(\sqrt{\log p/n}\) | diagonal bounded operator samples | operator norm | DISPROVED |
| IF-C-ACT | coercive inverse action on an independent score is dimension-free | empirical Hessian action | Hilbert norm, \(\|z\|/\sqrt n\) | PROVED |
| IF-C-DGP | (2.1)-(2.6) is a nonempty curved bounded-energy fixed-memory rank-one model | raw manifold observations | exact | PROVED |
| IF-C-EST | (3.5) is observable, split and gauge equivariant | known path family, raw folds, Jacobi derivative | exact | PROVED |
| IF-C-ROW | expansion (4.2) has (O_p(n^{-1})) post-influence remainder | three exact colours | HS | PROVED UNDER EXPLICIT ASSUMPTIONS |
| IF-C-CURV | the corrected derivative contains a nonzero non-rigid curvature term | constant-curvature variation | HS coefficient | PROVED UNDER EXPLICIT ASSUMPTIONS |
| IF-C-LOAD | corrected loading and null-spectrum rates follow through the actual gap | corrected lag row | operator/gap | PROVED UNDER EXPLICIT ASSUMPTIONS |

## 9. Nuisance and target ledger

| Nuisance | First-order coefficient | Estimate | Fold | Residual |
|---|---|---|---|---|
| scalar centre-path parameter | (K_{n,\theta}\) including mean and frame derivatives | (\widehat\theta_T-\widehat\theta_V) | T/V | (O_p(n^{-1})) after influence extraction |
| non-rigid frame | curvature/Jacobi part of (\dot g_t) | derivative of the observable evaluation row | E | included in the same (O_p(n^{-1})) Taylor residual |
| common gauge | common conjugation | exact equivariance | all | zero intrinsically |
| lag sampling | (g_t(\theta)-Eg_t(\theta)) | empirical evaluation row | E | leading (O_p(n^{-1/2})) influence |
| correction sampling | (K_{n,\theta}\eta_t) | validation mean | V | leading (O_p(n^{-1/2})) influence |
| mask/dependence | none after the exact stationary mask | deterministic colours | T/V/E | (O(n^{-1})) boundary only |

The target throughout is the masked lag-one row (2.6) in the canonical product anchor, modulo one common conjugation. It equals the unmasked stationary row exactly. No spectrum-only or quotient-summary target is substituted.

## 10. Final gate recommendation

Adopt the explicit one-dimensional hyperbolic-product theorem as a Gate-B closure for FRAME-IF: known parametric mean family, observable scalar producer, fixed-dimensional known symmetric geometry, exact finite-memory colours, fixed nonzero signal. The post-influence frame/mean nuisance residual is (O_p(n^{-1})), the corrected row is root-​(n), and the null spectrum is (O_p(n^{-1})).

Do not claim a generic impossibility theorem from operator entropy, pointwise frame estimation, or the correction-only Le Cam bound. They attack declared producer conventions only. The restricted theorem is the completed mathematical outcome of this track and introduces no further missing lemma.

**Final status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 11. First hostile cross-audit of frozen B and the lead two-path theorem

This pass audits the frozen B dossier and the lead's Sections 1--7 from raw folds through the loading claim. It treats the same-band disproof, the two-path repair, and the parametric fallback as three different claims.

### 11.1 Claim/attack/repair/status ledger

| Claim | Hostile attack | Exact repair or surviving proof | Status |
|---|---|---|---|
| Same-band validation score removes the canonical pilot bias | Each validation stage score is centred at its own smoothed population barycentre. The Richardson multiplier at order three is (1/8\ne0); a curved row with (K[B_3]\ne0) retains (b^3K[B_3]). | The counterexample uses a genuinely transverse (C^3) mean path in ​(\mathbb H^2(-1)), a rank-one lag row not commuting with planar skew, and (b=n^{-1/7}). This is a deterministic population defect, so folds and concentration do not alter it. | DISPROVED |
| A vertex derivative has norm (C/M), including the anchor vertex | A change of (q_0) moves the target anchor fibre and appears to affect every later transport. Calling it common gauge without a typed comparison would be false. | Compare (T_{q_0(s)}M) with (T_{q_0(0)}M) by the declared radial connector. Its first-order generator is zero. In the fixed fibre, differentiating the first cell gives only its curvature integral, of length (M^{-1}); its terminal connector cancels the next cell's initial connector. The base-log change occurs only for observations in the first cell, an (O(M^{-1})) row fraction. Thus (K_0=O(M^{-1})). The same argument at the terminal vertex and the matched two-cell argument internally prove (2A.3). No anchor vertex must be frozen, but radial fixed-fibre comparison is mandatory. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Bounded first replacements imply a (1/(n\sqrt c)) Hájek remainder | First bounded differences alone yield variance (O(n^{-1})) for the full functional; they do not show its nonlinear remainder is degenerate or smaller. | Require the empirical barycentre/Richardson map to have uniform first and second replacement stability. For observations (i,k) whose kernel windows overlap, strong convexity and two score derivatives give a vertex second difference (C/(n^2c^2)). They overlap at (O(Mc)) vertices, so after (C/M) row weights, ​(|\Delta_i\Delta_kF|_{HS}\le C/(n^2c)). Nonoverlapping windows give zero, apart from a fixed-memory enlargement. There are (O(n^2c)) overlapping pairs. The second-order Efron--Stein/ANOVA inequality therefore gives ​(|F-EF-\sum_iF_i|_{L^2(HS)}\le C\{n^2c(n^2c)^{-2}\}^{1/2}=C/(n\sqrt c)). This is (o(n^{-1/2})). B must add this displayed producer; the lead already states its rate but should retain the second-replacement premise. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Validation first-order action is root-​(n) despite pointwise ((nc)^{-1/2}) noise | A hidden ​(sqrt M) or (c^{-1/2}) factor could survive. | One observation affects (O(Mc)) vertices, each barycentre by (C/(nc)), and each vertex has row action (C/M); its aggregate coefficient is (C/n). Fixed dependence colouring and HS Efron--Stein give root-​(n). This is an action estimate, not full vertex-vector or operator recovery. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| The validation expectation is only (c^3+(nc)^{-1}) | Empirical barycentres need not be unbiased; a pointwise (O((nc)^{-1/2})) mean could destroy the theorem. | Delete the fixed dependence block containing observation (i). The leave-block-out barycentre is independent of its centred score term and differs from the full barycentre by (C/(nc)). Uniform Hessian Lipschitzness and strong convexity bound the score--Hessian covariance and Taylor remainder by (C/(nc)). Richardson has fixed (C^2) norm. Thus the population action is (O(c^3+(nc)^{-1})), plus the separately retained triangular-law/mask defects. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| The window (1/6<\gamma<3/14) closes every two-path remainder | The canonical (n^{-a}) term and mask/design bias were initially omitted; also the mixed polygon term (Mr_Tr_V) is load-bearing. | Require exact local-law sampling or (a>1/2), identical masked targets, and (o(n^{-1/2})) design/coupling defects. Retain (M(r_T^2+r_Tr_V+r_V^2)+M^{-2}). The exponent checks in Section 1.6 and B (2A.8)--(2A.8a) put every term below root-​(n) exactly on the stated window. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Positive three-scale validation vertices inherit Sturm stability automatically | The Richardson output is a signed nonlinear post-map, not itself a positive barycentre; a positive-barycentre theorem alone does not control its replacements or expectation. | Define the canonical Richardson post-map in one declared tangent fibre and assume/prove its uniform (C^2) norm on the generated tube. Apply the positive-weight stability separately to its three stage barycentres and then the chain rule. The fixed weights have finite ​(ell^1) norm. Without this post-map condition the stated stability claim is DISPROVED; with it, the lead calculation is valid. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| An explicit nonempty curved DGP satisfies the two-path assumptions | B's likelihood-score hyperbolic example is tailored to the parametric fallback, and compactly supported moving densities can hide common-support/bounded-score regularity. It does not by itself certify every nonparametric two-path producer. | Use Section 2 of this C dossier for nonemptiness: ​(\mathbb H^2(-1)\times\mathbb R), the smooth non-geodesic path (2.1), and the bounded one-dependent transported tangent process (2.3). The same innovations define the exact local proxy, so the extra (n^{-a}) approximation defect is absent; the law/mean are (C^4) after choosing the path family (C^4); energy, GLO, unique means, exact masks and positive rank-one gap are proved. Section 5 proves a nonzero time-varying curvature-frame derivative. This DGP is fixed-dimensional and lies in the repaired two-path class. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| The two-path theorem is Gate A/dimension-uniform | Bounded energy alone does not supply dimension-uniform second Jacobi derivatives, Richardson (C^2) action stability, vertex maxima, or generated-tube constants. | The Gate-A claim fails. State fixed (p,h_0,m_0), exact-local-law or (a>1/2), known geometry on a uniform compact tube, and the displayed replacement/action assumptions. The repaired result is Gate B. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Masks and dependence disappear by cyclic averaging | Different colour masks can target different triangular-array rows, and lag pairs may share innovations across deleted boundaries. | Use within-core lag pairs only, gaps at least (m_0+h_0), one identical declared masked target for row and derivative, and pay any comparison as a first-order defect. Cyclic averaging is optional symmetry, not a target proof. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Corrected loading/null rates follow directly from root-​(n) row | A common conjugation must be removed before error measurement; HS row error cannot be inserted into Davis--Kahan without assembly and the actual gap. | Gauge equivariance conjugates the base row and derivative together. With (d=O_p(n^{-1/2})), use ​(2A_2d+d^2), require it is (o_p(\Delta_n)), and use the row singular-value square ​(\widehat\lambda_{r+1}\le d^2). B/lead retain these consumers. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Parametric fallback is a complete curved theorem | A generic likelihood-score assertion could hide nonregular support; a path-family theorem alone would not exhibit an observable root-​(n) producer. | The explicit product-coordinate construction in Sections 2--6 of this dossier supplies the producer directly through ​((X_t)_R=\theta+\eta_t), avoiding likelihood regularity. Its row expansion has (O_p(n^{-1})) post-influence remainder and a nonzero non-rigid curvature coefficient. | PROVED UNDER EXPLICIT ASSUMPTIONS |

### 11.2 Direct-sum remainder after the repairs

Under the repaired two-path assumptions, let

\[
r_T=n^{-3/7},\qquad
r_V=c^3+(nc)^{-1/2},\qquad
M=n^{2/7},\qquad c=n^{-\gamma}.
\]

The leading validation linear action is a root-​(n) influence row. The nuisance remainder is

\[
O_p\!\left\{
M(r_T^2+r_Tr_V+r_V^2)+M^{-2}
+c^3+(nc)^{-1}+\frac1{n\sqrt c}
\right\}
+O(n^{-a})+\rho_{mask,n}+\rho_{CF,n}.
\tag{11.1}
\]

For (1/6<\gamma<3/14), exact local law or (a>1/2), and sub-root-​(n) mask/coupling defects, every displayed nuisance term is (o(n^{-1/2})). In particular, ​(1/(n\sqrt c)=n^{-1+\gamma/2}=o(n^{-1/2})). No validation correction fluctuation is mislabeled as nuisance residual.

### 11.3 Edge-family pass

| Edge family | Pass-1 conclusion | Status |
|---|---|---|
| flat Hilbert / fixed commuting flat | the Jacobi curvature part vanishes; the estimator does not invent non-rigid frame error | PROVED |
| common rigid skew | exact common conjugation, removed before the additive norm | PROVED |
| CE-B5 | the complete vertex derivative contains and corrects the noncommuting frame coefficient | PROVED UNDER EXPLICIT ASSUMPTIONS |
| zero signal | correction coefficient and gap vanish; no loading conclusion | PROVED |
| zero idiosyncratic noise | signal vectors can still carry curvature sensitivity | PROVED |
| constant curvature moving mean | C's explicit DGP supplies a nonzero non-rigid coefficient | PROVED UNDER EXPLICIT ASSUMPTIONS |
| high dimension | the generic promotion fails; the two-path proof is fixed-​(p) and makes no dimension-uniform claim | DISPROVED |
| one bad vertex | arbitrary-grid maximum/tube and (M r^2) remain explicit | PROVED UNDER EXPLICIT ASSUMPTIONS |
| high-frequency small amplitude | the unrestricted extension fails; fixed uniform acceleration/two-Jacobi bounds exclude the hostile family | DISPROVED |
| near commuting/changing basis | no commutation shortcut is used | PROVED |
| identical law/different target | unique mean, connection and path convention still block the pair | DISPROVED |

### 11.4 Pass-1 gate

The same-band score-only FRAME-IF formula is **DISPROVED**. The repaired undersmoothed two-path row is **PROVED UNDER EXPLICIT ASSUMPTIONS** as a fixed-dimensional Gate-B theorem, provided the lead/B records add the explicit second-replacement stability premise and retain radial fixed-fibre treatment of the anchor. The independent hyperbolic-product parametric fallback is also **PROVED UNDER EXPLICIT ASSUMPTIONS** and already suffices for Gate B if any broader two-path producer is rejected.

No Gate-A or generic impossibility claim is earned. No new open lemma is needed for the final outcome.

### 11.5 Addendum: hostile pass 1 against frozen A

| A claim | Hostile attack | Exact repair or surviving conclusion | Status |
|---|---|---|---|
| Cell derivative (A 1.2) and ordered polygon derivative | Fibres, connector signs, partial cell and curvature orientation could be lost in the product. | A uses the repaired FRAME-DB convention ((-E_b,+PE_a,+\int R(T,V))), radial source-fibre identification, every completed cell and the partial cell. | PROVED |
| Internal vertex action is (C/M) | Endpoint terms may be order one; A fixes the anchor and excludes or separately weights the terminal vertex. | For internal vertices the matched radial endpoint generators cancel and only two length-​(M^{-1}) curvature integrals plus an (O(M^{-1})) base-log row fraction remain. A's fixed anchor is a valid stricter repair. The lead's moving-anchor version requires the radial argument in Section 11.1. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Bilinear remainder is (CM\|z\|_{RMS}^2+CM^{-2}) | Nonadjacent product interactions and one concentrated vertex could invalidate an (O(\|z\|^2)) shortcut. | A retains diagonal/adjacent Hessian blocks, (M^{-2}) nonlocal blocks, the (M\)-factor and fixed generated-tube derivatives. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Finite-dimensional one-step sign and expansion | The correction may double-count the direct lag-law score or use the wrong Karcher sign. | A separates fixed-observation derivative from direct lag sampling and uses (D\Psi=-A), hence (T+KA^{-1}\Psi). With its explicit root-​(n) assumptions on \(\widehat\theta,\widehat A,\widehat K\), fold products are (O_p(n^{-1})), and the polygon remainder is (M/n+M^{-2}). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| A Section 5 is a proved nonempty statistical DGP | It gives a curved finite-state model but does not display the observable (k)-score \(\psi\), prove its population zero, or prove the asserted nonsingular Jacobian. A moving finite support is not automatically a regular likelihood model. | The claim as written fails. Cite the explicit product-coordinate producer of C Sections 2--4, which proves nonemptiness without likelihood or support regularity. | DISPROVED |
| A Section 6 proves generic growing-dimensional FRAME-IF impossible | FRAME-IF needs the cross-fitted action (KA^{-1}\Psi), not uniform recovery of the full inverse in operator norm. A's displayed alternatives have perturbation amplitude (c_0/\sqrt n) but then asserts order-one separation of inverses; that conclusion does not follow. The claimed Riemannian realization in \(\mathbb H^2\times\mathbb R^{p-2}\) is also not supplied: Euclidean distance Hessians are the identity in the Euclidean factors, so arbitrary rank-one Hessian directions are not thereby realized. | Retain only C (1.1), which disproves a declared unrestricted full-operator producer at rate \(\sqrt{\log p/n}\), and C (1.2), which proves why inverse actions can escape. Delete A's Gate-C/generic-impossibility language. The campaign outcome remains Gate B through the two proved restricted estimators. | DISPROVED |
| A concludes Gate B fixed-dimensional closure | This conclusion must not depend on the invalid generic lower bound or incomplete A Section 5 example. | The algebraic A theorem is valid under its explicit finite-dimensional producer assumptions, and C's explicit \(\mathbb H^2\times\mathbb R\) DGP supplies nonemptiness. State only Gate B. | PROVED UNDER EXPLICIT ASSUMPTIONS |

**Pass-1 repair required from A:** remove the generic growing-​(p) disproof in Sections 0, 6 and 8; replace it by the narrow full-operator warning or no lower-bound claim. Replace or complete the Section 5 statistical producer. Neither repair changes the proved Gate-B closure.

## 12. Second hostile cross-audit of repaired A, B, lead and C replacement

This is a fresh audit from the observable raw array to the loading and null-spectrum consumers. It does not rely on the pass-1 verdict. A claim passes only with the restrictions presently displayed in B/lead or explicitly stated below.

### 12.1 Complete-chain pass/fail ledger

| Link | Fresh hostile test | Pass/fail conclusion | Status |
|---|---|---|---|
| Observable target | Do (T,V,E) estimate one row, or do colour masks silently change the estimand? | Within-core lag pairs, gaps at least (m_0+h_0), one deterministic mask and its finite-array target make the computation coherent. Any unmasked comparison remains a first-order ​(\rho_{mask,n}). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Pilot and validation paths | Does the validation object merely repeat the same smoothing bias? | (b=n^{-1/7}) and independent (c=n^{-\gamma}) paths are different. The same-band score formula is disproved; the validation bias is (c^3), not (b^3). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Signed Richardson feasibility | Is the signed output falsely treated as a positive barycentre? | Each of three stages is a positive barycentre; their declared fixed-fibre post-map (R) has bounded first two differentials. Stability is transferred by the chain rule, not by Sturm convexity of the signed output. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Displacement sign and fibres | Does (d=\log_{\widehat q^T}\check q^V) actually cancel the pilot error? | Radial connector comparison gives (d=e_V-e_T+O(e_T^2+e_V^2)). Therefore (T(\widehat q_T)+DT(\widehat q_T)[d]) has the required plus sign and leaves (K[e_V]). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Anchor gauge | Does moving (q_0) create an order-one term or truth-selected alignment? | Varying anchor fibres are compared by the observable radial connector. Its generator is zero; the coordinate motion is common, while the first-cell curvature and base-log row mass are (O(M^{-1})). Base row and correction conjugate together under (Q). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Vertex derivative | Can a vertex perturbation affect all downstream transports at order one? | Matched endpoint generators cancel between adjacent cells. Only two (M^{-1})-length curvature integrals and an (O(M^{-1})) fraction of local logs remain. Completed/partial cells and the terminal endpoint obey the same row bound. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Second polygon variation | Is a hidden (M^2r^2) or one-bad-vertex term suppressed? | The conservative bound (CM\|v\|_{RMS}\|w\|_{RMS}), vertex maximum tube, and (M^{-2}) chord lens are retained. No (O(r^2)) shortcut is used. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Validation linear fluctuation | Does pointwise ((nc)^{-1/2}) noise pay ​(sqrt M)? | One observation affects (Mc) vertices, each by (1/(nc)), with row action (1/M); its aggregate action is (1/n). Fixed-memory Hilbert/HS Efron--Stein gives root-​(n). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Hájek remainder | Are bounded first replacements incorrectly promoted to asymptotic linearity? | The repaired premise includes mixed second replacement (C/(n^2c)) after row aggregation and (O(n^2c)) overlapping pairs. The second-order ANOVA bound is (1/(n\sqrt c)=o(n^{-1/2})). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Empirical-barycentre expectation | Can a first-order ((nc)^{-1/2}) bias remain? | Fixed-block deletion makes the centred score independent of the leave-block-out barycentre; strong convexity and bounded Hessian derivative give expectation (c^3+(nc)^{-1}), plus separately retained law/mask defects. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Triangular law | Is the retained (n^{-a}) defect squared or omitted? | The theorem expressly assumes exact local law or (a>1/2), and sub-root-​(n) design, mask and coupling defects. The baseline (a\ge3/7) alone is rejected. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Conditional evaluation derivative | Does fitting the derivative on (E) create an uncontrolled product? | Conditional on (V), ​((D\widehat T_E-DT)[e_V]=O_p(n^{-1/2}r_V)) by bounded finite-memory HS concentration. It is sub-root-​(n) on the rate window. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Full nuisance remainder | Are (Mr_T^2,Mr_Tr_V,Mr_V^2,M^{-2}) and validation biases all present? | They are all present in B/lead and in (11.1). For (1/6<\gamma<3/14), every exponent is strictly below (-1/2). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Correction noise convention | Is the root-​(n) validation fluctuation falsely called (o(n^{-1/2}))? | It is explicitly part of the leading influence row. Only post-linearisation terms define ​(d_{F,db,n}). | PROVED |
| Mean/frame separation | Is GLO used to erase the frame coefficient? | Base-log/Hessian and Jacobi/frame components are separate terms of the complete derivative. GLO centres the appropriate mean channel; the non-rigid frame action is explicitly corrected. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| HS/operator discipline | Is operator lag energy used for an HS coefficient? | Vertex actions and empirical rows are bounded directly in ​(\oplus HS); (G_{2,HS}) remains the generic frame-energy producer. (A_2) appears only in final assembly. | PROVED |
| High dimension | Are fixed-​(p) bounds silently called dimension-uniform Gate A? | B/lead state fixed (p,h_0,m_0) and call the theorem Gate B. No generic growing-​(p) conclusion survives this audit. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Nonempty curved class | Do all assumptions hold simultaneously on a nonflat non-rigid DGP? | B (2A.10)/C Section 2 uses ​(\mathbb H^2(-1)\times\mathbb R), a (C^4) nongeodesic mean, bounded one-dependent central-symmetric innovations, exact local proxy, fixed mask, rank-one positive gap, compact tube, and a nonzero time-varying curvature derivative. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Parametric fallback | If any two-path producer is rejected, is there still a complete outcome? | C Theorem IF-C1 uses the observed Euclidean product coordinate for a scalar root-​(n) producer and gives an exact oracle-row plus validation-influence expansion with (O_p(n^{-1})) residual. It avoids likelihood/support regularity. | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Row assembly | Is root-​(n) HS row error directly equated with loading error? | The consumer uses ​(2A_2d+d^2), the actual (\Delta_n), and the condition that assembly is (o_p(\Delta_n)). | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Null spectrum and selector | Is Weyl used instead of the row square, or is raw ratio silently rehabilitated? | ​(\widehat\lambda_{r+1}\le d^2=O_p(n^{-1})). Threshold selection additionally needs (n^{-1}=o(\tau_n)\ll\Delta_n); raw ratio remains disproved. | PROVED UNDER EXPLICIT ASSUMPTIONS |

### 12.2 Fresh audit of all edge families

| Edge family | Final audit | Status |
|---|---|---|
| Flat Hilbert | curvature-frame derivative vanishes after common alignment; mean correction may remain | PROVED |
| One fixed commuting SPD flat | falls into the existing fixed-flat branch; no curved frame term is invented | PROVED |
| Common rigid skew | entire row is commonly conjugated and receives no additive gap penalty | PROVED |
| CE-B5 | GLO alone still fails; the complete fitted vertex derivative corrects the noncommuting first variation under theorem assumptions | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Zero signal | correction coefficient is zero and (\Delta=0); no loading identification is claimed | PROVED |
| Zero idiosyncratic noise | moving-centre signal can retain curvature sensitivity; C's producer becomes exact if its auxiliary noise is zero | PROVED |
| Constant curvature moving mean | the explicit hyperbolic witness has nonzero time-varying frame derivative | PROVED UNDER EXPLICIT ASSUMPTIONS |
| High-dimensional bounded energy | outside Gate B; full-operator lower bound does not imply generic action impossibility | PROVED |
| One bad vertex | maximum tube and (Mr^2) are retained | PROVED UNDER EXPLICIT ASSUMPTIONS |
| High-frequency small amplitude | the unrestricted extension fails; bounded acceleration and two-Jacobi generated-tube constants exclude it | DISPROVED |
| Nearly commuting changing basis | no commutation surrogate is used | PROVED |
| Same law, different decomposition | unique mean, fixed connection/path and lag-range target prevent a different target modulo common conjugation | DISPROVED |

### 12.3 Pass-2 repairs — SUPERSEDED as current objections

The numbered findings below are the defects found by pass 2. The frozen A/B/lead records subsequently implemented all five repairs, including the final mechanical status and lag-row fixes. They are retained only as audit history. **Status: SUPERSEDED.**

1. A Section 7 still labels “high-dimensional bounded energy” as `DISPROVED`, and A Section 8 still says the unrestricted generic version is `DISPROVED`. A Section 6 correctly acknowledges that only full-operator estimation was attacked and that a composed action may escape. The two stale statements must be replaced by `SUPERSEDED` and prose saying no Gate-A theorem is proved.
2. A Section 5 asserts a nonsingular finite-dimensional Karcher Jacobian without displaying the observable score or computing its Jacobian. It must cite/import C's product-coordinate producer or add that calculation. This does not affect A's conditional theorem.
3. The lead Section 8 used temporary pre-audit labels. Replace them with the pass-2 statuses in Section 12.1 and remove its in-progress qualification from Section 7.
4. The lead metadata used an active-campaign administrative value. At freeze it must use the completed noncanonical adjudication value.
5. B's parametric Section 5 likelihood witness remains less explicit than C's producer. The lead correctly relies on C's ​(\mathbb H^2\times\mathbb R) construction; B should cross-reference it rather than treating moving-support likelihood regularity as automatic.

### 12.4 Final gate recommendation

**Gate B — restricted curved debiaser proved.** The undersmoothed two-path polygon estimator is proved at fixed dimension under exact local law or (a>1/2), common masks, fixed memory, bounded total energy, GLO, a (C^4) law/mean, a compact generated tube with bounded two-Jacobi/second-replacement/Richardson derivatives, and (1/6<\gamma<3/14). It has a root-​(n) direct-sum HS row and an (o_p(n^{-1/2})) post-influence nuisance remainder. The explicit hyperbolic-product parametric estimator independently proves Gate B with (O_p(n^{-1})) residual.

The old identically smoothed score-only formula is **DISPROVED**. Generic growing-dimensional feasibility and generic impossibility are both unproved and are not needed for the final closed outcome. There is no remaining open lemma in this campaign.

**Final pass-2 status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 13. Completion-audit addendum: dimension-uniform promotion

This addendum supersedes only the fixed-dimension gate classification in Sections 12.1 and 12.4. It audits the stronger theorem in which \(p=p_n\) is arbitrary and every producer constant used below is uniform in \(p_n\). It does not infer those constants from bounded energy alone.

### 13.1 Exact uniform producer package

Let the manifolds \(\mathcal M_n\) and observable triangular laws satisfy, uniformly in \(n\) and \(p_n\):

1. unique local Fréchet means and Karcher strong convexity \(A_{n,u}\succeq mI\), \(m>0\);
2. bounded total tangent energy \(\|Y_{n,t}\|\le R\), fixed lag count and fixed memory;
3. bounded operator norms for the score Hessian derivative, the first two barycentre replacement derivatives, Exp, Log, the Richardson post-map, chord PT/Jacobi maps, and the first two complete polygon variations on one generated tube;
4. dimension-uniform vertex actions
   \[
   \max_{j\le M_n}\|K_{n,j}\|\le C/M_n,
   \qquad \sum_{j\le M_n}\|K_{n,j}\|\le C;
   \tag{13.1}
   \]
5. dimension-uniform single and mixed double replacement actions
   \[
   \|\Delta_iF_n\|_{\oplus HS}\le C/n,\qquad
   \|\Delta_i\Delta_kF_n\|_{\oplus HS}
   \le {C\over n^2c_n}
   \tag{13.2}
   \]
   for overlapping validation windows, with only \(O(n^2c_n)\) overlapping pairs after fixed-memory enlargement;
6. the arbitrary-grid mean bounds
   \[
   \|e^T\|_{2,M}=O_p(n^{-3/7}),\quad
   \|e^V\|_{2,M}=O_p\{c_n^3+(nc_n)^{-1/2}\},
   \tag{13.3}
   \]
   and the deterministic maximum implication
   \[
   \|e\|_\infty\le\sqrt{M_n+1}\,\|e\|_{2,M}=o_p(1);
   \tag{13.4}
   \]
7. exact finite-memory folds and one identical masked target, exact local law or \(a>1/2\), and dimension-uniform sub-root-\(n\) design, mask and coupling defects.

### 13.2 No surviving dimension obstruction

Every stochastic object in FRAME-2P takes values in a Hilbert space or a direct sum of a fixed number of Hilbert--Schmidt spaces. The proof uses only squared-norm variance or replacement inequalities:

\[
E\left\|N^{-1}\sum_i(Z_i-EZ_i)\right\|^2
\le {C\over N},
\tag{13.5}
\]

and their fixed-memory block versions. These bounds do not contain \(p_n\).

For the validation action, (13.2) gives a root-\(n\) first-order fluctuation, while the degenerate Hájek remainder is

\[
\left\{O(n^2c_n){C^2\over n^4c_n^2}\right\}^{1/2}
=O\{(n\sqrt{c_n})^{-1}\}.
\tag{13.6}
\]

Neither calculation estimates an inverse Karcher operator in operator norm. Strong convexity is used pathwise to control how a barycentre changes under one or two replacements. Neither calculation takes a sphere net, a coordinate maximum over \(p_n\), or a trace/HS norm of a full Hessian. The old diagonal-operator lower bound therefore does not apply.

The polygon Taylor bound

\[
\|D^2\mathfrak T_n[v,w]\|_{\oplus HS}
\le CM_n\|v\|_{2,M}\|w\|_{2,M}
\tag{13.7}
\]

is dimension-uniform by assumption. The maximum tube event (13.4) pays only \(\sqrt{M_n}\), not \(\sqrt{p_n}\). Bounded total energy converts every differentiated rank-one lag product to HS norm through

\[
\|x\otimes y\|_{HS}=\|x\|\,\|y\|,
\tag{13.8}
\]

again without rank or dimension.

Thus no analytic obstruction survives the complete producer package. The theorem applies uniformly to every triangular law, in arbitrary \(p_n\), satisfying those assumptions. This is a uniform theorem over the declared class, not merely an existence example.

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

### 13.3 Uniform FRAME-2P theorem

Choose

\[
b_n=n^{-1/7},\qquad M_n\asymp n^{2/7},\qquad
c_n=n^{-\gamma},\qquad {1\over6}<\gamma<{3\over14}.
\]

Under Section 13.1, the same observable two-path polygon estimator satisfies uniformly over the class

\[
\widehat{\mathfrak T}^{2p}_n-\mathfrak T_n
=\mathbb G_{E,n}[Z_n]+\mathbb G_{V,n}[\varphi_{n,c}]+R_n,
\tag{13.9}
\]

\[
\|\mathbb G_{E,n}[Z_n]\|_{\oplus HS}
+\|\mathbb G_{V,n}[\varphi_{n,c}]\|_{\oplus HS}
=O_p(n^{-1/2}),
\tag{13.10}
\]

and

\[
\begin{aligned}
\|R_n\|_{\oplus HS}
=O_p\{&
M_n(r_T^2+r_Tr_V+r_V^2)+M_n^{-2}
+c_n^3+(nc_n)^{-1}\\
&+(n\sqrt{c_n})^{-1}+n^{-1/2}r_V\}
+O(n^{-a})+\rho_{mask,n}+\rho_{CF,n}
=o_p(n^{-1/2}).
\end{aligned}
\tag{13.11}
\]

All constants in (13.9)--(13.11) are uniform in \(p_n\). The downstream assembly remains

\[
\|\widehat{\mathbb L}^{db}_n-\mathbb L_n\|_{op}
\le2A_{2,n}d_n^{db}+(d_n^{db})^2,
\tag{13.12}
\]

so loading recovery additionally requires the actual uniform signal condition

\[
2A_{2,n}d_n^{db}+(d_n^{db})^2=o_p(\Delta_n).
\tag{13.13}
\]

The null spectrum still satisfies

\[
\widehat\lambda_{r+1,n}^{db}\le(d_n^{db})^2=O_p(n^{-1}).
\tag{13.14}
\]

No bounded-energy assumption is used to hide \(A_{2,n}\), rank, or the eigengap.

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

### 13.4 Nonempty genuinely curved growing-dimensional witness

For arbitrary \(p_n\ge3\), take

\[
\mathcal M_n=\mathbb H^2(-1)\times\mathbb R^{p_n-2}.
\]

Embed the C-dossier model of Sections 2--5 in the \(\mathbb H^2(-1)\times\mathbb R\) subproduct and set all remaining Euclidean coordinates identically to zero, or add independent bounded coordinates whose total squared energy is uniformly summable and whose positive-lag covariance is zero. Product curvature, injectivity, Karcher coercivity, Exp/Log/PT/Jacobi derivatives, and Richardson derivatives have the same dimension-uniform bounds as in the active subproduct. The same one-dependent innovations give exact local proxies and the same masks.

The lag signal and non-rigid frame coefficient remain in the hyperbolic two-plane:

\[
\Gamma_{n,1}=c^2\kappa\,a\otimes a,\qquad
\langle K_{n,0},b\otimes a+a\otimes b\rangle_{HS}\ne0.
\tag{13.15}
\]

Hence the class is nonempty for every \(p_n\), has bounded total energy and fixed rank, and remains genuinely nonflat and non-rigid. Zero inactive coordinates do not trivialise the geometric correction: the active hyperbolic frame generator varies with time and does not commute with the rank-one lag row.

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.**

### 13.5 Revised final gate

The completion audit promotes FRAME-2P from Gate B to Gate A under the explicit dimension-uniform producer package in Section 13.1. This is a generic theorem over arbitrary-\(p_n\) curved laws satisfying that package, with a nonempty genuinely curved growing-dimensional witness. It is not a theorem that bounded total energy alone implies the producer package.

The same-band score-only estimator remains **DISPROVED**. The finite-dimensional hyperbolic-product theorem remains a valid restricted fallback. The previous Gate-B-only classification is **SUPERSEDED**.

**Final completion-audit status: PROVED UNDER EXPLICIT ASSUMPTIONS.**
