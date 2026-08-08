---
type: canonical-application-map
title: Application map — geometry, symmetry, and rate accelerators
status: canonical-proof
verdict: robust bounded-energy Paper 1 and its application-specific accelerators are closed under explicit assumptions; growing-energy/pervasive-factor scaling and full moving-centre Bures–Wasserstein geometry are the two primary open application programmes
last-audited: 2026-08-08
---

# Application map — geometry, symmetry, and rate accelerators

> **Authority and scope.** [[HD1 — growing-dimension Paper 1 proof dossier]] remains the proof source for the robust theorem. This file is the canonical source for property-to-application matching. APP-A, APP-B, and APP-C are preserved under `Archived/Proof workstreams` as noncanonical proof records. Paper 2 is out of scope.

## 0. Current conclusions

1. The robust arbitrary-\(p_n\) result remains
   \[
   d_n=O_p(n^{-1/2}+\ell_n),\qquad
   \|\sin\Theta(\hat E_n,E_n)\|_{\rm op}
   =O_p\!\left(\frac{n^{-1/2}+\ell_n}{\Delta_n}\right),
   \quad
   \ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
   \tag{R}
   \]
   At \(b_n=n^{-1/7}\), \(a\ge3/7\), its numerator is \(n^{-3/7}\). **PROVED in HD1.**
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
8. When total energy grows, the proved defect identities expose factors \(R_n\) and \(R_n^2\) in mean-score and lag-product errors. Whether loading recovery survives depends jointly on these numerators, \(A_{2,n}\), and \(\Delta_n\). A complete pervasive-factor phase diagram is **OPEN**; normalisation is not a theorem because it may erase a localised signal.
9. The parent covariance application uses Bures–Wasserstein geometry. The AIRM differential theorem does not transfer to it. Diagonal fixed-basis BW is flat, but full noncommuting moving-centre BW requires a separate domain, differential, mean/frame, and lag-identification proof. **OPEN PROGRAMME.**

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
| FR-N | \(\Omega_tY_t\) | non-rigid frame | \(O_p(\ell_n)\) robustly | lag products | zero in one flat; otherwise direct coefficient bound |
| HOL | ribbon/polygon holonomy | curvature interaction | PF gives \(O_p(\ell_n)\) | FR-N | zero if \(R\) vanishes on normalized ribbon planes; \(\nabla R=0\) is insufficient |
| L-M1 | \(-H_te_t\otimes Y_{t-h}\) | linear mean lag term | \(O_p(\ell_n)\) pathwise | \(d_n\) | conditional GLO + exact split gives \(O_p(\ell_n/\sqrt n)\) |
| L-M2 | \(-Y_t\otimes H_{t-h}e_{t-h}\) | linear mean lag term | same | \(d_n\) | reverse-endpoint GLO |
| L-F1 | \(\Omega_tY_t\otimes Y_{t-h}\) | linear frame lag term | \(O_p(\ell_n)\) | \(d_n\) | frame rigidity/flatness/direct defect only |
| L-F2 | \(Y_t\otimes\Omega_{t-h}Y_{t-h}\) | linear frame lag term | same | \(d_n\) | same |
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
**PROVED UNDER EXPLICIT ASSUMPTIONS.** The concrete exact branch is flat/common-commuting geometry plus exact splitting, where \(\varepsilon_G=\phi_F=0\). A generic curved moving-centre branch is **CONDITIONAL** until it proves \(\phi_F=o(n^{-1/2})\); GLO does not imply this.

At \(b_n=n^{-1/7}\), \(a\ge3/7\), the squares \(b_n^6,(nb_n)^{-1},n^{-2a},n^{-2}\) are \(O(n^{-6/7})\), and cross-terms are bounded by sums of squares. Thus \(\ell_n^2=o(n^{-1/2})\), while \(\ell_n/\sqrt n=O(n^{-13/14})\). Split-mask terms must separately be \(o(n^{-1/2})\), e.g. block length \(B_n\) must satisfy \(B_n/n=o(n^{-1/2})\).

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

### T-APP-6 — growing-energy/pervasive-factor programme

Let \(R_n=\sup_t\|Y_{t,n}\|\) and let \(q_{R,n}\) denote a mean/frame error rederived with every energy, tail, dependence, and tube constant exposed. The proved algebraic and concentration ledgers give the benchmark scales

\[
\text{score}=O_p\!\left(\frac{R_n}{\sqrt{nb_n}}\right),\qquad
\text{oracle row}=O_p\!\left(\frac{R_n^2}{\sqrt n}\right),\qquad
\text{feasible comparison}\lesssim 2R_nq_{R,n}+q_{R,n}^2.
\tag{3.6}
\]

The operator perturbation remains \(\eta_n=2A_{2,n}d_n+d_n^2\), and the loading condition remains \(\eta_n=o(\Delta_n)\). Thus growing energy is not automatically fatal when pervasive lag signal strengthens \(\Delta_n\), but no such compensation may be assumed. **SCALING LEDGER PROVED; COMPLETE THEOREM AND PHASE DIAGRAM OPEN.**

