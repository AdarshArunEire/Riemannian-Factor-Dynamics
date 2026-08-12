---
type: working-proof-dossier
title: BW-SIZE-FIXED-MARGIN — Agent B transport and generated geometry
status: cross-audit-pass-1-complete-repairs-recorded-pending-agent-a-interface
authority: noncanonical-agent-b-only
scope: fixed-margin Stage 1 only
---

# BW-SIZE-FIXED-MARGIN — Agent B transport and generated geometry

> **NONCANONICAL FIRST DOSSIER.** This file contains Agent B's independent fixed-margin derivation. It does not change theorem status. It does not address any downstream margin regime. The archived incomplete sketch was read only after the current canonical and fixed-size consumers were identified; every display below was rederived from the quotient definitions.

## 0. Verdict of this workstream

With Agent A's repaired dimension-uniform interface A-IF from Section 3, the complete Agent-B consumer chain is proved on the explicit generated domain GD below, pending hostile pass two. Radial and polygonal BW transport are isometries. Their endpoint variations satisfy a typed variational ODE; ruled-surface comparison is additive in curvature-weighted area. An independently parameterized \(N\)-segment PT derivative has the explicit polynomial \(N+\mathsf L\) dependence in (4.13), while the coherent PF comparison has no multiplicative \(C^N\), hidden \(\sqrt m\), trace, or untyped-speed loss and pays the displayed \((N+1)r_N^2\).

The positive-Hessian radius follows from a uniform observation derivative of the Hessian and is not assumed. Exp, Log, polar alignment, Richardson, blend, chord, connector, and the canonical ruled maps are finite invariant compositions and have uniform fixed-order derivatives on `GD`.

Agent A's pass-one repairs to A-IF have been checked in Section 14.7. No B-side lemma is currently left unstated; the repaired chain awaits the mandated independent hostile pass.

## 1. Typed domain and norms

Fix \(0<\alpha<\beta<\infty\), \(\chi>0\), \(r_0>0\), and an integer \(k_0\ge1\). Put

\[
k_*=\max\{k_0,2\}.
\tag{1.0}
\]

The order-two floor is consumed only by the positive-Hessian radius: even when the requested output order is \(k_0=1\), \(D_B\mathsf H\) is a second derivative of Log. Write

\[
\pi(L)=LL^T,\qquad \mathcal P_m={\rm SPD}(m),\qquad
\mathcal B_{\alpha,\beta}=\{A:\alpha I\preceq A\preceq\beta I\}.
\]

The lift norm is Frobenius, (\|Z\|_{\ell}=\|Z\|_F); matrix coefficients are paid in (\|\cdot\|_{\rm op}). Tangent directions use

\[
\|U\|_{A,\rm BW}^2
=\frac12\operatorname{tr}\{U\mathcal L_A^{-1}U\},
\qquad \mathcal L_A(S)=AS+SA.
\tag{1.1}
\]

If (E_U=S_U L) is the horizontal lift, (S_U=\mathcal L_A^{-1}U), then

\[
\|E_U\|_F=\|U\|_{A,\rm BW}.
\tag{1.2}
\]

Diagonalising (A), not choosing eigenvectors as differentiable coordinates, gives the exact dimension-free equivalence

\[
\frac1{4\beta}\|U\|_F^2
\le \|U\|_{A,\rm BW}^2
\le\frac1{4\alpha}\|U\|_F^2.
\tag{1.3}
\]

This sharper formula replaces the looser equivalence in the archived seed. Base-varying tangent norms are compared only after a stated connector or by (1.3); PT itself is a BW isometry.

### GD — explicit generated-domain hypotheses

Every tuple consumed below must satisfy all of the following checkable conditions.

1. Every base, observation, stage mean, Richardson/blend output, chord point, connector point, ruled-surface point, and reconstruction output lies in (\mathcal B_{\alpha,\beta}).
2. Every lift used in an Exp output has (\sigma_{\min}(L+H)\ge\chi). Every polar input (C=M^TL) has (\sigma_{\min}(C)\ge\chi). (For two banded principal factors one automatically has (\sigma_{\min}(M^TL)\ge\alpha); the separate (\chi) covers all generated gauges and Exp inputs.)
3. Every radial or connector segment has lift length (\ell_j=\|D_j\|_F\le r_0). Every complete polygon has typed total lift length
   \[
   \mathsf L(\gamma)=\sum_{j=0}^{N-1}\ell_j\le r_0.
   \tag{1.4}
   \]
4. Parameter derivatives are operator norms on normalized endpoint/lift directions. The five-input theorem covers only the canonical ruled maps made by the chord/connector constructions from generated endpoints. For such a family \(F(s,t)\), define its actual typed zeroth budget
   \[
   \mathsf A_0(F)=\int_0^1\|F_s\|_{\rm BW}\|F_t\|_{\rm BW}\,dt,
   \tag{1.5}
   \]
   and, at higher order, the corresponding integrals of the displayed covariant derivatives of \(F_s,F_t\). Section 7 obtains these budgets by differentiating the canonical endpoint map, so they are outputs of the primitive recurrence, not uncapped extra inputs. For an arbitrary externally supplied or reparameterized ruled family, Sections 5 and 8 remain valid only with its \(\mathsf A_q(F)\) displayed separately; such a family is not covered by the five-input common constant.
5. The canonical blend weight and its derivatives through \(k_0\) are fixed numerical constants. The only signed lift combination is Richardson with \(\lambda=(1/3,-2,8/3)\).
6. **Named G1 constraint.** Assume the compatible case
   \(\max\{\chi,\chi^2\}<\beta\) and choose
   \[
   c=\frac{\beta+\max\{\alpha,\chi,\chi^2\}}2,\qquad A_*=cI.
   \]
   After \(\rho_{\rm H}\) is defined in (6.8), choose
   \[
   0<3\rho_c<
   \min\left\{\rho_{\rm H},
   \sqrt c-\sqrt\alpha,
   \sqrt\beta-\sqrt c\right\},
   \qquad
   \mathcal D_c=\overline B_{\rm BW}(A_*,\rho_c).
   \tag{1.5a}
   \]
   The positive stage means are constrained to \(\mathcal D_c\), every population stage lies at distance at least \(\delta_c>0\) from \(\partial\mathcal D_c\), and every internal criterion pair \((q,X)\) obeys \(q\in\mathcal D_c\) and \(d_{\rm BW}(q,X)\le\rho_{\rm H}\). This last condition is a support/generated-pair condition, not a consequence of the raw band.

`GD` is nonempty uniformly in (m): take a scalar base (cI), (\alpha<c<\beta), and all endpoint lift perturbations in an operator/Frobenius ball of radius

\[
\delta<\min\left\{r_0,
\frac{\rho_c}{5},\frac{\rho_{\rm H}}{10},
\frac{\sqrt c-\max\{\sqrt\alpha,\chi\}}5,
\frac{\sqrt\beta-\sqrt c}5,
\frac{\sqrt c-\sqrt\chi}5,
\frac{c-\chi}{10(1+\sqrt c)}\right\},
\tag{1.6}
\]

