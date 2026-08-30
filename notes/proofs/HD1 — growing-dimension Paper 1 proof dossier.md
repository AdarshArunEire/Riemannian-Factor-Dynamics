---
type: proof-dossier
title: HD1 — growing-dimension Paper 1 proof dossier
status: canonical-proof
verdict: a dimension-free growing-p Paper 1 theorem, feasible lag operator, loading theorem, and factor-number selector are proved under bounded total energy, fixed finite memory, and explicit uniform geometry; the generic oracle-rate quadratic recentering claim is false without extra symmetry
last-audited: 2026-08-12
---

# HD1 — growing-dimension Paper 1 proof dossier

> This is the complete proof dossier for the robust bounded-total-energy growing-dimension theorem. The parked moving-loading programme is out of scope. Growing-energy HE and restricted moving-centre Bures–Wasserstein extensions now have separate proved packages in the canonical ledger; they are not silently consumed by the baseline theorem here. Unrestricted nonlocal BW sharp powers remain optional and open. Only claims proved here, proved in a cited canonical dependency with all hypotheses verified, or explicitly assumed as model primitives may enter the final theorem.

## 0. Migration map before canonical edits

### Claims to prove or replace

1. A dimension-free, positive-weight, three-scale G1 theorem on a triangular array of uniformly controlled Hadamard manifolds under bounded total tangent energy and one coherent short-memory condition.
2. Integrated level and derivative mean-error bounds, with the raw level local-stationarity discrepancy separated from its differentiated counterpart.
3. A feasible lag-covariance and lag-operator theorem in Hilbert–Schmidt/operator norm, with all mean, frame, cross-fit, local-stationarity, and noise channels typed and bounded.
4. A final loading-space theorem in the honest eigengap form, followed only then by a signal-strength corollary.
5. A factor-number theorem based on a proved beyond-rank square; if the unregularised ratio is not justified, replace it by a proved regularised selector.

### Reusable proved inputs

- empirical Sturm score-to-distance reduction for positive weights;
- the uniform second-order population barycentre expansion and the one-sided scale-family cancellation with
  \(c=(1,1/2,1/4)\) and \(\lambda=(1/3,-2,8/3)\);
- the typed ribbon-holonomy inequality;
- dimension-uniform affine-invariant SPD curvature and H-LIP constants on uniformly bounded tubes;
- deterministic Davis–Kahan and the rank-one identity \(\|x\otimes y\|_{\mathrm{HS}}=\|x\|\,\|y\|\).

### Suspect current claims

- G1′ currently differentiates kernel weights without paying the possible \(n^{-a}/b\) local-stationarity term.
- P1-OP is assumed rather than proved.
- \(\kappa\) is currently called an eigengap while the displayed rate pays \(\kappa^{-2}\); the parent paper instead uses \(\kappa\) for a lag-factor singular value.
- the existing cross-fitting prose does not by itself prove every conditional cancellation used in the feasible lag moments.
- Weyl's inequality alone cannot yield the claimed \(O_p(n^{-1})\) eigenvalues beyond rank.
- the unregularised eigenvalue-ratio selector is not consistent merely from \(\hat\lambda_i=O_p(n^{-1})\) for all \(i>r\).

### Notation repair

Throughout this dossier,
\[
s_n:=\max_{1\le h\le h_0}\sigma_r(C_{f,n}(h)),
\qquad
\Delta_n:=\lambda_r(\mathbb L_n)-\lambda_{r+1}(\mathbb L_n).
\]
The symbol \(\kappa\) is not used for either quantity.

### Direct consumers

G1 and integrated G1/G1′ feed the feasible transported observations and the ribbon bound. P1-OP feeds the deterministic lag-operator assembly. The loading theorem consumes only the explicitly listed rates. The factor-number theorem consumes the stronger row-operator perturbation bound that yields a squared beyond-rank eigenvalue rate.

## 1. Final assumption set

The final theorem uses the following single regime. These are theorem assumptions, not conclusions inferred from fixed-dimensional compactness.

