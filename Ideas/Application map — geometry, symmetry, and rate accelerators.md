---
type: canonical-application-map
title: Application map — geometry, symmetry, and rate accelerators
status: canonical-proof
verdict: FRAME-2P-U is a closed conditional implication but has no verified growing-curvature application; HE and the scoped BW packages are separately closed under explicit assumptions
last-audited: 2026-08-12
---

# Application map — geometry, symmetry, and rate accelerators

> **Authority and scope.** [[HD1 — growing-dimension Paper 1 proof dossier]] remains the proof source for the robust theorem. This file is the canonical source for property-to-application matching. APP-A, APP-B, and APP-C are preserved under `Archived/Proof workstreams` as citable proof provenance, while current status is governed here. Paper 2 is out of scope.

## 0. Current conclusions

1. Under exact included-lag factorisation, the robust arbitrary-ambient-\(p_n\) bounded-energy result is
   \[
   d_n=O_p(n^{-1/2}+\ell_n),\qquad
   \|\sin\Theta(\hat E_n,E_n)\|_{\rm op}
   =O_p\!\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right),
   \quad
   \ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
   \tag{R}
   \]
   With approximate-target defect \(\zeta_n\), replace the row numerator by \(n^{-1/2}+\ell_n+\zeta_n\) and use the ideal-target gap. At \(b_n=n^{-1/7}\), \(a\ge3/7\), the exact-target numerator is \(n^{-3/7}\). **PROVED in HD1.**
2. After one common anchor rotation is removed, the feasible lag product has exactly four first-order nuisance terms: two base-point/Hessian terms and two non-rigid frame terms. Geometry, law symmetry, sample separation, and frame rigidity act on different terms. **PROVED, APP-B Lemma APP-B1.**
3. On a Hilbert space, the Frobenius vector space of symmetric matrices, or one fixed common-eigenbasis AIRM-SPD flat, exact training/evaluation separation conditionally centres the two additive terms and flatness removes the two frame terms. Then
   \[
   d_n=O_p(n^{-1/2}+\ell_n^2+\rho_n).
   \tag{O-row}
   \]
   If \(\ell_n^2+\rho_n=o(n^{-1/2})\), the loading numerator is \(n^{-1/2}\). **PROVED UNDER THE EXPLICIT SPLIT.**
4. A known centre removes the nuisance terms. A constant pooled or finite-dimensional parametric centre estimated at root-\(n\) generally leaves them linear but of root-\(n\) size. This is oracle order, not first-order immunity or automatic oracle equivalence. **PROVED.**
5. Full AIRM SPD is Hadamard and locally symmetric, not flat. On absolute spectral bands, all fixed-order Exp, Log, parallel-transport, Hessian, Richardson, connector, and ruled-surface differentials consumed by HD-G are uniform in matrix size in the project AIRM/Frobenius norms. This verifies geometry, not energy, GLO, frame cancellation, lag orthogonality, or signal. **PROVED, T-APP-2.**
6. Fixed finite memory may be replaced in the robust theorem by dimension-uniform causal Hilbert physical dependence with summable \(L^2\) and essential-sup innovation effects. Infinite-memory physical dependence does not create exact cross-fit independence. **PROVED / shortcut DISPROVED.**
7. Signed growing-\(p_n\) G1 is proved when the random Hessian is deterministic, scalar plus a uniformly Hilbert–Schmidt-bounded remainder, or controlled block-scalar. This includes flat/common-commuting flats and bounded constant-negative-curvature models. It is not verified for unrestricted full AIRM SPD, and faster signed mean convergence alone is not loading immunity. **PROVED UNDER EXPLICIT ASSUMPTIONS / OPEN AS QUALIFIED.**
8. The HE theorem is **PROVED UNDER EXPLICIT ASSUMPTIONS** for both bounded-tail and expanding-domain truncation packages. It exposes centre, frame, score, product, target, \(A_{2,n}\), and \(\Delta_n\) separately; proves sufficient flat and curved energy windows; supplies explicit pervasive and growing-rank DGPs; and gives a sub-Weibull truncation corollary with explicit score/product tail integrals.
9. The fixed-size full-rank local/regularized BW theorem, the noncommuting fixed-margin geometry producer, and a restricted fractional-normal shrinking-margin theorem are **PROVED UNDER EXPLICIT ASSUMPTIONS**. The shrinking theorem has sufficient—not globally sharp—windows and requires support/energy \(O(\sqrt{\alpha_n})\). Global/rank-changing PSD and unsafeguarded-estimator claims are **DISPROVED/RETRACTED**. The fixed-basis diagonal HE–BW branch is proved.
10. FRAME-2P-U is an entirely observable **conditional U2P implication**. Three exactly separated training/validation/evaluation colours, an independently undersmoothed validation path, and the exact derivative of the fitted evaluation polygon row jointly remove the first-order mean/base-log and non-rigid frame terms. With \(b_n=n^{-1/7}\), \(M_n\asymp n^{2/7}\), \(c_n=n^{-\gamma}\), \(1/6<\gamma<3/14\), its post-influence nuisance remainder is \(o_p(n^{-1/2})\) and its row is root-\(n\), uniformly only when every U2P primitive is uniform in \(p_n\). The current growing-\(p_n\) witness pads one fixed curved active block with flat inactive coordinates; no genuinely growing-curvature, growing-AIRM, or growing-BW application has been verified. **CONDITIONAL THEOREM PROVED; GROWING-CURVATURE APPLICATION OPEN.**

## 1. Term-by-term error ledger

After true-frame identification and removal of one common rigid rotation,

\[
U_t=Y_t-H_te_t+\Omega_tY_t+\xi_t^{(2)},\qquad
\|\xi_t^{(2)}\|\lesssim \|e_t\|^2+\|e_t\|\|\Omega_t\|+R\|\Omega_t\|^2.
\tag{1.1}
\]

Here \(e_t=\log_{\mu_t}\hat\mu_t\), \(H_t=\tfrac12\operatorname{Hess}_{\mu_t}d(\mu_t,X_t)^2\), and \(\Omega_t^*=-\Omega_t\) is the non-rigid relative-frame derivative.