where \(c\) is chosen so that
\(\max\{\alpha,\chi,\chi^2\}<c<\beta\). Then the scalar polar input \(cI\) has margin \(c>\chi\), while the Exp factor has margin \(\sqrt c>\chi\). Affine lift combinations, including Richardson since \(\sum|\lambda_j|=5\), retain the declared output band, polar margin, and Exp margin. This proves nonemptiness without a coordinate count. If \(\max\{\chi,\chi^2\}\ge\beta\), this GD package is empty and the theorem must say so.

The polar-margin algebra covers the largest affine output, not only raw endpoints. Richardson can enlarge a lift perturbation from \(\delta\) to at most \(5\delta\). Thus for any two generated factors
\(L=\sqrt c\,I+E\), \(M=\sqrt c\,I+F\) with
\(\|E\|_{\rm op},\|F\|_{\rm op}\le5\delta\),

\[
\sigma_{\min}(M^TL)
\ge\sigma_{\min}(M)\sigma_{\min}(L)
\ge(\sqrt c-5\delta)^2.
\tag{1.6a}
\]

The \((\sqrt c-\sqrt\chi)/5\) term in (1.6) makes \(\sqrt c-5\delta>\sqrt\chi\), so the last quantity is strictly larger than \(\chi\). The \(\rho_c/5,\rho_{\rm H}/10\) terms likewise cover the fivefold generated perturbation, putting every generated point in this full-dimensional example inside the constraint interior and making every pair of such points shorter than \(\rho_{\rm H}\). Thus the example checks the internal G1 pair condition as well as all generated-factor margins.

The constraint in (1.5a) is compact for each \(m\): it is closed and stays a positive Euclidean distance from the singular boundary. It is strongly geodesically convex with dimension-uniform modulus. Indeed, for \(A,B\in\mathcal D_c\), every point of their unique BW chord is within \(3\rho_c\) of \(A_*\) by the triangle inequality. The three-radius slacks in (1.5a) put this entire preliminary chord inside the declared spectral band and inside the radius \(\rho_{\rm H}\). Equation (6.9), applied to \((q,A_*)\), then makes \(\tfrac12d_{\rm BW}(q,A_*)^2\) \(1/2\)-strongly convex along that chord. Hence the chord cannot leave the smaller sublevel ball \(\mathcal D_c\). This also proves existence/uniqueness of every constrained positive stage objective: compactness gives existence, and the internal pair condition plus (6.9) gives strong convexity. The scalar-centred perturbation ball above gives a full-dimensional nonempty example, not only a scalar ray.

The elementary multiplication rules used everywhere are

\[
\|XYZ\|_F\le\|X\|_{\rm op}\|Y\|_F\|Z\|_{\rm op},
\quad
\|XY\|_F\le\|X\|_{\rm op}\|Y\|_F,
\quad
\|YX\|_F\le\|Y\|_F\|X\|_{\rm op}.
\tag{1.7}
\]

No Frobenius norm of an undifferentiated base lift is used.

## 2. Radial/chord geometry and endpoint variations

Let (L=A^{1/2}), (M=B^{1/2}),

\[
Q=\operatorname{polar}(M^TL),\qquad N=MQ,\qquad D=N-L.
\tag{2.1}
\]

Then (L^TD=D^TL), (\|D\|_F=d_{\rm BW}(A,B)), and the radial/chord lift is

\[
L_t=L+tD,\quad \dot L_t=D,\quad
\gamma_{A,B}(t)=L_tL_t^T.
\tag{2.2}
\]

The base speed is exactly typed:

\[
\|\dot\gamma(t)\|_{\gamma(t),\rm BW}=\|D\|_F=\ell(A,B).
\tag{2.3}
\]

The endpoint maps in (2.1) use only square root, transpose, multiplication, polar, and affine combination. At every multiplication, an undifferentiated factor is in operator norm, for example

\[
\|D(M^TL)[\dot M,\dot L]\|_F
\le\|\dot M\|_F\|L\|_{\rm op}
+\|M\|_{\rm op}\|\dot L\|_F
\le\sqrt\beta(\|\dot M\|_F+\|\dot L\|_F).
\tag{2.4}
\]

Invariant square-root and polar Sylvester/resolvent derivatives therefore give, for normalized endpoint directions and (q\le k_0),

\[
\sup_{t\in[0,1]}\|D^q_{A,B}L_t\|_{F^q\to F}
+\sup_t\|D^q_{A,B}\dot L_t\|_{F^q\to F}
\le C_{{\rm rad},q}(\alpha,\beta,\chi).
\tag{2.5}
\]

No eigenvector gap occurs. A chord between banded endpoints is uniformly full rank even before imposing `GD`: with (T=A^{-1/2}(A^{1/2}BA^{1/2})^{1/2}A^{-1/2}\succ0),

\[
\sqrt{\alpha/\beta}\,\|x\|\le\|Tx\|\le\sqrt{\beta/\alpha}\,\|x\|,
\]

so (L_t=((1-t)I+tT)L) has

\[
\sigma_{\min}(L_t)\ge\sqrt\alpha\min\{1,\sqrt{\alpha/\beta}\}.
\tag{2.6}
\]

The expanded chord band is thus dimension-uniform. `GD` simply requires that the chosen common band already contains it.

## 3. Exact Agent-A interface

Let \(C_{{\rm prim},q}\) bound the square-root, polar, horizontal-lift, projector, and aligned-chord derivatives; let \(C_{\Gamma,q}\) bound the quotient connection; and let \(C_{R,q}\) bound the covariant curvature derivatives, all in the displayed Frobenius/BW multilinear norms. The sole primitive interface used below is

\[
\max_{q\le k_*}C_{{\rm prim},q}
+\max_{q\le k_0-1}C_{\Gamma,q}
+\max_{q\le k_0-1}C_{R,q}
\le C_A(\alpha,\beta,\chi,k_*)<\infty,
\tag{A-IF}
\]

uniformly in (m), produced from the horizontal projector and O'Neill quotient calculus with the same operator-by-Frobenius rule (1.7). Section 4 independently derives the complete transport ODE from the quotient definition; it does not assume a PT formula from the archived seed.

## 4. Parallel transport ODE and parameter variations

Let (L(t)) be a horizontal lift of a (C^1) base path and let (H(t)\in\mathcal H_{L(t)}) lift a tangent field. The quotient Levi-Civita definition says that (H) is parallel iff

\[
P^{\mathcal H}_{L(t)}\dot H(t)=0.
\tag{4.1}
\]

Thus (\dot H=L\Omega) for a skew (\Omega). Differentiating horizontality (L^TH=H^TL) gives

\[
(L^TL)\Omega+\Omega(L^TL)=H^T\dot L-\dot L^TH,
\tag{4.2}
\]

and hence the exact lift ODE

\[
\boxed{\dot H
=L\,\mathscr S_{L^TL}^{-1}(H^T\dot L-\dot L^TH).}
\tag{4.3}
\]

Typing every multiplication,

\[
\|H^T\dot L-\dot L^TH\|_F
\le2\|H\|_F\|\dot L\|_{\rm op},
\quad
\|\mathscr S_{L^TL}^{-1}\|_{F\to F}\le(2\alpha)^{-1},
\]

