---
type: proof-dossier
title: APP-C — dependence, dimension, and hostile application audit
status: noncanonical-workstream
verdict: T-APP-4 is proved for summable dimension-uniform Hilbert physical dependence; T-APP-5 is proved for structural Hessian classes and remains open for unrestricted full AIRM SPD
last-audited: 2026-08-08
scope: Paper 1 application-map workstream only
---

# APP-C — dependence, dimension, and hostile application audit

> **Authority and scope.** This is a noncanonical workstream dossier for the Paper 1 application-map run. It does not edit or supersede [[HD1 — growing-dimension Paper 1 proof dossier]] or any other canonical file. Paper 2 is out of scope. The robust HD1 theorem remains valid exactly as stated.

## 1. Executive verdict

1. **T-APP-4 is settled positively for a useful causal physical-dependence class.** A weighted Hilbert sum obeys a dimension-free \(L^2\) inequality when its functional-dependence coefficients are summable in \(L^2\). If the innovation effects are summable in essential supremum, bounded differences gives a dimension-free sub-Gaussian tail. These are exactly the inequalities consumed by integrated/grid G1, uniform G1, and the Hilbert–Schmidt lag row. **PROVED.**
2. Fixed finite memory is the special case in which the coefficients vanish after a fixed lag. Summable absolute regularity gives a dimension-free second-moment result by coupling, but not the exponential uniform-G1 inequality proved here. Unqualified polynomial \(\alpha\)-mixing remains false by the bounded regenerative counterexample in HD1-C. **PROVED / DISPROVED AS QUALIFIED.**
3. **T-APP-5 is settled for structural Hessian classes.** A signed local-polynomial estimator can grow in ambient dimension without an operator sphere net when its observation Hessian is deterministic, scalar plus a uniformly Hilbert–Schmidt-bounded remainder, or block-scalar with a controlled number of fixed blocks. Shrinking localisation around a preliminary positive estimator replaces a fixed-radius spatial net. Flat Hilbert models, one fixed commuting AIRM flat, and bounded constant-curvature Hadamard spaces qualify. **PROVED UNDER EXPLICIT ASSUMPTIONS.**
4. Isotropy only scalarises the **expected** Hessian. It does not make the empirical Hessian deterministic. Arbitrary commuting Hessians reduce the operator norm to a maximum over blocks and pay \(\sqrt{\log K_n/(nb_n)}\) unless the block count is controlled. The required structural Hessian budget is not verified for unrestricted full AIRM SPD. **DISPROVED / OPEN AS QUALIFIED.**
5. Bounded total tangent energy is a trace-class regime. Coordinatewise bounded variance is insufficient. Trace-bounded covariance gives a second-moment budget but neither an almost-sure geometry tube nor, by itself, a root-\(n\) lag-product theorem. Fixed intrinsic rank with bounded coefficients or a justified norm normalisation can supply total-energy control. A normalisation can dilute \(\Delta_n\), so it is never rate-free. **PROVED / DISPROVED AS QUALIFIED.**

The physical-dependence extension changes dependence, not the robust numerator:

\[
\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1},\qquad
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
=O_p\!\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right).
\]

The signed structural-Hessian branch replaces \(b_n^3\) by \(b_n^q\), \(q=d+1\), in mean estimation. It does **not** by itself make the feasible lag perturbation quadratic and therefore does not alone recover an oracle loading numerator.

## 2. Energy and dimension ledger

Let \(H_n\) be the transported tangent Hilbert space and \(Y_{t,n}\in H_n\).

### Proposition C-E1 — exact total-energy implications

1. If \(\|Y_{t,n}\|\le R\) almost surely, then
   \[
   \|Y_{t,n}\otimes Y_{t-h,n}\|_{\rm HS}\le R^2,
   \qquad \operatorname{tr}\operatorname{Cov}(Y_{t,n})\le R^2.
   \]
2. If \(Y_{t,n}=B_nz_{t,n}\), \(\operatorname{rank}B_n\le k<\infty\), \(\|B_n\|_{\rm op}\le C_B\), and \(\|z_{t,n}\|\le C_z\), then total energy is bounded by \(C_BC_z\), regardless of \(\dim H_n\).
3. If only \(\operatorname{tr}\operatorname{Cov}(Y_{t,n})\le C\) and \(\mathbb EY_{t,n}=0\), then \(\mathbb E\|Y_{t,n}\|^2\le C\). This is enough for an independent score second-moment calculation. It does not imply a pathwise tube or the fourth/product moment needed under general serial dependence.
4. If raw coordinate energy is \(O(p_n)\) and \(\bar Y_{t,n}=p_n^{-1/2}Y_{t,n}\), then \(\mathbb E\|\bar Y_{t,n}\|^2=O(1)\). An almost-sure bound follows only from an almost-sure raw norm bound. This scaling changes every lag covariance and the lag-operator signal.

**Status: PROVED.** These are the rank-one identity, covariance trace identity, and direct scaling.

### Counterexample C-E2 — coordinatewise variance is not total energy

Let \(Y=(\xi_1,\ldots,\xi_{p_n})\), with independent Rademacher coordinates. Every coordinate is bounded with variance one, while \(\|Y\|=\sqrt{p_n}\). For \(N\) independent copies,

\[
\mathbb E\left\|N^{-1}\sum_{i=1}^NY_i\right\|^2=\frac{p_n}{N}.
\]

