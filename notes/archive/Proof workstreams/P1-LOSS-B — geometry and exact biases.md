---
type: working-proof-dossier
title: P1-LOSS-B — geometry and exact biases
status: active-campaign
last-audited: 2026-08-14
authorship: authored by the campaign lead after the Wave-1 agent interruption (see [[P1-LOSS — lead ledger]] §1). The lead is therefore NOT an admissible non-author auditor of this dossier.
---

# P1-LOSS-B — geometry and exact biases

Owns LO-2, LO-3, LO-5, and route E5.

## 0. Claim table

| ID | Exact statement | Assumptions | Conclusion | Proof | Status | Known weak point |
|---|---|---|---|---|---|---|
| B-2.1 | \(A\mapsto\operatorname{tr}(H^{1/2}AH^{1/2})^{1/2}\) is concave; hence \(A\mapsto d_{\rm BW}^2(A,H)\) is **strictly convex**, not affine, in the realisation | \(H\succ0\), \(A\succeq0\) | PROVED | §2.1 | PROVED | strictness fails on the commuting scalar ray only in the trivial \(m=1\) degenerate sense; checked |
| B-2.2 | \(\arg\min_H\mathbb E d_{\rm BW}^2(\widehat\Sigma,H)\) is the BW Fréchet barycentre, characterised by \(\mathbb E[T_{H\to\widehat\Sigma}]=I\), equivalently \(\mathbb E[(H^{1/2}\widehat\Sigma H^{1/2})^{1/2}]=H\) | law charges the open cone; \(\mathbb E\operatorname{tr}\widehat\Sigma<\infty\) | PROVED | §2.2 | PROVED | existence/uniqueness imported from P1-ID §14.2, which proves it for arbitrary \(Q\) |
| B-2.3 | **LO-2:** squared BW distance is **not** proxy-robust | rich proxy class | DISPROVED (as a robust loss) | §2.3 | DISPROVED | — |
| B-2.4 | exact closed-form ranking reversal: a two-point conditionally unbiased proxy under which the true conditional mean is strictly beaten by a shrunken forecast, for every \(a\in(0,1)\) | \(m=1\); lifts to \(m\ge2\) on the scalar ray | PROVED | §2.4 | PROVED | \(a<1\) keeps the proxy on the **open** cone, as B-2.2 requires; \(a\le1\) bounds only this parameterisation — the phenomenon itself extends to \(a\in(0,2)\) with margin \((2-a)^2/4\) (O-18) |
| B-3.1 | **scalar exact bias** \(H^\star=(\mathbb E\sqrt x)^2=\mathbb E[x]-\operatorname{Var}(\sqrt x)\) | \(x>0\), \(\mathbb E x<\infty\) | PROVED (exact, not asymptotic) | §3.1 | PROVED | — |
| B-3.2 | **matrix second-order bias**, Sylvester form: \(H^\star=\Sigma-\Sigma^{-1/2}\mathbb E[G^2]\Sigma^{-1/2}+O(\varepsilon^3)\), \(\Sigma G+G\Sigma=\Sigma^{1/2}\Delta\Sigma^{1/2}\) | \(\mathbb E\Delta=0\), \(\|\Delta\|=O(\varepsilon)\) | PROVED (formula); the remainder bound is verified, not derived | §3.2 | PROVED | \(B=O(\varepsilon^2)\) is posited rather than established a priori, and no explicit remainder bound is given; the \(O(\varepsilon^3)\) scaling is confirmed independently (ratio \(\to8.00\) under \(\varepsilon\)-halving) but that is verification, not proof |
| B-3.3 | eigenbasis form: \(B_{ij}=-\sum_k\lambda_k\,\mathbb E[\Delta_{ik}\Delta_{kj}]\big/\{(\lambda_i+\lambda_k)(\lambda_k+\lambda_j)\}\) | as above; **\(\lambda_i\ne\lambda_j\) for the rotation-angle reading** | PROVED | §3.3 | PROVED | the rotation criterion and the angle \(B_{ij}/(\lambda_i-\lambda_j)\) both break at degenerate eigenvalues, where \(\Sigma\)'s eigenvectors are not unique — and near-degeneracy is exactly where second-order rotation is largest (O-17) |
| B-3.4 | commuting / fixed-eigenbasis case: the bias is **exactly** eigenvalue-wise, \(h^\star_i=(\mathbb E\sqrt{\lambda_i})^2\), with **zero** eigenvector rotation, exactly and not merely to second order | all \(\widehat\Sigma\) share \(\Sigma\)'s eigenvectors | PROVED | §3.4 | PROVED | requires an exactly shared eigenbasis, which realised covariance never has |
| B-3.5 | **Wishart / Gaussian fourth-moment proxy: the second-order bias is exactly diagonal in \(\Sigma\)'s eigenbasis** — no eigenvector rotation — with closed form \(B_{ii}=-\frac{\lambda_i}{M}\big[\frac14+\sum_k\frac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\big]\) | \(\operatorname{Cov}(\widehat\Sigma_{ab},\widehat\Sigma_{cd})=\frac1M(\Sigma_{ac}\Sigma_{bd}+\Sigma_{ad}\Sigma_{bc})\) | PROVED | §3.5 | PROVED | it is a property of the **noise model**, not the geometry. Stronger than first written: for a genuine Wishart the rotation is **exactly zero at every order**, by sign-flip equivariance (O-15); under the second-moment condition alone only the second-order statement holds |
| B-3.6 | **the "purely spectral" claim is FALSE in general**: an explicit conditionally unbiased two-point proxy gives nonzero off-diagonal second-order bias and a genuinely rotated eigenbasis | explicit construction | DISPROVED (as a general claim) | §3.6 | DISPROVED | — |
| B-3.7 | AIRM induced bias: \(B_{ij}=-\tfrac12\sum_k\mathbb E[\Delta_{ik}\Delta_{kj}]/\lambda_k\); Wishart closed form \(B_{ii}=-\lambda_i(m+1)/(2M)\) | as B-3.2 | PROVED | §3.7 | PROVED | — |
| B-3.8 | log-Euclidean induced target is **exactly** \(H^\star=\exp\mathbb E[\log\widehat\Sigma]\); second-order bias \(B_{ij}=\big(\sum_k\mathbb E[\Delta_{ik}\Delta_{kj}]\,\ell[\lambda_i,\lambda_k,\lambda_j]\big)/\ell[\lambda_i,\lambda_j]\) with \(\ell=\log\) divided differences | as B-3.2 | PROVED | §3.8 | PROVED | in the commuting case it coincides with AIRM; in the noncommuting case it does not, and the difference was verified numerically |
| B-5.1 | **infill rate:** the distortion equals the proxy conditional variance passed through a fixed linear operator, hence is \(\Theta(M^{-1})\), and it is **not uniform** over the forecast class — it is degree-\(\tfrac12\) homogeneous | — | PROVED | §4.1 | PROVED | — |
| B-5.2 | **the relative distortion grows linearly in matrix size**: isotropic BW \(=(m+1)/(4M)\), AIRM \(=(m+1)/(2M)\); general BW range \(\big[\tfrac1{2M},\ \tfrac{m-1/2}{M}\big]\) | equal eigenvalues for the isotropic figures | PROVED | §4.2 | PROVED | the first draft's stated range was wrong at **both** ends (O-10); the corrected upper end is \(3.54\times\) larger at \(m=12\) |
| B-5.3 | at the flagship configuration (\(m=12\), \(M\approx21\), spectrum \(3.0\to0.5\)) the **exact** BW distortion is \(8.82\%\to35.86\%\) of the eigenvalue and the **exact** AIRM distortion is \(32.92\%\). It is not small | stated spectrum | PROVED BY EXACT COMPUTATION (second-order formula understates by \(3\)–\(8\%\) of itself) | §4.3 | PROVED | \(M\) is the effective number of independent increments and is application-specific; the second-order figures are an approximation and are labelled as one (O-14) |
| B-5.4 | BW distorts small eigenvalues **more** than large ones, so it compresses the forecast spectrum | \(\lambda\) spread | PROVED | §4.4 | PROVED | this concerns the *evaluation target's* spectrum, not the estimator's \(\Delta_n\) — see LO-6 |
| B-5.5 | recalibration restores the **location of the optimum** — the required map is \(\rho=\Phi\), the induced-target map itself, **not** its inverse — and can never restore **ranking robustness** | — | PROVED | §5.1 | PROVED | the first draft inverted the map (O-11); the impossibility half is BW-specific and is not a general non-Bregman theorem |
| B-5.6 | a **scalar** recalibration \(H\mapsto cH\) restores consistency iff the relative distortion is eigenvalue-independent; for AIRM \(c=1-\tfrac{m+1}{2M}\) exactly | Wishart proxy | PROVED | §5.2 | PROVED | the constant was inverted in the first draft (O-11); at the flagship the wrong constant gives \(0.477\Sigma\) where zero error was claimed |
| B-5.7 | exact debiasing map exists when the proxy's conditional second-moment tensor is known; it is a forecast transformation, not a loss repair | known \(C\) | PROVED | §5.3 | PROVED | needs a fourth-moment model |
| B-E5.1 | infill and microstructure noise **conflict**: the distortion falls at \(\Theta(M^{-1})\) while naive realised covariance acquires an \(\Theta(M)\) noise bias | iid noise | PROVED / CITED+APPLIED | §6.1 | PROVED | — |
| B-E5.2 | conditional unbiasedness of realised covariance is itself only exact when the drift vanishes; a nonzero drift contributes at \(\Theta(M^{-1})\) — the same **order** as the geodesic distortion, but with a constant roughly \(50\times\) smaller at realistic parameters | Itô semimartingale | CITED+APPLIED | §6.2 | CITED+APPLIED | same order, very different constant: \(\alpha^2/\sigma^2\approx0.06\) against \((m+1)/4=3.25\). The order-matching is real; the prose must not imply the effects are comparable in size (O-20) |
| B-E5.3 | the noise-robust estimators the literature offers are established as **consistent**, not conditionally unbiased; LO-1 needs the latter | — | CITED+APPLIED | §6.3 | CITED+APPLIED | absence of an unbiasedness theorem is not a proof of bias; stated as such |
| B-E5 | **E5 terminal:** infill is not a clean escape. It trades a proved \(\Theta(M^{-1})\) distortion for an unproved conditional-unbiasedness premise, and the two effects conflict rather than trade off | — | REFORMULATED+PROVED | §6.4 | REFORMULATED+PROVED | — |

