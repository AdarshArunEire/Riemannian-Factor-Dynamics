---
type: proof-dossier
title: FRAME-DB-A — geometry gauge and influence
status: noncanonical-workstream
scope: FRAME-DB geometry, gauge, and influence only; Paper 2 excluded
---

# FRAME-DB-A — geometry, gauge, and frame influence

> All sources mandated by FRAME-DB were read. This is the frozen repaired dossier, not canon.

## 0. Verdict

For the declared Levi–Civita frame functional, the fixed-observation frame derivative is a typed curvature/Jacobi functional modulo one common anchor rotation. The actual polygon has remainder \(Mr_N^2+M^{-2}\). Noisy frame differences do not recover their common truth-relative component; arbitrary external frames admit no centre-derived correction.

Generic feasible correction remains **OPEN — EXACT LEMMA STATED** at A-IF. The correct target is an asymptotically linear root-\(n\) influence row plus an \(o_p(n^{-1/2})\) nuisance remainder, not sub-root-\(n\) estimation of a regular correction coefficient.

## 1. Smooth-path variation: orientation and connector signs

Let \(S(\epsilon,s)\) be a \(C^2\) variation, \(T=\partial_sS|_0\), \(V=\partial_\epsilon S|_0\), and
\(P_{b\leftarrow a}^\epsilon:T_{S(\epsilon,a)}M\to T_{S(\epsilon,b)}M\).
Let \(C_r^\epsilon:T_{S(0,r)}M\to T_{S(\epsilon,r)}M\), \(C_r^0=I\), and define
\[
E_rW=\left.\nabla_\epsilon(C_r^\epsilon W)\right|_0,\qquad r=a,b.
\]
For fixed-fibre transport
\(\mathcal P_\epsilon=(C_b^\epsilon)^{-1}P_{b\leftarrow a}^\epsilon C_a^\epsilon\), under
\(R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}\),
\[
\boxed{\mathcal P'_0W=-E_bP_{b\leftarrow a}W+P_{b\leftarrow a}E_aW
+\int_a^bP_{b\leftarrow s}R(T(s),V(s))P_{s\leftarrow a}W\,ds.}
\tag{A.1}
\]
Proof: for \(W_\epsilon\) parallel in \(s\),
\(\nabla_\epsilon\nabla_sW-\nabla_s\nabla_\epsilon W=R(V,T)W\), so
\(\nabla_s\nabla_\epsilon W=R(T,V)W\). The terminal inverse connector differentiates to \(-E_b\); the initial connector to \(+E_a\). Radial connectors defined by PT along
\(\epsilon\mapsto\operatorname{Exp}_{S(0,r)}(\epsilon V_r)\) have \(E_r=0\). **PROVED.**

For \(F_t(\mu)=P^\mu_{0\leftarrow t}\), identify both varying fibres by these radial connectors and define
\[
\Omega_t(V)=DF_t(\mu)[V]F_t(\mu)^{-1}.
\tag{A.2}
\]
The family is orthogonal on one fixed anchor Hilbert space, hence \(\Omega_t(V)^*=-\Omega_t(V)\). A common first-order left rotation adds one time-constant skew; its finite action is common conjugation and is quotiented before measuring non-rigid error. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 2. Actual polygonal frame

For vertices \(q_0,\ldots,q_M\), \(P^{poly}=P_{M-1}\cdots P_0\), and
\[
DP^{poly}[v]=\sum_{j=0}^{M-1}
P_{M-1}\cdots P_{j+1}\,DP_j[v_j,v_{j+1}]\,P_{j-1}\cdots P_0.
\tag{A.3}
\]
Each \(DP_j\) is (A.1) on its geodesic cell. At a time inside cell \(j\), retain every completed cell and the partial-cell integral. Shared vertex generators telescope only with identical adjacent connector conventions.

