---
type: canonical-audit
title: References and external claim audit
status: current
last-audited: 2026-08-21 (P1-RANK primary-source audit integrated)
authority: external attribution, parent-paper comparison, and primary-source scope
---

# References and external claim audit

> This ledger is the citation authority for canonical notes. “Proved internally” and “cited externally” are different statuses. An external citation does not prove a project-specific uniformity claim unless the cited result has the same norm, domain, dependence, and triangular-array scope.

## 1. Parent paper

**Huang, Shuo-Chieh; Chen, Rong; Chen, Yaqing (2026). “A Riemannian Factor Model for Manifold-Valued Time Series.” arXiv:2607.28385v1.**

- Primary record: <https://arxiv.org/abs/2607.28385>
- Public reference implementation: <https://github.com/shuochieh/Riemannian_factor_model>. The repository includes Bures--Wasserstein utilities and simulations, the main RFM functions, and S&P 500 analysis/reproduction scripts. It is the reproduction baseline for APP-FIN and the numerical suite, not evidence for any project-specific extension.
- Section 2.2, (P2): the Fréchet mean of the marginal law \(Q_t\) exists and equals the same \(\mu\) for every \(t\). Remark 1 explains the tangent factor model as a model for the mean-zero process \(\operatorname{Log}_\mu(x_t)\). Thus centre drift is excluded by the parent specification; (P2) is not an empirical test that the centre is constant.
- Theorem 2: under the assumptions of Theorem 1 plus componentwise MA\((\infty)\) and short-memory covariance decay, the loading-space rate is \(O_p(1/(\kappa^2\sqrt n))\).
- Proposition 3: signal eigenvalues fluctuate at \(n^{-1/2}\), null eigenvalues at \(n^{-1}\), and \(\lambda_r\ge\kappa^2\).
- Theorem 2's short-memory condition is broader than fixed finite dependence: (13)--(14) require
  \[
  \frac{|\operatorname{Tr}\Gamma_\xi(s,t)|}
  {\{\operatorname{Tr}\Gamma_\xi(s,s)\operatorname{Tr}\Gamma_\xi(t,t)\}^{1/2}}
  \le C_\xi |s-t|^{-d_\xi},
  \]
  with \(\sup_{\xi\in B_\mu(\epsilon)}C_\xi=O(1)\) and a uniform lower bound on \(d_\xi\) strictly greater than one; the paper explicitly identifies finite \(m\)-dependence as a special case.
- The dimension-free rate is the theorem statement, but the paper's concrete P3 verification in Example 1 is dimension-restricted: geometric \(\alpha\)-mixing permits \(p=o(n^\gamma/\log n)\) for some \(0<\gamma<1/2\), while its algebraic-mixing verification assumes fixed \(p\). These are sufficient verifications, not a contradiction of Theorem 2.
- P1 is a bounded-radius/support assumption. The discussion following Theorem 2 explicitly notes that it prevents total factor and idiosyncratic energy from diverging with \(p\). The parent theorem is therefore dimension-free in a bounded-total-energy regime, not a classical per-coordinate-noise or pervasive-energy regime.
- APP-FIN uses 240 monthly realised covariance matrices from 12 U.S. stocks, modelled under Bures--Wasserstein geometry. It compares RFM with LFM, LOCF, and EWMA, forecasts one month ahead, and reports a market-wide factor that tracks VIX. This application and its public code mean project reproduction and extension do not start from zero.
- Identification comparison: P1-ID identifies unique marginal centres, the flat minimum dynamic quotient, pointwise/no-uniform spectral recovery, and the compatible-chart reference orbit; it disproves generic curved rank invariance and gives the complete fixed-centre lag decomposition. The empirical wording remains non-separation/sensitivity, not “spurious Factor 1” or drift dominance.
- Project comparison: robust Paper 1 preserves the parent’s arbitrary-ambient-dimension/bounded-energy character but pays the moving-centre \(n^{-3/7}\) numerator. FRAME-2P-U conditionally restores root-\(n\) **order**, not the parent limit law: its validation influence generally changes asymptotic variance.

### Remark P-RATIO — what Proposition 3 does and does not justify

