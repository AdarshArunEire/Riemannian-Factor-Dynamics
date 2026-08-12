---
type: proof-adjudication
title: FRAME-IF — closure adjudication
status: completed-noncanonical-adjudication
verdict: Gate A — dimension-uniform generic curved debiaser proved under explicit producer assumptions
scope: closure of FRAME-IF-POLY; Paper 2 excluded
---

# FRAME-IF — closure adjudication

> This is the lead's active proof record. Canonical files are not edited.

## 0. Completion rule

The campaign did not return Gate D. Its candidate rates were subjected to two hostile passes before the final adjudication in §17.

## 1. The obstruction in the old same-band score

For the positive three-scale mean with

\[
c=(1,1/2,1/4),\qquad \lambda=(1/3,-2,8/3),
\]

the population Richardson path has, generically,

\[
e_b^R(u)=b^3B_3(u)+o(b^3),\qquad
\sum_j\lambda_jc_j^3=\frac18.
\tag{1.1}
\]

A validation score using the same stage bandwidths is centred at the corresponding smoothed barycentres. It cannot estimate the displacement of those barycentres from the true pointwise mean. Consequently a same-band correction retains \(b^3K[B_3]\), which is \(n^{-3/7}\) at \(b=n^{-1/7}\) when the curved frame derivative is nonzero. This attacks the old formula, but not an independently undersmoothed validation path.

## 2. Undersmoothed two-path estimator

Let

\[
b_n=n^{-1/7},\qquad \ell_n=n^{-3/7},\qquad
M_n\asymp \ell_n^{-2/3}=n^{2/7},
\tag{2.1}
\]

and choose

\[
c_n=n^{-\gamma},\qquad \frac16<\gamma<\frac3{14}.
\tag{2.2}
\]

Assume additionally that the validation-law local-stationarity, design, mask, and coupling bias is \(o(n^{-1/2})\). A sufficient canonical power condition is \(a>1/2\); exact proxy stationarity is another. This is a real restriction: the old baseline \(a\ge3/7\) can leave an uncancelled first-order \(n^{-a}\) validation bias.

For one cyclic assignment of three exactly separated finite-memory folds:

1. fold \(T\) computes the positive three-scale pilot vertices \(\widehat q^T=(\widehat q_j^T)_{j=0}^{M}\) at bandwidth \(b_n\);
2. fold \(V\) computes independent positive three-scale validation vertices \(\check q^V=(\check q_j^V)_{j=0}^{M}\) at bandwidth \(c_n\);
3. fold \(E\) computes the masked polygon lag row \(\widehat{\mathfrak T}_E(q)\) and its exact vertex derivative by ordered Jacobi differentiation.

Put

\[
d_j^{TV}=\log_{\widehat q_j^T}\check q_j^V
\in T_{\widehat q_j^T}M
\tag{2.3}
\]

and define

\[
\boxed{
\widehat{\mathfrak T}^{2p}_{T,V,E}
=\widehat{\mathfrak T}_E(\widehat q^T)
+D\widehat{\mathfrak T}_E(\widehat q^T)[d^{TV}].}
\tag{2.4}
\]

Average (2.4) over the three cyclic role assignments. All rows use the same declared finite-array mask. The formula uses no true mean, true frame, true anchor alignment, population lag row, Hessian inverse, or unobserved ribbon. Every derivative in (2.4) is computed along the fitted polygon.

The sign is forced. If \(e^T_j=\log_{q_j}\widehat q_j^T\) and \(v^V_j=\log_{q_j}\check q_j^V\), radial comparison gives

\[
d_j^{TV}=v_j^V-e_j^T+O(\|e_j^T\|^2+\|v_j^V\|^2).
\tag{2.5}
\]

Thus the plus derivative in (2.4) cancels the pilot displacement and leaves the independently estimable validation displacement.

## 3. Geometric coordinate sensitivity

Write \(K_j=D_{q_j}\mathfrak T_n(q^0)\), with domain \(T_{q_j}M\) and codomain \(\oplus_{h\le h_0}\mathcal S_2(H_0)\). On a generated tube with bounded speed, acceleration, curvature, two Jacobi derivatives, lag count, and total tangent energy,

