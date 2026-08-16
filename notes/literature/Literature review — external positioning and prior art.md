---
type: canonical-literature-review
title: Literature review — external positioning and prior art
status: active
last-audited: 2026-08-16 (§2.4–§2.8 added)
authority: field map, prior-art comparison, and the novelty-claim boundary
---

# Literature review — external positioning and prior art

> **Scope, and how this differs from [[References and external claim audit]].** That file is an *attribution ledger*: for each claim the project consumes, which external source supplies it and under what restriction. This file is the *field map*: what already exists, how Paper 1 sits against it, and which novelty claims are defensible. Neither supersedes the other and neither carries theorem status — [[Analytical reconstruction — proof ledger and rebuilt spec]] governs that. Where this file records an unresolved attribution question, the action belongs in [[OPEN OBLIGATIONS — current research actions]], not here.

## 0. Status of this review

Compiled 2026-08-16 from a targeted search, not an exhaustive one. Coverage is good for the Bures–Wasserstein / object-data / manifold-time-series neighbourhoods and thin for anything not indexed on arXiv. Several rows below are marked **UNVERIFIED** — they are sources identified as relevant but not yet read in full. Do not cite an UNVERIFIED row.

## 1. The four neighbourhoods

Paper 1 sits at the intersection of four literatures. Positioning must be done against each separately; being novel in one is not being novel overall.

| Neighbourhood | What it contains | Paper 1's relation |
|---|---|---|
| **N1 — manifold/object-valued time series factor models** | the parent: Huang, Chen & Chen (2026), arXiv:2607.28385 | direct extension; the fixed-centre assumption (P2) is what Paper 1 relaxes |
| **N2 — Bures–Wasserstein statistics for time-varying covariance** | Santoro & Panaretos (2024), arXiv:2310.13764; Masarotto–Panaretos–Zemel; Zemel–Panaretos (2019); Nguyen–Uribe (2026), arXiv:2604.03566; Xu–Li, JMLR 26(77) (2025) | **the principal prior-art risk** — see §2, §2.6, §2.8 |
| **N2b — time-varying latent factor structure on a manifold** | Peng & Shen (2026), arXiv:2605.18316 | constrains **Paper 2's** moving-loading novelty, not Paper 1's — see §2.7 |
| **N3 — object-data change points and time-varying random objects** | Dubey & Müller (AoS 2020, JASA 2023); Change-Point Detection for Object-valued Time Series (arXiv:2606.00858) | external evidence that Fréchet centres move; **motivation source, not competition** |
| **N4 — forecast evaluation under an imperfect proxy** | Patton (2011); Laurent–Rombouts–Violante (2013); Gneiting (2011) | producers for P1-LOSS; the matrix characterisation is LRV's |

A fifth, **N5 — long memory versus level shifts in realised volatility** (Diebold–Inoue; Granger–Hyung; Perron–Qu; Choi–Yu–Zivot), is not a competing literature but the correct *framing precedent*: it is the Euclidean instance of a non-separable drift/persistence confounding whose value lay in characterising the confounding and its forecasting consequences, not in resolving it. Paper 1's identification result is the manifold-valued analogue.

## 2. PRIOR-ART CASE — Santoro & Panaretos, *Statistical Inference for Bures–Wasserstein Flows* (arXiv:2310.13764v2, June 2024)

**This paper defines a time-varying Bures–Wasserstein barycentre and calls it the Fréchet mean flow. The terminology and the pointwise-reduction result are theirs and must be cited.** The object is nevertheless not Paper 1's moving centre. The distinction is structural, not cosmetic, and it must be stated explicitly in the introduction rather than left for a referee to raise.

### 2.1 What they do