Assume a generated tube with dimension-uniform curvature, first two chord PT/Jacobi derivatives, inverse endpoint-Jacobi bounds, path length, and mean acceleration. If
\(r_N^2=(M+1)^{-1}\sum_j\|v_j\|^2\) and \(\max_j\|v_j\|=o(1)\), then
\[
\sup_t\|R_t-I-\Omega_v^{poly}(t)\|_{op}\le C\{Mr_N^2+M^{-2}\}.
\tag{A.4}
\]
The lens term \(M^{-2}\) needs acceleration; bounded length alone is insufficient. With
\(M\asymp\ell_n^{-2/3}\), \(r_N=O_p(\ell_n)\),
\[
Mr_N^2+M^{-2}=O_p(\ell_n^{4/3}).
\tag{A.5}
\]
At \(\ell_n=n^{-3/7}\), this is \(n^{-4/7}=o(n^{-1/2})\), but it is not \(O_p(\ell_n^2)\). **PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 3. Gauge, synchronization, and arbitrary frames

Under a pure common coordinate change \(Q\),
\[
Y_t\mapsto QY_t,\quad \Gamma_h\mapsto Q\Gamma_hQ^*,\quad
\Omega_t\mapsto Q\Omega_tQ^*.
\tag{A.6}
\]
Separately, changing the common anchor alignment by an infinitesimal common left rotation adds one time-constant skew \(B\). That constant generator is removed before the coefficient norm. Raw row and correction must be conjugated together; truth-Procrustes is only a proof comparison.

Two fitted frames identify \(\Omega_{v^{(2)}-v^{(1)}}\) plus quadratic error, not either truth-relative influence or the common component. Cycle synchronization reconstructs a gauge but does not erase the holonomy derivative. **PROVED.**

Multiplying an arbitrary external frame by a smooth time-varying orthogonal field fixing the anchor preserves centre/data while changing its skew derivative. Without a declared frame-generation rule, centre-derived correction is **DISPROVED**.

## 4. Fixed-observation derivative versus law-score derivative

Let \(\bar H_t=E\{H(\mu_t,X_t)\}\). Along a regular marginal-law path with score \(s_t\),
\[
V_t=\dot\mu_t=\bar H_t^{-1}E\{\log_{\mu_t}X_t\,s_t\},
\tag{A.7}
\]
because \(D_qE\log_qX[V]=-\bar H_tV\).

Hold \(x\) fixed and set \(y_t(P,x)=F_t(\mu(P))\log_{\mu_t(P)}x\). Its geometric derivative is
\[
D_\mu y_t[V]=\Omega_t(V)y_t-F_tH(\mu_t,x)V_t.
\tag{A.8}
\]
There is no direct law term here. For \(s=t-h\), the lag-law derivative is separately
\[
\dot\Gamma_{t,h}
=E\{D_\mu y_t[V]\otimes Y_s+Y_t\otimes D_\mu y_s[V]\}
+E\{(Y_t\otimes Y_s)s_{t,s}\}.
\tag{A.9}
\]
Thus frame, mean/base-log, and direct lag-law score channels are distinct and not double counted. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 5. A-IF — exact missing lemma

On the canonical tube and exact split/mask, construct a common-anchor-equivariant observable influence row \(\varphi_{n,P}\) such that
\[
\bigoplus_{h\le h_0}(\widehat\Gamma_h^{db}-\Gamma_h)
=(P_n-P)\varphi_{n,P}+\mathcal R_n,
\tag{A.10}
\]
where:

1. \(\varphi_{n,P}\) represents all terms of (A.9): inverse-Karcher influence, frame/base-log derivatives, and direct lag-law score.
2. The frame part uses either smooth (A.1) or, separately, polygon (A.3), including radial connectors, completed cells, and the partial cell.
3. Computation uses fitted Hessian/Riesz, connection-curvature/Jacobi, and cross-fitted lag objects, never true centre/frame/anchor/error/ribbon/population lag row.
4. A dimension-uniform HS dependence theorem gives
\(\|(P_n-P)\varphi_{n,P}\|_{\oplus HS}=O_p(n^{-1/2})\).
5. For the polygon,
\[
\|\mathcal R_n\|_{\oplus HS}
=O_p\{Mr_N^2+M^{-2}+r_e^2+r_er_F+r_F^2\}
+o_p(n^{-1/2})+\rho_{mask,n},
\tag{A.11}
\]
with every grid, curvature, length, acceleration, inverse-Hessian, lag-energy, dependence, and dimension constant explicit. Use the exact masked target unless \(\rho_{mask,n}\) is paid first order.

