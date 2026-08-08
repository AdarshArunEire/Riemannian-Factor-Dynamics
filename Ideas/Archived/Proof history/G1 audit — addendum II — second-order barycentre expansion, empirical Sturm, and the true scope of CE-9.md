---
type: idea
title: G1 audit — addendum II — second-order barycentre expansion, empirical Sturm, and the true scope of CE-9
aliases:
  - G1 addendum II
  - Second-order barycentre expansion
status: analytical-audit
verdict: G1 AS STATED IS PROVED (retracting "DISPROVED"); the J=3 bias claim of addendum I is DISPROVED and repaired by a scale family; Theorem A is replaced by an exact empirical-Sturm inequality
last-derived: 2026-08-08
area:
  - geometry
  - time-series
  - factor-models
tags:
  - idea
  - proof-audit
---

> **ARCHIVED CORRECTION LAYER — incorporated into the canonical G1 audit and Analytical reconstruction on 2026-08-08. Retained for audit history only. Do not treat this file as the current source of truth.**
>
> Later audit corrections also apply: the Hessian operator norm needs a sphere net in $S^{p-1}$, not a net in the $p(p+1)/2$-dimensional space of symmetric matrices; and the raw rates carry the local-stationarity remainder $n^{-a}$. See [[G1 audit — resolution of the uniform local Fréchet rate]].

# G1 audit — addendum II

> **Supersedes** [[G1 audit — resolution of the uniform local Fréchet rate]] on three points: its **Theorem A** (replaced), its **Theorem G1-H / §4.3** (its $J=3$ bias claim is **disproved**, and repaired), and its **headline verdict on CE-9** (**retracted and corrected**). Everything else in that note stands.
>
> **Three retractions are recorded in §0.2. They are the point of this note.**

---

## §0 Summary

### 0.1 What is now proved

| | |
|---|---|
| **Theorem A′ (empirical Sturm)** | $d(\hat\mu(u),\mu_b(u))\le\|\hat G_u(\mu_b(u))-G_u(\mu_b(u))\|$, **exactly**, with the score evaluated at the **deterministic** point $\mu_b(u)$. Constant $1$. Deletes §3.2 of addendum I entirely — no random-$q$ localisation, no peeling, no shells, no entropy in $q$, no $\zeta^*$, no Lemma P2/P3. |
| **Theorem X (second-order expansion)** | $x_*=b\,m_1A+b^2[\tfrac12m_2B+m_1^2C]+O(b^3)$ with $A=\mu'(u)$ **exactly**, $B=H_0^{-1}h_2$, $C=-H_0^{-1}(H_1A+\tfrac12T_0[A,A])$. Proved by plug-in + strong convexity, **not** by formal series inversion. |
| **Theorem Y ($C\equiv0$ in $\mathbb R^p$)** | The $m_1^2$ term is a **pure curvature/nonlinearity effect**: it is identically absent in Euclidean space, for every law family and every design. |
| **Theorem Z ($C\ne0$)** | Explicit exact witness on $\mathbb H^2$: $C=\psi(\lambda-1)/\lambda\cdot e_2\ne0$ for every $R>0$, $\psi\ne0$. **The $J=3$ multi-kernel claim of addendum I §4.3 is therefore false as proved.** |
| **Theorem W (the repair)** | $J=3$ **does** work — but only for a **one-sided scale family** $K_j(v)=K(v/c_j)/c_j$, because then $m_1(j)^2=(\mu_1^2/\mu_2)\,m_2(j)$ identically, so $\sum_j\lambda_jm_2(j)=0$ kills the $m_1^2$ term automatically. Explicit: $c=(1,\tfrac12,\tfrac14)$, $\lambda=(\tfrac13,-2,\tfrac83)$, $\|\lambda\|_1=5$. The user's proposed $J=4$ moment system $\{1,m_1,m_2,m_1^2\}$ is **not needed and in fact unachievable for a scale family** (its $4\times4$ matrix is identically singular). |
| **Theorem SW-AS (signed weights are asymptotically harmless)** | In the locally stationary model with $b\to0$, $\sup_u\sup_{q}\|\tfrac12\operatorname{Hess}\hat F_u-H_{P_u}(q)\|=O_p\big(b+\sqrt{(p+\log n)/(nb)}\big)\to0$, and $H_{P_u}\succeq\mathrm{Id}$ on Hadamard. Hence $\hat F_u$ is $2\lambda_n$-strongly geodesically convex with $\lambda_n\to1$, **with no condition relating curvature, support radius and negative mass.** |
| **Theorem G1-LP** | Consequently the **degree-$d$ signed local-polynomial Fréchet estimator, with a localised argmin specification**, satisfies $\sup_{u\in[0,1]}d(\hat\mu(u),\mu(u))=O_p(b^{d+1}+\sqrt{\log n/(nb)})$. **This is G1 exactly as originally stated**, with $q=q_{\mathrm{bdry}}=d+1\ge3$. |
| **Theorem G1′$_{L^2}$** | Now a genuine derivative theorem with explicit kernel-regularity, denominator and boundary-transition hypotheses. |

### 0.2 Three retractions

**RETRACTION 1 — "G1 AS STATED IS DISPROVED" is withdrawn.** CE-9 proves that an *arbitrary* signed Fréchet criterion on a Hadamard manifold can have multiple minimisers. It does **not** prove that the statistical estimator fails, and the gap between the two is not a technicality: in the locally stationary model the positively- and negatively-weighted observations are drawn from laws that converge to a *common* limit as $b\to0$, and Theorem SW-AS shows the resulting Hessian perturbation is $O_p(b+\sqrt{\log n/(nb)})=o_p(1)$. **The correct verdict is: G1 as stated is PROVED, for a localised argmin specification, which CE-9 shows is genuinely required.** The assumption **(G7)/(SW)** introduced in addendum I is **not needed asymptotically** and must be withdrawn from the assumption set as a *hypothesis*; it survives only as a *finite-$n$ sufficient condition* for global (as opposed to localised) uniqueness.

**RETRACTION 2 — the $J=3$ bias claim of addendum I §4.3 is disproved.** Its proof asserted that "all dependence on $j$ enters linearly through $m_1(j)$ and $m_2(j)$". Theorem X shows the $b^2$ coefficient also contains $m_1(j)^2C$, and Theorem Z shows $C\ne0$. Addendum I's Theorem G1-H is therefore **not proved as written**. It is repaired by Theorem W.

**RETRACTION 3 — addendum I's objection to bandwidth-Richardson at the boundary was wrong.** It said "the truncated kernel moments depend on the bandwidth, so bandwidth-Richardson does not cancel the boundary bias." That is true only for *two-sided kernels truncated by the domain*. For a **one-sided kernel looking into the domain**, the moments are $m_k(j)=c_j^k\mu_k$ with $\mu_k$ the fixed shape moments — completely $u$-independent — and bandwidth-Richardson works verbatim. This is exactly Theorem W, and it is simpler than the multi-shape construction addendum I proposed.

### 0.3 Two repairs to hypotheses (the user's "short repair" list)

