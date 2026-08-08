---
type: proof-dossier
title: HD1-B — lag operator signal and factor number proof dossier
status: current-proof-input
verdict: PROVED UNDER EXPLICIT ASSUMPTIONS; unrestricted curved-space quadratic recentering DISPROVED
last-audited: 2026-08-08
area:
  - time-series
  - factor-models
  - high-dimensional-statistics
---

# HD1-B — lag operator signal and factor number proof dossier

This is Workstream B's independent proof input for the growing-dimension Paper 1 run. It does not edit or supersede the canonical files. It treats the growing-dimension G1 and G1′ conclusions as explicit inputs and proves the lag-operator, signal/eigengap, loading, and factor-number chain conditional on those inputs. Paper 2 is not used.

The principal conclusions are:

1. factor signal and lag-operator eigengap are different quantities. Under exact lag-orthogonal noise,
   \(\Delta_n=\lambda_{\min}(\sum_h C_{f,n}(h)C_{f,n}(h)^*)\), and a full-rank included lag gives \(\Delta_n\ge s_n^2\);
2. Hilbert–Schmidt lag-covariance concentration is dimension-free under bounded total tangent energy and a causal finite-memory assumption. No net in \(\mathbb R^{p_n}\) is used;
3. on a curved manifold, the currently used assertion that mean recentering enters the lag covariance only quadratically is false without an additional geometric lag-orthogonality condition. Cross-fitting removes estimator/observation coupling but does not remove the observation-dependent Hessian in the derivative of the log map;
4. a robust derivative-free polygonal estimator bypasses that orthogonality issue: a controlled vertex-grid RMS bound gives feasible-observation RMS \(q_n=O_p(\rho_n)\), hence lag-row error \(O_p(n^{-1/2}+\rho_n)\). The sharper cross-fitted route is also quantified under geometric lag orthogonality. Non-rigid frame error is conservatively additive and pays \(\Delta_n^{-1}\); only a genuine rigid conjugation receives a no-gap treatment;
5. the row-operator structure gives the genuinely sharper beyond-rank bound \(\hat\lambda_{r_n+1}\le d_n^2\), where \(d_n\) is the lag-row error. Generic Weyl alone would give only first order;
6. the unregularised eigenvalue-ratio selector can over-select even in a deterministic rank-one example. A threshold selector is consistent, and a ridge-ratio selector is consistent when \(d_n^2=o(\tau_n)\), \(\tau_n=o(\Delta_n)\), and the nonzero population eigenvalue ratios do not collapse;
7. level-only local stationarity contributes \(n^{-a}/b_n\) to G1′. It enters the non-rigid frame term through \(r_{0,n}r_{1,n}\), including \(n^{-2a}/b_n\); it must not be silently replaced by \(n^{-a}\).

## 1. Spaces, operator orientation, and population target

For every \(n\), let \(H_n=T_{\mu_n(u_0)}M_n\), a real Hilbert space of finite dimension \(p_n\), with \(p_n\to\infty\) allowed. All observations below have already been transported to \(H_n\) in the true parallel frame. For \(x,y\in H_n\),

\[
(x\otimes y)z=\langle y,z\rangle x.
\]

Thus \(x\otimes y:H_n\to H_n\), \((x\otimes y)^*=y\otimes x\), and

\[
\|x\otimes y\|_{\mathrm{HS}}=\|x\|\,\|y\|.
\]

Let \(I_n\) be the set of evaluation indices in the block-split construction of Section 5 and let \(N_{n,h}=|\{t\in I_n:t-h\in I_n\}|\). Define the exact finite-array population lag covariance

\[
\Gamma_n(h)=N_{n,h}^{-1}\sum_{t\in I_n:\,t-h\in I_n}
\mathbb E(Y_{t,n}\otimes Y_{t-h,n}),\qquad 1\le h\le H_n^0,
\]

where \(H_n^0=h_{0,n}\) is the largest included lag. This finite-array average is the right target for a locally stationary triangular array. Targeting it avoids an unnecessary \(n^{-a}\) approximation to an ideal stationary covariance. If the covariance curve is Lipschitz and one instead wants the full-design Riemann integral, the deterministic mask/Riemann error is \(O(\ell_n/n)\), where \(\ell_n\) is the block length.

Define the row operator

\[
\mathcal G_n:H_n^{\oplus H_n^0}\to H_n,\qquad
\mathcal G_n(x_1,\ldots,x_{H_n^0})=\sum_{h=1}^{H_n^0}\Gamma_n(h)x_h,
\]

and

\[
\mathbb L_n=\mathcal G_n\mathcal G_n^*
=\sum_{h=1}^{H_n^0}\Gamma_n(h)\Gamma_n(h)^*.
\]

The empirical definitions use the same orientation and the same evaluation mask. This convention removes the fibre/type ambiguity in the old displays.

## 2. Signal strength is not the eigengap

Assume a rank-\(r_n\) isometry \(A_n:\mathbb R^{r_n}\to H_n\) and

\[
Y_{t,n}=A_nf_{t,n}+\varepsilon_{t,n}.
\]

The exact included-lag noise assumption is

\[
\mathbb E(\varepsilon_{t,n}\otimes\varepsilon_{t-h,n})=0,
\quad
\mathbb E(A_nf_{t,n}\otimes\varepsilon_{t-h,n})=0,
\quad
\mathbb E(\varepsilon_{t,n}\otimes A_nf_{t-h,n})=0
\tag{LN}
\]

for every retained \(t,h\). These are moment restrictions, not independence assertions. Contemporaneous and time-varying idiosyncratic covariance is unrestricted by (LN).

Put

\[
C_{f,n}(h)=N_{n,h}^{-1}\sum_t\mathbb E(f_{t,n}\otimes f_{t-h,n}),
\qquad
B_n=\sum_{h=1}^{H_n^0}C_{f,n}(h)C_{f,n}(h)^*.
\]

Then (LN) gives \(\Gamma_n(h)=A_nC_{f,n}(h)A_n^*\).

> **Theorem B1 (exact signal/eigengap relationship — PROVED).** Suppose (LN) holds and \(\operatorname{rank}B_n=r_n\). Let
> \[
> s_n=\max_{1\le h\le H_n^0}\sigma_{r_n}(C_{f,n}(h)),
> \qquad
> \Delta_n=\lambda_{r_n}(\mathbb L_n)-\lambda_{r_n+1}(\mathbb L_n).
> \]
> Then
> \[
> \operatorname{ran}\mathbb L_n=E_n:=\operatorname{ran}A_n,
> \quad \lambda_{r_n+1}(\mathbb L_n)=0,
> \quad \Delta_n=\lambda_{\min}(B_n)>0,
> \quad \Delta_n\ge s_n^2.
> \tag{2.1}
> \]
> The last inequality is useful only when at least one included lag has full rank. Full rank of \(B_n\) is weaker and is equivalent to
> \(\bigcap_{h=1}^{H_n^0}\ker C_{f,n}(h)^*=\{0\}\).

