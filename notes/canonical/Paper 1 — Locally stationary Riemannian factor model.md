---
type: idea
title: Paper 1 — Locally stationary Riemannian factor model
aliases:
  - Moving-centre RFM, covariantly constant loadings
  - Paper 1
status: current-spec
verdict: P1-ID is closed by exact identified quotients and impossibility boundaries; the robust and scoped sharper estimation theorems retain their separately adjudicated statuses
last-audited: 2026-08-25 (literal parent/RFD BW parity adjudicated; final scope narrowed to a non-forecast APP-FIN identification illustration)
area:
  - geometry
  - time-series
  - factor-models
tags:
  - idea
  - paper-spec
---

# Paper 1 — Locally stationary Riemannian factor model

> Parent: [[Time-varying Fréchet mean Riemannian factor model]]. The complete robust proof is [[HD1 — growing-dimension Paper 1 proof dossier]]. [[Analytical reconstruction — proof ledger and rebuilt spec]] governs current theorem status. Detailed HD1-A/B/C and APP-A/B/C records are preserved under `Archived/Proof workstreams`; they are proof provenance, not parallel canonical specifications.

## Scientific role

Paper 1 starts from an identification question: why analyse persistent fluctuations around a fixed Fréchet mean without first asking whether that mean moves? The parent assumption (P2) sets the marginal Fréchet mean equal to one fixed \(\mu\) at every time. If a real baseline drifts, the fixed-centre lag operator can superpose that drift with a persistent tangent factor and does not report their split.

The claim is deliberately not that the parent's Factor 1 is spurious. [[P1-ID — centre-drift and factor identification boundary]] now proves the exact boundary: a unique pointwise Fréchet mean is a marginal-law functional; the minimum dynamic loading span is identified up to factor gauge and white-at-zero allocation under the displayed orthogonal-white class; one-path recovery is pointwise but not uniform near frequency zero; weakened references identify a compatible-chart orbit and can change dynamic rank; and a fixed-centre lag row contains the complete drift/factor/cross/noise/geometry superposition. Either, neither, or both components may dominate in an application, and the lag output cannot decide which.

Conditional on an identified or explicitly convention-chosen decomposition, Paper 1 is a dynamic dimension-reduction model with a slowly moving baseline. It estimates a smooth Fréchet-centre path and a small number of serially persistent transported tangent-factor directions. It can be used for interpretation and reconstruction directly. Forecasting additionally requires a model for the extracted factor scores, followed by an Exp-map reconstruction. Paper 1 is therefore not a universal stand-alone forecaster and makes no claim of automatic superiority over direct matrix time-series models.

## Identification preconditions

The estimation theorem targets the declared transported loading space only after the following boundary is fixed.

0. **The centre must be declared deterministic in rescaled time, and that declaration is a convention, not a testable hypothesis.** If the baseline is a latent stochastic process \(C_t\), the marginal Fréchet mean is not the realised centre — in a Hilbert space it is \(\mathbb EC_u\), and in curvature it is not even the Fréchet mean of the mixing-centre law. On the latent class two models with different centre processes and incomparable loading ranges can share every finite-dimensional distribution, so nothing beyond the observed law is identified. Identification is restored **only** by a declared frequency-band separation — a centre-free high band and a factor-free low band — which P1-ID §14.3 proves both necessary and sufficient and which no data can verify. Paper 1 adopts that declaration explicitly; it does not claim to have tested it.
1. Each frozen marginal Fréchet objective has a nonempty singleton argmin, or the paper explicitly changes its target to a minimizer set/selected centre. The centre path \(\mu_n(u)\) is defined **pointwise by construction** as the Fréchet mean of the marginal \(Q_u\); no minimisation over centre *paths* is posed, so no path-to-pointwise reduction is consumed. (Where such an objective **is** posed over whole paths, the reduction is Santoro & Panaretos, arXiv:2310.13764v2, Lemma 1 — cited as comparison. Their *Fréchet mean flow* is a different object, estimated from i.i.d. replicate flows rather than one dependent path; Paper 1 therefore says **moving Fréchet centre** or **centre path** and does not adopt their term. See [[Literature review — external positioning and prior art]] §2.) Every Log uses one declared branch on the almost-sure support. On Bures–Wasserstein this is automatic — and this is a **cited** result, not an internal one: the Fréchet mean of any law charging the full-rank cone exists in the open cone and is unique (Kroshnin–Spokoiny–Suvorikova, *Ann. Appl. Probab.* 31(3) (2021), Theorem 2.1; Santoro & Panaretos, arXiv:2305.15592v3, Theorem 1; empirical case Masarotto–Panaretos–Zemel, *Sankhya A* 81(1) (2019), Corollary 9). See C-AUDIT-11. On spheres and sphere products it can fail, and where the argmin is nonsingleton **no continuous selection exists**; a selector jump of size \(\Delta\) at sample fraction \(\lambda\) injects a rank-one, lag-invariant, bandwidth-insensitive contamination \(\lambda(1-\lambda)\Delta^2\) into **every** lag of the row, which dominates an AR(1) factor at every \(h\ge1\) once \(\lambda(1-\lambda)>\rho/4\).
2. The loading target is the minimum lag-generated space \(\mathcal S_X=\operatorname{ran}\mathbb L_n\), and it equals \(\operatorname{ran}A_n\) exactly when \(Q_n\succ0\). A larger loading matrix includes dynamically silent coordinates and is not identified without an extra convention. "Loading" means the **total dynamic loading**: under a latent stochastic centre it absorbs the centre's own serial dependence, and the centre/factor sub-split inside it is not identified even from the full law.
3. Exact lag factorisation requires temporally white residual noise and both factor–noise cross-lag directions to vanish at every included signed lag. When they do not, the target is the contaminated lag row and its leading space, not a uniquely separated factor space.
4. Full Gaussian FDD identification is only up to the minimum-representation gauge, with a positive-definite factor covariance sequence and positive trace-class residual covariance. Outside a proved full-law class, second-order identification is not latent-law identification. **This limit binds the flagship application** — see the displayed scope limit below.
5. One-path mean recovery is pointwise under the no-zero-frequency-atom condition plus the displayed same-freeze local coupling. No theorem is uniform over persistence approaching frequency zero. The quantitative form is P1-ID §12: the price of persistence is \(\psi^+(nb_n)\), which replaces \((nb_n)^{-1/2}\) in \(\ell_n\), and the admissible window is \(d\in[0,\tfrac12)\) with the headline rate requiring \(d=0\).
6. Any comparison with a fixed-anchor or alternative-reference fit must retain the P1-ID compatible-chart orbit, the nine affine lag terms, and the nonlinear geometry remainder. Rank preservation needs the entire score/observation support on a common injective geodesic or totally geodesic flat. **This is now known to be the exact boundary**: P1-ID §13 proves rank inflation occurs on every manifold with nonzero sectional curvature, with exact witnesses in \(H^2\), AIRM \({\rm SPD}(m)\) and Bures–Wasserstein, so a reference change is not a robustness check. The same applies to a change of *centre convention* — a median- or trimmed-centred refit can report a different factor count for purely geometric reasons.

