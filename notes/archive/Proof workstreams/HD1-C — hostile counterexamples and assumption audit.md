---
type: proof-dossier
title: HD1-C — hostile counterexamples and assumption audit
status: current-audit
last-audited: 2026-08-08
scope: growing-dimension Paper 1 only
---

# HD1-C — hostile counterexamples and assumption audit

This dossier audits only the growing-$p_n$ Paper 1 chain. Paper 2 is not considered. A claim is accepted below only when the displayed assumptions imply it; otherwise an analytic counterexample or an exact theorem restriction is given.

## 1. Executive verdict

The dimension-free route is coherent, but only in a **bounded-total-energy, uniformly controlled geometry, genuinely short-memory** regime. The ambient dimension then disappears because the score lives in a Hilbert space and each lag product lives in the Hilbert--Schmidt class; it does not disappear under coordinatewise energy assumptions.

Four repairs are mandatory.

1. The current derivative theorem is false under level local stationarity alone. Its raw local-stationarity term is $n^{-a}/b_n$, and this order is attained by a deterministic flat counterexample. An $O(n^{-a})$ derivative contribution requires a separate differentiable local-stationarity assumption.
2. If $s_n$ is the largest smallest singular value of an included factor lag and $\Delta_n$ is the eigengap of the lag operator, then $\Delta_n\ge s_n^2$ only under the exact no-lag-noise/no-cross-term factorisation. Davis--Kahan pays $\Delta_n^{-1}$, not $\Delta_n^{-2}$. The weaker display $s_n^{-2}$ is legitimate only after the comparison.
3. A generic operator perturbation bound does not prove the $O_p(n^{-1})$ beyond-rank eigenvalue rate. The square is nevertheless available from the sum-of-squares construction if every population lag covariance has range in the same rank-$r$ space and each lag-covariance error is $O_p(n^{-1/2})$. The unregularised eigenvalue ratio can still over-select; a ridge is necessary.
4. Polynomial mixing without a sufficiently strong exponent is inadequate even in dimension one. A stationary regenerative bounded process with $\alpha(h)\asymp h^{-\beta}$, $0<\beta<1$, has sample-mean rate $n^{-\beta/2}$ rather than $n^{-1/2}$. A complete theorem should use a dimension-uniform short-memory condition such as fixed $m$-dependence, or prove the required Hilbert/HS concentration under a stronger physical-dependence assumption.

The cleanest fully internal restriction is fixed $m_0$-dependence with a.s. bounded total tangent norm. It permits nonzero factor autocovariances at the included lags, gives dimension-free concentration by residue-class blocking, makes a leave-block-out gap exact, and applies equally in the tangent Hilbert space and the HS operator space.

## 2. Dimension-free concentration: what is true

### 2.1 Independent Hilbert-valued weighted sums

Let $Z_i$ be independent, centred random elements of an arbitrary real Hilbert space $H$, with $\|Z_i\|\le R$ a.s., and let $w_i$ be deterministic. Put $S=\sum_iw_iZ_i$. Orthogonality of independent centred summands gives
$$
\mathbb E\|S\|^2=\sum_iw_i^2\mathbb E\|Z_i\|^2\le R^2\|w\|_2^2.
$$
Moreover $z\mapsto\|\sum_iw_iz_i\|$ changes by at most $2R|w_i|$ when coordinate $i$ is replaced. The bounded-difference inequality therefore gives
$$
\Pr\{\|S\|\ge R\|w\|_2+x\}
\le \exp\!\left(-\frac{x^2}{2R^2\|w\|_2^2}\right).
$$
Neither calculation uses $\dim H$. This closes the basic dimension question for independent tangent scores.

### 2.2 A fully internal dependent repair: fixed $m_0$-dependence

Suppose the triangular array is $m_0$-dependent for a constant $m_0$ independent of $n,p_n$. Partition the indices into the $m_0+1$ residue classes modulo $m_0+1$. Within each class the variables are independent. Apply the preceding inequality to each class and use the triangle inequality. Uniformly over Hilbert spaces,
$$
\left\|\sum_iw_iZ_i\right\|
=O_p\!\left(R\sqrt{m_0+1}\,\|w\|_2\right)
$$
pointwise, and a union over $N$ deterministic parameter values costs only $\sqrt{\log N}$. Constants depend on $m_0$ and $R$, not on $p_n$.

For kernel weights,
$$
\|w(u)\|_2^2\le \frac{C}{nb_n},\qquad
\|w(u)\|_\infty\le\frac{C}{nb_n}.
$$
Thus a polynomial-size $u$-grid yields $O_p(\sqrt{\log n/(nb_n)})$ in Hilbert norm. The same proof applies to $Z_t=Y_t\otimes Y_{t-h}$ in the Hilbert space $\mathcal S_2(H)$ because
$$
\|Y_t\otimes Y_{t-h}\|_{\rm HS}=\|Y_t\|\,\|Y_{t-h}\|\le R^2.
$$
For fixed $h_0$, these products are $(m_0+h_0)$-dependent. Hence both the score and all oracle lag covariances have dimension-free concentration under one common assumption set.

### 2.3 Continuous-$u$ interpolation has no ambient entropy when done in norm

Assume, after deterministic parallel identification, that the centred score $S_n(u)$ satisfies
$$
\|S_n(u)-S_n(v)\|\le L_n|u-v|,
\qquad L_n\le Cb_n^{-1},
$$
where the bound includes the derivative of the normalised weights and the uniform derivative of the deterministic centre/connector. At target resolution
$r_n=\sqrt{\log n/(nb_n)}$, a grid of mesh $r_n/L_n$ has
$$
N_n\le 1+C\frac{L_n}{r_n}
=1+O\!\left(\sqrt{\frac{n}{b_n\log n}}\right).
$$
For $b_n=n^{-\alpha}$ this is polynomial in $n$, so $\log N_n=O(\log n)$, independently of $p_n$. A sphere net is unnecessary. The same reasoning works for three fixed scales and a smooth boundary blend provided all derivative constants are uniform.

