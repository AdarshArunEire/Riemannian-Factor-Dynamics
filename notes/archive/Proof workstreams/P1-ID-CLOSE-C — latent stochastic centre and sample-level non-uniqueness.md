---
type: working-proof-dossier
title: P1-ID-CLOSE-C — latent stochastic centre and sample-level non-uniqueness
status: wave-1-terminal
workstream: C (hostile counterexamples and probability)
owns: ID-9 route R3, ID-9 route R5
last-audited: 2026-08-12
verdict: the ID-1 gate is TRUE BUT NON-BINDING on the latent-centre class; ID-2(1)–(3) are FALSE on that class; R5 separates on the strongly-convex class and is an identification node off it
---

# P1-ID-CLOSE-C — latent stochastic centre and sample-level non-uniqueness

> **Scope.** This dossier owns ID-9 routes **R3** (latent stochastic centre) and **R5** (sample-level non-uniqueness). It is a proof record, not a status authority; the lead ledger [[P1-ID-CLOSE — lead ledger]] merges. Every node introduced below carries a terminal status. Numerics were used only to sanity-check signs and constants and assign no status; every displayed claim has an exact analytic proof.

## 0. Verdict summary

**R3 verdict.** The ID-1 gate does **not** contain a false theorem. It contains a **true-but-non-binding** theorem whose scope condition is a modelling convention, and the convention is exactly what the scientific question was asking about. Precisely:

- **ID-1 is true and vacuous on the latent class.** Every functional of a law is a deterministic quantity (L-9.R3.0). A latent stochastic centre \(C_t\) is not deterministic. Therefore *no* information set in the campaign vocabulary — \(\mathcal I_M,\mathcal I_J,\mathcal I_1,\mathcal I_F(c_0),\mathcal I_R\) — can identify a realised centre path, and ID-1's hypothesis ("every admissible representation *whose centre must be the unique Fréchet mean*") quantifies over a class that a latent-centre model never joins.
- **What ID-1 actually pins in the flat case is \(\mathbb E C_u\)**, not \(C_u\) (L-9.R3.1).
- **In curvature ID-1 does not even pin the natural analogue of \(\mathbb E C_u\).** The marginal Fréchet mean of a latent-centre mixture differs from the Fréchet mean of the mixing-centre law, exactly and globally, on \(H^2\) (L-9.R3.2). The effect is curvature-induced: it is identically zero in a flat space.
- **The damage is not confined to ID-1.** Over the latent-centre class, ID-2(1)–(3) are **FALSE**: when the observed spectral density is uniformly positive definite, *every* subspace of *every* dimension \(r\le p\) is an admissible loading range (L-9.R3.3d). The latent centre defeats \(\mathcal I_J\), not merely \(\mathcal I_M\), because a serially dependent centre absorbs nonzero-lag covariance — precisely the energy ID-2 uses to pin \(\mathcal S_X\).
- **What survives** is exactly the total covariance sequence \(\Gamma_X(h)=\Gamma_C(h)+A\Gamma_f(h)A^*\) and its span \(\mathcal S_X\), read as the dynamic span of the *sum* \(C+Af\), with no split (L-9.R3.4).
- **What restores identification** is a *declared* frequency set on which the centre contributes nothing, plus band-contrast completeness; this is necessary as well as sufficient on the uniformly-pd class (L-9.R3.5). It is a convention, not a testable restriction.

**R5 verdict.** R5 **splits**, and both halves terminate.

- On the class the project actually declares for the mean estimator — Hadamard manifolds (HD-G), or any declared compact strongly geodesically convex regular domain with a positive Hessian margin — R5 is **OUT OF SCOPE BY PROVED SEPARATION**: the empirical Fréchet objective is strongly geodesically convex *for every realisation*, so the empirical argmin is a singleton with probability one, not \(1-o(1)\); the localisation/fallback never selects a branch; and no consumer of ID-1–ID-6 reads the estimator's localisation convention (L-9.R5.1, L-9.R5.5), subject to one displayed scope lock.
- Off that class — the parent's sphere products, and the Bures–Wasserstein cone, which is nonnegatively curved and **not** Hadamard — R5 is an **identification node**: the data-dependent localisation is a randomised selector, and on a degenerating-margin array the empirical mean sits a fixed positive distance from the population mean with probability tending to \(1/2\) although the population argmin is a singleton at every \(n\) (L-9.R5.3, L-9.R5.4).

---

# PART I — R3: the latent stochastic centre

## 1. The latent-centre class LC

Fix a complete Riemannian manifold \(M\) and a reference \(c_0\).

> **Definition LC.** A *latent-centre representation* of an \(M\)-valued process \((X_t)_{t\in\mathbb Z}\) is a tuple \((C,A,f,\delta)\) with:
>
> - **(LC1)** \(C=(C_t)\) an \(M\)-valued process with \(\mathbb E\,d(c_0,C_t)^2<\infty\), adapted to a filtration to which \(X\) is adapted;
> - **(LC2)** \(A:\mathbb R^r\to T_{c_0}M\) linear with \(A^*A=I_r\), \(r<\infty\) fixed; \(\mathcal P_t\) the parallel transport from \(T_{c_0}M\) to \(T_{C_t}M\) along the declared centre path (chords for discrete time);
> - **(LC3)** \(X_t=\operatorname{Exp}_{C_t}\!\big[\mathcal P_t(Af_t+\delta_t)\big]\), with all \(\operatorname{Exp}\) and \(\log\) single-valued on the almost-sure support;
> - **(LC4)** \(f\) stationary, \(\mathbb E[f_t\mid C]=0\) for every \(t\), \(\mathbb E\|f_t\|^2<\infty\);
> - **(LC5)** \(\delta\) temporally white, \(\mathbb E[\delta_t\mid C,f]=0\), and both factor–noise cross-lag covariances vanish at every lag.
>
> \(\mathrm{LC}^{\circ}\) denotes the flat/Hilbert instantiation \(M=H\) a real separable Hilbert space, \(\mathcal P_t=\mathrm{Id}\), \(X_t=C_t+Af_t+\delta_t\), with \(C\) and \((f,\delta)\) jointly stationary and \(\Gamma_{Cf}(h)=\Gamma_{fC}(h)=0\) for every \(h\).
>
> \(\mathrm{D}\subset\mathrm{LC}\) denotes the **deterministic-centre subclass** used by Paper 1: \(C_t=\mu_n(u_t)\) with \(\mu_n:[0,1]\to M\) a deterministic function of rescaled time, and (Paper 1 §"Model and estimator", HD1 (HD-M)) \(\mu_n(u)\) equal to the Fréchet mean of the frozen marginal law at \(u\).

Every construction below is checked against LC1–LC5 explicitly.

## 2. Question (i) — when is the mixture mean the mean of the mixing centres?

### 2.1 L-9.R3.0 — the vacuity lemma (universal; this is the load-bearing observation)

> **Lemma L-9.R3.0.** Let \(\mathcal I\) be any of \(\mathcal I_M,\mathcal I_J,\mathcal I_1^{\text{(law level)}},\mathcal I_F(c_0),\mathcal I_R\), i.e. any information set whose elements are *laws* (or functionals of laws). Let \(T\) be any \(\mathcal I\)-measurable functional with values in \(M\). Then \(T\) is a constant, i.e. \(\sigma(T)=\{\emptyset,\Omega\}\) up to null sets. Consequently, if \(C_u\) is a random element of \(M\) with \(\mathbb P(C_u=x)<1\) for every \(x\in M\), then \(\mathbb P(T=C_u)<1\) for every such \(T\): **no law-level information set identifies a nondegenerate latent centre.**

*Proof.* A functional of the law of \(X\) is computed from \(\mathrm{Law}(X)\), which is a single fixed probability measure, not a random object; it is therefore measurable with respect to the trivial \(\sigma\)-field. If \(T\) were a.s. equal to \(C_u\), then \(C_u\) would be a.s. constant, contradicting the hypothesis. \(\square\)

**Status: PROVED.** **Classification: information-deficient (universal; not curvature-, cut-locus-, or completeness-specific).**

> **Strongest corrected theorem removing exactly this feature.** The feature is "the target is random while the information is a law". Removing it means restricting to \(\mathrm{D}\): if \(C_t=\mu(u_t)\) is deterministic, then \(C_t\) *is* a law-level object and ID-1 applies verbatim. No nontrivial correction exists on \(\mathrm{LC}\setminus\mathrm{D}\): by L-9.R3.0 the only identifiable centre-related objects are deterministic functionals of \(\mathrm{Law}(C)\) that are *also* functionals of \(\mathrm{Law}(X)\), and §5 shows that on \(\mathrm{LC}^\circ\) with uniformly positive-definite spectral density there are none beyond the trivial ones.

### 2.2 L-9.R3.1 — the flat/Hilbert case

> **Lemma L-9.R3.1.** Let \(H\) be a real separable Hilbert space. Let \(C\) be an \(H\)-valued random element with \(\mathbb E\|C\|^2<\infty\) and let \(\xi=\mathcal PAf+\delta\) satisfy \(\mathbb E\|\xi\|^2<\infty\) and \(\mathbb E[\xi\mid C]=0\) a.s. (Bochner conditional expectation). Put \(X=C+\xi\) and \(Q=\mathrm{Law}(X)\). Then:
>
> 1. \(F_Q(x)=\mathbb E\|X-x\|^2\) is finite, strictly convex and coercive on \(H\), so \(\mathfrak M(Q)\) is a singleton;
> 2. \(\mathfrak M(Q)=\{\mathbb EX\}=\{\mathbb EC\}\), a **deterministic** element of \(H\);
> 3. \(\mathbb P(\mathfrak M(Q)\ni C)=1\) if and only if \(C\) is a.s. constant, i.e. \(\mathbb E\|C-\mathbb EC\|^2=0\);
> 4. the same conclusion (2) holds under the strictly weaker hypothesis \(\mathbb E\xi=0\); the conditional hypothesis \(\mathbb E[\xi\mid C]=0\) is not needed in the flat case and is stated only because it is the hypothesis under which the *curved* analogue is falsified in §2.3.

*Proof.* (1) \(F_Q(x)=\mathbb E\|X\|^2-2\langle\mathbb EX,x\rangle+\|x\|^2\) with \(\mathbb E\|X\|^2\le2\mathbb E\|C\|^2+2\mathbb E\|\xi\|^2<\infty\) and \(\mathbb EX\) well defined by Cauchy–Schwarz. It is a quadratic with unit leading coefficient, hence \(1\)-strongly convex and coercive; the unique minimiser is \(\mathbb EX\). (2) \(\mathbb EX=\mathbb EC+\mathbb E\xi\) and \(\mathbb E\xi=\mathbb E\big[\mathbb E[\xi\mid C]\big]=0\); Bochner integrability of \(\xi\) follows from \(\mathbb E\|\xi\|^2<\infty\). (3) \(\mathbb P(C=\mathbb EC)=1\iff\mathbb E\|C-\mathbb EC\|^2=0\). (4) Immediate from the display in (2). \(\square\)

**Status: PROVED.** **Classification: information-deficient (universal).** Combined with L-9.R3.0: **ID-1 pins \(\mathbb EC_u\), never the realised centre path**, and in the flat case the object it pins is exactly the ensemble mean of the mixing centres.

**Complete audit of the counterexample content of L-9.R3.1(3).** Manifold and metric: \(H\) with its inner-product metric (flat, complete, Hadamard, empty cut locus, all Logs global and single-valued, \(\log_xy=y-x\)). Stochastic construction: \(C\) any nondegenerate \(L^2\) random element, \(\xi\) any \(L^2\) element with \(\mathbb E[\xi\mid C]=0\). Fréchet means: unique by (1), computed exactly in (2). Support/normal neighbourhood: global. Factor rank/loading/factor law/noise law: arbitrary admissible \((r,A,f,\delta)\) satisfying LC2, LC4, LC5. Temporal dependence/spectra: irrelevant at the marginal level; §5 supplies them. Observational object claimed equal: the marginal law \(Q\). Violated conclusion: "the model's centre is the marginal Fréchet mean". Responsible feature: the centre is random and the mean of a mixture is the mean of its mixing measure only in the ensemble sense.

### 2.3 L-9.R3.2 — the curved case: an exact global counterexample on \(H^2\)

Throughout this subsection \(M=H^2\), the hyperbolic plane of constant sectional curvature \(K=-1\), with its complete Riemannian metric.

#### 2.3.1 L-9.R3.2a — geometric preconditions (external, cited and applied)