- **Datum.** A random *flow* \(F=\{F_t\}_{t\in[0,1]}\), a covariance-operator-valued functional observation over a possibly infinite-dimensional Hilbert space.
- **Fréchet mean flow.** The minimiser of \(G\mapsto\mathbb E[d^2(G,F)]\) over continuous flows, under moment condition A(1) and the regularity condition A(2). Their **Lemma 1** proves the minimisation over whole flows reduces to *pointwise* BW barycentres, \(M_t=\arg\min_{G\in\mathcal K}\mathbb E[\Pi^2(G,F_t)]\), stitched into a continuous trajectory.
- **Sampling scheme.** \(n\) **i.i.d. replications** \(F_1,\dots,F_n\) of the flow. Assumption S(3) in the sparse regime states \(\{F_i\}\) and the design points are *totally independent across all indices*.
- **Second-order structure.** A tangent-bundle covariance and a Karhunen–Loève expansion — i.e. **functional PCA** on the log-lifted flows.
- **Rates.** \(d(M,\widehat M_n)=O_p(n^{-1/2})\) in \(n\) replicates (Theorem 1); in finite dimension a uniform \(\sup_t\mathbb E[\Pi^2]=O(n^{-1})\) under B(2) (Theorem 3); Local Fréchet Regression for the sparse longitudinal design at the standard local-regression rate (Proposition 5); PACE for scores.
- **Applications.** EEG, dynamic functional connectivity, and functional time series in the frequency domain via spectral density operators.

### 2.2 The decisive separation — replication versus a single path

| | Santoro–Panaretos | Paper 1 |
|---|---|---|
| observed data | \(n\) i.i.d. **replicate flows** | **one** realisation of a dependent series |
| where strength is borrowed from | across independent replicates at fixed \(t\) | across **neighbouring times**, under local stationarity |
| dependence | independence across replicates (S(3)) | serial dependence: finite memory, physical dependence, or mixing |
| asymptotics | \(n\to\infty\) replicates | \(n\to\infty\) time points, \(u_t=t/n\) |
| residual structure | **PCA / Karhunen–Loève** — contemporaneous covariance | **factor model** — lag-generated span \(\mathcal S_X=\operatorname{ran}\mathbb L_n\), \(\mathbb L_n=\sum_h\Gamma_n(h)\Gamma_n(h)^*\) |
| what identifies the low-rank object | variance | **autocovariance at nonzero lags** |
| drift/factor identification | **does not arise** | the core theorem (P1-ID) |
| forecasting and evaluation loss | not addressed | central (P1-LOSS, APP-FIN) |

**The point to make in the introduction, in one sentence:** with i.i.d. replicate flows the centre is identified by averaging *across replicates* at each fixed time, so drift and persistent residual dynamics are never confounded and no identification theorem is required. Paper 1 has a single path, must borrow strength from neighbouring times instead, and the confounding is created by exactly that substitution. ID-3's zero-frequency-atom condition and ID-7's modulus \(\psi^+(nb_n)\) are the quantitative form of a problem that **cannot arise in their sampling scheme**.

The second separation is equally clean: their residual analysis is PCA, driven by contemporaneous covariance. Paper 1 inherits the parent's lag-operator construction, so the low-rank object is driven by **autocovariance at nonzero lags**. A dynamically white but heavily loaded coordinate is inside their leading eigenspace and outside Paper 1's estimand by CANON-1. These are different targets, not different estimators of one target.

### 2.3 What must change in the canon

1. **Cite Lemma 1 wherever the pointwise reduction of a time-varying Fréchet centre is used or implied.** It is theirs. Do not present pointwise solvability as internal.
2. **Adopt or explicitly avoid their terminology.** "Fréchet mean flow" now denotes their object. Paper 1 should say *moving Fréchet centre* or *centre path* \(\mu_n(u)\) throughout and note the distinction on first use.
3. **The uniqueness attribution is RESOLVED against the project — see §2.4.**

### 2.4 RESOLVED — the ID-9 R2 uniqueness result is not novel

**Verdict: the internal proof is correct and not new. The novelty claim is retracted (C-AUDIT-11).**

The internal argument (P1-ID §14.2, route R2) proves uniqueness by exhibiting the variational identity

\[
\operatorname{tr}\big((A^{1/2}\Sigma A^{1/2})^{1/2}\big)
=\tfrac12\inf_{T\succ0}\big[\operatorname{tr}TA+\operatorname{tr}T^{-1}\Sigma\big],
\]

so that the functional is an infimum of maps affine in \(A\), hence concave in the **ordinary linear structure**; \(\Pi^2(\cdot,\Sigma)\) is therefore convex, with strictness from non-constancy of the optimiser \(T^\star(A)=A^{-1/2}(A^{1/2}\Sigma A^{1/2})^{1/2}A^{-1/2}\). It concludes uniqueness for every \(Q\) charging the full-rank cone.