Thus coordinatewise moments do not yield a dimension-free \(N^{-1/2}\) Hilbert rate. **DISPROVED.**

### Counterexample C-E3 — trace covariance alone does not close lag rows

Let \(Z_k\) be iid, centred, with \(\mathbb EZ_k^2=1\) and \(\mathbb EZ_k^4=\infty\). Randomise a phase \(U\in\{0,1\}\), independently, and set

\[
Y_{2k+U}=Y_{2k+U+1}=Z_ke_1.
\]

The stationary version is one-dependent and has covariance trace one. At one of the phase-aligned lag-one rows, \(Y_t\otimes Y_{t-1}=Z_k^2(e_1\otimes e_1)\), whose variance is infinite. The HD1 \(L^2\) lag-row proof is unavailable, and root-\(n\) does not follow from trace covariance alone. A sufficient repair is

\[
\sup_{t,h\le h_0}\mathbb E\{\|Y_t\|^2\|Y_{t-h}\|^2\}<\infty
\]

plus a dependence inequality for the product process, or bounded total energy. **DISPROVED; corrected implication PROVED.**

### Counterexample C-E4 — normalisation can erase signal

Let a raw \(p_n\)-vector have a bounded serial factor only in direction \(e_1\), with factor lag \(C_f(h)=c\ne0\), and serially white coordinates elsewhere. Dividing the whole vector by \(\sqrt{p_n}\) makes total energy \(O(1)\), but the factor lag becomes \(c/p_n\), and the rank-one lag-operator eigengap becomes

\[
\Delta_n=\frac{c^2}{p_n^2}.
\]

Normalisation is not an innocuous proof trick. If a pervasive factor itself has raw size \(\sqrt{p_n}\), the same scaling may preserve signal; this must be checked from the DGP. **DISPROVED as a universal implication.**

### Matrix normalisations

For an \(m_n\times m_n\) symmetric matrix, \(p_n=m_n(m_n+1)/2\).

- Entrywise \(O(1)\) variation generally has Frobenius energy \(O(m_n^2)\); division by \(m_n\) makes it \(O(1)\).
- \(m_n\) log-eigenvalue coordinates of order one have AIRM tangent energy \(O(m_n)\); division of log coordinates by \(\sqrt{m_n}\), or the averaged metric \(m_n^{-1}g_{\rm AIRM}\), makes it \(O(1)\).
- Fixed-rank matrix variation with bounded singular values already has bounded Frobenius energy.

Changing the metric or scaling tangent observations changes lag covariances, \(\Delta_n\), and often the scientific estimand. These are modelling choices, not automatic verifications of HD-X.

## 3. T-APP-4 — dimension-uniform Hilbert physical dependence

### 3.1 Definition

Let \((\xi_j)_{j\in\mathbb Z}\) be independent innovations and

\[
Z_{t,n}=G_{t,n}(\ldots,\xi_{t-1},\xi_t)\in\mathcal H_n,
\]

where \(\mathcal H_n\) is any real Hilbert space. Let \(Z_{t,n}^{(k)}\) replace only \(\xi_{t-k}\) by an independent copy. Define

\[
\delta_{q,n}^Z(k)=\sup_t\|Z_{t,n}-Z_{t,n}^{(k)}\|_{L^q(\mathcal H_n)},
\qquad
\Theta_q^Z=\sup_n\sum_{k\ge0}\delta_{q,n}^Z(k).
\tag{PD}
\]

These are Hilbert-norm coefficients. Coordinatewise coefficients are not substitutes, because their aggregation can restore a \(p_n\) factor.

### Theorem C-PD1 — weighted Hilbert \(L^2\) inequality

If \(\Theta_2^Z<\infty\), then, for every finite deterministic scalar sequence \((a_t)\),

\[
\boxed{
\left\|\sum_ta_t(Z_{t,n}-\mathbb EZ_{t,n})\right\|_{L^2(\mathcal H_n)}
\le\Theta_2^Z\left(\sum_ta_t^2\right)^{1/2}.}
\tag{C-PD1}
\]

The constant is independent of \(n\) and \(\dim\mathcal H_n\).

**Proof.** Let \(\mathcal F_j=\sigma(\xi_s:s\le j)\) and \(P_jV=\mathbb E(V\mid\mathcal F_j)-\mathbb E(V\mid\mathcal F_{j-1})\). The causal martingale decomposition and standard one-innovation coupling give

\[
Z_{t,n}-\mathbb EZ_{t,n}=\sum_{j\le t}P_jZ_{t,n},
\qquad
\|P_{t-k}Z_{t,n}\|_2\le\delta_{2,n}^Z(k).
\]

Hilbert martingale differences at distinct \(j\) are orthogonal in \(L^2\). Minkowski in the Hilbert direct sum over \(j\) gives

\[
\begin{aligned}
\left\|\sum_ta_t(Z_t-\mathbb EZ_t)\right\|_2
&=\left\{\sum_j\left\|\sum_{k\ge0}a_{j+k}P_jZ_{j+k}\right\|_2^2\right\}^{1/2}\\
&\le\sum_{k\ge0}\left\{\sum_ja_{j+k}^2\|P_jZ_{j+k}\|_2^2\right\}^{1/2}\\
&\le\sum_{k\ge0}\delta_{2,n}^Z(k)\|a\|_2.
\end{aligned}
\]

