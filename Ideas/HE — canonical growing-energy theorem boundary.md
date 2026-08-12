---
type: canonical-proof
title: HE — canonical growing-energy theorem boundary
status: canonical-proof
last-audited: 2026-08-12
verdict: the bounded-tail and expanding-domain truncation assumption-to-loading chains are proved with explicit energy, geometry, dependence, target, signal, and gap budgets; the phase windows are sufficient rather than minimax
---

# HE — canonical growing-energy theorem boundary

> **Scope boundary.** HE does not say that arbitrary growing total energy is harmless. It proves recovery only when the complete mean, frame, product-row, target, assembly, and actual-gap ledger closes. The invariant end condition is
> \[
> 2A_{2,n}d_n+d_n^2=o_p(\Delta_n).
> \]
> Stronger signal may pay for growing row error; energy growth alone cannot.

## 1. Targets and typed quantities

In the true anchor Hilbert space let

\[
Y_{t,n}=A_nf_{t,n}+\varepsilon_{t,n},\qquad A_n^*A_n=I_{r_n}.
\]

For the declared clean or actual lag row \(T\in\{0,{\rm act}\}\), keep separate:

\[
\mathcal G_n^T=[\Gamma_n^T(1)\ \cdots\ \Gamma_n^T(h_{0,n})],\quad
\mathbb L_n^T=\mathcal G_n^T(\mathcal G_n^T)^*,
\]

\[
A_{2,n}^T=\Big\{\sum_h\|\Gamma_n^T(h)\|_{\rm op}^2\Big\}^{1/2},\qquad
\Delta_n^T=\lambda_{r_T}(\mathbb L_n^T)-\lambda_{r_T+1}(\mathbb L_n^T).
\]

If \(D_n(h)=\Gamma_n^{\rm act}(h)-\Gamma_n^0(h)\), define

\[
\zeta_n=\Big\{\sum_h\|D_n(h)\|_{\rm op}^2\Big\}^{1/2}.
\]

Estimation of the actual target uses the actual row and gap. Recovery of the clean factor space adds \(\zeta_n\) to the row error and uses the clean row and gap. These targets are never mixed or double-counted.

## 2. Low-level primitive producers

An HE application must supply the following primitives, uniformly over its triangular array.

1. **Generated-domain geometry (HE-G0).** Closed nested geodesically convex sets \(\mathcal C_n\subset\mathcal T_n\) with margin \(\delta_n>0\); support of actual and proxy observations in \(\mathcal C_n\); unique positive barycentres; score coercivity \(\kappa_n I\); and the consumed Exp, Log, Richardson, connector, transport, Jacobi, and ruled-map constants on \(\mathcal T_n\). These constants may grow and must be displayed.
2. **Mean producers (HE-M).** Third-order post-cancellation bias \(B_{3,n}\), level local-stationarity defect, design defect, Hilbert RMS score budget \(\Theta_{S,2,n}\), and a separately justified supremum/tube score budget \(\Theta_{S,\infty,n}\).
3. **Frame producers.** Mean-curve speed and acceleration, polygon size \(M_n\), endpoint-connector defects, and the required stage, vertex, chord, and ruled-surface localization inequalities against \(\delta_n\).
4. **Product-row dependence.** Either typed finite-memory product variance budgets or causal Hilbert/HS physical-dependence budgets for \(Y_t\otimes Y_{t-h}\). Score dependence does not imply product dependence.
5. **Energy and target.** Empirical retained-edge RMS energy \(\mathcal E_{2,n}\), lag count, mask/discretisation defects, included-lag contamination \(\zeta_n\), declared target rank, \(A_{2,n}\), and the actual eigengap \(\Delta_n>0\).

An almost-sure envelope \(\|Y_{t,n}\|\le R_n\) is one sufficient way to construct some budgets; it is not interchangeable with variance-sensitive score or product bounds.

## 3. Alternative expanding-domain truncation primitives

The unbounded route replaces fixed generated domains by deterministic clipping levels \(T_n\) and nested domains \(\mathcal C_n(T_n)\subset\mathcal T_n(T_n)\). It additionally assumes:

- a row-wide unconditional escape bound
  \[
  N_{X,n}\pi_{X,n}(T_n)+N_{Y,n}\pi_{Y,n}(T_n)\to0;
  \]
- all geometry constants and margins on \(\mathcal T_n(T_n)\);
- clipped-score dependence and concentration;
- explicit population score bias \(b_{S,n}(T_n)\);
- explicit product bias \(b_{W,n}(T_n)\) and clipped-product dependence.

The proof is performed on separately clipped arrays and transferred back on the no-clipping event. It never conditions the original dependent row on that event. Tail decay does not produce expanding-domain geometry.

## 4. Conditionally derived producers

| Producer | Status | Derived from | Not supplied by |
|---|---|---|---|
| complete generated-set event | derived conditionally | HE-G0 plus positive-stage, Richardson, grid, chord, and margin inequalities | bare Hadamard geometry or an energy bound |
| centre/grid RMS \(r_{\mu,n}\) and supremum \(r_{\infty,n}\) | derived conditionally | scale cancellation, score coercivity, typed bias/score/LS/design budgets | coordinatewise concentration |
| non-rigid polygon frame \(r_{F,n}\) | derived conditionally | grid RMS, curve speed/acceleration, polygon area, Jacobi/curvature constants, connector defects | centre error alone |
| feasible observation RMS \(q_{R,n}\) | derived conditionally | base-Log, frame, energy, connector, and reconstruction bounds | \(r_{\mu,n}\) alone |
| oracle row \(\omega_n\) | derived conditionally | finite-memory product variance or causal product physical dependence | score dependence or second moments alone |
| feasible row \(d_n\) | derived conditionally | \(\omega_n,q_{R,n},\mathcal E_{2,n}\), masks, discretisation, and target defect | geometry alone |
| assembly, loading, null square, selectors | deterministic consequences | \(d_n,A_{2,n},\Delta_n\), exact target rank, and selector separation | a leading signal eigenvalue alone |