> **Scope limit (CANON-3) — the exact FDD quotient is Gaussian and the application does not inherit it.** ID-2's classification of the full finite-dimensional-distribution quotient — loading gauge plus every feasible lag-zero allocation, with \(\Gamma_g(h)=R^{-1}\Gamma_f(h)R^{-*}\) for \(h\ne0\) and \(\Gamma_g(0)=R^{-1}\Gamma_f(0)R^{-*}+K\) — holds on the **centred jointly Gaussian minimum-representation class** with iid Gaussian noise independent of the complete factor process. Outside Gaussianity it classifies **second order only**, and ID-0 shows this is not a technicality: the stationary Rademacher three-block process matches iid Rademachers at every covariance lag while differing in a consecutive third moment. Tangent-space log-covariance data is not Gaussian — a realised covariance matrix mapped through \(\operatorname{Log}\) is a nonlinear function of returns — so APP-FIN, APP-NEURO and every covariance application inherit **second-order identification only**. Any claim about the latent factor law, as opposed to the identified span and its lag covariances, is outside the theorem.

> **Scope limit (CANON-4) — evaluation. The loss used to score a forecast is not free, and the natural geometric choice is not admissible.** If a later factor-score model turns RFD's reconstruction into a covariance forecast, that forecast is scored against an ex-post *proxy* — a realised covariance matrix, not the latent conditional mean. [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]] proves that a loss preserves the ranking of forecasts under such a proxy **iff** it is a Bregman divergence in the coordinate in which the proxy is conditionally unbiased, and that a **symmetric** loss can be robust only if it is a fixed Mahalanobis form in that coordinate. Squared Bures–Wasserstein, AIRM and log-Euclidean distances are therefore all inadmissible for scoring — the first two because they are curved, the third because it is flat in the *wrong* coordinate. What a geodesic loss actually rewards is the Fréchet barycentre of the *proxy's* conditional law, which is strictly below the conditional mean: exactly \(\mathbb E[x]-\operatorname{Var}(\sqrt x)\) in the scalar case, and for a Wishart-type proxy exactly \(-\frac{\lambda_i}{M}\big[\frac14+\sum_k\frac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\big]\) per eigenvalue. That distortion is \(\Theta(m/M)\), not \(\Theta(1/M)\), so it grows with the matrix size: at the flagship configuration of \(m=12\) assets and monthly realised covariance from \(M\approx21\) daily returns it is **8.8%–35.9%** under Bures–Wasserstein and **32.9%** under AIRM. A forecaster reporting the correct conditional mean is beaten by one reporting a substantially shrunken covariance.
>
> **Any downstream forecast comparison therefore reports squared Frobenius distance and multivariate QLIKE**, both of which are proxy-robust; QLIKE's *ranking* survives a singular proxy even though its *level* does not. If a geodesic loss is reported for comparability, its induced target is stated and the recalibration of P1-LOSS §4 is applied — for AIRM the scalar \(c=1-\frac{m+1}{2M}\) is exact, for Bures–Wasserstein a scalar correction is only partial. Recalibration restores the **location of the optimum** and never the **ranking robustness**: only the loss class does that. Paper 1's APP-FIN illustration does not rank forecasts; any reconstruction loss is labelled descriptive.
>
> **This is a scope condition on reporting. It changes no estimand, no rate, no assumption, and no application's standing** — the proved separation is P1-LOSS §6, and the only edge into the estimation chain is a \(\Theta(m/M)\) measurement-error contribution to the existing target-defect budget \(\zeta_n\).

If an application cannot verify these conditions, it may still estimate the declared row or sensitivity contrast, but it must not relabel the result as an identified drift/factor decomposition.

## Current scope

Paper 1 now has a nontrivial bounded-total-energy robust theorem for arbitrary ambient $p_n\to\infty$, a conditional root-\(n\) implication under FRAME-2P-U's stronger U2P package, and bounded-tail/expanding-domain high-energy theorems with explicit energy, product, geometry, signal, and gap budgets. The bounded-energy robust core is dimension-free because total tangent energy, finite-memory length, lag count, factor rank, and every geometric differential constant are uniformly bounded. This is a trace-class/function-space regime, not the classical regime where every added coordinate carries order-one noise. FRAME-2P-U has only a fixed-active-curvature padded growing-\(p_n\) witness; a genuinely growing-curvature application remains open.

