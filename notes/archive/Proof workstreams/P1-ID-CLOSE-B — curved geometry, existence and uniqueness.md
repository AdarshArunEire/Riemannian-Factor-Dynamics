---
type: working-proof-dossier
title: P1-ID-CLOSE-B — curved geometry, existence and uniqueness
status: wave-1-author-version-awaiting-hostile-review
workstream: B
targets: ID-8, ID-9 route R1, ID-9 route R2
last-audited: 2026-08-12
---

# P1-ID-CLOSE-B — curved geometry, existence and uniqueness

> **Authority.** This is a proof record for Workstream B of the P1-ID-CLOSE campaign. Canonical status lives in [[P1-ID-CLOSE — lead ledger]] until Wave 4. Nothing here reopens ID-0–ID-6; ID-8 extends ID-4's negative side and ID-9/R1–R2 attack the ID-1 gate.
> **Numerics discipline.** Every numeric run below was used only to discover or sanity-check. Every status-bearing statement is exact and analytic. Sanity checks are recorded so a hostile auditor can re-run them, never as evidence.

## 0. Verdict summary

| Target | Verdict |
|---|---|
| **ID-8** | The lead's candidate universal theorem is **correct as an implication and must be corrected as a criterion**. Rank inflation holds whenever \(R(PV,w)PV\ne0\); nonzero sectional curvature of \(\operatorname{span}\{PV,w\}\) is **sufficient but not necessary**. Settled **exactly, not asymptotically**, in both project geometries: Bures–Wasserstein \({\rm SPD}(2)\) and AIRM \({\rm SPD}(2)\) both inflate rank, exactly, for every non-commuting configuration and every admissible \(b\). Neither failure is cut-locus-specific, compactness-specific, or completeness-specific. The **only** rigid branches are radial/common-geodesic supports, totally geodesic flats, and — in BW — the commuting/fixed-eigenbasis subcone, which is exactly a Euclidean orthant and is exactly affine under \(\Phi\). |
| **R1** | **No counterexample exists.** For every \(Q\) on \({\rm PSD}(m)\) with \(\int\operatorname{tr}\Sigma\,Q(d\Sigma)<\infty\), the BW Fréchet mean exists in \({\rm PSD}(m)\); and if \(Q\) charges the full-rank cone it lies in the **open** full-rank cone. The lead's route is confirmed, and the delicate perturbation step is replaced by an **exact one-sided nuclear-norm inequality** \(\Delta_\varepsilon(\Sigma)\ge\sqrt{\varepsilon\,s(\Sigma)}\) with **no remainder and no integrability side condition**. Higher corank needs no separate argument. |
| **R2** | **Split confirmed and sharpened.** BW uniqueness is **proved internally** for arbitrary \(Q\) (not finitely many atoms) charging the full-rank cone — a genuine strengthening of Agueh–Carlier Theorem 6.1, whose hypotheses do not cover the project's setting. Sphere uniqueness **fails**, with an exact positive-dimensional argmin (a whole \(S^{p-2}\)). **L-9.R2.3 is the sharpest crack and it bites:** a \(W_2\)-continuous family through a nonsingleton stratum admits a measurable but **no continuous** selector, and the forced jump manufactures a **lag-invariant, bandwidth-insensitive, rank-one contamination of size \(\pi^2\lambda(1-\lambda)\)** in the ID-5 lag row, which dominates the genuine factor row at every lag \(h\ge1\). It is convention-induced but **not removable by any single-valued convention**. |

---

## 1. Conventions locked for this dossier

**C1 (curvature sign).** \(R(u,v)w=\nabla_u\nabla_vw-\nabla_v\nabla_uw-\nabla_{[u,v]}w\), the convention of Pennec (2019) Eq. (1). In this convention a space form of constant curvature \(K\) has
\[
R(X,Y)Z=K\{\langle Y,Z\rangle X-\langle X,Z\rangle Y\},
\qquad
\kappa(X,Y)=\frac{\langle R(X,Y)Y,X\rangle}{|X|^2|Y|^2-\langle X,Y\rangle^2}=K .
\tag{C1.1}
\]
This normalisation is not taken on faith: §1.2 derives it from the source's own displayed distance expansion.

**C2 (base-point direction).** \(x\) is the **old** reference, \(y\) the **new** one. \(w=\log_yx\in T_yM\); \(P=P_{x\to y}:T_xM\to T_yM\) is Levi-Civita transport along the declared unique connecting geodesic; \(\Phi_{x\to y}(v)=\log_y\operatorname{Exp}_xv\); \(c_V(t)=\Phi_{x\to y}(tV)=\log_y\operatorname{Exp}_x(tV)\). All Definition-B1 normal-branch hypotheses of the archived P1-ID-B dossier are inherited verbatim.

**C3 (rank).** "Minimum dynamic rank" is the archived Theorem B5 object: for a finite reset-chain probe supported on a finite configuration, minimum dynamic rank equals the **affine-hull dimension** of the configuration. Every rank claim below is routed through Theorem B5 and Lemma B5.1 of [[P1-ID-B — curved reference change and rigidity]] and inherits their hypotheses (positive invariant probabilities, \(0<\rho<1\), zero noise, two-sided cross-lag orthogonality vacuous).

---

## 2. L-8.1 — the Gavrilov–Pennec expansion: source, hypotheses, translation, and independent verification

### 2.1 Primary source, read verbatim

**Source.** X. Pennec, *Curvature effects on the empirical mean in Riemannian and affine manifolds: a non-asymptotic high concentration expansion in the small-sample regime*, arXiv:1906.07418v1 (18 June 2019), §3.1, **Theorem 2**, attributed there to A. V. Gavrilov, *Algebraic properties of covariant derivative and composition of exponential maps*, Math. Tr. 9(1) (2006) 3–20 (Siberian Adv. Math. 16(3) (2006) 54–70), and A. V. Gavrilov, *The double exponential map and covariant derivation*, Siberian Math. J. 48(1) (2007) 56–61.

**Theorem 2, as printed.** In a torsion-free affine connection manifold, with the double exponential \(\exp_x(v,u)=\exp_{\exp_x(v)}(\Pi^{\exp_x(v)}_xu)\),
\[
h_x(v,u)=\log_x(\exp_x(v,u))
= v+u+\tfrac16R(u,v)v+\tfrac13R(u,v)u
+\tfrac1{24}(\nabla_vR)(u,v)(2v+5u)+\tfrac1{24}(\nabla_uR)(u,v)(v+2u)+O(5).
\tag{2.1}
\]

**Hypotheses printed in the source.**
1. torsion-free affine connection (Pennec §2.3: "In the sequel, all connections are assumed to be symmetric"); a Riemannian Levi-Civita connection is a special case;
2. smooth connection; tensor values on the right are taken **at \(x\)**;
3. \(u,v\) lie in a convex neighbourhood \(U\) of \(x\) in the sense of Pennec §2.1/§2.2 (unique minimal geodesic between any pair, contained in \(U\), depending smoothly on endpoints; Whitehead), so all logs used are single-valued;
4. \(O(5)\) means **polynomial terms of total order \(\ge5\) jointly in \((u,v)\)**, with the explicit order accounting of Pennec §1: \(R(u,v)w\) counts as order 3 and \(\nabla R(u,v)w\) as order 4 for vectors of norm \(\le\varepsilon=\operatorname{diam}U\).

### 2.2 Line-by-line application to C-AUDIT-5 and to the ID-8 statement

Set \(y=\exp_x(v)\), so \(v=\log_xy\), and let \(Z\in T_yM\) with \(u=\Pi^x_yZ=:PZ\). Then \(\exp_x(v,u)=\operatorname{Exp}_y(Z)\), and (2.1) reads, with \(w:=v=\log_xy\),
\[
\log_x\operatorname{Exp}_yZ
= w+PZ+\tfrac16R(PZ,w)w+\tfrac13R(PZ,w)PZ+O(4).
\tag{2.2}
\]
This is **verbatim C-AUDIT-5**, including both coefficients \(\tfrac16,\tfrac13\), the argument order \(R(PZ,w)\cdot\), and the retraction of the older leading \(1/3\). **C-AUDIT-5 is confirmed against the primary source; no correction to the reference audit is required.** The remainder \(O(4)\) is the total-order-\(\ge4\) remainder of hypothesis 4, which is *not* "order 4 in \(Z\) alone"; the first omitted terms are the two \(\nabla R\) terms of (2.1).

Swapping the names \(x\leftrightarrow y\) to the campaign convention C2 (\(w=\log_yx\), \(P:T_xM\to T_yM\), \(V\in T_xM\), \(Z=tV\)) gives exactly the lead's displayed formula:
\[
c_V(t)=\log_y\operatorname{Exp}_x(tV)
= w+t\Big[PV+\tfrac16R(PV,w)w\Big]+t^2\cdot\tfrac13R(PV,w)PV+O(4).
\tag{2.3}
\]
**The lead's transcription is exact.** Note the typing: every term of (2.3) lies in \(T_yM\); the curvature tensor is evaluated at \(y\).

**Convention translation actually required.** The source does *not* fix the sign of \(R\) by an independent normalisation; it prints Eq. (1) and remarks that two conventions exist. The load-bearing translation is therefore made through the source's own downstream display, Pennec Eq. (9):
\[
\operatorname{dist}^2(x_v,x_w)=\|w-v\|^2_x+\tfrac13\langle R(w,v)w,v\rangle_x+O(6).
\tag{2.4}
\]
On the unit sphere with \(v\perp w\), \(|v|=a\), \(|w|=b\), the exact spherical relation \(\cos\rho=\cos a\cos b\) gives, by direct expansion, \(\rho^2=a^2+b^2-\tfrac13a^2b^2+O(6)\). Matching against (2.4) forces \(\langle R(w,v)w,v\rangle=-a^2b^2\) for orthogonal \(v,w\) on the unit sphere, i.e. exactly (C1.1) with \(K=+1\). **Convention (C1) is therefore the source's convention, established from the source's own displayed formula rather than assumed.**

### 2.3 Independent verification of the coefficients \(\tfrac16\) and \(\tfrac13\)

We do not rely on the citation alone. In a space form of constant curvature \(K\), take \(|PV|=1\), \(PV\perp w\), \(|w|=d\). By (C1.1),
\[
R(PV,w)w=K d^2\,PV,\qquad R(PV,w)PV=-K\,w .
\tag{2.5}
\]
So (2.3) predicts
\[
\underbrace{\langle c_V(t),\hat w\rangle}_{\text{radial}}=d\Big(1-\tfrac{K}{3}t^2\Big)+O(4),
\qquad
\underbrace{\langle c_V(t),PV\rangle}_{\text{transverse}}=t\Big(1+\tfrac{K}{6}d^2\Big)+O(4).
\tag{2.6}
\]
Exactly, in the constant-curvature right triangle with legs \(d\) (from \(y\) to \(x\)) and \(t\) (from \(x\) along \(V\)), right angle at \(x\), hypotenuse \(\rho\) and angle \(\theta\) at \(y\):
\[
K=-1:\quad \cosh\rho=\cosh d\cosh t,\quad \cos\theta=\frac{\tanh d}{\tanh\rho},\quad \sin\theta=\frac{\sinh t}{\sinh\rho};
\]
\[
K=+1:\quad \cos\rho=\cos d\cos t,\quad \cos\theta=\frac{\tan d}{\tan\rho},\quad \sin\theta=\frac{\sin t}{\sin\rho},
\]
and \(\langle c_V(t),\hat w\rangle=\rho\cos\theta\), \(\langle c_V(t),PV\rangle=\rho\sin\theta\). Joint Taylor expansion (sympy, `series` in \(t\) then in \(d\), both signs) gives
\[
K=-1:\ \rho\cos\theta=d\Big(1+\tfrac{t^2}{3}\Big)+O(4),\quad \rho\sin\theta=t\Big(1-\tfrac{d^2}{6}\Big)+O(4);
\]
\[
K=+1:\ \rho\cos\theta=d\Big(1-\tfrac{t^2}{3}\Big)+O(4),\quad \rho\sin\theta=t\Big(1+\tfrac{d^2}{6}\Big)+O(4).
\]
Both match (2.6) in both signs. Since at total order 3 the only admissible curvature contraction of type (1 in \(Z\), 2 in \(w\)) is \(R(PZ,w)w\) and the only one of type (2 in \(Z\), 1 in \(w\)) is \(R(PZ,w)PZ\) — \(\nabla R\) terms are order 4 — the two constant-curvature families **pin both coefficients uniquely** given the form of the expansion. The expansion's *form* is cited; its *coefficients* are verified internally.

**Status L-8.1: CITED+APPLIED (form and hypotheses, Pennec 2019 Thm. 2 / Gavrilov 2006–2007) with coefficients INDEPENDENTLY VERIFIED INTERNALLY.** C-AUDIT-5 requires no amendment.

---

## 3. L-8.2 — transversality and the wedge

**Lemma L-8.2.1 (exact transversality).** For every \(X,Y\) in a tangent space, \(\langle R(X,Y)X,X\rangle=0\).
*Proof.* By the pair antisymmetry \(R(X,Y,Z,W)=-R(X,Y,W,Z)\), \(\langle R(X,Y)X,X\rangle=R(X,Y,X,X)=-R(X,Y,X,X)=0\). \(\square\)
Applied with \(X=PV,Y=w\): the quadratic coefficient \(\tfrac13R(PV,w)PV\) of (2.3) is **exactly orthogonal to \(PV\)**, with no smallness hypothesis. **PROVED.**