* **Moment exponent.** Addendum I's $L^2$ theorem wrote $\sum_h\alpha(h)^{1-2/s}<\infty$ with $s$ elsewhere denoting the *smoothness of $\mu$*. That was a notation collision and an error of substance. The exponent in Rio's covariance inequality is a **moment order**. Correct statement in §4.
* **Local-stationarity remainder.** The additive $O(n^{-a})$ from replacing $X_{t,n}$ by $X^{(u_t)}_t$ was dropped in addendum I's Theorem G1-H. It is carried explicitly below and generates the condition $a>\min(q\alpha,\tfrac{1-\alpha}2)$ ($=2/5$ at $\alpha=1/5$, $q=3$).

---

## §1 Theorem A′ — the empirical Sturm inequality

**Setting** as in addendum I §1, weights **(P)** nonnegative summing to $1$.

> **Theorem A′.** On a Cartan–Hadamard manifold, for every $u$,
> $$\boxed{\ d\big(\hat\mu(u),\mu_b(u)\big)\ \le\ \big\|\hat G_u(\mu_b(u))-G_u(\mu_b(u))\big\|\ }$$
> with the score evaluated at the **deterministic** point $\mu_b(u)$.

*Proof.* $\hat P_u=\sum_tw_t(u)\delta_{X_{t,n}}$ is a probability measure with finite support, so by Sturm (2003) Prop. 4.3/4.4 it has a unique barycentre $\hat\mu(u)$ and $\hat F_u$ is $2$-strongly geodesically convex; by the gradient form derived in addendum I Lemma P1,
$$\|\operatorname{grad}\hat F_u(z)\|\ \ge\ 2\,d\big(z,\hat\mu(u)\big)\qquad\text{for every }z\in M .$$
Take $z=\mu_b(u)$ and use $\operatorname{grad}\hat F_u=-2\hat G_u$:
$$d\big(\mu_b(u),\hat\mu(u)\big)\ \le\ \big\|\hat G_u(\mu_b(u))\big\| .$$
Finally $\mu_b(u)$ is the barycentre of the probability measure $\bar P^b_u=\sum_tw_t(u)\operatorname{Law}(X_{t,n})$, so its Karcher equation gives $G_u(\mu_b(u))=0$ identically. Substitute. $\square$

**What this deletes from addendum I.** The entire §3.2 (Lemma P2 score-Lipschitz constant, Lemma P3 convex-hull confinement), the peeling over dyadic shells in the proof of Theorem C, the covering of the ball $\bar B(\mu_b(u),\delta)$, the constant $\zeta^*$, and the self-improvement step. Theorem C now reads:

> **Theorem C′.** $\sup_ud(\hat\mu(u),\mu_b(u))\le\sup_u\|\hat G_u(\mu_b(u))-G_u(\mu_b(u))\|=O_p\big(\sqrt{(p+\log n)/(nb)}\big)$, **immediately from Theorem B**, which was already a statement about the deterministic evaluation point $\mu_b(u)$.

**What it does not delete.** The a.s. support bound (H4a) is still needed — but now only to make the summands of Theorem B bounded for Liebscher's inequality, not to confine $\hat\mu$. That is a strictly weaker role, and it is what truncation handles under (H4b).

---

## §2 The second-order barycentre expansion, and the $m_1^2$ term

### 2.1 Setup

Fix $u$, $m:=\mu(u)$. On a Cartan–Hadamard manifold $\operatorname{Exp}_m:T_mM\to M$ is a global diffeomorphism, so $x\mapsto\operatorname{Exp}_mx$ is a global chart. Define, for weights $w_t$ supported on $|u_t-u|\le b$ with $\sum_tw_t=1$ and normalised moments $m_k:=b^{-k}\sum_tw_t(u_t-u)^k$,
$$\Lambda(x;b)\ :=\ \sum_tw_t\,\mathbb E\,d\big(X_{t,n},\operatorname{Exp}_mx\big)^2,\qquad x_*:=\arg\min_x\Lambda(x;b)=\log_m\mu_b(u).$$
Write $h(u,v):=\mathbb E\log_{\mu(u)}X^{(v)}\in T_mM$ (so $h(u,u)=0$), $h_k:=\partial_v^kh(u,v)|_{v=u}$, and
$$H(q,x):=\tfrac12\operatorname{Hess}_qd(x,q)^2,\qquad H_0:=\mathbb E\,H(m,X^{(u)}),\qquad H_1:=\partial_v\,\mathbb E\,H(m,X^{(v)})\big|_{v=u},$$
$$T_0:=D^3_x\Lambda_0(0),\qquad \Lambda_0(x):=\mathbb E\,d(X^{(u)},\operatorname{Exp}_mx)^2 .$$

**Standing hypotheses for §2.** (E1) $w_t\ge0$ (needed for convexity of $\Lambda$; the signed case is §3). (E2) $v\mapsto\operatorname{Law}(X^{(v)})$ is smooth enough that $h(u,\cdot)\in C^3$ and $v\mapsto\mathbb EH(m,X^{(v)})$ is $C^2$ near $u$, with domination allowing three differentiations under $\mathbb E$ and $\sup_{|x|\le Cb}\|D^4\Lambda\|<\infty$. (E3) $K$ compactly supported (so $|m_k|\le1$). (E4) On a Hadamard manifold $H_0\succeq\mathrm{Id}$ automatically (T-EXT-1), so $H_0^{-1}$ exists with $\|H_0^{-1}\|\le1$.

> **Remark (chart vs. Riemannian objects).** $H_b:=D^2_x\Lambda(0;b)$ and $T_b:=D^3_x\Lambda(0;b)$ are plain chart derivatives. At the **centre** of a normal chart the Christoffel symbols vanish, so $D^2_x\Lambda(0)=\operatorname{Hess}\Lambda(m)$; and $D^3_x\Lambda(0)=\nabla^3\Lambda(m)+(\partial_k\Gamma^l_{ij}(0))\partial_l\Lambda(0)$ with $\partial_l\Lambda_0(0)=0$ because $m$ **is** the Fréchet mean of $X^{(u)}$ — so $T_0=\nabla^3\Lambda_0(m)$ is tensorial too. Everything below is evaluated at $x=0$ only; the identification is not claimed elsewhere.

### 2.2 A clean identity: $A=\mu'(u)$ exactly

> **Lemma X0.** $h_1=H_0\,\mu'(u)$, hence $A:=H_0^{-1}h_1=\mu'(u)$ **exactly**.

*Proof.* Let $\Gamma(q,v):=\mathbb E\log_qX^{(v)}$. By definition of the Fréchet mean, $\Gamma(\mu(v),v)=0$ for all $v$. Since $\operatorname{grad}_q\tfrac12\mathbb E\,d(X^{(v)},q)^2=-\Gamma(q,v)$, we have $D_q\Gamma(q,v)=-\mathbb EH(q,X^{(v)})$, so $D_q\Gamma(m,u)=-H_0$. Differentiating $\Gamma(\mu(v),v)=0$ at $v=u$:
$$0=D_q\Gamma(m,u)[\mu'(u)]+\partial_v\Gamma(m,u)=-H_0[\mu'(u)]+h_1 .\qquad\square$$

