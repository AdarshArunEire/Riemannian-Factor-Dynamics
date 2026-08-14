---
type: canonical-audit
title: References and external claim audit
status: current
last-audited: 2026-08-12
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

### P1-ID-CLOSE external producers (ID-7–ID-10)

| Claim used | Source | Exact use and restriction |
|---|---|---|
| neighbouring-log expansion \(\log_y\operatorname{Exp}_xZ=w+PZ+\tfrac16R(PZ,w)w+\tfrac13R(PZ,w)PZ+O(4)\) | X. Pennec, arXiv:1906.07418, Theorem 2 (after Gavrilov) — the same source already carried for C-AUDIT-5 | ID-8's universal criterion. \(O(4)\) is **total** order jointly in both arguments, not \(O(t^4)\) at fixed \(w\); the curvature convention is pinned from the source's own displayed sectional-curvature form. Supplies the expansion only: the transversality identity \(\langle R(X,Y)X,X\rangle=0\), the wedge criterion, the converse rigidity, and every exact \(H^2\)/AIRM/BW witness are internal |
| Wasserstein barycentre uniqueness for Gaussians | M. Agueh and G. Carlier, "Barycenters in the Wasserstein space," *SIAM Journal on Mathematical Analysis* 43(2) (2011), 904–924, Theorem 6.1 | comparison only. It covers **finitely many** measures with one absolutely continuous. ID-9 route R2 needs arbitrary \(Q\in\mathcal P_2\) on a triangular array, so the project proves uniqueness internally by exhibiting \(\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}=\tfrac12\inf_{T\succ0}[\operatorname{tr}TA+\operatorname{tr}T^{-1}\Sigma]\), hence concavity in the **ordinary linear structure**, with strictness from non-constancy of the optimiser. The internal result **strictly extends** the citation; the citation is not load-bearing |
| measurable selection from a closed-valued measurable multifunction | K. Kuratowski and C. Ryll-Nardzewski, "A general theorem on selectors," *Bull. Acad. Polon. Sci.* 13 (1965), 397–403 | ID-9 route R2: existence of a measurable centre selector where the Fréchet argmin is nonsingleton. Applied with closed-valued argmin correspondence into a Polish target. It supplies **measurability only** — the impossibility of a *continuous* selection and the manufactured-drift constant \(\lambda(1-\lambda)\Delta^2\) are internal |
| local stationarity as an \(L^q\) stationary-approximation condition | R. Dahlhaus, S. Richter, W. B. Wu, *Bernoulli* 25(2) (2019), 1013–1044, Assumption 2.1 | ID-10's mode declaration only, consistent with C-AUDIT-8. The triangular-array time-varying AR(1) computation giving the induced exponent \(a=1-\theta\), and its sharpness, are internal |
| mean-square ergodic averaging | Doob (1953), Ch. X §7 — see the row above and the hypothesis map below | ID-7's modulus \(\psi_u(N)\to\nu_u(\{0\})^{1/2}\) is the same producer as ID-3. It supplies no rate and no uniformity; every evaluation of \(\psi\) (AR(1) closed form, the limit profile \(\Psi(x)=2(x-1+e^{-x})/x^2\), \(m_0\)-dependence, physical dependence, long memory) is internal |

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
| C-AUDIT-3 | Wu–Zhou–Hong has no confidence-band scale \(\varrho_n\); its dimension condition is moment-order polynomial, not a \(\log p\) statement. | Any Paper 2 localization/bootstrap scale must be proved internally. |
| C-AUDIT-4 | Continuity of \(p\mapsto\operatorname{inj}(p)\) is the Klingenberg/Gromoll–Klingenberg–Meyer pointwise-manifold result, not the Ehrlich/Sakai continuity-in-the-metric result. | Compactness can give a fixed-curve positive infimum, but triangular-array generated-tube margins remain explicit. |
| C-AUDIT-5 | Gavrilov/Pennec give \(\log_x\operatorname{Exp}_yZ=w+PZ+\frac16R(PZ,w)w+\frac13R(PZ,w)PZ+O(4)\). | The old \(1/3\) first coefficient and omitted cubic term are retracted; tensor typing is retained. |
| C-AUDIT-6 | The zero-frequency-atom statement is the \(L^2\) mean-square ergodic theorem; \(|D_N|^2\) is not itself the Fejér kernel—\(N|D_N|^2\) is. | Doob is cited; triangular-array rates are proved separately. |
| C-AUDIT-7 | The unit-constant norm tail is Gaussian Borell–TIS; \(\sqrt{\operatorname{tr}\Sigma}\) bounds \(E\|X\|\) but is not generally equal to it, and the sub-Gaussian analogue is Bernstein-shaped. | Gaussian and sub-Gaussian routes are not stated at parity. |
| C-AUDIT-8 | Dahlhaus (1997) uses evolutionary spectra; the stationary-approximation condition used here is Dahlhaus–Richter–Wu (2019), Assumption 2.1, with an explicit \(n^{-\alpha}\) rate. | Canonical local stationarity states its \(L^2\) or essential-sup mode and exponent. |
| C-AUDIT-9 | Chen–Müller’s displayed \((nb^2)^{-1/2}\) uniform term is an envelope artefact, not a lower bound or sharpness claim; their setting is i.i.d. and assumes signed-objective coercivity where used. | It neither disproves the internal G1 rate nor supplies the project’s dependence/geometry proof. |
| C-AUDIT-10 | Merlevède–Peligrad–Rio does not cover polynomial mixing, but that does not force sub-geometric mixing: Liebscher (1996), via Rio’s Bernstein inequality, supplies a bounded triangular-array route for polynomial \(\alpha\)-mixing with explicit exponent arithmetic. Mere summability is still insufficient. | G1’s fixed-\(p\) polynomial-mixing threshold is retained; growing-\(p\) robust work uses finite memory or typed physical dependence. |

## 4. Publication rule

Every canonical theorem row must use one of:

- **PROVED INTERNALLY**, with a canonical or archived proof-provenance link;
- **CITED EXTERNALLY**, with source and exact theorem/proposition/section;
- **CONDITIONAL**, with the unproved primitive producers listed;
- **OPEN** or **DISPROVED**.

The compound label “PROVED/CITED” is retired because it hides which part is internal and which part is borrowed.
