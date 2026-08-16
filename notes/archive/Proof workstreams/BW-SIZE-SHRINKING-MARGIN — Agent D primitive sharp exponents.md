---
type: noncanonical-working-proof-dossier
title: BW-SIZE-SHRINKING-MARGIN — Agent D primitive sharp exponents
status: first-complete-dossier-and-agent-e-cross-audit-pass-1-complete
authority: noncanonical-agent-d-only
stage: 2-shrinking-margin
prerequisite: BW-SIZE-FIXED-MARGIN Gate A
---

# BW-SIZE-SHRINKING-MARGIN — Agent D primitive sharp exponents

> **NONCANONICAL / STAGE 2 WORKING DOSSIER.** This file rederives margin powers from the quotient formulas. Stage 1 recurrence exponents are not used as sharpness evidence. Labels below distinguish **EXACT**, **NECESSARY**, **SUFFICIENT**, and **UNRESOLVED**. No statistical theorem or canonical status is asserted here.

## 1. Typed shrinking-margin variables

For each (n), put

\[
 a:=\sqrt{\alpha_n},\qquad B:=\sqrt{\beta_n}.
\tag{1.1}
\]

Thus lifts have singular values in ([a,B]). Two singular-value margins have different physical homogeneity and are separated throughout:

\[
 p:=\chi_{{\rm P},n}
 \quad\hbox{for }\sigma_{\min}(M^TL),
 \qquad
 e:=\chi_{{\rm E},n}
 \quad\hbox{for }\sigma_{\min}(L+H).
\tag{1.2}
\]

Here (p) has the units of an eigenvalue and (e) the units of a lift singular value. The repository currently uses one numeral (chi_n) in both places. Its convention is recovered only at the end by setting (p=e=chi_n); the compatibility test is then (max\{\chi_n,\chi_n^2\}<\beta_n). Conflating (1.2) before exponent algebra produces dimensionally misleading powers.

Useful dimensionless ratios are

\[
 \kappa=B/a,\qquad \kappa_{\rm P}=B^2/p,
 \qquad \kappa_{\rm E}=B/e,
 \qquad \tau=r_0/a.
\tag{1.3}
\]

All lift directions use Frobenius norm; fixed matrix coefficients use operator norm; intrinsic tangent directions use BW norm; transport differences use operator norm after typed endpoint connectors. A factor (m_n), a trace, or (|L|_F) never enters the estimates below.

## 2. Classification convention

An exponent is called **sharp** only when an upper bound and a retained-hypothesis lower family have the same homogeneity. A multivariate monomial is not called sharp merely because a proof produces it. For composed endpoint maps I retain the full finite sum when different monomials compete.

The scale map

\[
 L\mapsto tL,\quad A\mapsto t^2A,quad
 d_{\rm BW}\mapsto t,d_{\rm BW}
\tag{2.1}
\]

is used only as a homogeneity check. It does not determine dependence on the condition ratios in (1.3).

## 3. Exact invariant matrix primitives

### 3.1 Sylvester inverse

For (G\succeq a^2I), let (mathscr S_GX=GX+XG). Direct differentiation gives

\[
 D^k(\mathscr S_\bullet^{-1})_G[H_1,\ldots,H_k]Y
 =(-1)^k\sum_{\sigma\in S_k}
 \mathscr S_G^{-1}\mathscr S_{H_{\sigma(1)}}\cdots
 \mathscr S_{H_{\sigma(k)}}\mathscr S_G^{-1}Y,
\]

and therefore

\[
 \boxed{\|D^k\mathscr S_G^{-1}\|_{F^k\times F\to F}
 \le {k!\over2}\alpha_n^{-(k+1)}.}
\tag{3.1}
\]

This power is **EXACT/SHARP**. At (G=\alpha_n I), scalar directions make (3.1) an equality up to the fixed factorial coefficient. Repeated positive eigenvalues cause no new denominator.

### 3.2 Inverse, square root, and inverse square root

Invariant differentiation of (Q^2=A), followed by the Sylvester bound at (Q\succeq aI), yields

\[
 \boxed{
 \|D^k A^{1/2}\|_{F^k\to F}\le c_k a^{1-2k}
 =c_k\alpha_n^{1/2-k}.}
\tag{3.2}
\]

The inverse formula and composition give

\[
 \boxed{
 \|D^k A^{-1}\|\le k!\alpha_n^{-k-1},\qquad
 \|D^k A^{-1/2}\|\le c_k\alpha_n^{-k-1/2}.}
\tag{3.3}
\]

All three powers are **EXACT/SHARP in raw Frobenius coordinates**, by the scalar family (A=\alpha_n I). The upper band occurs only at order zero:

\[
 \|A^{1/2}\|_{\rm op}=B,\qquad \|A^{-1/2}\|_{\rm op}=a^{-1}.
\tag{3.4}
\]

If every raw base direction is first bounded by
(|U|_F\le2B|U|_{A,{\rm BW}}), (3.2) gives the valid but generally non-sharp chart bound

\[
 \|D^kA^{1/2}\|_{{\rm BW}^k\to F}
 \le c_k a^{1-2k}B^k.
\tag{3.5}
\]

The (B^k) in (3.5) is a norm-conversion artifact: at (A=a^2I), normalized BW directions give the smaller scale (a^{1-k}). Generated maps should therefore be differentiated in horizontal-lift charts whenever possible. I do not label (3.5) sharp.

### 3.3 Polar factor: no upper-band power is intrinsic

Write (C=QP), (Q={\rm polar}(C)), (P=(C^TC)^{1/2}\succeq pI). If (Omega=Q^TDQ[C][H]), differentiation of (Q^TQ=I) and symmetry of (Q^TC=P) gives the exact Sylvester equation

\[
 P\Omega+\Omega P=Q^TH-H^TQ.
\tag{3.6}
\]

