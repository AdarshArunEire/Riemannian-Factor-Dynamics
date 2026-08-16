---
type: working-proof-dossier
title: P1-LOSS-C — targets, proxies, and external claims
status: active-campaign
last-audited: 2026-08-14
authorship: authored by the campaign lead after the Wave-1 agent interruption (see [[P1-LOSS — lead ledger]] §1); the LO-7 verbatim record was produced by an independent narrow citation-audit agent and is preserved in [[P1-LOSS — LO-7 external positioning audit]]. The lead is NOT an admissible non-author auditor of the analytical sections of this dossier.
---

# P1-LOSS-C — targets, proxies, and external claims

Owns routes E2 and E3, the LO-7 adjudication, and the standing job of attacking the headline.

## 0. Claim table

| ID | Exact statement | Assumptions | Conclusion | Proof | Status | Known weak point |
|---|---|---|---|---|---|---|
| C-E2.1 | the conditional BW barycentre **of the proxy** is a functional of the measurement scheme, not of the data-generating process: it depends on the proxy's conditional variance and hence on the intraday sampling frequency \(M\) | B-3.2 | PROVED | §1.1 | PROVED | it is a DGP functional *conditional on a fixed measurement scheme*; the objection is that the scheme is a choice |
| C-E2.2 | the conditional BW barycentre **of the latent** \(\Sigma^\ast\) is a DGP functional; minimising expected BW loss against a \(\Sigma\)-unbiased proxy is **not unbiased** for it at fixed \(M\), and **is** consistent for it as \(M\to\infty\) at rate \(\Theta(M^{-1})\) | — | PROVED | §1.2 | PROVED | the first draft's table and body said opposite things — precisely the consistency/unbiasedness conflation this campaign polices (O-13); and the constant is **not** B-3.5's |
| C-E2.3 | decision-theoretic cost: portfolio variance and value-at-risk are linear/level-sensitive functionals of \(\Sigma\), so the conditional **mean** is the decision-relevant target for risk applications; targeting the barycentre systematically understates risk | — | PROVED | §1.3 | PROVED | it is a statement about variance- and VaR-type decisions, not about every conceivable decision |
| C-E2 | **E2 terminal:** redefining the target to the conditional Fréchet barycentre is not a defensible escape; if adopted it is a convention change and must be labelled one | — | DISPROVED (as an escape) | §1.4 | DISPROVED | — |
| C-E3.1 | scalar: a scaled realised absolute variation is conditionally unbiased for \(\sigma\) **only** under conditional Gaussianity and **constant** volatility within the window | — | PROVED | §2.1 | PROVED | the Gaussian constant \(\sqrt{\pi/2}\) is distribution-specific; any other law changes it |
| C-E3.2 | with no auxiliary knowledge of the within-window volatility path: (i) the absolute-variation/bipower family is excluded by Cauchy–Schwarz, since its infill limit is \(\int\sigma\,ds\le(\int\sigma^2ds)^{1/2}\) with equality iff \(\sigma\) is a.e. constant; (ii) every continuous function of realised covariance is conditionally biased for \(\Sigma^{1/2}\) by strict operator concavity of the square root | Cauchy–Schwarz; operator Jensen | REFORMULATED+PROVED | §2.2 | REFORMULATED+PROVED | the first draft claimed a general impossibility over **all** estimators; that is false — with a known within-window volatility shape an unbiased and consistent estimator exists (O-12). The claim is narrowed to what is proved, with its boundary reason stated |
| C-E3.3 | matrix: the same obstruction, plus non-commutativity of \(\int\) and \((\cdot)^{1/2}\) | — | PROVED | §2.3 | PROVED | — |
| C-E3.4 | \(\log\Sigma\): no conditionally unbiased estimator; additionally \(\log\widehat\Sigma\) is undefined when \(M<m\) | strict Jensen | PROVED | §2.4 | PROVED | — |
| C-E3 | **E3 terminal:** the no-go is real and **unavoidable by a change of proxy**. The advice is to change the loss, not the proxy | — | DISPROVED (as an escape) | §2.5 | DISPROVED | — |
| C-7.1 | **GMV blindness.** The global-minimum-variance weights depend on a covariance forecast \(H\) only through the ray of \(H^{-1}\mathbf 1\); they are **exactly** invariant to \(H\mapsto cH\), and at \(m=12\) they see \(11\) of the \(78\) degrees of freedom | \(H\succ0\) | PROVED | §3.1 | PROVED | it is a statement about GMV specifically |
| C-7.2 | GMV weights are **not** invariant to a non-scalar spectral distortion; the AIRM distortion is **exactly** a scalar multiple for a Wishart proxy and is therefore entirely invisible, while the BW distortion is only partially visible | B-3.5, B-3.7; congruence-equivariance of the Karcher mean | PROVED | §3.2 | PROVED | "entirely invisible" needs the exact equivariance argument, not second-order scalarity (O-16); the BW visibility figure is configuration-dependent and is now stated with its configuration |
| C-7.3 | level-sensitive evaluations (forecast portfolio variance vs realised, VaR exceedance, likelihood/QLIKE) **do** detect the distortion | — | PROVED | §3.3 | PROVED | — |
| C-7.4 | Bucci, Palma and Zhang, arXiv:2412.09517, trains on the log-Euclidean distance (their Eq. 7) and evaluates via a GMV portfolio (their §5, Table 4); the paper is **silent** on proxy-robustness of that training loss | verbatim verification | CITED+APPLIED | §3.4 | CITED+APPLIED | it is an arXiv preprint, not confirmed peer-reviewed; and silence is not error |
| C-7.5 | the informal clause "its GMV evaluation cannot detect the resulting bias" is **this campaign's theorem** (C-7.1/C-7.2), not a fact attributable to any author | — | REFORMULATED+PROVED | §3.5 | REFORMULATED+PROVED | — |
| C-ATT | no non-flat Riemannian metric on a convex domain has a proxy-robust squared geodesic distance; every construction attempt is provably futile, and the three most tempting candidates are shown to fail for three different reasons | A-4.3 | PROVED (impossibility) | §4 | PROVED | the impossibility is only as strong as A-4.3's richness hypothesis, which E1/E4 already bound |