This interpolation conclusion is conditional on a norm-Lipschitz score. It is false to obtain it merely from pointwise concentration: without a uniform weight/connector modulus, continuous-$u$ entropy has not been controlled.

### 2.4 Coordinatewise boundedness does not imply a dimension-free rate

Let $Z_i=(\xi_{i1},\ldots,\xi_{ip_n})$ with independent Rademacher coordinates and independent $i$. Every coordinate is bounded by one, but
$$
\mathbb E\left\|\frac1N\sum_{i=1}^NZ_i\right\|^2=\frac{p_n}{N}.
$$
Thus the norm rate is $\sqrt{p_n/N}$, not $N^{-1/2}$. The total-energy hypothesis $\|Z_i\|\le R$ (or a dimension-uniform norm-sub-Gaussian analogue) is substantive and cannot be replaced by coordinatewise moments.

## 3. Polynomial mixing is not enough as an unqualified assumption

Fix $0<\beta<1$. Let the positive integer block lengths $L_j$ be iid with
$$
\Pr(L_j\ge \ell)\asymp \ell^{-(1+\beta)},
$$
so $\mathbb EL_j<\infty$. Give each renewal block an independent Rademacher label and take the stationary version of the resulting piecewise-constant process $Z_t\in\{-1,1\}$. The event that $0$ and $h$ lie in the same block has probability
$$
q_h=\frac{\mathbb E(L-h)_+}{\mathbb EL}\asymp h^{-\beta}.
$$
Conditional on a renewal between the two times the labels are independent. Hence
$$
\operatorname{Cov}(Z_0,Z_h)=q_h\asymp h^{-\beta},
$$
and regenerative coupling gives $\alpha(h)\le q_h$; the covariance inequality in the reverse direction gives $\alpha(h)\ge |\operatorname{Cov}(Z_0,Z_h)|/4$. Thus $\alpha(h)\asymp h^{-\beta}$ exactly up to constants. Finally,
$$
\operatorname{Var}\!\left(n^{-1}\sum_{t=1}^nZ_t\right)
=n^{-2}\left[n+2\sum_{h=1}^{n-1}(n-h)q_h\right]
\asymp n^{-\beta}.
$$
Embedding $Z_t e_1$ in $\mathbb R^{p_n}$ gives bounded total energy for arbitrary $p_n\to\infty$ but a sample-mean scale $n^{-\beta/2}$. Therefore “polynomial mixing” without a summability/exponent condition cannot deliver the desired $n^{-1/2}$ oracle concentration. This is already a one-dimensional failure, not a hidden-net phenomenon.

For the final theorem, either retain fixed $m_0$-dependence, or state a Hilbert-valued physical/martingale dependence assumption and prove its weighted exponential inequality with constants uniform in $(n,p_n)$. A scalar polynomial-mixing citation is not interchangeable with that result.

## 4. The derivative local-stationarity term is $n^{-a}/b_n$

### 4.1 Attaining counterexample

Work on the flat Hadamard sequence $M_n=\mathbb R^{p_n}$ and let the stationary approximation be identically zero: $X_t^{(u)}=0$, $\mu_n(u)=0$. Fix an interior $u_0$. For a local kernel estimator write its effective derivative weights at $u_0$ as $d_{t,n}=\partial_uw_{t,n}(u_0)$. They satisfy
$$
\sum_t|d_{t,n}|\asymp b_n^{-1}
$$
for every nonconstant $C^1$ kernel with the usual normalisation. Define the deterministic triangular observations
$$
X_{t,n}=n^{-a}\operatorname{sign}(d_{t,n})e_1.
$$
Then $\|X_{t,n}-X_t^{(u_t)}\|=n^{-a}$ for every $t$, so the stated level local-stationarity assumption is satisfied with its best possible constant. Yet
$$
\left\|\partial_u\sum_tw_{t,n}(u)X_{t,n}\bigg|_{u=u_0}\right\|
=n^{-a}\sum_t|d_{t,n}|
\asymp \frac{n^{-a}}{b_n}.
$$
There is no randomness or curvature to blame. For the three-scale extrapolation, replace $d_{t,n}$ by the derivative of its effective equivalent kernel $\sum_j\lambda_jw_{j,t,n}$; this derivative is not identically zero, and the same sign construction gives the same order. Thus Richardson cancellation of smooth population bias does not cancel an adversarial local-stationarity remainder.

Consequently, under level local stationarity alone the honest derivative statement contains
$$
\|\nabla_ue_n\|_{L^2}
=O_p\!\left(b_n^3+(nb_n^3)^{-1/2}+n^{-a}/b_n\right),
$$
and the old display without a local-stationarity term is **DISPROVED**.

### 4.2 Exact sufficient repair

An $O(n^{-a})$ derivative contribution follows if the deterministic population score discrepancy, after a fixed fibre identification,
$$
D_n(u,v,q)
=\mathbb E\log_qX_{\lfloor nv\rfloor,n}
-\mathbb E\log_qX_{\lfloor nv\rfloor}^{(v)},
$$
has a $C^1$ extension in the smoothing variable $v$ on the tube with
$$
\sup_{n,u,v,q}\big(\|D_n(u,v,q)\|+\|\nabla_vD_n(u,v,q)\|\big)
\le Cn^{-a}.
$$
Integration by parts, or direct differentiation of the convolution after adding and subtracting $D_n(u,u,q)$, then yields $O(n^{-a})$ rather than $O(n^{-a}/b_n)$. A pathwise version with a differentiable coupling residual and the same norm bound also suffices. Merely assuming joint smoothness of the stationary law $P_u$ does not control the triangular-array discrepancy and does not repair the counterexample.