**Santoro–Panaretos (arXiv:2305.15592v3), Theorem 1** states: a BW Fréchet mean of \(\Sigma\in\mathcal K(H)\), \(H\) separable and possibly infinite-dimensional, exists **if and only if** A(1) \(\mathbb E\|\Sigma\|_1<\infty\); and if additionally A(2) \(\mathbb P\{\Sigma\succ0\}>0\), it is **unique**. Their proof uses the same structural fact — convexity of \(\Pi^2\) under *ordinary* linear interpolation \(\lambda F_1+(1-\lambda)F_2\), taken from Masarotto–Panaretos–Zemel Proposition 10 — plus coercivity, weak lower semicontinuity, and weak compactness of Hilbert–Schmidt balls for existence; strictness follows by conditioning on \(\{\Sigma\succ0\}\).

Comparison:

| | internal R2 | Santoro–Panaretos Thm 1 | Kroshnin–Spokoiny–Suvorikova Thm 2.1 |
|---|---|---|---|
| regularity hypothesis | \(Q\) charges the full-rank cone | A(2): \(\mathbb P\{\Sigma\succ0\}>0\) — **the same condition** | minimal conditions |
| ambient space | fixed-size SPD matrices | **general separable \(H\), incl. infinite-dimensional** | \(\mathbb R^d\) |
| existence | not claimed | proved, as an **equivalence** with A(1) | proved |
| regularity of the barycentre | not claimed | Proposition 2 | proved |
| convexity route | explicit variational identity, elementary and self-contained | cites MPZ Proposition 10 for the same inequality | finite-dimensional argument |
| year | 2026 | 2023/2024 | 2021 (*Ann. Appl. Probab.*) |

Santoro–Panaretos further observe that A(2) is **not necessary** for uniqueness, giving the counterexample \(\Sigma=\operatorname{diag}(W,0)\), \(W\sim\chi^2_1\) on \(\mathbb R^2\). The internal statement is therefore strictly weaker than the published state of the art on both the space and the sharpness of the hypothesis.

**The error was the benchmark, not the proof.** Agueh–Carlier (2011) is a general Wasserstein-barycentre paper and was never the state of the art for the BW population barycentre; the internal claim of a "strict extension" is true of that citation and irrelevant against Kroshnin–Spokoiny–Suvorikova and Santoro–Panaretos.

**What survives.** The variational identity is a clean, self-contained, elementary derivation of the one convexity step that Santoro–Panaretos import from MPZ Proposition 10. It may be retained as a short appendix remark, explicitly labelled an alternative elementary route and not a new result — or dropped. **Nothing downstream changes.** ID-9's load-bearing content is route R3 (the latent-stochastic-centre crack), the non-existence of a *continuous* selector with its exact \(\lambda(1-\lambda)\Delta^2\) manufactured-drift cost, ID-7, ID-8, and R5. None of those appear in this literature, and none depends on R2 being internal.

### 2.5 Le Gouic–Paris–Rigollet–Stromme — comparison benchmark, NOT a competitor

An earlier draft of this file flagged LGPRS as a rate-level overlap risk on the strength of Santoro–Panaretos's one-line description of it ("a minimal eigenvalue gap condition"). **Reading the source overturns that.** The description is also terminologically misleading: LGPRS's hypothesis is a bound on the **condition number** of the covariances in the support — a spectral *band* — and has nothing to do with an eigen*gap* in the sense of the project's \(\Delta_n=\lambda_r(\mathbb L_n)-\lambda_{r+1}(\mathbb L_n)\), which is a gap in the spectrum of the **lag operator**, a different object entirely.

What LGPRS actually prove, in the BW instance (**Corollary 17**): let \(P\) be supported on non-degenerate Gaussians \(N(m,\Sigma)\) on \(\mathbb R^D\) with **every** \(\Sigma\) having eigenvalues in a fixed band \([\kappa_0,\kappa_1]\); set \(\kappa=\kappa_1/\kappa_0\) and assume \(\kappa-\kappa^{-1}<1\). Then the barycentre is unique and the empirical barycentre from \(n\) i.i.d. draws satisfies