## 1. E2 — change the target to the conditional Fréchet barycentre

### 1.1 C-E2.1 — the induced target is a functional of the measurement scheme

By B-2.2 the BW loss's induced target is \(H^\star=\) BW barycentre of the conditional law of \(\widehat\Sigma\). By B-3.2/B-3.5 that barycentre is
\[
H^\star=\Sigma-\frac1M\operatorname{diag}_i\!\left(\lambda_i\left[\tfrac14+\sum_k\tfrac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\right]\right)+O(M^{-2})
\]
for a Wishart-type proxy with \(M\) intraday increments. **\(M\) is a choice made by the analyst, not a property of the market.** Two analysts observing the same price process and choosing 5-minute and 30-minute sampling face *different* induced targets, differing at first order in \(1/M\). Worse, by B-3.6 for a general proxy law the induced target has a *different eigenbasis* depending on the sampling scheme.

**Theorem (E2 fatal objection).** The conditional BW barycentre of the proxy is not a functional of the data-generating process. It is a functional of the pair (data-generating process, measurement scheme), with an explicit first-order dependence \(\partial H^\star/\partial(1/M)\ne0\) given by (3.5) of dossier B.

A forecast target that moves when you change your sampling grid is not a scientific estimand. This alone closes E2 in its natural form. ∎

### 1.2 C-E2.2 — the latent barycentre is a DGP functional, and BW loss does not estimate it

One could instead declare the target to be the BW barycentre of the conditional law of the **latent** \(\Sigma^\ast_t\) given \(\mathcal F_{t-1}\). That *is* a DGP functional and is identified from the conditional law of \(\Sigma^\ast\).

But at any fixed \(M\), minimising \(\mathbb E[d_{\rm BW}^2(\widehat\Sigma,H)\mid\mathcal F]\) does **not** estimate it. The minimiser is the barycentre of the law of \(\widehat\Sigma\), which is the law of \(\Sigma^\ast\) convolved with measurement error, and the barycentre operator is not additive over that convolution. The gap is \(\Theta(M^{-1})\), so BW-loss minimisation **is** consistent for the latent barycentre as \(M\to\infty\) and **is not** unbiased at any fixed \(M\). These are different statements and the first draft's claim table and body asserted opposite things; the audit was right to call that the exact conflation this campaign polices (O-13).