\[
\|\dot H\|_F
\le(\sqrt\beta/\alpha)\|\dot L\|_{\rm op}\|H\|_F.
\tag{4.4}
\]

More importantly, PT is exactly isometric. Since (H^TL) is symmetric and (\Omega) skew,

\[
\frac d{dt}\|H\|_F^2
=2\operatorname{tr}(H^TL\Omega)=0.
\tag{4.5}
\]

Thus the base propagator has norm one between the horizontal lift spaces; no Gronwall exponential and no segment factor is paid for transport itself.

Let \(\theta\) be a normalized endpoint or ruled-family parameter. With \(B(L,\dot L)\) denoting the linear coefficient in (4.3), differentiation yields for every multi-index \(\nu\ne0\)

\[
\partial_t H_\nu
=B H_\nu+
\sum_{0<\rho\le\nu}{\nu\choose\rho}
(\partial_\theta^\rho B)H_{\nu-\rho}.
\tag{4.6}
\]

Variation of constants uses the norm-one PT propagator. If

\[
K_q=\int_0^1\|D_\theta^q B(L,\dot L)\|_{\rm op}\,dt,
\tag{4.7}
\]

then induction gives the explicit complete-Bell-polynomial estimate for fixed trivialized initial data

\[
\|D_\theta^q{\rm PT}_\gamma\|_{\rm op}
\le \mathfrak B_q(K_1,\ldots,K_q),
\qquad q\le k_0,
\tag{4.8}
\]

where (\mathfrak B_0=1),

\[
\mathfrak B_q(K_1,\ldots,K_q)
=\sum_{\substack{a_1+2a_2+\cdots+qa_q=q}}
\frac{q!}{\prod_j a_j!(j!)^{a_j}}\prod_jK_j^{a_j}.
\tag{4.9}
\]

If the initial horizontal fibre varies and \(J_0(\theta):E_*\to\mathcal H_{L(0,\theta)}\) is its declared trivialization, put

\[
I_j=\|D_\theta^jJ_0(\theta)\|_{\rm op}.
\]

The missing initial-data terms are exactly

\[
\|D_\theta^q\{P_{\gamma_\theta}J_0(\theta)\}\|_{\rm op}
\le
\sum_{j=0}^q{q\choose j}
\mathfrak B_{q-j}(K_1,\ldots,K_{q-j})I_j.
\tag{4.9a}
\]

For endpoint-varying transport, use radial connectors
\(J_0(\theta)=C_0(\theta)\) and \(J_1(\theta)=C_1(\theta)\) from fixed reference fibres and differentiate the typed operator

\[
\mathscr P(\theta)=C_1(\theta)^{-1}
P_{\gamma_\theta}C_0(\theta).
\tag{4.9b}
\]

The connector recurrences are one-segment instances of (4.6)--(4.9a) with fixed initial fibre; differentiating \(C_1^{-1}\) adds the ordinary finite product/inverse majorant. Thus no varying-fibre derivative is omitted.

Equations (2.5), the differentiated Sylvester equation in (4.3), and (1.7) imply, for one radial segment,

\[
K_q\le C_{{\rm ode},q}(\alpha,\beta,\chi,k_0)(1+\ell(\gamma))
\le C_{{\rm ode},q}(\alpha,\beta,\chi,k_0)(1+r_0).
\tag{4.10}
\]

This proves radial/connector endpoint variations. The harmless constant \(1\) is real for separately varying segment endpoints: an endpoint derivative need not vanish when the segment collapses. A polygon is the same ODE on a piecewise-\(C^1\) path. Corners require composition, not differentiation of a nonexistent corner velocity.

### Polygonal parameter accumulation

For segment propagators (P_j), (P_{N-1}\cdots P_0) is an isometry. Differentiating the product and inserting isometries on both sides gives

\[
\|D(P_{N-1}\cdots P_0)\|
\le\sum_j\|DP_j\|.
\tag{4.11}
\]

At order \(q\), the Leibniz sum is bounded by the same Bell polynomial (4.9) with aggregate budgets

\[
K_s^{\rm pol}=\sum_{j=0}^{N-1}K_{s,j}
\le C_{{\rm ode},s}\{N+\mathsf L(\gamma)\}.
\tag{4.12}
\]

Here each endpoint-direction array is measured in the declared direct-sum maximum norm

\[
\|\delta\mathbf A\|_{\oplus,\infty}
=\max_{0\le j\le N}\|\delta A_j\|_{A_j,\rm BW}.
\tag{4.12a}
\]

Thus the derivative of an \(N\)-segment polygonal PT map with all segment endpoints allowed to vary independently has the honest bound

\[
\|D^q{\rm PT}_{\rm pol}\|_{\rm op}
\le \mathfrak B_q\!\left(
C_{{\rm ode},1}(N+\mathsf L),\ldots,
C_{{\rm ode},q}(N+\mathsf L)\right).
\tag{4.13}
\]

There is no factor \(C^N\), but there can be a polynomial segment-count factor for this stronger, independently parameterized map. If only \(\ell_j\le r_0\) is known, \(\mathsf L\le Nr_0\) must honestly be inserted. Under GD, \(\mathsf L\le r_0\), while \(N\) remains visible in (4.13).

With the direct-sum \(\ell^1\) endpoint norm, the first derivative can instead be bounded by the maximum one-vertex coefficient and has no \(N\), but that is a different input norm. No norm switch is made silently.

PF does **not** consume (4.13). It consumes a coherent ruled deformation of the complete polygon. For that map, adjacent endpoint gauge terms cancel and Section 5 bounds the derivative by the summed ruled budgets. Section 8 then shows exactly where \(N\) remains: only in the quadratic vertex accumulation and the chord-lens approximation.

## 5. Connection variation and ruled surfaces

Let \(F(s,t)\) be a regular ruled family, \(W(s,t)\) parallel in \(t\), and \(W(s,0)=w(s)\). Adopt Agent A's convention

\[
R(X,Y)Z=\nabla_Y\nabla_XZ-\nabla_X\nabla_YZ+\nabla_{[X,Y]}Z.
\]

Then the commuting-coordinate identity and its integrated form are

\[
\nabla_t\nabla_sW-\nabla_s\nabla_tW=R(F_s,F_t)W,
\]

\[
\nabla_sW(s,1)=P_{0\to1}\nabla_sw(s)
+\int_0^1P_{t\to1}R(F_s,F_t)W(s,t)\,dt.
\tag{5.1}
\]

The overall sign changes with the curvature convention but the type and bound do not. By PT isometry and `A-IF`,

\[
\|\nabla_sW(s,1)\|
\le\|\nabla_sw(s)\|
+C_{R,0}\|w(s)\|\mathsf A_0(F).
\tag{5.2}
\]

Repeated (s)-differentiation produces only covariant derivatives of (R,F_s,F_t,W). Using (5.1) recursively gives a Bell polynomial in the typed ruled budgets and (C_{R,q}), (q\le k_0-1). No coordinate sum occurs.

For a closed ruled cell, after endpoint connectors make the two transports have identical domain/codomain,