Numerical corroboration for every second-order formula is recorded in §7; §8 is the intermediate-claim register.

## 1. Setting and geometry primitives

BW geometry on \({\rm SPD}(m)\), verified rather than assumed:
- \(d_{\rm BW}(A,B)^2=\operatorname{tr}A+\operatorname{tr}B-2\operatorname{tr}(A^{1/2}BA^{1/2})^{1/2}\);
- metric at \(\Sigma\) on \(V\in\mathrm{Sym}\): \(\langle V,V\rangle_\Sigma=\tfrac12\operatorname{tr}(VL)\) where \(L=\mathcal S_\Sigma[V]\) solves \(\Sigma L+L\Sigma=V\);
- \(\operatorname{Exp}_\Sigma(V)=(I+L)\Sigma(I+L)\), \(L=\mathcal S_\Sigma[V]\);
- \(\operatorname{Log}_\Sigma(A)=(T-I)\Sigma+\Sigma(T-I)\), with the optimal transport map \(T=T_{\Sigma\to A}=\Sigma^{-1/2}(\Sigma^{1/2}A\Sigma^{1/2})^{1/2}\Sigma^{-1/2}\); equivalently \(\mathcal S_\Sigma[\operatorname{Log}_\Sigma A]=T-I\).

Proxy: \(\widehat\Sigma=\Sigma+\Delta\), \(\mathbb E[\Delta\mid\mathcal F]=0\), \(\|\Delta\|=O_p(\varepsilon)\). Write \(\Sigma=\operatorname{diag}(\lambda_1,\dots,\lambda_m)\) in its own eigenbasis, \(s_i=\sqrt{\lambda_i}\).

Throughout, \(G(H,A):=\operatorname{tr}(H^{1/2}AH^{1/2})^{1/2}\) and \(\Gamma(H):=2\{G(H,\Sigma)-\mathbb E G(H,\widehat\Sigma)\}\ge0\) as in dossier A §4.2.

## 2. LO-2 — squared BW distance is not proxy-robust

### 2.1 B-2.1 — strict convexity in the realisation

