---
type: noncanonical-working-proof-dossier
title: BW-SIZE-FIXED-MARGIN — Agent A quotient calculus
status: final-self-check-complete-awaiting-frozen-hostile-pass-2-and-lead-adjudication
authority: noncanonical-agent-a-only
stage: 1-fixed-margin-only
---

# BW-SIZE-FIXED-MARGIN — Agent A quotient calculus

> **NONCANONICAL / FIRST PASS.** This dossier is Agent A's independent fixed-margin derivation. It has no canonical theorem status until the mandated cross-audit, hostile passes, and lead adjudication are complete. It does not address shrinking margins. The archived incomplete sketch was treated only as a list of conjectural targets; every identity below was rederived.

## 1. Domain, actions, and typed norms

Fix a matrix size (m), and let

\[
\pi:{\rm GL}(m)\longrightarrow {\rm SPD}(m),\qquad \pi(L)=LL^T.
\]

The right action (R_Q(L)=LQ), (Q\in O(m)), is free and Frobenius-isometric. Thus the Euclidean metric

\[
\langle H,K\rangle_F={\rm tr}(H^TK),\qquad \|H\|_F^2=\langle H,H\rangle_F,
\]

on the open total space gives a Riemannian submersion. At (L), with (A=LL^T),

\[
\mathcal V_L=\{L\Omega:\Omega^T=-\Omega\},\qquad
\mathcal H_L=\{H:L^TH=H^TL\}.
\tag{1.1}
\]

The derivative is

\[
d\pi_L(H)=HL^T+LH^T.
\tag{1.2}
\]

For (U\in T_A{\rm SPD}(m)={\rm Sym}(m)), put

\[
\mathcal L_A(S)=AS+SA,\qquad S_U=\mathcal L_A^{-1}U.
\tag{1.3}
\]

Then (S_U=S_U^T), and the horizontal lift at an arbitrary lift (L) of (A) is

\[
\mathfrak h_L(U)=S_UL,\qquad d\pi_L\mathfrak h_L(U)=U.
\tag{1.4}
\]

The quotient metric and tangent norm are

\[
g_A(U,V)=\langle S_UL,S_VL\rangle_F
=\frac12{\rm tr}(U\mathcal L_A^{-1}V),\qquad
\|U\|_{A,{\rm BW}}=\|\mathfrak h_L(U)\|_F.
\tag{1.5}
\]

They do not depend on the chosen lift. In an eigenbasis of (A={\rm diag}(a_1,\ldots,a_m)),

\[
\|U\|_{A,{\rm BW}}^2
=\frac12\sum_{i,j=1}^m\frac{U_{ij}^2}{a_i+a_j}.
\tag{1.6}
\]

Consequently, on the fixed band (\alpha I\preceq A\preceq\beta I),

\[
\boxed{
\frac1{4\beta}\|U\|_F^2
\le \|U\|_{A,{\rm BW}}^2
\le \frac1{4\alpha}\|U\|_F^2.}
\tag{1.7}
\]

This is the exact band comparison. In particular,

\[
\|U\|_F\le2\sqrt\beta\|U\|_{A,{\rm BW}},\qquad
\|S_U\|_F\le\frac{\sqrt\beta}{\alpha}\|U\|_{A,{\rm BW}}.
\tag{1.8}
\]

No estimate here uses (\|L\|_F). Whenever (\alpha I\preceq LL^T\preceq\beta I), only

\[
\|L\|_{\rm op}\le\sqrt\beta,\qquad
\|L^{-1}\|_{\rm op}\le\alpha^{-1/2}
\tag{1.9}
\]

is used.

## 2. Dimension-free majorant calculus

All matrix directions below carry Frobenius norm; all fixed matrix coefficients carry operator norm. The multiplication rules used at every occurrence are

\[
\|XYZ\|_F\le\|X\|_{\rm op}\|Y\|_F\|Z\|_{\rm op},
\qquad
\|XY\|_F\le\min\{\|X\|_{\rm op}\|Y\|_F,\|X\|_F\|Y\|_{\rm op}\}.
\tag{2.1}
\]

For products of two variable directions, (\|H_1H_2\|_F\le\|H_1\|_F\|H_2\|_{\rm op}\le\|H_1\|_F\|H_2\|_F). This is dimension-free and is not a base-lift Frobenius estimate.

For later explicit bookkeeping, if (F) and (G) have derivative majorants (f_j,g_j), define

\[
(f\circledast g)_k
=\sum_{\mathcal P\in\Pi_k}f_{|\mathcal P|}
\prod_{B\in\mathcal P}g_{|B|},
\qquad
(f\star g)_k=\sum_{S\subseteq[k]}f_{|S|}g_{k-|S|},
\tag{2.2}
\]

where (\Pi_k) is the finite set of set partitions of ([k]). These are respectively the operator-by-Frobenius Faà di Bruno and product majorants. Thus every constant below is an explicit finite sum, not a compactness constant.

At order zero the majorant conventions are

\[
(f\circledast g)_0=f_0,\qquad (f\star g)_0=f_0g_0.
\tag{2.2a}
\]

### 2.1 Sylvester inverse

For symmetric (G\succeq aI), define (\mathscr S_G(X)=GX+XG) on all matrices. In an eigenbasis of (G),

\[
(\mathscr S_G^{-1}Y)_{ij}=\frac{Y_{ij}}{g_i+g_j},\qquad
\|\mathscr S_G^{-1}\|_{F\to F}\le\frac1{2a}.
\tag{2.3}
\]

Let (\mathscr S_H(X)=HX+XH). Direct differentiation of

\(
\mathscr S_G\mathscr S_G^{-1}=I
\)

gives the exact permutation identity

\[
D^k(\mathscr S_{\bullet}^{-1})_G[H_1,\ldots,H_k]Y
=(-1)^k\sum_{\sigma\in S_k}
\mathscr S_G^{-1}\mathscr S_{H_{\sigma(1)}}\mathscr S_G^{-1}
\cdots
\mathscr S_{H_{\sigma(k)}}\mathscr S_G^{-1}Y.
\tag{2.4}
\]

Since (\|\mathscr S_H\|_{F\to F}\le2\|H\|_{\rm op}\le2\|H\|_F),

\[
\boxed{
\|D^k(\mathscr S_{\bullet}^{-1})_G\|_{F^k\times F\to F}
\le\frac{k!}{2a^{k+1}}.}
\tag{2.5}
\]

The same formula, restricted to symmetric matrices, applies to (\mathcal L_A^{-1}). Repeated eigenvalues never appear in a denominator except through sums (a_i+a_j\ge2a).

### 2.2 Inversion and square root

For (X\) invertible,

\[
D^k(X^{-1})[H_1,\ldots,H_k]
=(-1)^k\sum_{\sigma\in S_k}
X^{-1}H_{\sigma(1)}X^{-1}\cdots H_{\sigma(k)}X^{-1},
\tag{2.6}
\]

so if (\sigma_{\min}(X)\ge s),

\[
\|D^k(X^{-1})\|_{F^k\to F}\le k!s^{-(k+1)}.
\tag{2.7}
\]

Let (Q(A)=A^{1/2}). Differentiating (Q^2=A) invariantly gives

\[
Q\,DQ[A][H]+DQ[A][H]Q=H,
\tag{2.8}
\]

and, for (k\ge2),

\[
QD^kQ[H_{[k]}]+D^kQ[H_{[k]}]Q
=-\sum_{\varnothing\ne S\subsetneq[k]}
D^{|S|}Q[H_S]D^{k-|S|}Q[H_{S^c}].
\tag{2.9}
\]

