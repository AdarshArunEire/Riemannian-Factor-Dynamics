---
type: canonical-theorem-boundary
title: P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary
status: canonical
last-audited: 2026-08-14
scope: evaluation only
authority: which loss may be used to score a covariance forecast against an imperfect proxy, and the exact bias induced by using one that may not
---

# P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary

> **Scope lock — read before consuming anything here.** This file governs **evaluation only**: how a forecast built on the project's estimator should be *scored*. It is **downstream of every identification and estimation theorem** in the programme. It consumes [[P1-ID — centre-drift and factor identification boundary]] §14.2 (existence and uniqueness of the Bures–Wasserstein Fréchet mean) and nothing else from the canon; it produces nothing that any estimation theorem consumes. The proved separation is §6. It changes no estimand, no rate, no assumption, and no application's standing.
>
> Proof provenance: [[P1-LOSS — lead ledger]], [[P1-LOSS-A — decision theory and characterisation]], [[P1-LOSS-B — geometry and exact biases]], [[P1-LOSS-C — targets, proxies, and external claims]], with the two non-author hostile audits [[P1-LOSS — Wave 3 audit A]] and [[P1-LOSS — Wave 3 audit BC]]. Archive location does not determine status; this file does.

## 0. Vocabulary (locked)

**Target functional** — the conditional functional a forecast reports; here the conditional mean \(\Sigma=\mathbb E[\Sigma^\ast\mid\mathcal F]\). **Proxy** \(\widehat\Sigma\) — an observable ex-post estimate, *conditionally unbiased in a stated coordinate*. **Loss** \(L(\text{realisation},\text{forecast})\). **Forecast class** \(\mathcal H\) — the forecasts actually compared. **Proxy-robust** — the expected-loss ranking under the proxy equals the ranking under the truth, for all compared forecasts and all admissible proxy laws. **Consistent for \(\theta\)** — \(\theta\) minimises expected loss.

Robustness is a property of a **pair** (loss, proxy coordinate), never of a loss alone. Estimation and evaluation are never interchanged: estimation produces \(\hat\mu_n,\widehat E_n\) from the observed array; evaluation scores a forecast against a proxy.

## 1. LO-1 — the proxy-robust class

**Theorem LO-1.** Let \(\mathcal H\subseteq\operatorname{int}\mathcal Y\) be open and convex in \(\mathrm{Sym}(m)\), let \(L\ge0\) with \(L(H,H)=0\), and let \(L\) be proxy-robust over a class containing every finitely supported law whose mean lies in \(\mathcal H\). Then \(L\) is strictly consistent for the conditional mean, and \(L\) is a **Bregman divergence**
\[
L(y,H)=B_\psi(y,H)=\psi(y)-\psi(H)-\langle\nabla\psi(H),y-H\rangle,\qquad\psi\ \text{convex on }\operatorname{conv}\mathcal Y .
\]
Conversely every such \(B_\psi\) is proxy-robust, and the proxy shifts every expected loss by **one common constant** — the Jensen gap \(\mathbb E\psi(\widehat\Sigma)-\psi(\Sigma)\) — so loss *differentials*, not merely rankings, are unchanged.

**Status: PROVED INTERNALLY** for the robustness ⟹ consistency step and the converse; **CITED EXTERNALLY AND APPLIED** for the consistency ⟹ Bregman step — Laurent–Rombouts–Violante (2013) Proposition 3 in the matrix case, Gneiting (2011) Theorem 3.1 (attributed there to Savage) in the scalar case. An internal multivariate proof is also recorded and needs three-atom richness.

Three scope facts are load-bearing and must travel with any use of LO-1:
1. **Patton (2011) and Gneiting (2011) are scalar.** Only LRV Proposition 3 is stated for matrix-valued forecasts. Using a scalar characterisation for the project's matrix problem is an error the campaign made and corrected.
2. **Two-atom richness is not enough** once \(m\ge2\); it yields only an odd-homogeneity condition. Three atoms suffice.
3. **The equivalence is class-dependent.** On a restricted class of proxy laws, non-Bregman losses can be consistent for the mean. That is not a loophole in LO-1; it is the exact content of routes E1 and E4.