\(\square\)

### Theorem C-PD2 — weighted dimension-free sub-Gaussian tail

Assume also \(\Theta_\infty^Z<\infty\). Then

\[
\boxed{
\Pr\left\{
\left\|\sum_ta_t(Z_t-\mathbb EZ_t)\right\|
\ge\Theta_2^Z\|a\|_2+x
\right\}
\le\exp\left[-\frac{2x^2}{(\Theta_\infty^Z)^2\|a\|_2^2}\right].}
\tag{C-PD2}
\]

**Proof.** Replacing innovation \(\xi_j\) changes the norm of the weighted sum by at most

\[
c_j=\sum_{t\ge j}|a_t|\delta_{\infty,n}^Z(t-j).
\]

Young's convolution inequality gives \(\sum_jc_j^2\le(\Theta_\infty^Z)^2\sum_ta_t^2\). Bounded differences, first for a finite innovation truncation and then by \(L^2\) convergence, gives the tail above its expectation. C-PD1 bounds the expectation. \(\square\)

### Corollary C-PD3 — the exact G1 inputs

Assume the proxy score at each deterministic population stage point has uniformly summable \((\Theta_2^S,\Theta_\infty^S)\), and the HD1 norm-Lipschitz interpolation modulus in \(u\) holds. Uniform Log Lipschitzness permits verification from physical coefficients of \(X_t\). Since \(\|w(u)\|_2\le C(nb_n)^{-1/2}\),

\[
\int_0^1\mathbb E\left\|\sum_tw_t(u)S_{t,n}(u)\right\|^2du
\le\frac{C(\Theta_2^S)^2}{nb_n},
\]

and the HD1 one-dimensional time grid gives

\[
\sup_u\left\|\sum_tw_t(u)S_{t,n}(u)\right\|
=O_p\!\left(\Theta_\infty^S\sqrt{\frac{\log n}{nb_n}}\right).
\]

Thus G1-HD, G1-HD-\(L^2\), GRID, and the polygonal frame remain valid after replacing fixed memory by (PD). **PROVED UNDER EXPLICIT ASSUMPTIONS.**

### Corollary C-PD4 — the exact oracle lag-row input

Assume \(\|Y_{t,n}\|\le R\) and let \(W_{t,h}=Y_t\otimes Y_{t-h}\in\mathcal S_2(H_n)\). The rank-one identity gives

\[
\delta_q^{W_h}(k)
\le R\{\delta_q^Y(k)+\mathbf1_{\{k\ge h\}}\delta_q^Y(k-h)\},
\qquad
\Theta_q^{W_h}\le2R\Theta_q^Y.
\tag{C-PROD}
\]

C-PD1 with average weights gives, for fixed \(h_0\),

\[
\boxed{
d_{\rm or,n}
=\left\{\sum_{h=1}^{h_0}
\|\widetilde\Gamma_n(h)-\Gamma_n(h)\|_{\rm HS}^2\right\}^{1/2}
=O_p\!\left(\frac{R\Theta_2^Y\sqrt{h_0}}{\sqrt n}\right).}
\tag{C-LAG}
\]

The robust feasible-versus-oracle comparison is pathwise, so dependence of the feasible transformed row need not be re-established. **PROVED.**

### Corollary C-PD5 — Paper 1 under physical dependence

Replace HD-M's fixed finite memory by C-PD3–4, retaining every other HD1 assumption. Then

\[
d_n=O_p(n^{-1/2}+\ell_n),
\qquad
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
=O_p\!\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right).
\]

Factor-number statements are unchanged after replacing their \(d_n\) input. At \(b_n=n^{-1/7}\), \(a\ge3/7\), the numerator remains \(n^{-3/7}\). This is a dependence generalisation, not an oracle accelerator. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

### 3.2 Martingale and mixing boundaries

**Martingale differences.** If \(Z_t\) is a Hilbert martingale difference, then

\[
\mathbb E\left\|\sum_ta_tZ_t\right\|^2
=\sum_ta_t^2\mathbb E\|Z_t\|^2.
\]

This closes integrated/grid second moments. A uniform G1 theorem additionally needs a dimension-free Hilbert martingale maximal/exponential inequality as an explicit assumption or an exactly checked citation. More importantly, if the transported factor row \(Y_t\) itself is a martingale difference, then \(\Gamma(h)=0\) for every positive lag, so the Paper 1 lag operator has no factor signal. Martingale innovations are useful building blocks for a serial factor process; “the observed score is an MDS” is generally incompatible with lag identification. **PROVED; application limitation explicit.**

**Absolute regularity.** If \(\|Z_t\|\le B\) and the row is absolutely regular with coefficients \(\beta(k)\), independent coupling gives

\[
|\mathbb E\langle Z_s,Z_t\rangle|\le2B^2\beta(|t-s|).
\]

Thus \(\sum_k\beta(k)<\infty\) gives a dimension-free weighted \(L^2\) inequality. This is enough for lag rows and integrated G1, but this dossier does not promote it to uniform G1 because an exponential inequality with the required bandwidth/grid constants has not been proved here. **PROVED FOR \(L^2\); UNIFORM BRANCH OPEN.**