\[
\boxed{\|K_j\|_{op\to\oplus HS}\le \frac{C}{M}.}
\tag{3.1}
\]

To prove (3.1), apply the fixed-fibre cell formula

\[
\mathcal P'_0=-E_bP+PE_a+\int P_{b\leftarrow s}R(T,V)P_{s\leftarrow a}\,ds.
\tag{3.2}
\]

For an internal vertex, the terminal generator of the preceding cell cancels the initial generator of the next cell under the same radial connector convention. The remaining curvature integrals occupy at most two cells, each of global parameter length \(M^{-1}\), while \(\|T\|\), curvature, and Jacobi interpolation are uniformly bounded. Therefore its effect on the transported vector at every later time is \(C\|v_j\|/M\). The base-log derivative is nonzero only for observations interpolated in the two adjacent cells, a fraction \(O(M^{-1})\) of the row. Lag products double these two bounds and bounded total energy converts them to HS norm. At the anchor, compare the varying output fibres by the radial connector \(C_0^s:T_{q_0}M\to T_{q_0(s)}M\). Its fixed-fibre endpoint generator is zero, so the apparent order-one change is a common coordinate motion; only the first-cell curvature integral and first-cell observations remain, both \(O(M^{-1})\). At the terminal vertex only an \(O(M^{-1})\) fraction of rows is affected. Partial cells obey the same bound.

The twice differentiated ordered product also gives the conservative bilinear bound

\[
\|D^2\mathfrak T_n(q)[v,w]\|_{\oplus HS}
\le CM\|v\|_{2,M}\|w\|_{2,M},
\quad
\|v\|_{2,M}^2=(M+1)^{-1}\sum_j\|v_j\|^2.
\tag{3.3}
\]

This retains the established polygon remainder \(M\|v\|_{2,M}^2+M^{-2}\); no \(O(\ell^2)\) shortcut is used.

## 4. Dimension-free validation stability and bias

Let \(r_{V,n}=(nc_n)^{-1/2}+c_n^3+\rho_{LS,n}\). Apply the positive-weight Sturm reduction separately to the three stage barycentres, followed by the explicit Richardson post-map

\[
R(q_1,q_2,q_3)=\operatorname{Exp}_{q_1}
\left(\sum_{s=1}^3\lambda_s\log_{q_1}q_s\right).
\]

The generated-tube package includes bounded first and second differentials of \(R\), so replacement stability and the expectation expansion are fixed multiples of the three stage bounds. Consequently

\[
\|v^V\|_{2,M}=O_p(r_{V,n}),\qquad
\|v^V\|_{\infty}=O_p(\sqrt M\,r_{V,n})=o_p(1).
\tag{4.1}
\]

For a local positive barycentre, one observation has normalised weight at most \(C/(nc_n)\). Replacing that observation changes the empirical score by at most \(C/(nc_n)\); uniform strong convexity therefore changes the barycentre by at most the same order. The Richardson post-map multiplies this by only \(\|\lambda\|_1\) and fixed geometry constants.

By (3.1), one validation observation affects \(O(Mc_n)\) vertices and changes the aggregate linear correction by at most

\[
(Mc_n)\frac{C}{M}\frac{C}{nc_n}=\frac{C}{n}.
\tag{4.2}
\]

Block Efron--Stein over the fixed dependence colours now gives

\[
\left\|K[v^V]-E K[v^V]\right\|_{\oplus HS}=O_p(n^{-1/2})
\tag{4.3}
\]

without an ambient-dimension net or an operator/HS substitution.

The expectation is second order around the population local barycentre. Indeed, delete the fixed dependence block containing observation \(i\). The leave-block-out barycentre is independent of its score/Hessian contribution and differs from the full barycentre by \(C/(nc_n)\). In the Karcher Taylor equation the centred linear score has expectation zero; replacing the estimator by its leave-block-out version bounds the Hessian--estimator covariance by \(C/(nc_n)\), and the quadratic Taylor remainder by the same effective-weight sum. Hence, uniformly in \(j\),

\[
\left\|E v_j^V-B_{3,j}c_n^3\right\|
\le C\{(nc_n)^{-1}+\rho_{LS,n}\}.
\tag{4.4}
\]