\[
\|P_{\partial F}-I\|_{\rm op}
\le C_{R,0}\int_0^1\int_0^1
\|F_s\|_{\rm BW}\|F_t\|_{\rm BW}\,dt,ds.
\tag{5.3}
\]

This is the connection-variation estimate consumed by PF.

## 6. Exp, Log, score, Hessian, and all consumed derivatives

With (2.1),

\[
\Log_AB=d\pi_L(D)=DL^T+LD^T,
\qquad
\Exp_A(d\pi_LH)=\pi(L+H).
\tag{6.1}
\]

The horizontal lift of (\Log_AB) is exactly (D), so

\[
\|\Log_AB\|_{A,\rm BW}=\|D\|_F=d_{\rm BW}(A,B).
\tag{6.2}
\]

For a base lift direction (E\in\mathcal H_L), let

\[
\mathcal N(L,M)=M\operatorname{polar}(M^TL).
\]

The horizontal lift of the observation Hessian
(\mathsf H(A,B)=-\nabla_A\Log_AB) is the exact invariant formula

\[
\boxed{
\overline{\mathsf H(A,B)U}
=P_L^{\mathcal H}\{E-D_L\mathcal N(L,M)[E]\},
\qquad E=\overline U.}
\tag{6.3}
\]

Observation differentiation of the Hessian, with \(A,U\) fixed and observation lift direction \(\dot M\), is the mixed derivative

\[
-P_L^{\mathcal H}D_M D_L\mathcal N(L,M)[\dot M,E],
\tag{6.3a}
\]

not \(-P_L^{\mathcal H}D_M\mathcal N[\dot M]\), which is only the observation derivative of Log. Base differentiation of (6.3) differentiates \(P_L^{\mathcal H}\), \(E\), and \(D_L\mathcal N\), with the quotient connection used to compare outputs. Thus every consumed base/observation derivative is a finite composition of projector, horizontal lift, square root, polar, multiplication, and connection derivatives. Formula (6.3a) is why the primitive order is \(k_*=\max\{k_0,2\}\).

At a representative multiplication,

\[
\|D(MQ)[\dot M,\dot Q]\|_F
\le\|\dot M\|_F\|Q\|_{\rm op}
+\|M\|_{\rm op}\|\dot Q\|_F
\le\|\dot M\|_F+\sqrt\beta\|\dot Q\|_F.
\tag{6.4}
\]

The same operator-by-Frobenius typing at every product and `A-IF` give

\[
\max_{q\le k_0}\{\|D^q\Exp\|,\|D^q\Log\|\}
+\max_{q\le k_0-1}\|D^q\mathsf H\|
\le C_{\rm EH}(\alpha,\beta,\chi,k_0),
\tag{6.5}
\]

independently of (m). The score of one-half squared distance is

\[
\operatorname{grad}_A\tfrac12d_{\rm BW}(A,B)^2=-\Log_AB,
\tag{6.6}
\]

so (6.5) is exactly the score/Hessian/base-observation package consumed by G1 and the feasible Log expansion.

### Positive Hessian and dimension-uniform normal radius

For every (A), (\mathsf H(A,A)=I_{T_A}). Hold (A) fixed and join (A) to (B) by its radial geodesic. Let (L_H) be the typed observation derivative bound from (6.5), after PT identifies the varying observation direction. Then

\[
\|\mathsf H(A,B)-I\|_{{\rm op},A}
\le L_Hd_{\rm BW}(A,B).
\tag{6.7}
\]

Consequently the explicit dimension-uniform radius

\[
\rho_{\rm H}=\min\{r_0,(2L_H)^{-1}\}
\tag{6.8}
\]

gives, on every `GD` pair with (d_{\rm BW}(A,B)\le\rho_{\rm H}),

\[
\frac12 I\preceq\mathsf H(A,B)\preceq\frac32 I.
\tag{6.9}
\]

The SPD polar alignment is unique, so Log exists on these pairs; (2.6) keeps the radial path full rank. This proves the normal-radius/coercivity step without fixed-dimensional compactness and without presupposing the desired radius.

## 7. Richardson, blend, chord, and generated-set closure

Align (L_j) to (L_1): (N_j=L_j\operatorname{polar}(L_j^TL_1)), (D_j=N_j-L_1). The Richardson lift and output are

\[
L_R=L_1+\sum_{j=1}^3\lambda_jD_j,
\qquad \mathscr R(A_1,A_2,A_3)=L_RL_R^T.
\tag{7.1}
\]

Since (\|D_j\|_{\rm op}\le\|D_j\|_F=d_{\rm BW}(A_1,A_j)),

\[
\sigma_{\min}(L_R)
\ge\sqrt\alpha-\sum_j|\lambda_j|d_{\rm BW}(A_1,A_j).
\tag{7.2}
\]

Thus the checkable closure condition

\[
\sum_j|\lambda_j|d_{\rm BW}(A_1,A_j)\le\sqrt\alpha-\chi
\tag{7.3}
\]

retains the Exp factor margin. It does **not** by itself retain the same lower output band \(\alpha I\): signed motion from a point on the lower boundary can leave that band. Full Richardson closure therefore also requires population inner-band slack and the separate output-membership test in GD. An analogous operator perturbation bound handles upper-band slack. The chord and fixed-width blend are the same construction with coefficients \((1-t,t)\); the ruled maps are two canonical nested chord families. Differentiating (7.1) and the chord formulas, then using (2.5), (4.8), and (5.1), yields

\[
\max_{q\le k_0}
\{\|D^q\mathscr R\|,\|D^q{\rm Blend}\|,
\|D^q{\rm Chord}\|,\|D^q{\rm Ruled}\|\}
\le C_{\rm gen}(\alpha,\beta,\chi,r_0,k_0).
\tag{7.4}
\]

The generated-domain event is not inferred from raw spectral bands: it is the finite membership test consisting of (i) nested inner/output band tests, (ii) all polar/Exp singular-value tests, (iii) (7.3), (iv) complete chord/connector/ruled-path tests, (v) the normal-pair test (6.8), and (vi) the constraint/interior tests in (1.5a).

Let \(\delta_{\rm GD}>0\) be the minimum population slack to every failure set in this list. The fixed-order endpoint maps in Sections 2 and 7 are Lipschitz with constant at most \(C_B^{\rm rec}\); hence endpoint perturbations of size \(o(\delta_{\rm GD}/C_B^{\rm rec})\) put the **complete images**, not only their endpoints, inside GD. On an \(N+1\)-vertex grid, the exact RMS-to-maximum implication is

\[
\max_{0\le j\le N}e_j
\le\sqrt{N+1}\,r_N.
\tag{7.5}
\]

Therefore generated-event reach requires either a separate sup-grid bound
\(\max_je_j=o_p(\delta_{\rm GD}/C_B^{\rm rec})\), or

\[
\sqrt{N+1}\,r_N
=o_p(\delta_{\rm GD}/C_B^{\rm rec}).
\tag{7.6}
\]