From the variational identity (proved in P1-ID §14.2 and re-verified here)
\[
\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}=\tfrac12\inf_{T\succ0}\big[\operatorname{tr}(TA)+\operatorname{tr}(T^{-1}\Sigma)\big],
\tag{2.1}
\]
\(A\mapsto G(A,\Sigma)\) is an infimum of functions **affine in \(A\)**, hence concave; and by the symmetry \(G(A,\Sigma)=G(\Sigma,A)\) the same holds in either slot. Strictness: the optimiser \(T^\star(A)=A^{-1/2}(A^{1/2}\Sigma A^{1/2})^{1/2}A^{-1/2}\) is constant along \(A_0+tH\) only if \(T^\star HT^\star=0\), i.e. \(H=0\).

Therefore
\[
A\mapsto d_{\rm BW}^2(A,H)=\operatorname{tr}A+\operatorname{tr}H-2G(H,A)
\]
is **strictly convex** in \(A\), not affine. Proxy-robustness demands (dossier A, A-1.1) that the loss be affine in the realisation up to a forecast-free term. \(\operatorname{tr}A\) is affine and \(\operatorname{tr}H\) is forecast-only; the entire obstruction is the cross term \(-2G(H,A)\), which is jointly nonlinear. ∎

### 2.2 B-2.2 — the induced target is the BW barycentre

\(H\mapsto\mathbb Ed_{\rm BW}^2(\widehat\Sigma,H)\) is the Fréchet functional of the conditional law of \(\widehat\Sigma\). Its stationarity condition is \(\mathbb E[\operatorname{Log}_H\widehat\Sigma]=0\). Substituting the Log formula,
\[
0=\mathbb E\big[(T_{H\to\widehat\Sigma}-I)H+H(T_{H\to\widehat\Sigma}-I)\big]
=(\mathbb E T-I)H+H(\mathbb E T-I).
\]
Because \(H\succ0\), the Sylvester operator \(X\mapsto XH+HX\) is injective, so \(\mathbb E T_{H\to\widehat\Sigma}=I\). Writing \(T=H^{-1/2}(H^{1/2}\widehat\Sigma H^{1/2})^{1/2}H^{-1/2}\) gives the fixed point
\[
\boxed{\ \mathbb E\big[(H^{1/2}\widehat\Sigma H^{1/2})^{1/2}\big]=H.\ }
\tag{2.2}
\]
Existence and uniqueness of the minimiser in the open cone are **not** assumed here: they are the project's own P1-ID §14.2 result (R1 and R2), proved for arbitrary laws charging the full-rank cone. ∎

### 2.3 B-2.3 — LO-2 terminal

By A-1.1/A-1.2 a proxy-robust loss must be Bregman in the linear coordinate; by B-2.1 \(d_{\rm BW}^2\) is strictly convex, hence not affine, in that coordinate; by A-4.3 it is symmetric and not a squared Mahalanobis form. **Squared Bures–Wasserstein distance is not proxy-robust. DISPROVED.** Its induced target is the conditional BW barycentre of the *proxy*, which by (2.2) differs from \(\Sigma=\mathbb E[\widehat\Sigma\mid\mathcal F]\) whenever the proxy is nondegenerate.

### 2.4 B-2.4 — the exact ranking reversal, in closed form