For a fixed real dataset, the bounded-energy condition is a finite constant and does not forbid using the method. When genuinely new noisy coordinates are added, the proved HE theorem applies only if its complete bounded-tail or truncation/generated-domain phase conditions hold.

For $m_n\times m_n$ SPD observations, the manifold dimension is

$$
p_n=m_n(m_n+1)/2,
$$

not $m_n$. On fixed absolute spectral bands, [[Application map — geometry, symmetry, and rate accelerators]] T-APP-2 now proves the dimension-uniform fixed-order Exp, Log, transport, Hessian, Richardson, connector, and ruled-surface bounds used by HD-G. This closes the former AIRM higher-differential primitive in the project AIRM/Frobenius norms. Spectral conditioning still does not imply bounded total tangent energy, bounded mean length, lag orthogonality, or signal.

## Application-specific branches

The canonical property-first map is [[Application map — geometry, symmetry, and rate accelerators]].

- **Robust arbitrary-\(p_n\) branch — PROVED.** HD-E remains the fallback under bounded total energy and the original explicit assumptions.
- **Flat/common-commuting exact-split oracle branch — PROVED UNDER EXPLICIT ASSUMPTIONS.** In one simply connected convex flat, exact innovation separation conditionally centres the remaining additive linear terms and the non-rigid frame term is zero:
  \[
  d_n=O_p(n^{-1/2}+\ell_n^2+\rho_n),\qquad
  \|\sin\Theta\|_{\rm op}=O_p(n^{-1/2}/\Delta_n)
  \]
  when the displayed defects are \(o(n^{-1/2})\). At \(b_n=n^{-1/7}\), \(a\ge3/7\), \(\ell_n^2=o(n^{-1/2})\).
- **FRAME-2P-U conditional two-path branch — PROVED AS AN U2P IMPLICATION.** Three exactly separated training, validation, and evaluation colours use
  \[
  b_n=n^{-1/7},\qquad M_n\asymp n^{2/7},\qquad
  c_n=n^{-\gamma},\quad \frac16<\gamma<\frac3{14}.
  \]
  The observable evaluation-row derivative from the training polygon toward an independent undersmoothed validation polygon cancels the complete first-order mean/base-log and non-rigid frame errors. Under U2P's generated-tube, Karcher, composed-action, single/double replacement, finite-memory split, mask, GLO, included-lag, and exact-local-law or \(a>1/2\) producers, all uniform in \(p_n\), its post-influence nuisance remainder is \(o_p(n^{-1/2})\) and the corrected row is root-\(n\). The implication permits arbitrary ambient \(p_n\), but the only growing-dimensional witness has fixed active curvature plus flat padding. No growing-size AIRM/BW or growing-active-curvature U2P verification exists. Bounded energy alone does not imply U2P.
- **Known/constant/parametric centre branch — PROVED.** A known centre is immune. A root-\(n\) constant or finite-dimensional parametric centre preserves oracle order but generally enters the first-order law; it is not first-order immunity.
- **Physical-dependence branch — PROVED.** Uniform summable Hilbert \(L^2\) and essential-sup innovation effects replace fixed memory in the robust G1/oracle-row chain. Exact cancellation under infinite memory remains conditional on a joint row coupling or conditional physical-dependence theorem.
- **Structured signed growing-\(p_n\) mean — PROVED UNDER EXPLICIT ASSUMPTIONS.** Deterministic, scalar-plus-Hilbert–Schmidt, and controlled block-scalar Hessians avoid the operator sphere net. This covers flat/common flats and bounded constant-negative-curvature tubes, but not unrestricted full AIRM SPD. Faster mean convergence alone does not imply oracle loading.

## Completed extensions and remaining boundary

### Growing energy and pervasive signal

Let \(R_n=\sup_t\|Y_{t,n}\|\to\infty\). Under the proved bounded-tail/generated-domain package, the centre and frame are estimated separately and the feasible observation error is

\[
q_{R,n}\lesssim
L_{\log,n}\{r_{\mu,n}+K_{\mu,n}M_n^{-2}\}
+r_{F,n}\{\mathcal E_{2,n}+L_{\log,n}r_{\mu,n}\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\]

With variance-sensitive product rate \(\omega_n\),

\[
d_n\lesssim \omega_n+\sqrt{h_{0,n}}
\{2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2\}
+\zeta_n+\rho_{{\rm mask},n}+\rho_{{\rm disc},n},
\]

and the loading numerator is \(2A_{2,n}d_n+d_n^2\). Sufficient fixed-gap envelope windows are \(\rho<3/13\) in a flat/rigid frame and \(\rho<3/20\) for the generic curved frame when \(R_n=n^\rho\), with the displayed local-stationarity competitors. A concrete pervasive model has \(R_n\asymp\sqrt{p_n}\), \(A_{2,n}\asymp p_n\), and \(\Delta_n\asymp p_n^2\), so the exact assembly/gap ratio remains consistent. Normalisation is allowed only after recomputing the scientific estimand and gap.

For unbounded observations, the proved expanding-domain route clips only for analysis, proves the clipped and original samples coincide with probability \(1-o(1)\), and pays explicit score and lag-product tail biases. A sub-Weibull sufficient choice is

\[
T_n=K_n\{c\log N_n\}^{1/\alpha},\qquad c>1,
\]

subject to the displayed expanding-domain geometry and actual-gap conditions. This is not a minimal-tail theorem.

### Moving-centre Bures–Wasserstein covariance dynamics

The parent covariance application uses Bures–Wasserstein geometry, not AIRM. The fixed-size theorem is now closed on full-rank SPD for a local/regularized estimator: constrained positive stage means, a complete generated-domain membership test with fallback, quotient Levi–Civita polygonal transport, and a reconstruction full-rank safeguard. Under its fixed-size bounded-energy, dependence, target, and gap assumptions,

\[
d_n=O_p(n^{-1/2}+\ell_n),\qquad
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
=O_p\!\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right).
\]