**Proof.** Since \(A_n^*A_n=I_{r_n}\),

\[
\mathbb L_n
=\sum_hA_nC_hA_n^*A_nC_h^*A_n^*
=A_nB_nA_n^*.
\]

The nonzero eigenvalues are exactly those of \(B_n\), its range is \(A_n\operatorname{ran}B_n=E_n\), and it vanishes on \(E_n^\perp\). Hence the first three conclusions follow. For each \(h\), \(B_n\succeq C_hC_h^*\), so

\[
\lambda_{\min}(B_n)\ge\lambda_{\min}(C_hC_h^*)=\sigma_{r_n}(C_h)^2.
\]

Maximising proves (2.1). Finally,
\(x^*B_nx=\sum_h\|C_h^*x\|^2\), proving the kernel statement. ∎

The comparison can be strict, and \(s_n\) can be zero although \(\Delta_n>0\). For \(r_n=2\), take
\(C_1=\operatorname{diag}(1,0)\) and \(C_2=\operatorname{diag}(0,1)\). Then \(s_n=0\) but \(B_n=I_2\) and \(\Delta_n=1\). Thus the honest theorem is always written with \(\Delta_n\); an \(s_n^{-2}\) corollary is available only under the full-rank-lag condition.

If (LN) fails, write \(\Gamma_n(h)=A_nC_{f,n}(h)A_n^*+D_n(h)\). The loading space is no longer exactly the range of the population lag operator. With

\[
d_{\mathrm{LN},n}=\Big(\sum_h\|D_n(h)\|_{\mathrm{op}}^2\Big)^{1/2},
\quad
A_{2,n}=\Big(\sum_h\|C_{f,n}(h)\|_{\mathrm{op}}^2\Big)^{1/2},
\]

the deterministic assembly lemma below gives population contamination at most
\(2A_{2,n}d_{\mathrm{LN},n}+d_{\mathrm{LN},n}^2\). Exact factor-number recovery needs (LN), or a threshold exceeding this approximate-rank contamination.

### Bounded total energy and factor strength

If \(\|Y_{t,n}\|\le R\) almost surely, all covariance and Hilbert–Schmidt constants for the observed lag process below are independent of \(p_n\). This does **not** by itself bound factor energy: \(A_nf_{t,n}\) and \(\varepsilon_{t,n}\) can cancel contemporaneously. For the following factor-strength compatibility statement, separately assume \(\|f_{t,n}\|\le R_f\) almost surely (a uniform second-moment total-factor-energy bound gives the analogous conclusion). This regime is compatible with a fixed positive \(\Delta_n\) when \(r_n\) is fixed. It is not compatible with classical pervasive-factor eigenvalues diverging like \(p_n\). If \(r_n\to\infty\), bounded total factor energy forces some signal to weaken: for example,

\[
\lambda_{\min}(B_n)\le r_n^{-1}\operatorname{tr}B_n
\le r_n^{-1}\sum_h\|C_{f,n}(h)\|_{\mathrm{HS}}^2
\le H_n^0R_f^4/r_n.
\]

This is the precise compatibility statement missing from the old strong-factor discussion.

## 3. Dimension-free Hilbert-valued concentration

The short-memory framework used in this dossier is deliberately explicit. There are iid innovations \((\xi_t)_{t\in\mathbb Z}\) and integers \(m_n\ge0\) such that, for deterministic measurable maps allowed to depend on \(t,n\),

\[
Y_{t,n}=G_{t,n}(\xi_t,\ldots,\xi_{t-m_n}),
\qquad \|Y_{t,n}\|\le R\quad\text{a.s.}
\tag{SM}
\]

This is a triangular, nonstationary, causal finite-memory condition. It is stronger than generic polynomial mixing but gives the needed conditional decoupling and dimension-uniform Hilbert inequalities without an unproved infinite-dimensional blocking step.

> **Lemma B2 (Hilbert \(m\)-dependent second-moment inequality — PROVED).** Let \(Z_1,\ldots,Z_N\) be centred random elements of a real Hilbert space \(\mathcal H\), with \(Z_s\) independent of \(Z_t\) when \(|s-t|>d\). Then
> \[
> \mathbb E\Big\|N^{-1}\sum_{t=1}^NZ_t\Big\|^2
> \le {2d+1\over N^2}\sum_{t=1}^N\mathbb E\|Z_t\|^2.
> \tag{3.1}
> \]

**Proof.** Expand the squared norm. Terms with \(|s-t|>d\) have zero expected inner product by independence and centring. For the remaining terms use
\(2|\langle Z_s,Z_t\rangle|\le\|Z_s\|^2+\|Z_t\|^2\). Each diagonal term is counted at most \(2d+1\) times. ∎

> **Theorem B3 (dimension-free oracle lag-row concentration — PROVED).** Under (SM), let
> \[
> \widetilde\Gamma_n(h)=N_{n,h}^{-1}\sum_{t\in I_n:t-h\in I_n}
> Y_{t,n}\otimes Y_{t-h,n}.
> \]
> If \(N_n=\min_{h\le H_n^0}N_{n,h}\asymp n\), then
> \[
> d_{\mathrm{or},n}:=
> \Big(\sum_{h=1}^{H_n^0}
> \|\widetilde\Gamma_n(h)-\Gamma_n(h)\|_{\mathrm{HS}}^2\Big)^{1/2}
> =O_p\!\left(R^2\sqrt{\frac{H_n^0(m_n+H_n^0+1)}{N_n}}\right).
> \tag{3.2}
> \]
> The constant is numerical and has no \(p_n\) dependence.

**Proof.** Work in the Hilbert direct sum
\(\mathcal S_2(H_n)\) separately at each lag. For lag \(h\), the centred product has norm at most \(2R^2\) and dependence range at most \(m_n+h\). Lemma B2 gives

\[
\mathbb E\|\widetilde\Gamma_n(h)-\Gamma_n(h)\|_{\mathrm{HS}}^2
\le C R^4{m_n+h+1\over N_{n,h}}.
\]

Summing this inequality over \(h\le H_n^0\), using \(N_{n,h}\ge N_n\), and applying Markov's inequality to the nonnegative sum proves (3.2). No scalarisation or net is present. ∎

The same proof permits norm-sub-Gaussian tails if one supplies a Hilbert-valued Bernstein inequality, but no such external result is consumed here. The proved \(L^2\) result is enough for the loading and selector theorems.

## 4. Curved recentering: the missing orthogonality