### 4.3 Bandwidth consequence

With only level local stationarity and $b_n=n^{-\alpha}$, making the derivative remainder vanish requires $a>\alpha$; making its product with a level error negligible at an $n^{-1/2}$ loading target imposes the actual product inequalities used by the ribbon proof. Any final bandwidth window must be recomputed with $n^{-a}/b_n$ unless the preceding $C^1$ discrepancy assumption is explicitly adopted.

More precisely, if
$$
L_n=b_n^3+(nb_n)^{-1/2}+n^{-a},\qquad
D_n=b_n^3+(nb_n^3)^{-1/2}+n^{-a}/b_n,
$$
then the absolute-value ribbon bound consumes $L_nD_n$, not merely $D_n=o(1)$. At $b_n=n^{-1/5}$ the new purely local-stationary product is $n^{-2a+1/5}$, and the cross-products with the stochastic terms require $a>3/10$; together these require $a>7/20$ for $L_nD_n=o(n^{-1/2})$. If the deterministic linear rotation $n^{-a}$ is also required to be $o(n^{-1/2})$, the stronger already-visible condition $a>1/2$ dominates. Thus the corrected derivative term does not kill $b_n=n^{-1/5}$ in the oracle-order regime, but it must appear in the theorem and in non-oracle rate statements.

## 5. Geometry and support across a manifold sequence

### 5.1 A bounded radius is not a uniform geometric constant

Take $M_n$ to be hyperbolic $p_n$-space of constant sectional curvature $-K_n$ with $K_n\to\infty$. Every $M_n$ is Hadamard and observations may be supported in a fixed radius $R$. The tangential eigenvalue of the Hessian of one-half squared distance at radius $r$ is
$$
r\sqrt{K_n}\coth(r\sqrt{K_n}),
$$
which diverges for fixed $r>0$. Therefore “Hadamard plus bounded support” does not make Hessian, log-map, Exp-map, connector, or derivative constants uniform over $n$. The final theorem must assume the needed dimension-uniform operator bounds, or specialise to a sequence such as affine-invariant SPD where they have been proved.

On non-Hadamard sequences, bounded curvature also does not replace a uniform non-conjugacy/tube margin: on a sphere the derivative of $\theta\cot\theta$ blows up as $\theta\uparrow\pi$. Every log, connector and differentiated Karcher equation must be restricted to one common tube event.

### 5.2 Affine-invariant SPD bookkeeping

For $m_n\times m_n$ SPD matrices,
$$
p_n=\dim\operatorname{Sym}(m_n)=m_n(m_n+1)/2,
$$
not $m_n$. A statement allowing $m_n=o(n^c)$ corresponds to $p_n=o(n^{2c})$. Bounded Frobenius tangent energy means the sum of the $p_n$ orthonormal-coordinate energies is $O(1)$; coordinatewise $O(1)$ energy instead gives total energy $O(p_n)$.

The established affine-invariant SPD curvature and local-symmetry bounds remove geometric dimension factors on bounded tubes. They do not remove the total-energy, dependence, support, signal, or idiosyncratic-noise restrictions.

### 5.3 The tube event must match its consumer

If the proof differentiates logs, connectors or Karcher equations for all observations simultaneously, a per-observation escape probability $q_n$ is insufficient: the union bound requires $nq_n\to0$. If escaped observations are trimmed and only an average lag operator is compared, a weaker $q_n$ may suffice, but its induced operator contamination must be shown smaller than the displayed perturbation rate. The simplest dimension-free theorem uses an a.s. total-radius bound, in which case every positive barycentre stays in the geodesically convex support ball on a Hadamard manifold. A probabilistic tube condition cannot be silently substituted for this pathwise event.

## 6. Bounded support and factor strength

Let $Y_t=Af_t+\varepsilon_t$, with $A^*A=I_r$. If $\|Y_t\|\le R$ alone is assumed, no bound on $f_t$ follows: one may take arbitrarily large $f_t$ and $\varepsilon_t=-Af_t+Y_t$. A factor-energy conclusion requires, for example, $A^*\varepsilon_t=0$ a.s., separate norm bounds, or the second-moment orthogonality $\mathbb E\langle Af_t,\varepsilon_t\rangle=0$. Under the last condition,
$$
\mathbb E\|f_t\|^2\le\mathbb E\|Y_t\|^2\le R^2.
$$
Hence bounded total energy is compatible with fixed-rank factors having constant lag signal, but incompatible with “pervasive” signal diverging like a positive power of $p_n$. If $r=r_n\to\infty$, then for every lag covariance $C_f(h)$,
$$
\sigma_{r_n}(C_f(h))
\le \frac{\|C_f(h)\|_*}{r_n}
\le \frac{\mathbb E\|f_t\|\|f_{t-h}\|}{r_n}
\le \frac{R^2}{r_n}.
$$
Thus a nonvanishing smallest-lag singular value forces fixed rank in the bounded-total-energy regime. The final theorem should take fixed $r$ unless it explicitly budgets this decay.

## 7. Signal strength, eigengap, and lag-rank

