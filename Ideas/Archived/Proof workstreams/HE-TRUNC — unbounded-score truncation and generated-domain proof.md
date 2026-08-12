---
type: working-proof-dossier
title: HE-TRUNC — unbounded-score truncation and generated-domain proof
status: internal-hostile-audit-passed
authority: noncanonical-until-integrated
last-audited: 2026-08-09
---

# HE-TRUNC — unbounded-score truncation and generated-domain proof

> This dossier closes the exact HE-TRUNC obligation by one explicit route: deterministic expanding convex-domain clipping plus tail transfer. It does not claim minimal moments. The proof never conditions the original array on the no-clipping event; it proves concentration for separately clipped variables and transfers back on an event where the two arrays coincide.

## 0. Verdict

The bounded-tail HE theorem extends to unbounded observations when deterministic clipping levels and expanding generated domains satisfy explicit escape, score-tail, product-tail, dependence, and margin conditions. The final rates are the bounded-tail rates with:

1. truncated score-concentration budgets in place of bounded-score budgets;
2. an additive population score bias \(b_{S,n}(T_n)\) in every mean rate;
3. an additive direct-sum target bias \(\sqrt{h_{0,n}}b_{W,n}(T_n)\) in the lag-row rate; and
4. all geometry constants evaluated on the expanding deterministic domain.

The theorem is nonempty. Uniform sub-Weibull tails permit \(T_n=K_n\{c\log N_n\}^{1/\alpha}\), \(c>1\), with explicit incomplete-gamma tail integrals. The result is **PROVED UNDER EXPLICIT ASSUMPTIONS**, subject to the hostile audit in Section 8.

## 1. Deterministic clipping construction

For each \(n\), let

\[
\mathcal C_n(T_n)\subset\mathcal T_n(T_n)
\]

be closed geodesically convex sets in a Hadamard manifold, with margin

\[
\delta_n(T_n)
=\inf\{d(x,y):x\in\mathcal C_n(T_n),\ y\notin\mathcal T_n(T_n)\}>0.
\tag{1.1}
\]

Let \(\Pi_{n,T_n}\) be metric projection onto \(\mathcal C_n(T_n)\). Projection is single-valued and nonexpansive for closed convex subsets of a Hadamard space. Define, for every actual and stationary/local-proxy endpoint consumed by the proof,

\[
X_{t,n}^{[T_n]}=\Pi_{n,T_n}X_{t,n}.
\tag{1.2}
\]

At the true anchor tangent space define radial Hilbert clipping

\[
P_Ty=y\min(1,T/\|y\|),
\qquad
Y_{t,n}^{[T_n]}=P_{T_n}Y_{t,n}.
\tag{1.3}
\]

The map \(P_T\) is the metric projection onto the Hilbert ball and is nonexpansive. Observation clipping and tangent clipping are separate analytical devices. They need not define the same modified population law; both equal the original sample on the simultaneous no-clipping event below.

Assume the true centre curve lies in \(\mathcal C_n(T_n)\), every clipped population stage barycentre lies there by convexity, and connectors from original population stages to clipped stages lie in \(\mathcal T_n(T_n)\). Assume all score/Hessian, Richardson, blend, chord, connector, parallel-transport, and ruled-surface bounds used below hold on \(\mathcal T_n(T_n)\), with the displayed \(T_n\)-dependent constants. These are expanding-domain versions of HE-G0; they are not consequences of tail decay.

Let \(N_{X,n}\) be the number of actual/proxy endpoints and \(N_{Y,n}\) the number of tangent endpoints in all retained empirical rows. Define

\[
\pi_{X,n}(T)
=\sup_{t,\mathrm{proxy}}P\{X_{t,n}\notin\mathcal C_n(T)\},
\qquad
\pi_{Y,n}(T)=\sup_tP\{\|Y_{t,n}\|>T\}.
\tag{1.4}
\]

The simultaneous equality event