An application may verify a high-level rate in this table directly instead of invoking its low-level derivation, but it must declare that abstraction level and may not count the same rate as both an assumption and an independent conclusion.

## 5. Canonical HE theorem

Under the primitives of §2 and the derived generated event,

\[
r_{\mu,n}=\frac{L_{\mathcal R,n}}{\kappa_n}
\left\{B_{3,n}b_n^3+\frac{\Theta_{S,2,n}}{\sqrt{nb_n}}
+L_{{\rm LS},n}+\frac{G_n}{n}\right\},
\tag{HE.0}
\]

with the analogous supremum-score substitution defining \(r_{\infty,n}\). Then

\[
r_{F,n}=J_n\Lambda_n\{L_{\mu,n}r_{\mu,n}
+M_nr_{\mu,n}^2+K_{\mu,n}M_n^{-2}\}+\rho_{F,n},
\]

and the full feasible tangent-observation error is

\[
q_{R,n}\lesssim
L_{\log,n}\{r_{\mu,n}+K_{\mu,n}M_n^{-2}\}
+r_{F,n}\{\mathcal E_{2,n}+L_{\log,n}r_{\mu,n}\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\tag{HE.1}
\]

With variance-sensitive oracle-row rate \(\omega_n\),

\[
d_{{\rm samp},n}=O_p\!\left[
\omega_n+\sqrt{h_{0,n}}\{2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2\}
+\rho_{{\rm mask},n}+\rho_{{\rm disc},n}
\right].
\tag{HE.2}
\]

Use \(d_n^{\rm act}=d_{{\rm samp},n}\) for the actual target and \(d_n^0\le d_{{\rm samp},n}+\zeta_n\) for the clean target. For either consistently matched target \(T\),

\[
\|\widehat{\mathbb L}_n-\mathbb L_n^T\|_{\rm op}
\le\eta_n^T:=2A_{2,n}^Td_n^T+(d_n^T)^2.
\tag{HE.3}
\]

If \(\eta_n^T=o_p(\Delta_n^T)\), then

\[
\|\sin\Theta(\widehat E_n,E_n^T)\|_{\rm op}
\le \frac{2\eta_n^T}{\Delta_n^T},
\qquad
\widehat\lambda_{r_T+1,n}\le(d_n^T)^2.
\tag{HE.4}
\]

Threshold selection requires \((d_n^T)^2=o_p(\tau_n)\ll\Delta_n^T\) together with the assembly/gap condition. A ridged ratio additionally requires a lower bound on adjacent nonzero population ratios. No raw-ratio conclusion follows from these rates alone.

Under the truncation primitives of §3, the same theorem holds with clipped score/product budgets, \(b_{S,n}(T_n)\) added to the mean ledger, \(\sqrt{h_{0,n}}b_{W,n}(T_n)\) added to the target-row ledger, and every geometry constant evaluated on \(\mathcal T_n(T_n)\).

## 6. Sufficient phase corollaries

Under fixed lag/rank/memory, fixed clean gap, uniform geometry, negligible named defects, and \(R_n\asymp\mathcal E_{2,n}=n^\rho\), balancing with \(b_n=n^{-(1-2\rho)/7}\) gives:

- flat or supplied rigid frame:
  \[
  d_n=O_p\{n^{-(3-13\rho)/7}+n^{-(a-\rho)}\},
  \qquad \rho<3/13, a>\rho;
  \]
- generic curved moving frame:
  \[
  d_n=O_p\{n^{-(3-20\rho)/7}+n^{-(a-2\rho)}\},
  \qquad \rho<3/20, a>2\rho.
  \]

These are sufficient envelope windows, not minimax boundaries. The pure balanced headline in either branch needs the separately stated stronger local-stationarity inequality.

A sub-Weibull truncation corollary may take

\[
T_n=K_n\{c\log N_n\}^{1/\alpha},\qquad c>1,
\]

provided the exact tail integrals, expanding-domain constants, closure inequalities, and final gap ratio all close. This is not a minimal-moment theorem.

## 7. Nonemptiness, failures, and application boundary

The explicit pervasive flat model has \(R_n\asymp\sqrt{p_n}\), \(A_{2,n}\asymp p_n\), \(\Delta_n\asymp p_n^2\), and row error of order \(p_n/\sqrt n\); the exact assembly/gap ratio is root-\(n\). This proves that signal can pay for energy.

The following shortcuts are analytically rejected:

- coordinatewise bounds in place of Hilbert/HS budgets;
- arbitrary growing energy with a fixed gap;
- normalisation without recomputing the estimand, row, \(A_2\), and \(\Delta\);
- coloured included-lag noise treated as harmless;
- unrestricted growing rank without its minimum gap and selector window;
- \(d_n/\Delta_n\) in place of \((2A_{2,n}d_n+d_n^2)/\Delta_n\).

No asset, sensor, gene, imaging, or covariance application inherits HE from its label. It must instantiate the geometry, energy/tail, product-dependence, target, and gap producers above.

## 8. Proof provenance

The bounded-tail derivations, phase models, and counterexamples are in [[HE — growing energy and pervasive signal working dossier]]. The expanding-domain proof is [[HE-TRUNC — unbounded-score truncation and generated-domain proof]]. The shared typed hostile audit is [[Joint HE-BW error ledger and hostile audit]]. Those archived files are citable proof provenance; this file is the canonical theorem boundary and producer classification.