Hence (|DQ(C)[H]|_F\le p^{-1}|H|_F). Repeatedly differentiating (3.6), and using (DP=\operatorname{sym}(Q^TH)) at first order, gives by induction

\[
 \boxed{\|D^k{\rm polar}(C)\|_{F^k\to F}
 \le c_k p^{-k}.}
\tag{3.7}
\]

This is **EXACT/SHARP**. The family (C=pI+tK), with a fixed (2\times2) skew block (K), has nonzero Taylor coefficients with scale (p^{-k}) (use independent multilinear directions if a one-parameter parity coefficient vanishes). There is no genuine (B)-power in the polar primitive. The much larger Stage 1 square-root/inverse composition is sufficient but not sharp.

For a polar input actually equal to (M^TL), with both factors in the band,

\[
 \sigma_{\min}(M^TL)\ge a^2=\alpha_n.
\tag{3.8}
\]

Thus the effective available polar margin is (max\{p,\alpha_n\}). A declared (p<\alpha_n) does not create additional blow-up for such a factored input.

### 3.4 Exact tangent/lift conversions

The Stage 1 identity remains exact:

\[
 {1\over4\beta_n}\|U\|_F^2
 \le\|U\|_{A,{\rm BW}}^2
 \le {1\over4\alpha_n}\|U\|_F^2.
\tag{3.9}
\]

Consequently (2B) in BW-to-Frobenius conversion and ((2a)^{-1}) in Frobenius-to-BW conversion are both **SHARP**, at (A=\beta_n I) and (A=\alpha_n I), respectively. These powers must not be reinterpreted as intrinsic curvature blow-up.

## 4. Quotient primitives in lift coordinates

### 4.1 Horizontal projector

Let (J_L:\mathfrak{so}(m)\to\mathbb R^{m\times m}), (J_L\Omega=L\Omega). Then

\[
 \sigma_{\min}(J_L)\ge a,\qquad
 P_L^{\mathcal V}=J_L(J_L^*J_L)^{-1}J_L^*,\qquad
 P_L^{\mathcal H}=I-P_L^{\mathcal V}.
\tag{4.1}
\]

Differentiating the orthogonal range projector (or using its local graph over ({\rm ran}(J_L))) gives

\[
 \boxed{
 \|D_L^kP_L^{\mathcal H}\|_{F^k\times F\to F}
 \le c_k a^{-k}=c_k\alpha_n^{-k/2},\quad k\ge1.}
\tag{4.2}
\]

This improves the uncancelled Stage 1 Sylvester expression. It is **SHARP in lower-margin homogeneity**: at (L=aI), a fixed nonscalar perturbation changes the horizontal subspace at order (a^{-1}), and higher derivatives scale by (2.1). No (B)-power is necessary.

### 4.2 Horizontal right inverse

For fixed raw symmetric (U), (mathfrak h_L(U)=\mathcal L_{LL^T}^{-1}(U)L) has degree (-1) in (L). The same range-inverse argument gives

\[
 \|D_L^k\mathfrak h_L(U)\|_F
 \le c_k a^{-k-1}\|U\|_F\prod_i\|H_i\|_F.
\tag{4.3}
\]

This is **SHARP in raw (U_F) typing** by the scalar family. When (U) is normalized in the BW norm at the same base, the zeroth map is an isometry and the natural coefficient scale is instead (c_ka^{-k}). Mixing these two input typings is the source of the Stage 1 (beta^{3/2} alpha^{-2}) connection envelope.

### 4.3 O'Neill tensor, connection, and curvature

For horizontal lift inputs (X,Y) of Frobenius norm one,

\[
 \mathcal A_XY={1\over2}P^{\mathcal V}
 \{(D P^{\mathcal H})[X]Y-(D P^{\mathcal H})[Y]X\}.
\tag{4.4}
\]

Equations (4.2) and (4.4) imply

\[
 \boxed{
 \|D_L^k\mathcal A\|_{F^k\times F^2\to F}
 \le c_k a^{-k-1}.}
\tag{4.5}
\]

At (L=aI), for symmetric horizontal (X,Y), direct substitution in the Stage 1 formula gives

\[
 \mathcal A_XY=-{[X,Y]\over2a}.
\tag{4.6}
\]

Thus the (a^{-1}) power in (4.5) is **SHARP** for noncommuting (2\times2) blocks.

O'Neill's exact formula is quadratic in (mathcal A). Therefore

\[
 \boxed{
 \|D_L^kR\|_{F^k\times F^3\to F}\le c_k a^{-k-2},
 \qquad
 \|\nabla^kR\|_{{\rm BW}^{k+3}\to{\rm BW}}
 \le c_k a^{-k-2}
 =c_k\alpha_n^{-(k+2)/2}.}
\tag{4.7}
\]

The zeroth power (a^{-2}=\alpha_n^{-1}) is **SHARP** because
(langle R(X,Y)X,Y\rangle=3\|\mathcal A_XY\|_F^2) and (4.6) is nonzero. Radial scaling of this noncommuting family supplies the necessary homogeneity at higher covariant orders; vanishing of a particular directional derivative is handled by a mixed radial/noncommuting tuple.

The constant-coordinate Christoffel bilinear map has

\[
 \boxed{\|D_A^k\Gamma_A\|_{{\rm BW}^{k+2}\to{\rm BW}}
 \le c_k a^{-k-1}=c_k\alpha_n^{-(k+1)/2}.}
\tag{4.8}
\]

This homogeneity is **SHARP already for (m=1)**: (g_A=(4A)^{-1}dA^2), so (Gamma_A(U,V)=-UV/(2A)).

## 5. Alignment, Exp, Log, Hessian, and normal radius

### 5.1 Raw factored alignment recurrence

For (C=M^TL), with lift-Frobenius endpoint directions,