The parent defines the raw estimator in Eq. (5),
\[
\widehat r=\arg\min_{1\le i\le R}\widehat\lambda_{i+1}/\widehat\lambda_i,
\]
and says that Proposition 3 justifies it. The displayed rates alone do not imply that conclusion: \(\widehat{\mathbb L}=\operatorname{diag}(1,d_n^2,0)\) has the advertised signal/null orders but the raw ratio selects two rather than one. This is a direct logical correction to the claimed implication, not a claim that the estimator fails empirically. The parent's Table 2 success rates (above 80% at \(n=100\) and about 100% at \(n=200\) in the reported designs) are fully compatible with the non-derivability result. The project's threshold and ridged-ratio selectors add the missing separation conditions.

## 2. Geometry and probability sources actually invoked

| Claim used in the project | Source | Exact use and restriction |
|---|---|---|
| mean-square ergodic averaging for a stationary Hilbert process | J. L. Doob, *Stochastic Processes*, Wiley, 1953, Chapter X, §7 | applied only to one centred, square-integrable, weakly stationary Hilbert-valued frozen process: Cesàro averages converge in \(L^2\) to the invariant projection; the spectral form identifies the squared limit norm with the mass at frequency zero. It supplies neither a rate nor uniformity over a triangular array. |
| holonomy generated by curvature | W. Ambrose and I. M. Singer, “A theorem on holonomy,” *Transactions of the AMS* 75 (1953), 428–443 | conceptual holonomy source, not a ready-made finite-ribbon error bound |
| parallel transport around a small rectangle | R. Hunger, “A coordinate free version of the Ambrose–Singer theorem,” arXiv:1607.07820v3, Proposition 2.7 | normalized rectangle/ribbon expansion; project-specific connector and norm bounds are internal |
| neighbouring-log/double-exponential expansion | X. Pennec, “Curvature effects on the empirical mean in Riemannian and affine manifolds: a non-asymptotic high concentration expansion in the small-sample regime,” arXiv:1906.07418 | coefficient and tensor-typing check; not dimension-uniform by itself |
| nonlinear locally stationary physical dependence | R. Dahlhaus, S. Richter, and W. B. Wu, “Towards a general theory for nonlinear locally stationary processes,” *Bernoulli* 25(2) (2019), 1013–1044 | \(L^q\)-style dependence/local-stationarity framework; not an essential-sup tube theorem |
| local Fréchet regression comparison | Y. Chen and H.-G. Müller, “Uniform convergence of local Fréchet regression, with applications to locating extrema and time warping for metric-space valued trajectories,” *Annals of Statistics* 50(3) (2022), 1573–1592 | comparison only; project rates require their own envelopes and geometry |
| Bures–Wasserstein geometry | R. Bhatia, T. Jain, and Y. Lim, “On the Bures–Wasserstein distance between positive definite matrices,” *Expositiones Mathematicae* 37(2) (2019), 165–191; A. Takatsu, “Wasserstein geometry of Gaussian measures,” *Osaka Journal of Mathematics* 48 (2011), 1005–1026 | background formulas and quotient geometry only; the project’s fixed-margin and shrinking-margin uniform constants are internal |
| BW boundary distance and injectivity claims | E. Massart and P.-A. Absil, “Quotient Geometry with Simple Geodesics for the Manifold of Fixed-Rank Positive-Semidefinite Matrices,” *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 171–198, DOI 10.1137/18M1231389 | carry the authors’ correction to Propositions 4.4–4.5; the repaired different-rank statement is Thanwerdas–Pennec, “Bures–Wasserstein Minimizing Geodesics between Covariance Matrices of Different Ranks,” arXiv:2204.09928, Theorem 5.3 |

### Signed-weight and BW-regression producers (G1/CE-9/SW-AS and the BW Richardson safeguard)

