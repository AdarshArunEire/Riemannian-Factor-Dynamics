---
type: archived-proof-workstream
title: Joint HE-BW error ledger and hostile audit
status: archived-after-two-hostile-passes
authority: archived-noncanonical
owner: Agent X
scope: Paper 1 HE and BW hostile audit only
last-audited: 2026-08-08
---

# Joint HE-BW error ledger and hostile audit

> **Archived hostile-audit provenance, not canon.** This file preserves the common typed ledger and both hostile passes. The bounded-tail HE theorem, fixed-size local BW theorem, and fixed-basis diagonal intersection passed; the exact open and disproved branches remain excluded. Current canonical sources govern all status decisions.

## 0. Audit rules and common notation

All quantities are compared in one anchor Hilbert space only after the necessary connector, lift, or alignment maps have made their domains and codomains identical. The default rank-one convention is

\[
(x\otimes y)z=\langle y,z\rangle x,
\qquad \|x\otimes y\|_{\rm HS}=\|x\|\,\|y\|.
\]

The norms are never interchangeable:

- \(\|\cdot\|_T\): the metric tangent norm at a stated base point;
- \(\|\cdot\|_{\rm op}\): operator norm on a tangent Hilbert space;
- \(\|\cdot\|_{\rm HS}\): Hilbert--Schmidt/Frobenius norm of a lag operator;
- \(\|D\|_{\oplus,\rm op}=(\sum_{h\le h_0}\|D_h\|_{\rm op}^2)^{1/2}\): lag-row direct-sum operator bound;
- \(\|D\|_{\oplus,\rm HS}=(\sum_{h\le h_0}\|D_h\|_{\rm HS}^2)^{1/2}\): lag-row direct-sum HS norm;
- \(\|\sin\Theta(\widehat E,E)\|_{\rm op}\): loading-subspace projector/operator loss.

For the bounded-energy canonical theorem,

\[
\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1},
\qquad R=\sup_t\|Y_{t,n}\|_T=O(1).
\]

For HE, do not define a single omnibus constant. Use at least

\[
R_n=\sup_t\|Y_{t,n}\|_T,\quad
V_{S,n}^2=\sup_{u,j}E\|S_{t,j}(u)-ES_{t,j}(u)\|_T^2,
\]

\[
V_{W,n,h}^2=E\|Y_t\otimes Y_{t-h}-E(Y_t\otimes Y_{t-h})\|_{\rm HS}^2,
\]

plus the corresponding score and product dependence budgets, geometry/tube constants, lag count \(h_{0,n}\), factor rank \(r_n\), row size \(A_{2,n}\), and actual gap \(\Delta_n\). The envelope bounds \(V_{S,n}\le C R_n\) and \(V_{W,n,h}\le C R_n^2\) are fallbacks, not definitions.

For BW, \(m\) is matrix size and \(p=m(m+1)/2\) only on the full SPD tangent space. A fixed-rank PSD stratum has a different tangent dimension and quotient structure. Every BW symbol must state the selected domain and tangent/lift convention before it is used.

### Status convention inside this dossier

`BASE PROVED` means the bounded-energy HD1 producer is proved. `HE OPEN` and `BW OPEN` mean the replacement producer has not yet survived audit. These labels are local shorthand; final canonical labels must be one of the repository's allowed statuses.

## 1. Shared row-by-row error ledger