The original unsafeguarded global estimator is retracted. A global/rank-changing PSD theorem is disproved. On fixed spectral, polar, Exp, normal-pair, and path-length margins, the noncommuting quotient calculus is proved uniformly in matrix size by an explicit recurrence-defined \(C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)\).

The recorded fixed-size BW experiment is a qualified empirical check of this
theorem boundary, not a proof. Its 496 frozen tasks completed with no ordinary
error or failed verdict; all 400 safe fit rows stayed within the declared
generated domain. Commuting/noncommuting centre exponents were \(0.41/0.42\),
polygon exponents \(0.58/0.58\), and loading exponents \(0.55/0.57\); regular
scientific-cell median loading-projector error at \(n=8192\) was
\(0.0105\)–\(0.0191\). Operator assembly and beyond-rank null bounds held, but
the conservative sufficient operator-error-below-gap certificate was not
uniform at finite \(n\). All rank-positive recovery figures use the known
synthetic rank. Selector outputs are diagnostic only, and Paper 1 claims no
automatic rank selection from this campaign. The signed-exit, rank-loss,
near-identical, incompatible-Exp, dispersion, and lower-margin controls all
produced their declared fallback, rejection, finite, or boundary outcome.

There is also a restricted shrinking-margin theorem. It requires a complete fractional-normal generated domain with strict population score-pair slack, support/energy \(O(\sqrt{\alpha_n})\), fractional-normal PF cells, and all object-count, path, lag, target, and actual-gap conditions left explicit. The active local coefficients are \(K_B=O(1+\alpha_n^{-1})\), \(K_{L2}=O(\alpha_n^{-1/2})\), and \(K_F=O(\alpha_n^{-1})\), while score coercivity and first local Log/Richardson derivatives stay \(O(1)\). A conservative rank-one corollary with \(\alpha_n\asymp m_n^{-A}\), \(m_n=n^x\), has the sufficient window \(0<x<3/(5A)\). This is not a sharp universal ceiling; a self-similar fixed active block permits arbitrary polynomial inactive dimension. Fixed/growing tangent energy is incompatible with this shrinking normal-pair branch. The fixed-basis diagonal/root-coordinate branch remains a separate flat HE intersection; it does not cover moving eigenvectors.

## Model and estimator

$$
X_{t,n}=\operatorname{Exp}_{\mu_n(u_t)}
\left[\mathcal P^{\mu_n}_{u_0\to u_t}A_nf_{t,n}+\delta_{t,n}\right],
\qquad
Y_{t,n}=\mathcal P^{\mu_n}_{u_t\to u_0}\log_{\mu_n(u_t)}X_{t,n}
=A_nf_{t,n}+\varepsilon_{t,n}.
$$

Here $A_n^*A_n=I_r$, with fixed $r$, and $\|Y_{t,n}\|\le R$ almost surely uniformly in $n,p_n$. The row and its smooth proxy laws are fixed-$m_0$-dependent. Baseline level local stationarity is the \(L^2\) coupling \(\sup_{t,n}\|d(X_{t,n},X_t^{(u_t,n)})\|_{L^2}=O(n^{-a})\). The optional continuous-\(u\) supremum theorem additionally uses the essential-sup version. Almost-sure tube containment is a separate support assumption.

The mean estimator uses three nonnegative one-sided scale kernels,

$$
c=(1,1/2,1/4),\qquad \lambda=(1/3,-2,8/3),
$$

and combines their positive barycentres by the Exp/Log Richardson map. Kernels and their first derivatives vanish at support endpoints. Forward and backward estimators are blended on a fixed-width interior overlap.

For the factor step, choose $M_n\asymp\ell_n^{-2/3}$ deterministic mean-grid cells, where

$$
\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
$$

Join estimated mean vertices by geodesic chords and parallel-transport along the resulting polygon. This is the canonical feasible frame. Its typed cellwise holonomy proof uses only level/grid RMS G1, and therefore bypasses G1′ in the final theorem.

## Dimension-free mean results

Under the uniform geometry, bounded-total-energy, fixed-memory, smooth-law, and bandwidth assumptions,

$$
\sup_u d(\hat\mu_n^{(3)}(u),\mu_n(u))
=O_p\!\left(b_n^3+n^{-a}+n^{-1}+\sqrt{\frac{\log n}{nb_n}}\right),
$$

$$
\|\log_{\mu_n}\hat\mu_n^{(3)}\|_{L^2}=O_p(\ell_n),
$$

and the same $O_p(\ell_n)$ RMS bound holds on any deterministic coarse grid. Concentration is performed directly in the tangent Hilbert space; there is no $p_n$-dimensional net.

The separately proved derivative result under level-only local stationarity is

$$
\|\nabla_u\log_{\mu_n}\hat\mu_n^{(3)}\|_{L^2}
=O_p\!\left(b_n^3+(nb_n^3)^{-1/2}+n^{-a}/b_n+(nb_n)^{-1}\right).
$$

The $n^{-a}/b_n$ term is sharp. It improves to $n^{-a}$ only under the explicit $C^1$ weighted score-discrepancy condition in HD1-A. A width-$b_n$ boundary blend is retracted because it pays $b_n^{5/2}$ in derivative $L^2$.