*(Counterexample record, per the campaign's counterexample standard.)*
**Target functional:** \(\Sigma=\mathbb E[\widehat x\mid\mathcal F]=1\), \(m=1\).
**Proxy law:** two points, \(\widehat x\in\{(1+a)^2,(1-a)^2\}\) with \(\mathbb P[(1+a)^2]=p=\frac{2-a}{4}\), for \(a\in(0,1]\).
*Unbiasedness:* \(\mathbb E\widehat x=p(1+a)^2+(1-p)(1-a)^2=1+2a(2p-1)+a^2=1-a^2+a^2=1\). ✓
**Loss:** \(L(\widehat x,h)=d_{\rm BW}(\widehat x,h)^2=(\sqrt{\widehat x}-\sqrt h)^2\), realisation first.
**Forecast class:** \(\{H_1,H_2\}\) with \(H_1=1\) (the true conditional mean) and \(H_2=(1-\tfrac{a^2}2)^2\).
Since \(a\le1\), \(\sqrt{(1-a)^2}=1-a\) and \(\mathbb E\sqrt{\widehat x}=1+a(2p-1)=1-\tfrac{a^2}2\).
**Expected losses under the truth** (degenerate proxy \(\equiv1\)):
\(L(1,H_1)=0\), \(L(1,H_2)=\big(1-(1-\tfrac{a^2}2)\big)^2=\tfrac{a^4}4>0\).
**Expected losses under the proxy:**
\(\mathbb E L(\widehat x,H_1)=\mathbb E\widehat x-2\mathbb E\sqrt{\widehat x}+1=2-2(1-\tfrac{a^2}2)=a^2\);
\(\mathbb E L(\widehat x,H_2)=1-2(1-\tfrac{a^2}2)^2+(1-\tfrac{a^2}2)^2=1-(1-\tfrac{a^2}2)^2=a^2-\tfrac{a^4}4\).
**Ranking reversal:** the truth ranks \(H_1\) strictly better (\(0<\tfrac{a^4}4\)); the proxy ranks \(H_2\) strictly better (\(a^2-\tfrac{a^4}4<a^2\)) for every \(a\in(0,1]\).
**Feature responsible:** strict concavity of \(x\mapsto\sqrt x\); the Jensen gap \(\mathbb E\sqrt{\widehat x}<\sqrt{\mathbb E\widehat x}\) enters the cross term and is forecast-dependent.
**Classification:** *coordinate-induced*. The proxy is unbiased in \(x\); the loss is Mahalanobis in \(\sqrt x\).
**Lift to \(m\ge2\):** take \(\widehat\Sigma=\widehat x\,I_m\), \(H_i=h_iI_m\); BW restricted to the scalar ray is \(\sqrt m\) times the scalar distance, so the identical reversal holds.
*(Closed form verified numerically at \(a=0.2,0.5,1.0\) to machine precision; \(a=1.5\) was checked and correctly **fails**, confirming that the parameterisation genuinely requires \(a\le1\).)* ∎

## 3. LO-3 — the exact induced bias

### 3.1 B-3.1 — scalar, exact

For \(m=1\), \(d_{\rm BW}(x,h)^2=(\sqrt x-\sqrt h)^2\). Minimising \(\mathbb E(\sqrt x-u)^2\) over \(u=\sqrt h>0\) gives \(u^\star=\mathbb E\sqrt x\), so
\[
\boxed{\;H^\star=(\mathbb E\sqrt x)^2=\mathbb E[x]-\operatorname{Var}(\sqrt x).\;}
\]
Exact for every law with \(\mathbb Ex<\infty\); no expansion, no small-noise hypothesis. The induced bias is \(-\operatorname{Var}(\sqrt x)\le0\), vanishing iff the proxy is degenerate. *(Verified to machine precision.)* ∎

### 3.2 B-3.2 — matrix, second order

Put \(H=\Sigma+B\) with \(B=O(\varepsilon^2)\), and expand (2.2) around \(\widehat\Sigma=H\):
\(\widehat\Sigma=H+(\Delta-B)\), \(M_H:=H^{1/2}\widehat\Sigma H^{1/2}=H^2+E\), \(E=H^{1/2}(\Delta-B)H^{1/2}\).
Write \((H^2+E)^{1/2}=H+D_1+D_2+O(\varepsilon^3)\). Matching orders in \((H+D_1+D_2)^2=H^2+E\):
\[
HD_1+D_1H=E\ \Rightarrow\ D_1=\mathcal S_H[E];\qquad
HD_2+D_2H+D_1^2=0\ \Rightarrow\ D_2=-\mathcal S_H[D_1^2].
\]
\(D_1\) is symmetric (Sylvester with symmetric data and \(H\succ0\)), so \(D_1^2\) is symmetric and \(D_2\) is well defined. Taking expectations in (2.2):
\[
H=\mathbb E[(H^2+E)^{1/2}]=H+\mathcal S_H[\mathbb EE]-\mathcal S_H[\mathbb E D_1^2]+O(\varepsilon^3).
\]
\(\mathbb EE=-H^{1/2}BH^{1/2}\), and to leading order \(D_1=\mathcal S_H[H^{1/2}\Delta H^{1/2}]\). Injectivity of \(\mathcal S_H\) gives \(-H^{1/2}BH^{1/2}=\mathbb E[D_1^2]\), i.e., replacing \(H\) by \(\Sigma\) to leading order,
\[
\boxed{\;H^\star=\Sigma-\Sigma^{-1/2}\,\mathbb E[G^2]\,\Sigma^{-1/2}+O(\varepsilon^3),\qquad
\Sigma G+G\Sigma=\Sigma^{1/2}\Delta\Sigma^{1/2}.\;}
\tag{3.1}
\]
**Scalar check.** \(m=1\): \(2\sigma^2G=\sigma^2\delta\Rightarrow G=\delta/2\), \(B=-\sigma^{-1}(\mathbb E\delta^2/4)\sigma^{-1}=-v/(4\sigma^2)\), matching the exact result since \(\operatorname{Var}(\sqrt x)\approx v/(4\sigma^2)\). ✓ ∎

### 3.3 B-3.3 — eigenbasis form

In \(\Sigma\)'s eigenbasis, \((\Sigma^{1/2}\Delta\Sigma^{1/2})_{ij}=s_is_j\Delta_{ij}\) and the Sylvester equation gives \(G_{ij}=s_is_j\Delta_{ij}/(\lambda_i+\lambda_j)\). Hence
\((G^2)_{ij}=s_is_j\sum_k\lambda_k\Delta_{ik}\Delta_{kj}/\{(\lambda_i+\lambda_k)(\lambda_k+\lambda_j)\}\), and
\[
\boxed{\;B_{ij}=-\sum_{k=1}^m\frac{\lambda_k\,\mathbb E[\Delta_{ik}\Delta_{kj}]}{(\lambda_i+\lambda_k)(\lambda_k+\lambda_j)}.\;}
\tag{3.2}
\]
**Eigenvector rotation** is governed entirely by the off-diagonal entries: to first order in \(B\), the eigenvector of \(H^\star\) associated with \(\lambda_i\) is rotated toward direction \(j\) by the angle \(B_{ij}/(\lambda_i-\lambda_j)+O(\|B\|^2)\). So *zero eigenvector rotation at second order \(\iff\) \(B_{ij}=0\) for all \(i\ne j\)*, i.e.
\[
\sum_k\frac{\lambda_k\,\mathbb E[\Delta_{ik}\Delta_{kj}]}{(\lambda_i+\lambda_k)(\lambda_k+\lambda_j)}=0\qquad\text{for all }i\ne j.
\tag{3.3}
\]
This is a **weighted** condition on the proxy's fourth-moment tensor. It is the exact necessary and sufficient condition, and it is manifestly not automatic.

### 3.4 B-3.4 — the commuting case, exactly

If every realisation of \(\widehat\Sigma\) is diagonal in \(\Sigma\)'s eigenbasis, BW restricted to that commuting orthant is **isometric to Euclidean space in the square-root coordinate**: \(d_{\rm BW}(A,B)^2=\sum_i(\sqrt{a_i}-\sqrt{b_i})^2\). The barycentre is therefore exactly \(h_i^\star=(\mathbb E\sqrt{\lambda_i(\widehat\Sigma)})^2=\mathbb E[\lambda_i]-\operatorname{Var}(\sqrt{\lambda_i})\), and the eigenvectors are exactly unchanged. **This is exact, not second order.**

Note also that this is the one branch in which BW *is* flat and *is* affinely charted — by \(\Sigma\mapsto\Sigma^{1/2}\) — so by A-4.3 it would be robust for a proxy unbiased for \(\Sigma^{1/2}\). Route E3 asks whether such a proxy exists; dossier C answers no.

### 3.5 B-3.5 — the Wishart case: exactly diagonal, with a closed form

Let the proxy have Gaussian fourth-moment structure,
\[
\operatorname{Cov}(\widehat\Sigma_{ab},\widehat\Sigma_{cd}\mid\mathcal F)=\tfrac1M(\Sigma_{ac}\Sigma_{bd}+\Sigma_{ad}\Sigma_{bc}),
\tag{3.4}
\]
which is the exact covariance of \(M^{-1}W_m(\Sigma,M)\) and the leading covariance of realised covariance under a continuous Itô semimartingale with \(M\) equally spaced increments. In \(\Sigma\)'s eigenbasis \(\Sigma_{ab}=\delta_{ab}\lambda_a\), so
\[
\mathbb E[\Delta_{ik}\Delta_{kj}]=\tfrac1M(\Sigma_{ij}\Sigma_{kk}+\Sigma_{ik}\Sigma_{kj})
=\tfrac1M(\delta_{ij}\lambda_i\lambda_k+\delta_{ik}\delta_{kj}\lambda_i\lambda_j).
\]
For \(i\ne j\) **both** terms vanish (\(\delta_{ij}=0\), and \(\delta_{ik}\delta_{kj}=0\) since \(k\) cannot equal both). Hence (3.3) holds identically and
\[
\boxed{\;B_{ij}=0\ (i\ne j),\qquad
B_{ii}=-\frac{\lambda_i}{M}\left[\frac14+\sum_{k=1}^m\frac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\right].\;}
\tag{3.5}
\]
*(Derivation: \(B_{ii}=-\sum_k\lambda_k\frac1M(\lambda_i\lambda_k+\delta_{ik}\lambda_i^2)/(\lambda_i+\lambda_k)^2\); the \(\delta_{ik}\) term contributes \(\lambda_i\cdot\lambda_i^2/(2\lambda_i)^2\cdot\frac1M=\lambda_i/(4M)\).)*
*Scalar check:* \(m=1\) gives \(-\frac\lambda M[\frac14+\frac14]=-\frac{\lambda}{2M}\), and indeed \(\operatorname{Var}(\sqrt x)\approx\operatorname{Var}(x)/(4\lambda)=2\lambda^2/(4M\lambda)=\lambda/(2M)\). ✓
*(Verified numerically: off-diagonal exactly \(0\) to machine zero for \(m=3,5,12\); closed form matches the tensor formula to \(10^{-17}\).)*

**Verdict on the informal claim.** "The matrix distortion is almost entirely in the eigenvalues" is **true for a Gaussian/Wishart-type proxy, and it is a property of the proxy's fourth-moment structure, not of Bures–Wasserstein geometry.** The one small simulation that produced the informal claim used exactly such a proxy. The claim must be stated with its hypothesis attached.

**Strengthening forced by the Wave-3 audit (O-15).** The first draft said rotation "reappears at \(O(M^{-2})\)" through the third-order term. That is wrong, and wrong in the project's favour: **for a genuine Wishart proxy the induced target is exactly diagonal at every order.** Let \(D=\operatorname{diag}(\pm1)\) in \(\Sigma\)'s eigenbasis. \(D\) commutes with \(\Sigma^{1/2}\), so \(D\widehat\Sigma D\) has the same Wishart law as \(\widehat\Sigma\). The BW barycentre is orthogonally equivariant, \(H^\star(UQU^\top)=UH^\star(Q)U^\top\), and it is unique (P1-ID §14.2). Hence \(DH^\star D=H^\star\) for all \(2^m\) sign patterns, which forces \(H^\star\) diagonal. No expansion is involved. (3.4) alone does **not** give this — it constrains only second moments — so the exact statement is a property of the Wishart law, not of its covariance tensor.

### 3.6 B-3.6 — the general claim is false: an explicit rotating counterexample

Take \(m=3\), \(\Sigma=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)\) with distinct \(\lambda_i\), and the symmetric two-point proxy
\[
\widehat\Sigma=\Sigma\pm\epsilon A,\quad\text{each w.p. }\tfrac12,\qquad
A=\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},
\]
which is conditionally unbiased by construction. Then \(\mathbb E[\Delta_{ik}\Delta_{kj}]=\epsilon^2\sum\)-free \(=\epsilon^2A_{ik}A_{kj}\), and for \((i,j)=(1,3)\),
\(\sum_k\lambda_k\epsilon^2A_{1k}A_{k3}/\{(\lambda_1+\lambda_k)(\lambda_k+\lambda_3)\}=\epsilon^2\lambda_2/\{(\lambda_1+\lambda_2)(\lambda_2+\lambda_3)\}\ne0\).
So \(B_{13}\ne0\): the induced target has a **genuinely rotated eigenbasis**, with rotation angle \(\asymp B_{13}/(\lambda_1-\lambda_3)\).
*(Verified: exact barycentre computed to convergence; empirical \(B_{13}=-7.144\times10^{-5}\) against theory \(-7.143\times10^{-5}\); the eigenvector matrix of \(H^\star\) is not a signed permutation.)*
**DISPROVED as a general claim; REFORMULATED as B-3.5.**