\[
\mathcal E_{n,T}
=\{X_{t,n}=X_{t,n}^{[T]}\text{ for every consumed endpoint},
\ Y_{t,n}=Y_{t,n}^{[T]}\text{ for every retained row endpoint}\}
\tag{1.5}
\]

satisfies the unconditional union bound

\[
P(\mathcal E_{n,T}^c)
\le N_{X,n}\pi_{X,n}(T)+N_{Y,n}\pi_{Y,n}(T).
\tag{1.6}
\]

Thus \(P(\mathcal E_{n,T_n})\to1\) whenever the right side tends to zero. The dependent array is never conditioned on this event.

## 2. Exact tail integrals and population biases

For a nonnegative random variable \(Z\), define

\[
\mathfrak t_{r,Z}(T)^r
=E\{Z^r\mathbf1(Z>T)\}
=T^rP(Z>T)+r\int_T^\infty x^{r-1}P(Z>x)\,dx.
\tag{2.1}
\]

Every tail term below is of this form.

### 2.1 Score bias

For every deterministic original stage population point \(q=q_{j,\pm,n}(u)\), define

\[
b_{S,n}(T)
=\sup_{u,j,\pm}
\left\|
E\{\log_qX_{t,n}-\log_qX_{t,n}^{[T]}\}
\right\|.
\tag{2.2}
\]

If the observation-variable Log map is \(L_{\log,n}(T)\)-Lipschitz on every pair joining \(x\) to \(\Pi_{n,T}x\), then

\[
b_{S,n}(T)
\le L_{\log,n}(T)
\sup_{t,\mathrm{proxy}}E\,d\{X_{t,n},\mathcal C_n(T)\}.
\tag{2.3}
\]

The expectation is the \(r=1\) tail integral of distance from the good domain.

Let \(z_{j,\pm,n}(u)\) and \(z_{j,\pm,n}^{[T]}(u)\) be the original and clipped population stage barycentres. If the clipped population Hessian is at least \(\kappa_n(T)I\) along their connector, the Karcher score equation and (2.2) give

\[
d\{z_{j,\pm,n}(u),z_{j,\pm,n}^{[T]}(u)\}
\le \kappa_n(T)^{-1}b_{S,n}(T).
\tag{2.4}
\]

Therefore the three-scale Richardson population expansion acquires at most

\[
L_{\mathcal R,n}(T)\kappa_n(T)^{-1}b_{S,n}(T)
\tag{2.5}
\]

in addition to the original third-order bias, local-stationarity, and design terms.

### 2.2 Product bias

Define

\[
b_{W,n}(T)
=\max_{h\le h_{0,n}}
E\left\|
Y_{t,n}\otimes Y_{t-h,n}
-Y_{t,n}^{[T]}\otimes Y_{t-h,n}^{[T]}
\right\|_{\rm HS}.
\tag{2.6}
\]

Let \(M_{2,n}=\sup_t\|Y_{t,n}\|_{L^2}\) and

\[
\tau_{2,Y,n}(T)
=\sup_t\left[
E\{\|Y_{t,n}\|^2\mathbf1(\|Y_{t,n}\|>T)\}
\right]^{1/2}.
\tag{2.7}
\]

Using
\(a\otimes b-a^T\otimes b^T=(a-a^T)\otimes b+a^T\otimes(b-b^T)\),
radial clipping, and Cauchy–Schwarz gives

\[
\boxed{b_{W,n}(T)\le2M_{2,n}\tau_{2,Y,n}(T).}
\tag{2.8}
\]

Hence the direct-sum population lag-row change is at most

\[
\zeta_{{\rm trunc},n}(T)
\le\sqrt{h_{0,n}}\,b_{W,n}(T).
\tag{2.9}
\]

This target change is paid whether the goal is the actual untruncated loading space or the ideal clean factor space.

## 3. Truncated score concentration

Let

