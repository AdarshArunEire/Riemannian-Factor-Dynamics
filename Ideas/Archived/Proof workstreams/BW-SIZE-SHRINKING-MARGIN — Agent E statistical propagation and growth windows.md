---
type: noncanonical-working-proof-dossier
title: BW-SIZE-SHRINKING-MARGIN — Agent E statistical propagation and growth windows
status: cross-audit-pass-1-complete-mutual-repairs-integrated-awaiting-hostile-pass
authority: noncanonical-agent-e-only
stage: 2-shrinking-margin
---

# BW-SIZE-SHRINKING-MARGIN — Agent E statistical propagation and growth windows

> **NONCANONICAL / AGENT E.** This is an independent propagation of typed symbolic geometry coefficients through the complete statistical chain. It imports no Stage 1 power as sharp. Agent D must fill the margin-power interfaces; Agent F must then audit them and the substitutions.

## 0. Independent-pass verdict

Once shrinking-margin geometry supplies the six typed coefficients in Section 1, the statistical chain closes by the exact monotone formulas below. Matrix size has no extra direct factor in the project Hilbert/Frobenius/operator norms. It enters only through:

1. spectral, polar/Exp, normal-pair, and generated-domain margins;
2. tangent energy and score/product-dependence budgets;
3. generated-object count, PF grid size, and retained lags;
4. lag-row magnitude \(A_{2,n}\) and the actual gap \(\Delta_n\).

The final condition is

\[
\eta_n=2A_{2,n}d_n+d_n^2=o_p(\Delta_n).
\tag{E.0}
\]

Replacing it by \(d_n=o_p(\Delta_n)\), or dividing by a factor-lag singular value before proving the relevant gap inequality, is invalid.

## 1. Typed geometry interface

Let \(\mathcal D_n\) be the complete checked BW generated domain, with spectral band \([\alpha_n,\beta_n]\), polar cross-Gram margin \(\chi_{{\rm P},n}\), Exp/factor margin \(\chi_{{\rm E},n}\), normal-pair radius \(\rho_{{\rm nor},n}\), path-length bound \(r_{0,n}\), and generated-set slack \(\delta_{{\rm GD},n}>0\). The polar margin has eigenvalue units, while the Exp margin has lift-singular-value units. Repeated positive eigenvalues are not a margin.

| Slot | Typed meaning | Consumer |
|---|---|---|
| \(K_{S,n}\) | inverse positive-stage score coercivity, including common-base norm conversion | stage localisation |
| \(K_{B,n}\) | deterministic third-order population bias/change-of-base coefficient after the scale cancellations | cubic bias only |
| \(K_{\mathcal R,n}\) | first derivative/Lipschitz coefficient of Richardson and the fixed-width blend on the generated tuple | propagation of stage errors |
| \(K_{G,n}\) | complete generated-tuple perturbation/membership coefficient | domain event |
| \(K_{L1,n}\) | first-order base/observation Log and recentering coefficient | feasible observations |
| \(K_{L2,n}\) | quadratic Log/recentring remainder coefficient | feasible-observation remainder |
| \(K_{F,n}\) | canonical ruled-cell curvature/Jacobi/PF coefficient | frame |
| \(K_{C,n}\) | endpoint connector/trivialisation coefficient not absorbed above | frame/observations |

The leading Hilbert score fluctuation pays \(K_{S,n}\) and the first derivative \(K_{\mathcal R,n}\), not a third-order curvature coefficient. The latter belongs only to the deterministic cubic bias/remainder. Agent D must provide exact formulas or justified bounds such as

\[
K_{Z,n}\le C_Z
\alpha_n^{-p_{Z,\alpha}}\beta_n^{p_{Z,\beta}}
\chi_{{\rm P},n}^{-p_{Z,P}}
\chi_{{\rm E},n}^{-p_{Z,E}}
\rho_{{\rm nor},n}^{-p_{Z,\rho}},
\qquad Z\in\{S,B,\mathcal R,G,L1,L2,F,C\},
\tag{E.1}
\]

while preserving the true max/additive/product structure. Equation (E.1) is one illustrative product monomial, not a claim that the real dependence is a single monomial or has those powers.

## 2. Mean localisation and G1

Write \(h_n\) for bandwidth. Let \(\mathcal O_n\ge1\) count independently indexed stage/grid/domain tests not already covered by the one-dimensional time interpolation. Define

\[
\begin{aligned}
\mathfrak s_{1,n}
&=B_{1,n}h_n+
\Theta_{S,\infty,n}\sqrt{\frac{\log(n\mathcal O_n)}{nh_n}}
+L_{{\rm LS},n}+G_n/n,\\
\mathfrak s_{3,2,n}
&=B_{3,n}h_n^3+
\frac{\Theta_{S,2,n}}{\sqrt{nh_n}}
+L_{{\rm LS},n}+G_n/n,\\
\mathfrak s_{3,\infty,n}
&=B_{3,n}h_n^3+
\Theta_{S,\infty,n}\sqrt{\frac{\log(n\mathcal O_n)}{nh_n}}
+L_{{\rm LS},n}+G_n/n.
\end{aligned}
\tag{E.2}
\]