If (\alpha I\preceq A\preceq\beta I), record the separate zero-order operator bound
(q_{\rm root}^{\rm op}=\sqrt\beta), and define the positive-order Frobenius
multilinear bounds

\[
q_1=(2\sqrt\alpha)^{-1},\qquad
q_k=(2\sqrt\alpha)^{-1}
\sum_{j=1}^{k-1}{k\choose j}q_jq_{k-j}\quad(k\ge2).
\tag{2.10}
\]

Equations (2.1), (2.8), and (2.9) prove

\[
\|D^kA^{1/2}\|_{F^k\to F}\le q_k.
\tag{2.11}
\]

Combining (2.6) with (2.2) gives explicit constants for (A^{-1/2}=(A^{1/2})^{-1}). This derivation is invariant and stays smooth at repeated positive eigenvalues.

### 2.3 Polar factor

For an invertible matrix (C),

\[
{\rm polar}(C)=C(C^TC)^{-1/2}.
\tag{2.12}
\]

Assume (\sigma_{\min}(C)\ge\chi) and (\|C\|_{\rm op}\le B). For (G(C)=C^TC),

\[
\|DG(C)[H]\|_F\le2B\|H\|_F,
\quad
\|D^2G(C)[H_1,H_2]\|_F\le2\|H_1\|_F\|H_2\|_F,
\quad D^jG=0\ (j\ge3).
\tag{2.13}
\]

Here (\chi^2I\preceq G\preceq B^2I). Apply (2.8)--(2.11), (2.6), and the explicit composition/product sums (2.2) to (2.12). This yields numbers

\[
p_k(\chi,B):=
\bigl(c\star[(\iota\circledast q)\circledast g]\bigr)_k<\infty,
\tag{2.14}
\]

where (c_0^{\rm op}=B,c_1=1,c_j=0 (j\ge2)), (g_1=2B,g_2=2,g_j=0 (j\ge3)), (q) is (2.10) with lower margin (\chi^2), and (\iota_j=j!\chi^{-(j+1)}) is the inverse majorant at (G^{1/2}\) (whose minimum singular value is (\chi)). Then

\[
\|D^k{\rm polar}(C)\|_{F^k\to F}\le p_k(\chi,B).
\tag{2.15}
\]

This formula uses no singular-vector gauge. The polar factor is unique for every invertible (C), including repeated singular values.

For banded lifts (L,M), (B=\beta) and

\[
\sigma_{\min}(M^TL)\ge\sigma_{\min}(M)\sigma_{\min}(L)\ge\alpha.
\tag{2.16}
\]

Thus a separate polar margin is redundant for pairs of lifts whose full singular bands are already checked, but retaining a declared (\chi\le\sigma_{\min}(M^TL)) is harmless and is necessary for more general generated polar inputs.

## 3. Horizontal projector and all fixed-order derivatives

Put (G=L^TL\). Orthogonality to every (L\Xi\), (\Xi^T=-\Xi\), shows that

\[
P_L^{\mathcal H}Z=Z-L\Omega_L(Z),
\qquad
\mathscr S_G\Omega_L(Z)=L^TZ-Z^TL.
\tag{3.1}
\]

The right side is skew and (\mathscr S_G\) preserves skew matrices, so (\Omega_L(Z)^T=-\Omega_L(Z)). Equation (3.1) is therefore the Frobenius-orthogonal horizontal projector; in particular

\[
\|P_L^{\mathcal H}\|_{F\to F}=1.
\tag{3.2}
\]

On (\alpha I\preceq LL^T\preceq\beta I), (G\) has the same spectral band and

\[
\|\Omega_L(Z)\|_F
\le\frac1{2\alpha}\|L^TZ-Z^TL\|_F
\le\frac{\sqrt\beta}{\alpha}\|Z\|_F.
\tag{3.3}
\]

For derivative bookkeeping,

\[
DG[L][H]=H^TL+L^TH,
\quad \|DG[L][H]\|_F\le2\sqrt\beta\|H\|_F,
\tag{3.4}
\]

\[
D^2G[L][H_1,H_2]=H_1^TH_2+H_2^TH_1,
\quad \|D^2G[L][H_1,H_2]\|_F\le2\|H_1\|_F\|H_2\|_F,
\tag{3.5}
\]

and (D^jG=0) for (j\ge3). With (K(L,Z)=L^TZ-Z^TL),

\[
\|K(L,Z)\|_F\le2\sqrt\beta\|Z\|_F,
\quad
\|D_LK[L,Z][H]\|_F\le2\|H\|_F\|Z\|_F,
\quad D_L^jK=0\ (j\ge2).
\tag{3.6}
\]

Since (\Omega_L(Z)=\mathscr S_{G(L)}^{-1}K(L,Z)), equations (2.2), (2.5), and (3.4)--(3.6) give an explicit finite constant (o_k(\alpha,\beta)) for every (k):

\[
\|D_L^k\Omega_L(Z)[H_1,\ldots,H_k]\|_F
\le o_k(\alpha,\beta)\|Z\|_F\prod_i\|H_i\|_F.
\tag{3.7}
\]

An entirely explicit definition is obtained by (2.2) with the Sylvester sequence (s_j=j!/(2\alpha^{j+1})), (g_1=2\sqrt\beta,g_2=2,g_j=0) otherwise, and (\kappa_0=2\sqrt\beta,\kappa_1=2,\kappa_j=0) otherwise:

\[
o=(s\circledast g)\star\kappa.
\tag{3.8}
\]

Finally (P_L^{\mathcal H}Z=Z-L\Omega_L(Z)) and the product rule give

\[
\boxed{
\|D_L^kP_L^{\mathcal H}[H_1,\ldots,H_k]Z\|_F
\le h_k(\alpha,\beta)\|Z\|_F\prod_i\|H_i\|_F,}
\tag{3.9}
\]

where (h_0=1) and one valid explicit choice for (k\ge1) is

\[
h_k=\sqrt\beta\,o_k+k\,o_{k-1}.
\tag{3.10}
\]

Mixed derivatives in (Z) vanish after the first (Z)-derivative because the projector is linear in (Z). Equations (3.8)--(3.10) prove every fixed order through (k_0), independently of (m).

## 4. Basic horizontal lift and quotient connection

The map

\[
\mathfrak h:(L,U)\mapsto \mathcal L_{LL^T}^{-1}(U)L
\tag{4.1}
\]

is linear in (U). Its derivatives are finite compositions of (L\mapsto LL^T), the Sylvester inverse (2.4), and multiplication by (L). The same explicit majorant algebra therefore gives

\[
\|D_L^k\mathfrak h_L(U)[H_1,\ldots,H_k]\|_F
\le b_k(\alpha,\beta)\|U\|_{A,{\rm BW}}\prod_i\|H_i\|_F,
\tag{4.2}
\]

where (b_k\) is obtained from (2.2), (2.5), the Gram derivatives

\[
D(LL^T)[H]=HL^T+LH^T,
\quad D^2(LL^T)[H_1,H_2]=H_1H_2^T+H_2H_1^T,
\tag{4.3}
\]

the input conversion (\|U\|_F\le2\sqrt\beta\|U\|_{A,{\rm BW}}), and the final product by (L). No derivative of a gauge or eigenvector is present.

Here is the exact quotient connection formula. Extend (U,V\in{\rm Sym}(m)) as constant-coordinate base fields near (A). Let

\[
S=\mathcal L_A^{-1}U,\qquad T=\mathcal L_A^{-1}V,
\tag{4.4}
\]