Let \(q=\mu_n(u_t)\), \(x=X_{t,n}\), \(Y=\log_qx\), and \(q_e=\operatorname{Exp}_q(e)\). Let \(\Phi_e:T_qM_n\to T_{q_e}M_n\) be radial parallel transport. Uniform \(C^2\) control of the base-point log map on the common tube gives

\[
\Phi_e^{-1}\log_{q_e}x
=Y-H(q,x)e+\mathcal R(q,x,e),
\qquad \|\mathcal R(q,x,e)\|\le J\|e\|^2,
\tag{4.1}
\]

where \(H(q,x)=\tfrac12\operatorname{Hess}_q d(q,x)^2\), and \(\|H(q,x)\|\le J\). The sign follows because \(\nabla_q\tfrac12d(q,x)^2=-\log_qx\).

In Euclidean space \(H=I\), so the derivative of lag covariance is killed by \(\mathbb EY=0\). In curved space \(H(q,X)\) is random. The relevant assumption is therefore

\[
\mathbb E\{H_t v\otimes Y_{t-h}\}=0,
\qquad
\mathbb E\{Y_t\otimes H_{t-h}v\}=0
\quad\text{for every deterministic }v\in H_n
\tag{GLO}
\]

at every retained \(t,h\), after true-frame identification. A sufficient condition on a locally symmetric space is joint central symmetry of the transported process: the law of every finite vector \((Y_{t_1},\ldots,Y_{t_k})\) is invariant under simultaneous sign reversal. The geodesic symmetry is an isometry fixing \(q\), hence \(H(q,\operatorname{Exp}_qY)=H(q,\operatorname{Exp}_q(-Y))\); the integrands in (GLO) are odd under simultaneous reversal.

> **Counterexample B4 (cross-fitting is not geometric orthogonality — DISPROVED).** There is a bounded, geometrically mixing, two-state process on the hyperbolic plane with Fréchet mean \(q\) for which (GLO) fails.

**Construction and proof.** Fix a geodesic through \(q\) with unit tangent \(e_1\), and an orthogonal unit vector \(e_2\). Let a stationary two-state Markov chain take values
\(Y_t=ae_1\) and \(Y_t=-be_1\), with transition matrix

\[
P=\begin{pmatrix}1-\alpha&\alpha\\ \beta&1-\beta\end{pmatrix},
\qquad 0<\alpha,\beta<1,
\]

stationary probabilities \(\pi_+=\beta/(\alpha+\beta)\), \(\pi_-=\alpha/(\alpha+\beta)\), and choose \(b=\beta a/\alpha\). Then \(\mathbb EY_t=0\), so because the support lies on one geodesic in a Hadamard space, \(q\) is the unique Fréchet mean. The chain is bounded, irreducible, aperiodic, and geometrically mixing.

On curvature \(-1\), the squared-distance Hessian has eigenvalue \(1\) radially and
\(\lambda(r)=r\coth r\) orthogonally. Therefore \(H_t e_2=\lambda(\|Y_t\|)e_2\), and direct calculation gives

\[
\mathbb E\{\lambda(\|Y_t\|)Y_{t-1}\}
=\pi_+a(1-\alpha-\beta)\{\lambda(a)-\lambda(b)\}.
\]

This is nonzero whenever \(\alpha+\beta\ne1\) and \(\alpha\ne\beta\). Hence
\(\mathbb E(H_te_2\otimes Y_{t-1})\ne0\). Even if a deterministic or independently trained centre perturbation \(e=\epsilon e_2\) is cross-fitted, (4.1) changes the lag covariance linearly in \(\epsilon\). Cross-fitting removes dependence between \(e\) and the evaluation chain; it does not remove \(H_t\)'s dependence on the evaluation observation. ∎

Thus the old generic claim \(M_e=O(r_{0,n}^2)\) is valid in flat geometry and under (GLO), but not under mean zero alone. Without (GLO), the safe recentering order is \(O(r_{0,n})\), which generally destroys the advertised oracle rate.

> **Lemma B5 (cross-fitted recentering bound under GLO — PROVED).** Suppose (4.1), (GLO), (SM), and let the centre errors \(e_t\) be measurable with respect to a training sigma-field independent of the innovations used by the evaluation blocks. Put
> \[
> r_{0,n}^2=N_n^{-1}\sum_{t\in I_n}\|e_t\|^2,
> \qquad \max_t\|e_t\|=o_p(1).
> \]
> Conditional on the training field,
> \[
> d_{\mathrm{mean},n}
> =O_p\!\left(
> \sqrt{H_n^0}\left[J Rr_{0,n}\sqrt{\frac{m_n+H_n^0+1}{N_n}}
> +C_{R,J}r_{0,n}^2\right]\right),
> \tag{4.2}
> \]
> where \(d_{\mathrm{mean},n}\) is the direct-sum HS norm of the recentered-minus-oracle lag covariances after radial connector identification.

**Proof.** Substitute (4.1) in each lagged rank-one product. The two terms linear in \(e\) have conditional expectation zero by (GLO). Their HS norms are bounded by a constant times \(JR(\|e_t\|+\|e_{t-h}\|)\). Lemma B2, conditionally on the training sigma-field, bounds their direct-sum sample average by the first term in (4.2). Every remaining term contains either one Taylor remainder or two linear perturbations. The triangle inequality, Cauchy–Schwarz, and shift invariance of the empirical \(L^2\) norm bound their direct-sum average by the second term. ∎

## 5. A cross-fitting construction that really decouples

The following construction is one sufficient route, not a claim that arbitrary \(K\)-fold cross-fitting works for dependent data.

Partition \(\{1,\ldots,n\}\) into consecutive blocks of length \(\ell_n\). Colour them alternately training and evaluation. In every evaluation block retain only the core obtained by deleting
\(g_n=m_n+H_n^0\) indices from each boundary. Estimate the entire mean curve and frame used on evaluation cores from training-block cores only. Use only lag products lying within one retained evaluation core. Require

\[
g_n=o(\ell_n),\qquad \ell_n=o(nb_n),\qquad N_n\asymp n.
\tag{CF}
\]

Under the causal representation (SM), an evaluation core and the training sigma-field use disjoint innovation sets. They are therefore independent, not merely uncorrelated. The condition \(\ell_n=o(nb_n)\) ensures every bandwidth window contains a fixed positive fraction of training design points and gives the same weight orders
\(\max_t|w_t|=O((nb_n)^{-1})\) and \(\sum_tw_t^2=O((nb_n)^{-1})\). It does not, by itself, preserve the ordinary-grid third-order bias. The periodic mask has cumulative discrepancy \(O(\ell_n)\) inside a bandwidth window, producing a normalised moment defect \(O(\ell_n/(nb_n))\), a level bias \(O(\ell_n/n)\), and a derivative defect \(O(\ell_n/(nb_n))\). The correct perforated-design inputs are therefore