The sign is fixed: if pilot displacement is \(e\), validation Karcher score obeys
\(\Psi(\widehat\mu)=-\bar He+o(\|e\|)\), hence
\(\widehat e=-\widehat{\bar H}^{-1}\widehat\Psi\). If \(Ke\) is the lag derivative,
\[
T(\widehat\mu)-K\widehat e
=T(\widehat\mu)+K\widehat{\bar H}^{-1}\widehat\Psi,
\tag{A.12}
\]
whose nuisance derivative is \(Kv+K\bar H^{-1}(-\bar Hv)=0\).

The empirical influence fluctuation in (A.10) is the leading root-\(n\) row; only \(\mathcal R_n\) is the debiasing residual. Thus A-IF earns oracle order, generally not the known-centre first-order law. By (A.5), its canonical polygon remainder is \(o_p(n^{-1/2})\).

**OPEN — EXACT LEMMA STATED.**

## 6. Candidate and edge audit

| Claim/case | Conclusion | Status |
|---|---|---|
| Naive pointwise plug-in | noisy-frame differences do not identify common error | DISPROVED |
| Influence/Jacobi | reduced exactly to A-IF | OPEN — EXACT LEMMA STATED |
| Fixed-fold Richardson | cannot cancel realised stochastic derivative | DISPROVED |
| Invariant-only redesign | changes loading estimand | DISPROVED |
| Cycle-synchronized redesign | must prove A-IF-equivalent cycle influence | OPEN — EXACT LEMMA STATED |
| Smooth finite-dimensional nuisance | needs displayed IF, folds, mask, computable geometry, curved DGP | OPEN — EXACT LEMMA STATED |
| Flat/common commuting flat | frame derivative zero after common alignment | PROVED |
| Common rigid skew | common conjugation, no gap penalty | PROVED |
| CE-B5 | survives GLO and splitting | DISPROVED |
| Zero signal | frame coefficient zero; loading unidentified | PROVED |
| Zero noise, moving estimated centre | curvature frame error can remain | PROVED |
| Constant curvature, moving mean | (A.1) generally nonzero | PROVED |
| High-dimensional bounded energy | HS concentration does not supply Hessian/Riesz estimation | OPEN — EXACT LEMMA STATED |
| One bad vertex | retains \(Mr_N^2\) and tube maximum | PROVED |
| High-frequency path | length cannot replace acceleration | DISPROVED |
| Changing eigenbasis | pointwise commutation does not give one flat | DISPROVED |
| Same law, unique mean, fixed connection | target agrees modulo common conjugation | PROVED |
| Arbitrary external frame | centre data do not determine its derivative | DISPROVED |

## 7. Pass-1 repairs and frozen conclusion

| B/C objection | Repair | Status |
|---|---|---|
| Connector/curvature signs unverified | \(-E_b,+E_a,R(T,V)\) derived in §1 | PROVED |
| Geometry and law score conflated | split in (A.8)–(A.9) | PROVED |
| Impossible sub-root-\(n\) coefficient property | replaced by asymptotic-linear (A.10) | SUPERSEDED |
| Polygon count suppressed | retained \(Mr_N^2+M^{-2}=\ell_n^{4/3}\) | PROVED UNDER EXPLICIT ASSUMPTIONS |
| One-step sign absent | fixed by (A.12) and zero derivative | PROVED |
| Truth-selected gauge | computation required equivariant | PROVED UNDER EXPLICIT ASSUMPTIONS |
| B triple product from RMS only | requires frame supremum or fourth/product moment | DISPROVED |
| Smooth/polygon claims combined | branches separated | SUPERSEDED |
| Correction fluctuation called negligible | influence row separated from residual | PROVED |

The geometric/gauge chain is closed. Generic feasibility is reduced to A-IF. At the canonical grid its geometric remainder is \(o_p(n^{-1/2})\); no false \(O_p(\ell_n^2)\) polygon claim remains.

**OPEN — EXACT LEMMA STATED.**