**Why this matters to this project.** A pure level effect on the evaluation target is a nuisance. An eigenvector rotation of the evaluation target is a distortion of the *direction* information — the same kind of object the identification campaign protects. The correct statement is that the flagship proxy class is protected and a general proxy class is not, and the protection must be *declared and checked*, not assumed.

### 3.7 B-3.7 — AIRM

The AIRM Fréchet (Karcher) mean satisfies \(\mathbb E[\log(H^{-1/2}\widehat\Sigma H^{-1/2})]=0\). With \(F=H^{-1/2}(\Delta-B)H^{-1/2}\), \(\log(I+F)=F-\tfrac12F^2+O(\varepsilon^3)\), so \(\mathbb EF=\tfrac12\mathbb E F^2\) and
\[
B=-\tfrac12\,\Sigma^{1/2}\,\mathbb E\big[(\Sigma^{-1/2}\Delta\Sigma^{-1/2})^2\big]\,\Sigma^{1/2}+O(\varepsilon^3),
\qquad
B_{ij}=-\tfrac12\sum_k\frac{\mathbb E[\Delta_{ik}\Delta_{kj}]}{\lambda_k}.
\tag{3.6}
\]
Under (3.4), off-diagonals vanish for the same reason and
\[
\boxed{\;B^{\rm AIRM}_{ii}=-\frac{\lambda_i\,(m+1)}{2M}.\;}
\tag{3.7}
\]
*(Scalar check \(m=1\): \(-\lambda/M\), and indeed the geometric mean of \(\sigma^2\chi^2_M/M\) is \(\sigma^2e^{\psi(M/2)-\log(M/2)}\approx\sigma^2(1-1/M)\). ✓ Verified numerically.)*

Note (3.7) is **exactly twice** the isotropic BW distortion of §4.2, and unlike BW it is *proportional* to \(\lambda_i\) — a pure uniform shrink.

### 3.8 B-3.8 — log-Euclidean

