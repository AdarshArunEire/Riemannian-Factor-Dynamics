---
type: idea
title: Paper 1 — Locally stationary Riemannian factor model
aliases:
  - Moving-centre RFM, covariantly constant loadings
  - Paper 1
status: current-spec
verdict: robust bounded-energy growing-p theorem and stated accelerators proved; growing-energy/pervasive-factor scaling and full moving-centre Bures–Wasserstein geometry are the two primary open extensions
last-audited: 2026-08-08
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

Paper 1 now has a nontrivial theorem for arbitrary $p_n\to\infty$. It is dimension-free because total tangent energy, finite-memory length, lag count, factor rank, and every geometric differential constant are uniformly bounded. It is not a classical pervasive-factor theorem with energy proportional to $p_n$, and its robust moving-centre loading rate is slower than the parent fixed-centre oracle rate.

For a fixed real dataset, this bounded-energy condition is a finite constant and does not forbid using the method. The restriction matters when making a uniform asymptotic claim while adding genuinely new noisy coordinates. That high-energy regime is an open extension, not evidence that the corresponding applications are unusable.

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
- **Known/constant/parametric centre branch — PROVED.** A known centre is immune. A root-\(n\) constant or finite-dimensional parametric centre preserves oracle order but generally enters the first-order law; it is not first-order immunity.
- **Physical-dependence branch — PROVED.** Uniform summable Hilbert \(L^2\) and essential-sup innovation effects replace fixed memory in the robust G1/oracle-row chain. Exact cancellation under infinite memory remains conditional on a joint row coupling or conditional physical-dependence theorem.
- **Structured signed growing-\(p_n\) mean — PROVED UNDER EXPLICIT ASSUMPTIONS.** Deterministic, scalar-plus-Hilbert–Schmidt, and controlled block-scalar Hessians avoid the operator sphere net. This covers flat/common flats and bounded constant-negative-curvature tubes, but not unrestricted full AIRM SPD. Faster mean convergence alone does not imply oracle loading.

## Primary next extensions

### Growing energy and pervasive signal

Let \(R_n=\sup_t\|Y_{t,n}\|\to\infty\). The current defect calculations show score, oracle-row, and feasible-comparison scales of benchmark order

\[
R_n(nb_n)^{-1/2},\qquad R_n^2n^{-1/2},\qquad 2R_nq_{R,n}+q_{R,n}^2,
\]

but the complete mean/frame rate \(q_{R,n}\), operator perturbation, and admissible joint growth of \((R_n,A_{2,n},\Delta_n)\) have not yet been assembled into a theorem. This programme is the route to expanding asset, sensor, gene, imaging, and connectivity panels. Normalisation is allowed only when it preserves the scientific estimand and a sufficient eigengap.

### Moving-centre Bures–Wasserstein covariance dynamics

The parent covariance application uses Bures–Wasserstein geometry, not AIRM. Full BW therefore needs its own controlled domain, mean uniqueness, alignment, Exp/Log/Hessian, connector/frame, and lag-identification proof. The fixed-basis diagonal BW submodel is flat in square-root coordinates; full noncommuting BW remains open. The fixed-matrix-size theorem must be closed before auditing matrix-size-uniform constants.

## Model and estimator

$$
X_{t,n}=\operatorname{Exp}_{\mu_n(u_t)}
\left[\mathcal P^{\mu_n}_{u_0\to u_t}A_nf_{t,n}+\delta_{t,n}\right],
\qquad
Y_{t,n}=\mathcal P^{\mu_n}_{u_t\to u_0}\log_{\mu_n(u_t)}X_{t,n}
=A_nf_{t,n}+\varepsilon_{t,n}.
$$

Here $A_n^*A_n=I_r$, with fixed $r$, and $\|Y_{t,n}\|\le R$ almost surely uniformly in $n,p_n$. The row and its smooth proxy laws are fixed-$m_0$-dependent. Level local stationarity is $O(n^{-a})$.

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
(Q_n=\sum_hC_{f,n}(h)C_{f,n}(h)^*\succ0), then

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

No cross-fitting or quadratic mean cancellation is consumed by this robust theorem. Cross-fitting alone is insufficient on curved manifolds: the random Hessian (H(q,X)) can leave a first-order recentering term.

> **Final loading theorem.** If $\eta_n=o_p(\Delta_n)$, then for arbitrary $p_n\to\infty$,
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

The Huang–Chen–Chen parent paper uses $\kappa$ for the factor-lag singular value corresponding here to $s_n$, and states $\lambda_r\ge\kappa^2$. The current theorem matches its dimension-free bounded-total-energy character for arbitrary $p_n$, but adds a moving centre and therefore uses stronger uniform geometry and a robust nonparametric loading rate. It does not claim the parent's fixed-centre $n^{-1/2}$ oracle rate, its broader short-memory formulation, or consistency of the unregularised ratio from the displayed eigenvalue rates alone.

## Claims excluded from Paper 1

- fixed (p) as the final scope;
- coordinatewise energy in place of bounded total norm;
- unqualified polynomial mixing as a dimension-free (n^{-1/2}) assumption;
- (n^{-a}) rather than (n^{-a}/b_n) in G1′ under level-only local stationarity;
- (Delta_n^{-2}) in Davis–Kahan;
- a generic quadratic mean-recentring claim from cross-fitting alone;
- beyond-rank (d_n^2) from Weyl alone;
- consistency of the raw eigenvalue ratio;
- automatic higher AIRM differential bounds from H-LIP alone;
- automatic transfer of AIRM geometry to Bures–Wasserstein covariance data;
- a pervasive-factor corollary obtained merely by dividing observations by \(\sqrt p\).

## Related notes

- [[HD1 — growing-dimension Paper 1 proof dossier]]
- [[HD1-A — G1 and derivative proof dossier]]
- [[HD1-B — lag operator signal and factor number proof dossier]]
- [[HD1-C — hostile counterexamples and assumption audit]]
- [[G1 audit — resolution of the uniform local Fréchet rate]]
- [[Analytical reconstruction — proof ledger and rebuilt spec]]
- [[OPEN OBLIGATIONS — current research actions]]

The HD1-A/B/C links resolve to archived proof records. Only the canonical files above govern current wording and status.
