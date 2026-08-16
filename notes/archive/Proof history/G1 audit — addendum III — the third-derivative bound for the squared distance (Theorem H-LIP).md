> **ARCHIVED CORRECTION LAYER — incorporated into the canonical G1 audit and Analytical reconstruction on 2026-08-08. Retained for audit history only. Do not treat this file as the current source of truth.**
>
> Later audit corrections also apply: bounded curvature is disproved only without quantitative non-conjugacy; $K_1^{\rm av}$ is formally weaker, not proved strictly weaker; fixed-dimensional compact tubes already give finite Hessian moduli by smoothness and compactness; and self-adjoint operator concentration uses a sphere net with entropy $O(p)$, not $O(p^2)$. See [[G1 audit — resolution of the uniform local Fréchet rate]].

# G1 audit — addendum III: the third-derivative bound for the squared distance (Theorem H-LIP), and the true geometric cost of SW-AS

*Analytical run. No literature, no citation, no numerics. Every non-elementary estimate below is derived.*

---

## A. ONE-SENTENCE VERDICT

**Theorem H-LIP is PROVED** — $\|\nabla_qH\|+\|\nabla_xH\|\le L_H(K_0,K_1,\rho^*,\Theta)$ on a geodesic tube with $|R|\le K_0$, $|\nabla R|\le K_1$ and a quantitative non-conjugacy constant $\Theta$ (which is $\Theta=1$ **free** on Cartan–Hadamard, i.e. under (H1)) — the locally symmetric case $\nabla R\equiv0$ gives $L_H=L_H(K_0,\rho^*)$ **exactly as SW-AS assumed**, and this case **covers the affine-invariant SPD manifold that Paper 1 actually uses** (proved in §G), so the SW-AS proof obligation is discharged for the intended application; bounded curvature *alone* is **disproved** as sufficient (sphere, near-conjugate), whereas the necessity of $\|\nabla R\|_\infty$ *inside a non-conjugate tube* is **UNRESOLVED** and is shown in §F to be blocked by a genuine $L^1$-vs-$L^\infty$ cancellation, so it must not be asserted.

---

## §0. Standing notation for this run

$(M,g)$ smooth Riemannian, $\dim M=p$, Levi-Civita $\nabla$, curvature convention
$$R(A,B)C=\nabla_A\nabla_BC-\nabla_B\nabla_AC-\nabla_{[A,B]}C .$$
Norms of curvature and its derivative are the *operator* norms
$$|R|\le K_0:\iff |R(A,B)C|\le K_0|A||B||C|,\qquad
|\nabla R|\le K_1:\iff |(\nabla_UR)(A,B)C|\le K_1|U||A||B||C| ,$$
for all tangent vectors at all points of the region considered.

$E(q,x):=\tfrac12d(q,x)^2$. $\mathcal T$ denotes a **geodesic tube**: an open set of pairs $(q,x)$ such that every pair is joined by a **unique** minimizing geodesic of length $\le\rho^*$, depending smoothly on $(q,x)$, and $x$ is not conjugate to $q$ along it. On $\mathcal T$, $E$ is smooth.

---

## §A. TYPE THE OBJECTS

### A.1 $H$

$$H(q,x):=\tfrac12\operatorname{Hess}_qd(q,x)^2=\operatorname{Hess}_qE(\cdot,x):T_qM\to T_qM,$$
the $g$-self-adjoint endomorphism associated with the symmetric bilinear form
$$\mathbb H(q,x)(v,w):=\big(\nabla dE(\cdot,x)\big)_q(v,w)=\langle H(q,x)v,w\rangle .$$
Equivalently, since $\operatorname{grad}_qE(\cdot,x)=-\log_qx$,
$$H(q,x)v=-\nabla_v\big(q\mapsto\log_qx\big).$$

### A.2 $\nabla_qH$ — an honest tensor, no connector needed

For **fixed $x$**, $q\mapsto\mathbb H(q,x)$ is a genuine $(0,2)$-tensor field on the slice $\mathcal T_x:=\{q:(q,x)\in\mathcal T\}$. Hence
$$\nabla_qH:=\nabla\big(\nabla dE(\cdot,x)\big)=\nabla^3_qE(\cdot,x)$$
is the Levi-Civita covariant derivative of a tensor field: a $(0,3)$-tensor at $q$. Its norm is
$$\|\nabla_qH(q,x)\|:=\sup_{|z|=|v|=|w|=1}\big|(\nabla_z\mathbb H)(v,w)\big| .$$
**No parallel transport has to be inserted**: covariant differentiation of a tensor field already *is* the transport-corrected difference quotient. Concretely, if $s\mapsto q(s)$ is a curve with $\dot q(0)=z$ and $v(s),w(s)$ are **parallel** along it, then
$$(\nabla_z\mathbb H)(v,w)=\frac{d}{ds}\Big|_{0}\big\langle H(q(s),x)v(s),w(s)\big\rangle . \tag{A.1}$$
This is the only interpretation used below, and it is the one that makes "$H$ Lipschitz in $q$" meaningful:
$$\big\|\Pi_{q'\to q}\,H(q',x)\,\Pi_{q\to q'}-H(q,x)\big\|_{\rm op}\le\Big(\sup\|\nabla_qH\|\Big)\,d(q,q'), \tag{A.2}$$
$\Pi$ = parallel transport along the (unique) minimizing geodesic $q'\to q$, obtained by integrating (A.1) along that geodesic. Both operators in (A.2) act on $T_qM$: the subtraction is legal.

### A.3 $\nabla_xH$ — a plain differential into a *fixed* vector space

For **fixed $q$**, the map
$$x\longmapsto \mathbb H(q,x)\ \in\ \operatorname{Sym}^2T_q^*M$$
takes values in a vector space that **does not depend on $x$**. Therefore $\nabla_xH$ is just the ordinary differential of a vector-space-valued map on the slice $\mathcal T^q:=\{x:(q,x)\in\mathcal T\}$:
$$\nabla_xH(q,x)[\xi]:=\frac{d}{dr}\Big|_0\mathbb H\big(q,\eta(r)\big)\in\operatorname{Sym}^2T_q^*M,\qquad \dot\eta(0)=\xi\in T_xM,$$
$$\|\nabla_xH(q,x)\|:=\sup_{|\xi|=1}\big\|\nabla_xH(q,x)[\xi]\big\|_{\rm op}.$$
**No connector is required in the $x$-slot.** Consequently "Lipschitz in $x$" is unambiguous and needs no transport:
$$\big\|H(q,x)-H(q,x')\big\|_{\rm op}\le\Big(\sup\|\nabla_xH\|\Big)\,d(x,x'), \tag{A.3}$$
both operators acting on the *same* space $T_qM$. **This is exactly the object Theorem SW-AS calls $\|\partial_xH(q,x)\|\le L_H$**, and the addendum-II statement is type-correct as written. (By contrast the addendum-II phrase "$H$ Lipschitz in $q$", used implicitly in the $\epsilon$-net step, is *only* meaningful in the sense (A.2); the patch list in §M records this.)

### A.4 Sign and parametrisation conventions for geodesics

Throughout, geodesics between the two arguments are parametrised on the **unit interval**:
$$\gamma(t)=\exp_q(t\log_qx),\qquad t\in[0,1],\qquad T:=\dot\gamma,\qquad |T|\equiv L:=d(q,x)\le\rho^* .$$
$\nabla_t:=\nabla_{\partial_t}$, $\nabla_s:=\nabla_{\partial_s}$. With this parametrisation the Jacobi equation reads $\nabla_t^2J+R(J,T)T=0$ with $|T|=L$, so the *effective* curvature parameter that appears in every estimate is
$$\boxed{\ \kappa:=K_0L^2\le K_0\rho^{*2}\ }$$
which is dimensionless, as it must be.

---

## §D1. THE VARIATIONAL REPRESENTATION OF $H$ (derived)

Everything in this run rests on one identity, which is proved here rather than quoted.

> **Lemma 1 (Jacobi boundary-value representation of $H$).** Let $(q,x)\in\mathcal T$, $\gamma$ the minimizing geodesic on $[0,1]$ as in §A.4. For $w\in T_qM$ let $J_w$ be **the** Jacobi field along $\gamma$ with
> $$\nabla_t^2J_w+R(J_w,T)T=0,\qquad J_w(0)=w,\qquad J_w(1)=0 .$$
> (It exists and is unique because $x$ is not conjugate to $q$ along $\gamma$ — see Lemma 3 for the quantitative version.) Then
> $$\boxed{\ H(q,x)\,w=-\nabla_tJ_w(0)\ }\tag{D1.1}$$
> as an identity of vectors in $T_qM$, for every $w$.

**Proof.** Let $c$ be the geodesic with $c(0)=q$, $\dot c(0)=w$, and define the smooth variation
$$\sigma(s,t):=\exp_{c(s)}\big(t\log_{c(s)}x\big),\qquad (s,t)\in(-\varepsilon,\varepsilon)\times[0,1],$$
which is well defined and smooth for $\varepsilon$ small because $\mathcal T$ is open and the minimizing geodesic depends smoothly on its endpoints there. Each $t\mapsto\sigma(s,\cdot)$ is a geodesic from $c(s)$ to $x$; a geodesic parametrised on $[0,1]$ has energy equal to half its squared length, so
$$\mathcal E(s):=\tfrac12\int_0^1|\partial_t\sigma(s,t)|^2\,dt=\tfrac12 d\big(c(s),x\big)^2=E\big(c(s),x\big). \tag{D1.2}$$
Write $J:=\partial_s\sigma$, $T:=\partial_t\sigma$; note $\nabla_sT=\nabla_tJ$ (symmetry of the connection) and $\nabla_tT=0$.

*First variation.*
$$\mathcal E'(s)=\int_0^1\langle\nabla_sT,T\rangle\,dt=\int_0^1\langle\nabla_tJ,T\rangle\,dt=\big[\langle J,T\rangle\big]_0^1-\int_0^1\langle J,\nabla_tT\rangle\,dt=\big[\langle J,T\rangle\big]_0^1 .$$
At $t=1$, $\sigma(s,1)\equiv x$, so $J(s,1)=0$; at $t=0$, $J(s,0)=\dot c(s)$ and $T(s,0)=\log_{c(s)}x$. Hence
$$\mathcal E'(s)=-\big\langle\dot c(s),\log_{c(s)}x\big\rangle,$$
which re-derives $\operatorname{grad}_qE(\cdot,x)=-\log_qx$ and confirms the convention.

*Second variation.* Differentiating once more,
$$\mathcal E''(s)=\int_0^1\Big(|\nabla_tJ|^2+\langle\nabla_s\nabla_tJ,T\rangle\Big)dt .$$
By the definition of curvature, $\nabla_s\nabla_tJ=\nabla_t\nabla_sJ+R(J,T)J$ (the last argument is $J=\partial_s\sigma$). Therefore
$$\int_0^1\langle\nabla_s\nabla_tJ,T\rangle=\int_0^1\langle\nabla_t\nabla_sJ,T\rangle+\int_0^1\langle R(J,T)J,T\rangle
=\big[\langle\nabla_sJ,T\rangle\big]_0^1-\int_0^1\langle\nabla_sJ,\nabla_tT\rangle+\int_0^1\langle R(J,T)J,T\rangle .$$
The middle integral vanishes ($\nabla_tT=0$). The boundary term vanishes at **both** ends: at $t=1$ because $J(s,1)\equiv0$ for all $s$, hence $\nabla_sJ(s,1)=0$; at $t=0$ because $J(s,0)=\dot c(s)$ and $c$ is a **geodesic**, hence $\nabla_sJ(s,0)=\nabla_s\dot c=0$. Using the pair symmetry $\langle R(J,T)J,T\rangle=-\langle R(J,T)T,J\rangle$,
$$\mathcal E''(0)=\int_0^1\Big(|\nabla_tJ|^2-\langle R(J,T)T,J\rangle\Big)dt=:I(J,J), \tag{D1.3}$$
the index form. Since $c$ is a geodesic, $\mathcal E''(0)=\operatorname{Hess}_qE(\cdot,x)(w,w)=\langle H(q,x)w,w\rangle$.