Put

\[
u_{{\rm stg},n}=K_{S,n}\mathfrak s_{1,n},
\tag{E.3a}
\]

\[
\begin{aligned}
r_{\mu,n}
&=K_{B,n}B_{3,n}h_n^3
+K_{\mathcal R,n}K_{S,n}
\left\{\frac{\Theta_{S,2,n}}{\sqrt{nh_n}}
+L_{{\rm LS},n}+G_n/n\right\},\\
r_{\infty,n}
&=K_{B,n}B_{3,n}h_n^3
+K_{\mathcal R,n}K_{S,n}
\left\{\Theta_{S,\infty,n}
\sqrt{\frac{\log(n\mathcal O_n)}{nh_n}}
+L_{{\rm LS},n}+G_n/n\right\}.
\end{aligned}
\tag{E.3}
\]

The positive-stage score inequality, scale identities, and Richardson map give

\[
\|\log_{\mu_n}\widehat\mu_n^{(3)}\|_{L^2}=O_p(r_{\mu,n}),\qquad
\sup_u d(\widehat\mu_n^{(3)}(u),\mu_n(u))=O_p(r_{\infty,n}),
\tag{E.4}
\]

and the same \(O_p(r_{\mu,n})\) RMS bound on every deterministic grid.

For HE-TRUNC, add \(b_{S,n}(T_n)\) inside each brace, use clipped score budgets, and impose the unconditional row-wide escape condition (E.7). Tail decay does not bound any \(K_{Z,n}\).

## 3. Complete generated event, object count, and grid slack

Let \(M_n+1\) be the PF vertex count and let \(a_{\mu,n}\) bound true mean acceleration. Normal-pair membership must include actual and proxy observations. Define

\[
s_{H,n}:=\rho_{{\rm nor},n}
-\sup\{d_{\rm BW}(q^0,x):
(q^0,x)\text{ is a consumed population/proxy score pair}\},
\qquad
\delta_{*,n}:=\min\{\delta_{{\rm GD},n},s_{H,n}\}.
\tag{E.5a}
\]

A nonempty theorem requires \(s_{H,n}>0\). Sufficient complete-domain conditions are

\[
K_{G,n}u_{{\rm stg},n}=o(\delta_{*,n}),\qquad
K_{G,n}r_{\infty,n}=o(\delta_{*,n}),
\tag{E.5}
\]

\[
K_{G,n}\left\{
\sqrt{M_n+1}\,r_{\mu,n}
+\frac{v_{\mu,n}}{M_n}
+a_{\mu,n}M_n^{-2}
+r_{{\rm con},\max,n}
\right\}=o(\delta_{*,n}).
\tag{E.6}
\]

Under the almost-sure support version of positive G1, a simpler sufficient pair condition is

\[
R_{X,n}^{\sup}:=
\sup_{t,\mathrm{proxy}}d_{\rm BW}(\mu_n(u_t),X_{t,n})
\le c\,\rho_{{\rm nor},n},\qquad c<1,
\tag{E.6a}
\]

together with stage displacement \(o(\rho_{{\rm nor},n})\). It implies \(\mathcal E_{2,n}\le R_{X,n}^{\sup}\). Thus a shrinking produced normal radius can force support and total tangent energy to shrink. The expanding-domain/truncation route must impose the analogous condition on clipped score pairs; tail control alone does not remove it.

The \(\sqrt{M_n+1}\) factor is necessary under only a grid RMS bound. It disappears only if a sup-grid bound is proved. The \(v_{\mu,n}/M_n\) term certifies that each true chord/ruled cell is fractional-normal; total path length alone does not. The term \(r_{{\rm con},\max,n}\) is the maximum connector endpoint displacement not already bounded by the vertex maximum. Conditions (E.5)–(E.6a) must cover every band, polar cross-Gram, Exp, score pair, Richardson/blend, chord, connector, ruled surface, and reconstruction test.

For probabilistic raw/proxy domains, additionally require

\[
\mathcal O_{X,n}\pi_{X,n}+\mathcal O_{Y,n}\pi_{Y,n}=o(1),
\tag{E.7}
\]

where the counts include every actual/proxy and retained-row endpoint. This is an unconditional union bound; one must not condition the dependent row on no escape.

The canonical choice

\[
M_n\asymp r_{\mu,n}^{-2/3}
\tag{E.8}
\]

balances \(M_nr_{\mu,n}^2\) and \(M_n^{-2}\). Its RMS-to-max cost is \(r_{\mu,n}^{2/3}\), which can hit a shrinking domain margin before the mean RMS rate fails.
This is the canonical fixed-margin choice, not a universal shrinking-margin optimum. When path speed, acceleration, curvature, and slack scale together, \(M_n\) should instead be chosen from the full inequalities (E.6) and (E.9); Section 7.4 gives one such choice.

## 4. Polygonal frame