Combining (3.1) and (4.4),

\[
\|E K[v^V]\|_{\oplus HS}
\le C\{c_n^3+(nc_n)^{-1}+\rho_{LS,n}\}.
\tag{4.5}
\]

Second-order replacement differences are supported only when two observations share a local window. Uniform strong convexity and the bounded second differentials of the barycentre and Richardson maps give a mixed replacement difference at most \(C/(n^2c_n)\) after aggregate action. There are \(O(n^2c_n)\) overlapping pairs. The second-order Efron--Stein/Hájek projection inequality therefore bounds the degenerate remainder's standard deviation by

\[
\left\{O(n^2c_n)\frac{C^2}{n^4c_n^2}\right\}^{1/2}
=\frac{C}{n\sqrt{c_n}}=o(n^{-1/2}).
\tag{4.6}
\]

Thus (4.3) admits a direct-sum HS asymptotic-linear representation; its population summand is the inverse-Karcher local score weighted by the coordinate maps \(K_j\), and its empirical infinitesimal-jackknife version is observable from the fitted barycentres and fitted Jacobi derivatives.

## 5. Cancellation and remainder calculation

Taylor expansion of the two terms in (2.4), using (2.5) and (3.3), yields pathwise

\[
\widehat{\mathfrak T}^{2p}_{T,V,E}
=\widehat{\mathfrak T}_E(q^0)
+D\widehat{\mathfrak T}_E(q^0)[v^V]+R_{T,V,E},
\tag{5.1}
\]

where

\[
\|R_{T,V,E}\|_{\oplus HS}
\le C\left[
M\{\|e^T\|_{2,M}^2+\|e^T\|_{2,M}\|v^V\|_{2,M}+\|v^V\|_{2,M}^2\}
+M^{-2}
\right].
\tag{5.2}
\]

Conditional on \(V\), exact separation and bounded finite-memory HS concentration give

\[
\|(D\widehat{\mathfrak T}_E-D\mathfrak T_n)[v^V]\|_{\oplus HS}
=O_p(n^{-1/2}r_{V,n}).
\tag{5.3}
\]

The oracle evaluation row is \(O_p(n^{-1/2})\). Combining (4.3)--(5.3), the post-influence nuisance remainder is bounded by

\[
\begin{aligned}
d_{F,db,n}\le O_p\big[&M\ell_n^2+M\ell_nr_{V,n}+Mr_{V,n}^2+M^{-2}\\
&+c_n^3+(nc_n)^{-1}+n^{-1/2}r_{V,n}+\rho_n\big].
\end{aligned}
\tag{5.4}
\]

With (2.1)--(2.2), and \(\rho_n=o(n^{-1/2})\),

\[
\begin{array}{c|c}
\text{term}&\text{order exponent at }c=n^{-\gamma}\\ \hline
M\ell^2,\ M^{-2}&n^{-4/7}\\
M\ell r_V&n^{-9/14+\gamma/2}\\
Mr_V^2&n^{-5/7+\gamma}\\
c^3&n^{-3\gamma}\\
(nc)^{-1}&n^{-1+\gamma}.
\end{array}
\tag{5.5}
\]

Every exponent is strictly smaller than \(-1/2\) exactly when
\(1/6<\gamma<3/14\). Therefore (5.4) is \(o_p(n^{-1/2})\).

## 6. Gauge, targets, and downstream consumers

Under a common anchor basis change \(Q\), the base row and its derivative in (2.4) both transform blockwise as \(B_h\mapsto QB_hQ^*\). The radial anchor connector removes the common endpoint generator; no time-varying component is quotiented. Hence the estimator is common-gauge equivariant.

The cyclic masks define one exact finite-array target. Any comparison with the unmasked row is paid as \(\rho_{mask,n}\). Direct lag-law sampling remains in the oracle evaluation row. Mean/base-log and non-rigid frame pieces remain separate components of the same derivative; the correction does not relabel GLO error as frame error.

If the hostile audits accept Sections 3--5, then

\[
d_n^{db}=O_p(n^{-1/2}),
\tag{6.1}
\]