and let (\bar U=SL,\bar V=TL) be their basic horizontal lifts. Along (\delta L=\bar U), one has (\delta A=U), and differentiation of (AT+TA=V) gives

\[
\dot T=-\mathcal L_A^{-1}(UT+TU).
\tag{4.5}
\]

Therefore

\[
Z_{U,V}(L):=D\bar V[L]\bar U
=-\mathcal L_A^{-1}(UT+TU)L+TSL.
\tag{4.6}
\]

The Levi--Civita connection and O'Neill vertical tensor are exactly

\[
\boxed{(\nabla_UV)^H_L=P_L^{\mathcal H}Z_{U,V}(L),}
\qquad
\boxed{\mathcal A_{\bar U}\bar V=P_L^{\mathcal V}Z_{U,V}(L),}
\tag{4.7}
\]

with (P^{\mathcal V}=I-P^{\mathcal H}). For a nonconstant field (V(A)), add the horizontal term

\[
\mathfrak h_L(DV[A]U)
\tag{4.8}
\]

to (4.6) before applying (P^{\mathcal H}); its vertical projection is zero. Formula (4.7) has the correct types

\[
(\nabla_UV)^H_L\in\mathcal H_L,\qquad
\mathcal A_{\bar U}\bar V\in\mathcal V_L.
\]

It also shows tensoriality of (\mathcal A) and, by torsion-freeness,

\[
\mathcal A_{\bar U}\bar V=-\mathcal A_{\bar V}\bar U
=\frac12P_L^{\mathcal V}[\bar U,\bar V].
\tag{4.9}
\]

As a concrete zeroth-order estimate, using only (2.1), (1.8), and (4.5),

\[
\|\mathcal L_A^{-1}(UT+TU)\|_F
\le\frac1\alpha\|U\|_{\rm op}\|T\|_F
\le\frac{2\beta}{\alpha^2}\|U\|_{A,{\rm BW}}\|V\|_{A,{\rm BW}},
\tag{4.10}
\]

and

\[
\|TSL\|_F
\le\|T\|_F\|S\|_{\rm op}\|L\|_{\rm op}
\le\frac{\beta^{3/2}}{\alpha^2}
\|U\|_{A,{\rm BW}}\|V\|_{A,{\rm BW}}.
\tag{4.11}
\]

Thus, since (P^{\mathcal H},P^{\mathcal V}) are orthogonal projections,

\[
\|\mathcal A_{\bar U}\bar V\|_F,
\ \|(\nabla_UV)^H_L\|_F
\le a_0(\alpha,\beta)\|U\|_{A,{\rm BW}}\|V\|_{A,{\rm BW}},
\quad
a_0=\frac{3\beta^{3/2}}{\alpha^2}.
\tag{4.12}
\]

Differentiating (4.6)--(4.8) uses only the already explicit sequences (h_j,b_j), the Sylvester sequence (2.5), and finite product sums. For fixed symmetric coefficient directions \(U,V\), there are explicit finite numbers \(a_j^{\rm coef,L}(\alpha,\beta)\) and \(\gamma_j(\alpha,\beta)\) satisfying

\[
\|D_L^j\mathbf A_L\|_{F^j\times{\rm Sym}_F\times{\rm Sym}_F\to F}
\le a_j^{\rm coef,L},
\qquad
\|D_A^j\Gamma_A^{\rm BW}\|_{{\rm BW}^{j+2}\to{\rm BW}}\le\gamma_j.
\tag{4.13}
\]

Here \(D_A^j\Gamma\) is the derivative of the constant-coordinate Christoffel bilinear map, and every base tangent direction is measured in the BW norm at \(A\). Its conversion to Frobenius is exactly (1.7), and the output is converted by the horizontal isometry (1.5). Moving horizontal arguments are not included in this coefficient statement; they are introduced and differentiated explicitly in (4.16). A convenient explicit recursive definition is: expand (4.6) as the expression tree

\[
P^{\mathcal H}\bigl[-\mathcal L_A^{-1}{U(\mathcal L_A^{-1}V)+(\mathcal L_A^{-1}V)U\}L
+(\mathcal L_A^{-1}V)(\mathcal L_A^{-1}U)L\bigr],
\tag{4.14}
\]

then replace every composition and product node by (\circledast) and (\star) from (2.2), every (P^{\mathcal H}) derivative by (h_j), and every Sylvester-inverse derivative by (j!/(2\alpha^{j+1})). For derivatives in the base variable (A), choose the invariant principal lift (L=A^{1/2}) and apply the square-root sequence (2.10) to this expression tree; right-orthogonal equivariance makes the resulting base tensor independent of that computational gauge. This is a finite algorithm depending only on ((\alpha,\beta,j)), and (2.1) proves each replacement. No coordinate count occurs.

### 4.1 Fixed-symmetric coefficient versus ambient horizontal tensor

To remove an ambiguity in (4.13), first define the coefficient on fixed symmetric base directions:

\[
\mathbf A_L(U,V):=P_L^{\mathcal V}Z_{U,V}(L),
\qquad U,V\in{\rm Sym}(m),
\tag{4.15}
\]

where (Z_{U,V}) is exactly (4.6). Derivatives of (\mathbf A_L(U,V)) hold (U,V) fixed. This is the coefficient controlled by the expression (4.14).

For arbitrary ambient matrices (X,Y\in\mathbb R^{m\times m}), define the fully ambient extension

\[
\boxed{
\widetilde{\mathcal A}_L(X,Y)
:=\mathbf A_L\bigl(d\pi_LP_L^{\mathcal H}X,
d\pi_LP_L^{\mathcal H}Y\bigr).}
\tag{4.16}
\]

It has values in (\mathcal V_L). If (X,Y\in\mathcal H_L), (4.16) is exactly the O'Neill tensor (\mathcal A_XY). Thus all derivatives with “moving horizontal inputs” mean ordinary derivatives of the fixed ambient multilinear map (4.16); derivatives of both (P_L^{\mathcal H}) and (d\pi_L) are included.

The latter map has the explicit coefficient bounds

\[
\|d\pi_LX\|_F\le2\sqrt\beta\|X\|_F,
\qquad
\|D_L(d\pi_{\bullet}X)[H]\|_F
\le2\|H\|_F\|X\|_F,
\qquad D_L^j(d\pi_{\bullet}X)=0\ (j\ge2).
\tag{4.17}
\]

These follow from (d\pi_LX=XL^T+LX^T), paying (L) in operator norm. Equations (3.9), (4.14), and (4.17) therefore give derivatives of (4.16) with no omitted moving-slot term.

For fixed (X), let (\widetilde{\mathcal A}_{L,X}:Y\mapsto
\widetilde{\mathcal A}_L(X,Y)) be a linear operator on the ambient Frobenius matrix space, and let (*) denote its ordinary Frobenius adjoint. The actual O'Neill adjoint between the moving vertical and horizontal spaces is exactly

\[
\boxed{
\mathcal A_X^\dagger\xi
=P_L^{\mathcal H}\!\left[
\widetilde{\mathcal A}_{L,X}^{*}
\bigl(P_L^{\mathcal V}\xi\bigr)\right].}
\tag{4.18}
\]

For (X\in\mathcal H_L), (\xi\in\mathcal V_L), the outer projectors act as the correct domain/codomain restrictions; (4.18) satisfies (5.4). The first \(X\)-slot is already projected inside the definition (4.16), so no second \(P_L^{\mathcal H}\) is needed in the subscript of the adjoint. Taking the adjoint in the fixed ambient Frobenius space preserves every operator norm. Differentiating (4.18) uses the product rule and explicitly differentiates both outer projectors and the ambient coefficient (4.16), including its internal projected \(X\)-slot.