\[
r_{0,n}^{\mathrm{CF}}
=b_n^3+\sqrt{\frac{m_n+1}{nb_n}}+n^{-a}+\frac{\ell_n}{n},
\qquad
r_{1,n}^{\mathrm{CF}}
=b_n^3+\sqrt{\frac{m_n+1}{nb_n^3}}+\frac{n^{-a}}{b_n}
+\frac{\ell_n}{nb_n},
\tag{5.1}
\]

up to the ordinary \(n^{-1}\) grid terms. Workstream A's G1/G1′ theorem must be applied to this deterministic perforated design with (5.1). The simpler rates are retained only if \(m_n=O(1)\), \(\ell_n/n=O(r_{0,n})\), and \(\ell_n/(nb_n)=O(r_{1,n})\). At \(b_n=n^{-1/5}\), \(\ell_n=O(n^{3/5})\) is sufficient and is compatible with \(m_n+H_n^0=o(\ell_n)=o(nb_n)\).

Only one evaluation colour is used in the theorem. This loses a constant fraction of observations but preserves \(N_n\asymp n\) and, importantly, produces one training-measurable rigid frame rotation. Combining both colours without aligning their two random frames is not covered by the proof.

For a stationary transported process, the mask causes no population bias after normalisation. For a Lipschitz locally stationary covariance curve, the masked finite-array target still has range \(A_n\). If it is compared with the unmasked integral target, the deterministic discrepancy is \(O(\ell_n/n)\). Lag truncation creates no bias relative to \(\mathbb L_n\); it enters only through the requirement \(\operatorname{rank}B_n=r_n\). Approximation to an infinite-lag operator separately requires a proved tail bound and is not consumed here.

## 6. Frame: what receives a gap and what does not

After connector identification and recentering, let \(\bar Y_{t,n}\) denote the vectors before using the estimated parallel frame. The frame input is stated at the exact level needed by P1-OP:

* there is a training-measurable orthogonal \(Q_n:H_n\to H_n\) with
  \(\|Q_n-I\|_{\mathrm{op}}=O_p(\omega_n)\);
* after undoing \(Q_n\), the non-rigid frame part changes the lag row by direct-sum HS norm at most \(\phi_n\):
  \[
  \left\{\sum_h\left\|
  N_{n,h}^{-1}\sum_tQ_n^*\hat Y_{t,n}\otimes Q_n^*\hat Y_{t-h,n}
  -N_{n,h}^{-1}\sum_t\bar Y_{t,n}\otimes\bar Y_{t-h,n}
  \right\|_{\mathrm{HS}}^2\right\}^{1/2}
  =O_p(\phi_n).
  \tag{FR}
  \]

(FR) is an explicit G1′/ribbon input, not a hidden lemma. A crude sufficient vector-level condition is
\(N_n^{-1}\sum_t\|Q_n^*\hat Y_t-\bar Y_t\|^2=O_p(v_n^2)\), which gives
\(\phi_n=O_p(\sqrt{H_n^0}(Rv_n+v_n^2))\) by Cauchy–Schwarz. A sharper ribbon argument may establish

\[
\omega_n=O_p\{\Lambda_nL_n(b_n^3+n^{-a}+n^{-1/2})\},
\qquad
\phi_n=O_p\{\sqrt{H_n^0}\Lambda_n r_{0,n}r_{1,n}+c_{\mathrm{disc},n}\}.
\tag{6.1}
\]

This dossier uses (6.1) only when explicitly invoked. A proof of G1′ under level-only local stationarity must use

\[
r_{0,n}=b_n^3+(nb_n)^{-1/2}+n^{-a},
\qquad
r_{1,n}=b_n^3+(nb_n^3)^{-1/2}+n^{-a}/b_n.
\tag{6.2}
\]

Consequently \(\phi_n\) contains \(r_{0,n}r_{1,n}\), in particular \(n^{-2a}/b_n\), as well as the cross terms involving \(n^{-a}/b_n\). The suspected derivative term is real unless a stronger differentiable local-stationarity assumption proves its removal.

Only \(Q_n\) is a rigid conjugation. It maps \(E_n\) exactly to \(Q_nE_n\), and

\[
\|\sin\Theta(Q_nE_n,E_n)\|_{\mathrm{op}}
\le\|Q_n-I\|_{\mathrm{op}}.
\tag{6.3}
\]

No eigengap is paid in (6.3). In contrast, \(\phi_n\) is a non-rigid lag-row error and is placed in the additive channel; claiming that it has no gap penalty would require a further exact conjugation proof.

## 7. Deterministic row-operator assembly

> **Lemma B6 (lag row to lag operator — PROVED).** Let
> \(\widehat\Gamma_h=Q\Gamma_hQ^*+D_h\), with \(Q\) orthogonal, and put
> \[
> A_2=\left(\sum_h\|\Gamma_h\|_{\mathrm{op}}^2\right)^{1/2},
> \qquad d=\left(\sum_h\|D_h\|_{\mathrm{op}}^2\right)^{1/2}.
> \]
> Then
> \[
> \|\widehat{\mathbb L}-Q\mathbb LQ^*\|_{\mathrm{op}}
> \le 2A_2d+d^2.
> \tag{7.1}
> \]
> If \(\operatorname{rank}\mathbb L=r\), then
> \[
> \lambda_{r+1}(\widehat{\mathbb L})\le d^2.
> \tag{7.2}
> \]

**Proof.** Let \(\mathcal G=[\Gamma_1\ \cdots\ \Gamma_H]\),
\(\widehat{\mathcal G}=[\widehat\Gamma_1\ \cdots\ \widehat\Gamma_H]\), and
\(\mathcal D=[D_1\ \cdots\ D_H]\) as row operators from \(H^{\oplus H}\) to \(H\). Then
\(\|\mathcal G\|\le A_2\), \(\|\mathcal D\|\le d\), and

\[
\widehat{\mathbb L}-Q\mathbb LQ^*
=(Q\mathcal GQ_\oplus^*)\mathcal D^*
+\mathcal D(Q\mathcal GQ_\oplus^*)^*+\mathcal D\mathcal D^*,
\]

which proves (7.1). For (7.2), the \((r+1)\)-st singular value of the rank-\(r\) row operator \(Q\mathcal GQ_\oplus^*+\mathcal D\) is at most \(\|\mathcal D\|\le d\) by the singular-value min–max principle. Its square is \(\lambda_{r+1}(\widehat{\mathbb L})\). ∎

Equation (7.2), not Weyl's inequality, produces the beyond-rank square.

### A derivative-free feasible-observation bypass