> **(i)** \(H^2\) is a Hadamard manifold: complete, simply connected, \(K\le0\). By Cartan–Hadamard, \(\operatorname{Exp}_x:T_xM\to M\) is a diffeomorphism for every \(x\); hence the cut locus is empty, every geodesic is minimising and unique, and \(\log_x\) is globally defined, single-valued and smooth.
> **(ii)** For every \(z\), \(x\mapsto\tfrac12 d(x,z)^2\) is smooth and satisfies \(\operatorname{Hess}\tfrac12d(\cdot,z)^2\succeq\mathrm{Id}\), with eigenvalue \(1\) in the radial direction toward \(z\) and \(d\coth d\) in the transverse directions (\(d=d(\cdot,z)\)).
> **(iii)** Consequently \(F_Q(x)=\int d(x,z)^2Q(dz)\) is \(2\)-strongly geodesically convex and coercive for every \(Q\in\mathcal P_2(H^2)\); \(\mathfrak M(Q)\) is a singleton and is the unique solution of the first-order condition \(\int\log_xz\,Q(dz)=0\).
> **(iv)** (CN / Bruhat–Tits inequality) In a CAT(0) space, for \(m\) the midpoint of \(p,q\) and any \(x\): \(d(x,p)^2+d(x,q)^2\ge2d(x,m)^2+\tfrac12d(p,q)^2\).

**Status: CITED+APPLIED.** Sources: Cartan–Hadamard theorem; Hessian comparison for \(d^2/2\) under \(K\le0\); Sturm, *Probability measures on metric spaces of nonpositive curvature* (2003), Prop. 4.3 and Thm 4.9 for (iii); Bridson–Haefliger II.1A.6 / II.2 for (iv). Every use below cites the exact item.

#### 2.3.2 L-9.R3.2b — the equal-weight two-point Fréchet mean is the midpoint

> **Lemma.** In a Hadamard manifold (indeed any CAT(0) space), let \(p\neq q\), \(m\) their geodesic midpoint, and \(Q=\tfrac12\delta_p+\tfrac12\delta_q\). Then \(F_Q(x)\ge F_Q(m)+d(x,m)^2\) for every \(x\); hence \(\mathfrak M(Q)=\{m\}\).

*Proof.* \(F_Q(x)=\tfrac12 d(x,p)^2+\tfrac12 d(x,q)^2\). By L-9.R3.2a(iv), \(F_Q(x)\ge d(x,m)^2+\tfrac14d(p,q)^2\). With \(s:=d(m,p)=d(m,q)=\tfrac12d(p,q)\), \(F_Q(m)=s^2=\tfrac14d(p,q)^2\). \(\square\)

**Status: PROVED (from a cited inequality).** In particular the *conditional* law of \(X\) given \(C=c_2\) in the construction below has conditional Fréchet mean exactly \(c_2\), as required.

#### 2.3.3 The construction

Fix \(\beta>0\). Let \(\gamma\) be a unit-speed geodesic of \(H^2\), and set

\[
m_0=\gamma(0),\qquad c_1=\gamma(-\beta),\qquad c_2=\gamma(\beta),\qquad a:=d(c_1,c_2)=2\beta .
\]

So \(m_0\) is the midpoint of \([c_1,c_2]\). Let \(u\in T_{c_2}H^2\) be the unit vector **orthogonal** to \(\dot\gamma(\beta)\), and let \(\ell\) be the geodesic through \(c_2\) with tangent \(u\); thus \(\ell\perp\gamma\) at \(c_2\) and \(c_1\notin\ell\). For \(s>0\),

\[
p(s)=\operatorname{Exp}_{c_2}(su),\qquad q(s)=\operatorname{Exp}_{c_2}(-su).
\]

**Latent-centre model.** \(C\in\{c_1,c_2\}\) with \(\mathbb P(C=c_1)=\mathbb P(C=c_2)=\tfrac12\). Conditionally on \(C=c_1\), the tangent vector is \(0\), so \(X=c_1\). Conditionally on \(C=c_2\), the tangent vector is \(\pm su\) with probability \(\tfrac12\) each, so \(X\in\{p(s),q(s)\}\). Formally \(r=1\), \(A=u\) (isometric: \(A^*A=1\)), \(f=\varepsilon\mathbf 1\{C=c_2\}s\) with \(\varepsilon=\pm1\) symmetric and independent of \(C\), \(\delta\equiv0\).

**LC audit.** LC1: \(C\) takes two values, \(\mathbb Ed(c_0,C)^2<\infty\). LC2: \(A\) isometric, \(r=1\); \(\mathcal P\) transport along \([c_0,C]\), immaterial here. LC3: \(X=\operatorname{Exp}_C(\mathcal PAf)\) by construction, all Logs single-valued (L-9.R3.2a(i)). LC4: \(\mathbb E[f\mid C=c_1]=0\) and \(\mathbb E[f\mid C=c_2]=\tfrac12(s)+\tfrac12(-s)=0\) — **the conditional centring hypothesis of L-9.R3.1 holds exactly.** LC5: \(\delta\equiv0\), vacuously white with zero cross-lags. Support: \(\{c_1,p(s),q(s)\}\), a finite set in a Hadamard manifold; no normal-neighbourhood restriction is needed anywhere. Temporal structure: extend to a process by taking \((C_t,\varepsilon_t)\) i.i.d.; then \(X\) is i.i.d. with marginal \(Q_s\) below, and all statements are marginal.

**The two candidate centres.**

\[
Q_s:=\mathrm{Law}(X)=\tfrac12\delta_{c_1}+\tfrac14\delta_{p(s)}+\tfrac14\delta_{q(s)},
\qquad
\nu:=\mathrm{Law}(C)=\tfrac12\delta_{c_1}+\tfrac12\delta_{c_2}.
\]

By L-9.R3.2b, \(\mathfrak M(\nu)=\{m_0\}\). By L-9.R3.2a(iii), \(\mathfrak M(Q_s)=\{m(s)\}\) is a singleton for every \(s\ge0\), and \(m(0)=m_0\).

#### 2.3.4 L-9.R3.2c — exact implicit-function reduction (general Hadamard manifold)