**(HD-G) Uniform geometry.** $M_n$ is a Hadamard manifold of arbitrary dimension $p_n$. On one deterministic expanded tube containing the mean curve, all observations, all three positive barycentres, their Richardson images, connectors, and geodesic polygonal interpolants, the Hessian of one-half squared distance is bounded below by $I$, and the Exp, Log, connector, Richardson, and ruled-surface Jacobi differentials used in Workstream A and in Theorem PF below are bounded through the stated orders by constants independent of $n,p_n$. Bare “Hadamard plus bounded radius” is insufficient: hyperbolic spaces of curvature $-K_n$, $K_n\to\infty$, are a counterexample. For generic manifold sequences these remain explicit primitives. For affine-invariant SPD on fixed absolute generated spectral bands, [[Application map — geometry, symmetry, and rate accelerators]] T-APP-2 supplies the separate fixed-order, matrix-size-uniform proof in the project norms. Full-rank Bures–Wasserstein SPD is not globally Hadamard; instead, the archived BW-SIZE-FIXED-MARGIN proof supplies the quantitative differential and coercivity inputs used by the local constrained analogue of HD-G on one compatible complete generated domain with fixed spectral, polar, Exp, normal-pair, and path-length margins. Its recurrence-defined \(C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)\) is independent of \(m_n\); generic polygon \(N+\mathsf L\) and canonical PF grid/path inputs remain explicit.

When \(\alpha_n\downarrow0\), the restricted BW shrinking-margin theorem verifies a triangular-array replacement only on complete fractional-normal domains: \(\rho_{H,n}=O(\sqrt{\alpha_n})\), support/energy is \(O(\sqrt{\alpha_n})\), cubic bias and PF coefficients may pay \(\alpha_n^{-1}\), and every grid, cell, path, object-count, row, signal, and actual-gap condition is propagated termwise. A conservative rank-one corollary with \(\alpha_n\asymp m_n^{-A}\) has \(m_n=n^x\), \(0<x<3/(5A)\). This is sufficient rather than minimax and does not authorize fixed/growing energy. Neither geometry producer supplies HD-X automatically. For $m_n\times m_n$ SPD, $p_n=m_n(m_n+1)/2$.

The HD-G differential order is fixed at \(k_0=4\), matching T-APP-2. The consumed list is Exp, Log, connector, Richardson, score/Hessian, and ruled-surface Jacobi differentiation; the theorem does not assume an unspecified number of derivatives.

**(HD-X) Model and total energy.** In the true parallel frame,

\[
X_{t,n}=\operatorname{Exp}_{\mu_n(u_t)}
  [\mathcal P^{\mu_n}_{u_0\to u_t}A_nf_{t,n}+\delta_{t,n}],
\qquad
Y_{t,n}=A_nf_{t,n}+\varepsilon_{t,n},
\]

where $A_n^*A_n=I_r$, $r<\infty$ is fixed, and $\|Y_{t,n}\|\le R$ almost surely with $R$ independent of $n,p_n$. This is bounded total tangent energy, not coordinatewise boundedness. It is a trace-class/function-space regime in which finer coordinates resolve one fixed amount of variation. It excludes the classical regime where each new coordinate contributes order-one noise and total energy grows like \(p_n\). Thus “arbitrary \(p_n\)” means ambient-dimension agnostic inside this energy class, not a universal cure for high-dimensional noise. It does not by itself bound $\|f_t\|$; no such inference is used.

**(HD-M) Mean law and local stationarity.** The actual and proxy rows are $m_0$-dependent for one fixed $m_0$. The proxy laws have Fréchet mean $\mu_n(u)$, the score/Hessian law has the uniform derivatives in HD-G and Workstream A (A4), and the baseline coupling satisfies
\[
\sup_{t,n}\|d(X_{t,n},X_t^{(u_t,n)})\|_{L^2}\le Cn^{-a}.
\tag{HD-M2}
\]
The mean curve has uniformly bounded derivatives through the order used below. The almost-sure radius/tube condition remains a separate support assumption in HD-X/HD-G; it is not inferred from (HD-M2). The optional continuous-\(u\) supremum theorem G1-HD additionally assumes
\[
\sup_{t,n}d(X_{t,n},X_t^{(u_t,n)})\le Cn^{-a}\quad\text{almost surely}.
\tag{HD-Minf}
\]

**(HD-M/HD-K persistence constraint — imposed by ID-10.)** The stochastic term \((nb_n)^{-1/2}\) appearing in \(\ell_n\) below is not universal. [[P1-ID — centre-drift and factor identification boundary]] §12 proves it is the specialisation to HD-M of the frozen-factor ergodic-average modulus \(\psi^+(nb_n)\), and that the correct object in general is

\[
\ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1},
\]

which propagates through G1-HD-L2, GRID, Theorem PF, OBS, P1-ROW, P1-OP, EV and Davis–Kahan with no other change. Three consequences bind HD-M and HD-K:

1. HD-M's \(m_0\)-dependence gives \(\psi^+(N)\le\sqrt{(2m_0+1)R^2/N}\), so \(\ell_n(\psi)\) reduces to \(\ell_n\) verbatim. The matching *lower* bound needs \(\Lambda_u=\sum_h\operatorname{tr}\Gamma_u(h)>0\); \(Z_t=e_t-e_{t-1}\) has \(\psi(N)=\sqrt2/N\). The upper bound is the only direction consumed.
2. Under a memory exponent \(d\in(0,\tfrac12)\), \(\psi^+(N)\asymp N^{-(1/2-d)}\), the optimal bandwidth becomes \(b_n=n^{-(1-2d)/(7-2d)}\) and the rate \(n^{-3(1-2d)/(7-2d)}\). HD-K's \(nb_n/\log n\to\infty\) never binds; \(b_n\to0\) forces \(d<\tfrac12\). The residue-class device used in the G1-HD-L2 proof has **no long-memory analogue**, and the optional sup-norm results G1-HD and HD-Minf do not survive \(d>0\). Neither is consumed by Theorem HD-E, so this is a proved separation and not a gap — but it is displayed rather than assumed.
3. **\(a\ge3/7\) is a design constant, not a primitive.** The primitive clause is \(a\ge3\alpha\) for \(b_n=n^{-\alpha}\) (HD-K separately needs only \(a\ge\alpha\)); \(a\ge3/7\) is its \(\alpha=1/7\) instance. In the near-unit-root parameterisation \(\rho_n=1-n^{-\theta}\) with persistence varying in rescaled time, the induced exponent is \(a=1-\theta\) exactly and sharply, the re-optimised \(\alpha=(1-\theta)/7\) satisfies \(a\ge3\alpha\) automatically, and the window is \(\theta\in[0,1)\) with rate \(n^{-3(1-\theta)/7}\).

**(HD-K) Mean estimator.** Use the nonnegative one-sided scale kernels

\[
c=(1,1/2,1/4),\qquad \lambda=(1/3,-2,8/3),
\]

with $K,K'$ vanishing at both support endpoints. Combine the three positive barycentres by the Exp/Log Richardson map. Blend forward and backward estimators on a fixed-width interior overlap, not on a width-$b_n$ layer. Assume $b_n\to0$, $nb_n/\log n\to\infty$, and $n^{-a}=O(b_n)$.

**(HD-L) Lag identification.** The lag count $h_0$ is fixed. For every included lag, idiosyncratic lag covariance and both factor–noise cross covariances vanish. Equivalently,

\[
\Gamma_n(h)=\mathbb E(Y_{t,n}\otimes Y_{t-h,n})
=A_nC_{f,n}(h)A_n^*.
\]

The matrix $Q_n=\sum_{h=1}^{h_0}C_{f,n}(h)C_{f,n}(h)^*$ is positive definite. All finite-array averages use the same edge mask and normalisation in population and sample.

## 2. Mean theorems

Under the optional stronger (HD-Minf), Workstream A proves, without a sphere net and uniformly for arbitrary $p_n$,

\[
r_{\infty,n}:=
b_n^3+n^{-a}+n^{-1}+\sqrt{\frac{\log n}{nb_n}},
\qquad
\sup_u d(\hat\mu_n^{(3)}(u),\mu_n(u))=O_p(r_{\infty,n}),
\tag{G1-HD}
\]

Under the baseline \(L^2\) coupling (HD-M2), it proves

\[
\ell_n:=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1},
\qquad
\|\log_{\mu_n}\hat\mu_n^{(3)}\|_{L^2}=O_p(\ell_n).
\tag{G1-HD-L2}
\]

The same $O_p(\ell_n)$ RMS bound holds on every deterministic coarse grid: if $v_0,\ldots,v_M$ are deterministic, then

\[
\left\{(M+1)^{-1}\sum_{j=0}^M
d(\hat\mu_n^{(3)}(v_j),\mu_n(v_j))^2\right\}^{1/2}
=O_p(\ell_n).
\tag{GRID}
\]

The proof is empirical Sturm at each deterministic population barycentre, the weighted Hilbert inequality obtained by splitting an $m_0$-dependent row into $m_0+1$ independent residue classes, and the scale identities $\sum\lambda_jc_j=\sum\lambda_jc_j^2=0$. For G1-HD-L2 and GRID, the coupling contribution is bounded in mean square and then by Markov; no essential-sup coupling is consumed. The scale identities cancel both the usual second-order term and the nonlinear $m_1^2C$ term. Continuous-$u$ interpolation for the optional supremum theorem uses a one-dimensional time grid with $O(\log n)$ entropy; no $S^{p_n-1}$ net occurs.

The corrected derivative theorem is also proved:

\[
\|\nabla_u\log_{\mu_n}\hat\mu_n^{(3)}\|_{L^2}
=O_p\left(b_n^3+(nb_n^3)^{-1/2}+\frac{n^{-a}}{b_n}+\frac1{nb_n}\right).
\tag{G1'-HD}
\]

Under the explicit $C^1$ weighted score-discrepancy assumption A5-1 of Workstream A, $n^{-a}/b_n$ improves to $n^{-a}$. The random-point Karcher step concentrates Hessian actions on fixed vectors, not the full operator norm. The final loading theorem below does **not** consume G1′; this removes the derivative theorem from its dependency graph while retaining the corrected result for other consumers.

### Theorem PF — feasible polygonal mean and frame

Let $\bar\ell_n$ be a deterministic upper-rate sequence for $\ell_n$, and take

\[
M_n=\left\lceil\bar\ell_n^{-2/3}\right\rceil,
\qquad v_j=j/M_n.
\]

Compute the three-scale estimates at the vertices, interpolate consecutive vertices by their unique geodesics, and parallel-transport along this estimated polygon. Then, after radial endpoint connectors,

\[
\left\{n^{-1}\sum_t d(\bar\mu_n(u_t),\mu_n(u_t))^2\right\}^{1/2}=O_p(\ell_n),
\qquad
\sup_u\|\bar P_n(u)-P_n(u)\|_{\rm op}=O_p(\ell_n).
\tag{PF}
\]

**Proof.** Put $e_j=d(\hat\mu(v_j),\mu(v_j))$. GRID gives
$((M_n+1)^{-1}\sum e_j^2)^{1/2}=O_p(\ell_n)$, hence
$\max_j e_j\le\sqrt{M_n+1}\,\mathrm{RMS}=O_p(\ell_n^{2/3})=o_p(1)$; this supplies the common tube event. Busemann convexity bounds the distance between geodesic interpolants by the linear interpolation of endpoint errors. The true curve differs from its chord by $O(M_n^{-2})$, so the design-point RMS centre error is $O_p(\ell_n+M_n^{-2})=O_p(\ell_n)$.

For one cell, use the geodesic interpolation homotopy between the true and estimated chords and split its boundary quadrilateral into two ruled geodesic triangles. Uniform Jacobi bounds from HD-G give

\[
\operatorname{area}_j\le C\{M_n^{-1}(e_j+e_{j+1})+e_j^2+e_{j+1}^2\}.
\]

The parallel-transport variation formula bounds holonomy by curvature operator norm times this area. Summing, Cauchy–Schwarz gives

\[
\|P_{\rm estimated\ polygon}-P_{\rm true\ polygon}\|_{\rm op}
\le C\Lambda\{L_\mu\ell_n+M_n\ell_n^2\}.
\]

The lens between a $C^2$ true-mean segment and its chord has area $O(M_n^{-3})$; summing adds $O(M_n^{-2})$. Since $M_n\ell_n^2$ and $M_n^{-2}$ are $O(\ell_n^{4/3})$, PF follows. Every transport is compared only after the endpoint/base connectors have made domains and codomains equal. Corners require no derivative of the estimated curve. $\square$

## 3. Signal, lag operator, and factor number

Use the rank-one convention ((x\otimes y)z=\langle y,z\rangle x), and put

\[
\mathbb L_n=\sum_{h=1}^{h_0}\Gamma_n(h)\Gamma_n(h)^*,
\quad
s_n=\max_{h\le h_0}\sigma_r(C_{f,n}(h)),
\quad
\Delta_n=\lambda_r(\mathbb L_n)-\lambda_{r+1}(\mathbb L_n).
\]

Under HD-L,

\[
\mathbb L_n=A_nQ_nA_n^*,\qquad
\lambda_{r+1}(\mathbb L_n)=0,\qquad
\Delta_n=\lambda_{\min}(Q_n)>0.
\tag{SIG}
\]

If one included lag is full rank, (Q_n\succeq C_{f,n}(h)C_{f,n}(h)^*), hence

\[
\Delta_n\ge s_n^2.
\tag{SIG2}
\]

One full-rank lag is sufficient, not necessary: complementary rank-deficient lags can make (Q_n) positive definite while (s_n=0).

Let \(\widehat Y_{t,n}\) use the polygonal centre/frame and the endpoint connector of PF. Uniform Log base-point Lipschitz bounds and PF imply the feasible-observation RMS error

\[
q_n^2:=\max_{h\le h_0}\frac1{N_{n,h}}\sum_t
\frac{\|\widehat Y_{t,n}-Y_{t,n}\|^2+
\|\widehat Y_{t-h,n}-Y_{t-h,n}\|^2}{2}
=O_p(\ell_n^2).
\tag{OBS}
\]

The transformed feasible row need not remain (m_0)-dependent: the next comparison is pathwise. Only the oracle row is concentrated.

### Theorem P1-OP-HD — feasible lag operator

In the Hilbert space of Hilbert–Schmidt operators, fixed \(m_0,h_0\) and \(\|Y_t\|\le R\) give

\[
d_{\rm or,n}:=
\left\{\sum_{h=1}^{h_0}
\|\widetilde\Gamma_n(h)-\Gamma_n(h)\|_{\rm HS}^2\right\}^{1/2}
=O_p(n^{-1/2}).
\]

Expanding each feasible lag product and applying Cauchy–Schwarz pathwise gives

\[
d_n:=\left\{\sum_{h=1}^{h_0}
\|\widehat\Gamma_n(h)-\Gamma_n(h)\|_{\rm op}^2\right\}^{1/2}
\le d_{\rm or,n}+\sqrt{h_0}(2Rq_n+q_n^2)
=O_p(n^{-1/2}+\ell_n).
\tag{P1-ROW}
\]

Let \(A_{2,n}=(\sum_h\|\Gamma_n(h)\|_{\rm op}^2)^{1/2}\le\sqrt{h_0}R^2\). Row-operator multiplication yields

\[
\boxed{
\|\widehat{\mathbb L}_n-\mathbb L_n\|_{\rm op}
\le \eta_n:=2A_{2,n}d_n+d_n^2.}
\tag{P1-OP}
\]

**Approximate-target corollary.** Exact HD-L is the special case \(\zeta_n=0\). More generally let
\[
\Gamma_n(h)=\Gamma_n^0(h)+D_n(h),\qquad
\Gamma_n^0(h)=A_nC_{f,n}(h)A_n^*,\qquad
\zeta_n=\left\{\sum_h\|D_n(h)\|_{\rm op}^2\right\}^{1/2}.
\]
Put \(\bar d_n=d_n+\zeta_n\), \(A_{2,n}^0=(\sum_h\|\Gamma_n^0(h)\|_{\rm op}^2)^{1/2}\), and \(\mathbb L_n^0=\sum_h\Gamma_n^0(h)\Gamma_n^0(h)^*\). Then
\[
\|\widehat{\mathbb L}_n-\mathbb L_n^0\|_{\rm op}
\le 2A_{2,n}^0\bar d_n+\bar d_n^2=:\bar\eta_n.
\tag{P1-OP-zeta}
\]
All loading and selector conclusions below hold relative to the ideal factor target after replacing \(d_n,\eta_n,\Delta_n\) by \(\bar d_n,\bar\eta_n,\Delta_n^0\). Consistency requires \(\bar\eta_n=o_p(\Delta_n^0)\); persistent unbudgeted contamination is not hidden by the exact-factorisation headline.

No cross-fitting is needed for this robust theorem. A leave-block-out implementation may be used, but its deletion error must be added; it is not called zero under generic mixing. The sharper quadratic curved-recentring route is excluded from the final theorem because Workstream B's bounded hyperbolic two-state counterexample shows that cross-fitting alone does not kill the random Hessian term \(H(q,X)e\).

### Beyond-rank square and factor number

Write the population and empirical row operators as
$\mathcal G=[\Gamma_1\ \cdots\ \Gamma_{h_0}]$ and
$\widehat{\mathcal G}=\mathcal G+\mathcal D$. Then
$\mathbb L=\mathcal G\mathcal G^*$, $\widehat{\mathbb L}=\widehat{\mathcal G}\widehat{\mathcal G}^*$, and $\|\mathcal D\|\le d_n$. Since $\operatorname{rank}\mathcal G=r$, singular-value min–max gives

\[
\widehat\lambda_{r+1,n}=s_{r+1}(\widehat{\mathcal G})^2\le d_n^2,
\qquad
|\widehat\lambda_{j,n}-\lambda_{j,n}|\le\eta_n\quad(j\le r).
\tag{EV}
\]

This is the structural square unavailable from Weyl alone.

Let $\tau_n$ be deterministic with

\[
d_n^2=o_p(\tau_n),\qquad \tau_n=o(\Delta_n),\qquad \eta_n=o_p(\Delta_n).
\tag{TAU}
\]

Then the threshold selector

\[
\widehat r_n^{\rm thr}=\#\{j:\widehat\lambda_{j,n}>\tau_n\}
\]

is consistent. If additionally
$\inf_{j<r}\lambda_{j+1,n}/\lambda_{j,n}\ge c_*>0$, the ridged ratio

\[
\widehat r_n^{\rm ridge}
=\arg\min_{1\le j\le R_n}
\frac{\widehat\lambda_{j+1,n}+\tau_n}
{\widehat\lambda_{j,n}+\tau_n},\qquad r<R_n\le p_n-1,
\]

is consistent. The common bound $\widehat\lambda_j\le d_n^2$ for every $j>r$ makes this uniform even when $R_n$ grows. Raw-ratio consistency does not follow from these displayed rates alone: the rate-valid matrix
$\widehat{\mathbb L}=\operatorname{diag}(1,d_n^2,0)$ selects two factors because the later ratio is zero. This disproves the rate-to-consistency implication, not favourable behaviour in particular finite-sample designs.

### Corollary P1-AR1-SIG — exact weak-factor calibration

On the independent stationary AR(1) subclass

\[
f_{j,t}=\rho_jf_{j,t-1}+s_j\sqrt{1-\rho_j^2}\,\xi_{j,t},
\qquad |\rho_j|<1,
\]

where \(s_j\) is the marginal standard deviation, \(A^*A=I_r\), and HD-L
holds, the factor lag matrices are diagonal and the nonzero population
lag-operator eigenvalues are the decreasing rearrangement of

\[
\boxed{\chi_j=s_j^4\sum_{h=1}^{h_0}\rho_j^{2h}.}
\tag{AR1-SIG}
\]

Hence \(\Delta_n=\chi_{\min,n}:=\min_j\chi_{j,n}\) whenever every
coordinate has positive scale and nonzero persistence. On the event (EV),
the threshold selector is exactly correct under the finite-sample separation

\[
\boxed{d_n^2<\tau_n<\chi_{\min,n}-\eta_n.}
\tag{AR1-THR}
\]

Indeed, every signal eigenvalue is then above \(\tau_n\), whereas every
beyond-rank eigenvalue is below it. If \(\tau_n\ge\chi_{\min,n}\), even the
exact population threshold rule underselects. Thus TAU specialises to
\(d_n^2=o_p(\tau_n)\) and
\((\tau_n+\eta_n)/\chi_{\min,n}\to_p0\). A final factor whose marginal
amplitude is multiplied by \(w\) while persistence is held fixed has its
operator signal multiplied by exactly \(w^4\). Under the N-RANK fixed-total-
scale convention \(F\), its exact signal is

\[
\chi_{\rm tail}
=\frac{F^4w^4}{(r-1+w^2)^2}
\sum_{h=1}^{h_0}\rho^{2h}.
\]

This is a proved DGP-to-theorem calibration, not a minimax lower bound or a
growing-rank theorem. The complete derivation and rate translation are
[[P1-RANK — AR1 signal strength and threshold boundary]].

## 4. Final loading-space theorem

> **Theorem HD-E (ambient-dimension-free bounded-energy Paper 1 theorem — PROVED UNDER EXPLICIT ASSUMPTIONS).** Under HD-G through HD-L, with the feasible polygonal estimator and fixed $r,h_0,m_0$, let $\widehat E_n$ be the leading $r$-dimensional eigenspace of $\widehat{\mathbb L}_n$, transported to the true reference tangent space by the endpoint connector. If $\eta_n=o_p(\Delta_n)$, then for arbitrary $p_n\to\infty$ inside HD-X's bounded-total-energy class,
>
> \[
> \boxed{
> \|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
> =O_p\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right),
> \qquad
> \ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.}
> \tag{HD-E}
> \]
>
> Under approximate included-lag factorisation, the corresponding headline is
> \[
> \|\sin\Theta(\widehat E_n,E_n^0)\|_{\rm op}
> =O_p\!\left(\frac{n^{-1/2}+\ell_n+\zeta_n}{\Delta_n^0}\right)
> \]
> whenever (P1-OP-zeta) is \(o_p(\Delta_n^0)\).
>
> If one included factor lag is full rank, the denominator may be weakened to $s_n^2$. The factor number is consistently estimated by the threshold selector under TAU, or by the ridged ratio under TAU and the nonzero-spectrum ratio condition.

