---
type: working-proof-dossier
title: P1-LOSS-A — decision theory and characterisation
status: active-campaign
last-audited: 2026-08-14
authorship: authored by the campaign lead after the Wave-1 agent interruption (see [[P1-LOSS — lead ledger]] §1). The lead is therefore NOT an admissible non-author auditor of this dossier.
---

# P1-LOSS-A — decision theory and characterisation

Owns LO-1, LO-4, and routes E1, E4.

## 0. Claim table

| ID | Exact statement | Assumptions | Conclusion | Proof | Status | Known weak point |
|---|---|---|---|---|---|---|
| ~~A-1.1~~ | ~~robustness alone forces \(L(y,h)=\psi(y)+a(h)+\langle b(h),y\rangle\)~~ | — | **FALSE**: \(L(y,h)=(1+h^2)e^y\) is robust and not affine; and the proof was a non sequitur | §2.1′ | **RETRACTED (O-1, O-2)** | replaced, not patched |
| A-1.1′ | robustness **plus** \(L\ge0,\ L(h,h)=0\) over a class rich in *finitely supported* laws \(\Rightarrow\) strictly consistent for the conditional mean \(\Rightarrow\) Bregman | \(\mathcal H\subseteq\operatorname{int}\mathcal Y\) open convex; three-atom richness for the internal route | PROVED (consistency step internal; Bregman step CITED+APPLIED to LRV Prop 3 in the matrix case, or internal under three-atom richness) | §2.1′ | PROVED | two atoms are not enough in dimension \(\ge2\) — the corrected richness hypothesis is load-bearing |
| A-1.2 | the Bregman form and its regularity: \(H\in\operatorname{int}\mathcal Y\); convexity of \(\psi\) is needed on \(\operatorname{conv}\mathcal Y\) | as stated | PROVED | §2.2 | PROVED | — |
| A-1.3 | Bregman \(\Rightarrow\) robust, with an exactly \(h\)-free offset (not merely order-preserving) | \(\mathbb E\psi(\widehat\Sigma)<\infty\) | PROVED | §2.3 | PROVED | integrability of \(\psi(\widehat\Sigma)\) can fail for \(\psi=-\log\det\) at a singular proxy — see A-1.7 |
| A-1.4 | on a rich class, robust \(\iff\) Bregman \(\iff\) strictly consistent for the conditional mean | rich class (finitely supported laws) | PROVED — scalar via Gneiting Thm 3.1, **matrix via LRV Prop 3**, or internally under three-atom richness | §2.4 | PROVED | **Gneiting Thm 3.1 is scalar** (\(I\subseteq\mathbb R\)); it may not be used for the matrix case (O-5) |
| A-1.4b | on a restricted class the equivalence FAILS: an explicit non-Bregman loss is consistent for the mean on a one-parameter scale family | explicit construction | PROVED | §2.5 | PROVED | the restricted class is small; its scientific adequacy is judged in E1 |
| A-1.5 | Patton (2011) Definition 1 + Proposition 1: necessary and sufficient, **scalar only** | as stated by the author | CITED+APPLIED | §6 | CITED+APPLIED | verified verbatim from text; typeset equation reconstructed from prose |
| A-1.6 | Laurent–Rombouts–Violante (2013) Proposition 3 + Corollary 1: necessary and sufficient, **matrix case**, in \(\operatorname{vech}\) coordinates | as stated by the authors | CITED+APPLIED | §6 | CITED+APPLIED | the authors' positive-definiteness requirement is inherited, and it binds A-1.7 |
| A-1.7 | multivariate QLIKE: the **loss level** requires \(\widehat\Sigma\succ0\), but the **ranking** of two forecasts is well defined for a singular proxy | \(H_i\succ0\); proxy PSD | REFORMULATED+PROVED | §2.6 | REFORMULATED+PROVED | the loss differential is linear in \(\widehat\Sigma\), so Diebold–Mariano on the differential is fine; only the loss *level* and the \(\S1\) sign-of-difference definition need reformulating at a singular proxy |
| A-4.1 | a Bregman divergence is symmetric iff its generator has constant Hessian iff it is a squared Mahalanobis form | \(\psi\) differentiable convex on an open convex set | PROVED (and CITED) | §3.1 | PROVED | the final step needs continuity of convex \(\psi\) plus Fréchet's theorem, not the second-difference criterion originally given (O-9); an independent counterexample hunt in dimensions 1 and 2 found nothing |
| A-4.2 | \(d_g^2(x,y)=Q(x-y)\) for a fixed positive quadratic form \(Q\) iff \(g\) is a constant metric in the linear chart | \(\mathcal X\) open convex in \(V\) | PROVED | §3.2 | PROVED | needs geodesic convexity of \(\mathcal X\); stated for the SPD cone, which is convex |
| A-4.3 | **LO-4, sharp form.** A symmetric normalised loss is proxy-robust iff it is \(\tfrac12\langle y-h,\mathcal A(y-h)\rangle\) with \(\mathcal A\succeq0\). Hence \(d_g^2\) is robust iff \(g\) is flat **and** the proxy's unbiasedness coordinate is an affinely parametrised geodesic chart for \(g\) | rich proxy class; \(L\) defined and symmetric on \(\mathcal H\times\mathcal H\) | REFORMULATED+PROVED | §3.3 | REFORMULATED+PROVED | \(\mathcal A\succeq0\) not \(\succ0\) (O-3); symmetry typechecks only on \(\mathcal H\times\mathcal H\) (O-4); "affinely parametrised" not merely "affine chart" — the Klein model has straight geodesics and curvature \(-1\) |
| A-4.4 | log-Euclidean is **flat** and still **not** proxy-robust for a \(\Sigma\)-unbiased proxy — the witness separating flatness from robustness | — | PROVED (and independently CITED: LRV list "log-Frobenius" as non-robust) | §3.4 | PROVED | LRV's "log-Frobenius" and the log-Euclidean distance must be checked to be the same object; done in §3.4 |
| A-4.5 | Fisher–Rao contrast: for centred Gaussians the AIRM geodesic distance is not robust while the KL/Bregman divergence generated by \(-\log\det\) is | — | PROVED | §3.5 | PROVED | the constant relating AIRM to Fisher–Rao is convention-dependent and is not load-bearing |
| A-E1.1 | robustness up to a strictly increasing transformation of the loss buys nothing | \(g\) strictly increasing, non-affine | PROVED | §4.1 | PROVED | an affine \(g\) is trivially allowed and is not an escape |
| A-E1.2 | **local robustness.** BW ranking is correct **if** \(\eta\gg\varepsilon^2/\|\Sigma\|\); and it always misranks the conditional mean itself (\(\eta=0\)), by the exact witness B-2.4 | second-order regularity of \(G\); \(H\) in a compact subset of the cone bounded away from the boundary | PROVED (sufficiency + exact failure witness) | §4.2 | PROVED | the converse is **not** proved and is no longer claimed (O-7); \(\nabla\Gamma=O(\varepsilon^2)\) is now derived on compacts rather than asserted (O-8) |
| A-E1.3 | restricting the proxy class to laws with a known conditional second-moment tensor admits a **gap-corrected** loss; the correction is not a new robust loss but a feasible \(O(\varepsilon^3)\) repair | known/estimable 4th-moment tensor | PROVED | §4.3 | PROVED | it needs the proxy's fourth-moment structure, which is a model assumption, not data |
| A-E1 | **E1 terminal:** no weakening of the robustness notion admits a non-flat geodesic loss as *exactly* robust; two weakenings (local robustness; gap correction) are useful and are stated with their exact cost | — | REFORMULATED+PROVED | §4 | REFORMULATED+PROVED | — |
| A-E4.1 | \(\Gamma(cH)=\sqrt c\,\Gamma(H)\) **exactly** for the BW Jensen gap | \(H\succ0\), \(c>0\) | PROVED | §5.1 | PROVED | exact, uses only homogeneity of \(G\) |
| A-E4.2 | constancy of \(\Gamma\) on \(\mathcal H'\) is **sufficient** for exact ranking preservation, and necessary only on classes containing an indifference pair; and **no level set contains two distinct positive multiples of one forecast** (given \(\Gamma>0\)) | — | PROVED (sufficiency); necessity restricted | §5.2 | PROVED | the original "iff" was **overturned** by an explicit pair with non-constant \(\Gamma\) whose ranking is preserved (O-6) |
| A-E4.3 | exact cancellation on the orbit of a forecast under the joint symmetry group of the target and the proxy law | group action | PROVED | §5.3 | PROVED | such orbits essentially never contain two *models* being compared |
| A-E4.4 | the closed-form scale distortion: the proxy-optimal scale is \(\big(1-\Gamma(H_0)/2G(H_0,\Sigma)\big)^2\) times the true optimal scale | \(\Gamma(H_0)>0\) | PROVED | §5.4 | PROVED | strictness of "\(<1\)" needs \(\Gamma>0\), i.e. a nondegenerate proxy |
| A-E4 | **E4 terminal:** the distortion cancels on an explicitly characterised codimension-one family and on symmetry orbits, and on nothing richer; it contaminates level-differing comparisons maximally | — | REFORMULATED+PROVED | §5 | REFORMULATED+PROVED | — |

Every intermediate claim introduced in this dossier is listed in §7 with a terminal status.

## 1. Setting

\(V\) is a finite-dimensional real inner-product space; for the flagship case \(V=\mathrm{Sym}(m)\) with \(\langle A,B\rangle=\operatorname{tr}(AB)\). \(\mathcal Y\subseteq V\) is the proxy's support set and \(\mathcal H\subseteq V\) is an open convex forecast set; for covariance forecasting \(\mathcal H\) is the open SPD cone and \(\mathcal Y\) its closure.

The **target** is \(\Sigma=\mathbb E[\Sigma^\ast\mid\mathcal F]\). The **proxy** \(\widehat\Sigma\) is conditionally unbiased in the linear coordinate: \(\mathbb E[\widehat\Sigma\mid\mathcal F]=\Sigma\). A **loss** is \(L:\mathcal Y\times\mathcal H\to[0,\infty]\).

**Definition (proxy-robust).** \(L\) is proxy-robust over a proxy class \(\mathcal Q\) and forecast class \(\mathcal H\) if for every \(Q\in\mathcal Q\) with mean \(\Sigma\) and every \(H_1,H_2\in\mathcal H\),
\[
\operatorname{sign}\{\mathbb E_QL(\widehat\Sigma,H_1)-\mathbb E_QL(\widehat\Sigma,H_2)\}
=\operatorname{sign}\{L(\Sigma,H_1)-L(\Sigma,H_2)\}.
\]

**Definition (rich class).** \(\mathcal Q\) is *rich at \(\Sigma\)* if it contains every two-point law \(\lambda\delta_{y_1}+(1-\lambda)\delta_{y_2}\) supported in \(\mathcal Y\) with mean \(\Sigma\). Richness is exactly the hypothesis that carries the necessity half of LO-1, and it is exactly the hypothesis that E1 and E4 weaken.

## 2. LO-1 — the characterisation

### 2.1′ A-1.1′ — robustness plus normalisation forces Bregman

> **Retraction, recorded rather than quietly replaced.** The first version of this section asserted that robustness alone forces \(L\) to be affine in its first argument up to a forecast-free term, and proved it by moving \(H_2\) onto an indifference surface. The Wave-3 auditor showed both halves are wrong, and the objections are sustained in full ([[P1-LOSS — lead ledger]] O-1, O-2):
> - **the statement is false.** \(L(y,h)=(1+h^2)e^y\) is proxy-robust over *every* class, because \(\operatorname{sign}\{\mathbb E_Q L(\widehat\Sigma,h_1)-\mathbb E_QL(\widehat\Sigma,h_2)\}=\operatorname{sign}\{c(h_1)-c(h_2)\}\) whatever \(Q\) is, and it is not affine in \(y\). Richness cannot exclude it; only the normalisation \(L\ge0,\ L(h,h)=0\) can, and that normalisation was in the *next* lemma's hypotheses, not this one's;
> - **the proof was a non sequitur.** Replacing \(H_2\) by a forecast on an indifference surface replaces \(\Phi\) by a different function, so no contradiction with the original \(\Phi\)'s non-affinity was ever derived. Worse, mean-preserving two-point spreads *at a single mean* give only an odd-homogeneity condition, not affinity, once \(\dim V\ge2\): \(\rho(w)=w_1+w_2^3/(w_1^2+w_2^2)\) satisfies the two-atom identity and is not additive.
>
> The repair below does not restore the affinity route. It removes it. The correct argument never needs affinity, is three lines, and routes through a characterisation that is already in the literature for exactly this problem.

**Definition (richness, corrected).** \(\mathcal Q\) is *rich* if it contains every finitely supported law on \(\mathcal Y\) whose mean lies in \(\mathcal H\). Two atoms are **not** enough in dimension \(\ge2\); three are. Richness is required at every attainable mean, not at one.

**Theorem A-1.1′.** Let \(\mathcal H\subseteq\mathcal Y\) with \(\mathcal H\) open and convex, let \(L\ge0\) with \(L(H,H)=0\) for every \(H\in\mathcal H\), and let \(L\) be proxy-robust over a rich \(\mathcal Q\). Then \(L\) is strictly consistent for the conditional mean, and hence — by the Savage/Gneiting characterisation in dimension one and by Laurent–Rombouts–Violante Proposition 3 in the matrix case — \(L\) is a Bregman divergence \(B_\psi\) with \(\psi\) convex.

*Proof of the first implication (the part that is genuinely internal).* Fix a finitely supported \(Q\in\mathcal Q\) with mean \(\mu\in\mathcal H\), and any \(H\in\mathcal H\). Apply robustness to the pair \((H,\mu)\):
\[
\operatorname{sign}\{\mathbb E_QL(\widehat\Sigma,H)-\mathbb E_QL(\widehat\Sigma,\mu)\}
=\operatorname{sign}\{L(\mu,H)-L(\mu,\mu)\}=\operatorname{sign}\{L(\mu,H)\}\ \ge 0,
\]
using \(L(\mu,\mu)=0\) and \(L\ge0\). Hence \(\mathbb E_QL(\widehat\Sigma,H)\ge\mathbb E_QL(\widehat\Sigma,\mu)\) for every \(H\), with equality only when \(L(\mu,H)=0\). So \(\mu=\mathbb E_Q[\widehat\Sigma]\) minimises the expected loss: \(L\) is consistent for the mean, and strictly so as soon as \(L(\mu,H)=0\Rightarrow H=\mu\). ∎

*The second implication.* Consistency for the mean over all finitely supported laws characterises Bregman divergences. Two routes, and the campaign uses the second for the matrix case:
- **scalar:** Gneiting (2011), Theorem 3.1, attributed there to Savage — but note its domain is \(I\subseteq\mathbb R\), so it is **scalar only**, exactly like Patton. Dossier A originally used it for the matrix case; that was O-5 and is corrected here.
- **matrix:** Laurent–Rombouts–Violante (2013), Proposition 3, verified verbatim, is stated for matrix-valued forecasts in \(\operatorname{vech}\) coordinates and is necessary *and* sufficient. Their form \(L(\widehat\Sigma,H)=\tilde C(H)-\tilde C(\widehat\Sigma)+C(H)'\operatorname{vech}(\widehat\Sigma-H)\) is exactly \(B_\psi\) with \(\psi=-\tilde C\) and \(C=\nabla\tilde C\); \(\psi\) convex \(\iff\tilde C\) concave. Their hypotheses — \(C^2\) losses and positive definiteness — are inherited and recorded.

**Internal multivariate necessity, for readers who do not want to consume LRV.** Suppose \(L(y,\cdot)\) is differentiable and consistent for the mean over all finitely supported laws. The first-order condition at a \(k\)-atom law \(\sum_i\lambda_i\delta_{y_i}\) with mean \(\mu\) reads \(\sum_i\lambda_iV(y_i,\mu)=0\), where \(V(y,h)=\nabla_hL(y,h)\), and \(V(\mu,\mu)=0\). Writing \(f(z):=V(\mu+z,\mu)\), the constraint \(\sum_i\lambda_iz_i=0\) gives
\[
\sum_i\lambda_iz_i=0\ \Longrightarrow\ \sum_i\lambda_if(z_i)=0 .
\]
With two atoms this yields only \(f\) odd and \(f(ad)/a=f(bd)/b\) for \(a+b=1\) — the homogeneity the auditor's counterexample exploits. With **three** atoms it yields full Cauchy additivity of \(f\), and \(f\) continuous (from differentiability of \(L\)) then gives \(f(z)=\mathcal A_\mu z\) linear. So \(\nabla_hL(y,h)\big|_{h=\mu}=\mathcal A_\mu(y-\mu)\) for every \(\mu\); integrating in the second argument and imposing \(L(H,H)=0\) reproduces \(B_\psi\) with \(\nabla^2\psi=\mathcal A\). **This is where the corrected richness hypothesis earns its keep, and it is exactly the step the retracted proof skipped.** ∎

*Weak point, stated:* the internal route needs \(\nabla_hL\) to exist and be continuous; LRV need \(C^2\). Neither is weaker than the other and the campaign consumes whichever the application supplies.

### 2.2 A-1.2 — the Bregman form and its regularity

Given the representation above, \(L(y,H)=\psi(y)-\psi(H)-\langle\nabla\psi(H),y-H\rangle\). Two regularity points that the audit corrected:
- the first-order condition needs \(H\in\operatorname{int}\mathcal Y\), not merely \(\mathcal H\) open (O-2 companion finding). Since the campaign takes \(\mathcal H\) to be the open SPD cone and \(\mathcal Y\) its closure, \(\mathcal H\subseteq\operatorname{int}\mathcal Y\) and the condition holds; it is now stated rather than assumed;
- \(B_\psi\ge0\) \(\iff\) \(\psi\) convex holds on the set where the divergence is evaluated, which is \(\operatorname{conv}\mathcal Y\), not merely \(\mathcal H\). A-1.3 uses convexity on \(\operatorname{conv}\mathcal Y\), so that is the hypothesis carried.

Strict positivity off the diagonal \(\iff\) strict convexity. ∎

### 2.3 A-1.3 — Bregman is robust, exactly

\(B_\psi(y,H)\) is affine in \(y\) up to the \(H\)-free term \(\psi(y)\). Hence for any \(Q\) with mean \(\Sigma\) and \(\mathbb E_Q\psi(\widehat\Sigma)<\infty\),
\[
\mathbb E_QB_\psi(\widehat\Sigma,H)=B_\psi(\Sigma,H)+\underbrace{\{\mathbb E_Q\psi(\widehat\Sigma)-\psi(\Sigma)\}}_{\text{does not depend on }H}.
\tag{2.3}
\]
The offset is the Jensen gap of \(\psi\); it is nonnegative and **exactly** \(H\)-free. So the proxy shifts every expected loss by one common constant and preserves not only the ranking but all differences. This is stronger than sign preservation: Diebold–Mariano loss differentials are *unchanged*, not merely co-signed. ∎

### 2.4 A-1.4 — the equivalence on a rich class

Consistency for the mean means \(\Sigma\in\arg\min_H\mathbb E_QL(\widehat\Sigma,H)\) for all \(Q\in\mathcal Q\).
*(Bregman \(\Rightarrow\) consistent.)* By (2.3), \(\arg\min_H\mathbb E_QB_\psi=\arg\min_HB_\psi(\Sigma,H)=\{\Sigma\}\) when \(\psi\) is strictly convex.
*(Consistent \(\Rightarrow\) Bregman.)* This is Gneiting (2011), Theorem 3.1, attributed there to Savage, on the class of compactly supported measures — see §6. It is also obtainable internally from A-1.1–A-1.2 by noting that consistency over the rich class forces \(\nabla_H\mathbb E_QL(\widehat\Sigma,H)|_{H=\Sigma}=0\) for all \(Q\), hence \(\mathbb E_Q\nabla_HL(\widehat\Sigma,\Sigma)=0\) for all mean-\(\Sigma\) two-point laws, hence \(y\mapsto\nabla_HL(y,\Sigma)\) is affine and vanishes at \(y=\Sigma\); integrating in \(H\) reproduces the Bregman form.
*(Bregman \(\Rightarrow\) robust)* is A-1.3; *(robust \(\Rightarrow\) Bregman)* is A-1.1–A-1.2. Hence on a rich class all three are equivalent. ∎

### 2.5 A-1.4b — the equivalence FAILS on restricted classes

The equivalence is a property of the class, not of the loss. Take \(m=1\), \(\mathcal Q\) the one-parameter family \(\{Q_\Sigma\}\) where \(\widehat\Sigma=\Sigma\cdot\chi^2_M/M\) with \(M\) **fixed and known**, and take
\[
L^\ast(y,h):=\big(\sqrt y-\kappa_M\sqrt h\big)^2,\qquad \kappa_M:=\mathbb E\big[\sqrt{\chi^2_M/M}\big]=\sqrt{2/M}\,\Gamma\big(\tfrac{M+1}2\big)\big/\Gamma\big(\tfrac M2\big).
\]
\(L^\ast\) is **not** a Bregman divergence in \(y\): the cross term \(-2\kappa_M\sqrt y\sqrt h\) is not affine in \(y\). (It is also not a divergence at all — \(L^\ast(h,h)=h(1-\kappa_M)^2\ne0\) — so it is a scoring function, not a normalised loss, and A-1.1′ does not apply to it. That is precisely why it can be consistent without being robust.) Yet \(\partial_h\mathbb E L^\ast(\widehat\Sigma,h)=0\) at \(\sqrt h=\mathbb E\sqrt{\widehat\Sigma}/\kappa_M=\sqrt\Sigma\), so \(L^\ast\) is **strictly consistent for the conditional mean on this class**. It is not robust: enlarging \(\mathcal Q\) to two-point laws destroys consistency, because \(\kappa\) is law-dependent.

This is the exact content of E1 and E4: *consistency for the mean is cheap on a small class; robustness is expensive because it is a demand over all classes.* ∎

### 2.6 A-1.7 — QLIKE and a singular proxy

Multivariate QLIKE is \(B_\psi\) with \(\psi(A)=-\log\det A\):
\[
B_\psi(\widehat\Sigma,H)=-\log\det\widehat\Sigma+\log\det H+\langle H^{-1},\widehat\Sigma-H\rangle
=\operatorname{tr}(H^{-1}\widehat\Sigma)-\log\det(H^{-1}\widehat\Sigma)-m .
\]
The only place \(\widehat\Sigma\) enters nonlinearly is \(-\log\det\widehat\Sigma\), which is the \(H\)-free \(\psi(y)\) term of (2.3).

- **Loss level.** If \(\widehat\Sigma\) is singular, \(-\log\det\widehat\Sigma=+\infty\) and the loss is \(+\infty\) for every forecast.
- **Ranking.** The difference \(B_\psi(\widehat\Sigma,H_1)-B_\psi(\widehat\Sigma,H_2)=\operatorname{tr}((H_1^{-1}-H_2^{-1})\widehat\Sigma)+\log\det(H_1/H_2)\) is **finite and well defined for any PSD proxy**, singular or not, and is linear in \(\widehat\Sigma\); so the *ranking* is robust even at a singular proxy. Only the forecasts must be positive definite.
- **Caveat that must travel with this.** \(\mathbb E\psi(\widehat\Sigma)=+\infty\) means (2.3)'s offset is infinite: the loss *level* is uninformative and any procedure that needs \(\mathbb E L\) itself (rather than a differential) breaks. Diebold–Mariano on the differential is fine; average-QLIKE reporting is not.

**Terminal:** REFORMULATED+PROVED. The project's near-singular realised covariances do not disqualify QLIKE ranking; they disqualify QLIKE *levels*. ∎

## 3. LO-4 — the no-go, sharpened

### 3.1 A-4.1 — symmetric Bregman \(\Rightarrow\) quadratic generator

**Statement.** Let \(\psi\) be differentiable and convex on an open convex \(\mathcal D\subseteq V\). Then \(B_\psi(x,y)=B_\psi(y,x)\) for all \(x,y\in\mathcal D\) iff \(\psi\) is a quadratic polynomial, and then \(B_\psi(x,y)=\tfrac12\langle x-y,\mathcal A(x-y)\rangle\) for the constant positive semidefinite \(\mathcal A=\nabla^2\psi\).

**Proof (low regularity; no \(C^3\) assumed).** Symmetry is
\[
2\{\psi(x)-\psi(y)\}=\langle\nabla\psi(x)+\nabla\psi(y),\,x-y\rangle,
\tag{3.1}
\]
i.e. the trapezoidal rule is exact on every segment. Fix \(x,y\), put \(v=x-y\), and let \(\varphi(t)=\psi(y+tv)\) on \([0,1]\). \(\psi\) differentiable convex on an open set implies \(\nabla\psi\) is continuous there, so \(\varphi\in C^1\). Applying (3.1) to the pair \((y+tv,\,y)\) gives
\[
\varphi(t)-\varphi(0)=\tfrac t2\{\varphi'(0)+\varphi'(t)\},\qquad t\in[0,1].
\tag{3.2}
\]
For \(t>0\), \(\varphi'(t)=\tfrac2t\{\varphi(t)-\varphi(0)\}-\varphi'(0)\). The right-hand side is differentiable in \(t\) on \((0,1]\) because \(\varphi\in C^1\); hence \(\varphi\in C^2((0,1])\). Differentiating (3.2),
\[
\varphi'(t)=\tfrac12\{\varphi'(0)+\varphi'(t)\}+\tfrac t2\varphi''(t)
\;\Longrightarrow\;
u(t)=t\,u'(t),\qquad u(t):=\varphi'(t)-\varphi'(0).
\]
So \((u(t)/t)'=0\) on \((0,1]\), giving \(u(t)=ct\), i.e. \(\varphi'(t)=\varphi'(0)+ct\) and \(\varphi\) is a quadratic polynomial in \(t\). Thus \(\psi\) is quadratic along **every** line segment in \(\mathcal D\). A function quadratic along every line on an open set is a quadratic polynomial. The second-difference criterion originally given here is **not sufficient** — \(\psi(x,y)=A(x)y\) with \(A\) an additive non-linear (Hamel) function is quadratic on every line with a \(z\)-independent second difference, and is not a polynomial (O-9). The correct step uses regularity, which convexity supplies for free: quadratic along every line gives the third difference \(\Delta_v^3\psi\equiv0\) for every \(v\), and a convex \(\psi\) is continuous on the interior of its domain, so Fréchet's theorem on the functional equation \(\Delta_v^3\psi\equiv0\) with continuity forces \(\psi\) to be a polynomial of degree \(\le2\), i.e. \(\psi(z)=\tfrac12\langle z,\mathcal Az\rangle+\langle c,z\rangle+d\). Substituting gives \(B_\psi(x,y)=\tfrac12\langle x-y,\mathcal A(x-y)\rangle\). The converse is immediate. ∎

**External corroboration.** Boissonnat, Nielsen and Nock, "Bregman Voronoi diagrams", arXiv:0709.2196, **Lemma 2**: *"\(D_F\) is symmetric if and only if the Hessian \(\nabla^2F\) is constant on \(\mathcal X\)."* This is the same statement under a \(C^2\) hypothesis; the proof above removes the \(C^2\) hypothesis and adds the Mahalanobis restatement. Status: **PROVED INTERNALLY, with the \(C^2\) version CITED EXTERNALLY**.

### 3.2 A-4.2 — a squared geodesic distance is a quadratic form iff the metric is constant

Let \(\mathcal X\subseteq V\) be open and convex and \(g\) a Riemannian metric on \(\mathcal X\).

*(⇐)* If \(g_x=\mathcal A\) for all \(x\), straight segments are geodesics (Christoffel symbols vanish) and stay in \(\mathcal X\) by convexity; they are minimising, so \(d_g^2(x,y)=\langle x-y,\mathcal A(x-y)\rangle\).

*(⇒)* If \(d_g^2(x,y)=Q(x-y)\) for a fixed positive quadratic form \(Q\), then for any \(x\in\mathcal X\) and \(v\in V\),
\(g_x(v,v)=\lim_{t\to0}t^{-2}d_g^2(x,x+tv)=\lim_{t\to0}t^{-2}Q(tv)=Q(v)\),
using that the Riemannian distance to a nearby point is asymptotically the norm of the displacement. So \(g\equiv Q\) is constant. ∎

*(Cut locus.)* No cut-locus caveat is needed: the hypothesis is that \(d_g^2\) *equals* a quadratic form globally on \(\mathcal X\times\mathcal X\), and the conclusion is drawn from the infinitesimal limit only.

### 3.3 A-4.3 — LO-4 in its sharp form

**Theorem (LO-4).** Let the proxy be conditionally unbiased in the linear coordinate of \(V\) and let \(\mathcal Q\) be rich. Let \(L\) be any **symmetric** loss, \(L(y,h)=L(h,y)\), with \(L\ge0\) and \(L(h,h)=0\), differentiable in its first argument. Then
\[
L\ \text{is proxy-robust}\iff L(y,h)=\tfrac12\langle y-h,\mathcal A(y-h)\rangle
\ \text{for a fixed}\ \mathcal A\succeq0 ,
\]
In particular, for \(L=d_g^2\) the geodesic distance squared of a metric \(g\) on an open convex \(\mathcal X\subseteq V\):
\[
d_g^2\ \text{is proxy-robust}\iff g\ \text{is a constant metric in the linear coordinate of }V,
\]
equivalently iff \((\mathcal X,g)\) is **flat and the proxy's unbiasedness coordinate is an affinely parametrised geodesic chart** for \(g\).

Three hypotheses that the Wave-3 audit forced into the open and that must travel with the statement:
1. \(\mathcal A\succeq0\), not \(\succ0\): a degenerate quadratic form is robust (it is Bregman with a degenerate generator). \(\mathcal A\succ0\) is what strict consistency needs, and it is the case the project wants, but it is not what robustness alone gives (O-3).
2. Symmetry is a statement on \(\mathcal H\times\mathcal H\). On \(\mathcal Y\times\mathcal H\) with \(\mathcal Y\ne\mathcal H\), \(L(h,y)\) need not be defined and "symmetric" does not typecheck; the theorem is stated on the open cone and extended to the boundary only where \(L(\cdot,h)\) is continuous (O-4).
3. "Affinely parametrised" is not "affine chart". A chart in which geodesics are straight lines but are not affinely parametrised — the Klein model of hyperbolic space is the standard example, with curvature \(-1\) — does not make \(d_g^2\) a quadratic form.

*Proof.* A-1.1′ gives Bregman; A-4.1 turns symmetry into a quadratic generator; A-4.2 converts that into constancy of the metric. ∎

**Consequences, stated as the campaign's headline.**
1. **Curvature kills it.** Any metric with nonzero curvature anywhere is excluded: AIRM (Hadamard, strictly negative curvature), Bures–Wasserstein (nonnegatively curved, strictly positive in noncommuting directions), spherical and product-spherical geometries. This covers every geometry the project uses and every future one.
2. **Flatness alone is NOT sufficient.** This is where the informal headline was imprecise. Flatness is necessary; the extra requirement is that the linear coordinate in which the proxy is unbiased must itself be an affine chart of the flat structure. Log-Euclidean is the witness (§3.4).
3. **The robust symmetric class is exactly one object up to the choice of \(\mathcal A\):** the Mahalanobis family on the proxy's own linear coordinate. On \(\mathrm{Sym}(m)\) with \(\mathcal A=\mathrm{Id}\) this is the squared Frobenius distance.
4. **Geodesic losses are a corollary, not the theorem.** The theorem is about symmetry, so it also excludes symmetrised divergences (Jeffreys/Jensen–Shannon-type symmetrisations, symmetrised Stein loss) at one stroke.

### 3.4 A-4.4 — log-Euclidean: flat and still not robust

The map \(\Lambda:\Sigma\mapsto\log\Sigma\) is a diffeomorphism of the SPD cone onto \(\mathrm{Sym}(m)\). The log-Euclidean metric is \(\Lambda^\ast(\text{Euclidean})\); it is therefore **flat** — zero curvature, geodesics \(\Lambda^{-1}\) of straight lines, and
\(d_{\rm LE}(A,B)^2=\|\log A-\log B\|_F^2\).

Is it robust for a \(\Sigma\)-unbiased proxy? By A-4.3 it would have to be a quadratic form in \(A-B\). It is not: \(d_{\rm LE}^2(A,B)=\|\log A-\log B\|_F^2\) is not a function of \(A-B\) at all (take \(A=2I,B=I\) versus \(A=3I,B=2I\): the differences are both \(I\), the log-Euclidean distances are \((\log2)\sqrt m\) and \((\log\tfrac32)\sqrt m\)). Hence **not proxy-robust**, despite flatness.

The mechanism is exactly the one A-4.3 names: log-Euclidean *is* a squared Mahalanobis distance — in the coordinate \(\Lambda=\log\Sigma\) — and the proxy is not conditionally unbiased in that coordinate. Robustness is a statement about a **pair** (loss, proxy coordinate), never about the loss alone.

**Independent external corroboration.** Laurent, Rombouts and Violante (2013) list "log-Frobenius" among their **non-robust** losses. Their log-Frobenius loss is \(\|\log\widehat\Sigma-\log H\|\)-based, i.e. the log-Euclidean distance; so a published necessary-and-sufficient matrix characterisation independently classifies this exact loss as non-robust. Status: **PROVED INTERNALLY AND CORROBORATED EXTERNALLY.**

### 3.5 A-4.5 — the Fisher–Rao contrast

For centred Gaussians \(N(0,\Sigma)\) the Fisher information metric is \(g(V,W)=\tfrac12\operatorname{tr}(\Sigma^{-1}V\Sigma^{-1}W)\), i.e. \(\tfrac12\times\) the AIRM metric; the Fisher–Rao geodesic distance is proportional to \(\|\log(\Sigma^{-1/2}H\Sigma^{-1/2})\|_F\). The **Bregman divergence** generated by \(\psi=-\log\det\) on the same cone is \(2\,\mathrm{KL}(N(0,\Sigma)\,\|\,N(0,H))=\operatorname{tr}(H^{-1}\Sigma)-\log\det(H^{-1}\Sigma)-m\), i.e. multivariate QLIKE.

So the *same* information geometry supplies both a distance and a divergence, and exactly one of them is admissible for forecast evaluation:

| Object | Symmetric? | Bregman in \(\Sigma\)? | Proxy-robust? |
|---|---|---|---|
| Fisher–Rao / AIRM geodesic distance squared | yes | no | **no** |
| KL divergence \(=\tfrac12\) multivariate QLIKE | no | yes (\(\psi=-\log\det\)) | **yes** |

The asymmetry of the divergence is not a defect to be repaired by symmetrising; by A-4.3 **it is the property that makes it usable**. Symmetrising it destroys robustness.

## 4. E1 — weakening the robustness notion

### 4.1 A-E1.1 — monotone transformations of the loss buy nothing

Suppose \(\tilde L=g\circ L\) with \(g\) strictly increasing. Robustness of \(\tilde L\) is a statement about \(\mathbb E g(L(\widehat\Sigma,H))\), and \(g\) does not commute with \(\mathbb E\). Running A-1.1 on \(\tilde L\) forces \(\tilde L\) itself into the form (2.2), i.e. \(g\circ L=B_{\tilde\psi}\); if \(L\) is symmetric so is \(g\circ L\), and A-4.1 applies to \(\tilde L\). Hence \(g\circ L\) must be a squared Mahalanobis form, and \(L=g^{-1}(\text{quadratic})\) is a *reparameterised* quadratic, whose ranking is identical to the quadratic's. So the class of *rankings* is unchanged. **Terminal: DISPROVED as an escape.** (The trivial case \(g\) affine is allowed and changes nothing.)

### 4.2 A-E1.2 — local robustness: exactly where BW ranks correctly

Write \(G(H,A)=\operatorname{tr}(H^{1/2}AH^{1/2})^{1/2}\), so \(d_{\rm BW}^2(A,H)=\operatorname{tr}A+\operatorname{tr}H-2G(H,A)\). Define the **Jensen gap**
\[
\Gamma(H):=\mathbb E\,d_{\rm BW}^2(\widehat\Sigma,H)-d_{\rm BW}^2(\Sigma,H)=2\{G(H,\Sigma)-\mathbb E\,G(H,\widehat\Sigma)\}\ \ge 0,
\]
nonnegative because \(A\mapsto G(H,A)\) is concave (B-2.1). Note \(\operatorname{tr}\widehat\Sigma\) contributes nothing to \(\Gamma\), because it is forecast-free — the *entire* distortion sits in the \(G\) cross-term.

Let \(\varepsilon^2\) denote the scale of the proxy's conditional second moment, \(\mathbb E\|\Delta\|^2\asymp\varepsilon^2\). Then \(\Gamma(H)=O(\varepsilon^2)\); and differentiating the exact expression \(\Gamma(H)=2\{G(H,\Sigma)-\mathbb EG(H,\widehat\Sigma)\}\) in \(H\) gives \(\nabla_H\Gamma=O(\varepsilon^2)\) uniformly on any compact subset of the cone bounded away from the boundary, because \(G\) is smooth there and the \(\varepsilon^2\) enters only through \(\mathbb E[\Delta\otimes\Delta]\). Uniformity fails as \(\lambda_{\min}(H)\to0\); that restriction has a boundary reason and is not a convenience (O-8). For two forecasts with \(\|H_i-\Sigma\|\asymp\eta\) and \(\|H_1-H_2\|=\delta\):
\[
\underbrace{|d_{\rm BW}^2(\Sigma,H_1)-d_{\rm BW}^2(\Sigma,H_2)|}_{\asymp\ \eta\delta\ \text{generically}}
\quad\text{versus}\quad
\underbrace{|\Gamma(H_1)-\Gamma(H_2)|}_{=\ O(\varepsilon^2\delta)} .
\]
Hence the proxy ranking agrees with the true ranking whenever \(\eta\gg\varepsilon^2/\|\Sigma\|\) (the ratio must be dimensionless; the bare \(\eta\gg\varepsilon^2\) of the first draft was not). **Only this sufficient direction is proved.** That reversal *must* occur below the threshold is not proved and is not claimed (O-7); what is proved is the single exact witness at \(\eta=0\), B-2.4, and that witness is the one that matters.

Two consequences must be stated together, because reporting only the first would be misleading:
1. **Positive.** Comparisons between genuinely different forecasting models, whose distances from the conditional mean exceed the distortion magnitude, are ranked correctly by BW loss. In realistic covariance forecasting \(\eta\) is large, so most model comparisons survive.
2. **Negative, and it is the one that matters.** The failure region is exactly the near-optimal region. At \(\eta=0\) — the true conditional mean itself — the ranking is *always* wrong: the conditional mean is strictly beaten by its own shrunk version (B-2.4 exhibits this in closed form). A loss that systematically penalises the correct answer is not repaired by being right about bad answers.

*Exceptional set, stated:* the "generically \(\asymp\eta\delta\)" step fails when \(H_1-H_2\) is tangent to the level set of \(d_{\rm BW}^2(\Sigma,\cdot)\) through \(H_1\); on that set the true difference is \(O(\delta^2)\) and the distortion dominates for \(\delta\lesssim\varepsilon^2\). This enlarges the failure region; it does not shrink it.

**Terminal: REFORMULATED+PROVED.** Local robustness holds, on an explicitly characterised class, and it does not rescue the near-optimal comparison.

### 4.3 A-E1.3 — restricting the proxy class: the gap-corrected loss

If the proxy's conditional second-moment tensor \(C_{ab,cd}=\operatorname{Cov}(\widehat\Sigma_{ab},\widehat\Sigma_{cd}\mid\mathcal F)\) is known or modelled (for realised covariance, the Gaussian/Wishart form with known \(M\)), then \(\Gamma(H)\) is computable to \(O(\varepsilon^2)\) from \(H\), \(\Sigma\) and \(C\); replacing \(\Sigma\) by \(\widehat\Sigma\) in that computation costs \(O(\varepsilon^3)\). Define
\[
L^\ast(\widehat\Sigma,H):=d_{\rm BW}^2(\widehat\Sigma,H)-\widehat\Gamma(H),\qquad
\widehat\Gamma(H)=\text{the }O(\varepsilon^2)\text{ gap evaluated at }\widehat\Sigma .
\]
Then \(\mathbb E L^\ast(\widehat\Sigma,H)=d_{\rm BW}^2(\Sigma,H)+O(\varepsilon^3)\), so the ranking distortion drops from \(O(\varepsilon^2)\) to \(O(\varepsilon^3)\).

**What this is and is not.** It is a genuine, feasible, order-improving repair. It is **not** a robust loss: \(L^\ast\) is not proxy-robust for any nondegenerate class (it is not Bregman; A-1.1′ forbids it — the correct citation, since A-4.3 is the *symmetry* theorem), and its validity is conditional on the proxy's fourth-moment model. Calling it "robust" would be exactly the kind of relabelling this campaign exists to prevent. **Terminal: PROVED, with its cost stated.**

### 4.4 E1 terminal verdict

No weakening of the robustness notion admits a non-flat geodesic loss as exactly robust. Two weakenings are scientifically useful and are stated with their exact price: *local robustness* (correct above the distortion scale, always wrong at the optimum) and *gap correction* (one order better, at the cost of a fourth-moment model). **E1: REFORMULATED+PROVED.**

## 5. E4 — restricting the forecast class

### 5.1 A-E4.1 — the exact scaling law of the Jensen gap

\(G(cH,A)=\operatorname{tr}((cH)^{1/2}A(cH)^{1/2})^{1/2}=\operatorname{tr}(c\,H^{1/2}AH^{1/2})^{1/2}=\sqrt c\,G(H,A)\), exactly, for every \(c>0\). Hence
\[
\boxed{\ \Gamma(cH)=\sqrt c\ \Gamma(H)\quad\text{exactly.}\ }
\]
(Verified numerically to 12 digits at \(c=1/4,4,9\).) The gap is a positively homogeneous function of degree \(\tfrac12\) in the forecast — **strictly increasing along every scalar ray**.

### 5.2 A-E4.2 — the exact E4 class

The proxy-expected loss is \(\mathbb E d_{\rm BW}^2(\widehat\Sigma,H)=d_{\rm BW}^2(\Sigma,H)+\Gamma(H)\). Therefore:

**Theorem (E4).** If \(\Gamma\) is constant on \(\mathcal H'\subseteq\mathcal H\) then the BW ranking is preserved exactly on \(\mathcal H'\). The converse holds only on classes containing an indifference pair: the auditor exhibited \(\mathcal H'=\{\operatorname{diag}(3.05,2.02,1.01),\operatorname{diag}(4,2.6,1.4)\}\) with \(\Gamma=0.0996\) versus \(0.1140\) — not constant — yet the true and proxy loss differences \(-0.1444\) and \(-0.1588\) have the same sign, so the ranking survives (O-6). Constancy of \(\Gamma\) is therefore **sufficient, and necessary only for classes rich enough to contain a tie**. \(\Gamma\) is explicitly computable from \(H\), \(\Sigma\), and the proxy's conditional second-moment tensor. Consequently:
- the admissible classes are precisely the subsets of level sets \(\{\Gamma=\gamma\}\), a codimension-one family — large (dimension \(m(m+1)/2-1\)) but not described by any structural condition on the forecasts;
- by A-E4.1, **no level set contains two distinct positive multiples of the same forecast**. So the natural "same shape, different level" comparison — precisely the comparison an EWMA-versus-factor-model horse race is — is never admissible;
- the "common trace" class \(\{\operatorname{tr}H=\tau\}\) is **not** admissible: \(\Gamma\) is not a function of \(\operatorname{tr}H\) (it depends on the spectrum of \(H^{1/2}\Sigma H^{1/2}\));
- the "common spectrum, different eigenvectors" class is **not** admissible either, since \(\Gamma\) depends on \(H\) through \(H^{1/2}\Sigma H^{1/2}\), which is not conjugation-invariant unless \(\Sigma\) is.

**This is the honest E4 answer: the positive result exists and is exact, and it is not rich enough to contain a real model comparison.** The one direction that *is* rich is the bad one — level-differing comparisons — because by B-3.5 the distortion is (for a Wishart-type proxy) exactly a spectral shrink, so it is maximally aligned with the very direction it must adjudicate.

### 5.3 A-E4.3 — exact cancellation on symmetry orbits

Let \(U\) be orthogonal with \(U\Sigma U^\top=\Sigma\) and let the conditional law of \(\Delta\) be invariant under \(\Delta\mapsto U\Delta U^\top\). Then \(G(UHU^\top,U\widehat\Sigma U^\top)=G(H,\widehat\Sigma)\) and hence \(\Gamma(UHU^\top)=\Gamma(H)\). So the ranking is exactly preserved on the orbit \(\{UHU^\top\}\). This is a genuine exact-cancellation class; it is not a class in which two competing models ever sit. **PROVED, and recorded as scientifically empty.**

### 5.4 A-E4.4 — the closed-form scale distortion

On the ray \(H=cH_0\), \(\mathbb E d_{\rm BW}^2(\widehat\Sigma,cH_0)=\operatorname{tr}\Sigma+c\operatorname{tr}H_0-2\sqrt c\,\mathbb E G(H_0,\widehat\Sigma)\), minimised at \(\sqrt{c^\ast}=\mathbb E G(H_0,\widehat\Sigma)/\operatorname{tr}H_0\), while the true optimum is \(\sqrt{c_0}=G(H_0,\Sigma)/\operatorname{tr}H_0\). Therefore
\[
\frac{c^\ast}{c_0}=\left(\frac{\mathbb E G(H_0,\widehat\Sigma)}{G(H_0,\Sigma)}\right)^2
=\left(1-\frac{\Gamma(H_0)}{2\,G(H_0,\Sigma)}\right)^{2}<1 .
\]
Exact, no expansion. The BW loss rewards a strictly shrunken level, by a factor it computes for you. ∎

### 5.5 E4 terminal verdict

**REFORMULATED+PROVED.** The distortion cancels exactly on level sets of an explicitly computable functional \(\Gamma\) and on symmetry orbits, and on nothing richer; \(\Gamma\) is strictly increasing along scalar rays, so level-differing comparisons — the common case — are never protected and are in fact the worst case.

## 6. External sources consulted

Detail and verbatim quotations are in [[P1-LOSS — external source verification]]. Summary of what this dossier consumes:

| Source | What is consumed | Verified? |
|---|---|---|
| Patton (2011), *J. Econometrics* 160(1), 246–256, **Definition 1 + Proposition 1** | necessary-and-sufficient robust-loss characterisation, **scalar volatility only**; generator conditions "\(B\) and \(C\) twice continuously differentiable, \(C\) strictly decreasing, \(\tilde C\) the antiderivative of \(C\)" | full text, verbatim |
| Laurent, Rombouts, Violante (2013), *J. Econometrics* 173(1), 1–10, **Proposition 3 + Corollary 1** | necessary-and-sufficient **matrix** characterisation \(L(\widehat\Sigma_t,H_t)=\tilde C(H_t)-\tilde C(\widehat\Sigma_t)+C(H_t)'\operatorname{vech}(\widehat\Sigma_t-H_t)\); robust: Frobenius, Stein, Euclidean, weighted Euclidean; **not robust: entrywise 1-norm, proportional Frobenius, log-Frobenius, correlation distance**; positive-definiteness required | full text, verbatim |
| Gneiting (2011), *JASA* 106(494), 746–762, **Theorem 3.1** (attributed there to Savage) | consistency for the mean \(\iff\) Bregman, over compactly supported measures | full text, verbatim (arXiv version) |
| Savage (1971), *JASA* 66(336), 783–801 | **NOT OBTAINED.** Cited only as Gneiting's attribution; no theorem number is asserted | NOT verified — recorded as such |
| Boissonnat, Nielsen, Nock, arXiv:0709.2196, **Lemma 2** | "\(D_F\) is symmetric if and only if the Hessian \(\nabla^2F\) is constant" | full text, verbatim |

Two scope facts matter for this project and are recorded rather than glossed:
- Patton is **scalar only**; the project's matrix case rests on LRV plus the internal proof in §2.
- LRV's characterisation is in \(\operatorname{vech}\) coordinates with a positive-definiteness requirement; the internal proof in §2 is coordinate-free on \(\mathrm{Sym}(m)\) and does not need PD except where the generator does.

## 7. Intermediate-claim register (transitive closure input)

| Node | Terminal status |
|---|---|
| A-1.1 affinity from richness | **RETRACTED — DISPROVED** (O-1, O-2); no consumer survives it |
| A-1.1′ robust + normalised ⟹ consistent ⟹ Bregman | PROVED (matrix Bregman step CITED+APPLIED to LRV Prop 3) |
| A-1.2 Bregman form and regularity | PROVED |
| A-1.3 Bregman ⟹ exactly \(h\)-free offset | PROVED |
| A-1.4 three-way equivalence on a rich class | PROVED (Gneiting Thm 3.1 CITED+APPLIED for one direction; also proved internally) |
| A-1.4b equivalence fails on restricted classes | PROVED by explicit construction |
| A-1.5 Patton verification | CITED+APPLIED |
| A-1.6 LRV verification | CITED+APPLIED |
| A-1.7 QLIKE / singular proxy | REFORMULATED+PROVED |
| A-4.1 symmetric Bregman ⟹ quadratic | PROVED INTERNALLY (final step repaired via Fréchet's theorem, O-9); \(C^2\) form CITED+APPLIED |
| A-4.2 quadratic \(d_g^2\) ⟹ constant metric | PROVED |
| A-4.3 LO-4 sharp form | REFORMULATED+PROVED |
| A-4.4 log-Euclidean witness | PROVED; corroborated by LRV |
| A-4.5 Fisher–Rao vs KL contrast | PROVED |
| A-E1.1 monotone transform | DISPROVED as an escape |
| A-E1.2 local robustness | PROVED as a sufficient condition plus an exact failure witness; the converse is not claimed (O-7) |
| A-E1.3 gap-corrected loss | PROVED, with cost stated |
| A-E4.1 \(\Gamma(cH)=\sqrt c\Gamma(H)\) | PROVED |
| A-E4.2 E4 class | PROVED as sufficiency; the original "iff" DISPROVED (O-6) |
| A-E4.3 symmetry-orbit cancellation | PROVED (scientifically empty) |
| A-E4.4 closed-form scale distortion | PROVED |
| Savage (1971) primary text | OUT OF SCOPE BY PROVED SEPARATION — no claim in this dossier consumes it; Gneiting Thm 3.1 is the producer and is verified |

No node in this dossier is left non-terminal. One node — the original A-1.1 — terminates as **DISPROVED**, and its consumer (A-4.3) is repaired by A-1.1′ rather than by weakening the consumer.

## 8. Wave-3 repair record

Every objection raised by the non-author auditor is adjudicated in [[P1-LOSS — lead ledger]] §5 (O-1 … O-21) and the repairs are applied in place above. Two were FATAL, both against the *proof* of the characterisation and neither against the headline; the headline A-4.3 stands with three hypotheses made explicit. The auditor's own counterexample hunt against A-4.1, in dimensions one and two, found nothing.