## 5. Exact O'Neill curvature formula and derivatives

This section fixes signs by convention. Define

\[
R(X,Y)Z=\nabla_Y\nabla_XZ-\nabla_X\nabla_YZ+\nabla_{[X,Y]}Z,
\tag{5.1}
\]

so that positive sectional curvature is (\langle R(X,Y)X,Y\rangle>0). For horizontal vectors (X,Y,Z,W\in\mathcal H_L), the total space is flat and O'Neill's identity is

\[
\boxed{
\langle R^{\rm BW}(X,Y)W,Z\rangle_F
=-2\langle\mathcal A_XY,\mathcal A_ZW\rangle_F
+\langle\mathcal A_YZ,\mathcal A_XW\rangle_F
-\langle\mathcal A_XZ,\mathcal A_YW\rangle_F.}
\tag{5.2}
\]

The calibration check (W=X,Z=Y), using (\mathcal A_YX=-\mathcal A_XY), gives

\[
\langle R^{\rm BW}(X,Y)X,Y\rangle_F=3\|\mathcal A_XY\|_F^2\ge0.
\tag{5.3}
\]

Let (\mathcal A_X^\dagger:\mathcal V_L\to\mathcal H_L) be the Frobenius adjoint,

\[
\langle\mathcal A_X^\dagger\xi,Z\rangle_F
=\langle\xi,\mathcal A_XZ\rangle_F.
\tag{5.4}
\]

Then the operator form equivalent to (5.2) is

\[
\boxed{
(R^{\rm BW}(X,Y)W)^H
=2\mathcal A_W^\dagger\mathcal A_XY
+\mathcal A_Y^\dagger\mathcal A_XW
-\mathcal A_X^\dagger\mathcal A_YW.}
\tag{5.5}
\]

This is the exact horizontal-lift type; every term lies in (\mathcal H_L). If the opposite curvature convention is used, both (5.2) and (5.5) change overall sign, while every bound is unchanged.

From (4.12) and (5.5),

\[
\|R^{\rm BW}(U,V)W\|_{A,{\rm BW}}
\le4a_0(\alpha,\beta)^2
\|U\|_{A,{\rm BW}}\|V\|_{A,{\rm BW}}\|W\|_{A,{\rm BW}}.
\tag{5.6}
\]

The ambient representatives and moving adjoint are exactly (4.16) and (4.18). Let \(\widetilde a_j\) and \(a_j^\dagger\) be their explicit derivative majorants (7.9)--(7.10), including both moving projectors, both \(d\pi_LP_L^{\mathcal H}\) input slots, and the fixed-ambient Frobenius adjoint. Differentiating (5.5) gives

\[
\rho_j(\alpha,\beta)
=4\sum_{q=0}^j{j\choose q}a_q^\dagger(\alpha,\beta)\widetilde a_{j-q}(\alpha,\beta),
\tag{5.7}
\]

with no implicit enlargement. Therefore

\[
\|D_L^j(R^{\rm BW})^H\|_{F^j\times F^3\to F}\le \rho_j(\alpha,\beta),
\qquad j\le K.
\tag{5.8}
\]

The direct-\(L\) bound (5.8) is converted to the base coefficient \(\rho^A\) by (7.10a), which composes the principal root, all three basic horizontal input lifts, and the horizontal output projection exactly once. Covariant derivatives are then obtained by one connection correction for the output and for each input slot. To make the finite bookkeeping explicit, let (\mathfrak T_0) be the expression (5.5), and define (\mathfrak T_{j+1}) from (\mathfrak T_j) by applying the product rule to its coefficient derivative, adding (+\Gamma) on the output slot, and adding (-\Gamma) on each of its (j+3) covariant input slots. Replace derivative, product, and connection nodes by the majorants (\rho^A_q,\star,\gamma_q). The resulting finite nonnegative number is denoted (\widehat\rho_{j+1}). A coarse scalar recursion dominating that exact expression-tree majorant is

\[
\widehat\rho_0=\rho^A_0,\qquad
\widehat\rho_{j+1}
=(j+5)2^{j+1}
\max_{q\le j+1}(1+\gamma_q+\rho^A_q)
\max_{q\le j}(1+\widehat\rho_q),
\tag{5.9}
\]

Then

\[
\|\nabla^jR^{\rm BW}\|_{{\rm BW}^{j+3}\to{\rm BW}}
\le\widehat\rho_j(\alpha,\beta),\qquad j\le K-1,
\tag{5.10}
\]

where the initial maximum for (j=0) is interpreted literally. This is the curvature/connection-variation input: it has no trace, Hilbert--Schmidt rank conversion, or multiplicity denominator.

## 6. Invariant alignment and horizontal chord formulas

For (A=LL^T), (B=MM^T), set

\[
Q={\rm polar}(M^TL),\qquad N=MQ.
\tag{6.1}
\]

Then (L^TN=N^TL\succ0), (H=N-L\in\mathcal H_L), and

\[
d_{\rm BW}(A,B)=\|H\|_F,
\quad
\Log_AB=d\pi_L(H),
\quad
\gamma_{A,B}(t)=\pi(L+tH).
\tag{6.2}
\]

If (L+H\) is invertible, then

\[
\Exp_A(d\pi_LH)=\pi(L+H).
\tag{6.3}
\]

The line remains horizontal because

\[
(L+tH)^TH=L^TH+tH^TH
\]

is symmetric. Equations (2.11), (2.15), and finite product rules give every fixed-order derivative of the aligned lift and chord on the checked margins. No eigenspace or singular-vector gauge is differentiated. In particular repeated positive eigenvalues of (A) or (B), and repeated positive singular values of (M^TL), cause no loss of smoothness.

## 7. Consolidated Agent A constant

The dependence can be exposed without pretending to have sharp shrinking-margin powers. Define

\[
\Lambda_A=4\bigl(1+\sqrt\beta+\alpha^{-1}+\chi^{-1}\bigr).
\tag{7.1}
\]

The consumer order must first be shifted backward through the dependency graph. The positive-Hessian radius needs one observation derivative of the Hessian even when the public requested order is (k_0=1). Define

\[
K:=\max\{k_0,2\}.
\tag{7.2}
\]

All square-root, polar, aligned-Log, projector, and horizontal-lift primitives are evaluated through order (K); connection primitives are evaluated through (K); curvature is evaluated through the largest order actually consumed, at most (K-1). This removes the first-pass order-floor defect.

Here is a fully specified majorant recurrence for the connection/curvature part that was previously described only by an expression-tree instruction. Set (u=2\sqrt\beta), which converts each unit BW tangent direction to Frobenius norm. Let

\[
f_j=\frac{j!}{2\alpha^{j+1}}u^j,
\qquad
t_j=\frac{j!}{2\alpha^{j+1}}u^{j+1},
\qquad 0\le j\le K,
\tag{7.3}
\]

where (f_j) is the (j)-th base derivative majorant of (A\mapsto\mathcal L_A^{-1}) and (t_j) is that map applied to one unit-BW tangent slot. Let

\[
l_0=\sqrt\beta,\qquad l_j=q_j u^j\quad(1\le j\le K)
\tag{7.4}
\]

be the principal-root sequence after converting base directions. Compose the lift-projector sequence by

\[
p=h\circledast l,
\tag{7.5}
\]

