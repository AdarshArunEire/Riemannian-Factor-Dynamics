---
type: proof-dossier
title: FRAME-DB-B — feasible estimator and row theorem
status: noncanonical-workstream
scope: FRAME-DB estimator and statistical row theorem only; Paper 2 excluded
---

# FRAME-DB-B — feasible estimator and row theorem

> All sources mandated by the FRAME-DB brief were read. This dossier is proof input, not canon.

## 0. Verdict

No generic feasible estimator is proved from the present inputs. Naive plug-in, fixed-fold averaging/Richardson, and invariant-only redesign fail. A coefficient-conditional plug-in inequality and a finite-dimensional one-step algebraic template are proved below, but neither is a reproducible curved estimator theorem on a proved nonempty DGP. The generic route is reduced to one precisely stated aggregate grid/influence lemma. **Final recommendation after hostile pass 1: Gate D.**

## 1. Observability architecture

Use three finite-memory colours with retained cores separated by at least \(m_0+h_0\): training \(T\), validation \(V\), and evaluation \(E\). On \(T\), compute observable positive three-scale vertex means, the geodesic polygonal frame, fitted Karcher Hessians/inverses, and fitted curvature/Jacobi derivatives. On \(V\), compute the actual masked, weighted Karcher score used to estimate the training centre error. On \(E\), compute lag products. All three folds use a declared common anchor synchronization and masks targeting the same finite-array row; comparison with an unmasked target adds \(\rho_{\rm mask,n}\). True centres, frames, anchor alignment, \(e_t\), \(\Omega_t\), and population \(\Gamma_{t,h}\) occur only in proof comparisons.

## 2. Exact plug-in correction and residual

Let \(\widetilde Y_t=Y_t+a_t\), \(\widetilde\Omega_t=\Omega_t+\delta_t\), in one proof-aligned anchor space after removing the best common skew. For every lag retain current and shifted RMS norms for \(a,\delta,\widetilde\Omega\), and
\[
r_{\widetilde\Omega a}^2=\max_{h,\pm}N_h^{-1}\sum_t
\|\widetilde\Omega_{t\mp h}a_{t\mp h}\|^2.
\tag{B.0}
\]
Let \(r_a,r_\delta,r_{\widetilde F}\) be the analogous shifted maxima. A sufficient triple-product envelope is \(\sup_t\|\widetilde\Omega_t\|_{op}\le\bar\omega_n\), giving \(r_{\widetilde\Omega a}\le\bar\omega_nr_a\); otherwise the action norm remains explicit. Define

\[
\widehat C_h=N_h^{-1}\sum_t\{
\widetilde\Omega_t\widetilde Y_t\otimes\widetilde Y_{t-h}
+\widetilde Y_t\otimes\widetilde\Omega_{t-h}\widetilde Y_{t-h}\}.
\tag{B.1}
\]

Subtracting (B.1) from the feasible lag row leaves the APP-B quadratic remainder, the mean channel (unless separately orthogonalized), and frame residual

\[
\begin{aligned}
R_{t,h}^{F}={}&-\delta_tY_t\otimes Y_{t-h}-Y_t\otimes\delta_{t-h}Y_{t-h}\\
&-\widetilde\Omega_ta_t\otimes Y_{t-h}-\widetilde\Omega_tY_t\otimes a_{t-h}\\
&-a_t\otimes\widetilde\Omega_{t-h}Y_{t-h}-Y_t\otimes\widetilde\Omega_{t-h}a_{t-h}\\
&-\widetilde\Omega_ta_t\otimes a_{t-h}-a_t\otimes\widetilde\Omega_{t-h}a_{t-h}.
\end{aligned}
\tag{B.2}
\]

Conditional on training, under the exact split and identical finite-array mask, the first line has population coefficient

\[
\mathcal B_h(\delta)=N_h^{-1}\sum_t\{\delta_t\Gamma_{t,h}-\Gamma_{t,h}\delta_{t-h}\}.
\tag{B.3}
\]