| Claim used | Source | Exact use and restriction | Role |
|---|---|---|---|
| existence of a **signed** BW barycentre under Spectral Dominance of Positive Weights | D. T. Nguyen and C. A. Uribe, "Fréchet Regression on the Bures-Wasserstein Manifold," arXiv:2604.03566v1 [math.OC] (2026), **Theorem 3.2**; with Prop. 3.3 (spectral box on stationary points), Prop. 3.4 (no local maxima), Prop. 3.7 (small-ball uniqueness) | verbatim condition: \(\sum_{i\in I}\lambda_i^{+}\sqrt{\lambda_{\min}(\Sigma_i)}>\sum_{j\in J}\lambda_j^{-}\sqrt{\lambda_{\max}(\Sigma_j)}\) — **the square roots are part of the theorem**. Their signed weights come from **extrapolation** in global Fréchet regression on i.i.d. regression pairs and do **not** vanish; no local stationarity, no \(b\to0\), no dependence. Two distinct project sites: (i) **comparison** beside CE-9/G7, where the failure mode differs — CE-9 is non-uniqueness on a Hadamard manifold, theirs is non-existence on nonnegatively-curved BW; (ii) **potential producer** at the BW signed-Richardson safeguard, where the project independently found that unsafeguarded signed extrapolation exits the cone. **Preprint, not peer-reviewed** | comparison; candidate producer |
| BW sectional-curvature and injectivity-radius bounds on a spectral floor | Nguyen–Uribe, **Lemma 3.5** (\(K\le3/(2\lambda_{\min}(\Sigma))\)) and **Lemma 3.6** (\(\operatorname{inj}=\sqrt\lambda\) on \(\{\lambda_{\min}\ge\lambda\}\), after Luo et al. 2021, Thm 6) | directly comparable to the project's BW generated-domain margins; **check against BW-FIXED-MARGIN before claiming either as internal** | comparison — **UNVERIFIED against the internal margins** |
| BW Fréchet regression: uniform-in-covariate rates, CLT, F-tests | H. Xu and H. Li, "Wasserstein F-tests for Fréchet regression on Bures-Wasserstein manifolds," *Journal of Machine Learning Research* 26(77) (2025), 1–123 | **published**. Covariance-matrix responses, conditional BW Fréchet mean as the target, i.i.d. regression pairs. Cite as BW Fréchet-regression inference prior art. It is **not** a locally stationary dependent-array result and supplies nothing the project consumes | comparison |
| time-varying low-rank factor structure on a manifold quotient | C. Peng and X. Shen, "Dynamic Elliptical Graph Factor Models via Riemannian Optimization with Geodesic Temporal Regularization," arXiv:2605.18316v1 [cs.LG] (2026), §III–§V | LRaD **precision** matrices on \(\prod_tB_{p,r}/O_r\); AIRM geodesic temporal penalty; \(n_t\) i.i.d. samples per window. **No Fréchet mean, no moving base point, no transport, no lag operator.** Constrains the **moving-loading programme's** novelty wording; does **not** touch Paper 1's moving-centre construction | comparison |
| computation of positive-weight BW barycentres | S. Chewi, T. Maunu, P. Rigollet, A. J. Stromme, "Gradient descent algorithms for Bures-Wasserstein barycenters," COLT (2020) — Prop. 15 used by Nguyen–Uribe for existence under a spectral band; also Altschuler–Chewi–Gerber–Stromme, NeurIPS 34 (2021) | optimisation/algorithmic prior art only. Not moving-centre inference and not consumed | comparison |
| empirical-barycentre rates via variance inequalities and extendible geodesics | A. Ahidar-Coutrix, T. Le Gouic, Q. Paris, arXiv:1806.02740 | the predecessor to LGPRS, carrying the \(n^{-1/D}\) curse. Background for why generic empirical-barycentre theory needs curvature/convexity/variance conditions; helps contextualise why the project's Cartan–Hadamard route is comparatively clean. Not consumed | comparison |

### P1-RANK external producers and comparisons (lag signal and factor number)