\[
\mathbb E\,W_2^2(\mu_n,\mu_\star)\le\frac{4\sigma^2}{(1-\kappa+\kappa^{-1})^2\,n}.
\]

| | LGPRS Corollary 17 | Paper 1's BW packages |
|---|---|---|
| dimension | **fixed \(D\)** | \(m_n\to\infty\) (fixed-margin) and \(m_n=n^x\) (shrinking-margin) |
| where the spectral bound sits | **directly on the covariance matrices in \(\operatorname{supp}P\)** | on generated-domain spectral/polar/Exp/normal-pair margins |
| sampling | \(n\) **i.i.d.** draws from one fixed \(P\) | one dependent, locally stationary path |
| target | **one fixed** barycentre | a **moving** centre path \(\mu_n(u)\), plus a lag-factor loading space |
| margin behaviour | fixed band, condition number \(<\) golden ratio | fixed band **and** an explicitly shrinking branch \(\alpha_n\to0\) |
| what is estimated | the barycentre only | centre path, polygonal frame, lag operator, loading space, factor number |

Their headline is that the rate is **dimension-free** — the constant does not involve \(D\) — which is the opposite of a growing-dimension result: it is the escape from the \(n^{-1/D}\) curse of Ahidar-Coutrix–Le Gouic–Paris.

**Usable positioning, and it favours the project.** \(\kappa-\kappa^{-1}<1\) means every covariance in the support must have condition number below \(\varphi=(1+\sqrt5)/2\approx1.618\). That is a severe absolute restriction, and it is the published state of the art for *parametric* BW barycentre rates, in fixed dimension, with i.i.d. data, for the mean step **alone**. It is legitimate — and useful — to cite it as evidence that the project's generated-domain margin conditions are not unusually restrictive for this geometry, and that the shrinking-margin branch deliberately enters a regime this literature excludes by hypothesis.

**No overlap. Cite as comparison in the BW sections; no retraction follows.**

## 2.6 Nguyen & Uribe — signed BW barycentres. TWO citation sites, one of them possibly a producer

**Duc Toan Nguyen, César A. Uribe, *Fréchet Regression on the Bures-Wasserstein Manifold*, arXiv:2604.03566v1 [math.OC], 4 April 2026 (Rice University; preprint, not peer-reviewed).**

**Theorem 3.2 (Spectral Dominance of Positive Weights).** Let \(\Sigma_1,\dots,\Sigma_n\in S^d_{++}\) and \(\lambda_1,\dots,\lambda_n\in\mathbb R\) with \(\sum_k\lambda_k=1\), \(I=\{k:\lambda_k>0\}\), \(J=\{k:\lambda_k<0\}\). If

\[
\sum_{i\in I}\lambda_i^{+}\sqrt{\lambda_{\min}(\Sigma_i)}\;>\;\sum_{j\in J}\lambda_j^{-}\sqrt{\lambda_{\max}(\Sigma_j)},
\]

then \(\min_{S\in S^d_{++}}\sum_k\lambda_kW_2^2(S,\Sigma_k)\) admits a solution. **The eigenvalues carry square roots** — a condition stated without them is not their theorem. Proof route: Löwner–Heinz operator monotonicity of \(t\mapsto t^{1/2}\), then coercivity on the closed cone. Companion results: Proposition 3.3 (stationary points lie in an explicit two-sided spectral box), Proposition 3.4 (no local maxima), Proposition 3.7 (uniqueness under a small-ball condition, via Wintraecken Thm 3.4.9), Lemma 3.5 (sectional curvature at \(\Sigma\) bounded above by \(3/(2\lambda_{\min}(\Sigma))\)), Lemma 3.6 (injectivity radius of \(\{\lambda_{\min}\ge\lambda\}\) equals \(\sqrt\lambda\), from Luo et al. 2021 Thm 6).

**Their setting.** I.i.d. regression pairs \((X_k,Y_k)\), Euclidean covariate, **global** Fréchet regression in the sense of Petersen–Müller, weights \(s_G(x)=1+(X-\mu)^\top\Sigma^{-1}(x-\mu)\) affine in \(x\). Negative weights arise from **extrapolation beyond the covariate range** and do not shrink. No local stationarity, no bandwidth asymptotics, no dependent data; the paper is math.OC and its second half is projection-free Riemannian optimisation.