Thus a pointwise \(O_p(\ell_n)\) frame estimator does not suffice. The exact required quantity is the direct-sum HS norm of (B.3), plus all products in (B.2). The centred first-line fluctuation is \(O_p(R^2r_\delta n^{-1/2})\) under \(\|Y_t\|\le R\), fixed lag/memory and the exact split. This is coefficient-conditional: neither \(\delta\) nor the truth-relative common skew is claimed observable.

## 3. Coefficient-conditional plug-in row inequality

Assume APP-B's exact split, GLO, bounded energy, fixed rank/lag/memory, uniform Taylor tube, and \(r_e+r_F=o_p(1)\). Suppose a proposed plug-in, after theoretical common-gauge alignment, satisfies

\[
\beta_{\delta,n}:=\|\oplus_h\mathcal B_h(\delta)\|_{\rm HS},
\quad r_a,r_\delta,r_{\widetilde F},r_{\widetilde\Omega a}<\infty.
\]

Then direct rank-one expansion and Cauchy–Schwarz give

\[
d_{F,{\rm plug},n}
=O_p\{\beta_{\delta,n}+R^2r_\delta n^{-1/2}
+C\sqrt{h_0}(Rr_{\widetilde\Omega a}+Rr_{\widetilde F}r_a+r_{\widetilde\Omega a}r_a)\}.
\tag{B.4}
\]

Including mean empirical fluctuation and all APP-B quadratic terms,

\[
d_n^{\rm plug}=O_p\{n^{-1/2}+(r_e+r_F)n^{-1/2}
+\varepsilon_G r_e+r_e^2+r_er_F+r_F^2+d_{F,{\rm plug},n}+\rho_n\}.
\tag{B.5}
\]

Equations (B.4)–(B.5) are **PROVED UNDER EXPLICIT ASSUMPTIONS** as a coefficient-conditional inequality; they are not a feasible generic theorem until an observable producer proves the inputs without truth alignment.

The plug-in statement is `PROVED UNDER EXPLICIT ASSUMPTIONS` only as a coefficient-conditional inequality. It is not a feasible theorem until an observable producer proves the shifted/action inputs and synchronization. The valid coefficient envelope is
\[
G_{2,HS,n}^2=\sum_{h=1}^{h_0}\sup_t\|\Gamma_{t,h}\|_{HS}^2,
\qquad \beta_{\delta,n}\le2G_{2,HS,n}r_\delta,
\tag{B.5a}
\]
not operator lag energy without rank control.

## 4. Fixed-fold/Richardson test

If a scalar projection of the nuisance has derivative \(c\ne0\) and \(K\) independent fold estimators have expansion \(\eta+r_nZ_k\), any deterministic target-preserving weights \(\sum_kw_k=1\) leave variance at least \(r_n^2\operatorname{Var}(cZ)/K\). With fixed \(K\) and \(r_n=\ell_n=n^{-3/7}\), this is not \(o(n^{-1/2})\). Richardson may cancel known deterministic bandwidth powers, not realised stochastic frame error. **Status: DISPROVED for fixed-fold linear combinations.**

Neyman orthogonality requires the Gateaux derivative of the complete lag score to vanish for every admissible centre-path direction. A score correcting \(-H_te_t\) but omitting \((DP^\mu[e])Y_t\), endpoint connectors, or lag-law derivatives is not orthogonal.

## 5. Frame-avoiding test

Spectra or singular values are gauge invariant but do not determine the Paper 1 loading space, so invariant-only estimation changes the estimand. **Status: DISPROVED.** Pairwise transports can recover the target only if their noisy transports are cycle-consistently synchronized up to one common \(Q\), with second-order sensitivity to centre error. No such generic theorem is currently proved; that route is **OPEN — EXACT LEMMA STATED** through FRAME-IF.

## 6. One-step sign, folds, and status