*(This corrects a plausible-looking but invalid inference. It is **not** true that $h_1=\mu'(u)$ — $\log_m$ does not commute with taking a Fréchet mean. An independent adversarial computation on a 3-atom $\mathbb H^2$ family produced $h_1=1.21972252652$ against $\mu'=1$; solving $\tfrac12(1+R\coth R)=1.21972252652$ returns $R=1.2000000000$ to ten digits, i.e. **exactly** $h_1=H_0\mu'$ for that model. Numerics have zero proof status; Lemma X0 is the proof.)*

### 2.3 The expansion

> **Theorem X.** Under (E1)–(E4),
> $$\boxed{\ x_*\;=\;b\,m_1A\;+\;b^2\Big[\tfrac12m_2\,B+m_1^2\,C\Big]\;+\;O(b^3),\qquad A=\mu'(u),\quad B=H_0^{-1}h_2,}$$
> $$\boxed{\ C=-H_0^{-1}\Big(H_1A+\tfrac12T_0[A,A]\Big).\ }$$

*Proof.* Write $g_b:=D_x\Lambda(0;b)$, $H_b:=D_x^2\Lambda(0;b)$, $T_b:=D^3_x\Lambda(0;b)$. Since $D_x\,d(y,\operatorname{Exp}_mx)^2|_{x=0}=-2\log_my$ and $d\operatorname{Exp}_m|_0=\mathrm{Id}$,
$$g_b=-2\sum_tw_t\,\mathbb E\log_mX_{t,n}=-2\Big[\sum_tw_t\,h(u,u_t)\Big]+O(n^{-a}),$$
and Taylor expansion of $h(u,\cdot)$ with $\sum_tw_t(u_t-u)^k=b^km_k$ gives $\sum_tw_th(u,u_t)=b\,m_1h_1+\tfrac12b^2m_2h_2+O(b^3)$. Similarly $H_b=2[H_0+b\,m_1H_1+O(b^2)]$ and $T_b=2[T_0+O(b)]$.

Set the candidate $\hat x:=b\,m_1A+b^2[\tfrac12m_2B+m_1^2C]$. Then $\hat x=O(b)$ and a third-order Taylor expansion of $D_x\Lambda$ at $0$ gives
$$D_x\Lambda(\hat x;b)=g_b+H_b\hat x+\tfrac12T_b[\hat x,\hat x]+O(|\hat x|^3).$$
Collect by the grading $\deg(m_k)=k$, $\deg(b)=1$ (so $b^km_k$ has weight $2k$ and $\hat x$ has weight $\ge2$). The weight-$2$ terms cancel by $A=H_0^{-1}h_1$. The weight-$4$ terms are
$$-m_2h_2-2m_1^2H_1A+2H_0\big[\tfrac12m_2B+m_1^2C\big]+T_0[m_1A,m_1A]$$
(times $b^2$), which vanishes precisely for the stated $B$ and $C$. **No weight-$4$ monomial in $m_1m_2$ exists** — $m_1m_2$ has weight $3$, hence appears only at order $b^3$; the $O(b^2)$ part of $H_b$ multiplies $\hat x=O(b)$ giving $O(b^3)$; the $O(b)$ part of $T_b$ multiplies $|\hat x|^2=O(b^2)$ giving $O(b^3)$. Hence $\|D_x\Lambda(\hat x;b)\|=O(b^3)+O(n^{-a})$.

Finally, $\Lambda(\cdot;b)$ is $2$-strongly geodesically convex (Sturm, applied to the probability measure $\bar P^b_u$), and on a Hadamard manifold $\log_m$ is $1$-Lipschitz, so
$$|x_*-\hat x|\;\le\;d(\mu_b(u),\operatorname{Exp}_m\hat x)\;\le\;\tfrac12\|\operatorname{grad}\Lambda(\hat x)\|\;=\;O(b^3)+O(n^{-a}).\qquad\square$$

> **Why this is a proof and the earlier one was not.** Addendum I "solved $\operatorname{grad}\Lambda=0$ to second order", which presupposes that $x_*$ *has* an expansion in $b$. It does not follow from the implicit function theorem, because $\Lambda(x;b)$ is not jointly smooth in $b$ (the weights and design points are $b$-dependent). The plug-in-plus-coercivity route above avoids the issue entirely.

### 2.4 $C$ vanishes identically in flat space

> **Theorem Y.** If $M=\mathbb R^p$ with the Euclidean metric, then $C=0$ for **every** law family and **every** design.

*Proof.* $\tfrac12\operatorname{Hess}_q|x-q|^2=\mathrm{Id}$ for all $x,q$, so $\mathbb EH(m,X^{(v)})=\mathrm{Id}$ for every $v$ and $H_1=0$. And $\Lambda_0(x)=\mathbb E|X|^2-2\langle\mathbb EX,x\rangle+|x|^2$ is an exact quadratic, so $T_0=D^3\Lambda_0(0)=0$. $\square$

So the $m_1^2$ term is invisible in the Euclidean intuition — which is exactly why addendum I missed it. (Note $\tfrac12m_2B$ survives in $\mathbb R^p$; it is the classical local-polynomial bias. Only $C$ is a curvature effect.)

### 2.5 $C\ne0$ — an exact witness

> **Theorem Z.** Let $M=\mathbb H^2$ (curvature $-1$), $\gamma$ a unit-speed geodesic, $m=\gamma(0)$, $e_1=\gamma'(0)$, $e_2$ the unit normal, $\mu(v)=\gamma(v)$. Fix $R>0$, $\psi\ne0$, and let $w(v)\in T_{\mu(v)}M$ be the unit vector making angle $\psi(v-u)$ with $\gamma'(v)$. Let
> $$\operatorname{Law}(X^{(v)})=\tfrac12\delta_{\operatorname{Exp}_{\mu(v)}(Rw(v))}+\tfrac12\delta_{\operatorname{Exp}_{\mu(v)}(-Rw(v))}.$$
> Then $\mu(v)$ is the Fréchet mean of $X^{(v)}$, $T_0=0$, $H_0=\operatorname{diag}(1,\lambda)$ with $\lambda=R\coth R$, $A=e_1$, $H_1=\psi(1-\lambda)\sigma_x$, and
> $$\boxed{\ C=\frac{\psi(\lambda-1)}{\lambda}\,e_2\ \ne\ 0\quad\text{for every }R>0,\ \psi\ne0.\ }$$

*Proof.*
**(a) $\mu(v)$ is the Fréchet mean.** The two atoms are antipodal through $\mu(v)$, so $\tfrac12(Rw)+\tfrac12(-Rw)=0$ is the Karcher equation; on a Hadamard manifold the Fréchet functional is strictly geodesically convex, so this critical point is the unique global minimiser.

**(b) $T_0=0$, exactly.** At $v=u$ the law is $\tfrac12\delta_{\gamma(R)}+\tfrac12\delta_{\gamma(-R)}$. The geodesic symmetry $s_m(x)=\operatorname{Exp}_m(-\log_mx)$ is a global isometry of the symmetric space $\mathbb H^2$ fixing $m$, with $s_m\circ\operatorname{Exp}_m=\operatorname{Exp}_m\circ(-\mathrm{Id})$, and it swaps $\gamma(R)\leftrightarrow\gamma(-R)$, so the law is $s_m$-invariant. Hence $\Lambda_0(-x)=\Lambda_0(x)$ and every odd derivative vanishes at $0$.

**(c) $H_0=\operatorname{diag}(1,\lambda)$.** On $\mathbb H^2(-1)$, $\tfrac12\operatorname{Hess}_qd(z,\cdot)^2$ has eigenvalue $1$ in the radial direction $\log_qz$ and $\theta\coth\theta$ orthogonally, $\theta=d(z,q)$ (**CITED**, verbatim below). At $q=m$ both atoms are radial along $e_1$ at distance $R$, so both give $\operatorname{diag}(1,R\coth R)$ in the basis $(e_1,e_2)$.

**(d) $A=e_1$.** By Lemma X0, $A=\mu'(u)=\gamma'(0)=e_1$.

**(e) $H_1=\psi(1-\lambda)\sigma_x$.** Define $F(v,\alpha):=\operatorname{Exp}_{\gamma(v)}(\pm R\,w_\alpha(v))$, $w_\alpha(v)$ being $\gamma'(v)$ rotated by $\alpha$; the actual path is $v\mapsto F(v,\psi v)$, so by the chain rule $\tfrac{d}{dv}\big|_0=\partial_vF(0,0)+\psi\,\partial_\alpha F(0,0)$ — a legitimate first-order superposition. The difference between rotating about $\gamma(\delta)$ and about $m=\gamma(0)$ is $\partial_\alpha F(\delta,0)-\partial_\alpha F(0,0)=O(\delta)$, multiplied by the rotation amount $\psi\delta$, hence $O(\delta^2)$: it does not contaminate the first order.
*Translation part:* the atoms move to $\gamma(R+\delta)$ and $\gamma(-R+\delta)$, both still radial along $e_1$, so $\mathbb EH=\operatorname{diag}(1,\tfrac12[\lambda(R+\delta)+\lambda(R-\delta)])=\operatorname{diag}(1,\lambda(R))+O(\delta^2)$: **contributes zero at first order.**
*Rotation part:* both atoms stay at distance $R$ and their radial directions become $\psi\delta$ and $\pi+\psi\delta$. Since $R_{\pi+\theta}DR_{\pi+\theta}^{\!\top}=R_\theta DR_\theta^{\!\top}$, both give $R_{\psi\delta}\operatorname{diag}(1,\lambda)R_{\psi\delta}^{\!\top}$, and
$$\tfrac{d}{d\theta}\Big[R_\theta\operatorname{diag}(1,\lambda)R_\theta^{\!\top}\Big]_{\theta=0}=\big[\Omega,\operatorname{diag}(1,\lambda)\big]=(1-\lambda)\sigma_x,\qquad\Omega=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}.$$
Hence $H_1=\psi(1-\lambda)\sigma_x$.

**(f)** $C=-H_0^{-1}(H_1A+\tfrac12T_0[A,A])=-\operatorname{diag}(1,\lambda^{-1})\cdot\psi(1-\lambda)\sigma_xe_1=\tfrac{\psi(\lambda-1)}{\lambda}e_2$, and $\lambda=R\coth R>1$ for $R>0$. $\square$

> **CITED — the Hessian eigenvalues on hyperbolic space.**
> **SOURCE:** X. Pennec, *Hessian of the Riemannian Squared Distance*, supplement to *Barycentric Subspace Analysis on Manifolds*, Ann. Statist. **46**(6A) 2018, §4.1.
> **VERBATIM:** *"The eigenvectors and eigenvalues of (half) the Hessian operator are now easy to determine. By construction, $x$ is an eigenvector with eigenvalue $\mu_0=0$ (restriction to the tangent space). Then, within the tangent space at $x$, the vector $u$ (or equivalently $\log_x(y)=\theta u$) is an eigenvector with eigenvalue $\mu_1=1$. Lastly, every vector $v$ which is orthogonal to these two vectors (i.e. orthogonal to the plane spanned by $0$, $x$ and $y$) has eigenvalue $\mu_2=\theta\coth\theta$. Since $\theta\coth\theta\ge1$ (with equality only for $\theta=0$), we can conclude that the Hessian of the squared distance is always positive definite and does never vanish along the hyperbolic space."*
> **HYPOTHESIS CHECK:** the $\mu_0=0$ eigenvalue is the ambient Minkowski direction of the hyperboloid embedding, not intrinsic; it is discarded. For $n=2$ the "orthogonal complement of the plane spanned by $0,x,y$" is exactly $e_2$. **MISSING TRANSLATION:** none. **DISCHARGES:** step (c) and the sign of $\lambda-1$ in (f).

*(Independent adversarial check, zero proof status: $D^3\Lambda_0(0)$ computed to $30$ digits has all components $<1.1\times10^{-47}$; $H_0$ agrees with $\operatorname{diag}(1,R\coth R)$ to $40$ digits; $H_1$ off-diagonal agrees with $\psi(1-\lambda)$ to $40$ digits; and solving the true weighted Fréchet problem for $b=2^{-2},\dots,2^{-7}$ gives residual-halving ratio $8.000$ against the **full** prediction and $4.000$ against the prediction **with $C$ dropped** — i.e. dropping $C$ leaves an $O(b^2)$ error. The analytic proof stands without any of this.)*

### 2.6 The repair — Theorem W

> **Theorem W (scale families kill $m_1^2$ automatically).** Let $K$ be a fixed nonnegative kernel on $[0,1]$ with shape moments $\mu_k=\int v^kK(v)dv/\int K$, and let $K_j(v):=K(v/c_j)/c_j$, $j=1,\dots,J$, be one-sided kernels on $[0,c_jb]$ with distinct $c_j>0$. Then
> $$m_1(j)=c_j\mu_1,\qquad m_2(j)=c_j^2\mu_2,\qquad m_1(j)^2=c_j^2\mu_1^2=\frac{\mu_1^2}{\mu_2}\,m_2(j)\quad\text{identically in }j .$$
> Consequently the $b^2$ coefficient $\tfrac12m_2(j)B+m_1(j)^2C=m_2(j)\big[\tfrac12B+\tfrac{\mu_1^2}{\mu_2}C\big]$ is a **single fixed vector times $m_2(j)$**, and any $\lambda$ with $\sum_j\lambda_j=1$, $\sum_j\lambda_jc_j=0$, $\sum_j\lambda_jc_j^2=0$ annihilates both the $b$ and the $b^2$ terms. **$J=3$ suffices.**

*Equivalent one-line reason.* For a scale family the entire bias is a function of the **single** effective bandwidth $h_j=c_jb$: $x_*(j)=\beta(c_jb)$ with $\beta(h)=\mu_1Ah+[\tfrac12\mu_2B+\mu_1^2C]h^2+O(h^3)$ and $h$-independent coefficients. Classical Richardson extrapolation in $h$ then applies verbatim, at the boundary as much as in the interior — because a **one-sided kernel looking into the domain is never truncated**, so its moments are $u$-independent throughout $[0,1-c_{\max}b]$.

**Explicit admissible choice.** $K(v)=v^2(1-v)^2$ on $[0,1]$ — nonnegative, $C^1$, and vanishing to first order at *both* endpoints ($K(0)=K'(0)=K(1)=K'(1)=0$), which is what makes $u\mapsto w_t(u)$ differentiable as design points enter and leave the window (§5). Its shape moments are $\mu_1=\tfrac12$, $\mu_2=\tfrac27$, so $\mu_1^2/\mu_2=\tfrac78$. With
$$c=(1,\tfrac12,\tfrac14),\qquad \lambda=(\tfrac13,\,-2,\,\tfrac83),\qquad\|\lambda\|_1=5,$$
one has $\sum\lambda=1$, $\sum\lambda m_1=0$, $\sum\lambda m_2=0$ and $\sum\lambda m_1^2=0$, the last **automatically**.

> **Why the user's proposed $J=4$ system is not the repair.** The $4\times4$ matrix $[\,1;\,m_1(j);\,m_2(j);\,m_1(j)^2\,]$ is **identically singular for any scale family** (column 4 $=\tfrac{\mu_1^2}{\mu_2}\times$ column 3), so it cannot be made nonsingular by choosing the $c_j$. It becomes nonsingular only for kernels of genuinely different **shapes**, with at least two distinct values of $\mu_1^2/\mu_2$ (uniform $\tfrac34$, $2(1-t)$ $\tfrac23$, $2t$ $\tfrac89$, $v^2(1-v)^2$ $\tfrac78$). So the correct statement is: *four constraints are required in general; for a one-parameter scale family the fourth is implied by the third, and $J=3$ suffices.* The user's diagnosis of the **defect** was exactly right; the proposed **remedy** is unnecessary and, for the natural construction, unachievable.

**Verification of the $J=3$ claim of addendum I as it was actually written.** Addendum I proposed $J=3$ kernels of *different shapes* with $\sum\lambda=1$, $\sum\lambda m_1=0$, $\sum\lambda m_2=0$. For the shape family $K_p(v)=(p+1)v^p$, $p=0,1,2$: $\lambda=(9,-18,10)$ and $\sum_j\lambda_jm_1(j)^2=-\tfrac18\ne0$. **Addendum I's construction leaves an $O(b^2)$ bias. Disproved.**

---

## §3 What CE-9 actually proves — and why G1 as stated survives

### 3.1 The correct scope of CE-9

CE-9 proves, and only proves:

1. **No unconditional global-convexity or uniqueness theorem exists for signed Fréchet criteria on Cartan–Hadamard manifolds.** (Independently reproduced: weights $(3,-2)$ on $\mathbb H^2$ with atoms at distances $0.2$ and $3.0$ give $\operatorname{Hess}\Lambda(0)=\operatorname{diag}(2,-5.9798\ldots)$, indefinite — while the *same weights* in $\mathbb R^p$ give $2\sum_tw_t\,\mathrm{Id}=2\,\mathrm{Id}\succ0$ always. **The failure mode is invisible in Euclidean intuition.**)
2. Hence the bare `argmin` specification of the estimator is genuinely **set-valued** for admissible finite configurations and must be replaced by a **localised** specification.
3. Hence the assumptions (L0)/(L3) of Petersen–Müller and (R1)/(R3) of Chen–Müller — which are imposed *on the signed objective* — are **not derivable from Hadamard geometry alone**, and their only manifold-side citation (Afsari 2011) is stated for probability measures and does not apply.

CE-9 does **not** prove that the statistical $O_p$ rate fails. Addendum I's headline claimed otherwise. **That claim is withdrawn.**

### 3.2 Why the statistical estimator is safe: the signed part is a vanishing perturbation

Write $w_t=w_t^+-w_t^-$, $W^\pm=\sum_tw_t^\pm$, $W^+-W^-=1$, $\|w\|_1=W^++W^-$. The crucial structural fact, invisible in a worst-case deterministic construction, is that **in the locally stationary model the positively- and negatively-weighted observations are drawn from laws that converge to the *same* limit $P_u=\operatorname{Law}(X^{(u)})$ as $b\to0$**, at rate $O(b)$.

> **Theorem SW-AS.** Assume (H1)–(H7) with signed weights satisfying $\sup_u\|w(u)\|_1\le W<\infty$; a.s. support radius $\rho^*$; $v\mapsto\mathbb EH(q,X^{(v)})$ Lipschitz in $v$ uniformly in $q\in\bar B(\mu(u),\rho)$; and $x\mapsto H(q,x)$ Lipschitz with constant $L_H=L_H(\bar K,\rho^*)$ on the relevant range. Then
> $$\sup_{u\in[0,1]}\ \sup_{q\in\bar B(\mu(u),\rho)}\Big\|\tfrac12\operatorname{Hess}_q\hat F_u-H_{P_u}(q)\Big\|_{\mathrm{op}}\;=\;O_p\Big(W\big[b+n^{-a}+\sqrt{\tfrac{p+\log n}{nb}}\big]\Big)\;\xrightarrow{\ p\ }\;0,$$
> where $H_{P_u}(q):=\mathbb E\,H(q,X^{(u)})\succeq\mathrm{Id}$ on a Hadamard manifold (T-EXT-1). Hence, with probability tending to one, $\hat F_u$ is $2\lambda_n$-strongly geodesically convex on $\bar B(\mu(u),\rho)$ **uniformly in $u$**, with $\lambda_n\to1$. The same statement with the stochastic term deleted holds for $\bar F_u$.

*Proof.* $\tfrac12\operatorname{Hess}_q\hat F_u=\sum_tw_t(u)H(q,X_{t,n})$. Split:
$$\sum_tw_t\big[H(q,X_{t,n})-\mathbb EH(q,X_{t,n})\big]\;+\;\sum_tw_t\big[\mathbb EH(q,X^{(u_t)})-H_{P_u}(q)\big]\;+\;H_{P_u}(q)\;+\;O(WL_Hn^{-a}),$$
using $\sum_tw_t=1$ in the third term and the local-stationarity replacement (bounded by $L_H\sum_t|w_t|\,\|X_{t,n}-X^{(u_t)}_t\|_1$) in the fourth. The second term is $O(WLb)$ by the assumed Lipschitz continuity in $v$ and $|u_t-u|\le b$. The first is a matrix-valued kernel-weighted centred sum with bounded entries ($\|H\|\le\zeta(2\rho^*)$, T-EXT-1) and Lipschitz-in-$q$ with constant $L_H$; the argument of addendum I Theorem B applies verbatim after (i) a $\tfrac12$-net of the $p(p+1)/2$-dimensional unit sphere of symmetric matrices and (ii) an $\epsilon$-net of $\bar B(\mu(u),\rho)$ with $\log N(\epsilon)\le p\log(C/\epsilon)$, both absorbed into $\gamma$; it is $O_p(W\sqrt{(p+\log n)/(nb)})$. $\square$

> **This is the exact point the user identified.** Curvature ($\zeta$ unbounded) can destroy convexity for an *arbitrary* signed configuration; it cannot do so for the configurations the model actually produces, because the negative weights attach to observations whose law is within $O(b)$ of the law carrying the positive weights.

### 3.3 The estimator specification CE-9 forces

> **Definition (localised local-polynomial Fréchet estimator).** Let $\tilde\mu(u)$ be the positive-weight kernel Fréchet mean (unique by Sturm, no assumption). Fix $\delta_0>0$ and set
> $$\hat\mu(u)\ :=\ \arg\min\big\{\hat F_u(q)\ :\ q\in\bar B\big(\tilde\mu(u),\delta_0\big)\big\}.$$
> The ball is geodesically convex (Hadamard), so on the event of Theorem SW-AS the restricted problem is strictly convex and the minimiser is unique; and since $d(\hat\mu(u),\mu_b(u))=o_p(1)$ and $d(\tilde\mu(u),\mu(u))=o_p(1)$ uniformly, the minimiser is interior with probability tending to one, so it is a genuine critical point of $\hat F_u$.

> **Theorem G1-LP.** Under (H1)–(H7) with the degree-$d$ local-polynomial equivalent weights ($d\ge2$), the localised specification above, (H4a), $\mu\in C^{d+1}$, $\alpha(m)\le Am^{-\beta}$ with $\beta>1+2\gamma/(1-\alpha)$, $nb/\log n\to\infty$, $a>\min\big((d{+}1)\alpha,\tfrac{1-\alpha}2\big)$, and $\inf_u\lambda_{\min}$ of the local design matrix bounded away from $0$:
> $$\boxed{\ \sup_{u\in[0,1]}d\big(\hat\mu(u),\mu(u)\big)\;=\;O_p\Big(b^{\,d+1}+\sqrt{\tfrac{\log n}{nb}}\Big).\ }$$
> **This is G1 exactly as originally stated**, with $q=q_{\mathrm{bdry}}=d+1\ge3$, on the closed $[0,1]$, under polynomial mixing, with **no** (G7)/(SW) condition.

*Proof.* By Theorem SW-AS, on an event of probability $\to1$ both $\hat F_u$ and $\bar F_u$ are $2\lambda_n$-strongly geodesically convex on the (convex) ball, with $\lambda_n\to1$. Strong convexity gives $\|\operatorname{grad}\hat F_u(z)\|\ge2\lambda_nd(z,\hat\mu(u))$ for $z$ in the ball; taking $z=\mu_b(u)$ and using $G_u(\mu_b(u))=0$ reproduces **Theorem A′ with constant $\lambda_n^{-1}$**:
$$d(\hat\mu(u),\mu_b(u))\ \le\ \lambda_n^{-1}\big\|\hat G_u(\mu_b(u))-G_u(\mu_b(u))\big\| .$$
Theorem B then gives $O_p(\sqrt{(p+\log n)/(nb)})$ uniformly. For the bias, the degree-$d$ equivalent weights satisfy the reproducing property $\sum_tw_t(u)(u_t-u)^k=\delta_{k0}$ for $k=0,\dots,d$ — **exactly, at boundary points too**, provided the local design matrix is nonsingular, which the equispaced grid with $nb\to\infty$ and the bounded-below design-matrix condition guarantee. Hence $m_1=\dots=m_d=0$ **exactly**, so in Theorem X's grading the leading surviving term is
$$x_*=\frac{b^{\,d+1}m_{d+1}}{(d+1)!}H_0^{-1}h_{d+1}+O(b^{\,d+2})+O(n^{-a}),$$
and **all cross terms are automatically absorbed**: $H_b-2H_0=O(b^{d+1})$ and $x_*=O(b^{d+1})$, so nonlinear corrections are $O(b^{2d+2})$ and $2d+2\ge d+3$ for $d\ge1$. **The $m_1^2$ problem does not arise for this estimator at all.** $\square$

> **Two things worth recording.** (i) The signed local-polynomial estimator, once localised, is *better behaved* than the positive-weight multi-kernel construction, because $m_1=0$ exactly removes the entire $C$ issue. (ii) It is the *only* one of the two that needs Theorem SW-AS, i.e. a maximal inequality for the Hessian. The positive-weight route (Theorem W) needs none — Sturm does everything. Both are now proved; they trade a maximal inequality against a constant $\|\lambda\|_1=5$ inflation of the variance.

### 3.4 What remains genuinely open about signed weights

* Theorem SW-AS is an **asymptotic** statement. For fixed $n$ the localisation radius $\delta_0$ and the event probability are not quantified beyond $O_p$; a finite-sample statement would need explicit constants in $\zeta(2\rho^*)$, $L_H$, $W$.
* The Lipschitz-in-$x$ bound $\|\partial_xH(q,x)\|\le L_H(\bar K,\rho^*)$ is used but not proved here. It is a third-covariant-derivative bound on $\tfrac12d^2$ under two-sided curvature bounds on a compact range; it is standard comparison geometry but it is a **proof obligation**, not a citation, and it is recorded as such.
* **(G7)/(SW) is withdrawn as a hypothesis.** It survives only as: *a sufficient condition under which the un-localised global argmin is unique for every finite $n$.* It is proved sufficient (addendum I Theorem SW) and proved necessary in kind for that purpose (CE-9(f)) — but it is **not** needed for the rate.

---

## §4 The $L^2$ theorem, repaired

Addendum I §5.1 is correct in architecture and wrong in two hypotheses. Corrected statement:

> **Theorem E$_{L^2}$ (corrected).** Assume (H1)–(H3), (H6), (H7)(P), and: for some **moment order $r>2$**,
> $$\sup_{t,n}\ \mathbb E\,d\big(X_{t,n},\mu_b(u)\big)^{r}\ \le\ C_r<\infty,\qquad \mathcal A_r:=\sum_{h\ge1}\alpha(h)^{1-2/r}<\infty .$$
> Then
> $$\Big(\int_0^1d\big(\hat\mu(u),\mu_b(u)\big)^2du\Big)^{1/2}=O_p\big((nb)^{-1/2}\big)\qquad\text{with no }\log n,$$
> and, with the bias of §2 and the boundary region having Lebesgue measure $O(b)$,
> $$\big\|d(\hat\mu(\cdot),\mu(\cdot))\big\|_{L^2(du)}=O_p\big(b^{\,q_{\mathrm{int}}}+b^{\,q_{\mathrm{bdry}}+1/2}+(nb)^{-1/2}+n^{-a}\big).$$

*Proof.* By **Theorem A′** — not by any entropy argument —
$$\mathbb E\,d(\hat\mu(u),\mu_b(u))^2\ \le\ \mathbb E\big\|\hat G_u(\mu_b(u))-G_u(\mu_b(u))\big\|^2 .$$
Fix the deterministic orthonormal frame $\Xi_u$ of addendum I Lemma P4 and set $\xi_t:=\Xi_u(\log_{\mu_b(u)}X_{t,n}-\mathbb E\log_{\mu_b(u)}X_{t,n})\in\mathbb R^p$, so $\|\xi_t\|\le2d(X_{t,n},\mu_b(u))$ and $\mathbb E\|\xi_t\|^r\le2^rC_r$. Then
$$\mathbb E\Big\|\sum_tw_t\xi_t\Big\|^2=\sum_{j=1}^p\sum_{t,s}w_tw_s\operatorname{Cov}(\xi_{tj},\xi_{sj}).$$
By Rio's covariance inequality (Davydov form) with exponents $(r,r,w)$, $\tfrac2r+\tfrac1w=1$, i.e. $\tfrac1w=1-\tfrac2r$,
$$|\operatorname{Cov}(\xi_{tj},\xi_{sj})|\ \le\ 2^{1+1/w}\alpha(|t-s|)^{1-2/r}\|\xi_{tj}\|_r\|\xi_{sj}\|_r .$$
Hence the double sum is at most $C\,p\,C_r^{2/r}\big(1+2\mathcal A_r\big)\max_t|w_t|\sum_t|w_t|=O(p/(nb))$, using $\max_tw_t(u)=O((nb)^{-1})$ and $\sum_tw_t=1$. Integrate in $u$ (Fubini) and apply Markov. $\square$

**The two repairs.** (i) The exponent is the **moment order $r$**, not the smoothness $s$ of $\mu$ — a notation collision in addendum I that also mis-stated the substance. With $\mathbb E D_t^4<\infty$ ($r=4$) the requirement is $\sum_h\alpha(h)^{1/2}<\infty$, exactly as the user guessed. (ii) The proof no longer invokes "a Dudley entropy bound in $L^2$"; Theorem A′ removes the need for any entropy argument, because the evaluation point $\mu_b(u)$ is deterministic.

**Corollary (the boundary is softened by half an order in $L^2$).** For the plain positive-weight kernel Fréchet estimator ($q_{\mathrm{int}}=2$, $q_{\mathrm{bdry}}=1$) this is $O_p(b^{3/2}+(nb)^{-1/2}+n^{-a})$.

---

## §5 Theorem G1′$_{L^2}$, as a real derivative theorem

Addendum I asserted this in one sentence. The hypotheses the user asked for are exactly the following, and none of them is cosmetic.

> **Hypotheses.**
> **(D1) Kernel regularity.** $K\in C^1$, supported on a compact interval, and **vanishing to first order at both endpoints of its support**: for the one-sided family, $K(0)=K'(0)=K(1)=K'(1)=0$. Concretely $K(v)=v^2(1-v)^2$ on $[0,1]$. *Reason:* on the equispaced grid, design points enter and leave the window as $u$ varies; without $K=K'=0$ at the endpoints, $u\mapsto w_t(u)$ has jumps of size $O((nb)^{-1})$ at $\Theta(n)$ values of $u$ per unit interval, contributing total variation $\Theta(1/b)$ — the same order as the smooth part — and $u\mapsto\hat\mu(u)$ is then not $C^1$. The Epanechnikov kernel **fails** this ($K'(\pm1)\ne0$); the biweight and $v^2(1-v)^2$ satisfy it.
> **(D2) Denominator.** $\inf_{u}\ (nb)^{-1}\sum_sK((u_s-u)/(c_jb))\ \ge\ \underline c>0$ for each $j$ and all large $n$. On the equispaced grid this is the Riemann sum of $\int K>0$ over a window of length $c_jb$ fully inside $[0,1]$, so it holds for $u\in[0,1-c_{\max}b]$ (forward kernels) and $u\in[c_{\max}b,1]$ (backward kernels).
> **(D3) Boundary transition.** Use forward kernels on $[0,1-2b]$, backward kernels on $[1-b,1]$, and on the overlap $[1-2b,1-b]$ set $\hat\mu(u):=\operatorname{Exp}_{\hat\mu_F(u)}\big(\chi(u)\log_{\hat\mu_F(u)}\hat\mu_B(u)\big)$ with $\chi\in C^1$, $\chi(1-2b)=0$, $\chi(1-b)=1$, $|\chi'|=O(1/b)$. *Reason:* a hard switch leaves a jump in $\hat\mu$ of size $O(b^q+\sqrt{\log n/(nb)})$, which contributes a Dirac to $\nabla_se$ and a holonomy of order $n^{-2/5}\gg n^{-1/2}$ at $\alpha=1/5$ — **not negligible**. The blend costs nothing: the bias is a convex combination of two $O(b^q)$ biases, and $|\chi'|\cdot d(\hat\mu_F,\hat\mu_B)=O(b^{q-1}+(nb^3)^{-1/2})$, the same order as $\nabla_u\hat\mu$ itself.
> **(D4) Hessian invertibility.** $\tfrac12\operatorname{Hess}\hat F_u\succeq\lambda_n\mathrm{Id}$ — free by Sturm for positive weights, by Theorem SW-AS for signed weights.
> **(D5) Differentiability of the bias.** $h(u,v)$ jointly $C^{q+1}$, $u\mapsto H_0(u)$ and $u\mapsto h_k(u)$ in $C^1$, and the moments $u$-independent (guaranteed by the one-sided scale family on $[0,1-c_{\max}b]$, and by the reproducing property for the local-polynomial weights).