### 2.6.1 Against CE-9 — different geometry, different pathology, complementary results

| | CE-9 (internal) | Nguyen–Uribe Example 3.1 / Thm 3.2 |
|---|---|---|
| manifold | \(\mathbb H^2\) — **Hadamard, negatively curved** | BW \(S^d_{++}\) — **nonnegatively curved** |
| where the negative weights come from | **forced** by degree-\(d\ge2\) local-polynomial exact reproduction, \(\sum_tw_t(u)(u_t-u)^2=0\) | **extrapolation** past the covariate range in global Fréchet regression |
| failure mode | objective is **coercive**; minimisers exist but are **non-unique** (two global minimisers by reflection symmetry); Hessian can be indefinite, e.g. \(\operatorname{diag}(2,-5.9798)\) for weights \((3,-2)\) | objective **loses coercivity**; **no critical point exists** and minimising sequences drift to the PSD boundary |
| the sufficient condition | \(\tfrac12\operatorname{Hess}\hat F_u\succeq[W^+-\zeta(2\rho)W^-]\mathrm{Id}\), \(\zeta(r)=\sqrt{\bar K}r\coth(\sqrt{\bar K}r)\) — curvature-and-radius weighted, for **Hessian positivity** | spectral dominance above — eigenvalue weighted, for **coercivity** |
| asymptotic status | **withdrawn as a hypothesis** by SW-AS; survives only as a finite-\(n\) sufficient condition for *global* rather than localised uniqueness | a standing hypothesis; their weights do not vanish |

**The mechanism that separates them, and it is the sentence to write.** Under local stationarity with \(b\to0\), the positively- and negatively-weighted observations are drawn from laws converging to a **common** limit \(P_u\) at rate \(O(b)\). Theorem SW-AS then gives

\[
\sup_{u}\sup_{q\in\bar B(\mu(u),\rho)}\Big\|\tfrac12\operatorname{Hess}_q\hat F_u-H_{P_u}(q)\Big\|_{\rm op}
=O_p\Big(W\big[b+n^{-a}+\sqrt{\tfrac{p+\log n}{nb}}\big]\Big)\to0,
\]

with **no condition relating curvature, support radius and negative mass**. Nguyen–Uribe's negative weights are generated by a *fixed* extrapolation distance and never become benign; the project's are generated by a *shrinking* bandwidth and do. That is a clean, citable contrast — and it is a point in the project's favour, not against it.

**Caveat that must be stated with it.** SW-AS is proved on **Hadamard** manifolds (it consumes \(H_{P_u}\succeq\mathrm{Id}\) via T-EXT-1). BW is **nonnegatively** curved, so SW-AS does **not** transfer to the BW branch as written. Do not present the signed local-polynomial route as covering the flagship covariance application.

### 2.6.2 The second citation site — the BW Richardson safeguard. Possibly a producer, not a comparison

This is the connection not yet recorded anywhere in the canon. The three-scale mean estimator combines positive barycentres with **signed** Richardson coefficients \(\lambda=(1/3,-2,8/3)\). The canon already records, independently, that

- **unsafeguarded Richardson images are a disproved/retracted construction** (OPEN OBLIGATIONS §0.5), and
- the fixed-size BW estimator therefore carries a **generated-set membership test with deterministic fallback** and a **reconstruction full-rank safeguard**, and
- **N-12** is designed precisely around "positive diagonal roots whose signed extrapolation reaches zero — raw correction exits the domain".

That is the *same geometric fact* Nguyen–Uribe formalise: a **signed affine combination of SPD matrices can leave the cone / lose coercivity**. The project found it as a Richardson-extrapolation failure; they found it as a regression-extrapolation failure. It must be cited there, not only beside CE-9.

**And it may be more than a citation.** The current safeguard is a *runtime* admissibility test with fallback. Theorem 3.2 is a **verifiable a-priori condition** on the spectra and weights. Whether it can supply a checkable sufficient condition for the Richardson step — replacing or supplementing the membership test — is an open question worth one afternoon. Routed to the live queue.