**Proof.** G1-HD-L2 and GRID feed Theorem PF. PF and uniform Log stability give OBS. Hilbert–Schmidt finite-memory concentration plus the pathwise feasible expansion give P1-ROW; deterministic row assembly gives P1-OP. Davis–Kahan uses the actual eigengap $\Delta_n$, producing HD-E. SIG2 alone permits the $s_n^{-2}$ weakening. EV and TAU prove the two factor selectors. Every node has been proved above or in the cross-audited A/B dossiers. G1′, cross-fitting, GLO symmetry, a full empirical Hessian operator bound, and the raw ratio are not consumed. $\square$

For $b_n=n^{-\alpha}$, the explicit level rate is

\[
\ell_n=O\{n^{-3\alpha}+n^{-(1-\alpha)/2}+n^{-a}\}.
\]

Balancing the first two terms gives $\alpha=1/7$ and $\ell_n=O(n^{-3/7})$ when $a\ge3/7$. The former practical choice $b_n=n^{-1/5}$ remains admissible; it gives $\ell_n=O(n^{-2/5}+n^{-a})$, hence $O_p(n^{-2/5}/\Delta_n)$ when $a\ge2/5$, null eigenvalues $O_p(n^{-4/5})$, and—for strong fixed signal—one may take any ridge/threshold between these two scales. There is no separate algebraic restriction on $p_n$ because all norm, geometry, energy, and memory constants are assumed dimension-uniform. HD-X nevertheless excludes order-one variation in each of \(p_n\) new coordinates; the HE theorem is the separate route for growing energy.

