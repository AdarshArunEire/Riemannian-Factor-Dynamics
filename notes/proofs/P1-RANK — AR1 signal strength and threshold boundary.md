---
title: P1-RANK — exact AR(1) signal strength and threshold boundary
status: proved internally on the stated orthogonal stationary AR(1) subclass
scope: analytical bridge into HD1; no minimax lower bound and no selector-optimality claim
updated: 2026-08-21
---

# P1-RANK — exact AR(1) signal strength and threshold boundary

## 1. Purpose and scope

HD1 states factor-number consistency in terms of the lag-operator gap
\(\Delta_n\), the row error \(d_n\), the operator error
\(\eta_n=2A_{2,n}d_n+d_n^2\), and a threshold \(\tau_n\). The simulation
configuration is instead expressed through factor marginal scales and AR(1)
persistences. This note gives the exact map between those two descriptions.

The result is deliberately narrow. It covers independent stationary AR(1)
coordinates with an isometric loading map and the exact HD-L lag
factorisation. It proves the finite-sample separation event consumed by the
existing threshold theorem. It does **not** prove a minimax impossibility
result, optimal threshold calibration, raw-ratio consistency, a growing-rank
theorem, or an application-level weak-factor claim.

## 2. Exact population spectrum

Let \(A:\mathbb R^r\to H\) satisfy \(A^*A=I_r\). For
\(j=1,\ldots,r\), let

\[
 f_{j,t}=\rho_j f_{j,t-1}
 +s_j\sqrt{1-\rho_j^2}\,\xi_{j,t},
 \qquad |\rho_j|<1,
\tag{2.1}
\]

where the innovations are independent standard Gaussians and the initial
law is stationary. Thus \(s_j\) is the marginal standard deviation, not the
innovation standard deviation. Let the included positive lags be a fixed
finite set \(\mathcal H\subset\{1,2,\ldots\}\). Assume HD-L, so residual lag
covariance and both factor--residual cross-lag directions vanish and

\[
 \Gamma(h)=A C_f(h)A^*.
\]

> **Proposition AR1-SIG (exact lag-operator eigenvalues).** Under (2.1),
> \[
> C_f(h)=\operatorname{diag}
> \bigl(s_1^2\rho_1^h,\ldots,s_r^2\rho_r^h\bigr),
> \]
> and
> \[
> \mathbb L=\sum_{h\in\mathcal H}\Gamma(h)\Gamma(h)^*
> =A\,\operatorname{diag}(\chi_1,\ldots,\chi_r)A^*,
> \qquad
> \boxed{\chi_j=s_j^4\sum_{h\in\mathcal H}\rho_j^{2h}.}
> \tag{AR1-SIG}
> \]
> Consequently, the nonzero eigenvalues of \(\mathbb L\) are the decreasing
> rearrangement of the positive \(\chi_j\). If every \(s_j>0\) and every
> \(\rho_j\ne0\), then \(\operatorname{rank}\mathbb L=r\) and
> \[
> \Delta=\lambda_r(\mathbb L)-\lambda_{r+1}(\mathbb L)
> =\min_j\chi_j.
> \tag{2.2}
> \]
> A coordinate with \(\rho_j=0\) is dynamically silent at all included
> positive lags and is not part of the minimum lag-generated loading space,
> even if its lag-zero variance is positive.

**Proof.** Stationarity of (2.1) gives
\(\mathbb E f_{j,t}f_{j,t-h}=s_j^2\rho_j^h\). Independence across
coordinates makes \(C_f(h)\) diagonal. Since \(A^*A=I_r\),

\[
 \Gamma(h)\Gamma(h)^*
 =A C_f(h)A^*A C_f(h)^*A^*
 =A C_f(h)C_f(h)^*A^*.
\]

Summing over \(h\in\mathcal H\) gives (AR1-SIG). An isometry preserves the
nonzero spectrum, so (2.2) follows when every \(\chi_j>0\). If
\(\rho_j=0\), every positive-lag covariance of that coordinate is zero.
\(\square\)

## 3. Exact hand-off to the HD1 threshold theorem

HD1 proves for the empirical lag operator that

\[
 \widehat\lambda_{r+1}\le d^2,
 \qquad
 |\widehat\lambda_j-\lambda_j|\le\eta
 \quad(j\le r).
\tag{3.1}
\]

> **Proposition AR1-THR (finite-sample separation event).** Put
> \(\chi_{\min}=\min_j\chi_j\). On every event where (3.1) holds, the
> threshold selector
> \[
> \widehat r^{\rm thr}=\#\{j:\widehat\lambda_j>\tau\}
> \]
> returns exactly \(r\) whenever
> \[
> \boxed{d^2<\tau<\chi_{\min}-\eta.}
> \tag{AR1-THR}
> \]
> Conversely, if \(\tau\ge\chi_{\min}\), even the exact population operator
> is underselected by this threshold rule. Thus, relative to the HD1 error
> bounds, the unresolved strip is precisely where the weakest signal and
> its perturbation interval meet the threshold.