**The constant is not B-3.5's, and the first draft wrongly borrowed it.** B-3.5 is derived for a degenerate latent law; with an \(O(1)\) latent spread the linearisation runs through a non-identity Fréchet Hessian. The auditor measured \(\text{gap}\times M\to1.149\) (stable at \(1.1527/1.1490/1.1491\) for \(M=400/1600/6400\)) against B-3.5's \(1.321\). Only the **order** \(\Theta(M^{-1})\) is consumed by canon; the constant for the latent-barycentre gap is a separate computation and is not claimed here.

So E2 in this second form is not an escape: it names an admissible target, and supplies only a consistent — not conditionally unbiased — route to it, which is precisely the property LO-1 cannot use. ∎

### 1.3 C-E2.3 — what a risk application loses

Let \(w\) be a portfolio weight vector fixed at the time the forecast is made. Realised portfolio variance is \(w^\top\Sigma^\ast w\) and its conditional expectation is \(w^\top\Sigma w\) — **linear in \(\Sigma\)**. Therefore:
- for any variance-, tracking-error-, or risk-budget decision, the decision-relevant conditional functional is the conditional **mean**, and any target other than the mean systematically misprices the decision;
- the barycentre satisfies \(H^\star\preceq\Sigma\) in the sense that its spectrum is uniformly shrunk (B-3.5), so a barycentre-targeting forecaster **systematically understates portfolio variance**, by 9%–33% at the flagship configuration;
- for Gaussian value-at-risk at level \(z\), \(\mathrm{VaR}=z\sqrt{w^\top Hw}\), so an understatement of \(H\) by a factor \(1-\kappa\) understates VaR by a factor \(\sqrt{1-\kappa}\); at \(\kappa=0.3\) that is a 16% understatement of the risk number, in the conservative direction of *under*-reserving.

This is not a matter of taste between two estimands. For the applications this project names — APP-FIN above all — the conditional mean is the functional the decision consumes. ∎

### 1.4 C-E2 — terminal verdict