and the existing deterministic consumers give, whenever
\(2A_{2,n}d_n^{db}+(d_n^{db})^2=o_p(\Delta_n)\),

\[
\|\sin\Theta(\widehat E_n^{db},E_n)\|_{op}
=O_p(n^{-1/2}/\Delta_n),\qquad
\widehat\lambda_{r+1,n}^{db}=O_p(n^{-1}).
\tag{6.2}
\]

## 7. Proved finite-dimensional fallback

Independently of the two-path audit, the B/C dossiers prove a finite-dimensional complete one-step theorem: a regular parametric mean path, computable curved geometry, fixed nuisance dimension, and a bounded invertible global estimating equation give nuisance remainder

\[
O_p(n^{-1}+M_n/n+M_n^{-2})
\tag{7.1}
\]

with \(M_n\asymp n^{1/3}\). The sharper explicit C construction is on \(\mathbb H^2_{-1}\times\mathbb R\): the Euclidean product coordinate supplies an observable noisy scalar mean parameter, while a bounded one-dependent rank-one signal in the hyperbolic tangent factor produces a nonzero, time-varying curvature-frame derivative. Its estimator

\[
\widehat\Gamma_n^{db}
=\widehat T_E(\widehat\theta_T)
-\dot{\widehat T}_E(\widehat\theta_T)
(\widehat\theta_T-\widehat\theta_V)
\tag{7.2}
\]

has the exact expansion

\[
\widehat\Gamma_n^{db}-\Gamma_1
=N_E^{-1}\sum_{t\in E}\{g_t(\theta)-Eg_t(\theta)\}
+K_{n,\theta}N_V^{-1}\sum_{t\in V}\eta_t+R_n,
\quad \|R_n\|_{HS}=O_p(n^{-1}).
\tag{7.3}
\]

All quantities in (7.2) are observable from the known path family and known product geometry. Common anchor changes conjugate both terms. This proves a nonflat, genuinely non-rigid Gate-B result even if the generic two-path theorem is rejected.

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS**, accepted again by the fresh complete-chain hostile pass.

## 8. Audit ledger

| Claim | Attack | Repair or counterexample | Checker | Final status | Consequence |
|---|---|---|---|---|---|
| same-band score removes pilot bias | stage scores centre at smoothed means | use independent \(c_n\)-undersmoothed path | C, pass 1 | DISPROVED | old score formula cannot be reused |
| one-vertex sensitivity is \(C/M\) | endpoint generators may be order one | radial fixed-fibre anchor comparison and adjacent-cell telescoping | C, pass 1 | PROVED UNDER EXPLICIT ASSUMPTIONS | supplies (4.2) |
| validation aggregate is root-\(n\) | pointwise rate is only \((nc)^{-1/2}\) | single replacement \(C/n\), double replacement \(C/(n^2c)\), Hájek remainder \(C/(n\sqrt c)\) | C, pass 1 | PROVED UNDER EXPLICIT ASSUMPTIONS | removes grid cost |
| validation expectation is second order | empirical barycentre may be biased | leave-block-out Hessian covariance plus uniform \(C^2\) Richardson map | C, pass 1 | PROVED UNDER EXPLICIT ASSUMPTIONS | removes \((nc)^{-1/2}\) bias |
| full correction preserves target | fold masks may differ | identical within-core masks, phase balance, explicit defect | C, pass 1 | PROVED UNDER EXPLICIT ASSUMPTIONS | no silent estimand change |

## 9. Closed theorem