\[
 c_0=B^2,qquad c_1=2B,qquad c_2=2,qquad c_j=0\ (j\ge3).
\tag{5.1}
\]

Combining (3.7) with the exact set-partition chain rule gives the **SUFFICIENT** finite sum

\[
 q_k^{\rm pol\circ gram}
 \le C_k\sum_{s=0}^{\lfloor k/2\rfloor}
 B^{k-2s}p^{-(k-s)}.
\tag{5.2}
\]

For (mathcal N(L,M)=M{\rm polar}(M^TL)),

\[
 \boxed{
 \|D^k\mathcal N\|_{F^k\to F}
 \le C_k\{Bq_k^{\rm pol\circ gram}+kq_{k-1}^{\rm pol\circ gram}\}.}
\tag{5.3}
\]

Equations (5.2)--(5.3) are explicit and valid, but are **NOT CLAIMED SHARP**. When (L,M) are banded factors, (3.8), horizontality, and alignment produce cancellations not seen by treating (C) as an arbitrary matrix. In particular, commuting diagonal variations have identically constant polar factor. Determining the smallest joint ((a,B,p)) powers of the full factored map beyond first order remains item U-D1 below.

### 5.2 Exp forward map and Exp margin

In lift coordinates,

\[
 \operatorname{Exp}_A(d\pi_LH)=\pi(L+H),qquad
 D\pi_Z[K]=KZ^T+ZK^T,qquad D^2\pi_Z[K_1,K_2]
 =K_1K_2^T+K_2K_1^T.
\tag{5.4}
\]

Thus the forward Exp polynomial has no inverse power of (e): its first derivative pays (|L+H|_{\rm op}), its second derivative is absolute, and higher lift derivatives vanish. The Exp margin is a **domain/closure margin**, not a forward-differential singularity. If the output is also required to lie in the spectral band, then (sigma_{\min}(L+H)\ge a) automatically, so the effective lower factor margin is (max\{e,a\}).

### 5.3 Intrinsic scaling of Log and generated geodesic maps

On normal pairs contained in a quotient ball of radius (ca), intrinsic endpoint derivatives have the homogeneity

\[
 \|D^k\Log\|_{{\rm BW}^k\to{\rm BW}}
 +\|D^k\operatorname{Chord}\|_{{\rm BW}^k\to{\rm BW}}
 \le C_k(c) a^{1-k}.
\tag{5.5}
\]

This is a **SUFFICIENT local invariant bound** obtained from (4.7), the Jacobi equation after rescaling length by (a), and the no-conjugacy condition. The (a^{1-k}) homogeneity is necessary whenever the corresponding derivative is nonzero, by (2.1). A global pair may additionally pay condition-ratio/alignment factors; (5.2)--(5.3) are the safe raw-coordinate fallback.

The same local homogeneity applies to fixed-coefficient Richardson, blend, and nested ruled maps, except that their output membership and signed-factor margin must be checked separately.

### 5.4 Observation Hessian

Let (mathsf H(A,B)=-\nabla_A\Log_AB). In a normal pair ball (d(A,B)\le ca), the Jacobi expansion and (4.7) give

\[
 \boxed{
 \|\nabla_{A,B}^{,q}\mathsf H(A,B)\|
 \le C_q(c)a^{-q},\qquad q\ge0,}
\tag{5.6}
\]

where (q=0) is (O(1)). In particular the uniform observation Lipschitz coefficient satisfies

\[
 L_H\le C(c)a^{-1}=C(c)\alpha_n^{-1/2}.
\tag{5.7}
\]

The first observation derivative vanishes at (B=A), but its supremum on a radius-(ca) ball has scale (a^{-1}); the second derivative at the diagonal contains curvature and has scale (a^{-2}). Thus (5.6) is the correct uniform-ball scaling, not a claim that every diagonal derivative is nonzero.

### 5.5 Produced normal radius and generated radii

Since (mathsf H(A,A)=I), (5.7) produces

\[
 \boxed{
 \rho_H=\min\{r_0,c_Ha\}}
\tag{5.8}
\]

for a numerical \(c_H>0\) after intersecting with all other domain
slacks. The power \(a=\sqrt{\alpha_n}\) is **SHARP for a uniform
full-rank normal-domain radius**: the BW distance from \(a^2I\) to a
matrix obtained by collapsing one root coordinate to zero is exactly
\(a\). No full-rank normal ball centred there can have a larger order
uniformly in \(m\). This boundary family does not by itself prove that
the Hessian loses positivity at radius \(a\); no separate sharp
Hessian-loss constant is claimed.

For Richardson coefficients with (sum|\lambda_j|=5), the factor-margin test gives the separate produced radius

\[
 r_R\le {a-e\over5}.
\tag{5.9}
\]

This is a domain restriction. Retaining the output lower spectral band (alpha_n I) additionally requires inner-band slack; a point on the lower boundary has no nonzero signed radius. For polar inputs, if the population cross-Gram slack is
(s_P=\sigma_{\min}(M^TL)-p), perturbing both factors by (z) changes the cross Gram by at most (2Bz+z^2), so a sufficient polar-neighbourhood radius is

\[
 z\le c\min\{B,s_P/B\}.
\tag{5.10}
\]

Similarly define factor slacks (s_-=\sigma_{\min}(L)-a),
(s_+=B-\sigma_{\max}(L)), and (s_E=\sigma_{\min}(L+H)-e). The complete generated radius is bounded by the minimum of these raw slacks after division by the corresponding first derivative of the generated map. It cannot be expressed from ((\alpha_n,\beta_n,p,e)) alone when a population tuple lies on a declared boundary.

## 6. Parallel transport and its variations

### 6.1 Coefficient of the exact lift ODE

The Stage 1 ODE is