\[
S_{t,j,u}^{[T]}
=\log_{z_j^{[T]}(u)}X_{t,n}^{[T]}
-E\log_{z_j^{[T]}(u)}X_{t,n}^{[T]}.
\tag{3.1}
\]

Assume either:

1. the clipped score row is \(m_n^S\)-dependent; or
2. it is a causal Hilbert Bernoulli shift with clipped Hilbert physical-dependence budgets \(\Theta_{S,2,n}^{[T]}\) and \(\Theta_{S,\infty,n}^{[T]}\).

For finite memory, measurable clipping preserves the dependence range. For causal physical dependence, the clipped **score** budgets are explicit assumptions: manifold projection followed by Log may multiply a coupled difference by \(L_{\log,n}(T)\). Only the Hilbert radial projection used for \(Y^{[T]}\) is automatically nonexpansive.

Let

\[
\sigma_{S,n}^{[T]}
=\sup_{t,j,u}\|S_{t,j,u}^{[T]}\|_{L^2},
\qquad
B_{S,n}^{[T]}
=\sup_{t,j,u}\|S_{t,j,u}^{[T]}\|_\infty.
\tag{3.2}
\]

Assume the parallel-trivialised clipped score has deterministic \(u\)-modulus
\(D_{S,n}(T)|u-v|/b_n\), and that the corresponding one-dimensional interpolation grid has polynomial cardinality. The finite-memory Hilbert second-moment and bounded-difference proof, or the canonical Hilbert physical-dependence proof, gives

\[
\left\|\sum_tw_t(u)S_{t,j,u}^{[T]}\right\|_{L^2}
\le
{C\Theta_{S,2,n}^{[T]}\over\sqrt{nb_n}},
\tag{3.3}
\]

\[
\sup_u\left\|\sum_tw_t(u)S_{t,j,u}^{[T]}\right\|
=O_p\!\left(
\Theta_{S,\infty,n}^{[T]}
\sqrt{\frac{\log n}{nb_n}}
\right).
\tag{3.4}
\]

For finite memory one may take

\[
\Theta_{S,2,n}^{[T]}
\le C\sqrt{2m_n^S+1}\,\sigma_{S,n}^{[T]},
\qquad
\Theta_{S,\infty,n}^{[T]}
\le C(m_n^S+1)B_{S,n}^{[T]}.
\tag{3.5}
\]

On \(\mathcal E_{n,T}\), the original empirical stage criterion equals the clipped empirical criterion. Equations (2.4), (3.3), and (3.4) therefore transfer the clipped-stage theorem to the original estimator without conditioning the row.

## 4. Mean and generated-domain theorem

Define

\[
\begin{aligned}
r_{\mu,n}^{[T]}
:={L_{\mathcal R,n}(T)\over\kappa_n(T)}
\bigg\{&
B_{3,n}(T)b_n^3+b_{S,n}(T)
{\Theta_{S,2,n}^{[T]}\over\sqrt{nb_n}}\\
&+L_{{\rm LS},n}(T)+{G_n(T)\over n}
\bigg\},
\end{aligned}
\tag{4.1}
\]

\[
\begin{aligned}
r_{\infty,n}^{[T]}
:={L_{\mathcal R,n}(T)\over\kappa_n(T)}
\bigg\{&
B_{3,n}(T)b_n^3+b_{S,n}(T)
\Theta_{S,\infty,n}^{[T]}
\sqrt{\frac{\log n}{nb_n}}\\
&+L_{{\rm LS},n}(T)+{G_n(T)\over n}
\bigg\}.
\end{aligned}
\tag{4.2}
\]

For positive stages before Richardson, define the analogous uncancelled stage radius \(u_{{\rm stg},n}^{[T]}\), with \(B_{1,n}(T)b_n\), \(b_{S,n}(T)\), and the truncated supremum-score term. Require

\[
(1+L_{\mathcal R,n}(T))u_{{\rm stg},n}^{[T]}
=o\{\delta_n(T)\},
\tag{4.3}
\]