Let the Karcher score use the convention \(\Psi(\mu)=E\log_\mu X\), so \(D_\mu\Psi[v]=-Av\). Let \(K=D_\mu T\) be only the nuisance derivative of the lag functional; the direct lag-law empirical influence remains in the base row. The orthogonal population functional is
\[
S(\mu,P)=T(\mu,P)+K_\mu A_\mu^{-1}\Psi_P(\mu),
\qquad D_\mu S[v]=Kv+KA^{-1}(-Av)=0.
\tag{B.6}
\]
Thus the sign is plus. Fold \(T\) estimates \(\widehat\mu,\widehat K,\widehat A^{-1}\); fold \(V\) supplies the identically masked weighted score \(\widehat\Psi^V(\widehat\mu)\); fold \(E\) supplies \(\widehat T^E(\widehat\mu)\). The reproducible candidate is
\[
\widehat S=\widehat T^E(\widehat\mu)+\widehat K^T(\widehat A^T)^{-1}
\widehat\Psi^V(\widehat\mu),
\tag{B.7}
\]
after observable common-anchor synchronization. Mask comparisons, fold deletion, and coupling enter \(\rho_{mask,n},\rho_{CF,n}\).

If an explicit nuisance class proved all derivative estimates and aggregate HS concentration, Taylor expansion would yield

\[
\widehat S_n-T_n(\eta_0)
=(P_n-P)\varphi_{n,\eta_0}+O_p(\|\widehat\eta-\eta_0\|^2)+o_p(n^{-1/2}).
\tag{B.8}
\]

The empirical influence fluctuation in (B.8) is part of the leading root-\(n\) row, not the nuisance residual \(d_{F,db,n}\). No fully instantiated curved DGP in this campaign presently proves \(\widehat K,\widehat A^{-1}\), synchronization, masks, and direct-sum HS concentration at the required rates. Therefore (B.6)--(B.8) are an algebraic template, not Gate B. Their status is `OPEN — EXACT LEMMA STATED` through FRAME-IF.

If the phrase \(d_{F,db,n}\) is defined to include every stochastic fluctuation of the estimated correction, uniform \(o_p(n^{-1/2})\) is information-theoretically impossible on regular nonzero-derivative parametric submodels. The coherent one-step convention places the unavoidable influence fluctuation in the leading empirical row and calls only the nuisance remainder \(d_{F,db,n}\).

## 7. Generic missing lemma FRAME-IF

For the observable-law functional

\[
\mathfrak T_n(P)=\left[\left(N_h^{-1}\sum_tE_P\{Y_t(P)\otimes Y_{t-h}(P)\}\right)_{h\le h_0}\right],
\]

construct a common-gauge-equivariant influence map \(\varphi_{n,P}\) and feasible cross-fitted estimate such that:

1. its nuisance derivative contains inverse Karcher influence, base-log Hessians, full path/polygon Jacobi transport derivative, and endpoint connectors; the direct lag-law empirical influence remains in the base row;
2. it uses no true centre/frame/anchor, \(e,\Omega,\Gamma\), or unobserved ribbon;
3. the one-step expansion has remainder
   \[
   O_p(r_e^2+r_er_F+r_F^2)+o_p(n^{-1/2})
   \]
   in direct-sum HS norm;
4. its aggregate vertex-grid influence row is \(O_p(n^{-1/2})\) dimension-uniformly in direct-sum HS under the exact split, with \(M_n\), weight norms, \(\|KA^{-1}\|_{\ell_M^2\to HS^{\oplus h_0}}\), masks, synchronization and dependence explicit;
5. for deterministic \(M_n\asymp\bar\ell_n^{-2/3}\), its polygon remainder is \(C_{geo,n}\{M_n\ell_n^2+M_n^{-2}\}=C_{geo,n}O(\ell_n^{4/3})=o(n^{-1/2})\) at \(\ell_n=n^{-3/7}\), with \(C_{geo,n}=O(1)\) and a proved vertex-maximum tube event.

**Status: OPEN — EXACT LEMMA STATED.** This aggregate grid/HS statement is smaller than “estimate the frame better”; pointwise \(\Omega\) recovery is unnecessary.

## 8. Propagation if FRAME-IF holds

At \(b_n=n^{-1/7}\), \(r_e,r_F=O_p(\ell_n)\) and \(\ell_n^2=o(n^{-1/2})\). Hence FRAME-IF would give

\[
d_n^{db}=O_p(n^{-1/2}+\ell_n^2+\varepsilon_G\ell_n+\rho_n).
\]