\[
 \dot H=L\mathscr S_{L^TL}^{-1}
 (H^T\dot L-\dot L^TH)=:\mathcal B(L,\dot L)H.
\tag{6.1}
\]

Diagonalizing (L^TL) and using
(x/(x^2+y^2)\le(2y)^{-1}) gives the sharper bound

\[
 \boxed{\|\mathcal B(L,\dot L)\|_{F\to F}
 \le C a^{-1}\|\dot L\|_{\rm op}.}
\tag{6.2}
\]

The (B/\alpha_n) bound from paying (L) before the Sylvester solve is not sharp. Equation (6.2) has the necessary (a^{-1}) scale, consistent with (4.8). Transport itself remains exactly isometric.

For lift variations (V_j=\partial_\theta^jL), differentiation gives the typed first budget

\[
 \int\|D_\theta\mathcal B\|dt
 \le C\left{
 a^{-2}\int\|\dot L\|\,dt\ \sup_t\|V_1\|_F
 +a^{-1}\int\|\dot V_1\|_Fdt\right}.
\tag{6.3}
\]

At order (q), the exact sufficient recurrence is

\[
 K_q\le C_q\sum_{\mathcal P}
 a^{-|\mathcal P|-1}
 \left[
 r_0\prod_{C\in\mathcal P}\sup_t\|V_{|C|}\|_F
 +\sum_{C_0\in\mathcal P}
 \int\|\dot V_{|C_0|}\|_Fdt
 \prod_{C\ne C_0}\sup_t\|V_{|C|}\|_F
 \right],
\tag{6.4}
\]

where the finite sum uses the partitions created by differentiating the coefficient and one block is allowed to hit (dot L). Formula (6.4), rather than one coarse monomial, is the exact Agent-E interface for an explicitly supplied canonical lift family.

Variation of constants uses norm-one PT, hence

\[
 \boxed{\|D_\theta^qP_\gamma\|_{\rm op}
 \le\mathfrak B_q(K_1,\ldots,K_q).}
\tag{6.5}
\]

There is no exponential in (r_0/a). Endpoint-fibre connectors add finite product/inverse recurrences but no Gronwall factor. For independently varying (N)-segment polygons, replace every (K_q) by its sum over cells; the resulting Bell polynomial retains the explicit (N+\mathsf L) dependence in the (oplus,\infty) endpoint norm.

### 6.2 Curvature variation and PF coefficient

For a ruled cell (F),

\[
 \|P_{\partial F}-I\|_{\rm op}
 \le C_R\operatorname{Area}(F),\qquad
 \boxed{C_R\le C\alpha_n^{-1}.}
\tag{6.6}
\]

The \(\alpha_n^{-1}\) power is **SHARP** by the small noncommuting rectangle at \(L=aI\), using (4.6). Let

\[
\vartheta_{\rm cell}
:=a^{-1}\max_j\{\ell_j,e_j,e_{j+1}\}.
\tag{6.6a}
\]

On the declared fractional-normal cell regime
\(\vartheta_{\rm cell}\le c_{\rm cell}<c_H\), the endpoint Jacobi
operators and direct chord maps are \(O_{c_{\rm cell}}(1)\): rescale
the Jacobi equation by \(a\), use (4.7), and use the quantitative
no-conjugacy/Exp margin supplied by the same fractional-normal ball.
Total mean-path length need not be \(O(a)\); it is resolved into local
cells. Outside this cell regime no bound depending only on
\(r_0/a\) is asserted. One must use the raw alignment recurrence and a
separate quantitative Exp/no-conjugacy margin.

The canonical PF inequality therefore has geometry coefficient

\[
 \boxed{
 C_{{\rm PF},n}\le C(c_{\rm cell})\alpha_n^{-1}}
\tag{6.7}
\]

and keeps the statistical/path bracket visible:

\[
 \|C_N^{-1}\widehat P C_0-P_\mu\|_{\rm op}
 \le C_{{\rm PF},n}
 \{v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}\}.
\tag{6.8}
\]

Thus fixed fractional-normal ruled cells give the sharp
necessary/sufficient lower-margin power \(\alpha_n^{-1}\), even when
the complete mean path has fixed nonshrinking total length.

## 7. Primitive exponent ledger

| Object and derivative order | Typed norm | Upper dependence | Classification | Lower family / comment |
|---|---|---:|---|---|
| (mathscr S_G^{-1}), (D^k) | (F^k\times F\to F) | (alpha_n^{-(k+1)}) | EXACT/SHARP | scalar (G=\alpha_n I) |
| (A^{1/2}), (D^k) | raw (F^k\to F) | (alpha_n^{1/2-k}) | EXACT/SHARP | scalar |
| (A^{-1/2}), (D^k) | raw (F^k\to F) | (alpha_n^{-k-1/2}) | EXACT/SHARP | scalar |
| (A^{-1}), (D^k) | raw (F^k\to F) | (alpha_n^{-k-1}) | EXACT/SHARP | scalar |
| polar, (D^k) | (F^k\to F) | (p^{-k}) | EXACT/SHARP | near-singular (2\times2) skew family |
| BW/F norm conversion | tangent | (2B,(2a)^{-1}) | EXACT/SHARP | isotropic upper/lower bases |
| (P_L^H), (D_L^k) | (F^k\times F\to F) | (a^{-k}) | SHARP lower power | range-projector family at (aI) |
| horizontal inverse, (D_L^k) | raw (U_F) | (a^{-k-1}) | SHARP raw typing | scalar |
| O'Neill (mathcal A), (D_L^k) | (F^{k+2}\to F) | (a^{-k-1}) | SHARP | noncommuting (2\times2) block |
| (\nabla^kR) | ({\rm BW}^{k+3}\to{\rm BW}) | (a^{-k-2}) | SHARP homogeneity | noncommuting isotropic family |
| (D_A^k\Gamma) | ({\rm BW}^{k+2}\to{\rm BW}) | (a^{-k-1}) | SHARP | scalar Christoffel |
| PT ODE coefficient | (F\to F) | (a^{-1}\|\dot L\|) | SHARP scale | direct diagonalized coefficient |
| Hessian (q)-derivative on (ca)-ball | ({\rm BW}^q\to{\rm End}) | (a^{-q}) | SHARP homogeneity; diagonal caveat | curvature at (q=2) |
| normal radius | BW length | (c_Ha) | SHARP order | rank-boundary distance (a) |
| forward Exp in lift coordinates | lift polynomial | no (e^{-1}) | EXACT | (e) is closure only |
| holonomy/PF area coefficient | area-to-operator | (a^{-2}=\alpha_n^{-1}) | SHARP | noncommuting small rectangle |
| factored alignment (D^k) | lift endpoints | (5.2)--(5.3) | SUFFICIENT ONLY | cancellation unresolved |