using the set-partition operation (2.2). Define finite-subset convolution (\star) exactly as in (2.2), and put

\[
w_j=2u\,t_j,
\qquad
z=(f\star w\star l)+(t\star t\star l),
\qquad
\gamma=p\star z,
\qquad
b=t\star l.
\tag{7.6}
\]

The two summands in (z) are respectively the majorants of

\[
-\mathcal L_A^{-1}(UT+TU)L,
\qquad TSL,
\]

in (4.6), for unit-BW (U,V). For the ambient tensor, one must differentiate (4.15) directly as a function of \(L\); it is equivariant but is not literally a function of \(A=LL^T\) alone. Define the direct-lift vertical-projector sequence

\[
v^L_0=1,\qquad v^L_j=h_j\quad(j\ge1),
\tag{7.7}
\]

and let

\[
\bar g_1=2\sqrt\beta,\qquad \bar g_2=2,\qquad \bar g_j=0\quad(j\ge3)
\]

be the Frobenius derivative sequence of \(L\mapsto LL^T\), and let

\[
\bar s=s\circledast\bar g,\qquad
\ell^L_0=\sqrt\beta,\quad \ell^L_1=1,\quad \ell^L_j=0\ (j\ge2).
\]

For fixed unit-Frobenius symmetric \(U,V\), the two occurrences
\(\mathcal L_{LL^T}^{-1}U,\mathcal L_{LL^T}^{-1}V\) both have sequence
\(\bar t=\bar s\). Therefore the direct-\(L\) expression (4.14) has

\[
\bar z=
\{\bar s\star(2\bar t)\star\ell^L\}
+\{\bar t\star\bar t\star\ell^L\},
\qquad
a^{\rm coef,L}=v^L\star\bar z.
\tag{7.8}
\]

This recurrence differentiates the actual lift \(L\), its Gram matrix, the Sylvester inverse, and the vertical projector; it does not introduce a principal-root gauge. Next let

\[
\delta_0=2\sqrt\beta,\qquad \delta_1=2,\qquad \delta_j=0\quad(j\ge2)
\]

be the (d\pi_L) sequence from (4.17), and put

\[
d=\delta\star h,
\tag{7.9}
\]

Here \(d\) is a Frobenius-output majorant for the complete map
\(d\pi_LP_L^{\mathcal H}\). Since \(a^{\rm coef,L}\) is typed on fixed
Frobenius symmetric inputs, no intermediate BW conversion is needed.
The ambient-tensor, moving-adjoint, and curvature majorants are

\[
\widetilde a=a^{\rm coef,L}\star d\star d,
\qquad
a^\dagger=h\star\widetilde a\star v^L,
\qquad
\rho=4(a^\dagger\star\widetilde a).
\tag{7.10}
\]

Thus (\widetilde a) differentiates both projected/differentiated input slots, while (a^\dagger) additionally differentiates the moving domain and codomain projectors in (4.18). Taking a Frobenius adjoint contributes no additional norm factor. The factor (4) is the sum of the absolute coefficients in the exact curvature operator (5.5).

To convert the direct-\(L\) Frobenius coefficient \(\rho\) to a base coefficient, use the principal root only as an invariant computational section after the arbitrary-gauge ambient calculation is complete. The sequence \(b=t\star l\) in (7.6) bounds the basic horizontal lift \(A\mapsto\mathfrak h_{A^{1/2}}(U)\). Define

\[
\rho^A
=p\star(\rho\circledast l)\star b\star b\star b.
\tag{7.10a}
\]

Here \(\rho\circledast l\) composes the direct-\(L\) curvature coefficient with \(L=A^{1/2}\); the three \(b\) factors differentiate all three basic horizontal input lifts; and \(p=h\circledast l\) supplies the moving horizontal output projection. Right-orthogonal equivariance makes this computational section independent of gauge at the tensor level. Thus no root factor is missing and no Gram map is counted twice. Finally define covariant-curvature majorants recursively by

\[
\widehat\rho_0=\rho^A_0,
\qquad
\widehat\rho_{j+1}
=(j+5)2^{j+1}
\max_{q\le j+1}(1+\gamma_q+\rho^A_q)
\max_{q\le j}(1+\widehat\rho_q),
\quad 0\le j<K-1.
\tag{7.11}
\]

Every sequence in (7.3)--(7.11) is a finite list computed from the explicit primitive sequences (2.5), (2.10), (3.8)--(3.10). The polar list (p_j(\chi,\beta)) in (2.14) is kept separately; to avoid overloading notation, denote it below by (p_j^{\rm pol}).

A single explicit finite number for the Agent A primitives is therefore

\[
C_A(\alpha,\beta,\chi,k_0)
:=1+\max_{0\le j\le K}
\{q_j,p_j^{\rm pol},h_j,l_j,f_j,t_j,p_j,z_j,\gamma_j,b_j,
v_j^L,\bar s_j,\bar t_j,\bar z_j,a_j^{\rm coef,L},
d_j,\widetilde a_j,a_j^\dagger,\rho_j,\rho_j^A\}
+\max_{0\le j\le K-1}\widehat\rho_j.
\tag{7.12}
\]

Every entry is an explicitly computable finite sum of factorials and powers of (\alpha^{-1},\sqrt\beta,\chi^{-1}). The earlier first-pass closed domination by ( (k_0+2)^{k_0+2}(k_0+2)!\Lambda_A^{16(k_0+2)^2}) is **WITHDRAWN AS UNVERIFIED**: its exponent was asserted without counting the depth and arity of every expression tree. Equation (7.12), not that withdrawn envelope, is the proposed explicit Agent A constant for hostile review.

**Symbol/order closure for (7.12).** The lists \(q,p^{\rm pol},h\) are defined in (2.10), (2.14), and (3.10); \(l,f,t,p,z,\gamma,b\) are defined in (7.3)--(7.6); \(v^L,\bar s,\bar t,\bar z,a^{\rm coef,L}\) are defined by the wholly direct-\(L\) recurrence (7.7)--(7.8); and \(d,\widetilde a,a^\dagger,\rho,\rho^A,\widehat\rho\) are defined in (7.9)--(7.11). Every one of these lists is truncated to \(0\le j\le K\), except \(\widehat\rho\), which is required and defined only for \(0\le j\le K-1\). The direct-\(L\) block uses \(L\mapsto LL^T\), direct projector derivatives \(h_j\), and \(d\pi_L\); it contains no principal-root section and no second Gram composition. The principal-root sequences \(l,p,b\) enter only after that direct calculation, to type the base-\(A\) connection coefficient and to convert the already gauge-equivariant ambient curvature tensor to base covariant form via (7.10a).

This is a fixed-margin bound only. The path-length parameter (r_0) does not enter the algebraic quotient, connection, or curvature primitives; it first enters the variational ODE/Gronwall composition owned by Agent B. Thus the lead may take, at the shared boundary,

\[
C_A\le C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)
\]

after composing with Agent B's typed ODE constants. No claim about shrinking-margin sharpness is made.

## 8. Edge-case and sign/type audit