| ID / channel | Exact mathematical quantity | Typed norm | Producer lemma | Direct consumer | Bounded-energy rate | Proposed HE rate or required replacement | Proposed BW replacement | Current status | Failure / counterexample if shortcut is false |
|---|---|---|---|---|---|---|---|---|---|
| M-B: mean bias | \(\beta_n(u)=\Log_{\mu_n(u)}\mu^{(3)}_{\mathrm{pop},n}(u)\), with local-stationarity discrepancy separated into M-LS | \(\sup_u\|\beta_n(u)\|_T\) and \(L^2(du;T)\) | HD1-A Lemmas 5.1--5.2; canonical G1 | stage mean error, generated-tube event, grid mean | \(O(b_n^3+n^{-1})\) for smooth/design bias; add M-LS separately | \(O(\mathfrak B_{3,n}b_n^3+\mathfrak G_n/n)\), where \(\mathfrak B_{3,n}\) contains the actual law/score/Exp--Log derivatives. It is **not proved** to be \(R_n b_n^3\), \(b_n^3\), or any universal power of \(R_n\) | BW population three-scale barycentre expansion in the chosen domain, including base-change/Richardson cubic remainder and its generated-set margin | BASE PROVED; HE OPEN; BW OPEN | Multiplying only the stochastic term by \(R_n\) leaves a hidden growing bias/tube constant. In diagonal BW square-root coordinates the bias is Euclidean, but this does not cover noncommuting BW |
| M-S: mean score fluctuation | \(Z_{j,n}(u)=\sum_t w_{j,t}(u)\{\Log_{z_{j,n}(u)}X_{t,n}-E\Log_{z_{j,n}(u)}X_{t,n}\}\) | tangent Hilbert norm; sup in \(u\) or \(L^2(du)\) | HD1-A Lemmas 4.1--4.2; APP-C C-PD1--3 | empirical Sturm/strong-convexity mean reduction | RMS \((nb_n)^{-1/2}\); sup \(\sqrt{\log n/(nb_n)}\) | variance-sensitive RMS \(\Theta^S_{2,n}/\sqrt{nb_n}\); sup requires an explicit tail budget, e.g. \(\Theta^S_{\infty,n}\sqrt{\log n/(nb_n)}\). Envelope fallback \(R_n/\sqrt{nb_n}\) and \(R_n\sqrt{\log n/(nb_n)}\) | BW score at a deterministic population barycentre, transported/lifted to one Hilbert space; prove its second moment, dependence coefficients, and coercive score-to-distance reduction | BASE PROVED; HE OPEN; BW OPEN | Coordinatewise bounds yield \(\sqrt{p_n/(nb_n)}\), not a dimension-free Hilbert rate. A scalar tail citation does not prove a tangent-Hilbert tail |
| M-LS: local stationarity | actual/proxy score defect \(D_{j,n}(u,q)=\sum_t w_{j,t}(u)\{E\Log_qX_{t,n}-E\Log_qX_t^{(u_t,n)}\}\) | tangent norm, with separate level and \(u\)-derivative norms | HD1-A A5-0/A5-1 and Lemma 5.1; HD1-C Section 4 | M-B, M-D/PF, target comparison only if target is changed | level \(O(n^{-a})\); derivative \(O(n^{-a}/b_n)\), improved to \(O(n^{-a})\) only under A5-1 | define \(\delta_{S,0,n}=\sup\|D_{j,n}\|_T\) and, if a derivative route is used, \(\delta_{S,1,n}=\sup\|\nabla_uD_{j,n}\|_T\). No automatic \(R_n n^{-a}\) or \(n^{-a}\) rate | BW metric coupling must imply a BW score defect after alignment; raw matrix norm or another metric's distance is not enough | BASE PROVED; HE OPEN; BW OPEN | The deterministic sign-of-kernel-derivative construction attains \(n^{-a}/b_n\). Smooth proxy laws do not control the triangular-array discrepancy |
| TUBE: generated-set localisation | event \(\mathcal T_n\) that raw observations, population and empirical scale means, Richardson/blend images, chords, connectors/lifts, reconstructed observations, and every comparison surface lie in one controlled domain | metric distance plus spectral/rank/alignment margins; this is an event, not an untyped norm rate | HD1 A1/HD-G, PF; APP-A generated-band audit | every differential, Log, Hessian, connector, and frame lemma | probability \(1-o(1)\) under an a.s. bounded tube and PF nodal control; \(\max_j e_j=O_p(\ell_n^{2/3})\) for \(M_n\asymp\ell_n^{-2/3}\) | must state a tube radius \(\rho_n^{\rm geo}\), all derivative constants on it, and a closure probability. If the observation radius grows like \(R_n\), uniform geometry cannot be inferred from the old fixed tube | primary BW obligation: lower eigenvalue/rank margin, uniqueness/alignment margin, and closure of **all generated images**, not only raw SPD/PSD data | BASE PROVED; HE OPEN; BW OPEN | Hadamard plus fixed radius does not give uniform constants: curvature \(-K_n\), \(K_n\to\infty\), blows up the Hessian. In scalar diagonal BW, positive stage means can still have a signed Richardson combination outside the positive square-root orthant unless closeness is proved |
| M-D / PF: derivative or polygonal-frame input | optional derivative \(\nabla_u\Log_{\mu_n}\widehat\mu_n^{(3)}\); canonical consumer instead uses grid RMS \(((M_n+1)^{-1}\sum_j e_j^2)^{1/2}\) and polygonal area \(\sum_j[M_n^{-1}(e_j+e_{j+1})+e_j^2+e_{j+1}^2]\) | derivative \(L^2(du;T)\); grid RMS tangent distance; frame operator norm | HD1-A Theorem G1'-HD; HD1 Theorem PF; HD1-B B6''' | feasible centre/frame and observation error | derivative \(b_n^3+(nb_n^3)^{-1/2}+n^{-a}/b_n+(nb_n)^{-1}\); canonical PF frame \(O_p(\ell_n)\) | preferred HE route: prove grid RMS \(r_{\mu,n}\), choose \(M_n\) after all constants are known, and obtain \(r_{F,n}\le \mathfrak C_{R,n}\{L_{\mu,n}r_{\mu,n}+M_nr_{\mu,n}^2+M_n^{-2}\}\). Do not assume \(M_n\asymp r_{\mu,n}^{-2/3}\) is optimal if \(\mathfrak C_{R,n}\), \(L_{\mu,n}\), or energy grows | prove a BW polygonal/horizontal-lift analogue, or replace the frame estimator. AIRM PT/ribbon identities are unavailable by analogy | BASE PROVED; HE OPEN; BW OPEN | A width-\(b_n\) blend costs \(b_n^{5/2}\) in derivative \(L^2\). RMS on an arbitrary continuum does not imply deterministic-grid RMS or tube closure without the pointwise second-moment argument |
| LOG: base-point recentering | \(\Phi_{e_t}^{-1}\Log_{\widehat\mu_t}X_t-Y_t=-H_te_t+r_t\), \(\|r_t\|_T\le J\|e_t\|_T^2\) | tangent norm at the true base after radial connector; RMS over \(t\) | HD1-B (4.1); APP-B Lemma APP-B1 | feasible observation error and the two linear mean lag terms | \(O_p(\ell_n)\) robustly; quadratic only under separate cancellation conditions | define \(q_{{\rm Log},n}\le H_{*,n}r_{\mu,n}+J_n r_{\mu,n}^2\). Both \(H_{*,n}\) and \(J_n\) must be exposed on the HE tube; they need not be \(O(1)\) | BW base-point Log/lift Taylor expansion with an explicitly unique Log/alignment and uniform fixed-size \(C^2\) remainder on the generated set | BASE PROVED; HE OPEN; BW OPEN | Cross-fitting alone does not kill \(H_te_t\): the bounded hyperbolic Markov example has a nonzero first derivative. Flatness makes \(H=I\) but does not centre data-dependent \(e_t\) |
| CON: endpoint connectors / anchor identification | connector-typed difference between the true-frame and estimated-frame maps after removing one common anchor isometry \(Q_n\); schematically \(C_{t,n}=Q_n^*\widehat P_{t\to0}\Phi_{e_t}-P_{t\to0}\) | operator norm between the now-common tangent spaces; vector effect \(\|C_{t,n}Y_t\|_T\) | HD1 PF and OBS; APP-A connector calculus | feasible observation error and subspace comparison convention | contained in \(O_p(\ell_n)\) frame/observation rate; one common rigid \(Q_n\) is exact conjugation | expose \(c_{{\rm end},n}=\sup_t\|C_{t,n}\|_{\rm op}\); its observation cost is \(R_n c_{{\rm end},n}\). A common rigid rotation is aligned away; residual time variation is not | unique BW endpoint comparison map or horizontal lift, with a stated gauge/alignment. If the lift is only defined up to an orthogonal action, prove gauge invariance or fix a measurable unique gauge | BASE PROVED; HE OPEN; BW OPEN | Subtracting vectors in different tangent spaces is ill-typed. Charging a common rigid rotation through Davis--Kahan is also wrong; failing to remove a time-varying residual is equally wrong |
| FR/HOL: non-rigid frame and ribbon holonomy | after best common alignment, \(R_t=I+\Omega_t+O(\Omega_t^2)\), \(\Omega_t^*=-\Omega_t\); lag coefficient \(N_h^{-1}\sum_t(\Omega_t\Gamma_{t,h}-\Gamma_{t,h}\Omega_{t-h})\) | \(\Omega_t\) in operator norm; coefficient in direct-sum HS norm \(\phi_{F,n}\) | APP-B Sections 2--4; HD1 PF; APP-A ribbon audit | feasible lag row | robust vector/frame contribution \(O_p(\ell_n)\); exact flat gives zero | vector cost \(R_nr_{F,n}\); row coefficient must be bounded by \(G_{2,{\rm HS},n}r_{F,n}\), where \(G_{2,{\rm HS},n}^2=\sum_h\sup_t\|\Gamma_{t,h}\|_{\rm HS}^2\), not by \(A_{2,n}r_{F,n}\) without a rank bound | BW lift/connection holonomy coefficient in the chosen quotient gauge, or a replacement estimator that avoids it. Prove whether the residual acts as one common conjugation or a time-varying nuisance | BASE PROVED; HE OPEN; BW OPEN | GLO and cross-fitting do not kill frame terms. APP-B CE-B5 gives a first-order commutator. The invalid transfer \(\|\Gamma\|_{\rm HS}\lesssim\|\Gamma\|_{\rm op}\) hides rank/dimension |
| O-S: oracle lag-product concentration | \(d_{{\rm or},n}^2=\sum_{h\le h_0}\|N_h^{-1}\sum_t\{Y_t\otimes Y_{t-h}-E(Y_t\otimes Y_{t-h})\}\|_{\rm HS}^2\) | direct-sum HS norm | HD1-B Theorem B3; APP-C C-PD4 | total lag-row error | \(O_p(n^{-1/2})\) for fixed memory/lag and bounded total energy | variance-sensitive \(O_p([\sum_h(\Theta^{W_h}_{2,n})^2/n]^{1/2})\); envelope fallback \(O_p(R_n^2\sqrt{h_{0,n}(m_n+h_{0,n}+1)/n})\). Product moments and product-process dependence are separate assumptions | identical Hilbert--Schmidt theorem after BW observations are represented in one fixed anchor tangent/lift Hilbert space; geometry supplies no concentration by itself | BASE PROVED; HE OPEN; BW statistical input OPEN | Trace/second moment alone does not close lag products: the paired heavy-tail example has finite \(E\|Y\|^2\) and infinite product variance. Coordinatewise physical dependence hides a dimension sum |
| COMP: feasible versus oracle row | for \(\zeta_t=Q_n^*\widehat Y_t-Y_t\), \(N_h^{-1}\sum_t[(Y_t+\zeta_t)\otimes(Y_{t-h}+\zeta_{t-h})-Y_t\otimes Y_{t-h}]\) | per-lag HS, then direct-sum HS/op | HD1-B Lemma B6'; canonical P1-ROW | lag-row \(d_n\) | \(\le\sqrt{h_0}(2Rq_n+q_n^2)=O_p(\ell_n)\) | exact moment form is \(q_{t,h}R_{2,t-h}+R_{2,t}q_{t-h}+q_{t,h}q_{t-h}\), with empirical RMS energies retained. Under an a.s. envelope it becomes \(\sqrt{h_{0,n}}(2R_nq_{R,n}+q_{R,n}^2)\). Split Log, endpoint, and frame contributions before claiming cancellation | same pathwise rank-one expansion in a common BW anchor representation; first prove the representation, lift/gauge alignment, and \(q_{{\rm BW},n}\) | BASE PROVED; HE OPEN; BW OPEN | Feasible transformed rows need not preserve short memory, so concentrating them directly without proof is invalid. The robust comparison is pathwise and concentrates only the oracle row |
| LN: included-lag population contamination | \(D_n(h)=\Gamma_n(h)-A_nC_{f,n}(h)A_n^*\), \(\zeta_n^2=\sum_h\|D_n(h)\|_{\rm op}^2\) | direct-sum operator norm; optional HS budget must not be substituted | HD1-B Theorem B1 and APP-B/C contamination lemmas | target range, actual eigengap, assembly, factor selection | zero under HD-L; otherwise population-operator defect \(2A_{2,n}\zeta_n+\zeta_n^2\) | retain \(\zeta_n\), \(A_{2,n}\), and the actual contaminated gap. Pervasive signal plus coloured noise is safe only if the target rotation and beyond-rank contamination meet their displayed gap/threshold scales | define the BW tangent lag target after the selected transport/lift; preliminary covariance-estimation error is a separate contribution to \(D_n(h)\), not geometry | BASE PROVED under exact LN; HE/BW target assumptions OPEN | A weak outside-loading coloured component can dominate a localised factor. Under contamination, \(\Delta_n\ge s_n^2\) need not hold and the population rank may exceed \(r\) |
| ASM: lag-operator assembly | \(\widehat{\mathbb L}-\mathbb L=\widehat{\mathcal G}\widehat{\mathcal G}^*-\mathcal G\mathcal G^*\), with \(A_{2,n}^2=\sum_h\|\Gamma_n(h)\|_{\rm op}^2\), \(d_n^2=\sum_h\|\widehat\Gamma_n(h)-\Gamma_n(h)\|_{\rm op}^2\) | operator norm | HD1-B Lemma B6; HD1 P1-OP | Davis--Kahan and nonzero eigenvalues | \(\eta_n\le2A_{2,n}d_n+d_n^2\) | same exact algebra, with \(A_{2,n}\), \(h_{0,n}\), and \(d_n\) visible. Do not simplify to \(O(d_n)\) unless \(A_{2,n}=O(1)\) is proved | unchanged Hilbert-space algebra after the BW row is well-defined | PROVED algebraically for all programmes | Replacing \(A_{2,n}\) by a leading singular value, a gap, or an HS quantity changes the theorem. Growing signal can make assembly larger even while it makes the gap larger |
| DK: loading perturbation | leading eigenspaces of \(\widehat{\mathbb L}\) and \(\mathbb L\) with \(\Delta_n=\lambda_r(\mathbb L)-\lambda_{r+1}(\mathbb L)\) | loading-subspace operator norm | Davis--Kahan as used in HD1-B Theorem B8 | loading theorem | \(\|\sin\Theta\|_{\rm op}\lesssim\eta_n/\Delta_n\) | unchanged: require \(\eta_n=o(\Delta_n)\). Replace by \(s_n^{-2}\) only after proving \(\Delta_n\ge s_n^2\) for the exact included-lag factorisation | unchanged once the BW population and empirical operators act on the same anchor Hilbert space | PROVED algebraically; HE/BW inputs OPEN | Davis--Kahan never pays \(\Delta_n^{-2}\). A large first singular direction does not imply a lower bound on the \(r\)-th gap |
| EV/SEL: beyond-rank eigenvalues and factor selection | \(\widehat\lambda_{r+1}=s_{r+1}(\widehat{\mathcal G})^2\); threshold \(\widehat r=\#\{j:\widehat\lambda_j>\tau_n\}\) | scalar eigenvalues, but producer uses lag-row operator norm | HD1-B Theorems B9--B12 | factor-number theorem | \(\widehat\lambda_{r+1}\le d_n^2\); require \(d_n^2=o_p(\tau_n)\), \(\tau_n=o(\Delta_n)\), \(\eta_n=o_p(\Delta_n)\) | same square only relative to a rank-\(r_n\) population row. If LN contamination is included in the population target, rank may exceed \(r_n\); instead compare to the clean rank-\(r_n\) row and include \(\zeta_n\) in total row error. Growing-rank selectors also need a search and internal-spectrum condition | same algebra after BW lag target/rank is proved; no geometry-specific shortcut | PROVED algebraically under exact rank; HE/BW rank/target inputs OPEN | Weyl alone gives only first order. The raw eigenvalue ratio over-selects for \(\operatorname{diag}(1,d_n^2,0)\); use threshold or ridge |

## 2. The exact four first-order nuisance terms

After one common anchor rotation is removed, every proposed HE or BW feasible observation theorem must reduce to a typed analogue of

\[
U_t=Y_t-H_te_t+\Omega_tY_t+\xi_t^{(2)},
\qquad
\|\xi_t^{(2)}\|_T
\lesssim \|e_t\|_T^2+\|e_t\|_T\|\Omega_t\|_{\rm op}
+\|Y_t\|_T\|\Omega_t\|_{\rm op}^2.
\]

The four linear lag-product channels are

\[
-H_te_t\otimes Y_{t-h},\qquad
-Y_t\otimes H_{t-h}e_{t-h},
\]

\[
+\Omega_tY_t\otimes Y_{t-h},\qquad
+Y_t\otimes\Omega_{t-h}Y_{t-h}.
\]

No programme may call the feasible comparison quadratic until it has separately eliminated or centred all four channels. For HE, their envelope size grows with \(R_n\) and possibly the Hessian/frame constants. For BW, the very definitions of \(H_t\), \(\Omega_t\), and their common anchor representation are open until the fixed-size calculus and lift/gauge choice are complete.

In particular, the minimum HE bookkeeping is

\[
r_{\mu,n}=\left(n^{-1}\sum_t\|e_t\|_T^2\right)^{1/2},
\qquad
r_{F,n}=\sup_t\|C_{t,n}^{\rm nonrigid}\|_{\rm op},
\]

\[
q_{R,n}\le C_{{\rm Log},n}r_{\mu,n}+R_nr_{F,n}
+q_{{\rm conn},n}+q_{{\rm quad},n},
\qquad
d_{{\rm comp},n}\le\sqrt{h_{0,n}}(2R_nq_{R,n}+q_{R,n}^2).
\]

The first display concerns centre and frame estimation; the second concerns feasible tangent observations and lag rows. They may not be collapsed into one symbol before each producer is proved.

## 3. HE dependency ledger and pre-audit

| Node | Exact producer obligation | Consumer | Current status | Hostile checkpoint |
|---|---|---|---|---|
| HE-0 typed assumptions | separate score moments/tails, product moments/tails, score/product dependence, tube geometry, rank/lag growth, target contamination, \(A_{2,n}\), \(\Delta_n\) | every HE result | OPEN -- EXACT LEDGER REQUIRED | An a.s. \(R_n\) envelope may be sufficient but is not minimal. Any weaker moment route must state truncation bias and high-probability tube control |
| HE-1 mean bias/localisation | prove \(\mathfrak B_{3,n}\), strong convexity/localisation, and generated-tube event | HE mean and grid | OPEN | Do not scale only the empirical score by \(R_n\); the population derivatives and tube radius may grow |
| HE-2 score concentration | Hilbert weighted inequality with \(V_{S,n}\), \(\Theta^S_{2,n}\), and a tail budget for the sup theorem | empirical mean | OPEN | Coordinatewise physical-dependence coefficients must be aggregated in Hilbert norm; otherwise a hidden \(\sqrt{p_n}\) reappears |
| HE-3 grid and polygonal frame | deterministic-grid RMS, controlled vertex maximum, area/holonomy with growing constants, endpoint connectors | \(q_{R,n}\) | OPEN | Choosing \(M_n\asymp r_{\mu,n}^{-2/3}\) before exposing geometry/energy constants is unjustified |
| HE-4 oracle product row | direct-sum HS concentration with variance-sensitive product budget and growing lag/dependence factors | HE lag row | OPEN | Second moments of \(Y\) alone do not imply second moments of \(Y_t\otimes Y_{t-h}\) |
| HE-5 feasible row | pathwise typed expansion of Log, connector, frame, and quadratic errors; exact definition of \(q_{R,n}\) | \(d_n\) | OPEN | The term \(2R_nq_{R,n}+q_{R,n}^2\) is only an envelope corollary; do not hide \(\sqrt{h_{0,n}}\) |
| HE-6 clean target and contamination | prove rank/range of the clean lag row and quantify \(D_h\) | signal, gap, factor selection | OPEN | Pervasive factors do not protect against outside-loading coloured contamination unless the rotation defect is small relative to the actual gap |
| HE-7 assembly/loading | insert the proved \(d_n\) into \(2A_{2,n}d_n+d_n^2\) and require \(o(\Delta_n)\) | headline loading theorem | algebra PROVED; rate substitution OPEN | It is possible for both \(A_{2,n}\) and \(\Delta_n\) to grow; compare their exact powers rather than cancelling them informally |
| HE-8 factor number | prove rank-row square and a nonempty threshold/ridge window | selector | algebra PROVED; phase window OPEN | If \(r_n\) grows, the minimum signal and internal spectrum may collapse even with large total lag energy |
| HE-9 phase models | exhibit explicit DGPs satisfying every prior node in localised, pervasive, preserved-normalisation, diluted-normalisation, matrix, and growing-rank regimes | HE conclusions/applications | OPEN | A rate table without an attainable DGP is not closure |

### HE analytic attacks already available from canon

1. **Coordinatewise control without total/product control -- DISPROVED.** Independent Rademacher coordinates have \(\|Y\|=\sqrt{p_n}\), score RMS \(\sqrt{p_n/(nb_n)}\), and can produce lag-operator fluctuations of order \(p_n/\sqrt n\).
2. **Growing energy with fixed gap -- impossibility boundary.** Under the envelope benchmark, \(d_{\rm or,n}\gtrsim R_n^2/\sqrt n\) in worst-case product-variance models. With \(A_{2,n},\Delta_n\asymp1\), consistency cannot be guaranteed unless this and the feasible terms vanish. This is a worst-case boundary, not a universal lower bound for variance-sensitive models.
3. **Global normalisation of a localised factor -- DISPROVED.** Dividing by \(\sqrt{p_n}\) can send a fixed factor lag to \(p_n^{-1}\) and the lag-operator gap to \(p_n^{-2}\).
4. **Pervasive signal plus coloured idiosyncratic lag -- target failure.** A bounded outside-loading serial component can create a competing population eigen-direction. Strengthening the factor does not prove exact target recovery; the defect must be compared with the actual gap.
5. **Coordinatewise physical dependence -- hidden dimension.** Coordinatewise summability does not imply a bounded Hilbert coefficient sum. The HE theorem must use Hilbert/HS coefficients or display their aggregate.
6. **Growing rank with insufficient lag energy.** Under bounded factor energy, \(\Delta_n\le h_0R_f^4/r_n\); growing rank forces some signal to weaken. With growing energy, the corresponding trace budget must remain explicit.

## 4. BW dependency ledger and fixed-size gate

No growing-matrix-size BW claim may be audited as a theorem until BW-F1 through BW-F9 below are closed for a fixed matrix size.

| Node | Exact producer obligation | Consumer | Current status | Hostile checkpoint |
|---|---|---|---|---|
| BW-F1 domain | choose SPD, one fixed-rank PSD stratum, or quotient; state metric, tangent norm, Exp/Log domain, horizontal lift/alignment, and quantitative boundary margins | every BW node | OPEN -- EXACT DEFINITIONS REQUIRED | Mixing SPD and PSD formulas, or changing rank mid-proof, invalidates all subsequent maps |
| BW-F2 uniqueness | prove uniqueness/measurability of population/local means, Log, optimal alignment/lift, and any gauge choice on the selected domain | estimator definition | OPEN | On SPD, repeated eigenvalues alone should not be called nonuniqueness if invariant square-root/polar formulas remain unique. The real obstruction must be tied to singular cross-Gram/rank loss or a specific quotient stabiliser |
| BW-F3 generated closure | show every scale mean, Richardson/blend image, chord, connector/lift, reconstructed point, and comparison surface stays inside the regular domain with probability \(1-o(1)\) | differential calculus and estimator existence | OPEN | Raw-data spectral bounds do not imply closure. Negative Richardson coefficients are a direct danger even in scalar square-root coordinates |
| BW-F4 score/Hessian | derive the BW squared-distance score, observation Hessian, coercivity/strong convexity, and fixed-size derivative bounds on the generated set | G1/Sturm replacement and Log recentering | OPEN | BW is not globally Hadamard; the canonical Sturm minorant cannot be imported by name |
| BW-F5 Exp/Log/alignment calculus | fixed-size base-point/vector derivatives and alignment/horizontal-lift derivatives through the order actually consumed | bias, Log Taylor, connectors | OPEN | Eigenvector-by-eigenvector differentiation can introduce fake spectral-gap denominators. Use invariant matrix equations where possible; otherwise state the real multiplicity margin |
| BW-F6 frame/replacement | prove a BW Levi-Civita/polygonal frame theorem, horizontal-lift comparison, or a redesigned estimator avoiding unavailable transport maps | feasible observations | OPEN | Calling an optimal alignment “parallel transport” without an identity is invalid. A time-varying gauge residual may act on the signal like \(\Omega_t\Gamma_h-\Gamma_h\Omega_{t-h}\) |
| BW-F7 mean/grid theorem | positive three-scale fixed-size mean existence, bias, score rate, arbitrary-grid RMS, and tube event; specify a localised empirical minimiser if global uniqueness is not proved | BW-F6 and feasible row | OPEN | Diagonal fixed-basis flatness proves only a special case. A local strong-convexity argument does not justify an unqualified global `argmin` |
| BW-F8 lag target | define anchor tangent observations and prove the exact included-lag factorisation/contamination budget in the BW tangent norm | gap and factor number | OPEN | A covariance time series is the scientific observation. A preliminary covariance estimator from raw returns adds measurement error/dependence and cannot be silently absorbed |
| BW-F9 fixed-size lag/loading theorem | oracle row, feasible comparison, assembly, actual gap, loading, and threshold/ridge selector | fixed-size BW verdict | OPEN | The statistical algebra can be reused only after the BW anchor representation is proved |
| BW-G1 constant audit | expose every fixed-size constant as a function of \(m_n\), tangent dimension, eigenvalue/rank margins, alignment margin, and generated radius | growing-size BW | BLOCKED BY FIXED-SIZE GATE, not a final blocked status | A fixed-size compactness proof gives no growth rate |
| BW-G2 HE intersection | combine the completed BW constant audit with the completed HE energy/signal inequalities | growing-energy/growing-size BW corollary | NOT YET ADMISSIBLE | The intersection may be empty; do not merge notation or assumptions before both ledgers close |

### BW analytic boundary attacks available now

1. **Generated-set failure from Richardson extrapolation.** In scalar diagonal BW, write the SPD coordinate as \(r=\sqrt a>0\). The three-scale combination uses \(r_R=(1/3)r_1-2r_2+(8/3)r_3\). Positive \(r_j\) do not imply \(r_R>0\); for \((r_1,r_2,r_3)=(1,10,1)\), \(r_R=-17\). The actual theorem may avoid this by proving the three stages are sufficiently close, but positivity of raw data or stage means alone is insufficient.
2. **Boundary distance and energy are separate.** Even on a fixed spectral band, \(d_{\rm BW}^2(I,cI)=m(1-\sqrt c)^2\). Conditioning does not bound total BW energy as \(m\to\infty\).
3. **Rank loss destroys regular quotient calculus.** At singular PSD matrices, cross-Gram/polar factors can lose invertibility and quotient stabilisers can enlarge. Any claimed alignment derivative must show a quantitative singular-value margin.
4. **Multiplicity is not automatically a defect.** Repeated eigenvalues may break eigenvector-coordinate formulas while invariant matrix square roots remain smooth on SPD bands. A hostile audit will reject either an unnecessary eigengap assumption or a missing genuine alignment margin.
5. **Moving eigenvectors are not a fixed diagonal algebra.** Pointwise diagonalisation does not put the path, support, means, and generated images in one common square-root flat.
6. **Preliminary covariance estimation is an extra layer.** Overlapping windows create dependence and lag contamination before the BW model begins. The geometric theorem cannot call those matrices noise-free observations unless that is its declared input model.

## 5. Assumption-to-consumer reach audit

| Assumption or property | What it actually reaches | What it does not reach |
|---|---|---|
| Bounded/growing tangent envelope \(R_n\) | score and rank-one product envelopes; pathwise feasible comparison | mean bias constants, tube closure, dependence, clean target, or eigengap |
| Score second moment / score PD budget | M-S and hence empirical mean | lag-product concentration or sample splitting |
| Product second moment / product PD budget | oracle lag row | mean localisation or generated geometry |
| Uniform geometry/tube constants | bias/Taylor/frame bounds | bounded energy, concentration, LN, GLO, or signal |
| Exact finite-memory split | conditional training/evaluation independence | GLO mean coefficient or non-rigid frame coefficient |
| GLO / joint reflection | two mean-linear population coefficients | frame terms, oracle sampling, or LN |
| Flat/common fixed algebra | zero geometric remainder and non-rigid frame after common alignment | centring of data-dependent additive mean errors |
| Local symmetry | differential simplification and Hessian parity | flatness, GLO without joint law symmetry, or holonomy zero |
| Spectral band / lower eigenvalue margin | matrix functional-calculus constants and boundary avoidance, if generated closure is proved | total energy, lag orthogonality, dependence, or signal |
| Exact LN | clean population range and \(\Delta_n\ge s_n^2\) corollary under full-rank lag | feasible mean/frame errors |
| Large/pervasive signal | possibly large \(A_{2,n}\) and \(\Delta_n\) | small assembly ratio unless their relative powers are computed; no protection from target mismatch by itself |
| Root-\(n\) centre | oracle **order** of nuisance perturbation | oracle equivalence or coefficient cancellation |
| BW optimal alignment | a pointwise comparison map, once unique | Levi-Civita parallel transport, frame holonomy control, or time-consistent gauge by assertion |

## 6. Norm-transfer and dimension traps to check in both hostile passes

1. \(\|A\|_{\rm op}\le\|A\|_{\rm HS}\) is valid; the reverse costs \(\sqrt{\operatorname{rank}A}\) and cannot be used silently.
2. A direct-sum HS row bound implies a direct-sum operator row bound, but an operator row bound does not imply an HS frame coefficient without a rank budget.
3. For \(m\times m\) full symmetric tangents, \(p=m(m+1)/2\), not \(m\). A Frobenius energy of order \(m\) or \(m^2\) must not be described as “dimension free.”
4. A spectral operator-norm band can coexist with Frobenius distance \(\asymp\sqrt m\). Matrix conditioning is not energy.
5. Lag aggregation costs at least the displayed direct-sum norm; fixed \(h_0\) may be hidden only in the bounded-energy baseline, never in HE/growing-lag claims.
6. Davis--Kahan consumes the actual self-adjoint operator gap once. The square \(s_n^2\) belongs to the lag-factor-to-operator comparison, not to a second perturbation step.
7. The beyond-rank square is a singular-value statement about the lag row. It disappears if the chosen population row is not rank \(r\).

## 7. Pre-audit objection table

This is the required objection table. Rows will be amended, not replaced, when the HE and BW dossiers arrive.

| Claim | Attack | Resolution | Final status | Canonical consequence |
|---|---|---|---|---|
| “HE follows by replacing \(R\) with \(R_n\) in stochastic terms” | M-B, TUBE, LOG, CON, and FR have geometry/law constants that may grow independently of the score envelope | Require a complete \(q_{R,n}\) derivation with bias, localisation, connectors, frame, and dependence constants exposed | OPEN -- EXACT LEMMAS STATED IN Sections 1 and 3 | No HE theorem or application remapping yet |
| “Trace/second-moment control is enough for the HE oracle row” | Paired heavy-tail one-dependent process has finite trace covariance and infinite product variance | Add typed product second moments/tails and dependence for \(Y_t\otimes Y_{t-h}\), or use truncation with bias | DISPROVED as stated | HE assumptions must separate score and product budgets |
| “Coordinatewise dependence is dimension free” | Independent coordinates aggregate to \(\sqrt{p_n}\) in Hilbert norm | Use Hilbert/HS physical-dependence coefficients or display their aggregate | DISPROVED | No coordinatewise-to-Hilbert shortcut enters canon |
| “Pervasive signal cancels growing energy” | Assembly is \(2A_{2,n}d_n+d_n^2\), while the gap is \(\Delta_n\); both can grow at different powers | Prove the exact ratio \((2A_{2,n}d_n+d_n^2)/\Delta_n\to0\) in each DGP | OPEN pending HE phase models | Application claims remain unclassified |
| “The HE loading rate is \(d_n/\Delta_n\)” | Assembly contains \(A_{2,n}\); when signal grows, \(A_{2,n}\) need not be bounded even if \(d_n\to0\) | State the theorem as \((2A_{2,n}d_n+d_n^2)/\Delta_n\), simplifying only under a proved relation among \(A_{2,n},d_n,\Delta_n\) | DISPROVED as an unconditional simplification | No canonical HE rate may hide \(A_{2,n}\) |
| “Normalising by \(\sqrt p\) repairs HE” | Localised-factor gap can shrink as \(p^{-2}\) | Recompute estimand, lag row, \(A_2\), and \(\Delta\) after scaling | DISPROVED as universal | Only preserved-signal normalisations may receive a corollary |
| “Full BW inherits AIRM/Hadamard geometry” | BW has a finite-distance PSD boundary and different alignment/quotient structure | Build BW-F1--F9 independently | DISPROVED | AIRM proof nodes cannot support a BW theorem |
| “Raw BW data in a spectral band imply estimator closure” | Negative Richardson coefficients can leave the positive square-root domain even when all stage points are positive | Prove stage closeness and closure of every generated image, or redesign the estimator | DISPROVED as stated | BW generated-set closure remains a headline gate |
| “Local BW Hessian coercivity defines the empirical mean globally” | A local critical point/strongly convex ball does not exclude other minima outside the ball on a non-Hadamard or quotient domain | Define a localised estimator with a preliminary centre and prove it is interior, or prove global uniqueness on the full generated domain | OPEN -- EXACT BW-F2/F7 | Fixed-size BW theorem must state the estimator actually proved |
| “Repeated eigenvalues automatically make BW alignment nonunique” | Invariant SPD square-root/polar formulas can remain unique and smooth despite multiplicity | Tie every nonuniqueness or derivative blow-up to an actual singular cross-Gram/quotient margin; otherwise remove the fake eigengap | REJECTED as an unqualified claim | BW assumptions must use genuine margins only |
| “An optimal BW alignment is the feasible frame” | Pointwise optimal alignment need not equal parallel transport or form a time-consistent gauge | Prove horizontal-lift/connection identities or redesign the estimator | OPEN -- EXACT BW-F6 | Fixed-size BW theorem not closed |
| “Conditioning controls BW growing-size energy” | \(d_{\rm BW}(I,cI)=\sqrt m|1-\sqrt c|\) | Separate spectral margins from total tangent/root energy | DISPROVED | BW growing-size audit must intersect HE explicitly |
| “A large first lag singular value is the eigengap” | Rank-two \(C_h=\operatorname{diag}(1,\varepsilon)\) has a weak second direction; complementary deficient lags show the converse issue | Use \(\Delta_n=\lambda_r(\mathbb L)-\lambda_{r+1}(\mathbb L)\); invoke \(s_n^2\) only after exact factorisation/full-rank-lag proof | DISPROVED as stated | All loading rates remain in actual-gap form |
| “Weyl proves null eigenvalues are \(d_n^2\)” | Weyl controls the operator perturbation at first order | Use the rank-\(r\) lag-row singular-value min--max argument | DISPROVED as an implication; corrected theorem PROVED | Factor selector must consume the row proof |
| “The raw eigenvalue ratio is consistent” | \(\operatorname{diag}(1,d_n^2,0)\) selects the later zero ratio | Use threshold or ridged ratio with the exact window | DISPROVED | No raw-ratio claim may return |
| Lead edge check: zero signal | If \(C_f(h)=0\) at every included lag, then \(Q_n=0\), \(\Delta_n=0\), and a positive-rank loading space is not identified | Suppress the loading theorem. A selector may return \(r=0\) only under a separately stated null-row threshold window controlling the whole empirical row | DISPROVED for any positive-rank conclusion | Canon must not divide by a zero gap or infer loadings from null lags |
| Lead edge check: zero idiosyncratic noise | Setting \(Y_t=A_nf_t\) removes LN contamination but does not make the moving centre or feasible frame known | Retain M-B/M-S/M-LS, LOG, CON, and FR unless the centre/frame is explicitly supplied | DISPROVED as an oracle shortcut | A noiseless-factor corollary still pays feasible-geometry error |
| Lead edge check: fixed dimension | HE with fixed \(p\), \(R_n=O(1)\), fixed lags/rank/dependence, and bounded geometry must reproduce canonical HD1; any BW growing-size audit with fixed \(m\) must reduce exactly to its already closed fixed-size theorem | Compare every term row by row and reject extra dimension costs or missing canonical defects | REQUIRED REDUCTION CHECK | Prevents a purported extension from contradicting or weakening its base theorem silently |
| Lead edge check: high-dimensional localised background | A fixed serial factor in \(e_1\) plus serially white independent Rademacher background has \(R_n\asymp\sqrt{p_n}\) and fixed population gap, while the sample cross-lag background has HS scale \(p_n/\sqrt n\) and operator scale that does not vanish when \(p_n/n\not\to0\) | The fixed-gap HE theorem needs an explicit dimension/product condition; the envelope sufficient condition requires at least \(p_n/\sqrt n\to0\), while sharper operator analysis must be separately proved | ANALYTIC FIXED-GAP FAILURE REGIME | No blanket “growing energy with fixed gap” consistency claim |
| Lead edge check: explicit pervasive offset | With known centre/frame and \(Y_t=\sqrt{p_n}\,v f_t\), \(\|v\|=1\), fixed-rank serial \(f_t\), one has \(R_n\asymp\sqrt{p_n}\), \(A_{2,n}\asymp p_n\), \(\Delta_n\asymp p_n^2\), and oracle row error \(d_n\asymp p_n/\sqrt n\), so \((2A_2d+d^2)/\Delta=O_p(n^{-1/2}+n^{-1})\) | Use this only as an attainable oracle/statistical phase model; a moving-centre corollary must additionally prove its \(q_{R,n}\) terms satisfy the same ratio | NONEMPTY PERVASIVE ORACLE REGIME; moving-centre extension OPEN | Shows energy can be offset by signal, but only through the exact assembly/gap powers |

## 8. First- and second-pass protocol for incoming dossiers

### First hostile pass

For each HE or BW headline display:

1. expand every \(O_p\) term into the ledger row that produces it;
2. check the norm and the base space at the producer and consumer;
3. expose \(R_n,m_n,p_n,h_{0,n},r_n\), dependence budgets, geometry margins, \(A_{2,n}\), and \(\Delta_n\);
4. verify that every assumption reaches the claimed consumer rather than an adjacent quantity;
5. construct the zero-signal, zero-noise, fixed-dimension, boundary, and high-dimension reductions;
6. enter every objection in Section 7 with a demanded repair or an analytic counterexample.

### Second hostile pass

After repairs:

1. rerun the entire dependency chain from definitions to selectors;
2. reject repairs that merely rename a missing coefficient as an assumption without showing a nonempty model;
3. check that all counterexamples and narrowed scopes have propagated to applications;
4. verify fixed-size BW closure before reading any growing-size conclusion as more than a constant audit;
5. verify the HE--BW intersection by simultaneous inequalities, not prose;
6. permit canonical integration only for rows whose final status is proved, disproved with a corrected theorem, or exactly open with one irreducible lemma.

## 9. Current bottom line for the lead

The canonical bounded-energy chain is internally closed. The active joint ledger identifies no legal shortcut from that chain to either HE or full BW.

- HE's algebraic endgame is already proved, but its mean/tube/frame rate, product concentration, target contamination, and attainable phase models remain open.
- BW must first choose a regular domain and close a fixed-size generated-set/differential/frame theorem. Its statistical row and spectral algebra can be reused only after that representation exists.
- The two programmes must remain independent until those verdicts are fixed. A growing-energy/growing-size BW result is an intersection corollary, not a starting theorem.
- Application remapping and numerical-suite design are downstream and therefore intentionally absent from this pre-audit dossier.

## 10. First hostile pass — completed 2026-08-08

Both complete working dossiers were read from definitions through selectors. Statuses below are provisional until repaired; no canonical edits are authorized.

### HE objections

| Claim | Attack | Demanded resolution | Provisional status | Canonical consequence |
|---|---|---|---|---|
| HE generated closure | HE-G assumes that all raw, population-stage, Richardson, chord, connector, and ruled-surface objects remain in one tube | Derive closure from explicit support/tail and margin conditions, including population proxy objects; otherwise state one exact open lemma | MATERIAL GAP | HE mean/frame and curved phases remain noncanonical |
| Polygon tube condition (2.5) | It says \(\sqrt M,r_\mu=o(\mathrm{margin})\), not \(\sqrt M\,r_\mu=o(\mathrm{margin})\), and omits chord error | Require \(\sqrt M\,r_\mu+K_\mu M^{-2}=o(\mathrm{margin})\) plus the true-curve margin | REPAIR | PF and \(q_R\) are not closed |
| Full \(q_R\) rate | Frame acts on the recentered Log; a \(r_F L_{\log}r_\mu\) cross term and named connector defects are not proved negligible | Add/absorb the cross term on a proved event and rate every defect | REPAIR | Phase substitutions are premature |
| Unbounded-score scope | HE-MEAN assumes a sup-tail budget; no Orlicz/truncation proof or truncation bias is supplied | Keep the explicit tail theorem and mark unbounded-score truncation OPEN — EXACT LEMMA STATED | NARROWED | No minimal-moment claim |
| Product PD producer | The \(W-W^{(k)}\) display leaves an undefined symmetric term and does not fully type the \(k-h\) shift or lag aggregation | Give the exact coupling expansion and constants | REPAIR | Physical-dependence HE-ROW provisional; finite-memory row survives |
| Memory/matrix notation | \(m_n\) denotes both dependence memory and matrix size | Rename the memory sequence | REPAIR | Prevent false growth conditions |
| Flat phase headline | The rate omits \(R_nn^{-a}=n^{-(a-\rho)}\) | State \(n^{-(3-13\rho)/7}+n^{-(a-\rho)}\); require \(a\ge(3-6\rho)/7\) for the balanced exponent | MATERIAL RATE REPAIR | \(\rho<3/13\) is only a sufficient consistency window |
| Curved phase headline | The rate omits \(R_n^2n^{-a}=n^{-(a-2\rho)}\) | State \(n^{-(3-20\rho)/7}+n^{-(a-2\rho)}\); require \(a\ge(3-6\rho)/7\) for the balanced exponent | MATERIAL RATE REPAIR | \(\rho<3/20\) is only a sufficient consistency window |
| Phase completeness | Tube sup rate, \(\sqrt M r_\mu\), geometry/dependence growth, and all \(\rho\)-defects are omitted | Display them as zero or negligible in every phase corollary | DOWNGRADE | HE-PHASE not yet proved |
| Pervasive DGP | Noise centering, coordinate law, cross moments, product budgets, centre, and exact target are not fully specified | Give a complete triangular DGP and verify every HE assumption row | REPAIR | Nonempty phase plausible, not yet proved |
| Coloured-contamination counterexample | It postulates \(\zeta_n=\epsilon_np_n\) instead of constructing a process | Construct an explicit outside-loading serial or factor-noise cross process giving fixed rotation or an extra population factor | REPAIR | Negative result not yet analytic |
| Growing-rank DGP | \(C_f=cI_{r_n}\) is asserted without a full process/product/selector verification | Construct the process and verify \(R,\omega,d,\eta/\Delta\) and selector windows | REPAIR | Growing-rank claim conditional |
| Clean versus contaminated target | \(d_n\) already includes \(\zeta_n\), then the population penalty is presented separately | Define \(d_{\rm samp}\) about the actual row and \(d_{\rm ideal}\le d_{\rm samp}+\zeta\), with separate gaps/ranks | REPAIR | Avoid double counting and wrong-target consistency |
| Lead edges | Zero signal gives \(\Delta=0\); zero noise still leaves centre/frame error; localised high-dimensional Rademacher background can have fixed gap and nonvanishing row error | Add the zero-signal \(r=0\) window, retain feasible geometry under zero noise, and add the explicit high-dimensional failure | REQUIRED | No hidden oracle/fixed-gap shortcut |
| Fixed-dimensional reduction | The extension must recover canonical HD1 when all sequence budgets are bounded | Show \(r_\mu,r_F,q_R,d\) reduce row by row to \(\ell,\ell,\ell,n^{-1/2}+\ell\) | REQUIRED | Base theorem consistency check |
| HE file integrity | Embedded carriage returns from \(\rho\), a backspace from \(\bar\), zero valid inline delimiters, and stripped LaTeX commands were detected | Rewrite and scan all C0 controls/LaTeX | MATERIAL FILE DEFECT | Not integration-ready |

### BW objections

| Claim | Attack | Demanded resolution | Provisional status | Canonical consequence |
|---|---|---|---|---|
| BW-G3 / BW-DIFF-FIX | BW-G3 assumes the bounded derivatives that BW-DIFF-FIX then proves by compactness | Remove the circular assumption and derive the fixed-size maps from regular square-root, polar, Sylvester, and ODE primitives | MATERIAL CIRCULARITY | Fixed-size mean/PF/loading remain provisional |
| Complete generated set | Proxy-law support, population smoothed stages, constraint geodesics, and all score/Hessian pairs are not explicitly covered | Add and prove margins for every producer object | REPAIR | Mean proof has a reach gap |
| Constrained stage uniqueness | \(\overline{\mathcal D_0}\) is not stated geodesically convex and the Hessian margin is not proved along all internal geodesics | Require a compact geodesically convex local domain and interior population-stage margin | REPAIR | Stage argmin not closed |
| Richardson safeguard | (3.4) proves invertibility only, not membership in \(\mathcal D_1\), \(\mathcal N\), or later Hessian/connector/ruled margins | Safeguard full regular-domain membership on one uniform event | MATERIAL GAP | BW-2 remains open |
| Chord/blend closure | “Unique geodesic convexity” is invoked without a declared convex regular set | Prove the exact convex set or add path membership tests/fallbacks | REPAIR | BW-PF not closed |
| Equality to original estimator | Inactive Richardson fallback does not make the constrained local stage argmin equal the original global unconstrained argmin | Prove global localisation/uniqueness or retract equality and call it a localized replacement | RETRACT CLAIM | Canon must state the estimator actually proved |
| Endpoint typing | The empirical and population lag operators are subtracted without explicitly defining the anchor-connector conjugation | Define aligned vectors/row/operator and separate common gauge from non-rigid residual | REPAIR | Loading subtraction otherwise ill-typed |
| Fixed-size BW theorem | It consumes the circular calculus and incomplete closure/convexity inputs | Repair those nodes and rerun the dependency chain | NOT CLOSED | BW-4 PROVED is premature |
| Fixed-margin growing-\(m\) calculus | The “differentiate inductively” sketch does not prove uniform PT/ODE derivatives, curvature, Hessian, Richardson, or ruled-surface constants | Downgrade to OPEN — EXACT LEMMA STATED unless a complete typed matrix/ODE derivation is supplied | MATERIAL GAP | No growing-size BW theorem yet |
| Shrinking margin is the only open size node | Fixed-margin calculus is also unproved at the required detail | Split the two open obligations | STATUS REPAIR | Section 9.2 cannot enter canon |
| HE×BW condition (10.1) | It hides producer constants, omits \(d^2\), and divides by \(A_2\) unsafely | Use the exact HE ledger and require \(2A_2d+d^2=o(\Delta)\) after closure | MATERIAL REPAIR | No noncommuting intersection |
| Diagonal HE intersection | Flat root coordinates alone do not verify boundary, product dependence, target, gap, or a DGP | Give explicit HE inequalities and a positive-root DGP | REPAIR | Candidate only, not classified theorem |
| Repeated positive spectra | Invertible polar/square-root maps remain unique; multiplicity is not the obstruction | Retain the dossier’s rank-loss/singular-lift correction | ACCEPT | No fake eigenvalue-gap margin |
| Global rank-changing PSD | Orthogonal rank-one endpoints yield nonunique alignments/geodesics/midpoints | Retain the analytic counterexample and full-rank local scope | ACCEPT NEGATIVE | Global PSD theorem disproved |
| Raw band closure | Scalar Richardson can hit rank zero | Retain counterexample; strengthen safeguard as above | ACCEPT NEGATIVE / REPAIR | Closure remains load-bearing |
| Lead edges and reduction | Zero signal gives \(\Delta=0\); zero noise leaves geometry; future growing-\(m\) result must reduce to repaired fixed \(m\) | Add explicit checks | REQUIRED | No spectral/geometry shortcut |
| BW file integrity | No C0 corruption was found; delimiters are present | Recheck cross-references after repair | PASS WITH RECHECK | Readable but provisional |

### First-pass verdict

- HE row concentration, pathwise comparison, assembly, actual-gap perturbation, and selector algebra survive. The theorem/phase/DGP/closure claims above require repair.
- BW full-rank quotient definitions, the multiplicity correction, Richardson escape, and rank-changing PSD counterexample survive. Fixed-size and growing-size theorem claims do not yet close.
- No canonical integration, application remapping, archival, HE×BW theorem, numerical-suite design, or second hostile pass is authorized yet.

## 11. Second hostile pass — completed 2026-08-08

Both repaired dossiers were reread from primitive definitions through their final loading and selector consumers. Every first-pass response was attacked again against the typed ledger. No canonical file was edited.

### 11.1 Objection-by-objection closure

| Claim | Second-pass attack and resolution | Final status | Canonical consequence |
|---|---|---|---|
| HE generated-set closure | HE-G0 now states nested primitive domains, support/proxy coverage, margins, and stage conditions; HE-CLOSURE derives empirical Richardson, blend, chord, connector, and ruled-surface membership. The flat Euclidean DGP is a nonempty model, so this is not a renamed empty assumption. | **CLOSED — PROVED UNDER EXPLICIT ASSUMPTIONS** | May integrate the conditional closure theorem; preserve every primitive margin. |
| HE polygonal tube and frame | The tube uses \(\sqrt{M_n}r_{\mu,n}+K_{\mu,n}M_n^{-2}=o(\delta_n)\). The frame row retains \(L_\mu r_\mu\), \(M_nr_\mu^2\), discretisation, and geometry constants. | **CLOSED** | No malformed \(\sqrt M\) condition or hidden frame constant may return. |
| HE feasible observation | The repaired rate separates centre error and frame error and contains the cross term: \(L_{\log}(r_\mu+K_\mu M^{-2})+r_F(\mathcal E_2+L_{\log}r_\mu)+\rho_{\rm con}+\rho_{\rm obs}\). | **CLOSED** | Canon must not collapse \(q_R\) to centre error alone. |
| HE unbounded scores | HE-TRUNC states the exact simultaneous tail, truncation-bias, product, and domain obligations and is consumed by no proved theorem. | **OPEN — EXACT LEMMA STATED** | Integrate only the bounded-tail theorem; archive HE-TRUNC as an open extension. |
| HE lag producers | Finite-memory and causal physical-dependence rows now use Hilbert/HS budgets, an exact product coupling including the shifted coefficient, and explicit lag aggregation. | **CLOSED — PROVED** | No coordinatewise or trace-moment shortcut. |
| HE target and assembly | Actual-row sampling error and ideal-row contamination are separated. Every loading theorem uses matching \((d^T,A_2^T,\Delta^T)\) and \(\eta^T=2A_2^Td^T+(d^T)^2\). | **CLOSED — PROVED** | Never replace \(\eta/\Delta\) by \(d/\Delta\) without a proved \(A_2\) bound. |
| HE phase rates | LS competitors are present: flat \(n^{-(3-13\rho)/7}+n^{-(a-\rho)}\), curved \(n^{-(3-20\rho)/7}+n^{-(a-2\rho)}\), with the stronger balanced-rate condition stated separately. | **CLOSED — SUFFICIENT ENVELOPE REGIMES** | Integrate as sufficient, not minimax, phase windows. |
| HE nonempty regimes and counterexamples | Fully specified pervasive and growing-rank bounded DGPs verify the row, \(A_2\), gap, assembly, and selector windows. Explicit coloured contamination and localized-background constructions prove the negative claims. | **CLOSED — PROVED / DISPROVED AS LABELLED** | Positive and negative regimes may enter canon with their exact targets. |
| BW quotient and alignment | Square-root, polar, horizontal projector, Log/Exp, connection, and typed PT are derived on full-rank primitive domains. Repeated positive eigenvalues do not cause nonuniqueness; singular cross matrices/rank loss do. | **CLOSED FOR FIXED \(m\)** | Require zero-singular-value margins, not spectral-multiplicity gaps. |
| BW localized mean | The estimator is the constrained minimizer on a compact strongly geodesically convex domain, with Hessian control along every internal consumer pair and population stages uniformly interior. Equality to the original global argmin is retracted. | **CLOSED — CORRECTED ESTIMATOR PROVED** | Canon must name the localized replacement estimator. |
| BW generated-domain event | The regular event checks complete tuples, outputs, chords, connectors, ODE trajectories, reconstructions, and ruled surfaces; continuity and compact population margins make the fallback asymptotically inactive. A scalar Richardson rank-collapse example proves why raw bands alone fail. | **CLOSED / UNSAFEGUARDED CLAIM DISPROVED** | Full generated membership, not invertibility alone, is load-bearing. |
| BW fixed-size calculus and frame | Circular BW-G3 was removed. Fixed-dimensional smooth primitive compositions plus typed variational ODEs and compactness prove the required fixed-order constants and polygonal comparison. | **CLOSED FOR FIXED \(m\)** | Fixed-size mean/PF may consume BW-DIFF-FIX. |
| BW lag/loading/selector | Feasible and oracle rows are mapped to one true anchor fibre; only the time-varying residual frame enters. Bounded energy gives \(A_2=O(1)\); the row, assembly, actual gap, null-square, and threshold/ridged-selector chain closes. | **CLOSED — PROVED UNDER EXPLICIT ASSUMPTIONS** | Integrate the full-rank local/regularized fixed-size theorem only. |
| BW rank-changing/global extension | Orthogonal rank-one PSD endpoints have nonunique alignment, geodesics, Logs, and means; Richardson and Exp can also hit rank loss. | **DISPROVED** | No global PSD or rank-changing theorem. |
| BW growing matrix size | Primitive spectral-band bounds do not establish dimension-uniform PT, curvature, Hessian, Richardson, or ruled-surface calculus. The former arbitrary-\(m_n\) theorem is retracted and split into fixed-margin and shrinking-margin exact lemmas. | **OPEN — TWO EXACT LEMMAS STATED** | No full noncommuting growing-size BW theorem. |
| BW–HE ledger | A second-pass mismatch was found and repaired: BW (10.1) now includes \(r_F(\mathcal E_2+L_{\log}r_\mu)\) and both connector and observation defects; downstream rows retain \(d^2\), contamination, \(A_2\), and the actual gap. | **CLOSED AS A CONDITIONAL LEDGER, NOT A THEOREM** | The general noncommuting intersection remains unavailable because BW size/local-energy obligations are open. |
| Diagonal BW–HE branch | The fixed-basis positive-root DGP verifies boundary margin, moving centre, dependence, \(R_n\asymp\sqrt{m_n}\), \(A_2\asymp m_n\), \(\Delta\asymp m_n^2\), bandwidth closure, and \(\eta/\Delta=o_p(1)\). | **CLOSED — PROVED UNDER EXPLICIT ASSUMPTIONS** | A restricted diagonal/fixed-basis intersection corollary may integrate; it says nothing about moving eigenvectors. |

### 11.2 Surviving analytical classification

| Track | Proved or corrected theorem | Analytic counterexample | Exact open obligation |
|---|---|---|---|
| HE | bounded-tail generated-domain mean; polygonal frame; finite-memory/product-PD row; actual/clean loading and selectors; flat/curved sufficient envelopes; pervasive and growing-rank DGPs | coordinate aggregation, inadequate trace moment, fixed-gap high-dimensional background, harmful normalization, coloured outside-loading contamination, insufficient growing-rank lag energy | HE-TRUNC only; consumed by no theorem |
| BW fixed size | full-rank local/regularized constrained mean, quotient polygonal frame, typed lag/loading/selector theorem | raw-band Richardson escape; eigenvalue-collapse constants; rank-changing PSD nonuniqueness; diagonal proof cannot cover rotating eigenspaces | none inside the fixed-size theorem |
| BW growing size | fixed-basis diagonal root-coordinate corollary only | fixed spectral band does not bound total BW energy | BW-SIZE-FIXED-MARGIN, then BW-SIZE-SHRINKING-MARGIN |

### 11.3 Exact HE–BW intersection

The intersection has three distinct statuses:

1. **Fixed-size full noncommuting BW:** proved under the localized full-rank assumptions and reduces to bounded-energy HD1.
2. **Growing-size full noncommuting BW:** **NO THEOREM**. The exact HE inequalities are now recorded, but the dimension-uniform BW differential lemma is open; shrinking margins require the second open lemma. The small-normal/support package also excludes a genuine unbounded local-energy regime unless separately relaxed and proved.
3. **Fixed-basis diagonal/root BW:** proved under the explicit positive-root DGP. Its nonempty window includes \(b_n=n^{-1/7}\) and \(m_n=o(n^{6/7}/\log n)\), together with its displayed boundary/supremum condition. This branch is flat and does not consume the noncommuting size lemmas.

### 11.4 Lead edge checks rerun

| Edge | Second-pass verdict | Canonical consequence |
|---|---|---|
| Zero signal | \(C_f(h)=0\) at every included lag gives \(\Delta=0\), so no positive-rank loading theorem. A threshold can select \(r=0\) only under its own null-row window \(d_n^2=o_p(\tau_n)\). | No division by zero and no positive-rank conclusion. |
| Zero noise | \(Y=Af\) removes idiosyncratic lag contamination but not estimated-centre, connector, or non-rigid frame error. | Retain \(q_R\) unless centre/frame is supplied. |
| Fixed dimension/energy | HE reduces row by row to \(r_\mu,r_F,q_R=O(\ell_n)\), \(d=O_p(n^{-1/2}+\ell_n)\); fixed \(m\) BW gives the same HD1 chain. | Base-case compatibility passes. |
| Localized high-dimensional background | The explicit Rademacher background keeps the population gap fixed while its empirical lag row can fail to vanish. | No blanket fixed-gap HE consistency. |
| Pervasive signal | The explicit one-factor DGP has \(A_2\asymp p_n\), \(\Delta\asymp p_n^2\), so signal can offset energy through the exact assembly ratio. | Permitted only with the verified DGP inequalities. |

### 11.5 Integrity, application gate, and integration verdict

Independent UTF-8 scans after the final repairs found no disallowed C0 controls or replacement characters. HE has balanced inline delimiters \(206/206\) and displays \(69/69\); BW has balanced inline delimiters \(232/232\), displays \(58/58\), and one balanced fenced block. Stale provisional strings were removed. The only remaining uses of **OPEN** are the three exact lemmas classified above; none is consumed by a proved headline theorem.

**GO for selective canonical integration:** integrate the corrected HE bounded-tail chain and its explicit regimes/counterexamples; the corrected fixed-size local/regularized BW theorem and counterexamples; and the restricted diagonal HE–BW corollary. Preserve all target, norm, domain, energy, \(A_2\), gap, and selector conditions.

**NO-GO for overbroad integration:** do not integrate an unbounded-score HE theorem, a global/rank-changing BW theorem, a full noncommuting growing-\(m\) BW theorem, or a general noncommuting HE–BW theorem. Carry HE-TRUNC and the two BW size lemmas into the canonical open-problems ledger.

Application remapping is now the next allowed analytical step, but only against these closed theorem scopes. Numerical-suite design remains downstream of canonical integration and application remapping. Automatic archival should preserve both repaired dossiers and this joint ledger as the working proof record.