The only unavoidable upper-band powers in this table are the exact raw tangent conversion (B) and order-zero lift size. No intrinsic quotient-curvature primitive needs a positive power of beta_n.

## 8. Lower-bound families and artifacts

1. **Scalar root family.** (A=x^2) proves the powers for Sylvester, square root, inverse maps, raw horizontal inverse, tangent conversion, and Christoffel. It cannot lower-bound curvature or PF because the scalar BW manifold is flat.
2. **Commuting diagonal family.** All polar, O'Neill, curvature, and holonomy terms vanish. Any claimed universal lower bound based only on rank loss but not noncommutativity is false.
3. **Noncommuting isotropic family.** At (L=aI), symmetric unit-Frobenius (X,Y) with ([X,Y]\ne0) give (mathcal A_XY=-[X,Y]/(2a)), curvature (a^{-2}), and holonomy (a^{-2}\times\) area. This proves genuine geometric blow-up independent of multiplicity.
4. **Polar-near-singular family.** (C=pI+tK) proves (p^{-k}) for the polar primitive. It need not be realizable with fixed banded factors when (p<\alpha_n); in the factored consumer (3.8) must be enforced.
5. **Rank-boundary family.** Collapsing one root coordinate from (a) to zero costs BW distance (a), proving that the normal/full-rank radius cannot exceed order (sqrt{\alpha_n}).
6. **Upper-band artifact check.** The Stage 1 connection estimate beta_n^{3/2} alpha_n^{-2} contradicts the exact scalar and isotropic scaling and is only a sufficient uncancelled expression-tree bound. It is not a shrinking-margin exponent.
7. **Exp-margin artifact check.** No (e^{-1}) occurs in forward Exp. A vanishing (e)-slack makes the generated-domain event fail; it does not make the polynomial map derivative singular before inversion or output norm conversion.

## 9. Exact interface for Agent E

Agent E may use the following without importing Stage 1's coarse common constant.

### 9.1 Sharp invariant coefficients

For fixed public derivative order (k_0), (K=\max\{k_0,2\}), define

\[
 G_{R,j}=C_j\alpha_n^{-(j+2)/2},\quad 0\le j\le K-1,
\qquad
 G_{H,j}=C_j\alpha_n^{-j/2},\quad0\le j\le K,
\tag{9.1}
\]

\[
 \rho_{H,n}=\min\{r_{0,n},c_H\sqrt{\alpha_n},
 \hbox{all declared generated-domain radii}\},
\tag{9.2}
\]

and, on fractional-normal ruled cells satisfying (6.6a),

\[
 G_{{\rm PF},n}=C\alpha_n^{-1}.
\tag{9.3}
\]

No bound on total path length divided by \(\sqrt{\alpha_n}\) is needed
for (9.3). Instead every PF cell must satisfy (6.6a). Outside that
local-cell regime, use the raw alignment/Exp recurrences and retain
their separate margins.

### 9.1a Composite slots consumed by Agent E

On the half-Hessian ball, all norms are BW norms at typed connected
bases. The sufficient geometry-only slot values are

\[
\boxed{
K_{S,n}=O(1),\qquad
K_{{\rm R1},n}=O(1),\qquad
K_{B,n}\le C(1+\alpha_n^{-1}),\qquad
K_{L,n}^{(1)}=O(1),\qquad
K_{L,n}^{(2)}\le C\alpha_n^{-1/2},
}
\tag{9.4}
\]

\[
\boxed{
K_{F,n}\le C\alpha_n^{-1},\qquad
K_{C,n}=O(1),\qquad
K_{G,n}=O(1)
}
\tag{9.4a}
\]

provided \(\delta_{{\rm GD},n}\) is measured in the normalized
length/factor units of (9.6), rather than raw eigenvalue units.
Here:

1. \(K_S\) is \(O(1)\) because the produced Hessian is between
   \(I/2\) and \(3I/2\); no Frobenius norm conversion is used in the
   score-to-distance inequality.
2. The cubic mean/implicit-function calculation uses Hessian
   derivatives through order two and the generated
   Richardson/Exp/Log map through order three. Equations (5.5)--(5.6)
   therefore give the sufficient cubic-bias factor
   \(K_B\le C(1+\alpha_n^{-1})\). The first Richardson differential
   multiplying stochastic score error is only \(K_{\rm R1}=O(1)\).
   The time/law third-derivative budget \(B_{3,n}\) remains separate
   and is not proved by geometry. Using one lumped
   \(K_M=K_B\) on both bias and variance is valid but non-sharp.
   Higher generated-map remainders are absorbed only after the
   positive-stage localization error is \(o(a)\).
3. First-order local Log/recentring is \(O(1)\). Its quadratic
   remainder is bounded separately by
   \(C\alpha_n^{-1/2}r_{\mu,n}^2\). It can be absorbed into
   \(K_L^{(1)}r_{\mu,n}\) only after
   \(r_{\mu,n}=o(\sqrt{\alpha_n})\).