> **Lemma.** Let \(M\) be Hadamard, \(x_1,\dots,x_k(s)\) smooth curves of atoms with weights \(w_i>0\), \(\sum w_i=1\), and let \(m(s)\) be the (unique) Fréchet mean of \(\sum_iw_i\delta_{x_i(s)}\). Write \(v(s)=\log_{m_0}m(s)\in T_{m_0}M\) where \(m_0=m(0)\). Define, for \(x\) in a neighbourhood of \(m_0\),
> \[
> \Phi(v,s)=P_{\operatorname{Exp}_{m_0}v\to m_0}\Big[\sum_iw_i\log_{\operatorname{Exp}_{m_0}v}x_i(s)\Big]\in T_{m_0}M,
> \]
> \(P\) the radial parallel transport. Then \(\Phi\) is smooth, \(\Phi(v(s),s)\equiv0\), \(D_v\Phi(0,0)=-H\) with
> \(H=\sum_iw_i\operatorname{Hess}_{m_0}\tfrac12d(\cdot,x_i(0))^2\succeq\mathrm{Id}\), and \(v\) is smooth in \(s\). If moreover the family \(\{x_i(s)\}_i\) is invariant under \(s\mapsto-s\) (as a weighted set), then \(v\) is even, \(v'(0)=0\), and
> \[
> v(s)=s^2m_2+O(s^4),\qquad m_2=\tfrac12v''(0)=\tfrac12H^{-1}\,\partial_s^2\Phi(0,0).
> \]

*Proof.* Smoothness of \((x,z)\mapsto\log_xz\) on a Hadamard manifold is L-9.R3.2a(i); \(\operatorname{Exp}_{m_0}\) is a global diffeomorphism, so \(\Phi\) is smooth on \(T_{m_0}M\times\mathbb R\). \(\operatorname{grad}_x\tfrac12d(x,z)^2=-\log_xz\), hence \(D_x(-\log_xz)=\operatorname{Hess}_x\tfrac12d(\cdot,z)^2\); evaluating at \(v=0\) (where the radial transport is the identity to first order) gives \(D_v\Phi(0,0)=-H\), and \(H\succeq\mathrm{Id}\) by L-9.R3.2a(ii), hence invertible. The implicit function theorem gives a unique smooth local solution \(v(s)\); by strict convexity (L-9.R3.2a(iii)) the zero of the score is the Fréchet mean, so this solution is \(\log_{m_0}m(s)\). Symmetry gives \(\Phi(v,s)=\Phi(v,-s)\), hence \(v(s)=v(-s)\) by local uniqueness, hence \(v'(0)=0\) and \(v'''(0)=0\). Differentiating \(\Phi(v(s),s)=0\) twice at \(s=0\) and using \(v'(0)=0\) kills all cross terms and gives \(-Hv''(0)+\partial_s^2\Phi(0,0)=0\). \(\square\)

**Status: PROVED.** Applied to the construction with \(x_1\equiv c_1\) (\(w_1=\tfrac12\)), \(x_2=p(s)\), \(x_3=q(s)\) (\(w_2=w_3=\tfrac14\)):

\[
\partial_s^2\Phi(0,0)=\tfrac14\,\omega''(0),\qquad
\omega(s):=\log_{m_0}p(s)+\log_{m_0}q(s),
\]
and with \(E(\zeta):=\log_{m_0}\operatorname{Exp}_{c_2}\zeta\), \(\omega(s)=E(su)+E(-su)\), so \(\omega''(0)=2\,D^2E(0)[u,u]\) and

\[
\boxed{\;m_2=\tfrac14\,H^{-1}D^2E(0)[u,u]\;}\tag{R3.2-EXACT}
\]

This identity is exact on any Hadamard manifold; no expansion or remainder has been used.

#### 2.3.5 L-9.R3.2d — exact evaluation on \(H^2\), and a **global** (all \(s>0\)) conclusion

Two exact facts about the construction:

**(a) The mean stays on \(\gamma\).** Let \(\sigma\) be the geodesic reflection of \(H^2\) across \(\gamma\). It is an isometry; it fixes \(c_1,c_2,m_0\) and, because \(\ell\perp\gamma\) at \(c_2\), it maps \(p(s)\leftrightarrow q(s)\). Hence \(\sigma_\#Q_s=Q_s\), so \(F_{Q_s}\circ\sigma=F_{Q_s}\), so \(\sigma\) permutes \(\mathfrak M(Q_s)\); the argmin is a singleton (L-9.R3.2a(iii)); therefore \(m(s)\in\operatorname{Fix}(\sigma)=\gamma\).

**(b) Closed form along \(\gamma\).** Parametrise \(m_\tau:=\gamma(\tau)\), \(\tau\in\mathbb R\) (so \(\tau>0\) means "toward \(c_2\)"). Then \(d(m_\tau,c_1)=\beta+\tau\), and \(m_\tau,c_2,p(s)\) form a geodesic triangle with a right angle at \(c_2\) and legs \(|\beta-\tau|\), \(s\); the hyperbolic Pythagorean theorem gives \(\cosh d(m_\tau,p(s))=\cosh(\beta-\tau)\cosh s\), and by (a)'s reflection \(d(m_\tau,q(s))=d(m_\tau,p(s))\). Hence, exactly,

\[
\mathcal F_s(\tau):=F_{Q_s}(m_\tau)
=\tfrac12(\beta+\tau)^2+\tfrac12\big[\operatorname{arccosh}\!\big(\cosh(\beta-\tau)\cosh s\big)\big]^2 .
\tag{R3.2-CF}
\]

> **Theorem L-9.R3.2d.** For every \(\beta>0\) and every \(s>0\), the Fréchet mean \(m(s)\) of \(Q_s\) lies on \(\gamma\) strictly between \(m_0\) and \(c_2\). Consequently
> \[
> m(s)\ne m_0=\mathfrak M(\mathrm{Law}(C))\qquad\text{for every }s>0 .
> \]
> Moreover the exact second-order coefficient is
> \[
> m_2=\frac14\cdot\frac{\sinh\beta\cosh\beta-\beta}{\sinh^2\beta}\;\hat w,
> \qquad \hat w=\dot\gamma(0)=\frac{\log_{m_0}c_2}{\|\log_{m_0}c_2\|},
> \]
> which is a **strictly positive** multiple of \(\hat w\) for every \(\beta>0\), and \(\to\frac\beta6\hat w\) as \(\beta\to0\).

*Proof.* Write \(D(\tau,s)=\operatorname{arccosh}(\cosh(\beta-\tau)\cosh s)\) and \(D_0(s)=D(0,s)\). From (R3.2-CF),
\(\partial_\tau\mathcal F_s(\tau)=(\beta+\tau)-D\,\dfrac{\sinh(\beta-\tau)\cosh s}{\sinh D}\).
At \(\tau=0\), using \(\cosh s=\cosh D_0/\cosh\beta\),
\[
\partial_\tau\mathcal F_s(0)=\beta-D_0\frac{\sinh\beta\cosh s}{\sinh D_0}
=\beta-\tanh\beta\;D_0\coth D_0=:-\psi(D_0).
\]
Set \(\psi(D)=\tanh\beta\,D\coth D-\beta\). Then \(\psi(\beta)=\beta\tanh\beta\coth\beta-\beta=0\) and
\[
\psi'(D)=\tanh\beta\cdot\frac{\sinh D\cosh D-D}{\sinh^2D}>0\quad(D>0),
\]
since \(\sinh D\cosh D=\tfrac12\sinh2D>D\). Because \(\cosh D_0=\cosh\beta\cosh s>\cosh\beta\) for \(s>0\), we get \(D_0(s)>\beta\) and therefore \(\psi(D_0(s))>0\), i.e. \(\partial_\tau\mathcal F_s(0)<0\) for every \(s>0\). By L-9.R3.2a(iii) \(F_{Q_s}\) is \(2\)-strongly convex, so \(\mathcal F_s\) is strongly convex on \(\mathbb R\); a strictly negative derivative at \(\tau=0\) forces its unique minimiser \(\tau(s)\) to satisfy \(\tau(s)>0\). Together with (a), \(m(s)=\gamma(\tau(s))\) with \(\tau(s)>0\), and \(\tau(s)<\beta\) because \(\partial_\tau\mathcal F_s(\beta)=2\beta-0>0\) (at \(\tau=\beta\) the second term's derivative vanishes since \(\sinh(\beta-\tau)=0\)).

For the coefficient: by the reflection, \(\omega(s)=2\big(\text{component of }\log_{m_0}p(s)\text{ along }\hat w\big)\hat w\). In the right triangle \(m_0c_2p(s)\) with right angle at \(c_2\), the angle \(\theta\) at \(m_0\) satisfies \(\cos\theta=\tanh\beta/\tanh D_0\), and \(\|\log_{m_0}p(s)\|=D_0\); hence \(\omega(s)=2D_0\tanh\beta\coth D_0\,\hat w\). With \(G(D)=D\coth D\), \(D_0'(0)=0\) and \(\sinh\beta\,D_0''(0)=\cosh\beta\) (differentiate \(\cosh D_0=\cosh\beta\cosh s\) twice), so \(D_0''(0)=\coth\beta\) and
\[
\omega''(0)=2\tanh\beta\,G'(\beta)\coth\beta\,\hat w
=2\,\frac{\sinh\beta\cosh\beta-\beta}{\sinh^2\beta}\,\hat w .
\]
Thus \(D^2E(0)[u,u]=\tfrac12\omega''(0)=\frac{\sinh\beta\cosh\beta-\beta}{\sinh^2\beta}\hat w\). Since \(\hat w\) is the radial direction toward both \(c_1\) and \(c_2\) from \(m_0\), L-9.R3.2a(ii) gives \(H\hat w=\hat w\) (both atoms contribute radial eigenvalue \(1\)), so \(H^{-1}D^2E(0)[u,u]=D^2E(0)[u,u]\), and (R3.2-EXACT) gives the stated \(m_2\). Positivity is \(\sinh\beta\cosh\beta>\beta\). The limit follows from \(\sinh\beta\cosh\beta-\beta=\tfrac23\beta^3+O(\beta^5)\) and \(\sinh^2\beta=\beta^2+O(\beta^4)\). \(\square\)

**Status: PROVED.** *(Numerical sanity check, no status: direct minimisation of \(F_{Q_s}\) on the hyperboloid model reproduces \(\tau(s)>0\), \(\tau(s)/s^2\to m_2\) to eight digits for \(\beta\in\{0.3,1,2\}\), and confirms the second normal coordinate of the minimiser is \(<10^{-8}\), i.e. the mean is on \(\gamma\).)*

#### 2.3.6 L-9.R3.2e — curvature attribution, and the flat certificate

> **Proposition (mechanism).** On a general Hadamard manifold, with \(w=\log_{m_0}c_2\), \(P\) the parallel transport \(T_{c_2}M\to T_{m_0}M\) along \([c_2,m_0]\), and \(R\) the curvature tensor, the Gavrilov–Pennec double expansion (lead-ledger node L-8.1)
> \[
> \log_y\operatorname{Exp}_xZ=w+PZ+\tfrac16R(PZ,w)w+\tfrac13R(PZ,w)PZ+O(4),\qquad w=\log_yx,
> \]
> gives \(D^2E(0)[u,u]=\tfrac23R(Pu,w)Pu+O(\|w\|^3)\), hence via (R3.2-EXACT)
> \[
> m_2=\tfrac16H^{-1}R(Pu,w)Pu+O(\|w\|^3)
> \;\overset{\text{const. curv. }K}{=}\;-\tfrac K6H^{-1}w^{\perp}+O(\|w\|^3),
> \qquad w^\perp:=w-\langle w,Pu\rangle Pu .
> \]
> Therefore: \(m_2=0\) whenever \(w^\perp=0\), i.e. whenever \(c_1\in\ell\); \(\langle m_2,w^\perp\rangle>0\) when \(K<0\) and \(<0\) when \(K>0\); and \(m_2\equiv0\) identically in a flat space.

*Consistency check (this is a proof obligation, not decoration).* For \(K=-1\) and the perpendicular configuration (\(w^\perp=w\), \(\|w\|=\beta\), \(H^{-1}w=w\)) the formula predicts \(m_2=\tfrac\beta6\hat w\), which is exactly the \(\beta\to0\) limit computed **independently and exactly** in L-9.R3.2d. The two derivations are logically independent (one is an expansion, one is a closed form), and they agree. \(\square\)

**Status of the expansion: CITED+APPLIED** (external producer L-8.1, owned by B; used here only for the *interpretation*, never for the exact claim). **Status of the consistency check and of the corollaries: PROVED.**

> **L-9.R3.2f (flat certificate — exact, not asymptotic).** Run the identical construction in \(\mathbb R^d\): \(c_1,c_2\) arbitrary, \(m_0=\tfrac12(c_1+c_2)\), \(p=c_2+su\), \(q=c_2-su\). Then the mixture mean is \(\tfrac12c_1+\tfrac14p+\tfrac14q=\tfrac12c_1+\tfrac12c_2=m_0\) **for every \(s\), exactly**. Hence \(m(s)\equiv\mathfrak M(\mathrm{Law}(C))\) in flat space and the discrepancy proved in L-9.R3.2d is **entirely curvature-induced**. **Status: PROVED.**

**Classification of the L-9.R3.2 failure: curvature-specific** (it vanishes identically in a flat space and its leading coefficient is a curvature contraction), on top of the universal latent-centre/information deficiency of L-9.R3.0.

> **Strongest corrected theorem removing exactly the curvature feature.** *If the entire support of \(Q_s\) together with \(m_0\) lies in one totally geodesic flat submanifold \(F\subseteq M\) (equivalently, in the constant-curvature case, on one geodesic), then \(\mathfrak M(Q)=\mathfrak M(\mathrm{Law}(C))\) whenever \(\mathbb E[\text{tangent}\mid C]=0\).* Proof: the Fréchet mean of a law supported in a closed convex set of a Hadamard manifold lies in that set (nearest-point projection onto a convex set is \(1\)-Lipschitz and strictly decreases distance off the set), a totally geodesic flat is convex and isometric to a Euclidean space, and L-9.R3.1 applies inside it. **Status: PROVED.** This is sharp: L-9.R3.2d shows the conclusion fails for every \(s>0\) as soon as the support leaves the geodesic (\(c_1\notin\ell\)).

#### 2.3.7 Explicit admissible ranges and support conditions

Because \(H^2\) is Hadamard: (i) every \(\log\) used is globally defined and single-valued; (ii) no normal-neighbourhood, injectivity-radius, convexity-radius or cut-locus condition is required; (iii) \(\mathfrak M(Q_s)\) and \(\mathfrak M(\nu)\) are singletons for all parameter values; (iv) the admissible range is \(\beta\in(0,\infty)\) and \(s\in(0,\infty)\) — **the whole parameter space**. The IFT statement (L-9.R3.2c) is local in \(s\) by construction; the *conclusion* \(m(s)\ne m_0\) is global by L-9.R3.2d and needs no smallness. Quantitatively, \(\tau(s)\) is the unique root of \(\partial_\tau\mathcal F_s=0\) and satisfies \(0<\tau(s)<\beta\) and \(\tau(s)\ge\psi(D_0(s))/\Lambda\) where \(\Lambda=\sup_{|\tau|\le\beta}\partial^2_\tau\mathcal F_s\le1+ \big(2\beta+ s\big)\coth\big(2\beta+s\big)+1\) by L-9.R3.2a(ii).

**Positive-curvature remark (scope-locked).** On \(S^2\) with all four points inside an open geodesic ball of radius \(\pi/4\) (so that \(\mathfrak M\) is a singleton and all Logs are unique by standard Karcher/Kendall conditions), the same computation with \(K=+1\) gives \(\langle m_2,w^\perp\rangle<0\): the mixture mean moves *away* from \(c_2\). **Status: CITED+APPLIED (leading order in \(\|w\|\), via L-8.1) with an explicit support lock.** It is recorded only as the sign complement of L-9.R3.2e; nothing downstream depends on it.

### 2.4 The exact class on which mixture mean \(=\) mixing-centre mean

#### 2.4.1 L-9.R3.2g — the equivariance/symmetry class is **sufficient**

> **Proposition.** Let \(G\le\operatorname{Isom}(M)\) with \(\operatorname{Fix}(G)=\{m^\star\}\) a single point. If \(Q\) is \(G\)-invariant and \(\mathfrak M(Q)\) is a singleton, then \(\mathfrak M(Q)=\{m^\star\}\). If in addition \(\nu=\mathrm{Law}(C)\) is \(G\)-invariant with singleton argmin, then \(\mathfrak M(\nu)=\{m^\star\}=\mathfrak M(Q)\).

*Proof.* For \(g\in G\), \(F_Q(gx)=\int d(gx,z)^2Q(dz)=\int d(gx,gz)^2Q(dz)=\int d(x,z)^2Q(dz)=F_Q(x)\), using \(g_\#Q=Q\) and that \(g\) is an isometry. Hence \(g\) permutes \(\mathfrak M(Q)\); a singleton is fixed by every \(g\), so it lies in \(\operatorname{Fix}(G)\). \(\square\)

**Status: PROVED.**

#### 2.4.2 L-9.R3.2h — the symmetry class is **not necessary**, and the exact characterisation

> **Theorem (exact characterisation).** Let \(M\) be Hadamard, \(\nu=\mathrm{Law}(C)\in\mathcal P_2(M)\) with Fréchet mean \(m_C\), and let \(Q\) be the mixture with conditional laws \(Q_c=\mathrm{Law}(X\mid C=c)\), each having Fréchet mean \(c\). Define the **curvature defect** of \(Q_c\) at base point \(y\),
> \[
> \Delta(y,c):=\mathbb E\big[\log_yX\mid C=c\big]-\log_yc\;\in T_yM .
> \]
> Then
> \[
> \mathfrak M(Q)=\{m_C\}\quad\Longleftrightarrow\quad \int_M\Delta(m_C,c)\,\nu(dc)=0 .
> \]
> In a flat space \(\Delta\equiv0\), so equality always holds. By L-8.1, \(\Delta(y,c)=\tfrac13\mathbb E[R(PV,w_c)PV\mid C=c]+O(4)\) with \(w_c=\log_yc\), \(V=\log_cX\), \(P\) the transport \(T_cM\to T_yM\).

*Proof.* On a Hadamard manifold the Fréchet mean is the unique zero of \(x\mapsto\mathbb E\log_xX\) (L-9.R3.2a(iii)). Now \(\mathbb E\log_{m_C}X=\int\mathbb E[\log_{m_C}X\mid C=c]\nu(dc)=\int\log_{m_C}c\,\nu(dc)+\int\Delta(m_C,c)\nu(dc)\), and the first integral is \(0\) because \(m_C\) is the Fréchet mean of \(\nu\). Hence \(\mathbb E\log_{m_C}X=\int\Delta(m_C,c)\nu(dc)\), which vanishes iff \(m_C\) solves the first-order condition for \(Q\), iff \(m_C\) is the Fréchet mean of \(Q\). In flat space \(\log_yx=x-y\) is affine, so \(\Delta(y,c)=\mathbb E[X\mid C=c]-c=0\). \(\square\)

> **Corollary (symmetry is sufficient but not necessary).**
> **(a) Flat non-symmetric example.** \(M=\mathbb R\); \(C=0\) w.p. \(1/3\), \(C=1\) w.p. \(2/3\); given \(C=0\), \(X=\pm1\) w.p. \(1/2\); given \(C=1\), \(X=1\). Then \(Q=\tfrac16\delta_{-1}+\tfrac56\delta_{1}\), \(\mathfrak M(Q)=\{2/3\}=\mathfrak M(\nu)\). The stabiliser of \(Q\) in \(\operatorname{Isom}(\mathbb R)\) is \(\{\mathrm{id}\}\), whose fixed set is \(\mathbb R\), not a point. So the hypothesis of L-9.R3.2g fails while its conclusion holds.
> **(b) Curved non-symmetric example.** In the \(H^2\) construction take \(c_1\in\ell\) (i.e. rotate \(\ell\) onto \(\gamma\)). Then the whole support lies on one geodesic, a totally geodesic flat, and by L-9.R3.2f's corrected theorem \(m(s)\equiv m_0\) for every \(s\). The stabiliser of \(Q_s\) is \(\{\mathrm{id},\text{reflection across }\gamma\}\), whose fixed set is \(\gamma\), a one-dimensional set, not a point. Equality holds without the single-fixed-point condition.
> **(c) Cancellation class.** By the theorem, equality holds on the (generically codimension-\(\dim M\)) set where the \(\nu\)-average of the curvature defect cancels; e.g. two conditional laws whose defects are equal and opposite. This class contains laws with trivial isometry stabiliser.

**Status: PROVED (characterisation and all three non-necessity witnesses).**

**Answer to (i), in one line.** *Mixture mean \(=\) mixing-centre mean exactly when the \(\nu\)-average of the curvature defect vanishes. Sufficient conditions: a flat/totally-geodesic support; or a \(G\)-invariance with a single fixed point. Neither is necessary. In flat space the mixture mean is \(\mathbb EC\) and is never the realised \(C\) unless \(C\) is degenerate.*

---

## 3. Question (ii) — different latent centres and different loadings sharing every marginal

### 3.1 L-9.R3.3-mar-flat (flat witness)

\(H=\mathbb R^2\). Both models are i.i.d. in time; \(\Gamma_\delta\) white by construction.

- **Model 1** (deterministic centre): \(C^{(1)}_t\equiv0\); \(r=1\), \(A^{(1)}=e_1\), \(f^{(1)}_t\sim N(0,1)\) i.i.d.; \(\delta^{(1)}_t=e_2\eta_t\), \(\eta_t\sim N(0,1)\) i.i.d. independent of \(f^{(1)}\).
- **Model 2** (latent stochastic centre): \(C^{(2)}_t=e_1\gamma_t\), \(\gamma_t\sim N(0,1)\) i.i.d.; \(r=1\), \(A^{(2)}=e_2\), \(f^{(2)}_t=\eta_t\); \(\delta^{(2)}\equiv0\).

**Audit.** LC1 ✓ (\(\mathbb E\|C\|^2=1<\infty\)). LC2 ✓ (\(\|e_1\|=\|e_2\|=1\)). LC3 ✓ (flat, global charts). LC4 ✓ (\(f\) independent of \(C\), centred). LC5 ✓ (\(\delta\) white and independent; cross-lags zero). Marginals: both \(N(0,I_2)\) ✓. Centre processes: \(0\) versus a nondegenerate i.i.d. process — different. Loading ranges: \(\operatorname{span}(e_1)\ne\operatorname{span}(e_2)\) — different, and **not** related by any \(R\in GL(1)\). Fréchet mean of each marginal: \(0\) in both, equal to neither model's centre in Model 2. **Status: PROVED.**

### 3.2 L-9.R3.3-mar-curved (curved witness, reusing §2.3)

Take \(Q_s\) from §2.3 with \(s>0\) and \(\beta>0\).

- **Model A** (latent centre): as constructed; centre \(C\in\{c_1,c_2\}\), \(r=1\), \(A=u\).
- **Model B** (deterministic centre at the marginal Fréchet mean): \(C^{B}\equiv m(s)\) deterministic, \(r=0\) (no factor), \(\delta^{B}=\log_{m(s)}X\), a mean-zero (by the first-order condition) i.i.d. tangent noise.

Both have marginal \(Q_s\); Model B satisfies Paper 1's precondition 1 exactly (\(C^B\) is the unique marginal Fréchet mean by L-9.R3.2a(iii)); Model A does not. Loading ranks are \(1\) and \(0\); loading ranges \(\operatorname{span}(u)\) at \(c_2\) and \(\{0\}\). By L-9.R3.2d, \(m(s)\notin\{c_1,c_2,m_0\}\): **the ID-1 centre is neither a realised latent centre, nor the mean of the mixing centres.** **Status: PROVED.** **Classification: latent-centre-induced, aggravated by a curvature-specific term.**

**Answer to (ii): yes**, in flat and in curved geometry, with all admissibility conditions verified.

---

## 4. Question (iii) — sharing every finite-dimensional distribution (L-9.R3.3)

### 4.1 (a) The cheap version, stated exactly, and its admissibility audit

> **L-9.R3.3a.** Let \(H\) be a real separable Hilbert space, \(A:\mathbb R^r\to H\) isometric, \((f_t)\) stationary centred with \(\mathbb E\|f_t\|^2<\infty\), \((\delta_t)\) white and independent of \(f\). Define
> \[
> \text{Model I: }C^{\mathrm I}_t\equiv0,\quad A^{\mathrm I}=A,\quad f^{\mathrm I}=f,\quad\delta^{\mathrm I}=\delta;
> \qquad
> \text{Model II: }C^{\mathrm{II}}_t=Af_t,\quad r^{\mathrm{II}}=0,\quad\delta^{\mathrm{II}}=\delta .
> \]
> Then \(X^{\mathrm I}_t=X^{\mathrm{II}}_t\) **pathwise**, hence the two models have identical finite-dimensional distributions, identical marginals, and identical fixed-anchor lag rows: they are \(\mathcal I_J\)-, \(\mathcal I_M\)-, \(\mathcal I_1\)- and \(\mathcal I_F(c_0)\)-equivalent. Yet their centre processes are \(0\) and \(Af\), and their loading ranks are \(r\) and \(0\).

*Proof.* \(C^{\mathrm{II}}_t+0+\delta_t=Af_t+\delta_t=C^{\mathrm I}_t+Af_t+\delta_t\). \(\square\) **Status: PROVED.**

**Which declared condition rules Model II out, exactly.** Two, and it matters which:

- **(α) Determinism in rescaled time.** Paper 1 §"Model and estimator" writes the centre as \(\mu_n(u_t)\) with \(\mu_n:[0,1]\to M\) a *function*; HD1 (HD-M) makes the same declaration. Model II's centre \(Af_t\) is not a function of \(u_t\).
- **(β) Centre \(=\) marginal Fréchet mean.** HD1 (HD-M) states "the proxy laws have Fréchet mean \(\mu_n(u)\)"; Paper 1 "Identification preconditions" item 1 presupposes it. Model II's centre is not the marginal Fréchet mean of \(X_t\) (which is \(0\)).

**Is that scientifically defensible, or does it beg the question?** Split the verdict, because the two conditions have different standing.

- **(β) is a defensible normalisation.** It is isometry-equivariant, it is a functional of each marginal law, it produces a well-defined estimand, and by L-9.R3.0 it is the *only* kind of rule that can make the centre law-measurable at each \(u\). Registered as: **REFORMULATED+PROVED — (β) is a normalisation, not an identifying restriction.**
- **(α) begs the question, in the exact technical sense that it is untestable and it presupposes the answer.** By §4.4 (Theorem R3-D) the deterministic-centre representation always exists whenever the observed spectral density is uniformly positive definite, so (α) is never rejected by the data; and by §4.2–§4.3 different choices consistent with (α)-violation change \(\operatorname{ran}A\) arbitrarily. Since the financial application's motivating object is *a baseline volatility level that is plausibly a latent stochastic process*, (α) converts the scientific question "does the baseline drift stochastically?" into "what is the deterministic part of the level?" by fiat. Registered as: **DISPROVED as an identifying restriction; REFORMULATED+PROVED as a declared modelling convention** — admissible only if displayed as such, with the §5 frequency-band reading attached.

**Status of §4.1: PROVED.** **Classification: latent-centre-induced + convention-induced.**

### 4.2 (b) The non-trivial version: incomparable loading ranges, identical FDDs

> **L-9.R3.3b.** Let \(H=\mathbb R^3\). Let \(g,k,l\) be three mutually independent stationary Gaussian AR(1) processes with parameters \(\rho_g,\rho_k,\rho_l\in(0,1)\) pairwise distinct and unit marginal variances. Set
> \[
> X_t=e_1g_t+e_2k_t+e_3l_t .
> \]
> Define two latent-centre representations:
> \[
> \text{Model 1: } C^{(1)}_t=e_1g_t,\quad A^{(1)}=[e_2\;e_3],\quad f^{(1)}=(k,l)^\top,\quad\delta^{(1)}\equiv0;
> \]
> \[
> \text{Model 2: } C^{(2)}_t=e_3l_t,\quad A^{(2)}=[e_1\;e_2],\quad f^{(2)}=(g,k)^\top,\quad\delta^{(2)}\equiv0 .
> \]
> Then the two models generate the *same process pathwise*, hence share every finite-dimensional distribution; their centre processes are different, both nondegenerate and both serially dependent; and their loading ranges
> \[
> \operatorname{ran}A^{(1)}=\operatorname{span}\{e_2,e_3\},\qquad \operatorname{ran}A^{(2)}=\operatorname{span}\{e_1,e_2\}
> \]
> are **incomparable**: neither contains the other. Neither model is a relabelling, gauge change, or dynamically silent reallocation of the other.

**Full audit.** Manifold/metric: \(\mathbb R^3\) Euclidean (flat, complete, Hadamard, global charts, empty cut locus). Construction: three independent Gaussian AR(1)s, jointly stationary and jointly Gaussian, \(\Gamma_X(h)=\operatorname{diag}(\rho_g^{|h|},\rho_k^{|h|},\rho_l^{|h|})\). Fréchet means: each marginal is \(N(0,I_3)\); \(F_Q\) is strictly convex with unique minimiser \(0\); both models' marginal Fréchet mean is \(0\) and equals neither centre process. Support/normal neighbourhoods: global, no restriction. Factor rank: \(2\) in both; loading maps isometric (\(A^*A=I_2\)); factor laws are bivariate Gaussian AR(1)s with positive-definite spectral density; noise laws are zero. Temporal dependence and spectra: each component has spectral density \((1-\rho^2)/(2\pi|1-\rho e^{-i\lambda}|^2)>0\) on \([-\pi,\pi]\); no atom at zero; all processes are geometrically \(\alpha\)-mixing. LC1–LC5 verified: LC1 ✓; LC2 ✓; LC3 ✓; LC4 ✓ (factor independent of centre, centred); LC5 ✓ (\(\delta\equiv0\)). Observational object claimed equal: the **entire law of the process** (pathwise identity, hence all FDDs, hence \(\mathcal I_J\)). Conclusion violated: ID-2(1)–(3), i.e. "every admissible loading contains \(\mathcal S_X\)", "minimum dynamic rank is \(q=\dim\mathcal S_X\)", and "every minimum loading range equals \(\mathcal S_X\)". Here
\[
\mathcal S_X=\overline{\operatorname{span}}\{\operatorname{ran}\Gamma_X(h):h\ne0\}=\mathbb R^3,
\]
while \(\operatorname{ran}A^{(1)}\) and \(\operatorname{ran}A^{(2)}\) are two-dimensional: \(\mathcal S_X\not\subseteq\operatorname{ran}A^{(i)}\). Responsible feature: the reallocated component (\(g\) in Model 1, \(l\) in Model 2) is **dynamically active** — it carries nonzero-lag covariance — and ID-2/C-7 correctly proved that such a component cannot be moved between factor and *noise*; it can be moved into the **centre**. That is a strictly new reallocation channel.

**Status: PROVED.** **Classification: latent-centre-induced (universal — it is present in flat space; not curvature-, cut-locus-, or completeness-specific).**

**Why this kills the gate rather than decorating it.** ID-2 is stated over \(\mathcal I_J\) and is the campaign's strongest positive identification result for the loading space. L-9.R3.3b shows ID-2's conclusion (1) is *false* on LC, not merely weakened, because the class LC contains representations whose loading range omits part of \(\mathcal S_X\).

### 4.3 (c) The curved version on a Hadamard product (\(H^2\times H^2\))

Curvature is not the mechanism (§4.2 is flat), so the point of this construction is to certify that nothing in §4.2 is an artefact of flatness, with curvature genuinely active — i.e. with support that is *not* contained in any one-dimensional geodesic or flat.

> **L-9.R3.3c.** Let \(M=H^2\times H^2\) with the product metric. Fix \(\mu_1,\mu_2\) and let \(\xi=(\xi_t)\) be a stationary \(T_{\mu_1}H^2\cong\mathbb R^2\)-valued Gaussian VAR(1) with nonsingular lag-1 covariance and nonsingular innovation covariance, and \(\eta=(\eta_t)\) an independent stationary \(T_{\mu_2}H^2\cong\mathbb R^2\)-valued Gaussian VAR(1) with the same properties and different parameters. Define
> \[
> X_t=\big(\operatorname{Exp}_{\mu_1}\xi_t,\ \operatorname{Exp}_{\mu_2}\eta_t\big)\in M .
> \]
> Then:
> \[
> \text{Model A: } C^A_t=\big(\operatorname{Exp}_{\mu_1}\xi_t,\ \mu_2\big),\quad
> \operatorname{ran}A^{A}=\{0\}\oplus T_{\mu_2}H^2,\quad f^A=\eta,\ \delta^A\equiv0;
> \]
> \[
> \text{Model B: } C^B_t=\big(\mu_1,\ \operatorname{Exp}_{\mu_2}\eta_t\big),\quad
> \operatorname{ran}A^{B}=T_{\mu_1}H^2\oplus\{0\},\quad f^B=\xi,\ \delta^B\equiv0
> \]
> generate the same process pathwise, hence share every FDD; their centre processes are different, both nondegenerate, both \(M\)-valued and serially dependent; their loading ranges are two-dimensional and **orthogonal**, hence incomparable.

**Full audit.**
*Manifold and metric.* \(H^2\times H^2\), product of Hadamard manifolds, hence Hadamard: complete, simply connected, \(K\le0\), empty cut locus, all Logs global and single-valued, \(\operatorname{Exp}\) a global diffeomorphism (L-9.R3.2a(i)).
*Exactness of the model equation.* In a Riemannian product, \(\operatorname{Exp}_{(a,b)}(v,w)=(\operatorname{Exp}_av,\operatorname{Exp}_bw)\) and \(\log_{(a,b)}(x,y)=(\log_ax,\log_by)\). Hence \(\operatorname{Exp}_{C^A_t}(0,\eta_t)=(\operatorname{Exp}_{\mu_1}\xi_t,\operatorname{Exp}_{\mu_2}\eta_t)=X_t\) exactly, and symmetrically for B. No approximation.
*Covariantly constant loading (Paper 1's \(\mathcal P^{\mu}_{u_0\to u_t}\)).* The Levi-Civita connection of a product is the product connection, so parallel transport along any curve contained in the slice \(H^2\times\{\mu_2\}\) acts as (transport in the first factor) \(\oplus\ \mathrm{Id}\). The Model-A centre path lies in that slice, so \(\operatorname{ran}A^A=\{0\}\oplus T_{\mu_2}H^2\) is preserved **exactly** and the transported loading map is literally constant. Symmetrically for B. Paper 1's covariant-constancy requirement is therefore met exactly, not approximately.
*Fréchet means.* For a product metric, \(F_Q(x,y)=F_{Q^{(1)}}(x)+F_{Q^{(2)}}(y)\) for the two marginals \(Q^{(1)},Q^{(2)}\) — no independence needed. On a Hadamard manifold \(m\) is the Fréchet mean iff \(\mathbb E\log_mX=0\) (L-9.R3.2a(iii)); since \(\mathbb E\xi_t=0\) and \(\mathbb E\eta_t=0\), the marginal Fréchet mean of \(X_t\) is exactly \((\mu_1,\mu_2)\), deterministic, and equals neither model's centre process.
*Support and curvature activity.* \(\xi_t\) has nonsingular covariance, so the support of the first coordinate of \(X_t\) is all of \(H^2\) and is contained in no geodesic; the curvature term of L-9.R3.2e is generically nonzero on this support. Nothing here is a flat artefact.
*Factor rank, loading, factor law, noise law.* \(r=2\) in both; \(A^A,A^B\) isometric onto their two-dimensional ranges; factor laws are Gaussian VAR(1) with positive-definite spectral density on \([-\pi,\pi]\); \(\delta\equiv0\).
*Temporal dependence and spectra.* Both factors are geometrically \(\alpha\)-mixing with no spectral atom at zero; \(\Gamma_X(h)\) is block diagonal with blocks \(\Gamma_\xi(h),\Gamma_\eta(h)\), both nonzero for \(h\ne0\).
*LC audit.* LC1 ✓; LC2 ✓; LC3 ✓ exactly; LC4 ✓ (the two factors are independent, so \(\mathbb E[f\mid C]=0\)); LC5 ✓.
*Observational object claimed equal.* The full path law.
*Violated conclusion.* Same as §4.2: \(\mathcal S_X=T_{\mu_1}H^2\oplus T_{\mu_2}H^2\) after transport, while both loading ranges are proper two-dimensional subspaces.
*Responsible feature.* Latent centre absorbing dynamically active energy. Curvature is present and active but is *not* the mechanism.

*Third model, for contrast.* \(C^0\equiv(\mu_1,\mu_2)\) deterministic, \(r=4\), \(A^0=\mathrm{Id}\), \(f^0=(\xi,\eta)\), \(\delta^0\equiv0\). This satisfies Paper 1's (α) and (β) exactly and has \(\operatorname{ran}A^0=\mathcal S_X\). It is the representative selected by the convention, and nothing in the data prefers it.

**Status: PROVED.** **Classification: latent-centre-induced (universal); certified non-flat.**

### 4.4 (d) What survives — the exact quotient

Work on \(\mathrm{LC}^{\circ}\) with \(H=\mathbb R^p\) (the Hilbert case is identical with trace-class operators in place of matrices). Let \(f_X\) denote the spectral density matrix of the observed process, and \(f_C,f_f,f_\delta=\Gamma_\delta(0)/2\pi\) those of the components.

> **Theorem R3-D (complete non-identification of the loading range).** Suppose the observed process is centred, stationary, Gaussian, with spectral density satisfying \(f_X(\lambda)\succeq\varepsilon I_p\) for all \(\lambda\in[-\pi,\pi]\) and some \(\varepsilon>0\). Then for **every** subspace \(V\subseteq\mathbb R^p\) and every \(r=\dim V\in\{0,1,\dots,p\}\) there exists an \(\mathrm{LC}^{\circ}\) representation \((C,A,f,\delta)\) of the observed law with \(\operatorname{ran}A=V\), \(A^*A=I_r\), \(\{\Gamma_f(h)\}\) a positive-definite covariance sequence, \(\delta\equiv0\), \(\Gamma_{Cf}\equiv0\), and \(C\) a stationary Gaussian process with \(\mathbb E C_t=0\).

*Proof.* Fix \(V\), pick \(A\) with \(A^*A=I_r\) and \(\operatorname{ran}A=V\). Choose \(\rho\in(0,1)\) and \(\varepsilon'>0\) with \(\varepsilon'\frac{1+\rho}{1-\rho}<\varepsilon\). Let \(f\) be an \(\mathbb R^r\)-valued Gaussian AR(1) with \(\Gamma_f(h)=\varepsilon'\rho^{|h|}I_r\); its spectral density is \(g(\lambda)=\frac{\varepsilon'}{2\pi}\frac{1-\rho^2}{|1-\rho e^{-i\lambda}|^2}I_r\), which is positive definite and satisfies \(\|2\pi g(\lambda)\|\le\varepsilon'\frac{1+\rho}{1-\rho}<\varepsilon\). Set \(f_C(\lambda)=f_X(\lambda)-Ag(\lambda)A^*\). Since \(\|Ag(\lambda)A^*\|=\|g(\lambda)\|<\varepsilon/2\pi\cdot\)—more precisely \(Ag A^*\preceq\|g\|I_p\prec\varepsilon I_p/(2\pi)\cdot 2\pi\)—we get \(f_C(\lambda)\succ0\) for all \(\lambda\); \(f_C\) is Hermitian, measurable, integrable and positive semidefinite, hence is the spectral density of a centred stationary Gaussian process \(C\), which we take independent of \(f\). Then \(C+Af\) is centred Gaussian stationary with spectral density \(f_C+AgA^*=f_X\), hence has exactly the law of \(X\) (a centred Gaussian process is determined by its covariance sequence). LC1 ✓, LC2 ✓, LC3 ✓ (flat), LC4 ✓ (independence), LC5 ✓ (\(\delta\equiv0\)); \(\Gamma_{Cf}\equiv0\) ✓; \(\{\Gamma_f(h)\}\) is positive definite ✓. \(\square\)

**Status: PROVED.** **Sharp form on degenerate spectra.** Without uniform positive definiteness the following two-sided bound is exact:
- *Necessary:* if \(\operatorname{ran}A=V\) is admissible with factor spectral density \(g\), then \(AgA^*\preceq f_X\) a.e., so \(V\subseteq\operatorname{ran}f_X(\lambda)\) for a.e. \(\lambda\) in \(\{g\succ0\}\), a set of positive measure.
- *Sufficient:* if there are \(c>0\) and a positive-measure \(\Lambda\subseteq[-\pi,\pi]\) with \(f_X(\lambda)\succeq cP_V\) on \(\Lambda\) in the sense that \(f_X-c\mathbf1_\Lambda P_V\succeq0\) a.e., then \(V\) is admissible (take \(g=\varepsilon\mathbf1_\Lambda P_V\), \(\varepsilon\le c\)).

The gap between the two concerns only laws whose spectral density is degenerate on a positive-measure frequency set; on the regime Paper 1 works in (nondegenerate idiosyncratic noise) the sufficient condition holds for every \(V\).

> **Theorem R3-SURV (the honest replacement statement).** Over \(\mathrm{LC}^{\circ}\), under \(\mathcal I_J\):
> 1. The identified object is \(\mathrm{Law}(X)\) and its functionals — nothing more. In particular the total covariance sequence
> \[
> \Gamma_X(h)=\Gamma_C(h)+A\Gamma_f(h)A^*\ (h\ne0),\qquad
> \Gamma_X(0)=\Gamma_C(0)+A\Gamma_f(0)A^*+\Gamma_\delta(0)
> \]
> is identified, **as a sum**, and so is \(\mathcal S_X=\overline{\operatorname{span}}\{\operatorname{ran}\Gamma_X(h):h\ne0\}\).
> 2. \(\mathcal S_X\) is the minimum dynamic span of the **total** signal \(C+Af\), not of \(Af\). The decomposition \(\mathcal S_X\supseteq\mathcal S_C+\operatorname{ran}A\) holds, with equality failing only through cancellation (C-10's mechanism), and **neither summand is identified**.
> 3. Consequently \(r\), \(\operatorname{ran}A\), \(\{\Gamma_f(h)\}\), \(\{\Gamma_C(h)\}\) and \(\Gamma_\delta(0)\) are each non-identified, and **ID-2 conclusions (1), (2), (3) are FALSE on \(\mathrm{LC}^\circ\)**. ID-2(4) (white-at-zero reallocation) survives *a fortiori* — it is a special case of a strictly larger reallocation group.
> 4. On the marginal level, the identified centre is the mixture Fréchet mean \(\mathfrak M(Q_u)\), which by L-9.R3.1 equals \(\mathbb EC_u\) in flat space and by L-9.R3.2d does not even equal \(\mathfrak M(\mathrm{Law}(C_u))\) in curvature.
> 5. Therefore **there is no nontrivial surviving quotient of the parameter \((C,A,f,\delta)\)** on the uniformly-positive-definite class: the quotient map to the observed law has fibres as large as Theorem R3-D describes, and the induced quotient is the identity on laws.

*Proof.* (1) is the definition of \(\mathcal I_J\) plus bilinearity of covariance and \(\Gamma_{Cf}\equiv0\). (2)–(3) follow from Theorem R3-D and §4.2. (4) is §2. (5) restates R3-D. \(\square\)

**Status: PROVED.** **Classification: latent-centre-induced + information-deficient (universal).**

> **Strongest corrected theorem on this class.** *None nontrivial exists without a further declaration.* Proof: by R3-D, for any two subspaces \(V_1,V_2\) there are representations with \(\operatorname{ran}A=V_1\) and \(=V_2\) of the same law; any functional of \(\operatorname{ran}A\) that is a law functional must therefore be constant across all subspaces, i.e. trivial. Symmetrically for \(r\), \(\Gamma_f\), \(\Gamma_C\). \(\square\) **Status: PROVED (no-go).**

### 4.5 (e) The restriction that restores identification

The only escape allowed by §4.4 is to *declare* a set of frequencies on which the centre contributes nothing. This is exactly the scale/frequency separation the lead anticipated, and it is stated below in primitive spectral terms — no opaque assumption is introduced.

> **Theorem R3-BAND.** Work on \(\mathrm{LC}^{\circ}\) and declare:
> - **(FS-1)** a Borel set \(B_H\subseteq[-\pi,\pi]\) of positive Lebesgue measure with \(f_C(\lambda)=0\) for a.e. \(\lambda\in B_H\) (the centre has **no energy** in the declared high band);
> - **(FS-2)** \(f_f(\lambda)=0\) for a.e. \(\lambda\in B_L:=[-\pi,\pi]\setminus B_H\) (the factor has **no energy** in the declared low band);
> - **(FS-3)** \(\delta\) white, so \(f_\delta\equiv\Gamma_\delta(0)/2\pi\) is a constant matrix;
> - **(FS-4)** \(\Gamma_{Cf}\equiv0\);
> - **(FS-5)** *band-contrast completeness:* \(\operatorname{span}\{\operatorname{ran}(f_f(\lambda)-f_f(\lambda')):\lambda,\lambda'\in B_H\}=\mathbb R^r\).
>
> Then, exactly,
> \[
> \operatorname{ran}A=\operatorname{span}\big\{\operatorname{ran}\big(f_X(\lambda)-f_X(\lambda')\big):\lambda,\lambda'\in B_H\big\},
> \qquad
> \mathcal S_C=\operatorname{span}\big\{\operatorname{ran}\big(f_X(\lambda)-f_X(\lambda')\big):\lambda,\lambda'\in B_L\big\},
> \]
> both identified from \(\mathcal I_J\). The factor lag structure \(\{\Gamma_f(h)\}\) is identified up to the ID-2 gauge \(R\in GL(r)\) (orthogonal after isometric normalisation), and the centre's dynamics is identified on \(B_L\). The residual non-identification is **exactly** ID-2(4): the split of the frequency-constant part among \(\Gamma_\delta(0)\), the band-constant part of \(f_f\), and the band-constant part of \(f_C\) is the white-at-zero reallocation quotient, and nothing else survives.

*Proof.* \(f_X=f_C+Af_fA^*+f_\delta\) by (FS-4). On \(B_H\), (FS-1) and (FS-3) give \(f_X(\lambda)=Af_f(\lambda)A^*+f_\delta\); differencing two frequencies in \(B_H\) removes the constant \(f_\delta\), so \(f_X(\lambda)-f_X(\lambda')=A(f_f(\lambda)-f_f(\lambda'))A^*\), whose range is \(A\operatorname{ran}(f_f(\lambda)-f_f(\lambda'))\subseteq\operatorname{ran}A\); taking the span and using (FS-5) with injectivity of \(A\) gives equality. Symmetrically on \(B_L\) with (FS-2). Two loading maps with the same range and both isometric differ by an orthogonal \(R\), which transforms \(\Gamma_f\) as in ID-2(3). The remaining constant matrix is unidentified exactly as in ID-2(4). \(\square\)

> **Theorem R3-BAND-NEC (the restriction is necessary, not merely convenient).** If no set \(\Lambda\) of positive measure is declared on which \(f_C\) vanishes, and if \(f_X\succeq\varepsilon I\) uniformly, then by Theorem R3-D every subspace of every dimension is an admissible loading range, so \(\operatorname{ran}A\) is not identified. Hence a declared centre-free frequency set is necessary and (with FS-5) sufficient. \(\square\)

**Status: PROVED (both directions on the uniformly-pd class).** **Classification of the underlying failure: zero-frequency-induced / convention-induced.** The restriction cannot be tested: by R3-D the data are compatible with any assignment, so which band belongs to the centre is a **declaration**. Paper 1 must say so.

#### 4.5.1 L-9.R3.6 — the locally stationary version, and the exact hand-off to Workstream A (ID-7)

In the triangular array the band declaration becomes: the centre varies only in rescaled time \(u=t/n\) (energy confined to frequencies \(O(n^{-1})\)), while the factor is mean-zero with persistent energy bounded away from frequency zero. The three-scale mean estimator is a low-pass operation over an effective window of length \(N_n=nb_n\); the centre passes because \(n^{-1}\ll(nb_n)^{-1}\), and the factor leaks in with amplitude equal to its normalised partial-sum modulus. Define, with \(f^{(u)}\) the frozen factor,

\[
\psi_n(N):=\sup_u\Big\|N^{-1}\sum_{t=1}^{N}f^{(u)}_t\Big\|_{L^2},
\qquad
\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
\]

> **Proposition L-9.R3.6.** Let \(b_n=n^{-\alpha}\), \(\alpha\in(0,1)\), and suppose the frozen factor has memory exponent \(d\in[0,1/2)\), i.e. \(\psi_n(N)\asymp N^{d-1/2}\) (\(d=0\) short memory). Then:
> 1. \(\psi_n(nb_n)=o(\ell_n)\) is **impossible** for every \(d\ge0\) and every \(\alpha\in(0,1)\). Indeed \(\ell_n\ge(nb_n)^{-1/2}\) and \(\psi_n(nb_n)=(nb_n)^{d-1/2}\ge(nb_n)^{-1/2}\).
> 2. At \(d=0\) the leakage is exactly of the same order as the stochastic term: \(\psi_n(nb_n)\asymp(nb_n)^{-1/2}\asymp n^{-3/7}=\ell_n\) at \(\alpha=1/7\), \(a\ge3/7\). It is therefore **at the design point**, not negligible, and must be treated as a leading term.
> 3. For \(d>0\), \(\psi_n(nb_n)/(nb_n)^{-1/2}=(nb_n)^{d}\to\infty\): the leakage strictly dominates the centre estimator's stochastic error at every admissible bandwidth. Re-optimising \(\max\{n^{-3\alpha},n^{(1-\alpha)(d-1/2)}\}\) gives
> \[
> \alpha^\star=\frac{1-2d}{7-2d},\qquad \ell_n^\star=n^{-3(1-2d)/(7-2d)},
> \]
> which reduces to \(\alpha^\star=1/7\), \(\ell_n^\star=n^{-3/7}\) at \(d=0\).

*Proof.* (1) and (2) are the displayed inequalities. (3): with \(b_n=n^{-\alpha}\), \(nb_n=n^{1-\alpha}\), so the leakage exponent is \((1-\alpha)(d-1/2)\) and the bias exponent is \(-3\alpha\); equating gives \(3\alpha=(1-\alpha)(1/2-d)\), i.e. \(\alpha(3+1/2-d)=1/2-d\), i.e. \(\alpha^\star=(1-2d)/(7-2d)\). \(\square\)

**Status: PROVED.**

> **Recorded obligations for Workstream A (ID-7), stated exactly.** These are *demands on A*, not open nodes of this dossier.
> - **(O1)** Prove that \(\psi_n(nb_n)\) is the correct modulus for the factor's leakage into \(\widehat\mu^{(3)}_n\) — i.e. that the leading factor contribution to \(\log_{\mu_n}\widehat\mu_n^{(3)}\) is a weighted local average of the frozen factor scores, with weights summing to one, so that its \(L^2\) norm is \(\Theta(\psi_n(nb_n))\) up to the kernel's \(\|\lambda\|_1=5\) constant.
> - **(O2)** Because L-9.R3.6(1) rules out \(\psi_n(nb_n)=o(\ell_n)\), A must state which of the three dispositions holds for the leading leakage term: (α) it is mean-zero and enters the influence function (so the rate is unchanged but the asymptotic variance is not the oracle one); (β) it is removed by FRAME-2P-U's training/validation differencing; or (γ) it is budgeted as part of \(\zeta_n\) in the approximate-target loading numerator \(2A^0_{2,n}\bar d_n+\bar d_n^2\). Any ID-7 statement that asserts a clean separation without choosing one of these is false by L-9.R3.6(1).
> - **(O3)** ID-10 must record L-9.R3.6(3): under any positive memory exponent \(d>0\) the centre/factor separation is not first-order clean at any bandwidth, and the re-optimised exponent is \(3(1-2d)/(7-2d)\). This must be checked against HD-K (\(nb_n/\log n\to\infty\)) and HD-M (\(a\ge3/7\)): at \(d>0\), \(\alpha^\star<1/7\), so \(nb_n=n^{1-\alpha^\star}\) grows faster and HD-K is easier, while the requirement \(n^{-a}=O(b_n)\) becomes \(a\ge\alpha^\star\), also easier; the binding constraint is instead \(n^{-a}=o(\ell^\star_n)\), i.e. \(a>3(1-2d)/(7-2d)\).
> - **(O4)** ID-7's identification premise must be the declared band separation of Theorem R3-BAND, in primitive spectral terms, and must be labelled a convention (Theorem R3-BAND-NEC).

### 4.6 L-9.R3.7 — the logical status of ID-1 (false theorem, or true-but-non-binding?)

> **Proposition.** ID-1 as written in [[P1-ID — centre-drift and factor identification boundary]] §4 is **true**. Its second sentence is conditional: "every admissible representation *whose centre must be the unique Fréchet mean* has centre \(m_Q\)". A latent-centre representation does not satisfy the antecedent. Hence ID-1 is a **true theorem that is non-binding on \(\mathrm{LC}\setminus\mathrm{D}\)**: on that class it quantifies over the empty set. Moreover, by L-9.R3.0, no repair is possible within the campaign's information vocabulary: the antecedent cannot be weakened to any law-level condition that would make the conclusion about a random centre. Therefore the operative content of ID-1 is:
> \[
> \textbf{ID-1 identifies a convention's representative, not the scientific object.}
> \]

*Proof.* Truth: the proof in §4 of the canonical file is a two-line argument about equal objectives and is correct. Non-bindingness: §4.1–§4.3 exhibit LC representations, admissible under LC1–LC5, whose centres are not the marginal Fréchet mean; by L-9.R3.0 no law-level functional equals a nondegenerate \(C_u\). \(\square\)

**Status: PROVED.** **Classification: convention-induced.**

> **What P1-ID must be restated as, over the latent-centre class.**
> 1. **ID-1 gains an explicit scope declaration.** "Within the deterministic-centre class \(\mathrm D\) — \(C_t=\mu(u_t)\) a function of rescaled time, declared equal to the frozen marginal Fréchet mean — the centre is a marginal-law functional and is identified. Over the latent-centre class \(\mathrm{LC}\), no information set in §2 identifies the realised centre path (L-9.R3.0), and the marginal Fréchet mean equals \(\mathbb EC_u\) in flat geometry (L-9.R3.1) and does not equal \(\mathfrak M(\mathrm{Law}(C_u))\) in curvature (L-9.R3.2d)."
> 2. **A new node ID-1′ (latent-centre vacuity)** must be registered with the content of L-9.R3.0 and L-9.R3.7.
> 3. **ID-2 gains a hard scope lock:** conclusions (1)–(3) are proved on \(\mathrm D\) and are **FALSE** on \(\mathrm{LC}\) (L-9.R3.3b, Theorem R3-D). ID-2(4) survives and is strictly weaker than the full latent-centre reallocation group.
> 4. **Paper 1 "Identification preconditions" item 1** must be split into (α) determinism-in-rescaled-time and (β) centre-\(=\)-Fréchet-mean, with (β) labelled a normalisation and (α) labelled an untestable modelling convention whose scientific content is the frequency-band separation of Theorem R3-BAND.
> 5. **Paper 1 "Claims excluded"** must add: *"identification of the centre path or of the loading span when the baseline level is itself a latent stochastic process with serial dependence."*
> 6. **The Application map** must record that in the realised-covariance application the baseline volatility level is exactly the object at risk, so the convention is load-bearing there and must be displayed at the point of use.

---

# PART II — R5: sample-level non-uniqueness

## 5. Statement of the question and the split

Population uniqueness of \(\mathfrak M(Q)\) does not by itself give a unique or stable *empirical* argmin. The decisive question set by the lead: does the estimator's **localisation/fallback event** change the estimand? The relevant estimator conventions in this repository are:

- the signed local-polynomial mean is defined as \(\widehat\mu(u)=\arg\min\{\widehat F_u(q):q\in\bar B(\tilde\mu(u),\delta_0)\}\), and [[G1 audit — resolution of the uniform local Fréchet rate]] §6 states explicitly: *"This localisation is part of the estimator, not merely a proof device"*;
- the BW estimator constrains positive stage means to a declared compact strongly geodesically convex regular domain, runs a generated-domain membership test on every produced object, and triggers a deterministic full-rank fallback; [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]] §1 states: *"The fallback is asymptotically inactive relative to this constrained estimator on its regular event. No equality with the original unconstrained global argmin is claimed."*

The answer is a clean dichotomy, decided by geodesic convexity.

## 6. L-9.R5.1 — the strongly convex class: probability-one uniqueness, and proved separation

> **Theorem L-9.R5.1.** Let \(D\) be either (i) a Hadamard manifold \(M\) (the class declared by HD-G), or (ii) a compact strongly geodesically convex subset of a complete manifold on which \(\operatorname{Hess}\tfrac12d(\cdot,z)^2\succeq\lambda\,\mathrm{Id}\) for every \(z\) in the a.s. support, with \(\lambda>0\) (the class declared by BW-FIXED-MARGIN §2 and by HD-G's "Hessian of one-half squared distance bounded below by \(I\)"). Let \(x_1,\dots,x_n\in D\) and \(w_1,\dots,w_n>0\). Then:
> 1. \(\widehat F(q)=\sum_iw_id(q,x_i)^2\) is \(2\lambda\sum_iw_i\)-strongly geodesically convex on \(D\); hence \(\operatorname*{argmin}_{q\in D}\widehat F\) is a **singleton for every realisation** — a deterministic statement, with no exceptional event and no rate.
> 2. The same applies to \(F_Q\) restricted to \(D\); if in addition \(Q(D)=1\) and \(D=M\) is Hadamard, the population argmin is a global singleton.
> 3. Consequently the localisation constraint \(q\in\bar B(\tilde\mu(u),\delta_0)\) (or \(q\in D\)) never has to break a tie: on the event \(\{\arg\min_{D}\widehat F\in\operatorname{int}\bar B(\tilde\mu(u),\delta_0)\}\), which has probability \(1-o(1)\) under the declared SW-AS package, the localised estimator equals the \(D\)-restricted argmin, and the localisation is *inactive as a selector*, not merely asymptotically negligible.
> 4. Under the additional condition \(F_Q(m)<\inf_{M\setminus D}F_Q\) with \(m=\arg\min_DF_Q\in\operatorname{int}D\), the \(D\)-restricted population argmin **equals** the global argmin \(\mathfrak M(Q)\), so the estimand of the constrained estimator is the ID-1 estimand.

*Proof.* (1) For \(K\le0\) or on a strongly convex domain with the stated Hessian bound, \(q\mapsto\tfrac12d(q,z)^2\) is \(\lambda\)-strongly geodesically convex (L-9.R3.2a(ii) for the Hadamard case; the Hessian bound is the hypothesis in case (ii)). A positive combination of \(\lambda\)-strongly convex functions with weights \(w_i\) is \(\lambda\sum w_i\)-strongly convex; a strongly convex function on a geodesically convex set has at most one minimiser, and existence follows from compactness (case (ii)) or coercivity (case (i)). No probabilistic input is used, so the conclusion holds pathwise. (2) Same argument with \(Q\) in place of the empirical measure. (3) On that event the constraint is not binding and the two argmins coincide by (1). (4) Immediate. \(\square\)

**Status: PROVED.** **Classification of the *absence* of failure: this is the corrected theorem, and the feature removed is exactly the possibility of a second minimising branch.**

> **Corollary (R5 is an estimation node on the declared class).** On the class of L-9.R5.1, empirical non-uniqueness has probability **zero**, not \(o(1)\); the localisation/fallback event does not change the estimand; and R5 does not interact with the identification boundary. \(\square\)

## 7. L-9.R5.5 — the formal dependency separation

The lead's standard requires a formal dependency argument, not an assertion. Here it is.

> **Proposition L-9.R5.5.** Let \(\mathcal C\) be the set of consumers of the identification theorems, i.e. the statements whose proofs cite ID-1: P1-ID §§4–9 (ID-1 through ID-6), Paper 1 "Identification preconditions" items 1–6, Paper 1 §"Scientific role", the Analytical-reconstruction P1-ID terminal register, and the Application map. Let \(\mathcal E\) be the set of estimator conventions: the localisation ball \(\bar B(\tilde\mu(u),\delta_0)\) of G1-LP, the declared compact strongly geodesically convex regular domain of the BW estimator, the generated-domain membership test, and the deterministic fallback. Then:
> 1. **No element of \(\mathcal C\) quantifies over \(\mathcal E\).** ID-1's statement is \(\mathfrak M(Q)=\operatorname*{argmin}_{x\in M}F_Q(x)\), an unconstrained population argmin; ID-2 through ID-5 are population statements about \(\Gamma_X(h)\), chart changes, and lag rows; Paper 1's preconditions are stated for the frozen marginal objective. Hence the identification theorems remain literally unchanged if every element of \(\mathcal E\) is deleted.
> 2. **The converse direction is where the dependency lives.** The estimator's estimand is \(\arg\min_{q\in D}F_{Q_u}(q)\). By L-9.R5.1(4), this equals the ID-1 estimand **iff** \(\arg\min_DF_{Q_u}\in\operatorname{int}D\) and \(F_{Q_u}\) has no lower value outside \(D\). This is a proposition about the population law and the declared \(D\), not about the sample.
> 3. Therefore the separation is: *identification does not read the estimator; the estimator reads identification through one displayed containment condition.* If that condition is displayed, R5 is an estimation node. If it is not displayed, the defect is an estimation-consistency defect (the estimator targets a different population functional), still not an identification defect.

**Status: REFORMULATED+PROVED, with one scope lock.**

> **SCOPE LOCK R5-L1 (obligation on the lead, to be executed in the canonical files).** Paper 1 and P1-ID must display, at the point where the constrained estimator is introduced: *"the declared domain \(D\) is assumed to contain the population Fréchet mean of every frozen marginal in its interior, and \(F_{Q_u}(m_u)<\inf_{M\setminus D}F_{Q_u}\); under this condition the constrained estimand equals the ID-1 estimand."* Without the lock, BW-FIXED-MARGIN §1's honest disclaimer ("no equality with the original unconstrained global argmin is claimed") leaves the estimand unpinned.

## 8. The exact examples that show why the separation needs a margin

The examples below live on \(S^1\) with its unit geodesic metric — a complete manifold with nonempty cut locus and positive curvature. This is deliberately outside L-9.R5.1's class, and it is in the parent's scope: [[P1-ID — centre-drift and factor identification boundary]] §2 and the R2 route both list the parent's sphere products; the BW cone is nonnegatively curved (it is a Riemannian submersion image of a flat space, so O'Neill gives \(K\ge0\)) and is explicitly **not** globally Hadamard.

### 8.1 L-9.R5.2 — population argmin singleton, empirical argmin non-unique with positive probability

> **Construction.** \(M=S^1\), angle coordinate, \(d(\theta,\phi)=\min(|\theta-\phi|\bmod2\pi,\,2\pi-|\theta-\phi|\bmod2\pi)\). Let
> \[
> Q=p\,\delta_{0}+p\,\delta_{\pi}+w\,\delta_{\pi/2},\qquad w=1-2p,\quad 0<p<\tfrac12 .
> \]
>
> **Population.** On the upper arc \(\theta\in[0,\pi]\), \(F_Q(\theta)=p\theta^2+p(\pi-\theta)^2+w(\theta-\pi/2)^2\), so \(F_Q'(\theta)=2(2p+w)(\theta-\pi/2)=2(\theta-\pi/2)\): the unique upper-arc minimiser is \(\pi/2\) with \(F_Q(\pi/2)=p\pi^2/2\). On the lower arc \(\theta=\pi+s\), \(s\in[0,3\pi/4]\), \(F_Q'=2\big[s+\pi(\tfrac12-2p)\big]\), so for \(p<\tfrac14\) the lower arc has no interior critical point and its infimum is at \(s=0\), where \(F_Q(\pi)=p\pi^2+w\pi^2/4>p\pi^2/2\); on \(s\in[3\pi/4,\pi]\), \(F_Q'=2[s+2p\pi-3\pi/2]<0\) for \(p<3/8\), and \(F_Q(0)=p\pi^2+w\pi^2/4>F_Q(\pi/2)\). Hence
> \[
> \mathfrak M(Q)=\{\pi/2\}\quad\text{is a singleton for }0<p<\tfrac14 .
> \]
> The two candidate points \(\pi/2\) and \(3\pi/2\) are separated by the value margin \(F_Q(3\pi/2)-F_Q(\pi/2)=w\pi^2>0\).
>
> **Sample.** Draw \(X_1,\dots,X_n\) i.i.d. \(\sim Q\) with empirical weights \((\hat p_0,\hat p_1,\hat w)\). \(\widehat F\) is invariant under the reflection \(\sigma(\theta)=-\theta\) (which fixes \(0\) and \(\pi\)) **exactly when \(\hat w=0\)**; on that event, if additionally \(\hat p_0=\hat p_1\), the empirical objective is \(\tfrac12 d(\cdot,0)^2+\tfrac12 d(\cdot,\pi)^2\), whose argmin is the two-point set \(\{\pi/2,3\pi/2\}\) (this is exactly C-4). Hence
> \[
> \mathbb P\big(\widehat{\mathfrak M}_n\text{ is not a singleton}\big)
> \;\ge\;\mathbb P(\hat w=0,\ \hat p_0=\hat p_1)
> \;=\;(1-w)^{n}\binom{n}{n/2}2^{-n}\quad(n\text{ even}),
> \]
> which for \(p=1/4\), \(n=2\) equals \(2\cdot(1/4)(1/4)=1/8>0\), and in general is \(\asymp(1-w)^n(\pi n/2)^{-1/2}\): **exponentially small, but never zero at finite \(n\).**

**Status: PROVED.** **Classification: cut-locus-specific / positive-curvature-specific.** The mechanism is that \(0\) and \(\pi\) are antipodal, so \(d(\cdot,0)^2+d(\cdot,\pi)^2\) is constant-ish with two symmetric minima; in a Hadamard manifold the same law has a strictly convex objective and a pathwise unique empirical argmin (L-9.R5.1).

> **Corrected theorem removing exactly this feature.** *If the a.s. support of \(Q\) lies in a geodesic ball of radius \(<\pi/4\) on \(S^1\) (more generally, in a strongly convex ball with the Karcher/Kendall radius bound), then \(\widehat F\) is strongly geodesically convex on that ball and the empirical argmin is pathwise unique.* This is L-9.R5.1(ii) applied to the ball; the radius bound removes exactly the cut-locus/antipodality feature. **Status: PROVED.**

### 8.2 L-9.R5.3 — a degenerating margin makes the empirical mean flip branches with probability \(\to1/2\)

The previous example has exponentially small instability *because* the margin is fixed. The next one degenerates the margin and shows the separation is not free.

> **Construction.** \(M=S^1\). Fix \(a\neq b\) with \(a+b<1\) (breaking the reflection across the \(\pi/2\)–\(3\pi/2\) axis) and \(c>0\). For \(\delta_n>0\) let
> \[
> Q_n=a\,\delta_0+b\,\delta_\pi+(c+\delta_n)\,\delta_{\pi/2}+(c-\delta_n)\,\delta_{3\pi/2},
> \qquad a+b+2c=1 .
> \]
> Let \(\sigma(\theta)=-\theta\), the reflection fixing \(0\) and \(\pi\) and swapping \(\pi/2\leftrightarrow3\pi/2\).
>
> **(P1) Exact symmetry identity.** For any weights \((\hat a,\hat b,\hat c_1,\hat c_2)\) and any \(\theta\),
> \[
> \widehat F(\theta)-\widehat F(\sigma\theta)=(\hat c_1-\hat c_2)\big[d(\theta,\pi/2)^2-d(\theta,3\pi/2)^2\big].
> \]
> *Proof:* \(\sigma\) fixes \(0\) and \(\pi\) and swaps the other two atoms, and \(d(\sigma\theta,x)=d(\theta,\sigma x)\). \(\square\)
>
> **(P2) Branch selection is exactly the sign of \(\hat c_1-\hat c_2\).** If \(\hat c_1>\hat c_2\), then every global minimiser of \(\widehat F\) lies in the closed upper half \(\{d(\theta,\pi/2)\le d(\theta,3\pi/2)\}\); if \(\hat c_1<\hat c_2\), in the closed lower half. *Proof:* if \(\hat c_1>\hat c_2\) and \(\hat\theta\) is a global minimiser with \(d(\hat\theta,\pi/2)>d(\hat\theta,3\pi/2)\), then (P1) gives \(\widehat F(\sigma\hat\theta)<\widehat F(\hat\theta)\), a contradiction. \(\square\)
>
> **(P3) Population.** For \(\delta_n>0\), \(\mathfrak M(Q_n)\) is a **singleton** in the open upper half, at \(\hat\theta_n\to\theta^\star\) as \(\delta_n\to0\), where \(\theta^\star\) is the upper member of the mirror pair \(\{\theta^\star,\sigma\theta^\star\}\) that constitutes \(\mathfrak M(Q_\infty)\) for the tied law \(\delta_n=0\). Its value margin over the mirror local minimum is exactly
> \[
> F_{Q_n}(\sigma\theta_n)-F_{Q_n}(\theta_n)=2\delta_n\big[d(\theta_n,3\pi/2)^2-d(\theta_n,\pi/2)^2\big]=\kappa\delta_n+o(\delta_n),\ \ \kappa>0,
> \]
> by (P1) with \(\hat c_1-\hat c_2=2\delta_n\). Uniqueness for \(\delta_n>0\) is (P2) applied at the population weights together with the fact that the tied law's argmin is exactly the mirror pair (its objective is \(\sigma\)-invariant and its two upper-half local minima are separated because \(a\ne b\)).
>
> **(P4) Empirical instability.** Let \(n_1,n_2\) be the counts of the atoms \(\pi/2,3\pi/2\). By (P2), the empirical argmin lies in the upper half iff \(n_1>n_2\), in the lower half iff \(n_1<n_2\), and is a \(\sigma\)-mirror pair (hence **non-unique**) iff \(n_1=n_2\) and the common argmin is off the axis \(\{0,\pi\}\) — which holds on a neighbourhood of the population weights by continuity of \(\widehat F\) in the weights and the strict gap \(\min_\theta F_{Q_\infty}<\min\{F_{Q_\infty}(0),F_{Q_\infty}(\pi)\}\). Therefore:
> \[
> \mathbb P\big(\widehat{\mathfrak M}_n\text{ non-singleton}\big)\;\asymp\;\mathbb P(n_1=n_2)\;\asymp\;(4\pi nc)^{-1/2},
> \]
> by the local CLT for \(n_1-n_2\) (variance \(\asymp 2nc\)); and if \(\delta_n=o(n^{-1/2})\), then \(n_1-n_2\) has mean \(2n\delta_n=o(\sqrt n)\) and standard deviation \(\asymp\sqrt{2nc}\), so
> \[
> \mathbb P\big(\widehat{\mathfrak M}_n\subseteq\text{lower half}\big)\longrightarrow\tfrac12 ,
> \]
> while \(\mathfrak M(Q_n)\) is a singleton in the upper half for every \(n\). On that event \(d(\widehat\mu_n,\mathfrak M(Q_n))\to d(\sigma\theta^\star,\theta^\star)>0\), a **fixed positive distance**.
>
> **(P5) Contrast with a fixed margin.** If \(\delta_n\equiv\delta>0\), then \(\mathbb P(n_1\le n_2)\) is exponentially small by Hoeffding, and non-uniqueness has probability \(\asymp n^{-1/2}\) only in the exactly-tied design.

**Status: PROVED.** *(Numerical sanity check, no status: with \(a=0.28\), \(b=0.32\), \(c=0.2\), the tied law has argmin \(\{2.26195,4.02124\}\) — exactly two tied points; \(\delta>0\) selects \(2.199\) and \(\delta<0\) selects its mirror \(4.084\); the margin/\(\delta\) ratio converges to \(2[d(\theta^\star,3\pi/2)^2-d(\theta^\star,\pi/2)^2]=11.05\), matching (P3).)*

**Classification: cut-locus-specific + convention-induced.** The instability requires (i) a nonconvex objective, which requires positive curvature or a cut locus, and (ii) a vanishing margin. Feature (i) is removed exactly by L-9.R5.1; feature (ii) is removed exactly by the uniform-margin hypothesis below.

> **Corrected theorem removing exactly the margin feature.** *Let \(D\) be compact and let \(F_{Q_n}\) have a unique minimiser \(m_n\in\operatorname{int}D\) with a **uniform** margin: there are \(\lambda>0\) and \(\varrho>0\), independent of \(n\), with \(\operatorname{Hess}F_{Q_n}\succeq\lambda\,\mathrm{Id}\) on \(\bar B(m_n,\varrho)\subseteq D\) and \(\inf_{D\setminus B(m_n,\varrho)}F_{Q_n}\ge F_{Q_n}(m_n)+\varsigma\) for a fixed \(\varsigma>0\). Suppose \(\sup_{q\in D}|\widehat F_n(q)-F_{Q_n}(q)|=o_p(\min(\varsigma,\lambda\varrho^2))\) (which the project's SW-AS/Sturm concentration supplies). Then with probability \(1-o(1)\) every empirical minimiser lies in \(B(m_n,\varrho)\), where \(\widehat F_n\) is \(\lambda/2\)-strongly convex on the same event; hence the empirical argmin is a singleton on an event of probability \(1-o(1)\) and \(d(\widehat m_n,m_n)\to0\).* Proof: the uniform-value-margin bound confines the argmin to the ball; on the ball, uniform closeness of the Hessians (SW-AS S1–S5) transfers strong convexity; strong convexity gives uniqueness. \(\square\) **Status: PROVED.** L-9.R5.3 shows the uniform margin is not removable: with \(\varsigma_n=\kappa\delta_n\to0\) faster than \(n^{-1/2}\), the conclusion fails with probability \(\to1/2\).

### 8.3 L-9.R5.4 — the data-dependent localisation is a **randomised selector**

This is the exact sense in which the localisation convention can become part of the identification, and it terminates the "identification node" branch.

> **Theorem L-9.R5.4.** Suppose \(\mathfrak M(Q)=\{m^{(1)},m^{(2)}\}\) with \(m^{(1)}\ne m^{(2)}\) (or, in the triangular array, suppose the margin \(\varsigma_n\) satisfies \(\varsigma_n=o(n^{-1/2})\) as in L-9.R5.3). Let the estimator be \(\widehat\mu=\arg\min\{\widehat F(q):q\in\bar B(\tilde\mu,\delta_0)\}\) with \(\tilde\mu\) a preliminary estimator computed from the same or a different sample, and \(\delta_0<\tfrac12d(m^{(1)},m^{(2)})\). Then:
> 1. \(\widehat\mu\) converges to \(m^{(j)}\) on the event \(\{\tilde\mu\in\bar B(m^{(j)},\delta_0/2)\}\), \(j=1,2\);
> 2. if both events have probability bounded away from \(0\) and \(1\) — which L-9.R5.3(P4) exhibits explicitly with limiting probabilities \(1/2,1/2\) — then \(\widehat\mu\) has no deterministic limit, and the "estimand" of the localised estimator is a **random element of \(\mathfrak M(Q)\)**;
> 3. hence the localisation is not a measurable selector in the sense of L-9.R2.3 (which asks for a deterministic law-functional selector): it is a *randomised* selector whose randomisation is driven by the data, so the induced target is not a functional of \(Q\) at all;
> 4. consequently the identification statement that must be made is: *over the nonsingleton-argmin class, the constrained estimator has no population estimand; a deterministic selection convention must be declared before the estimator is defined, and then the declared convention — not the localisation — is the identifying object.*

*Proof.* (1) is L-9.R5.1(1) applied inside the ball once the ball contains exactly one element of \(\mathfrak M(Q)\) and \(\widehat F\to F_Q\) uniformly. (2)–(3) follow because a functional of \(Q\) is deterministic (L-9.R3.0) while \(\widehat\mu\) has a nondegenerate limit distribution over \(\{m^{(1)},m^{(2)}\}\). (4) restates (2)–(3). \(\square\)

**Status: PROVED.** **Classification: convention-induced (randomisation of a selector) on the nonsingleton class; the underlying nonsingleton-ness is cut-locus/positive-curvature-specific.**

## 9. R5 terminal verdict

> **R5 terminates as a two-branch statement, both branches terminal.**
>
> **(R5-A) On the class declared by HD-G and BW-FIXED-MARGIN §2 — Hadamard, or a compact strongly geodesically convex regular domain with \(\operatorname{Hess}\tfrac12d(\cdot,z)^2\succeq\lambda\,\mathrm{Id}\) and a uniform value margin: OUT OF SCOPE BY PROVED SEPARATION.** The separation is formal, not asserted: (a) L-9.R5.1 gives pathwise (probability-one) uniqueness of both population and empirical argmins, so the localisation never selects a branch; (b) L-9.R5.1(4) plus §8.2's corrected theorem give the exact conditions under which the population argmin is a singleton with a positive Hessian margin and the empirical argmin is unique on a \(1-o(1)\) event inside the declared domain; (c) L-9.R5.5 proves by inspection of the dependency graph that no consumer of ID-1–ID-6 quantifies over any estimator convention. The separation carries **SCOPE LOCK R5-L1**, which is an obligation on the lead, not an open node.
>
> **(R5-B) Off that class — the parent's sphere products and the nonnegatively curved BW cone outside a declared strongly convex domain: IDENTIFICATION NODE.** The exact statement is L-9.R5.4: on the nonsingleton (or \(o(n^{-1/2})\)-margin) class the data-dependent localisation is a randomised selector, the localised estimator has no population estimand, and a deterministic selection convention must be declared *before* the estimator and becomes part of the identification. L-9.R5.2 and L-9.R5.3 supply the exact examples, including the required "population singleton, empirical non-singleton" witness and the \(\Omega(1)\) branch-flip witness that shows the margin is not removable.
>
> R5-B does **not** overlap R2 (owned by B): R2 asks whether a *deterministic measurable selector* exists and what it costs; R5-B proves that the estimator as currently specified does not implement any deterministic selector at all. The two must be merged by the lead into a single canonical statement.

---

## 10. Node register — every node terminal

| Node | Content | Terminal status | Location |
|---|---|---|---|
| L-9.R3.0 | law functionals are deterministic; no information set identifies a random centre | PROVED | §2.1 |
| L-9.R3.1 | flat: \(\mathfrak M(Q)=\{\mathbb EC\}\); equals realised \(C\) iff \(C\) degenerate; sharpened hypothesis | PROVED | §2.2 |
| L-9.R3.2a | Hadamard: Cartan–Hadamard, Hessian comparison, Sturm uniqueness, CN inequality | CITED+APPLIED | §2.3.1 |
| L-9.R3.2b | equal-weight two-point Fréchet mean is the midpoint | PROVED | §2.3.2 |
| L-9.R3.2c | exact IFT reduction \(m_2=\frac14H^{-1}D^2E(0)[u,u]\) | PROVED | §2.3.4 |
| L-9.R3.2d | exact \(H^2\) closed form; \(m(s)\ne m_0\) for **all** \(s>0\); \(m_2>0\) along \(\hat w\) | PROVED | §2.3.5 |
| L-9.R3.2e | curvature attribution \(m_2=-\frac K6H^{-1}w^\perp+O(\|w\|^3)\); consistency with R3.2d | CITED+APPLIED (expansion) / PROVED (check) | §2.3.6 |
| L-9.R3.2f | flat certificate: \(m(s)\equiv m_0\) exactly | PROVED | §2.3.6 |
| L-9.R3.2g | single-fixed-point isometry class is sufficient | PROVED | §2.4.1 |
| L-9.R3.2h | exact characterisation via the \(\nu\)-averaged curvature defect; symmetry not necessary (3 witnesses) | PROVED | §2.4.2 |
| L-9.R3.3-mar-flat / -curved | marginal-equivalent latent-centre models, different centres and loadings | PROVED | §3 |
| L-9.R3.3a | cheap FDD version; audit of which precondition rules it out; (α) vs (β) verdict | PROVED / (α) DISPROVED as identifying, REFORMULATED+PROVED as convention | §4.1 |
| L-9.R3.3b | non-trivial FDD version, incomparable loading ranges, active reallocated dynamics | PROVED | §4.2 |
| L-9.R3.3c | curved \(H^2\times H^2\) version, exact, covariantly constant loadings | PROVED | §4.3 |
| L-9.R3.3d (R3-D) | every subspace of every dimension is an admissible loading range | PROVED | §4.4 |
| L-9.R3.4 (R3-SURV) | surviving quotient = the observed law; ID-2(1)–(3) FALSE on LC; no-go corollary | PROVED | §4.4 |
| L-9.R3.5 (R3-BAND / -NEC) | declared centre-free band restores identification; necessary on the uniformly-pd class | PROVED | §4.5 |
| L-9.R3.6 | \(\psi_n(nb_n)=o(\ell_n)\) impossible for \(d\ge0\); re-optimised \(\alpha^\star=(1-2d)/(7-2d)\) | PROVED | §4.5.1 |
| L-9.R3.7 | ID-1 is true-but-non-binding, not false; exact restatement list | PROVED | §4.6 |
| L-9.R5.1 | strong convexity ⇒ pathwise unique empirical argmin; localisation not a selector | PROVED | §6 |
| L-9.R5.2 | population singleton, empirical non-singleton with positive probability | PROVED | §8.1 |
| L-9.R5.3 | degenerating margin ⇒ branch flip with probability \(\to1/2\); non-uniqueness rate \(n^{-1/2}\) | PROVED | §8.2 |
| L-9.R5.4 | data-dependent localisation is a randomised selector; no population estimand | PROVED | §8.3 |
| L-9.R5.5 | formal dependency separation + SCOPE LOCK R5-L1 | REFORMULATED+PROVED | §7 |

No node in this dossier is deferred, and no assumption introduced above is stated in non-primitive terms: every new hypothesis is a spectral support condition, a Hessian/convexity bound, a support/radius condition, or an independence/centring condition.

## 11. Objections this dossier anticipates against itself

| # | Objection | Test | Disposition |
|---|---|---|---|
| C-1 | "L-9.R3.3b is just renaming a factor coordinate as a centre." | The two loading ranges are **incomparable** (§4.2) and in §4.3 **orthogonal**; no \(R\in GL(r)\) relates them, and the reallocated component carries nonzero-lag covariance, which C-7 proved cannot be moved between factor and noise. | **REJECTED.** The reallocation channel is new, and Theorem R3-D shows it is not a finite list of relabellings but the full subspace lattice. |
| C-2 | "The \(H^2\) example is a small-\(s\) expansion dressed as a theorem." | L-9.R3.2d is a closed-form computation valid for all \(\beta>0,s>0\); the expansion appears only in the *interpretation* (L-9.R3.2e) and is independently verified against the closed form. | **REJECTED.** |
| C-3 | "Latent centres are excluded by Paper 1's model, so R3 attacks a straw man." | Correct that they are excluded — §4.1 identifies exactly which declaration excludes them, and proves (Theorem R3-D) that the declaration is untestable. The attack is on the *status* of the exclusion, not on its existence. | **SUSTAINED AS REFRAMING:** the verdict is "true-but-non-binding", not "false". |
| C-4 | "R3's curved example (§4.3) uses a product manifold, which is a cheat." | \(H^2\times H^2\) is Hadamard, the support is not contained in any flat, and Paper 1's covariant-constancy requirement is met exactly rather than approximately. SPD(2) with AIRM is isometric to \(\mathbb R\times H^2\), so the same device is available in the project's own geometry. | **REJECTED**, with the note that the mechanism is universal and the curved version is a non-artefact certificate, not the source of the failure. |
| C-5 | "R5-A's separation is asserted." | §7 enumerates the consumer set and shows the estimator conventions appear in none of their statements; §6 gives pathwise, not asymptotic, uniqueness. | **REJECTED**, subject to SCOPE LOCK R5-L1. |
| C-6 | "R5's \(S^1\) examples are irrelevant because HD-G declares Hadamard." | The parent's data live on sphere products and the BW cone is \(K\ge0\), not Hadamard; both are in the repository's declared application scope. | **REJECTED**; this is precisely why R5 splits rather than separating outright. |