> **Theorem G1′$_{L^2}$.** Under (D1)–(D5) and the hypotheses of Theorem E$_{L^2}$,
> $$\big\|\nabla_se\big\|_{L^2(du)}\;=\;O_p\big(b^{q}+(nb^3)^{-1/2}\big),\qquad e(u):=\log_{\mu(u)}\hat\mu(u).$$

*Proof.* By (D1)–(D2), $u\mapsto w_t(u)$ is $C^1$ with $|\partial_uw_t(u)|=O((nb^2)^{-1})$, and differentiating $\sum_tw_t(u)=1$ gives $\sum_t\partial_uw_t(u)=0$ identically — so $\partial_u\hat G_u(q)=\sum_t\partial_uw_t(u)\log_qX_t$ is automatically weight-centred.
By (D4) and the implicit function theorem applied to the smooth section $(u,q)\mapsto\hat G_u(q)$ (whose $q$-derivative is $-\tfrac12\operatorname{Hess}\hat F_u$, invertible), $u\mapsto\hat\mu(u)$ is $C^1$ and
$$\nabla_u\hat\mu(u)=\Big[\tfrac12\operatorname{Hess}\hat F_u(\hat\mu(u))\Big]^{-1}\partial_u\hat G_u\big(\hat\mu(u)\big).$$
Exactly as in Theorem E$_{L^2}$ but with $w_t$ replaced by $\partial_uw_t$,
$$\mathbb E\big\|\partial_u\hat G_u(q)-\partial_uG_u(q)\big\|^2\ \le\ C\,p\,C_r^{2/r}(1+2\mathcal A_r)\max_t|\partial_uw_t|\sum_t|\partial_uw_t|\ =\ O\!\Big(\tfrac1{nb^2}\cdot\tfrac1b\Big)=O\Big(\tfrac1{nb^3}\Big),$$
using $\sum_t|\partial_uw_t|=O(1/b)$. The deterministic part is $\nabla_u(\mu_b-\mu)=O(b^q)$ by (D5).
Finally, $e=\log_\mu\hat\mu$ gives $\nabla_se=D_1\log(\mu,\hat\mu)[\mu']+D_2\log(\mu,\hat\mu)[\nabla_u\hat\mu]$, and at $\hat\mu=\mu$ one has $D_1=-\mathrm{Id}$, $D_2=+\mathrm{Id}$, with corrections **quadratic** in $|e|$ (Pennec eq. (5): $-[D_x\log_x(y)]^a_b=\delta^a_b-\tfrac13R^a_{cbd}\,\overrightarrow{xy}^{\,c}\overrightarrow{xy}^{\,d}+\dots$). Hence
$$\nabla_se=\big(\nabla_u\hat\mu-\mu'\big)+O\big(\bar K|e|^2(|\mu'|+|\nabla_u\hat\mu|)\big),$$
and the remainder is $o_p((nb^3)^{-1/2})$ since $|e|\to0$. Integrate in $u$ and apply Markov; on the blend interval (D3) the extra contribution is of the same order and the interval has length $b$. $\square$