There is a completely deterministic route that does not require (GLO), cross-fitted first-order cancellation, or a differentiable estimated frame. It is slower when the feasible observation error is larger than \(n^{-1/2}\), but it is the safest integration route for a polygonal-frame construction.

For this route take the full evaluation design \(I_n=\{1,\ldots,n\}\) and normalise each lag by \(N_{n,h}=n-h\). No perforated-design or deletion term is present; replacing \((n-h)^{-1}\) by \(n^{-1}\) costs at most \(O(R^2H_n^0/n)\).

Suppose one orthogonal alignment \(Q_n\) has been fixed and put

\[
\zeta_{t,n}=Q_n^*\widehat Y_{t,n}-Y_{t,n},
\qquad
q_n^2=\max_{0\le h\le H_n^0}\max\left\{
N_{n,h}^{-1}\sum_{t\in I_n:t-h\in I_n}\|\zeta_{t,n}\|^2,
N_{n,h}^{-1}\sum_{t\in I_n:t-h\in I_n}\|\zeta_{t-h,n}\|^2
\right\}.
\tag{7.3}
\]

No independence between \(\zeta_t\) and \(Y_t\) is assumed.

> **Lemma B6′ (RMS feasible-versus-oracle bound — PROVED).** If \(\|Y_{t,n}\|\le R\), then for each retained lag
> \[
> \left\|Q_n^*\widehat\Gamma_n(h)Q_n-\widetilde\Gamma_n(h)\right\|_{\mathrm{HS}}
> \le 2Rq_n+q_n^2,
> \tag{7.4}
> \]
> and hence the lag-row error satisfies
> \[
> d_{\mathrm{RMS},n}
> \le d_{\mathrm{or},n}+\sqrt{H_n^0}(2Rq_n+q_n^2)
> +d_{\mathrm{LN},n}+d_{\mathrm{mask},n}+d_{\mathrm{disc},n}.
> \tag{7.5}
> \]

**Proof.** Expand

\[
(Y_t+\zeta_t)\otimes(Y_{t-h}+\zeta_{t-h})-Y_t\otimes Y_{t-h}
=\zeta_t\otimes Y_{t-h}+Y_t\otimes\zeta_{t-h}
+\zeta_t\otimes\zeta_{t-h}.
\]

Average HS norms. Cauchy–Schwarz and the definition of \(q_n\) bound the first two averages by \(Rq_n\) each and the last by \(q_n^2\). Taking the direct-sum norm over lags gives (7.5). ∎

Combining Lemma B6′ with Lemma B6 yields, without G1′,

\[
\|\widehat{\mathbb L}_n-Q_n\mathbb L_nQ_n^*\|_{\mathrm{op}}
\le 2A_{2,n}d_{\mathrm{RMS},n}+d_{\mathrm{RMS},n}^2,
\tag{7.6}
\]

and
\(\widehat\lambda_{r_n+1,n}\le d_{\mathrm{RMS},n}^2\). For fixed lag and memory budgets this is the requested generic form

\[
d_{\mathrm{RMS},n}=O_p(n^{-1/2}+q_n+q_n^2)
\tag{7.7}
\]

up to the explicitly displayed modelling, mask, and discretisation terms. If a derivative-free polygonal-frame theorem proves \(q_n=O_p(\rho_n)\) for a feasible-observation RMS rate \(\rho_n\), then (7.5)–(7.7) close P1-OP directly. This bypass does not assert the sharper quadratic mean cancellation. It is therefore unaffected by Counterexample B4 and does not consume the \(n^{-a}/b_n\) derivative rate.

The alignment in Route R need not be training-measurable: every bound in Lemmas B6′ and B6 is pathwise. In the polygonal construction below, \(Q_n\) is the random connector/alignment at the anchor.

> **Lemma B6″ (polygonal feasible-observation RMS — PROVED UNDER UNIFORM TUBE GEOMETRY).** Suppose Workstream A's pointwise second-moment argument holds at every deterministic vertex, the mean curve has uniformly bounded speed and covariant acceleration, and the common tube has dimension-uniform Jacobi, log-Lipschitz, and curvature-area constants. Put
> \[
> \rho_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}\to0,
> \qquad M_n=\left\lceil\rho_n^{-2/3}\right\rceil,
> \]
> compute the positive three-scale mean at \(v_j=j/M_n\), join adjacent estimates by their unique geodesic chords, and parallel transport along this polygon. Then the polygon remains in the tube with probability tending to one and, after the anchor alignment \(Q_n\),
> \[
> q_n=O_p\!\left(\rho_n+\Lambda_nL_{\mu,n}\rho_n
> +\Lambda_n\rho_n^{4/3}\right).
> \tag{7.8}
> \]
> In particular, if \(\Lambda_n,L_{\mu,n}=O(1)\), then \(q_n=O_p(\rho_n)\). No derivative of the estimated mean and no concentration of the feasible transformed process is used.

**Proof.** Let
\(e_j=d\{\widehat\mu_n(v_j),\mu_n(v_j)\}\). The pointwise stage second-moment bound, the Lipschitz Richardson map, averaging over the deterministic vertices, and Markov's inequality give

\[
\left\{(M_n+1)^{-1}\sum_{j=0}^{M_n}e_j^2\right\}^{1/2}
=O_p(\rho_n).
\tag{7.9}
\]

No independence across vertices is needed. Moreover

\[
\max_je_j\le\left(\sum_je_j^2\right)^{1/2}
=O_p(\sqrt{M_n}\rho_n)=O_p(\rho_n^{2/3})=o_p(1),
\]

so the estimated vertices and their chords stay in the fixed tube by Busemann convexity. This is why a rate-controlled grid RMS is sufficient here; an unrestricted RMS statement with arbitrarily many vertices would not be.

Compare one estimated chord with the corresponding true chord. Split their connector-closed quadrilateral into two ruled geodesic triangles. Uniform Jacobi bounds on the tube bound its area by

\[
C\{M_n^{-1}(e_j+e_{j+1})+e_je_{j+1}\}.
\]

The curvature variation formula for parallel transport bounds the connector-identified cell holonomy by \(C\Lambda_n\) times this area. Summing cells and using Cauchy–Schwarz in (7.9) gives

\[
C\Lambda_n\{L_{\mu,n}\rho_n+M_n\rho_n^2\}.
\]

The area between a true \(C^2\) curve segment of length \(O(M_n^{-1})\) and its geodesic chord is \(O(M_n^{-3})\): in normal coordinates this is the product of segment length and the \(O(M_n^{-2})\) interpolation remainder, with the uniform Jacobi constant converting coordinate area to Riemannian area. Summing contributes \(C\Lambda_nM_n^{-2}\). Orthogonal transports telescope, so the same sum bounds the frame discrepancy at every cell endpoint and on every partial cell. Since
\(M_n\rho_n^2+M_n^{-2}=O(\rho_n^{4/3})\), the polygonal frame error has the last two terms in (7.8).

