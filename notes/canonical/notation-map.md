---
type: canonical-reference
title: Parent-to-project notation map
status: canonical
last-audited: 2026-08-19
sources:
  - reference/2607.28385v1.pdf
  - reference/Riemannian_factor_model-main
upstream-commit: c07d49c257d489e00b7e15bdd432954946a2a694
---

# Parent-to-project notation map

> **Purpose.** This is the translation layer between Huang, Chen and Chen (2026), their pinned R code, and the Paper 1 canon. It changes no hypothesis, norm, estimand, rate, or theorem status. A row marked “special case” is not an equality outside the stated special case.

## 1. Reading rules and source pin

The parent source is 'reference/2607.28385v1.pdf', arXiv:2607.28385v1. Code locations refer to 'reference/Riemannian_factor_model-main' at upstream commit 'c07d49c257d489e00b7e15bdd432954946a2a694'. [[reference/AUDIT|AUDIT]] and 'reference/PROVENANCE.md' record the implementation audit and pin.

| Mark | Meaning |
|---|---|
| \(=\) | the same mathematical object after the stated coordinate identification |
| \(\leftrightarrow\) | an implementation or notation counterpart, possibly represented in coordinates |
| \(\rightsquigarrow\) | only a special-case reduction or bound; never silently substitute it |

The parent is fixed-centre and stationary in its main theorem. Paper 1 is a moving-centre triangular-array model. The parent is recovered only after setting \(\mu_n(u)\equiv\mu\), making the transported loading constant, and imposing the exact included-lag factorisation below.

## 2. Collision guard

| Parent paper | Parent code | Project canon | Translation and guard |
|---|---|---|---|
| \(p=\dim M\) | 'p = dim(x)[2]' in BW code | \(p_n=\dim H_n\), the tangent dimension | Paper \(p\) is manifold dimension. BW code 'p' is SPD matrix order. Write it as \(m\); then \(p_n=m(m+1)/2\). |
| \(r\), factor/loading rank | 'r', requested eigenvectors and raw-ratio cap | \(r_n=\dim\mathcal S_{X,n}\), usually fixed \(r\) | Code 'r' is not automatically the identified rank. 'LYB_fm' returns \(r\) columns but searches ratios only over \(1,\ldots,r-1\). |
| \(R\), support radius in (P1) | no exact code variable; \(R\) also denotes a selector cap in Eq. (5) | \(R_n=\sup_t\|Y_{t,n}\|\); use \(R_n^{\rm cap}\) for a selector cap | Never use one symbol for energy and selector range. |
| \(h_0\) | 'h'; local 'H = h + 1' | \(h_{0,n}\), usually fixed \(h_0\) | Code 'H' is an indexing offset, not an operator or forecast horizon. |
| \(n\) | overwritten after the train/test split | row size \(n\), effective training size \(N_n\) | State which sample size a numerical result uses. |
| \(\lambda_i\) | 'evals' | \(\lambda_i(\mathbb L_n)\), \(\widehat\lambda_{i,n}\) | Always attach the operator and hat in project prose. |
| \(\kappa\) | no named code variable | \(s_n\) in one special case; only indirectly \(\Delta_n\) | \(\kappa=s_n\) only when both maxima use the same stationary factor-lag matrices. One full-rank lag gives \(\Delta_n\ge s_n^2\); it does not give \(\kappa^2=\Delta_n\). |
| \(A_E\) | 'A', 'V', 'true_A' | declared \(A_n\); estimand \(\mathcal S_{X,n}\) | A matrix representative is not the identified object. |
| \(E,\widehat E\), tangent bases | 'E'; BW 'E_lyapunov' | a frame/coordinate isometry and its common rigid gauge | 'E_lyapunov' is a dual-coordinate aid, not another loading space. |
| \(c_n\), (P3) objective concentration | no named code variable | direct centre-distance rate \(\ell_n\), separately row error \(d_n\) | The parent proves \(d_M(\widehat\mu,\mu)=O_p(c_n^{1/2})\). Thus \(c_n^{1/2}\), not \(c_n\), is comparable to a fixed-centre version of \(\ell_n\). |

## 3. Model and geometry