## Signal and eigengap

Use different symbols:

$$
s_n=\max_{1\le h\le h_0}\sigma_r(C_{f,n}(h)),
\qquad
\Delta_n=\lambda_r(\mathbb L_n)-\lambda_{r+1}(\mathbb L_n),
$$

where

$$
\Gamma_n(h)=A_nC_{f,n}(h)A_n^*,
\qquad
\mathbb L_n=\sum_{h=1}^{h_0}\Gamma_n(h)\Gamma_n(h)^*.
$$

The displayed factorisation requires zero idiosyncratic lag covariance and zero factor–noise cross covariances at included lags. If
\(Q_n=\sum_hC_{f,n}(h)C_{f,n}(h)^*\succ0\), then

$$
\operatorname{ran}\mathbb L_n=\operatorname{ran}A_n,
\qquad
\Delta_n=\lambda_{\min}(Q_n).
$$

If one included lag is full rank, $\Delta_n\ge s_n^2$. This condition is sufficient, not necessary: complementary rank-deficient lags can make $Q_n$ full rank even when $s_n=0$.

## Feasible lag operator and loading theorem

After endpoint connectors, the polygonal centre/frame gives feasible observation RMS error $q_n=O_p(\ell_n)$. For fixed $m_0,h_0$, Hilbert–Schmidt concentration of the oracle lag products and a pathwise feasible-versus-oracle expansion give

$$
d_n:=\left\{\sum_{h=1}^{h_0}
\|\hat\Gamma_n(h)-\Gamma_n(h)\|_{\rm op}^2\right\}^{1/2}
=O_p(n^{-1/2}+\ell_n).
$$

With $A_{2,n}=(\sum_h\|\Gamma_n(h)\|_{\rm op}^2)^{1/2}$,

$$
\|\hat{\mathbb L}_n-\mathbb L_n\|_{\rm op}
\le 2A_{2,n}d_n+d_n^2=:\eta_n.
$$

If included-lag factorisation is only approximate, write
\[
\Gamma_n(h)=\Gamma_n^0(h)+D_n(h),\qquad
\zeta_n=\left\{\sum_h\|D_n(h)\|_{\rm op}^2\right\}^{1/2}.
\]
Then the row error to the ideal factor target is \(\bar d_n=d_n+\zeta_n\) and the honest loading numerator is
\[
2A_{2,n}^0\bar d_n+\bar d_n^2.
\]
Thus the general robust rate is \(O_p((n^{-1/2}+\ell_n+\zeta_n)/\Delta_n^0)\); the shorter display below is its exact-target \(\zeta_n=0\) case.

No cross-fitting or quadratic mean cancellation is consumed by this robust theorem. Cross-fitting alone is insufficient on curved manifolds: the random Hessian \(H(q,X)\) can leave a first-order recentering term.

The separate FRAME-2P-U estimator uses fitted training vertices \(\widehat q^T\), independent validation vertices \(\check q^V\), and one masked evaluation-row functional:

\[
d_j^{TV}=\log_{\widehat q_j^T}\check q_j^V,
\qquad
\widehat{\mathfrak T}^{2p}_{T,V,E}
=\widehat{\mathfrak T}_E(\widehat q^T)
+D\widehat{\mathfrak T}_E(\widehat q^T)[d^{TV}],
\]

averaged over cyclic colour assignments. Its expansion is

\[
\widehat{\mathfrak T}^{2p}_n-\mathfrak T_n
=\mathbb G_{E,n}[Z_n]+\mathbb G_{V,n}[\varphi_{n,c}]+R_n,
\qquad \|R_n\|_{\oplus HS}=o_p(n^{-1/2}),
\]

where both displayed influence rows are \(O_p(n^{-1/2})\). The validation influence is part of the leading sampling law, not the nuisance remainder. Common rigid gauge changes conjugate the whole corrected row; only time-varying non-rigid frame motion is corrected additively. Consequently, if

\[
2A_{2,n}d_n^{db}+(d_n^{db})^2=o_p(\Delta_n),
\]

then

\[
\|\sin\Theta(\widehat E_n^{db},E_n)\|_{op}
=O_p(n^{-1/2}/\Delta_n),
\qquad
\widehat\lambda_{r+1,n}^{db}=O_p(n^{-1}).
\]

This theorem does not validate the same-band score/Richardson correction: that route generically retains an \(n^{-3/7}\) curved bias and is disproved. Direct frame/\(\Omega\) plug-in remains conditional on an extra frame producer, while an invariant-only redesign changes the estimand. The extra validation influence is leading root-\(n\) noise, so the result has oracle rate order but is not oracle-equivalent and generally has a different asymptotic variance.

> **Final robust loading theorem (exact-target case \(\zeta_n=0\)).** If $\eta_n=o_p(\Delta_n)$, then for arbitrary $p_n\to\infty$ inside the bounded-total-energy class,
>
> $$
> \boxed{
> \|\sin\Theta(\hat E_n,E_n)\|_{\rm op}
> =O_p\!\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right).}
> $$

Only after proving $\Delta_n\ge s_n^2$ may the denominator be weakened to $s_n^2$. Davis–Kahan pays $\Delta_n^{-1}$, not $\Delta_n^{-2}$.

For $b_n=n^{-\alpha}$, the level rate is

$$
\ell_n=O\{n^{-3\alpha}+n^{-(1-\alpha)/2}+n^{-a}\}.
$$

The robust optimum is $\alpha=1/7$, giving $n^{-3/7}$ when $a\ge3/7$. The former $b_n=n^{-1/5}$ remains admissible and gives $n^{-2/5}$ when $a\ge2/5$. There is no restriction on $p_n$ beyond the uniform total-energy and geometry primitives.