1. **Scalar (m=1).** There is no vertical space, (P^{\mathcal H}=I), (\mathcal A=0), and (R=0). Formula (1.6) becomes (\|u\|_a^2=u^2/(4a)), the Euclidean positive-root metric.
2. **Commuting diagonal matrices.** All aligned lifts remain in the diagonal horizontal flat; (\mathcal A=0) on diagonal directions, hence (5.5) gives zero curvature on that flat.
3. **Repeated positive eigenvalues.** The only inverses are (a_i+a_j\), square-root Sylvester sums, and the invariant polar inverse square root. No difference (a_i-a_j\) occurs.
4. **Identity base.** At (L=I), (P_I^{\mathcal H}Z=(Z+Z^T)/2), obtained from (2\Omega=Z-Z^T). This fixes the projector sign.
5. **Sectional sign.** Under convention (5.1), (5.3) is (+3\|\mathcal A_XY\|^2). Switching curvature convention changes the overall sign, not individual relative coefficients.
6. **Gauge equivariance.** (P_{LQ}^{\mathcal H}(ZQ)=P_L^{\mathcal H}(Z)Q), (\mathfrak h_{LQ}(U)=\mathfrak h_L(U)Q), and every Frobenius bound is right-orthogonally invariant.
7. **No base-lift Frobenius norm.** Every fixed lift is paid by (\|L\|_{\rm op}\le\sqrt\beta); Frobenius norms are used only for variable directions or horizontal tangent lifts.

## 9. Claim-ledger subset

| ID | Exact claim | Domain and margins | Input/output norms | Producer | Direct consumer | Dimension dependence | Objection | Resolution | First-pass status |
|---|---|---|---|---|---|---|---|---|---|
| A-Q1 | (\pi:{\rm GL}(m)/O(m)\to{\rm SPD}(m)), (1.1)--(1.5), is a Riemannian submersion and (\mathfrak h_L(U)=\mathcal L_A^{-1}(U)L) | Full rank; (\alpha I\preceq A\preceq\beta I) for bounds | lift (F); base BW | direct quotient derivation | all BW consumers | none | invalid horizontal/vertical identification | orthogonality and (d\pi) checked explicitly | **DERIVED — AWAITING AUDIT** |
| A-Q2 | Exact norm identity (1.6) and band equivalence (1.7) | fixed spectral band | (F\leftrightarrow{\rm BW}) | eigenbasis of invariant Sylvester equation | all norm conversions | none | archived seed used a looser formula | replaced by exact constants (1/(4\beta),1/(4\alpha)) | **DERIVED — AWAITING AUDIT** |
| A-SYL | Sylvester inverse derivative formula (2.4) and bound (2.5) | lower margin (a>0) | (F^k\times F\to F) | differentiated inverse operator identity | projector, lift, connection | none | multiplicity/eigengap | denominators are spectral sums only | **DERIVED — AWAITING AUDIT** |
| A-SQ | invariant square-root recursion (2.8)--(2.11) | (\alpha I\preceq A\preceq\beta I) | (F^k\to F) | differentiated (Q^2=A) | principal lifts, alignment | none | differentiating eigenvectors | no eigenvectors chosen | **DERIVED — AWAITING AUDIT** |
| A-POL | polar derivative bound (2.12)--(2.15) | (\sigma_{\min}C\ge\chi,\ \|C\|_{op}\le B) | (F^k\to F) | Gram, inverse square root, product | alignment/Log/chords | none | repeated singular values/nonunique gauge | invariant unique polar on invertible cone | **DERIVED — AWAITING AUDIT** |
| A-PROJ | exact projector (3.1), (\|P_H\|=1), derivatives (3.9) through (k_0) | lift singular band ([\sqrt\alpha,\sqrt\beta]) | (F^k\times F\to F) | Sylvester plus explicit Gram/K derivatives | quotient connection, PT | none | hidden (\|L\|_F) | every (L) paid in operator norm | **DERIVED — AWAITING AUDIT** |
| A-CONN | exact constant-coordinate connection formula (4.6)--(4.8), derivative bounds (4.13) | base fixed band | (\mathrm{BW}^{j+2}\to\mathrm{BW}) or horizontal-lift (F) | horizontal lift plus Euclidean derivative/projector | connection variation, PT | none | wrong sign/type; extension dependence | sign fixed by differentiating (AT+TA=V); vertical part tensorial | **DERIVED — AWAITING AUDIT** |
| A-ON | exact O'Neill 4-tensor/operator formulas (5.2),(5.5) | quotient regular domain | (H^3\to H), Frobenius/BW | flat total-space O'Neill identity | curvature/holonomy/connection variation | none | relative signs | convention stated and sectional (+3\|A\|^2) calibration checked | **DERIVED — AWAITING AUDIT** |
| A-CURV | (D^jR) and (\nabla^jR) bounds (5.7)--(5.10) | fixed spectral band | (F^j\times F^3\to F), restricted to horizontal/BW slots | ambient extension (4.16), moving adjoint (4.18), projectors, connection | Agent B variational ODE | none | moving adjoint/subspace derivative | both \(P_H/P_V\), both \(d\pi P_H\) input slots, and fixed-ambient adjoint differentiated in (7.9)--(7.10) | **REPAIRED — AWAITING HOSTILE PASS 2** |
| A-ALIGN | unique invariant alignment and horizontal chord (6.1)--(6.3) | full rank; checked polar and Exp margins | aligned lift (F), base BW | polar calculus | Log/Exp/connector primitives | none | non-smooth gauge at multiplicity | no singular-vector gauge | **DERIVED — AWAITING AUDIT** |
| A-COMMON | \(C_A\) from (7.12), with primitive order \(K=\max\{k_0,2\}\), controls all Agent A primitives | fixed (\alpha,\beta,\chi,k_0) | displayed multilinear norms | explicit finite recurrence | lead's \(C_{\rm BW}\) | none | unsupported closed envelope and shifted consumer order | old envelope withdrawn; fully specified recurrence maximum retained | **REPAIRED — AWAITING HOSTILE PASS 2** |

## 10. Irreducible gaps and handoff boundary

There is no remaining algebraic gap in the first-pass Agent A subset, but it is not yet independently verified. In particular, the following are outside this dossier and must not be inferred from it:

1. parameter derivatives of parallel transport and their Gronwall/path-length constants;
2. accumulation over finitely many polygonal segments, including whether total length or segment count is paid;
3. observation Hessian coercivity and a uniform normal radius on the complete generated pair set;
4. Richardson/blend/ruled-surface closure and derivative composition;
5. confirmation that Agent B uses the same curvature convention or changes all curvature signs consistently;
6. confirmation that the proposed lead-level common constant actually reaches every G1/PF consumer.

Those are the mandated Agent B/lead interfaces. Until the two hostile passes close them, the only honest status of BW-SIZE-FIXED-MARGIN remains **OPEN — EXACT LEMMA STATED**.

## 11. Mandatory cross-audit of Agent B — pass 1

This section audits the first complete Agent B dossier, `BW-SIZE-FIXED-MARGIN — Agent B transport and generated geometry.md`, against the independently derived quotient formulas above. No statement here changes canonical status.

### 11.1 Findings

#### B-X1 — `A-IF` has an unresolved derivative-order floor

Agent B assumes connection derivatives through (k_0) and curvature derivatives through (k_0-1). That shift is correct for a (k_0)-th parameter derivative of the first connection-variation formula: the first variation uses (R), and the (k_0)-th variation uses at most (\nabla^{k_0-1}R). Likewise (D^q\mathsf H) consumes (D^{q+1}\Log), so (D^{k_0-1}\mathsf H) is compatible with (D^{k_0}\Log).

However, the positive-Hessian radius consumes the first observation derivative (D_B\mathsf H), hence a second derivative of the aligned Log. Agent B allows (k_0\ge1), but when (k_0=1), its displayed package (6.5) bounds only (D^0\mathsf H), not (D_B\mathsf H). The repair is to set

\[
K=\max\{k_0,2\}
\tag{11.1}
\]

