---
type: idea
title: Paper 1 — Locally stationary Riemannian factor model
aliases:
  - Moving-centre RFM, covariantly constant loadings
  - Paper 1
status: current-spec
verdict: the robust theorem is proved; FRAME-2P-U is a proved conditional U2P implication with only fixed-active-curvature padded growing-dimensional witnesses, not a verified generic growing-curvature or AIRM result; HE and scoped BW results remain as separately adjudicated
last-audited: 2026-08-12
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

Paper 1 is a dynamic dimension-reduction model with a slowly moving baseline. It separates a smooth Fréchet-centre path from a small number of serially persistent tangent-factor directions. It can be used for interpretation and reconstruction directly. Forecasting additionally requires a model for the extracted factor scores, followed by an Exp-map reconstruction. Paper 1 is therefore not a universal stand-alone forecaster and makes no claim of automatic superiority over direct matrix time-series models.

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

is consistent. A ridge-ratio selector is also consistent under a lower bound on adjacent nonzero population eigenvalue ratios. The raw ratio is **DISPROVED**: for $\hat{\mathbb L}=\operatorname{diag}(1,d_n^2,0)$, minimising consecutive unregularised ratios selects rank two.

## Parent comparison

Huang, Chen and Chen (2026), *A Riemannian Factor Model for Manifold-Valued Time Series*, arXiv:2607.28385v1, Theorem 2 and Proposition 3, use \(\kappa\) for a factor-lag singular-value strength, obtain \(O_p(1/(\kappa^2\sqrt n))\), and state \(\lambda_r\ge\kappa^2\). Their P1 bounded-radius condition explicitly implies total factor and noise energy cannot diverge with \(p\); their theorem is not a classical pervasive-energy result. The robust moving-centre theorem matches that bounded-total-energy/arbitrary-ambient-dimension character but has a slower fallback rate. Conditional FRAME-2P-U matches the root-\(n\) rate order under U2P and three colours; its added validation influence prevents a claim of oracle limit-law equivalence. See [[References and external claim audit]].

## Claims excluded from Paper 1

- fixed \(p\) as the final scope;
- coordinatewise energy in place of bounded total norm;
- unqualified polynomial mixing as a dimension-free \(n^{-1/2}\) assumption;
- \(n^{-a}\) rather than \(n^{-a}/b_n\) in G1′ under level-only local stationarity;
- \(\Delta_n^{-2}\) in Davis–Kahan;
- a generic quadratic mean-recentring claim from cross-fitting alone;
- bounded total energy alone as sufficient for FRAME-2P-U;
- the same-band score/Richardson construction as a valid generic curved correction;
- an invariant-only redesign as an estimator of the original loading space;
- beyond-rank \(d_n^2\) from Weyl alone;
- consistency of the raw eigenvalue ratio;
- automatic higher AIRM differential bounds from H-LIP alone;
- automatic transfer of AIRM geometry to Bures–Wasserstein covariance data;
- a pervasive-factor corollary obtained merely by dividing observations by \(\sqrt p\).
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
- [[HE — growing energy and pervasive signal working dossier]]
- [[BW — moving-centre Bures-Wasserstein working dossier]]
- [[FRAME-IF — closure adjudication]]
- [[FRAME-2P-U — conditional two-path debiasing theorem]]
- [[References and external claim audit]]
- [[Joint HE-BW error ledger and hostile audit]]
- [[OPEN OBLIGATIONS — current research actions]]

The HD1-A/B/C and HE/BW campaign links resolve to archived proof records. Only the canonical files above govern current wording and status.