The log-Euclidean loss is Euclidean in \(\Lambda=\log\Sigma\), so its induced target is **exact and requires no expansion**:
\[
\boxed{\;H^\star_{\rm LE}=\exp\big(\mathbb E[\log\widehat\Sigma]\big).\;}
\]
Second order, using the Daleckiĭ–Kreĭn second-derivative formula \(D^2\log_\Sigma[\Delta,\Delta]_{ij}=2\sum_k\Delta_{ik}\Delta_{kj}\,\ell[\lambda_i,\lambda_k,\lambda_j]\) with \(\ell=\log\) and \(\ell[\cdot,\cdot],\ell[\cdot,\cdot,\cdot]\) its first and second divided differences, and \(D\exp_\Lambda[X]_{ij}=X_{ij}/\ell[\lambda_i,\lambda_j]\):
\[
B^{\rm LE}_{ij}=\frac{\sum_k\mathbb E[\Delta_{ik}\Delta_{kj}]\ \ell[\lambda_i,\lambda_k,\lambda_j]}{\ell[\lambda_i,\lambda_j]} .
\tag{3.8}
\]
*(Scalar check: \(\ell[\lambda,\lambda,\lambda]=-1/(2\lambda^2)\), \(\ell[\lambda,\lambda]=1/\lambda\), giving \(-\mathbb E\Delta^2/(2\lambda)\) — the same as AIRM. ✓ Verified numerically: relative error halves with the noise scale.)*
In the **commuting** case (3.8) coincides with (3.6); in the noncommuting case it does **not**, and the discrepancy was verified numerically to be \(O(1)\) relative, not \(O(\varepsilon)\). Both are non-robust; the project consumes only the exact statement \(H^\star_{\rm LE}=\exp\mathbb E\log\widehat\Sigma\) and the fact that (3.8) is diagonal under (3.4).

## 4. LO-5 part 1, and E5 part 1 — infill

### 4.1 B-5.1 — rate and non-uniformity

By (3.1) the distortion is the proxy's conditional second moment passed through the fixed bounded linear map \(\Delta\mapsto-\Sigma^{-1/2}\mathcal S_\Sigma[\Sigma^{1/2}\Delta\Sigma^{1/2}]^2\Sigma^{-1/2}\). Hence
\[
\|H^\star-\Sigma\|\asymp\mathbb E\|\Delta\|^2\asymp M^{-1},
\]
exactly the order of the proxy's conditional variance, with no geometric amplification and no geometric cancellation.

**Uniformity.** The distortion in the *ranking* is governed by \(\Gamma\), and by A-E4.1 \(\Gamma(cH)=\sqrt c\,\Gamma(H)\) exactly. So the distortion is **not uniform** over the forecast class: it is degree-\(\tfrac12\) homogeneous and grows without bound as the forecast level grows. Uniformity holds only on norm-bounded subsets of the cone bounded away from the boundary, and the constant degrades as \(\lambda_{\min}(H)\to0\).

### 4.2 B-5.2 — the relative distortion grows with matrix size

From (3.5), with all eigenvalues equal to \(\lambda\):
\[
\frac{|B_{ii}|}{\lambda}=\frac1M\left[\frac14+\frac m4\right]=\frac{m+1}{4M}\quad\text{(BW)},
\qquad
\frac{|B^{\rm AIRM}_{ii}|}{\lambda}=\frac{m+1}{2M}\quad\text{(AIRM)}.
\]
Both grow **linearly in the matrix size**. This is the single most consequential fact in this dossier: the distortion is not a small fixed constant, it is a constant times \(m/M\), and covariance forecasting is precisely the setting in which \(m\) is not small.

For a general spectrum the relative distortion is \(\frac1M\big[\frac14+\sum_k\lambda_k^2/(\lambda_i+\lambda_k)^2\big]\), and its exact range is
\[
\frac1{2M}\ \le\ \frac{|B_{ii}|}{\lambda_i}\ \le\ \frac{m-\tfrac12}{M},
\]
**not** the range the first draft gave (O-10). The \(k=i\) term contributes exactly \(\tfrac14\) always, so the infimum — attained as \(\lambda_i\) dominates every other eigenvalue — is \(\frac1M(\tfrac14+\tfrac14)=\frac1{2M}\); the supremum — attained as \(\lambda_i\) is dominated by every other — is \(\frac1M(\tfrac14+(m-1)+\tfrac14)=\frac{m-1/2}{M}\). The isotropic value \((m+1)/(4M)\) is an interior point, not an endpoint. At \(m=12\) the true upper end is \(11.5/M\) against the \(3.25/M\) first written — a factor \(3.54\). The auditor confirmed it directly: at \(\operatorname{cond}\Sigma=100\) and \(M=21\) the smallest eigenvalue's distortion is \(51.9\%\). **The correction makes the finding larger, not smaller.**

### 4.3 B-5.3 — the flagship numbers

The parent's APP-FIN uses \(m=12\) U.S. stocks and 240 **monthly** realised covariance matrices built from daily returns, so the effective number of independent increments per observation is \(M\approx21\).

| Configuration | BW relative distortion | AIRM relative distortion |
|---|---|---|
| \(m=12\), \(M=21\) (monthly RC from daily returns, spectrum \(3.0\to0.5\)) | **8.82%** (largest eigenvalue) to **35.86%** (smallest) — **exact**; the second-order formula gives \(8.91\%\to33.37\%\) and understates | **32.92%** (uniform) — **exact**; second order gives \(30.95\%\) |
| \(m=12\), \(M=78\) (daily RC from 5-minute returns) | ≈ 2.4% to 9.0% | ≈ 8.3% |
| \(m=12\), \(M=1638\) (monthly RC from 5-minute returns) | ≈ 0.11% to 0.43% | ≈ 0.40% |
| \(m=3\), \(M=500\), spectrum \(3.0\to0.5\) | 0.13% to 0.37% | 0.40% |

**Plainly stated: at the project's flagship sampling configuration the distortion is not small. It is tens of percent.** A forecaster who reports the correct conditional mean is beaten, under an AIRM loss, by one who shrinks the whole covariance by about a third; under a BW loss, by one who shrinks it by about a fifth on average and by more than a third in its smallest direction. (The first draft said "roughly a third" of both; that is right for AIRM and wrong for BW, whose mean shrink is \(\approx19\%\) — O-14.) Infill does fix it — but only by moving to intraday sampling, which is the regime where E5's microstructure conflict bites.

### 4.4 B-5.4 — spectral compression

From (3.5), \(|B_{ii}|/\lambda_i\) is **decreasing** in \(\lambda_i\): large eigenvalues are shrunk proportionally less than small ones. Hence the induced target's spectrum is *compressed* relative to \(\Sigma\)'s. Concretely, at \(m=12,M=21\) the largest eigenvalue loses 8.9% and the smallest 33.4%, so eigenvalue *ratios* are distorted, not merely the level.