## Factor-number theorem

Let the lag row operator be $\mathcal G=[\Gamma_1\ \cdots\ \Gamma_{h_0}]$. Since $\mathbb L=\mathcal G\mathcal G^*$ and $\operatorname{rank}\mathcal G=r$, singular-value min–max gives

$$
\hat\lambda_{r+1,n}\le d_n^2,
\qquad
|\hat\lambda_{j,n}-\lambda_{j,n}|\le\eta_n\quad(j\le r).
$$

Thus the beyond-rank square is proved at the lag-row level; it does not follow from Weyl alone. If

$$
d_n^2=o_p(\tau_n),\qquad \tau_n=o(\Delta_n),\qquad \eta_n=o_p(\Delta_n),
$$

then the threshold selector

$$
\hat r_n=\#\{j:\hat\lambda_{j,n}>\tau_n\}
$$

is consistent. A ridge-ratio selector is also consistent under a lower bound on adjacent nonzero population eigenvalue ratios. Consistency of the raw ratio **does not follow from the displayed rates alone**: for $\hat{\mathbb L}=\operatorname{diag}(1,d_n^2,0)$, the signal and null eigenvalues have the claimed orders but minimising consecutive unregularised ratios selects rank two.

### Exact AR(1) signal calibration

The abstract gap condition has a direct interpretation on the independent
stationary AR(1) DGP. If factor \(j\) has marginal standard deviation \(s_j\)
and persistence \(\rho_j\), the isometric-loading, exact-HD-L subclass has

$$
\lambda_j(\mathbb L)
=s_j^4\sum_{h=1}^{h_0}\rho_j^{2h}
$$

up to decreasing rearrangement. Therefore the threshold selector is exactly
correct on the finite-sample event

$$
d_n^2<\tau_n<
\min_j\left\{s_j^4\sum_{h=1}^{h_0}\rho_j^{2h}\right\}-\eta_n.
$$

This makes the weak-factor boundary explicit: multiplying one factor's
marginal amplitude by \(w\) multiplies its lag-operator eigenvalue by
\(w^4\). Geometry enters this decision only through its contribution to
\(d_n\) and \(\eta_n\); if the population signal is already below
\(\tau_n\), an oracle centre and frame cannot rescue this threshold rule.
The proof, fixed-total-energy dilution formula, and robust/oracle rate
translations are [[P1-RANK — AR1 signal strength and threshold boundary]].
They are sufficient selector boundaries, not minimax impossibility or
selector-optimality claims.

The synthetic loading and reconstruction headlines do not depend on selecting
rank: they supply the known DGP rank so centre, frame, lag, and loading errors
are not confounded with weak-factor detectability. The completed selector sweep
remains supporting evidence that feasible geometry created no visible extra
rank boundary on its controlled cells. APP-FIN has no true-rank labels. Paper 1
therefore fixes \(r=2\), matching the parent's published forecast specification
without presenting it as recovered truth. Ranks \(1,\ldots,15\) are a labelled
sensitivity envelope only. Predictive rank selection remains in
[[Future application programme — factor scores, predictive rank, and online RFD]].

The use of a squared nonzero-lag covariance operator to identify a dynamic
factor space is established time-domain ancestry, not a novelty claim:
Lam and Yao (2012) give the finite-dimensional construction, while Bhatia,
Yao and Ziegelmann (2010) give its functional/Hilbert-space analogue and a
thresholded factor-number rule. Hallin and Liška (2007) provide the main
frequency-domain information-criterion comparator, and Chang, Guo and Yao
(2015) provide generated-residual and ridged-ratio precedent. Paper 1's
contribution at this step is the integration of that lag signal with an
estimated moving Fréchet centre, polygonal frame and their complete nuisance
budget; the independent-AR(1) display above is the exact calibration of the
project's theorem, not a claim that real factors must be AR(1). No applicable
minimax lower bound for this weak-serial-factor boundary was located, so the
display is not labelled optimal or necessary. The source-by-source scope is
recorded in [[References and external claim audit]].

### Remark P-RATIO — correction to the parent paper's Eq. (5) justification

The parent uses $\widehat r=\arg\min_{1\le i\le R}\widehat\lambda_{i+1}/\widehat\lambda_i$ in Eq. (5) and says Proposition 3 justifies it. The counterexample above disproves that implication from Proposition 3's displayed rates without extra post-rank separation. It does **not** show practical failure: the parent's Table 2 reports selection above 80% at $n=100$ and about 100% at $n=200$ in its simulated designs. Paper 1 therefore uses the proved threshold or ridged-ratio selector and treats the raw ratio as an empirical comparator, not a theorem-backed selector under rates alone.

## Parent comparison

Huang, Chen and Chen (2026), *A Riemannian Factor Model for Manifold-Valued Time Series*, arXiv:2607.28385v1, assume in (P2) that the Fréchet mean of \(Q_t\) exists and equals the same \(\mu\) for every \(t\). Their model therefore studies dynamics around a fixed centre; it does not estimate a drift/factor decomposition. Paper 1 treats that separation as an identification problem rather than calling the parent's empirical leading factor erroneous.

### Corollary P-DRIFT — when the parent's fixed-centre fit is valid under centre drift

ID-6 is worded defensively and never states the positive result in citable form. It is stated here, and it is a repackaging of ID-5's proved consequences, not a new theorem.