For canonical \(N\asymp\ell_n^{-2/3}\) and \(r_N=O_p(\ell_n)\), the left side is \(O_p(\ell_n^{2/3})\). Population interior slack \(\delta_c\) is included in \(\delta_{\rm GD}\). Scalar multiples of \(I\) with perturbations satisfying (1.6) show the complete assumption package is nonempty.

## 8. Exact finite-polygon accumulation and PF reach

Let true vertices (A_j=\mu(j/N)), estimated vertices (\widehat A_j), and

\[
e_j=d_{\rm BW}(A_j,\widehat A_j),\quad
r_N^2=(N+1)^{-1}\sum_{j=0}^Ne_j^2,
\]

\[
\ell_j=d_{\rm BW}(A_j,A_{j+1}),\quad
\mathsf L_N=\sum_{j=0}^{N-1}\ell_j\le r_0.
\tag{8.1}
\]

Let \(C_j:T_{A_j}\mathcal P_m\to T_{\widehat A_j}\mathcal P_m\) be radial PT along the unique connector. If

\[
P_{\rm pol}:T_{A_0}\to T_{A_N},\qquad
\widehat P_{\rm pol}:T_{\widehat A_0}\to T_{\widehat A_N},
\]

the only typed global difference is

\[
\mathcal E_{\rm pol}
=C_N^{-1}\widehat P_{\rm pol}C_0-P_{\rm pol}
:T_{A_0}\to T_{A_N}.
\tag{8.1a}
\]

The canonical geodesic ruled cell and the derivative bounds in Section 7 give

\[
c_j(s)=\gamma_{A_j,\widehat A_j}(s),\qquad
c_{j+1}(s)=\gamma_{A_{j+1},\widehat A_{j+1}}(s),
\]

\[
F_j(s,t)=\gamma_{c_j(s),c_{j+1}(s)}(t),
\qquad (s,t)\in[0,1]^2.
\tag{8.2a}
\]

Its four boundary maps are exactly the true chord \(F_j(0,\cdot)\), estimated chord \(F_j(1,\cdot)\), and radial connectors \(F_j(\cdot,0)=c_j\), \(F_j(\cdot,1)=c_{j+1}\). Equivalently it may be split along either geodesic diagonal into the two ruled triangles used by the fixed-size proof.

Let \(J=F_{j,s}\). Along each \(t\)-geodesic, \(J\) is the endpoint Jacobi field with
\(\|J(s,0)\|=e_j\) and \(\|J(s,1)\|=e_{j+1}\). The endpoint Jacobi operators vanish at the opposite endpoint. Their uniform first derivative from (7.4), followed by Taylor's theorem at \(t=0,1\), gives

\[
\|F_{j,s}(s,t)\|_{\rm BW}
\le C_J\{(1-t)e_j+t e_{j+1}\}.
\tag{8.2b}
\]

This is the first-order vanishing missing from a bare bounded-derivative citation. Since each connector has constant speeds \(e_j,e_{j+1}\), the triangle inequality gives

\[
\|F_{j,t}(s,t)\|_{\rm BW}
=d_{\rm BW}(c_j(s),c_{j+1}(s))
\le \ell_j+s(e_j+e_{j+1}).
\tag{8.2c}
\]

Therefore, writing \(E_j=e_j+e_{j+1}\),

\[
\begin{aligned}
\operatorname{Area}(F_j)
&\le\int_0^1\!\!\int_0^1
\|F_{j,s}\|_{\rm BW}\|F_{j,t}\|_{\rm BW}\,dt\,ds\\
&\le C_J\frac{E_j}{2}\left(\ell_j+\frac{E_j}{2}\right)\\
&\le C_J'\{\ell_j(e_j+e_{j+1})+e_j^2+e_{j+1}^2\}.
\end{aligned}
\tag{8.2d}
\]

Renaming \(C_J'\) as \(C_J\) proves the advertised producer

\[
\operatorname{Area}(F_j)
\le C_J\{\ell_j(e_j+e_{j+1})+e_j^2+e_{j+1}^2\}.
\tag{8.2}
\]

At cell \(j\), the typed difference is
\(C_{j+1}^{-1}\widehat P_jC_j-P_j:T_{A_j}\to T_{A_{j+1}}\).
Telescoping these products, with every outside factor an isometry, and using (5.3),

\[
\boxed{
\|\mathcal E_{\rm pol}\|_{\rm op}
\le C_{R,0}C_J
\left[\sum_{j=0}^{N-1}\ell_j(e_j+e_{j+1})
+2\sum_{j=0}^Ne_j^2\right].}
\tag{8.3}
\]

There is no unshown segment factor. With only total length, the exact first sum in (8.3) must be retained (or bounded by (2\mathsf L_N\max e_j)); replacing it by a dimension-free RMS term would be false. For the canonical uniform time grid, let the typed mean-curve speed and acceleration be

\[
v_\mu=\sup_u\|\dot\mu(u)\|_{\rm BW},\qquad
a_\mu=\sup_u\|\nabla_u\dot\mu(u)\|_{\rm BW}.
\tag{8.4}
\]

Then (\ell_j\le v_\mu/N), and Cauchy--Schwarz gives

\[
\sum_j\ell_j(e_j+e_{j+1})
\le2v_\mu\sqrt{(N+1)/N}\,r_N,
\qquad
\sum_je_j^2=(N+1)r_N^2.
\tag{8.5}
\]

The lens between (\mu) and its chord has total area at most

\[
C_Jv_\mu a_\mu N^{-2}.
\tag{8.6}
\]

Indeed, on one interval of width \(\Delta=N^{-1}\), covariant Taylor expansion about the left endpoint gives transverse curve-to-chord displacement at most \(C_Ja_\mu\Delta^2\), while the longitudinal speed is at most \(C_Jv_\mu\Delta\) after rescaling the cell to \([0,1]\). Their ruled-lens area is therefore at most \(C_Jv_\mu a_\mu\Delta^3\); summing \(N\) cells gives (8.6).

Combining (8.3)--(8.6), including radial endpoint connectors, proves

\[
\boxed{
\|C_N^{-1}P_{\widehat{\rm pol}}C_0-P_\mu\|_{\rm op}
\le C_{\rm PF}
\{v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}\}.}
\tag{8.7}
\]

Here (C_{\rm PF}) depends only on the fixed-margin geometry and (k_0); (v_\mu,a_\mu,N,r_N) are visible path/statistical inputs. If (r_N=O_p(\ell_n)) and (N\asymp\ell_n^{-2/3}), the last two terms are (O_p(\ell_n^{4/3})), so (8.7) is (O_p(\ell_n)). This reaches canonical PF exactly.

## 9. One common B-side constant

The former closed power/exponential display is retracted: neither its particular exponent nor its prefactor had been proved. The valid common constant is recurrence-defined.

Use Agent A's repaired finite product and composition majorants \(\star\) and \(\circledast\). To avoid symbol collisions with the B-side alignment sequence below, define

\[
\mathbf A_q^{\rm rec}=
\max\{q_q,p_q^{\rm pol},h_q,l_q,f_q,t_q,p_q,z_q,\gamma_q,b_q,
v_q^L,\bar s_q,\bar t_q,\bar z_q,a_q^{\rm coef,L},
d_q,\widetilde a_q,a_q^\dagger,\rho_q,\rho_q^A\},
\qquad 0\le q\le k_*,
\tag{9.1}
\]