Busemann convexity also gives, within each cell, polygonal centre error at most the linear interpolation of \(e_j,e_{j+1}\) plus the \(O(M_n^{-2})\) true-chord error. Summing over the approximately \(n/M_n\) design points in each cell shows its design-grid RMS is \(O_p(\rho_n+M_n^{-2})=O_p(\rho_n)\). Uniform base-point log Lipschitzness converts this to the same RMS error in connector-identified log vectors. Multiplying the uniform frame discrepancy by the bounded oracle log norm and adding the two errors proves (7.8).

Finally, feasible transformation can create arbitrary long-range dependence because all vertices are data-dependent, but Lemma B6′ is deterministic conditional on the realised feasible vectors. Oracle concentration is applied only to the true \(m_n\)-dependent \(Y_{t,n}\). Therefore no unproved preservation of dependence after feasible transformation is consumed. ∎

> **Corollary B6‴ (robust polygonal P1-OP rate — PROVED).** Under Lemma B6″, (LN), (SM), bounded total oracle energy, and uniformly bounded \(m_n,H_n^0,\Lambda_n,L_{\mu,n},A_{2,n}\),
> \[
> d_n=O_p\{n^{-1/2}+\rho_n\},
> \qquad
> \|\widehat{\mathbb L}_n-Q_n\mathbb L_nQ_n^*\|_{\mathrm{op}}
> =O_p\{A_{2,n}(n^{-1/2}+\rho_n)+(n^{-1/2}+\rho_n)^2\},
> \tag{7.10}
> \]
> and
> \(\widehat\lambda_{r_n+1,n}=O_p\{(n^{-1/2}+\rho_n)^2\}\).
> At \(b_n=n^{-1/5}\), if \(a\ge2/5\), then
> \(\rho_n=O(n^{-2/5})\), the connector-aligned loading perturbation is
> \(O_p(n^{-2/5}/\Delta_n)\), and the beyond-rank eigenvalues are \(O_p(n^{-4/5})\). If an unaligned coordinate comparison is requested, add the explicit anchor rotation. If Workstream A's weaker level-localisation minimum \(a\ge1/5\) is used, retain the honest rate
> \(\rho_n=O(n^{-2/5}+n^{-a})\).

## 8. Feasible lag-operator and loading theorem

Collect the lag-row errors as

\[
d_n=d_{\mathrm{or},n}+d_{\mathrm{mean},n}+\phi_n+d_{\mathrm{LN},n}
+d_{\mathrm{mask},n}+d_{\mathrm{disc},n},
\tag{8.1}
\]

where \(d_{\mathrm{mask},n}=0\) for the exact masked finite-array target and is
\(O(\sqrt{H_n^0}\ell_n/n)\) for a Lipschitz comparison to the full-design integral. Any chordal-frame or numerical discretisation error is explicitly included in \(d_{\mathrm{disc},n}\).

There are now two fully separated routes:

* **Route R (recommended robust bypass):** use \(d_n=d_{\mathrm{RMS},n}\) from (7.5). It needs only a feasible-observation RMS theorem and no derivative or GLO assumption;
* **Route S (sharper cross-fitted route):** use (8.1) with Lemma B5 and (FR). It obtains quadratic mean recentering but requires GLO and a proved non-rigid frame rate.

> **Theorem B7 (growing-\(p_n\) feasible lag operator — PROVED UNDER EXPLICIT ASSUMPTIONS).** Assume (LN), (SM), (CF), the tube Taylor bound (4.1), (GLO), cross-fitted G1 level error \(r_{0,n}\), and frame input (FR). Then, for arbitrary \(p_n\),
> \[
> d_n=O_p\!\left[
> R^2\sqrt{\frac{H_n^0(m_n+H_n^0+1)}{n}}
> +\sqrt{H_n^0}\left\{JRr_{0,n}\sqrt{\frac{m_n+H_n^0+1}{n}}
> +C_{R,J}r_{0,n}^2\right\}
> +\phi_n+d_{\mathrm{mask},n}+d_{\mathrm{disc},n}
> \right],
> \tag{8.2}
> \]
> and
> \[
> \|\widehat{\mathbb L}_n-Q_n\mathbb L_nQ_n^*\|_{\mathrm{op}}
> \le 2A_{2,n}d_n+d_n^2.
> \tag{8.3}
> \]
> Every displayed constant is independent of \(p_n\). Its dependence is only on the total-energy bound \(R\), tube derivative bound \(J\), and the explicitly displayed memory, lag, mean, frame, and design quantities.

**Proof.** The oracle term is Theorem B3, recentering is Lemma B5, and (FR) supplies the non-rigid frame term. Triangle inequality in the direct-sum Hilbert–Schmidt norm gives (8.2), which also bounds the row operator norm. Lemma B6 gives (8.3). ∎

For fixed \(H_n^0,m_n,R,J,A_{2,n}\), the positive-weight \(q=3\) G1 rate and (6.1) give the transparent form

\[
d_n=O_p\left\{n^{-1/2}+r_{0,n}^2+\Lambda_nr_{0,n}r_{1,n}
+d_{\mathrm{mask},n}+d_{\mathrm{disc},n}\right}.
\tag{8.4}
\]

The target \(n^{-1/2}+b_n^6+(nb_n)^{-1}+n^{-2a}\) is therefore correct for the oracle-plus-mean additive channel under (GLO), but it omits the non-rigid frame product. Under level-only local stationarity the complete theorem must retain
\(\Lambda_nr_{0,n}r_{1,n}\), including \(n^{-2a}/b_n\).

> **Theorem B8 (loading space — PROVED).** Under either Theorem B7 (Route S) or Lemma B6′ together with (7.6) (Route R), suppose \(\Delta_n>0\) and
> \(2A_{2,n}d_n+d_n^2=o_p(\Delta_n)\). If \(\widehat E_n\) is the top \(r_n\) eigenspace of \(\widehat{\mathbb L}_n\), then
> \[
> \|\sin\Theta(Q_n^*\widehat E_n,E_n)\|_{\mathrm{op}}
> \le {2\{2A_{2,n}d_n+d_n^2\}\over\Delta_n}.
> \tag{8.5}
> \]
> This is the intrinsic connector-aligned conclusion. If \(Q_n\) is represented as a rotation in a preselected common coordinate system and an unaligned comparison is desired, then additionally
> \[
> \|\sin\Theta(\widehat E_n,E_n)\|_{\mathrm{op}}
> \le \|Q_n-I\|_{\mathrm{op}}
> +{2\{2A_{2,n}d_n+d_n^2\}\over\Delta_n}.
> \tag{8.6}
> \]
> If an included lag is full rank, (2.1) permits the weaker denominator \(s_n^2\):
> \[
> O_p\left({A_{2,n}d_n+d_n^2\over s_n^2}\right)
> \]
> for the aligned space, with \(\omega_n=\|Q_n-I\|_{\mathrm{op}}\) added only for the unaligned convention.