4. \(K_F\) is (6.7). Typed radial connectors and endpoint fibre
   identifications are isometries, so the residual \(K_C\) is \(O(1)\);
   their parameter derivatives, when separately requested, use
   (6.4)--(6.5).
5. \(K_G=O(1)\) only because raw spectral and polar slacks are first
   converted to factor/BW length slacks in (9.6). If a consumer keeps
   raw eigenvalue slack, its conversion factor must remain visible.

Consequently the sharp-interface mean formula is termwise:

\[
r_{\mu,n}\lesssim
K_{B,n}B_{3,n}h_n^3
K_{{\rm R1},n}\left\{
{\Theta_{S,2,n}\over\sqrt{nh_n}}
+L_{{\rm LS},n}+G_n/n\right\}
+{\rm Rem}_{\mu,n},
\tag{9.4b}
\]

with the analogous logarithmic score term for the supremum rate.
Under \(u_{{\rm stg},n}=o(a)\), the higher generated-map stochastic
remainders satisfy
\[
{\rm Rem}_{\mu,n}
\le C a^{-1}u_{{\rm stg},n}
\left\{{\Theta_{S,2,n}\over\sqrt{nh_n}}
+L_{{\rm LS},n}+G_n/n\right\},
\tag{9.4c}
\]
and are therefore absorbed by the linear score term. A single common
\(K_M=K_B\) multiplying (9.4b) is sufficient but discards this
first-derivative cancellation and is not an exponent-sharp
propagation.

### 9.2 Endpoint and transport recurrence

For every canonical lift family actually used, compute (V_j,\dot V_j) and insert them in (6.4), then define

\[
 T_q=\mathfrak B_q(K_1,\ldots,K_q).
\tag{9.5}
\]

For raw principal-root/polar endpoint coordinates, use (3.2), (5.2), and (5.3) as a sufficient recurrence. Do not compress their competing monomials to a “sharp” (alpha^{-a}\beta^bp^{-c}) claim.

### 9.3 Complete generated-set slack

Let

\[
 \delta_{{\rm GD},n}=\min\{
 s_-,s_+,s_E,s_P/B,
 s_{H,n},(a-e)/5,
 \delta_{c,n},\hbox{path/ruled membership slacks}\}.
\tag{9.6}
\]

The normal-pair entry is the **strict population slack**

\[
s_{H,n}:=\rho_{H,n}
-\sup\{d_{\rm BW}(q^0,X):
(q^0,X)\text{ is any population/proxy score pair consumed}\}>0,
\tag{9.6a}
\]

not \(\rho_{H,n}\) itself. Perturbing a stage base by \(z\) consumes at
most \(z\) of this slack. Nonemptiness therefore requires all raw and
proxy observations to be supported strictly inside the produced
normal ball. In the full noncommuting theorem this implies the
pathwise tangent-support bound

\[
\|Y_{t,n}\|_{\rm BW}\le R_n<\rho_{H,n}
\lesssim\sqrt{\alpha_n},
\qquad
\mathcal E_{2,n}\le R_n.
\tag{9.6b}
\]

A nonempty shrinking-margin family is obtained by taking
\(Y_{t,n}=\sqrt{\alpha_n}\,\widetilde Y_{t,n}\), with
\(\|\widetilde Y_{t,n}\|\le c<c_H\), and placing every generated
population tuple at a fixed fractional slack from the remaining
failure sets. Fixed or growing tangent energy is incompatible with
\(\alpha_n\downarrow0\) under this full noncommuting normal-pair
package; the globally flat diagonal submodel is a separate theorem
class.

This notation suppresses fixed numerical constants only. If (L_{{\rm gen},n}) is the first-derivative recurrence of the complete generated map, the event requires

\[
 \max_j e_j=o_p(\delta_{{\rm GD},n}/L_{{\rm gen},n})
\quad\hbox{or}\quad
 \sqrt{N+1}\,r_N=o_p(\delta_{{\rm GD},n}/L_{{\rm gen},n}).
\tag{9.7}
\]

No theorem can replace the population slacks in (9.6) by ((\alpha_n,\beta_n,p,e)) alone.

### 9.4 PF propagation input

Agent E should propagate exactly

\[
 r_{F,n}\le G_{{\rm PF},n}
 \{v_{\mu,n}r_N+(N+1)r_N^2
 +v_{\mu,n}a_{\mu,n}N^{-2}\},
\tag{9.8}
\]

plus any endpoint-connector term already included in the typed definition of (r_{F,n}). Matrix size enters (9.1)--(9.8) only through margins, path quantities, the number of vertices/generated objects, and the statistical errors.

## 10. Unresolved sharp entries

| ID | Exact unresolved question | Current valid fallback | Why not closed here |
|---|---|---|---|
| U-D1 | Smallest joint ((a,B,p)) powers of (D^k[M{\rm polar}(M^TL)]) on banded horizontal endpoint directions | finite sum (5.2)--(5.3), with (p\leftarrow\max\{p,\alpha_n\}) | factored/horizontal cancellations can remove the raw (B^kp^{-k}) term |
| U-D2 | Sharp endpoint-Jacobi envelope outside a fixed fractional normal cell | raw alignment/Exp recurrence with a quantitative no-conjugacy margin | total path length alone cannot bound a boundary-value Jacobi inverse |
| U-D3 | Smallest powers for higher derivatives of complete Richardson/blend/ruled endpoint maps on nonlocal pairs | invariant local (a^{1-k}), otherwise raw recurrence | signed closure and alignment condition ratios compete |
| U-D4 | Whether every higher PT endpoint derivative has a polynomial, rather than merely recurrence-defined, dependence on the normalized path/cell budgets after canonical cancellations | (6.4)--(6.5) | Bell recurrence is exact and finite but not exponent-minimized |