With negligible defects and \(2A_{2,n}d_n^{db}+(d_n^{db})^2=o_p(\Delta_n)\), row assembly and Davis–Kahan yield

\[
\|\sin\Theta(\widehat E_n^{db},E_n)\|_{op}=O_p(n^{-1/2}/\Delta_n),
\qquad \widehat\lambda_{r+1,n}^{db}=O_p(n^{-1}).
\]

Use \(G_{2,HS,n}\), not operator lag energy, for frame-coefficient HS bounds. Use the actual \(\Delta_n\); replace it by \(s_n^2\) only after the canonical factorisation/gap proof.

## 9. Candidate and edge ledger

| Class/case | Verdict | Status |
|---|---|---|
| Naive pointwise plug-in | (B.3) remains first order and no coefficient producer is supplied | DISPROVED |
| Complete one-step/Jacobi | reduced to FRAME-IF | OPEN — EXACT LEMMA STATED |
| Fixed-fold jackknife/Richardson | cannot cancel realised nuisance noise | DISPROVED |
| Invariant-only redesign | changes loading estimand | DISPROVED |
| Parametric observable nuisance | algebraic template lacks instantiated curved DGP and aggregate proof | OPEN — EXACT LEMMA STATED |
| Flat/fixed commuting flat | frame channel zero after common alignment in the existing branch | PROVED |
| Common rigid rotation | quotient conjugation | PROVED |
| CE-B5 | survives GLO/splitting and defeats the GLO-only claim | DISPROVED |
| Zero signal | frame coefficient zero, loading unidentified | PROVED |
| High dimension | HS lag-energy producer is mandatory | PROVED |

## 10. First hostile cross-audit of A — SUPERSEDED as a current objection list

This section records pass 1 against the pre-repair A draft. Its objections drove the repaired A dossier and are **SUPERSEDED** as current claims wherever the repair column was implemented. No objection changes A's `OPEN — EXACT LEMMA STATED` verdict.