| Parent symbol/object | Paper location | Code object | Project symbol/source | Translation or boundary |
|---|---|---|---|---|
| \(M,d_M,\operatorname{Exp},\operatorname{Log}\) | §2; Eqs. (1)–(3) | 'geod_BWS', 'Exp_BWS', 'Log_BWS'; sphere analogues | \(M,d,\operatorname{Exp},\log\); [[Paper 1 — Locally stationary Riemannian factor model]] | Same roles. Code order is Exp_BWS(tangent, base) and Log_BWS(point, base), opposite to subscript notation. |
| \(x_t\in M\) | Eq. (1) | 'x', 'x_test', 'x_train' | \(X_{t,n}\) | Constant-centre special case of the triangular array. |
| \(\mu\) | (P2) | 'mu_hat', 'true_mu', 'dta$mu' | \(\mu_n(u)\), anchor \(\mu_n(u_0)\) | Parent (P2) sets \(\mu_n(u)\equiv\mu\). This assumes centre drift away; it does not identify a drift/factor split. |
| \(\widehat\mu\) | Proposition 2 | 'mean_on_BWS', 'model$mu_hat' | \(\widehat\mu_n(u)\), or its fixed-centre special case | Parent rate \(O_p(c_n^{1/2})\); project \(\ell_n\) also contains smoothing, localisation, and grid terms. |
| \(z_t=\operatorname{Log}_{\mu}x_t\) | Eqs. (1)–(2) | 'log_x_vec' | \(Y_{t,n}=\mathcal P_{u_t\to u_0}\log_{\mu_n(u_t)}X_{t,n}\) | Equal after fixing the centre, choosing a basis, and identifying the tangent fibre with coordinates. |
| \(z_{t,E}\) | Eq. (3) | row 'log_x_vec[t, ]' | frame coordinates of \(Y_{t,n}\) | Coordinate representative only. Project norms are intrinsic Hilbert/Hilbert–Schmidt norms. |
| \(\mathcal A:\mathbb R^r\to T_\mu M\), \(A_E\) | Eqs. (2)–(3) | 'model$A = model$V'; top-level 'V' | declared \(A_n\); target \(\mathcal S_{X,n}=\operatorname{ran}\mathbb L_n\) | \(\operatorname{ran}A_n=\mathcal S_{X,n}\) only when \(Q_n\succ0\). |
| \(f_t\) | Eq. (2) | 'f_hat', 'Factors' | \(f_{t,n}\) | Estimated by projection; retains orthogonal/gauge ambiguity. |
| \(\delta_t,\delta_{t,E}\) | Eqs. (2)–(3) | 'e_hat' | \(\varepsilon_{t,n}\) | Exact factorisation requires zero included-lag residual and both factor–residual cross covariances; violations enter \(\zeta_n\). |
| \(E=(e_1,\ldots,e_p)\), \(\widehat E\) | §2.2, Eq. (4) | 'E', 'coord$E' | chosen/estimated frame | Paper 1 tracks non-rigid frame error; a common rigid rotation acts by joint conjugation. |
| \(J_{\widehat E}(a)=\sum_ja_j\widehat e_j\) | Eq. (4) | 'log_to_tangent(z,E)' | inverse coordinate isometry | Exact reconstruction role. |
| \(\Phi_{\widehat\mu,\mu}\) | Eq. (7) | 'pt_bws' in the simulation diagnostic | connector conjugation/common gauge \(Q_n\) | Project geometry additionally separates endpoint connectors and non-rigid frame error. |
| \(\widehat x_t\) | Eq. (4) | 'x_hat', 'RFM_xhat' | \(\operatorname{Exp}_{\widehat\mu}(\widehat Y_t)\) | Reconstruction unless a separate score model predicts future factors. 'dyn_RFM' adds VAR(1), making it a forecast. |

## 4. Lag row, operator, signal, and loading space

The parent coordinate lag matrix is

\[
\widehat S_{\widehat E}(h)
=\frac1n\sum_{t=h+1}^n
\widehat z_{t,\widehat E}\widehat z_{t-h,\widehat E}^{\mathsf T}.
\]

Code uses

\[
\text{temp}_i=\frac1n\sum_{t=h+1}^{n}x_tx_{t-i}^{\mathsf T},
\]