**DISPROVED as an escape.** The natural version of E2 (target the barycentre of the proxy's conditional law) names an object that depends on the sampling scheme and is therefore not an estimand. The repaired version (target the latent barycentre) names a legitimate estimand that BW-loss minimisation does not estimate, only approaches under infill. And in either version a risk application pays a quantified, one-directional cost.

**If a future application nevertheless adopts a barycentre target, it is a convention change of exactly the kind P1-ID was created to police**, and it must be labelled with the same wording: *the target is declared, the declaration is not testable from the observed law, and the reported object is a convention-dependent functional, not an identified one.*

## 2. E3 — change the proxy

Robustness needs conditional unbiasedness **in the loss's natural coordinate**. BW restricted to a commuting orthant is Mahalanobis in \(\Sigma^{1/2}\) (B-3.4); log-Euclidean is Mahalanobis in \(\log\Sigma\) (A-4.4). So E3 asks: is there a realised estimator conditionally unbiased for \(\Sigma^{1/2}\), or for \(\log\Sigma\)?

### 2.1 C-E3.1 — the scalar case looks promising and is a trap

Under conditional Gaussianity with **constant** volatility \(\sigma\) on the window and \(M\) equally spaced increments, \(r_\ell\sim N(0,\sigma^2/M)\) and \(\mathbb E|r_\ell|=\sigma\sqrt{2/(\pi M)}\). Hence
\[
\widehat\sigma:=\sqrt{\tfrac{\pi M}{2}}\cdot\tfrac1M\sum_{\ell=1}^M|r_\ell|
\quad\text{satisfies}\quad \mathbb E\widehat\sigma=\sigma .
\]
So an exactly unbiased estimator of \(\sigma\) does exist — **in that model**. Two hypotheses are doing all the work: (i) conditional Gaussianity, which fixes the constant \(\sqrt{\pi/2}\) and is falsified by any jump or fat tail; (ii) constancy of \(\sigma\) within the window.

### 2.2 C-E3.2 — under stochastic volatility the target itself splits

Drop constancy. Then \(\mathbb E\big[\sum_\ell|r_\ell|\,\big|\,\sigma\big]=\sqrt{2/(\pi M)}\sum_\ell\big(\int_{I_\ell}\sigma^2_s\,ds\big)^{1/2}\cdot\sqrt M\to\sqrt{2/\pi}\cdot\sqrt{M}\cdots\), and the infill limit of the scaled realised absolute variation is
\[
\sqrt{\tfrac\pi2}\cdot\tfrac1{\sqrt M}\textstyle\sum_\ell|r_\ell|\ \longrightarrow\ \int_0^1\sigma_s\,ds,
\]
**not** \(\big(\int_0^1\sigma_s^2\,ds\big)^{1/2}\). By Cauchy–Schwarz on \([0,1]\),
\[
\int_0^1\sigma_s\,ds\ \le\ \Big(\int_0^1\sigma_s^2\,ds\Big)^{1/2},
\qquad\text{equality iff }\sigma_s\text{ is a.e. constant.}
\]
The gap is exactly the within-window dispersion of volatility. Therefore:

**Theorem (E3 obstruction, scalar) — corrected scope (O-12).** Absolute-variation-type estimators are conditionally unbiased for the *integrated volatility path functional* \(\int\sigma\,ds\), while the BW loss's natural coordinate is the *square root of integrated variance* \((\int\sigma^2ds)^{1/2}\). These coincide iff volatility is a.e. constant on the window. Hence **the whole absolute-variation/bipower family is excluded.**

The first draft went further and claimed that *no* estimator can be both conditionally unbiased for \((\int\sigma^2)^{1/2}\) and infill-consistent. That does not follow, and the auditor supplied the counterexample: if the within-window volatility *shape* is known — say \(\sigma=\sigma_a\) on \([0,\tfrac12]\) and \(c\sigma_a\) on \([\tfrac12,1]\) with \(c\) known — an estimator that is both exists. The claim is therefore narrowed to what is proved, with its boundary reason stated:

> **E3 obstruction, as proved.** With no auxiliary knowledge of the within-window volatility path, (i) the absolute-variation/bipower family is excluded by Cauchy–Schwarz, and (ii) every continuous function of realised covariance is conditionally biased for \(\Sigma^{1/2}\), because \(A\mapsto A^{1/2}\) is strictly operator concave, so \(\mathbb E[\widehat\Sigma^{1/2}\mid\mathcal F]\prec\Sigma^{1/2}\) strictly whenever \(\widehat\Sigma\) is nondegenerate. A general impossibility over *all* estimators is **not** claimed.

The boundary is exactly "knowledge of the within-window volatility path", and an application that has it has already assumed away the stochastic-volatility problem the proxy exists to solve. E3's route verdict is unchanged. ∎

This is the same Jensen-type obstruction that generated the whole problem, displaced one level: you cannot buy unbiasedness in the root coordinate, because the root of an integral is not the integral of the root.

### 2.3 C-E3.3 — the matrix case is worse

The matrix analogue of the same statement is \(\int_0^1\sigma_s\,ds\ne\big(\int_0^1\sigma_s\sigma_s^\top ds\big)^{1/2}\), which now fails for two independent reasons: the Cauchy–Schwarz gap of §2.2, and non-commutativity — even with \(\|\sigma_s\|\) constant, a rotating \(\sigma_s\) makes the two objects differ, since the matrix square root does not commute with integration. Moreover any candidate estimator built from \(\sum_\ell|r_\ell|\)-type statistics is not even symmetric-matrix-valued without further construction, and the Gaussian constant becomes a dimension-dependent tensor. **PROVED.**

### 2.4 C-E3.4 — the log coordinate

For \(\log\Sigma\) the obstruction is immediate and does not need a stochastic-volatility argument: \(\log\) is strictly concave in the operator sense on the cone, so \(\mathbb E[\log\widehat\Sigma]\prec\log\mathbb E[\widehat\Sigma]=\log\Sigma\) strictly whenever \(\widehat\Sigma\) is nondegenerate. An estimator conditionally unbiased for \(\log\Sigma\) would have to correct that gap exactly, which requires knowing the proxy's law — i.e. it is a debiasing under a model, not a change of proxy. Additionally \(\log\widehat\Sigma\) is undefined whenever \(\widehat\Sigma\) is singular, which for realised covariance happens exactly when \(M<m\) — a live regime for \(m=12\) assets and monthly windows built from \(M\approx21\) daily returns, where the proxy is only barely nonsingular. **PROVED.**

### 2.5 C-E3 — terminal verdict

**DISPROVED as an escape.** There is no admissible change of proxy that restores robustness for a geodesic loss. The obstruction is not a gap in the literature; it is the Cauchy–Schwarz/Jensen inequality, and it is exactly zero only in the constant-volatility model the application exists to reject. **The correct advice therefore changes not at all: change the loss, not the grid and not the proxy.**

## 3. LO-7 — external positioning, and the GMV question underneath it

### 3.1 C-7.1 — the GMV blindness theorem

For \(H\succ0\) the global-minimum-variance weights are \(w(H)=H^{-1}\mathbf 1/(\mathbf 1^\top H^{-1}\mathbf 1)\).

**Theorem.** \(w(H_1)=w(H_2)\iff H_1^{-1}\mathbf 1\parallel H_2^{-1}\mathbf 1\). Consequently:
1. \(w(cH)=w(H)\) for every \(c>0\), **exactly**;
2. \(w\) depends on \(H\) only through the ray \([H^{-1}\mathbf 1]\in\mathbb{RP}^{m-1}\), i.e. through **\(m-1\)** real parameters out of the \(m(m+1)/2\) that specify \(H\). At \(m=12\) that is 11 of 78; **67 of the 78 degrees of freedom of the forecast are invisible to GMV**;
3. any evaluation statistic that is a function of \(w(H)\) alone — realised GMV portfolio variance \(w^\top\Sigma^\ast w\), GMV turnover, GMV Sharpe ratio — inherits the same blindness.

*Proof.* \(w(H_1)=w(H_2)\) means the two normalised vectors coincide, i.e. \(H_1^{-1}\mathbf 1=\kappa H_2^{-1}\mathbf 1\) for \(\kappa>0\). Scaling: \((cH)^{-1}\mathbf 1=c^{-1}H^{-1}\mathbf 1\), same ray. The invariance set of a given ray is \(\{H\succ0:H^{-1}\mathbf 1=\kappa v\}=\{H\succ0:\mathbf 1=\kappa Hv\}\), which is \(m\) linear constraints with one free scalar \(\kappa\), hence codimension \(m-1\) in \(\mathrm{Sym}(m)\). ∎

**A pure multiplicative level bias in a covariance forecast is therefore completely undetectable by a GMV-portfolio evaluation.** This is elementary, and it is exactly why the question is worth asking.

### 3.2 C-7.2 — how much of the actual distortion GMV sees

- **AIRM.** By B-3.7 the Wishart-case AIRM distortion is \(H^\star=(1-\tfrac{m+1}{2M})\Sigma\) to second order. "Entirely invisible" does not follow from second-order scalarity — but it is nonetheless **exactly true**, by an argument the first draft did not give (O-16): the AIRM Karcher mean is congruence-equivariant and the Wishart law is orthogonally invariant, so \(H^\star=h\Sigma\) **exactly**, with \(\log h=\tfrac1m\big[\sum_{i=1}^m\psi\big(\tfrac{M+1-i}2\big)+m\log2-m\log M\big]\). Under the second-moment condition (3.4) alone the exactness genuinely fails; it is a property of the Wishart law. By C-7.1(1) the distortion is therefore **entirely invisible** to GMV. A model trained to minimise an AIRM loss will be shrunk by \(\approx31\%\) at the flagship configuration and a GMV evaluation will report nothing at all.
- **Bures–Wasserstein.** By B-3.5 the distortion is a spectral shrink that is *not* a scalar multiple (small eigenvalues shrink more). Writing \(H^\star=\Sigma-\operatorname{diag}(\beta_i\lambda_i)\), the visible part is only the deviation of \(\beta_i\) from its mean; at \(m=12,M=21\) with the spectrum \(3.0\to0.5\), \(\beta\) ranges over \([0.088,0.359]\), so the *scalar* component (\(\approx0.19\)) is invisible and only the residual spread is visible. At exactly that configuration the induced weight change is \(\|\Delta w\|=0.040\), about \(12\%\) of \(\|w\|\) — but the statistic that matters is the **excess realised GMV variance**, which is \(1.17\%\) in \(\Sigma\)'s eigenbasis and \(1.43\%\) in a random basis. A one-percent excess variance is what a 240-month panel would have to detect, and that is the honest quantification; the first draft asserted "negligible against sampling noise" without computing anything.
- **log-Euclidean.** Diagonal under (3.4) and, in the isotropic case, a scalar multiple; its visible component is likewise only the spectral residual.

**So the sharpened claim is:** GMV evaluation is *exactly* blind to the scalar component of the distortion, which is the whole of it for AIRM and the bulk of it for BW and log-Euclidean.

### 3.3 C-7.3 — what does detect it

Any evaluation that consumes the forecast's level rather than only its GMV weights:
- realised-versus-forecast portfolio variance (a calibration regression of \(w^\top\Sigma^\ast w\) on \(w^\top Hw\)): the slope is exactly \(1/(1-\beta)\) under a scalar distortion;
- Gaussian VaR exceedance rates: a \(1-\beta\) level distortion multiplies the VaR by \(\sqrt{1-\beta}\) and inflates exceedances;
- QLIKE and Frobenius losses, which are proxy-robust by A-1.6 and by construction see the level.

This is the constructive half of LO-7 and it is what should be reported: *if a method is trained on a geodesic loss, its output must be evaluated with a level-sensitive, proxy-robust metric, because the standard economic evaluation is blind to the exact distortion the training loss induces.*

### 3.4 C-7.4 — the verbatim external record

The narrow citation-audit agent identified and full-text-verified **Bucci, Palma and Zhang, "Geometric Deep Learning for Realized Covariance Matrix Forecasting", arXiv:2412.09517**. Verified verbatim (full record and quotations in [[P1-LOSS — LO-7 external positioning audit]]):
- the headline **training loss is the log-Euclidean (Riemannian/SPD-geodesic) distance**, their Eq. (7), reported as outperforming an MSE/Euclidean loss;
- the paper **evaluates economically via a global-minimum-variance portfolio**, their §5 and Table 4;
- the paper's only proxy-robustness remark cites Laurent–Rombouts–Violante (2013) and is **scoped to the Frobenius/Euclidean evaluation metrics**, not to the log-Euclidean training loss;
- the paper is **silent** on whether a geodesic training loss is proxy-robust and on whether a GMV evaluation could detect a resulting bias.

**Statement of record, in the narrowest form the evidence supports:** *This paper trains on a loss that the present campaign proves is not proxy-robust (A-4.4; and which Laurent–Rombouts–Violante independently classify as non-robust under the name "log-Frobenius"), and evaluates with a criterion the present campaign proves is blind to the scalar component of the induced distortion (C-7.1). The paper does not discuss either point. Nothing here asserts that the authors claimed otherwise, and nothing here asserts that their empirical findings are wrong.*

Two limitations travel with this and must not be dropped: it is an **arXiv preprint**, not confirmed peer-reviewed at the time of audit; and **silence is not error**. Five other candidate papers were screened and rejected on structural grounds; the list and reasons are in the audit file.

### 3.5 C-7.5 — the reformulation

The informal analysis stated one compound claim. It splits into two, with different statuses:
- *"the paper trains on a non-robust loss"* — **verified**, in the narrow form above, from the paper's own displayed Eq. (7) plus this campaign's A-4.4 and LRV's own classification;
- *"its GMV evaluation cannot detect the resulting bias"* — **this is a theorem of the present campaign (C-7.1/C-7.2), not an attribution to any author.** Presenting it as a defect the authors committed would misrepresent them. It is presented here as a general property of GMV evaluation.

**REFORMULATED+PROVED.**

## 4. C-ATT — the standing attack: can a non-flat robust metric be built?

The campaign's most valuable possible outcome would be a construction. It does not exist, and the futility is a theorem rather than a report of failed attempts.

**Impossibility.** By A-4.3, a symmetric loss is proxy-robust over a rich class iff it is \(\tfrac12\langle y-h,\mathcal A(y-h)\rangle\) for a constant \(\mathcal A\); by A-4.2 the corresponding metric is constant, hence flat with the proxy coordinate as an affine chart. There is no room for a non-flat example. Any purported construction must therefore violate one named hypothesis, and it is worth recording which hypothesis each tempting candidate violates, because each violation is a real (if limited) escape and they are exactly E1–E4:

| Candidate | Why it fails | Which hypothesis it attacks |
|---|---|---|
| a metric that is flat in a nonlinear chart (log-Euclidean, Cholesky-flat, any \(\Phi^\ast(\text{Euclidean})\) with \(\Phi\) nonlinear) | flat but not affinely charted by the proxy coordinate; not a quadratic form in \(y-h\) | none — it is simply not robust (A-4.4) |
| the commuting/fixed-eigenbasis BW orthant | genuinely flat *and* affinely charted — by \(\Sigma\mapsto\Sigma^{1/2}\). It **would** be robust for a proxy unbiased for \(\Sigma^{1/2}\) | the proxy coordinate — this is E3, and E3 is closed negatively (§2) |
| a curved metric evaluated only on a restricted forecast set | \(\Gamma\) constant on level sets only | the forecast class — this is E4, closed in dossier A §5 |
| a curved metric with the Jensen gap subtracted | the corrected object is not a metric-squared and not a robust loss; it is a feasible \(O(\varepsilon^3)\) repair | the robustness notion — this is E1, closed in dossier A §4 |
| a curved metric with an asymmetric "divergence" built from it (e.g. KL from Fisher–Rao) | this **succeeds**, and it is not a counterexample: the resulting object is a Bregman divergence and is not a geodesic distance | symmetry — which is precisely what LO-4 identifies as the obstruction |

The last row is the constructive content of the whole campaign and is worth stating positively: **every Riemannian geometry the project uses does supply a robust loss — but its divergence, not its distance.** For the Fisher–Rao/AIRM geometry that divergence is KL, i.e. multivariate QLIKE. For the flat Euclidean structure it is the squared Frobenius distance. Asymmetry is the feature, not the bug.

## 5. Intermediate-claim register (transitive closure input)

| Node | Terminal status |
|---|---|
| C-E2.1 barycentre target is measurement-scheme dependent | PROVED |
| C-E2.2 latent barycentre not estimated by BW-loss minimisation | PROVED (with the consistency-under-infill caveat recorded) |
| C-E2.3 decision-theoretic cost | PROVED |
| C-E2 route verdict | DISPROVED as an escape |
| C-E3.1 scalar unbiased-for-\(\sigma\) estimator exists under two strong hypotheses | PROVED |
| C-E3.2 Cauchy–Schwarz separation of \(\int\sigma\) and \((\int\sigma^2)^{1/2}\) | PROVED |
| C-E3.3 matrix obstruction, two independent causes | PROVED |
| C-E3.4 log coordinate obstruction + singularity at \(M<m\) | PROVED |
| C-E3 route verdict | DISPROVED as an escape |
| C-7.1 GMV blindness theorem | PROVED |
| C-7.2 quantified visibility per geometry | PROVED |
| C-7.3 level-sensitive evaluations detect it | PROVED |
| C-7.4 Bucci–Palma–Zhang verbatim record | CITED+APPLIED |
| C-7.5 split of the compound informal claim | REFORMULATED+PROVED |
| C-ATT impossibility of a non-flat robust metric | PROVED |
| the five other LO-7 candidate papers | OUT OF SCOPE BY PROVED SEPARATION — screened and rejected on structural grounds; no claim consumes them |

No node in this dossier is left non-terminal.