**Proof.** Apply the self-adjoint Davis–Kahan sin-Theta inequality to
\(\widehat{\mathbb L}_n\) and \(Q_n\mathbb L_nQ_n^*\), using (8.3) and gap \(\Delta_n\). This compares \(\widehat E_n\) with \(Q_nE_n\), equivalently \(Q_n^*\widehat E_n\) with \(E_n\), and proves (8.5). The projector triangle inequality and (6.3) give (8.6) when the unaligned convention is used. ∎

The weak-factor condition is \(A_{2,n}d_n+d_n^2=o(\Delta_n)\), not a condition involving \(\Delta_n^2\). In the full-rank-lag corollary it is enough that this perturbation be \(o(s_n^2)\).

### The bandwidth \(b_n=n^{-1/5}\)

With \(b_n=n^{-1/5}\), (6.2) gives

\[
r_{0,n}=O_p(n^{-2/5}+n^{-a}),
\qquad
r_{1,n}=O_p(n^{-1/5}+n^{-a+1/5}),
\]

and therefore

\[
r_{0,n}r_{1,n}
=O_p(n^{-3/5}+n^{-a-1/5}+n^{-2a+1/5}).
\tag{8.7}
\]

The product in (8.7) alone vanishes for \(a>1/10\), but Workstream A's proved level-only derivative theorem assumes \(n^{-a}/b_n\to0\). Therefore Route S, as presently proved, requires \(a>1/5\) for consistency at \(b_n=n^{-1/5}\); the weaker \(a>1/10\) would require a new product theorem allowing a diverging derivative norm. To retain the full oracle \(n^{-1/2}\) rate, the direct rigid rotation already requires \(n^{-a}=O(n^{-1/2})\), so \(a\ge1/2\) (strict \(>1/2\) for a negligible local-stationarity term); under this stronger condition every term in (8.7) is \(o(n^{-1/2})\). The derivative penalty is therefore compatible with the old practical bandwidth, but it cannot be deleted from the theorem. Route R consumes no derivative restriction: at \(b_n=n^{-1/5}\), its \(\rho_n\) is \(n^{-2/5}+n^{-a}\) up to constants and the smaller bias/design terms, under Workstream A's level-theorem localisation condition \(n^{-a}=O(b_n)\).

For growing lags/memory, oracle order requires
\(H_n^0(m_n+H_n^0)=O(1)\); consistency requires
\(H_n^0(m_n+H_n^0)=o(n)\). More generally, use the explicit quantity in (8.2), not a hidden \(h_0\) constant. The cross-fitting design also requires
\(m_n+H_n^0=o(\ell_n)=o(nb_n)\).

## 9. Factor-number selection

Let \(\widehat\lambda_{1,n}\ge\widehat\lambda_{2,n}\ge\cdots\ge0\) be the eigenvalues of \(\widehat{\mathbb L}_n\). Because conjugation by \(Q_n\) does not change eigenvalues, Lemma B6 applies directly.

> **Theorem B9 (beyond-rank rate — PROVED).** Under either feasible route and exact rank \(r_n\),
> \[
> \widehat\lambda_{r_n+1,n}\le d_n^2,
> \qquad
> |\widehat\lambda_{j,n}-\lambda_{j,n}|
> \le 2A_{2,n}d_n+d_n^2\quad(j\le r_n).
> \tag{9.1}
> \]
> If \(d_n=O_p(n^{-1/2})\), the beyond-rank eigenvalues are \(O_p(n^{-1})\), even though the nonzero eigenvalues are in general estimated only at \(O_p(n^{-1/2})\).

**Proof.** The first statement is the row-operator singular-value bound (7.2). The second is Weyl applied only to the nonzero block, using (7.1). ∎

This square survives feasible mean and frame estimation precisely when their lag-row errors are included in \(d_n\). It is not obtained by applying Weyl to \(\widehat{\mathbb L}-\mathbb L\).

> **Counterexample B10 (raw ratio over-selects — DISPROVED).** Let
> \(\mathbb L=\operatorname{diag}(1,0,0)\) and
> \(\widehat{\mathcal G}=\operatorname{diag}(1,d,0)\), so
> \(\widehat{\mathbb L}=\operatorname{diag}(1,d^2,0)\) and the true rank is one. The unregularised ratios are
> \(\widehat\lambda_2/\widehat\lambda_1=d^2\) and
> \(\widehat\lambda_3/\widehat\lambda_2=0\). Minimising the ratio over \(j=1,2\) returns \(2\) for every \(d>0\). If both beyond-rank eigenvalues are zero, a later ratio is \(0/0\) and the selector is not even defined. Therefore loading consistency and the \(O_p(d_n^2)\) beyond-rank bound do not prove consistency of the raw ratio selector.

> **Theorem B11 (threshold selector — PROVED).** Let \(\eta_n=2A_{2,n}d_n+d_n^2\). Suppose there is a deterministic threshold \(\tau_n>0\) such that
> \[
> \tau_n\to0,\qquad d_n^2=o_p(\tau_n),\qquad \tau_n=o(\Delta_n),
> \qquad \eta_n=o_p(\Delta_n).
> \tag{9.2}
> \]
> Define
> \[
> \widehat r_n^{\mathrm{thr}}=#\{j:\widehat\lambda_{j,n}>\tau_n\}.
> \]
> Then \(\mathbb P(\widehat r_n^{\mathrm{thr}}=r_n)\to1\).

**Proof.** Theorem B9 gives \(\widehat\lambda_{r_n+1,n}\le d_n^2<\tau_n\) with probability tending to one. Also
\(\widehat\lambda_{r_n,n}\ge\Delta_n-\eta_n>\tau_n\). Monotonicity of the ordered eigenvalues finishes the proof. ∎

The threshold rule needs no separation among the nonzero eigenvalues and is the preferred corrected selector.

> **Theorem B12 (ridge-regularised ratio — PROVED).** Fix a deterministic search cap \(R_n\) with \(r_n<R_n\le p_n-1\). Assume (9.2) and, for some \(c_*>0\),
> \[
> \min_{1\le j<r_n}{\lambda_{j+1,n}\over\lambda_{j,n}}\ge c_*.
> \tag{9.3}
> \]
> Define
> \[
> \mathcal R_{j,n}(\tau_n)=
> {\widehat\lambda_{j+1,n}+\tau_n\over
>  \widehat\lambda_{j,n}+\tau_n},
> \qquad
> \widehat r_n^{\mathrm{ridge}}=
> \arg\min_{1\le j\le R_n}\mathcal R_{j,n}(\tau_n),
> \]
> with the smallest-index tie rule. Then
> \(\mathbb P(\widehat r_n^{\mathrm{ridge}}=r_n)\to1\).

