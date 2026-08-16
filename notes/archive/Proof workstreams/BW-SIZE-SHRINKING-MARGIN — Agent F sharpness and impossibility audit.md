---
type: noncanonical-working-proof-dossier
title: BW-SIZE-SHRINKING-MARGIN — Agent F sharpness and impossibility audit
status: frozen-chain-hostile-pass-2-complete
authority: noncanonical-agent-f-only
stage: 2-shrinking-margin
---

# BW-SIZE-SHRINKING-MARGIN — Agent F sharpness and impossibility audit

> **NONCANONICAL INDEPENDENT FIRST PASS.** This dossier attacks Stage 2 before reading either optimistic Stage 2 workstream. It was derived from the full campaign brief, the archived proved Stage 1 A/B/C dossiers and Gate A ledger, and the canonical statistical consumers. It has no canonical theorem status. A failed proof technique is not called a counterexample, and an unproved sharp exponent is left open.

## 0. First-pass verdict

There is no single universal matrix-size window and no single “BW margin exponent.” At least six independent channels survive the fixed-margin theorem:

1. distance to rank loss and generated-domain slack;
2. intrinsic quotient curvature and transport sensitivity;
3. polar/alignment conditioning;
4. total tangent energy and product-row sampling;
5. dependence, lag count, and path discretisation;
6. lag signal, the actual eigengap, and factor selection.

Several lower powers are analytically forced:

- a full-rank neighbourhood at lower eigenvalue \(\alpha_n\) cannot have BW radius larger than order \(\sqrt{\alpha_n}\);
- \(\|D_LP_L^{\mathcal H}\|\) is at least order \(\alpha_n^{-1/2}\) on a two-by-two noncommuting family;
- the normalized curvature-operator coefficient is at least order \(\alpha_n^{-1}\);
- the first polar derivative is at least order \(\sigma_{{\rm pol},n}^{-1}\);
- an RMS grid error alone pays the exact worst-case factor \(\sqrt{N_n+1}\);
- in the one-lag rank-one signal model, loading recovery and a nonempty selector window require total lag-row error \(d_n=o(s_n)=o(\sqrt{\Delta_n})\), not merely \(d_n=o(1)\).

These floors do **not** justify multiplying every coarse Stage 1 power. Scalar and commuting-diagonal BW are Euclidean in square-root coordinates and cancel many apparent \(\alpha_n^{-q}\) factors. Exp itself is polynomial in a lift and has no inverse-margin derivative singularity. Upper spectral growth can reduce, rather than increase, intrinsic curvature under uniform dilation. Every claimed exponent must therefore be attached to a typed map and survive cancellation at the final consumer.

No retained-hypothesis counterexample presently proves that every shrinking-margin theorem is impossible. What is impossible is any theorem that suppresses the rank-boundary radius, generated-set slack, path quantities, energy, dependence, actual gap, or object count.

## 1. Margin notation and dimensional audit

The Stage 1 symbol \(\chi\) combines quantities with different scaling. For the sharp audit they must be separated:

\[
\alpha_n I\preceq A\preceq\beta_n I,
\qquad
\sigma_{\min}(M^TL)\ge \sigma_{{\rm pol},n},
\qquad
\sigma_{\min}(L+H)\ge \sigma_{{\rm exp},n}.
\tag{1.1}
\]

Here \(\alpha_n,\beta_n,\sigma_{{\rm pol},n}\) have matrix-eigenvalue scale, whereas \(\sigma_{{\rm exp},n}\) has square-root/lift scale. When both aligned factors represent banded SPD matrices,

\[
\sigma_{\min}(M^TL)\ge\alpha_n,
\qquad
\sigma_{\min}(L+H)\ge\sqrt{\alpha_n}
\tag{1.2}
\]

whenever the Exp output is itself in the same band. Thus a declared common \(\chi_n\) can be redundant, or can impose an additional interior restriction. A sharp theorem must use the actual active margins rather than automatically multiplying separate \(\alpha_n^{-a}\chi_n^{-b}\) bounds.

Uniform dilation is a compulsory consistency check. Under \(A\mapsto cA\), lift lengths and BW distances scale by \(\sqrt c\), polar cross-Grams scale by \(c\), and normalized curvature scales by \(c^{-1}\). Any proposed monomial bound whose units do not respect this transformation is not sharp and may be false.

## 2. Analytic primitive lower bounds

### 2.1 Scalar root coordinate: boundary radius, exact norm powers, and cancellations

For \(m=1\), write \(A=a=r^2\), \(r>0\). Then

\[
d_{\rm BW}(a,b)=|\sqrt a-\sqrt b|,
\qquad
\|u\|_{a,{\rm BW}}=\frac{|u|}{2\sqrt a}.
\tag{2.1}
\]

Consequences:

1. The distance from \(a=\alpha\) to rank loss is exactly \(\sqrt\alpha\). No ball centred there and contained in the full-rank cone can have radius exceeding \(\sqrt\alpha\). Hence a uniform normal/support/generated radius \(\rho_n\gg\sqrt{\alpha_n}\) is impossible for a theorem class allowing points at the lower edge.
2. The tangent conversion
   \[
   \|u\|_{a,{\rm BW}}\le (2\sqrt\alpha)^{-1}|u|
   \]
   is sharp, as is \(|u|\le2\sqrt\beta\|u\|_{a,{\rm BW}}\).
3. Ordinary scalar derivatives satisfy
   \[
   \frac{d^k}{da^k}\sqrt a=c_k a^{1/2-k}.
   \tag{2.2}
   \]
   After feeding \(k\) unit-BW tangent directions, each with Euclidean size \(2\sqrt a\), the ordinary principal-section derivative scales as \(a^{(1-k)/2}\).
4. Nevertheless the intrinsic scalar BW manifold is the Euclidean half-line in coordinate \(r\): curvature is zero, PT is the identity, and the squared-distance Hessian is exactly the identity. Thus the powers in (2.2) are chart/section costs unless a final consumer prevents their cancellation.

This family rejects any argument that declares every Sylvester or square-root recurrence power intrinsically necessary merely because it appears in an intermediate expression tree.

### 2.2 Horizontal projector: an \(\alpha^{-1/2}\) first-derivative floor

Let \(m=2\), \(L_s=sI_2\), \(s=\sqrt\alpha\), and perturb