> **Corollary P-DRIFT.** Let the parent's fixed-centre RFM be fitted, with anchor \(c_0\) and one declared Log branch, to data generated by a moving-centre model with deterministic centre path \(\mu(u)\), and let \(d_t=\log_{c_0}\mu(u_t)\) with \(D=\overline{\operatorname{span}}\{d_t\}\) and \(M_d\) the lag-invariant drift contribution. Suppose the ID-5 conditions hold — pointwise factor/noise centring, both factor–noise cross-lag directions zero, idiosyncratic whiteness at every included lag — so that \(S_n(h)=D_{d,n}(h)+A\Gamma_{f,n}(h)A^*\) with the curved remainder \(g_{t,n}\) absorbed or budgeted. Then:
>
> 1. **(aligned drift)** if \(D\subseteq\mathcal S_X\), the fitted leading \(r\)-space is consistent for the same \(\mathcal S_X\) and the parent's Theorem 2 rate applies verbatim. Drift adds no outside direction. It may still change the eigenstructure inside \(\mathcal S_X\), so the *ordering and interpretation* of individual factors is not protected even here;
> 2. **(small drift)** if \(\|D_{d,n}\|\) is \(O(n^{-1/2}+\ell_n)\) in the lag-row norm, drift is absorbed into the existing target-defect budget \(\zeta_n\) and the rate is unchanged with denominator \(\Delta_n^0\);
> 3. **(orthogonal drift)** if \(D\perp\mathcal S_X\), the fitted row has range \(\mathcal S_X\oplus D\) and the recovered dimension is inflated by exactly \(\dim P_{\mathcal S_X^\perp}D\) — a clean, predictable, and detectable failure;
> 4. **(partial drift)** under factor-complete lag contrasts the range is \(\mathcal S_X+D\) with \(\dim P_{\mathcal S_X^\perp}D\) added directions; otherwise cancellation between drift and factor is possible and the fitted row reports neither.
>
> In cases 1 and 2 the parent's conclusions survive centre drift unchanged. In case 3 the damage is exactly quantified. Only case 4 is genuinely uninformative.

This is the honest positive statement, and it is why P1-ID does not license calling the parent's leading empirical factor spurious: under aligned or small drift the parent is simply right, and no fixed-centre output can tell an analyst which case obtains without the identifying assumptions.

### Remark P-DRIFT-\(\nu\) — the downstream static-centre phase boundary

For the controlled family \(\mu_\nu(u)=\operatorname{Exp}_{\mu_0}\{\nu g(u)V\}\), \(\nu\) is a clean experimental axis from a genuinely static centre at \(\nu=0\) to increasing drift. The intrinsic report is the corresponding path length or energy. P1-ID §17 defines a target- and risk-specific crossover between a fixed-centre and moving-centre estimator and explains why no universal threshold exists.

In the clean flat/orthogonal/pointwise-centred branch, drift displacement is \(O(\nu)\) and its lag row is \(O(\nu^2)\). Balancing that row against \(e_n=n^{-1/2}+\ell_n\) gives the conditional candidate \(\nu_{\rm est}^\star\asymp e_n^{1/2}\), hence \(n^{-3/14}\) when short-memory \(\ell_n\asymp n^{-3/7}\) dominates. This exponent is not exported to curved, partial, or non-centred regimes: a surviving cross/base-change term can be \(O(\nu)\), aligned drift need not damage the loading span, and forecast risk has its own loss- and horizon-dependent crossover. N-18c is the numerical phase-diagram diagnostic; it cannot by itself identify empirical drift or prove the exponent.

Their Theorem 2 and Proposition 3 use \(\kappa\) for a factor-lag singular-value strength, obtain \(O_p(1/(\kappa^2\sqrt n))\), and state \(\lambda_r\ge\kappa^2\). Their P1 bounded-radius condition explicitly implies total factor and noise energy cannot diverge with \(p\); their theorem is not a classical pervasive-energy result. Their short-memory conditions (13)--(14) are broader than fixed finite dependence: they require trace-normalised algebraic covariance decay with \(C_\xi\) uniformly bounded and a uniform lower bound on \(d_\xi\) strictly greater than one near \(\mu\), and identify finite \(m\)-dependence as a special case. Theorem 2 is dimension-free as stated, but Example 1 verifies P3 under geometric \(\alpha\)-mixing only for \(p=o(n^\gamma/\log n)\), \(0<\gamma<1/2\), and under algebraic mixing only for fixed \(p\). The robust moving-centre theorem matches the bounded-total-energy/arbitrary-ambient-dimension character but has a slower fallback rate and presently uses fixed finite memory. Conditional FRAME-2P-U matches the root-\(n\) rate order under U2P and three colours; its added validation influence prevents a claim of oracle limit-law equivalence. The parent's realised-covariance APP-FIN and public implementation provide the numerical reproduction baseline. See [[References and external claim audit]].

## Current numerical standing and final empirical gates

The AIRM Paper 1 evidence is frozen at the experiment level. The centre-rate,
bounded-energy, selector, eleven-cell control, 15-cell orientation phase, and
low-sample amplitude runs are complete. They support accurate loading-space
recovery and moving-centre reconstruction on the declared synthetic class,
show no gain on the fixed-centre placebo, and localize low-$n$ factor-score
loss to the feasible centre/Log/polygon/frame row bundle rather than loading
directions. The compact fixed-size BW campaign is also complete with the
qualified fixed-rank verdict stated above. The literal parent comparison then
completed all 576 common BW draws without failure. Parent RFM won every
home/fixed/aligned draw; RFD won every mixed/orthogonal/curved draw. At
\(n=8192\), RFD reduced median latent-signal RMS by 42.5%, 57.8%, and 55.8% in
the latter regimes, while the penalty in the former regimes had shrunk to about
1%. The aligned result is the identification boundary in numerical form: RFD
reduced centre-path error by 60.5% but remained 1% worse in reconstruction,
because drift inside the loading space can be absorbed as common factor
movement. These are reconstruction and identification evidence, not a
forecasting theorem or a real-data dominance claim. Full adjudication:
`results/final/parent_rfd_bw_parity_adjudication/report.md`.