## 2.7 Peng & Shen — the constraint on *moving-loading* novelty (Paper 2, not Paper 1)

**Chuansen Peng, Xiaojing Shen, *Dynamic Elliptical Graph Factor Models via Riemannian Optimization with Geodesic Temporal Regularization*, arXiv:2605.18316v1 [cs.LG], 18 May 2026 (Sichuan University).**

DEGFM models a sequence of time-varying **precision** matrices as low-rank-plus-diagonal \(\Theta_t=Y_tY_t^\top+D_t\), estimated on the product quotient manifold \(\prod_tB_{p,r}/O_r\) — the \(O_r\) gauge on the factor matrix is exactly a Grassmann-type quotient. Temporal coherence is imposed by a geodesic penalty; note that despite the abstract's "geodesic penalty defined on the Grassmann manifold", §III-C actually penalises \(d^2_{S^p_{++}}(\Theta_t,\Theta_{t+1})\), the **AIRM** distance on the reconstructed precision matrices. Theory: convergence to a stationary point (Thm V.1) and a non-asymptotic bound \(O(p_{\rm eff}\log p/n_{\min})\) with an explicit statistical-error / smoothing-bias split (Thm V.2), plus edge recovery under a beta-min condition.

**Consequence, and it is real:** *"the first model with a time-varying factor subspace on a manifold"* is **no longer safe wording**. But the collision is with **[[Paper 2 — Moving loading subbundle]]**, not Paper 1 — Paper 1's loading space is covariantly constant and its moving object is the *centre*.

What they do **not** have: any Fréchet mean or barycentre; any moving base point or tangent space \(T_{\mu(u)}M\); any transport between tangent spaces; any lag operator — their factor comes from a per-window likelihood, not from autocovariance; any local-stationarity asymptotics — they observe \(n_t\) **i.i.d.** samples per window; any identification theory. It is an optimisation paper with a finite-sample bound.

**Net: they are close to complementary to Paper 1** (moving subspace, fixed centre, per-window i.i.d. versus fixed subspace, moving centre, single dependent path), and directly adjacent to Paper 2.

## 2.8 Xu & Li — BW Fréchet regression inference

**H. Xu and H. Li, *Wasserstein F-tests for Fréchet regression on Bures-Wasserstein manifolds*, Journal of Machine Learning Research 26(77) (2025), 1–123** — note this is **published**, not a preprint. Covariance-matrix responses, regression target formulated as a conditional BW Fréchet mean, uniform-in-covariate rates, CLT and F-tests. Nguyen–Uribe record that Xu–Li and Kroshnin et al. "assume the existence of the regression estimator without deriving the geometric conditions required for signed weights."

The statistical problem differs on the same axis as everything else in N2: i.i.d. regression pairs \((X_i,Y_i)\) versus a dependent, locally stationary array \(X_{t,n}\). **Cite as BW Fréchet-regression inference prior art; not a local-time-series result.**


## 3. Open attribution checks — route to the live queue