This is a trace-class/bounded-total-energy theorem. It does not claim a pervasive-factor regime with energy proportional to $p_n$, and it does not attain the parent fixed-centre $n^{-1/2}$ rate on a generic curved moving-centre model. The slower rate is the price of retaining a pathwise robust theorem after the generic quadratic curved-recentring claim was disproved.

## 5. Counterexamples and superseded claims

- **DISPROVED:** level local stationarity implies an \(O(n^{-a})\) derivative contribution. The sharp flat sign-of-kernel-derivative construction attains \(n^{-a}/b_n\).
- **DISPROVED:** a width-\(b_n\) forward/backward blend preserves \(b_n^3\) derivative bias. Its \(L^2\) derivative cost is \(b_n^{5/2}\); the fixed-width blend replaces it.
- **DISPROVED:** coordinatewise bounded moments imply dimension-free norm concentration. Independent Rademacher coordinates give \(\sqrt{p_n/(nb_n)}\).
- **DISPROVED:** unqualified polynomial mixing yields an \(n^{-1/2}\) Hilbert rate. A bounded regenerative process with \(\alpha(h)\asymp h^{-\beta}\), \(0<\beta<1\), has sample-mean scale \(n^{-\beta/2}\).
- **DISPROVED:** cross-fitting alone makes curved mean recentering quadratic. The random Hessian in Workstream B's hyperbolic Markov example leaves a nonzero first derivative.
- **DISPROVED:** \(\kappa^{-2}\) is correct when \(\kappa\) denotes the eigengap. Davis–Kahan pays \(\Delta_n^{-1}\); \(s_n^{-2}\) follows only from SIG2.
- **DISPROVED:** one full-rank lag is necessary. Complementary deficient lags can identify the full loading space.
- **DISPROVED:** Weyl implies the beyond-rank square. The row-operator min–max proof is required.
- **DISPROVED:** the raw eigenvalue-ratio selector follows from the beyond-rank square. The threshold or ridge is required.
- **SUPERSEDED:** G1′ as a loading-theorem dependency. The proved polygonal construction bypasses it.
- **SUPERSEDED:** cross-fitting as a prerequisite of the final robust P1-OP. Route R is pathwise and explicitly retains the first-order feasible RMS error.