These are unresolved exponent minimizations, not failures of the fixed-margin theorem. Agent E can state a theorem with the displayed sufficient recurrences. A claim of a single sharp monomial must wait for U-D1--U-D4 or an argument that the relevant consumer avoids them.

## 11. First-pass conclusion

The genuine singular geometry scale is the lower root margin (a=\sqrt{\alpha_n}): projector derivatives cost (a^{-k}), curvature costs (a^{-2}), the Hessian derivative costs (a^{-1}), and the produced normal radius is (a). Polar calculus has its own exact (p^{-k}) primitive, but for banded factored alignments (p\ge\alpha_n) automatically. The Exp factor margin controls closure and admissible signed radii, not the forward Exp derivative. Upper-band powers occur in raw coordinate conversions and a safe alignment recurrence; they have not been shown intrinsic. PF necessarily pays (alpha_n^{-1}) times its visible area/error bracket on a fractional normal domain.

This dossier is ready for Agent E propagation with the exact interface in Section 9 and for Agent F's independent sharpness attack.

## 12. Mandatory cross-audit of Agent E — pass 1

I read Agent E's complete first dossier and checked every substitution
against Sections 3--9 above.

### 12.1 Objection ledger

| ID | E claim/interface | Attack | Required repair or disposition | Status |
|---|---|---|---|---|
| E-X1 | \(\delta_{\rm GD}\) contains only a named normal radius | A radius is not population slack; every score pair may already sit on its boundary | replace it by \(s_H\) in (9.6a), and require perturbation smaller than \(s_H/K_G\) | VALID; D repaired |
| E-X2 | tangent energy \(m^e\) is freely combined with a shrinking \(\alpha_n\) | the full noncommuting GD requires every observation score pair inside \(\rho_H\lesssim\sqrt{\alpha_n}\), hence \(R_n,\mathcal E_{2,n}\lesssim\sqrt{\alpha_n}\) | add the support/energy compatibility (9.6b); a fixed/growing-energy branch is empty when \(\alpha_n\downarrow0\) unless a different flat/global theorem is invoked | VALID; E must repair |
| E-X3 | \(K_S,K_M,K_G,K_L,K_F,K_C\) left as lumped monomial slots | this can hide order shifts and falsely multiply stochastic score noise by the cubic-bias coefficient | use the termwise (9.4)--(9.4a): \(K_S=K_{\rm R1}=1\), \(K_B\lesssim1+\alpha^{-1}\); keep \(B_{3,n}\) and law smoothness separate | VALID; D supplied interface |
| E-X4 | one \(\chi_n\) exponent controls polar and Exp margins | cross-Gram and lift margins have different homogeneity | use \(p=\chi_P\), \(e=\chi_E\), or state that the repository's common numeral is substituted into two differently typed tests | VALID |
| E-X5 | first-order feasible Log error is \(K_Lr_\mu\) | the quadratic remainder has coefficient \(\alpha_n^{-1/2}\) | add \(C\alpha_n^{-1/2}r_\mu^2\), or impose \(r_\mu=o(\sqrt{\alpha_n})\) before absorbing it into \(O(r_\mu)\) | VALID |
| E-X6 | PF grid condition uses only estimation and acceleration errors | the local-cell producer \(K_F=O(\alpha_n^{-1})\) also requires \(\ell_j\le v_\mu/M=o(\sqrt{\alpha_n})\) and connector maxima \(o(\sqrt{\alpha_n})\) | add \(v_\mu/M\) to the generated-cell test; for RMS-only vertices use \(\max e_j\le\sqrt{M+1}r_\mu\) | VALID |
| E-X7 | \(K_F\) may be treated as a function of total path length alone | endpoint Jacobi boundary maps need a local Exp/no-conjugacy margin; total length does not provide it | use local cells (6.6a); total path may remain fixed | VALID; D repaired |
| E-X8 | “nonempty for sufficiently small \(x\)” whenever the formal exponents are finite | finiteness does not imply the support-radius, signed Exp slack, polar slack, or signal/gap package is nonempty | demonstrate a DGP satisfying (9.6b) and recompute \(A_2,\Delta\); see Section 12.3 | VALID |
| E-X9 | positive-stage coefficient may pay a BW/F conversion | empirical score and distance live at the same BW base and Hessian coercivity is \(1/2\) | \(K_S=O(1)\); no \(\alpha^{-1/2}\) norm conversion is consumed | REPAIRED by (9.4) |
| E-X10 | one \(K_M\) multiplies cubic bias and score variance | third-order implicit/Richardson expansion needs Hessian derivatives through two and generated-map derivatives through three only for bias/remainders; the first stochastic differential is \(O(1)\) | sufficient \(K_B\le C(1+\alpha_n^{-1})\), \(K_{\rm R1}=O(1)\); law/time \(B_3\) remains external | REPAIRED by (9.4) |
| E-X11 | \(K_C\) may multiply frame error with another margin blow-up | typed radial connectors are isometries; their endpoint parameter variations are a different object | take residual \(K_C=O(1)\); keep (6.4)--(6.5) if a derivative of the connector map is actually used | REPAIRED |
| E-X12 | lumped mean balance (E.24)--(E.34) | one \(g_M\) on bias and score noise destroys the first-derivative cancellation and gives the wrong shrinking-margin window | split \(g_B\) from \(g_{\rm R1}\); recompute bandwidth and mean as (12.6a)--(12.7). The later row/gap algebra remains valid after this substitution | VALID; REPAIRED IN D |
| E-X13 | row assembly, Davis--Kahan, null square, selector | possible loss of \(A_2\), \(\Delta\), or \(d^2\) | E keeps \(\eta=2A_2d+d^2\), actual \(\Delta\), row min--max \(d^2\), and both selector inequalities | PASS |
| E-X14 | object counts and PF speed | possible hidden dimension/segment factor | E keeps \(\log(n\mathcal O_n)\), \(\sqrt{M+1}\), \(\sqrt{h_0}\), typed \(v_\mu\), and visible PF terms | PASS, subject to E-X6 |
| E-X15 | self-similar branch asserts \(r_\mu=O(a_n n^{-3/7})\) from “bounded normalized law derivatives” | the displayed lump \(K_BB_3h^3\) gives this only if the curvature-sensitive third-order input is \(B_3=O(a_n^3)\), while direct third law-score terms scale \(O(a_n)\) and must not be multiplied by \(K_B\) | E now states both scalings explicitly, so \(K_BB_3=O(a_n)\) and the direct term is also \(O(a_n)\) | REPAIRED AND ACCEPTED |