Keep the curvature list separately at its exact consumed range:

\[
A_{\rm curv}^{\rm rec}
=\max_{0\le q\le k_*-1}\widehat\rho_q.
\tag{9.1a}
\]

Together (9.1)--(9.1a) are exactly the current Agent A (7.12), whose component recurrences are A (7.3)--(7.11). For any displayed finite expression tree \(\mathcal T\), let \(\mathfrak M_q(\mathcal T;\mathbf A^{\rm rec})\) mean: replace every product node by \(\star\), every composition node by \(\circledast\), and every algebraic primitive derivative by its same-order entry in \(\mathbf A^{\rm rec}\). Curvature entries use (9.1a)/(9.5b). This is a finite, computable sum over subsets and set partitions, not a supremum or compactness constant.

Define successively

\[
e_q=\mathfrak M_q\!\left[
(L,M)\mapsto M\,{\rm polar}(M^TL)-L;\mathbf A^{\rm rec}\right],
\tag{9.2}
\]

\[
b_q^{\rm ode}=\mathfrak M_q\!\left[
(L,\dot L,H)\mapsto
L\mathscr S_{L^TL}^{-1}(H^T\dot L-\dot L^TH);
\mathbf A^{\rm rec},e\right],
\tag{9.3}
\]

\[
t_q=\mathfrak B_q\!\left(
(1+r_0)b_1^{\rm ode},\ldots,(1+r_0)b_q^{\rm ode}\right),
\tag{9.4}
\]

with \(t_0=1\). A radial endpoint connector is a one-segment instance of this same sequence. Since inverse PT is its metric adjoint and differentiation of the adjoint preserves operator norms in the fixed connector trivialization, the typed endpoint map (4.9b) has the explicit product majorant

\[
c^{\rm end}=t\star t\star t
\quad\text{for}\quad
C_1^{-1}P_\gamma C_0.
\tag{9.4a}
\]

\[
h_q^{\rm obs}=\mathfrak M_{q+1}\!\left[
(L,M,E)\mapsto
P_L^H\{E-D_L(M{\rm polar}(M^TL))[E]\};
\mathbf A^{\rm rec}\right],
\quad 0\le q\le k_*-1,
\tag{9.5}
\]

and let \(g_q\) be the same expression-tree majorant for Richardson (7.1), blend/chord (2.2), and the explicit canonical ruled map (8.2a). For the curvature factors below define, with no new free symbol,

\[
C_{R,a}:=\widehat\rho_a
\quad(0\le a\le k_0-1),
\tag{9.5b}
\]

the exact covariant-curvature entry of Agent A (7.11)--(7.12). Finally, define \(w_q\) recursively by differentiating (5.1). Since (8.2a) is on the unit square,

\[
\mathsf A_0(F)\le
\sup_{s,t}\|F_s\|\sup_{s,t}\|F_t\|
\le g_1^2,
\qquad
w_0=1+C_{R,0}g_1^2.
\tag{9.5a}
\]

For \(q\ge1\), \(w_q\) is the finite multinomial sum of products

\[
C_{R,a}\,
\|\nabla^{b}F_s\|\,
\|\nabla^{c}F_t\|\,w_d,
\qquad a+b+c+d=q-1,
\tag{9.6}
\]

with the canonical ruled derivative factors bounded by \(g_{b+1},g_{c+1}\) and integrated over the unit square. Thus (9.6) contains no uncapped external ruled budget.

The common B-side consumer constant is

\[
\boxed{
C_B^{\rm rec}(\alpha,\beta,\chi,r_0,k_0)
=1+A_{\rm curv}^{\rm rec}
+\max_{0\le q\le k_0}
\{e_q,b_q^{\rm ode},t_q,c_q^{\rm end},g_q,w_q\}
+\max_{0\le q\le k_*-1}h_q^{\rm obs}.}
\tag{9.7}
\]

Every entry is a finite recurrence in the five inputs once Agent A's repaired \(\mathbf A_q^{\rm rec}\) is substituted. This is the common constant actually consumed by G1 and PF. The stronger independently parameterized polygon derivative is not hidden inside (9.7); it has the separate direct-sum/segment-count bound (4.13).

For the edge order \(k_0=1\), \(k_*=2\): algebraic/Log primitives run through order two, \(h_q^{\rm obs}\) runs through \(q=1\), PT/generated maps run through \(q=1\), and (9.5b) uses only \(\widehat\rho_0\). Thus neither \(\widehat\rho_1\) nor \(\widehat\rho_2\) is silently requested by the normal-radius step.

## 10. Reach to G1, PF, and feasible observations

| Consumer | Exact B-side producer | Reach |
|---|---|---|
| positive stage-mean score-to-distance | (6.9) | strong convexity (1/2) on every generated score pair |
| three-scale population expansion | (6.5), (7.4) | score/Hessian and Richardson derivatives through the fixed consumed order |
| arbitrary-grid/tube event | (7.2)--(7.3) | checkable closure with positive slack; no raw-band shortcut |
| base-point Log recentering | (6.3)--(6.5) | \(\Phi_e^{-1}\Log_{\widehat A}X=\Log_AX-\mathsf H(A,X)e+O(C_B^{\rm rec}\|e\|^2)\) |
| radial endpoint connectors | (4.3)--(4.10) | typed endpoint derivatives and isometry |
| polygonal frame PF | (5.3), (8.3)--(8.7) | exact (v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}) |
| feasible observation RMS | Sections 4, 6, 8 | \(q_n\lesssim C_B^{\rm rec}(r_{\mu,n}+r_{F,n})\) under bounded tangent energy; energy remains a separate assumption |

The geometry proves no energy, dependence, lag orthogonality, signal, eigengap, or selector statement.

## 11. Claim-ledger subset