\[
r_{\infty,n}^{[T]}=o\{\delta_n(T)\},
\qquad
\sqrt{M_n}r_{\mu,n}^{[T]}+K_{\mu,n}(T)M_n^{-2}
=o\{\delta_n(T)\}.
\tag{4.4}
\]

Then clipped positive stages lie in \(\mathcal C_n(T)\). Richardson/blend images, chords, connectors, and ruled surfaces lie in \(\mathcal T_n(T)\) with probability tending to one by HE-CLOSURE. On \(\mathcal E_{n,T_n}\), original and clipped finite-sample constructions are identical. Consequently

\[
\|\log_{\mu_n}\widehat\mu_n^{(3)}\|_{L^2}
=O_p(r_{\mu,n}^{[T_n]}),
\qquad
\sup_ud(\widehat\mu_n^{(3)}(u),\mu_n(u))
=O_p(r_{\infty,n}^{[T_n]}).
\tag{4.5}
\]

The polygonal-frame and feasible-observation rates are

\[
\begin{aligned}
r_{F,n}^{[T]}
=J_n(T)\Lambda_n(T)
\big\{&
L_{\mu,n}(T)r_{\mu,n}^{[T]}
+M_n(r_{\mu,n}^{[T]})^2\\
&+K_{\mu,n}(T)M_n^{-2}
\big\}
+\rho_{F,n},
\end{aligned}
\tag{4.6}
\]

\[
\begin{aligned}
q_{R,n}^{[T]}
\lesssim{}&
L_{\log,n}(T)
\{r_{\mu,n}^{[T]}+K_{\mu,n}(T)M_n^{-2}\}\\
&+r_{F,n}^{[T]}
\{\mathcal E_{2,n}^{[T]}+L_{\log,n}(T)r_{\mu,n}^{[T]}\}\\
&+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\end{aligned}
\tag{4.7}
\]

Here \(\mathcal E_{2,n}^{[T]}\) is the empirical RMS norm of clipped oracle tangent observations on retained edges. It may be bounded by \(T_n\), but sharper moment/empirical-energy bounds should be retained when available. All constants are evaluated on the expanding deterministic domain. No uniform-geometry conclusion follows merely from a tail assumption.

## 5. Truncated lag-product theorem

Let

\[
W_{t,h,n}^{[T]}
=Y_{t,n}^{[T]}\otimes Y_{t-h,n}^{[T]}
-E(Y_{t,n}^{[T]}\otimes Y_{t-h,n}^{[T]}).
\tag{5.1}
\]

For finite memory define

\[
(v_{h,n}^{[T]})^2
=N_{n,h}^{-1}\sum_tE\|W_{t,h,n}^{[T]}\|_{\rm HS}^2.
\tag{5.2}
\]

For causal physical dependence, radial projection is nonexpansive and

\[
\delta_{2,W_h^{[T]},n}(k)
\le M_{4,n}^{[T]}
\left\{
\delta_{4,Y^{[T]},n}(k)
+\mathbf1_{\{k\ge h\}}\delta_{4,Y^{[T]},n}(k-h)
\right\},
\tag{5.3}
\]

with \(M_{4,n}^{[T]}\le M_{4,n}\) and
\(\delta_{4,Y^{[T]},n}(k)\le\delta_{4,Y,n}(k)\).
The canonical HE-ROW proof gives

\[
\left\{
\sum_{h\le h_{0,n}}
\|\widetilde\Gamma_n^{[T]}(h)-\Gamma_n^{[T]}(h)\|_{\rm HS}^2
\right\}^{1/2}
=O_p(\omega_n^{[T]}),
\tag{5.4}
\]

where

\[
(\omega_n^{[T]})^2
=
\sum_{h\le h_{0,n}}
{(2d_{h,n}+1)(v_{h,n}^{[T]})^2\over N_{n,h}}
\tag{5.5a}
\]