| Claim or comparison | Source | Exact use and restriction | Role |
|---|---|---|---|
| squared nonzero-lag covariance operator identifies the dynamic loading space | C. Lam and Q. Yao, "Factor modeling for high-dimensional time series: inference for the number of factors," *Annals of Statistics* 40(2) (2012), 694–726, DOI 10.1214/12-AOS970, §2, Proposition 1 and Theorem 1 | finite-dimensional stationary time series. Supplies the standard population construction and loading-space identification, not the project's moving-centre nuisance bounds or AR(1) calibration | producer for ancestry |
| Hilbert-space lag operator and eigenvalue-threshold factor-number rule | N. Bhatia, Q. Yao and F. Ziegelmann, "Identifying the finite dimensionality of curve time series," *Annals of Statistics* 38(6) (2010), 3352–3386, DOI 10.1214/10-AOS819, Proposition 1 and Theorems 1 and 3 | functional time series observed with measurement error. Supplies the closest infinite-dimensional lag-operator and threshold precedent; it does not cover estimated manifold centres, polygon transport, triangular arrays, or growing-energy geometry | producer for ancestry |
| spectral information criteria for dynamic factor number | M. Hallin and R. Liška, "Determining the number of factors in the general dynamic factor model," *JASA* 102(478) (2007), 603–617, DOI 10.1198/016214506000001275, Propositions 3–4 | frequency-domain general dynamic factor model; a comparator rather than a producer for the project's time-domain threshold | comparison |
| ridged eigenvalue-ratio precedent under generated residuals | J. Chang, B. Guo and Q. Yao, "High dimensional stochastic regression with latent factors, endogeneity and nonlinearity," *Journal of Econometrics* 189(2) (2015), 297–312, DOI 10.1016/j.jeconom.2015.03.024, Eq. (10) and Theorem 2.4 | supports the narrow claim that a ridge can regularise ratios when inputs are estimated. It does not prove the project's geometric generated-row theorem or remove the need for its adjacent-spectrum condition | comparison and selector precedent |
| generated Fréchet-mean coordinates in manifold time series | Z. Lin and F. Yao, "Intrinsic Riemannian functional data analysis," *Annals of Statistics* 47(6) (2019), 3533–3577, DOI 10.1214/18-AOS1787, Proposition 2 and Theorems 6–7 | confirms that estimating a manifold mean can enter downstream tangent-coordinate analysis. It does not contain a moving local centre, polygonal transport, lag-row squaring, or the project's complete nuisance decomposition | comparison |
| weak-factor terminology and local alternatives | N. Bailey, G. Kapetanios and M. H. Pesaran, "Measurement of factor strength: Theory and practice," *Journal of Applied Econometrics* 36(5) (2021), 621–638, DOI 10.1002/jae.2830 | language and comparison only. Its strength parameter is not the project's \(\chi_j=s_j^4\sum_h\rho_j^{2h}\), so it cannot be used as a detection boundary | comparison |
| post-rank raw eigenvalue ratios | M. Caro and D. Peña, "Selecting the number of factors in multi-variate time series," *Journal of Time Series Analysis* (2024), DOI 10.1111/jtsa.12760, Proposition 1 | related ratio-selector formulation under its own conditions. It does not repair the logical gap in the parent paper's Eq. (5) from the parent's displayed rates alone | comparison |
| sparse-spike minimax lower bounds | T. T. Cai, Z. Ma and Y. Wu, "Sparse PCA: optimal rates and adaptive estimation," *Probability Theory and Related Fields* 161 (2015), 1–48, DOI 10.1007/s00440-014-0562-z, Theorems 2 and 5 | checked and rejected as a producer: independent spiked covariance observations are not serial lag-factor detection with generated manifold coordinates. No matching minimax weak-serial-factor boundary was located | rejected near-match |

The exact independent-AR(1) spectrum
\(\chi_j=s_j^4\sum_h\rho_j^{2h}\), the threshold event
\(d_n^2<\tau_n<\chi_{\min,n}-\eta_n\), and the fixed-total-energy
rank-dilution formula are **PROVED INTERNALLY** in
[[P1-RANK — AR1 signal strength and threshold boundary]]. They are sufficient
calibrations, not externally supplied optimality or impossibility results.

### P1-ID-CLOSE external producers (ID-7–ID-10)