| ID | Exact claim | Domain and margins | Input/output norms | Producer | Direct consumer | Dimension dependence | Objection | Resolution | Status |
|---|---|---|---|---|---|---|---|---|---|
| B-PT0 | (4.3) is the BW PT lift ODE | `GD`, banded horizontal lift | lift (F\to F) | Section 4 | radial/polygonal PT | none | sign/order in Sylvester RHS | derived by differentiating (L^TH=H^TL) | **PROVED in B dossier; audit pending** |
| B-PT1 | PT is isometric | same | BW tangent/operator | (4.5) | all accumulation | none | archived seed used Gronwall | symmetric-times-skew trace is zero | **PROVED in B dossier; audit pending** |
| B-PTK | endpoint/parameter derivatives obey (4.8), (4.9a)--(4.9b) | GD, normalized endpoint/ruled budgets | multilinear BW operator | (4.6)--(4.10) | connectors, chord, ruled | none | arbitrary reparameterization/varying fibre | canonical ruled budgets and connector trivializations stated | **REPAIRED — AWAITING HOSTILE PASS 2** |
| B-RULED | connection variation is curvature-weighted area | `GD` ruled surfaces | PT operator norm | (5.1)--(5.3) | PF | none | wrong sign/type | convention stated; bound sign-free | **PROVED CONDITIONAL ON A-IF** |
| B-EH | Exp/Log/score/Hessian derivatives uniform | `GD`, band/polar/Exp margins | lift (F), BW multilinear | (6.1)--(6.6) | G1, Log Taylor | none | eigenvector gap or (\|L\|_F) | invariant polar plus op-by-F products | **PROVED CONDITIONAL ON A-IF** |
| B-HESS+ | (\frac12I\preceq\mathsf H\preceq\frac32I) on radius (6.8) | generated pairs within (\rho_H) | BW operator | (6.7)--(6.9) | strong convexity/G1 | none | circular local Hessian radius | derived from (\mathsf H(A,A)=I) and observation derivative | **PROVED CONDITIONAL ON A-IF** |
| B-GEN | Richardson/blend/chord/ruled closure and derivatives | complete `GD` test, (7.3) | BW/F lift multilinear | Section 7 | G1/PF/reconstruction | none | raw bands not closed | explicit singular-value/membership tests; nonempty ball (1.6) | **PROVED UNDER EXPLICIT GENERATED-DOMAIN ASSUMPTIONS** |
| B-POLY | finite PF accumulation is (8.3)/(8.7); stronger derivative is (4.13) | total length \(\le r_0\), \(N\) cells | PT operator; \(\oplus,\infty\); typed speed/acceleration | Sections 4, 8 | PF | none | hidden \(N,C^N,\sqrt N\) | stronger derivative exposes \(N+\mathsf L\); PF pays \((N+1)r_N^2\) | **REPAIRED — AWAITING HOSTILE PASS 2** |
| B-NORM | tangent/lift equivalence (1.3) | (\mathcal B_{\alpha,\beta}) | tangent BW vs matrix F | Section 1 | all conversions | none | looser archived constants | direct Sylvester diagonal calculation | **PROVED** |
| A-IF | uniform quotient connection/curvature derivatives | fixed margins | BW multilinear | Agent A/lead | all B conditional rows | none | moving adjoint/type/closed envelope | repaired by A (4.15)--(4.18), (7.3)--(7.12); checked in Section 14.7 | **REPAIRED — AWAITING HOSTILE PASS 2** |

## 12. First-pass objections already answered

| Claim | Attack | Repair or counterexample | Independent checker | Final status | Canonical consequence |
|---|---|---|---|---|---|
| polygon PT derivatives are bounded uniformly | multiplying (N) segment constants gives (C^N) | use norm-one segment propagators and aggregate Bell budgets, (4.11) | Agent A mandated | pending | no theorem edit |
| PF linear area term is (O(r_N)) | total path length alone permits concentration at one bad vertex | retain exact weighted sum in (8.3); use typed (v_\mu/N) only for canonical grid | Agent C mandated | pending | no hidden (\sqrt N) |
| fixed bands imply Richardson closure | scalar signed combination can hit zero | impose (7.3) plus full membership test; show nonempty ball | Agent C mandated | pending | local/regularized scope retained |
| positive Hessian follows locally | radius may depend on (m) | uniform (D_B\mathsf H) plus (6.7)--(6.9) | Agent A/lead | pending | G1 coercivity only after A-IF |
| parameter derivatives depend only on path length | arbitrary family reparameterization makes (F_s) arbitrarily large | derivative operator norms use normalized endpoints; ruled budgets stated in (1.5) | Agent C mandated | pending | theorem wording must retain typed inputs |

## 14. Mandatory cross-audit of Agent A — pass 1

Agent A's complete first dossier was checked formula by formula against the ODE, Hessian, ruled-surface, and PF consumers above.

### 14.1 Formulas that pass

1. Agent A (1.6)--(1.8) agrees with (1.2)--(1.3): the base/lift comparison is exact and every fixed lift is paid only in matrix operator norm. No \(\sqrt m\), trace, or reverse HS-to-operator conversion was found.
2. Agent A (3.1) has the correct projector sign and norm one. Its constant-coordinate connection formula (4.6)--(4.8) has the correct horizontal/vertical types; differentiating \(AT+TA=V\) gives \(\dot T=-\mathcal L_A^{-1}(UT+TU)\).
3. Under Agent A's curvature convention, (5.2) gives \(3\|\mathcal A_XY\|_F^2\) when \(W=X,Z=Y\), and (5.5) follows from \(\mathcal A_ZW=-\mathcal A_WZ\). Section 5 here was repaired to use \(R(F_s,F_t)\) under that convention.
4. The square-root, inverse, polar, and Sylvester recurrences use spectral sums or singular-value margins, never eigenvector gaps. Their products are operator-by-Frobenius.
5. There is no derivative-order deficit if the moving-adjoint repair below is completed:

| B consumer | Highest A primitive required | Agent A supplies |
|---|---:|---:|
| \(D^{k_0}\) radial/connector PT | \(D^{k_0}P^{\mathcal H}\), Sylvester \(D^{k_0}\) | through \(k_0\) |
| \(D^{k_0}\Exp,D^{k_0}\Log\) | square root/polar/projector through \(k_0\) | through \(k_0\) |
| \(D^{k_0-1}\mathsf H\) | aligned lift through \(k_0\), connection through \(k_0-1\) | through \(k_0\) |
| \(k_0\)-th ruled/PT variation | \(\nabla^qR,\ q\le k_0-1\) | claimed through \(k_0\) |
| PF first variation | \(R\) only | supplied |

### 14.2 Objections requiring repair

| ID | Agent A claim | Attack | Required repair | Status |
|---|---|---|---|---|
| BA-1 | (5.7)--(5.10) differentiate \(\mathcal A^\dagger\) on moving horizontal/vertical spaces | “After enlarging \(a_j\)” is not an explicit proof. Domain, codomain, and both projectors vary with \(L\). | Define an ambient extension \(\widetilde{\mathcal A}_L(X,Y)=\mathcal A_L(P_L^HX,P_L^HY)\), then write \(\mathcal A_X^\dagger\xi=P_L^H\widetilde{\mathcal A}_{L,X}^{*}P_L^V\xi\). Differentiate it, including \(DP^H,DP^V,d\pi_L\), and basic-lift factors, and add the resulting majorant. | **OPEN — EXACT REPAIR DEMANDED** |
| BA-2 | (7.3) is a closed bound for every expression-tree recurrence | No induction proves the exponent \(16(k_0+2)^2\) or prefactor. Finite expression-tree depth proves fixed-order finiteness, not that display. | Prove (7.3) by induction over every tree, or retract it and retain only fully defined recurrences. B may consume the recurrence maximum \(C_A^*\), not the unsupported power. | **REJECTED AS WRITTEN; RECURRENCE ROUTE SURVIVES** |
| BA-3 | (4.13) types \(D_L^j\mathcal A_L\) as \(F^j\times H\times H\to F\) | Formula (4.14) uses fixed base-coordinate inputs \(U,V\), while the norm names moving horizontal inputs. This can omit derivatives of \(d\pi_L\) and the lift. | State one convention. Prefer a coefficient \(\mathbf A_L(U,V)\) on fixed symmetric directions, followed by explicit \(U=d\pi_LX,V=d\pi_LY\) and projector/lift derivatives for the ambient tensor. | **OPEN — TYPE REPAIR DEMANDED** |
| BA-4 | A primitives automatically survive fixed-total-length polygon composition without \(N\) | A segment endpoint derivative has a real \(C(1+\ell_j)\); independently varied endpoints give \(C(N+\mathsf L)\). | Use (4.13) for the stronger polygon map. PF instead uses coherent ruled-area cancellation and (8.3). | **REPAIRED IN B; \(N\) EXPLICIT** |
| BA-5 | \(C_A\) reaches Hessian/ruled/PF | Hessian and PF use the primitives, but higher ruled derivatives rely on BA-1 and the common closed constant relied on BA-2. | After BA-1/BA-3, use the recurrence-defined maximum in A-IF and no unsupported closed exponent. | **CONDITIONAL** |