Assume for every included lag that serial idiosyncratic covariance and both factor--noise cross covariances vanish. Then in the true frame
$$
\Gamma_n(h)=A_nC_{f,n}(h)A_n^*,
$$
and
$$
\mathbb L_n
=A_nQ_nA_n^*,
\qquad Q_n=\sum_{h=1}^{h_0}C_{f,n}(h)C_{f,n}(h)^*.
$$
If $Q_n$ is positive definite, $\lambda_{r+1}(\mathbb L_n)=0$ and
$$
\Delta_n=\lambda_r(\mathbb L_n)=\lambda_{\min}(Q_n).
$$
Defining
$$
s_n=\max_{h\le h_0}\sigma_r(C_{f,n}(h)),
$$
choose a maximising lag $h_*$. Since $Q_n\succeq C_{f,n}(h_*)C_{f,n}(h_*)^*$,
$$
\Delta_n\ge s_n^2.
$$
Therefore Davis--Kahan gives
$$
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
\le C\frac{\|\widehat{\mathbb L}_n-\mathbb L_n\|_{\rm op}}{\Delta_n}
\le C\frac{\|\widehat{\mathbb L}_n-\mathbb L_n\|_{\rm op}}{s_n^2}.
$$
The first denominator is the theorem; the second is a weakening. If a symbol $\kappa_n$ denotes $\Delta_n$, then $\kappa_n^{-2}$ is wrong by one power.

The one-full-rank-lag condition is sufficient but not necessary. Let bounded independent innovations generate
$$
f_{1t}=\eta_t+a\eta_{t-1},\qquad
f_{2t}=\zeta_t+b\zeta_{t-2},
$$
with the two innovation sequences independent and Rademacher. For lags $1,2$,
$$
C_f(1)=\begin{pmatrix}a&0\\0&0\end{pmatrix},\qquad
C_f(2)=\begin{pmatrix}0&0\\0&b\end{pmatrix}.
$$
Each included lag covariance loses rank, yet $Q=\operatorname{diag}(a^2,b^2)$ is full rank. The minimal identification assumption is $Q_n\succ0$, equivalently $\cap_{h\le h_0}\ker C_f(h)^*=\{0\}$, not existence of one full-rank lag.

Conversely, if a nonzero $v$ lies in that common kernel, then $Av$ is absent from every $\Gamma(h)$ and the lag operator cannot identify the full loading space. No sample theorem can repair this population failure.

If idiosyncratic lag covariance or factor--noise cross terms are present, the factorisation above fails and neither $\operatorname{Im}\mathbb L_n=\operatorname{Im}A_n$ nor $\Delta_n\ge s_n^2$ follows. Those terms must vanish exactly or enter as explicit population contamination smaller than the relevant eigengap.

## 8. Idiosyncratic energy and dependence

Coordinatewise bounded idiosyncratic noise can destroy dimension-free lag concentration. Let $\zeta_t$ be iid Rademacher and
$$
\varepsilon_t=\zeta_t\mathbf 1_{p_n}.
$$
Every coordinate is bounded and every positive-lag population covariance is zero, but
$$
\frac1n\sum_t\varepsilon_t\varepsilon_{t-1}^*
=\left(\frac1n\sum_t\zeta_t\zeta_{t-1}\right)
\mathbf 1_{p_n}\mathbf 1_{p_n}^*.
$$
The scalar products $\zeta_t\zeta_{t-1}$ are iid Rademacher (up to one initial sign), while $\|\mathbf 1\mathbf 1^*\|_{\rm op}=p_n$. Thus the operator fluctuation is $\Theta_p(p_n/\sqrt n)$. Bounded total energy would exclude this example because $\|\varepsilon_t\|=\sqrt{p_n}$.

Bounded total energy alone does not exclude population lag contamination. Take a bounded two-state Markov scalar $g_t$ with $\mathbb E g_tg_{t-h}=\rho^h$ and a unit vector $v\perp\operatorname{Im}A$. With $\varepsilon_t=g_tv$, the lag operator has an idiosyncratic eigen-direction $v$, which can dominate weak factors. The final identification theorem must assume $\Gamma_\varepsilon(h)=0$ and zero factor--noise lag cross terms for the included lags, or explicitly bound the resulting population operator and its angle effect.

## 9. Cross-fitting: exact benefit and exact limitation

In flat scalar iid noise, let a local mean use $N\asymp nb_n$ equal weights and define $\widehat Y_t=Y_t-\widehat\mu_t$. For $1\le h<N$, direct expansion gives
$$
\mathbb E(\widehat Y_t\widehat Y_{t-h})
=-\frac{2\sigma^2}{N}+\frac{N-h}{N^2}\sigma^2
=-\frac{\sigma^2}{N}+O(h/N^2).
$$
Thus feasible orthogonality is not exact without deletion; the defect is genuinely $(nb_n)^{-1}$. It is smaller than $n^{-1/2}$ when $b_n\gg n^{-1/2}$, but it cannot be set equal to zero and it matters to beyond-rank squares and weak-signal conditions.

Under fixed $m_0$-dependence, excluding a block of radius at least $m_0+h_0$ around both indices in each lagged product gives exact independence between training and evaluation variables. If the deleted radius is $g_n$, preserving the local mean rate also requires
$$
g_n=o(nb_n),
$$
and the deterministic deletion perturbation $g_n/(nb_n)$ must be included. Under generic mixing, a finite gap does **not** create exact conditional independence. A proof must either use a coupling theorem and pay its coupling probability, or retain a dependence condition such as fixed $m_0$-dependence for which the claimed decoupling is literal.