| ID | Exact term or scale | Type | Baseline order | Direct consumer | What can improve it |
|---|---|---|---|---|---|
| M-B | \(b_n^3\) after three-scale cancellation | deterministic mean bias | \(b_n^3\) | \(e_t\), PF | higher positive correction or signed order \(q\) |
| M-S | \((nb_n)^{-1/2}\) RMS; \(\sqrt{\log n/(nb_n)}\) sup | empirical score | displayed | \(e_t\), tube | dependence/design constants |
| M-LS | \(n^{-a}\) | local-stationarity approximation | displayed | \(e_t\) | stronger approximation model |
| M-G | \(n^{-1}\) | grid/design | displayed | \(e_t\) | exact design |
| M-D | \(b_n^3+(nb_n^3)^{-1/2}+n^{-a}/b_n+(nb_n)^{-1}\) | derivative error | optional | smooth-frame routes | \(C^1\) coupling; PF bypasses it in robust HD1 |
| LOG-1 | \(-H_te_t\) | linear base-point recentering | \(O_p(\ell_n)\) pathwise | lag products | GLO plus exact split centres it; parametric centre shrinks it |
| LOG-2 | quadratic Log remainder | Taylor remainder | \(O_p(\ell_n^2)\) | lag products | zero in a vector space; already oracle-negligible |
| CON | endpoint connectors | typed geometric error | HD-G controlled | observation/frame map | identity in one affine flat |
| FR-R | one common orthogonal \(Q_n\) | rigid frame | exact conjugation | intrinsic target | absorbed by aligned comparison; no eigengap |
| FR-N | \(\Omega_tY_t\) | non-rigid frame | \(O_p(\ell_n)\) robustly | lag products | zero in one flat; direct coefficient bound; or FRAME-2P-U full-functional correction |
| HOL | ribbon/polygon holonomy | curvature interaction | PF gives \(O_p(\ell_n)\) | FR-N | zero if \(R\) vanishes on normalized ribbon planes; \(\nabla R=0\) is insufficient |
| L-M1 | \(-H_te_t\otimes Y_{t-h}\) | linear mean lag term | \(O_p(\ell_n)\) pathwise | \(d_n\) | conditional GLO + exact split; or FRAME-2P-U inverse-Karcher/base-log action |
| L-M2 | \(-Y_t\otimes H_{t-h}e_{t-h}\) | linear mean lag term | same | \(d_n\) | reverse-endpoint GLO; or the lagged FRAME-2P-U derivative action |
| L-F1 | \(\Omega_tY_t\otimes Y_{t-h}\) | linear frame lag term | \(O_p(\ell_n)\) | \(d_n\) | frame rigidity/flatness/direct defect; or FRAME-2P-U Jacobi/connector action |
| L-F2 | \(Y_t\otimes\Omega_{t-h}Y_{t-h}\) | linear frame lag term | same | \(d_n\) | same at the lagged endpoint |
| L-Q | terms quadratic in \(e,\Omega\) | feasible remainder | \(O_p(r_e^2+r_er_F+r_F^2)\) | \(d_n\) | harmless if nuisance rates are \(o(n^{-1/4})\) |
| O-S | oracle lag-row fluctuation | HS sampling | \(n^{-1/2}\) | \(d_n\) | fixed memory or C-PD; oracle floor |
| LN | \(D_h=\Gamma_h-AC_f(h)A^*\) | population target bias | \(\zeta_n=(\sum_h\|D_h\|_{op}^2)^{1/2}\) | target/gap | exact included-lag orthogonality |
| DEP | dependence/coupling tail | sampling/approximation | \(\rho_{D,n}\) | score, O-S, split | summable physical coefficients; finite memory for exact split |
| MASK | deleted/perforated design | estimator/target artifact | block scale divided by \(n\), as typed | mean/lag row | explicit tuning |
| ASM | \(\eta_n=2A_{2,n}d_n+d_n^2\) | operator assembly | linear in \(d_n\) for signal | Davis–Kahan | only improved \(d_n\) or signal |
| DK | \(\|\sin\Theta\|\lesssim\eta_n/\Delta_n\) | eigengap denominator | \(\Delta_n^{-1}\) | loading | proved stronger gap; never numerator cancellation |
| EV | \(\hat\lambda_{r+1}\le d_n^2\) | beyond-rank square | \(d_n^2\) | factor selection | improved row rate |

Thus a property is a loading accelerator only if it improves L-M1/L-M2 and L-F1/L-F2, or makes \(r_e+r_F=O_p(n^{-1/2})\). Improving M-B alone is only a mean accelerator.

## 2. Assumption-to-cancellation matrix

Levels are **G** geometry, **L** law/symmetry, **M** model alignment, **D** dependence, and **E** estimator design.

| Property package | Exact checkable criterion | Proof identity | Term killed or improved | Mode | Estimator change | New rate | Dimension | Examples | Nonexamples | Status | Proof |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Known centre/frame (M) | \(\mu\) and true frame supplied | \(e=\Omega=0\) | LOG, CON, FR, L-M/L-F | pathwise | none | \(d_n=n^{-1/2}+\rho_n\) | energy-uniform | designed reference paths | estimated centre | **PROVED** | APP-B §5 |
| Constant pooled centre (M/E) | \(\mu(u)=\mu_0\); pooled root-\(n\) estimator | \(r_F=0,r_e=n^{-1/2}\) | order, not coefficient | pathwise bound | pooled mean | oracle order | uniform Hessian | stationary manifold factor | local moving mean | **PROVED; not immunity** | APP-B §5 |
| Parametric centre (M/E) | \(\mu(u;\theta)\), root-\(n\) \(\hat\theta\), uniform derivative | \(r_e+r_F=n^{-1/2}\) | order only | pathwise bound | parametric fit | oracle order | fixed/stated parameter growth | scientific trajectory model | misspecified sieve | **PROVED; not immunity** | APP-B §5 |
| Hilbert/flat + exact split (G/D/E) | one affine convex flat; disjoint innovation sets | \(H=I,\Omega=0,E(Y\mid\mathcal T)=0\) | L-M centred; L-F zero | conditional | leave-block-out | \(n^{-1/2}+\ell_n^2+\rho_n\) | total-energy uniform | functions, Sym-Frobenius | arbitrary same-sample error | **PROVED UNDER EXPLICIT ASSUMPTIONS** | T-APP-1/3 |
| Common commuting AIRM flat (G/M/D/E) | one fixed eigenbasis contains model and all estimator images | log-eigenvalue Euclidean reduction | geometric terms zero; L-M centred by split | pathwise + conditional | constrain to flat | same oracle branch | arbitrary size with log-energy | diagonal/fixed-axis SPD | changing basis | **PROVED** | APP-A §2; APP-B §4 |
| Full AIRM local symmetry (G) | fixed generated bands; project norms | \(\nabla R=0\), matrix calculus | differential constants only | bound | none | robust rate unchanged | uniform matrix size | full SPD | flatness claim | **PROVED; no cancellation** | T-APP-2 |
| Simultaneous reflection (L) | retained-lag law invariant under joint sign reversal | \(H(Y)=H(-Y)\), integrand odd | population L-M coefficient | expectation | split still needed | \(\ell/\sqrt n+\ell^2\) mean channel | envelope-uniform | centrally symmetric lag law | marginal sign symmetry | **PROVED** | APP-A §3.4; APP-B §3 |
| Isotropy (L) | merely \(EH=cI\) or marginal rotation invariance | no lag GLO identity | none | — | — | none | — | isotropic marginals | conditional radii | **DISPROVED as sufficient** | APP-B CE-B4; APP-C C-S2 |
| Deterministic/scalar Hessian (L/G) | \(H_t=H_0\) pathwise, especially \(I\) | mean zero passes through \(H_0\) | GLO coefficient; signed Hessian fluctuation | expectation/conditional | split for lag; signed LP | signed growing-\(p\); oracle only with frame | dimension-free | flat/common flat | scalar expected Hessian | **PROVED / shortcut DISPROVED** | APP-C C-SG1; APP-B §3 |
| GLO + exact split + frame rigidity (L/D/G/E) | both GLO identities; disjoint innovations; \(\phi_F=o(n^{-1/2})\) | all four linear coefficients centred/negligible | L-M/L-F | conditional + direct | split/frame correction | equation (3.1) | envelope-uniform | abstract curved package | GLO alone | **PROVED UNDER ASSUMPTIONS** | T-APP-3 |
| FRAME-2P-U (G/L/M/D/E) | U2P uniform tube/action/replacement producers; exact three colours; GLO/LN; exact law or \(a>1/2\); \(1/6<\gamma<3/14\) | full fitted-row derivative toward independent undersmoothed path | all four L-M/L-F pilot terms | pathwise cancellation + Hilbert Hájek projection | cyclic two-path polygon correction | root-\(n\) row; \(o_p(n^{-1/2})\) nuisance remainder | arbitrary \(p_n\) only when U2P is uniform | fixed-dimensional curved models; fixed curved active block with flat padding | bounded energy alone; same-band score; growing-curvature inference from padding | **CONDITIONAL IMPLICATION PROVED; APPLICATION VERIFICATION OPEN** | [[FRAME-2P-U — conditional two-path debiasing theorem]] |
| Higher-order smoothing (E) | certified order \(q\) | \(b^3\to b^q\) | M-B only | bias | higher correction/signed LP | \(n^{-q/(2q+1)}\) mean | proof-dependent | structural signed classes | oracle claim from smoother | **rate distinction PROVED** | APP-B §8 |
| Signed structural G1 (G/L/E/D) | localized LP; \(H=aI+K\), HS-bounded/PD \(K\), or blocks | scalar + HS concentration | signed empirical Hessian | empirical | localized signed LP | \(\ell_{q,n}\) | arbitrary \(p_n\) under budget | flat, common flat, constant negative curvature | unrestricted full AIRM | **PROVED UNDER ASSUMPTIONS** | T-APP-5 |
| Hilbert physical dependence (D) | uniform summable \(L^2\) and essential-sup effects for scores/rows | martingale projection and bounded differences | dependence assumption for M-S/O-S | empirical | none for Route R | same robust rate | Hilbert dimension-free | causal functional/matrix processes | generic polynomial mixing | **PROVED** | T-APP-4 |
| Bounded total energy (M/E) | \(\sup\|Y_t\|\le R\), or typed product-moment substitute | Hilbert/HS envelopes | constants/scope, no coefficient | pathwise/moment | normalization only if estimand retained | no cancellation | arbitrary \(p_n\) | fixed intrinsic rank | coordinatewise variance | **PROVED; shortcut DISPROVED** | APP-C §2 |
| Exact lag orthogonality (M) | \(D_h=0\) for every included lag | \(\Gamma_h=AC_f(h)A^*\) | LN target bias | population | model/target restriction | exact target/gap | dimension-free | innovation noise at positive lags | coloured noise | **PROVED** | HD1-B; APP-C §5 |
| Strong eigengap (M) | actual \(\Delta_n\), or proved \(\Delta_n\ge s_n^2\) | Davis–Kahan/SIG2 | denominator/tuning only | deterministic | none | divide by \(\Delta_n\) | algebraic | stable lag signal | one large leading singular value | **PROVED distinction** | HD1 §§3–4 |