**Lemma L-8.2.2 (first derivative).** \(c_V'(0)=PV+\tfrac16R(PV,w)w+O(|w|^3)\), and \(\big|c_V'(0)-PV\big|\le\tfrac16\|R_y\|\,|V|\,|w|^2+O(|w|^3)\). Hence there is \(\varepsilon_1(x)>0\) with \(c_V'(0)\ne0\) whenever \(0<|w|<\varepsilon_1\). **PROVED** (multilinearity of \(R\); \(|PV|=|V|\)).

**Lemma L-8.2.3 (collinearity \(\Leftrightarrow\) wedge).** Let \(c\) be \(C^3\) with \(c(0)=w\). Then
\[
\big(c(b)-c(0)\big)\wedge\big(c(-b)-c(0)\big)=2b^3\,c'(0)\wedge c''(0)+O(b^4).
\]
*Proof.* \(c(\pm b)-c(0)=\pm bc'(0)+\tfrac{b^2}2c''(0)\pm\tfrac{b^3}6c'''(0)+O(b^4)\). Wedging and using bilinearity and antisymmetry, the \(b^2\) terms cancel, the \(b^3\) terms give \(bc'\wedge\tfrac{b^2}2c''-\tfrac{b^2}2c''\wedge bc'=b^3c'\wedge c''\) from the first cross pair and an equal contribution from the second, total \(2b^3c'\wedge c''\). \(\square\)
Three points are affinely dependent (collinear) iff that wedge vanishes; so for small \(b\), non-collinearity \(\Leftrightarrow c'(0)\wedge c''(0)\ne0\). **PROVED.** (The lead's guess "\(b^3c'\wedge c''+O(b^4)\)" is right up to the factor 2; the factor is immaterial to every consumer but is recorded for exactness.)

**Lemma L-8.2.4 (wedge nonvanishing).** With \(c''_V(0)=\tfrac23R(PV,w)PV\),
\[
c_V'(0)\wedge c_V''(0)=\tfrac23\Big[PV\wedge R(PV,w)PV\Big]+\tfrac19\Big[R(PV,w)w\wedge R(PV,w)PV\Big].
\]
The first bracket has norm \(|PV|\cdot\tfrac23|R(PV,w)PV|\) exactly, by L-8.2.1. The second is bounded by \(\tfrac19\|R\||V||w|^2\cdot|R(PV,w)PV|\). Hence if \(R(PV,w)PV\ne0\) and \(|w|<\varepsilon_2:=\min\{\varepsilon_1,\ (6\|R_y\|)^{-1/2}\}\cdot\) (with \(\|R_y\|\) the operator norm of the curvature tensor at \(y\)), then \(c_V'(0)\wedge c_V''(0)\ne0\). **PROVED.**

**Lemma L-8.2.5 (curvature sufficiency, and the correction).**
\[
\kappa(PV,w)\ne0\ \Longrightarrow\ R(PV,w)PV\ne0,
\]
because \(\langle R(PV,w)PV,w\rangle=-\langle R(PV,w)w,PV\rangle=-\kappa(PV,w)\cdot\big(|PV|^2|w|^2-\langle PV,w\rangle^2\big)\ne0\).
**The converse is false.** In \(M=S^2(1)\times H^2(-1)\), take \(V=(V_1,V_2)\), \(w=(w_1,w_2)\) with \(V_i\perp w_i\) and \(|V_i|=|w_i|=1/\sqrt2\). Then \(\kappa(V,w)=\tfrac14-\tfrac14=0\) while \(R(V,w)V=(-\tfrac12w_1,\ \tfrac12w_2)\ne0\). **PROVED.**
Consequently **the sharp criterion is \(R(PV,w)PV\ne0\)** and nonzero sectional curvature is sufficient only.
**Where the correction does and does not bite.** If all sectional curvatures of \(M\) have one sign — true for Hadamard (AIRM), for nonnegatively curved BW, and for products of round spheres — then \(\kappa(PV,w)=0\iff R(PV,w)PV=0\), because \(\kappa=0\) forces every factorwise contribution to vanish. So the correction **does not affect any geometry the project uses**; it affects only the general statement.

**Status L-8.2: PROVED INTERNALLY (all five sublemmas).**

---

## 4. ID-8 — general theorem

**Theorem ID-8 (curvature class of reference-dependent dynamic rank).** Let \(M\) be smooth Riemannian, \(x\ne y\) in a common normal configuration (Definition B1), \(w=\log_yx\), \(P=P_{x\to y}\), \(V\in T_xM\setminus\{0\}\). Let \(C_b=\{\operatorname{Exp}_x(-bV),\,x,\,\operatorname{Exp}_x(bV)\}\), whose \(\log_x\)-images \(\{-bV,0,bV\}\) have affine dimension 1, and let the probe be a three-state reset chain with positive invariant probabilities on \(C_b\).

1. **(Exact.)** For all sufficiently small \(b>0\), the minimum dynamic rank of the probe at \(y\) is 2 (inflated from 1 at \(x\)) **iff** \(c_V'(0)\wedge c_V''(0)\ne0\).
2. **(Curvature criterion.)** There is \(\varepsilon_2(x,y)>0\) such that if \(0<|w|<\varepsilon_2\) and \(R(PV,w)PV\ne0\), then (1) holds. In particular it holds whenever the sectional curvature \(\kappa(\operatorname{span}\{PV,w\})\ne0\).
3. **(Correction to the lead's hypothesis.)** \(\kappa\ne0\) is sufficient, not necessary; the sharp criterion is \(R(PV,w)PV\ne0\). On one-signed-curvature manifolds (all project geometries) the two agree.
4. **(Not a small-\(|w|\) phenomenon.)** §5 and §6 settle the two applied geometries **exactly, for all admissible displacements**, without any smallness in \(|w|\) or \(b\).

*Proof.* (1) is Theorem B5/Lemma B5.1 (rank \(=\) affine-hull dimension of the transformed configuration) composed with L-8.2.3. (2) is L-8.2.4 + L-8.2.5 with (2.3). (3) is L-8.2.5. (4) is §5, §6. \(\square\)

**Classification of the failure.** Not cut-locus-specific (AIRM has no cut locus; the BW cone has none between full-rank points), not compactness-specific, not completeness-specific (AIRM is complete), not sign-specific (it occurs at \(K>0\) and \(K<0\) alike), not a nonunique-mean, deterministic-trend, or coloured-noise artefact. It is **curvature-specific**, and the strongest correction that removes exactly the responsible feature is: *rigidity holds precisely on configurations for which \(R(PV,w)PV=0\) for every direction \(V\) actually charged* — which is realised by radial/common-geodesic supports and by totally geodesic flats, and, in BW, by the commuting subcone (§5.4). No further nontrivial correction exists at the infinitesimal level, by L-8.5.

**Status ID-8: PROVED INTERNALLY, with the lead's candidate REFORMULATED (implication kept, criterion sharpened).**

---

## 5. L-8.3 — exact Bures–Wasserstein computation on \({\rm SPD}(2)\)

### 5.1 Geometry, and why there is no cut locus to blame

\(M={\rm SPD}(m)\) full rank, free quotient \(\pi(L)=LL^\top\), \(L\in GL(m)\), \(L\sim LQ\), \(Q\in O(m)\), Frobenius lift metric, BW base metric (the file [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]] §1 representation). Facts used:
\[
\operatorname{Exp}_A(U)=A+U+L_A[U]\,A\,L_A[U],\quad L_A[U]A+AL_A[U]=U;\qquad
\operatorname{Exp}_I(U)=(I+U/2)^2,\quad \operatorname{Log}_I(B)=2(B^{1/2}-I).
\tag{5.1}
\]
Since \(A\succ0\), the Sylvester operator \(L\mapsto LA+AL\) is invertible on \({\rm Sym}(m)\), so \(L_A[U]\) is **unique**.

**Lemma B8-0 (unique log between full-rank points; no cut locus).** For \(A\succ0\), \(B\succeq0\), the BW distance equals \(W_2(N(0,A),N(0,B))\), and \(N(0,A)\) is absolutely continuous, hence vanishes on small sets in the sense of Agueh–Carlier Definition 3.2. By Agueh–Carlier Proposition 3.3 (Brenier/McCann), the optimal plan is unique and is the graph of \(\nabla\varphi\) with \(\varphi\) convex; in the Gaussian case \(\nabla\varphi=T=A^{-1/2}(A^{1/2}BA^{1/2})^{1/2}A^{-1/2}\succeq0\). The unique \(W_2\)-geodesic is \(t\mapsto((1-t)I+tT)A((1-t)I+tT)\), and it stays full rank when \(T\succ0\). Hence \(\log_A\) is **single-valued on the whole open cone** and
\[
\operatorname{Log}_A(B)=(T-I)A+A(T-I).
\tag{5.2}
\]
**Status: CITED+APPLIED** (Agueh–Carlier 2011 Def. 3.2, Prop. 3.3, read verbatim from the primary text) **+ PROVED INTERNALLY** (the Gaussian specialisation and (5.2), by direct verification: with \(S=T-I\), \(\operatorname{Exp}_A(SA+AS)=A+SA+AS+SAS=TAT=B\)).
*Consequence for the audit:* the BW counterexample below cannot be dismissed as a cut-locus artefact. The BW boundary is rank loss, not a cut locus (consistent with BW-FIXED-MARGIN §7).

### 5.2 The exact configuration

Take the **new** reference \(y=I\), the **old** base \(x=\operatorname{diag}(a,1)\) with \(a=s^2>0\), \(s\ne1\), and \(V=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).

**Step 1 (Sylvester solutions, exact).** For diagonal \(x\), \((Lx+xL)_{ij}=L_{ij}(x_i+x_j)\), so
\[
L:=L_x[V]=\frac{V}{1+a},\qquad
W:=LxL=\frac{VxV}{(1+a)^2}=\frac{\operatorname{diag}(1,a)}{(1+a)^2},
\]
\[
Y:\ Yx^{1/2}+x^{1/2}Y=V\ \Longrightarrow\ Y=\frac{V}{1+\sqrt a}=\frac{V}{1+s},\qquad
Y^2=\frac{I}{(1+s)^2}.
\tag{5.3}
\]
(Every identity is a one-line matrix multiplication; \(VxV=\operatorname{diag}(1,a)\) and \(V^2=I\).) So
\[
W-Y^2=\operatorname{diag}\!\Big(\tfrac1{(1+s^2)^2}-\tfrac1{(1+s)^2},\ \tfrac{s^2}{(1+s^2)^2}-\tfrac1{(1+s)^2}\Big).
\tag{5.4}
\]
Its \((1,1)\) entry vanishes iff \((1+s)^2=(1+s^2)^2\) iff \(1+s=1+s^2\) (both positive) iff \(s=1\). **Hence \(W\ne Y^2\) for every \(a\ne1\).**

**Step 2 (second-order Sylvester step).** \(\gamma(t)=\operatorname{Exp}_x(tV)=x+tV+t^2W\); writing \(\gamma(t)^{1/2}=x^{1/2}+tY+t^2Z+O(t^3)\) and squaring gives, at order \(t\), \(Yx^{1/2}+x^{1/2}Y=V\) (already used), and at order \(t^2\),
\[
x^{1/2}Z+Zx^{1/2}=W-Y^2 .
\tag{5.5}
\]
Because \(x^{1/2}\succ0\), (5.5) has a **unique** solution, which since \(W-Y^2\) is diagonal is
\[
Z=\operatorname{diag}\Big(\tfrac{(W-Y^2)_{11}}{2s},\ \tfrac{(W-Y^2)_{22}}{2}\Big)
=\frac{1}{2(1+s)^2(1+s^2)^2}\operatorname{diag}\big(-(s-1)(s^2+s+2),\ (s-1)(2s^2+s+1)\big).
\tag{5.6}
\]
\(Z\ne0\) for every \(s\ne1\). Since \(Y\) is off-diagonal and \(Z\) is diagonal, \(Y\wedge Z\ne0\) whenever \(Z\ne0\), and by L-8.2.3 the leading collinearity defect is \(2b^3\,Y\wedge Z\ne0\).

**Collinearity criterion in the required form.** \(\operatorname{Log}_I\) is affine in \(B^{1/2}\), so \(\{\operatorname{Log}_I\gamma(-b),\operatorname{Log}_I\gamma(0),\operatorname{Log}_I\gamma(b)\}\) is collinear in \(T_I M\) iff \(\{\gamma(-b)^{1/2},x^{1/2},\gamma(b)^{1/2}\}\) is collinear in \({\rm Sym}(2)\). To second order this is \(Z\parallel Y\), i.e. \(Z=0\), i.e. \(W=Y^2\) — **the equivalence asserted in the lead's L-8.3 is confirmed**, with \(W\ne Y^2\) for every \(a\ne1\).

### 5.3 The computation done **exactly in \(b\)** (no truncation, no remainder to bound)

For \(2\times2\) \(M\succ0\): \(M^{1/2}=(M+\sqrt{\det M}\,I)/\sqrt{\operatorname{tr}M+2\sqrt{\det M}}\).

\[
\gamma(t)=\begin{pmatrix}a+\tfrac{t^2}{(1+a)^2}&t\\[1mm] t&1+\tfrac{at^2}{(1+a)^2}\end{pmatrix},
\qquad
\operatorname{tr}\gamma(t)=(1+a)+\frac{t^2}{1+a},
\]
\[
\det\gamma(t)=a\Big(1-\frac{t^2}{(1+a)^2}\Big)^{2},
\qquad
\operatorname{tr}\gamma+2\sqrt{\det\gamma}=(1+s)^2+\frac{t^2(1-s)^2}{(1+s^2)^2}=:N(t)^2 .
\tag{5.7}
\]
(All three identities verified symbolically; \(\det\gamma=a(1-t^2/(1+a)^2)^2\) also follows structurally from the lift \(\gamma(t)=\pi\big((I+tL)x^{1/2}\big)\) with \(\operatorname{spec}(L)=\{\pm(1+a)^{-1}\}\).)

Put \(u:=t^2/(1+s^2)^2\). Then, **exactly**,
\[
\gamma(t)^{1/2}=\frac1{N(t)}
\begin{pmatrix}
s(1+s)+u(1-s) & t\\[1mm]
t & (1+s)-su(1-s)
\end{pmatrix}
=:\frac1{N(t)}\begin{pmatrix}P(t)&t\\ t&R(t)\end{pmatrix},
\qquad
N(t)=\sqrt{(1+s)^2+u(1-s)^2}.
\tag{5.8}
\]
At \(t=0\): \(N=1+s\), \(P=s(1+s)\), \(R=1+s\), giving \(\gamma(0)^{1/2}=\operatorname{diag}(s,1)=x^{1/2}\). ✓ (Formula (5.8) was checked against `scipy.linalg.sqrtm` at several \((s,b)\); the identity \(\gamma^{1/2}\gamma^{1/2}=\gamma\) is exact by construction.)

**Exact collinearity theorem.** Write, in the coordinates \((E_{11},E_{22},\text{off-diagonal coefficient})\) on \({\rm Sym}(2)\),
\[
\alpha(b):=\frac{P(b)}{N(b)}-s,\qquad
\beta(b):=\frac{R(b)}{N(b)}-1,\qquad
c(b):=\frac{b}{N(b)}\ne0 .
\]
Then \(\gamma(\pm b)^{1/2}-x^{1/2}=(\alpha,\beta,\pm c)\), and
\[
\big(\gamma(b)^{1/2}-x^{1/2}\big)\times\big(\gamma(-b)^{1/2}-x^{1/2}\big)=(-2\beta c,\ 2\alpha c,\ 0),
\qquad\text{norm}=2c\sqrt{\alpha^2+\beta^2}.
\tag{5.9}
\]
Hence, **exactly and for every \(b\ne0\) in the admissible range**,
\[
\{\gamma(-b)^{1/2},\ x^{1/2},\ \gamma(b)^{1/2}\}\ \text{collinear}
\iff \alpha(b)=\beta(b)=0 .
\]
And \(\beta=0\) means \(N=R\), whence \(\alpha=0\) means \(P=sN=sR\), i.e.
\[
s(1+s)+u(1-s)=s\big[(1+s)-su(1-s)\big]\iff u(1-s)(1+s^2)=0\iff s=1 .
\]

> **Theorem L-8.3 (exact BW non-collinearity).** For every \(a>0\) with \(a\ne1\) and every \(b\) with \(0<|b|<1+a\), the three points \(\gamma(-b)^{1/2},\ x^{1/2},\ \gamma(b)^{1/2}\) are **not** collinear, with exact defect \(2c(b)\sqrt{\alpha(b)^2+\beta(b)^2}>0\). For \(a=1\) they are collinear for every \(b\). **PROVED INTERNALLY, exactly in \(b\); nothing is truncated and no remainder needs bounding.**

**Order-\(b^2\) defect, and its consistency.** As \(b\to0\), \(\alpha(b)=Z_{11}b^2+O(b^4)\), \(\beta(b)=Z_{22}b^2+O(b^4)\), \(c(b)=b/(1+s)+O(b^3)\), so
\[
\text{defect}(b)=2b^3\,\frac{\sqrt{Z_{11}^2+Z_{22}^2}}{1+s}+O(b^5)=2b^3\,|Y\wedge Z|+O(b^5),
\]
exactly the L-8.2.3 prediction with \(Z\) from (5.6). (Checked numerically at \(s\in\{0.5,2,3\}\), \(b\) down to \(0.05\): ratios agree to 4–6 digits and converge.)

**Admissible \(b\)-range, stated explicitly.** \(\det\gamma(t)=a(1-t^2/(1+a)^2)^2>0\) and \(\operatorname{tr}\gamma(t)>0\), so \(\gamma(t)\succ0\) iff \(|t|\ne1+a\); and the BW geodesic segment from \(x\) is the minimising one precisely while the optimal map \(T_t=I+tL=I+tV/(1+a)\) is positive definite, i.e. \(|t|<1+a\). Therefore
\[
\boxed{\ 0<|b|<1+a\ }
\]
is the exact admissible range, on which \(\gamma(\pm b)\succ0\), \(\operatorname{Log}_x\gamma(\pm b)=\pm bV\) (from (5.2) with \(T=I\pm bL\)), and \(\operatorname{Log}_I\gamma(\pm b)=2(\gamma(\pm b)^{1/2}-I)\) are all unique.

### 5.4 The commuting/diagonal branch is **exactly** rigid

**Lemma B8-1 (exact commuting rigidity).** If \(Vx=xV\) then \(L_x[V]=\tfrac12Vx^{-1}\), \(W=\tfrac14V^2x^{-1}\), and
\[
\gamma(t)=\operatorname{Exp}_x(tV)=\big(x^{1/2}+\tfrac t2Vx^{-1/2}\big)^2,\qquad
\gamma(t)^{1/2}=x^{1/2}+\tfrac t2Vx^{-1/2},
\]
so \(\operatorname{Log}_I\gamma(t)=2(x^{1/2}-I)+tVx^{-1/2}\) is **exactly affine in \(t\)**. Also \(Y=\tfrac12Vx^{-1/2}\) and \(Y^2=\tfrac14V^2x^{-1}=W\), so the second-order criterion agrees. **PROVED** (direct expansion; positivity of \(x^{1/2}+\tfrac t2Vx^{-1/2}\) is the admissible range).

**Lemma B8-2 (the diagonal BW subcone is a Euclidean orthant).** Let \(\mathcal D=\{\operatorname{diag}(\lambda_1,\dots,\lambda_m):\lambda_i>0\}\). Its BW-horizontal lift is the linear space of diagonal matrices (diagonal \(L,K\) satisfy \(LK^\top=KL^\top\)), a totally geodesic flat of \((GL(m),\|\cdot\|_F)\); hence \(\mathcal D\) is totally geodesic in BW. Intrinsically, \(\langle U,U\rangle_{{\rm BW},A}=\tfrac14\operatorname{tr}(A^{-1}U^2)=\sum_i\frac{u_i^2}{4\lambda_i}\), and the substitution \(\lambda_i=r_i^2\) turns it into \(\sum_i dr_i^2\): \((\mathcal D,d_{\rm BW})\) is **isometric to the Euclidean orthant \(\mathbb R_{>0}^m\)** via \(A\mapsto A^{1/2}\), and \(\operatorname{Log}_I\) is exactly the affine chart of that orthant. **PROVED.**
*Consequence.* The fixed-eigenbasis (commuting) BW branch is exactly the "common simply connected totally geodesic flat" producer of Theorem B4. It is the **only** rigid branch in BW other than radial supports, by ID-8(2)–(3).

### 5.5 Lifting to \({\rm SPD}(m)\), \(m\ge3\)

**Lemma B8-3 (block embedding is totally geodesic, both metrics).** \(\iota:A_0\mapsto\operatorname{diag}(A_0,I_{m-2})\).
*BW:* for \(A=\iota(A_0)\), \(U=\iota_*(U_0)=\operatorname{diag}(U_0,0)\), \(L_A[U]=\operatorname{diag}(L_{A_0}[U_0],0)\) (block-diagonal Sylvester, unique), so \(\operatorname{Exp}_A(tU)=\iota(\operatorname{Exp}_{A_0}(tU_0))\).
*AIRM:* \(\operatorname{Exp}_A(tU)=A^{1/2}\exp(tA^{-1/2}UA^{-1/2})A^{1/2}\) is block-diagonal with the second block \(=I\).
Both \(\iota\) are isometric onto their images for the corresponding metrics, and \(\operatorname{Log}_{\iota(I_2)}\) restricts. **PROVED.**
Therefore the \({\rm SPD}(2)\) counterexamples of §5 and §6 lift verbatim to \({\rm SPD}(m)\) for **every** \(m\ge2\), in both geometries.

### 5.6 Complete counterexample to the §5 standard (BW)

| Standard item | Content |
|---|---|
| **Manifold and metric** | \(M={\rm SPD}(2)\) full rank, Bures–Wasserstein metric, as in BW-FIXED-MARGIN §1. Nonnegatively curved; incomplete (boundary = rank loss); **no cut locus between full-rank points** (Lemma B8-0). Lifts to \({\rm SPD}(m)\), \(m\ge2\), by Lemma B8-3. |
| **Parameters** | \(a=s^2>0\), \(a\ne1\); \(x=\operatorname{diag}(a,1)\); \(V=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\); \(0<b<1+a\); \(0<\rho<1\). |
| **Complete stochastic construction** | \(F_t\in\{-b,0,b\}\) is the stationary three-state reset chain (B5.2) with uniform invariant law \(\pi=(\tfrac13,\tfrac13,\tfrac13)\) and \(\Pr(F_t=j\mid F_{t-1}=i)=\rho1_{\{i=j\}}+(1-\rho)\pi_j\). Set \(Y^x_t=F_tV\in T_x M\) and \(X_t=\operatorname{Exp}_x(Y^x_t)=\gamma(F_t)\). |
| **Normal-neighbourhood / support** | Support \(\{\gamma(-b),x,\gamma(b)\}\subset{\rm SPD}(2)\), all \(\succ0\) since \(|b|<1+a\). By Lemma B8-0 both \(\operatorname{Log}_x\) and \(\operatorname{Log}_I\) are single-valued on the whole open cone; \(\operatorname{Log}_x\gamma(\pm b)=\pm bV\), \(\operatorname{Log}_I\gamma(\pm b)=2(\gamma(\pm b)^{1/2}-I)\). Bounded support. |
| **Fréchet mean** | The marginal law \(Q=\tfrac13(\delta_{\gamma(-b)}+\delta_x+\delta_{\gamma(b)})\) has \(\int\operatorname{Log}_x\Sigma\,dQ=\tfrac13(-bV+0+bV)=0\), hence \(\nabla F_Q(x)=0\) (§9.1 (9.4)); \(Q\) charges the full-rank cone, so by **L-9.R2.1** \(F_Q\) is strictly convex on the open cone and by **L-9.R1.1–R1.2** the minimiser exists and is full rank. Therefore \(x\) is the **unique** BW Fréchet mean of \(Q\). Nevertheless the construction uses \(x\) and \(y=I\) only as *weakened references* in the ID-4 sense; the uniqueness statement removes the "nonunique mean" escape. |
| **Factor rank, loading, factor law, noise law** | Rank \(r=1\) at \(x\); loading \(A:\mathbb R\to T_xM\), \(A\mathfrak a=\mathfrak aV\); factor \(f_t=F_t\), \(\mathbb Ef_t=0\), \(\operatorname{Cov}(f_t,f_{t-h})=\rho^h\cdot\tfrac{2b^2}3\); noise \(\delta_t\equiv0\) (independent, temporally white, two-sided cross-lag orthogonal, trivially). |
| **Temporal dependence / spectral properties** | Geometric \(\alpha\)-mixing with rate \(\rho^h\); bounded; strictly stationary; \(0<\rho<1\) so no zero-frequency spectral atom and no deterministic trend. |
| **Every assumption of the attacked claim** | The attacked claim is "fixed minimum dynamic rank is preserved under a compatible weakened-reference change". Assumptions verified: common normal configuration (Lemma B8-0), unique logs at both references, exact rank-one affine factor representation at \(x\) with white (zero) noise and two-sided cross-lag orthogonality, unique marginal Fréchet mean, bounded support, geometric mixing, nonzero ordinary persistence. |
| **Equality of the observational object** | The observation path law is one and the same; by Theorem B2 the tangent coordinate laws at \(x\) and at \(I\) are exact pushforwards of each other under \(\Phi_{x\to I}\), pointwise at every time. |
| **Explicit violation** | Let \(G_t=\operatorname{Log}_IX_t\). Write \(\alpha,\beta,c\) as in §5.3 and use the \((E_{11},E_{22},V)\) coordinates. Then by Lemma B5.1, \(\Gamma_G(h)=\rho^h\Sigma_G\) for \(h\ge1\) with (Frobenius inner product on \({\rm Sym}(2)\)) \[\Sigma_G=\tfrac89\,q\otimes q+\tfrac{8}{3}c^2\,V\otimes V,\qquad q=\alpha E_{11}+\beta E_{22},\] whose nonzero eigenvalues are \(\tfrac89(\alpha^2+\beta^2)>0\) and \(\tfrac{16}3c^2>0\). Hence \(\operatorname{rank}\Sigma_G=2\) exactly, so the minimum dynamic rank at \(I\) is **2**, while at \(x\) it is **1**. Any proposed representation \(G_t=m'+A'f'_t+\delta'_t\) with scalar factor, white \(\delta'\), and both cross-lag directions zero would force every nonzero-lag covariance to have rank \(\le1\) — contradiction. |
| **Responsible mathematical feature** | \(W\ne Y^2\), i.e. \(Z\ne0\) in (5.6): the second-order Sylvester defect of the BW square root along a non-commuting geodesic. Equivalently, nonzero BW sectional curvature on \(\operatorname{span}\{PV,w\}\), realised as failure of \(x\) and \(V\) to commute. |
| **Classification** | **curvature-specific.** Not cut-locus-specific (no cut locus), not completeness-specific (the whole configuration is interior and bounded away from the boundary), not convention-induced, not sign-specific. |
| **Strongest correction removing exactly that feature** | Rigidity holds iff the entire charged direction set commutes with \(x\), i.e. iff the support lies in a fixed-eigenbasis subcone (Lemma B8-2: a Euclidean orthant, hence a common totally geodesic flat), or on one geodesic through \(x\) and the new reference. By ID-8(2)–(3) no further infinitesimal escape exists. |

**Status L-8.3: PROVED INTERNALLY, exactly in \(b\).**

---

## 6. L-8.4 — exact AIRM / Hadamard computation

Both routes are executed exactly; they are mutually validating.

### 6.1 Route (b) — direct \({\rm SPD}(2)\) AIRM computation, exact for all \(b\in\mathbb R\)

AIRM: \(\langle U,U'\rangle_A=\operatorname{tr}(A^{-1}UA^{-1}U')\), \(\operatorname{Exp}_A(U)=A^{1/2}\exp(A^{-1/2}UA^{-1/2})A^{1/2}\), \(\log_AB=A^{1/2}\log(A^{-1/2}BA^{-1/2})A^{1/2}\), \(\log_IB=\log B\). \(({\rm SPD}(m),\text{AIRM})\) is a **complete simply connected nonpositively curved (Hadamard)** manifold, so \(\log\) is globally defined and single-valued: **no cut locus, no incompleteness, no branch choice.**

Take \(y=I\), \(x=\operatorname{diag}(s^2,1)\) with \(s>0\), \(s\ne1\), \(V=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\). Since \(x^{-1/2}Vx^{-1/2}=V/s\) and \(\exp(\tau V)=\cosh\tau\,I+\sinh\tau\,V\),
\[
\gamma(t)=\operatorname{Exp}_x(tV)=\begin{pmatrix}s^2\cosh(t/s)&s\sinh(t/s)\\ s\sinh(t/s)&\cosh(t/s)\end{pmatrix},
\qquad
\det\gamma(t)\equiv s^2 .
\tag{6.1}
\]
(Verified symbolically and numerically against `expm`.) Write \(D=\operatorname{diag}(1,-1)\) and use the basis \(\{I,D,V\}\) of \({\rm Sym}(2)\). Let \(\lambda_\pm(t)=se^{\pm\varphi(t)}\) be the eigenvalues of \(\gamma(t)\); then \(\lambda_++\lambda_-=(1+s^2)\cosh(t/s)\), so
\[
\cosh\varphi(t)=\cosh\varphi_0\cdot\cosh(t/s),\qquad \varphi_0:=\varphi(0)=|\log s| .
\tag{6.2}
\]
For a symmetric \(2\times2\) matrix, \(\log M=\tfrac12\log(\det M)\,I+\kappa\,(M-\tfrac12\operatorname{tr}M\,I)\) with \(\kappa=\frac{\log\lambda_+-\log\lambda_-}{\lambda_+-\lambda_-}=\frac{\varphi}{s\sinh\varphi}\). Substituting (6.1),
\[
\log\gamma(t)=\log s\cdot I\;+\;g(t)\,D\;+\;\nu(t)\,V,
\qquad
g(t)=\frac{s^2-1}{s^2+1}\,\varphi(t)\coth\varphi(t),
\qquad
\nu(t)=\kappa(t)\,s\sinh(t/s).
\tag{6.3}
\]
Two exact structural facts:
* the \(I\)-component is **constant** \(=\log s\) for all \(t\) (because \(\det\gamma\equiv s^2\));
* \(g\) is **even** in \(t\), \(\nu\) is **odd** in \(t\), and \(g(0)=\log s\) (check: \(s>1\Rightarrow\varphi_0=\log s\), \(\coth\varphi_0=\frac{s^2+1}{s^2-1}\); \(s<1\Rightarrow\varphi_0=-\log s\), \(\coth\varphi_0=\frac{1+s^2}{1-s^2}\); both give \(g(0)=\log s\)). ✓ so \(\log\gamma(0)=\log x\).

Hence the three points \(\log\gamma(-b),\log\gamma(0),\log\gamma(b)\) have coordinates \((\log s,\,g(b),\,-\nu(b))\), \((\log s,\,\log s,\,0)\), \((\log s,\,g(b),\,\nu(b))\) with \(\nu(b)\ne0\); exactly as in §5.3 they are collinear **iff \(g(b)=\log s\)**.

> **Theorem L-8.4b (exact AIRM non-collinearity).** \(\varphi\coth\varphi\) is strictly increasing on \((0,\infty)\) (derivative \(=\frac{\sinh2\varphi-2\varphi}{2\sinh^2\varphi}>0\)), and by (6.2) \(\varphi(b)>\varphi_0\) for every \(b\ne0\). Therefore, for every \(s\ne1\) and every \(b\ne0\),
> \[
> \Delta_{\rm AIRM}(b):=g(b)-\log s=\frac{s^2-1}{s^2+1}\Big[\varphi(b)\coth\varphi(b)-\varphi_0\coth\varphi_0\Big]\ \ne 0,
> \]
> with \(\Delta>0\) for \(s>1\) and \(\Delta<0\) for \(s<1\). The three points are **never** collinear. For \(s=1\) the factor \(\frac{s^2-1}{s^2+1}\) vanishes and they are always collinear. **PROVED INTERNALLY, exactly in \(b\), for all \(b\in\mathbb R\) (AIRM is complete: there is no admissibility restriction at all).**

(Numeric sanity check: \(g(b)\) from `logm` agrees with the closed form to 10 digits at \((s,b)\in\{(2,0.5),(2,3),(0.4,0.8),(1.05,0.1)\}\), and vanishes identically at \(s=1\).)

**Commuting rigidity in AIRM.** If \(Vx=xV\) then \(\operatorname{Exp}_x(tV)=x\exp(tx^{-1}V)\) with \(x^{-1}V\) symmetric and commuting with \(x\), so \(\log_I\gamma(t)=\log x+t\,x^{-1}V\) is exactly affine. Same rigid branch as BW.

### 6.2 Route (a) — hyperbolic plane, exact, and verification/correction of the lead's derivative

**Setup.** \(H^2\) of curvature \(-1\); \(x,y\) at distance \(d>0\); \(\gamma\) the unit-speed geodesic through \(x\) perpendicular to \(xy\). Let \(\rho=d(y,\gamma(b))\) and \(\theta\) the angle at \(y\) between \(yx\) and \(y\gamma(b)\). Since \(H^2\) is Hadamard, \(\log_y\) is a global diffeomorphism, and \(\log_y\gamma(\pm b)\) have polar coordinates \((\rho,\pm\theta)\), \(\log_yx=(d,0)\). The three points are collinear iff the vertical line at abscissa \(\rho\cos\theta\) contains \((d,0)\), i.e.
\[
\text{collinear}\iff \rho\cos\theta=d .
\]
Hyperbolic right-triangle relations (right angle at \(x\); legs \(d\) and \(b\); hypotenuse \(\rho\); \(\theta\) opposite the leg \(b\)):
\[
\cosh\rho=\cosh d\cosh b,\qquad \cos\theta=\frac{\tanh d}{\tanh\rho}.
\tag{6.4}
\]

> **Theorem L-8.4a (exact \(H^2\) non-collinearity).** For every \(d>0\) and every \(b\ne0\),
> \[
> \rho\cos\theta-d=\tanh d\cdot\frac{\rho}{\tanh\rho}-d\;>\;0 .
> \]
> *Proof.* \(\rho\mapsto\rho/\tanh\rho\) is strictly increasing on \((0,\infty)\) (derivative \(=\frac{\sinh2\rho-2\rho}{2\sinh^2\rho}>0\)), and (6.4) gives \(\cosh\rho>\cosh d\), i.e. \(\rho>d\). Hence \(\tanh d\cdot\frac{\rho}{\tanh\rho}>\tanh d\cdot\frac{d}{\tanh d}=d\). \(\square\)
> The sign is **positive**: in the \(\log_y\) chart the perpendicular geodesic bends **away** from \(y\). **PROVED, exactly, globally in \((d,b)\).**

**Verification of the lead's derivative.** 
\[
\frac{d}{d\rho}\Big[\rho\frac{\tanh d}{\tanh\rho}\Big]_{\rho=d}
=\tanh d\Big[\frac1{\tanh d}-\frac{d}{\sinh^2 d}\Big]
=1-\frac{d}{\sinh d\cosh d}
=1-\frac{2d}{\sinh(2d)}\;>\;0 ,
\]
since \(\sinh(2d)>2d\) for \(d>0\). **The lead's calculation is verified verbatim, including the strict positivity.** Note it is \(O(d^2)\) as \(d\to0\) (\(=\tfrac23d^2+O(d^4)\)) — the deviation is a genuine curvature effect that switches off as \(|w|\to0\), as ID-8 predicts.

**Exact second-order-in-\(b\) defect.** From (6.4), \(\rho(0)=d\), \(\rho'(0)=0\), \(\rho''(0)=\coth d\), so
\[
\rho\cos\theta-d=\Big(1-\frac{2d}{\sinh 2d}\Big)\coth d\cdot\frac{b^2}{2}+O(b^4),
\]
which for small \(d\) equals \(\tfrac13db^2+O(\cdot)\), matching the ID-8/GP prediction \(d(1-\tfrac K3b^2)\) at \(K=-1\). (Numeric check at \(d\in\{0.1,0.5,1,2\}\), \(b\in\{0.01,0.1,0.5\}\): exact defect vs. the displayed second-order formula agrees to 4–6 digits and converges as \(b\to0\).)

### 6.3 The embedding \(H^2\hookrightarrow({\rm SPD}(2),\text{AIRM})\): statement, total geodesy, and curvature normalisation

**Lemma B8-4 (totally geodesic determinant leaves).** For \(c>0\) let \(\mathcal S_c=\{A\in{\rm SPD}(m):\det A=c\}\). AIRM geodesics satisfy \(\det\operatorname{Exp}_A(tU)=\det A\cdot e^{t\operatorname{tr}(A^{-1}U)}\), and \(T_A\mathcal S_c=\{U:\operatorname{tr}(A^{-1}U)=0\}\). Hence every geodesic with initial data tangent to \(\mathcal S_c\) stays in \(\mathcal S_c\): **\(\mathcal S_c\) is totally geodesic.** Moreover \(A\mapsto\lambda A\) is an AIRM isometry, so \(\mathcal S_c\cong\mathcal S_1={\rm SSPD}(m)\). **PROVED.**

**Lemma B8-5 (curvature normalisation, derived, not cited).** For \(m=2\), the configuration of §6.1 lies entirely in \(\mathcal S_{s^2}\) (since \(\det\gamma\equiv s^2\)). Computing AIRM lengths there:
\[
d_{\rm AIRM}(I,\tilde x)=\sqrt2\,\varphi_0,\qquad
d_{\rm AIRM}(\tilde x,\tilde\gamma(b))=\sqrt2\,|b|/s,\qquad
d_{\rm AIRM}(I,\tilde\gamma(b))=\sqrt2\,\varphi(b),
\]
where \(\tilde\cdot=\cdot/s\in{\rm SSPD}(2)\) (eigenvalues of \(\log\tilde\gamma(t)\) are \(\pm\varphi(t)\); \(\|V\|_x=\sqrt{\operatorname{tr}(x^{-1}Vx^{-1}V)}=\sqrt2/s\)). Substituting into (6.2):
\[
\cosh\!\Big(\frac{\rho}{\sqrt2}\Big)=\cosh\!\Big(\frac{d}{\sqrt2}\Big)\cosh\!\Big(\frac{b_{\rm A}}{\sqrt2}\Big),
\]
which is the hyperbolic Pythagoras relation of a space form of curvature \(K\) with \(1/\sqrt{-K}=\sqrt2\). Hence **\({\rm SSPD}(2)\) with AIRM is isometric to the hyperbolic plane of curvature \(-1/2\)**, and \(({\rm SPD}(2),\text{AIRM})\cong\mathbb R\times H^2_{-1/2}\) as a Riemannian product (the \(\mathbb R\) factor is \(\log\det\), orthogonal to the traceless directions at \(I\)). **PROVED INTERNALLY** — the normalisation is *derived* from the exact metric relations of §6.1, not imported.

**Consistency of the two routes.** \(\log_I\tilde\gamma(b)=g(b)D+\nu(b)V\) and \(\log_I\tilde x=\log s\cdot D\). Since \(|D|_F=\sqrt2\), the component of \(\log_I\tilde\gamma(b)\) along the unit vector toward \(\tilde x\) is \(\sqrt2\,g(b)\) (sign \(=\operatorname{sgn}\log s\)), and \(d=\sqrt2|\log s|\). So
\[
\rho\cos\theta-d=\sqrt2\,|\Delta_{\rm AIRM}(b)| ,
\]
and \(\rho\cos\theta=\rho\tanh(d/\sqrt2)/\tanh(\rho/\sqrt2)=\sqrt2\frac{s^2-1}{s^2+1}\varphi(b)\coth\varphi(b)\cdot\operatorname{sgn}(\log s)\), which is exactly (6.3). **Routes (a) and (b) agree identically.**

**Status L-8.4: PROVED INTERNALLY by two exact independent routes; the lead's \(1-2d/\sinh(2d)>0\) is VERIFIED.**

### 6.4 Complete counterexample to the §5 standard (AIRM / Hadamard)

Identical table to §5.6 with these substitutions, all verified: manifold \(({\rm SPD}(2),\text{AIRM})\) — **complete, simply connected, nonpositively curved, no cut locus, globally unique logs**; \(x=\operatorname{diag}(s^2,1)\), \(s\ne1\); \(V\) off-diagonal; \(F_t\in\{-b,0,b\}\) the same reset chain with **no restriction on \(b\)**; \(X_t=\operatorname{Exp}_x(F_tV)\); rank 1 at \(x\); at \(y=I\), \(G_t=\log X_t\) takes three non-collinear values by Theorem L-8.4b, so \(\Gamma_G(h)=\rho^h\Sigma_G\) with \(\operatorname{rank}\Sigma_G=2\) (same computation as §5.6 with \((\alpha,\beta,c)\) replaced by \((0,g(b)-\log s,\nu(b))\) in the \((I,D,V)\) coordinates — note the \(I\)-component is identically zero, which is exactly the flat direction of the product \(\mathbb R\times H^2_{-1/2}\)). Fréchet mean: \(\sum\log_x X_t=-bV+0+bV=0\), and AIRM \(F_Q\) is strictly geodesically convex on a Hadamard manifold, so \(x\) is the **unique** Fréchet mean. Responsible feature: \(\kappa(\operatorname{span}\{PV,w\})=-\tfrac12\ne0\).
**Classification: curvature-specific; explicitly NOT cut-locus-specific, NOT completeness-specific, NOT compactness-specific, NOT sign-specific.**

---

## 7. L-8.5 — converse rigidity

**Theorem L-8.5a (exact fixed-pair criterion).** Fix \(x\ne y\) in a common normal configuration. The following are equivalent:
1. for every \(V\in T_xM\) there is \(b_V>0\) such that \(\Phi_{x\to y}\) preserves the affine dimension of \(\{-bV,0,bV\}\) for all \(0<b<b_V\);
2. \(c'_V(0)\wedge c''_V(0)=0\) for every \(V\), i.e.
\[
\nabla^2(\log_y)_x(V,V)\in\operatorname{span}\big\{D(\log_y)_xV\big\}\qquad\forall V\in T_xM ,
\]
where \(c_V(t)=\log_y\operatorname{Exp}_x(tV)\) is a curve in the fixed vector space \(T_yM\), so \(c'_V(0)=D(\log_y)_xV\) and \(c''_V(0)=\nabla^2(\log_y)_x(V,V)\) are ordinary derivatives.
*Proof.* Immediate from L-8.2.3: (1) says the wedge vanishes for all small \(b\); its \(b^3\)-coefficient is \(2c'\wedge c''\); conversely if \(c'\wedge c''=0\) the affine dimension is preserved only if the higher terms also vanish — but affine dimension **is preserved for small \(b\)** already needs only \(\le\) 1, and inflation to 2 is detected exactly by the wedge, which is real-analytic in \(b\) when \(M\) is analytic and \(C^\infty\) with vanishing 3-jet otherwise; for the direction (2)\(\Rightarrow\)(1) we state the conclusion in the form actually used: (2) is **necessary** for (1) and is the exact obstruction at third order. \(\square\)
**Status: PROVED INTERNALLY as the exact necessary criterion; the reverse implication is stated as third-order only and is not consumed by any claim below.** (This is a deliberate scope lock: the finite-displacement sufficient producers are ID-4's B3/B4, which are exact and do not go through L-8.5.)

**Theorem L-8.5b (curvature converse).** Suppose that for a family of new references \(y_\varepsilon=\operatorname{Exp}_x(-\varepsilon\hat w)\), \(\varepsilon\downarrow0\), condition (1) of L-8.5a holds for every \(\varepsilon\) small. Then
\[
R(V,\hat w)V=0\qquad\text{for every }V\in T_xM .
\]
If this holds for **every** unit \(\hat w\in T_xM\), then all sectional curvatures at \(x\) vanish, and hence \(R_x\equiv0\).
*Proof.* By L-8.5a(2), \(c'_V(0)\wedge c''_V(0)=0\). By (2.3) and L-8.2.1, \(c'_V(0)=PV+O(\varepsilon^2)\) and \(c''_V(0)=\tfrac23R(PV,w_\varepsilon)PV\) with \(w_\varepsilon=\varepsilon\hat w+O(\varepsilon^2)\), and \(R(PV,w_\varepsilon)PV\perp PV\). Therefore
\[
0=|c'\wedge c''|=|PV|\cdot\tfrac23|R(PV,w_\varepsilon)PV|+O(\varepsilon^2\cdot\varepsilon).
\]
Dividing by \(\varepsilon\) and letting \(\varepsilon\downarrow0\) (parallel transport is an isometry converging to the identity) gives \(R(V,\hat w)V=0\). Taking the inner product with \(\hat w\) gives \(\kappa(V,\hat w)=0\); ranging over all \(V,\hat w\) makes every sectional curvature at \(x\) vanish, and a curvature tensor with all sectional curvatures zero is zero. \(\square\)
**Status: PROVED INTERNALLY.**

**Exact relation to ID-4's positive statement.**
* **Common injective geodesic (Theorem B3).** The support lies on one geodesic through \(x\) and \(y\), so \(V\parallel w\) and \(R(PV,w)PV=0\) automatically. **ID-8's criterion is satisfied.**
* **Common simply connected totally geodesic flat \(F\) (Theorem B4).** For \(F\) totally geodesic, the Codazzi equation with vanishing second fundamental form gives \(R^M(X,Y)Z\in TF\) for \(X,Y,Z\in TF\), and the Gauss equation gives \(R^M|_{TF}=R^F=0\). Hence \(R(PV,w)PV=0\) for all \(V\in T_xF\). **ID-8's criterion is satisfied.**
* **Conversely**, L-8.5b says there is **no third infinitesimal producer**: if rigidity holds for all directions and all small displacements, the manifold is flat at \(x\).

> **Verdict on the ID-4 relation.** ID-8 **strengthens** ID-4's negative side (it replaces one \(S^2\) example by a complete curvature criterion plus two exact counterexamples in the geometries the project actually uses) and **infinitesimally matches, but does not imply,** ID-4's positive side. ID-4's B3/B4 are exact finite-displacement theorems; ID-8's positive direction is a *necessary* infinitesimal condition. ID-8 does **not** weaken anything in ID-4. Theorem B5's finite-subset affine-dimension boundary remains the sharp *support-level* characterisation; ID-8 supplies its *curvature-level* explanation.

---

## 8. ID-8 — verdict per geometry, and consequences for APP-FIN and APP-NEURO

| Geometry | Verdict | Evidence |
|---|---|---|
| **General Riemannian** | Rank inflation whenever \(R(PV,w)PV\ne0\) and \(|w|\) small; \(\kappa\ne0\) sufficient. Criterion **sharpened** from the lead's. | §4, L-8.2 |
| **Hadamard (nonpositive curvature)** | **No rescue.** \(H^2\) fails exactly, globally, for all \(d>0,b\ne0\). No cut locus, complete. | §6.2 |
| **AIRM \({\rm SPD}(2)\)** | Inflation for **every** \(a\ne1\) and **every** \(b\ne0\), exactly. Rigid only if \(V\) commutes with \(x\), or the support is radial. | §6.1 |
| **AIRM \({\rm SPD}(m)\), every \(m\ge2\)** | Same, by the totally geodesic block embedding. | Lemma B8-3 |
| **BW \({\rm SPD}(2)\) full rank** | Inflation for **every** \(a\ne1\) and **every** \(0<|b|<1+a\), exactly. | §5.3 |
| **BW \({\rm SPD}(m)\) full rank, every \(m\ge2\)** | Same, by the totally geodesic block embedding. | Lemma B8-3 |
| **Diagonal / fixed-eigenbasis BW subcone** | **RIGID, exactly.** \(Vx=xV\Rightarrow W=Y^2\) and \(\operatorname{Log}_I\gamma(t)\) is exactly affine in \(t\); the subcone is isometric to a Euclidean orthant via \(A\mapsto A^{1/2}\), i.e. a common totally geodesic flat. **The lead's expectation is confirmed, and strengthened from "second order" to "exact".** It is the **only** rigid branch other than radial supports. | Lemmas B8-1, B8-2 |
| **Round sphere \(S^{p-1}\)** | Inflation whenever \(V\not\parallel w\) (ID-4's \(S^2\) case, now with the general criterion). | §4, ID-4 Thm. B6 |
| **Products \(S^{p_1-1}\times\cdots\times S^{p_k-1}\)** | \(R(V,w)V=0\iff\) in **every** factor \(V_i\parallel w_i\) or \(V_i=0\); otherwise inflation. Since all factors have curvature \(+1\), \(\kappa=0\iff R(V,w)V=0\) here, so the lead's phrasing is exact on this class. | L-8.2.5 |
| **Mixed-sign products (e.g. \(S^2\times H^2\))** | The lead's \(\kappa\ne0\) criterion is **strictly weaker** than the truth; use \(R(PV,w)PV\ne0\). | L-8.2.5 |

**Consequence for APP-FIN.** The application is realised covariance matrices of 12 U.S. stocks under BW. Realised covariance matrices do **not** share a fixed eigenbasis and do not lie on a single BW geodesic through any candidate reference. Therefore APP-FIN sits squarely inside the non-rigid class: **any moving-reference comparison changes minimum dynamic rank**, and a rank/factor-number comparison across two references is not an observational-law statement. In particular the "\(\widehat r\) selected at reference \(A\) vs. at reference \(A'\)" comparison is reference-dependent by theorem, not by estimation error.

**Consequence for APP-NEURO.** Whatever the ambient object (SPD connectivity matrices under AIRM or BW, or sphere/product-sphere directional data), all four candidate geometries are covered above and all inflate rank generically. The **only** legitimate escapes are: (i) declare and fix the reference by convention and never compare ranks across references; (ii) verify a fixed-eigenbasis / commuting-support condition (BW) or a common-geodesic condition; (iii) report the rank as a reference-indexed quantity. This is a scope lock on the application map, not an empirical claim about either dataset.

---

## 9. TARGET R1 — existence of the BW Fréchet mean

Throughout, \(d_{\rm BW}(A,B)^2=\operatorname{tr}A+\operatorname{tr}B-2\operatorname{tr}(A^{1/2}BA^{1/2})^{1/2}\) on \({\rm PSD}(m)\), and \(F_Q(A)=\int d_{\rm BW}(A,\Sigma)^2Q(d\Sigma)\).

### 9.0 A variational identity used throughout (registered sublemma B9-a)

**Lemma B9-a.** For \(A,\Sigma\succeq0\),
\[
\operatorname{tr}\big(A^{1/2}\Sigma A^{1/2}\big)^{1/2}=\big\|A^{1/2}\Sigma^{1/2}\big\|_*
=\tfrac12\inf_{T\succ0}\big[\operatorname{tr}(TA)+\operatorname{tr}(T^{-1}\Sigma)\big],
\tag{9.1}
\]
and for \(A,\Sigma\succ0\) the infimum is attained uniquely at \(T_A(\Sigma)=A^{-1/2}(A^{1/2}\Sigma A^{1/2})^{1/2}A^{-1/2}\succ0\), which is exactly the BW optimal map from \(A\) to \(\Sigma\).
*Proof.* "\(\le\)": Hölder for Schatten norms, \(\|XY\|_*\le\|X\|_F\|Y\|_F\), with \(X=A^{1/2}T^{1/2}\), \(Y=T^{-1/2}\Sigma^{1/2}\), \(XY=A^{1/2}\Sigma^{1/2}\), followed by \(\|X\|_F\|Y\|_F\le\tfrac12(\|X\|_F^2+\|Y\|_F^2)=\tfrac12(\operatorname{tr}(TA)+\operatorname{tr}(T^{-1}\Sigma))\). "\(\ge\)" and attainment: \(T\mapsto\operatorname{tr}(TA)+\operatorname{tr}(T^{-1}\Sigma)\) is convex on \(T\succ0\); its stationarity condition \(A=T^{-1}\Sigma T^{-1}\), i.e. \(TAT=\Sigma\), has the unique positive solution \(T_A(\Sigma)\), at which the value is \(2\operatorname{tr}(T_AA)=2\operatorname{tr}((A^{1/2}\Sigma A^{1/2})^{1/2})\). \(\square\)
(Numerically verified to \(10^{-14}\) on random \(4\times4\) pairs.) **PROVED INTERNALLY.**
Two immediate corollaries, both used below:
\[
A\ \longmapsto\ \psi_\Sigma(A):=\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}\ \text{is \emph{concave} on }{\rm PSD}(m)
\tag{9.2}
\]
(an infimum of affine functions of \(A\)), and, by Danskin's theorem at \(A\succ0,\Sigma\succ0\),
\[
\nabla_A\,d_{\rm BW}(A,\Sigma)^2=I-T_A(\Sigma)\qquad\text{(Euclidean gradient on }{\rm Sym}(m)).
\tag{9.3}
\]
Combining (9.3) with \(\operatorname{Log}_A\Sigma=(T_A-I)A+A(T_A-I)\) and the invertibility of the Sylvester operator at \(A\succ0\),
\[
\nabla F_Q(A)=0\iff\int T_A(\Sigma)\,Q(d\Sigma)=I\iff\int\operatorname{Log}_A\Sigma\,Q(d\Sigma)=0\iff A=\int(A^{1/2}\Sigma A^{1/2})^{1/2}Q(d\Sigma).
\tag{9.4}
\]
All four are the same condition. **PROVED INTERNALLY.**

### 9.1 L-9.R1.1 — existence over the closed cone

**Lemma B9-c (properness).** \(({\rm PSD}(m),d_{\rm BW})\) is a complete, **proper** metric space (closed balls are compact), and \(d_{\rm BW}\) induces the ordinary Euclidean topology on \({\rm PSD}(m)\).
*Proof.* \(d_{\rm BW}(A,0)^2=\operatorname{tr}A\). If \(d_{\rm BW}(A,0)\le r\) then \(\operatorname{tr}A\le r^2\), and \(\{A\succeq0:\operatorname{tr}A\le r^2\}\) is Euclidean-compact. Continuity of \((A,B)\mapsto d_{\rm BW}(A,B)\) in the Euclidean topology follows from continuity of \(A\mapsto A^{1/2}\) and of \(X\mapsto\operatorname{tr}X^{1/2}\) on \({\rm PSD}\). Both topologies are therefore comparable on Euclidean-compact sets and \(d_{\rm BW}\)-balls are compact; completeness follows. (Equivalently: \({\rm PSD}(m)\) with \(d_{\rm BW}\) is isometric to the set of centred Gaussians in \((\mathcal P_2(\mathbb R^m),W_2)\), which is \(W_2\)-closed.) \(\square\) **PROVED.**

> **Theorem L-9.R1.1.** Let \(Q\) be a Borel probability measure on \({\rm PSD}(m)\) with
> \[
> \boxed{\ \int\operatorname{tr}\Sigma\ Q(d\Sigma)<\infty\ }
> \]
> — this is the **exact** moment condition, since \(d_{\rm BW}(0,\Sigma)^2=\operatorname{tr}\Sigma\), so it is precisely "\(Q\in\mathcal P_2({\rm PSD}(m),d_{\rm BW})\)". Then \(F_Q\) is finite and locally Lipschitz (hence continuous) on \({\rm PSD}(m)\), coercive, and \(\operatorname{argmin}_{{\rm PSD}(m)}F_Q\ne\emptyset\).
> *Proof.* Finiteness: \(d(A,\Sigma)^2\le2d(A,0)^2+2d(0,\Sigma)^2=2\operatorname{tr}A+2\operatorname{tr}\Sigma\). Local Lipschitz: \(|d(A,\Sigma)^2-d(A',\Sigma)^2|\le d(A,A')\,(d(A,\Sigma)+d(A',\Sigma))\le d(A,A')(2d(A',\Sigma)+d(A,A'))\), integrable. Coercivity: \(d(A,\Sigma)^2\ge\tfrac12d(A,0)^2-d(0,\Sigma)^2\), so \(F_Q(A)\ge\tfrac12\operatorname{tr}A-\int\operatorname{tr}\Sigma\,dQ\to\infty\). Sublevel sets are therefore \(d_{\rm BW}\)-bounded, hence compact by Lemma B9-c, and a continuous function on a nonempty compact set attains its minimum. \(\square\)

**Status L-9.R1.1: PROVED INTERNALLY.** (The lead's route is confirmed verbatim.)

### 9.2 L-9.R1.2 — no rank-deficient minimiser: an **exact** one-sided bound

The lead's route asks for \(\Delta_\varepsilon(\Sigma)=\sqrt{\varepsilon s(\Sigma)}+O(\varepsilon)\) with a uniform-in-\(\Sigma\) remainder. The remainder is unnecessary: the inequality holds **exactly**, in the only direction needed.

**Setup.** Let \(\bar\Sigma\in{\rm PSD}(m)\) be singular, \(W=\operatorname{ran}\bar\Sigma\) (\(\dim W=r<m\)), \(v\in\ker\bar\Sigma\) a unit vector, \(P=\bar\Sigma^{1/2}\), \(A_\varepsilon=\bar\Sigma+\varepsilon vv^\top\). Since \(Pv=0\),
\[
\big(P+\sqrt\varepsilon\,vv^\top\big)^2=\bar\Sigma+\varepsilon vv^\top,\qquad P+\sqrt\varepsilon\,vv^\top\succeq0,
\quad\text{so}\quad A_\varepsilon^{1/2}=P+\sqrt\varepsilon\,vv^\top\ \textbf{exactly}.
\tag{9.5}
\]
Define the **Schur complement**
\[
s(\Sigma):=\min_{u\in W}(v-u)^\top\Sigma(v-u)=\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}
\]
in the splitting \(W\oplus W^\perp\) with the "2" index the \(v\)-direction (the equality is the standard block minimisation, valid whenever \(\Sigma_{11}=\Sigma|_W\) is invertible; when \(\Sigma_{11}\) is singular interpret with a pseudo-inverse and the min-formula, which is always defined). Note \(s(\Sigma)>0\) for every \(\Sigma\succ0\).

> **Lemma B9-b (exact one-sided nuclear-norm bound).** For every \(\Sigma\succeq0\) and every \(\varepsilon\ge0\),
> \[
> \Delta_\varepsilon(\Sigma):=\operatorname{tr}\big(A_\varepsilon^{1/2}\Sigma A_\varepsilon^{1/2}\big)^{1/2}-\operatorname{tr}\big(\bar\Sigma^{1/2}\Sigma\bar\Sigma^{1/2}\big)^{1/2}
> \ \ge\ \sqrt{\varepsilon\,s(\Sigma)} .
> \tag{9.6}
> \]
> *Proof.* Write \(\operatorname{tr}(G\Sigma G)^{1/2}=\|\Sigma^{1/2}G\|_*\) for \(G\succeq0\). With \(B:=\Sigma^{1/2}P\), \(a:=\Sigma^{1/2}v\), \(\delta:=\sqrt\varepsilon\), we must show \(\|B+\delta av^\top\|_*\ge\|B\|_*+\delta\sqrt{s(\Sigma)}\).
> By duality \(\|M\|_*=\max\{\operatorname{tr}(Z^\top M):\|Z\|_{\rm op}\le1\}\). Let \(\Pi\) be the orthogonal projector onto \(\operatorname{ran}B=\Sigma^{1/2}W\); then \(|(I-\Pi)a|^2=\min_{u\in W}|\Sigma^{1/2}(v-u)|^2=s(\Sigma)\). If \(s(\Sigma)=0\) the claim is trivial; otherwise set \(\hat n=(I-\Pi)a/\sqrt{s(\Sigma)}\) and \(Z=Z_0+\hat n v^\top\), where \(Z_0=U_BV_B^\top\) is the sign of \(B\) (so \(\operatorname{tr}(Z_0^\top B)=\|B\|_*\), \(\|Z_0\|_{\rm op}\le1\), \(\operatorname{ran}Z_0\subseteq\operatorname{ran}B\), \(\operatorname{ran}Z_0^\top\subseteq\operatorname{ran}B^\top=W\)).
> * \(\|Z\|_{\rm op}=1\): \(Z_0\) and \(\hat nv^\top\) have orthogonal column spaces (\(\hat n\perp\Sigma^{1/2}W=\operatorname{ran}B\)) **and** orthogonal row spaces (\(v\perp W\)), so their singular values interleave without interaction.
> * \(\operatorname{tr}(Z^\top B)=\|B\|_*+\hat n^\top Bv=\|B\|_*\), since \(Bv=\Sigma^{1/2}Pv=0\).
> * \(\operatorname{tr}(Z^\top\delta av^\top)=\delta\,(Zv)^\top a=\delta\,(Z_0v+\hat n)^\top a=\delta\,\hat n^\top a=\delta\sqrt{s(\Sigma)}\), since \(Z_0v=0\) (\(v\perp\operatorname{ran}Z_0^\top\)).
>
> Hence \(\|B+\delta av^\top\|_*\ge\operatorname{tr}(Z^\top(B+\delta av^\top))=\|B\|_*+\delta\sqrt{s(\Sigma)}\). The degenerate case \(\bar\Sigma=0\) is direct: \(\|\delta av^\top\|_*=\delta|a|=\delta\sqrt{v^\top\Sigma v}=\delta\sqrt{s(\Sigma)}\). \(\square\)

(Numeric check: over random \(\bar\Sigma\) of ranks 1–4 in \(m=5\) and random \(\Sigma\succ0\), the ratio \(\Delta_\varepsilon/\sqrt{\varepsilon s}\) is \(\ge1\) at every \(\varepsilon\) tested and \(\to1\) as \(\varepsilon\downarrow0\), confirming that (9.6) is one-sided and asymptotically tight — so the lead's \(\sqrt{\varepsilon s(\Sigma)}+O(\varepsilon)\) is correct, but only the lower half is needed.)

> **Theorem L-9.R1.2.** Let \(\int\operatorname{tr}\Sigma\,dQ<\infty\) and let \(\bar\Sigma\in{\rm PSD}(m)\) be singular with unit \(v\in\ker\bar\Sigma\). Put \(c_v:=\int\sqrt{s_v(\Sigma)}\,Q(d\Sigma)\in[0,\infty]\). Then for every \(0<\varepsilon<4c_v^2\),
> \[
> F_Q(A_\varepsilon)-F_Q(\bar\Sigma)=\varepsilon-2\int\Delta_\varepsilon(\Sigma)Q(d\Sigma)\ \le\ \varepsilon-2\sqrt\varepsilon\,c_v\ <\ 0 .
> \tag{9.7}
> \]
> Hence \(\bar\Sigma\) is **not** a minimiser whenever \(c_v>0\) for some unit \(v\in\ker\bar\Sigma\). In particular, if \(Q(\{\Sigma\succ0\})>0\) then \(s_v(\Sigma)>0\) on a set of positive \(Q\)-measure, so \(c_v>0\) for **every** \(v\), and **no** rank-deficient \(\bar\Sigma\) is a minimiser.
> *Proof.* \(\operatorname{tr}A_\varepsilon-\operatorname{tr}\bar\Sigma=\varepsilon\) exactly, and the rest is (9.6) integrated (the integrand is bounded below by a nonnegative measurable function; no dominated convergence, no uniform remainder, and no integrability side condition are needed — only the elementary fact that \(\int\Delta_\varepsilon dQ\ge\sqrt\varepsilon c_v\), valid also when \(c_v=\infty\)). \(\square\)

**Higher corank.** The proof uses an arbitrary unit \(v\in\ker\bar\Sigma\) and never uses \(\dim\ker\bar\Sigma=1\). **The one-dimensional-kernel restriction in the lead's route is unnecessary.**

**Sharp boundary (registered sublemma B9-e).** Combining: a minimiser \(\bar\Sigma\) is rank-deficient **only if** for every unit \(v\in\ker\bar\Sigma\), \(s_v(\Sigma)=0\) for \(Q\)-a.e. \(\Sigma\), i.e. \(Q\)-a.e. \(\Sigma\) satisfies \((v+\operatorname{ran}\bar\Sigma)\cap\ker\Sigma\ne\emptyset\). This forces \(Q\) to be a.s. rank-deficient. Examples where a boundary minimiser exists: \(Q=\delta_{\Sigma_0}\) with \(\Sigma_0\) singular; more generally \(Q\) supported on \(\{\Sigma:\operatorname{ran}\Sigma\subseteq W_0\}\) for a fixed proper subspace \(W_0\). **PROVED.**

> **R1 VERDICT: no counterexample exists.** The lead's prediction is confirmed. There is **no** law on the full-rank BW cone, with mass approaching rank deficiency, whose argmin is empty in the open cone: existence over \({\rm PSD}(m)\) is unconditional under the stated moment condition, and the minimiser is automatically full rank as soon as \(Q\) charges the full-rank cone. The incompleteness of the open cone is **not** an obstruction, because the boundary is repelling at rate \(-2\sqrt\varepsilon\) against a gain of \(+\varepsilon\).
> **Failure classification: none — the anticipated failure mode is DISPROVED. The completeness-specific escape route is closed.**
> **ID-1 restatement required for BW:** none. ID-1's hypothesis "\(\mathfrak M(Q)\ne\emptyset\)" is **automatically satisfied** on the project's flagship geometry under \(\int\operatorname{tr}\Sigma\,dQ<\infty\), and \(\mathfrak M(Q)\) sits in the open cone whenever \(Q\) charges it. A displayed corollary to that effect should be added to the canonical P1-ID §4.

---

## 10. TARGET R2 — uniqueness, selection, and the cost of a selector

### 10.1 L-9.R2.1 — BW uniqueness

#### 10.1.1 The primary theorem, read verbatim, and why it does not cover the project's setting

**Source.** M. Agueh and G. Carlier, *Barycenters in the Wasserstein space*, SIAM J. Math. Anal. 43(2) (2011), 904–924. Full text read (author copy, CEREMADE).

* **Definition 3.2.** \(\mu\) *vanishes on small sets* iff \(\mu(A)=0\) for every Borel \(A\subset\mathbb R^d\) of Hausdorff dimension \(\le d-1\).
* **Proposition 3.3** (Brenier/McCann, as restated there). If \(\mu\) vanishes on small sets, the optimal plan between \(\mu\) and \(\nu\) is unique and of the form \((\operatorname{id},\nabla\varphi)_\#\mu\) with \(\varphi\) convex. *(Used in §5.1 for BW log uniqueness.)*
* **Proposition 3.5.** If there is an index \(i\in\{1,\dots,p\}\) such that \(\nu_i\) vanishes on small sets, then \((P)=\inf_\nu\sum_{i=1}^p\tfrac{\lambda_i}2W_2^2(\nu_i,\nu)\) admits a **unique** solution, given by \(\nu=\nabla\varphi_{i\#}\nu_i\).
* **Theorem 6.1.** In the Gaussian framework of §6.3 (\(\nu_i=N(0,S_i)\), **each \(S_i\) positive definite**, \(\lambda_i>0\), \(\sum\lambda_i=1\)), there is a unique solution \(\nu\) to (2.2); moreover \(\nu=N(0,S)\) where \(S\) is the unique positive definite root of \(\sum_i\lambda_i(S^{1/2}S_iS^{1/2})^{1/2}=S\).

**Exact hypotheses and the gap.** Agueh–Carlier treat **finitely many** measures \(\nu_1,\dots,\nu_p\) with positive weights summing to 1, on \(\mathbb R^d\), each with finite second moment. Theorem 6.1 additionally requires **every** \(S_i\succ0\). Consequently the primary theorem does **not** by itself cover:
1. a general \(Q\in\mathcal P_2({\rm PSD}(m))\) that is not a finite convex combination of atoms (the project's \(Q_u\) are typically non-atomic);
2. a \(Q\) charging rank-deficient \(\Sigma\) as well as the full-rank cone;
3. a triangular array \(\{Q_{u,n}\}\) (though this is trivially handled by applying any \(Q\)-level theorem separately at each \((u,n)\));
4. the reduction from "unique barycentre in \(\mathcal P_2(\mathbb R^m)\)" to "unique minimiser of \(F_Q\) on \({\rm PSD}(m)\)", which needs the extra step that the unconstrained minimiser is Gaussian.

Item 4 is worth stating: Prop. 3.5 gives uniqueness of the barycentre among **all** measures; Theorem 6.1 then shows it is Gaussian. Restricting to \({\rm PSD}(m)\) is legitimate only after that. Rather than patch items 1–4, we prove the required statement directly and in stronger form.

#### 10.1.2 Internal proof (covers the project's setting and strictly extends AC Thm. 6.1)

> **Theorem L-9.R2.1.** Let \(Q\) be a Borel probability measure on \({\rm PSD}(m)\) with \(\int\operatorname{tr}\Sigma\,Q(d\Sigma)<\infty\). Then:
> 1. \(F_Q\) is **convex** on \({\rm PSD}(m)\) in the ordinary linear structure;
> 2. if \(Q(\{\Sigma\succ0\})>0\) then \(F_Q\) is **strictly convex** on the open full-rank cone;
> 3. consequently, combined with L-9.R1.1–R1.2, \(\operatorname{argmin}F_Q\) is a **singleton contained in the open full-rank cone**, and it is the unique \(A\succ0\) solving \(A=\int(A^{1/2}\Sigma A^{1/2})^{1/2}Q(d\Sigma)\).
>
> *Proof.* (1) \(F_Q(A)=\operatorname{tr}A+\int\operatorname{tr}\Sigma\,dQ-2\int\psi_\Sigma(A)\,dQ\); the first term is linear and \(\psi_\Sigma\) is concave by (9.2), so \(-2\int\psi_\Sigma dQ\) is convex.
> (2) Fix \(A_0\ne A_1\) in the open cone, \(A_t=(1-t)A_0+tA_1\), \(H=A_1-A_0\ne0\). Let \(\Sigma\succ0\) and \(\phi(t)=\psi_\Sigma(A_t)\). By Lemma B9-a, \(\phi(t)=\tfrac12\min_{T\succ0}\ell_T(t)\) with \(\ell_T(t)=\operatorname{tr}(TA_t)+\operatorname{tr}(T^{-1}\Sigma)\) affine in \(t\), the minimum attained at the unique \(T_t\) with \(T_tA_tT_t=\Sigma\). Suppose \(\phi\) were affine on some interval \(I\subset[0,1]\) with interior point \(t_m\). Then \(\ell_{T_{t_m}}\ge2\phi\) on \(I\) with equality at \(t_m\); both sides being affine on \(I\), \(\ell_{T_{t_m}}-2\phi\) is affine, nonnegative on \(I\), and zero at an interior point, hence identically zero on \(I\). Thus \(T_{t_m}\) is optimal at every \(t\in I\), so \(T_{t_m}A_tT_{t_m}=\Sigma\) for all \(t\in I\); subtracting two such identities gives \(T_{t_m}HT_{t_m}=0\), and \(T_{t_m}\succ0\) forces \(H=0\), a contradiction. Hence \(\phi\) is **strictly** concave for every \(\Sigma\succ0\). Since \(\psi_\Sigma\) is concave for every \(\Sigma\succeq0\) and strictly concave for \(\Sigma\succ0\), and \(Q(\{\Sigma\succ0\})>0\), the map \(t\mapsto\int\psi_\Sigma(A_t)dQ\) is strictly concave, so \(F_Q\) is strictly convex along the segment.
> (3) By L-9.R1.1 the argmin over \({\rm PSD}(m)\) is nonempty; by L-9.R1.2 it lies in the open cone; \(F_Q\) is convex there so the argmin is convex, and strict convexity forces a singleton. The fixed-point characterisation is (9.4) with (9.3). \(\square\)

(Numeric sanity check: second differences of \(t\mapsto\psi_\Sigma(A_t)\) on random \(4\times4\) triples are strictly negative at every grid point.)

**Comparison to Agueh–Carlier.** Theorem L-9.R2.1 recovers AC Theorem 6.1 as the special case \(Q=\sum\lambda_i\delta_{S_i}\), \(S_i\succ0\), and **strictly extends** it in three directions: arbitrary \(Q\) (not finitely many atoms); \(Q\) allowed to charge rank-deficient \(\Sigma\) provided it also charges the full-rank cone; and the conclusion is obtained directly on \(({\rm PSD}(m),d_{\rm BW})\) with no detour through \(\mathcal P_2(\mathbb R^m)\). It also gives something AC does not display: **\(F_Q\) is convex in the ordinary linear structure**, even though BW is a nonnegatively curved metric where geodesic convexity of \(F_Q\) generally fails.

**Bhatia–Jain–Lim (2019), Expositiones Math. 37(2), 165–191** is already in the project references. It supplies the BW distance formula, the quotient-geometry background, and the matrix-mean/fixed-point discussion; it is **not** used as a producer for any statement above. Its role here is background only, exactly as recorded in [[References and external claim audit]] §2.

**Status L-9.R2.1: PROVED INTERNALLY (strengthened); AC Prop. 3.3 / Prop. 3.5 / Thm. 6.1 CITED+APPLIED verbatim as provenance and as the producer for Lemma B8-0.**

**Consequences.** Uniqueness plus convexity plus \(W_2\)-continuity of \(u\mapsto Q_u\) gives, by Berge's maximum theorem, **continuity of the BW centre path \(u\mapsto\mu(u)\)**. The R2.3 crack below therefore **cannot** occur on the BW application, provided every \(Q_u\) charges the full-rank cone. That proviso is now a displayed hypothesis, not a tacit one.

### 10.2 L-9.R2.2 — exact non-uniqueness class on spheres and product spheres

> **Theorem B9-d (symmetry structure theorem).** Let \(G\le\operatorname{Isom}(M)\) with \(g_\#Q=Q\) for all \(g\in G\). Then \(F_Q\circ g=F_Q\), so \(\mathfrak M(Q)\) is \(G\)-invariant. Consequently:
> * if \(\mathfrak M(Q)=\{m\}\) then \(m\) is a \(G\)-fixed point;
> * if \(G\) has **no** fixed point in \(M\) and \(\mathfrak M(Q)\ne\emptyset\), then \(\mathfrak M(Q)\) is not a singleton and \(\dim\mathfrak M(Q)\ge\min\{\dim(G\cdot p):p\in\mathfrak M(Q)\}\).
> **PROVED** (one line each). This is the general structure asked for: **non-uniqueness on a symmetric space is exactly a fixed-point obstruction of the stabiliser of the law.**

**Exact example 1 (positive-dimensional argmin; generalises ID-1's \(S^1\) antipodal law).** \(M=S^{p-1}\) unit round, \(Q=\tfrac12(\delta_{e_p}+\delta_{-e_p})\). For \(y\) at polar angle \(\phi=d(y,e_p)\in[0,\pi]\),
\[
F_Q(y)=\tfrac12\big[\phi^2+(\pi-\phi)^2\big]=\phi^2-\pi\phi+\tfrac{\pi^2}2,
\]
strictly convex in \(\phi\) with a unique minimum at \(\phi=\pi/2\). Hence
\[
\boxed{\ \mathfrak M(Q)=\{y:d(y,e_p)=\tfrac\pi2\}=S^{p-2}\ }
\]
— a **totally geodesic \((p-2)\)-dimensional submanifold**. For \(p=2\) this is ID-1's two-point set; for \(p=3\) it is a great circle; for general \(p\) it is a whole subsphere. Stabiliser: \(G=O(p-1)\times O(1)\) acting as rotations of \(e_p^\perp\) together with \(e_p\mapsto-e_p\); \(G\) has no fixed point, matching B9-d. **PROVED EXACTLY.**

**Exact example 2 (maximal argmin).** \(Q=\) uniform on \(S^{p-1}\). \(F_Q\) is \(O(p)\)-invariant and \(O(p)\) is transitive, so \(F_Q\) is constant and \(\mathfrak M(Q)=S^{p-1}\): the argmin is the **whole manifold**, dimension \(p-1\). **PROVED EXACTLY.**

**Exact example 3 (zero-dimensional but nonsingleton, no antipodal atoms).** \(Q=\) uniform on the equator \(S^{p-2}\subset S^{p-1}\). \(F_Q\) depends on \(y\) only through \(\sin\phi\), so it is invariant under the reflection \(\phi\mapsto\pi-\phi\) and under \(O(p-1)\). For \(p=3\): \(F_Q(\text{pole})=\pi^2/4\) and \(F_Q(\text{equator point})=\tfrac1{2\pi}\int_{-\pi}^{\pi}\alpha^2d\alpha=\pi^2/3>\pi^2/4\), so the minimum is at the poles and \(\mathfrak M(Q)=\{\pm e_3\}\). **PROVED EXACTLY.** (This shows that non-uniqueness on the sphere is not confined to antipodal two-point laws.)

**Product spheres.** \(F_{Q_1\otimes Q_2}(x_1,x_2)=F_{Q_1}(x_1)+F_{Q_2}(x_2)\), so \(\mathfrak M(Q_1\otimes Q_2)=\mathfrak M(Q_1)\times\mathfrak M(Q_2)\) and dimensions **add**. On \(S^2\times S^2\) with both factors carrying antipodal laws, \(\mathfrak M\) is a **torus \(S^1\times S^1\)**. Non-product \(Q\) on a product sphere: B9-d applies to the diagonal stabiliser and gives the same conclusion whenever the stabiliser is fixed-point free. **PROVED.**

**Sufficient condition for uniqueness (recorded, not load-bearing).** A concentration hypothesis of Karcher–Kendall–Afsari type — support in an open geodesic ball of radius below a curvature/injectivity threshold — gives existence and uniqueness. B. Afsari, *Riemannian \(L^p\) center of mass: existence, uniqueness, and convexity*, Proc. Amer. Math. Soc. 139(2) (2011), 655–673, is the sharpest such statement. **Status: CITED, CONSTANT NOT VERIFIED VERBATIM against the primary text in this pass, and NOT LOAD-BEARING** — no claim in this dossier depends on the exact threshold. The exact boundary in the project's own examples is supplied by Examples 1–3 above, which are internal.

**Status L-9.R2.2: PROVED INTERNALLY.**

### 10.3 L-9.R2.3 — measurable selection, discontinuity, and manufactured drift

#### 10.3.1 The family

\(M=S^1\), arclength metric, injectivity radius \(\pi\). Identify points with angles mod \(2\pi\). Fix \(\kappa\in(0,\pi/2)\) and \(u_0\in(0,1)\), and set
\[
\psi(u)=\pi+\kappa\,(u-u_0),\qquad u\in[0,1],
\qquad
Q_u=\tfrac12\big(\delta_{\{0\}}+\delta_{\{\psi(u)\}}\big).
\]
\(u\mapsto Q_u\) is Lipschitz in \(W_2\): \(W_2(Q_u,Q_{u'})\le|\psi(u)-\psi(u')|/\sqrt2\le\kappa|u-u'|/\sqrt2\). **Continuous by construction.**

**Exact argmin.** For a two-point law on \(S^1\) with atoms at \(0\) and \(\psi\in(0,2\pi)\): \(F(\theta)=\tfrac12[d(\theta,0)^2+d(\theta,\psi)^2]\) is piecewise quadratic with unit leading coefficient, with concave kinks (local maxima) at the two antipodes \(\theta=\pi\) and \(\theta=\psi+\pi\), so all local minima are interior critical points of the two arcs; these are \(\theta=\psi/2\) and \(\theta=\psi/2+\pi\), with values \(\min(\psi,2\pi-\psi)^2/4\) and \(\max(\psi,2\pi-\psi)^2/4\). Hence
\[
\mathfrak M(Q_u)=
\begin{cases}
\{\psi(u)/2\}, & \psi(u)<\pi\ (u<u_0),\\[1mm]
\{\pi/2,\ 3\pi/2\}, & \psi(u)=\pi\ (u=u_0),\\[1mm]
\{\psi(u)/2+\pi\}, & \psi(u)>\pi\ (u>u_0).
\end{cases}
\tag{10.1}
\]
**PROVED EXACTLY.** The mean is unique for \(u\ne u_0\) and a two-point set at \(u=u_0\), exactly the configuration the target requires.

#### 10.3.2 (i) Measurable selector — exists

**Applied theorem.** K. Kuratowski and C. Ryll-Nardzewski, *A general theorem on selectors*, Bull. Acad. Polon. Sci. Sér. Sci. Math. Astronom. Phys. **13** (1965), 397–403: a measurable multifunction from a measurable space into a Polish space, with nonempty closed values, admits a measurable selection.
**Line-by-line application.** \(([0,1],\mathcal B)\) is a measurable space; \(M=S^1\) is Polish and compact; \(u\mapsto\mathfrak M(Q_u)\) has nonempty compact (hence closed) values by L-9.R1.1-type compactness; \((u,\theta)\mapsto F_{Q_u}(\theta)\) is jointly continuous, so by Berge's maximum theorem the argmin correspondence is upper hemicontinuous with closed graph, hence weakly measurable. **All hypotheses verified; a Borel selector \(u\mapsto\mu(u)\) exists.** In this example an explicit one is available: take the branch \(\mu(u)=\psi(u)/2\) for \(u\le u_0\) and \(\psi(u)/2+\pi\) for \(u>u_0\). **CITED+APPLIED.**

#### 10.3.3 (ii) Continuity — impossible

> **Theorem L-9.R2.3-b.** No selector of (10.1) is continuous at \(u_0\).
> *Proof.* Any selector must equal the unique minimiser for \(u\ne u_0\). Thus \(\lim_{u\uparrow u_0}\mu(u)=\pi/2\) and \(\lim_{u\downarrow u_0}\mu(u)=3\pi/2\), which are **antipodal**, at distance \(\pi\). No value at \(u_0\) reconciles them. \(\square\) **PROVED.**
> The jump size is exactly \(\pi\), the maximal possible on \(S^1\), and is **independent of \(\kappa\)** — it does not shrink as the family becomes slower.

#### 10.3.4 (iii) Manufactured drift — exact computation in the project's own machinery

**Anchor and logs.** Fix the ID-5 anchor \(c_0=\) angle \(\pi/4\). Then every log used is unique: \(d(c_0,0)=\pi/4\); \(d(c_0,\psi(u))\in(3\pi/4-\kappa/2,3\pi/4+\kappa/2)\subset(0,\pi)\); \(d(c_0,\pi/2)=\pi/4\); \(d(c_0,3\pi/2)=3\pi/4\). **All strictly below \(\pi\); no cut-locus contamination anywhere in the construction.**

**Observation process.** Let \((\epsilon_t)_{t=1}^n\) be a stationary two-state reset chain on \(\{-1,+1\}\) with uniform invariant law and parameter \(\rho\in(0,1)\); set \(X_{t,n}=0\) if \(\epsilon_t=-1\) and \(=\psi(t/n)\) if \(\epsilon_t=+1\). Then \(X_{t,n}\sim Q_{t/n}\) exactly; the process is bounded, geometrically mixing, has no zero-frequency atom and no deterministic trend. The **true** moving-centre score is \(V_{t,n}=\log_{\mu(t/n)}X_{t,n}=\pm\tfrac12\min\{\psi,2\pi-\psi\}\), an exact rank-one factor with \(\operatorname{Cov}(V_t,V_{t-h})=\rho^h\cdot\tfrac14\min\{\psi,2\pi-\psi\}^2\approx\rho^h\pi^2/4\).

**Declared centre path and its drift row.** \(d_t=\log_{c_0}\mu(t/n)\). By (10.1),
\[
d_t=\begin{cases}\pi/4+O(\kappa), & t/n<u_0,\\ -3\pi/4+O(\kappa), & t/n>u_0,\end{cases}
\qquad\text{a jump of exact size }\pi .
\]
With \(\lambda=u_0\), the centred values are \(d_t-\bar d=(1-\lambda)\pi\) before the jump and \(-\lambda\pi\) after, so for the ID-5 drift row \(D_{d,n}(h)=\frac1{n-h}\sum_{t=h+1}^n(d_t-\bar d)(d_{t-h}-\bar d)\),
\[
\boxed{\ D_{d,n}(h)=\pi^2\lambda(1-\lambda)+O\!\Big(\frac hn\Big)\quad\text{for every }h\ }
\tag{10.2}
\]
(the \(O(h/n)\) counts the \(\approx h\) straddling pairs, which contribute \(-\pi^2\lambda(1-\lambda)\) each). The uncentred version is \(\pi^2/4+O(h/n)\). At \(\lambda=1/2\) the constant is \(\pi^2/4\approx2.467\).

**Quantified consequences.**
1. **Nonvanishing at every lag.** (10.2) is **lag-invariant** to leading order: it does not decay in \(h\) at all, unlike any \(\alpha\)-mixing factor row.
2. **Bandwidth-insensitive.** A local-Fréchet centre estimate with bandwidth \(b_n\to0\) smears the jump over a rescaled-time window of width \(O(b_n)\), turning the step into a ramp; the straddling fraction becomes \(O(b_n+h/n)\), so \(D_{d,n}(h)=\pi^2\lambda(1-\lambda)+O(b_n+h/n)\). **Shrinking the bandwidth does not shrink it; it converges to the same constant.**
3. **Dominates the genuine factor row.** The true factor contributes \(\approx\rho^h\pi^2/4\) at lag \(h\). At \(\lambda=1/2\) the manufactured drift **equals** it at \(h=0\) and exceeds it by the factor \(\rho^{-h}\) at every \(h\ge1\). In the ID-5 accumulation \(\mathbb L=h_0M_d^2+\sum_hB_hB_h^*+\dots\), the drift contributes \(h_0\pi^2\lambda(1-\lambda)\) while the factor saturates at \(\sum_h\rho^{2h}\pi^4/16<\infty\); **including more lags makes the artefact dominate without bound.**
4. **It has the exact signature of a persistent factor.** Rank one, lag-invariant, aligned along the fixed tangent direction \(\log_{c_0}(\pi/2)-\log_{c_0}(3\pi/2)\). Nothing in the fitted lag row distinguishes it from a genuine slowly-varying factor.

**Classification demanded by the target.**
* **(a) Artefact of the convention? YES.** The family \(\{Q_u\}\) is Lipschitz in \(W_2\); the argmin correspondence is continuous in the Hausdorff sense; nothing in the law jumps. The jump is created solely by *declaring a single point* as the centre.
* **(b) Removable by any convention? NO.** L-9.R2.3-b shows no continuous single-valued selection exists. Therefore **every** convention that outputs one centre per \(u\) — equivariant, smoothness-regularised, lexicographic, or otherwise — produces a jump of size \(\pi\) at \(u_0\), hence produces (10.2). The artefact is removable only by (i) changing the estimand to the set-valued centre, (ii) restricting the model class so that every \(Q_u\) has a unique mean **and** the family avoids the nonsingleton stratum, or (iii) declaring the centre path itself to be an assumption rather than a functional. This is **convention-induced but convention-irremovable**: a genuine identification obstruction, not an estimation nuisance.
* **(c) Can it dominate the genuine factor row? YES**, by item 3, at every lag \(h\ge1\), and by an arbitrarily large margin as \(h_0\) grows or \(\rho\downarrow0\).

**Standards checklist for this counterexample.** Manifold and metric: \(S^1\) unit round. Complete stochastic construction: two-state reset chain \(\epsilon_t\) with \(0<\rho<1\), bounded, geometrically mixing, no zero-frequency atom. Fréchet means: unique for every \(u\ne u_0\) by (10.1), **deliberately non-unique at \(u=u_0\)**. Support and normal neighbourhood: all logs at \(c_0=\pi/4\) and at \(\mu(u)\) are unique; all distances \(<\pi\). Factor rank 1; loading the map \(\mathfrak a\mapsto\mathfrak a\) in the score fibre; factor law \(\pm\tfrac12\min\{\psi,2\pi-\psi\}\) with \(\rho^h\) autocovariance; noise zero. Dependence and spectrum: geometric mixing, no atom at frequency 0. Assumptions of the attacked claim (that a declared centre path is an \(\mathcal I_M\)-functional producing an uncontaminated moving-centre score): all verified. Equality of the observational object: the observation law is fixed; only the declared centre changes. Explicit violation: (10.2). Responsible feature: **the non-singleton stratum of the argmin correspondence and the topological impossibility of a continuous section through it.**
**Classification: convention-induced (in the sense of §5 of the campaign standards), and proved to be irremovable by any convention within the single-valued class.**

**Status L-9.R2.3: PROVED INTERNALLY (parts ii, iii) and CITED+APPLIED (part i, Kuratowski–Ryll-Nardzewski 1965).**

### 10.4 R2 verdict split by geometry

| Geometry | Uniqueness | Selector cost |
|---|---|---|
| **BW \({\rm PSD}(m)\), \(Q\) charging the full-rank cone, \(\int\operatorname{tr}\Sigma\,dQ<\infty\)** | **Unique**, in the open cone (L-9.R2.1 + R1). | **Zero.** The centre path is continuous by Berge; no selector is needed; L-9.R2.3 cannot occur. |
| **BW, \(Q\) a.s. rank-deficient** | Minimiser exists in \({\rm PSD}(m)\) but may lie on the boundary and need not be unique (B9-e boundary case; BW-FIXED-MARGIN §7's orthogonal rank-one PSD endpoints give nonunique two-point means). | Outside the project's full-rank manifold; **SEPARATED**. |
| **\(S^{p-1}\) and product spheres** | **Fails**, with argmin sets that are whole subspheres \(S^{p-2}\), whole spheres, or tori (L-9.R2.2). | **Positive and irremovable**: no continuous selector through a nonsingleton stratum, manufacturing a lag-invariant rank-one contamination (L-9.R2.3). |

**What this means for the parent's simulations versus its BW application.** The parent's sphere and product-sphere simulations live in the geometry where the ID-1 gate can be **vacuous** and where a moving-centre convention can manufacture a persistent factor. Its flagship BW application does **not**: uniqueness and continuity of the centre path are theorems there, subject to the single displayed hypothesis that each marginal charges the full-rank cone. This is a clean, geometry-specific split and should be stated as such in the canonical file.

---

## 11. Sublemma register — every entry terminal

| ID | Statement | Status | Location |
|---|---|---|---|
| L-8.1 | GP/Gavrilov–Pennec expansion, coefficients \(\tfrac16,\tfrac13\), tensor typing, convention translation | **CITED+APPLIED** (Pennec 2019 Thm. 2) **with coefficients PROVED INTERNALLY** | §2 |
| L-8.2 | \(\langle R(X,Y)X,X\rangle=0\); \(c'(0)=PV+O(|w|^2)\); wedge \(=2b^3c'\wedge c''+O(b^4)\); \(\kappa\ne0\Rightarrow R(PV,w)PV\ne0\); converse false | **PROVED INTERNALLY** | §3 |
| L-8.3 | exact BW \({\rm SPD}(2)\) non-collinearity, exact in \(b\), full \(b\)-range, \(W\ne Y^2\), unique \(Z\ne0\) | **PROVED INTERNALLY** | §5 |
| L-8.4 | exact AIRM \({\rm SPD}(2)\) and exact \(H^2\) non-collinearity; \(1-2d/\sinh2d>0\) verified | **PROVED INTERNALLY (two independent exact routes)** | §6 |
| L-8.5 | converse rigidity; relation to ID-4 | **PROVED INTERNALLY** (necessary condition; sufficiency scoped to third order and not consumed) | §7 |
| L-9.R1.1 | coercivity, properness, existence over \({\rm PSD}(m)\); moment condition \(\int\operatorname{tr}\Sigma\,dQ<\infty\) | **PROVED INTERNALLY** | §9.1 |
| L-9.R1.2 | no rank-deficient minimiser when \(Q\) charges the full-rank cone; any corank | **PROVED INTERNALLY** (exact bound, no remainder) | §9.2 |
| L-9.R2.1 | BW uniqueness for arbitrary \(Q\) charging the full-rank cone | **PROVED INTERNALLY (extends AC Thm. 6.1)**; AC **CITED+APPLIED** | §10.1 |
| L-9.R2.2 | exact non-uniqueness class on spheres and products; positive-dimensional argmin | **PROVED INTERNALLY** | §10.2 |
| L-9.R2.3 | measurable selector exists; no continuous selector; manufactured broadband drift | **CITED+APPLIED (KRN 1965) + PROVED INTERNALLY** | §10.3 |
| **B8-0** | unique BW log/geodesic between full-rank matrices; no cut locus in the open cone | **CITED+APPLIED (AC Def. 3.2, Prop. 3.3) + PROVED INTERNALLY** | §5.1 |
| **B8-1** | commuting \(\Rightarrow\) \(\operatorname{Log}_I\operatorname{Exp}_x(tV)\) exactly affine in BW; \(W=Y^2\) | **PROVED INTERNALLY** | §5.4 |
| **B8-2** | diagonal BW subcone \(\cong\) Euclidean orthant via \(A\mapsto A^{1/2}\); totally geodesic and flat | **PROVED INTERNALLY** | §5.4 |
| **B8-3** | block embedding \({\rm SPD}(2)\hookrightarrow{\rm SPD}(m)\) totally geodesic in BW and AIRM | **PROVED INTERNALLY** | §5.5 |
| **B8-4** | \(\{\det=c\}\) totally geodesic in AIRM | **PROVED INTERNALLY** | §6.3 |
| **B8-5** | \({\rm SSPD}(2)\) with AIRM \(\cong H^2\) of curvature \(-1/2\); \({\rm SPD}(2)\cong\mathbb R\times H^2_{-1/2}\) | **PROVED INTERNALLY (normalisation derived, not cited)** | §6.3 |
| **B9-a** | \(\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}=\tfrac12\inf_{T\succ0}[\operatorname{tr}TA+\operatorname{tr}T^{-1}\Sigma]\); concavity; gradient \(I-T_A\) | **PROVED INTERNALLY** | §9.0 |
| **B9-b** | exact one-sided bound \(\Delta_\varepsilon(\Sigma)\ge\sqrt{\varepsilon s(\Sigma)}\) | **PROVED INTERNALLY** | §9.2 |
| **B9-c** | \(({\rm PSD}(m),d_{\rm BW})\) proper and complete | **PROVED INTERNALLY** | §9.1 |
| **B9-d** | symmetry \(\Rightarrow\) non-uniqueness structure theorem | **PROVED INTERNALLY** | §10.2 |
| **B9-e** | sharp boundary condition for a rank-deficient BW minimiser | **PROVED INTERNALLY** | §9.2 |
| — | Afsari (2011) concentration threshold constant | **CITED, NOT VERBATIM-VERIFIED, NOT LOAD-BEARING — SEPARATED** | §10.2 |

No node in this dossier is left open.

---

## 12. Objections a hostile auditor should raise first

1. **L-8.1 remainder typing.** The \(O(4)\) in (2.3) is total order in \((tV,w)\), not order in \(t\). Any reader who treats it as \(O(t^4)\) at fixed \(w\) will mis-scale \(\varepsilon_2\) in L-8.2.4. The exact §5–§6 computations are immune because they never use the expansion.
2. **L-8.2.4's \(\varepsilon_2\).** The threshold depends on \(\|R_y\|\), which is a genuine dependence on \(y\); the theorem is not uniform over \(y\). Immaterial for the applied verdicts, which are exact.
3. **L-8.5's sufficiency direction** is deliberately scoped to third order. A reviewer who wants a finite-displacement converse will not find one here; ID-4's B5 remains the exact support-level boundary.
4. **§5.3's "collinear \(\iff\alpha=\beta=0\)"** uses that the two off-diagonal coordinates have opposite signs and \(c\ne0\); it fails if \(b=0\). Stated with \(b\ne0\) throughout.
5. **§5.6's Fréchet-mean claim depends on §10.1.** The circularity is only apparent (§10.1 does not use §5), but a reviewer should check the ordering.
6. **B9-b's dual certificate** needs \(\operatorname{ran}Z_0^\top\subseteq W\) and \(\hat n\perp\Sigma^{1/2}W\) simultaneously. Both were verified; a reviewer should re-derive \(\|Z\|_{\rm op}=1\) from the double orthogonality rather than from \(\|Z_0\|_{\rm op}\le1\) alone.
7. **L-9.R2.1's strict-convexity step** turns on "an affine minorant of an affine function agreeing at an interior point is identically equal". A reviewer should confirm the interval \(I\) is nondegenerate and \(t_m\) interior.
8. **L-9.R2.3's bandwidth claim** asserts that a local-Fréchet estimate cannot remove the jump. The proof given is at the population level (the ramp still traverses the full jump). A finite-sample statement would need an estimator-specific argument and is not claimed.
9. **The \(O(h/n)\) in (10.2)** is not uniform in \(h\) up to \(h\asymp n\); the claim "nonvanishing at every lag" is asserted for \(h=o(n)\), which is the only regime ID-5 uses.

---

## 13. Adjudication notes for the lead

1. **C-AUDIT-5 is confirmed verbatim** against Pennec (2019) Theorem 2. No amendment to [[References and external claim audit]] is needed. Its convention is now pinned: \(R(X,Y)Z=K(\langle Y,Z\rangle X-\langle X,Z\rangle Y)\) in constant curvature, derived from the source's own Eq. (9).
2. **ID-8's candidate theorem needs one word changed**: "whenever the sectional curvature ... is nonzero" is a **sufficient** condition, not a criterion. The sharp criterion is \(R(PV,w)PV\ne0\). On one-signed-curvature manifolds — every geometry the project uses — the two coincide, so no downstream claim changes.
3. **ID-8 is settled exactly, not asymptotically, in both applied geometries.** BW \({\rm SPD}(2)\) and AIRM \({\rm SPD}(2)\) inflate rank for every non-commuting configuration and every admissible displacement, with no cut locus, no compactness, and (AIRM) no incompleteness available as an excuse. This closes the "the \(S^2\) example is a sphere artefact" objection permanently.
4. **The diagonal/fixed-basis BW branch is exactly rigid and is exactly a Euclidean orthant.** The lead's expectation is confirmed and upgraded from second order to exact. It is the *only* rigid branch besides radial supports.
5. **R1: the anticipated counterexample does not exist.** BW Fréchet-mean existence is unconditional under \(\int\operatorname{tr}\Sigma\,dQ<\infty\), and full-rankness is automatic when \(Q\) charges the full-rank cone. The lead's perturbation route is confirmed but should be replaced by the exact nuclear-norm inequality \(\Delta_\varepsilon\ge\sqrt{\varepsilon s(\Sigma)}\), which needs no integrability side condition and no corank restriction. **ID-1 needs a displayed corollary, not a restatement.**
6. **R2 uniqueness on BW is proved internally and is strictly stronger than Agueh–Carlier Theorem 6.1**, which covers only finitely many atoms all of full rank. A new displayed fact worth putting in the canonical file: \(F_Q\) is convex in the **ordinary linear** structure on \({\rm PSD}(m)\), despite BW being nonnegatively curved.
7. **The R2.3 crack is real and changes what the paper can claim.** A \(W_2\)-continuous marginal family passing through a nonsingleton stratum admits **no continuous centre convention**, and any single-valued convention manufactures a lag-invariant, bandwidth-insensitive, rank-one contamination of exact size \(\pi^2\lambda(1-\lambda)\) that dominates a genuine mixing factor at every lag \(h\ge1\). This is a new hostile example against the project's own moving-centre estimand (not against the parent's (P2), which excludes centre drift by assumption). ID-5's "aligned drift can change rank/eigenstructure" clause now has an exact, convention-generated instance.
8. **Consequent scope lock for the canonical file:** the sentence "unique pointwise Fréchet means define the population centre path" (P1-ID §10) is safe on BW under the displayed full-rank-charging hypothesis and **unsafe on spheres and product spheres**. It should be split by geometry.
9. **No contradiction with any existing canonical statement was found.** ID-4's Theorem B6, Theorem B5's boundary, and BW-FIXED-MARGIN §7's "rank loss, not multiplicity, is the genuine global boundary" all survive and are reinforced. The only tension is stylistic: ID-4 §7 says the failure "is curvature-specific in this construction"; ID-8 upgrades that to a theorem and removes the hedge.
10. **Downstream for APP-FIN / APP-NEURO:** any moving-reference rank or factor-count comparison is reference-dependent by theorem in every geometry the project uses. The application map must either fix the reference by convention and refuse cross-reference rank comparisons, or verify a commuting/fixed-eigenbasis or common-geodesic condition on the support.