**Status.** This is now a theorem, not a skeleton. Its weakest link is (D5)'s joint smoothness assumption on the law family, which is a modelling hypothesis and should be stated in the paper's assumption set rather than assumed silently.

---

## §6 Revised status board

| Item | Addendum I status | Status now | Why |
|---|---|---|---|
| **G1 as stated** | DISPROVED | **PROVED** (Theorem G1-LP), for the localised argmin specification, $q=d+1\ge3$, closed $[0,1]$, polynomial mixing | Retraction 1; Theorem SW-AS |
| **(G7)/(SW)** | NEW assumption, "necessary in kind" | **WITHDRAWN as a hypothesis.** Survives only as a finite-$n$ sufficient condition for *global* (un-localised) uniqueness | Theorem SW-AS |
| **CE-9** | "disproves G1" | **Correct as a counterexample; headline corrected.** It disproves unconditional signed-objective uniqueness/global convexity and forces the localised specification. Nothing more. | Retraction 1 |
| **Addendum I Theorem A** | PROVED | **SUPERSEDED** by Theorem A′ (constant $1$, deterministic evaluation point) | §1 |
| **Addendum I §3.2** (Lemmas P2, P3, peeling) | PROVED | **NO LONGER NEEDED** | §1 |
| **Addendum I Theorem G1-H ($J=3$, multi-shape)** | PROVED | **DISPROVED as written** ($\sum\lambda m_1^2=-\tfrac18\ne0$ for its own kernel family) | Theorems X, Z |
| **Addendum I §4.1** ("bandwidth-Richardson fails at the boundary") | asserted | **WITHDRAWN.** True only for truncated two-sided kernels; false for one-sided kernels looking into the domain | Retraction 3 |
| **Repair** | — | **PROVED**: Theorem W, $J=3$ one-sided **scale** family, $c=(1,\tfrac12,\tfrac14)$, $\lambda=(\tfrac13,-2,\tfrac83)$ | §2.6 |
| **User's $J=4$ system $\{1,m_1,m_2,m_1^2\}$** | — | **Not needed; unachievable for a scale family** (matrix identically singular). Needed only for genuinely different shapes | §2.6 |
| **Theorem E$_{L^2}$** | PROVED (with a wrong exponent and an unnecessary Dudley step) | **PROVED**, repaired: moment order $r>2$, $\sum_h\alpha(h)^{1-2/r}<\infty$; no entropy argument at all | §4 |
| **G1′$_{L^2}$** | "PROVED" (one sentence) | **PROVED**, with (D1)–(D5) stated and justified | §5 |
| **$n^{-a}$ remainder** | omitted | **carried**; requires $a>\min(q\alpha,\tfrac{1-\alpha}2)$ ($=2/5$ at $\alpha=1/5$, $q=3$) | §3.3, §4 |
| **$A=\mu'(u)$** | — | **PROVED** (Lemma X0). Note $h_1\ne\mu'(u)$; the correct identity is $h_1=H_0\mu'(u)$ | §2.2 |
| **Theorem E, T17–T26, downstream** | PROVED | **unchanged** — the $L^2$ sufficiency argument of addendum I §5.2 is untouched and is strengthened by Theorem A′ | — |