**Unqualified polynomial mixing.** The bounded stationary regenerative scalar process in HD1-C has \(\alpha(h)\asymp h^{-\beta}\), \(0<\beta<1\), and sample-mean variance \(n^{-\beta}\). Embedding it in \(e_1\subset\mathbb R^{p_n}\) preserves bounded total energy for arbitrary \(p_n\). Hence “polynomial mixing” does not imply root-\(n\) Hilbert or lag-row concentration. **DISPROVED.**

### 3.3 Dependence-tail stability

Let

\[
\vartheta_q(L)=\sup_n\sum_{k>L}\delta_{q,n}(k).
\]

Successively replacing innovations older than \(L\) gives an \(L\)-memory approximation with \(\|Z_t-Z_t^{[L]}\|_q\le\vartheta_q(L)\). If one uses the finite-memory proof instead of C-PD1–2, the honest score and lag penalties are

\[
\rho_{\rm score}(L)
=\vartheta_\infty^S(L)+R\sqrt{\frac{L+1}{nb_n}},
\]

\[
\rho_{\rm lag}(L)
=R\vartheta_2^Y(L)+R^2\sqrt{\frac{L+h_0+1}{n}}.
\]

The first terms are coupling defects; the second are sampling errors of the truncated process. If the full summability budgets are bounded, direct physical-dependence concentration is sharper and no growing truncation length is needed.

A finite cross-fitting gap does not create independence for an infinite-memory Bernoulli shift. For

\[
Y_t=\sum_{k\ge0}\rho^k\xi_{t-k},\qquad |\rho|<1,
\]

with bounded Rademacher innovations, training and evaluation fields separated by \(g\) still share remote innovations; the natural coupling defect is of order \(|\rho|^g\), not zero. Any conditional GLO argument must add its first-order defect, typically \(O\{\vartheta_\infty(g)r_{0,n}\}\), and must prove stability of the trained estimator under that coupling. Robust Route R avoids this requirement. **DISPROVED: finite gap implies exact independence.**

## 4. T-APP-5 — signed growing-\(p_n\) smoothing

### 4.1 Structural Hessian condition

Let signed degree-\(d\) local-polynomial weights reproduce powers through \(d\), have \(\sum_t|w_t(u)|\le W\), and \(\sum_tw_t(u)^2\le C/(nb_n)\). Put \(q=d+1\). Use a preliminary positive estimator \(\widetilde\mu_n(u)\) and define the signed estimator as the minimiser over

\[
\overline B\{\widetilde\mu_n(u),\delta_n\},
\qquad \delta_n\downarrow0,
\tag{LOC}
\]

where the preliminary uniform error is \(o_p(\delta_n)\).

At \(q_0=\mu_n(u)\), assume

\[
H(q_0,X_{t,n})=a_{t,n}(u)I+K_{t,n}(u),
\tag{SH}
\]

with scalar \(|a_{t,n}|\le A\), Hilbert–Schmidt \(\|K_{t,n}\|_{\rm HS}\le B_K\), and dimension-uniform summable physical coefficients for the scalar and \(\mathcal S_2(H_n)\)-valued centred processes. Assume also:

- \(H(q,X)\) is \(L_H\)-Lipschitz in \(q\) in operator norm on the shrinking tube;
- the expected local-law Hessian is at least \(c_0I\), \(c_0>0\);
- law smoothing and local stationarity make the expected signed Hessian differ from the local Hessian by \(o(1)\);
- the signed score has the physical-dependence and smooth-bias assumptions of C-PD3.

### Theorem C-SG1 — structural signed growing-dimension G1

Under (LOC)–(SH), uniformly for arbitrary \(p_n\),

\[
\boxed{
\sup_ud\{\widehat\mu_n^{\rm LP}(u),\mu_n(u)\}
=O_p\!\left(
b_n^q+n^{-a}+n^{-1}
+\sqrt{\frac{\log n}{nb_n}}
\right).}
\tag{C-SG1}
\]

The integrated and deterministic-grid RMS stochastic term is \((nb_n)^{-1/2}\). No sphere net in \(H_n\) or the operator space is used.

**Proof.** At deterministic \(\mu_n(u)\), decompose the centred signed empirical Hessian into a scalar weighted sum and a Hilbert–Schmidt weighted sum. C-PD2 controls the first directly and the second in \(\mathcal S_2(H_n)\); \(\|K\|_{\rm op}\le\|K\|_{\rm HS}\). A polynomial time grid plus the norm modulus gives a uniform \(o_p(1)\) operator perturbation. On the preliminary-estimator event, every point in (LOC) lies within \(2\delta_n\) of \(\mu_n(u)\); Hessian Lipschitzness adds \(2L_H\delta_n=o(1)\). The signed criterion is therefore uniformly \(c_0/2\)-strongly convex on the local ball.

The score at \(\mu_n(u)\) is a Hilbert weighted sum. Polynomial reproduction gives bias \(O(b_n^q+n^{-a}+n^{-1})\), and C-PD2 gives the displayed stochastic rate. Strong convexity converts score norm to distance. Choose \(\delta_n\) larger than the preliminary and score rates, so the critical point is interior and unique. C-PD1 gives the integrated/grid version. \(\square\)

Localisation is essential: CE-9 still disproves uniqueness of an arbitrary global signed Fréchet objective.

### 4.2 Geometries and laws covered by C-SG1