Let \(v_{\mu,n}:=\sup_{u\in[0,1]}\|\dot\mu_n(u)\|_{\rm BW}\) be the typed supremum speed. It implies both total length at most \(v_{\mu,n}\) on the unit interval and the uniform-grid cell bound \(\ell_j\le v_{\mu,n}/M_n\). Total length alone would not imply that cellwise bound and is not substituted here. The frozen Stage 1 PF inequality gives, after endpoint connectors,

\[
r_{F,n}:=
K_{F,n}\left\{
v_{\mu,n}r_{\mu,n}+(M_n+1)r_{\mu,n}^2
+v_{\mu,n}a_{\mu,n}M_n^{-2}
\right\}+\rho_{F,n}.
\tag{E.9}
\]

There is no hidden \(K^{M_n}\): PT is isometric and ruled-cell variation is additive. A generic independently parameterised polygon derivative instead retains its visible Bell-polynomial \(M_n+\mathsf L_n\) dependence and cannot replace (E.9).

With \(v_{\mu,n},a_{\mu,n}=O(1)\) and (E.8),

\[
r_{F,n}=O_p\{K_{F,n}(r_{\mu,n}+r_{\mu,n}^{4/3})+\rho_{F,n}\}.
\tag{E.10}
\]

Thus \(K_{F,n}r_{\mu,n}=o(1)\) is separate. In a supplied common flat/rigid frame set \(r_{F,n}=0\); small curvature or repeated eigenvalues do not imply rigidity.

## 5. Feasible observations and lag rows

Let \(\mathcal E_{2,n}\) be oracle tangent-energy RMS on every retained mask. The connector-aligned feasible observation error is