| Claim used | Source | Exact use and restriction |
|---|---|---|
| neighbouring-log expansion \(\log_y\operatorname{Exp}_xZ=w+PZ+\tfrac16R(PZ,w)w+\tfrac13R(PZ,w)PZ+O(4)\) | X. Pennec, arXiv:1906.07418, Theorem 2 (after Gavrilov) — the same source already carried for C-AUDIT-5 | ID-8's universal criterion. \(O(4)\) is **total** order jointly in both arguments, not \(O(t^4)\) at fixed \(w\); the curvature convention is pinned from the source's own displayed sectional-curvature form. Supplies the expansion only: the transversality identity \(\langle R(X,Y)X,X\rangle=0\), the wedge criterion, the converse rigidity, and every exact \(H^2\)/AIRM/BW witness are internal |
| BW Fréchet mean existence and uniqueness (ID-9 route R2, P1-ID §14.2) | **A. Kroshnin, V. Spokoiny, A. Suvorikova, "Statistical inference for Bures–Wasserstein barycenters," *Annals of Applied Probability* 31(3) (2021), 1264–1298, Theorem 2.1** (finite-dimensional population case, minimal conditions); **L. V. Santoro and V. M. Panaretos, "Large Sample Theory for Bures–Wasserstein Barycentres," arXiv:2305.15592v3, Theorem 1** (general separable Hilbert space: existence **iff** \(\mathbb E\|\Sigma\|_1<\infty\); uniqueness under \(\mathbb P\{\Sigma\succ0\}>0\)); **V. Masarotto, V. M. Panaretos, Y. Zemel, "Procrustes metrics on covariance operators and optimal transportation of Gaussian processes," *Sankhya A* 81(1) (2019), 172–213, Corollary 9 and Proposition 10** (empirical case on general \(H\); Proposition 10 supplies the linear-structure convexity inequality) | **CITED EXTERNALLY. The former internal-novelty claim is RETRACTED — see C-AUDIT-11.** Santoro–Panaretos Theorem 1 is strictly stronger than the internal R2 statement: same regularity condition, but on a general separable Hilbert space rather than fixed-size matrices, and with the existence half proved as an equivalence. They further note \(\mathbb P\{\Sigma\succ0\}>0\) is **not necessary**, with an explicit finite-dimensional counterexample. No project theorem depends on the internal derivation |
| Wasserstein barycentre existence, general \(\mathcal P_2\) | M. Agueh and G. Carlier, "Barycenters in the Wasserstein space," *SIAM Journal on Mathematical Analysis* 43(2) (2011), 904–924, Theorem 6.1 | **retained as historical context only, and no longer the comparison benchmark.** It covers finitely many measures with one absolutely continuous and was never the state of the art for the BW-specific population barycentre; benchmarking the internal R2 argument against it was the error recorded in C-AUDIT-11 |
| parametric rates for empirical barycentres under geodesic bi-extendibility; BW instance | T. Le Gouic, Q. Paris, P. Rigollet, A. J. Stromme, "Fast convergence of empirical barycenters in Alexandrov spaces and the Wasserstein space," arXiv:1908.00828v4, **Theorem 10 and Corollary 17** | **COMPARISON ONLY — verified against the source.** Corollary 17 fixes \(D\), places the eigenvalue band \([\kappa_0,\kappa_1]\) **directly on the covariance matrices in \(\operatorname{supp}P\)**, samples \(n\) **i.i.d.** draws from one fixed \(P\), estimates **one fixed** barycentre, and requires condition number \(\kappa-\kappa^{-1}<1\), i.e. \(\kappa<\varphi\approx1.618\). Its headline is a **dimension-free** constant, not a growing-dimension theorem. It shares no axis with the project's moving-centre, single-path, growing-\(m_n\), lag-operator setting. Santoro–Panaretos's characterisation of it as "a minimal eigenvalue gap condition" is loose: it is a condition-number **band**, unrelated to the project's lag-operator eigengap \(\Delta_n\). **No novelty claim is affected**; cite as the fixed-dimension i.i.d. benchmark |
| measurable selection from a closed-valued measurable multifunction | K. Kuratowski and C. Ryll-Nardzewski, "A general theorem on selectors," *Bull. Acad. Polon. Sci.* 13 (1965), 397–403 | ID-9 route R2: existence of a measurable centre selector where the Fréchet argmin is nonsingleton. Applied with closed-valued argmin correspondence into a Polish target. It supplies **measurability only** — the impossibility of a *continuous* selection and the manufactured-drift constant \(\lambda(1-\lambda)\Delta^2\) are internal |
| local stationarity as an \(L^q\) stationary-approximation condition | R. Dahlhaus, S. Richter, W. B. Wu, *Bernoulli* 25(2) (2019), 1013–1044, Assumption 2.1 | ID-10's mode declaration only, consistent with C-AUDIT-8. The triangular-array time-varying AR(1) computation giving the induced exponent \(a=1-\theta\), and its sharpness, are internal |
| mean-square ergodic averaging | Doob (1953), Ch. X §7 — see the row above and the hypothesis map below | ID-7's modulus \(\psi_u(N)\to\nu_u(\{0\})^{1/2}\) is the same producer as ID-3. It supplies no rate and no uniformity; every evaluation of \(\psi\) (AR(1) closed form, the limit profile \(\Psi(x)=2(x-1+e^{-x})/x^2\), \(m_0\)-dependence, physical dependence, long memory) is internal |