implemented at 'BWS_util.R:287' as 't(x[H:n,]) %*% x[(H-i):(n-i),] / n', with 'H = h + 1'. The paper’s intrinsic \(\widehat z_{t-h}\otimes\widehat z_t\) is the same orientation because \(u\otimes v:w\mapsto\langle u,w\rangle v\).

| Parent paper | Parent code | Project canon | Relation and warning |
|---|---|---|---|
| \(\widehat S_{\widehat E}(h)\); intrinsic \(\widehat S(h)\) | 'temp' | feasible \(\widehat\Gamma_n(h)\) | Same orientation after the tensor-convention translation. Parent/code divide by \(n\), not \(n-h\), and code uses one common tail for all lags. |
| \(S(h)=\mathbb E(z_{t-h}\otimes z_t)\) | population limit of 'temp' | \(\Gamma_n(h)\) | Same in the stationary fixed-centre case. Ideal factor row is \(\Gamma_n^0(h)=A_nC_{f,n}(h)A_n^*\). |
| \(\widehat L_{\widehat E}=\sum_h\widehat S_{\widehat E}(h)\widehat S_{\widehat E}(h)^{\mathsf T}\); intrinsic \(\widehat{\mathcal L}\) | 'pd' | \(\widehat{\mathbb L}_n=\sum_h\widehat\Gamma_n(h)\widehat\Gamma_n(h)^*\) | Exact coordinate/intrinsic counterparts. 'pd' is positive semidefinite, not necessarily positive definite. |
| \(\mathcal L=\sum_hS(h)S(h)^*\) | population 'pd' | \(\mathbb L_n\) | Same parent special case; project attaches \(n\) because target, dimension, and signal may vary. |
| loading space \(\operatorname{span}(A_E)\) | 'V = Evec[,1:r]' | \(\mathcal S_{X,n}=\operatorname{ran}\mathbb L_n\) | Code estimates the requested leading space. It estimates \(\operatorname{ran}A_n\) only if \(Q_n\succ0\) and the requested dimension is the dynamic rank. |
| \(\widehat A_{\widehat E}\) | 'V', also 'model$A' | matrix representative of \(\widehat{\mathcal S}_{X,n}\) | Compare spans/projectors, not ordered signed columns. |
| \(\lambda_i,\widehat\lambda_i\) | 'evals' | \(\lambda_i(\mathbb L_n),\widehat\lambda_{i,n}\) | Same in coordinates. |
| \(\lambda_r\ge\kappa^2\) | no named check | \(\Delta_n=\lambda_r(\mathbb L_n)-\lambda_{r+1}(\mathbb L_n)\) | Parent Proposition 3 has exact population rank, hence \(\lambda_{r+1}=0\). Only there is \(\lambda_r\) the gap. |
| \(\kappa=\max_{h\le h_0}\sigma_r\{\mathbb E(f_{t-h}\otimes f_t)\}\) | no named variable | \(s_n=\max_{h\le h_0}\sigma_r(C_{f,n}(h))\) | Same one-lag certificate in the stationary exact-factor case. Complementary rank-deficient lags can give \(\Delta_n>0\) when \(s_n=0\). |
| no named stacked row | loop of 'temp' | \(\mathcal G_n=[\Gamma_n(1)\ \cdots\ \Gamma_n(h_0)]\) | \(\mathbb L_n=\mathcal G_n\mathcal G_n^*\); row control yields the beyond-rank square. |
| lag-product error \(\epsilon_n\), Theorem 1 | sampling error inside 'temp' | one component of \(d_n\) | Parent \(\epsilon_n\) excludes moving-centre, connector, frame, mask, discretisation, and target-defect channels. |
| no named row norm | none | \(d_n^2=\sum_h\|\widehat\Gamma_n(h)-\Gamma_n(h)\|_{\rm op}^2\) | Canonical direct-sum row error; it gives \(\widehat\lambda_{r+1,n}\le d_n^2\). |
| no named row size | none | \(A_{2,n}^2=\sum_h\|\Gamma_n(h)\|_{\rm op}^2\) | Needed because squaring the row amplifies error by signal size. |
| operator perturbation \(O_p(c_n^{1/2}+\epsilon_n)\) schematically | perturbation of 'pd' | \(\eta_n=2A_{2,n}d_n+d_n^2\) | Exact deterministic assembly bound. Do not replace \(\eta_n\) by \(d_n\) when \(A_{2,n}\) grows. |
| exact lag-factor target | imposed | \(\zeta_n^2=\sum_h\|\Gamma_n(h)-A_nC_{f,n}(h)A_n^*\|_{\rm op}^2\) | Paper 1 makes misspecification explicit. |