### T-APP-7 — moving-centre Bures–Wasserstein programme

For full noncommuting covariance matrices under BW geometry, a Paper 1 theorem requires: a quantitative domain away from rank-loss/nonunique-alignment strata; uniqueness of every population and empirical mean; dimension-uniform score, Hessian, Exp/Log, alignment, connector, Richardson, and ruled-surface bounds on generated images; a BW-valid feasible frame or replacement estimator; and a lag-identification theorem in the BW tangent norm. **OPEN.**

The diagonal fixed-basis submodel reduces to flat square-root coordinates and may reuse T-APP-1 after checking boundary, energy, dependence, and signal. This special case does not prove the full BW programme.

## 4. Stability and reality bridge

| Approximate property | Defect | Proven penalty | Effect | Oracle requirement at \(b=n^{-1/7}\) | Feasibility |
|---|---|---|---|---|---|
| GLO/reflection | \(\varepsilon_{G,n}=\max_h\sup_{\|v\|=1}\|E(H_tv\otimes Y_{t-h})\|\vee\cdots\) | \(\varepsilon_{G,n}\ell_n\) | population linear coefficient | \(\varepsilon_{G,n}=o(n^{-1/14})\) | stable only if model supplies this operator defect |
| fixed algebra | \(Y=D+N\), aligned \(D,e\), \(\|N\|_F\le\varepsilon_{A,n}\) | \(O(\varepsilon_{A,n}\ell_n)\) Hessian action | recentering | same \(o(n^{-1/14})\) | **STABLE APPROXIMATE** if basis is meaningful |
| relevant-plane flatness | normalized \(\varepsilon_{R,n}=\sup\|R(S_s,S_\tau)\|/\|S_s\wedge S_\tau\|\) | \(\varepsilon_{R,n}\operatorname{Area}\) | frame | direct frame term \(o(n^{-1/2})\) | raw commutators remain diagnostic |
| frame rigidity | direct-sum HS \(\phi_{F,n}\) | additive \(\phi_{F,n}\) | signal-carrying frame bias | \(o(n^{-1/2})\) | exact in one flat; fragile in full AIRM |
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
| Known centre | zero | zero | \(n^{-1/2}+\rho_n\) | oracle | \(n^{-1}\) | oracle window | **PROVED** |
| Constant/parametric centre | \(n^{-1/2}\) | \(n^{-1/2}\) or rigid | \(n^{-1/2}\) | oracle order; changed limit possible | \(n^{-1}\) | oracle window | **PROVED; not immunity** |
| Signed structural mean | \(\ell_{q,n}\) | first order unless flat | \(n^{-1/2}+\ell_{q,n}\) robustly | \((n^{-1/2}+\ell_{q,n})/\Delta_n\) | row square | row-based | **PROVED mean; robust loading chain** |
| Growing energy/pervasive signal | \(q_{R,n}\), to be rederived | energy-scaled | benchmark \(R_n^2n^{-1/2}+2R_nq_{R,n}+q_{R,n}^2+\) defects | \((2A_{2,n}d_n+d_n^2)/\Delta_n\) | row square after proof | regime-specific | **OPEN; component scaling ledger proved** |

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
| Full covariance/correlation SPD | AIRM; \(m(m+1)/2\) | band is insufficient; bounded energy uses R, pervasive energy awaits T-APP-6 | Hadamard, locally symmetric, curved; GLO absent generically | finite memory/C-PD robust; LN/gap explicit | positive three-scale PF; no automatic cancellation | noncommutation, frame, escape, LN, HE scaling | bounded-energy robust HD1/C-PD; pervasive branch open | moving eigenvectors, coloured noise, signal dilution | **EXACT AIRM GEOMETRY; HE ACCELERATION OPEN** | T-APP-2/6; R |
| Individual diffusion tensors | AIRM SPD(3), fixed \(p=6\) | band/tube plausible | curved unless common axes | temporal and gap checked | fixed-\(p\) positive; flat submodel | axis change/band escape | robust fixed-\(p\), or flat oracle | fibre crossings/rotations | **STABLE APPROXIMATE MATCH** | APP-A/C |
| Functional connectivity covariance | regularized SPD, \(m_n\) regions | bounded-energy continuum or HE theorem needed | generally noncommuting/singularity risk | overlapping-window dependence; signal may dilute or strengthen | robust positive only at bounded energy | regularization target, escape, LN, overlap, HE phase | conditional bounded-energy fallback; HE open | changing eigenvectors/pervasive modes | **MODEL-FRAGILE; HIGH-VALUE HE TARGET** | T-APP-6 |
| Product manifolds / voxelwise tensors | product dimension sum | summable component energy | componentwise; flat only if active factors flat | vector C-PD and aggregate gap | positive; signed with block budget | energy, block count, dilution | robust or signed mean | growing components/cross dependence | **STABLE APPROXIMATE MATCH** | T-APP-4/5 |
| Constant-negative-curvature embeddings | bounded hyperbolic tube; \(p_n\) may grow | bounded radius/energy | locally symmetric, curved; GLO separate | C-PD; LN/gap | structural signed LP | GLO and frame must separately satisfy (3.1) | faster mean; robust loading | heteroskedasticity, frame | **EXACT STRUCTURAL MATCH for signed mean only** | T-APP-5 |
| Grassmann/shape/compact symmetric | metric-specific | tube model needed | cut/conjugacy risks despite local symmetry | separate | new localized theorem | quantitative margins | no current growing-\(p\) corollary | nonunique Log/mean | **UNKNOWN / DIAGNOSTIC-ONLY** | APP-A §6 |
| Diagonal BW SPD | fixed diagonal algebra; square-root coordinates | bounded root-energy/lower margin | flat diagonal coordinates | C-PD possible; gap checked | coordinate estimator/split | boundary and standard flat defects | flat robust/oracle | zero eigenvalues/basis change | **EXACT STRUCTURAL MATCH under diagonal restriction** | APP-A §6 |
| Full BW covariance | full BW metric | separate BW and HE budgets | incomplete on SPD; quotient/alignment structure | separate dependence and lag target | BW-specific mean/frame estimator | PSD boundary, alignment, generated-set calculus | diagonal flat only; full theorem open | rank loss, nonuniqueness, target change | **PRIMARY OPEN PROGRAMME** | T-APP-7 |