### P1-LOSS external producers (forecast evaluation)

| Claim used | Source | Exact use and restriction | Role |
|---|---|---|---|
| robust-loss characterisation for **scalar** volatility forecasts | A. J. Patton, "Volatility forecast comparison using imperfect volatility proxies," *Journal of Econometrics* 160(1) (2011), 246–256, **Definition 1 and Proposition 1** | necessary **and** sufficient. Verbatim: a loss \(L\) is robust "if and only if it takes the following form … where \(B\) and \(C\) are twice continuously differentiable, \(C\) is a strictly decreasing function on \(\mathcal H\), and \(\tilde C\) is the anti-derivative of \(C\)". **Scalar volatility only.** It does **not** cover the project's matrix case and must not be cited for it | comparison and scalar producer |
| robust-loss characterisation for **matrix-valued** covariance forecasts | S. Laurent, J. V. K. Rombouts, F. Violante, "On loss functions and ranking forecasting performances of multivariate volatility models," *Journal of Econometrics* 173(1) (2013), 1–10, **Proposition 3 and Corollary 1** | necessary **and** sufficient. Verbatim: consistent "if and only if it takes the form \(L(\widehat\Sigma_t,H_t)=\tilde C(H_t)-\tilde C(\widehat\Sigma_t)+C(H_t)'\operatorname{vech}(\widehat\Sigma_t-H_t)\)" — a Bregman divergence with generator \(\psi=-\tilde C\). Robust: Frobenius, Stein, Euclidean, weighted Euclidean. **Not** robust: entrywise 1-norm, proportional Frobenius, **log-Frobenius**, correlation distance. Requires positive definiteness and \(C^2\) losses. This is the **matrix producer** for P1-LOSS LO-1, and its log-Frobenius row independently corroborates the internal log-Euclidean result | producer |
| consistency for the mean \(\iff\) Bregman | T. Gneiting, "Making and evaluating point forecasts," *JASA* 106(494) (2011), 746–762, **Theorem 3.1**, labelled there "(Savage)" | verbatim: "\(S\) is consistent for the mean functional relative to the class of the compactly supported probability measures on \(I\) if, and only if, it is of the form \(S(x,y)=\varphi(y)-\varphi(x)-\varphi'(x)(y-x)\)". **Domain \(I\subseteq\mathbb R\): scalar only.** Used only for the scalar case; the matrix case uses LRV | producer (scalar) |
| symmetric Bregman \(\iff\) constant Hessian | J.-D. Boissonnat, F. Nielsen, R. Nock, "Bregman Voronoi diagrams," arXiv:0709.2196, **Lemma 2** | verbatim: "\(D_F\) is symmetric if and only if the Hessian \(\nabla^2F\) is constant on \(\mathcal X\)". Stated under a \(C^2\) hypothesis; P1-LOSS proves the same statement for a merely differentiable convex generator and adds the Mahalanobis restatement, so the citation is corroborating rather than load-bearing | comparison |
| realised covariance is unbiased for integrated covariance only when the drift vanishes | O. E. Barndorff-Nielsen and N. Shephard (2002), *Journal of Applied Econometrics* 17(5) | a nonzero drift contributes at \(\Theta(M^{-1})\); only the **order** is consumed | producer |
| naive realised variance under i.i.d. microstructure noise is biased by \(+2M\sigma_u^2\) | L. Zhang, P. A. Mykland, Y. Aït-Sahalia, *JASA* 100 (2005), Eq. (18); also Hansen–Lunde | the \(\Theta(M)\) growth in the sampling frequency is the half of E5's conflict that infill makes worse | producer |
| noise-robust estimators are **consistent**, not conditionally unbiased | Zhang–Mykland–Aït-Sahalia (2005) Thm 4; Zhang (2006) *Bernoulli*; Barndorff-Nielsen–Hansen–Lunde–Shephard (2008/2011) realised kernels; Jacod–Li–Mykland–Podolskij–Vetter (2009) and Christensen–Kinnebrock–Podolskij (2010) pre-averaging | each establishes consistency and a central limit theorem; **none establishes conditional unbiasedness**, which is what a robustness characterisation needs. The efficient pre-averaging form is not guaranteed positive semidefinite. Absence of an unbiasedness theorem is recorded as such and is **not** a claim of bias | comparison |
| geometric deep learning trained on a log-Euclidean loss with GMV evaluation | A. Bucci, M. Palma, C. Zhang, "Geometric Deep Learning for Realized Covariance Matrix Forecasting," arXiv:2412.09517, **Eq. (7)** and **§5, Table 4** | verified verbatim: training loss log-Euclidean; economic evaluation by a GMV portfolio; the paper is **silent** on proxy-robustness of that training loss. arXiv preprint, not confirmed peer-reviewed. **Silence is not error** and no defect is attributed to the authors | comparison |