1. **Flat Hilbert space:** \(H(q,x)=I\) pathwise. Take \(a=1,K=0\). This includes unconstrained symmetric matrices with Frobenius geometry. **EXACT STRUCTURAL MATCH.**
2. **One fixed commuting AIRM flat:** if centre, observations, loading directions, and the constrained estimator stay in one fixed jointly diagonal SPD flat, log-eigenvalue coordinates are Euclidean and the restricted Hessian is \(I\). Pairwise commutation with changing eigenbasis does not qualify. **EXACT STRUCTURAL MATCH UNDER THE FIXED-FLAT RESTRICTION.**
3. **Constant curvature \(-\kappa^2\le0\):** for \(r=d(q,x)\) and radial unit vector \(v\),
   \[
   H(q,x)=\alpha_\kappa(r)I+\{1-\alpha_\kappa(r)\}v\otimes v,
   \qquad
   \alpha_\kappa(r)=\kappa r\coth(\kappa r),
   \]
   with continuous value one at \(\kappa r=0\). At \(r=0\), where \(v\) is undefined, write the remainder as
   \[
   \{1-\alpha_\kappa(r)\}v\otimes v
   =\beta_\kappa(r)\,\log_q(x)\otimes\log_q(x),\qquad
   \beta_\kappa(r)=\{1-\alpha_\kappa(r)\}/r^2,
   \]
   with continuous limit \(-\kappa^2/3\). This proves that the rank-one Hilbert–Schmidt remainder extends smoothly through \(r=0\). On a bounded common tube, the scalar coefficient and remainder are uniformly bounded and Lipschitz, independently of dimension. No isotropy is needed. **PROVED UNDER COMMON-TUBE AND PHYSICAL-DEPENDENCE ASSUMPTIONS.**
4. **Fixed block-scalar structure:** if \(H_t=\sum_{k=1}^{K}a_{t,k}\Pi_k\) for fixed orthogonal projections and fixed \(K\), scalar concentration gives dimension-free SW-AS. For \(K=K_n\), the perturbation is
   \[
   O_p\!\left(\sqrt{\frac{\log(nK_n)}{nb_n}}\right),
   \]
   so strong convexity requires \(\log K_n=o(nb_n)\). **PROVED.**
5. **Scalar expected Hessian / isotropy:** this is not itself (SH). It controls the expectation but says nothing about the structural size of the centred empirical Hessian. It becomes sufficient only after (SH), fixed block count, or another proved operator inequality. **INSUFFICIENT ALONE.**
6. **Full AIRM SPD:** on a fixed spectral band, APP-A T-APP-2 proves the required matrix-size-uniform geometric differentials by direct matrix calculus; local symmetry alone would not prove this without the band/tube control. This dossier has not proved a matrix-size-uniform scalar-plus-HS or fixed-block decomposition for the random observation Hessian. The signed growing-\(p_n\) branch is **OPEN**. The positive three-scale HD1 route remains the robust fallback.

### Counterexample C-S2 — isotropy does not make the empirical Hessian deterministic

On hyperbolic \(p\)-space, let \(X=\operatorname{Exp}_q(rU)\), where \(U\) is uniform on the tangent unit sphere and \(r>0\). The law is invariant under the full stabiliser of \(q\), and

\[
H(q,X)=\alpha(r)I+\{1-\alpha(r)\}U\otimes U,
\]

so \(\mathbb EH(q,X)\) is scalar. For every realised \(U\) and \(p>1\), \(H(q,X)\) has radial eigenvalue one and tangential eigenvalue \(\alpha(r)>1\); it is not scalar. The corrected positive result is that constant-curvature geometry supplies the stronger scalar-plus-rank-one decomposition in C-SG1. **DISPROVED; corrected theorem PROVED.**

### Counterexample C-S3 — commuting empirical Hessians can retain a block-count cost

Consider bounded positive commuting operators

\[
H_t=I+c\operatorname{diag}(\varepsilon_{t1},\ldots,\varepsilon_{tK_n}),
\qquad 0<c<1,
\]

with iid Rademacher entries. Then \(\mathbb EH_t=I\), every \(H_t\) commutes, and

\[
\left\|N^{-1}\sum_{t=1}^N(H_t-I)\right\|_{\rm op}
=c\max_{j\le K_n}\left|N^{-1}\sum_t\varepsilon_{tj}\right|.
\]

If \(K_n\ge2^N\), with probability bounded away from zero at least one coordinate is constant across the sample, and the deviation is \(c\). Thus commuting **operators** do not remove the block maximum. This attacks the abstract empirical-Hessian implication; a geometric common commuting SPD flat is stronger because its restricted Hessian is exactly \(I\). **DISPROVED; corrected block theorem PROVED.**

### Rate consequence of the signed branch

Let

\[
\ell_{q,n}=b_n^q+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
\]

Under robust Route R, C-SG1 yields only

\[
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
=O_p\!\left(\frac{n^{-1/2}+\ell_{q,n}}{\Delta_n}\right).
\]

Balancing gives \(b_n\asymp n^{-1/(2q+1)}\) and \(\ell_{q,n}\asymp n^{-q/(2q+1)}\), still slower than \(n^{-1/2}\). If a **separate** first-order-immunity theorem makes the lag-row contribution quadratic, then \(\ell_{q,n}^2=o(n^{-1/2})\) can deliver an oracle numerator. C-SG1 supplies faster mean estimation; it does not prove immunity. **PROVED distinction.**