### Still open after this run

1. **The Lipschitz bound $\|\partial_xH(q,x)\|\le L_H(\bar K,\rho^*)$** used in Theorem SW-AS. Standard comparison geometry; a proof obligation, not yet discharged.
2. **Finite-sample quantification of Theorem SW-AS** — the localisation radius $\delta_0$ and the event probability.
3. **Growing dimension $p_n\to\infty$** — unchanged and still the binding structural gap (no Hilbert-valued Bernstein under mixing; the sphere-net device costs $5^p$, and Theorem SW-AS additionally needs a net of symmetric matrices costing $5^{p(p+1)/2}$, so the signed route degrades **faster** in $p$ than the positive-weight route).
4. **$q\ge4$** for the positive-weight scale family: Theorem W's argument extends ($\sum\lambda c_j^k=0$, $k=1,2,3$, $J=4$), but the tangent-space combination's curvature cost $O(\bar Kr_n^3)$ still caps the achievable order at $3$ unless a third-order correction is added. For the **local-polynomial** route there is no such cap: $q=d+1$ for any $d$.
5. **Necessity of the mixing threshold** and **Paper 2's gap 2** — unchanged.

---

## §7 Patches

### To [[G1 audit — resolution of the uniform local Fréchet rate]]
1. **§0 verdict table** — replace the "G1 as stated: DISPROVED" row with "**PROVED** (Theorem G1-LP, addendum II), localised argmin specification required".
2. **§2.4 (G7)/(SW)** — retitle as a *finite-$n$ sufficient condition for global uniqueness*; delete "necessary in kind" as a claim about the **rate**.
3. **§2.3 CE-9** — keep the counterexample verbatim; replace the three "What it kills" items with the corrected scope of addendum II §3.1.
4. **§3.1 Theorem A** — replace by Theorem A′.
5. **§3.2 (Lemmas P2, P3) and the peeling in Theorem C** — delete.
6. **§4.1** — delete the claim that bandwidth-Richardson fails at the boundary; replace by Retraction 3.
7. **§4.2–4.3** — replace the multi-shape $J=3$ construction and Theorem G1-H by Theorem W and Theorem G1-LP.
8. **§5.1** — replace $\sum_h\alpha(h)^{1-2/s}$ by $\sum_h\alpha(h)^{1-2/r}$ with $r$ a moment order, and state the moment hypothesis.
9. **§5.1 Corollary (G1′)** — replace by §5 of this note.
10. **§9 status table** and **§10 patch list** — regenerate from §6 above.