**Savage (1971)**, *JASA* 66(336), 783–801, **could not be obtained** and is therefore cited only through Gneiting's own attribution. No theorem number is asserted for it and no claim in the canon depends on its text.

**Empirical exponents are not external producers.** The long-memory literature on realised volatility (notably Andersen, Bollerslev, Diebold and Labys, *Econometrica* 71(2) (2003), 579–625) estimates \(d\approx0.4\) for **daily realised volatility of exchange rates**. Temporal aggregation preserves \(d\), but the asset class and the object differ from monthly realised covariance of US equities, and \(d\) is not separately estimated in the parent's 240-month panel. **No theorem in the canonical chain consumes an empirical memory exponent.** ID-10 states the analytic window; the exponent for the flagship application is an assumption under test, routed to N-18/APP-FIN.

### P1-ID mean-ergodic hypothesis map

Let \(Z_t\) be the centred frozen process used in ID-3, taking values in a real separable Hilbert space \(H\), with \(\mathbb E\|Z_0\|^2<\infty\) and weak stationarity. On the closed \(L^2\)-span generated by the process, the time shift is an isometry and extends to the unitary stationary shift. Doob's mean-square ergodic theorem gives

\[
\frac1N\sum_{t=1}^N Z_t\longrightarrow P_{\mathrm{inv}}Z_0
\quad\text{in }L^2(H),
\]

where \(P_{\mathrm{inv}}\) is the orthogonal projection onto the shift-invariant subspace. If \(F_Z\) is the finite positive trace-class operator-valued spectral measure of \(Z\), the spectral representation of that projection gives

\[
\mathbb E\|P_{\mathrm{inv}}Z_0\|^2
=\operatorname{tr}F_Z(\{0\}).
\]

Consequently the frozen averages converge to zero in mean square exactly when the process has no spectral atom at frequency zero. This use requires no mixing assumption and yields no convergence rate. The passage from a frozen process to a locally stationary observed path is not cited from Doob: P1-ID proves it separately from an explicit same-freeze \(L^2\) coupling for the averaged path, or from a direct two-index pair-moment approximation. The conclusion is pointwise in the rescaled time and model; the internal AR(1) contiguity construction and moving nonzero-frequency atoms or mass approaching zero disprove a uniform recovery claim.

Before publication, bibliography software should resolve the final journal metadata and DOI for every row. No theorem in the canonical chain depends on an unresolved author-name shortcut.

## 3. Restored C-AUDIT ledger

These ten corrections were previously stranded in archived notes. They are canonical audit outcomes again:

| ID | Corrected claim | Canonical consequence |
|---|---|---|
| C-AUDIT-1 | Lam–Yao (2012) does not contain the project’s \(1/(\kappa^2\sqrt n)\) rate, and its rate assumptions restrict idiosyncratic noise more than its identification algebra does. | The rate is attributed to Huang–Chen–Chen (2026), Theorem 2; no Lam–Yao shortcut is used. |
| C-AUDIT-2 | Lam–Yao’s post-rank raw eigenvalue ratios were conjectural, not a proved finite-sample selector theorem. The parent paper's Eq. (5) conclusion likewise does not follow from Proposition 3's displayed rates alone. | Paper 1 uses the internally proved threshold/ridged selector; Remark P-RATIO makes the logical correction without claiming empirical failure. |
| C-AUDIT-3 | Wu–Zhou–Hong has no confidence-band scale \(\varrho_n\); its dimension condition is moment-order polynomial, not a \(\log p\) statement. | Any moving-loading localization/bootstrap scale must be proved internally. |
| C-AUDIT-4 | Continuity of \(p\mapsto\operatorname{inj}(p)\) is the Klingenberg/Gromoll–Klingenberg–Meyer pointwise-manifold result, not the Ehrlich/Sakai continuity-in-the-metric result. | Compactness can give a fixed-curve positive infimum, but triangular-array generated-tube margins remain explicit. |
| C-AUDIT-5 | Gavrilov/Pennec give \(\log_x\operatorname{Exp}_yZ=w+PZ+\frac16R(PZ,w)w+\frac13R(PZ,w)PZ+O(4)\). | The old \(1/3\) first coefficient and omitted cubic term are retracted; tensor typing is retained. |
| C-AUDIT-6 | The zero-frequency-atom statement is the \(L^2\) mean-square ergodic theorem; \(|D_N|^2\) is not itself the Fejér kernel—\(N|D_N|^2\) is. | Doob is cited; triangular-array rates are proved separately. |
| C-AUDIT-7 | The unit-constant norm tail is Gaussian Borell–TIS; \(\sqrt{\operatorname{tr}\Sigma}\) bounds \(E\|X\|\) but is not generally equal to it, and the sub-Gaussian analogue is Bernstein-shaped. | Gaussian and sub-Gaussian routes are not stated at parity. |
| C-AUDIT-8 | Dahlhaus (1997) uses evolutionary spectra; the stationary-approximation condition used here is Dahlhaus–Richter–Wu (2019), Assumption 2.1, with an explicit \(n^{-\alpha}\) rate. | Canonical local stationarity states its \(L^2\) or essential-sup mode and exponent. |
| C-AUDIT-9 | Chen–Müller’s displayed \((nb^2)^{-1/2}\) uniform term is an envelope artefact, not a lower bound or sharpness claim; their setting is i.i.d. and assumes signed-objective coercivity where used. | It neither disproves the internal G1 rate nor supplies the project’s dependence/geometry proof. |
| C-AUDIT-11 | The internal ID-9 route R2 uniqueness argument was benchmarked against Agueh–Carlier (2011) and declared a strict extension. That benchmark was wrong: the BW-specific population result was already established by Kroshnin–Spokoiny–Suvorikova (2021, AAP) Theorem 2.1 in finite dimensions and by Santoro–Panaretos (arXiv:2305.15592) Theorem 1 on a general separable Hilbert space, with the empirical case in Masarotto–Panaretos–Zemel (2019) Corollary 9. The internal proof is **correct but not novel**. | The novelty claim is retracted. P1-ID §14.2 R1/R2 become CITED EXTERNALLY. The internal variational identity \(\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}=\tfrac12\inf_{T\succ0}[\operatorname{tr}TA+\operatorname{tr}T^{-1}\Sigma]\) may be retained as a short self-contained appendix derivation of the convexity step that Santoro–Panaretos take from Masarotto–Panaretos–Zemel Proposition 10, explicitly labelled an alternative elementary route and **not** a new result. **No downstream node changes**: ID-9's load-bearing content is routes R3 (latent stochastic centre), the non-existence of a continuous selector and its \(\lambda(1-\lambda)\Delta^2\) cost, and R5, none of which are touched. |
| C-AUDIT-10 | Merlevède–Peligrad–Rio does not cover polynomial mixing, but that does not force sub-geometric mixing: Liebscher (1996), via Rio’s Bernstein inequality, supplies a bounded triangular-array route for polynomial \(\alpha\)-mixing with explicit exponent arithmetic. Mere summability is still insufficient. | G1’s fixed-\(p\) polynomial-mixing threshold is retained; growing-\(p\) robust work uses finite memory or typed physical dependence. |

## 4. Publication rule

Every canonical theorem row must use one of:

- **PROVED INTERNALLY**, with a canonical or archived proof-provenance link;
- **CITED EXTERNALLY**, with source and exact theorem/proposition/section;
- **CONDITIONAL**, with the unproved primitive producers listed;
- **OPEN** or **DISPROVED**.

The compound label “PROVED/CITED” is retired because it hides which part is internal and which part is borrowed.