*Identification.* $J(0,\cdot)=\partial_s\sigma(0,\cdot)$ is the variation field of a family of geodesics, hence a Jacobi field, with $J(0,0)=w$ and $J(0,1)=0$; by uniqueness $J(0,\cdot)=J_w$. Integrating (D1.3) by parts once more and using the Jacobi equation,
$$I(J_w,J_w)=\big[\langle\nabla_tJ_w,J_w\rangle\big]_0^1-\int_0^1\big\langle\nabla_t^2J_w+R(J_w,T)T,\,J_w\big\rangle\,dt=-\big\langle\nabla_tJ_w(0),w\big\rangle .$$
Thus $\langle H(q,x)w,w\rangle=-\langle\nabla_tJ_w(0),w\rangle$ for every $w$. The map $w\mapsto -\nabla_tJ_w(0)$ is linear (the BVP is linear in its data) and $H$ is self-adjoint, so equality of the two quadratic forms upgrades to equality of the operators by polarisation. $\blacksquare$

---

## §B. EUCLIDEAN SANITY CHECK

On $\mathbb R^p$, $R\equiv0$, so the Jacobi equation is $\nabla_t^2J=J''=0$, and the BVP $J(0)=w$, $J(1)=0$ has the unique solution $J_w(t)=(1-t)w$, whence $J_w'(0)=-w$ and, by Lemma 1,
$$H(q,x)w=-J_w'(0)=w\qquad\Longrightarrow\qquad H(q,x)=\mathrm{Id}\ \ \text{for all }q,x .$$
Independently: $E(q,x)=\tfrac12|x-q|^2$ has $\operatorname{Hess}_q=\mathrm{Id}$. The two agree, confirming the sign convention in (D1.1). Since $H$ is the constant field $\mathrm{Id}$,
$$\nabla_qH=0,\qquad \nabla_xH=0 .$$
Consistent with Theorem H-LIP below, whose constant vanishes when $K_0=K_1=0$. $\square$

---

## §D2. THE DIFFERENTIATED JACOBI EQUATION (every term tracked)

Let $s\mapsto(q(s),x(s))$ be a smooth curve in $\mathcal T$ and let
$$\Gamma(s,t):=\exp_{q(s)}\big(t\log_{q(s)}x(s)\big),\qquad T:=\partial_t\Gamma,\quad S:=\partial_s\Gamma .$$
$\Gamma(s,\cdot)$ is a geodesic for each $s$, so $\nabla_tT=0$ and $S$ is a **Jacobi field in $t$**:
$$\nabla_t^2S+R(S,T)T=0,\qquad S(s,0)=\dot q(s),\qquad S(s,1)=\dot x(s). \tag{D2.1}$$
Let $w(s)$ be a vector field along $s\mapsto q(s)$ and let $J(s,\cdot)$ be the Jacobi field with $J(s,0)=w(s)$, $J(s,1)=0$, so that by Lemma 1
$$\big\langle H(q(s),x(s))\,w(s),\,w(s)\big\rangle=-\big\langle\nabla_tJ(s,0),\,w(s)\big\rangle. \tag{D2.2}$$
Put $Y:=\nabla_sJ$.

> **Lemma 2 (the $Y$-equation).** $Y$ satisfies the **inhomogeneous Jacobi equation**
> $$\boxed{\ \nabla_t^2Y+R(Y,T)T=-\mathcal F\ },\qquad Y(s,0)=\nabla_sw(s),\quad Y(s,1)=0,$$
> with forcing
> $$\mathcal F=\underbrace{(\nabla_SR)(J,T)T+(\nabla_TR)(S,T)J}_{\textstyle \mathcal F_{\nabla R}}\;+\;\underbrace{R(J,\nabla_tS)T+R(J,T)\nabla_tS+R(\nabla_tS,T)J+2R(S,T)\nabla_tJ}_{\textstyle \mathcal F_{R}} .$$

**Proof.** Commute derivatives on the second-order term. Using $\nabla_s\nabla_tA=\nabla_t\nabla_sA+R(S,T)A$ twice,
$$\nabla_s\nabla_t^2J=\nabla_t\big(\nabla_s\nabla_tJ\big)+R(S,T)\nabla_tJ
=\nabla_t\big(\nabla_t\nabla_sJ+R(S,T)J\big)+R(S,T)\nabla_tJ,$$
$$=\nabla_t^2Y+\nabla_t\big[R(S,T)J\big]+R(S,T)\nabla_tJ .$$
Since $\nabla_tT=0$, the product rule for the $(1,3)$-tensor $R$ gives
$$\nabla_t\big[R(S,T)J\big]=(\nabla_TR)(S,T)J+R(\nabla_tS,T)J+R(S,T)\nabla_tJ .$$
Next, the curvature term. Using again $\nabla_sT=\nabla_tS$,
$$\nabla_s\big[R(J,T)T\big]=(\nabla_SR)(J,T)T+R(\nabla_sJ,T)T+R(J,\nabla_tS)T+R(J,T)\nabla_tS$$
$$=(\nabla_SR)(J,T)T+R(Y,T)T+R(J,\nabla_tS)T+R(J,T)\nabla_tS .$$
Adding the two displays and setting $\nabla_s\big[\nabla_t^2J+R(J,T)T\big]=0$ yields the stated equation with the stated $\mathcal F$. The boundary conditions follow from $J(s,0)=w(s)$ and $J(s,1)\equiv0$. $\blacksquare$

> **Answer to the question posed in the brief (attack order D).** A term of the form $(\nabla_{\partial_s}R)(J,T)T$ **does** appear — and so does a *second*, structurally different $\nabla R$ term, $(\nabla_TR)(S,T)J$, which arises from differentiating the *transport* of the curvature operator along the geodesic and is easy to miss. Both are collected in $\mathcal F_{\nabla R}$. **At this stage the only legitimate conclusion is: this natural differentiated-Jacobi proof requires control of $\nabla R$.** Whether the *theorem* requires it is a separate question, taken up in §F.

### D2.1 The derivative of $H$ in terms of $Y$

> **Lemma 2′.** With $w(s)$ **parallel** along $s\mapsto q(s)$ (so $\nabla_sw=0$, hence $Y(s,0)=0=Y(s,1)$),
> $$\frac{d}{ds}\big\langle H(q(s),x(s))w,w\big\rangle=-\big\langle\nabla_tY(s,0),\,w\big\rangle-\big\langle R\big(\dot q(s),T(s,0)\big)w,\,w\big\rangle. \tag{D2.3}$$

**Proof.** Differentiate (D2.2). Since $\nabla_sw=0$,
$$\frac{d}{ds}\big\langle H w,w\big\rangle=-\big\langle\nabla_s\nabla_tJ(s,0),w\big\rangle
=-\big\langle\nabla_t\nabla_sJ(s,0)+R(S,T)J\big|_{t=0},\,w\big\rangle,$$
and at $t=0$: $S(s,0)=\dot q(s)$, $J(s,0)=w$. $\blacksquare$

By §A.2, the left side of (D2.3) is exactly $(\nabla_{\dot q}\mathbb H)(w,w)$ when $\dot x=0$, and exactly $\nabla_x\mathbb H[\dot x](w,w)$ when $\dot q=0$. **Both derivatives are computed by the same formula.** Note the second term of (D2.3) drops out identically in the $x$-derivative, since then $\dot q=0$.

Finally, in a frame parallel along $s\mapsto q(s)$ the matrix of $\mathbb H(q(s),x(s))$ is a curve of symmetric matrices, so its $s$-derivative is a symmetric bilinear form and
$$\big\|\nabla_\bullet\mathbb H\big\|_{\rm op}=\sup_{|w|=1}\big|(\nabla_\bullet\mathbb H)(w,w)\big| . \tag{D2.4}$$
Hence a bound on (D2.3) for all unit $w$ **is** a bound on $\|\nabla_qH\|$ and $\|\nabla_xH\|$.

---

## §E. THE QUANTITATIVE ESTIMATES

All four lemmas below are proved from scratch. Throughout, $\gamma$ is a fixed geodesic on $[0,1]$ with $|T|\equiv L$, $\kappa:=K_0L^2$, and all fields are along $\gamma$.

### E.1 The energy/Grönwall bound for the initial-value problem

> **Lemma 3 (IVP bound).** Let $Z$ solve $\nabla_t^2Z+R(Z,T)T=-F$ on $[0,1]$. Then
> $$\Big(|Z(t)|^2+|\nabla_tZ(t)|^2\Big)^{1/2}\ \le\ e^{(1+\kappa)|t-t_0|/2}\left[\Big(|Z(t_0)|^2+|\nabla_tZ(t_0)|^2\Big)^{1/2}+\int_{t_0\wedge t}^{t_0\vee t}|F(\tau)|\,d\tau\right].$$
> In particular, with $\Lambda:=e^{(1+\kappa)/2}$ and $t_0=0$,
> $$\sup_{[0,1]}\big(|Z|+|\nabla_tZ|\big)\ \le\ \sqrt2\,\Lambda\left[\big(|Z(0)|^2+|\nabla_tZ(0)|^2\big)^{1/2}+\|F\|_{L^1[0,1]}\right]. \tag{E.1}$$