Cross-fitting is not needed to identify the oracle population lag operator; it is needed by the present feasible-moment orthogonality and rigid-rotation arguments. Any no-cross-fit bypass must bound the coupled first-order term directly rather than call it a commutator.

## 10. Operator assembly and beyond-rank eigenvalues

Let $B_n=\max_{h\le h_0}\|\Gamma_n(h)\|_{\rm op}$ and
$d_n=\max_{h\le h_0}\|\widehat\Gamma_n(h)-\Gamma_n(h)\|_{\rm op}$. Deterministically,
$$
\|\widehat{\mathbb L}_n-\mathbb L_n\|_{\rm op}
\le \sum_{h=1}^{h_0}
\left(2\|\Gamma_n(h)\|_{\rm op}d_n+d_n^2\right)
\le h_0(2B_nd_n+d_n^2).
$$
No theorem allowing $h_0\to\infty$ may hide this factor without additional square-summability arguments.

Now suppose $\operatorname{ran}\Gamma_n(h)\subset E_n$ for every $h$, where $\dim E_n=r$. For $x\in E_n^\perp$,
$$
x^*\widehat{\mathbb L}_nx
=\sum_h\|\widehat\Gamma_n(h)^*x\|^2
=\sum_h\|(\widehat\Gamma_n(h)-\Gamma_n(h))^*x\|^2
\le h_0d_n^2\|x\|^2.
$$
The min--max principle with the trial space $E_n$ gives
$$
\widehat\lambda_{r+1}\le h_0d_n^2.
$$
This is the structural square that a generic Weyl inequality misses. If $h_0=O(1)$ and $d_n=O_p(n^{-1/2})$, beyond-rank eigenvalues are $O_p(n^{-1})$. If feasible mean, frame, deletion, or local-stationarity errors make $d_n$ larger, their **lag-covariance-level** rate must be squared here. A bound stated only for $\widehat{\mathbb L}-\mathbb L$ cannot recover this conclusion.

An approximately common rigid rotation preserves all eigenvalues exactly and should be removed before applying the preceding argument. Time-varying non-rigid frame error belongs in $d_n$.

## 11. Factor-number ratios

The unregularised ratio selector is inconsistent even when the beyond-rank square holds. Consider the deterministic sequence
$$
\widehat\Gamma_n=\operatorname{diag}(1,\delta_n,0),
\qquad
\widehat{\mathbb L}_n=\operatorname{diag}(1,\delta_n^2,0),
$$
with true rank $r=1$ and $\delta_n\downarrow0$. Then
$$
\widehat\lambda_2/\widehat\lambda_1=\delta_n^2,
\qquad
\widehat\lambda_3/\widehat\lambda_2=0,
$$
so minimising the raw ratio over $j=1,2$ selects $j=2$, not $r=1$.

A corrected fixed-search-range selector is
$$
\widehat r
=\arg\min_{1\le j\le R}
\frac{\widehat\lambda_{j+1}+c_n}{\widehat\lambda_j+c_n}.
$$
It is consistent under all of the following:

- $r\le R<\infty$;
- $\lambda_r(\mathbb L_n)\gg c_n$;
- $h_0d_n^2=o_p(c_n)$;
- $h_0(2B_nd_n+d_n^2)=o_p(\lambda_r(\mathbb L_n))$;
- $\inf_{j<r}\lambda_{j+1}(\mathbb L_n)/\lambda_j(\mathbb L_n)\ge\eta>0$.

Indeed, at $j=r$ the ratio tends to zero; for $j>r$, both eigenvalues are $o_p(c_n)$ and the ratio tends to one; for $j<r$, Weyl plus the last condition keeps the ratio bounded below by (say) $\eta/2$. If $R=R_n\to\infty$, uniform control of all beyond-rank eigenvalues and the search multiplicity is an additional theorem, not a consequence of loading consistency.

## 12. Consumer/dependency audit

| Node | Hostile outcome | Exact assumption or replacement | Direct consumers |
|---|---|---|---|
| Hilbert score concentration | PROVED for independent/fixed $m_0$-dependent bounded-total-energy arrays | $\|Z_t\|\le R$, fixed $m_0$, deterministic weight norms | G1 stage barycentres; integrated G1 |
| HS lag concentration | PROVED under the same regime | $\|Y_t\|\le R$, fixed $h_0,m_0$ | P1-OP oracle term |
| Dimension-free claim under coordinatewise moments | DISPROVED | retain total norm/trace budget | every growing-$p_n$ stochastic rate |
| Unqualified polynomial mixing | DISPROVED | fixed $m_0$, or a separately proved dimension-uniform Hilbert dependence inequality | G1, P1-OP |
| Continuous-$u$ interpolation | PROVED conditionally without $p_n$ entropy | norm-Lipschitz score/connector, polynomial-size grid | uniform G1 |
| Uniform manifold constants | DISPROVED from bare varying Hadamard + bounded radius | uniform operator geometry, preferably AIRM SPD bounded tube | all Exp/Log/Hessian/frame steps |
| Level local-stationarity derivative rate $n^{-a}$ | DISPROVED | use $n^{-a}/b_n$, or impose $C^1$ score-discrepancy local stationarity | G1$'$; ribbon correction; bandwidth |
| Three-scale cancellation of local-stationarity derivative | DISPROVED | same repair; equivalent derivative kernel is nonzero | G1$'$ |
| Bounded support implies bounded factor energy | DISPROVED without separation | pointwise/separate bound or second-moment factor--noise orthogonality | signal admissibility |
| $\Delta_n\ge s_n^2$ | PROVED under exact factorised lag covariances | zero included-lag noise/cross terms; one full-rank lag | weakened $s_n^{-2}$ loading rate |
| One full-rank lag is necessary | DISPROVED | use $Q_n=\sum_hC_hC_h^*\succ0$ | identification, eigengap |
| Eigengap denominator $\kappa^{-2}$ when $\kappa=\Delta$ | DISPROVED algebraically | Davis--Kahan uses $\Delta^{-1}$; $s^{-2}$ only after comparison | final loading theorem |
| Cross-fitting gives exact independence under mixing | DISPROVED as stated | fixed $m_0$ with adequate gap, or explicit coupling error | feasible P1-OP; rotation channel |
| Beyond-rank $O_p(n^{-1})$ from Weyl | DISPROVED as an implication | prove lag-level $d_n=O_p(n^{-1/2})$ and common population range | factor-number theorem |
| Raw eigenvalue ratio | DISPROVED | ridge $c_n$ between $h_0d_n^2$ and $\lambda_r$ plus no internal signal cliff | factor-number consistency |
| SPD dimension $p_n=m_n$ | DISPROVED | $p_n=m_n(m_n+1)/2$ | every growth condition |