for the primitive square-root/polar/Log calculus, or explicitly assume (k_0\ge2). After this repair, the connection/curvature order shift itself is accepted.

**Verdict:** **MATERIAL REPAIR REQUIRED**, local and repairable.

#### B-X2 — Hessian formula (6.3) is correct in the base variable, but its observation derivative is misstated

Fix (B=MM^T), and let

\[
\bar Y(L)=\mathcal N(L,M)-L,
\qquad \mathcal N(L,M)=M\operatorname{polar}(M^TL).
\]

This is the basic horizontal lift of (A\mapsto\Log_AB). For (E=\bar U\),

\[
-P_L^{\mathcal H}D_L\bar Y[E]
=P_L^{\mathcal H}\{E-D_L\mathcal N(L,M)[E]\},
\]

so Agent B's boxed formula (6.3) is exact and agrees with (4.7).

The following sentence in Agent B is not exact: observation differentiation does not “replace the last term” by

\[
-P_L^{\mathcal H}D_M\mathcal N[\dot M].
\]

That is the observation derivative of the aligned endpoint (\mathcal N), not the observation derivative of the Hessian operator. The latter is the mixed derivative

\[
\boxed{
D_B\overline{\mathsf H(A,B)U}[V]
=-P_L^{\mathcal H}
D_M D_L\mathcal N(L,M)[\dot M,E],}
\tag{11.2}
\]

with (\dot M=D(B^{1/2})[V]) in the principal-root computational section (or any other differentiated lift, with gauge invariance checked). Higher mixed base/observation derivatives similarly add one (L)-derivative to the polar-alignment order. Formula (11.2) is bounded by Agent A's invariant calculus, but it must replace the stated sentence before (6.7) is a proof.

**Verdict:** boxed (6.3) **ACCEPTED**; observation-derivative claim **REJECTED AS WRITTEN / REPAIR (11.2)**.

#### B-X3 — PT ODE (4.3) has the correct sign and type

Differentiating (L^TH=H^TL) and using (\dot H=L\Omega), (\Omega^T=-\Omega), gives

\[
(L^TL)\Omega+\Omega(L^TL)=H^T\dot L-\dot L^TH.
\]

Thus Agent B's (4.2)--(4.3) agrees with the quotient projector sign in (3.1). The coefficient bound can even be written with the displayed (\sqrt\beta/\alpha), and (4.5) correctly proves isometry because (H^TL) is symmetric while (\Omega) is skew.

Two typing qualifications remain. First, a derivative of PT as a map between parameter-varying horizontal spaces is not defined until domain and codomain are trivialized (for example by principal lifts plus horizontal-lift maps, or by radial endpoint connectors). Second, if the initial lifted vector depends on the parameter under that trivialization, the differentiated ODE has initial-data terms in addition to Agent B's forcing sum (4.6). These terms are bounded by the lift/projector calculus but are absent from the exact Bell display (4.8).

**Verdict:** ODE sign/isometry **ACCEPTED**; parameter-map formula **CONDITIONAL ON EXPLICIT ENDPOINT TRIVIALIZATION AND INITIAL TERMS**.

#### B-X4 — the per-segment (+1) invalidates the claimed (N)-free polygon derivative bound

Agent B proves only

\[
K_{q,j}\le C_q(1+\ell_j).
\]

Summation over (N) segments gives

\[
K_q^{\rm pol}=\sum_{j=0}^{N-1}K_{q,j}
\le C_q\{N+\mathsf L(\gamma)\},
\tag{11.3}
\]

not (C_q(1+r_0)). Total path length controls the sum of (\ell_j), but it does not control the sum of the per-segment constants. The (+1) is genuinely needed for arbitrary normalized endpoint variations: even at a zero-length segment, varying one endpoint changes (\dot L_t) to first order.

Isometric outer factors remove a multiplicative (C^N); they do not remove the additive (N) in the differentiated product. An (N)-free theorem requires one of the following additional statements:

1. prove a sharper segment budget (K_{q,j}\le C_q\ell_j\) for the particular global path parameter (false for arbitrary independent endpoint perturbations);
2. type polygon endpoint directions in an (\ell^1) direct-sum norm and retain that norm explicitly;
3. retain explicit (N), (\sqrt N), or weighted-vertex dependence appropriate to the chosen (\ell^1/\ell^2) parameter norm; or
4. avoid generic differentiated-product PT and use the ruled-cell curvature/area telescoping separately for PF.

Option 4 can still support the specific PF estimate, but it does not prove Agent B's general statement that all polygonal PT parameter derivatives are bounded by a five-input constant independent of segment count.

**Verdict:** **DISPROVED AS STATED** by the algebra (11.3); theorem must retain segment/direct-sum dependence or narrow the consumer.

#### B-X5 — connector and gauge typing is incomplete

The expressions

\[
\|P_{\widehat{\rm pol}}-P_{\rm pol}\|_{\rm op}
\]

in (8.3) and (8.7) are ill-typed when the estimated and true polygons have different initial or final vertices. Let (C_0:T_{A_0}\to T_{\widehat A_0}) and (C_N:T_{A_N}\to T_{\widehat A_N}) be the explicitly chosen radial endpoint connectors. A typed comparison is, for example,

\[
\boxed{
\|P_{\widehat{\rm pol}}C_0-C_NP_{\rm pol}\|_{{\rm op}:T_{A_0}\to T_{\widehat A_N}},}
\tag{11.4}
\]

or the conjugate equivalent after moving everything to one fibre. If quotient lifts are used, the recursive lift alignment for each polygonal chord and the one removable common right-orthogonal gauge at the anchor must also be stated. Pointwise polar alignment is not itself parallel transport.

Agent B says endpoint connectors are included, but does not define (11.4) before subtracting the maps. This omission also affects the definition of parameter derivatives in (4.8).

**Verdict:** **MATERIAL TYPE REPAIR REQUIRED**; the norm bound may survive after the maps are rewritten as (11.4).

#### B-X6 — Agent A and Agent B use opposite curvature conventions

Agent A fixed

\[
R_A(X,Y)Z=\nabla_Y\nabla_XZ-\nabla_X\nabla_YZ+\nabla_{[X,Y]}Z.
\]

Agent B writes

\[
\nabla_t\nabla_sW-\nabla_s\nabla_tW=R_B(F_t,F_s)W,
\]

which is the opposite convention: (R_B=-R_A). Therefore, if the lead retains Agent A's convention, Agent B's (5.1) must read

\[
\nabla_sW(s,1)
=P_{0\to1}\nabla_sw(s)
-\int_0^1P_{t\to1}R_A(F_t,F_s)W(s,t)\,dt,
\tag{11.5}
\]

equivalently with (+R_A(F_s,F_t)). All norm/area estimates are unchanged. Agent B notes that an overall sign can change, but the shared interface must select one convention before the formula is called exact.

**Verdict:** **SIGN REPAIR REQUIRED; NORM CONSEQUENCES ACCEPTED**.

#### B-X7 — the proposed common constant (9.1) is not yet an explicit five-input producer

There are four defects.