## 3. Accelerator theorems

### T-APP-1 — exact flat/commutative reduction

If the centre, observations, tangent loading/noise support, all positive barycentres, Richardson images, blends, chords, connectors, and ribbons lie in one simply connected convex flat, the model reduces by an affine isometry to a Hilbert locally stationary factor model. Then \(H=I\), higher base-change terms, connectors, holonomy, and non-rigid frame error vanish. The additive linear recentering terms remain. This applies to Hilbert spaces, \({\rm Sym}(m)\) with Frobenius metric, and AIRM SPD in one fixed common eigenbasis. **PROVED.**

Flat topology is insufficient: a flat torus can have cut-locus/nonunique-mean problems and a flat Klein bottle can have nontrivial linear holonomy. Time-local commutation is not one common flat.

### T-APP-2 — AIRM growing-size differential verification

Fix \(0<c<C<\infty\), a differential order \(k_0\le4\), and expanded absolute bands containing all generated estimator images. The covariant differentials through order \(k_0\) of AIRM Exp, Log, parallel transport/connectors, the observation Hessian/base-point Log map, fixed Richardson/blend maps, and ruled-surface/Jacobi maps are bounded independently of matrix size. **PROVED.**

The proof uses dimension-free multilinear Frobenius product bounds; integral/divided-difference formulas for exp/log; Sylvester/resolvent bounds for square roots; the explicit AIRM connection; and
\[
R(U,V)W=-\tfrac14\bigl[\, [U,V],W\,\bigr],\qquad \nabla R=0.
\]
It uses operator-norm bounds on whitened logs, not their possibly \(O(\sqrt m)\) Frobenius length. HD-G is therefore verified for fixed-band AIRM. Total energy, mean length, dependence, LN, and signal remain separate.

### T-APP-3 — first-order cancellation and oracle loading

Assume canonical signal/target conditions and oracle row concentration. Assume exact training/evaluation innovation separation; both lag-specific GLO identities; a direct non-rigid frame coefficient \(\phi_{F,n}\); GLO defect \(\varepsilon_{G,n}\); and typed mask/coupling/target remainders \(\rho_n\). Then
\[
d_n=O_p\!\left(n^{-1/2}+\ell_n^2+\varepsilon_{G,n}\ell_n+\phi_{F,n}+\rho_n\right).
\tag{3.1}
\]
If all non-oracle terms are \(o(n^{-1/2})\) and \(\eta_n=o(\Delta_n)\),
\[
\boxed{\|\sin\Theta(\hat E_n,E_n)\|_{op}
=O_p\!\left(\frac{n^{-1/2}}{\Delta_n}\right)},\qquad
\hat\lambda_{r+1}=O_p(n^{-1}).
\tag{3.2}
\]
**PROVED UNDER EXPLICIT ASSUMPTIONS.** The concrete exact branch is flat/common-commuting geometry plus exact splitting, where \(\varepsilon_G=\phi_F=0\). For an uncorrected generic curved row, the direct-defect version remains **CONDITIONAL** until it proves \(\phi_F=o(n^{-1/2})\); GLO does not imply this. T-APP-3B below is the separate proved observable correction route and does not assume the uncorrected coefficient is negligible.

At \(b_n=n^{-1/7}\), \(a\ge3/7\), the squares \(b_n^6,(nb_n)^{-1},n^{-2a},n^{-2}\) are \(O(n^{-6/7})\), and cross-terms are bounded by sums of squares. Thus \(\ell_n^2=o(n^{-1/2})\), while \(\ell_n/\sqrt n=O(n^{-13/14})\). Split-mask terms must separately be \(o(n^{-1/2})\), e.g. block length \(B_n\) must satisfy \(B_n/n=o(n^{-1/2})\).

### T-APP-3B — FRAME-2P-U observable conditional correction

Let \(\widehat q^T\) be the positive three-scale training polygon at \(b_n=n^{-1/7}\), \(\check q^V\) an independent validation polygon at \(c_n=n^{-\gamma}\), and \(\widehat{\mathfrak T}_E(q)\) the complete masked evaluation-row functional. With \(M_n\asymp n^{2/7}\), define

\[
d_j^{TV}=\log_{\widehat q_j^T}\check q_j^V,
\qquad
\widehat{\mathfrak T}^{2p}_{T,V,E}
=\widehat{\mathfrak T}_E(\widehat q^T)
+D\widehat{\mathfrak T}_E(\widehat q^T)[d^{TV}],
\tag{3B.1}
\]

and average over the three cyclic fold roles. The derivative in (3B.1) includes the inverse-Karcher base-log action and the fitted polygon's transport, Jacobi, connector, and curvature actions. Common rigid gauge changes jointly conjugate both terms; they are not additive error.

Assume the full U2P package uniformly in \(p_n\): fixed lag/memory; bounded total energy; unique strongly convex Karcher means; a \(C^4\) law/mean; one known generated tube with the consumed score, barycentre-replacement, Richardson, Exp/Log, PT/Jacobi, and first two masked-row polygon derivatives bounded; vertex actions \(\max_j\|K_{n,j}\|\le C/M_n\), \(\sum_j\|K_{n,j}\|\le C\); aggregate single/double replacements \(C/n\), \(C/(n^2c_n)\); exact three-colour innovation separation and identical phase-balanced masks; GLO and included-lag factorisation; and exact local law or \(a>1/2\) with all mask/design/coupling defects \(o(n^{-1/2})\). If

