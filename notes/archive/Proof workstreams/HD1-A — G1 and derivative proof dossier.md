---
type: proof-dossier
title: HD1-A — G1 and derivative proof dossier
status: noncanonical-workstream
verdict: growing-p positive-weight G1 and the integrated derivative chain are proved under a uniform bounded-total-energy, finite-memory regime; the generic derivative term is n^{-a}/b
last-audited: 2026-08-08
area:
  - geometry
  - time-series
  - factor-models
---

# HD1-A — G1 and derivative proof dossier

> **Scope and authority.** This is Workstream A's noncanonical proof dossier for the growing-dimension Paper 1 run. It does not edit or supersede the canonical files. It concerns only G1, integrated G1, and G1′. Paper 2 is not considered.

## 1. Verdict and migration map

The positive-weight three-scale route admits a genuinely dimension-free theorem for arbitrary \(p_n=\dim M_n\), hence in particular for \(p_n\to\infty\), provided total tangent energy, short-memory length, and geometric \(C^1\) constants are uniform. No sphere net occurs. The direct concentration variable is a vector in \(T_qM_n\), treated as a Hilbert-space element.

The derivative statement currently recorded in the canonical G1 audit is not valid under its stated level-only local-stationarity hypothesis. The generic contribution is

$$
\frac{n^{-a}}{b_n},
$$

and this loss is sharp. It improves to \(n^{-a}\) only under a differentiably coherent local-stationarity assumption stated below. A second repair is required: a forward/backward transition layer of width \(b_n\) changes an \(O(b_n^3)\) deterministic level discrepancy into an \(O(b_n^{5/2})\) \(L^2\)-derivative discrepancy. A fixed-width interior blend preserves order \(b_n^3\).

| Node | Status here | Direct consumers |
|---|---|---|
| deterministic three-scale weight bounds | **PROVED** | score concentration, derivative theorem |
| dimension-free Hilbert concentration under finite memory | **PROVED** | uniform G1, integrated G1, derivative G1′ |
| continuous-\(u\) interpolation without a \(p_n\)-net | **PROVED** | uniform G1 |
| empirical Sturm reduction for each positive stage | **PROVED/CITED** in the canonical audit; application checked here | stage G1 |
| uniform \(C^1\) population barycentre expansion | **PROVED UNDER EXPLICIT ASSUMPTIONS** | Richardson bias and derivative bias |
| three-scale cancellation including \(m_1^2C\) | **PROVED** | final \(b_n^3\) bias |
| differentiation through the Exp/Log Richardson map | **PROVED UNDER EXPLICIT ASSUMPTIONS** | G1′ |
| random-point implicit Karcher differentiation without operator concentration | **PROVED** | dimension-free G1′ |
| width-\(b_n\) boundary blend at derivative order \(b_n^3\) | **DISPROVED** | replaced by fixed-width blend |
| derivative theorem without a local-stationarity term | **DISPROVED** | replaced by \(n^{-a}/b_n\) theorem |
| improvement \(n^{-a}/b_n\to n^{-a}\) | **PROVED UNDER EXPLICIT ASSUMPTIONS** | optional stronger G1′ |

The signed local-polynomial route is not consumed. Its empirical Hessian process is bypassed, not solved.

## 2. Uniform triangular-array assumptions

Let \(M_n\) be a Hadamard manifold of dimension \(p_n\), with \(p_n\) unrestricted. Put \(u_t=t/n\), \(b=b_n\), and let \(\mu_n:[0,1]\to M_n\).

**(A1) Uniform bounded geometry on the working tube.** There are constants \(R_*,H_*,L_*,C_*\), independent of \(n,p_n\), such that on every pair and triple of points at distance at most \(R_*\) from the mean curve:

1. \(I\preceq H_n(q,x):=\frac12\operatorname{Hess}_q d_n(q,x)^2\preceq H_*I\);
2. \(H_n(q,x)\) is \(L_*\)-Lipschitz in \(q\), after parallel identification, and in \(x\);
3. the first four differentials of Exp, Log, parallel connectors, and
   $$
   \mathcal R_n(x_1,x_2,x_3)
   :=\operatorname{Exp}_{x_1}\left(\sum_{j=1}^3\lambda_j\operatorname{Log}_{x_1}x_j\right)
   $$
   have norm at most \(C_*\), after the natural parallel identifications. Equivalently, the third differential used in the cubic Taylor remainder and its first covariant derivative are uniformly bounded.

These are abstract dimension-uniform tube constants. For affine-invariant SPD of arbitrary matrix size, the archived H-LIP proof establishes the curvature, non-conjugacy, and first-Hessian-derivative portion: \(\nabla R=0\), \(\lvert R\rvert\le1\), nonpositive curvature, and dimension-free first-variation Jacobi bounds on a uniformly bounded tube. That archived proof does **not** derive the third/fourth Exp--Log differentials now consumed by Lemma 5.2. Their uniform boundedness remains an explicit primitive of this theorem unless a higher-Jacobi-variation lemma is supplied; it must not be attributed to H-LIP alone. If observations are \(m_n\times m_n\) SPD matrices, then \(p_n=m_n(m_n+1)/2\).