## 13. Restrictions that make a complete final theorem defensible

A complete theorem may safely consume the following common regime.

1. $M_n$ is affine-invariant $m_n\times m_n$ SPD with $p_n=m_n(m_n+1)/2\to\infty$, or an explicitly uniformly controlled Hadamard sequence; all observations and estimator stages remain in a common fixed-radius tube.
2. The transported total tangent norm is a.s. bounded by a constant independent of $n,p_n$; factor/noise separation prevents hidden cancellation. Factor rank $r$ and lag count $h_0$ are fixed.
3. The triangular array is fixed $m_0$-dependent (or a stronger proved Hilbert physical-dependence replacement), uniformly in $n,p_n,u$.
4. The positive three-scale mean estimator has uniform deterministic bias expansion and norm-Lipschitz score. For G1$'$, either retain $n^{-a}/b_n$ or impose the $C^1$ local-stationarity discrepancy in §4.2.
5. Leave-block-out gaps exceed $m_0+h_0$, deleted mass is $o(1)$, and its explicit rate is included.
6. At included lags, idiosyncratic lag covariance and both factor--noise cross covariances vanish. $Q_n=\sum_hC_{f,n}(h)C_{f,n}(h)^*$ is positive definite. Define $s_n$ and $\Delta_n$ separately.
7. The additive lag-covariance error $d_n$ is proved term by term. The loading condition is $h_0(2B_nd_n+d_n^2)=o(\Delta_n)$, while common rigid rotation is controlled separately without a gap penalty.
8. If factor number is claimed, use the regularised selector of §11 with $h_0d_n^2=o(c_n)\ll\lambda_r$ and a fixed search range.

Under these restrictions, no dimension sequence appears in concentration constants; $p_n\to\infty$ is permitted because total energy, geometry and dependence are uniform. This is a trace-class/high-dimensional regime, not the classical pervasive-factor regime with energy proportional to $p_n$.

### 13.1 Hostile audit of the no-cancellation fallback

A slower feasible theorem can avoid every cross-fit cancellation. It needs two distinct level norms. Define
$$
\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a},
$$
and prove both
$$
\|e_n\|_{L^2(du)}=O_p(\ell_n),
\qquad
\left(n^{-1}\sum_{t=1}^n\|e_n(u_t)\|^2\right)^{1/2}=O_p(\ell_n).
$$
The first statement alone does not imply the second: a continuous random error field can spike at all design points while having arbitrarily small Lebesgue $L^2$ norm. The design-grid RMS bound must be proved directly by summing the pointwise second-moment bound.