**Scope warning, stated so it cannot be misread.** This is a statement about the spectrum of the *evaluation target* \(H^\star\), i.e. about what a BW loss rewards. It is **not** a statement about the estimator's eigengap \(\Delta_n\), which is defined from the lag operator on the observed array and is untouched. The relationship between the two is the subject of LO-6, and it is an edge into the existing \(\zeta_n\) budget, not a change to any estimation theorem.

## 5. LO-5 part 2 — recalibration

### 5.1 B-5.5 — what recalibration can and cannot restore

Let \(\rho:\mathcal H\to\mathcal H\) be any forecast transformation ("recalibration") and consider the composite loss \(\tilde L(y,h)=L(y,\rho(h))\).

- **Location of the optimum.** \(\mathbb EL(\widehat\Sigma,u)\) is minimised at \(u=\Phi(\Sigma)\), where \(\Phi\) is the induced-target map \(\Sigma\mapsto H^\star\). So \(\arg\min_h\mathbb E\tilde L(\widehat\Sigma,h)=\Sigma\) requires \(\rho(\Sigma)=\Phi(\Sigma)\), i.e. **\(\rho=\Phi\), not \(\Phi^{-1}\)**. The first draft had this backwards (O-11): with \(\rho=\Phi^{-1}\) the minimiser is \((1-\kappa)^2\Sigma\), which at the flagship configuration lands at \(0.586\Sigma\) rather than \(\Sigma\). Read plainly: a forecaster whose belief is the conditional mean must **shrink before submitting** in order to win a contest scored by a geodesic loss. Recalibration therefore *can* restore Fisher-consistency, exactly, when \(\Phi\) is known.
- **Ranking robustness.** It *cannot*. Robustness requires \(\tilde L\) to be affine in \(y\) up to an \(h\)-free term (A-1.1). But \(\tilde L(y,h)=d_{\rm BW}^2(y,\rho(h))\) has exactly the same \(y\)-dependence as \(d_{\rm BW}^2(y,\cdot)\), which is strictly convex in \(y\) (B-2.1) for every fixed second argument. Reparameterising the second argument cannot change the first argument's convexity. Hence **no recalibration of the forecast makes a non-Bregman loss proxy-robust.**

This is the sharpest thing in the constructive half of the campaign and it must be stated in exactly these terms: *recalibration fixes the target; only the loss class fixes the ranking.* Conflating them would be the error the campaign is designed to catch. **PROVED.**

### 5.2 B-5.6 — when a scalar recalibration suffices

A scalar Mincer–Zarnowitz correction \(H\mapsto cH\) restores consistency iff the induced-target map is a scalar multiple, i.e. iff \(B_{ii}/\lambda_i\) is the same for all \(i\) (and \(B_{ij}=0\)). Under (3.4) that requires
\[
\sum_k\frac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\ \text{independent of }i,
\]
which holds iff all \(\lambda_i\) are equal, or \(m=1\). **So for BW, a scalar recalibration is exact only in the isotropic case and is otherwise a partial repair**: it removes the common level shift and leaves the spectral compression of §4.4.
For **AIRM** the situation is better: (3.7) is exactly proportional to \(\lambda_i\), so the **single scalar** \(c=1-\dfrac{m+1}{2M}\) restores consistency exactly to second order under (3.4) — and, by the congruence-equivariance argument of C-7.2, exactly at all orders for a genuine Wishart, with \(\log c=\tfrac1m\big[\sum_{i=1}^m\psi(\tfrac{M+1-i}2)+m\log2-m\log M\big]\). That is a genuine asymmetry between the geometries and it is worth reporting: AIRM's distortion is a pure uniform shrink, BW's is a shrink plus a spectral compression. **PROVED.**

### 5.3 B-5.7 — the exact debiasing map

If the conditional second-moment tensor \(C\) is known or modelled, (3.2) defines \(B=B(\Sigma,C)\) explicitly and the corrected report is \(H\mapsto H-B(H,C)\), consistent to \(O(\varepsilon^3)\). Together with A-E1.3's gap-corrected loss these are the campaign's two constructive companions. Both are conditional on a fourth-moment model, and both must be labelled conditional. **PROVED, with the hypothesis stated.**

## 6. E5 — infill asymptotics and the microstructure conflict

### 6.1 B-E5.1 — the two effects move in opposite directions

The geodesic-loss distortion is \(\Theta(M^{-1})\) (B-5.1). Under additive i.i.d. microstructure noise with variance \(\sigma^2_u\), naive realised variance satisfies \(\mathbb E[\mathrm{RV}]=\mathrm{IV}+2M\sigma_u^2\) — a bias that is \(\Theta(M)\), i.e. **increasing** in the sampling frequency (Zhang–Mykland–Aït-Sahalia 2005, JASA, Eq. (18); Hansen–Lunde). So the two effects are not a trade-off along a common axis: increasing \(M\) monotonically improves one and monotonically destroys the other. Balancing them gives an interior optimal \(M\), which is precisely the classical "optimal sampling frequency" problem, and at that optimum **neither** effect is negligible. **PROVED / CITED+APPLIED.**

### 6.2 B-E5.2 — conditional unbiasedness is itself only \(O(M^{-1})\)-exact

Even with no microstructure noise, realised covariance is exactly conditionally unbiased for integrated covariance only when the drift vanishes. With drift \(\alpha\), each increment contributes \(\mathbb E[r_\ell r_\ell^\top]=\int\Sigma_s\,ds+O(M^{-2})\) per increment, so summing gives a drift contribution of order \(M^{-1}\) (Barndorff-Nielsen and Shephard, 2002, *J. Applied Econometrics* 17(5)). **The premise of the entire robustness framework — conditional unbiasedness of the proxy — therefore fails at exactly the same order \(M^{-1}\) as the distortion the framework is used to diagnose.**

This is a genuine and uncomfortable finding and it is recorded as such rather than smoothed over. It does **not** dissolve the no-go: LO-4 is a statement about the loss class, proved under exact unbiasedness, and an approximately unbiased proxy makes both the Bregman offset and the geodesic distortion approximate at the same order. What it does is bound how much the constructive companions can be trusted: correcting a \(\Theta(M^{-1})\) distortion is only meaningful if the unbiasedness premise holds to better than \(\Theta(M^{-1})\), which under drift it does not. **CITED+APPLIED, with the consequence stated.**

### 6.3 B-E5.3 — noise-robust estimators are consistent, not conditionally unbiased