| A claim attacked | Statistical objection | Exact repair | Final status |
|---|---|---|---|
| The population frame is observable from the law | Law-identifiability is not an estimator. Computing the derivative requires the population path, inverse Karcher Hessian, curvature/Jacobi map, and anchor synchronization. Two noisy frames do not identify either error relative to truth. | Use three separated folds to estimate \(A^{-1}\), the polygon derivative \(K\), and one common gauge; state their producer norms. | Population identification `PROVED`; feasible rate `OPEN — EXACT LEMMA STATED`. |
| (A.4) supplies an influence estimate | (A.4) is a population derivative. The empirical centre uses kernel weights, Richardson stages, a perforated design, and a polygon grid. Validation-score smoothing/design bias is absent. | Define the actual weighted validation score at every training vertex and prove \(\widehat e=-\widehat A^{-1}\widehat\Psi^V\) jointly over vertices, including bandwidth, mask, local-stationarity, and inverse-Hessian errors. | `OPEN — EXACT LEMMA STATED`. |
| The full law derivative (A.5) may be subtracted | The direct lag-pair-law derivative is the oracle target's sampling influence. Subtracting it can change the estimand or erase the root-\(n\) oracle fluctuation. Only the nuisance-induced base-log/frame derivative is plug-in bias. | Decompose \(D_PT=D_P^{direct}T+D_\mu T[D_P\mu]\). Retain the direct empirical row and correct only the second term, or derive a complete efficient influence function with expectation \(T(P)\). | Decomposition `PROVED`; unqualified full-derivative subtraction `DISPROVED`. |
| A-IF is feasible because inputs are manifold operations | A-IF(3) contains population \(\Gamma_{t,h}\). It is a theoretical residual, not a computable correction. An empirical replacement adds dependence, HS fluctuation, and target/mask mismatch. | Fold \(T\): \(\widehat K,\widehat A\); fold \(V\): influence score; fold \(E\): base row and correction action on retained lag pairs, conditional on \(T,V\). The population residual identity is proved, but the centred correction row in \(\mathcal S_2(H)^{\oplus h_0}\) is the missing consumer. | `OPEN — EXACT LEMMA STATED` |
| Polygon remainder is second order | \(Mr_e^2\) requires a declared vertex norm. For vertex RMS, \(\sum_j e_j^2=(M+1)r_e^2\); one error of size \(\sqrt M r_e\) also threatens the tube and derivative constants. | Retain \(r_{2,V}^2=(M+1)^{-1}\sum e_j^2\) and \(r_{\infty,V}=\max e_j\); require \(r_{\infty,V}=o_p(1)\); write \(C\{Mr_{2,V}^2+M^{-2}\}\). | `PROVED UNDER EXPLICIT ASSUMPTIONS`; RMS-only tube claim `DISPROVED`. |
| \(M\asymp r_e^{-2/3}\) makes the polygon remainder negligible | The arithmetic needs deterministic tuning and uniform acceleration, curvature/Jacobi and generated-tube constants. Bounded path length alone does not control the chord lens. | Choose deterministic \(M_n\asymp\bar\ell_n^{-2/3}\) and retain \(C_{geo,n}(M_nr_e^2+M_n^{-2})\) until dimension uniformity is proved. | Fixed-\(p\) arithmetic `PROVED`; uniform result `PROVED UNDER EXPLICIT ASSUMPTIONS`. |
| Cell derivatives telescope | Endpoint terms telescope only with identical connector conventions and synchronized cell gauges. Fold-specific polygons can leave first-order boundary terms. | Specify one observable anchor, radial endpoint connectors, ordered cell composition, and cross-fold synchronization. Quotient one time-constant skew; keep all nonconstant endpoint generators in \(K\). | Pathwise identity `PROVED`; unsynchronized telescoping `DISPROVED`. |
| Aggregate influence is root-\(n\) after splitting | Vertexwise estimation can pay \(\sqrt M\), a grid maximum, or operator entropy. Bounded total energy concentrates fixed Hilbert/HS maps; it does not estimate \(A^{-1}\) or the full vertex-to-row operator \(K\) in operator norm. | Concentrate the aggregate Riesz row \(KA^{-1}\Psi\) directly in direct-sum HS, exposing \(\|K\|_{\ell^2_M\to\mathcal S_2^{\oplus h_0}}\), weights, memory and mask. Fixed-dimensional closure under explicit producer assumptions does not establish the canonical growing-\(p_n\) consumer. | `OPEN — EXACT LEMMA STATED` |
| A-IF(3) is the required row residual | It controls only the population frame coefficient. It omits correction noise, products with \(\widetilde Y-Y\), inverse-Hessian/kernel errors, mean channel, masks, coupling and target defects. | Add \(s_Kr_e+s_Ar_\Psi+r_{IF}+n^{-1/2}r_e+Mr_e^2+M^{-2}\) and all typed defects; correct mean and frame derivatives together. The repaired statement is FRAME-IF rather than a proved row theorem. | `DISPROVED` |
| Gauge equivariance closes loading propagation | It removes the penalty for one common rotation only. A time-varying residual remains additive and pays the actual gap. | Prove \(d_n^{db}\) in direct-sum HS; assemble \(2A_{2,n}d_n^{db}+(d_n^{db})^2\); require it is \(o_p(\Delta_n)\); use the row singular-value square for \(\widehat\lambda_{r+1}\). Never replace HS frame energy by operator energy without rank control. | `DISPROVED` |

### Cross-audit conclusion

A correctly isolates the geometric derivative but stops before observability and statistical closure. The viable repair is the aggregate three-fold nuisance derivative \(KA^{-1}\Psi\), not pointwise recovery of every \(\Omega_t\). Fixed dimension or a structured finite-dimensional/known-geometry nuisance class can satisfy the repair. The canonical growing-\(p_n\) package does not estimate the required inverse Hessian and derivative operator, so the generic result remains `OPEN — EXACT LEMMA STATED`.

## 11. First-pass conclusion

Gate A is not earned. Gate B is not earned because no fully reproducible curved estimator and nonempty curved DGP close every derivative, mask, synchronization, and aggregate HS input. Gate C is not earned because the target is an observable-law functional under unique means. Final B verdict: Gate D, **OPEN — EXACT LEMMA STATED** at FRAME-IF.