### 14.3 Lead segment-count objection

The lead's objection to the former reading of (4.10) is sustained. For independently varied endpoints,

\[
K_q^{\rm pol}\le C_{{\rm ode},q}\{N+\mathsf L(\gamma)\},
\]

and the \(q\)-th derivative is (4.13). Fixed total length alone does not remove \(N\). For PF, adjacent endpoint terms cancel in the coherently endpoint-typed ruled deformation; isometric telescoping gives (8.3), whose only explicit segment count is \(2(N+1)r_N^2\). The linear term becomes uniform only after the typed speed condition \(\ell_j\le v_\mu/N\) is invoked. No \(C^N\), hidden \(\sqrt N\), or untyped speed remains.

### 14.4 Cross-audit verdict

At the time of the initial attack, Agent A's projector, connection, invariant primitives, O'Neill relative signs, and derivative-order coverage survived, while BA-1--BA-3 remained demanded. Section 14.7 records the subsequent repairs and pass-one acceptance of A-IF, still subject to hostile pass two.

### 14.5 Response to Agent A objections B-X1--B-X7

| Objection | Disposition in this repair |
|---|---|
| B-X1: Hessian observation derivative | **SUSTAINED AND REPAIRED.** Formula (6.3a) is \(-P_L^H D_MD_L\mathcal N[\dot M,E]\). |
| B-X2: derivative-order floor | **SUSTAINED AND REPAIRED.** Section 1 defines \(k_*=\max\{k_0,2\}\); A-IF and (9.1)--(9.7) use it only where consumed. |
| B-X3: endpoint connectors/gauge | **SUSTAINED AND REPAIRED.** Equations (8.1a), (8.3), and (8.7) compare \(C_N^{-1}\widehat PC_0-P\); no different fibres are subtracted. |
| B-X4: curvature convention | **SUSTAINED AND REPAIRED.** Section 5 adopts Agent A's convention and uses \(R(F_s,F_t)\). |
| B-X5: segment/direct-sum dependence | **SUSTAINED AND REPAIRED.** Equations (4.12a)--(4.13) state the \(\oplus,\infty\) input norm and polynomial \(N+\mathsf L\) dependence; PF uses the separate ruled-area formula. |
| B-X6: GD nonempty radius and ruled budgets | **SUSTAINED AND REPAIRED.** Equation (1.6) retains both \(\sqrt\alpha\) and \(\chi\), records the necessary \(\chi<\sqrt\beta\), and GD item 4 restricts the common constant to canonical ruled maps. |
| B-X7: common constant | **SUSTAINED AND REPAIRED.** The unsupported closed power/exponential was retracted. Equations (9.1)--(9.7) give the recurrence-defined maximum, subject to Agent A's BA-1--BA-3 repairs. |

### 14.6 Response to Agent C complete-chain objections

| Agent C objection | Repair |
|---|---|
| B-C2 varying initial fibre | Equations (4.9a)--(4.9b) add the complete initial-data sequence \(I_j\) and fixed-fibre radial connector trivializations. |
| B-C3 per-segment \(+1\) | Sustained: (4.12a)--(4.13) expose \(\oplus,\infty\) input and polynomial \(N+\mathsf L\); PF does not consume this stronger map. |
| B-C4 sign mismatch | Section 5 now uses Agent A's convention and \(R(F_s,F_t)\). |
| B-C5 higher ruled data | GD item 4 restricts the common theorem to the canonical nested-chord ruled map; (9.6) is the differentiated curvature recurrence with canonical endpoint factors. Arbitrary ruled families retain their \(\mathsf A_q\) as external typed inputs. |
| B-C6 missing G1 constraint | GD item 6 defines compact strongly geodesically convex \(\mathcal D_c\), population interior slack \(\delta_c\), and the internal \(q\)-observation radius; the paragraph after (1.6) proves existence, uniqueness, and nonemptiness. |
| B-C7 incompatible/nonempty GD | Compatibility is \(\max\{\chi,\chi^2\}<\beta\). Equations (1.5a)--(1.6) include lower/upper band, Exp, and polar slack. |
| B-C8 grid reach | Equations (7.5)--(7.6) display the exact \(\sqrt{N+1}r_N\) cost and complete-image Lipschitz closure against \(\delta_{\rm GD}\). |
| B-C9 Richardson is not band closure | Section 7 now says (7.3) is only an Exp-factor margin; nested-band membership and inner slack remain separate tests. |
| B-C10 unproved area producer | Equations (8.2a)--(8.2d) give the exact ruled quadrilateral/boundaries, endpoint-Jacobi Taylor vanishing, typed speed, and integrated area. Equation (8.6) now has its cellwise Taylor proof. |
| common constant incomplete | The closed display is retracted; (9.1)--(9.7) use all repaired A primitives, canonical ruled factors, and separate the \(N\)-dependent stronger polygon derivative. |

### 14.7 Verification of Agent A repairs

Agent A has now supplied the demanded repairs: fixed-symmetric coefficient (A 4.15), ambient projected tensor (A 4.16), explicit \(d\pi\) derivatives (A 4.17), moving adjoint \(P_H\widetilde{\mathcal A}^{*}P_V\) (A 4.18), and recurrence majorants through A (7.12). The unsupported closed envelope was withdrawn and \(k_*=\max\{k_0,2\}\) adopted.

These formulas resolve BA-1--BA-3 at the B interface. In particular, A (7.8)--(7.10) differentiates both \(d\pi_LP_L^H\) input slots and both moving outer projectors before taking the fixed-ambient Frobenius adjoint. Agent B therefore accepts A-IF for pass-one composition, subject to Agent C's mandated second hostile check of the repaired recurrences.

## 13. Exact remaining obligation before adjudication

The pass-one shared boundary is closed by Agent A's repairs and Sections 14.5--14.7. The remaining obligation is the mandated independent hostile pass over the repaired recurrences, constraint/GD reach, initial-fibre terms, and area producer. Agent B currently identifies no further unstated B-side lemma.

If hostile pass two rejects a recurrence or typed composition, the exact rejected row—not the entire theorem by rhetoric—must be marked `OPEN — EXACT LEMMA STATED`. If it passes, (9.7) is the recurrence-defined common fixed-margin consumer constant. This dossier makes no claim about any later margin regime.