**(A2) Bounded total energy.** Almost surely,

$$
\sup_{t,n}d_n(X_{t,n},\mu_n(u_t))\le R<R_*/12.
$$

The same bound holds for the stationary proxy variables below. This is a total Hilbert-norm bound, not a coordinatewise bound. Also \(\sup_n(\|\mu_n'\|_\infty+\|\nabla_u\mu_n'\|_\infty)\le C_\mu\).

**(A3) Coherent finite memory.** For one fixed integer \(m\), independent of \(n,p_n\), every row \((X_{t,n})_{t=1}^n\) is \(m\)-dependent: sigma fields generated by indices at distance greater than \(m\) are independent. The stationary proxy rows have the same property. This includes finite-memory Bernoulli shifts. It is a dependent, dimension-uniform short-memory regime. No claim is made here that a fixed polynomial-mixing exponent suffices.

**(A4) Smooth proxy laws.** There are stationary proxy variables \(X_t^{(v,n)}\), \(v\in[0,1]\), whose Fréchet mean is \(\mu_n(v)\). In a parallel trivialisation of the mean-curve tube, the maps

$$
(u,v,q)\longmapsto \mathbb E\operatorname{Log}_qX_t^{(v,n)},\qquad
(u,v,q)\longmapsto \mathbb EH_n(q,X_t^{(v,n)})
$$

have all covariant derivatives used below, through total order four for the first map and order three for the second, bounded by one constant. Differentiation under expectation is part of this assumption. This supplies a \(C^1\)-uniform third-order Taylor remainder; merely \(C^3\) pointwise smoothness is not enough for G1′.

**(A5-0) Level local stationarity.** The variables can be coupled so that

$$
\sup_{t,n}\|d_n(X_{t,n},X_t^{(u_t,n)})\|_{L^\infty}\le Cn^{-a}.
$$

By (A1), the induced score and Hessian-action defects are \(O(n^{-a})\). This gives \(n^{-a}\) in the level theorem and \(n^{-a}/b\) in the derivative theorem.

The optional stronger replacement is:

**(A5-1) Differentiably coherent local stationarity.** For each stage, the weighted expected-score defect

$$
D_{j,n}(u,q):=\sum_t w_{j,t}(u)
\left\{\mathbb E\operatorname{Log}_qX_{t,n}
-\mathbb E\operatorname{Log}_qX_t^{(u_t,n)}\right\}
$$

satisfies, on the tube,

$$
\sup_{j,u,q}\big(\|D_{j,n}\|+\|\nabla_uD_{j,n}\|+\|\nabla_qD_{j,n}\|\big)\le Cn^{-a}.
$$

This is the exact stronger hypothesis that removes \(b^{-1}\); it is not implied by (A5-0).

**(A6) Kernel, scales, and design.** Extend a nonnegative \(K\in C^2[0,1]\) by zero outside \([0,1]\), assume \(K(0)=K'(0)=K(1)=K'(1)=0\), and \(\int_0^1K>0\). Use

$$
c=(1,1/2,1/4),\qquad \lambda=(1/3,-2,8/3).
$$

For a forward stage,

$$
w^+_{j,t}(u)=\frac{K((u_t-u)/(c_jb))/c_j}{\sum_sK((u_s-u)/(c_jb))/c_j};
$$

the backward weights replace \(u_t-u\) by \(u-u_t\). A direction is used only where its full window lies in \([0,1]\).

**(A7) Bandwidth.** \(b\to0\), \(nb/\log n\to\infty\), \(nb^3\to\infty\), and \(b\ge n^{-B}\) for some fixed \(B\). For localisation of the population expansion assume \(n^{-a}=O(b)\). In the (A5-0) branch, \(n^{-a}/b\to0\) is an explicit theorem hypothesis; it keeps the population stage speeds uniformly bounded and makes the displayed derivative rate consistent. Under (A5-1), only \(n^{-a}\to0\) is required for this purpose.

## 3. Weights and boundary construction

### Lemma 3.1 — weight bounds

Uniformly over every valid forward or backward stage,

$$
\sum_tw_{j,t}=1,\quad w_{j,t}\ge0,\quad
\max_tw_{j,t}\le\frac C{nb},\quad
\sum_tw_{j,t}^2\le\frac C{nb},
$$

$$
\max_t|w'_{j,t}|\le\frac C{nb^2},\quad
\sum_t|w'_{j,t}|\le\frac Cb,\quad
\sum_t|w'_{j,t}|^2\le\frac C{nb^3},\quad
\sum_tw'_{j,t}=0.
$$

For \(k=1,2,3\),

$$
b^{-k}\sum_tw^+_{j,t}(u)(u_t-u)^k=c_j^k\mu_k+O((nb)^{-1}),
$$