### 12.2 Corrected generated/PF tests

In Agent E's notation, the complete conditions must include

\[
K_Gu_{{\rm stg},n}=o(s_{H,n}),\qquad
K_Gr_{\infty,n}=o(s_{H,n}),
\tag{12.1}
\]

and, for the canonical PF grid,

\[
K_G\left\{
\sqrt{M_n+1}\,r_{\mu,n}
+{v_{\mu,n}\over M_n}
+a_{\mu,n}M_n^{-2}\right\}
=o(\delta_{{\rm GD},n}).
\tag{12.2}
\]

Here \(\delta_{{\rm GD},n}\) already includes \(s_H\) and all other
normalized slacks. Under (12.2), (6.6a) holds and
\(K_F=C\alpha_n^{-1}\). The feasible-observation expansion is

\[
q_{R,n}\lesssim
r_{\mu,n}
+\alpha_n^{-1/2}r_{\mu,n}^2
+r_{F,n}\{\mathcal E_{2,n}+r_{\mu,n}
+\alpha_n^{-1/2}r_{\mu,n}^2\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\tag{12.3}
\]

Once \(r_{\mu,n}=o(\sqrt{\alpha_n})\), (12.3) reduces to E's (E.11)
with \(K_L=K_C=O(1)\).

### 12.3 A nonempty full-noncommuting shrinking-margin window

This example is sufficient, not claimed sharp. To avoid collision with
the root scale \(a=\sqrt{\alpha_n}\), write \(A>0\) for the power in

\[
m_n=n^x,\qquad \alpha_n\asymp m_n^{-A},
\qquad \beta_n\asymp1.
\tag{12.4}
\]

Take separately typed margins \(p_n\asymp\alpha_n\) and
\(e_n\asymp\sqrt{\alpha_n}\), each with fixed fractional slack. Under
the repository's one-\(\chi_n\) convention, the sufficient common
choice \(\chi_n\asymp\alpha_n\) passes both tests. Let

\[
\|Y_{t,n}\|\le c\sqrt{\alpha_n},\qquad
\mathcal E_{2,n},\Theta_{S,2,n},\Theta_{S,\infty,n}
\asymp m_n^{-A/2},
\tag{12.5}
\]

and put every population generated tuple at fixed fractional
factor/normal slack. A bounded noncommuting \(2\times2\) block scaled
by \(\sqrt{\alpha_n}\), embedded in arbitrary matrix size, gives such
a family. Then

\[
g_S=g_G=g_L=g_C=g_{\rm R1}=0,\qquad
g_B=g_F=A,\qquad
d_G=A/2,\qquad e_{\rm stat}=-A/2.
\tag{12.6}
\]

The termwise balance is
\[
m_n^A h_n^3
\asymp m_n^{-A/2}(nh_n)^{-1/2}.
\tag{12.6a}
\]

Thus the bandwidth and mean exponent are

\[
h_n=n^{-(1+3xA)/7},\qquad
\zeta_\mu={3+2Ax\over7},\qquad
r_{\mu,n}=n^{-\zeta_\mu+o(1)}.
\tag{12.7}
\]

The stage/normal test gives \(x<2/A\), while the RMS grid and
local-cell test gives \(x<12/(13A)\). PF has

\[
r_{F,n}=O_p(\alpha_n^{-1}r_{\mu,n}),
\qquad
q_{R,n}=O_p(\alpha_n^{-1/2}r_{\mu,n}),
\tag{12.8}
\]

and multiplication by \(\mathcal E_{2,n}=O(\sqrt{\alpha_n})\) makes
the feasible row error \(d_n=O_p(r_{\mu,n})\), apart from the faster
oracle term \(O(\alpha_n n^{-1/2})\).

The support bound forces, for fixed lag count,

\[
A_{2,n}=O(\alpha_n),\qquad
\Delta_n=O(\alpha_n^2).
\tag{12.9}
\]

Choose a rank-one finite-memory factor block with matching lower
orders \(A_{2,n}\asymp\alpha_n\),
\(\Delta_n\asymp\alpha_n^2\). Then loading and selector consistency
both reduce to \(r_{\mu,n}=o(\alpha_n)\), namely

\[
\boxed{0<x<{3\over5A}.}
\tag{12.10}
\]

This interval is nonempty and is stricter than the stage and grid
conditions. It proves that shrinking-margin full-BW regimes are not
automatically empty, while also showing why Agent E's fixed/growing
energy and “pervasive signal” examples cannot be imported unchanged
into the full noncommuting normal-pair theorem.

### 12.4 Cross-audit verdict

Agent E's assembly, gap, null-spectrum, selector algebra, and symbolic
propagation after a termwise mean rate pass. Its original lumped
mean/power window does not pass. E-X1--E-X15 require the repairs
recorded above. The corrected sufficient geometry slots are
(9.4)--(9.4a), the termwise mean producer is (9.4b), the complete
domain tests are (12.1)--(12.2), and one verified nonempty
full-noncommuting window is (12.10). No nonsharp factored-alignment
monomial is needed in this local generated regime.