## 8. Ranked programme

1. **HE theorem:** reopen expanding asset, sensor, gene, imaging, and connectivity systems by proving the joint \((R_n,A_{2,n},\Delta_n)\) regime rather than normalising by fiat.
2. **Moving-centre full BW theorem:** connect Paper 1 directly to the parent covariance application, fixed matrix size first and growing size second.
3. **Hilbert functional/multivariate factors:** exact flatness, interpretable C-PD, robust and split-oracle branches already available.
4. **Fixed-axis diagonal covariance/volatility/diffusion:** exact common flat when the axes are scientific structure, not preprocessing.
5. **Full AIRM covariance/correlation:** high scientific value and verified growing-size geometry; bounded-energy robust theorem is honest, pervasive and oracle branches remain application-fragile.
6. **Symmetric-matrix factors under Frobenius loss and individual diffusion tensors:** credible present applications when their stated metric/axis assumptions are the scientific estimand.
7. **Constant-curvature embeddings:** clean signed growing-\(p\) mean application, not an oracle loading application without T-APP-3.
8. **Compact symmetric spaces:** future local-geometry programmes; no current growing-\(p\) corollary.

Every fragile accelerator within the bounded-energy AIRM/Hadamard scope retains (R) as its robust fallback. T-APP-6 and T-APP-7 lie outside that scope: high energy must satisfy its own phase condition, and full BW must first supply its own geometry-and-estimator theorem.

## 9. Dependency graph

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
    \text{T-APP-6 HE OPEN}\dashrightarrow\{\text{G1,row,comparison,gap phase}\};\qquad
    \text{T-APP-7 BW OPEN}\dashrightarrow\{\text{geometry,mean/frame,lag target}\}.
\end{array}
\]

No OPEN or CONDITIONAL node is consumed by a proved theorem. The flat oracle branch uses exact finite-memory separation, not the open infinite-memory coupling branch. Full-AIRM robust HD1 uses T-APP-2, not the open full-AIRM signed or oracle branches.

## 10. Status and optional work

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
| generic frame/Hessian debiasing | **OPEN** | consumed by no theorem | APP-B §7 |
| growing-energy/pervasive-factor theorem | **OPEN; component scalings proved** | primary next programme | T-APP-6 / OPEN OBLIGATIONS HE |
| full moving-centre BW theorem | **OPEN; diagonal flat special case only** | primary next programme | T-APP-7 / OPEN OBLIGATIONS BW |

## 11. Cross-audit record

The hostile pass made these material corrections before integration:

- Ribbon stability now uses normalized curvature-operator action on the actual ribbon planes, not sectional-curvature shorthand.
- Near-commuting Hessian stability uses analytic functional calculus and a direct fixed-algebra off-component bound, not a raw commutator slogan.
- Pairwise conditional total variation does not give whole-row concentration; approximate infinite-memory splitting requires joint row coupling or conditional C-PD plus estimator stability.
- The frame coefficient uses the direct-sum HS lag-energy budget, not a potentially smaller operator-norm signal quantity.
- Lag contamination enters as \(2A_{2,n}\zeta_n+\zeta_n^2\); the actual gap remains \(\Delta_n\).
- AIRM calculus verifies HD-G only. Constant-curvature scalar-plus-rank-one structure proves signed G1 only. Neither is a statistical cancellation theorem.

The cross-audit records are APP-A §11, APP-B §14, and APP-C §9 under `Archived/Proof workstreams`. Every proved application row depends only on proved nodes; conditional accelerators display their missing coefficient. The HE and BW programmes were added after canonical reconstruction and are not consumed by any proved branch.