This is the high-level invocation. [[FRAME-2P-U — conditional two-path debiasing theorem]] separately classifies the vertex and aggregate replacement rates as conditionally derived from lower-level curvature, strong-convexity, local-support, and composed-row primitives. An application must verify either the low-level producer chain or the high-level rates directly; it must not count the same rate as both an assumption and an independent conclusion.

\[
\frac16<\gamma<\frac3{14},
\]

then

\[
\widehat{\mathfrak T}^{2p}_n-\mathfrak T_n
=\mathbb G_{E,n}[Z_n]+\mathbb G_{V,n}[\varphi_{n,c}]+R_n,
\quad
\|R_n\|_{\oplus HS}=o_p(n^{-1/2}),
\tag{3B.2}
\]

and both influence rows are \(O_p(n^{-1/2})\). Hence \(d_n^{db}=O_p(n^{-1/2})\); if \(2A_{2,n}d_n^{db}+(d_n^{db})^2=o_p(\Delta_n)\), loading error is \(O_p(n^{-1/2}/\Delta_n)\) and \(\widehat\lambda_{r+1,n}^{db}=O_p(n^{-1})\). The validation influence is leading sampling noise, so the result matches oracle **rate order**, not the oracle limit law or efficiency. **CONDITIONAL IMPLICATION PROVED.**

The same-band score/Richardson construction is **DISPROVED** because it generically retains \(b_n^3K[B_3]\asymp n^{-3/7}\). Direct frame/\(\Omega\) plug-in is only conditionally valid. Invariant-only redesign is rejected because it changes the estimand. The padded \(\mathbb H^2(-1)\times\mathbb R^{p_n-2}\) witness proves only logical nonemptiness at every ambient \(p_n\): all active curvature stays in one fixed two-dimensional block. It does not verify growing active curvature or growing-size AIRM/BW.

### T-APP-4 — broader dependence

For a causal Hilbert Bernoulli shift with \(L^2\) innovation effects \(\delta_2(k)\), martingale projection gives
\[
\left\|\sum_t a_t(Z_t-EZ_t)\right\|_2
\le \left(\sum_{k\ge0}\delta_2(k)\right)\|a\|_2.
\tag{3.3}
\]
Summable essential-sup effects and bounded differences give a dimension-free sub-Gaussian norm tail. For \(Y_t\otimes Y_{t-h}\), product coefficients are bounded by \(R\) times shifted coefficients of \(Y\), so the oracle HS lag row stays root-\(n\). G1, GRID, PF, robust Route R, loading, and factor selection therefore remain valid under the stated C-PD budgets. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

This is unconditional. Under infinite memory, a finite cross-fit gap shares remote innovations; the oracle cancellation branch needs a joint retained-row coupling or conditional C-PD theorem plus estimator stability. That branch is **OPEN/CONDITIONAL**. Unqualified polynomial mixing is **DISPROVED**.

### T-APP-5 — signed growing-dimension G1

For a localized signed local-polynomial criterion, suppose on a shrinking preliminary-estimator ball
\[
H(q,X)=a(q,X)I+K(q,X),\qquad \sup\|K(q,X)\|_{HS}<\infty,
\tag{3.4}
\]
with uniform physical-dependence/Lipschitz budgets, or a controlled block-scalar decomposition. Scalar plus HS concentration controls the empirical Hessian without an \(S^{p_n-1}\) net. The RMS rate is
\[
\ell_{q,n}=b_n^q+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
\tag{3.5}
\]
Flat/common-flat Hessians have \(K=0\). In constant negative curvature the Hessian is scalar plus a rank-one HS term, including its continuous \(r=0\) value. Controlled \(K_n\) blocks pay \(\sqrt{\log K_n/(nb_n)}\). **PROVED UNDER EXPLICIT ASSUMPTIONS.** Full AIRM lacks a verified uniform scalar-plus-HS or fixed-block decomposition, so its signed growing-\(p_n\) branch is **OPEN**.

Balancing yields \(n^{-q/(2q+1)}\), slower than \(n^{-1/2}\) for finite \(q\). Faster mean convergence is not immunity. Under a separate T-APP-3 package, \(\ell_{q,n}^2=o(n^{-1/2})\) is enough.

### T-APP-6 — growing-energy/pervasive-factor theorem

Under the bounded-tail/generated-domain assumptions, define the full feasible error

\[
q_{R,n}\lesssim
L_{\log,n}\{r_{\mu,n}+K_{\mu,n}M_n^{-2}\}
+r_{F,n}\{\mathcal E_{2,n}+L_{\log,n}r_{\mu,n}\}
+\rho_{{\rm con},n}+\rho_{{\rm obs},n}.
\]

With variance-sensitive product rate \(\omega_n\),

\[
d_n\lesssim\omega_n+\sqrt{h_{0,n}}
\{2\mathcal E_{2,n}q_{R,n}+q_{R,n}^2\}
+\zeta_n+\rho_{{\rm mask},n}+\rho_{{\rm disc},n}.
\tag{3.6}
\]

The loading condition is \(\eta_n=2A_{2,n}d_n+d_n^2=o_p(\Delta_n)\). For \(R_n=n^\rho\), simplified sufficient fixed-gap windows are \(\rho<3/13\) in a flat/rigid frame and \(\rho<3/20\) for the generic curved frame, with their displayed local-stationarity competitors. A concrete pervasive DGP has \(A_{2,n}\asymp p_n\) and \(\Delta_n\asymp p_n^2\). **PROVED UNDER EXPLICIT ASSUMPTIONS.**

For unbounded observations, deterministic expanding-domain clipping adds \(b_{S,n}(T_n)\) to the mean rate and \(\sqrt{h_{0,n}}b_{W,n}(T_n)\) to the lag row, and requires

\[
N_{X,n}\pi_{X,n}(T_n)+N_{Y,n}\pi_{Y,n}(T_n)\to0.
\]

The original and clipped empirical constructions coincide on this event; concentration is proved for the clipped array without conditioning. Sub-Weibull tails admit \(T_n=K_n\{c\log N_n\}^{1/\alpha}\), \(c>1\), subject to the expanding-domain geometry and final gap condition. **PROVED UNDER EXPLICIT ASSUMPTIONS; NOT MINIMAL.**

### T-APP-7 — moving-centre Bures–Wasserstein theorem

For fixed matrix size, full-rank SPD BW has a **PROVED UNDER EXPLICIT ASSUMPTIONS** local/regularized theorem using constrained stage means, complete generated-domain safeguards, quotient Levi–Civita polygonal transport, and exact lag identification. Its robust rate is \(O_p\{(n^{-1/2}+\ell_n)/\Delta_n\}\).

The fixed-margin noncommuting geometry is also **PROVED UNDER EXPLICIT COMPATIBLE GENERATED-DOMAIN ASSUMPTIONS**: one recurrence-defined \(C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)\), independent of matrix size, reaches the G1 and PF geometric consumers. Generic polygon derivatives retain explicit \(N+\mathsf L\) dependence; the canonical PF error retains \(v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}\). This is a geometry producer, not a shrinking-margin, energy, dependence, signal, or eigengap theorem.