### Rate translation

The parent’s Theorem 1 is schematically

\[
\text{loading error}
=O_p\!\left(\frac{c_n^{1/2}+\epsilon_n}{\kappa^2}\right).
\]

The project’s exact-target robust theorem is

\[
\|\sin\Theta(\widehat{\mathcal S}_{X,n},\mathcal S_{X,n})\|_{\rm op}
=O_p\!\left(\frac{\eta_n}{\Delta_n}\right),
\qquad
\eta_n=2A_{2,n}d_n+d_n^2,
\]

with \(d_n=O_p(n^{-1/2}+\ell_n)\) in the bounded-energy fixed-lag route. The displays agree in order only after fixing \(A_{2,n}\), imposing exact rank, and using \(\Delta_n\ge s_n^2=\kappa^2\). They are not notation-identical.

## 5. Rank selection

| Object | Definition | Actual action | Project status |
|---|---|---|---|
| Parent raw ratio | Eq. (5): \(\widehat r=\arg\min_{1\le i\le R}\widehat\lambda_{i+1}/\widehat\lambda_i\) | Unridged search to cap \(R\) | Not justified by Proposition 3’s displayed rates alone. The witness \(\operatorname{diag}(1,d_n^2,0)\) satisfies them and selects rank two. This is non-derivability, not claimed practical failure. |
| Code raw ratio | 'BWS_util.R:305-306': 'evals[2:r] / evals[1:(r-1)]'; 'which.min' | Input 'r' is extraction and search cap; output lies in \(1,\ldots,r-1\) | Parent parity comparator only. No explicit \(r=1\) or zero-denominator rule. |
| Threshold | project canon | \(\widehat r_n^{\rm thr}=\#\{j:\widehat\lambda_{j,n}>\tau_n\}\) | Proved if \(d_n^2=o_p(\tau_n)\), \(\tau_n=o(\Delta_n)\), and \(\eta_n=o_p(\Delta_n)\). |
| Ridged ratio | project canon | \((\widehat\lambda_{j+1,n}+\tau_n)/(\widehat\lambda_{j,n}+\tau_n)\), smallest-index tie rule | Proved with nonzero-spectrum ratio separation; removes post-rank \(0/0\) and zero-ratio pathologies. |

Parent Table 2 remains a valid N-00 empirical target: the raw ratio succeeds above 80% at \(n=100\) and about 100% at \(n=200\) in those designs. The correction says only that this does not follow from the displayed rates without extra post-rank separation.

## 6. Complete 'main_func.R' symbol ledger

Every formal parameter, returned field, and substantive local object is below. Ephemeral loop and linear-algebra workspaces are explicitly grouped.

### 'subspace_d' ('main_func.R:5-60')

| Symbol | Meaning | Canonical counterpart/rule |
|---|---|---|
| 'U', 'V' | vector/matrix representatives of two subspaces | loading-space representatives; compare spans |
| 'type = \"sine-theta\"' | maximum sine of principal angles for equal multi-column ranks | \(\|\sin\Theta(U,V)\|_{\rm op}\) in the matrix branch. The vector branch assumes unit inputs, does not take an absolute inner product, and is therefore sign-sensitive rather than a true one-dimensional subspace metric. |
| 'type = \"trace-projection\"' | \(\{1-\operatorname{tr}(P_1P_2)/\max(q_1,q_2)\}^{1/2}\) | normalized chordal/projection loss, not the canonical operator sine-theta norm |
| 'Q', 'Q1', 'Q2', 'P1', 'P2', 'q1', 'q2', 'res' | QR bases, projectors, ranks, return scalar | computation only |
| 'Inf' return | unequal-rank/type sentinel | diagnostic, not a mathematical unequal-rank distance |

### 'main_BWS' ('main_func.R:72-183')

| Symbol | Meaning | Canonical counterpart/boundary |
|---|---|---|
| 'x' | \(n\times m\times m\) SPD observations | \(X_{t,n}\) |
| 'r' | requested loading columns and cap passed to 'LYB_fm' | truncation/search cap; not automatically dynamic rank |
| 'test_size' | held-out tail | evaluation split; training size \(N=n-\text{test_size}\) |
| 'h' | maximum included lag | \(h_0\) |
| 'batch_size', 'max.iter' | mean-optimizer controls | numerical controls, not statistical rates |
| input/output 'mu_hat' | optional/reused or fitted BW centre | fixed-centre \(\widehat\mu\) |
| 'true_A', local 'A' | simulation loading truth | representative of declared \(A_n\) |
| 'true_mu' | simulation centre truth | \(\mu\) |
| 'fraction' | FVU if true, squared-error sums if false | evaluation switch |
| 'return_predictions' | additionally return final rank-\(r\) reconstructions | output switch |
| first and reassigned 'n', plus 'n_test' | total, training, test sizes | report separately |
| local 'p' | SPD order | \(m\); tangent dimension \(m(m+1)/2\) |
| 'Euclidean_mean' | entrywise training mean | Frobenius baseline, not BW Fréchet centre |
| 'x_test'; reassigned 'x' | test/training arrays | split samples |
| first 'model = rfm_bws(...)' | parent RFM fit | fixed-centre lag-operator estimator |
| 'V' | coordinate loading matrix | representative of requested \(\widehat{\mathcal S}_{X,n}\) |
| 'Factors' | estimated RFM scores | \(\widehat f_t=V^{\mathsf T}\widehat z_t\) |
| 'E', 'E_lyapunov' | BW basis and Lyapunov dual helper | frame and coordinate helper |
| 'r_hat_RFM' | tangent-fit raw ratio | parent parity selector |
| 'z_bar' | tangent-coordinate sample mean before demeaning | finite-sample/numerical intercept; population ideal is zero |
| 'transported_V', 'v_to_matrix', 'transport_matrix' | connector-aligned loading columns/workspace | typed loading transport to truth fibre |
| 'subspace_dist' | attempted first-\(i\) loading-space distances | Only the final \(i=r\) entry is usable when 'true_A' has \(r\) columns: earlier calls compare unequal column counts and 'subspace_d' returns 'Inf'. |
| 'dta$mu' at line 110 | hidden/global simulation centre used for coordinates | simulation truth; not a formal argument |
| 'res1', 'res2' | RFM BW/Frobenius evaluation vectors | evaluation only; BW comparison is secondary under [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]] |
| 'x_vector' | upper-triangle raw SPD vectorization | linear benchmark input, not log coordinates |
| 'm' | observation loop index | bookkeeping |
| second 'model = LYB_fm(...)' | linear factor benchmark | overwrites local RFM object after outputs are copied |
| 'r_hat_LYB', 'V_LYB' | benchmark raw ratio and loadings | comparator outputs |
| 'res3', 'res4' | benchmark BW/Frobenius evaluation vectors | evaluation only; the two branches can score different matrices because only BW projects to SPD |
| 'FVU_RFM_BWS', 'FVU_RFM_Euc', 'FVU_LYB_BWS', 'FVU_LYB_Euc' | returned rank curves | evaluation quantities, not convergence rates |
| 'loading_dist' | returned 'subspace_dist' | simulation diagnostic |
| 'RFM_xhat', 'LYB_xhat' | final rank-\(r\) returned reconstructions | final loop rank only |