## 6. Closed dependency ledger

| Load-bearing node | Final status | Direct consumer |
|---|---|---|
| positive three-scale weights and fixed-width boundary construction | PROVED | G1-HD |
| Hilbert score concentration under fixed finite memory | PROVED | G1-HD, GRID |
| integrated and arbitrary-grid RMS mean rate | PROVED | PF |
| corrected derivative theorem and $n^{-a}/b_n$ | PROVED; sharp counterexample | optional only |
| typed polygonal centre/frame theorem | PROVED | OBS |
| oracle HS lag-row concentration | PROVED | P1-ROW |
| feasible-versus-oracle Route R | PROVED pathwise | P1-OP |
| signal/eigengap identity and $\Delta_n\ge s_n^2$ | PROVED under HD-L | HD-E |
| lag-row/operator assembly | PROVED | HD-E, EV |
| Davis–Kahan with $\Delta_n^{-1}$ | PROVED | HD-E |
| beyond-rank square | PROVED | factor number |
| threshold and ridged selectors | PROVED | factor-number result |
| raw ratio from the displayed signal/null rates alone | DISPROVED AS AN IMPLICATION | not consumed |
| generic quadratic curved recentering | DISPROVED | not consumed |

There is no OPEN or CONDITIONAL node in the dependency graph of HD-E. Later application-map work proved a broader causal Hilbert physical-dependence version of the robust chain, fixed-band higher AIRM differentials, and two sharper oracle branches. The first uses exact sample separation, lag-specific GLO, and a negligible direct non-rigid frame coefficient, with one exact flat as the clean sufficient geometry. The second is the conditional FRAME-2P-U implication: an entirely observable three-colour, undersmoothed two-path polygon correction with \(b_n=n^{-1/7}\), \(M_n\asymp n^{2/7}\), and \(c_n=n^{-\gamma}\), \(1/6<\gamma<3/14\). If an array satisfies the full U2P generated-tube, composed-action, replacement, mask, dependence, GLO, and included-lag package uniformly in \(p_n\), then its post-influence mean/frame remainder is \(o_p(n^{-1/2})\) and its row is root-\(n\). The repository currently verifies growing-\(p_n\) nonemptiness only by padding a fixed curved active block with flat inactive coordinates; it has no genuinely growing-curvature, growing-size AIRM, or growing-size BW verification. Bounded total energy alone does not supply U2P. These sharper branches do not alter HD-E. Infinite-memory conditional splitting remains open. The later HE campaigns separately rederived the mean/frame and lag-row inputs with \(R_n\) under bounded-tail and expanding-domain truncation packages; those results are not corollaries of HD-E. The adjudicated local BW analogue supplies the geometric inputs at fixed margin and under a restricted fractional-normal shrinking regime; global, rank-changing, pervasive shrinking-normal, and unrestricted sharp-window variants remain outside that theorem class.