\[
\boxed{
q_{R,n}\lesssim
K_{L1,n}\{r_{\mu,n}+a_{\mu,n}M_n^{-2}\}
+K_{L2,n}\{r_{\mu,n}+a_{\mu,n}M_n^{-2}\}^2
+K_{C,n}r_{F,n}
\left\{\mathcal E_{2,n}
+K_{L1,n}r_{\mu,n}
+K_{L2,n}r_{\mu,n}^2\right\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.}
\tag{E.11}
\]

Agent D's local interface gives \(K_{L1,n}=O(1)\) and
\(K_{L2,n}=O(\alpha_n^{-1/2})\). The quadratic term is absorbed by
the first-order term only after \(r_{\mu,n}=o(\sqrt{\alpha_n})\).
The frame multiplies energy. Hence feasible error is not merely centre
error unless the frame is rigid or all relevant inputs are uniformly
bounded.

Retain the variance-sensitive oracle row rate

\[
\omega_n^2=
\sum_{h\le h_{0,n}}\frac{(2d_{h,n}+1)v_{h,n}^2}{N_{n,h}}
\quad\text{or}\quad
\sum_{h\le h_{0,n}}\frac{\Theta_{2,W_h,n}^2}{N_{n,h}},
\tag{E.12}
\]

for finite memory or causal physical dependence. Under only \(\|Y_t\|\le R_n\), fixed lag/memory gives the coarser \(\omega_n=O(R_n^2/\sqrt n)\).

The pathwise feasible product expansion gives

\[
\boxed{
d_n=O_p\left[
\omega_n+\sqrt{h_{0,n}}\{2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2\}
+\zeta_n+\rho_{{\rm mask},n}+\rho_{{\rm disc},n}
\right].}
\tag{E.13}
\]

For clipping, add \(\sqrt{h_{0,n}}b_{W,n}(T_n)\), use \(\omega_n^{[T]}\), and keep the declared untruncated target.

## 6. Assembly, Davis–Kahan, null spectrum, and selection

Define

\[
A_{2,n}=\left\{\sum_{h\le h_{0,n}}\|\Gamma_n(h)\|_{\rm op}^2\right\}^{1/2},
\quad
\mathbb L_n=\sum_h\Gamma_n(h)\Gamma_n(h)^*,
\tag{E.14}
\]

and, for the declared target rank \(r_n\),

\[
\Delta_n=\lambda_{r_n}(\mathbb L_n)-\lambda_{r_n+1}(\mathbb L_n)>0.
\tag{E.15}
\]

Row assembly gives exactly

\[
\|\widehat{\mathbb L}_n-\mathbb L_n\|_{\rm op}
\le\eta_n:=2A_{2,n}d_n+d_n^2.
\tag{E.16}
\]

If \(\eta_n=o_p(\Delta_n)\), Davis–Kahan yields

\[
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
\le \frac{2\eta_n}{\Delta_n}.
\tag{E.17}
\]

Under exact lag factorisation, \(\lambda_{r_n+1}(\mathbb L_n)=0\), and row min–max—not Weyl alone—gives

\[
\widehat\lambda_{r_n+1,n}\le d_n^2,\qquad
|\widehat\lambda_{j,n}-\lambda_{j,n}|=O_p(\eta_n),\quad j\le r_n.
\tag{E.18}
\]

For deterministic \(\bar d_n\) with \(d_n=O_p(\bar d_n)\), a threshold selector is consistent if

\[
\bar d_n^2=o(\tau_n),\qquad
\tau_n=o(\Delta_n),\qquad
2A_{2,n}\bar d_n+\bar d_n^2=o(\Delta_n).
\tag{E.19}
\]

If \(\bar d_n^2=o(\Delta_n)\), one explicit threshold is

\[
\tau_n=(\bar d_n^2\Delta_n)^{1/2}.
\tag{E.20}
\]

A ridged ratio also requires adjacent nonzero population eigenvalue ratios bounded below. The raw ratio remains disproved.

## 7. Power-law propagation and explicit \(m_n\)-versus-\(n\) windows

These windows are sufficient, not sharp. Set

\[
m_n=n^x,\quad
\alpha_n\asymp m_n^{-a},\quad
\beta_n\asymp m_n^b,\quad
\chi_{{\rm P},n}\asymp m_n^{-c_P},\quad
\chi_{{\rm E},n}\asymp m_n^{-c_E},\quad
\rho_{{\rm nor},n}\asymp m_n^{-d_\rho},\quad
\delta_{*,n}\asymp m_n^{-d_*}.
\tag{E.21}
\]

After Agent D fills the primitive powers, write

\[
K_{Z,n}\lesssim m_n^{g_Z},\qquad
g_Z=ap_{Z,\alpha}+bp_{Z,\beta}
+c_Pp_{Z,P}+c_Ep_{Z,E}+d_\rho p_{Z,\rho}.
\tag{E.22}
\]

Assume

\[
\mathcal E_{2,n}\asymp
\Theta_{S,2,n}\asymp\Theta_{S,\infty,n}\asymp m_n^e,\qquad
\omega_n=O(m_n^{g_\omega}n^{-1/2}),
\tag{E.23}
\]

where \(e\) is signed. Under the almost-sure normal-pair package, (E.6a) and \(\rho_{{\rm nor},n}\asymp m_n^{-d_\rho}\) require

\[
e\le-d_\rho
\tag{E.23a}
\]

when the score and energy scales are comparable. Thus an arbitrary growing-energy exponent \(e>0\) is incompatible with a shrinking produced normal radius. Let

\[
K_{B,n}\lesssim m_n^{g_B},\qquad
K_{\mathcal R,n}K_{S,n}\lesssim m_n^{g_V}.
\tag{E.23b}
\]

With bounded \(B_1,B_3\), typed supremum speed \(v_\mu\), acceleration \(a_\mu\), and smaller LS/design/defect terms, balancing the separately weighted cubic bias and score variance gives

\[
h_n=n^{-y},\qquad
y=\frac{1-2x(g_V+e-g_B)}7>0,
\tag{E.24}
\]

\[
r_{\mu,n}=n^{-\zeta_\mu+o(1)},\qquad
\zeta_\mu=\frac{3-x(g_B+6g_V+6e)}7.
\tag{E.25}
\]

The uncancelled stage radius is slower:

\[
u_{{\rm stg},n}=O\left(m_n^{g_S}n^{-y}\right).
\tag{E.26}
\]

Sufficient generated-domain conditions are

\[
x<\frac{1}{
7(g_G+g_S+d_*)+2(g_V+e-g_B)},
\tag{E.27}
\]

and, from the RMS grid maximum under (E.8),

\[
x<\frac{6}{
2(g_B+6g_V+6e)+21(g_G+d_*)}.
\tag{E.28}
\]

The quotient forms (E.27)–(E.28) are used only when their displayed
denominators are positive. With signed shrinking energy or
model-specific shrinking law jets, use the underlying exponent
inequalities before division.

Define

\[
g_Q=\max\{g_{L1},\ g_C+g_F+e\},\qquad
g_D=\max\{g_{L1}+e,\ g_C+g_F+2e\}.
\tag{E.29}
\]

Here the quadratic Log remainder is assumed absorbed through
\(K_{L2,n}r_{\mu,n}=o(K_{L1,n})\); otherwise it must be added as a
third competing monomial in \(g_Q,g_D\).

Then

\[
q_{R,n}=O_p(m_n^{g_Q}r_{\mu,n}),\qquad
d_n=O_p(m_n^{g_\omega}n^{-1/2}+m_n^{g_D}r_{\mu,n}),
\tag{E.30}
\]

and one row exponent is

\[
\zeta_d=\min\left\{\frac12-xg_\omega,\,
\frac{3-x(g_B+6g_V+6e+7g_D)}7\right\}.
\tag{E.31}
\]

Let

\[
A_{2,n}\asymp m_n^{s_A},\qquad
\Delta_n\asymp m_n^{s_\Delta},
\tag{E.32}
\]

where \(s_\Delta\) is signed. Sufficient loading and selector conditions are

\[
\zeta_d>x(s_A-s_\Delta),
\tag{E.33}
\]

\[
2\zeta_d+xs_\Delta>0.
\tag{E.34}
\]

Together with (E.24), (E.27), and (E.28), these give a nonempty \(0<x<x_{\max}\) whenever the filled powers are finite and the fixed-\(m\) statistical model has positive signal and vanishing defects.

### 7.1 Localised fixed-signal branch

Take \(s_A=s_\Delta=0\), \(g_\omega=2e\), and fixed \(h_0\). In a rigid frame \(g_D=g_{L1}+e\), hence

\[
d_n=O_p\left[
n^{-1/2+2xe}
+n^{-\{3-x(g_B+6g_V+7g_{L1}+13e)\}/7}
\right],
\tag{E.35}
\]

and

\[
x<\frac{3}{g_B+6g_V+7g_{L1}+13e}
\tag{E.36}
\]

is sufficient. Uniform geometry gives \(xe<3/13\), the archived flat HE window.

For a generic curved frame, if \(g_C=0\) and \(g_F+e\ge g_{L1}\),

\[
d_n=O_p\left[
n^{-1/2+2xe}
+n^{-\{3-x(g_B+6g_V+7g_F+20e)\}/7}
\right],
\tag{E.37}
\]

so

\[
x<\frac{3}{g_B+6g_V+7g_F+20e}
\tag{E.38}
\]

is sufficient. Uniform geometry gives \(xe<3/20\), the archived curved HE window. If \(s_A-s_\Delta>0\), add \(7(s_A-s_\Delta)\) to the denominators in (E.36)–(E.38); the oracle term also needs \(1/2>x(g_\omega+s_A-s_\Delta)\).
As above, a nonpositive denominator is not divided through; one
returns to the corresponding exponent inequality.

### 7.2 Pervasive signal branch

If \(A_{2,n}\asymp m_n^s\) and \(\Delta_n\asymp m_n^{2s}\), then

\[
\frac{\eta_n}{\Delta_n}
=O_p\left(\frac{d_n}{m_n^s}+\frac{d_n^2}{m_n^{2s}}\right).
\tag{E.39}
\]

Thus growing row error can be harmless if \(d_n=o_p(m_n^s)\). Requiring \(d_n=o_p(1)\) is stronger than necessary. However, this pervasive branch is admissible under the present BW theorem only if its observation support also satisfies (E.6a). A model with \(\mathcal E_{2,n}\to\infty\) and \(\rho_{{\rm nor},n}\to0\) makes the generated-domain package empty, regardless of signal growth. Generated-domain and mean/frame conditions remain mandatory: signal cannot repair geometric escape.

### 7.3 Fractional-normal BW benchmark from D's verified local powers

Write \(\alpha_n=m_n^{-A}\), so the produced normal radius is
\(\rho_{{\rm nor},n}\asymp\sqrt{\alpha_n}=m_n^{-A/2}\).
On the fractional-normal local theorem, use the termwise coefficients

\[
K_{B,n}\lesssim\alpha_n^{-1}=m_n^A,\qquad
K_{\mathcal R,n}K_{S,n}=O(1),\qquad
\Theta_{S,2,n}\asymp\sqrt{\alpha_n}=m_n^{-A/2}.
\tag{E.39a}
\]

This is the conservative local cubic-bias branch: the normalized law
coefficient \(B_{3,n}\) is held \(O(1)\), rather than assumed to shrink
with the root scale. The termwise balance (E.24)–(E.25) becomes

\[
h_n=n^{-(1+3Ax)/7},\qquad
r_{\mu,n}=n^{-(3+2Ax)/7}.
\tag{E.39b}
\]

Two distinct restrictions follow:

\[
r_{\mu,n}=o(\alpha_n)
\quad\Longleftrightarrow\quad
x<\frac{3}{5A},
\tag{E.39c}
\]

\[
r_{\mu,n}^{2/3}=o(\sqrt{\alpha_n})
\quad\Longleftrightarrow\quad
x<\frac{12}{13A}.
\tag{E.39d}
\]

The first is the generic curved-frame/loading restriction when
\(K_F\asymp\alpha_n^{-1}\), energy is \(O(\sqrt{\alpha_n})\), path
speed is not granted an extra root-scale factor, and
\(A_{2,n}\asymp\alpha_n,\Delta_n\asymp\alpha_n^2\). The second is the
RMS-to-grid/local-cell restriction. Thus \(x<3/(5A)\) is a concrete
nonempty sufficient window for this conservative local branch. A
coefficient obtained by multiplying the score fluctuation by
\(K_B\) would give a different, erroneous balance.

### 7.4 Nonempty self-similar shrinking-margin branch

Let \(a_n=\sqrt{\alpha_n}\downarrow0\). Embed one fixed noncommuting \(2\times2\) block in \(m_n\times m_n\) matrices and keep all remaining root coordinates deterministic. Scale the entire active root-coordinate law, mean speed, acceleration, and support radius by \(a_n\), with fixed fractional band, polar, Exp, and normal-pair slacks:

\[
R_{X,n}^{\sup}\asymp\mathcal E_{2,n}\asymp
v_{\mu,n}\asymp a_n,\qquad
\chi_{{\rm P},n}\asymp\alpha_n,\qquad
\chi_{{\rm E},n}\asymp a_n.
\tag{E.40a}
\]

Use a fixed-rank serial factor of root-coordinate amplitude \(a_n\). Then

\[
A_{2,n}\asymp\alpha_n,\qquad
\Delta_n\asymp\alpha_n^2,\qquad
\omega_n=O(\alpha_n n^{-1/2}).
\tag{E.40b}
\]

Assume the model-specific curvature-sensitive time/law jets scale so
that \(B_{3,n}=O(\alpha_n^{3/2})=O(a_n^3)\), and every direct third
law-score term not multiplied by \(K_{B,n}\) is \(O(a_n)\). Since
\(K_{B,n}=O(\alpha_n^{-1})\), the complete deterministic cubic
coefficient is then \(K_{B,n}B_{3,n}=O(a_n)\), matching the score
scale. With \(h_n=n^{-1/7}\),
\(r_{\mu,n}=O(a_nn^{-3/7})\). Choose \(M_n\asymp n^{2/7}\), rather
than the fixed-margin shorthand \(r_{\mu,n}^{-2/3}\). Then the three
PF area terms have orders \(a_n^2n^{-3/7}\),
\(a_n^2n^{-4/7}\), and \(a_n^2n^{-4/7}\), while
\(\sqrt{M_n}r_{\mu,n}=a_nn^{-2/7}=o(a_n)\).
Agent D's local coefficient \(K_{F,n}\asymp\alpha_n^{-1}=a_n^{-2}\)
therefore gives

\[
r_{F,n}=O(n^{-3/7}),\quad
q_{R,n}=O(a_nn^{-3/7}),\quad
d_n=O(\alpha_nn^{-3/7}),\quad
\eta_n/\Delta_n=O(n^{-3/7}).
\tag{E.40c}
\]

All generated errors are \(o(a_n)\) relative to their proportional slacks. Hence this is a nonempty full-rank, locally noncommuting branch for arbitrary polynomial \(m_n=n^x\); dimension is added through inactive coordinates, not through unbounded energy. It is an attainability example, not a pervasive theorem or a sharp maximum-growth claim.

### 7.5 Concrete margin substitution template

If Agent D proves, for example,

\[
K_{B,n}\lesssim\alpha_n^{-u_B}\beta_n^{v_B}
\chi_{{\rm P},n}^{-w_{B,P}}\chi_{{\rm E},n}^{-w_{B,E}},
\qquad
K_{F,n}\lesssim\alpha_n^{-u_F}\beta_n^{v_F}
\chi_{{\rm P},n}^{-w_{F,P}}\chi_{{\rm E},n}^{-w_{F,E}},
\tag{E.41}
\]

then \(g_B=au_B+bv_B+c_Pw_{B,P}+c_Ew_{B,E}\), with the analogous formula for \(g_F\). Substitution in (E.27), (E.28), and (E.36) or (E.38) is mechanical. The displayed powers are placeholders only.

## 8. Dependency/exponent table

| Node | Exact rate | Margin input | Energy/count input | Failure boundary |
|---|---|---|---|---|
| positive stage | \(K_S\mathfrak s_1\) | score radius/coercivity | score sup, \(\log(n\mathcal O)\) | \(K_Gu_{\rm stg}\not=o(\delta_*)\) |
| mean RMS/sup | \(K_BB_3h^3+K_{\mathcal R}K_S\{\text{score+LS+design}\}\) | bias and first-derivative factors kept separate | score, LS, design | no localisation or generated escape |
| grid max | \(\sqrt{M+1}\,r_\mu\) | \(K_G\) | vertex count | (E.6) fails |
| PF frame | (E.9) | \(K_F\) | \(M\), typed sup speed \(v_\mu\), acceleration \(a_\mu\) | ribbon escape or \(K_Fr_\mu\not\to0\) |
| feasible observations | (E.11) | \(K_{L1},K_{L2},K_C\) | energy multiplies frame | too large for row/gap |
| oracle row | (E.12) | none beyond true frame | product moments/dependence/lags | \(\omega_n\) too large |
| feasible row | (E.13) | through \(q_R\) | \(\sqrt{h_0},\mathcal E_2,\zeta\) | assembly fails |
| assembly/loading | \(\eta=2A_2d+d^2\), \(2\eta/\Delta\) | none | \(A_2,\Delta\) | \(\eta\not=o(\Delta)\) |
| null/selector | \(d^2\), \(d^2\ll\tau\ll\Delta\) | exact target rank | gap/nonzero ratios | interval empty; raw ratio invalid |
| truncation | score/product biases + (E.7) | expanding-domain \(K_Z(T)\) | object counts/tails | tails without geometry do not close |

## 9. Agent D interface slots

| ID | Exact coefficient needed | Consumed order | D value |
|---|---|---:|---|
| D→E-S | \(K_{S,n}\): inverse stage Hessian/coercivity and BW norm conversion | 1 | \(O(1)\) on half-Hessian ball |
| D→E-B | \(K_{B,n}\): deterministic cubic score/change-of-base coefficient only | 3 | \(O(1+\alpha_n^{-1})\), with law \(B_3\) separate |
| D→E-R | \(K_{\mathcal R,n}\): first derivative/Lipschitz coefficient of Richardson/blend | 1 | \(O(1)\) locally |
| D→E-G | \(K_{G,n}\): generated-map membership in normalized length/factor slacks | fixed maximum | \(O(1)\) locally; raw slack conversions visible |
| D→E-L1 | \(K_{L1,n}\): first-order Log/recentring | 1 | \(O(1)\) locally |
| D→E-L2 | \(K_{L2,n}\): quadratic Log/recentring remainder | 2 | \(O(\alpha_n^{-1/2})\) locally |
| D→E-F | \(K_{F,n}\): ruled-cell curvature/Jacobi PF coefficient | connection variation | \(O(\alpha_n^{-1})\) on fractional-normal cells |
| D→E-C | \(K_{C,n}\): residual connector/trivialisation factor | 1 | \(O(1)\); parameter derivatives use PT recurrence |
| D→E-N | produced \(\rho_{{\rm nor},n}\) from mixed Hessian derivative | 1 mixed | \(O(\sqrt{\alpha_n})\), intersected with all slacks |
| D→E-DOM | exact slack contraction for Richardson/blend/chord/ruled maps | fixed maximum | strict \(s_H\), factor/polar/Exp/cell slacks required |

## 10. Failure boundaries and claims not made

1. If \(\alpha_n=0\) or a required polar/Exp singular value vanishes, the full-rank theorem class is left. This is not a repeated-eigenvalue issue.
2. Mean consistency does not imply (E.5)–(E.7); stage, grid, signed output, connector, ruled, and reconstruction tests are separate.
3. A generic frame produces \(r_F\mathcal E_2\), which enters the lag row multiplied by another \(\mathcal E_2\).
4. RMS grid control costs \(\sqrt{M+1}\); a candidate family costs its actual entropy/union bound. Neither is hidden in \(C_{\rm BW}\).
5. Score control does not imply product concentration. Equation (E.12) remains separate.
6. Geometry does not imply signal. Recompute the target, \(A_2\), and \(\Delta\) after normalization or contamination.
7. The null square uses lag-row factorisation; Weyl alone does not provide it. Shrinking margins do not revive the raw ratio.
8. Section 7 becomes a BW theorem only after Agent D verifies the powers and Agent F fails to disprove them.

## 11. Mandatory cross-audit of Agent D — pass 1

This audit read Agent D's complete first dossier and tested its Section 9 interface against (E.2)–(E.20).

### 11.1 Accepted local primitive interfaces

The following interfaces are correctly typed and reach the stated local consumers on a fixed fractional-normal generated domain:

| D producer | E use | Pass-1 disposition |
|---|---|---|
| \(G_{R,j}=C_j\alpha_n^{-(j+2)/2}\) | curvature/connection variation | accepted locally; lower \(2\times2\) noncommuting block certifies \(\alpha_n^{-1}\) at \(j=0\) |
| \(G_{H,j}=C_j\alpha_n^{-j/2}\) | Hessian derivatives | accepted on a \(c\sqrt{\alpha_n}\) pair ball |
| \(\rho_{H,n}\lesssim\sqrt{\alpha_n}\) | normal-pair domain | accepted as a sharp full-rank-domain order; rank-boundary distance supplies the upper obstruction |
| \(G_{{\rm PF},n}=C\alpha_n^{-1}\) | ruled-cell area to transport | accepted when every cell is fractional-normal; the statistical/path area remains visible |
| polar primitive \(D^k{\rm polar}=O(\chi_{{\rm P},n}^{-k})\) | raw fallback | accepted for an arbitrary polar input; factored banded inputs have the effective lower margin \(\max\{\chi_{{\rm P},n},\alpha_n\}\) |
| forward Exp polynomial | generated maps | accepted: \(\chi_{{\rm E},n}\) is closure, not a forward derivative singularity |
| PT recurrence (D 6.4–6.5) | connector/endpoint variations | accepted as sufficient when all canonical path jets are supplied; no exponential Gronwall multiplier is introduced |

On the half-Hessian ball, \(K_{S,n}=O(1)\). Local first derivatives of Log and Richardson are homogeneous of order zero, so \(K_{L1,n}=O(1)\) and \(K_{\mathcal R,n}=O(1)\); the quadratic Log remainder pays \(K_{L2,n}=O(\alpha_n^{-1/2})\). These statements do not determine the deterministic cubic law-bias coefficient \(K_{B,n}B_{3,n}\).

### 11.2 Objections and required repairs

| ID | Attack | Consequence for E | Required repair / theorem restriction | Status |
|---|---|---|---|---|
| D-X1 | D (9.6) initially included \(\rho_{H,n}\), but not the actual population score-pair slack \(\rho_{H,n}-\sup d(q^0,x)\). | A support law can lie outside the produced normal ball; growing energy with shrinking \(\rho_H\) can make the theorem empty. | D added \(s_{H,n}\) and support-energy compatibility; E uses (E.5a)–(E.6a). | **REPAIRED AND ACCEPTED; UNRESTRICTED GROWING ENERGY EXCLUDED** |
| D-X2 | D's primitive table did not initially fill E's termwise \(K_B,K_{\mathcal R},K_S,K_G,K_{L1},K_{L2},K_C\). | Multiplying the Hilbert score fluctuation by a third-order coefficient would overstate margin blow-up; omitting cubic law derivatives would understate it. | D now gives \(K_S,K_{\mathcal R},K_G,K_{L1},K_C=O(1)\), \(K_B\lesssim1+\alpha^{-1}\), and \(K_{L2}\lesssim\alpha^{-1/2}\); E (E.3)/(E.11) are termwise. | **REPAIRED AND ACCEPTED** |
| D-X3 | The old single \(\chi_n\) convention conflates eigenvalue-unit polar margin and lift-unit Exp margin. | A power of one numeral has no stable homogeneity. | Use \(\chi_{{\rm P},n}\) and \(\chi_{{\rm E},n}\). On proportional local domains take \(\chi_P\asymp\alpha_n\), \(\chi_E\asymp\sqrt{\alpha_n}\); a common repository numeral is only a conservative convention. | **D SEPARATION ACCEPTED; E PROPAGATED** |
| D-X4 | D's first safe PF Jacobi envelope used \(J_*(r_{0,n}/\sqrt{\alpha_n})\). Total path length may be much larger than one cell length and would create a spurious exponential. | A numerical \(m_n\)-window could be destroyed despite isometric cellwise telescoping. | D now uses maximum fractional-normal ruled-cell diameter; total speed/length remains only in the visible area bracket. | **REPAIRED AND ACCEPTED** |
| D-X5 | U-D1 and U-D3 leave sharp factored alignment and nonlocal generated-map powers unresolved. | They block a single sharp monomial for the unrestricted nonlocal generated theorem. | State the statistical theorem either with D's finite raw recurrences, or restrict every consumed endpoint pair/map to the intrinsic fractional-normal domain with proportional slacks. They do not block the restricted sufficient theorem or Sections 7.3–7.4. | **ISOLATED, NOT A FIXED-MARGIN GAP** |
| D-X6 | Path length alone does not bound higher PT endpoint derivatives; D 6.4 needs \(\sup\|V_j\|\) and \(\int\|\dot V_j\|\). | A bare \(r_0\) exponent cannot fill \(K_C\) or generic polygon derivatives. | Supply the jets of the actual radial/chord/ruled lift families; keep generic \(M+\mathsf L\) Bell dependence visible. PF itself uses area, not the generic derivative. | **RECURRENCE SUFFICIENT; SINGLE POWER UNRESOLVED (U-D4)** |
| D-X7 | The rank-boundary family proves a full-rank-domain radius cannot exceed \(O(\sqrt\alpha)\); it does not alone prove Hessian loss exactly at that radius. | Calling exact Hessian loss sharp would overstate the lower result. | Interpret D's label as sharp order for a uniform full-rank normal-domain radius; \(c\sqrt\alpha\) is the sufficient Hessian radius. | **CLARIFIED AND ACCEPTED** |
| D-X8 | Tool rendering suggested possible C0 loss in \(\rho,\tau\). | A direct filesystem scan found zero C0 controls. | Withdraw the mechanical objection. | **WITHDRAWN** |

### 11.3 Do U-D1–U-D4 block numerical windows?

- **Unrestricted nonlocal theorem:** yes. U-D1 and U-D3 prevent a justified single sharp power, so only the exact finite recurrence may be propagated.
- **Fractional-normal local theorem:** no. Intrinsic Log/generated-map homogeneity, proportional polar/Exp slacks, per-cell Jacobi control, and the exact PT recurrence give a sufficient theorem. U-D2 is avoided cellwise; U-D4 remains recurrence-defined but finite at fixed order.
- **Claim of sharp maximum \(m_n\)-growth:** yes, all four must be minimized or matched by lower families before “sharp” is used. E's inequalities remain explicitly sufficient.

The nonempty root-scaled branch in Section 7.4 lies inside the restricted theorem and demonstrates that shrinking \(\alpha_n\) is not automatically impossible. It does not support a pervasive growing-energy claim.

## 12. Independent-pass conclusion

The statistical propagation is complete at the symbolic level. Conditions (E.2)–(E.20), including the actual normal-pair slack and support compatibility, are an exact sufficient chain. Section 7.3 gives the conservative \(x<3/(5A)\) fractional-normal benchmark, while Section 7.4 gives a model-specific self-similar noncommuting branch. A pervasive growing-energy branch is unavailable when its support violates the shrinking normal radius. An honest unrestricted numerical \(x_{\max}\) awaits Agent D's composite-interface repairs, resolution or restriction of U-D1–U-D4, and the hostile audit.