### 'main_sphere' ('main_func.R:192-272')

| Symbol | Meaning | Canonical counterpart/boundary |
|---|---|---|
| 'x' | list of sphere arrays | \(X_{t,n}\in\prod_{j=1}^dS^{q_j-1}\) |
| 'r', 'test_size', 'h', 'max.iter', 'true_A', 'true_mu', 'fraction' | same roles as BW | same rank-cap and split warnings |
| 'tau' | sphere mean-gradient step | numerical control |
| 'true_E' | true component tangent bases | simulation alignment frame |
| 'n', 'n_test' | training/test sizes | \(N_n,N_{\rm test}\) |
| 'd' | product-component count | not manifold dimension |
| 'qs' | ambient sphere dimensions \(q_j\) | tangent dimension \(\sum_j(q_j-1)\); raw benchmark dimension \(\sum_jq_j\) |
| 'x_test' and reassigned component arrays | test/training product samples | split samples |
| 'Euclidean_mean' | ambient component means | Euclidean baseline, not generally sphere-valued |
| first 'model = rfm_sphere(...)' | product-sphere RFM | parent fixed-centre estimator |
| 'V', 'Factors', 'mu_hat', 'E', 'r_hat_RFM' | loadings, scores, centres, bases, raw ratio | same intrinsic roles/caveats as BW |
| 'transported_V', 'subspace_dist', 'idx', 'temp' | transported diagnostic and component workspace | connector-aligned span comparison |
| 'res1', 'res2' | RFM sphere/Euclidean evaluation | comparison metrics |
| 'x_vector' | concatenated raw ambient coordinates | linear benchmark, not tangent coordinates |
| second 'model = LYB_fm(...)', 'r_hat_LYB', 'res3', 'res4' | benchmark fit, selector, evaluation | comparator outputs |
| returned 'mu_hat', 'FVU_RFM_Sphere', 'FVU_RFM_Euc', 'FVU_LYB_Sphere', 'FVU_LYB_Euc', 'loading_dist', 'r_hat_RFM', 'r_hat_LYB' | top-level fields | fixed-centre reproduction objects |
| loop indices 'i', 'j' | rank/component counters | bookkeeping |