1. The exponent display is malformed: `[10\Lambda C_A^*]^{,8(k_0+1)^2}` and the analogous second exponent must be `[10\Lambda C_A^*]^{8(k_0+1)^2}` and `[10\Lambda C_A^*]^{2(k_0+1)}`.
2. (C_A^*=1+\max_{q\le k_0}(C_{\Gamma,q}+C_{R,q})) refers to (C_{R,k_0}), although `A-IF` supplies curvature only through (k_0-1). The maxima must be separated.
3. `GD` item 4 declares higher ruled-family derivative integrals as “actual budgets” but places no upper bound on them as a function of (\alpha,\beta,\chi,r_0,k_0). Therefore a constant depending only on the five campaign inputs cannot dominate arbitrary families admitted by the literal `GD`. Either these budgets become additional visible inputs or the domain is restricted to the canonical ruled maps and their budgets are proved from the invariant composition constants.
4. By B-X4, generic polygonal PT parameter derivatives also carry (N) or a typed direct-sum endpoint norm. Formula (9.1) contains neither.

The large exponential may be a valid coarse envelope after these repairs, but Section 9 currently asserts rather than verifies that its exponents dominate every partition/product depth.

**Verdict:** **REJECTED AS THE CURRENT COMMON CONSTANT; REPAIRABLE ONLY AFTER B-X1, B-X4, AND THE RULED-BUDGET RESTRICTION**.

### 11.2 Cross-audit objection table

| Claim | Attack | Repair or counterexample | Independent checker requested | Pass-1 verdict | Canonical consequence |
|---|---|---|---|---|---|
| `A-IF` order | positive Hessian uses (D_B\mathsf H), absent when (k_0=1) | use (K=\max\{k_0,2\}) or assume (k_0\ge2) | lead / Agent B | material repair | no normal-radius claim before repair |
| B (6.3) | possible missing quotient connection term | base formula exactly equals (-P_HD_L(\mathcal N-L)[E]) | lead | accepted | may be used after convention match |
| observation derivative after B (6.3) | uses (D_M\mathcal N) instead of (D_MD_L\mathcal N) | replace by (11.2) and shift derivative order | Agent B | rejected as written | Hessian derivative/normal radius pending repair |
| B (4.3)--(4.5) | PT Sylvester sign/type and isometry | direct differentiation agrees with Agent A projector sign | lead | accepted | PT base ODE survives |
| B (4.8) | PT maps have varying endpoint fibres and initial lift | choose explicit trivializations/connectors and add initial terms | Agent B | conditional | endpoint derivative bound not yet exact |
| polygon derivative accumulation | (K_{q,j}\le C(1+\ell_j)) sums to (C(N+\mathsf L)) | retain (N)/direct-sum norm or restrict to ruled-area PF route | Agent B / Agent C | disproved as stated | no (N)-free generic polygon derivative theorem |
| B (8.3),(8.7) | subtract transports with different domain/codomain | rewrite as (11.4); state recursive gauge alignment | Agent B | ill-typed pending repair | PF comparison not yet exact |
| B (5.1) | curvature convention opposite Agent A | use (11.5) or globally flip Agent A convention | lead | sign repair | norm bounds unchanged |
| B (9.1) | malformed exponents, wrong curvature max, unbounded ruled budgets, omitted polygon input | correct display and include/restrict all budgets | Agent B / lead | rejected currently | common (C_{\rm BW}) not yet produced |

### 11.3 Cross-audit conclusion

Agent B's base PT ODE, isometry, exact tangent norm conversion, and boxed base-Hessian formula survive this pass. The full B chain does not yet close because the generic polygon derivative claim incorrectly removes an additive segment contribution, endpoint comparisons are not fully typed, the observation derivative of the Hessian is one mixed derivative short, and the proposed common constant omits declared ruled/polygon budgets. These are proof gaps, not counterexamples to the fixed-margin theorem class. Stage 1 therefore remains **OPEN — EXACT LEMMA STATED** pending repair and hostile review.

## 12. Repair response to B/lead/C pass-1 objections

The following repairs were made after Agent B §14, the lead ledger, and Agent C pass 1.

| Objection | Repair in this dossier | Result |
|---|---|---|
| BA-1 / C moving \(H/V\) domains and adjoint | Defined fixed-ambient \(\widetilde{\mathcal A}\) in (4.16), the restricted adjoint as \(P_H\widetilde{\mathcal A}^*P_V\) in (4.18), and derivative sequences \(\widetilde a,a^\dagger\) in (7.9)--(7.10) including both projectors and both input slots | **REPAIRED; awaiting hostile pass 2** |
| BA-3 fixed \(U,V\) versus moving horizontal inputs | Retyped (4.13) as the coefficient \(\mathbf A_L(U,V)\) on fixed symmetric directions; moving ambient inputs are composed explicitly with \(d\pi_LP_H\) in (4.16), whose derivatives are (4.17) | **REPAIRED; awaiting hostile pass 2** |
| BA-2 / lead / C unsupported closed (7.3) | Withdrew the asserted factorial/power envelope. Replaced it by the fully specified finite recurrence (7.3)--(7.12) | **REPAIRED BY RETRACTION AND RECURRENCE** |
| backward derivative order | Adopted \(K=\max\{k_0,2\}\); curvature is supplied through the actually consumed order \(K-1\) | **REPAIRED** |
| curvature convention mismatch | Agent B reports that its ruled formula now uses Agent A's convention and \(R(F_s,F_t)\); the norm estimates were invariant throughout | **SYNCHRONIZED, subject to lead check** |
| Agent C preliminary attack on \(a_0=3\beta^{3/2}/\alpha^2\) | Agent C withdrew it: (4.10) is the bound before the final multiplication by \(L\), which contributes \(\sqrt\beta\), so the two terms sum to \(3\beta^{3/2}/\alpha^2\) for every \(\beta>0\) | **OBJECTION WITHDRAWN; (4.12) RETAINED** |
| Agent C pass-2 gauge/double-count objection | Replaced the mixed principal/base-plus-Gram recurrence by the wholly intrinsic direct-\(L\) recurrence \(\bar g,\bar s,\bar z,a^{\rm coef,L}\) in (7.8), then composed only the actual \(d\pi_LP_H\) slots in (7.9)--(7.10); corrected (4.18) to apply the adjoint to \(P_V\xi\) | **REPAIRED; RERUN REQUESTED** |

The repaired Agent A interface is therefore recurrence-explicit and correctly typed on a fixed ambient Frobenius space before restriction to quotient horizontal/vertical spaces. It still has no canonical status until Agent C's second hostile pass and lead verification.

### 12.1 Hostile-objection closure self-check

The final self-check confirms:

1. (4.18) is parenthesized as the ambient adjoint applied to \(P_L^{\mathcal V}\xi\), followed by \(P_L^{\mathcal H}\); there is no comma or ambiguous multiplication.
2. The ambient curvature recurrence (7.7)--(7.10) is entirely direct in an arbitrary lift \(L\). It does not differentiate \(Q=A^{-1/2}L\), does not choose a principal section, and does not compose a base-\(A\) coefficient with the Gram map twice.
3. Only after the arbitrary-gauge ambient coefficient is complete, (7.10a) uses the principal root as an invariant computational section and explicitly composes the root sequence \(l\), three basic-lift sequences \(b\), and output-projector sequence \(p\). The same principal-root sequences give the base-\(A\) connection coefficient \(\gamma\).
4. Every symbol entering \(C_A\) in (7.12) is defined and capped at \(K=\max\{k_0,2\}\); covariant curvature is capped at the consumed order \(K-1\).

**Exact Agent A status:** quotient identities, projector/connection signs, O'Neill relative signs, invariant primitive bounds, and the repaired ambient derivative recurrence are **DERIVED AND INTERNALLY CLOSED; AWAITING FINAL EXTERNAL HOSTILE-PASS-2 CONFIRMATION AND LEAD ADJUDICATION**. This is not a canonical proved label.