> **Theorem FRAME-2P-U — dimension-uniform undersmoothed two-path polygon debiasing.** Let \(p=p_n\) be arbitrary while \(h_0,m_0\) remain fixed. Assume uniformly in \(n,p_n\): bounded total tangent energy; exact GLO and included-lag factorisation; a \(C^4\) mean/law; unique means with Karcher strong convexity bounded below by \(mI\); and a known compact generated tube on which the score Hessian derivative, first two barycentre replacement derivatives, Exp, Log, the three-stage Richardson post-map, chord PT/Jacobi maps, and the first two complete masked-row polygon variations have bounded operator norms. Assume \(\max_j\|K_{n,j}\|\le C/M_n\), \(\sum_j\|K_{n,j}\|\le C\), and the dimension-uniform single/double aggregate replacement bounds \(C/n\) and \(C/(n^2c_n)\) derived in §§3--4. Use deterministic superblocks whose training, validation, and evaluation cores have disjoint innovation sigma-fields, gaps at least \(m_0+h_0\), and phase-balanced within-core masks for one common finite-array target. Assume exact local-law sampling, or \(a>1/2\) with all coupling, design, and mask comparisons \(o(n^{-1/2})\). Let
>
> \[
> b_n=n^{-1/7},\qquad M_n\asymp n^{2/7},\qquad
> c_n=n^{-\gamma},\quad \frac16<\gamma<\frac3{14}.
> \]
>
> Then the entirely observable estimator (2.4), averaged over cyclic fold roles, is common-gauge equivariant and has
>
> \[
> \widehat{\mathfrak T}^{2p}_n-\mathfrak T_n
> =\mathbb G_{E,n}[Z]+\mathbb G_{V,n}[\varphi_c]+R_n,
> \tag{9.1}
> \]
>
> where both centred direct-sum Hilbert--Schmidt rows are \(O_p(n^{-1/2})\), while
>
> \[
> \begin{aligned}
> \|R_n\|_{\oplus HS}=O_p\{&M_n(r_T^2+r_Tr_V+r_V^2)+M_n^{-2}
> +c_n^3+(nc_n)^{-1}\\
> &+(n\sqrt{c_n})^{-1}+n^{-1/2}r_V\}
> +O(n^{-a})+\rho_{mask,n}+\rho_{CF,n},
> \end{aligned}
> \tag{9.2}
> \]
>
> with \(r_T=n^{-3/7}\) and \(r_V=c_n^3+(nc_n)^{-1/2}\). Every term in (9.2) is \(o_p(n^{-1/2})\). The validation influence in (9.1) is leading sampling noise, not part of \(d_{F,db,n}\). Consequently
>
> \[
> d_{F,db,n}=o_p(n^{-1/2}),\qquad
> \|\widehat{\mathfrak T}^{2p}_n-\mathfrak T_n\|_{\oplus HS}=O_p(n^{-1/2}).
> \tag{9.3}
> \]

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.** This is Gate A. Every constant is uniform in \(p_n\), and the theorem is uniform over all curved triangular laws satisfying the displayed producer package. Bounded total energy alone is not claimed to imply that package.

### Proof compression

The proof has five noninterchangeable steps.

1. Radial connector comparison gives
   \(d^{TV}=e_V-e_T+O(e_T^2+e_V^2)\); hence the plus derivative in (2.4) cancels the complete pilot first variation, including both base-log/Hessian and non-rigid frame/Jacobi pieces.
2. Matched cell endpoint generators cancel. Each vertex retains two length-\(M^{-1}\) curvature integrals and \(O(M^{-1})\) local row mass, so \(\max_j\|K_j\|\le C/M\) and \(\sum_j\|K_j\|\le C\). The radial fixed-fibre argument supplies the same bound at the moving anchor.
3. One validation observation has aggregate action \(C/n\). Overlapping double replacements have action \(C/(n^2c)\), with \(O(n^2c)\) such pairs, so the validation action is a root-\(n\) Hájek projection plus \(O_{L^2}(1/(n\sqrt c))\). Leave-block-out Karcher expansion bounds its expectation by \(c^3+(nc)^{-1}\).
4. The full second polygon variation is \(CM\|v\|_{2,M}\|w\|_{2,M}\), giving (9.2). Direct exponent substitution yields the nonempty window \(1/6<\gamma<3/14\).
5. Every stochastic bound is a Hilbert or direct-sum HS squared-norm replacement inequality. No sphere net, coordinate maximum over \(p_n\), or full Hessian operator estimate appears. The tube maximum pays \(\sqrt M\), and \(\|x\otimes y\|_{HS}=\|x\|\|y\|\) converts bounded total energy without a rank factor.

No true centre, frame, anchor alignment, ribbon, \(e\), \(\Omega\), population Hessian, or population lag row appears in the computation.

## 10. What was disproved

The old identically smoothed score correction is not the theorem above. If validation uses the same bandwidth stages as the pilot, every validation score is centred at its smoothed population barycentre. The three-scale weights satisfy