## 5. Approximate-assumption defect ledger

| Defect | Exact quantity | Leading penalty | Type of effect | Oracle-scale requirement | Status |
|---|---|---|---|---|---|
| Growing total energy | \(R_n=\sup_t\|Y_t\|\) | score \(R_n(nb)^{-1/2}\); oracle lag \(R_n^2n^{-1/2}\); feasible comparison \(2R_nq_n+q_n^2\) | sampling and geometry-tube enlargement | insert in full numerator | **PROVED** |
| Physical-dependence budget | \(\Theta_2^S,\Theta_\infty^S,\Theta_2^Y\) | multiplies score and lag stochastic terms | sampling constant/rate if budgets grow | meet desired numerator scale | **PROVED** |
| Dependence truncation tail | \(\vartheta_q(L)=\sum_{k>L}\delta_q(k)\) | §3.3 score and lag penalties | approximation plus sampling | choose \(L_n\) from displayed terms | **PROVED** |
| Included-lag noise/cross covariance | \(D_h=\Gamma_h-AC_f(h)A^*\), \(\zeta_n=(\sum_h\|D_h\|_{\rm op}^2)^{1/2}\) | \(2A_{2,n}\zeta_n+\zeta_n^2\) | population target/loading bias | \(o(\Delta_n)\); oracle scale if claimed | **PROVED** |
| Spectral-band escape | \(\pi_n=\sup_tP(X_t\notin\mathcal T_n)\) | all-row proof fails with probability at most \(n\pi_n\) | theorem-event failure | \(n\pi_n\to0\) unmodified | **PROVED** |
| Clipped spectral escape | bounded clipping, probability \(\pi_n\) | RMS \(O_p(R\sqrt{\pi_n})\); population lag bias \(O(R^2\pi_n)\) | changes estimand and sampling | meet numerator/gap scale | **PROVED UNDER BOUNDED CLIPPING** |
| Infinite-lag target | \(\rho_H=\sum_{h>h_0}\|\Gamma(h)\|_{\rm op}^2\) | \(\|\mathbb L_\infty-\mathbb L_{h_0}\|_{\rm op}\le\rho_H\) | finite-lag target bias | \(o(\Delta_\infty)\) | **PROVED** |
| Signal dilution | \(\Delta_n\downarrow0\) | every non-rigid numerator divided by \(\Delta_n\) | denominator | \(\eta_n=o(\Delta_n)\) | **PROVED** |
| Growing rank with bounded factor energy | \(r_n\to\infty\) | \(\Delta_n\le h_0R_f^4/r_n\) | signal dilution | budget decay | **PROVED** |
| Approximate cross-fit separation | gap \(g_n\), tail \(\vartheta_\infty(g_n)\) | \(O\{\vartheta_\infty(g_n)r_{0,n}\}\) plus estimator coupling | failure of conditional cancellation | proved remainder \(o(n^{-1/2})\) | **CONDITIONAL** |

For lag contamination, writing \(\mathcal G_0=[AC_f(1)A^*\ \cdots]\) and \(\mathcal D=[D_1\ \cdots]\) gives

\[
\|(\mathcal G_0+\mathcal D)(\mathcal G_0+\mathcal D)^*-\mathcal G_0\mathcal G_0^*\|_{\rm op}
\le2A_{2,n}\zeta_n+\zeta_n^2.
\]

The contaminated population \(\lambda_{r+1}\) is at most \(\zeta_n^2\), while its leading space can rotate at first order \(A_{2,n}\zeta_n/\Delta_n\). Included-lag noise is population bias, not merely sampling noise.

## 6. Hostile counterexamples and corrected implications

| False implication | Attack | Corrected implication | Status |
|---|---|---|---|
| coordinatewise variance implies total energy | C-E2 | impose total norm/trace budget | **DISPROVED** |
| trace covariance closes lag rows | C-E3 | add product moment or total bound | **DISPROVED** |
| normalisation is harmless | C-E4 | recompute \(s_n,\Delta_n\) | **DISPROVED** |
| polynomial mixing gives root-\(n\) | HD1-C regenerative scalar process | use C-PD/fixed memory | **DISPROVED** |
| finite cross-fit gap creates independence | infinite Bernoulli shift in §3.3 | pay coupling tail or use finite memory | **DISPROVED** |
| marginal sign symmetry implies GLO | C-L1 below | require joint/conditional lag symmetry | **DISPROVED** |
| isotropic expected Hessian is empirical scalar | C-S2 | add structural concentration | **DISPROVED** |
| commuting Hessians remove dimension cost | C-S3 | fixed blocks or \(\log K_n=o(nb_n)\) | **DISPROVED** |
| \(\pi_n\to0\) band escape suffices for all rows | if \(n\pi_n\nrightarrow0\), escape probability need not vanish | require \(n\pi_n\to0\), or clip and pay bias | **DISPROVED** |

### Counterexample C-L1 — marginal sign symmetry is not lag symmetry