The restricted fractional-normal shrinking-margin chain is **PROVED UNDER EXPLICIT ASSUMPTIONS**. It requires strict score-pair/generated slack, support and energy \(O(\sqrt{\alpha_n})\), fractional-normal PF cells, and the exact row/assembly/gap conditions. Its active coefficients include \(K_B=O(1+\alpha_n^{-1})\), \(K_{L2}=O(\alpha_n^{-1/2})\), \(K_F=O(\alpha_n^{-1})\), and \(\rho_H=O(\sqrt{\alpha_n})\). For \(\alpha_n\asymp m_n^{-A}\) with matched local rank-one signal, \(m_n=n^x\), the sufficient window is \(0<x<3/(5A)\). This is not a maximum growth law; a self-similar fixed active block admits arbitrary polynomial inactive dimension. Fixed/growing energy is outside this shrinking normal-pair class.

The global/rank-changing PSD theorem is **DISPROVED**, and the original unsafeguarded global estimator is **RETRACTED**. Unrestricted nonlocal sharp exponent minimisation remains **OPEN but unconsumed**. The diagonal fixed-basis positive-root branch has a proved HE corollary; it does not cover rotating eigenspaces.

## 4. Stability and reality bridge

| Approximate property | Defect | Proven penalty | Effect | Oracle requirement at \(b=n^{-1/7}\) | Feasibility |
|---|---|---|---|---|---|
| GLO/reflection | \(\varepsilon_{G,n}=\max_h\sup_{\|v\|=1}\|E(H_tv\otimes Y_{t-h})\|\vee\cdots\) | \(\varepsilon_{G,n}\ell_n\) | population linear coefficient | \(\varepsilon_{G,n}=o(n^{-1/14})\) | stable only if model supplies this operator defect |
| fixed algebra | \(Y=D+N\), aligned \(D,e\), \(\|N\|_F\le\varepsilon_{A,n}\) | \(O(\varepsilon_{A,n}\ell_n)\) Hessian action | recentering | same \(o(n^{-1/14})\) | **STABLE APPROXIMATE** if basis is meaningful |
| relevant-plane flatness | normalized \(\varepsilon_{R,n}=\sup\|R(S_s,S_\tau)\|/\|S_s\wedge S_\tau\|\) | \(\varepsilon_{R,n}\operatorname{Area}\) | frame | direct frame term \(o(n^{-1/2})\) | raw commutators remain diagnostic |
| frame rigidity | direct-sum HS \(\phi_{F,n}\) | additive \(\phi_{F,n}\) | signal-carrying frame bias | \(o(n^{-1/2})\) | exact in one flat; fragile in full AIRM |
| FRAME-2P-U producer defects | failure of uniform vertex actions, replacement bounds, common masks, exact separation, or local-law accuracy | retain each failed producer as an explicit row/tube/mask/coupling remainder | mean and frame correction | full remainder \(o(n^{-1/2})\) | application-verifiable; not implied by energy |
| lag noise/cross terms | \(\zeta_n=(\sum_h\|D_h\|_{op}^2)^{1/2}\) | \(2A_{2,n}\zeta_n+\zeta_n^2\) | population target bias | exact expression \(o(n^{-1/2})\) and \(o(\Delta_n)\) | restrictive but model-checkable |
| infinite-memory split | \(\vartheta_\infty(g_n)\) plus estimator coupling | coefficient plus conditional sampling remainder | dependence leakage | entire proved remainder \(o(n^{-1/2})\) | **CONDITIONAL** |
| PD budgets | \(\Theta_2,\Theta_\infty\) | multiply score/lag stochastic terms | sampling | bounded or displayed growth | plausible causal short memory |
| growing energy | \(R_n\) | score \(R_n(nb)^{-1/2}\), lag \(R_n^2n^{-1/2}\), feasible \(2R_nq_n+q_n^2\) | sampling/tube | insert everywhere | normalization may distort model |
| band escape | \(\pi_n\) | event \(n\pi_n\); clipping RMS \(R\sqrt{\pi_n}\), bias \(R^2\pi_n\) | failure/estimand | \(n\pi_n\to0\), or clipped penalties negligible | observable, but clipping changes target |
| infinite-lag target | \(\rho_H=\sum_{h>h_0}\|\Gamma(h)\|_{op}^2\) | \(\|\mathbb L_\infty-\mathbb L_{h_0}\|\le\rho_H\) | truncation bias | \(o(\Delta_\infty)\) and oracle scale if claimed | model/diagnostic bridge |
| signal dilution | actual \(\Delta_n\downarrow0\) | numerator divided by \(\Delta_n\) | denominator | \(\eta_n=o(\Delta_n)\) | recompute after normalization |

An empirical commutator is diagnostic until linked to both the fixed-algebra and normalized ribbon defects. Marginal symmetry is diagnostic until linked to lag-specific GLO. A fitted small lag-noise covariance does not establish its population scale without inference.

## 5. Rate ledger

| Branch | Mean RMS | Frame | Lag row \(d_n\) | Loading | Null eigenvalue | Factor-number window | Status |
|---|---|---|---|---|---|---|---|
| Robust positive HD1 | \(\ell_n\) | \(O_p(\ell_n)\) PF | \(n^{-1/2}+\ell_n\) | \((n^{-1/2}+\ell_n)/\Delta_n\) | \(O_p(d_n^2)\) | \(d_n^2=o_p(\tau_n)\ll\Delta_n\) | **PROVED** |
| Robust under C-PD | same | same | same with PD constants | same | same | same | **PROVED** |
| Flat/common flat + split | \(\ell_n\) | zero after anchor | \(n^{-1/2}+\ell_n^2+\rho_n\) | \(n^{-1/2}/\Delta_n\) if defects negligible | \(O_p(n^{-1})\) | \(n^{-1}=o(\tau_n)\ll\Delta_n\) | **PROVED UNDER SPLIT** |
| Abstract curved GLO | \(\ell_n\) | direct \(\phi_F\) | equation (3.1) | oracle only if frame/defects negligible | row square | corresponding window | **CONDITIONAL for generic application** |
| FRAME-2P-U conditional U2P | training \(n^{-3/7}\); validation \(c^3+(nc)^{-1/2}\) | corrected inside the full row derivative | \(n^{-1/2}\) | \(n^{-1/2}/\Delta_n\) under assembly/gap | \(O_p(n^{-1})\) | \(n^{-1}=o(\tau_n)\ll\Delta_n\) | **IMPLICATION PROVED; GROWING-\(p\) WITNESS IS FLAT-PADDED** |
| Known centre | zero | zero | \(n^{-1/2}+\rho_n\) | oracle | \(n^{-1}\) | oracle window | **PROVED** |
| Constant/parametric centre | \(n^{-1/2}\) | \(n^{-1/2}\) or rigid | \(n^{-1/2}\) | oracle order; changed limit possible | \(n^{-1}\) | oracle window | **PROVED; not immunity** |
| Signed structural mean | \(\ell_{q,n}\) | first order unless flat | \(n^{-1/2}+\ell_{q,n}\) robustly | \((n^{-1/2}+\ell_{q,n})/\Delta_n\) | row square | row-based | **PROVED mean; robust loading chain** |
| Growing energy/pervasive signal | typed centre RMS \(r_{\mu,n}\), frame \(r_{F,n}\), and full \(q_{R,n}\) | empirical-energy scaled | \(\omega_n+\sqrt{h_{0,n}}(2E_{2,n}q_{R,n}+q_{R,n}^2)+\zeta_n+\) typed defects | \((2A_{2,n}d_n+d_n^2)/\Delta_n\) | \(O_p(d_n^2)\) | \(d_n^2\ll\tau_n\ll\Delta_n\), \(\eta_n=o(\Delta_n)\) | **PROVED UNDER EXPLICIT BOUNDED-TAIL ASSUMPTIONS** |