| Estimator | Established property | Source |
|---|---|---|
| realised covariance, no noise | exactly unbiased iff drift \(\equiv0\); otherwise \(O(M^{-1})\) drift term | Barndorff-Nielsen–Shephard (2002) |
| naive RV under i.i.d. noise | biased by \(+2M\sigma_u^2\) | Zhang–Mykland–Aït-Sahalia (2005), Eq. (18) |
| two-scale / multi-scale (TSRV, MSRV) | **consistency + CLT only**; no unbiasedness theorem | ZMA (2005) Thm 4; Zhang (2006) |
| realised kernels | consistency + asymptotic normality; multivariate form PSD by construction | Barndorff-Nielsen–Hansen–Lunde–Shephard (2008/2011) |
| pre-averaging | consistency + CLT; the efficient bias-corrected form is **not guaranteed PSD** in finite samples | Jacod–Li–Mykland–Podolskij–Vetter (2009); Christensen–Kinnebrock–Podolskij (2010) |

Two things follow. First, LO-1 requires **conditional unbiasedness**, and the literature supplies **consistency**; these are different, and the gap is not closed by citing a consistency theorem. Second, a proxy that is not guaranteed PSD is not admissible for a geodesic loss at all — the loss is undefined off the cone — so the noise-robust estimators that would be needed to push \(M\) up are exactly the ones that can leave the domain.

*(Absence of an unbiasedness theorem is not a proof of bias. This row records what is established, not a claim that these estimators are biased.)*

### 6.4 B-E5 — terminal verdict on E5

**REFORMULATED+PROVED.** Infill removes the geodesic-loss distortion at \(\Theta(M^{-1})\), and the distortion's constant grows linearly in matrix size, so the relevant quantity is \(m/M\) and not \(1/M\). At the project's flagship configuration \(m/M\approx0.57\) and the distortion is tens of percent. Pushing \(M\) up conflicts with microstructure noise, whose naive bias grows as \(\Theta(M)\); the noise-robust estimators that would resolve that are established as consistent rather than conditionally unbiased, and some are not guaranteed positive semidefinite. Infill is therefore **not** a clean escape from LO-4: it trades a proved \(\Theta(m/M)\) distortion for an unproved conditional-unbiasedness premise. The honest advice is to use a robust loss, not a finer grid.

## 7. Computation record — what is closed form and what is numerical

Closed form (proved above, numerics used only for corroboration): B-2.1, B-2.2, B-2.4, B-3.1, B-3.2, B-3.3, B-3.4, B-3.5, B-3.6, B-3.7, B-3.8, B-5.1–B-5.7.

Numerical corroboration performed (scripts under `/home/claude/verif`, not part of the repository):
1. scalar identity \((\mathbb E\sqrt x)^2=\mathbb E x-\operatorname{Var}\sqrt x\), \(4\times10^6\) draws — agreement to \(10^{-15}\);
2. second-order BW, AIRM and log-Euclidean formulas against **exactly solved** barycentres of random 4-atom laws on \({\rm SPD}(3)\), at two noise scales — relative error halves when \(\varepsilon\) halves, the signature of a correct second-order expansion and a genuine \(O(\varepsilon^3)\) remainder;
3. Wishart tensor: off-diagonal bias exactly \(0\) (machine zero) for \(m=3,5,12\); closed form (3.5) matches the tensor formula (3.2) to \(10^{-17}\); (3.7) likewise;
4. the rotating counterexample of §3.6: theory \(-7.143\times10^{-5}\) versus exactly solved \(-7.144\times10^{-5}\), and a genuinely rotated eigenbasis;
5. the closed-form ranking reversal of §2.4 at \(a=0.2,0.5,1.0\) (holds) and \(a=1.5\) (correctly fails, confirming the stated restriction \(a\le1\));
6. \(\Gamma(cH)=\sqrt c\,\Gamma(H)\) to 12 digits at \(c=1/4,4,9\).

**Three claims did rest on numerics alone in the first draft, and the audit named them (O-19):** B-3.8's \(O(1)\) relative discrepancy between the log-Euclidean and AIRM second-order biases in the noncommuting case; B-3.6's assertion that the perturbed eigenbasis is "not a signed permutation"; and C-7.2's \(\|\Delta w\|\) figure. All three were independently reproduced by the auditor (0.197, \(1.67\times10^{-4}\), 0.040). They are now labelled as **numerically established, not proved**, and no *status* in the node register depends on them: B-3.8's terminal status rests on its exact induced-target formula, B-3.6's on the closed-form off-diagonal computation, and C-7.2's on the exact GMV blindness theorem.

## 8. Intermediate-claim register (transitive closure input)

| Node | Terminal status |
|---|---|
| B-2.1 strict convexity of \(d^2_{\rm BW}\) in the realisation | PROVED |
| B-2.2 barycentre fixed point | PROVED (existence/uniqueness CITED to P1-ID §14.2, internal) |
| B-2.3 LO-2 | DISPROVED (BW is not proxy-robust) |
| B-2.4 exact ranking reversal | PROVED |
| B-3.1 scalar exact bias | PROVED |
| B-3.2 matrix second-order bias | PROVED |
| B-3.3 eigenbasis form and rotation criterion | PROVED |
| B-3.4 commuting case exact | PROVED |
| B-3.5 Wishart diagonality + closed form | PROVED |
| B-3.6 general "purely spectral" claim | DISPROVED, with explicit counterexample |
| B-3.7 AIRM bias | PROVED |
| B-3.8 log-Euclidean exact target + second-order bias | PROVED |
| B-5.1 infill rate, non-uniformity | PROVED |
| B-5.2 linear growth in \(m\) | PROVED |
| B-5.3 flagship numbers | PROVED (arithmetic) |
| B-5.4 spectral compression | PROVED |
| B-5.5 recalibration cannot restore robustness | PROVED |
| B-5.6 scalar recalibration: exact for AIRM, partial for BW | PROVED |
| B-5.7 exact debiasing map | PROVED (conditional on a fourth-moment model, stated) |
| B-E5.1 infill/noise conflict | PROVED / CITED+APPLIED |
| B-E5.2 drift breaks exact conditional unbiasedness at \(O(M^{-1})\) | CITED+APPLIED |
| B-E5.3 consistency ≠ conditional unbiasedness | CITED+APPLIED |
| B-E5 route verdict | REFORMULATED+PROVED |
| Daleckiĭ–Kreĭn second-derivative formula (used in B-3.8) | CITED+APPLIED; the only consumer is (3.8), whose scalar and commuting specialisations are independently verified |

No node in this dossier is left non-terminal.