for finite memory, or

\[
(\omega_n^{[T]})^2
=
\sum_{h\le h_{0,n}}
{(\Theta_{2,W_h^{[T]},n})^2\over N_{n,h}}
\tag{5.5b}
\]

for causal physical dependence.

On \(\mathcal E_{n,T_n}\), empirical original and clipped lag rows are identical. Comparing this common empirical row with the untruncated population row adds exactly (2.9).

## 6. Loading and selector propagation

Let

\[
\begin{aligned}
d_n^{[T]}
=O_p\bigg[&
\omega_n^{[T]}
+\sqrt{h_{0,n}}
\{2\mathcal E_{2,n}^{[T]}q_{R,n}^{[T]}
+(q_{R,n}^{[T]})^2+b_{W,n}(T)\}\\
&+\rho_{{\rm mask},n}+\rho_{{\rm disc},n}+\zeta_n
\bigg],
\end{aligned}
\tag{6.1}
\]

where \(\zeta_n\) is any non-truncation included-lag contamination. This is the error about the declared untruncated target row. Put

\[
\eta_n^{[T]}=2A_{2,n}d_n^{[T]}+(d_n^{[T]})^2.
\tag{6.2}
\]

If

\[
N_{X,n}\pi_{X,n}(T_n)+N_{Y,n}\pi_{Y,n}(T_n)\to0,
\tag{6.3}
\]

the domain conditions (4.3)–(4.4) hold, and

\[
\eta_n^{[T_n]}=o_p(\Delta_n),
\tag{6.4}
\]

then

\[
\boxed{
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
\lesssim{\eta_n^{[T_n]}\over\Delta_n}.}
\tag{6.5}
\]

The lag-row min–max argument still gives

\[
\widehat\lambda_{r_n+1}\le(d_n^{[T_n]})^2.
\tag{6.6}
\]

Threshold and ridged-ratio selectors are consistent under the canonical windows with \(d_n\) replaced by \(d_n^{[T_n]}\). No raw-ratio conclusion follows.

## 7. Sub-Weibull corollary

Suppose all consumed score-distance and anchor-energy tails satisfy, uniformly,

\[
P(Z_n>x)\le2\exp\{-(x/K_n)^\alpha\},
\qquad\alpha>0.
\tag{7.1}
\]

For \(r>0\), (2.1) gives

\[
\mathfrak t_{r,Z_n}(T)^r
\le
2T^re^{-(T/K_n)^\alpha}
+{2rK_n^r\over\alpha}
\Gamma\!\left({r\over\alpha},(T/K_n)^\alpha\right),
\tag{7.2}
\]

where \(\Gamma(s,z)=\int_z^\infty u^{s-1}e^{-u}du\).

Let \(N_n=N_{X,n}+N_{Y,n}\to\infty\) and choose

\[
T_n=K_n\{c\log N_n\}^{1/\alpha},
\qquad c>1.
\tag{7.3}
\]

Then

\[
N_nP(Z_n>T_n)\le2N_n^{1-c}\to0,
\tag{7.4}
\]

and every score/product bias is explicitly bounded by (2.3), (2.8), and (7.2). For fixed finite memory, the supremum-score contribution is of order

\[
K_n(\log N_n)^{1/\alpha}
\sqrt{\frac{\log n}{nb_n}},
\tag{7.5}
\]

while RMS-score and lag-product terms may retain variance-sensitive second/fourth-moment budgets instead of paying \(T_n\) and \(T_n^2\). If (4.3), (4.4), and (6.4) hold after substitution, the unbounded-score HE loading and selector theorem follows.

This corollary is automatic in a Hilbert/flat model with global geometry. On a curved manifold it additionally requires the expanding convex-domain and generated-map constants in Sections 1 and 4; a sub-Weibull tail does not itself supply geometry.

## 8. Hostile audit