Signal remains separate. Under exact factorization,
\[
\Delta_n=\lambda_{\min}\!\left(\sum_h C_f(h)C_f(h)^*\right).
\]
One full-rank included lag implies \(\Delta_n\ge s_n^2\). Complementary rank-deficient lags can yield \(\Delta_n>0\) while \(s_n=0\).

## 6. Analytic counterexamples

| False shortcut | Attack | Correct statement | Status / proof |
|---|---|---|---|
| \(\nabla R=0\) kills recentering/holonomy | noncommuting AIRM and hyperbolic B4 | local symmetry controls derivatives/parity, not \(R\) or GLO | **DISPROVED**, APP-A §3; HD1-B B4 |
| \(R=0\) gives oracle loading | flat scalar \(e_t=\varepsilon Y_{t-1}\) leaves linear lag bias | add separation/centring/debiasing | **DISPROVED**, APP-A (2.7) |
| marginal sign symmetry gives lag GLO | four-state mixing cycle has symmetric marginals and nonzero GLO coefficient | simultaneous lag/conditional symmetry | **DISPROVED**, APP-C C-L1 |
| isotropic \(EH\) makes empirical Hessian scalar | constant-curvature draw has radial/tangential eigenvalues | scalar-plus-HS structure suffices | **DISPROVED / corrected**, APP-C C-S2 |
| split + zero covariance gives independence | \(W\) and \(W^2-EW^2\) | disjoint innovations or joint coupling | **DISPROVED**, APP-B CE-B8 |
| timewise commuting SPD gives one flat | common basis \(U_t\) changes with time | one fixed basis must contain all objects | **DISPROVED**, APP-B CE-B7 |
| spectral band gives total energy | \(d_{\rm AIRM}(I,eI)=\sqrt m\) | band gives differentials, not energy/path length | **DISPROVED**, APP-A §5.5 |
| coordinate moments give total energy | independent Rademacher coordinates have norm \(\sqrt p\) | total norm/trace/product budget | **DISPROVED**, APP-C C-E2 |
| higher smoother gives root-\(n\) loading | \(n^{-q/(2q+1)}\) and linear L-M | add immunity or root-\(n\) centre | **DISPROVED**, APP-B §8 |
| strong leading lag direction gives gap | \(C_h=\operatorname{diag}(1,\varepsilon)\) | use actual \(\Delta_n\) or minimum singular value | **DISPROVED as stated**, HD1-B |
| root-\(n\) centre is negligible | hyperbolic B4 with \(e_n=n^{-1/2}e_2\) changes lag at root-\(n\) | oracle order is not oracle equivalence | **DISPROVED**, APP-B CE-B6 |
| symmetric matrices are flat under any metric | full AIRM SPD has commutator curvature | name Sym-Frobenius versus AIRM | **DISPROVED**, APP-A §5 |
| flat means global Euclidean chart | torus/Klein bottle | simply connected convex support tube | **DISPROVED**, APP-A §3 |
| polynomial mixing gives root-\(n\) | bounded regenerative scalar process | C-PD or checked stronger inequality | **DISPROVED**, APP-C §3 |
| normalization is harmless | \(Y/\sqrt p\) can dilute \(\Delta_n\) | recompute energy, signal, and estimand | **DISPROVED**, APP-C C-E4 |

## 7. Property-first application scorecard

Rates use the actual \(\Delta_n\); replace it by \(s_n^2\) only after verifying the HD1 full-rank-lag condition.

| Family | Space / dimension | Energy | Geometry / law | Dependence / signal | Estimator / cancellation | Defects and scale | Result | Failure modes | Feasibility | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Hilbert functional/multivariate | separable Hilbert; basis may grow | bounded functional norm/fixed intrinsic rank | globally flat; no symmetry needed for split branch | finite memory split; C-PD robust; LN and gap | positive or signed; FR zero and L-M centred | mask/coupling/LN; \(\ell^2+\rho=o(n^{-1/2})\) | robust R; oracle (3.2) under split | long memory, pervasive energy, weak gap | **EXACT STRUCTURAL MATCH** | T-APP-1/3/4/5 |
| Symmetric matrices, Frobenius | \({\rm Sym}(m)\), \(m(m+1)/2\) | bounded Frobenius variation | vector-space flat | finite memory/C-PD; LN/gap | Euclidean signed/positive; same split | PSD/metric target, mask/LN | robust and split-oracle | entrywise energy; AIRM estimand differs | **EXACT STRUCTURAL MATCH** | T-APP-1/3 |
| Fixed-basis SPD | common AIRM flat; \(m\) log coordinates | bounded log-eigenvalue energy | flat totally geodesic | finite memory/C-PD; LN/gap in algebra | estimator constrained to flat | off-algebra \(\varepsilon_A=o(n^{-1/14})\) for approximate oracle | robust fallback; exact-split oracle | changing axes, zero eigenvalues, dilution | **EXACT STRUCTURAL MATCH** if DGP-fixed basis | T-APP-1/3 |
| Nearly fixed-basis SPD | full AIRM band | separate bounded energy | curved perturbation of fixed algebra | same temporal/signal checks | constrained/regularized | direct off-algebra and normalized ribbon defects, total \(o(n^{-1/2})\) | degraded equation (3.1) | raw commutators, multiplicity, basis drift | **STABLE APPROXIMATE MATCH** only with direct defects | APP-A §4; APP-B §7 |
| Full covariance/correlation SPD | AIRM; \(m(m+1)/2\) | band is insufficient; bounded energy uses R; HE uses its typed energy/signal ledger | Hadamard, locally symmetric, curved; GLO absent generically | finite memory/C-PD robust; LN/gap explicit | positive three-scale PF; FRAME-2P-U only if U2P/GLO/split checks hold | noncommutation, frame, escape, LN, HE scaling, U2P actions | bounded-energy HD1/C-PD; bounded-tail HE; conditional curved oracle | moving eigenvectors, coloured noise, signal dilution, unverified U2P | **CONDITIONAL MATCH — CHECKS LISTED** | T-APP-2/3B/6; R |
| Individual diffusion tensors | AIRM SPD(3), fixed \(p=6\) | band/tube plausible | curved unless common axes | temporal and gap checked | fixed-\(p\) positive; flat submodel | axis change/band escape | robust fixed-\(p\), or flat oracle | fibre crossings/rotations | **STABLE APPROXIMATE MATCH** | APP-A/C |
| Functional connectivity covariance | regularized SPD, \(m_n\) regions | bounded-energy continuum, bounded-tail HE, or proved truncation regime | generally noncommuting/singularity risk | overlapping-window dependence; signal may dilute or strengthen | positive three-scale PF | regularization target, escape, LN, overlap, HE phase | conditional bounded-energy fallback or HE theorem | changing eigenvectors/pervasive modes | **CONDITIONAL MATCH — CHECKS LISTED** | T-APP-6 |
| Product manifolds / voxelwise tensors | product dimension sum | summable component energy | componentwise; flat only if active factors flat | vector C-PD and aggregate gap | positive; signed with block budget | energy, block count, dilution | robust or signed mean | growing components/cross dependence | **STABLE APPROXIMATE MATCH** | T-APP-4/5 |
| Constant-negative-curvature embeddings | bounded hyperbolic tube; \(p_n\) may grow | bounded radius/energy | locally symmetric, curved; GLO separate | exact finite-memory colours for FRAME-2P-U; LN/gap | structural signed LP or two-path correction | verify U2P actions/replacements, masks, GLO, and law accuracy | faster mean; robust loading; curved oracle under U2P | heteroskedasticity, frame, failed split | **CONDITIONAL ORACLE MATCH — CHECKS LISTED** | T-APP-3B/5 |
| Grassmann/shape/compact symmetric | metric-specific | tube model needed | cut/conjugacy risks despite local symmetry | separate | new localized theorem | quantitative margins | no current growing-\(p\) corollary | nonunique Log/mean | **UNKNOWN / DIAGNOSTIC-ONLY** | APP-A §6 |
| Diagonal BW SPD | fixed basis; positive square-root coordinates | root-energy and coordinatewise lower margin | exactly flat root coordinates | finite memory/C-PD and actual gap checked | localized coordinate mean; rigid frame | Richardson/blend positivity and standard flat defects | fixed-basis diagonal HE–BW corollary | zero coordinates, basis change, diluted gap | **EXACT MATCH** within the stated direct-observation model | T-APP-7 |
| Full BW covariance | full-rank SPD, fixed or growing matrix size | bounded tangent energy on fixed margins; shrinking support/energy on the fractional-normal branch | free quotient with dimension-uniform fixed-margin calculus and restricted shrinking-margin calculus | finite memory or proved dependence and actual lag target | localized/regularized mean and generated-object fallback | spectral, polar, Exp, normal-pair, path, connector, reconstruction, object-count, and gap checks | fixed-size theorem; fixed-margin growing-size geometry; restricted shrinking-margin statistical theorem | rank loss; global means; pervasive shrinking-normal energy; generated-domain escape | **CONDITIONAL MATCH — CHECKS LISTED** | T-APP-7 |