**Proof.** At \(j=r_n\), Theorem B9 and (9.2) give

\[
\mathcal R_{r_n,n}(\tau_n)
\le {d_n^2+\tau_n\over \Delta_n-\eta_n+\tau_n}=o_p(1).
\]

For \(j>r_n\), both eigenvalues are bounded by \(d_n^2\), hence

\[
{\tau_n\over\tau_n+d_n^2}
\le\mathcal R_{j,n}(\tau_n)
\le{\tau_n+d_n^2\over\tau_n},
\]

so the ratios converge uniformly to one. For \(j<r_n\), Weyl, \(\eta_n=o_p(\Delta_n)\), and (9.3) give a uniform lower bound \(c_*/2\) with probability tending to one. Therefore the unique asymptotic minimum is at \(r_n\). ∎

No fixed-search-cap or multiplicity assumption is hidden here. The event
\(\widehat\lambda_{r_n+1,n}\le d_n^2\) simultaneously bounds every later ordered eigenvalue, so the two-sided ridge bound is uniform over all \(r_n<j\le R_n\), even when \(R_n\to\infty\) or \(R_n=p_n-1\). The growing positive block is handled uniformly by the minima in (9.3) and by \(\lambda_{j,n}\ge\lambda_{r_n,n}=\Delta_n\).

The ridge condition required by the proof is exactly \(d_n^2=o_p(\tau_n)\), not merely \(\eta_n=o_p(\tau_n)\). The latter would often be unnecessarily strong because \(\eta_n\) is first order while the entire null spectrum is second order.

## 10. Status of every load-bearing node

| Node | Status in this dossier | Exact condition or replacement |
|---|---|---|
| Signal/eigengap identity | PROVED | (LN), \(\operatorname{rank}B_n=r_n\) |
| \(\Delta_n\ge s_n^2\) | PROVED | One full-rank included lag; otherwise may be vacuous |
| Dimension-free oracle lag concentration | PROVED | Bounded total energy and causal finite memory (SM) |
| Generic polynomial mixing version | SUPERSEDED for this theorem | Not consumed; (SM) is the coherent proved short-memory route |
| Cross-fitting independence | PROVED for the stated split | (CF), causal finite memory, one evaluation colour |
| Polygonal feasible-observation RMS | PROVED UNDER UNIFORM TUBE GEOMETRY | Lemma B6″, controlled vertex count, grid RMS, cellwise holonomy |
| Robust derivative-free P1-OP | PROVED | Corollary B6‴ and Route R |
| Quadratic mean recentering from mean zero alone | DISPROVED | Counterexample B4 |
| Quadratic mean recentering after repair | PROVED | Tube Taylor bound plus (GLO) and cross-fitting |
| Idiosyncratic/cross terms | PROVED as zero under explicit moments | (LN); approximate violations enter \(d_{\mathrm{LN},n}\) |
| Rigid frame rotation without gap | PROVED | Exact single orthogonal \(Q_n\) |
| Non-rigid frame residual without gap | REJECTED | It enters \(d_n\) and pays \(\Delta_n^{-1}\) unless an exact conjugation theorem is supplied |
| G1′ local-stationarity rate | Explicit input | \(r_{1,n}\) retains \(n^{-a}/b_n\) |
| Lag-operator assembly | PROVED | Lemma B6, explicit \(H_n^0\) through row norms |
| Loading theorem | PROVED UNDER EXPLICIT ASSUMPTIONS | Theorem B8 |
| Beyond-rank \(O_p(n^{-1})\) | PROVED when \(d_n=O_p(n^{-1/2})\) | Row-operator singular values, not generic Weyl |
| Raw eigenvalue ratio | DISPROVED | Counterexample B10 |
| Threshold factor selector | PROVED | Theorem B11 |
| Ridge ratio selector | PROVED | Theorem B12 and nonzero-spectrum ratio separation |

## 11. Exact inputs needed from Workstream A and the main integration

Route R consumes Workstream A's pointwise second-moment/design-grid RMS argument on the deterministic polygon vertices, plus the uniform tube geometry used in Lemma B6″. It does not consume G1′ or preservation of dependence after feasible transformation. Route S instead needs the following outputs on the perforated training design:

1. \(N_n^{-1}\sum_{t\in I_n}\|e_t\|^2=O_p((r_{0,n}^{\mathrm{CF}})^2)\), with \(r_{0,n}^{\mathrm{CF}}\) as in (5.1);
2. a tube event on which (4.1) has dimension-uniform constant \(J\) and
   \(\max_{t\in I_n}\|e_t\|=o_p(1)\);
3. for the sharper ribbon/frame route, the corrected perforated-design derivative rate \(r_{1,n}^{\mathrm{CF}}\) in (5.1), retaining \(n^{-a}/b_n\) under level-only local stationarity;
4. a proved frame statement at least as strong as (FR), with explicit
   \(\omega_n,\phi_n,d_{\mathrm{disc},n}\). If only the crude vector-level frame bound is available, it must be used and the resulting slower additive rate retained;
5. the periodic-mask moment calculation and its \(\ell_n/n\), \(\ell_n/(nb_n)\) defects; merely noting half-density and \(\ell_n=o(nb_n)\) is insufficient.

The final Paper 1 theorem can therefore be genuinely growing-dimensional and dimension-free under bounded total energy. The robust final route is the polygonal Route R, which accepts a first-order \(O(q_n)\) feasible-observation term and bypasses both GLO and G1′. The sharper Route S requires (GLO), with joint sign symmetry as a checkable sufficient condition on affine-invariant SPD, as well as the perforated-design rates. The old generic quadratic claim cannot be retained.

## 12. Parent-scope comparison

The theorem here permits arbitrary \(p_n\to\infty\) because all stochastic concentration is in Hilbert or Hilbert–Schmidt norm and total energy is uniformly bounded. It does not reproduce a classical pervasive-factor regime in which total energy and signal eigenvalues grow with \(p_n\). It also replaces unverified polynomial-mixing and raw-ratio claims by a proved finite-memory theorem and a proved threshold/ridge selector. This is a nontrivial growing-\(p_n\) theorem, but its short-memory, bounded-total-energy, and lag-orthogonal-noise assumptions must be stated as scope restrictions rather than attributed to the parent RFM. Geometric lag orthogonality is an additional restriction only for sharper Route S; derivative-free Route R bypasses it.