On \(\{-2,-1,1,2\}\), let \(T\) be the cycle
\(-2\mapsto-1\mapsto1\mapsto2\mapsto-2\), and take
\[
P=(1-\epsilon)T+\epsilon\mathbf1\mathbf1^*/4,\qquad0<\epsilon<1.
\]
The stationary law is uniform, hence \(Y_t\overset d=-Y_t\), and the chain is geometrically mixing. Its lag-one law is not centrally symmetric. Embed the states on a hyperbolic geodesic through the mean. With transverse Hessian eigenvalue \(\lambda(|Y_t|)=|Y_t|\coth|Y_t|\),
\[
\mathbb E\{\lambda(|Y_t|)Y_{t-1}\}
=\frac{3(1-\epsilon)}4\{\lambda(2)-\lambda(1)\}\ne0.
\]
Thus marginal sign symmetry does not imply lag GLO. **DISPROVED.**

## 7. Proof-ready application feasibility rows

| Exact family | Energy/dependence check | Hostile failure | Strongest conclusion | Feasibility |
|---|---|---|---|---|
| bounded Hilbert functional data with quadrature \(L^2\) norm and causal C-PD law | bounded functional norm; Hilbert coefficients summable | raw grid norm and long memory | signed \(q=d+1\) mean plus physical-dependence HD1; loading first order absent immunity | **EXACT STRUCTURAL MATCH under stated DGP** |
| unconstrained symmetric matrices, Frobenius metric, fixed-rank/bounded-Frobenius variation | \(p_n=m_n(m_n+1)/2\); C-PD in Frobenius norm | entrywise \(O(1)\) energy grows; PSD meaning may be lost | flat signed/positive route and robust loading | **EXACT STRUCTURAL MATCH** |
| diagonal/fixed-eigenbasis SPD under AIRM | bounded log-eigenvalue energy; C-PD in log coordinates | changing eigenvectors, band escape | constrained \(H=I\), signed mean, robust loading | **EXACT under fixed basis** |
| full covariance/correlation SPD under AIRM | spectral band does not imply bounded AIRM Frobenius energy | noncommutation, escape, lag noise, dilution | positive robust HD1 only; signed APP-C unverified | **DIAGNOSTIC-ONLY / CONDITIONAL** |
| individual \(3\times3\) diffusion tensors | fixed dimension six | changing eigenvectors breaks commuting flat | fixed-\(p\) theorem; flat submodel if common eigenvectors | **STABLE fixed-dimensional match** |
| voxelwise diffusion-tensor product | product energy grows unless averaged/fixed active rank | spatial dependence and dilution | C-PD after explicit product norm and signal | **DIAGNOSTIC-ONLY** |
| functional-connectivity covariance matrices | band, energy, overlap dependence and regularisation explicit | singularity, eigenvector changes, target change | conditional positive-route fallback | **APPLICATION-FRAGILE** |
| bounded constant-negative-curvature embeddings | arbitrary \(p_n\); bounded radius; C-PD | curvature/tube growth and GLO failure | C-SG1 signed mean; robust loading first order | **EXACT STRUCTURAL MATCH** |
| product manifolds with \(K_n\) components | product-norm coefficients summable | energy sum; block-count Hessian cost | C-PD; signed with block budget | **STABLE APPROXIMATE MATCH** |
| Grassmann/shape/compact symmetric spaces | HD1 Hadamard fails globally | cut locus/nonunique Log | local tube reformulation needed | **UNKNOWN** |
| Bures–Wasserstein covariance data | metric-specific boundary/energy needed | PSD boundary and target change | no transfer from AIRM/flat results | **UNKNOWN** |

## 8. Integration matrix and closed dependencies

| Property | Exact criterion | Term improved | Rate/scope | Status |
|---|---|---|---|---|
| Hilbert physical dependence | C-PD for scores and \(Y\) | score and oracle lag sampling | same HD1 rate, broader dependence | **PROVED** |
| deterministic Hessian | \(H=H_0\), especially \(I\) | signed empirical Hessian vanishes | signed arbitrary \(p_n\) | **PROVED** |
| scalar plus HS Hessian | (SH) | operator net becomes Hilbert concentration | signed arbitrary \(p_n\) | **PROVED** |
| block scalar | fixed projections, \(K_n\) coefficients | sphere net becomes block maximum | \(\sqrt{\log(nK_n)/(nb)}\) | **PROVED** |
| isotropy alone | only \(\mathbb EH=cI\) | no empirical term killed | no theorem alone | **DISPROVED AS SUFFICIENT** |
| signed smoother alone | C-SG1 without immunity | \(b^3\to b^q\) only | faster mean, not oracle loading | **PROVED distinction** |

Dependency chain: C-PD gives score G1 and the HS lag row; existing HD1 polygonal framing and pathwise Route R then give the robust loading and selector theorems. C-SG1 gives faster signed mean convergence. An oracle numerator additionally requires a separate first-order-immunity theorem.

No OPEN node above is consumed by canonical HD1 or by a theorem labelled proved here. Optional nodes are unrestricted full-AIRM signed Hessian concentration, uniform G1 from weaker mixing alone, and estimator-stable approximate cross-fitting under infinite memory.

## 9. Cross-audit of APP-A and APP-B