## 7. Supporting API and estimator locals

| Function/object | File:line | Canonical role | Important distinction |
|---|---:|---|---|
| 'geod_BWS_core', 'geod_BWS' | BWS_util.R:6, :14 | BW distance | Direct square root of trace radicand; pinned parity path has no zero clip. |
| 'Exp_BWS_core', 'Exp_BWS' | :51, :60 | BW exponential | tangent first, base second |
| 'Log_BWS_core', 'Log_BWS' | :80, :96 | BW logarithm | point first, base second; uses nonsymmetric products and 'sqrtm' |
| 'log_vec_construct' | :114 | coordinates of \(\log_Mx\) | produces \(z_{t,E}\) code matrix |
| 'log_to_tangent', 'tangent_in_E' | :159, :178 | \(J_E\) and coordinate analysis | tangent/coordinate conversions |
| 'symmetric_to_vector', 'vector_to_symmetric' | :196, :200 | raw upper-triangle encoding | not BW tangent coordinates; not Frobenius-isometric without off-diagonal weights |
| 'is.spd', 'project_to_SPD' | :208, :220 | domain check/benchmark repair | projection changes a forecast |
| 'mean_on_BWS' | :230 | empirical BW centre routine | 'rfm_bws' uses tau .5, tol -1, and fixed iteration budget; first-observation initialization; stochastic when batched |
| 'LYB_fm' | :271 | coordinate lag-operator factor estimator | builds row products, assembled operator, loadings, scores, residuals, raw ratio |
| 'predict_fm' | :313 | coordinate projection plus intercept | reconstruction, not temporal forecasting |
| 'Christoffel_BWS_core', 'Christoffel_BWS', 'pt_bws' | :332, :342, :368 | connection/numerical parallel transport | used for simulation comparison, not model fitting |
| 'tan_basis_bws' | :386 | BW orthonormal tangent basis | repeated eigenvalues allow basis rotations |
| 'rfm_bws' | :439 | parent BW RFM | centre \(\to\) basis \(\to\) logs \(\to\) 'LYB_fm' |
| 'Frac_Var_bws' | :476 | RFM reconstruction score curve | 'xhat' is final rank reconstruction |
| 'Frac_Var_LYB' | :570 | linear benchmark score curve | SPD projection only on BW branch |
| 'Frac_Var_ora' | :663 | simulation oracle curve | consumes DGP truth |
| 'VAR1' | :748 | OLS VAR(1) with intercept | separate forecast model |
| 'dyn_RFM' | :762 | expanding-window RFM+VAR forecast | first centre reused; loading, factors, intercept, VAR refitted |
| 'dyn_LFM' | :806 | expanding-window LFM+VAR forecast | may output indefinite matrices |
| sphere geometry, 'tan_basis_sphere', 'q_index', 'rfm_sphere', 'Frac_Var_sphere' | sphere_util.R | product-sphere counterparts | sphere cut-locus/uniqueness conditions differ from BW |

### 'LYB_fm' locals and returns