The sole remaining Paper 1 empirical gate is deliberately narrow: on the
rebuilt 240-month, 12-stock APP-FIN BW panel, fit literal parent RFM and RFD at
fixed \(r=2\); quantify intrinsic centre motion, its projection inside and
outside the parent loading span, loading/reconstruction sensitivity, Factor
1/VIX interpretation, and all numerical/theorem diagnostics. This is an
application illustration of whether the fixed-centre assumption is empirically
consequential. It cannot establish predictive superiority, structural factor
amplitudes, or a true financial rank.

The full growing-size BW, shrinking-margin BW, FRAME-2P-U application,
exhaustive phase, selector-efficiency, factor-score filtering, predictive-rank,
future-centre, and forecasting programmes are not prerequisites. A negative
APP-FIN result narrows the empirical claim; it
does not reopen P1-ID or any proved assumption-to-conclusion theorem.

## Claims excluded from Paper 1

- fixed \(p\) as the final scope;
- \(E_n=\operatorname{ran}A_n\) as the estimand without the minimum-representation condition \(Q_n\succ0\); the estimand is \(\mathcal S_{X,n}=\operatorname{ran}\mathbb L_n\);
- a centre/factor decomposition presented as identified when the baseline may be a latent stochastic process; on that class the declared frequency-band separation is a convention and must be labelled one;
- a moving-reference, alternative-anchor, or alternative-centre-convention refit presented as a robustness check on the factor count, when reference-dependent rank inflation is a theorem in every curved geometry the project uses;
- a selector through a nonsingleton Fréchet argmin presented as harmless; it manufactures lag-invariant drift of size \(\lambda(1-\lambda)\Delta^2\) at every lag;
- an APP-FIN online predictive-rank path presented as identification of a
  time-varying latent factor rank;
- the exact Gaussian FDD quotient applied to non-Gaussian tangent log-covariance data;
- the advertised \(n^{-3/7}\) rate under long memory; it requires \(d=0\), and \(d\in(0,\tfrac12)\) gives \(n^{-3(1-2d)/(7-2d)}\);
- an empirical memory exponent imported from daily exchange-rate realised volatility used as a property of monthly equity realised covariance;
- coordinatewise energy in place of bounded total norm;
- unqualified polynomial mixing as a dimension-free \(n^{-1/2}\) assumption;
- \(n^{-a}\) rather than \(n^{-a}/b_n\) in G1′ under level-only local stationarity;
- \(\Delta_n^{-2}\) in Davis–Kahan;
- a generic quadratic mean-recentring claim from cross-fitting alone;
- bounded total energy alone as sufficient for FRAME-2P-U;
- the same-band score/Richardson construction as a valid generic curved correction;
- an invariant-only redesign as an estimator of the original loading space;
- beyond-rank \(d_n^2\) from Weyl alone;
- consistency of the raw eigenvalue ratio from the displayed signal/null rates alone;
- automatic higher AIRM differential bounds from H-LIP alone;
- automatic transfer of AIRM geometry to Bures–Wasserstein covariance data;
- a pervasive-factor corollary obtained merely by dividing observations by \(\sqrt p\);
- a squared Bures–Wasserstein, AIRM, or log-Euclidean distance used to score or train a covariance forecast against a proxy that is conditionally unbiased for \(\Sigma\); each rewards a strictly shrunken target and none preserves the ranking;
- a recalibration of the forecast presented as restoring proxy-robustness; it restores the location of the optimum only;
- a global-minimum-variance portfolio evaluation presented as detecting a level or scalar distortion in a covariance forecast; it is exactly blind to it.
- an unbounded-score HE extension that suppresses escape probabilities, tail integrals, expanding-domain constants, or target bias;
- a global, rank-changing, pervasive shrinking-normal, or unrestricted sharp noncommuting BW corollary;
- a general HE–BW intersection beyond the proved fixed-basis positive-root case.

## Related notes

- [[HD1 — growing-dimension Paper 1 proof dossier]]
- [[HD1-A — G1 and derivative proof dossier]]
- [[HD1-B — lag operator signal and factor number proof dossier]]
- [[HD1-C — hostile counterexamples and assumption audit]]
- [[G1 audit — resolution of the uniform local Fréchet rate]]
- [[Analytical reconstruction — proof ledger and rebuilt spec]]
- [[Application map — geometry, symmetry, and rate accelerators]]
- [[Numerical suite — theorem-driven design matrix]]
- [[HE — canonical growing-energy theorem boundary]]
- [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]]
- [[BW-SHRINKING-MARGIN — canonical restricted theorem boundary]]
- [[HE — growing energy and pervasive signal working dossier]]
- [[BW — moving-centre Bures-Wasserstein working dossier]]
- [[FRAME-IF — closure adjudication]]
- [[FRAME-2P-U — conditional two-path debiasing theorem]]
- [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]]
- [[References and external claim audit]]
- [[Literature review — external positioning and prior art]]
- [[Joint HE-BW error ledger and hostile audit]]
- [[OPEN OBLIGATIONS — current research actions]]
- [[Paper 1 shape — identification to application]]

The HD1-A/B/C and working-dossier campaign links resolve to archived proof records. FRAME, HE, and both BW size packages now have explicit canonical theorem-boundary files above; those files and the top-level ledgers govern current wording and status.