| Claim attacked | Objection | Resolution / correction | Final status |
|---|---|---|---|
| APP-A AIRM finite-order constants are dimension-free | A fixed spectral band can have AIRM diameter \(\sqrt m\,\log(C/c)\), so a Jacobi proof based on Frobenius geodesic length would hide dimension growth | APP-A uses absolute bands, AIRM/Frobenius project norms, operator-norm bounds for whitened logs, Sylvester/resolvent calculus, and commutator Jacobi bounds. Constants are uniform only for fixed differential order and generated images in fixed expanded bands; no arbitrary Schatten/nuclear-norm claim is made | **ACCEPT IN THE STATED NORMS** |
| AIRM band verifies the complete statistical theorem | Spectral conditioning does not bound total tangent energy, mean-curve length, dependence budgets, lag orthogonality, or signal | APP-A explicitly separates HD-G from HD-X/HD-M/HD-L; \(d_{\rm AIRM}(I,eI)=\sqrt m\) is its counterexample | **SHORTCUT DISPROVED** |
| APP-A near-commuting Hessian defect | The former “convergent power series on \([-2L,2L]\)” need not lie inside the Taylor radius of \(s\coth s\) | §4.2 was repaired using dimension-free analytic functional calculus for the self-adjoint operators \({\rm ad}_Y,{\rm ad}_D\). The result still requires \(D,e\) in one fixed algebra and \(\|N\|_F\) small | **REPAIRED, THEN ACCEPT** |
| APP-A ribbon defect times area | Defining \(\varepsilon_R=\sup\|R(\partial_sS,\partial_\tau S)\|\) and then multiplying by geometric area double-counts ribbon velocities | §4.3 now normalises by \(\|\partial_sS\wedge\partial_\tau S\|\) before multiplying by area | **REPAIRED** |
| APP-B centred mean/frame fluctuations | Hidden ambient dimension could enter operator concentration | Conditional on an exact finite-memory split, \(e_t,\Omega_t\) are fixed and the summands live directly in \(\mathcal S_2(H_n)\); RMS envelopes and the Hilbert second-moment inequality give \(r_e\sqrt{(m+h)/N}\) and \(r_F\sqrt{(m+h)/N}\) without a net | **ACCEPT** |
| APP-B approximate cross-fitting from conditional TV | Pairwise conditional total variation controls a mean coefficient but not dependence/concentration of the full retained row | §7.1 now requires a joint row coupling or a conditional Hilbert/HS physical-dependence inequality, plus trained-estimator stability. T-APP-3B remains exact-split only | **SCOPE CORRECTED; APPROXIMATE BRANCH CONDITIONAL** |
| Physical dependence itself creates cross-fit independence | Summable infinite-memory effects leave shared remote innovations across every finite gap | APP-C C-PD1–2 broaden unconditional score/oracle-row concentration only. Conditional oracle immunity needs a separate joint coupling with its tail in \(d_{\rm CF,n}\) | **DISPROVED AS AN AUTOMATIC IMPLICATION** |
| APP-B frame coefficient satisfies \(\phi_F\lesssim A_2r_F\) | \(\phi_F\) is measured in HS norm, while \(A_2\) uses operator norms and may be much smaller at growing dimension | §7.2 now uses \(G_{2,{\rm HS}}\le\sqrt{h_0}R^2\), preserving dimension-free control under bounded total energy | **REPAIRED** |
| APP-B lag contamination requires exactly \(\zeta_n=o(n^{-1/2})\) | The true population-operator defect is \(2A_{2,n}\zeta_n+\zeta_n^2\); \(\zeta_n=o(n^{-1/2})\) is sufficient but not necessary when signal scale weakens | §§7.3 and 10 now state the exact condition. Target stability also separately requires this defect to be \(o(\Delta_n)\) | **REPAIRED** |
| Strong factor lag automatically supplies the relevant gap under contamination | \(\Delta_n\ge s_n^2\) uses exact factorised lag covariances; outside-loading lag noise can rotate or dominate the target | APP-B retains exact LN for its oracle theorem and treats \(D_h\) as population bias. The theorem uses the actual \(\Delta_n\); \(s_n^{-2}\) is only a proved weakening under factorisation | **ACCEPT** |
| APP-B mask/deletion defects are quadratic | The perforated training design changes mean moments by \(L_n/n\), while comparison of masked and unmasked lag targets is first order | APP-B §8 distinguishes \(L_n/n\) inside \(r_e^{\rm CF}\), whose contribution is squared under immunity, from \(d_{\rm mask}=O(L_n/n)\), which must itself be oracle-negligible | **ACCEPT** |
| Signed/constant-curvature mean theorem implies oracle loading | Faster bias or scalar-plus-HS Hessian structure controls mean estimation, not GLO or the non-rigid frame coefficient | APP-C and APP-B keep the signed branch first order under Route R. Oracle loading still needs exact separation, GLO, and frame rigidity or direct defect bounds | **SHORTCUT DISPROVED** |
| Full AIRM application is now an exact accelerated match | APP-A closes differential constants but not random-Hessian SH structure, total energy, dependence, LN, symmetry, or eigengap | Full AIRM remains a conditional robust positive-route match. The unrestricted signed and oracle branches remain unproved | **APPLICATION ROW QUALIFIED** |

Cross-audit conclusion:
\[
\text{APP-A differential control}\not\Rightarrow\text{cancellation},\qquad
\text{APP-C physical dependence}\not\Rightarrow\text{conditional separation},
\]
\[
\text{APP-C signed G1}\not\Rightarrow\text{first-order immunity},\qquad
\text{APP-B CF+GLO+frame rigidity}\Rightarrow\text{oracle numerator}
\]
only with every mask, coupling, contamination, and eigengap defect at its displayed scale. No remaining OPEN item is consumed by a theorem labelled proved.