**Multivariate QLIKE and a singular proxy.** For \(\psi=-\log\det\), \(L=\operatorname{tr}(H^{-1}\widehat\Sigma)-\log\det(H^{-1}\widehat\Sigma)-m\). The **loss level** requires \(\widehat\Sigma\succ0\); the **ranking** does not — the differential \(\operatorname{tr}\{(H_1^{-1}-H_2^{-1})\widehat\Sigma\}+\log\det(H_1/H_2)\) is linear in \(\widehat\Sigma\) and finite for any PSD proxy. Near-singular realised covariances therefore disqualify QLIKE *levels*, not QLIKE *ranking*. Only the forecasts must be positive definite.

## 2. LO-4 — the no-go, in its sharp form

**Theorem LO-4.** Let the proxy be conditionally unbiased in the linear coordinate of \(V\), let \(\mathcal Q\) be rich, and let \(L\) be **symmetric** on \(\mathcal H\times\mathcal H\), nonnegative, vanishing on the diagonal, differentiable in its first argument. Then
\[
L\ \text{is proxy-robust}\iff L(y,h)=\tfrac12\langle y-h,\mathcal A(y-h)\rangle,\quad \mathcal A\succeq0\ \text{fixed}.
\]
Consequently, for a squared geodesic distance \(d_g^2\) of a metric \(g\) on an open convex \(\mathcal X\subseteq V\):
\[
\boxed{\ d_g^2\ \text{is proxy-robust}\iff g\ \text{is a constant metric in the proxy's unbiasedness coordinate,}\ }
\]
equivalently iff \((\mathcal X,g)\) is **flat and that coordinate is an affinely parametrised geodesic chart** for \(g\).

**Status: SHARPLY REFORMULATED AND PROVED.** The informal headline — "the robust class is flat" — is **necessary but not sufficient**, and the campaign's principal correction is to replace it with the displayed criterion.

Three hypotheses travel with the statement and are not decoration: \(\mathcal A\succeq0\) and not \(\succ0\) (a degenerate quadratic form is robust; \(\succ0\) is what *strict consistency* needs); symmetry typechecks only on \(\mathcal H\times\mathcal H\); and "affinely parametrised" is stronger than "straight geodesics" — the Klein model has straight geodesics and curvature \(-1\).

### 2.1 What the theorem excludes, and why each is excluded

| Geometry | Flat? | Robust for a \(\Sigma\)-unbiased proxy? | Reason |
|---|---|---|---|
| squared Frobenius / Mahalanobis on \(\mathrm{Sym}(m)\) | yes | **yes** | it *is* the constant-metric case |
| Bures–Wasserstein | no (nonnegatively curved, strictly so in noncommuting directions) | **no** | curvature |
| AIRM / Fisher–Rao for centred Gaussians | no (Hadamard) | **no** | curvature |
| **log-Euclidean** | **yes** | **no** | flat but the proxy is not unbiased in \(\log\Sigma\) — the witness separating flatness from robustness |
| Cholesky-flat and any \(\Phi^\ast(\text{Euclidean})\), \(\Phi\) nonlinear | yes | **no** | same misalignment |
| fixed-eigenbasis BW orthant | yes, and affinely charted by \(\Sigma\mapsto\Sigma^{1/2}\) | **only** for a \(\Sigma^{1/2}\)-unbiased proxy | no such proxy exists — route E3 |
| spheres, sphere products | no | **no** | curvature |

The log-Euclidean row is independently corroborated: LRV (2013) list "log-Frobenius" among their **non-robust** losses.

### 2.2 The constructive contrast that should be reported alongside the no-go

The theorem is about **symmetry**, so it also excludes symmetrised divergences at one stroke — and it points at the repair. Every Riemannian geometry the project uses *does* supply a robust loss; it is the geometry's **divergence**, not its **distance**:

| Object | Symmetric | Bregman in \(\Sigma\) | Robust |
|---|---|---|---|
| Fisher–Rao / AIRM geodesic distance squared | yes | no | **no** |
| KL divergence of the same Gaussian family \(=\tfrac12\) multivariate QLIKE | no | yes, \(\psi=-\log\det\) | **yes** |
| Euclidean distance squared on \(\mathrm{Sym}(m)\) | yes | yes, \(\psi=\|\cdot\|_F^2\) | **yes** |

Asymmetry is the property that makes a divergence usable, not a defect to be repaired by symmetrising.

## 3. LO-2 and LO-3 — the induced target and the exact bias

**LO-2. Squared Bures–Wasserstein distance is not proxy-robust. DISPROVED as a robust loss.** \(A\mapsto d_{\rm BW}^2(A,H)\) is strictly convex, not affine, in the realisation; its minimiser is the BW Fréchet barycentre of the conditional law of the **proxy**, characterised by \(\mathbb E[(H^{1/2}\widehat\Sigma H^{1/2})^{1/2}]=H\).

**Exact counterexample (closed form).** \(m=1\), \(\Sigma=1\), proxy on two points \((1\pm a)^2\) with \(\mathbb P[(1+a)^2]=\frac{2-a}4\), \(a\in(0,1)\) — conditionally unbiased. Compare \(H_1=1\) (the conditional mean) and \(H_2=(1-\tfrac{a^2}2)^2\). True losses \(0\) and \(\tfrac{a^4}4\); proxy-expected losses \(a^2\) and \(a^2-\tfrac{a^4}4\). **The ranking reverses for every such \(a\): the true conditional mean is strictly beaten by its own shrunk version.** Feature responsible: strict concavity of \(\sqrt\cdot\); classification: *coordinate-induced*. Lifts to \(m\ge2\) on the scalar ray.

**LO-3, scalar — exact, not asymptotic.**
\[
\boxed{\ H^\star=(\mathbb E\sqrt x)^2=\mathbb E[x]-\operatorname{Var}(\sqrt x).\ }
\]

**LO-3, matrix — second order.** With \(\widehat\Sigma=\Sigma+\Delta\), \(\mathbb E\Delta=0\),
\[
H^\star=\Sigma-\Sigma^{-1/2}\mathbb E[G^2]\Sigma^{-1/2}+O(\varepsilon^3),\qquad \Sigma G+G\Sigma=\Sigma^{1/2}\Delta\Sigma^{1/2},
\]
equivalently, in \(\Sigma\)'s eigenbasis,
\[
B_{ij}=-\sum_k\frac{\lambda_k\,\mathbb E[\Delta_{ik}\Delta_{kj}]}{(\lambda_i+\lambda_k)(\lambda_k+\lambda_j)} .
\]
The **off-diagonal entries are the eigenvector rotation**; for \(\lambda_i\ne\lambda_j\) the rotation angle is \(B_{ij}/(\lambda_i-\lambda_j)+O(\|B\|^2)\).

### 3.1 Is the distortion spectral or does it rotate the eigenbasis? — the question that mattered most

**Both answers are true, of different proxy classes, and the distinction must be declared rather than assumed.**

- **General proxy: it rotates. DISPROVED as a general claim.** An explicit conditionally unbiased two-point proxy on \({\rm SPD}(3)\) produces nonzero \(B_{13}=\epsilon^2\lambda_2/\{(\lambda_1+\lambda_2)(\lambda_2+\lambda_3)\}\) and a genuinely rotated induced eigenbasis.
- **Wishart / Gaussian fourth-moment proxy: it does not rotate, exactly and at every order. PROVED.** If \(\operatorname{Cov}(\widehat\Sigma_{ab},\widehat\Sigma_{cd})=\tfrac1M(\Sigma_{ac}\Sigma_{bd}+\Sigma_{ad}\Sigma_{bc})\) then \(B_{ij}=0\) for \(i\ne j\) at second order; and for a genuine Wishart law the induced target is diagonal **exactly**, by sign-flip equivariance of the law together with orthogonal equivariance and uniqueness of the BW barycentre (P1-ID §14.2). The closed diagonal form is
\[
\boxed{\ B_{ii}=-\frac{\lambda_i}{M}\left[\frac14+\sum_{k=1}^m\frac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\right].\ }
\]
- **AIRM:** \(B_{ij}=-\tfrac12\sum_k\mathbb E[\Delta_{ik}\Delta_{kj}]/\lambda_k\); under the Wishart tensor, \(B^{\rm AIRM}_{ii}=-\lambda_i(m+1)/(2M)\), a **pure uniform shrink**, and exactly so for a genuine Wishart.
- **Log-Euclidean:** the induced target is exactly \(H^\star=\exp\mathbb E[\log\widehat\Sigma]\).

**Consequence for the programme, stated so it cannot be over-read.** The claim "the distortion is almost entirely in the eigenvalues" is a property of the **noise model**, not of Bures–Wasserstein geometry. For the flagship proxy class it is exactly true and the identified directions are untouched. For a general proxy it is false. An application that wants the protection must **declare the proxy's fourth-moment structure and check it**, exactly as it declares its centre convention.

## 4. LO-5 — how large, how fast it vanishes, and what recalibration restores

**Size.** The relative distortion is \(\dfrac{|B_{ii}|}{\lambda_i}=\dfrac1M\Big[\dfrac14+\sum_k\dfrac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\Big]\), with exact range
\[
\frac1{2M}\ \le\ \frac{|B_{ii}|}{\lambda_i}\ \le\ \frac{m-\tfrac12}{M},
\qquad\text{isotropic value }\frac{m+1}{4M};
\qquad
\text{AIRM: }\frac{m+1}{2M}\ \text{uniformly}.
\]
**It grows linearly in matrix size.** The governing ratio is \(m/M\), not \(1/M\).

**At the project's flagship configuration it is not small.** For \(m=12\) assets and monthly realised covariance built from \(M\approx21\) daily returns, with spectrum \(3.0\to0.5\), the **exact** distortions (computed from exactly solved barycentres, not from the expansion) are

| | BW | AIRM |
|---|---|---|
| \(m=12,\ M\approx21\) (monthly RC from daily returns) | **8.82% – 35.86%** | **32.92%** |
| \(m=12,\ M\approx78\) (daily RC from 5-minute returns) | ≈ 2.4% – 9.0% | ≈ 8.3% |
| \(m=12,\ M\approx1638\) (monthly RC from 5-minute returns) | ≈ 0.11% – 0.43% | ≈ 0.40% |

The second-order formula understates the exact values by 3–8% of themselves and is labelled as an approximation wherever it is used.

**Infill (E5, first half).** The distortion is the proxy's conditional variance passed through a fixed bounded linear map, so it is \(\Theta(M^{-1})\) — no geometric amplification, no geometric cancellation. It is **not uniform** over the forecast class: the Jensen gap satisfies \(\Gamma(cH)=\sqrt c\,\Gamma(H)\) exactly, so it is degree-\(\tfrac12\) homogeneous and degrades as \(\lambda_{\min}(H)\to0\).

**Spectral compression.** \(|B_{ii}|/\lambda_i\) is decreasing in \(\lambda_i\): BW shrinks small eigenvalues proportionally more, so the *evaluation target's* spectrum is compressed. This is a statement about what the loss rewards, not about the estimator's eigengap \(\Delta_n\) — see §6.

**Recalibration — the sharpest statement in the constructive half.**
- Recalibration **restores the location of the optimum**, exactly, when the induced-target map \(\Phi\) is known: the required map is \(\rho=\Phi\) **itself**, not its inverse. Read plainly, *a forecaster whose belief is the conditional mean must shrink before submitting in order to win a contest scored by a geodesic loss.*
- Recalibration **can never restore ranking robustness**. Reparameterising the second argument cannot change the first argument's convexity, and robustness is a property of the first argument. **Recalibration fixes the target; only the loss class fixes the ranking.**
- A **scalar** recalibration is exact for **AIRM** — \(c=1-\frac{m+1}{2M}\), and exactly at all orders for a genuine Wishart — and only partial for **BW**, which leaves the spectral compression behind. That asymmetry between the two geometries is worth reporting.
- A **gap-corrected loss** \(L^\ast=d_{\rm BW}^2-\widehat\Gamma(H)\), with \(\widehat\Gamma\) built from a known conditional fourth-moment tensor, reduces the ranking distortion from \(O(\varepsilon^2)\) to \(O(\varepsilon^3)\). It is **not** a robust loss and must not be called one.

## 5. The five escape routes — each terminal

| Route | Verdict | Content |
|---|---|---|
| **E1** — weaken the robustness notion | **REFORMULATED AND PROVED** | Monotone transformation of the loss buys nothing (the induced rankings are identical). **Local robustness** holds: BW ranks correctly *if* the forecasts' distance from the truth exceeds the distortion scale, \(\eta\gg\varepsilon^2/\|\Sigma\|\) — so ordinary model horse-races are usually safe. But the failure region is the near-optimal region, and at \(\eta=0\) the ranking is *always* wrong. Restricting the proxy class admits the gap-corrected loss, at the price of a fourth-moment model. **No weakening admits a non-flat geodesic loss as exactly robust.** |
| **E2** — retarget to the conditional Fréchet barycentre | **DISPROVED as an escape** | The barycentre *of the proxy* depends on the proxy's conditional variance, hence on the sampling frequency \(M\): two analysts sampling at 5 and 30 minutes face different targets. **A target that moves when you change your grid is not an estimand.** The barycentre *of the latent* \(\Sigma^\ast\) is a legitimate DGP functional, but BW-loss minimisation is only **consistent** for it as \(M\to\infty\), never conditionally unbiased at fixed \(M\) — and consistency is exactly what LO-1 cannot use. Decision cost: portfolio variance \(w^\top\Sigma w\) is **linear** in \(\Sigma\), so the conditional mean is the decision-relevant functional; a barycentre target understates portfolio variance by the §4 percentages and Gaussian VaR by their square root. **If ever adopted, it is a convention change of exactly the kind P1-ID exists to police and must be labelled one.** |
| **E3** — change the proxy | **DISPROVED as an escape**, with a stated boundary | Robustness would need a proxy unbiased for \(\Sigma^{1/2}\) or \(\log\Sigma\). With no auxiliary knowledge of the within-window volatility path: the absolute-variation/bipower family is excluded because its infill limit is \(\int\sigma\,ds\), and \(\int_0^1\sigma\,ds\le(\int_0^1\sigma^2ds)^{1/2}\) by Cauchy–Schwarz with equality iff \(\sigma\) is a.e. constant; and every continuous function of realised covariance is conditionally biased for \(\Sigma^{1/2}\) by strict operator concavity of the square root. For \(\log\Sigma\) the obstruction is strict operator Jensen, plus \(\log\widehat\Sigma\) being undefined when \(M<m\). A general impossibility over *all* estimators is **not** claimed: with a *known* within-window volatility shape one exists — and an application that has that knowledge has assumed away the problem the proxy exists to solve. |
| **E4** — restrict the forecast class | **REFORMULATED AND PROVED** | Ranking is preserved exactly on any set where the Jensen gap \(\Gamma(H)=2\{G(H,\Sigma)-\mathbb EG(H,\widehat\Sigma)\}\) is constant — an explicitly computable codimension-one family — and on symmetry orbits of the pair (target, proxy law). Constancy is *sufficient*; it is necessary only on classes containing an indifference pair. **Since \(\Gamma(cH)=\sqrt c\,\Gamma(H)\) exactly, no admissible class contains two distinct multiples of one forecast.** Neither "common trace" nor "common spectrum" is admissible. The distortion therefore contaminates *level-differing* comparisons maximally — which is what a shrinkage-versus-factor-model comparison is. Closed form: the proxy-optimal scale is \(\big(1-\Gamma(H_0)/2G(H_0,\Sigma)\big)^2\) times the true one. |
| **E5** — infill asymptotics | **REFORMULATED AND PROVED** | The distortion falls at \(\Theta(M^{-1})\) with a constant growing linearly in \(m\). Raising \(M\) conflicts with microstructure noise, whose naive realised-covariance bias is \(\Theta(M)\) — the two move in opposite directions, so the optimum is interior and **neither effect is negligible there**. The noise-robust estimators (two-scale, realised kernels, pre-averaging) are established as **consistent**, not conditionally unbiased, and the efficient pre-averaging form is not guaranteed positive semidefinite — so it can leave the domain a geodesic loss needs. Separately, conditional unbiasedness of realised covariance is itself exact only when the drift vanishes; a drift contributes at \(\Theta(M^{-1})\), the same *order* as the distortion though with a much smaller constant. **Infill is not a clean escape: it trades a proved \(\Theta(m/M)\) distortion for an unproved conditional-unbiasedness premise. The advice is to change the loss, not the grid.** |

**No sixth route exists within the theorem's hypotheses**, and the impossibility of constructing a non-flat robust geodesic loss is a corollary of LO-4 rather than a report of failed attempts: any purported construction must violate one named hypothesis, and each such violation is one of E1–E4.

## 6. LO-6 — the proved separation from the estimation theorems

**Theorem LO-6.** No node of this file is an ancestor of any node in the estimation or identification dependency graph.

*Proof by edge audit.* The estimation chain's nodes — the three-scale moving centre \(\hat\mu_n\), the polygonal frame, the lag operator \(\widehat{\mathbb L}_n\), the row error \(d_n\), the assembly \(\eta_n=2A_{2,n}d_n+d_n^2\), Davis–Kahan, the selectors, and every P1-ID identified object — are functionals of the **observed array** \((X_{t,n})\) alone. None is defined by minimising a forecast loss against a proxy, and none takes a forecast as an argument. The evaluation node takes as input a pair (forecast, proxy) and returns a scalar ranking; it has no outgoing edge into the estimator's definition. Hence no closed **P1-ID, HD1, HE, BW-FIXED-MARGIN, BW-SHRINKING-MARGIN or FRAME-2P-U** node is disturbed. ∎

**The one real edge, stated rather than hidden.** The estimator *does* contain a Fréchet-mean step, and if the observed \(X_{t,n}\) are themselves proxies of a latent \(\Sigma^\ast_t\), then \(\hat\mu_n\) estimates the barycentre of the **observed** law, which differs from the barycentre of the latent law by the §3 formula at order \(\Theta(m/M)\). This is not a defect in any theorem: **CANON-1 defines the estimand from the observed law**, and every estimation theorem is stated for the observed array. What the edge does is quantify a measurement-error term that the canon already routes to two existing budgets:

1. the **target-defect budget (P1-OP-zeta)**: a smooth deterministic \(O(m/M)\) perturbation of the centre path is a reference change of that size, contributing \(\zeta_n^{\rm proxy}=O(m/M)\) times the energy scale to the existing \(\zeta_n\), with the loading rate already stated as \(O_p\{(n^{-1/2}+\ell_n+\zeta_n)/\Delta_n^0\}\);
2. the **APP-FIN measurement-error item** in [[OPEN OBLIGATIONS — current research actions]] §3, which already requires quantifying covariance-estimation measurement error, dependence, and included-lag contamination.

No theorem changes, no rate changes, and no budget is newly introduced. The contribution of P1-LOSS is to give that pre-existing budget an explicit order and an explicit constant.

**Two things this file does *not* license.** It does not license reading the §4 spectral compression as a statement about \(\Delta_n\): \(\Delta_n\) is the eigengap of the lag operator on the observed array and is untouched. And it does not license any change to the identified estimand \(\mathcal S_{X,n}\).

## 7. LO-7 — external positioning, only as far as it was verified

**Verified verbatim.** Bucci, Palma and Zhang, "Geometric Deep Learning for Realized Covariance Matrix Forecasting", arXiv:2412.09517: the headline **training loss is the log-Euclidean distance** (their Eq. 7), reported as outperforming an MSE/Euclidean loss; the paper **evaluates economically via a global-minimum-variance portfolio** (their §5, Table 4); its only proxy-robustness remark cites Laurent–Rombouts–Violante (2013) and is scoped to the Frobenius/Euclidean **evaluation** metrics. The paper is **silent** on whether a geodesic training loss is proxy-robust. It is an arXiv preprint, not confirmed peer-reviewed at the time of audit.

**Statement of record, in the narrowest form the evidence supports.** This paper trains on a loss that §2 proves is not proxy-robust — and which LRV independently classify as non-robust under the name "log-Frobenius" — and evaluates with a criterion §7.1 proves is blind to the scalar component of the induced distortion. *The paper does not discuss either point. Nothing here asserts that its authors claimed otherwise, and nothing here asserts that their empirical findings are wrong. Silence is not error.*

### 7.1 GMV blindness — a theorem of this campaign, not an attribution

**Theorem.** For \(H\succ0\), the global-minimum-variance weights \(w(H)=H^{-1}\mathbf 1/(\mathbf 1^\top H^{-1}\mathbf 1)\) satisfy \(w(H_1)=w(H_2)\iff H_1^{-1}\mathbf 1\parallel H_2^{-1}\mathbf 1\). Hence \(w(cH)=w(H)\) **exactly** for every \(c>0\), and \(w\) depends on \(H\) only through the ray \([H^{-1}\mathbf 1]\), i.e. through \(m-1\) of the \(m(m+1)/2\) parameters — **11 of 78 at \(m=12\)**; the Jacobian of \(H\mapsto w(H)\) has numerical rank exactly \(11\). Every statistic that is a function of the GMV weights alone — realised GMV variance, GMV turnover, GMV Sharpe — inherits the blindness.

Consequently: the **AIRM** distortion, being exactly a scalar multiple for a Wishart proxy, is **entirely invisible** to a GMV evaluation; the **BW** distortion is only partially visible — at the flagship configuration it moves the weights by \(\|\Delta w\|=0.040\) but raises realised GMV variance by only about \(1.2\%\).

**What does detect it:** calibration of realised against forecast portfolio variance; Gaussian VaR exceedance rates; and QLIKE or Frobenius losses, which are proxy-robust and level-sensitive. *A method trained on a geodesic loss must be evaluated with a level-sensitive, proxy-robust metric, because the standard economic evaluation is blind to the distortion its training loss induces.*

## 8. What Paper 1 should report

1. **Report Frobenius and multivariate QLIKE.** Both are proxy-robust by LO-1; QLIKE's ranking survives a singular proxy, its level does not.
2. **Do not score forecasts with squared Bures–Wasserstein, AIRM, or log-Euclidean distance**, and do not train on them either. If one is reported for comparability with the literature, report it *alongside* a robust loss and state the induced target.
3. **If a geodesic loss is used at all, apply the §4 recalibration and say so.** For AIRM the scalar \(c=1-\frac{m+1}{2M}\) is exact; for BW it is partial.
4. **Declare the proxy's coordinate of unbiasedness** and, if the eigenvector-protection of §3.1 is relied on, declare and check the fourth-moment structure.
5. **None of this changes the estimator, the estimand, the rates, or the application set.** The scientific contribution of Paper 1 remains the moving-centre estimator, the identified subspace, and the rate theorems. This is a scope condition on how results are reported.

## 9. Claims excluded from this boundary

- "the proxy-robust class is flat" without the affine-parametrisation clause;
- a symmetric loss, geodesic or otherwise, presented as robust because its geometry is natural;
- the "purely spectral" distortion claim without its fourth-moment hypothesis;
- recalibration presented as restoring ranking robustness;
- a gap-corrected loss presented as a robust loss;
- infill presented as a clean escape from LO-4;
- the conditional Fréchet barycentre presented as an identified estimand without the convention label;
- consistency of a noise-robust proxy presented as conditional unbiasedness;
- Patton (2011) or Gneiting (2011) cited for the matrix case;
- any statement that a named author's method is defective, where the paper is silent on the point;
- any reading of §4's spectral compression as a statement about the estimator's eigengap \(\Delta_n\).

## 10. Related notes

- [[Analytical reconstruction — proof ledger and rebuilt spec]] — programme status and the estimation⟶evaluation edge
- [[Paper 1 — Locally stationary Riemannian factor model]] — the estimator whose output is scored
- [[P1-ID — centre-drift and factor identification boundary]] — §14.2 supplies BW Fréchet-mean existence and uniqueness
- [[Application map — geometry, symmetry, and rate accelerators]] — §0A evaluation declaration
- [[Numerical suite — theorem-driven design matrix]] — N-19, the evaluation diagnostic
- [[References and external claim audit]] — Patton, LRV, Gneiting, Boissonnat–Nielsen–Nock, and the measurement-error sources
