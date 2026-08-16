---
type: canonical-proof
title: BW-SHRINKING-MARGIN — canonical restricted theorem boundary
status: canonical-proof
last-audited: 2026-08-12
verdict: the shrinking-margin theorem is proved on a complete restricted fractional-normal package with termwise geometry, mean, frame, row, signal, and gap budgets; its polynomial window is sufficient and no universal geometry-only matrix-size ceiling exists
---

# BW-SHRINKING-MARGIN — canonical restricted theorem boundary

> **Scope boundary.** This is not an unrestricted theorem for BW matrices approaching rank loss. It is a local full-rank triangular-array theorem whose observations, score pairs, generated maps, polygon cells, and reconstructions retain strict fractional-normal slack. Fixed or growing tangent energy is incompatible with this shrinking full-noncommuting normal-pair package. Global/rank-changing PSD and pervasive shrinking-normal claims remain excluded.

## 1. Primitive fractional-normal package

Let the complete checked generated domain \(\mathcal D_n\) have lower spectral margin \(\alpha_n>0\), upper margin \(\beta_n\), polar cross-Gram margin \(\chi_{{\rm P},n}\), Exp-factor margin \(\chi_{{\rm E},n}\), normal radius \(\rho_{H,n}\), path/cell margins, and generated-set slack \(\delta_{{\rm GD},n}\). Polar and Exp margins have different homogeneity and are never represented by one untyped \(\chi_n\).

The application supplies:

1. strict fractional slack for every actual/proxy score pair and every population/empirical stage, Richardson/blend output, chord, connector, ODE path, ruled cell, and reconstruction;
2. positive score-pair slack
   \[
   s_{H,n}=\rho_{H,n}-\sup_{(q^0,X)}d_{\rm BW}(q^0,X)>0,
   \qquad
   \delta_{*,n}=\min\{\delta_{{\rm GD},n},s_{H,n}\};
   \]
3. support and retained-edge energy compatible with the normal domain,
   \[
   R_{X,n}^{\sup},\mathcal E_{2,n}=O(\sqrt{\alpha_n});
   \]
4. typed cubic bias, Hilbert score RMS/supremum, local-stationarity, design, speed, acceleration, connector, and object-count budgets;
5. finite-memory or causal Hilbert/HS product-dependence budgets, lag count, masks, discretisation, and included-lag target defect \(\zeta_n\);
6. a declared target rank, \(A_{2,n}\), actual eigengap \(\Delta_n>0\), and selector threshold or ridge conditions.

If unbounded observations are treated by HE-TRUNC, every expanding-domain constant, row-wide escape probability, score bias, and product bias is added explicitly. Tail decay alone does not supply the fractional-normal geometry.

## 2. Derived local geometry producers

On the package of §1, the proved local coefficients are

\[
K_S,K_{R1},K_G,K_{L1},K_C=O(1),\qquad
K_B=O(1+\alpha_n^{-1}),
\]

\[
K_{L2}=O(\alpha_n^{-1/2}),\qquad
K_F=O(\alpha_n^{-1}),\qquad
\rho_{H,n}=O(\sqrt{\alpha_n}).
\tag{BWS.1}
\]

Their roles remain termwise:

| Producer | Status | Exact role | Forbidden simplification |
|---|---|---|---|
| score coercivity and first local Log/Richardson actions | derived, \(O(1)\) | leading Hilbert score fluctuation and first-order recentering | multiply all stochastic terms by \(\alpha_n^{-1}\) |
| cubic bias action \(K_B\) | derived sufficient | deterministic third-order population bias | treat it as the score coefficient |
| quadratic Log action \(K_{L2}\) | derived sufficient | quadratic centre remainder | omit \(r_{\mu,n}^2\) near the boundary |
| PF action \(K_F\) | derived and sharp on the noncommuting class | ruled-cell curvature/area term | hide it in a dimension-free constant |
| normal radius | derived order \(\sqrt{\alpha_n}\) | score-pair and generated-domain support | infer a larger uniform full-rank radius |

The primitive floors \(D^k\mathscr S_G^{-1}\asymp\alpha_n^{-(k+1)}\), \(D_L^kP_L^{\mathcal H}\asymp\alpha_n^{-k/2}\), and \(\nabla^kR^{\rm BW}\asymp\alpha_n^{-(k+2)/2}\) are proved in their typed raw/intrinsic norms. No direct matrix-size factor is added unless it enters through margins, energy, signal, path/object counts, or an independently proved conversion.

## 3. Conditionally derived statistical producers

Define the mean rates termwise:

\[
r_{\mu,n}
=K_{B,n}B_{3,n}b_n^3
+K_{R1,n}K_{S,n}
\left\{\frac{\Theta_{S,2,n}}{\sqrt{nb_n}}
+L_{{\rm LS},n}+G_n/n\right\},
\tag{BWS.2}
\]

with the analogous supremum score budget defining \(r_{\infty,n}\). The complete generated event additionally requires stage/supremum localization and

\[
K_{G,n}\left\{
\sqrt{M_n+1}\,r_{\mu,n}
+\frac{v_{\mu,n}}{M_n}
+a_{\mu,n}M_n^{-2}
+r_{{\rm con},\max,n}
\right\}=o(\delta_{*,n}),
\tag{BWS.3}
\]

or a separately proved supremum-grid alternative, together with the actual object-count escape event.

The non-rigid polygon frame is

\[
r_{F,n}=K_{F,n}\left\{
v_{\mu,n}r_{\mu,n}
+(M_n+1)r_{\mu,n}^2
+v_{\mu,n}a_{\mu,n}M_n^{-2}
\right\}+\rho_{F,n}.
\tag{BWS.4}
\]