\[
L_s(\varepsilon)=\operatorname{diag}(s+\varepsilon,s),
\qquad
Z=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For \(P_L^{\mathcal H}Z=Z-L\Omega\), the Sylvester equation gives

\[
\Omega_{12}(\varepsilon)
=\frac{\varepsilon}{(s+\varepsilon)^2+s^2},
\qquad
\Omega_{21}=-\Omega_{12}.
\tag{2.3}
\]

Therefore

\[
\left\|D_LP^{\mathcal H}_{sI_2}
[\operatorname{diag}(1,0)]Z\right\|_F
=\frac{1}{\sqrt2\,s}
\asymp\alpha^{-1/2}.
\tag{2.4}
\]

No dimension, trace, or eigenvalue multiplicity is involved. Homogeneity gives

\[
D^kP^{\mathcal H}_{sL}[H_1,\ldots,H_k]
=s^{-k}D^kP^{\mathcal H}_{L}[H_1,\ldots,H_k]
\tag{2.5}
\]

whenever the displayed derivative is nonzero. Hence a proposed \(o(\alpha^{-k/2})\) uniform bound at a nonzero \(k\)-th derivative is impossible. This does not prove that every derivative and every final quotient tensor pays that full power; invariant cancellations must still be checked.

### 2.3 Polar alignment: a \(\sigma_{\rm pol}^{-1}\) floor

Let \(C_s=sI_2\) and \(J=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\). Then

\[
\operatorname{polar}(C_s+tJ)
=\frac{sI_2+tJ}{\sqrt{s^2+t^2}},
\qquad
D\operatorname{polar}_{C_s}[J]=s^{-1}J.
\tag{2.6}
\]

Thus the first polar derivative has unavoidable size \(\sigma_{{\rm pol}}^{-1}\). Higher nonzero derivatives obey the homogeneity scale \(s^{-k}\). Repeated singular values do not regularize this example: \(C_s\) has maximal multiplicity. The singular-value margin, not a singular-vector gap, is the genuine input.

For aligned lifts of banded SPD matrices, (1.2) may replace this by an \(\alpha_n^{-1}\) floor. It is generally incorrect to pay both \(\sigma_{{\rm pol},n}^{-1}\) and \(\alpha_n^{-1}\) if the former is only the redundant consequence of the latter.

### 2.4 Curvature: an \(\alpha^{-1}\) intrinsic floor

At \(L=sI_2\), take Frobenius-orthonormal noncommuting symmetric horizontal directions, for example normalized versions of

\[
X=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
Y=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The O'Neill tensor scales as

\[
\mathcal A_XY=-\frac1{2s}[X,Y]
\tag{2.7}
\]

up to the fixed normalization of \(X,Y\). Stage 1's exact sectional calibration then gives

\[
\langle R(X,Y)X,Y\rangle
=3\|\mathcal A_XY\|_F^2
=c_0s^{-2}=c_0\alpha^{-1},
\qquad c_0>0.
\tag{2.8}
\]

This is an intrinsic BW-normalized lower bound. It persists at the repeated-spectrum point \(A=\alpha I_2\), so repeated positive eigenvalues are not a protective margin. By dilation, every nonzero \(j\)-th covariant curvature derivative has the natural scale

\[
\|\nabla^jR\|\sim \alpha^{-1-j/2}
\tag{2.9}
\]

on a scale family, although (2.8) alone proves sharpness only for \(j=0\).

For a sufficiently small geodesic rectangle with side lengths \(a,b\), infinitesimal holonomy is

\[
P_{\partial\Box}-I=R(X,Y)ab+o(ab).
\tag{2.10}
\]

Therefore no ruled-surface/connection-variation theorem on the full noncommuting class can replace the curvature coefficient by \(o(\alpha^{-1})\).

### 2.5 Squared-distance Hessian and the normal-radius scale

In normal coordinates,

\[
\mathsf H(A,\Exp_Av)
=I-\frac13R(\,·\,,v)v+O(\|v\|^3\|\nabla R\|).
\tag{2.11}
\]

On the two-by-two family above, take \(\|v\|\asymp\sqrt\alpha\). Equations (2.8)--(2.11) give an observation-Hessian variation coefficient of order at least \(\alpha^{-1/2}\) somewhere in that shrinking neighbourhood. This matches the independent boundary obstruction \(\rho_H=O(\sqrt\alpha)\).

The scalar family shows that this Hessian blow-up is not universal on flats; the noncommuting family shows it is unavoidable for a theorem uniform over the whole quotient class.

### 2.6 Exp margin: domain obstruction, not an automatic derivative power

In lift variables,

\[
\Exp_A(d\pi_LH)=\pi(L+H)=(L+H)(L+H)^T.
\tag{2.12}
\]

This map is polynomial. Its first two lift derivatives do not blow up as \(\sigma_{\min}(L+H)\downarrow0\), and higher lift derivatives vanish. The Exp singular-value margin is required for full-rank output, inverse maps, later Log/alignment operations, and generated-domain closure. It must not be assigned a negative power in the derivative of Exp itself.

### 2.7 Upper spectral scale

The reverse norm conversion \(\|U\|_F\le2\sqrt\beta\|U\|_{\rm BW}\) is sharp. However, under the uniform family \(A=\beta I\), normalized curvature is order \(\beta^{-1}\), not a positive power of \(\beta\). Hence a positive \(\beta_n\) exponent in an intrinsic final consumer needs a mixed-condition-number example; it cannot be justified by the Stage 1 operator-by-Frobenius envelope alone.

## 3. Generated-domain and rank-loss attacks

### 3.1 Compatibility and emptiness

With one common numerical margin \(\chi_n\), the scalar-centred Stage 1 construction requires

\[
\max\{\chi_n,\chi_n^2\}<\beta_n.
\tag{3.1}
\]

If (3.1) fails, that generated package is empty. This is generated-domain failure, not geometry blow-up and not a counterexample to a theorem that explicitly assumes a nonempty domain.

### 3.2 Interior slack is separate from derivative control

In scalar root coordinates the Richardson output is

\[
r_R=\tfrac13r_1-2r_2+\tfrac83r_3.
\tag{3.2}
\]

Positive inputs need not give \(r_R>0\). If the population output has root slack \(\delta_{R,n}\), perturbing the three inputs by at most \(e\) can change \(r_R\) by as much as \(5e\). Thus a worst-case generated-domain guarantee requires

\[
5e=o(\delta_{R,n})
\tag{3.3}
\]

or a sharper map-specific analogue. No derivative constant can replace a missing population slack.

### 3.3 RMS grid error cannot authorize every generated object without a count cost

For \(N+1\) vertices,

\[
\max_j e_j\le\sqrt{N+1}
\left\{\frac1{N+1}\sum_je_j^2\right\}^{1/2}.
\tag{3.4}
\]

Equality is attained by concentrating all error at one vertex. Therefore any theorem using only grid RMS to authorize all vertices, chords, connectors, Richardson images, and ruled cells must retain \(\sqrt{N+1}\). A probabilistic sup bound can replace (3.4), but then its \(\log N_{\rm obj}\), tail, dependence, and escape-probability terms must be proved.

If the available population slack is at most order \(\sqrt{\alpha_n}\), the RMS-only route necessarily asks

\[
\sqrt{N_n+1}\,r_{\mu,n}=o(\sqrt{\alpha_n}/C_{{\rm gen},n}).
\tag{3.5}
\]

For the canonical fixed-constant choice \(N_n\asymp r_{\mu,n}^{-2/3}\), even with \(C_{{\rm gen},n}=O(1)\), (3.5) becomes

\[
r_{\mu,n}^{2/3}=o(\sqrt{\alpha_n}),
\qquad\text{equivalently}\qquad
r_{\mu,n}=o(\alpha_n^{3/4}).
\tag{3.6}
\]

At the bounded-energy benchmark \(r_{\mu,n}\asymp n^{-3/7}\), this worst-case RMS-only condition is \(\alpha_n\gg n^{-4/7}\). It is not a universal minimax boundary: a proved sup-grid rate, larger population slack, or a different grid can change it.

### 3.4 Object-count escape probabilities

If one primitive object fails its margin with probability \(\pi_n\) and the complete estimator generates \(N_{{\rm obj},n}\) checked objects, the elementary worst-case sufficient condition is

\[
N_{{\rm obj},n}\pi_n\to0.
\tag{3.7}
\]

The count includes observations, positive stage means, Richardson/blend outputs, vertices, chords, connector paths, ruled cells, reconstructions, and any truncation objects. A statement proving only a one-object tail and then invoking the complete generated event omits a load-bearing union bound.

## 4. Path, transport, and polygon attacks

### 4.1 Zeroth PT is safe; variation is not

Stage 1 proves exact PT isometry, so no \(\exp(C\,\mathsf L)\) loss is necessary for the transported vector itself. Endpoint/surface variation, however, detects curvature. The local rectangle family (2.10) forces the coefficient \(\alpha_n^{-1}\) in a general noncommuting ruled-area estimate.

### 4.2 Moving-eigenvector and high-frequency families

Embed the two-by-two block

\[
A_s(u)=R(\theta_s(u))
\operatorname{diag}(s^2,2s^2)R(\theta_s(u))^T
\tag{4.1}
\]

in any larger SPD matrix with fixed remaining eigenvalues. Then \(\alpha=s^2\), while eigenvectors move.

- If \(\theta_s(u)=u\), the BW speed and acceleration in the shrinking block are order \(s\). Curvature times the ribbon area generated by a transverse mean error \(e\) is order \(e/s=\alpha^{-1/2}e\).
- If \(\theta_s(u)=\sin(u/s)\), the BW speed is order one but acceleration is order \(s^{-1}=\alpha^{-1/2}\). The curvature-weighted linear ribbon term can be order \(\alpha^{-1}e\), while the discretisation lens must display the growing acceleration.

Thus a claimed frame exponent depends on the separately stated path-speed and path-acceleration scales. Bounded total length does not control acceleration, and “moving eigenvectors” cannot be replaced by a fixed diagonal root model.

### 4.3 Exact PF phase inequalities

Stage 1's typed PF bound has the form

\[
r_{F,n}\lesssim C_{R,n}
\{v_{\mu,n}r_{\mu,n}
+N_nr_{\mu,n}^2
+v_{\mu,n}a_{\mu,n}N_n^{-2}\},
\tag{4.2}
\]

with \(C_{R,n}\ge c\alpha_n^{-1}\) on the full noncommuting class by (2.8)--(2.10). Therefore a sufficient shrinking-margin theorem must leave visible, at minimum,

\[
\alpha_n^{-1}v_{\mu,n}r_{\mu,n}\to0,
\quad
\alpha_n^{-1}N_nr_{\mu,n}^2\to0,
\quad
\alpha_n^{-1}v_{\mu,n}a_{\mu,n}N_n^{-2}\to0,
\tag{4.3}
\]

unless it proves a smaller curvature action on the actual ribbon planes. The first coefficient is sharp for general small ruled cells. In a path class whose speed itself is only \(O(\sqrt\alpha)\), the effective lower cost is \(\alpha^{-1/2}r_\mu\), illustrating why geometry and path scale must not be merged.

Balancing only the last two terms gives

\[
N_n\asymp
\left(\frac{v_{\mu,n}a_{\mu,n}}{r_{\mu,n}^2}\right)^{1/3},
\qquad
N_nr_{\mu,n}^2+v_{\mu,n}a_{\mu,n}N_n^{-2}
\asymp(v_{\mu,n}a_{\mu,n})^{1/3}r_{\mu,n}^{4/3}.
\tag{4.4}
\]

This choice must still satisfy the generated-event constraint (3.5). Choosing \(N_n\asymp r_{\mu,n}^{-2/3}\) before exposing \(a_{\mu,n}\), curvature, and slack is not generally optimal.

### 4.4 Generic polygon derivatives retain segment count

For independently varying vertices in the \(\oplus,\infty\) norm, Stage 1 correctly retains Bell-polynomial budgets in \(N+\mathsf L\). The zero-length segment family shows why: a segment endpoint derivative need not vanish when the segment collapses. PT isometry removes multiplicative \(C^N\), not the additive count. Any Stage 2 bound that silently moves this stronger generic derivative into a margin-only constant is false.

## 5. Mean localisation and feasible-observation propagation

### 5.1 Necessary localisation scale

Any local full-rank theorem allowing population centres at distance \(O(\sqrt{\alpha_n})\) from rank loss must have

\[
r_{\infty,n}=o(\sqrt{\alpha_n})
\tag{5.1}
\]

or an explicit larger centre-specific boundary slack. For complete grid generation, replace \(r_{\infty,n}\) by the left side of (3.5). This condition concerns domain validity before Taylor expansion; it cannot be recovered after applying a divergent differential constant.

The positive-Hessian radius is also at most order \(\sqrt{\alpha_n}\) on the full class. Hence the support/score radius, empirical centre error, Richardson displacement, connector length, and reconstruction perturbation must each be checked against that scale. They are not consequences of a spectral band alone.

### 5.2 Full feasible tangent error

The canonical consumer is

\[
q_{R,n}\lesssim
L_{\log,n}\{r_{\mu,n}+K_{\mu,n}N_n^{-2}\}
+r_{F,n}\{\mathcal E_{2,n}+L_{\log,n}r_{\mu,n}\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\tag{5.2}
\]

No margin theorem is complete until it substitutes its typed bounds into every term of (5.2). In particular:

- the scalar/diagonal family can have \(r_F=0\), so an \(\alpha^{-1}\) frame factor is not universal across restricted flats;
- the noncommuting curvature family forces such a coefficient for general ruled comparison;
- growing tangent energy \(\mathcal E_{2,n}\) multiplies frame error and is not supplied by geometry;
- connector and observation defects may carry covariance-measurement or regularisation errors unrelated to \(\alpha_n\).

### 5.3 Lag row and assembly

The exact downstream inequalities remain

\[
d_n\lesssim \omega_n+sqrt{h_{0,n}}
\{2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2\}
+\zeta_n+\rho_{{\rm mask},n}+\rho_{{\rm disc},n},
\tag{5.3}
\]

\[
\eta_n=2A_{2,n}d_n+d_n^2,
\qquad
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
\lesssim\eta_n/\Delta_n.
\tag{5.4}
\]

Thus “geometry error \(\to0\)” is insufficient. The actual requirement is (5.4) with all energy, lag-count, dependence, contamination, and gap scales retained.

## 6. Energy, dimension, dependence, and signal counterfamilies

### 6.1 Fixed bands do not bound energy

For \(A_m=I_m\), \(B_m=cI_m\) in one fixed band,

\[
d_{\rm BW}(A_m,B_m)=\sqrt m\,|1-\sqrt c|.
\tag{6.1}
\]

Hence conditioning does not bound score radius, total path length, or tangent energy. A fixed-radius local theorem excludes this family; it cannot simultaneously advertise it as a pervasive-energy theorem.

### 6.2 No universal direct \(m_n\)-restriction

Three compatible families give incompatible size windows:

1. **Bounded-energy localized family.** Scale new-coordinate noise so total Hilbert/BW energy stays bounded. Geometry and sampling can remain dimension-free, so \(m_n\) may grow arbitrarily unless margins, object counts, or signal are linked to it.
2. **Fixed-gap diagonal background.** In the flat diagonal root model, add \(m_n\) serially white coordinates with constant variance and one fixed serial factor. The lag sample cross-covariance of the white background has operator scale \(\sqrt{m_n/n}\) under the standard sub-Gaussian model. It does not vanish when \(m_n/n\not\to0\), despite fixed spectral margins. Thus no fixed-gap theorem can ignore energy/dimension sampling.
3. **Pervasive diagonal factor.** The archived proved root-coordinate DGP has
   \[
   R_n\asymp\sqrt{m_n},\quad
   A_{2,n}\asymp m_n,\quad
   \Delta_n\asymp m_n^2,\quad
   \omega_n\asymp m_n/\sqrt n.
   \tag{6.2}
   \]
   Signal offsets energy through \(\eta_n/\Delta_n\). Its \(m_n=o(n^{6/7}/\log n)\) window comes from the positive-root boundary/supremum event, not from noncommuting BW curvature.

Therefore a matrix-size window exists only after a model links \(m_n\) to margins, energy, dependence, path scales, \(A_{2,n}\), and \(\Delta_n\).

### 6.3 Growing lag count and dependence

With \(h_{0,n}\) approximately orthogonal lag-row errors of size \(n^{-1/2}\), their direct-sum norm is at least order \(\sqrt{h_{0,n}/n}\). This cost is not a union-bound artifact. Long-memory scalar processes can make the oracle row slower than root-\(n\) even when every BW margin is fixed. Margin control never substitutes for a product-process dependence theorem.

### 6.4 Rank-one signal dilution and selector impossibility

For one included lag and a rank-one population row

\[
\Gamma_n=s_n a_n\otimes a_n,
\qquad
\Delta_n=s_n^2,
\qquad
A_{2,n}=s_n,
\tag{6.3}
\]

equations (5.4) reduce to

\[
\eta_n/\Delta_n
\asymp d_n/s_n+(d_n/s_n)^2.
\tag{6.4}
\]

Thus loading recovery requires \(d_n=o(s_n)=o(\sqrt{\Delta_n})\). The factor-number threshold window

\[
d_n^2=o(\tau_n),
\qquad
\tau_n=o(\Delta_n)
\tag{6.5}
\]

is nonempty under the same separation.

This is also statistically necessary in a bounded basic experiment. Compare an iid Rademacher null with the stationary two-state Markov chain having transition law
\(P(Y_t=Y_{t-1})=(1+s_n)/2\). Its lag-one covariance is \(s_n\). For \(s_n=c/\sqrt n\), the log-likelihood ratio has bounded nondegenerate local-asymptotic variance, so the null and alternative experiments are contiguous for fixed \(c\). No selector can distinguish rank zero from rank one with probability tending to one. Hence \(\sqrt n\,s_n\to\infty\), equivalently \(n\Delta_n\to\infty\), is necessary in that benchmark. Geometry cannot rescue a signal below the lag-sampling floor.

### 6.5 Growing rank and total signal

Large total lag energy does not lower-bound the weakest nonzero eigenvalue. A diagonal factor lag with singular values \((1,\ldots,1,\varepsilon_n)\) has large total signal but \(\Delta_n\asymp\varepsilon_n^2\). Growing-rank selection additionally needs a minimum-signal and internal-spectrum condition. Any theorem using only \(\|\Gamma\|\), trace, or the leading singular value in place of the actual \(\Delta_n\) is false.

## 7. Growth-window audit template

A proposed shrinking-margin window is admissible only if all of the following inequalities are nonempty simultaneously.

### Geometry and generated set

\[
\begin{aligned}
&\text{compatibility of }(\alpha_n,\beta_n,
\sigma_{{\rm pol},n},\sigma_{{\rm exp},n}),\\
&r_{\infty,n}=o(\delta_{{\rm centre},n}),\\
&\sqrt{N_n+1}\,r_{\mu,n}
=o(\delta_{{\rm GD},n}/C_{{\rm gen},n}),\\
&N_{{\rm obj},n}\pi_n\to0,\\
&r_{F,n}\text{ satisfies (4.2)--(4.3)},\\
&\delta_{{\rm centre},n},\delta_{{\rm GD},n}
\le O(\sqrt{\alpha_n})
\text{ when the class reaches the lower edge.}
\end{aligned}
\tag{7.1}
\]

### Statistical row and loading

\[
q_{R,n}\to0,
\qquad
d_n\text{ satisfies (5.3)},
\qquad
2A_{2,n}d_n+d_n^2=o(\Delta_n).
\tag{7.2}
\]

### Selection

\[
d_n^2=o(\tau_n),
\qquad
\tau_n=o(\Delta_n),
\tag{7.3}
\]

plus the adjacent nonzero-spectrum condition for a ridged ratio and an explicit clean-target comparison when lag contamination is present.

No cancellation between separate lines of (7.1)--(7.3) is allowed unless an exact model identity proves it. In particular, stronger signal can offset energy only in (7.2); it cannot repair generated-domain failure in (7.1).

## 8. First-pass attack ledger

| Target claim | Analytic attack | Classification | Required repair or honest scope |
|---|---|---|---|
| fixed normal radius as \(\alpha_n\downarrow0\) | scalar root distance to rank loss is \(\sqrt{\alpha_n}\) | **DISPROVED** on lower-edge class | radius/slack \(O(\sqrt\alpha)\) or restrict centres away from lower edge |
| projector derivative smaller than \(\alpha^{-1/2}\) | explicit two-by-two family (2.3)--(2.4) | **DISPROVED** | retain at least first-derivative floor; prove cancellation at consumers if claimed |
| curvature coefficient \(o(\alpha^{-1})\) | repeated-spectrum noncommuting block (2.8) | **DISPROVED** | retain \(\alpha^{-1}\) or restrict actual ribbon planes to a flatter class |
| repeated eigenvalue gap is needed | \(A=\alpha I_2\) is smooth but curved | **DISPROVED** | singular-value/rank margin only |
| polar derivative bounded as margin shrinks | rotation family (2.6) | **DISPROVED** | retain \(\sigma_{\rm pol}^{-1}\) floor |
| Exp derivative necessarily blows like \(\sigma_{\rm exp}^{-q}\) | lift formula (2.12) is polynomial | **DISPROVED AS A GENERIC DERIVATIVE CLAIM** | attach margin to closure/inverse consumers, not Exp itself |
| every Stage 1 \(\alpha\)-power is sharp | scalar root-coordinate cancellations | **DISPROVED AS AN INFERENCE** | rederive the final typed map |
| positive \(\beta\)-power is intrinsically necessary | uniform dilation makes curvature \(\beta^{-1}\) | **NOT ESTABLISHED** | give a mixed-condition-number lower family |
| RMS grid error closes the full generated event without \(N\) | concentrated single-vertex error | **DISPROVED** | retain \(\sqrt N\) or prove a sup event |
| path length controls discretisation jets | high-frequency rotating-eigenvector family | **DISPROVED** | retain \(a_{\mu,n}\) and higher consumed path budgets |
| generic polygon derivative is margin-only | zero-length varying segments | **DISPROVED** | retain \(N+\mathsf L\) and declared direct-sum norm |
| fixed bands imply bounded energy | (6.1) | **DISPROVED** | separate energy/radius assumptions |
| geometry yields a universal \(m_n\)-window | localized, fixed-gap-background, and pervasive families | **DISPROVED** | state model links among size, margins, energy, and signal |
| \(d_n=o(1)\) suffices under shrinking signal | rank-one calculation (6.4) | **DISPROVED** | require exact assembly/gap ratio |
| selector can work at \(s_n\asymp n^{-1/2}\) | contiguous rank-zero/rank-one lag experiments | **DISPROVED** in benchmark class | require signal above sampling floor |
| one-object tail closes all generated objects | union count (3.7) | **DISPROVED AS A PROOF STEP** | count objects or prove a joint event |
| shrinking margins alone determine sampling | long-memory and growing-lag families | **DISPROVED** | retain \(\omega_n,h_{0,n}\), product dependence |

## 9. Exact open questions for the later hostile passes

The following are not settled by this first pass and must not be called false:

1. the smallest intrinsic powers of \(\alpha_n\) for every fixed-order base/observation derivative of Log, the squared-distance Hessian, and canonical endpoint PT after all principal-section cancellations;
2. whether the sharp upper-band dependence is only through condition number and norm conversion, or whether a noncommuting mixed-scale family forces additional \(\beta_n\) powers;
3. the sharp joint dependence on \(\alpha_n\) and the active polar margin when every polar input arises from banded generated factors;
4. whether canonical PF ribbons admit smaller curvature action than the full \(c/\alpha_n\) coefficient under additional path structure;
5. optimal \(N_n\) after simultaneously enforcing PF error, complete generated-set closure, and object-count tails;
6. minimax mean/localisation rates when the support radius itself shrinks like \(\sqrt{\alpha_n}\);
7. full noncommuting matrix models linking \(m_n\) to \(\alpha_n,\beta_n\), energy, path smoothness, \(A_{2,n}\), and \(\Delta_n\) and yielding a nonempty statistical window.

## 10. Handoff status

This independent first pass finds hard lower floors and several impossible shortcuts, but no complete counterexample to every explicitly restricted shrinking-margin theorem. The correct provisional classification is:

- **geometry blow-up:** proved at least \(\alpha^{-1/2}\) for the projector derivative, \(\alpha^{-1}\) for curvature, and \(\sigma_{\rm pol}^{-1}\) for polar differentiation;
- **generated-domain failure:** unavoidable unless all radius/slack/object-count conditions are explicit, with rank-boundary scale at most \(\sqrt\alpha\);
- **energy and sampling:** independent of spectral conditioning;
- **dependence/lag sampling:** independent of geometry;
- **signal/eigengap dilution:** governed by the exact assembly/gap ratio;
- **selection impossibility:** present at or below the lag-sampling signal floor.

The next Agent F action must be a complete-chain hostile pass on the frozen D/E/lead theorem, checking each proposed exponent and window against the families above. Until that pass, no optimistic Stage 2 conclusion is accepted here.

## 11. Mandatory frozen-chain hostile pass 2

This section rereads and attacks the current on-disk versions of:

- `BW-SIZE-SHRINKING-MARGIN — Agent D primitive sharp exponents.md`;
- `BW-SIZE-SHRINKING-MARGIN — Agent E statistical propagation and growth windows.md`;
- `BW-SIZE-SHRINKING-MARGIN — lead dependency and exponent ledger.md`.

It supersedes the provisional handoff in Section 10 wherever the repaired D/E chain now closes an objection. It does not change canonical status.

### 11.1 Frozen-chain verdict

No retained-hypothesis counterexample defeats the **restricted fractional-normal shrinking-margin theorem** after the latest repairs. Its geometry coefficients, generated-domain conditions, termwise mean rate, PF bound, feasible row, assembly, actual-gap loading result, null square, and threshold/ridged-selector conditions form a compatible sufficient chain.

The strongest justified result is not a globally sharp theorem. It is:

1. a symbolic sufficient shrinking-margin theorem on complete fractional-normal generated domains, with every population/proxy score pair strictly inside a radius (c\sqrt{\alpha_n}), proportional polar/Exp/factor slacks, fractional-normal PF cells, and the exact statistical conditions in E (E.2)--(E.20);
2. a conservative explicit power-law corollary with
   \[
   \alpha_n\asymp m_n^{-A},\qquad m_n=n^x,qquad
   0<x<\frac{3}{5A},
   \tag{11.1}
   \]
   under the matched shrinking-support, rank-one signal, bounded-law-budget, fixed-lag/dependence, and negligible-defect assumptions stated below;
3. a self-similar fixed-active-block construction allowing any fixed polynomial (m_n=n^x), because all active geometry, support, path, energy, and signal scales dilate together while added coordinates are deterministic and inactive.

The following stronger labels do not survive:

- a sharp maximum (m_n)-growth boundary;
- one sharp monomial for unrestricted nonlocal alignment, generated maps, or higher endpoint PT;
- a pervasive/growing-energy full-noncommuting theorem when the produced normal radius shrinks;
- a universal direct matrix-size exponent independent of the model's margins, energy, path, signal, and object counts.

### 11.2 Audit of every primitive sharp label

| D claim | Hostile test | Pass-2 disposition |
|---|---|---|
| raw (D^k\mathscr S^{-1}=O(\alpha^{-(k+1)})) | scalar (G=\alpha I) reaches the power | **PASS — sharp raw Frobenius primitive** |
| raw (D^kA^{1/2}=O(\alpha^{1/2-k})), inverse powers | scalar differentiation reaches them; root-coordinate covariant maps cancel them | **PASS with chart warning** |
| (D^k\operatorname{polar}=O(\chi_P^{-k})) | (C=\chi_PI+tK), including mixed directions for parity | **PASS — sharp arbitrary-polar primitive** |
| (D_L^kP_L^H=O(\alpha^{-k/2})) | explicit rational two-by-two projector family (2.3) and homogeneity | **PASS — sharp lower homogeneity** |
| (D^k\mathcal A=O(\alpha^{-(k+1)/2})) | noncommuting symmetric block at (L=\sqrt\alpha I) | **PASS** |
| (\nabla^kR=O(\alpha^{-(k+2)/2})) | radial dilation of a nonzero noncommuting sectional component; radial derivatives remain nonzero | **PASS — sharp intrinsic homogeneity** |
| (D_A^k\Gamma=O(\alpha^{-(k+1)/2})) | scalar coordinate Christoffel coefficient | **PASS only for the declared constant-coordinate coefficient; connection is not a tensor** |
| Hessian (q)-derivative (O(\alpha^{-q/2})) on a (c\sqrt\alpha)-ball | normal-coordinate curvature expansion with a small fixed fractional radius | **PASS as a uniform-ball sufficient scale; the first derivative vanishes on the diagonal** |
| full-rank normal-domain radius (O(\sqrt\alpha)) | scalar distance to rank loss | **PASS — sharp domain order, not exact Hessian-failure location** |
| forward Exp has no inverse (chi_E) power | lift map is quadratic | **PASS** |
| PF area coefficient (O(\alpha^{-1})) | infinitesimal noncommuting holonomy rectangle | **PASS — sharp coefficient on the general noncommuting class** |
| no universal positive $\beta$-power in intrinsic consumers | uniform dilation decreases curvature; no repaired lower family forces positive $\beta$ | **PASS as a negative conclusion; raw conversions/nonlocal recurrences may still pay $\beta$** |

The higher-curvature sharpness label needs the radial direction. A single fixed-scale directional derivative may vanish by symmetry, but differentiating the nonzero normalized sectional component along the quotient-cone dilation gives the required (a^{-k-2}) scale. This is sufficient for the lower homogeneity claim.

### 11.3 Polar and Exp active-margin logic

The repaired separation is correct:

\[
\sigma_{\min}(M^TL)\ge\max\{\chi_{P,n},\alpha_n\},
\qquad
\sigma_{\min}(L+H)\ge\max\{\chi_{E,n},\sqrt{\alpha_n}\}
\tag{11.2}
\]

whenever the factors and Exp output lie in the declared band. Therefore:

1. (chi_{P,n}<\alpha_n) is inactive for factored banded alignment and must not create an extra polar power.
2. (chi_{E,n}<\sqrt{\alpha_n}) is inactive for an output already checked in the band.
3. (chi_E) is a closure/inverse-consumer margin, not a forward-Exp derivative denominator.
4. Under the repository's one-numeral convention, choosing (chi_n\asymp\alpha_n) makes the polar test active at order (alpha_n), while the band supplies the stronger Exp-factor lower bound (sqrt{\alpha_n}). One must not pretend that the same numeral has the same homogeneity in both tests.

No new polar-near-singular counterexample survives (11.2) with (p<\alpha); such a family violates the factored-band relation rather than the theorem.

## 12. Audit of the D-to-E composite interface

### 12.1 Slot-by-slot verdict

| Slot | Repaired value | Hostile disposition |
|---|---:|---|
| (K_S) | (O(1)) | **PASS.** Positive-stage score and Hessian coercivity are typed in the same BW tangent norm; no Frobenius conversion is consumed. |
| (K_{\mathcal R}) / (K_{R1}) | (O(1)) | **PASS locally.** The first derivative of the fixed Richardson/blend map is scale-homogeneous of order zero. |
| (K_B) | (O(1+\alpha^{-1})) | **PASS as a sufficient cubic-bias coefficient, not a sharp universal lower power.** The law/time third-order input (B_3) remains separate. |
| (K_G) | (O(1)) | **PASS only in normalized BW-length/factor slacks.** Raw eigenvalue, polar, and cross-Gram slack conversions must remain visible. |
| (K_{L1}) | (O(1)) | **PASS on the fractional-normal ball.** |
| (K_{L2}) | (O(\alpha^{-1/2})) | **PASS.** Absorption requires (r_\mu=o(\sqrt\alpha)). |
| (K_F) | (O(\alpha^{-1})) | **PASS for fractional-normal ruled cells.** The path/error area bracket stays visible. |
| (K_C) | (O(1)) | **PASS for connector-aligned vector/operator comparison.** Derivatives of the connector as a parameterized map still use D (6.4)--(6.5). |

The most important repair is the split between (K_B) and (K_{R1}K_S). Multiplying the leading Hilbert score fluctuation by (K_B\asymp\alpha^{-1}) is an artificial chain-rule loss and gives the wrong bandwidth. Conversely, suppressing (K_BB_3) from deterministic cubic bias is also invalid.

### 12.2 Termwise mean algebra

With (m_n=n^x), (alpha_n=m_n^{-A}), score scale (m_n^{-A/2}), (K_B=m_n^A), and (K_{R1}K_S=1), the correct balance is

\[
m_n^Ah_n^3
\asymp m_n^{-A/2}(nh_n)^{-1/2}.
\tag{12.1}
\]

It gives

\[
h_n=n^{-(1+3Ax)/7},
\qquad
r_{\mu,n}=n^{-(3+2Ax)/7+o(1)}.
\tag{12.2}
\]

Direct substitution verifies E (E.24)--(E.25). The ordinary bandwidth conditions require (x<2/A), and the RMS-grid/fractional-cell condition requires (x<12/(13A)). Both are weaker than the final row/gap condition (x<3/(5A)).

Logarithmic sup-score and polynomial object-count factors change (12.2) only by (n^{o(1)}). They must still be included at equality boundaries; the displayed strict power window is unaffected.

## 13. Strict normal slack, support energy, and nonemptiness

### 13.1 Radius is not slack

The complete domain parameter must contain

\[
s_{H,n}=\rho_{H,n}-
\sup_{(q^0,X)}d_{\rm BW}(q^0,X)>0,
\tag{13.1}
\]

not merely $\rho_{H,n}$. If a population/proxy score pair sits on the boundary, no positive empirical perturbation radius follows. D (9.6a) and E (E.5a) now repair this point.

### 13.2 Shrinking normal radius forces shrinking support and energy

Under the full noncommuting positive-G1 package,

\[
\|Y_{t,n}\|_{\rm BW}\le R_{X,n}^{\sup}
<\rho_{H,n}=O(\sqrt{\alpha_n}),
\qquad
\mathcal E_{2,n}=O(\sqrt{\alpha_n}).
\tag{13.2}
\]

Consequently

\[
A_{2,n}=O(\sqrt{h_{0,n}}\,\alpha_n),
\qquad
\Delta_n\le A_{2,n}^2=O(h_{0,n}\alpha_n^2)
\tag{13.3}
\]

for clean lag targets; at fixed lag count this is (A_{2,n}=O(\alpha_n)). A fixed or growing tangent-energy branch with (\alpha_n\downarrow0) is empty under this theorem class. Signal growth cannot repair the failed support event. Flat/global diagonal models with different convexity and support arguments are separate theorem classes.

### 13.3 Nonempty local family

A fixed noncommuting (2\times2) active block scaled by (a_n=\sqrt{\alpha_n}), embedded beside deterministic inactive coordinates, realizes strict fractional spectral, polar, Exp, and normal-pair slacks. Bounded finite-memory tangent factors of amplitude (a_n) give (A_{2,n}\asymp\alpha_n) and (Delta_n\asymp\alpha_n^2). This family retains noncommutativity and repeated-spectrum tests while satisfying (13.1)--(13.3).

The conservative (x<3/(5A)) theorem is nonempty even if its (B_3=O(1)) upper budget is loose for this particular family: a self-similar (B_3=O(a_n^3)) law is a member of the larger (B_3=O(1)) assumption class.

## 14. Per-cell Jacobi/PT, PF, grid, and object counts

### 14.1 Local cells versus total path

D's repaired producer requires

\[
\max_j\{\ell_j,e_j,e_{j+1}\}=o(\sqrt{\alpha_n}),
\tag{14.1}
\]

or a fixed sufficiently small fractional version. E correctly supplies the true-cell term (v_{\mu,n}/M_n), the RMS vertex maximum (sqrt{M_n+1},r_{\mu,n}), acceleration/chord defect, and connector maximum in (E.6).

The total mean-path length may remain nonshrinking because the comparison telescopes cellwise through isometries. No exponential in (r_{0,n}/\sqrt{\alpha_n}) is needed. Conversely, total path length alone cannot imply (14.1), cannot bound acceleration, and cannot control generic endpoint-PT jets.

### 14.2 PF coefficient and visible area

The correct bound remains

\[
r_{F,n}\lesssim\alpha_n^{-1}
\{v_{\mu,n}r_{\mu,n}
+(M_n+1)r_{\mu,n}^2
+v_{\mu,n}a_{\mu,n}M_n^{-2}\}
+\rho_{F,n}.
\tag{14.2}
\]

The (alpha_n^{-1}) coefficient is sharp for arbitrary small noncommuting cells. This does not mean every path attains (alpha_n^{-1}v_\mu r_\mu): a self-similar path has (v_\mu=O(\sqrt\alpha)), while a flat path has zero curvature action. Equation (14.2) is the correct worst-class upper theorem.

### 14.3 Grid and generated objects

E retains both alternatives:

- RMS-only authorization pays (sqrt{M_n+1});
- a proved sup-grid event may replace it and pays its actual entropy/tail cost.

The complete escape condition

\[
\mathcal O_{X,n}\pi_{X,n}
+\mathcal O_{Y,n}\pi_{Y,n}=o(1)
\tag{14.3}
\]

is also present. Counts must include raw/proxy observations, stage means, signed outputs, vertices, connectors, ruled cells, reconstruction objects, and retained lag endpoints. In the bounded self-similar construction these failures are deterministically excluded, so (14.3) is vacuous rather than omitted.

No new many-vertex or concentrated-error family violates the repaired conditions.

## 15. Feasible observations, row, gap, null spectrum, and selectors

### 15.1 Conservative local power branch

Under the conservative local coefficients,

\[
r_F=O_p(\alpha_n^{-1}r_\mu),
\qquad
q_R=O_p(\alpha_n^{-1/2}r_\mu),
\qquad
d_n=O_p(r_\mu),
\tag{15.1}
\]

apart from the faster oracle term (O(\alpha_n n^{-1/2})) and declared defects. The middle identity uses (mathcal E_2=O(\sqrt\alpha)); it would be false under fixed/growing energy, which is already excluded by (13.2).

With (A_2\asymp\alpha_n), (Delta\asymp\alpha_n^2),

\[
\frac{\eta_n}{\Delta_n}
\asymp \frac{r_{\mu,n}}{\alpha_n}
+\left(\frac{r_{\mu,n}}{\alpha_n}\right)^2.
\tag{15.2}
\]

Thus loading consistency and a nonempty threshold window both require

\[
r_{\mu,n}=o(\alpha_n),
\tag{15.3}
\]

which, using (12.2), is exactly (11.1). This also implies the weaker quadratic-Log, stage, grid, cell, and (q_R\to0) conditions.

### 15.2 Null spectrum and selection

E correctly retains the row min--max conclusion

\[
\widehat\lambda_{r_n+1}\le d_n^2
\tag{15.4}
\]

only under exact rank-(r_n) population-row factorisation. With lag contamination, the clean-target comparison must absorb (zeta_n) into total row error; otherwise the population rank may already exceed (r_n).

The explicit threshold $\tau_n=(\bar d_n^2\Delta_n)^{1/2}$ is valid when $\bar d_n^2=o(\Delta_n)$. The assembly condition remains separately necessary when $A_2$ is not tied to $\sqrt\Delta$. A ridged ratio still needs its internal nonzero-spectrum condition, and the raw ratio remains false.

The bounded two-state local-alternative attack from Section 6.4 still proves a sampling impossibility at (s_n\asymp n^{-1/2}). It does not defeat the local branch, whose signal-to-noise ratio is fixed after division by the common amplitude scale (a_n).

## 16. Self-similar arbitrary-polynomial inactive-dimension branch

The repaired E Section 7.4 construction survives all attacks. Let (a_n=\sqrt{\alpha_n}), scale one fixed noncommuting active block, its support, mean path, law jets, and factor amplitude by (a_n), and add only deterministic inactive coordinates. Then

\[
v_\mu,a_\mu,\mathcal E_2=O(a_n),
\quad B_3=O(a_n^3),
\quad A_2\asymp a_n^2,
\quad\Delta\asymp a_n^4.
\tag{16.1}
\]

With (h_n=n^{-1/7}), (M_n\asymp n^{2/7}),

\[
r_\mu=O(a_nn^{-3/7}),
\quad r_F=O(n^{-3/7}),
\quad q_R=O(a_nn^{-3/7}),
\quad d_n=O(a_n^2n^{-3/7}),
\quad \eta_n/\Delta_n=O(n^{-3/7}).
\tag{16.2}
\]

Every generated displacement divided by its proportional slack tends to zero. Polynomial object counts add only logarithms, and deterministic inactive coordinates add neither energy nor product noise. Therefore any fixed polynomial (m_n=n^x) is admissible when (alpha_n=m_n^{-A}) and the physical model dilates as above.

This branch is deliberately nonpervasive. It proves the impossibility of a universal direct (m_n)-restriction; it does not prove that arbitrary active dimension, growing rank, or growing energy is harmless.

## 17. New retained-hypothesis counterexample search

The frozen theorem was re-attacked with the following families.

| Family | Attempted failure | Result |
|---|---|---|
| scalar/commuting roots | expose artificial (alpha)-powers | rejects sharpness of raw composite powers, but lies in the flat restricted submodel; no failure of sufficient local theorem |
| repeated-spectrum noncommuting block | remove eigenvector-gap dependence while retaining curvature blow-up | agrees with D's (alpha^{-1}) curvature coefficient |
| polar-near-singular rotation | force extra (chi_P) power | already captured by (chi_P^{-k}); invalid when (p<\alpha) is claimed active for factored banded inputs |
| Exp factor near rank loss | force forward derivative blow-up | fails: forward Exp remains polynomial; only closure/inverse consumers fail |
| one bad grid vertex | escape despite RMS consistency | repaired by (sqrt M r_\mu=o(\delta_*)) |
| many zero-length varying segments | remove generic segment count | repaired by retaining the Bell (M+\mathsf L) budget; PF uses a different coherent area proof |
| high-frequency rotating eigenvectors | hide acceleration under total length | repaired by explicit (v_\mu,a_\mu) and cell-size tests |
| fixed/growing energy with shrinking (alpha) | overpower frame and row terms | violates strict normal support (13.2); proves theorem-class incompatibility, not failure |
| weakened lag signal | defeat loading/selection | repaired by exact (A_2,d,\Delta) assembly and threshold window |
| concentrated/generated-object tail | defeat complete GD probability | repaired by object counts and unconditional escape condition |
| active dimension added with independent noise | force a direct (m) sampling term | not covered by the inactive-coordinate construction; must enter through energy/product budgets as E states |

No new family satisfying the complete fractional-normal slacks, shrinking support, supplied path jets, dependence/product conditions, exact target, and actual gap violates the corrected sufficient theorem.

## 18. Scope of U-D1--U-D4

The four unresolved entries remain genuine but narrowly scoped.

| ID | What remains OPEN | What is already proved despite it |
|---|---|---|
| U-D1 | smallest joint ((a,B,p)) powers of higher factored alignment derivatives | exact polar primitive; finite raw recurrence; local intrinsic first/cubic consumer bounds |
| U-D2 | sharp endpoint-Jacobi envelope outside fractional-normal cells | fractional-normal cell theorem and PF telescoping |
| U-D3 | smallest powers for higher complete nonlocal Richardson/blend/ruled derivatives | local homogeneity (a^{1-k}) and sufficient cubic-bias/PF coefficients |
| U-D4 | minimized closed polynomial for all higher endpoint-PT derivatives | exact finite Bell recurrence with supplied path jets; PT isometry; first-order PF area route |

They block a claim of one sharp unrestricted monomial and a sharp maximum (m_n)-window. They do **not** block:

- the restricted fractional-normal sufficient theorem;
- the conservative window (11.1);
- the self-similar active-block construction;
- an unrestricted theorem stated with the exact finite raw recurrences rather than minimized exponents, provided every nonlocal margin/no-conjugacy hypothesis is separately checked.

## 19. Gate recommendation to the lead

### Strongest theorem earned

Recommend the Stage 2 verdict:

> **PROVED UNDER EXPLICIT RESTRICTED FRACTIONAL-NORMAL ASSUMPTIONS, WITH SUFFICIENT RATHER THAN GLOBALLY SHARP GROWTH WINDOWS.**

The theorem should state the D interface

\[
K_S,K_{R1},K_G,K_{L1},K_C=O(1),
\quad K_B=O(1+\alpha_n^{-1}),
\quad K_{L2}=O(\alpha_n^{-1/2}),
\quad K_F=O(\alpha_n^{-1}),
\quad\rho_H=O(\sqrt{\alpha_n}),
\tag{19.1}
\]

only on complete fractional-normal generated domains with strict population score-pair slack, proportional polar/Exp/factor slacks, shrinking support (O(\sqrt\alpha)), and fractional-normal PF cells. It should then propagate E (E.2)--(E.20) without suppressing path, energy, lag, object-count, target, (A_2), or actual-gap inputs.

The explicit conservative corollary is (x<3/(5A)) under its matched rank-one/local assumptions. It must be called **sufficient**, not sharp. The self-similar branch should be recorded as an attainability result showing that no universal direct polynomial (m_n)-ceiling exists.

### Exact impossibility statements earned

The campaign may mark the following as analytically impossible for the stated theorem classes:

1. a full-rank uniform normal/generated radius of order larger than (sqrt{\alpha_n}) for a class reaching the lower spectral edge;
2. a fixed- or growing-energy full-noncommuting branch under a shrinking positive-G1 normal-pair support radius;
3. a geometry-only or margin-only (m_n)-window;
4. a general noncommuting PF curvature coefficient (o(\alpha_n^{-1}));
5. an active polar derivative bound (o(\chi_{P,n}^{-1}));
6. a complete generated event from RMS grid error without either the (sqrt M) cost or a proved sup event;
7. loading or factor selection without the exact assembly/gap and row-square separation conditions;
8. using repeated positive eigenvalue gaps as a required BW margin;
9. assigning an inverse (chi_E) power to forward Exp merely because rank loss is near.

### Items that must remain OPEN

U-D1--U-D4 remain `OPEN — EXACT EXPONENT MINIMISATION STATED`. They are optional sharpness improvements for the restricted theorem but mandatory before claiming an unrestricted globally sharp monomial or sharp maximum matrix-growth boundary.

This hostile pass finds no basis for a Stage 2 disproof of every shrinking-margin theorem. It supports a restricted sufficient theorem plus the exact impossibility boundaries above.