**Proof.** Set $\mathcal Q(t):=|Z|^2+|\nabla_tZ|^2$. Then
$$\mathcal Q'=2\langle Z,\nabla_tZ\rangle+2\langle\nabla_tZ,\nabla_t^2Z\rangle=2\langle Z,\nabla_tZ\rangle-2\langle\nabla_tZ,R(Z,T)T\rangle-2\langle\nabla_tZ,F\rangle .$$
Now $|R(Z,T)T|\le K_0|Z||T|^2=\kappa|Z|$, so by Cauchy–Schwarz
$$|\mathcal Q'|\le 2|Z||\nabla_tZ|+2\kappa|Z||\nabla_tZ|+2|\nabla_tZ||F|\le(1+\kappa)\mathcal Q+2\sqrt{\mathcal Q}\,|F|,$$
using $2|Z||\nabla_tZ|\le\mathcal Q$ and $|\nabla_tZ|\le\sqrt{\mathcal Q}$. Where $\mathcal Q>0$, $\big|\tfrac{d}{dt}\sqrt{\mathcal Q}\big|=\tfrac{|\mathcal Q'|}{2\sqrt{\mathcal Q}}\le\tfrac{1+\kappa}{2}\sqrt{\mathcal Q}+|F|$; the differential inequality integrates by Grönwall (and extends across zeros of $\mathcal Q$ by continuity, $\sqrt{\mathcal Q}$ being locally Lipschitz). The final display uses $|Z|+|\nabla_tZ|\le\sqrt2\sqrt{\mathcal Q}$. $\blacksquare$

### E.2 Quantitative non-conjugacy

Let $\mathcal A:T_qM\to T_{\gamma(1)}M$ be the linear map $a\mapsto Z_a(1)$, where $Z_a$ is the Jacobi field with $Z_a(0)=0$, $\nabla_tZ_a(0)=a$. Non-conjugacy of $x$ to $q$ along $\gamma$ is exactly invertibility of $\mathcal A$; the **quantitative** version is the standing hypothesis

> **(NC)** $\ \mathcal A$ is invertible and $\ \Theta:=\sup_{\mathcal T}\ \|\mathcal A^{-1}\|_{\rm op}<\infty .$

> **Lemma 4 (two regimes in which (NC) is free, with explicit $\Theta$).**
> **(i) Non-positive curvature.** If $K\le0$ on $\mathcal T$ then $|Z_a(1)|\ge|a|$, so **(NC) holds with $\Theta=1$**, with no restriction on $L$.
> **(ii) Small tube.** If $|R|\le K_0$ and $\kappa=K_0L^2<1$ then $|Z_a(1)|\ge\frac{2-2\kappa}{2-\kappa}|a|$, so **(NC) holds with $\Theta\le\frac{2-\kappa}{2-2\kappa}$.**

**Proof of (i).** Let $g(t):=|Z_a(t)|$. On any interval where $Z_a\ne0$, $g$ is smooth and
$$g\,g''=\langle Z_a,\nabla_t^2Z_a\rangle+|\nabla_tZ_a|^2-(g')^2 .$$
Now $\langle Z_a,\nabla_t^2Z_a\rangle=-\langle R(Z_a,T)T,Z_a\rangle=-K(Z_a,T)\big(|Z_a|^2|T|^2-\langle Z_a,T\rangle^2\big)\ge0$ because $K\le0$ and the Gram determinant is $\ge0$; and $(g')^2=\langle Z_a,\nabla_tZ_a\rangle^2/|Z_a|^2\le|\nabla_tZ_a|^2$ by Cauchy–Schwarz. Hence $g''\ge0$: $g$ is convex. Also $g(0)=0$ and $g(t)/t\to|\nabla_tZ_a(0)|=|a|$ as $t\downarrow0$ (Taylor). Convexity with $g(0)=0$ makes $t\mapsto g(t)/t$ non-decreasing, so $g(1)\ge|a|$. (Regularity: $g$ is continuous on $[0,1]$ and smooth wherever $Z_a\ne0$. Let $(0,t_1)$ be the maximal interval on which $Z_a\ne0$; on it $g$ is convex with $g(0)=0$, so $g(t)/t$ is non-decreasing there and $g(t)\ge t|a|>0$ for $t\in(0,t_1)$. Letting $t\uparrow t_1$ gives $g(t_1)\ge t_1|a|>0$, contradicting $Z_a(t_1)=0$; hence $t_1=1$ and $g(1)\ge|a|$.) 

**Proof of (ii).** Work in a frame parallel along $\gamma$, in which the equation is the linear ODE $Z''=-\mathcal R(t)Z$ with $\mathcal R(t)A=R(A,T)T$, $\|\mathcal R(t)\|_{\rm op}\le K_0L^2=\kappa$. Integrating twice from $0$ with $Z(0)=0$, $Z'(0)=a$,
$$Z(t)=ta-\int_0^t(t-\tau)\mathcal R(\tau)Z(\tau)\,d\tau .$$
Let $N:=\sup_{[0,1]}|Z|$. Taking norms at $t\le1$: $|Z(t)|\le|a|+\tfrac{\kappa}{2}N$, so $N\le|a|+\tfrac\kappa2N$, i.e. $N\le|a|/(1-\tfrac\kappa2)$ when $\kappa<2$. Then
$$|Z(1)-a|\le\tfrac\kappa2N\le\frac{\kappa|a|}{2-\kappa},\qquad\text{so}\qquad |Z(1)|\ge|a|\Big(1-\frac{\kappa}{2-\kappa}\Big)=\frac{2-2\kappa}{2-\kappa}|a| . \qquad\blacksquare$$

**Remark.** Under (H1) of the project — Cartan–Hadamard, $-\bar K\le K\le0$ — case (i) applies and **$\Theta=1$ is free, for every tube radius**. Case (ii) is what a two-sided-curvature manifold with no sign hypothesis costs.

### E.3 The homogeneous boundary-value problem

> **Lemma 5 (BVP bound).** Assume (NC). Let $Z$ be the Jacobi field with $Z(0)=z_0$, $Z(1)=z_1$. Then
> $$\sup_{[0,1]}\big(|Z|+|\nabla_tZ|\big)\ \le\ C_J\big(|z_0|+|z_1|\big),\qquad C_J:=\sqrt2\,\Lambda\big(1+\Theta+\Theta\Lambda\big),\quad\Lambda=e^{(1+\kappa)/2} .$$

**Proof.** Decompose $Z=P+Z_a$ where $P$ is the Jacobi field with $P(0)=z_0$, $\nabla_tP(0)=0$, and $Z_a$ is as in §E.2. Existence and uniqueness of this decomposition is exactly (NC): we need $Z_a(1)=z_1-P(1)$, i.e. $a=\mathcal A^{-1}(z_1-P(1))$. By Lemma 3 with $F=0$, $\sup(|P|+|\nabla_tP|)\le\sqrt2\Lambda|z_0|$, hence $|P(1)|\le\sqrt2\Lambda|z_0|$; more sharply $|P(1)|\le\Lambda|z_0|$ since $\sqrt{\mathcal Q_P(1)}\le\Lambda\sqrt{\mathcal Q_P(0)}=\Lambda|z_0|$ and $|P(1)|\le\sqrt{\mathcal Q_P(1)}$. Therefore $|a|\le\Theta(|z_1|+\Lambda|z_0|)$, and again by Lemma 3, $\sup(|Z_a|+|\nabla_tZ_a|)\le\sqrt2\Lambda|a|$. Adding,
$$\sup(|Z|+|\nabla_tZ|)\le\sqrt2\Lambda|z_0|+\sqrt2\Lambda\Theta(|z_1|+\Lambda|z_0|)\le C_J(|z_0|+|z_1|). \qquad\blacksquare$$

### E.4 The inhomogeneous problem with zero boundary data

> **Lemma 6 (forced BVP; the only place the forcing enters).** Assume (NC). Let $Y$ solve $\nabla_t^2Y+R(Y,T)T=-\mathcal F$ with $Y(0)=Y(1)=0$. Then, in a parallel frame, writing $\Psi(t,\tau)$ for the matrix solution of $\partial_t^2\Psi+\mathcal R\Psi=0$, $\Psi(\tau,\tau)=0$, $\partial_t\Psi(\tau,\tau)=\mathrm{Id}$,
> $$\nabla_tY(0)=\mathcal A^{-1}\!\left[\int_0^1\Psi(1,\tau)\,\mathcal F(\tau)\,d\tau\right],\tag{E.2}$$
> and consequently
> $$\big|\nabla_tY(0)\big|\ \le\ \Theta\left\|\int_0^1\Psi(1,\tau)\mathcal F(\tau)\,d\tau\right\|\ \le\ \Theta\,\Lambda\,\|\mathcal F\|_{L^1[0,1]}\ \le\ \Theta\Lambda\,\|\mathcal F\|_\infty . \tag{E.3}$$

**Proof.** Let $Y_0$ solve the same forced equation with $Y_0(0)=0$, $\nabla_tY_0(0)=0$. Duhamel's principle for the second-order linear system $Y_0''=-\mathcal RY_0-\mathcal F$ gives $Y_0(t)=-\int_0^t\Psi(t,\tau)\mathcal F(\tau)d\tau$ — verified directly: the right side vanishes at $t=0$ together with its $t$-derivative (because $\Psi(t,t)=0$), and
$\partial_t^2Y_0=-\partial_t\Psi(t,t)\mathcal F(t)-\int_0^t\partial_t^2\Psi(t,\tau)\mathcal F(\tau)d\tau=-\mathcal F(t)+\mathcal R\int_0^t\Psi\mathcal F=-\mathcal F-\mathcal RY_0$. ✓
Then $Y=Y_0+Z_a$ with $Z_a(0)=0$, $\nabla_tZ_a(0)=a$, and $Y(1)=0$ forces $\mathcal Aa=-Y_0(1)=\int_0^1\Psi(1,\tau)\mathcal F(\tau)d\tau$, which is (E.2) since $\nabla_tY(0)=a$. For (E.3): each column of $\tau\mapsto\Psi(\cdot,\tau)$ is a Jacobi field with zero value and unit-norm derivative at $t=\tau$, so Lemma 3 (with $F=0$, $t_0=\tau$) gives $\|\Psi(1,\tau)\|_{\rm op}\le\Lambda$ for every $\tau\in[0,1]$. $\blacksquare$

**Note.** (E.3) records *two* bounds. The middle expression — the norm of a **smoothed integral** of $\mathcal F$ — is what the proof actually uses; the right-hand $\|\mathcal F\|_\infty$ is a crude relaxation of it. §F exploits exactly this gap.

### E.5 The forcing bound

> **Lemma 7.** With $\mathcal S:=\sup_{[0,1]}(|S|+|\nabla_tS|)$ and $\mathcal J:=\sup_{[0,1]}(|J|+|\nabla_tJ|)$,
> $$\|\mathcal F_{\nabla R}\|_\infty\le 2K_1L^2\,\mathcal S\mathcal J,\qquad \|\mathcal F_{R}\|_\infty\le 5K_0L\,\mathcal S\mathcal J,$$
> hence $\|\mathcal F\|_\infty\le\big(2K_1L^2+5K_0L\big)\mathcal S\mathcal J$.

**Proof.** Term by term, using $|T|=L$ and the definitions of $K_0,K_1$:
$$|(\nabla_SR)(J,T)T|\le K_1|S||J|L^2,\qquad |(\nabla_TR)(S,T)J|\le K_1L\,|S|\,L\,|J|=K_1L^2|S||J| ;$$
$$|R(J,\nabla_tS)T|\le K_0|J||\nabla_tS|L,\quad |R(J,T)\nabla_tS|\le K_0|J|L|\nabla_tS|,\quad |R(\nabla_tS,T)J|\le K_0|\nabla_tS|L|J|,$$
$$|2R(S,T)\nabla_tJ|\le 2K_0|S|L|\nabla_tJ| .$$
Bounding each of $|S|,|\nabla_tS|$ by $\mathcal S$ and each of $|J|,|\nabla_tJ|$ by $\mathcal J$ and summing gives $2K_1L^2\mathcal S\mathcal J$ and $(1+1+1+2)K_0L\mathcal S\mathcal J$. $\blacksquare$

---

## §B(main). THEOREM H-LIP

> ### THEOREM H-LIP.
> Let $\mathcal T$ be a geodesic tube: every pair $(q,x)\in\mathcal T$ is joined by a unique minimizing geodesic of length $\le\rho^*$, depending smoothly on the endpoints, along which $x$ is not conjugate to $q$. Assume on $\mathcal T$
> $$|R|\le K_0,\qquad |\nabla R|\le K_1,\qquad \textbf{(NC)}\ \ \|\mathcal A^{-1}\|\le\Theta .$$
> Put $\kappa:=K_0\rho^{*2}$, $\Lambda:=e^{(1+\kappa)/2}$, $C_J:=\sqrt2\Lambda(1+\Theta+\Theta\Lambda)$. Then for all $(q,x)\in\mathcal T$
> $$\boxed{\ \big\|\nabla_xH(q,x)\big\|\ \le\ \Theta\Lambda\,C_J^2\big(2K_1\rho^{*2}+5K_0\rho^{*}\big)\ }$$
> $$\boxed{\ \big\|\nabla_qH(q,x)\big\|\ \le\ K_0\rho^*+\Theta\Lambda\,C_J^2\big(2K_1\rho^{*2}+5K_0\rho^{*}\big)\ }$$
> and hence
> $$\sup_{(q,x)\in\mathcal T}\Big(\|\nabla_qH\|+\|\nabla_xH\|\Big)\ \le\ L_H:=K_0\rho^*+2\,\Theta\Lambda\,C_J^2\big(2K_1\rho^{*2}+5K_0\rho^{*}\big)\ <\ \infty .$$
> Consequently (A.2)–(A.3): $H$ is $L_H$-Lipschitz in $x$ (no transport needed) and $L_H$-Lipschitz in $q$ modulo parallel transport, uniformly on $\mathcal T$.
>
> **Under (H1) (Cartan–Hadamard, $-\bar K\le K\le0$)** Lemma 4(i) gives $\Theta=1$ **free**, so with $K_0=\bar K$:
> $$L_H\ \le\ \bar K\rho^*+2\Lambda C_J^2\big(2K_1\rho^{*2}+5\bar K\rho^*\big),\qquad \Lambda=e^{(1+\bar K\rho^{*2})/2},\ \ C_J=\sqrt2\Lambda(2+\Lambda).$$

**Proof.** Fix $(q,x)\in\mathcal T$ and a unit $w\in T_qM$. By (D2.4) it suffices to bound $\big|\tfrac{d}{ds}\langle H(q(s),x(s))w(s),w(s)\rangle\big|$ at $s=0$ for curves $(q(s),x(s))$ with $w$ parallel along $q(\cdot)$, in the two cases $\dot x=0$ (giving $\nabla_qH$, direction $\dot q$, $|\dot q|=1$) and $\dot q=0$ (giving $\nabla_xH$, direction $\dot x$, $|\dot x|=1$).

By Lemma 2′,
$$\Big|\frac{d}{ds}\langle Hw,w\rangle\Big|\ \le\ \big|\nabla_tY(0)\big|\,|w|+K_0|\dot q|\,L\,|w|^2 . \tag{P.1}$$

*Bound on $\mathcal J$.* $J(\cdot)$ is the Jacobi field with $J(0)=w$, $J(1)=0$; Lemma 5 gives $\mathcal J\le C_J|w|=C_J$.

*Bound on $\mathcal S$.* By (D2.1) $S$ is a Jacobi field with $S(0)=\dot q$, $S(1)=\dot x$; Lemma 5 gives $\mathcal S\le C_J(|\dot q|+|\dot x|)=C_J$ in each of the two cases.

*Bound on the forcing.* Lemma 7 with $L\le\rho^*$:
$$\|\mathcal F\|_\infty\ \le\ \big(2K_1\rho^{*2}+5K_0\rho^*\big)\,\mathcal S\mathcal J\ \le\ \big(2K_1\rho^{*2}+5K_0\rho^*\big)C_J^2 .$$

*Bound on $\nabla_tY(0)$.* $Y=\nabla_sJ$ satisfies the hypotheses of Lemma 6: $Y(0)=\nabla_sw=0$ because $w$ is parallel, and $Y(1)=\nabla_s(0)=0$. Hence by (E.3)
$$\big|\nabla_tY(0)\big|\ \le\ \Theta\Lambda\,\|\mathcal F\|_\infty\ \le\ \Theta\Lambda\,C_J^2\big(2K_1\rho^{*2}+5K_0\rho^*\big).$$

*Assembly.* For $\nabla_x H$ we have $\dot q=0$, so the second term of (P.1) vanishes identically and $\|\nabla_xH\|\le\Theta\Lambda C_J^2(2K_1\rho^{*2}+5K_0\rho^*)$. For $\nabla_qH$ we have $|\dot q|=1$ and $L\le\rho^*$, adding $K_0\rho^*$. Taking suprema over unit $w$ and over $\mathcal T$, and using (D2.4), gives the two boxed displays; summing gives $L_H$. $\blacksquare$

> **Dependence on the assumptions, explicitly (as the brief requires).**
> * $K_1$ enters **linearly**, through the single factor $2K_1\rho^{*2}$, and **only** through $\mathcal F_{\nabla R}$.
> * $K_0$ enters **linearly** in the visible factors and **exponentially** through $\Lambda=e^{(1+K_0\rho^{*2})/2}$ inside $C_J$; the total $K_0$-dependence is $O\!\big(K_0\rho^*e^{3(1+K_0\rho^{*2})/2}\big)$ at fixed $\Theta$.
> * $\rho^*$ enters both explicitly and through $\kappa=K_0\rho^{*2}$.
> * $\Theta$ enters **cubically** ($\Theta$ from Lemma 6, $\Theta^2$ from $C_J^2$) — and §C shows this is not an artefact: $L_H$ genuinely blows up as $\Theta\to\infty$.
> * The injectivity radius $i_0$ enters **only** through the standing requirement that $\mathcal T$ be a tube of unique minimizing geodesics; given that, $i_0$ appears nowhere in the constant. On Cartan–Hadamard $i_0=\infty$ and the tube condition is automatic for every $\rho^*$.
> * $p=\dim M$ appears **nowhere**. The constant is dimension-free given $(K_0,K_1,\rho^*,\Theta)$. This is the fact that §J turns into the high-dimensional statement.

---

## §C. CONSTANT CURVATURE — WHAT IT DOES AND DOES NOT SHOW

Here $\nabla R\equiv0$ ($K_1=0$) and Lemma 1 can be solved in closed form, which lets us compute $\nabla H$ **exactly** and test the theorem.

### C.1 Radial/tangential decomposition and the eigenvalues of $H$ (derived, not cited)

Let $K\equiv\varepsilon c^2$ with $\varepsilon=-1$ (hyperbolic, $c=\sqrt{\bar K}$) or $\varepsilon=+1$ (sphere). In constant curvature $R(A,B)C=\varepsilon c^2\big(\langle B,C\rangle A-\langle A,C\rangle B\big)$, so for a field $J$ along $\gamma$, splitting $J=J_\parallel+J_\perp$ with $J_\parallel\parallel T$:
$$R(J,T)T=\varepsilon c^2\big(|T|^2J-\langle J,T\rangle T\big)=\varepsilon c^2L^2\,J_\perp .$$
The Jacobi equation therefore decouples:
$$\nabla_t^2J_\parallel=0,\qquad \nabla_t^2J_\perp+\varepsilon c^2L^2J_\perp=0 .$$
Write $\theta:=cL=\sqrt{|K|}\,d(q,x)$.

*Radial.* $J_\parallel(0)=w_\parallel$, $J_\parallel(1)=0$ gives $J_\parallel(t)=(1-t)w_\parallel$, $\nabla_tJ_\parallel(0)=-w_\parallel$, so by Lemma 1 the radial eigenvalue of $H$ is
$$\mu_{\rm rad}=1 \qquad\text{(for both signs, all }\theta).$$
*Tangential, $\varepsilon=-1$.* $J_\perp''=\theta^2J_\perp$, so $J_\perp(t)=w_\perp\frac{\sinh(\theta(1-t))}{\sinh\theta}$, $\nabla_tJ_\perp(0)=-\theta\coth\theta\,w_\perp$:
$$\mu_{\rm tan}=\theta\coth\theta .$$
*Tangential, $\varepsilon=+1$.* $J_\perp''=-\theta^2J_\perp$, so $J_\perp(t)=w_\perp\frac{\sin(\theta(1-t))}{\sin\theta}$ (well defined iff $\theta\notin\pi\mathbb Z$, i.e. no conjugate point):
$$\mu_{\rm tan}=\theta\cot\theta .$$

> **This derives T-EXT-1 rather than citing it.** On $\mathbb H^p(-1)$ the eigenvalues of $\tfrac12\operatorname{Hess}_qd(x,\cdot)^2$ are exactly $1$ (radial) and $\theta\coth\theta$ (orthogonal), $\theta=d(x,q)$; and since $\theta\coth\theta\ge1$ with equality only at $\theta=0$, $\ \mathrm{Id}\preceq H$. The upper bound $H\preceq\zeta(d)\mathrm{Id}$, $\zeta(\rho)=\sqrt{\bar K}\rho\coth(\sqrt{\bar K}\rho)$, for general $-\bar K\le K\le0$ is **not** proved by this computation (it needs a comparison argument) and remains as recorded in the ledger; but the constant-curvature *equality* case, which is what CE-9 and the (G7) sharpness argument actually consume, is now self-contained.

### C.2 Differentiating the eigenvalues — hyperbolic

$\mu_{\rm tan}(L)=\theta\coth\theta$, $\theta=cL$, so
$$\frac{d\mu_{\rm tan}}{dL}=c\left(\coth\theta-\frac{\theta}{\sinh^2\theta}\right)=:c\,\varphi(\theta).$$
$\varphi(\theta)=\frac{\sinh\theta\cosh\theta-\theta}{\sinh^2\theta}$. As $\theta\downarrow0$, $\sinh\theta\cosh\theta=\theta+\tfrac23\theta^3+O(\theta^5)$ and $\sinh^2\theta=\theta^2+O(\theta^4)$, so $\varphi(\theta)=\tfrac23\theta+O(\theta^3)\to0$. As $\theta\to\infty$, $\varphi\to1$. Both bounds $0\le\varphi\le1$ hold for every $\theta>0$, and both are elementary:
$$\varphi\ge0\iff\sinh\theta\cosh\theta\ge\theta\iff\tfrac12\sinh(2\theta)\ge\theta,\quad\text{true};$$
$$\varphi\le1\iff\sinh\theta\cosh\theta-\theta\le\sinh^2\theta\iff\sinh\theta\,(\cosh\theta-\sinh\theta)\le\theta\iff\tfrac12\big(1-e^{-2\theta}\big)\le\theta,$$
the last because $1-e^{-2\theta}\le2\theta$. Hence
$$0\le\frac{d\mu_{\rm tan}}{dL}\le c=\sqrt{\bar K}\qquad\textbf{uniformly in }L .$$
**Conclusion (hyperbolic).** The radial derivative of the eigenvalues of $H$ is bounded by $\sqrt{\bar K}$ **alone** — no dependence on $\rho^*$ at all, and no blow-up at any radius. So in constant *negative* curvature, $|\nabla H|$ **is** controlled by curvature magnitude alone.

*(Completeness: moving $x$ transversally also rotates the eigenframe. The rotation rate is $|\nabla_tS(0)|/L$ where $S$ is the Jacobi field with $S(0)=0$, $|S(1)|=1$; from §C.1, $|S(t)|=\sinh(\theta t)/(\theta)\cdot|\nabla_tS(0)|\cdot 1$, so $|\nabla_tS(0)|=\theta/\sinh\theta$ and the angular rate at $q$ is $c/\sinh\theta$. The induced change in $H$ is at most twice the spectral gap times this rate, i.e. $\le 2c\,\frac{\theta\coth\theta-1}{\sinh\theta}$, which tends to $0$ at both $\theta\to0$ ($\sim\tfrac13c\theta$) and $\theta\to\infty$ ($\sim2c\theta e^{-\theta}$) and is therefore bounded by an absolute multiple of $c$. So the full $\|\nabla_xH\|\le C\sqrt{\bar K}$ in constant negative curvature.)*

### C.3 Differentiating the eigenvalues — sphere, and the conjugate radius

$\mu_{\rm tan}(L)=\theta\cot\theta$, so
$$\frac{d\mu_{\rm tan}}{dL}=c\left(\cot\theta-\frac{\theta}{\sin^2\theta}\right).$$
As $\theta\uparrow\pi$ (the first conjugate radius $L=\pi/c$), $\sin\theta\sim(\pi-\theta)$ and
$$\frac{d\mu_{\rm tan}}{dL}\sim-\frac{c\,\pi}{(\pi-\theta)^2}\ \longrightarrow\ -\infty .$$
Meanwhile the curvature bound $K_0=c^2$ and $|\nabla R|=0$ are **fixed**.

> **PROVED (negative result).** There is **no** bound of the form
> $$\|\nabla_xH(q,x)\|\le C\big(K_0,K_1\big)$$
> — not even with $K_1=0$ and $\nabla R\equiv0$ — that is uniform over all pairs $(q,x)$ with $|R|\le K_0$. Any such bound must degrade as the pair approaches the conjugate locus. Quantitatively, at $\theta=cL$ close to $\pi$ the constant must be at least $c\pi/(\pi-\theta)^2$.
>
> **This is exactly the role of $\Theta$.** For the sphere, $Z_a(t)=a\sin(\theta t)/\theta$, so $|Z_a(1)|=|a|\sin\theta/\theta$ and $\Theta=\theta/\sin\theta\to\infty$ as $\theta\to\pi$, at the rate $\pi/(\pi-\theta)$; Theorem H-LIP's $\Theta^3$ therefore blows up like $(\pi-\theta)^{-3}$ against a true rate of $(\pi-\theta)^{-2}$. **The structure of the theorem is right; the power of $\Theta$ is not sharp.**

### C.4 Summary of what constant curvature settles

| Question | Constant-curvature answer |
|---|---|
| Is $H$ itself controlled by $K_0,\rho^*$? | Yes: $\mu\in\{1,\theta\coth\theta\}$ (hyperbolic) — this is T-EXT-1's equality case, now derived |
| Is $\nabla H$ controlled by $K_0$ alone, away from conjugate points? | **Yes in constant curvature**, with $\|\nabla_xH\|\le C\sqrt{K_0}$ — but $\nabla R=0$ there, so this says nothing about the general case |
| Is $\nabla H$ controlled by $K_0$ alone, *including* near conjugate points? | **No — disproved** (§C.3) |
| Does constant curvature tell us whether $K_1$ is needed? | **No.** It is the $K_1=0$ slice of the problem and is silent on $K_1>0$ |

---

## §F. IS $K_1$ NECESSARY? — THE HONEST ANSWER

### F.1 What the proof consumes versus what the theorem might need

Trace the $\nabla R$-dependence back through §E. It enters at exactly **one** place: the middle expression of (E.3),
$$\big|\nabla_tY(0)\big|\ \le\ \Theta\left\|\int_0^1\Psi(1,\tau)\,\mathcal F_{\nabla R}(\tau)\,d\tau\ +\ \int_0^1\Psi(1,\tau)\,\mathcal F_{R}(\tau)\,d\tau\right\| .$$
The step from that expression to $\|\mathcal F_{\nabla R}\|_\infty$ is a **crude relaxation**: it replaces the norm of a smoothed integral by the sup of the integrand. This is exactly where a putative counterexample must live, and exactly why the counterexample is hard.

### F.2 The oscillation strategy, and why it does not obviously work

The natural search direction (as the brief suggests): take a fixed background metric $g$ and perturb,
$$g_\omega=g+\epsilon_\omega h(\omega\,\cdot),$$
with $h$ a fixed smooth tensor and $\omega\to\infty$. Schematically, curvature involves two derivatives of the metric and $\nabla R$ three, so
$$|R_\omega|\asymp\epsilon_\omega\omega^2,\qquad|\nabla R_\omega|\asymp\epsilon_\omega\omega^3 .$$
Choosing $\epsilon_\omega=\omega^{-2}$ keeps $|R_\omega|\le C$ while $|\nabla R_\omega|\asymp\omega\to\infty$. **This is the family the brief asks about.** But now observe what happens in (E.3): $\mathcal F_{\nabla R}$ inherits the oscillation, so along a geodesic of fixed length it is of the form $\omega\,\Xi(\omega t)$ with $\Xi$ bounded and (to leading order) mean-zero in $t$. Integrating against the **smooth, $\omega$-independent** kernel $\Psi(1,\cdot)$,
$$\int_0^1\Psi(1,\tau)\,\omega\,\Xi(\omega\tau)\,d\tau\ =\ O(1)\quad\text{by one integration by parts},$$
**not** $O(\omega)$. The blow-up of $\|\nabla R\|_\infty$ is therefore *invisible* to the quantity that actually controls $\nabla_tY(0)$.

This is not a proof that no counterexample exists — the mean-zero property of $\Xi$ at leading order in $t$ is not established here, $\Psi$ itself depends on $\omega$ through $\mathcal R$, and the $\mathcal F_R$ term also changes. But it **is** a proof that the obvious construction is blocked at the obvious place, and it forbids asserting necessity.

> **STATUS: necessity of $\|\nabla R\|_\infty$ is UNRESOLVED.** Neither a proof of necessity nor a counterexample is offered. No claim of necessity may be recorded anywhere in the programme. *(§C.3, by contrast, IS a proved negative result, but about $\Theta$, not about $K_1$.)*

### F.3 A strictly weaker sufficient condition, proved

The observation in §F.1 upgrades to a theorem which is **strictly weaker than $\|\nabla R\|_\infty\le K_1$** and is what Theorem H-LIP truly needs.

> **DEFINITION (averaged curvature-derivative bound).** For a geodesic tube $\mathcal T$ define
> $$K_1^{\rm av}:=\sup\left\{\ \left\|\int_0^1\Psi_\gamma(1,\tau)\Big[(\nabla_{S}R)(J,T)T+(\nabla_TR)(S,T)J\Big](\tau)\,d\tau\right\|\ \right\}$$
> the supremum being over all $(q,x)\in\mathcal T$, all Jacobi fields $J$ along $\gamma=\gamma_{qx}$ with $J(0)$ of unit norm and $J(1)=0$, and all Jacobi fields $S$ with $|S(0)|+|S(1)|\le1$, $\Psi_\gamma$ being the fundamental matrix of Lemma 6.
>
> **THEOREM H-LIP′.** Under the hypotheses of Theorem H-LIP with "$|\nabla R|\le K_1$" replaced by "$K_1^{\rm av}<\infty$",
> $$\sup_{\mathcal T}\Big(\|\nabla_qH\|+\|\nabla_xH\|\Big)\ \le\ K_0\rho^*+2\Theta\Big(K_1^{\rm av}+5\Lambda K_0\rho^*C_J^2\Big).$$

**Proof.** Identical to the proof of Theorem H-LIP, except that in (E.3) the two pieces of $\mathcal F$ are estimated separately: the $\mathcal F_{\nabla R}$ piece by the definition of $K_1^{\rm av}$ directly (after normalising $J(0)=w$, $|w|=1$, and $|S(0)|+|S(1)|\le1$, which is the case in both branches of the proof), and the $\mathcal F_R$ piece by Lemma 7 and $\|\Psi(1,\cdot)\|\le\Lambda$. $\blacksquare$

**Consequences.**
* $K_1^{\rm av}\le 2\Lambda K_1\rho^{*2}C_J^2$ always (relax the integral to the sup), so H-LIP′ implies H-LIP.
* $K_1^{\rm av}$ is **finite for the oscillatory family of §F.2 whenever the oscillation averages out**, whereas $K_1$ diverges. So the gap between the two is not vacuous in principle.
* $K_1^{\rm av}=0$ whenever $\nabla R=0$.

> **This is the correct primitive to record in the assumption set.** Recording $\|\nabla R\|_\infty$ instead is *convenient*, not minimal.

---

## §G. THE LOCALLY SYMMETRIC CASE $\nabla R\equiv0$

> **THEOREM H-LIP-SYM.** Let $\mathcal T$ be a geodesic tube with $|R|\le K_0$, (NC) with constant $\Theta$, and $\nabla R\equiv0$ on $\mathcal T$. Then
> $$\sup_{\mathcal T}\Big(\|\nabla_qH\|+\|\nabla_xH\|\Big)\ \le\ L_H\ =\ K_0\rho^*\big(1+10\,\Theta\Lambda C_J^2\big),\qquad \Lambda=e^{(1+K_0\rho^{*2})/2},$$
> i.e. **$L_H=L_H(K_0,\rho^*,\Theta)$ with no $K_1$ whatsoever.** On a Cartan–Hadamard manifold ($\Theta=1$ by Lemma 4(i)) this is
> $$L_H=L_H(\bar K,\rho^*)=\bar K\rho^*\big(1+10\,\Lambda C_J^2\big),\qquad C_J=\sqrt2\Lambda(2+\Lambda),\ \Lambda=e^{(1+\bar K\rho^{*2})/2},$$
> **which is exactly the form Theorem SW-AS assumed.**

**Proof.** $\nabla R\equiv0$ makes $\mathcal F_{\nabla R}\equiv0$ identically in Lemma 2, so $\mathcal F=\mathcal F_R$ and Lemma 7 gives $\|\mathcal F\|_\infty\le5K_0\rho^*C_J^2$. Substitute into the proof of Theorem H-LIP with $K_1=0$. $\blacksquare$

**The simplification in the differentiated Jacobi equation, stated precisely.** Under $\nabla R=0$ the $Y$-equation of Lemma 2 becomes
$$\nabla_t^2Y+R(Y,T)T=-\Big[R(J,\nabla_tS)T+R(J,T)\nabla_tS+R(\nabla_tS,T)J+2R(S,T)\nabla_tJ\Big],$$
a forced Jacobi equation whose forcing is **bilinear in $(S,J)$ with coefficients built from $R$ alone**. Since $S$ and $J$ are themselves controlled by $K_0$ and the boundary data (Lemma 5), the whole estimate closes on $(K_0,\rho^*,\Theta)$. **No classification of symmetric spaces is used; the theorem is purely conditional on $\nabla R=0$.**

### G.1 The condition is satisfied by the manifold Paper 1 actually uses

The affine-invariant SPD manifold $\mathcal P(p)=\{A\in\mathbb R^{p\times p}:A=A^\top\succ0\}$ with $\langle U,V\rangle_A:=\operatorname{tr}(A^{-1}UA^{-1}V)$ satisfies $\nabla R\equiv0$. Proof, elementary and self-contained:

1. *Congruences are isometries.* For $G\in GL(p)$, $\Phi_G(A):=GAG^\top$ has $d\Phi_G[U]=GUG^\top$ and
 $$\langle GUG^\top,GVG^\top\rangle_{GAG^\top}=\operatorname{tr}\big(G^{-\top}A^{-1}G^{-1}GUG^\top G^{-\top}A^{-1}G^{-1}GVG^\top\big)=\operatorname{tr}(A^{-1}UA^{-1}V)=\langle U,V\rangle_A .$$
 These act transitively ($A=GG^\top$ carries $I$ to $A$).
2. *There is a geodesic symmetry at $I$.* Let $\sigma(A):=A^{-1}$. Then $d\sigma_A[U]=-A^{-1}UA^{-1}$ and
 $$\langle d\sigma_A U,d\sigma_A V\rangle_{A^{-1}}=\operatorname{tr}\big(A\,A^{-1}UA^{-1}\,A\,A^{-1}VA^{-1}\big)=\operatorname{tr}(UA^{-1}VA^{-1})=\langle U,V\rangle_A,$$
 so $\sigma$ is an isometry; $\sigma(I)=I$ and $d\sigma_I=-\mathrm{id}$.
3. *Hence $\nabla R=0$.* $\nabla R$ is a covariant tensor of odd total degree $5$. An isometry $\sigma$ fixing $I$ preserves the Levi-Civita connection and curvature, so $\sigma^*(\nabla R)_I=(\nabla R)_I$; but $d\sigma_I=-\mathrm{id}$ gives $\sigma^*(\nabla R)_I=(-1)^5(\nabla R)_I=-(\nabla R)_I$. Hence $(\nabla R)_I=0$. By step 1 and transitivity, $\nabla R\equiv0$ everywhere. $\blacksquare$

4. *Curvature is bounded independently of $p$.* At $I$ the curvature of this symmetric space is $R(U,V)W=-\tfrac14[[U,V],W]$ for $U,V,W$ symmetric. In the Frobenius norm (which is the metric at $I$), $\|[U,V]\|\le2\|U\|\|V\|$, so $|R|\le\tfrac14\cdot2\cdot2=1$ and $K\in[-1,0]$ — **uniformly in $p$**. (The sign: $\langle R(U,V)V,U\rangle=-\tfrac14\langle[[U,V],V],U\rangle=-\tfrac14\|[U,V]\|^2\le0$ by the invariance of the trace form, so $K\le0$, consistent with (H1).)

> **CONSEQUENCE — the SW-AS proof obligation is DISCHARGED for Paper 1.** On the affine-invariant SPD manifold: $\nabla R\equiv0$, $K\in[-1,0]$ so $\bar K\le1$ and $\Theta=1$, and Theorem H-LIP-SYM gives
> $$L_H\le \rho^*\big(1+10\Lambda C_J^2\big),\qquad\Lambda=e^{(1+\rho^{*2})/2},$$
> a finite constant depending only on the support radius $\rho^*$ — **and on nothing else, in particular not on $p$.** The line in addendum II §3.4 ("used but not proved here … standard comparison geometry but a proof obligation") is now closed for this manifold, and closed in general under the added hypothesis $K_1<\infty$ (or $K_1^{\rm av}<\infty$).

---

## §H. DOES SW-AS NEED ALL OF H-LIP? — LINE-BY-LINE AUDIT

Theorem SW-AS decomposes $\tfrac12\operatorname{Hess}_q\hat F_u=\sum_tw_t(u)H(q,X_{t,n})$ into four pieces. Take them one at a time and record **exactly** which regularity each consumes.

### (i) Stochastic uniformity in $q$ — the term $\sum_tw_t\big[H(q,X_{t,n})-\mathbb EH(q,X_{t,n})\big]$

The proof applies Liebscher/Rio to scalar projections $\langle \mathbb H(q,X_{t,n})-\mathbb E\mathbb H,\,\Sigma\rangle$ over a $\tfrac12$-net of the unit sphere of $\operatorname{Sym}^2$, then a $\epsilon$-net of $\bar B(\mu(u),\rho)$ in $q$, then a grid in $u$.

* **Boundedness** $\|H\|\le\zeta(2\rho^*)$: consumed by the Bernstein step ($|Z_t|\le B$). Needs only the *upper* Hessian comparison, **no derivative**.
* **Modulus of continuity in $q$**: consumed by the $\epsilon$-net. Needs (A.2), i.e. $\|\nabla_qH\|$ — *or, strictly, only a modulus $\omega_q$ with $\log N_{\omega_q}(\epsilon)\lesssim p\log(1/\epsilon)$*. Lipschitz is sufficient; Hölder-$\alpha$ would also do at the cost of $\alpha^{-1}$ in the net constant.
* **Modulus in $u$**: consumed by the time grid; supplied by $|\partial_uw_t|=O((nb^2)^{-1})$, **not** by geometry.

> **Verdict (i): the $q$-derivative is genuinely required.** It cannot be moved to the law, because the net is applied to the *empirical* process pathwise, before any expectation. There is no route to SW-AS that avoids some third-derivative-of-$d^2$ modulus in the $q$-slot.

### (ii) The local-stationarity replacement $X_{t,n}\rightsquigarrow X^{(u_t)}_t$

The proof bounds this by $L_H\sum_t|w_t|\,d(X_{t,n},X^{(u_t)}_t)$ and then uses (H3), $\mathbb E d(X_{t,n},X^{(u_t)}_t)^2\le Cn^{-2a}$, plus Markov. This is the **only** consumer of $\nabla_xH$.

* It uses $\|H(q,x)-H(q,x')\|\le L_H\,d(x,x')$ — statement (A.3), which is type-correct with no transport (§A.3).
* It uses it only in **$L^1$/expectation**, and only at the resolution $n^{-a}$. So a modulus $\omega_x$ with $W\,\omega_x(n^{-a})=o(1)$ suffices; Lipschitz is again convenient, not minimal.
* **And it can be dispensed with entirely** by strengthening (H3) at the level of the expected Hessian — see (A3) below.

> **Verdict (ii): $\nabla_xH$ is AVOIDABLE.** It is a convenience for converting a *pathwise* coupling assumption into a *Hessian* statement. If the model is assumed to be locally stationary directly in the expected-Hessian sense, $\nabla_xH$ never appears.

### (iii) The law replacement $u_t\rightsquigarrow u$ — the term $\sum_tw_t\big[\mathbb EH(q,X^{(u_t)})-\mathbb EH(q,X^{(u)})\big]$

This is bounded by the **already-assumed** Lipschitz-in-$v$ of $v\mapsto\mathbb EH(q,X^{(v)})$, times $\max_t|u_t-u|\le b$. It is a **law-level, population** assumption. **No geometry, no curvature, no derivative of $H$ is consumed here at all.** The brief's proposed
$$\sup_{u,v,q}\frac{\|\mathbb EH(q,X^{(v)})-\mathbb EH(q,X^{(u)})\|}{|v-u|}\le L_{\rm law}$$
is precisely this assumption, and it is already present in SW-AS as stated.

### (iv) The population term $H_{P_u}(q)\succeq\mathrm{Id}$

Hadamard lower Hessian comparison; no derivative.

### H.1 The minimal ABSTRACT SW-AS assumptions

> **ABSTRACT (S1)–(S5).** With $\mathbb H(q,x)$ the symmetric form of §A.1 and $\bar B:=\bar B(\mu(u),\rho)$:
> * **(S1) Boundedness.** $\displaystyle\sup_{q\in\bar B}\ \operatorname*{ess\,sup}_{x}\ \|H(q,x)\|_{\rm op}\le\bar H<\infty .$
> * **(S2) Modulus in $q$, pathwise.** For all $x$ in the a.s. support and $q,q'\in\bar B$: $\ \|\Pi H(q',x)\Pi^{-1}-H(q,x)\|_{\rm op}\le L_q\,d(q,q')$.
> * **(S3) Expected-Hessian local stationarity.** $\displaystyle\sup_{t,n}\ \sup_{q\in\bar B}\big\|\mathbb EH(q,X_{t,n})-\mathbb EH(q,X^{(u_t)}_t)\big\|_{\rm op}\le\Delta_n=O(n^{-a}).$
> * **(S4) Expected-Hessian smoothness in the law index.** $\displaystyle\sup_{q\in\bar B}\big\|\mathbb EH(q,X^{(v)})-\mathbb EH(q,X^{(u)})\big\|_{\rm op}\le L_{\rm law}|u-v| .$
> * **(S5) Population lower bound.** $\mathbb EH(q,X^{(u)})\succeq\mathrm{Id}$ for $q\in\bar B$.
>
> **THEOREM SW-AS (abstract form).** Under (H2), (H3), (H5), (H6), (H7) with $\sup_u\|w(u)\|_1\le W$, and (S1)–(S5), and the mixing threshold $\beta>1+2\gamma/(1-\alpha)$ with $\gamma>c(p+p^2)$:
> $$\sup_{u\in[0,1]}\ \sup_{q\in\bar B(\mu(u),\rho)}\Big\|\tfrac12\operatorname{Hess}_q\hat F_u-H_{P_u}(q)\Big\|_{\rm op}=O_p\!\left(W\Big[L_{\rm law}\,b+\Delta_n+(\bar H+L_q)\sqrt{\tfrac{p+\log n}{nb}}\Big]\right).$$

**Proof.** Verbatim the addendum-II proof, with: the first term handled by Theorem B's argument with the two nets, using (S1) for the Bernstein bound $B$ and (S2) for the $q$-net; the second by (S4); the third by (S5); the fourth by (S3) instead of the geometric Lipschitz-in-$x$ bound. $\blacksquare$

**The two-stage implication chain, now explicit.**

$$
\underbrace{\begin{array}{c}\text{PRIMITIVE GEOMETRIC}\\ |R|\le K_0,\ \ \nabla R=0\ \text{(or }K_1^{\rm av}<\infty)\\ \text{tube }\rho^*,\ \ \Theta\end{array}}_{\text{Thm H-LIP / H-LIP-SYM}}
\ \Longrightarrow\
\underbrace{\begin{array}{c}\text{(S1) via T-EXT-1}\\ \text{(S2) with }L_q=L_H\\ \text{(S3) via }\|\nabla_xH\|\le L_H\text{ and (H3)}\end{array}}_{\text{abstract}}
\ \Longrightarrow\ \text{SW-AS}\ \Longrightarrow\ \text{G1-LP}.
$$

with (S4), (S5) supplied respectively by the **model** (a law-level smoothness hypothesis, not geometry) and by **Hadamard geometry**.

> **The containment point the brief insists on.** Only (S2) and (S3) touch $\nabla H$. (S3) can be **assumed directly**, in which case the primitive geometric input reduces to $|R|\le K_0$ plus (S2) alone — i.e. $\|\nabla_qH\|$, i.e. still Theorem H-LIP, but only its $q$-half. **There is no version of SW-AS that needs neither.**

### H.2 Corrected statement of SW-AS

> **THEOREM SW-AS (corrected).** Assume (H1)–(H7) with signed weights, $\sup_u\|w(u)\|_1\le W$, a.s. support radius $\rho^*$, and:
> * **(SW-G)** the geodesic tube $\mathcal T=\{(q,x):q\in\bar B(\mu(u),\rho),\ x\in\operatorname{supp}P_{u_t},\ |u_t-u|\le b\}$ satisfies $|R|\le K_0$ and **either** $\nabla R\equiv0$ **or** $K_1^{\rm av}<\infty$ (in particular, **or** $|\nabla R|\le K_1$). Under (H1) the non-conjugacy constant is $\Theta=1$ automatically (Lemma 4(i)). Then $L_H<\infty$ by Theorem H-LIP/H-LIP-SYM, giving (S1), (S2), (S3).
> * **(SW-L)** $v\mapsto\mathbb EH(q,X^{(v)})$ is $L_{\rm law}$-Lipschitz uniformly in $q\in\bar B(\mu(u),\rho)$.
>
> Then
> $$\sup_{u}\sup_{q\in\bar B(\mu(u),\rho)}\Big\|\tfrac12\operatorname{Hess}_q\hat F_u-H_{P_u}(q)\Big\|_{\rm op}=O_p\!\left(W\Big[L_{\rm law}b+L_{H}n^{-a}+(\zeta(2\rho^*)+L_H)\sqrt{\tfrac{p+\log n}{nb}}\Big]\right),$$
> and if this is $o_p(1)$ then $\hat F_u$ is $2\lambda_n$-strongly geodesically convex on $\bar B(\mu(u),\rho)$ uniformly in $u$, with $\lambda_n\to1$.
>
> **Changes from the addendum-II statement:** (a) "$x\mapsto H(q,x)$ Lipschitz with constant $L_H=L_H(\bar K,\rho^*)$" is no longer an assumption — it is **proved**, but the proof requires either $\nabla R=0$ or a bound on (an averaged) $\nabla R$, so the *hypothesis set* grows by (SW-G); (b) the Lipschitz-in-$q$ requirement, previously implicit in "the argument of addendum I Theorem B applies verbatim", is now **explicit** and is the non-removable half; (c) $L_H$ is carried explicitly in the rate rather than absorbed into $O_p$, because §J shows it need not be $n$-free.

---

## §I. CORRECTED G1 STATUS

**Theorem G1-LP is unchanged in statement and in rate.** Its proof consumed SW-AS, which consumed an unproved Lipschitz bound. That bound is now proved, at the cost of one new geometric hypothesis (SW-G).

> **G1-LP (status).** **PROVED**, for the localised local-polynomial specification, under (H1)–(H7) + (SW-G) + (SW-L) + the stated mixing/bandwidth conditions:
> $$\sup_{u\in[0,1]}d\big(\hat\mu(u),\mu(u)\big)=O_p\Big(b^{d+1}+\sqrt{\tfrac{\log n}{nb}}\Big).$$
> **On the affine-invariant SPD manifold, (SW-G) is automatically satisfied** (§G.1: $\nabla R\equiv0$, $\bar K\le1$, $\Theta=1$), so for the manifold Paper 1 actually uses, **G1-LP is proved with no new assumption at all.**
>
> **In general:** G1-LP is **CONDITIONAL on (SW-G)**, and (SW-G) is a genuinely new hypothesis on the geometry, not a consequence of (H1). It is *not* conditional on any unproved lemma.

**What is NOT claimed.** That (SW-G) is necessary. §F leaves that open. The programme must not record $\|\nabla R\|_\infty<\infty$ as "necessary" or as "the right condition"; it is a *sufficient* condition, and $K_1^{\rm av}$ is a strictly weaker sufficient condition.

---

## §J. FIXED-$p$ / GROWING-$p$ GEOMETRIC CONSEQUENCE

For a manifold sequence $M_n$ write $K_{0,n},K_{1,n},\rho^*_n,\Theta_n,L_{H,n}$. Theorem H-LIP gives
$$L_{H,n}\ \le\ K_{0,n}\rho^*_n+2\Theta_n\Lambda_nC_{J,n}^2\big(2K_{1,n}\rho_n^{*2}+5K_{0,n}\rho^*_n\big),\qquad \Lambda_n=e^{(1+K_{0,n}\rho_n^{*2})/2},$$
$C_{J,n}=\sqrt2\Lambda_n(1+\Theta_n+\Theta_n\Lambda_n)$. **Crucially, $p$ does not appear in this bound** — the constant is dimension-free *given* $(K_{0,n},K_{1,n},\rho^*_n,\Theta_n)$. Also $\zeta_n=\zeta(2\rho^*_n)=\sqrt{K_{0,n}}\,2\rho^*_n\coth(2\sqrt{K_{0,n}}\rho^*_n)$ is dimension-free.

> **$L_H$ MAY NOT BE CALLED A CONSTANT.** It is $n$-free **only if** $K_{0,n},K_{1,n},\rho^*_n,\Theta_n$ are bounded in $n$. This must be **assumed or proved**, per manifold sequence:
> * **Affine-invariant SPD, $M_n=\mathcal P(p_n)$:** $K_{0,n}\le1$ (§G.1 step 4, uniformly in $p$), $K_{1,n}=0$, $\Theta_n=1$. So $L_{H,n}=L_H(\rho_n^*)$ and is bounded **iff $\rho^*_n=O(1)$** — which is exactly the a.s.-support half of (G4)/(G5), already in the assumption set. **Uniformity in $n$ is therefore PROVED for this sequence, conditional on $\rho^*_n=O(1)$.**
> * **A general sequence:** nothing may be assumed. Record $L_{H,n}$ explicitly.

**Exact consistency requirement.** With SW-AS in its corrected form,
$$\sup_u\sup_q\Big\|\tfrac12\operatorname{Hess}_q\hat F_u-H_{P_u}(q)\Big\|_{\rm op}=O_p\!\left(W_n\Big[L_{\rm law}b+L_{H,n}n^{-a}+(\zeta_n+L_{H,n})\sqrt{\tfrac{p+\log n}{nb}}\Big]\right),$$
so the requirement for asymptotic strong convexity (and hence for G1-LP) is
$$\boxed{\ W_n\,L_{H,n}\left[b+n^{-a}+\sqrt{\frac{p+\log n}{nb}}\right]\ \longrightarrow\ 0\ }$$
together with the separate requirement carrying the $H$-bound rather than its derivative,
$$W_n\,\zeta_n\sqrt{\frac{p+\log n}{nb}}\ \longrightarrow\ 0,\qquad \zeta_n=\zeta(2\rho^*_n)=2\sqrt{K_{0,n}}\,\rho^*_n\coth\!\big(2\sqrt{K_{0,n}}\rho^*_n\big),$$
and $L_{\rm law}$ absorbed into the constant. No inequality between $\zeta_n$ and $L_{H,n}$ is asserted; they are tracked separately.

**Reading it.** At $b=n^{-\alpha}$ the binding term is $\sqrt{(p+\log n)/(nb)}=\sqrt{(p+\log n)n^{\alpha-1}}$, so the requirement is
$$L_{H,n}^2\,W_n^2\,(p_n+\log n)\ =\ o\big(n^{1-\alpha}\big),$$
i.e. **the geometric Lipschitz constant enters the dimension budget quadratically and multiplies $p_n$.** With $L_{H,n}\asymp e^{cK_{0,n}\rho_n^{*2}}$, an unbounded tube radius is fatal well before the dimension is.

> Additionally, the signed route pays a $p(p+1)/2$-dimensional net of symmetric matrices, so its $\gamma$ must exceed $c\,p^2$, not $c\,p$. This is already recorded in addendum II §6 item 3 and is **not** changed by the present run; it remains the binding structural obstruction for $p_n\to\infty$, ahead of the geometry.

---

## §K. DOWNSTREAM ASSUMPTION-PROPAGATION TABLE

Does the result depend on the new geometric condition (SW-G), i.e. on $\nabla R$ (in any form)?

| Result | Needs $\|H\|\le\zeta$ (T-EXT-1)? | Needs $\|\nabla_qH\|$? | Needs $\|\nabla_xH\|$? | Needs (SW-G) / $\nabla R$? | Reason |
|---|---|---|---|---|---|
| **T-EXT-1 itself** | — | no | no | **NO** | Second-derivative comparison only; §C.1 derives the constant-curvature equality case |
| **Lemma P1 / Theorem A′** | no | no | no | **NO** | Sturm quadratic minorant; no Hessian at all |
| **Lemma P2 (score Lipschitz)** | yes | no | no | **NO** | Uses $\|H\|_{\rm op}\le\zeta$, an $H$-bound, not a derivative |
| **Theorem B (score concentration)** | yes | no | no | **NO** | The net is on $\log_qX$, whose $q$-modulus is $\zeta$ |
| **Theorem C (uniform rate to $\mu_b$)** | yes | no | no | **NO** | Same |
| **Theorem W / G1-H (positive-weight route)** | yes | no | no | **NO** | Sturm supplies strong convexity outright; no Hessian maximal inequality is used |
| **Theorem SW-AS** | yes | **YES** | **YES** (avoidable via (S3)) | **YES** | §H(i),(ii) |
| **Theorem G1-LP (signed sup-norm G1)** | yes | **YES** | **YES** (avoidable) | **YES** | Consumes SW-AS |
| **G1 via the positive-weight route (Thm W)** | yes | no | no | **NO** | Independent of SW-AS entirely |
| **Theorem E$_{L^2}$** | no | no | no | **NO** | Proof is Theorem A′ + Rio covariance inequality; no Hessian |
| **Theorem G1′$_{L^2}$** | via (D4) | no | no | **NO for positive weights**; YES for signed | (D4) is "free by Sturm" with positive weights |
| **Theorem E (factor/subspace)** | no | no | no | **NO** | Downstream of $\|e\|_{L^2}$ only (T17, T18, ledger) |
| **T31 ribbon holonomy** | no | no | no | **NO** | Jacobi/Riccati comparison uses $|R|\le\bar K$ only |
| **T54 (flat case)**, T22–T25, $\sin\Theta$ bound | no | no | no | **NO** | Same |
| **Paper 2** | no | no | no | **NO** | Inherits T31 |

> **CONTAINMENT VERDICT — stated explicitly as the brief demands.**
> **Theorem E survives without any $\nabla R$ assumption.** So do the ribbon/holonomy results (T31, T54), Paper 2, Theorem E$_{L^2}$, and the entire positive-weight route including Theorem W and Theorem G1-H. **The new geometric condition (SW-G) propagates to exactly one place: Theorem SW-AS, and through it to Theorem G1-LP — i.e. only to the signed-weight (degree-$\ge2$ local-polynomial) estimator.** The programme must **not** be globally re-assumed under bounded $\nabla R$.
>
> Corollary of practical importance: **the positive-weight multi-kernel route (Theorem W, $J=3$, $q=3$) is now strictly cheaper in assumptions than the signed local-polynomial route** — it buys $q=3$ with no geometric condition beyond (H1), whereas the signed route buys arbitrary $q=d+1$ at the price of (SW-G) and a $5^{p(p+1)/2}$ net. On the affine-invariant SPD manifold (SW-G) is free, so there the signed route is still preferable for $d\ge3$; on a general Cartan–Hadamard manifold it is not.

---

## §L. REMAINING PROOF OBLIGATIONS

1. **Necessity of $K_1$ / $K_1^{\rm av}$ — UNRESOLVED.** §F.2 shows the natural oscillatory construction is blocked by an integration-by-parts cancellation in (E.3). Neither direction is proved. *No necessity claim may be recorded.*
2. **Sharpness of the $\Theta$-power.** Theorem H-LIP gives $\Theta^3$; the sphere computation (§C.3) exhibits only $\Theta^2$. Not resolved; harmless for the application, where $\Theta=1$.
3. **The upper Hessian comparison $H\preceq\zeta(d)\mathrm{Id}$ for general $-\bar K\le K\le0$** (T-EXT-1's upper half) is used by (S1) and by Lemma P2 and is **still cited, not derived**, in this programme. §C.1 derives only the constant-curvature equality case. *This is a pre-existing obligation that this run does not close.* It is a Rauch/Riccati comparison and is a strictly easier obligation than the one just discharged.
4. **Finite-sample quantification of SW-AS** ($\delta_0$, event probability) — unchanged, open.
5. **Growing dimension $p_n\to\infty$** — unchanged, open, and still binding ahead of the geometry (§J).
6. **(S4) / (SW-L)** — a law-level smoothness hypothesis of the locally stationary model. Not geometric; belongs in the model assumption set, and is currently assumed rather than derived from (H3).

**Nothing in Theorem H-LIP, H-LIP′ or H-LIP-SYM is conditional on any of the above.** Those three are proved outright from the stated hypotheses.

---

## §M. EXACT PATCHES

### To `Ideas/G1 audit — addendum II — second-order barycentre expansion, empirical Sturm, and the true scope of CE-9.md`

**M1. §3.4, third bullet** — replace
> *"The Lipschitz-in-$x$ bound $\|\partial_xH(q,x)\|\le L_H(\bar K,\rho^*)$ is used but not proved here… standard comparison geometry but it is a proof obligation, not a citation, and it is recorded as such."*

by
> *"**[2026-08-08, addendum III] DISCHARGED.** Theorem H-LIP proves $\|\nabla_qH\|+\|\nabla_xH\|\le L_H(K_0,K_1,\rho^*,\Theta)$ on a geodesic tube, with $\Theta=1$ free under (H1). It is **not** standard comparison geometry: bounded curvature alone is **disproved** as sufficient (sphere, near-conjugate radius, §C.3), and the differentiated Jacobi equation genuinely produces $\nabla R$ terms, $(\nabla_SR)(J,T)T$ and $(\nabla_TR)(S,T)J$. The theorem therefore requires the new hypothesis (SW-G): $|R|\le K_0$ and either $\nabla R\equiv0$ or $K_1^{\rm av}<\infty$ (weaker than $\|\nabla R\|_\infty<\infty$). **On the affine-invariant SPD manifold $\nabla R\equiv0$ and $|K|\le1$ uniformly in $p$, so (SW-G) is free and $L_H=L_H(\rho^*)$ — exactly the form assumed. Necessity of the $\nabla R$ hypothesis in general is UNRESOLVED and must not be asserted.*"

**M2. §3.2, Theorem SW-AS statement** — replace the hypothesis clause *"and $x\mapsto H(q,x)$ Lipschitz with constant $L_H=L_H(\bar K,\rho^*)$ on the relevant range"* by *"and (SW-G) of addendum III, which yields by Theorem H-LIP both the Lipschitz-in-$x$ constant $L_H$ **and the Lipschitz-in-$q$ constant** (previously used implicitly in the $\epsilon$-net step and not stated)"*. Carry $L_H$ **explicitly** in the displayed rate rather than inside $O_p$; see M4.

**M3. §3.2, proof, sentence "The first is a matrix-valued kernel-weighted centred sum with bounded entries … and Lipschitz-in-$q$ with constant $L_H$"** — add the footnote: *"the Lipschitz-in-$q$ statement is (A.2) of addendum III, i.e. a bound on $\|\nabla_qH\|=\|\nabla^3_qE\|$ modulo parallel transport; it is a separate consequence of Theorem H-LIP and is the half that **cannot** be traded for a law-level assumption."*

**M4. §3.2, displayed rate** — replace by
$$O_p\Big(W\big[L_{\rm law}b+L_{H}n^{-a}+(\zeta(2\rho^*)+L_H)\sqrt{\tfrac{p+\log n}{nb}}\big]\Big),$$
and add: *"$L_H$ is not automatically $n$-free; see addendum III §J. The consistency requirement is $W_nL_{H,n}[b+n^{-a}+\sqrt{(p+\log n)/(nb)}]\to0$."*

**M5. §6 status board** — add a row:
> | **$\|\partial_xH\|\le L_H$ (SW-AS's geometric input)** | assumed, flagged as a proof obligation | **PROVED (Theorem H-LIP, addendum III)** under new hypothesis (SW-G); **free on affine-invariant SPD**; bounded curvature alone **disproved** as sufficient; necessity of $\nabla R$ **unresolved** | addendum III §§D2, E, C.3, F |

**M6. §6 "Still open after this run", item 1** — replace *"The Lipschitz bound … Standard comparison geometry; a proof obligation, not yet discharged"* by *"**Closed** by Theorem H-LIP at the price of (SW-G). What remains open is (a) necessity of the $\nabla R$ hypothesis, (b) the **upper** Hessian comparison $H\preceq\zeta\mathrm{Id}$ for general $-\bar K\le K\le0$, which is still cited rather than derived."*

**M7. §7 patch list** — append the propagation table of addendum III §K and the sentence: *"(SW-G) propagates to Theorem SW-AS and Theorem G1-LP **only**. Theorem E, Theorem E$_{L^2}$, the positive-weight route (Theorem W, G1-H), T31/T54 and Paper 2 are unaffected."*

### To `Ideas/Analytical reconstruction — proof ledger and rebuilt spec.md`

**M8. §5.1 assumption set** — insert a new assumption between (G5) and (G7):
> *"**(G8) [signed weights only] Curvature-derivative control on the estimation tube.** On $\mathcal T=\{(q,x):d(q,\mu(u))\le\rho,\ d(x,\mu(u))\le\rho^*\}$: $|R|\le K_0$ and either $\nabla R\equiv0$ or $K_1^{\rm av}<\infty$ (implied by $|\nabla R|\le K_1$). Under (H1) the non-conjugacy constant is $\Theta=1$ automatically. Yields $L_H<\infty$ (Theorem H-LIP, addendum III) and hence Theorem SW-AS. **Vacuous on the affine-invariant SPD manifold** ($\nabla R\equiv0$, $|K|\le1$ uniformly in $p$). **Not required by the positive-weight estimator.** Necessity unresolved."*

**M9. §1.3 ledger** — add rows:
> | **T-EXT-3** | **Theorem H-LIP.** $\|\nabla_qH\|+\|\nabla_xH\|\le L_H(K_0,K_1,\rho^*,\Theta)$ on a geodesic tube; $\Theta=1$ on Hadamard | Lemmas 1–7, addendum III | SW-AS | **PROVED** | III §B | — | — |
> | **T-EXT-4** | **H-LIP-SYM.** $\nabla R\equiv0\Rightarrow L_H=L_H(K_0,\rho^*,\Theta)$; and $\mathcal P(p)$ affine-invariant satisfies $\nabla R\equiv0$, $|K|\le1$ uniformly in $p$ | geodesic symmetry $\sigma(A)=A^{-1}$; odd-degree tensor argument | (G8) vacuity | **PROVED** | III §G | — | — |
> | **D-EXT-1** | *"Bounded curvature alone controls $\nabla H$."* | — | — | **DISPROVED.** $S^p$: $\mu_{\rm tan}=\theta\cot\theta$, $d\mu_{\rm tan}/dL\sim-c\pi/(\pi-\theta)^2\to-\infty$ at fixed $K_0$, $\nabla R=0$. A non-conjugacy constant is unavoidable | III §C.3 | — | T-EXT-3 |
> | **U-EXT-1** | Necessity of $\|\nabla R\|_\infty$ (or $K_1^{\rm av}$) for H-LIP | — | — | **UNRESOLVED.** The oscillatory-perturbation route is blocked by integration by parts against the Green kernel $\Psi(1,\cdot)$ | III §F | Do not record as necessary | — |

**M10. §1.7 / T-EXT-1** — append: *"The constant-curvature equality case (eigenvalues $1$ and $\theta\coth\theta$ on $\mathbb H^p(-1)$; $1$ and $\theta\cot\theta$ on $S^p$) is now **derived** from the Jacobi BVP in addendum III §C.1 and no longer needs the Pennec citation. The **upper comparison** $H\preceq\zeta(d)\mathrm{Id}$ for general $-\bar K\le K\le0$ remains cited."*

**M11. §9 "still open", and §10 minimal viable path** — the ordering is unchanged, but add: *"the positive-weight route is now strictly assumption-cheaper than the signed route on a general Cartan–Hadamard manifold, because the latter alone consumes (G8). On affine-invariant SPD the two are on a par and the signed route wins for $d\ge3$."*

### To `Ideas/Paper 1 — Locally stationary Riemannian factor model.md`

**M12. Assumption section** — add (G8) as above, with the one-line remark that it is vacuous for the SPD model of the paper, together with the two-line proof of §G.1 (steps 2–4) as a footnote. This is worth stating explicitly in the paper: it is the reason the paper can use a degree-$d$ local-polynomial Fréchet estimator without any curvature-derivative hypothesis.

**M13. Named gap 1** — keep **closed**; add: *"the last geometric proof obligation inside G1 (the third-derivative bound on $\tfrac12d^2$) is discharged by Theorem H-LIP and is vacuous for the SPD geometry."*

**M14.** Do **not** add $\|\nabla R\|_\infty<\infty$ to the paper's global assumption set. It belongs only to the signed-weight branch (§K).

---

## FINAL STATUS LINE

**Terminal outcomes attained, in the brief's own taxonomy:**

* **(1) H-LIP PROVED UNDER $|R|+|\nabla R|$ BOUNDS** — yes, Theorem H-LIP, with the additional and unavoidable non-conjugacy constant $\Theta$ (free on Hadamard).
* **(2) BOUNDED CURVATURE ALONE DISPROVED** — yes, but precisely: disproved *without* a non-conjugacy constant (§C.3, sphere). **Not** disproved for $(K_0,\rho^*,\Theta)$ with $\nabla R$ unbounded.
* **(3) BOUNDED CURVATURE ALONE UNRESOLVED; $|\nabla R|$ SUFFICIENT** — yes, this is the status of the $(K_0,\rho^*,\Theta)$-only question. $K_1$ is **sufficient**; **necessity unresolved**; $K_1^{\rm av}$ is a proved strictly weaker sufficient condition, so $\|\nabla R\|_\infty$ is best described as **one convenient primitive assumption**.
* **(4) WEAKER EXPECTED-HESSIAN ASSUMPTION PROVED SUFFICIENT FOR SW-AS** — yes, for the $x$-slot: (S3) replaces $\nabla_xH$ entirely. **Not** for the $q$-slot: (S2) is irreducible.
* **(5) LOCALLY SYMMETRIC VERSION PROVED** — yes, Theorem H-LIP-SYM, and shown to cover the affine-invariant SPD manifold.
* **(6) G1 remains CONDITIONAL** — **only in general geometry, on the explicitly stated hypothesis (SW-G)**, which is not an unproved lemma but a new assumption. **On the affine-invariant SPD manifold, G1-LP is unconditional.**

**No lemma required for Theorem H-LIP, H-LIP′ or H-LIP-SYM is left unproved.** Those are written PROVED. Theorem SW-AS and Theorem G1-LP are **PROVED CONDITIONAL on (SW-G)** in general, **PROVED unconditionally** on the affine-invariant SPD manifold. The necessity question of §F is written UNRESOLVED and is not upgraded.