| Proposed shortcut | Attack | Resolution | Status |
|---|---|---|---|
| Condition on all observations being small, then reuse independence | Conditioning on a row-wide event destroys finite-memory/innovation independence | Prove concentration for independently defined clipped variables; transfer only after the unconditional proof | **DISPROVED / REPAIRED** |
| Clipping changes no population quantity | The score mean and every lag covariance change in the tails | Pay \(b_S(T)\) in mean expansion and \(\sqrt{h_0}b_W(T)\) in the target row | **DISPROVED / REPAIRED** |
| Second moments close the lag row | Product variance may be infinite under finite trace variance | Retain \(v_{h,n}^{[T]}\), fourth/product moments, or product physical dependence | **DISPROVED / REPAIRED** |
| Sub-Weibull observations imply uniform manifold geometry | Tail control says nothing about cut, Hessian, connector, or ruled-surface constants | Require expanding nested convex domains and expose every geometry constant | **DISPROVED** |
| Projection preserves every manifold derivative | Metric projection can be nonsmooth at the clipping boundary | Do not differentiate projection; use the original population expansion plus score-bias comparison | **REPAIRED** |
| Radial tangent clipping and manifold clipping define one common modified DGP | They are different maps | Use them only as analytical arrays, require simultaneous sample equality, and compare each population target explicitly | **REPAIRED** |
| \(d_n/\Delta_n\) is the HE rate | Signal magnitude \(A_{2,n}\) may grow | Retain \((2A_{2,n}d_n+d_n^2)/\Delta_n\) | **DISPROVED** |

### Audit verdict

The proof closes one explicit truncation route and does not claim minimality. Its load-bearing assumptions are expanding-domain geometry, unconditional escape probability, explicit score and product tail integrals, clipped-array dependence, and the final actual-gap condition. No current theorem is weakened or used circularly.

### Edge checks

1. **Flat sub-Gaussian attainability.** Take fixed memory, global Hilbert geometry, \(K_n=O(1)\), \(\alpha=2\), \(N_n\asymp n\), and \(T_n\asymp\sqrt{\log n}\). The supremum score term is
   \[
   O_p\!\left({\log n\over\sqrt{nb_n}}\right),
   \]
   while RMS score and product-row terms retain their second/fourth-moment rates. At \(b_n=n^{-1/7}\), the domain/supremum requirement \(nb_n/\log^2n\to\infty\) holds. Choosing \(c\) sufficiently large makes the tail biases negligible relative to any displayed polynomial HE phase window. Thus the theorem has a nonempty genuinely unbounded DGP.
2. **Curved expanding domains.** Tail decay does not control \(L_{\log,n}(T)\), \(J_n(T)\), \(\Lambda_n(T)\), or \(\delta_n(T)\). These remain visible in (4.1)–(4.7); if they grow too quickly, the curved corollary is unavailable rather than silently asserted.
3. **Target rank.** Equations (6.5)–(6.6) require the declared untruncated target row to have rank \(r_n\) and gap \(\Delta_n>0\). Truncation is only an analytical comparison and does not redefine the target to manufacture rank.
4. **Zero signal.** If \(\Delta_n=0\), (6.4) cannot hold and no positive-rank loading conclusion follows.
5. **Dependence.** Finite-memory preservation follows from measurable coordinatewise clipping. Causal score dependence is assumed after the manifold projection/Log composition; only anchor-Hilbert radial clipping inherits nonexpansiveness automatically. No coordinatewise-to-Hilbert shortcut is used.
6. **Rare extreme observations.** The no-clipping transfer requires the row-wide escape probability (6.3), not merely \(\pi_{X,n}(T_n)\to0\). This prevents one extreme observation among \(n\) rows from invalidating the generated-domain proof.

**Internal hostile-pass verdict: PROVED UNDER EXPLICIT ASSUMPTIONS.** The remaining question is sharpness/minimality of the tail package, which is optional and not a load-bearing open lemma.