\[
\sum_s\lambda_sc_s^3=\frac18,
\]

so a generic curved moving mean leaves \(b_n^3K[B_3]\). On the explicit constant-curvature noncommuting lag row in B §2, this has norm bounded below by \(cn^{-3/7}\). It is larger than root-\(n\).

**Status: DISPROVED** for the identically smoothed score-only construction. This is an estimator-class counterexample, not a generic impossibility theorem.

The attempted generic growing-dimensional impossibility is **SUPERSEDED**. Full empirical Hessian operator recovery can pay an entropy cost, but FRAME-2P-U uses only dimension-uniform composed actions and replacement inequalities. No generic impossibility theorem is claimed.

## 11. Independent finite-dimensional fallback

FRAME-IF-C Theorem IF-C1 provides a second, logically independent closure on \(\mathbb H^2(-1)\times\mathbb R\). The Euclidean product coordinate observes \(\theta+\eta_t\), giving an explicit scalar training/validation producer, while the hyperbolic factor has a moving nongeodesic mean and a nonzero time-varying curvature-frame coefficient. Its observable row satisfies

\[
\widehat\Gamma_n^{db}-\Gamma_1
=N_E^{-1}\sum_{t\in E}\{g_t(\theta)-Eg_t(\theta)\}
+K_{n,\theta}N_V^{-1}\sum_{t\in V}\eta_t+R_n,
\qquad \|R_n\|_{HS}=O_p(n^{-1}).
\tag{11.1}
\]

**Status: PROVED UNDER EXPLICIT ASSUMPTIONS.** This Gate-B fallback survives even if an application cannot verify the full dimension-uniform FRAME-2P-U producer package.

## 12. Mean, frame, nuisance, and target ledger

| Nuisance/target | First-order object | Observable correction | Residual/status |
|---|---|---|---|
| mean/base-log error | \(-H_te_t\) in each lag factor | base-log part of \(D\widehat{\mathfrak T}_E[d^{TV}]\) | pilot term cancels; validation influence leads; remainder (9.2) |
| non-rigid frame | \(\Omega_t\Gamma_{t,h}-\Gamma_{t,h}\Omega_{t-h}\) | ordered polygon Jacobi/connector part of the same derivative | pilot term cancels; no pointwise truth-frame estimate |
| common rigid gauge | common conjugation | radial fixed-fibre convention; conjugate base row and correction together | zero additive error |
| direct lag law | centred evaluation lag products | \(\mathbb G_E[Z]\) | root-\(n\) leading row |
| validation sampling | aggregate inverse-Karcher action | \(\mathbb G_V[\varphi_c]\) | root-\(n\) leading row, not \(d_{F,db}\) |
| oracle target | true-anchor masked finite-array row | compared modulo one common conjugation | unchanged estimand |
| feasible row | pilot polygon row | contains time-varying first-order contamination | debiased by (2.4) |
| invariant-only target | spectra/singular values | not used | changes the estimand; DISPROVED |

## 13. Downstream Paper 1 result

With GLO, exact included-lag factorisation, and all defects in (9.2) sub-root-\(n\),

\[
d_n^{db}=O_p(n^{-1/2}).
\tag{13.1}
\]

Let \(A_{2,n}^2=\sum_h\|\Gamma_h\|_{op}^2\), used only at assembly. If

\[
2A_{2,n}d_n^{db}+(d_n^{db})^2=o_p(\Delta_n),
\tag{13.2}
\]

then the existing deterministic consumers give

\[
\|\sin\Theta(\widehat E_n^{db},E_n)\|_{op}
=O_p(n^{-1/2}/\Delta_n),\qquad
\widehat\lambda_{r+1,n}^{db}\le(d_n^{db})^2=O_p(n^{-1}).
\tag{13.3}
\]

Threshold factor selection requires \(n^{-1}=o(\tau_n)\ll\Delta_n\). The unregularised eigenvalue ratio remains **DISPROVED** under only a null-spectrum upper bound. Frame coefficients use \(G_{2,HS,n}\), never operator lag energy without rank control.

## 14. Hostile audit adjudication

