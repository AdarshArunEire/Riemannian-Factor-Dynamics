---
type: archived-proof-workstream
title: HE — growing energy and pervasive signal working dossier
status: archived-after-two-hostile-passes
authority: archived-noncanonical
owner: Agent HE
last-audited: 2026-08-08
---

# HE — growing energy and pervasive signal working dossier

> **Archived proof provenance, not canon.** This dossier gives the bounded-tail conditional growing-energy theorem, explicit attainable phase models, and analytic counterexamples that survived two hostile passes. The canonical analytical ledger and Paper 1 note govern current theorem wording.

## 0. Bottom line

Growing total tangent energy is compatible with loading recovery only through the exact joint condition

\[
\eta_n:=2A_{2,n}d_n+d_n^2=o_p(\Delta_n).
\tag{0.1}
\]

The full feasible tangent-observation error is not the centre error. If \(r_{\mu,n}\) is centre RMS and \(r_{F,n}\) is non-rigid frame error, then

\[
q_{R,n}
\lesssim L_{\log,n}r_{\mu,n}
+r_{F,n}\{\mathcal E_{2,n}+L_{\log,n}r_{\mu,n}\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\tag{0.2}
\]

The frame therefore creates an additional energy factor in generic curved models. Variance-sensitive product budgets are retained before any \(R_n^2/\sqrt n\) envelope bound.

| Claim | Repaired first-pass status |
|---|---|
| positive three-scale mean/grid theorem | **PROVED UNDER EXPLICIT BOUNDED-TAIL AND GENERATED-DOMAIN ASSUMPTIONS** |
| generated-set closure | **PROVED UNDER THE NESTED CONVEX-DOMAIN PRIMITIVES IN HE-G0** |
| unbounded-score truncation extension | **OPEN — EXACT LEMMA STATED** |
| polygonal frame and full \(q_{R,n}\) | **PROVED UNDER HE-G0 AND HE-M** |
| variance-sensitive finite-memory and causal-PD lag row | **PROVED** |
| feasible row, assembly, loading, and selectors | **PROVED** |
| flat \(\rho<3/13\) and curved \(\rho<3/20\) windows | **PROVED AS SUFFICIENT ENVELOPE REGIMES, NOT MINIMAX CLAIMS** |
| concrete pervasive and growing-rank regimes | **PROVED BY EXPLICIT DGPs** |
| harmless normalisation, arbitrary fixed-gap energy, and contamination immunity | **DISPROVED** |

No concrete asset, sensor, gene, neuro, or finance family is yet labelled **EXACT MATCH**. Application remapping is downstream of both hostile passes and BW closure.

## 1. Typed model, targets, and norms

After true parallel transport to the anchor Hilbert space \(H_n=T_{\mu_n(u_0)}M_n\),

\[
Y_{t,n}=A_nf_{t,n}+\varepsilon_{t,n},
\qquad A_n^*A_n=I_{r_n}.
\tag{1.1}
\]

For retained lags \(h\le h_{0,n}\), define the clean factor row

\[
\Gamma_n^0(h)=A_nC_{f,n}(h)A_n^*,
\qquad
\mathcal G_n^0=[\Gamma_n^0(1)\ \cdots\ \Gamma_n^0(h_{0,n})],
\tag{1.2}
\]

\[
\mathbb L_n^0=\mathcal G_n^0(\mathcal G_n^0)^*,
\qquad
A_{2,n}^0=
\left\{\sum_{h\le h_{0,n}}\|\Gamma_n^0(h)\|_{\rm op}^2\right\}^{1/2},
\tag{1.3}
\]

\[
\Delta_n^0
=\lambda_{r_n}(\mathbb L_n^0)-\lambda_{r_n+1}(\mathbb L_n^0).
\tag{1.4}
\]

The actual population row may be contaminated:

\[
\Gamma_n(h)=\Gamma_n^0(h)+D_n(h),
\qquad
\zeta_n=
\left\{\sum_h\|D_n(h)\|_{\rm op}^2\right\}^{1/2}.
\tag{1.5}
\]

Write \(A_{2,n}^{\rm act}\), \(\mathbb L_n^{\rm act}\), \(\Delta_n^{\rm act}\), and \(E_n^{\rm act}\) for the corresponding actual-row quantities. Estimation of \(E_n^{\rm act}\) and recovery of \(E_n^0=\operatorname{ran}A_n\) are different theorems.

The same edge mask and normalisation are used in every population and empirical row. Tangent vectors use the manifold tangent norm, products use Hilbert–Schmidt norm, lag rows use the direct-sum Hilbert–Schmidt/operator norm, and loading spaces use operator-norm sine-theta distance.

## 2. Primitive geometry and derived generated-set closure

### HE-G0 — nested convex-domain primitives

For each \(n\), assume closed geodesically convex sets

\[
\mathcal C_n\subset \mathcal T_n
\]

with positive margin

\[
\delta_n=\inf\{d(x,y):x\in\mathcal C_n,\ y\notin\mathcal T_n\}>0.
\tag{2.1}
\]

The following are primitive:

1. the centre curve, all actual observations, and every stationary/local proxy observation used in the mean proof lie in \(\mathcal C_n\);
2. positive weighted barycentres of laws supported in \(\mathcal C_n\) exist uniquely and remain in \(\mathcal C_n\);
3. every score pair \((q,x)\in\mathcal T_n\times\mathcal C_n\) has Hessian lower bound \(\kappa_n I\) and the required upper and Lipschitz bounds;
4. Exp, Log, radial connectors, Richardson, blends, geodesic interpolation, parallel transport, and ruled geodesic homotopies have the consumed fixed-order bounds on \(\mathcal T_n\), denoted by \(L_{\log,n}\), \(L_{\mathcal R,n}\), \(J_n\), and \(\Lambda_n\);
5. the true centre speed and acceleration are bounded by \(L_{\mu,n}\) and \(K_{\mu,n}\).

These constants may grow. Bare Hadamard geometry or a growing radius does not make them uniform.

For the positive stages, let

\[
u_{{\rm stg},n}
=\frac1{\kappa_n}
\left\{
B_{1,n}b_n
+\Theta_{S,\infty,n}\sqrt{\frac{\log n}{nb_n}}
+L_{{\rm LS},n}+\frac{G_n}{n}
\right\},
\tag{2.2}
\]

where \(B_{1,n}\) is the uncancelled first-order stage-bias budget. Assume

\[
(1+L_{\mathcal R,n})u_{{\rm stg},n}=o(\delta_n).
\tag{2.3}
\]

### Lemma HE-CLOSURE — generated-set closure

Under HE-G0 and (2.3), every population proxy stage, empirical positive stage, Richardson output, fixed-width blend, polygonal chord, radial connector, and ruled comparison surface lies in \(\mathcal T_n\) with probability tending to one.

**Proof.** Positive population and empirical stages remain in \(\mathcal C_n\) by convexity. The score-to-distance inequality and the uniform score bound put every stage within \(O_p(u_{{\rm stg},n})\) of the local centre. Richardson is a fixed smooth map equal to the diagonal point when all inputs coincide, so its output is within \(L_{\mathcal R,n}O_p(u_{{\rm stg},n})=o_p(\delta_n)\) of \(\mathcal C_n\). The same holds for the fixed-width blend. Convexity of \(\mathcal T_n\) keeps every chord and radial connector inside it. A ruled surface is obtained by geodesic interpolation between points of two such curves; convexity again keeps it in \(\mathcal T_n\). Actual and proxy score endpoints are in \(\mathcal C_n\), so every consumed score/Hessian pair is covered. \(\square\)

This is a strong but noncircular domain package. A weaker high-probability or truncation-based domain theorem is not claimed.

## 3. Mean and polygonal frame

### HE-M — typed mean producers

Use the canonical positive one-sided scales

\[
c=(1,1/2,1/4),\qquad \lambda=(1/3,-2,8/3),
\]

with endpoint-flat kernels and the fixed-width forward/backward blend. Assume:

- third-order post-cancellation bias budget \(B_{3,n}\);
- local-stationarity score defect \(L_{{\rm LS},n}\);
- design error \(G_n/n\);
- weighted score inequalities

\[
\left\|\sum_t w_t(u)S_{t,n}(u)\right\|_{L^2(H_n)}
\le \frac{\Theta_{S,2,n}}{\sqrt{nb_n}},
\tag{3.1}
\]

\[
\sup_u\left\|\sum_t w_t(u)S_{t,n}(u)\right\|
=O_p\!\left(
\Theta_{S,\infty,n}\sqrt{\frac{\log n}{nb_n}}
\right).
\tag{3.2}
\]

Define

\[
r_{\mu,n}
=\frac{L_{\mathcal R,n}}{\kappa_n}
\left\{
B_{3,n}b_n^3
+\frac{\Theta_{S,2,n}}{\sqrt{nb_n}}
+L_{{\rm LS},n}+\frac{G_n}{n}
\right\},
\tag{3.3}
\]

\[
r_{\infty,n}
=\frac{L_{\mathcal R,n}}{\kappa_n}
\left\{
B_{3,n}b_n^3
+\Theta_{S,\infty,n}\sqrt{\frac{\log n}{nb_n}}
+L_{{\rm LS},n}+\frac{G_n}{n}
\right\}.
\tag{3.4}
\]

### Theorem HE-MEAN

Under HE-G0, HE-CLOSURE, and HE-M,

\[
\|\log_{\mu_n}\widehat\mu_n^{(3)}\|_{L^2}
=O_p(r_{\mu,n}),
\qquad
\sup_u d(\widehat\mu_n^{(3)}(u),\mu_n(u))
=O_p(r_{\infty,n}),
\tag{3.5}
\]

and the same \(O_p(r_{\mu,n})\) RMS bound holds on every deterministic grid.

**Proof.** The three scale identities cancel the first- and second-order population terms, including the nonlinear \(m_1^2C\) term. Strong convexity converts the deterministic-point score into distance with factor \(\kappa_n^{-1}\); Richardson/blend stability contributes \(L_{\mathcal R,n}\). Equations (3.1)–(3.2) give the stochastic terms without an ambient sphere net. HE-CLOSURE supplies the domain for every Taylor map. \(\square\)

### Polygonal frame

Let \(M_n+1\) be the deterministic vertex count and require

\[
\sqrt{M_n}\,r_{\mu,n}
+K_{\mu,n}M_n^{-2}
=o(\delta_n),
\tag{3.6}
\]

together with \(r_{\infty,n}=o(\delta_n)\). The corrected tube condition includes both the maximum vertex error and true-chord interpolation error.

The polygonal holonomy proof gives

\[
r_{F,n}
=J_n\Lambda_n
\left\{
L_{\mu,n}r_{\mu,n}
+M_nr_{\mu,n}^2
+K_{\mu,n}M_n^{-2}
\right\}
+\rho_{F,n}.
\tag{3.7}
\]

Let the empirical oracle-energy budget satisfy, for every retained edge set,

\[
\max_h
\left\{
N_{n,h}^{-1}\sum_t\|Y_{t,n}\|^2,\,
N_{n,h}^{-1}\sum_t\|Y_{t-h,n}\|^2
\right\}^{1/2}
=O_p(\mathcal E_{2,n}).
\tag{3.8}
\]

### Theorem HE-PF

The full connector-aligned feasible observation RMS obeys

\[
\boxed{
q_{R,n}
=O_p\!\left[
L_{\log,n}\{r_{\mu,n}+K_{\mu,n}M_n^{-2}\}
+r_{F,n}\{\mathcal E_{2,n}+L_{\log,n}r_{\mu,n}\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}
\right].
}
\tag{3.9}
\]

**Proof.** Base-point recentering gives the first term. The frame acts on the recentered Log, whose RMS is at most \(\mathcal E_{2,n}+L_{\log,n}r_{\mu,n}\); this yields both the energy term and the formerly omitted cross term. Endpoint connector and numerical/reconstruction defects are named separately. \(\square\)

When the constants are uniform, defects vanish, and \(M_n\asymp r_{\mu,n}^{-2/3}\), one has \(r_{F,n}=O_p(r_{\mu,n})\). In one common flat or a supplied rigid frame, \(r_{F,n}=0\).

## 4. Unbounded-score route

The theorem above consumes the explicit sup-tail budget (3.2). It does not prove a minimal-moment or generic Orlicz theorem.

> **OPEN — EXACT LEMMA HE-TRUNC.** Given truncation levels \(T_n\), prove simultaneously:
>
> 1. a clipped or high-probability generated-domain event for actual and proxy observations;
> 2. uniform positive-stage score concentration for the truncated row;
> 3. explicit score bias
>    \[
>    b_{S,n}(T_n)
>    =\sup_{u,q}\left\|
>    E\{\log_qX-\log_qX^{[T_n]}\}
>    \right\|;
>    \]
> 4. explicit product bias
>    \[
>    b_{W,n}(T_n)
>    =\max_h E\|
>    Y_t\otimes Y_{t-h}
>    -Y_t^{[T_n]}\otimes Y_{t-h}^{[T_n]}
>    \|_{\rm HS};
>    \]
> 5. truncated score/product dependence budgets and the induced change of population target;
> 6. choices of \(T_n\) making every bias and escape term negligible relative to (0.1).

Until HE-TRUNC is proved, unbounded-score/truncation and weaker generated-tube claims remain open and are consumed by no theorem here.

## 5. Oracle lag row

Let

\[
W_{t,h,n}
=Y_{t,n}\otimes Y_{t-h,n}
-E(Y_{t,n}\otimes Y_{t-h,n})
\in\mathcal S_2(H_n).
\tag{5.1}
\]

### Finite-memory producer

Let \(\ell_{{\rm dep},n}\) be the causal memory length; this symbol is never matrix size. If \(W_{t,h,n}\) has dependence range \(d_{h,n}\le \ell_{{\rm dep},n}+h\), define

\[
v_{h,n}^2
=\frac1{N_{n,h}}\sum_tE\|W_{t,h,n}\|_{\rm HS}^2.
\tag{5.2}
\]

### Causal physical-dependence producer

Let \(Y_{t,n}^{(k)}\) replace innovation \(\xi_{t-k}\) by an independent copy, and put

\[
\delta_{4,Y,n}(k)
=\sup_t\|Y_{t,n}-Y_{t,n}^{(k)}\|_{L^4(H_n)},
\qquad
M_{4,n}=\sup_t\|Y_{t,n}\|_{L^4(H_n)}.
\tag{5.3}
\]

For \(Z_{t,h}=Y_t\otimes Y_{t-h}\),

\[
Z_{t,h}-Z_{t,h}^{(k)}
=(Y_t-Y_t^{(k)})\otimes Y_{t-h}
+Y_t^{(k)}\otimes(Y_{t-h}-Y_{t-h}^{(k)}).
\tag{5.4}
\]

The second difference is zero for \(k<h\), and for \(k\ge h\) its \(L^4\) norm is bounded by \(\delta_{4,Y,n}(k-h)\). The coupled product has the same marginal law as the original product, so centering adds no extra term. Hence

\[
\delta_{2,W_h,n}(k)
\le
M_{4,n}
\left\{
\delta_{4,Y,n}(k)
+\mathbf 1_{\{k\ge h\}}\delta_{4,Y,n}(k-h)
\right\},
\tag{5.5}
\]

and therefore

\[
\Theta_{2,W_h,n}:=\sum_{k\ge0}\delta_{2,W_h,n}(k)
\le2M_{4,n}\Theta_{4,Y,n},
\quad
\Theta_{4,Y,n}:=\sum_{k\ge0}\delta_{4,Y,n}(k).
\tag{5.6}
\]

Under an a.s. envelope, the \(L^2\) version gives
\(\Theta_{2,W_h,n}\le2R_n\Theta_{2,Y,n}\), including the shifted coefficient sum.

Define

\[
\omega_n^2=
\begin{cases}
\displaystyle
\sum_{h\le h_{0,n}}
\frac{(2d_{h,n}+1)v_{h,n}^2}{N_{n,h}},
&\text{finite memory},\\[3mm]
\displaystyle
\sum_{h\le h_{0,n}}
\frac{\Theta_{2,W_h,n}^2}{N_{n,h}},
&\text{causal physical dependence}.
\end{cases}
\tag{5.7}
\]

### Theorem HE-ROW

\[
\left\{
\sum_{h\le h_{0,n}}
\|\widetilde\Gamma_n(h)-\Gamma_n(h)\|_{\rm HS}^2
\right\}^{1/2}
=O_p(\omega_n).
\tag{5.8}
\]

The finite-memory proof expands the Hilbert–Schmidt second moment and keeps only dependent pairs. The physical-dependence proof applies the Hilbert martingale-projection inequality to (5.1). Lag aggregation is explicit in (5.7). Under fixed lag/memory and \(\|Y_t\|\le R_n\), \(\omega_n=O(R_n^2/\sqrt n)\).

## 6. Feasible row, clean target, and contaminated target

The pathwise product expansion and (3.8) give

\[
\left\|
N_{n,h}^{-1}\sum_t
(\widehat Y_t\otimes\widehat Y_{t-h}
-Y_t\otimes Y_{t-h})
\right\|_{\rm HS}
\le 2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2.
\tag{6.1}
\]

Define sampling error about the actual row:

\[
d_{{\rm samp},n}
=
\left\{
\sum_h
\|\widehat\Gamma_n(h)-\Gamma_n(h)\|_{\rm op}^2
\right\}^{1/2}.
\tag{6.2}
\]

Then

\[
d_{{\rm samp},n}
=O_p\!\left[
\omega_n
+\sqrt{h_{0,n}}
\{2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2\}
+\rho_{{\rm mask},n}+\rho_{{\rm disc},n}
\right].
\tag{6.3}
\]

For the clean factor row,

\[
d_{{\rm ideal},n}
:=
\left\{
\sum_h
\|\widehat\Gamma_n(h)-\Gamma_n^0(h)\|_{\rm op}^2
\right\}^{1/2}
\le d_{{\rm samp},n}+\zeta_n.
\tag{6.4}
\]

There is no double counting:

- estimation of \(E_n^{\rm act}\) uses \(d_{{\rm samp},n}\), \(A_{2,n}^{\rm act}\), and \(\Delta_n^{\rm act}\);
- recovery of \(E_n^0\) uses \(d_{{\rm ideal},n}\), \(A_{2,n}^0\), and \(\Delta_n^0\);
- direct population comparison of actual and clean operators pays

\[
\|\mathbb L_n^{\rm act}-\mathbb L_n^0\|_{\rm op}
\le 2A_{2,n}^0\zeta_n+\zeta_n^2.
\tag{6.5}
\]

### Theorem HE-LOAD

For either target \(T\in\{{\rm act},0\}\), with its matching \(d_n^T,A_{2,n}^T,\Delta_n^T\),

\[
\|\widehat{\mathbb L}_n-\mathbb L_n^T\|_{\rm op}
\le
\eta_n^T:=2A_{2,n}^Td_n^T+(d_n^T)^2,
\tag{6.6}
\]

\[
\widehat\lambda_{r_T+1,n}\le(d_n^T)^2.
\tag{6.7}
\]

If \(\eta_n^T=o_p(\Delta_n^T)\),

\[
\|\sin\Theta(\widehat E_n,E_n^T)\|_{\rm op}
\le\frac{2\eta_n^T}{\Delta_n^T}.
\tag{6.8}
\]

The threshold selector is consistent when

\[
(d_n^T)^2=o_p(\tau_n),\qquad
\tau_n=o(\Delta_n^T),\qquad
\eta_n^T=o_p(\Delta_n^T).
\tag{6.9}
\]

The ridged ratio additionally needs a lower bound on adjacent nonzero population eigenvalue ratios. The raw ratio remains disproved.

## 7. Envelope phase diagram

These are sufficient attainable regimes, not universal optima. Throughout this section:

- \(h_0,r,\ell_{\rm dep}\) are fixed;
- the clean target is exact, so \(\zeta_n=0\);
- all geometry, bias, and dependence constants not displayed are uniform;
- all \(\rho\)-defects in (3.7), (3.9), and (6.3) are zero;
- the nested-domain margin \(\delta_n\) is bounded below;
- \(r_{\infty,n}=o(1)\) and (3.6) hold;
- \(R_n\asymp\mathcal E_{2,n}=n^\rho\);
- \(B_{3,n}=O(1)\), \(\Theta_{S,2,n}\asymp R_n\), and

\[
r_{\mu,n}
\asymp b_n^3+\frac{R_n}{\sqrt{nb_n}}+n^{-a}.
\tag{7.1}
\]

Let \(b_n=n^{-\alpha}\). Balancing the feasible bias and stochastic terms gives

\[
\alpha=\frac{1-2\rho}{7}.
\tag{7.2}
\]

The positive-stage closure rate (2.2), the tube sup rate, and (3.6) are additional explicit assumptions; with fixed margin and the displayed bounded-envelope finite-memory model, they hold throughout the windows below up to the harmless \(\sqrt{\log n}\) factor.

### Flat or rigid frame, fixed clean gap

Here \(r_{F,n}=0\), \(q_{R,n}=O_p(r_{\mu,n})\), \(A_{2,n}^0\asymp1\), and \(\Delta_n^0\asymp1\). Equation (6.3) gives

\[
d_{{\rm ideal},n}
=O_p\!\left(
n^{-(3-13\rho)/7}
+n^{-(a-\rho)}
\right).
\tag{7.3}
\]

Thus

\[
\rho<\frac3{13},\qquad a>\rho
\tag{7.4}
\]

is a sufficient consistency window. The pure balanced headline rate
\(n^{-(3-13\rho)/7}\) requires the stronger condition

\[
a\ge\frac{3-6\rho}{7}.
\tag{7.5}
\]

### Generic curved moving frame, fixed clean gap

With \(L_\mu>0\), (3.9) gives \(q_{R,n}=O_p(R_nr_{\mu,n})\). Therefore

\[
d_{{\rm ideal},n}
=O_p\!\left(
n^{-(3-20\rho)/7}
+n^{-(a-2\rho)}
\right).
\tag{7.6}
\]

Hence

\[
\rho<\frac3{20},\qquad a>2\rho
\tag{7.7}
\]

is sufficient for consistency. The balanced headline rate
\(n^{-(3-20\rho)/7}\) again requires (7.5).

## 8. Explicit pervasive DGP

Let \(H_n=\mathbb R^{p_n}\), \(\mu_n(u)\equiv0\), and \(a_n=e_1\). Let
\(\xi_t\) and \(\eta_{t,j}\) be mutually independent iid Rademacher variables. For fixed \(\theta\ne0\), define

\[
g_t=\frac{\xi_t+\theta\xi_{t-1}}{\sqrt{1+\theta^2}},
\qquad
c=\operatorname{Cov}(g_t,g_{t-1})
=\frac{\theta}{1+\theta^2}\ne0,
\tag{8.1}
\]

\[
\varepsilon_{t,n}
=(0,\eta_{t,2},\ldots,\eta_{t,p_n})^T,
\qquad
Y_{t,n}=\sqrt{p_n}\,a_ng_t+\varepsilon_{t,n}.
\tag{8.2}
\]

Verification:

1. \(EY_{t,n}=0\), the centre is exactly zero, and the geometry is globally flat;
2. the row is one-dependent and \(\|Y_{t,n}\|\le C\sqrt{p_n}\);
3. \(\varepsilon_t\) is serially white, independent of \(g\), and both factor–noise lag cross moments vanish;
4. the included-lag target is exact:

\[
\Gamma_n(1)=p_nc\,a_n\otimes a_n;
\tag{8.3}
\]

5. \(v_{1,n}=O(p_n)\), so \(\omega_n=O(p_n/\sqrt n)\);
6. \(A_{2,n}\asymp p_n\) and \(\Delta_n\asymp p_n^2\).

The Euclidean positive-stage/Richardson estimator is linear and has frame error zero. Its row error obeys

\[
d_n
=O_p\!\left(
\frac{p_n}{\sqrt n}
+\sqrt{p_n}\,b_n^3
+\frac{p_n}{\sqrt{nb_n}}
+q_{R,n}^2
\right).
\tag{8.4}
\]

Consequently

\[
\frac{\eta_n}{\Delta_n}
=O_p\!\left(
\frac{d_n}{p_n}+\frac{d_n^2}{p_n^2}
\right)
=O_p\!\left(
n^{-1/2}+(nb_n)^{-1/2}
+\frac{b_n^3}{\sqrt{p_n}}
+\frac{q_{R,n}^2}{p_n}
\right).
\tag{8.5}
\]

This is a fully specified nonempty pervasive regime. Pervasive signal pays the \(O(p_n)\) row error because \(A_{2,n}\asymp p_n\) and \(\Delta_n\asymp p_n^2\).

## 9. Normalisation and matrix regimes

For \(\bar Y=Y/c_n\),

\[
\bar R_n=R_n/c_n,\quad
\bar\Gamma_h=\Gamma_h/c_n^2,\quad
\bar A_{2,n}=A_{2,n}/c_n^2,\quad
\bar\Delta_n=\Delta_n/c_n^4.
\tag{9.1}
\]

In the pervasive DGP, \(c_n=\sqrt{p_n}\) preserves \(A_2,\Delta\asymp1\). For a localised \(O(1)\) serial factor plus \(p_n\) white background coordinates, the same normalisation gives \(A_2\asymp p_n^{-1}\), \(\Delta\asymp p_n^{-2}\), and bounded-energy robust loading requires \(p_nd_n\to0\). At \(d_n\asymp n^{-3/7}\), this is \(p_n=o(n^{3/7})\), whereas the unnormalised flat envelope window is \(p_n=o(n^{6/13})\). Normalisation can shrink the admissible region.

Always distinguish matrix size \(m_n\) from
\(p_n=m_n(m_n+1)/2\).

| Matrix model | Energy scale | Sufficient localised fixed-gap window |
|---|---:|---:|
| \({\rm Sym}(m_n)\), Frobenius, entrywise \(O(1)\) | \(R_n\asymp m_n\asymp\sqrt{p_n}\) | flat: \(m_n=o(n^{3/13})\), \(p_n=o(n^{6/13})\) |
| fixed-basis diagonal AIRM, \(m_n\) \(O(1)\) log coordinates | \(R_n\asymp\sqrt{m_n}\) | flat: \(m_n=o(n^{6/13})\) |
| full AIRM fixed spectral band, whitened log operator norm \(O(1)\) | \(R_n\asymp\sqrt{m_n}\) | curved: \(m_n=o(n^{3/10})\), \(p_n=o(n^{3/5})\) |
| fixed-rank bounded-singular-value variation | \(R_n=O(1)\) | canonical bounded-energy regime |

These are conditional statistical rows, not application verdicts and not BW claims.

## 10. Explicit growing-rank DGP

Let \(H_n=\mathbb R^{2r_n}\), and let \(A_n\) embed \(\mathbb R^{r_n}\) into the first \(r_n\) coordinates. For independent iid Rademacher arrays \(\xi_{j,t}\), define

\[
g_{j,t}
=\frac{\xi_{j,t}+\theta\xi_{j,t-1}}{\sqrt{1+\theta^2}},
\qquad
f_{t,n}=(g_{1,t},\ldots,g_{r_n,t})^T.
\tag{10.1}
\]

Let \(\varepsilon_{t,n}\) occupy the last \(r_n\) coordinates with iid centered Rademacher entries, independent across time and from \(f\). Then:

\[
\|Y_{t,n}\|\le C\sqrt{r_n},\qquad
C_f(1)=cI_{r_n},
\tag{10.2}
\]

\[
A_{2,n}=|c|,\qquad
\Delta_n=c^2,\qquad
\omega_n=O(r_n/\sqrt n).
\tag{10.3}
\]

All target and cross moments are exact, the row is one-dependent, and the flat mean/frame theorem applies. Setting \(R_n\asymp\sqrt{r_n}\) in (7.3) gives consistency for

\[
r_n=o(n^{6/13})
\tag{10.4}
\]

with the displayed bandwidth and local-stationarity conditions. Let \(\bar d_n\downarrow0\) be a deterministic upper rate for \(d_n\); choosing
\(\tau_n=\bar d_n\) gives \(d_n^2=o_p(\tau_n)\) and
\(\tau_n=o(c^2)\). Every nonzero population eigenvalue equals \(c^2\), so the adjacent-ratio condition is one. Both threshold and ridged selectors are therefore consistent.

The necessary energy warning remains:

\[
\Delta_n
\le\frac{h_{0,n}\mathcal F_n^4}{r_n},
\qquad
\mathcal F_n^2=\sup_tE\|f_{t,n}\|^2.
\tag{10.5}
\]

Bounded total factor energy cannot support a fixed gap as \(r_n\to\infty\).

## 11. Analytic counterexamples and lead edges

### CE-HE1 — coordinatewise control

Independent Rademacher coordinates satisfy bounded coordinate moments and coordinatewise dependence budgets, but

\[
E\left\|N^{-1}\sum_{i=1}^NY_i\right\|^2=p_n/N.
\]

Hilbert score and dependence budgets carry a hidden \(\sqrt{p_n}\) if only coordinates are controlled.

### CE-HE2 — trace second moment does not close products

Repeat an iid centered scalar \(Z_k\) twice, with \(EZ_k^2=1\) and
\(EZ_k^4=\infty\). The stationary row is one-dependent and trace-bounded, but its aligned lag product contains \(Z_k^2\) and has infinite variance.

### CE-HE3 — growing energy with a fixed gap

For orthogonal unit \(a,v\), let \(g_t\) have fixed nonzero lag covariance and let \(\zeta_t\) be iid Rademacher:

\[
Y_{t,n}=ag_t+R_nv\zeta_t.
\]

The background population lag is zero, but its empirical lag coefficient is
\(\Theta_p(R_n^2/\sqrt n)\). If this does not vanish, the fixed-gap oracle row is inconsistent.

An explicitly high-dimensional coordinatewise-bounded version uses
\(\varepsilon_{t,n}=\zeta_t\mathbf 1_{p_n}\) in a background subspace orthogonal to the factor. Then \(\|\varepsilon_t\|=\sqrt{p_n}\) and the empirical lag operator has norm \(\Theta_p(p_n/\sqrt n)\) despite zero population lag.

### CE-HE4 — localised-factor normalisation

An \(O(1)\) serial factor in \(e_1\) plus \(p_n-1\) white coordinates has fixed raw gap. Division by \(\sqrt{p_n}\) sends its factor lag to \(c/p_n\) and its lag-operator gap to \(c^2/p_n^2\).

### CE-HE5 — explicit coloured outside-loading contamination

Let the clean pervasive factor be \(\sqrt{p_n}a g_t\) with lag \(c\), and let
\(v\perp a\). Independently define

\[
z_t=\frac{\nu_t+\vartheta\nu_{t-1}}{\sqrt{1+\vartheta^2}},
\qquad c_z=\frac{\vartheta}{1+\vartheta^2}\ne0,
\]

and add coloured idiosyncratic noise

\[
\varepsilon_{t,n}^{\rm col}=\sqrt{p_n}\,b\,v z_t.
\]

Then

\[
\Gamma_n(1)
=p_nc\,a\otimes a+p_nb^2c_z\,v\otimes v,
\]

and

\[
\mathbb L_n
=p_n^2c^2\,a\otimes a
+p_n^2b^4c_z^2\,v\otimes v.
\]

If \(|b^2c_z|>|c|\), the leading population loading switches from \(a\) to \(v\). If \(0<|b^2c_z|<|c|\), the actual population rank is two and the second eigenvalue is a fixed fraction of the first, so any selector consistent for the actual row selects an extra factor. This is an analytic counterexample, not an upper-bound argument.

### CE-HE6 — insufficient lag energy with growing rank

If \(r_n\) independent components each have variance \(1/r_n\) and lag covariance \(c/r_n\), then total factor energy is one but

\[
C_f(1)=(c/r_n)I_{r_n},
\qquad
\Delta_n=c^2/r_n^2\to0.
\]

### Lead edge checks

1. **Zero signal.** If all included population lags vanish, then \(\mathbb L=0\) and no positive-rank loading space is identifiable. A rank-zero threshold statement is possible when \(d_n^2=o_p(\tau_n)\), but Davis–Kahan has no positive \(\Delta_n\).
2. **Zero idiosyncratic noise.** Setting \(\varepsilon_t=0\) does not remove nonparametric centre or frame error. Unless the centre/frame is known, \(q_{R,n}\) remains in (6.3).
3. **Fixed dimension.** Fixed \(p\) does not remove the four producer channels; it only makes all energy and geometry constants finite.

## 12. Reduction to canonical bounded-energy HD1

Suppose \(R_n,\mathcal E_{2,n},B_{3,n},\Theta_{S,2,n}\), all geometry constants, lag count, dependence memory, and rank are bounded; defects vanish; the clean target is exact; and \(M_n\asymp\ell_n^{-2/3}\), where

\[
\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
\]

Then, row by row,

\[
r_{\mu,n}=O(\ell_n),\qquad
r_{F,n}=O(\ell_n),\qquad
q_{R,n}=O(\ell_n),
\]

\[
\omega_n=O(n^{-1/2}),\qquad
d_{{\rm samp},n}=d_{{\rm ideal},n}
=O_p(n^{-1/2}+\ell_n).
\]

Equations (6.6)–(6.9) become exactly the canonical HD1 operator, loading, null-square, and selector chain.

## 13. First hostile-pass response table

| Objection | Resolution | Status |
|---|---|---|
| generated closure was assumed | HE-G0 now splits primitive nested domains from derived Lemma HE-CLOSURE and includes proxy objects | **REPAIRED** |
| polygon tube condition malformed/incomplete | (3.6) now uses \(\sqrt{M_n}r_{\mu,n}+K_{\mu,n}M_n^{-2}\) and the true margin | **REPAIRED** |
| \(q_R\) omitted frame–Log cross term/defects | (3.9) includes \(r_F L_{\log}r_\mu\) and named connector/observation defects | **REPAIRED** |
| unbounded-score/truncation overclaim | Section 4 states exact open lemma HE-TRUNC; no minimal-moment claim remains | **NARROWED HONESTLY** |
| product-PD coupling undefined | (5.4)–(5.6) give the exact coupling, shift, centering factor, and lag sum | **REPAIRED** |
| memory and matrix size both used \(m_n\) | dependence memory is now \(\ell_{{\rm dep},n}\); \(m_n\) is reserved for matrix size | **REPAIRED** |
| flat phase omitted local stationarity | (7.3) includes \(n^{-(a-\rho)}\); (7.5) gives the exact stronger balanced-rate condition | **REPAIRED** |
| curved phase omitted local stationarity | (7.6) includes \(n^{-(a-2\rho)}\); (7.5) gives the exact stronger balanced-rate condition | **REPAIRED** |
| phase conditions omitted closure/defects | Section 7 lists fixed margin, sup/tube, dependence, geometry, and zero-defect assumptions explicitly | **REPAIRED** |
| pervasive DGP incomplete | Section 8 specifies centered bounded innovations, memory, cross moments, product budget, target, \(A_2\), and \(\Delta\) | **REPAIRED** |
| coloured contamination was only postulated | CE-HE5 constructs a bounded serial outside-loading process causing a switch or extra factor | **REPAIRED** |
| growing-rank DGP incomplete | Section 10 specifies the process, row budget, gap, loading condition, and selector window | **REPAIRED** |
| clean and contaminated targets were double counted | Section 6 separates \(d_{\rm samp}\), \(d_{\rm ideal}\), actual/clean gaps, and the population penalty | **REPAIRED** |
| lead edge cases missing | Section 11 adds zero signal, zero noise, and high-dimensional fixed-gap failures | **REPAIRED** |
| bounded-energy reduction missing | Section 12 recovers \(\ell,\ell,\ell,n^{-1/2}+\ell\) row by row | **REPAIRED** |
| application status premature | Section 0 states that no concrete application is yet an exact match | **REPAIRED** |
| file had C0/LaTeX corruption | file rewritten with literal backslashes; C0, delimiter, and diff integrity scans passed | **REPAIRED — INTEGRITY SCAN PASSED** |

## 14. Exact dependencies and remaining HE obligation

The proved chain is

\[
\{\text{HE-G0, score tails}\}
\to\text{HE-CLOSURE}
\to r_{\mu,n}
\to r_{F,n}
\to q_{R,n},
\]

\[
\text{finite-memory or product-PD producer}
\to\omega_n,
\]

\[
\{\omega_n,q_{R,n},\mathcal E_{2,n}\}
\to d_{{\rm samp},n}
\to\{d_{{\rm ideal},n},\eta_n,\text{loading/selectors}\}.
\]

The only exact open HE lemma in this dossier is HE-TRUNC, the unbounded-score/truncation and weaker generated-domain extension. It is consumed by no theorem. The repaired HE analytical package has passed the second hostile pass; application remapping and numerical-suite design remain outside this dossier and must follow the lead’s joint HE–BW adjudication.