The connector-aligned feasible observation rate is

\[
\begin{aligned}
q_{R,n}\lesssim{}&
K_{L1,n}\{r_{\mu,n}+a_{\mu,n}M_n^{-2}\}
+K_{L2,n}\{r_{\mu,n}+a_{\mu,n}M_n^{-2}\}^2\\
&+K_{C,n}r_{F,n}\{\mathcal E_{2,n}
+K_{L1,n}r_{\mu,n}+K_{L2,n}r_{\mu,n}^2\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\end{aligned}
\tag{BWS.5}
\]

Thus centre RMS, generated-set closure, frame error, and feasible-observation error are separate outputs. None follows merely from \(\alpha_n>0\).

## 4. Canonical restricted theorem

Let \(\omega_n\) be the variance-sensitive oracle product-row rate under the supplied finite-memory or causal physical-dependence producer. Then

\[
d_n=O_p\left[
\omega_n+\sqrt{h_{0,n}}\{2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2\}
+\zeta_n+\rho_{{\rm mask},n}+\rho_{{\rm disc},n}
\right].
\tag{BWS.6}
\]

For the consistently declared clean or actual target,

\[
\|\widehat{\mathbb L}_n-\mathbb L_n\|_{\rm op}
\le\eta_n:=2A_{2,n}d_n+d_n^2.
\tag{BWS.7}
\]

If \(\eta_n=o_p(\Delta_n)\), then

\[
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
\le\frac{2\eta_n}{\Delta_n}.
\tag{BWS.8}
\]

Under exact rank-\(r_n\) lag factorisation,

\[
\widehat\lambda_{r_n+1,n}\le d_n^2.
\tag{BWS.9}
\]

Threshold selection requires \(d_n^2=o_p(\tau_n)\ll\Delta_n\) and the assembly/gap condition. A ridged ratio additionally requires nonzero adjacent population ratios bounded below. No raw-ratio conclusion follows.

This is a proved assumption-to-conclusion chain on the restricted fractional-normal class. An application may invoke high-level rates such as (BWS.2)--(BWS.6) directly, but then those rates are supplied assumptions rather than independently rederived conclusions.

## 5. Conservative polynomial corollary

Take

\[
\alpha_n\asymp m_n^{-A},\qquad m_n=n^x,
\]

with proportional spectral/factor/polar/Exp/normal slacks, support and score scale \(O(\sqrt{\alpha_n})\), fixed lag/dependence, negligible named defects, bounded cubic law budget, and a rank-one target satisfying

\[
A_{2,n}\asymp\alpha_n,\qquad \Delta_n\asymp\alpha_n^2.
\]

The termwise balance gives

\[
b_n=n^{-(1+3Ax)/7},\qquad
r_{\mu,n}=n^{-(3+2Ax)/7+o(1)}.
\]

Stage localization allows \(x<2/A\), grid/local-cell closure allows \(x<12/(13A)\), and the final PF/loading/selector requirement \(r_{\mu,n}=o(\alpha_n)\) yields

\[
\boxed{0<x<\frac{3}{5A}.}
\tag{BWS.10}
\]

This is sufficient, not minimax and not a universal maximum matrix-size law.

## 6. Nonemptiness and impossibility boundary

A self-similar construction embeds one fixed noncommuting active block and scales its law, path jets, support, energy, and signal with \(a_n=\sqrt{\alpha_n}\), while additional coordinates are deterministic. With \(M_n\asymp n^{2/7}\),

\[
r_{\mu,n}=O(a_nn^{-3/7}),\quad
r_{F,n}=O(n^{-3/7}),\quad
d_n=O(\alpha_nn^{-3/7}),\quad
\eta_n/\Delta_n=O(n^{-3/7}).
\]

It permits any fixed polynomial inactive dimension. This proves logical attainability and disproves a geometry-only \(m_n\)-ceiling; it is not a pervasive or growing-active-dimension theorem.

The hostile passes rule out within the stated full-noncommuting class:

- a uniform full-rank normal/generated radius larger than order \(\sqrt{\alpha_n}\);
- a PF curvature coefficient \(o(\alpha_n^{-1})\);
- fixed or growing tangent energy inside the shrinking support package;
- generated-set authorization from RMS grid error without object-count/supremum control;
- loading or factor selection without the actual assembly/gap and row-square windows;
- repeated positive eigenvalues as a BW singularity margin.

Rank loss remains the boundary. Signal cannot repair geometric escape.

## 7. Optional open sharpness problems

U-D1--U-D4 ask for smallest unrestricted nonlocal factored-alignment powers, sharp nonlocal Jacobi envelopes, smallest higher generated-map powers, and a minimized closed polynomial for all higher endpoint-PT derivatives. The proved finite recurrences and the fractional-normal restriction bypass these minimisations.

These problems block a globally sharp unrestricted monomial and a sharp universal growth window. They do not block the theorem in §4 or corollary (BWS.10).

## 8. Proof provenance

Primitive sharp/sufficient exponents are in [[BW-SIZE-SHRINKING-MARGIN — Agent D primitive sharp exponents]]. Statistical propagation and phase windows are in [[BW-SIZE-SHRINKING-MARGIN — Agent E statistical propagation and growth windows]]. Independent counterexamples and both hostile passes are in [[BW-SIZE-SHRINKING-MARGIN — Agent F sharpness and impossibility audit]]. The final adjudication is [[BW-SIZE-SHRINKING-MARGIN — lead dependency and exponent ledger]]. The fixed-margin prerequisite is classified in [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]]. Those archived dossiers are citable proof provenance; this file is the canonical theorem boundary and producer classification.