## 8. Post-closure application remapping

These labels govern application claims after the HE/BW proof campaign. They classify the complete observation-to-estimand route, not just the ambient geometry.

| Application family | Authoritative label | What is matched | Mandatory checks or displayed defect |
|---|---|---|---|
| Fixed-axis diagonal covariance/volatility | **EXACT MATCH** | directly observed positive diagonal covariance series in one scientific basis, analysed in BW root coordinates | common basis, coordinatewise root margin, bounded-tail/dependence ledger, actual \(\Delta_n\), and generated Richardson/blend positivity |
| Functional/Hilbert data | **CONDITIONAL MATCH — CHECKS LISTED** | direct Hilbert-valued observations with flat geometry | total rather than coordinatewise energy, product-process dependence, mean/frame budget, lag target, and eigengap |
| Expanding sensor arrays | **CONDITIONAL MATCH — CHECKS LISTED** | direct high-dimensional observations under the bounded-tail or expanding-domain truncation HE theorem | effective energy/truncation scale, \(A_{2,n},\Delta_n\), product dependence, tail integrals, generated-tube closure, contamination, and selector window |
| Gene-expression panels | **CONDITIONAL MATCH — CHECKS LISTED** | direct panel observations under the bounded-tail or expanding-domain truncation HE theorem | preprocessing/normalisation must preserve the estimand; verify energy/tails, dependence, pervasive versus localised signal, target contamination, and gap |
| Realised covariance/correlation finance | **CONDITIONAL MATCH — CHECKS LISTED** | full-rank BW analysis of a fixed- or growing-size covariance-matrix series after construction, using the fixed-margin or restricted fractional-normal package as applicable; parent APP-FIN and public code supply a 12-stock monthly baseline | reproduce/audit the parent RFM/LFM/LOCF/EWMA pipeline, then check sampling/noise/asynchronicity covariance-estimation error, regularisation target, complete generated-domain margins, support/energy regime, temporal dependence, object counts, and actual lag gap |
| Functional-connectivity covariance/diffusion | **CONDITIONAL MATCH — CHECKS LISTED** | fixed- or growing-size regularised SPD series under local AIRM or the applicable BW package | window-overlap dependence, preliminary covariance error, regularisation bias, spectral/polar/Exp/normal margins, support/energy, signal dilution, generated-domain reach, and estimand-specific gap |
| Nearly fixed-axis covariance | **APPROXIMATE MATCH — DEFECT PENALTY DISPLAYED** | a fixed-basis diagonal/root model plus controlled off-basis motion | add the measured off-algebra, frame, connector, and target-contamination defects to \(q_{R,n}\) and \(d_n\); require \(\eta_n=o(\Delta_n)\) |
| Rank-changing or globally singular BW covariance | **REJECTED MATCH — ESTIMAND OR ASSUMPTIONS NOT DEFENSIBLE** | none under the present theorem | continuum alignments/geodesics/means and singular Log/lift behaviour invalidate the claimed construction |
| General growing-size noncommuting BW covariance | **CONDITIONAL MATCH — CHECKS LISTED** | directly observed full-rank matrix series on either the compatible fixed-margin domain or the restricted fractional-normal shrinking domain | verify complete generated-domain margins, support/energy, path/grid/object counts, dependence and lag target, (A_{2,n}), and (Delta_n); fixed bands alone still do not prove those statistical conditions |

For covariance applications the scientific pipeline is explicitly
\[
\text{raw multivariate data}\longrightarrow
\text{estimated/regularised covariance series}\longrightarrow
\text{AIRM or BW RFM}\longrightarrow
\text{separate factor forecasting}.
\]

For APP-FIN this pipeline has a concrete starting implementation: the parent repository contains BW utilities, simulation code, and S&P 500 analysis/reproduction scripts. That lowers engineering cost and fixes a comparison baseline; it does not verify the project's moving-centre, HE, selector-repair, or FRAME assumptions.
The first arrow has its own measurement-error, dependence, and target budget. The RFM theorem does not prove that layer, and reconstruction error is not a forecasting theorem.

## 9. Ranked programme

1. **HE application verification:** instantiate either the proved bounded-tail \((R_n,A_{2,n},\Delta_n)\) ledger or the expanding-domain truncation ledger for asset, sensor, gene, imaging, and connectivity systems rather than normalising by fiat.
2. **BW application verification and covariance-measurement layer:** use the proved fixed-margin or restricted fractional-normal theorem only when its complete support/slack/path/row/gap package is verified; separately quantify preliminary covariance estimation.
3. **FRAME-2P-U application verification:** first construct or disprove a genuinely growing-curvature family satisfying the dimension-uniform composed-action and replacement producers; then identify data laws satisfying exact colours, masks, GLO, and exact-law/\(a>1/2\). Retain the robust theorem whenever any producer fails.
4. **Hilbert functional/multivariate factors:** exact flatness, interpretable C-PD, robust and split-oracle branches already available.
5. **Fixed-axis diagonal covariance/volatility/diffusion:** exact common flat when the axes are scientific structure, not preprocessing.
6. **Full AIRM covariance/correlation:** high scientific value and verified growing-size geometry; bounded-energy robust theorem is honest, while FRAME-2P-U is available only after its application-specific U2P/GLO/split checks.
7. **Symmetric-matrix factors under Frobenius loss and individual diffusion tensors:** credible present applications when their stated metric/axis assumptions are the scientific estimand.
8. **Constant-curvature embeddings:** clean signed growing-\(p\) mean application and the explicit nonempty FRAME-2P-U curved witness class.
9. **Compact symmetric spaces:** future local-geometry programmes; no current growing-\(p\) corollary.