Under level local stationarity put
$$
d'_n=b_n^3+(nb_n^3)^{-1/2}+n^{-a}/b_n;
$$
under the $C^1$ discrepancy repair replace the last term by $n^{-a}$. The typed ribbon inequality then gives a uniform frame discrepancy
$$
r_{{\rm fr},n}
=O_p\!\left(\Lambda_n\ell_n[L_{\mu,n}+d'_n]\right).
$$
After inserting the endpoint connectors, uniform log/base-point Lipschitz bounds on the expanded deterministic tube yield the feasible-observation RMS rate
$$
q_n
:=\left(n^{-1}\sum_t\|\widehat Y_t-Y_t\|^2\right)^{1/2}
=O_p\!\left(\ell_n+r_{{\rm fr},n}\right).
$$
Here the displayed subtraction is shorthand for the connector-identified fibres; without that identification it is ill-typed.

Let $\widetilde\Gamma_n(h)=n^{-1}\sum_tY_t\otimes Y_{t-h}$. Bounded total oracle norm and Cauchy--Schwarz give pathwise
$$
\|\widehat\Gamma_n(h)-\widetilde\Gamma_n(h)\|_{\rm HS}
\le 2R q_n+q_n^2+O(h_0/n),
$$
uniformly over fixed $h_0$. Fixed $(m_0,h_0)$ gives
$$
\max_{h\le h_0}\|\widetilde\Gamma_n(h)-\Gamma_n(h)\|_{\rm HS}
=O_p(n^{-1/2}).
$$
Thus
$$
d_n:=\max_{h\le h_0}\|\widehat\Gamma_n(h)-\Gamma_n(h)\|_{\rm op}
=O_p(n^{-1/2}+q_n+q_n^2+h_0/n).
$$
No stochastic independence between mean estimation and lag products is used.

For a nonstationary triangular array, $\Gamma_n(h)$ in this statement must be defined as the finite-sample time-average $n^{-1}\sum_t\mathbb E(Y_t\otimes Y_{t-h})$. Comparing it to an integrated stationary-approximation target is a separate local-stationarity/Riemann-sum term. Omitting that definition hides another $n^{-a}+h_0/n$ contribution.

At $b_n=n^{-1/5}$, $a>1/2$, bounded $L_{\mu,n},\Lambda_n$, one has
$$
\ell_n\asymp n^{-2/5},\qquad d'_n\asymp n^{-1/5},
\qquad q_n\asymp d_n\asymp n^{-2/5}.
$$
The resulting loading rate is $O_p(n^{-2/5}/\Delta_n)$ (plus any separately chosen target-comparison term), and the beyond-rank rate is $O_p(n^{-4/5})$. This is slower than the cancellation-based oracle rate but is fully dimension-free and requires no cross-fitting. Consistency requires $d_n=o(\Delta_n)$; the ridged selector additionally requires $h_0d_n^2=o(c_n)\ll\lambda_r$ and the positive-spectrum separation stated in §11.

### 13.2 Derivative-free polygonal-frame bypass

The final theorem can avoid G1$'$ altogether by changing the feasible centre/frame estimator. Let $v_j=j/m$, compute the positive three-scale mean only at these vertices, join consecutive estimated vertices by their unique geodesic chords, and parallel transport along the resulting polygon.

Write
$$
e_j=d(\widehat\mu(v_j),\mu(v_j)),\qquad
\left((m+1)^{-1}\sum_{j=0}^me_j^2\right)^{1/2}=O_p(\ell_n).
$$
This grid-RMS theorem must be proved directly from the pointwise second moments; it does not follow from continuous $L^2(du)$. On a common bounded tube with uniform Jacobi/surface constants, split the cell quadrilateral
$$
(\mu_j,\mu_{j+1},\widehat\mu_{j+1},\widehat\mu_j)
$$
into two geodesic triangles. A ruled-geodesic parametrisation gives
$$
\operatorname{Area}_j
\le C\left[L_\mu m^{-1}(e_j+e_{j+1})+e_j^2+e_{j+1}^2\right].
$$
The curvature variation formula for parallel transport then bounds the connector-identified cell holonomy by $C\Lambda\operatorname{Area}_j$. Cauchy--Schwarz yields
$$
\sum_{j=0}^{m-1}m^{-1}(e_j+e_{j+1})=O_p(\ell_n),
\qquad
\sum_{j=0}^{m-1}(e_j^2+e_{j+1}^2)=O_p(m\ell_n^2).
$$
If $\mu$ has uniformly bounded covariant acceleration, the area between each true curve segment and its true chord is $O(m^{-3})$, hence $O(m^{-2})$ after summation. Therefore
$$
r_{{\rm fr},n}^{\rm poly}
\le C\Lambda\left[L_\mu\ell_n+m\ell_n^2+m^{-2}\right].
$$
Choosing $m\asymp\ell_n^{-2/3}$ makes the last two terms $O(\ell_n^{4/3})$, so the frame rate is $O_p(\ell_n)$ when $L_\mu=O(1)$.

The tube event follows from
$$
\max_j e_j\le\left(\sum_je_j^2\right)^{1/2}
=O_p(\sqrt m\,\ell_n)=O_p(\ell_n^{2/3})=o_p(1),
$$
plus a fixed margin around the true curve. Busemann convexity of geodesic interpolation shows that the level error between vertices is bounded by the linear interpolation of $(e_j,e_{j+1})$ plus the $O(m^{-2})$ true-curve chord error. Hence the design-observation RMS log/base-point error is $O_p(\ell_n+m^{-2})$.

This is a genuinely feasible estimator: it uses only estimated vertices, geodesic interpolation and polygonal parallel transport. The connector at the unknown true base point appears only in the theoretical comparison, not in computation. Corners cause no problem because parallel transport along a piecewise smooth path is well-defined and no derivative of the estimated curve is taken. The cost is that this is a different canonical estimator and it supports the slower no-cancellation operator rate of §13.1; it does not recover the oracle $n^{-1/2}$ loading rate. Under this route G1$'$ remains an audited theorem but is not a consumer of the final theorem.

## 14. No-loose-ends rule for the integrated proof

The final loading theorem must not consume any of the following unless the indicated branch is selected:

- polynomial-mixing concentration: consume fixed $m_0$ instead, unless an exact Hilbert theorem is proved;
- a derivative rate without local-stationarity contribution: consume $n^{-a}/b_n$ or the $C^1$ discrepancy assumption;
- a $p_n$-net: consume direct Hilbert/HS norm concentration;
- a generic varying-Hadamard compactness argument: consume uniform operator-geometry constants or AIRM SPD;
- $\kappa^{-2}$ with $\kappa$ called an eigengap: consume $\Delta_n^{-1}$, and only then optionally $s_n^{-2}$;
- factor-number consistency from Davis--Kahan: consume the lag-level square and the ridged-ratio proof separately.

Any sharper mixing class, growing $h_0$, growing factor rank, unbounded total energy, or unregularised ratio is optional research only and must not be a hidden dependency of the final theorem.

## 15. Final cross-audit objection ledger

This section records the hostile read of the completed HD1-A and HD1-B workstreams and the proposed polygonal integration route.

| Claim | Verdict | Exact disposition |
|---|---|---|
| A: finite-memory Hilbert concentration and dimension-free level G1 | **ACCEPT** | The residue-class/second-moment proof is Hilbert-valued, dimension-free, and uses the stated total norm and weight bounds. |
| A: continuous-$u$ interpolation | **ACCEPT** | The pathwise norm modulus and polynomial grid cost only $O(\log n)$; there is no sphere net. |
| A: random-point Karcher derivative stability | **ACCEPT after patch** | Positive Hessian gives inverse norm at most one; only the fixed-vector Hessian action is concentrated. The patched absorption event and exceptional-event $b^{-1}$ bound close the integrated second moment. |
| A: cubic Richardson differentiation | **REPAIR SCOPE** | The patched proof now assumes four uniform Exp/Log/Richardson differentials. This closes the abstract theorem. The existing archived H-LIP result alone does not establish all four derivatives for an AIRM sequence; either retain them as explicit A1 primitives for the SPD application or add a higher-Jacobi/symmetric-space proof. |
| A: fixed-width forward/backward blend | **ACCEPT** | Both full one-sided windows are valid on the fixed overlap for $b<1/3$; bounded $\chi'$ transfers the level discrepancy without a $b^{-1}$ loss. The former width-$b$ blend is correctly rejected at derivative order. |
| A: corrected G1$'$ | **ACCEPT under A1--A7** | The $n^{-a}/b$ term is sharp; the patched final Log remainder is explicitly dominated. It is not consumed by the robust polygonal final theorem. |
| A: design-grid RMS for polygon vertices | **REPAIR STATEMENT** | Corollary 6.3 is stated on all observation design points. The proof by uniform pointwise second moments and Markov applies verbatim to any deterministic polygon grid; this arbitrary-grid version must be stated in the integrated dossier. Subsetting the all-design RMS inequality alone would lose $\sqrt{n/m}$. |
| B: curved Hessian counterexample B4 | **ACCEPT** | The process is bounded with mean at the geodesic origin, and the hyperbolic transverse Hessian $r\coth r$ makes the first lag derivative nonzero. It correctly proves that cross-fitting is not geometric orthogonality. |
| B: sharp cross-fitted Route S | **REPAIR / DO NOT CONSUME IN ROBUST FINAL** | It is valid only with GLO, the stated exact block independence, and a G1 theorem on the perforated design. The last input is listed rather than proved. Route S may remain a conditional sharper theorem, not the no-loose-ends final route. |
| B: pathwise RMS Route R | **ACCEPT after minor wording repair** | The rank-one expansion and Cauchy--Schwarz need no independence or GLO. “Training-measurable” is unnecessary for its alignment $Q_n$; a random theoretical base connector/alignment is allowed because every inequality is pathwise. |
| B: signal/eigengap theorem | **ACCEPT** | LN gives the exact factorisation; $\sum_hC_{f,n}(h)C_{f,n}(h)^*\succ0$ is the minimal lag-rank condition; $\Delta_n\ge s_n^2$ is only the full-rank-lag corollary. |
| B: bounded support versus factor energy | **REPAIR WORDING** | Bounded $Y_t$ alone does not bound $f_t$ because of cancellation. Under LN it does bound the included lag covariance since $C_f(h)=A^*\Gamma(h)A$, which is all the signal theorem needs. Do not call this a pointwise factor-energy bound. |
| B: row-operator beyond-rank square | **ACCEPT** | Singular-value min--max gives $\widehat\lambda_{r+1}\le\|\mathcal D\|^2$; no Weyl misuse remains. |
| B: threshold and ridged selectors | **ACCEPT** | The threshold rule is simplest. The ridge proof correctly requires $d_n^2=o_p(\tau_n)$, $\tau_n=o(\Delta_n)$, operator perturbation $o_p(\Delta_n)$, and a lower bound on internal nonzero ratios. |
| Polygon: quadrilateral/frame lemma | **REPAIR PROOF, THEN ACCEPT** | Use the geodesic-interpolation homotopy between the true and estimated chords. Uniform Jacobi bounds give $\operatorname{Area}_j\le C[\delta(e_j+e_{j+1})+e_j^2+e_{j+1}^2]$, which is sufficient. The parallel-transport variation formula bounds the connector-identified cell error by curvature times this area. |
| Polygon: true curve versus chord | **ACCEPT under uniform $C^2$ mean bound** | Sagitta is $O(\delta^2)$ and cell length is $O(\delta)$, so area is $O(\delta^3)$ per cell and $O(m^{-2})$ in total. |
| Polygon: RMS-to-sum and maximum | **ACCEPT with arbitrary-grid RMS repair** | Cauchy--Schwarz gives the linear $L_\mu\ell_n$ term and $\sum e_j^2=O_p(m\ell_n^2)$. With $m\asymp\ell_n^{-2/3}$, $\max_je_j\le\sqrt{m+1}\,\mathrm{RMS}=O_p(\ell_n^{2/3})=o_p(1)$, supplying the tube event. |
| Polygon: observation error and feasibility | **ACCEPT** | Busemann convexity transfers endpoint errors to every chord point; uniform base-log Lipschitzness and the polygonal frame bound give $q_n=O_p(\ell_n)$. The estimator uses only observable vertex barycentres, geodesic interpolation and piecewise-geodesic parallel transport. True connectors are theoretical comparison devices only. |

### Accepted final dependency path

The no-loose-ends final route should be
$$
\text{A level G1 + arbitrary-grid RMS}
\longrightarrow
\text{proved polygonal centre/frame lemma}
\longrightarrow
q_n=O_p(\ell_n)
\longrightarrow
\text{B Route R}
\longrightarrow
\text{row assembly/Davis--Kahan}
\longrightarrow
\text{threshold or ridged factor selector}.
$$
It does not consume G1$'$, GLO, perforated-design cross-fitting, polynomial mixing, a $p_n$-net, or the old quadratic recentering assertion. Those sharper or broader nodes may remain optional without being unresolved dependencies of the final theorem.