Pass 1 was three-sided: C attacked B and the lead; A attacked B's connector, anchor, and polygon claims; B attacked A's observability, score producer, masks, and rates. Accepted objections forced the radial anchor proof, \(C^2\) Richardson condition, double-replacement/Hájek calculation, mixed \(Mr_Tr_V\) term, exact masks, \(a>1/2\) restriction, explicit product-coordinate witness, and removal of the invalid growing-dimensional impossibility.

The fresh C pass 2 in §12 rechecked every fixed-dimensional link, and its completion-audit §13 independently rechecked the dimension-uniform promotion; B §11 and A §10 supplied separate statistical and geometric audits. Every Gate-A link is **PROVED UNDER EXPLICIT ASSUMPTIONS**. The same-band construction is **DISPROVED**. The former high-dimensional negative claim is **SUPERSEDED**. There is no remaining open lemma in this campaign.

## 15. Application boundary

Newly enabled:

- arbitrary \(p_n\) known curved geometry with a \(C^4\) nonparametric moving mean, exact local law or \(a>1/2\), and dimension-uniform generated-tube, composed-action, and single/double replacement producers;
- the explicit hyperbolic-product parametric family of C, with \(O_p(n^{-1})\) post-influence residual;
- fixed-dimensional special homogeneous geometries satisfying the same generated-tube and mask package;
- \(\mathbb H^2(-1)\times\mathbb R^{p_n-2}\), which supplies a nonempty genuinely non-rigid growing-dimensional witness.

Still excluded:

- growing \(p_n\) when the dimension-uniform composed-action and replacement producers fail or are not verified;
- the old baseline with only \(a\ge3/7\) when its coupling defect enters first order;
- infinite memory, growing energy/rank/lag count, shrinking gap/margin, or uncontrolled high-frequency mean paths;
- arbitrary external frame rules not generated by the declared Levi--Civita polygon.

The robust \(n^{-3/7}\) Paper 1 theorem remains unchanged outside the FRAME-2P-U package.

## 16. Proposed canonical migration table

| Canonical file | Proposed replacement | Proven producer | Status effect |
|---|---|---|---|
| `Analytical reconstruction — proof ledger and rebuilt spec.md` | replace FRAME-IF open node by Gate-A FRAME-2P-U theorem and same-band counterexample; retain robust fallback | this adjudication §§9--10 + A §10/B §11/C §13 | dimension-uniform oracle branch added under producer package |
| `Application map — geometry, symmetry, and rate accelerators.md` | add the two-path bandwidth window, exact-law/\(a>1/2\), uniform replacement-action checks, and padded hyperbolic-product witness | B §§2A,11; C §§2--5,13 | generic curved applications enabled conditionally |
| `OPEN OBLIGATIONS — current research actions.md` | close FRAME-DB/FRAME-IF; list application-specific verification of uniform producer constants as theorem checking, not an open baseline lemma | this adjudication | no FRAME-IF lemma remains open |
| `Paper 1 — Locally stationary Riemannian factor model.md` | add uniform theorem (9.1)--(9.3), loading/null corollary (13.3), and correction-noise convention | this adjudication | oracle numerator under explicit Gate-A producer package |
| `Time-varying Fréchet mean Riemannian factor model.md` | distinguish same-band failure from undersmoothed two-path success | §§9--10 | correct estimator boundary |

No change is proposed to HD1's robust theorem, G1's proved mean rates, Paper 2, or the numerical suite.

## 17. Final verdict

**Gate A — generic curved debiaser proved under explicit dimension-uniform producer assumptions.** FRAME-IF-POLY is closed by Theorem FRAME-2P-U uniformly over arbitrary-\(p_n\) curved triangular laws satisfying its generated-tube, composed-action, replacement, mask, and dependence package. Its post-influence frame/mean nuisance residual is \(o_p(n^{-1/2})\), its row is root-\(n\) in direct-sum HS norm, and its loading/null consequences are (13.3). The padded \(\mathbb H^2(-1)\times\mathbb R^{p_n-2}\) model is a genuinely curved, non-rigid, growing-dimensional witness. An explicit parametric construction independently has \(O_p(n^{-1})\) residual. No lemma remains open.