**Proof.** Every signal eigenvalue obeys
\(\widehat\lambda_j\ge\chi_{\min}-\eta>\tau\). Positive-semidefinite
ordering and (3.1) give \(\widehat\lambda_j\le d^2<\tau\) for every
\(j>r\). Hence exactly the first \(r\) eigenvalues exceed \(\tau\). If
\(\tau\ge\chi_{\min}\), applying the rule to
\(\widehat{\mathbb L}=\mathbb L\) discards at least one population signal
eigenvalue because the rule uses a strict inequality. \(\square\)

For a triangular array, the convenient sufficient formulation is

\[
 d_n^2=o_p(\tau_n),
 \qquad
 \frac{\tau_n+\eta_n}{\chi_{\min,n}}\xrightarrow{p}0.
\tag{3.2}
\]

Because \(\Delta_n=\chi_{\min,n}\) on this subclass, (3.2) is exactly the
AR(1) specialisation of HD1's conditions TAU. It does not add a new
assumption to HD1; it expresses the existing gap assumption in DGP
parameters.

## 4. Why amplitude is raised to the fourth power

Suppose the first \(r-1\) factors share marginal scale \(s\) and persistence
\(\rho\), while the final factor has scale \(ws\), \(0<w\le1\), and the
same persistence. Proposition AR1-SIG gives the exact within-cell ratio

\[
 \frac{\chi_{\rm tail}}{\chi_{\rm strong}}=w^4.
\tag{4.1}
\]

The two powers of \(w\) from lag covariance are squared again when the lag
row is assembled into \(\mathbb L=\mathcal G\mathcal G^*\). Thus a
\(w=0.2\) amplitude tail has only

\[
 0.2^4=0.0016
\]

of a strong factor's lag-operator eigenvalue, before any sampling or geometry
error enters.

The N-RANK DGP fixes the total factor-scale norm at \(F\). With weights
\((1,\ldots,1,w)\),

\[
 s_{\rm strong}=\frac{F}{\sqrt{r-1+w^2}},
 \qquad
 s_{\rm tail}=\frac{Fw}{\sqrt{r-1+w^2}},
\]

so the exact weakest signal is

\[
 \boxed{
 \chi_{\rm tail}
 =\frac{F^4w^4}{(r-1+w^2)^2}
 \sum_{h\in\mathcal H}\rho^{2h}.}
\tag{4.2}

This separates two effects that should not be conflated: the \(w^4\) weak
tail and the \((r-1+w^2)^{-2}\) dilution caused by distributing fixed total
energy across more factors. Formula (4.2) is exact for every fixed-rank cell;
it is not itself a growing-rank theorem.

Combining (4.2) with AR1-THR gives the observable sufficient boundary

\[
 \frac{F^4w^4}{(r-1+w^2)^2}
 \sum_{h\in\mathcal H}\rho^{2h}
 >\tau+\eta,
 \qquad d^2<\tau.
\tag{4.3}

For fixed \(r,\rho,\mathcal H\), (4.3) makes the fourth-root nature of
factor-amplitude detectability explicit.

## 5. Rate consequences and the oracle/feasible split

In bounded energy with fixed lag count and \(A_{2,n}=O(1)\), HD1 gives

\[
 \eta_n=2A_{2,n}d_n+d_n^2=O_p(d_n).
\]

On the generic robust moving-centre branch,
\(d_n=O_p(n^{-3/7})\). If persistence stays bounded away from zero and the
threshold is no larger in order, a shrinking marginal factor scale must
satisfy

\[
 s_{\min,n}^4\gg n^{-3/7},
 \qquad\text{equivalently}\qquad
 s_{\min,n}\gg n^{-3/28}.
\tag{5.1}

On a root-\(n\) oracle row, the corresponding sufficient envelope is
\(s_{\min,n}\gg n^{-1/8}\). These are consequences of the proved operator
perturbation bound, not minimax lower bounds; necessity beyond the exact
population-threshold obstruction in AR1-THR is not claimed.

The modular interpretation is now exact. Geometry affects factor-number
selection only through its contribution to \(d_n\) and hence \(\eta_n\).
If \(\chi_{\min}\) lies safely above \(\tau+\eta_n\), oracle and feasible
RFD may have different centre and frame estimates yet make the same discrete
rank decision. If \(\chi_{\min}\le\tau\), the thresholded oracle already
misses the factor, so improved geometry cannot recover it. The completed
N-RANK experiment exhibits both regimes, but the experiment is evidence for
this mechanism rather than part of its proof.

## 6. What this result does and does not settle

**Closed internally:** the exact AR(1) population spectrum; the finite-sample
threshold separation event; the fourth-power weak-tail map; the fixed-total-
energy dilution formula; and the hand-off to HD1's \(d_n,\eta_n,\Delta_n\)
theorems.

**Not claimed:** that thresholding is minimax optimal; that the raw ratio is
consistent; that no estimator can detect a factor below (4.3); that a factor
which improves an application forecast must clear this particular selector;
or that the completed AIRM DGP exhausts geometry, dependence, or
contamination failures. Those are literature-positioning and application
questions, not missing lemmas in AR1-SIG or AR1-THR.