### To [[Analytical reconstruction — proof ledger and rebuilt spec]]
11. **Header note (2026-08-08)** — replace "G1 as stated is DISPROVED" by "**G1 as stated is PROVED** for the localised local-polynomial specification; CE-9 forces the localisation but does not defeat the rate."
12. **§5.1 (G7)** — demote to a remark: *sufficient for global uniqueness at finite $n$; not required for the rate (Theorem SW-AS).*
13. **§4.9 CE-9** — replace the "What it kills" list by addendum II §3.1, and add the independently reproduced indefinite-Hessian example (weights $(3,-2)$, atoms at $0.2$ and $3.0$ on $\mathbb H^2$, $\operatorname{Hess}=\operatorname{diag}(2,-5.9798)$, versus $2\,\mathrm{Id}\succ0$ for the same weights in $\mathbb R^p$).
14. **§5.4** — the correction stands, but restate the conclusion: on Cartan–Hadamard the assumptions are vacuous for the population mean and for positive weights, and for the signed estimator they are replaced not by (G7) but by a **specification requirement** (localised argmin) plus Theorem SW-AS.

### To [[Paper 1 — Locally stationary Riemannian factor model]]
15. **Line 162** — the $\lambda_-/\lambda_+>(L-1)/(L+1)$ condition remains proved sufficient, but add: *it is not required for the asymptotic rate; what is required is that the estimator be specified as a localised argmin.*
16. **Line 35** — the estimator display must be corrected to the degree-$d$ local-polynomial form and must state the localisation.
17. **Named gap 1** — mark **closed** by Theorem G1-LP; keep growing dimension as the successor gap.

---

## Related notes

- [[G1 audit — resolution of the uniform local Fréchet rate]] — addendum I, superseded on three points
- [[Analytical reconstruction — proof ledger and rebuilt spec]]
- [[Paper 1 — Locally stationary Riemannian factor model]]
- [[Paper 2 — Moving loading subbundle]]
- [[Local Fréchet regression]], [[Holonomy]]
