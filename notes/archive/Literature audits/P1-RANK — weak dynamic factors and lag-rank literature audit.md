# P1-RANK — weak dynamic factors and lag-rank literature audit

> **ARCHIVED 2026-08-21.** The publication-safe conclusions and source roles from this completed audit are integrated into [[Paper 1 — Locally stationary Riemannian factor model]], [[Analytical reconstruction — proof ledger and rebuilt spec]], [[References and external claim audit]], and [[Literature review — external positioning and prior art]]. This file preserves the full search and adjudication trail; it is not a parallel source of live theorem or queue status.

**Audit date:** 2026-08-21  
**Scope:** primary-source literature and analytical positioning only  
**Internal status authority:** `P1-RANK — AR1 signal strength and threshold boundary.md`, HD1, and the Paper 1 canonical theorem boundary  
**No claim made here changes a canonical theorem.**

## Executive verdict — ten lines

1. Identifying a loading space by squaring and summing nonzero-lag covariance operators is established in finite-dimensional and functional time-series work.
2. The exact formula \(\lambda_j(\mathbb L)=s_j^4\sum_h\rho_j^{2h}\) was not found stated as a theorem; it is an elementary diagonal-AR(1) specialisation of that established construction.
3. The literature's terms *strong* and *weak factor* usually measure cross-sectional loading pervasiveness or diverging spectral/covariance eigenvalues, not the project's bounded-energy factor amplitude \(s_j\).
4. Consequently, the project's fourth-power attenuation is an internally proved translation for its squared lag operator, not a universal definition of weak-factor strength.
5. Consistent threshold, information-criterion, raw-ratio-under-extra-separation, and ridged-ratio selectors all exist, but under materially different signal, dimension, and nuisance regimes.
6. Lam and Yao themselves did not prove the needed post-rank raw-ratio behaviour; Chang, Guo and Yao later called raw-ratio consistency unresolved and added a ridge to prove consistency.
7. This directly supports P-RATIO's narrow conclusion: signal/null eigenvalue rates alone do not justify the unrestricted raw argmin, without implying that the selector must fail in the parent's simulations.
8. No applicable minimax lower bound was found for detecting a weak serial factor through this dependent squared-lag operator, so AR1-THR remains sufficient rather than necessary or optimal.
9. Two-stage nuisance propagation is established for estimated regression residuals and, separately, for Riemannian covariance operators based on estimated mean curves, but not for RFD's moving centre, polygon transport, and lag-rank operator together.
10. Paper 1 should cite the lag-operator and selector ancestry, label AR1-SIG/AR1-THR as internally proved adaptations, and make no first, minimax, universal, or selector-optimality claim.

## 1. Question register

| Item | Terminal status | Terminal evidence verdict |
|---|---|---|
| **LIT-R1 — lag-operator population spectrum** | **CITED AND APPLIED** | Lam–Yao and Bhatia–Yao–Ziegelmann prove loading/dynamic-space identification from sums of squared nonzero-lag covariance matrices/operators. The diagonal AR(1) eigenvalue formula is an internal specialisation, not found verbatim. |
| **LIT-R2 — weak dynamic factors and minimum signal** | **COMPARISON ONLY** | Lam–Yao use cross-sectional loading strength, Bailey–Kapetanios–Pesaran use support pervasiveness, and Hallin–Liška use diverging spectral eigenvalues. None is interchangeable with bounded-energy amplitude. No checked source stated the project's fourth-power amplitude map as a general weak-factor law. |
| **LIT-R3 — factor-number selectors** | **CITED AND APPLIED** | Primary theorems cover a functional threshold, spectral information criteria, and a ridged lag-eigenvalue ratio. Raw ratios are supported only with extra post-rank/adjacent-spectrum control; Lam–Yao explicitly leave that behaviour conjectural. |
| **LIT-R4 — detection lower bounds** | **NOT FOUND AFTER DOCUMENTED SEARCH** | A sharp i.i.d. sparse-spiked covariance lower bound was verified, but its experiment and parameter class do not map to a dependent lag operator without a new reduction. No directly applicable serial-factor rank lower bound was found. |
| **LIT-R5 — estimated-coordinate nuisance layer** | **COMPARISON ONLY** | The parent propagates a globally estimated, time-invariant Fréchet centre into a manifold lag operator; Chang–Guo–Yao handle generated regression residuals and Lin–Yao handle an estimated manifold mean curve. None covers a single locally stationary series aligned by a shared polygonal frame. |
| **LIT-R6 — parent-paper scope** | **CITED AND APPLIED** | The PDF verifies Proposition 3's rates, Eq. (5)'s raw ratio, Example 1's dimension/dependence restrictions, and Table 2's finite-sample success. The rates-alone correction is preserved exactly. |
| **LIT-R7 — publication-safe positioning** | **CITED AND APPLIED** | Section 11 provides citation-safe lists, one related-work paragraph, and one theorem note with all novelty and optimality language bounded. |

## 2. Primary-source claim table