uniformly, with sign \((-1)^k\) for backward weights, where \(\mu_k=\int v^kK(v)dv/\int K(v)dv\). Their \(u\)-derivative defects are \(O((nb^2)^{-1})\).

*Proof.* The denominators are Riemann sums for \(nb\int K\), bounded above and below because the whole window is inside the design interval. Differentiate the quotient. The endpoint conditions make the zero extension \(C^1\), so there are no entry/exit jumps. The moment statements follow from

$$
\left|\frac1n\sum_tf(t/n)-\int f\right|\le \frac{\operatorname{TV}(f)}n
$$

applied to the scaled \(C^1\) functions. Differentiation adds one \(b^{-1}\). No constant depends on \(p_n\). \(\square\)

### Fixed-width blend

For \(b<1/3\), compute the forward three-scale estimator on \([0,2/3]\) and the backward estimator on \([1/3,1]\). Choose fixed \(C^2\) \(\chi\), zero on \((-\infty,1/3]\), one on \([2/3,\infty)\), with \(\|\chi'\|_\infty=O(1)\). On the overlap set

$$
\hat\mu^{(3)}(u)=\operatorname{Exp}_{\hat\mu_F^{(3)}(u)}
\left[\chi(u)\operatorname{Log}_{\hat\mu_F^{(3)}(u)}\hat\mu_B^{(3)}(u)\right].
$$

This, rather than a width-\(b\) transition, is consumed by G1′.

## 4. Dimension-free Hilbert concentration

### Lemma 4.1 — finite-memory weighted Hilbert inequality

Let \(\xi_t\) be centred, \(m\)-dependent random variables in any real Hilbert space, with \(\|\xi_t\|\le B\) almost surely. For deterministic \(a_t\),

$$
\mathbb E\left\|\sum_ta_t\xi_t\right\|^2
\le (2m+1)B^2\sum_ta_t^2. \tag{4.1}
$$

For \(0<\delta<1\), with probability at least \(1-\delta\),

$$
\left\|\sum_ta_t\xi_t\right\|
\le C_mB\|a\|_2\sqrt{1+\log((m+1)/\delta)}. \tag{4.2}
$$

*Proof.* Expand the squared norm. Only pairs \(|s-t|\le m\) remain; use \(2|a_sa_t|\le a_s^2+a_t^2\), proving (4.1). For (4.2), split indices into \(m+1\) residue classes; each class is independent. For one class let \(F=\|\sum a_t\xi_t\|\). Replacing one variable changes \(F\) by at most \(2B|a_t|\). Reveal variables sequentially. The scalar Hoeffding lemma applied to the Doob differences gives

$$
\Pr\{F-\mathbb EF>x\}\le
\exp\{-x^2/(2B^2\sum a_t^2)\}.
$$

Here the Hoeffding lemma follows directly by bounding the exponential of a centred variable on an interval by the chord joining its endpoint values. Also \(\mathbb EF\le(\mathbb EF^2)^{1/2}\le B(\sum a_t^2)^{1/2}\). Union bound the residue classes, then use the triangle inequality and Cauchy--Schwarz. \(\square\)

### Lemma 4.2 — uniform continuous-\(u\) score

Let \(z_j(u)\) be a deterministic stage population barycentre and parallel-trivialise \(T_{z_j(u)}M_n\) along \(z_j\). Then

$$
Z_j(u):=\sum_tw_{j,t}(u)
\left(\operatorname{Log}_{z_j(u)}X_{t,n}
-\mathbb E\operatorname{Log}_{z_j(u)}X_{t,n}\right)
$$

satisfies

$$
\sup_u\|Z_j(u)\|
=O_p\left(\sqrt{\frac{\log n}{nb}}\right), \tag{4.3}
$$

uniformly in \(j,n,p_n\), and

$$
\int_0^1\mathbb E\|Z_j(u)\|^2du\le \frac C{nb}. \tag{4.4}
$$

Replacing \(w\) by \(w'\) gives

$$
\int_0^1\mathbb E\left\|\sum_tw'_{j,t}(u)\xi_{t,j}(u)\right\|^2du
\le\frac C{nb^3}. \tag{4.5}
$$

*Proof.* At fixed \(u\), bounded total energy bounds the centred log vector in norm, so Lemmas 3.1 and 4.1 apply. The population Karcher equation and \(H\succeq I\) give \(\|z_j'\|\le C\). In the parallel frame along \(z_j\), the score has deterministic modulus \(C|u-v|/b\). Take a grid of mesh

$$
\delta_n=b\sqrt{\frac{\log n}{nb}}/C.
$$

Its logarithmic cardinality is \(O(\log n)\) by (A7). Apply (4.2) at grid points and interpolate. Equations (4.4)--(4.5) follow directly from (4.1), Fubini, and the two weight-square bounds. No sphere or spatial net is used. \(\square\)

## 5. Population expansion and Richardson differentiation

Let \(z_{j,\pm}(u)\) be the actual-law population barycentres and
\(x_{j,\pm}(u)=\operatorname{Log}_{\mu_n(u)}z_{j,\pm}(u)\).

### Lemma 5.1 — \(C^1\) stage expansion

Under (A1), (A4), (A5-0), and (A6), uniformly \(C^1\) vector fields \(A_1,A_2\), independent of \(j\), satisfy

$$
x_{j,\pm}=\pm c_jbA_1+c_j^2b^2A_2+r_{j,\pm}, \tag{5.1}
$$

$$
\|r_{j,\pm}\|_\infty\le C(b^3+n^{-a}+n^{-1}), \tag{5.2}
$$

$$
\|\nabla_ur_{j,\pm}\|_\infty
\le C\left(b^3+\frac{n^{-a}}b+\frac1{nb}\right). \tag{5.3}
$$

Under (A5-1), \(n^{-a}/b\) in (5.3) is replaced by \(n^{-a}\).

*Proof.* Write the population score in normal coordinates at \(\mu_n(u)\). Taylor-expand the proxy score in \(v-u\) through order two and its \(q\)-dependence through order two. Substitution in the Karcher equation gives

$$
x=bm_1A+b^2\{\tfrac12m_2B+m_1^2C\}+O(b^3).
$$

Thus for a scale family the whole second-order coefficient, including \(m_1^2C\), is \(c_j^2A_2\). The \(C^4\) domination in (A4) permits differentiation of the integral Taylor remainder and leaves it \(O(b^3)\), because displacement relative to moving \(\mu_n\), and its covariant derivative, are both \(O(b)\). Lemma 3.1 supplies the design terms. The coupling score defect is \(O(n^{-a})\); differentiating under (A5-0) creates \(\sum_tw'_{j,t}O(n^{-a})=O(n^{-a}/b)\), while (A5-1) bounds it directly by \(O(n^{-a})\). Finally \(H\succeq I\) converts score residuals to barycentre residuals. \(\square\)

### Lemma 5.2 — base-change expansion

If \(q_j=\operatorname{Exp}_m x_j\), \(\max_j\|x_j\|\le r\), and \(\sum_j\lambda_j=1\), then

$$
\operatorname{Log}_m\mathcal R_n(q_1,q_2,q_3)
=\sum_j\lambda_jx_j+\mathcal C_n(x_1,x_2,x_3), \tag{5.4}
$$

where

$$
\|\mathcal C_n\|\le Cr^3,\qquad
\|\nabla_u\mathcal C_n\|
\le Cr^2\left(\max_j\|\nabla_ux_j\|+r\|\mu_n'\|\right). \tag{5.5}
$$

*Proof.* In normal coordinates at \(m\), the first differential of the Exp/Log composition is the affine combination. The second differential at the diagonal vanishes because the connection is torsion free and Christoffel symbols vanish at the origin; curvature first enters in cubic order. Taylor's formula with integral remainder and (A1)(3) gives the first bound. Differentiate the remainder for the second. \(\square\)

Since \(\sum_j\lambda_j=1\), \(\sum_j\lambda_jc_j=0\), and \(\sum_j\lambda_jc_j^2=0\), Lemmas 5.1--5.2 give

$$
\|\operatorname{Log}_{\mu_n}\mu^{(3)}_{\pm,\mathrm{pop}}\|_\infty
\le C(b^3+n^{-a}+n^{-1}), \tag{5.6}
$$

$$
\|\nabla_u\operatorname{Log}_{\mu_n}\mu^{(3)}_{\pm,\mathrm{pop}}\|_\infty
\le C\left(b^3+\frac{n^{-a}}b+\frac1{nb}\right). \tag{5.7}
$$

Under (A5-1), the local-stationarity term in (5.7) is \(n^{-a}\). The fixed-width blend preserves both orders because \(\|\chi'\|_\infty=O(1)\) and its forward/backward discrepancy has level order (5.6).

## 6. Growing-\(p_n\) level theorems

### Theorem G1-HD-PW — uniform level rate

Under (A1)--(A7), for arbitrary \(p_n\),

$$
\boxed{\sup_{u\in[0,1]}d_n(\hat\mu_n^{(3)}(u),\mu_n(u))
=O_p\left(b^3+n^{-a}+n^{-1}+\sqrt{\frac{\log n}{nb}}\right).} \tag{6.1}
$$

*Proof.* Each stage uses probability weights. Empirical Sturm bounds \(d(\hat z_j,z_j)\) by the centred-score norm at deterministic \(z_j\). Lemma 4.2 gives the stochastic rate. The Richardson map is uniformly Lipschitz, so the stage errors cost only a fixed constant. Add (5.6), then apply the fixed-width blend. Each positive barycentre lies in the closed convex hull of observations within \(R+Cb\) of \(\mu_n(u)\); Richardson and blend paths have fixed-multiple-\(R\) length and remain in the assumed tube. Dimension never enters. \(\square\)

### Theorem G1-HD-\(L^2\) — integrated level rate

$$
\boxed{\left\|\operatorname{Log}_{\mu_n}\hat\mu_n^{(3)}\right\|_{L^2}
=O_p\left(b^3+(nb)^{-1/2}+n^{-a}+n^{-1}\right).} \tag{6.2}
$$

*Proof.* Use (4.4), empirical Sturm, Fubini and Markov for each stage; then the Lipschitz Richardson/blend maps and (5.6). There is no entropy step or coordinate sum. \(\square\)

If total radius is \(R_n\), stochastic terms are multiplied by \(R_n\), and geometry must be controlled on a radius-\(R_n\) tube. If \(R_n^2\asymp p_n\), the explicit \(\sqrt{p_n}\) loss returns.

### Corollary 6.3 — design-grid RMS

For \(e_{t,n}=\operatorname{Log}_{\mu_n(u_t)}\hat\mu_n^{(3)}(u_t)\),

$$
\boxed{
\left(\frac1n\sum_{t=1}^n\|e_{t,n}\|^2\right)^{1/2}
=O_p\left(b^3+(nb)^{-1/2}+n^{-a}+n^{-1}\right).} \tag{6.3}
$$

The same conclusion holds when the average is taken over any deterministic subset of design points, or over any deterministic evaluation grid \(v_{1,n},\ldots,v_{M_n,n}\subset[0,1]\) (the \(v_{j,n}\) need not equal observation times), with \(M_n^{-1}\) as normalisation.

*Proof.* At every deterministic \(u\in[0,1]\), including every \(u_t\) and every off-design \(v_{j,n}\), (4.1), Sturm, and the uniform weight-square bound give

$$
\mathbb E\,d(\hat z_j(u_t),z_j(u_t))^2\le C/(nb)
$$

for each stage, uniformly in \(u,n,p_n\). The bounded differential of the Richardson and blend maps transfers this pointwise second moment to the final estimator. Add the squared deterministic bias from (5.6), average over the chosen deterministic evaluation grid, and apply Markov. No independence across evaluation points, and no lower bound on their number beyond non-emptiness, is used. \(\square\)

## 7. Random-point implicit differentiation without an operator net

### Lemma 7.1 — derivative stability

For a positive stage let \(z,\hat z\) be population and empirical barycentres. Put

$$
\bar H(q)=\sum_tw_t\mathbb EH(q,X_t),\quad
\hat H(q)=\sum_tw_tH(q,X_t),
$$

$$
\bar D(q)=\sum_tw_t'\mathbb E\operatorname{Log}_qX_t,\quad
\hat D(q)=\sum_tw_t'\operatorname{Log}_qX_t.
$$

After parallel identification,

$$
\|\hat z'-z'\|\le C\left[
\|\hat D(z)-\bar D(z)\|
+\|\{\hat H(z)-\bar H(z)\}z'\|
+\frac{d(\hat z,z)}b+d(\hat z,z)(1+\|z'\|)
\right]. \tag{7.1}
$$

*Proof.* Differentiate the two Karcher equations:

$$
\hat H(\hat z)\hat z'=\hat D(\hat z),\qquad
\bar H(z)z'=\bar D(z).
$$

Positive weighted Hessians are at least \(I\), so \(\|\hat H(\hat z)^{-1}\|\le1\), without operator concentration. Transport and subtract. The \(D\)-change is at most \(C(\sum|w_t'|)d\le Cd/b\); the Hessian change is \(CL_*d\). Differentiating the short connector first gives \(Cd(1+\|z'\|+\|\hat z'-z'\|)\). On the uniform stage event \(d(\hat z,z)\le(2C)^{-1}\), supplied by Lemma 4.2 and Sturm, the last term is absorbed into the left side, proving (7.1). Outside that event, the deterministic weight bounds and \(H\succeq I\) give \(\|\hat z'\|+\|z'\|\le C/b\). Lemma 4.2 can be run with failure \(n^{-D}\) for arbitrary fixed \(D\); choose \(D>2B+3\) in (A7), so the exceptional contribution is negligible in every integrated second moment used below. \(\square\)

The Hessian term is only an action on fixed \(z'(u)\):

$$
\{\hat H(z)-\bar H(z)\}z'
=\sum_tw_t\{H(z,X_t)z'-\mathbb EH(z,X_t)z'\}.
$$

It is a bounded centred Hilbert sum, so Lemma 4.1 controls it dimension-free. Combining (4.4), (4.5), and (7.1),

$$
\int_0^1\mathbb E\|\hat z'-z'\|^2du\le \frac C{nb^3}. \tag{7.2}
$$

### Theorem G1′-HD-\(L^2\) — corrected derivative rate

Under (A1)--(A7),

$$
\boxed{\left\|\nabla_u\operatorname{Log}_{\mu_n}\hat\mu_n^{(3)}\right\|_{L^2}
=O_p\left(b^3+(nb^3)^{-1/2}+\frac{n^{-a}}b+\frac1{nb}\right).} \tag{7.3}
$$

Under (A5-1),

$$
\boxed{\left\|\nabla_u\operatorname{Log}_{\mu_n}\hat\mu_n^{(3)}\right\|_{L^2}
=O_p\left(b^3+(nb^3)^{-1/2}+n^{-a}+\frac1{nb}\right).} \tag{7.4}
$$

*Proof.* Equation (7.2) gives each stage's stochastic derivative error. Differentiate \(\mathcal R_n\); its first and second differentials are bounded by (A1). Lemma 5.2, which uses the bounded third differential and its covariant derivative, makes the **population** cubic base-change derivative \(O(b^3+n^{-a}/b)\), because relative population stage displacements and their derivatives are \(O(b)\) for the proxy law. Empirical-minus-population differentiation is handled by the ordinary first/second-differential stability bound, using stage \(L^2\) derivative error (7.2) and uniform level error (4.3); it does not apply the cubic expansion at empirical arguments and therefore does not require the empirical stage error to be \(o_p(b)\). In particular, \(nb^3/\log n\to\infty\) is unnecessary; \(nb^3\to\infty\) and \(nb/\log n\to\infty\) suffice.

Combine (5.7) and (7.2). The fixed-width blend adds \(\chi'\operatorname{Log}_{\hat\mu_F^{(3)}}\hat\mu_B^{(3)}\), whose \(L^2\) size is only the level rate. For the final Log comparison set

$$
\ell_{\infty,n}:=b^3+n^{-a}+n^{-1}+\sqrt{\frac{\log n}{nb}},
\qquad
d_n:=b^3+(nb^3)^{-1/2}+\frac{n^{-a}}b+\frac1{nb}.
$$

The deviation of \(D\operatorname{Log}\) from \((-I,I)\) is \(O(\ell_{\infty,n}^2)\), while the absolute velocity has \(L^2\) norm \(O_p(1+d_n)\). Thus the omitted term is

$$
O_p\{\ell_{\infty,n}^2(1+d_n)\}.
$$

Under (A7), \(d_n=o(1)\) and

$$
\frac{b^6}{b^3}\to0,\qquad
\frac{n^{-2a}}{n^{-a}/b}=bn^{-a}\to0,\qquad
\frac{\log n/(nb)}{(nb^3)^{-1/2}}
=\frac{\sqrt b\,\log n}{\sqrt n}\to0,
$$

and the \(n^{-2}\) term is smaller than \((nb)^{-1}\); every cross-product is bounded by the corresponding sum of squares. Hence \(\ell_{\infty,n}^2(1+d_n)=o(d_n)\), which closes (7.3) quantitatively. Under (A5-1), replace \(n^{-a}/b\) by \(n^{-a}\); then \(n^{-2a}/n^{-a}=n^{-a}\to0\), and the same proof gives (7.4). \(\square\)

## 8. Counterexamples and failed implications

### CE-A1 — \(n^{-a}/b\) is sharp

Take \(M_n=\mathbb R\), \(X_t^{(u,n)}\equiv0\), and \(\mu_n\equiv0\). Fix interior \(u_*\). The three-scale estimator is linear:

$$
\hat\mu^{(3)}(u)=\sum_tW_t(u)X_{t,n},\qquad
W_t=\sum_j\lambda_jw_{j,t}.
$$

Set \(X_{t,n}=n^{-a}\operatorname{sign}W_t'(u_*)\). The row is deterministic, hence finite-memory, and its level local-stationarity error is exactly \(n^{-a}\). But

$$
|\partial_u\hat\mu^{(3)}(u_*)|
=n^{-a}\sum_t|W_t'(u_*)|.
$$

The continuous equivalent kernel \(L=\sum_j\lambda_jc_j^{-1}K(\cdot/c_j)/\int K\) is compactly supported and has integral one, so it is not constant and \(\int|L'|>0\). Riemann-sum convergence gives

$$
\sum_t|W_t'(u_*)|\sim b^{-1}\int|L'(v)|dv.
$$

Thus the derivative error is at least \(cn^{-a}/b\). The hostile-audit version \(X_{t,n}=n^{-a}\operatorname{sign}K'((u_t-u_*)/b)e_1\) is the same construction for one stage; choosing the sign of the combined \(W'\) proves sharpness for the complete Richardson estimator.

### CE-A2 — width-\(b\) blending loses half an order

In \(\mathbb R\), let already corrected curves be \(F=\mu+b^3\) and \(B=\mu-b^3\). If \(\chi\) changes across an interval of length \(Cb\), the blend is \(G=\mu+b^3(1-2\chi)\), so

$$
\|G'-\mu'\|_{L^2}\asymp b^3b^{-1}b^{1/2}=b^{5/2},
$$

not \(b^3\). This disproves the current width-\(b\) claim and motivates the fixed-width blend.

### CE-A3 — coordinatewise boundedness is not bounded total energy

Let \(N=nb\) and \(\xi_1,\ldots,\xi_N\in\mathbb R^{p_n}\) have independent Rademacher coordinates. Every coordinate is bounded by one, but \(\|\xi_i\|=\sqrt{p_n}\), and

$$
\mathbb E\left\|N^{-1}\sum_i\xi_i\right\|^2=\frac{p_n}{N}.
$$

Moreover the fourth moment is at most three times the square of this expectation, so Paley--Zygmund gives probability at least \(1/12\) that the norm is at least \(\sqrt{p_n/(2N)}\). A dimension-free \(N^{-1/2}\) norm rate is therefore false under coordinatewise bounded energy.

## 9. Admissible regimes and downstream ribbon use

For consistency under (A5-0), it suffices that

$$
b\to0,\qquad \frac{nb}{\log n}\to\infty,\qquad
nb^3\to\infty,\qquad \frac{n^{-a}}b\to0.
$$

There is no condition on \(p_n\). At \(b=n^{-1/5}\), derivative consistency needs \(a>1/5\). The level stochastic orders are \(n^{-2/5}\sqrt{\log n}\) uniformly and \(n^{-2/5}\) in \(L^2\); the derivative stochastic order is \(n^{-1/5}\); and the local-stationarity derivative term is \(n^{-a+1/5}\).

The ribbon product consumed downstream obeys

$$
\|e_n\|_{L^2}\|\nabla e_n\|_{L^2}
=O_p\left[
\{b^3+(nb)^{-1/2}+n^{-a}\}
\{b^3+(nb^3)^{-1/2}+n^{-a}/b\}
\right]. \tag{9.1}
$$

At \(b=n^{-1/5}\), the pure local-stationarity product is \(n^{-2a+1/5}=o(n^{-1/2})\) if \(a>7/20\); cross-products require \(a>3/10\). If the final loading theorem already needs deterministic rotation \(n^{-a}=o(n^{-1/2})\), then \(a>1/2\) dominates these restrictions. Under (A5-1), replace \(n^{-a}/b\) by \(n^{-a}\).

## 10. Audit of the polygonal-frame derivative bypass

A coarse-grid positive three-scale mean followed by geodesic polygonal interpolation can bypass G1′ for a **consistency-level** frame theorem, but the proposed deterministic holonomy estimate does not by itself recover the oracle \(n^{-1/2}\) loading rate.

Suppose \(m+1\) grid vertices satisfy the uniform nodal event

$$
\max_{0\le k\le m}d(\hat\mu(k/m),\mu(k/m))\le\ell_n,
$$

and \(\mu\) has uniformly bounded covariant acceleration. Chordal interpolation of the true vertices is \(O(m^{-2})\) from \(\mu\). Hence the entire polygonal ribbon stays in the geometry tube if

$$
\ell_n+m^{-2}<R_*/4. \tag{10.1}
$$

An \(L^2\) or RMS nodal statement is insufficient for (10.1): one bad vertex can leave the tube. The required input is uniform G1, so here one may take

$$
\ell_n=b^3+n^{-a}+\sqrt{\frac{\log n}{nb}}
$$

up to the \(n^{-1}\) design term. If a cellwise quadrilateral-holonomy proof yields

$$
\|\hat P-P\|_{\mathrm{op}}
\le C\Lambda\{L\ell_n+m\ell_n^2+m^{-2}\}, \tag{10.2}
$$

then choosing \(m\asymp\ell_n^{-2/3}\) gives

$$
\|\hat P-P\|_{\mathrm{op}}
\le C\Lambda\{L\ell_n+\ell_n^{4/3}\}. \tag{10.3}
$$

This proves frame consistency whenever \(\ell_n\to0\), without differentiating the estimated mean. It does not prove oracle-rate loading recovery: the leading deterministic bound \(L\ell_n\) is much larger than \(n^{-1/2}\) at any local-mean bandwidth. To replace G1′ in the final oracle theorem one still needs a proved cross-fitted averaging/cancellation result that turns the stochastic part of the first term in (10.2) into \(n^{-1/2}\), while retaining (10.1). Therefore the bypass is **CONDITIONAL for consistency, not yet a proved oracle-rate substitute**. It needs: a proof of (10.2) with correctly typed connectors, the uniform nodal G1 event, \(m\ell_n^2\to0\), \(m^{-2}\to0\), and the tube margin (10.1).

## 11. Dependency closure ledger

The final mean statements (6.1), (6.2), (7.3), and (7.4) consume only:

1. Lemma 3.1 (proved);
2. Lemmas 4.1--4.2 (proved internally and dimension-free);
3. empirical Sturm for positive weights (proved/cited in the canonical audit, with hypotheses verified here);
4. Lemmas 5.1--5.2 under the explicit uniform \(C^1\)-Taylor and tube assumptions;
5. Lemma 7.1 (proved; only Hessian actions are concentrated);
6. the fixed-width blend (defined and rate-checked).

No unresolved signed-Hessian lemma, sphere-net inequality, polynomial-mixing extension, factor theorem, or Paper 2 result is consumed. Optional questions that block none of these statements are replacement of finite memory by a broader Hilbert physical-dependence class and weakening the abstract tube constants outside affine-invariant SPD.

## 12. Cross-audit of HD1-B

Workstream B's signal/eigengap algebra, Hilbert--Schmidt oracle concentration, row-operator assembly, beyond-rank square, and corrected threshold/ridge selectors survive audit. The following corrections are required where B consumes the mean theorem.

### B-AUDIT-1 — the perforated design changes high-order mean bias

Alternating training blocks of length \(\ell_n\) with deleted cores do preserve \(\max|w|=O((nb)^{-1})\) and \(\sum w^2=O((nb)^{-1})\) when \(g_n=o(\ell_n)=o(nb)\). That condition alone does **not** preserve the exact rates stated in B. The cumulative discrepancy of the periodic training mask over a kernel window is \(O(\ell_n)\). Repeating Lemma 3.1 on the masked design gives normalised moment defects

$$
O\left(\frac{\ell_n}{nb}\right),
$$

so the uncancelled first-order population bias is \(O(\ell_n/n)\), and its derivative is \(O(\ell_n/(nb))\). The correct perforated-design inputs are therefore

$$
r_{0,n}^{\rm CF}
=b^3+\sqrt{\frac{m_n+1}{nb}}+n^{-a}+\frac{\ell_n}{n}, \tag{12.1}
$$

$$
r_{1,n}^{\rm CF}
=b^3+\sqrt{\frac{m_n+1}{nb^3}}+\frac{n^{-a}}b+\frac{\ell_n}{nb}, \tag{12.2}
$$

up to fixed constants and the \(n^{-1}\) ordinary-grid term. Here the memory factors appear because Workstream A's displayed theorem fixed \(m\), whereas B allows \(m_n\) to grow. B may retain its simpler \(r_0,r_1\) only by imposing \(m_n=O(1)\) and

$$
\ell_n/n=O(r_{0,n}),\qquad \ell_n/(nb)=O(r_{1,n}). \tag{12.3}
$$

At \(b=n^{-1/5}\) with fixed memory, \(\ell_n=O(n^{3/5})\) suffices for both and is compatible with \(g_n=o(\ell_n)=o(n^{4/5})\).

### B-AUDIT-2 — Route S's consistency exponent

B states that \(b=n^{-1/5}\) is admissible for consistency when \(a>1/10\), based only on the product \(r_0r_1\). The proved (A5-0) derivative theorem itself assumes \(n^{-a}/b\to0\), hence \(a>1/5\), to keep population stage speeds bounded. Route S can claim \(a>1/10\) only after a separate product theorem which permits a diverging derivative norm; it cannot consume Theorem (7.3) for that range. With the present input, Route S requires \(a>1/5\). Route R does not consume this restriction.

### B-AUDIT-3 — bounded observation energy does not bound factor energy

The compatibility display \(\Delta_n\le H_n^0R^4/r_n\) is valid if \(\|f_{t,n}\|\le R_f\) uniformly (with \(R_f\) in place of \(R\)), or under a separate total factor-energy moment bound. It does not follow from \(\|Y_{t,n}\|\le R\): \(Af_t\) and \(\varepsilon_t\) can cancel contemporaneously. This affects scope discussion, not B's operator theorem.

### B-AUDIT-4 — exact status of derivative-free Route R

Lemma B6′ correctly converts a proved feasible-observation RMS rate \(q_n\) into a lag-row bound without GLO, cross-fitted cancellation, or G1′. Corollary 6.3 supplies the recentering RMS on every deterministic evaluation subset and coarse grid. The log Taylor bound gives

$$
\left(\frac1N\sum_t
\|\Phi_{e_t}^{-1}\log_{\hat\mu(u_t)}X_t-\log_{\mu(u_t)}X_t\|^2
\right)^{1/2}
=O_p(r_{0,n}^{\rm CF})
$$

on the tube event, without differentiating \(\hat\mu\).

The frame part of \(q_n\) still needs a discrete polygonal-frame theorem. Grid RMS alone cannot guarantee its tube: one must also consume uniform nodal G1, namely \(\max_k\|e(k/m)\|=o_p(1)\). Once a correctly typed cellwise holonomy theorem bounds polygonal frame RMS using only deterministic vertex errors and this tube event, Route R can consume Corollary 6.3 without any continuous derivative lemma. Until that discrete theorem is supplied, B's sentence “if a derivative-free polygonal-frame theorem proves \(q_n=O_p(\ell_n)\)” is correctly conditional and must not be promoted to a proved final theorem.

### B-AUDIT-5 — cross-fitting and tube events

Deleting \(g_n=m_n+H_n^0\) indices from both sides of each core genuinely separates the causal innovation sets, so B's conditional independence claim is correct. Only one evaluation colour may be used unless the two trained frames are explicitly aligned. For every route, the uniform tube event is still a sup-norm input; the RMS theorem alone is insufficient. Under (12.1)--(12.3), the positive three-scale mean proof extends to the deterministic perforated design by the same Hilbert argument, with mask discrepancy carried explicitly.