Every fragile accelerator within the bounded-energy AIRM/Hadamard scope retains (R) as its robust fallback. The HE theorem is usable only after its complete phase and generated-domain conditions are checked. BW is closed at fixed size, on fixed-margin size-uniform generated domains, and on the restricted fractional-normal shrinking class. Rank change, pervasive shrinking-normal energy, and unrestricted globally sharp growth remain outside the proved scope.

## 10. Dependency graph

\[
\begin{array}{c}
\text{T-APP-1 flat}\to \text{frame zero},\qquad
\text{exact split + GLO}\to\text{conditional mean centring},\\
\{\text{frame zero},\text{mean centring},\text{oracle HS row},\text{LN}\}
\to\text{T-APP-3 row}\to
\{2A_2d+d^2,\text{ Davis--Kahan},d^2\text{ null spectrum}\};\\
\text{T-APP-2 AIRM calculus}\to\text{HD-G}\to\text{robust HD1};\qquad
\text{T-APP-4 C-PD}\to\{\text{G1},\text{oracle HS row}\};\\
    \text{T-APP-5 signed structure}\to\text{faster mean}
    \not\Rightarrow\text{immunity};\qquad
    \text{root-}n\text{ parametric centre}\to\text{oracle order, not immunity};\\
    \text{U2P + three colours + undersmoothed validation}\to
    \text{T-APP-3B corrected root-}n\text{ row};\\
    \text{T-APP-6 HE}\to\{\text{G1,row,comparison,gap phase}\};\qquad
    \text{T-APP-7 BW fixed/fractional-normal}\to
    \{\text{local geometry,mean/frame,lag target,restricted size growth}\};\\
    \text{unrestricted nonlocal sharp powers OPEN}\dashrightarrow
    \text{optional sharper BW windows}.
\end{array}
\]

The robust HD1 and exact-flat branches consume no open node. FRAME-2P-U is instead an explicit conditional implication: it consumes U2P primitives, and verification for a genuinely growing-curvature application remains open. Full-AIRM robust HD1 uses T-APP-2; a full-AIRM FRAME-2P-U application does not inherit U2P, GLO, masks, or sample separation from local symmetry.

## 11. Status and optional work

| Node | Status | Consequence | Proof |
|---|---|---|---|
| four-linear-term expansion | **PROVED** | all cancellation rows | APP-B Lemma APP-B1 |
| exact flat/common-flat reduction | **PROVED** | T-APP-1 | APP-A §§2–3 |
| AIRM fixed-band finite-order HD-G | **PROVED** | closes AIRM differential primitive | APP-A §5 and cross-audits |
| flat exact-split oracle branch | **PROVED UNDER ASSUMPTIONS** | T-APP-3 | APP-B §§3–4 |
| GLO implies generic curved oracle | **DISPROVED** | direct frame coefficient required | APP-B CE-B5 |
| parametric centre root-\(n\) rate | **PROVED; not immunity** | oracle-order corollary | APP-B §5/CE-B6 |
| C-PD robust extension | **PROVED** | T-APP-4 | APP-C §3 |
| infinite-memory conditional split | **OPEN/CONDITIONAL** | consumed by no theorem | APP-C §3.3; APP-B §7.1 |
| structural signed growing-\(p\) G1 | **PROVED UNDER ASSUMPTIONS** | T-APP-5 | APP-C §4 |
| unrestricted full-AIRM signed G1 | **OPEN** | consumed by no theorem | APP-C §4.2 |
| positive curvature-corrected \(q\ge4\) | **OPEN** | consumed by no theorem | G1 / OPEN OBLIGATIONS |
| FRAME-2P-U conditional frame/mean debiasing | **ASSUMPTION-TO-CONCLUSION IMPLICATION PROVED** | root-\(n\) row order and \(n^{-1}\) null spectrum; no oracle limit-law equivalence | [[FRAME-2P-U — conditional two-path debiasing theorem]]; archived FRAME-IF dossiers |
| same-band score/Richardson debiasing | **DISPROVED** | generically retains \(n^{-3/7}\) curved bias | FRAME-IF-B/C |
| direct frame/\(\Omega\) plug-in | **CONDITIONAL** | valid only with an extra observable frame producer | FRAME-IF closure |
| invariant-only frame redesign | **REJECTED FOR THIS ESTIMAND** | changes the loading target | FRAME-IF closure |
| bounded-tail growing-energy/pervasive-factor theorem | **PROVED UNDER EXPLICIT ASSUMPTIONS** | selective HE application remapping | [[HE — canonical growing-energy theorem boundary]]; archived HE dossier |
| expanding-domain HE truncation theorem | **PROVED UNDER EXPLICIT ASSUMPTIONS** | unbounded-score HE applications with explicit tail/domain checks | [[HE — canonical growing-energy theorem boundary]]; archived HE-TRUNC dossier |
| fixed-size local full-rank moving-centre BW theorem | **PROVED UNDER EXPLICIT ASSUMPTIONS** | fixed-size BW applications | [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]]; archived BW dossier |
| diagonal fixed-basis HE–BW corollary | **PROVED UNDER EXPLICIT ASSUMPTIONS** | exact restricted intersection | T-APP-7 / archived joint dossier |
| noncommuting BW fixed-margin geometry | **PROVED UNDER EXPLICIT ASSUMPTIONS** | closes the HD-G producer on compatible generated domains | [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]]; archived A/B/C dossiers |
| BW shrinking-margin statistical extension | **PROVED UNDER RESTRICTED FRACTIONAL-NORMAL ASSUMPTIONS** | sufficient local windows; no growing-energy claim | [[BW-SHRINKING-MARGIN — canonical restricted theorem boundary]]; archived D/E/F dossiers |
| unrestricted nonlocal BW sharp powers | **OPEN — OPTIONAL EXPONENT MINIMISATION** | consumed by no theorem | OPEN OBLIGATIONS BW-U-D1--U-D4 |

## 12. Cross-audit record

The hostile pass made these material corrections before integration:

- Ribbon stability now uses normalized curvature-operator action on the actual ribbon planes, not sectional-curvature shorthand.
- Near-commuting Hessian stability uses analytic functional calculus and a direct fixed-algebra off-component bound, not a raw commutator slogan.
- Pairwise conditional total variation does not give whole-row concentration; approximate infinite-memory splitting requires joint row coupling or conditional C-PD plus estimator stability.
- The frame coefficient uses the direct-sum HS lag-energy budget, not a potentially smaller operator-norm signal quantity.
- Lag contamination enters as \(2A_{2,n}\zeta_n+\zeta_n^2\); the actual gap remains \(\Delta_n\).
- AIRM calculus verifies HD-G only. Constant-curvature scalar-plus-rank-one structure proves signed G1 only. Neither is a statistical cancellation theorem.

The cross-audit records are APP-A §11, APP-B §14, APP-C §9, the archived FRAME-DB/FRAME-IF two-pass campaign, the joint HE–BW hostile audit, the HE-TRUNC proof, and the fixed- and shrinking-margin BW campaigns under Archived/Proof workstreams. Every proved application row depends only on proved nodes; conditional application labels display their remaining model-specific checks. FRAME-2P-U, the bounded-tail HE theorem, expanding-domain truncation theorem, fixed-size local BW theorem, fixed-margin growing-size geometry, restricted fractional-normal shrinking-margin theorem, and diagonal intersection are proved under their displayed packages. Unrestricted nonlocal BW exponent minimisation remains optional and is consumed by no proved theorem.

The planned empirical stress tests are specified in [[Numerical suite — theorem-driven design matrix]]. They are downstream diagnostics and do not change any analytical status.