| Primary source | Exact result inspected | Model and regime | What it proves | Project use and boundary |
|---|---|---|---|---|
| [Lam & Yao (2012), *Factor modeling for high-dimensional time series: inference for the number of factors*](https://doi.org/10.1214/12-AOS970), §2, Proposition 1, Theorem 1, Corollary 1, Remark 2 | \(M=\sum_{k=1}^{k_0}\Sigma_y(k)\Sigma_y(k)^\top\); eigenanalysis and raw ratio (2.8) | Stationary finite-dimensional \(p\)-vector; fixed or growing \(p\); white-noise idiosyncratic component; factor strength indexed by \(\delta\) | Range of \(M\) identifies the loading space. Signal and null eigenvalues have different rates. Under their high-dimensional conditions \(\widehat\lambda_{r+1}/\widehat\lambda_r\to0\). | Core ancestry for AR1-SIG. Their \(\delta\) is loading/pervasiveness strength, not \(s_j\). Remark 2(ii) says post-rank ratios were not established, so it does not defeat P-RATIO. |
| [Bhatia, Yao & Ziegelmann (2010), *Identifying the finite dimensionality of curve time series*](https://doi.org/10.1214/10-AOS819), Proposition 1, Theorems 1 and 3 | \(K=\sum_{k=1}^{p}M_kM_k^*\), with a threshold \(\widehat d=\#\{j:\widehat\theta_j\ge\epsilon_n\}\) | Stationary functional time series with additive curve noise; finite dynamic dimension | A full-rank lag covariance suffices for the dynamic space; \(\|\widehat K-K\|_{HS}=O_p(n^{-1/2})\), nonzero eigenvalue error is root-\(n\), null eigenvalues are \(O_p(n^{-1})\); threshold consistency if \(\epsilon_n\to0\) and \(n\epsilon_n^2\to\infty\). | Closest external threshold theorem and functional operator analogue. Their one-full-rank-lag condition is stronger than HD-L's positive aggregate \(Q\). They do not have growing tangent coordinates or geometric nuisance. |
| [Hallin & Liška (2007), *Determining the number of factors in the general dynamic factor model*](https://www.princeton.edu/~erp/Econometrics/Old%20Pdfs/Hallin-Liska.pdf), DOI 10.1198/016214506000001275, Proposition 3 and Proposition 4 | Spectral-density residual criterion plus \(k p(n,T)\), minimised over \(0\le k\le q_{\max}\) | General dynamic factor model; cross-section \(n\) and time length \(T\) both grow; pervasive dynamic eigenvalues | Consistency when the first \(q\) dynamic eigenvalues diverge linearly, the rest remain bounded, the penalty vanishes, and the effective estimation rate times the penalty diverges. Rank zero is allowed. | Valid information-criterion comparison. It is a two-way pervasive spectral regime, not the bounded-energy fixed-rank lag-row experiment used by RFD. |
| [Bailey, Kapetanios & Pesaran (2021), *Measurement of factor strength: Theory and practice*](https://doi.org/10.1002/jae.2830), §§1–4 | Strength exponent \(\alpha\), defined through the rate at which the number of nonzero loadings grows with cross-section size | Static multifactor model; observed and latent factors; cross-section and sample size grow | \(\alpha=1\) is maximum strength, \(1/2<\alpha<1\) is semi-strong/pervasive, and \(\alpha<1/2\) is weak; the proposed strength estimator is developed for \(\alpha>1/2\). | Primary source for support-pervasiveness and localized/nonpervasive terminology. It measures how many coordinates a factor reaches, not its marginal time-series amplitude or persistence. |
| [Chang, Guo & Yao (2015), *High dimensional stochastic regression with latent factors, endogeneity and nonlinearity*](https://doi.org/10.1016/j.jeconom.2015.03.024), Eq. (10), Theorem 2.4 | \(\widetilde r=\arg\min_{1\le j\le R}(\widehat\lambda_{j+1}+C_T)/(\widehat\lambda_j+C_T)\) | High-dimensional, possibly nonstationary Euclidean regression plus serial latent factors; estimated regression residuals; \(p,T\to\infty\) | Under Conditions 2.1–2.5 and \(C_T=(p^{1-\delta}+\kappa_2)pT^{-1/2}\log T=o(1)\), \(P(\widetilde r\ne r)\to0\). The paper says raw-ratio consistency remained unresolved. | Direct precedent for a ridged lag-operator ratio and for generated rows. Its ridge and rates are model-specific, its candidate set excludes zero, and it is not a proof for HD1's chosen \(\tau_n\). |
| [Lin & Yao (2019), *Intrinsic Riemannian functional data analysis*](https://doi.org/10.1214/18-AOS1787), Proposition 2, Theorems 6–7 | Estimate a Fréchet mean curve, log-map observations there, transport estimated covariance/eigenfunctions into the population tensor Hilbert space | i.i.d. manifold-valued functional observations, general Riemannian manifold, dense trajectories | Uniform root-\(n\) mean-curve control; after intrinsic parallel transport, squared Hilbert–Schmidt covariance error is \(O_p(n^{-1})\), with eigenvalue/eigenfunction perturbation bounds. | Strong geometric two-stage comparison for HD-E. It is not a time-series lag-rank theorem and transports pointwise between estimated and true mean curves, not recursively along RFD's shared polygon. |
| [Cai, Ma & Wu (2015), *Optimal estimation and rank detection for sparse spiked covariance matrices*](https://doi.org/10.1007/s00440-014-0562-z), Theorems 2 and 5 | Exact rank recovery and minimax impossibility for sparse covariance spikes | \(n\) i.i.d. \(N(0,I_p+V\Lambda V^\top)\) observations; joint \(k\)-row-sparse spike space | Rank boundary \(\lambda_r\asymp\sqrt{(k/n)\log(ep/k)}\), with an upper theorem and a lower theorem. | Rejected lower-bound near-match. There is no serial dependence, lag covariance, squared lag operator, moving centre, or generated-coordinate nuisance. Substituting \(s^4\sum_h\rho^{2h}\) for \(\lambda_r\) is not justified. |
| [Caro & Peña (2024), *Selecting the number of factors in multi-variate time series*](https://e-archivo.uc3m.es/rest/api/core/bitstreams/36613676-92ea-424c-b8e4-e72b15b402bd/content), DOI 10.1111/jtsa.12760, Proposition 1 | Raw adjacent ratio of eigenvalues of a pooled squared lag-zero/nonzero-lag covariance matrix | Approximate dynamic factor model with \(N,T\to\infty\) | Consistency follows under A5: the first \(r\) sample operator eigenvalues grow like \(N\), the remainder are bounded, and hence the \(r\)-ratio diverges while other adjacent ratios remain bounded. | Useful modern confirmation that a raw-ratio theorem must control all competing adjacent ratios. A5 supplies the separation P-RATIO says cannot be inferred from signal/null rates alone. Candidate ranks start at one. |
| [Huang, Chen & Chen (2026), *A Riemannian Factor Model for Manifold-Valued Time Series*](https://arxiv.org/abs/2607.28385), Eq. (5), Proposition 3, Example 1, Table 2 | Raw ratio on the squared lag operator, with signal/root-\(n\) and null/\(n^{-1}\) rates | Stationary manifold-valued factor model with a time-invariant population Fréchet centre estimated globally from the data; fixed \(p\) theorem with concrete growing-\(p\) verification under stronger mixing/concentration | Proposition 3 gives the displayed eigenvalue rates. Example 1 verifies P3 under geometric mixing for restricted growing \(p\), and only fixed \(p\) under algebraic mixing. Table 2 reports strong finite-sample selection. | Parent comparison and correction target. The displayed rates alone do not establish the global raw argmin; this does not negate the reported simulations. |

## 3. LIT-R1 — lag-operator population spectrum

### 3.1 What is standard

The population construction is standard in the relevant time-series sense. Lam and Yao define

\[
M=\sum_{h=1}^{k_0}\Sigma_y(h)\Sigma_y(h)^\top
\]

and recover the loading space from its nonzero eigenspace. Their model permits a factor–future-noise cross-covariance term, but the left range of each lag covariance still lies in the loading space under their orientation of the assumptions. Bhatia, Yao and Ziegelmann give the Hilbert-space analogue

\[
K=\sum_{h=1}^{p}M_hM_h^*.
\]

Their Proposition 1 shows that if one factor lag-covariance matrix is full rank, \(K\) has exactly the dynamic dimension's nonzero eigenvalues and its range is the dynamic space.

Thus these sources produce the general mechanism consumed by AR1-SIG:

\[
\text{nonzero-lag covariance}
\longrightarrow
\text{squared positive operator}
\longrightarrow
\text{loading/dynamic space}.
\]

### 3.2 What is the internal specialisation

Under the internal independent stationary AR(1) model,

\[
\operatorname{Cov}(f_{t+h,j},f_{t,j})=s_j^2\rho_j^h.
\]

Hence the factor lag covariance is diagonal and

\[
\sum_{h\in\mathcal H}
\operatorname{Cov}(f_{t+h},f_t)
\operatorname{Cov}(f_{t+h},f_t)^\top
=
\operatorname{diag}\!\left(
s_j^4\sum_{h\in\mathcal H}\rho_j^{2h}
\right)_{j=1}^r.
\]

An isometric loading map preserves these nonzero eigenvalues. This is exactly AR1-SIG, up to decreasing rearrangement.

No checked primary source stated this diagonal AR(1) formula as a named proposition. The defensible description is therefore **"an elementary AR(1) specialisation of the standard squared-lag-operator construction"**, not a novelty claim about the operator idea itself.

### 3.3 Scope difference from HD-L

HD-L assumes exact vanishing of the residual lag covariance and both cross-lag directions, then only requires positivity of the aggregate factor operator \(Q\). Bhatia's one-full-rank-lag condition is sufficient but stronger. Lam and Yao allow a particular factor–noise cross term because their algebra still preserves the left loading range. Neither source supplies HD-L under the project's moving-frame, locally stationary coordinate construction.

## 4. LIT-R2 — weak factors and signal quantities

The word *weak* is not portable without its signal definition.

| Source/programme | Strength quantity | Strong/weak meaning | Relation to AR1-SIG |
|---|---|---|---|
| Lam–Yao | Pre-normalisation loading-column norm, with squared norm of order \(p^{1-\delta_j}\) | \(\delta_j=0\) strong/pervasive; \(\delta_j>0\) weaker in loading-norm order | A cross-sectional loading-strength notion. Weakness can come from sparse support or diffuse small loadings; it is not synonymous with localization and is not the marginal amplitude \(s_j\) under fixed total energy. |
| Bailey–Kapetanios–Pesaran | Exponent \(\alpha\) governing how the number of nonzero loadings grows with the cross-section | \(\alpha=1\) maximum strength; \(1/2<\alpha<1\) semi-strong/pervasive; \(\alpha<1/2\) weak/nonpervasive | This directly formalizes support pervasiveness and localized influence, but it does not encode serial persistence or the squared-lag signal. |
| Hallin–Liška | Eigenvalues of the common spectral-density matrix as cross-section grows | The \(q\) dynamic eigenvalues diverge, linearly under A5; idiosyncratic eigenvalues remain bounded | A frequency-domain pervasiveness notion with two-way asymptotics, not a finite-energy lag-row signal. |
| Cai–Ma–Wu | Minimum covariance spike \(\lambda_r\), plus support size \(k\) | Detectable/undetectable relative to \(\sqrt{(k/n)\log(ep/k)}\) | A static i.i.d. covariance spike, not an amplitude passed through a lag covariance and then squared. |
| Internal AR1-SIG | Marginal factor scale \(s_j\), persistence \(\rho_j\), lag set \(\mathcal H\) | Lag-operator signal \(\chi_j=s_j^4\sum_h\rho_j^{2h}\) | Exact only under the stated diagonal AR(1), isometric loading, and HD-L factorisation. |

The fourth power has a simple structural source: covariance is quadratic in amplitude (\(s_j^2\)); the positive lag operator squares that covariance (\(s_j^4\)). Under a weak-tail multiplier \(w\), the relevant eigenvalue is therefore multiplied by \(w^4\). This fourth power is **not** evidence that every dynamic-factor method pays a fourth power. A method based directly on a covariance or spectral spike, a row singular value, or a likelihood can have a different signal parameter.

Under fixed total factor-scale norm, the internal note also produces the separate dilution denominator

\[
\chi_{\mathrm{tail}}
=
\frac{F^4w^4}{(r-1+w^2)^2}
\sum_{h\in\mathcal H}\rho^{2h}.
\]

This combines amplitude weakness with rank dilution. No checked external weak-factor definition automatically supplies this denominator.

## 5. LIT-R3 — factor-number selectors

### 5.1 Selector audit

| Selector | Primary theorem | Candidate ranks; zero allowed? | Required separation | Signal/null rates | Exact conclusion |
|---|---|---|---|---|---|
| Eigenvalue threshold \(\#\{j:\widehat\theta_j\ge\epsilon_n\}\) | Bhatia–Yao–Ziegelmann, Theorem 3 | Counting form can return zero, although their model assumes fixed \(d\ge1\) | Fixed positive population signals; \(\epsilon_n\to0\), \(n\epsilon_n^2\to\infty\) | Signal error \(O_p(n^{-1/2})\); null eigenvalues \(O_p(n^{-1})\) | \(P(\widehat d\ne d)\to0\). |
| Spectral information criterion | Hallin–Liška, Propositions 3–4 | \(0\le k\le q_{\max}\); **yes** | First \(q\) spectral eigenvalues diverge linearly; remaining eigenvalues bounded; vanishing but sufficiently large penalty | Spectral-estimator rates enter the penalty condition | \(P(\widehat q=q)\to1\). |
| Raw lag-eigenvalue ratio | Lam–Yao, Eq. (2.8), Theorem 1/Corollary 1/Remark 2 | \(1\le j\le R\); **no** | Their theorems control the signal/null boundary; the required post-rank global comparison was conjectured, not proved | Faster null than signal rates | Boundary ratio tends to zero, but full argmin consistency is not supplied by the displayed rates alone. |
| Ridged lag-eigenvalue ratio | Chang–Guo–Yao, Eq. (10), Theorem 2.4 | \(1\le j\le R\); **no** | Signal eigenvalues dominate \(C_T\); null empirical eigenvalues are \(o_p(C_T)\); pre-r ratios have positive limits; post-r ridged ratios tend to one | Model-specific \(\|\widehat M-M\|\) rate, with \(C_T\) chosen larger by \(\log T\) | \(P(\widetilde r\ne r)\to0\). |
| Raw pooled squared-covariance ratio | Caro–Peña, Proposition 1 | \(1\le i\le r_{\max}\); **no** | A5 assumes first \(r\) sample eigenvalues are order \(N\), the rest bounded, and all competing adjacent ratios remain bounded | Not the HD1 \(d_n,\eta_n\) decomposition | Consistency follows under A1–A5. |
| Parent Eq. (5) raw ratio | Parent Proposition 3 plus prose | \(1\le i\le R\); **no** | PDF displays signal/root-\(n\) and null/\(n^{-1}\) rates but no separate global post-r ratio condition | As displayed | The prose says Proposition 3 justifies Eq. (5); the rates alone do not establish that global argmin. |

### 5.2 Exact comparison with P-RATIO

P-RATIO uses the admissible spectrum

\[
\operatorname{diag}(1,d_n^2,0)
\]

to show that the displayed boundary rates can coexist with a smaller empirical ratio after the true rank. Therefore:

- it **does contradict** the implication "signal error plus null-eigenvalue order alone implies consistency of the unrestricted raw-ratio argmin";
- it **does not contradict** Chang–Guo–Yao, because their ridge forces post-r ratios to one and their theorem proves the needed comparisons;
- it **does not contradict** Caro–Peña, because their A5 explicitly controls the competing adjacent ratios;
- it **does not contradict** Hallin–Liška, whose selector is a penalised information criterion;
- it **does not claim** the parent's raw ratio fails in practice.

The most important external corroboration is unusually direct. Lam and Yao's Remark 2(ii) says that they were unable to establish the post-r ratio asymptotics and treated them as conjectural. Chang, Guo and Yao then state that, despite favourable finite-sample evidence, consistency of the raw ratio remained unresolved, and their Theorem 2.4 proves consistency after adding \(C_T\). That history is exactly compatible with P-RATIO's logical correction.

### 5.3 Mapping to AR1-THR and TAU

Bhatia–Yao–Ziegelmann give the closest classical threshold template, but the internal theorem is more explicit for the HD1 decomposition. On the event EV,

\[
\widehat\lambda_{r+1}\le d_n^2,
\qquad
|\widehat\lambda_r-\lambda_r(\mathbb L)|\le\eta_n.
\]

Therefore exact threshold recovery holds iff the deterministic/random realised window is nonempty and

\[
d_n^2<\tau_n<\lambda_r(\mathbb L)-\eta_n.
\]

TAU's asymptotic producers

\[
d_n^2=o_p(\tau_n),
\qquad
\tau_n=o(\Delta_n),
\qquad
\eta_n=o_p(\Delta_n)
\]

are the project's sufficient way to make that window hold with probability tending to one. This is an internal adaptation, not a restatement of the functional theorem.

## 6. LIT-R4 — detection lower bounds

### 6.1 Verified near-match

Cai, Ma and Wu study \(n\) independent Gaussian vectors with

\[
\Sigma=I_p+V\Lambda V^\top,
\]

where the spike subspace has at most \(k\) nonzero rows. Their upper and lower rank-detection results establish the matching boundary

\[
\lambda_r
\asymp
1\wedge\sqrt{\frac{k}{n}\log\frac{ep}{k}}.
\]

The lower theorem is information-theoretic: below a small constant times this boundary, every rank estimator has error probability bounded away from zero over their parameter class.

### 6.2 Why it cannot be mapped to AR1-SIG

The RFD experiment is not a sample of i.i.d. Gaussian vectors with a static covariance spike. A serial factor changes the joint time-domain covariance, its lag covariance is then estimated, and that estimate is squared and summed. The effective experiment also contains local-centre and frame estimation. A valid reduction would need to specify, at minimum:

1. a complete Gaussian or other dominated law for the dependent series;
2. the observation-noise law and temporal covariance under ranks \(r\) and \(r-1\);
3. whether the manifold/tangent map is oracle-known or estimated;
4. a parameter class for loadings, persistence, energy, and dimension;
5. a Kullback–Leibler, chi-square, or total-variation comparison between the two rank experiments.

None of those steps follows by writing \(\lambda_r=s_{min}^4\sum_h\rho^{2h}\). The Cai–Ma–Wu boundary is therefore a **scope mismatch**, not a lower bound for RFD.

### 6.3 Documented negative search

Discovery searches were run across general web indexing, arXiv, Project Euclid/IMS records, journal DOI pages, and citation chains from Lam–Yao, Bhatia–Yao–Ziegelmann, Hallin–Liška, Chang–Guo–Yao, and the parent. Query families included:

- `minimax detection weak factor time series serial correlation rank r versus r-1 lower bound`;
- `minimax lower bound detecting weak dynamic factor spectral density spike time series`;
- `detection boundary spiked covariance dependent observations time series minimax`;
- `information theoretic lower bound factor number time series weak factor`;
- `minimax testing number of factors dynamic factor model time series rank`;
- `weak serial factor detection boundary lag covariance operator`.

Rejected hits included static approximate-factor tests, high-dimensional white-noise tests, change-point detection in spectral densities, and sparse PCA/spiked-covariance detection. They change the experiment, hypothesis, or signal metric and do not prove a rank \(r\) versus \(r-1\) boundary for a squared nonzero-lag operator built from dependent generated coordinates.

**Terminal conclusion:** no applicable minimax or information-theoretic lower bound was found after documented search. The internal rates

\[
s_{\min}\gg n^{-3/28}
\quad\text{(generic robust sufficient branch)},
\qquad
s_{\min}\gg n^{-1/8}
\quad\text{(oracle root-\(n\) sufficient branch)}
\]

remain sufficient translations of AR1-THR. They are not necessity, minimax, or optimality statements.

## 7. LIT-R5 — estimated-coordinate nuisance

### 7.1 A Euclidean generated-row precedent

Chang, Guo and Yao observe \(y_t\) and regressors \(z_t\), estimate a regression matrix \(D\), form residuals

\[
\widehat\eta_t=y_t-\widehat D z_t,
\]

and only then build the lag-covariance operator used for factor recovery. Their Theorems 2.1–2.3 show that the loading-space rate can be adaptive to the unknown first-stage regression coefficient under their assumptions; Theorem 2.4 gives the consistent ridged factor-number selector.

This is a genuine two-stage factor/rank precedent, not merely a generic Davis–Kahan citation. It proves that a generated-row nuisance can be propagated through a lag operator. Its nuisance is a Euclidean regression residual, however, not a locally estimated manifold centre or transported frame.

### 7.2 A geometric generated-coordinate precedent

Lin and Yao estimate a time-varying Fréchet mean curve \(\widehat\mu\), map each manifold-valued trajectory with \(\operatorname{Log}_{\widehat\mu}\), and define a sample covariance operator on the random tensor Hilbert space along \(\widehat\mu\). They intrinsically transport that operator and its eigenfunctions to the population space along \(\mu\). Their Theorem 7 proves

\[
\|\widehat C\ominus_\Phi C\|_{HS}^2=O_p(n^{-1})
\]

and corresponding eigenstructure bounds under their mean and moment assumptions.

This is the closest geometric precedent for the principle

\[
\text{estimate nuisance geometry}
\longrightarrow
\text{transport to a common space}
\longrightarrow
\text{bound operator perturbation relative to a spectral margin}.
\]

But their data are i.i.d. manifold-valued functions, not one locally stationary time series. Their parallel transport compares the estimated and population mean curves pointwise; it does not construct a sampled centre polygon, recursively transport each time-series residual to one reference tangent space, or form nonzero-lag row products.

### 7.3 Exact status of HD-E

The parent adds a fixed-centre manifold time-series nuisance layer. Lin–Yao add a moving mean-curve covariance layer. Chang–Guo–Yao add a generated-residual lag-factor layer. No checked source combines all three components needed by HD-E:

\[
\text{moving local Fréchet centre}
+\text{shared polygon/frame transport}
+\text{dependent lag-rank operator}.
\]

Accordingly, it is safe to say **"the perturbation strategy has clear precedents in adjacent two-stage and Riemannian operator problems; the complete RFD nuisance composition is proved internally here."** It is not safe to say **"two-stage geometric lag-rank theory is standard"** or **"this is the first such theorem."**

## 8. LIT-R6 — exact parent-paper scope

The local PDF and the arXiv record support the following bounded comparison.

1. **Model.** The parent uses a time-invariant population Fréchet centre and fixed tangent-space loading map, while estimating the global centre and resulting tangent coordinates from the data. Dynamic information is extracted from nonzero-lag covariance products of those log-mapped rows.
2. **Eq. (5).** The selector is the raw ratio
   \[
   \widehat r
   =\arg\min_{1\le i\le R}
   \frac{\widehat\lambda_{i+1}}{\widehat\lambda_i}.
   \]
   Its candidate set does not include rank zero.
3. **Proposition 3.** Under the stated conditions, signal eigenvalues have root-\(n\) estimation error and null eigenvalues are \(O_p(n^{-1})\); the smallest signal is bounded through the paper's lag-signal condition. These statements control the true boundary ratio but do not, by themselves, compare it with every post-rank ratio.
4. **Dependence.** Conditions (13)–(14) are broader than fixed \(m_0\)-dependence: they impose trace-normalised algebraic decay with exponent greater than one, uniformly over the local centre set; finite dependence is a special case.
5. **Example 1 and dimension.** Under geometric \(\alpha\)-mixing, the concrete concentration verification allows \(p=o(n^\gamma/\log n)\) for \(\gamma<1/2\). Under algebraic mixing, that verification is only given for fixed \(p\). Thus the theorem's displayed rate can be dimension-free while the supplied producer is not arbitrary-growing-\(p\).
6. **Table 2.** Across 300 replications, the raw ratio selects correctly roughly 57–61% at \(n=50\), 83–91% at \(n=100\), and 98–99% at \(n=200\), depending on the reported design.

The publication-safe correction is:

> Proposition 3 controls the signal eigenvalues and the order of the null eigenvalues, but those displayed rates alone do not establish consistency of the unrestricted raw-ratio argmin in Eq. (5), because ratios wholly within the empirical null spectrum require separate control. This is a non-derivability statement, not evidence that the selector fails in the paper's designs; Table 2 reports strong finite-sample performance.

## 9. Theorem-by-theorem project map

| Internal node | External producer or comparison | What enters the project | What remains internal |
|---|---|---|---|
| **AR1-SIG** | Lam–Yao's squared lag-covariance matrix; Bhatia–Yao–Ziegelmann's Hilbert operator | The population range/eigenspace mechanism | The exact diagonal AR(1) spectrum, \(w^4\) translation, fixed-energy dilution formula, and compatibility with HD-L |
| **AR1-THR** | Bhatia–Yao–Ziegelmann Theorem 3 | Thresholding between vanishing null estimates and fixed positive signals is standard | The exact finite-sample EV window \(d_n^2<\tau_n<\chi_{\min}-\eta_n\), and its weak-amplitude translations |
| **HD1 EV** | Bhatia–Yao–Ziegelmann Theorem 1; generic Weyl perturbation | Squared lag operators can yield faster null eigenvalue rates than signal eigenvalue rates | The row-error assembly, \(d_n^2\) null bound, and \(\eta_n\) producer for estimated RFD coordinates |
| **HD1 TAU** | Functional threshold and Hallin–Liška penalty separation are analogues | A selector scale must lie above noise and below signal | The three explicit relations \(d_n^2=o_p(\tau_n)\), \(\tau_n=o(\Delta_n)\), \(\eta_n=o_p(\Delta_n)\) for this operator |
| **HD-E** | Chang–Guo–Yao generated residuals; Lin–Yao estimated mean curve and transported covariance | Two-stage nuisance-to-operator perturbation is established in adjacent settings | Moving local means, polygon transport, frame error, dependence, and their composed dimension-uniform bound |
| **P-RATIO** | Lam–Yao Remark 2(ii); Chang–Guo–Yao Theorem 2.4; Caro–Peña A5/Proposition 1 | Raw ratios need post-rank control; ridging or explicit adjacent-spectrum conditions can supply it | The concrete diagonal counterexample showing the parent's displayed rates alone are insufficient |

## 10. Rejected near-matches and search coverage

| Near-match | Why it was rejected as a direct producer |
|---|---|
| Sparse spiked covariance rank detection (Cai–Ma–Wu) | Independent Gaussian vectors, static covariance spike, sparse support; no serial lag experiment or generated geometric coordinates. |
| General dynamic-factor information criteria (Hallin–Liška) | Pervasive spectral eigenvalues diverge with cross-section and the criterion integrates frequency-domain residual spectra; this is not bounded-energy lag-row thresholding. |
| Lam–Yao weak factors | Weakness is defined through loading norm/pervasiveness as \(p\) grows, not by shrinking marginal factor amplitude under a fixed energy budget. |
| Caro–Peña pooled-covariance raw ratio | Their consistency proposition assumes the decisive adjacent-spectrum separation in A5; it does not derive a selector theorem from HD1's two displayed eigenvalue orders alone. |
| Static covariance eigenvalue-ratio tests, including Ahn–Horenstein | They use contemporaneous covariance spikes in approximate factor models, not the nonzero-lag squared operator under exact lag-noise separation. |
| High-dimensional white-noise and serial-correlation tests | They test whether a vector process or component is white noise, not rank \(r\) versus \(r-1\) with the RFD parameter class and loss. |
| Riemannian FPCA (Dai–Müller; Lin–Yao) | It estimates covariance eigenstructure around a mean curve across independent functions; it does not select persistent time-series factor rank from lag products. Lin–Yao remains a valid nuisance comparison. |
| Generic Davis–Kahan/Weyl perturbation | These convert an operator error into spectral/subspace error once an operator bound exists. They do not prove the RFD mean/frame/polygon operator bound. |

Search coverage included author/journal versions and citation chains for the nine primary sources in Section 2; arXiv and DOI searches for `lag covariance operator`, `dynamic factor rank`, `weak factor`, `eigenvalue threshold`, `ridged eigenvalue ratio`, `generated residual factor number`, `estimated mean manifold covariance`, and the lower-bound query families documented in §6.3. Search engines were used only for discovery; theorem claims above were checked in the primary papers. No inaccessible or abstract-only source is used as a theorem producer.

## 11. LIT-R7 — publication-safe positioning

### 11.1 Paper 1 may call these standard and cite them

- Identification of a dynamic/loading space by eigenanalysis of a sum of squared nonzero-lag covariance matrices or operators: Lam–Yao; Bhatia–Yao–Ziegelmann.
- Faster convergence of empirical null eigenvalues than nonzero eigenvalues for a squared lag operator in the classical functional setting: Bhatia–Yao–Ziegelmann.
- Consistent factor-number selection by a vanishing eigenvalue threshold under a suitable signal/noise separation: Bhatia–Yao–Ziegelmann.
- Consistent dynamic-factor selection by penalised spectral criteria under pervasive spectral separation: Hallin–Liška.
- Consistent ridged adjacent-eigenvalue ratios under explicit null, signal, and competing-ratio control: Chang–Guo–Yao.
- Intrinsic comparison of covariance operators and eigenfunctions after estimating a Riemannian mean curve by parallel transport: Lin–Yao.

### 11.2 These are internally proved adaptations

- The exact AR(1) formula \(s_j^4\sum_h\rho_j^{2h}\) for the project's lag operator.
- The \(w^4\) weak-tail attenuation and the separate fixed-total-energy rank-dilution denominator.
- The exact threshold window \(d_n^2<\tau_n<\lambda_r(\mathbb L)-\eta_n\) under EV, together with the TAU producers.
- Propagation of the moving-centre, base-log, polygon transport, frame, dependence, and dimension-uniform nuisance channels into HD-E.
- P-RATIO's diagonal counterexample and its correction to the inference drawn from the parent's displayed rates.

### 11.3 Paper 1 must not say these are novel, optimal, necessary, or universal

- Do not call squared-lag loading-space identification novel.
- Do not call \(s_j^4\) the universal weak-factor signal law; it belongs to the specified squared-lag AR(1) route.
- Do not call \(n^{-3/28}\) or \(n^{-1/8}\) minimax detection boundaries; they are sufficient amplitude scales for two internal nuisance branches.
- Do not say raw eigenvalue ratios are inconsistent in general or fail in the parent simulations.
- Do not say thresholding is universally superior to ratios or information criteria.
- Do not say the complete geometric nuisance theorem is the first of its kind. The defensible negative statement is only that this audit found no prior source combining a moving local manifold centre, shared polygon transport, and dependent lag-rank recovery.
- Do not equate Lam–Yao/Hallin–Liška pervasiveness with the project's bounded-energy assumption.

### 11.4 One compact related-work paragraph

> Our factor-space estimator follows the established time-domain strategy of recovering a dynamic loading space from sums of products of nonzero-lag covariance operators, developed for high-dimensional vector series by Lam and Yao (2012) and for functional series by Bhatia, Yao and Ziegelmann (2010). Those works also motivate eigenvalue-based dimension selection, while Hallin and Liška (2007) provide a frequency-domain information-criterion route and Chang, Guo and Yao (2015) prove consistency for a ridged lag-eigenvalue ratio under explicit separation conditions. Our contribution here is not the lag-operator principle itself, but its integration with estimated moving Riemannian centres and frames and the resulting operator-error and threshold conditions. Related Riemannian functional theory controls covariance eigenstructure after estimating and transporting between mean curves (Lin and Yao, 2019), but does not cover the locally stationary polygon-transported lag operator considered here.

### 11.5 One compact theorem note

> **Signal interpretation.** In the independent diagonal AR(1) special case, the squared lag operator has nonzero eigenvalues \(s_j^4\sum_{h\in\mathcal H}\rho_j^{2h}\). The fourth power is caused by taking a lag covariance, which is quadratic in factor amplitude, and then squaring that covariance in the positive lag operator. Combining this identity with EV yields the sufficient threshold window \(d_n^2<\tau_n<\lambda_r(\mathbb L)-\eta_n\). These conditions are sufficient for this estimator; no minimax necessity or selector optimality is claimed.

## 12. Final separation of evidence

### The literature proves

- squared nonzero-lag covariance operators identify dynamic/loading spaces under source-specific factor/noise assumptions;
- classical squared-lag operators can have root-\(n\) signal-eigenvalue error and order-\(n^{-1}\) null eigenvalues;
- thresholds, spectral information criteria, and ridged ratios can consistently select factor number under their respective separation conditions;
- generated Euclidean residuals can feed a lag-factor procedure without changing the loading-space rate under strong assumptions;
- estimated Riemannian mean curves can be accounted for by intrinsic transport when estimating covariance eigenstructure from independent functional observations;
- static i.i.d. sparse covariance-spike rank detection has a sharp minimax boundary, in a different experiment.

### This project proves internally

- AR1-SIG's exact spectrum, weak-tail fourth power, and fixed-energy rank dilution;
- AR1-THR's exact realised threshold window and its sufficient robust/oracle amplitude translations;
- HD1 EV/TAU for the project's empirical lag operator;
- HD-E's complete moving-centre and frame nuisance propagation under its explicit producers;
- P-RATIO's counterexample showing why the parent's displayed rates alone do not prove its raw-ratio argmin claim.

### Unproved, and not consumed by Paper 1

- a minimax or information-theoretic detection boundary for weak serial factors in the RFD dependent generated-coordinate experiment;
- necessity or sharpness of \(s_{\min}\gg n^{-3/28}\) or \(s_{\min}\gg n^{-1/8}\);
- universal superiority or optimal tuning of threshold, ridged-ratio, raw-ratio, or information-criterion selectors;
- an external theorem reproducing the entire moving-centre polygon/frame lag-rank construction;
- equivalence between bounded-energy amplitude weakness and cross-sectional pervasiveness notions.

None of these open literature/theory questions is consumed by the proved Paper 1 theorem. They are boundaries on positioning, not holes in the theorem dependency graph.