## 7. Parent comparison and verification history

The primary parent paper defines its $\kappa$ as the maximum smallest singular value of an included factor lag, not as an eigengap, and states $\lambda_r\ge\kappa^2$. Its fixed-centre short-memory theorem reports $n^{-1/2}/\kappa^2$, and its Proposition 3 reports $n^{-1/2}$ signal-eigenvalue errors and $n^{-1}$ null eigenvalues. HD-E matches the parent's dimension-free **bounded-total-energy / arbitrary-$p_n$** character and internally proves the lag-row square, but differs by using fixed finite memory, explicit uniform moving-mean geometry, a slower robust moving-centre rate, and a proved threshold/ridged selector. HD-E itself does not claim the parent's oracle rate or unregularised ratio conclusion. Conditional FRAME-2P-U matches the parent numerator's root-\(n\) order under U2P; its validation influence changes the first-order law, and the current growing-\(p_n\) witness has fixed active curvature plus flat padding.

Two parent-scope caveats are essential. First, conditions (13)--(14) allow trace-normalised algebraic covariance decay with $C_\xi$ uniformly bounded and a uniform lower bound on $d_\xi$ strictly greater than one near $\mu$; finite $m$-dependence is a special case, so the parent dependence condition is broader than HD-E's baseline fixed finite memory. Second, Theorem 2 is dimension-free as stated, but Example 1 verifies P3 under geometric $\alpha$-mixing for $p=o(n^\gamma/\log n)$, $0<\gamma<1/2$, and under algebraic mixing only for fixed $p$. Remark P-RATIO in [[Paper 1 — Locally stationary Riemannian factor model]] records the direct Eq. (5) correction: raw-ratio consistency does not follow from Proposition 3's displayed rates alone, although the parent's Table 2 reports strong finite-sample selection. The public APP-FIN implementation is the numerical reproduction baseline.

Independent proof work is retained under `Archived/Proof workstreams` in:

- [[HD1-A — G1 and derivative proof dossier]];
- [[HD1-B — lag operator signal and factor number proof dossier]];
- [[HD1-C — hostile counterexamples and assumption audit]].

The later FRAME-2P-U proof and hostile closure records are [[FRAME-IF — closure adjudication]], [[FRAME-IF-A — geometry closure]], [[FRAME-IF-B — statistical closure]], and [[FRAME-IF-C — impossibility and replacement]]. They are not dependencies of the robust HD-E proof.

Workstream A attacked B's G1/G1′ and perforated-design inputs; Workstream B attacked A's random-point differentiation and grid sufficiency; Workstream C attacked both and the main polygonal integration. The repairs incorporated here are the fixed-width blend, $n^{-a}/b_n$, higher-geometry assumptions, arbitrary-grid RMS theorem, typed polygonal area proof, pathwise Route R, signal/eigengap separation, and regularised factor selector.