| Code object | Formula/meaning | Canonical name |
|---|---|---|
| 'mean' | column mean before demeaning | coordinate intercept |
| demeaned 'x' | \(z_t-\bar z\) | centred feasible coordinates |
| 'H = h + 1' | common starting index | indexing offset |
| 'temp' | \(n^{-1}\sum_{t=h+1}^nz_tz_{t-i}^{\mathsf T}\) | coordinate \(\widehat\Gamma_n(i)\) |
| 'pd' | \(\sum_i\text{temp}_i\text{temp}_i^{\mathsf T}\) | coordinate \(\widehat{\mathbb L}_n\) |
| 'model', 'Evec', 'evals' | eigendecomposition of 'pd' | empirical eigenvectors/eigenvalues |
| 'V' | first 'r' eigenvectors | requested leading-space representative |
| 'f_hat' | \(xV\) | factor scores |
| 'e_hat' | \(x-f_{\rm hat}V^{\mathsf T}\) | coordinate residuals |
| 'fitted.val' | \(f_{\rm hat}V^{\mathsf T}\) | coordinate reconstruction |
| 'ratios', 'r_hat' | raw consecutive ratios and minimizing index | parent parity selector |

## 8. Simulation and APP-FIN names

| Code name | Meaning | Project reporting name/rule |
|---|---|---|
| 'num_sim = 300' | Monte Carlo replicates | \(B=300\) |
| simulation 'p in {5,10}' | SPD order | \(m\in\{5,10\}\), not tangent dimension |
| simulation 'r = 10', true rank 5 | extraction/ratio cap and DGP rank | \(R^{\rm cap}=10\), \(r_0=5\) |
| simulation 'n in {50,100,200}', test 200 | training/test sizes | \(N\in\{50,100,200\}\), \(N_{\rm test}=200\) |
| 'dta', 'dta$mu', 'dta$A', 'dta$Factors' | generated data and truth | DGP object, centre, loading representative, factors |
| 'RFM_res', 'LFM_res' | application forecast outputs | RFM+VAR and raw-matrix LFM+VAR |
| APP-FIN 'q = 12' | matrix order/assets | \(m=12\), tangent dimension 78 |
| APP-FIN RFM 'r=2', LFM 'r=1' | imposed capacities | unmatched model capacities, not estimated ranks |
| 'RFM_xhat', 'LFM_xhat', LOCF, EWMA | covariance forecasts | methods evaluated under predeclared proxy-robust primary losses |
| 'BWS_errors', 'Euc_errors', 'risk_error' | BW, Frobenius, GMV-risk errors | legacy outputs; BW is not a proxy-robust primary score, Frobenius is |
| 'FVU_*' | fraction-unexplained curves | metric-specific reconstruction curves, not universal \(R^2\) |

## 9. Normative translation checklist

1. Rename BW code 'p' to matrix order \(m\), then compute \(p_n=m(m+1)/2\).
2. Separate dynamic rank \(r_n\), extraction size, and selector cap.
3. State whether \(n\) is total, training, lag-pair, or test size.
4. Translate 'temp' to \(\widehat\Gamma_n(h)\) before 'pd' to \(\widehat{\mathbb L}_n\); retain code normalization and tail indexing.
5. Translate loading matrices to spans. Use \(\mathcal S_{X,n}=\operatorname{ran}\mathbb L_n\) unless \(Q_n\succ0\) is established.
6. Translate \(\kappa\) to \(s_n\) only in the stationary exact-factor case. Davis–Kahan uses \(\Delta_n\); substitute \(s_n^2\) only after proving the bound.
7. Keep \(d_n,A_{2,n},\eta_n,\zeta_n\) separate: row error, row size, assembled error, target defect.
8. Treat 'r_hat' as the raw-ratio parity comparator. Use threshold/ridged selection for theorem-backed claims.
9. Distinguish reconstruction ('predict_fm', 'Frac_Var_*') from forecasting ('dyn_RFM', 'dyn_LFM' plus VAR).
10. State the scoring target; a geodesic reconstruction score is not interchangeable with a proxy-robust covariance forecast score.

This checklist is normative for notation only. Any translation that changes an assumption, norm, target, or rate is a new mathematical claim and belongs in the canonical proof ledger.