| # | Source | Why it matters | Status |
|---|---|---|---|
| L-1 | Masarotto, Panaretos & Zemel (2019), *Sankhya A* 81(1), Corollary 9 / Propositions 10, and Theorems 11–12 | supplies the empirical BW barycentre existence/uniqueness and the linear-structure convexity inequality | **RESOLVED — cited. See §2.4 and C-AUDIT-11** |
| L-2 | Santoro & Panaretos, arXiv:2305.15592v3, *Large Sample Theory for Bures–Wasserstein Barycentres* | Theorem 1 supersedes the internal R2 uniqueness argument | **RESOLVED — read. Novelty claim retracted; see §2.4** |
| L-2b | **Kroshnin, Spokoiny & Suvorikova (2021), *Annals of Applied Probability* 31(3), 1264–1298, Theorem 2.1** | the finite-dimensional population existence/uniqueness/regularity result, under minimal conditions — this is the correct benchmark, not Agueh–Carlier | **RESOLVED by citation trail — read in full before the appendix is written** |
| L-2c | **Le Gouic, Paris, Rigollet & Stromme**, *Fast convergence of empirical barycenters in Alexandrov spaces and the Wasserstein space*, arXiv:1908.00828v4 | parametric rates for empirical barycentres under geodesic bi-extendibility; Corollary 17 is the Gaussian/BW instance | **RESOLVED — READ. NOT a competitor; a comparison benchmark. See §2.5. An earlier draft of this file overstated the risk on a secondhand description** |
| L-2d | Chewi, Maunu, Rigollet & Stromme (2020), *Gradient descent algorithms for Bures–Wasserstein barycenters*, COLT, Proposition 15; Ahidar-Coutrix, Le Gouic & Paris, arXiv:1806.02740 | existence under a spectral band, and the predecessor rate paper with the \(n^{-1/D}\) curse | **UNVERIFIED — skim** |
| L-3 | Zemel & Panaretos (2019), *Fréchet means and Procrustes analysis in Wasserstein space*, Bernoulli 25(2), 932–976; and Masarotto–Panaretos–Zemel (2022), arXiv:2212.04797, *Transportation-based functional ANOVA and PCA for covariance operators* | standard BW barycentre and BW-PCA references, absent from the bibliography | **UNVERIFIED — read and cite** |
| L-4 | Santoro–Panaretos Remark 6 — their proof strategy for LFR deliberately avoids Petersen–Müller's assumptions | possible competing or corroborating technique for the G1 mean chain | **UNVERIFIED — compare against [[G1 audit — resolution of the uniform local Fréchet rate]]** |
| L-5 | arXiv:2606.00858, *Change-Point Detection for Object-valued Time Series* | motivation citation; situates itself in the statistics **and econometrics** literature | **UNVERIFIED — read for the introduction** |
| L-6 | arXiv:2605.18316, *Dynamic Elliptical Graph Factor Models via Riemannian Optimization* | adjacent time-varying Riemannian structure; related-work only | **UNVERIFIED — skim** |
| L-7 | arXiv:2604.03566 and arXiv:2404.03878 (Fréchet regression / F-tests on BW) | the BW inference toolkit being built concurrently; related-work only | **UNVERIFIED — skim** |

## 4. The defensible novelty claim

Stated so that each clause survives §2:

> Paper 1 is the first treatment of a **moving Fréchet centre for a single realisation of a dependent, locally stationary manifold-valued time series**, in which the centre path and a serially persistent tangent factor are **not separately identified**, and it establishes the exact identification boundary, an estimation theory with an explicit rate cost for relaxing the fixed-centre assumption, and the admissible loss class for scoring the resulting covariance forecasts against an imperfect proxy.

Each qualifier is doing work. Remove *single realisation* and Santoro–Panaretos have the centre. Remove *dependent / locally stationary* and the confounding disappears. Remove *serially persistent factor* and it is functional PCA. Remove *not separately identified* and it is the parent with a smoother.

**Claims that are NOT available:**

- that a time-varying BW barycentre is a new object — it is not;
- that pointwise reduction of the time-varying Fréchet minimisation is internal — it is Lemma 1 of arXiv:2310.13764;
- BW barycentre existence or uniqueness as novel — **settled against the project**, see §2.4 and C-AUDIT-11;
- that the parent's leading empirical factor is spurious or drift-dominated — forbidden by ID-6 regardless of any literature;
- that the moving-centre model's forecasting advantage demonstrates centre drift — see the predictive-adequacy-versus-identification separation.

## 5. Competitive position, 2026-08-16

The parent posted **2026-07-30**. As of this audit it has **no citations** (Google Scholar, checked by hand; corroborated by negligible alphaXiv engagement). No work extending it to a moving centre was found.

The real signal is not that the exact problem is unclaimed — it is that **N2 is being built out rapidly by several groups** (four BW-inference papers in the last two years, three of them 2026). The window is measured in months. A weekly automated scoop-check is in place covering N1–N4; it reports only new items.

## 6. Related notes

- [[References and external claim audit]] — attribution ledger; the C-AUDIT rows and the publication rule
- [[Analytical reconstruction — proof ledger and rebuilt spec]] — theorem status
- [[P1-ID — centre-drift and factor identification boundary]] — the identification claim this file positions
- [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]] — N4
- [[OPEN OBLIGATIONS — current research actions]] — where L-1 to L-7 become actions
