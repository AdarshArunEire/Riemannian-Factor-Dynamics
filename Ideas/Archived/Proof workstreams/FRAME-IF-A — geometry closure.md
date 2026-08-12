---
type: proof-dossier
title: FRAME-IF-A — geometry closure
status: noncanonical-workstream
scope: FRAME-IF-POLY geometry and restricted closure; Paper 2 excluded
---

# FRAME-IF-A — geometry closure

> The authoritative FRAME-DB brief and archived lead/A/B/C records were reread. This dossier closes the geometry track and proves the strongest nontrivial curved replacement. No canonical file is edited.

## 0. Verdict

The earlier claim that the generic growing-dimensional FRAME-IF-POLY lemma follows merely from Hilbert concentration plus formal differentiation is **SUPERSEDED**. The argument below does not prove a generic impossibility theorem: full inverse-Karcher operator estimation is not logically necessary if only a low-complexity composed action is needed. Sections 1--9 prove the finite-parameter route; §10 proves the dimension-uniform geometry consumed by the Gate-A FRAME-2P-U theorem in B §11/C §13.

A genuinely curved restricted replacement is **PROVED UNDER EXPLICIT ASSUMPTIONS** for a fixed-dimensional \(k\)-parameter mean-path family on a known bounded-geometry manifold, using the actual geodesic polygon, fixed anchor, and three independent colors. It is common-gauge equivariant and has
\[
\widehat{\mathfrak T}^{\,1s}-\mathfrak T
=(P_E-P)\varphi_E+(P_V-P)\varphi_V
+O_p(Mn^{-1}+M^{-2})+o_p(n^{-1/2}).
\tag{0.1}
\]
For \(M\asymp\ell_n^{-2/3}=n^{2/7}\), \(Mn^{-1}=n^{-5/7}\) and \(M^{-2}=n^{-4/7}\), both \(o(n^{-1/2})\). This is oracle order with a generally different influence law.

## 1. Typed polygon and connector calculus

Let \(M\) be a known \(d\)-dimensional Riemannian manifold and
\(\mu_\theta:[0,1]\to M\), \(\theta\in\Theta\subset\mathbb R^k\), a known \(C^3\) map. Fix the anchor:
\[
\mu_\theta(0)=q_0\quad\text{for all }\theta.
\tag{1.1}
\]
Put \(v_j=j/M\), \(q_j(\theta)=\mu_\theta(v_j)\), and let
\[
P_j(\theta):T_{q_j(\theta)}M\to T_{q_{j+1}(\theta)}M
\]
be PT along the unique geodesic chord. For \(u\in[v_j,v_{j+1}]\), let
\[
F_{\theta,M}(u):T_{\bar\mu_{\theta,M}(u)}M\to H_0:=T_{q_0}M
\]
be inverse PT along all completed chords followed by the partial chord. Every source fibre is radially identified before differentiation.

For a variation \(a\mapsto\theta+ab\), the cell derivative is
\[
DP_j[b]W=-E_{j+1}P_jW+P_jE_jW
+\int_0^1P_{1\leftarrow r}R(T_j(r),J_{j,b}(r))P_{r\leftarrow0}W\,dr,
\tag{1.2}
\]
where \(J_{j,b}\) is the endpoint Jacobi field with
\(J_{j,b}(0)=D_\theta q_j[b]\),
\(J_{j,b}(1)=D_\theta q_{j+1}[b]\), and \(E_j=0\) for radial connectors. This uses
\(R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}\).
The derivative of the ordered product is
\[
D(P_{j}\cdots P_0)[b]
=\sum_{a=0}^{j}P_j\cdots P_{a+1}\,DP_a[b]\,P_{a-1}\cdots P_0.
\tag{1.3}
\]
For a partial cell, replace the last integral's upper endpoint by the observed fractional position. Thus endpoints and partial cells are included. **PROVED.**

### Lemma 1 — internal-vertex \(M^{-1}\) derivative

Let \(z=(z_1,\ldots,z_{M-1})\), \(z_j\in T_{q_j}M\), perturb polygon vertices by
\(\operatorname{Exp}_{q_j}(az_j)\), and keep \(q_0\) fixed. Assume:

1. chord lengths are at most \(L/M\);
2. curvature and the first two endpoint-Jacobi/PT derivatives are bounded by \(C_G\);
3. observation Log/base derivatives through order two are bounded by \(C_L\);
4. \(\|Y_t\|\le R\), fixed lag count, and every cell contains at most \(C_Dn/M\) retained design points.

For an internal vertex \(j\), after radial identification, the terminal endpoint generator of cell \(j-1\) is the same typed operator as the initial generator of cell \(j\), with opposite product-rule signs. It therefore cancels. Only the curvature integrals on cells \(j-1,j\) remain, each over length \(O(M^{-1})\). Hence
\[
\sup_u\|D_{z_j}F_M(u)\|_{\rm op}\le C/M.
\tag{1.4}
\]
For \(u\) before cell \(j-1\) the derivative is zero; inside either adjacent cell use the corresponding partial integral, also \(O(M^{-1})\); after cell \(j\) the two full curvature integrals are transported isometrically. At \(j=0,M\), one uncancelled endpoint generator remains. The fixed-anchor condition eliminates \(j=0\); the terminal vertex affects only the final cell and is excluded from the interior parameter or separately given weight \(O(M^{-1})\).

The connector-identified base-log derivative from \(z_j\) is supported on the two adjacent cells, hence on \(O(n/M)\) observations. Averaging the bounded lag-product derivative over \(N_h\asymp n\) gives
\[
\|D_{z_j}\mathfrak T_{M,h}\|_{\rm HS}\le C/M.
\tag{1.5}
\]
The same result holds when \(t\) or \(t-h\) lies in a partial adjacent cell; a fixed lag changes the count by \(O(h_0)\), absorbed into \(C/n\le C/M\). A common anchor-coordinate rotation conjugates both sides and preserves the norm. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

### Lemma 2 — bilinear polygon remainder

Under the same assumptions and uniform third generated-map bounds, the Hessian blocks of the complete masked lag functional satisfy
\[
\|D^2_{jj}\mathfrak T_M\|+\|D^2_{j,j\pm1}\mathfrak T_M\|\le C,
\qquad
\|D^2_{jk}\mathfrak T_M\|\le C/M^2\quad(|j-k|>1).
\tag{1.6}
\]
Reason: local diagonal/adjacent blocks contain second base-log and cell endpoint derivatives on \(O(n/M)\) rows plus at most two cell second variations; bounding them by \(C\) is conservative. Nonadjacent vertices interact only through products of two first PT derivatives, each \(O(M^{-1})\). Therefore
\[
\|D^2\mathfrak T_M[z,z]\|_{\oplus{\rm HS}}
\le C\sum_j\|z_j\|^2
+{C\over M^2}\Big(\sum_j\|z_j\|\Big)^2
\le C M\|z\|_{\rm RMS}^2.
\tag{1.7}
\]
Taylor's theorem gives the required
\[
\|\mathfrak T_M(z)-\mathfrak T_M(0)-D\mathfrak T_M[z]\|_{\oplus{\rm HS}}
\le C M\|z\|_{\rm RMS}^2.
\tag{1.8}
\]
The true \(C^2\) path/chord lens contributes \(CM^{-2}\). **PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 2. Fixed-observation, Karcher, and lag-law derivatives

For the triangular array put (O_{n,t}=(u_t,X_t)) and use the observable squared-distance score
\[
\psi_{n,t}(\theta)={1\over2}D_\theta d^2\{X_t,\mu_\theta(u_t)\},
\qquad \Psi_n(\theta)=|I_n|^{-1}\sum_{t\in I_n}E\psi_{n,t}(\theta),
\tag{2.1}
\]
with \(\Psi_n(\theta_0)=0\) and
\[
A_n:=-D_\theta\Psi_n(\theta_0),
\quad \sigma_{\min}(A_n)\ge c_A>0.
\tag{2.2}
\]
The parameter influence is
\[
IF_{n,t}=A_n^{-1}\psi_{n,t}(\theta_0).
\tag{2.3}
\]
For a fixed observation \(x\),
\[
D_\theta\{F_{\theta,M}(u)\log_{\bar\mu_{\theta,M}(u)}x\}[b]
=\Omega_{\theta,M,u}[b]Y
-F_{\theta,M}(u)H(\bar\mu_{\theta,M}(u),x)D_\theta\bar\mu_{\theta,M}(u)[b],
\tag{2.4}
\]
where \(\Omega\) is generated by (1.2)–(1.3). The direct lag-law derivative is separate:
\[
D_P\Gamma_h[s]
=E\{D_\theta(Y_t\otimes Y_{t-h})[IF_\theta s]\}
+E\{(Y_t\otimes Y_{t-h})s_{t,t-h}\}.
\tag{2.5}
\]
Thus inverse Karcher, base-log, polygon PT/Jacobi, connector, partial-cell, and lag-law terms are all typed without double counting. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 3. Three-fold observable estimator

Let \(g=m_0+h_0+1\) and split time into superblocks of length \(12g\). In block \(j\), take the core indices
\[
t^s_{T,j}=12gj+g,\quad t^p_{T,j}=12gj+3g,
\quad t^s_{V,j}=12gj+6g,\quad t^p_{E,j}=12gj+9g.
\tag{3.1}
\]
Delete boundary blocks and, for a lag-(h) pair core, retain both \(t\) and \(t-h\). If \(\mathcal U_t\) denotes the underlying innovation, define \(\mathcal F_T\), \(\mathcal F_V\), and \(\mathcal F_E\) from all innovations within distance \(m_0\) of their respective score/pair cores. The gaps in (3.1) make these sigma-fields independent. Each core has cardinality comparable to \(n\).

On the T-score core, \(\widehat\theta\) is the interior root of
\[
|T_s|^{-1}\sum_{t\in T_s}\psi_{n,t}(\widehat\theta)=0,
\qquad
\widehat A=-|T_s|^{-1}\sum_{t\in T_s}D_\theta\psi_{n,t}(\widehat\theta).
\tag{3.2}
\]
Work on \(\mathcal E_A=\{s_{\min}(\widehat A)\ge c_A/2\}\), whose probability tends to one. The T-pair core estimates
\(\widehat K_h=D_\theta\widehat{\mathfrak T}_{T_p,M,h}(\widehat\theta)\); V evaluates
\(\widehat\Psi_V=|V_s|^{-1}\sum_{t\in V_s}\psi_{n,t}(\widehat\theta)\); E evaluates \(\widehat{\mathfrak T}_{E_p,M,h}(\widehat\theta)\). All derivatives are of the known fitted Exp/Log/PT/Jacobi composition.

Because score and pair masks are different objects, define one finite-array pair target
\[
\mathfrak T_{n,M,h}(\theta)=|E_{p,h}|^{-1}\sum_{t\in E_{p,h}}E\,Z_{n,t,h,M}(\theta).
\tag{3.3}
\]
Require phase balance of the T- and E-pair expectations and derivatives up to \(\rho_{mask,n}=o(n^{-1/2})\), or cyclically average the four role rotations on disjoint macroblocks, in which case (3.3) is their exact common average. This is the masked target throughout.

Define
\[
\boxed{
\widehat{\mathfrak T}^{\,1s}_{M,h}
=\widehat{\mathfrak T}_{E,M,h}(\widehat\theta)
+\widehat K_h\widehat A^{-1}\widehat\Psi_V(\widehat\theta).}
\tag{3.4}
\]
The sign follows \(D_\theta\Psi_n=-A_n\):
\(D_\theta\{\mathfrak T+KA^{-1}\Psi\}[b]=Kb+KA^{-1}(-Ab)=0\).
Everything in (3.1) is observable. No true centre, frame, anchor alignment, \(e,\Omega,\Gamma\), or true ribbon is used. Under a common anchor basis change \(Q\), both terms conjugate by \(Q\). **PROVED.**

## 4. Restricted curved closure theorem

Assume:

1. \(d,k,h_0,m_0\) are fixed; \(M\) is known with the geometry bounds of §1;
2. \(\theta_0\) is interior, (2.1) holds, and \(\psi\), \(A\), \(K\), Exp, Log, PT, Jacobi, and lag products have uniformly bounded derivatives/moments through the orders used;
3. the exact cores, boundary deletion, sigma-fields, and common masked target of Section 3 are used;
4. \(\widehat\theta-\theta_0=O_p(n^{-1/2})\),
   \(\widehat A-A=O_p(n^{-1/2})\), and
   \(\widehat K-K=O_p(n^{-1/2})\);
5. oracle pair rows and validation scores obey fixed-dimensional finite-memory root-\(n\) concentration;
6. either the finite-array local law is exact, or its coupling error is \(O(n^{-a})\) for \(a>1/2\), and \(\rho_{mask,n}=o(n^{-1/2})\).

Then conditional Taylor expansion, (1.8), and fold independence give
\[
\begin{aligned}
\widehat{\mathfrak T}^{\,1s}_{M}-\mathfrak T_{n,M}(\theta_0)
={}&\bigoplus_{h\le h_0}{1\over |E_{p,h}|}\sum_{t\in E_{p,h}}
 \{Z_{n,t,h,M}(\theta_0)-EZ_{n,t,h,M}(\theta_0)\}\\
&+K_nA_n^{-1}{1\over|V_s|}\sum_{t\in V_s}\psi_{n,t}(\theta_0)
+O_p(Mn^{-1})+o_p(n^{-1/2})+O(n^{-a})+\rho_{mask,n}.
\end{aligned}
\tag{4.1}
\]
On \(\mathcal E_A\), the previously suppressed coefficient products obey
\[
\|(\widehat K-K_n)\widehat A^{-1}\widehat\Psi_V\|=O_p(n^{-1}),
\qquad
\|K_n(\widehat A^{-1}-A_n^{-1})\widehat\Psi_V\|=O_p(n^{-1}).
\tag{4.2}
\]
Replacing the population smooth-path row by the polygon target adds \(O(M^{-2})\):
\[
\|\mathcal R_n\|_{\oplus{\rm HS}}
=O_p(Mn^{-1}+M^{-2}+n^{-1})+o_p(n^{-1/2})+O(n^{-a})+\rho_{mask,n}.
\tag{4.3}
\]
Both empirical rows are \(O_p(n^{-1/2})\) in direct-sum HS norm. With
\(M\asymp n^{2/7}\), (4.3) is \(o_p(n^{-1/2})\).
The estimator therefore closes FRAME-IF-POLY on this genuinely curved restricted class. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

The leading validation influence generally changes the known-centre oracle law. This theorem proves oracle order, not oracle equivalence. The APP-B row assembly then yields the root-\(n\) loading numerator and \(O_p(n^{-1})\) null spectrum under its separate GLO, target, energy, and actual-gap assumptions. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

Precisely, after one common anchor conjugation, if \(d_n\) is the direct-sum HS row error and \(A_{2,n}\) the oracle row norm, then
\[
\|\widehat{\mathbb L}-\mathbb L\|_{op}\le 2A_{2,n}d_n+d_n^2.
\tag{4.4}
\]
Loading-space recovery additionally divides this numerator by the actual eigengap \(\Delta_n\); no operator-energy substitute for the HS frame coefficient and no undeclared uniform gap is used. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 5. Nonempty genuinely curved class

Use the explicit product-coordinate producer proved in FRAME-IF-C §§2--5. The known manifold is
\(M=\mathbb H^2(-1)\times\mathbb R\). Its hyperbolic centre follows a \(C^4\) nongeodesic circle arc with a scalar radial-drift parameter \(\theta\), while its Euclidean centre coordinate is also \(\theta\). For bounded Rademacher noise \(\eta_t\), the raw observation satisfies

\[
(X_t)_{\mathbb R}=\theta+\eta_t.
\tag{5.1}
\]

Hence the observable score is \(\psi_t(\alpha)=(X_t)_{\mathbb R}-\alpha\), the training root is the clipped training average, and \(A=-D_\alpha E\psi_t=1\) exactly. A bounded one-dependent rank-one tangent factor has lag row \(\Gamma_1=s\,a\otimes a\), \(s\ne0\), with serially white orthogonal Euclidean noise. The product is Hadamard, so the centre is unique; exact innovation reuse supplies the local proxy; central symmetry supplies GLO; deterministic superblock cores separated by \(m_0+h_0\) give independent training, validation, and evaluation sigma-fields and one stationary masked target.

FRAME-IF-C §5 computes the constant-curvature ribbon term and proves that its generator varies as \(u^2\) and does not commute with \(a\otimes a\). Thus \(K\ne0\) is genuinely non-rigid, rather than asserted generically. Every Exp, Log, PT, Jacobi, and product derivative used above is uniformly bounded on the fixed compact generated tube. This gives an explicit observable nonflat member of Theorem 4's class. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 6. Scope boundary for the growing-dimensional claim

Bounded Hilbert-valued scores yield dimension-free concentration of empirical means, but do not by themselves yield operator-norm concentration of empirical Hessians. The archived diagonal Rademacher operator example gives commuting, uniformly bounded positive operators whose empirical operator-norm fluctuation stays order one when the number of coordinates grows exponentially. Thus the proof step
\[
\|\widehat A-A\|_{\rm op}=O_p(n^{-1/2})
\quad\hbox{from bounded score energy alone}
\tag{6.1}
\]
is **DISPROVED**.

This does not disprove every possible growing-dimensional estimator: a future construction might estimate only the composed action \(KA^{-1}\psi\), using additional low-complexity structure and never estimating \(A^{-1}\) in full operator norm. No such structure appears in the displayed generic assumptions, and no such proof is supplied here. Accordingly the generic Gate-A closure claim is **SUPERSEDED**, while Theorem 4 is the final closed result. This dossier deliberately makes no stronger minimax assertion.

## 7. Gauge and mandatory edge audit

| Case | Verdict | Status |
|---|---|---|
| Common anchor rotation | (3.1) conjugates as a whole; no additive gap cost | PROVED |
| Internal vertex | derivative \(C/M\), including partial cells | PROVED UNDER EXPLICIT ASSUMPTIONS |
| Endpoint vertex | anchor fixed; terminal endpoint restricted or separately weighted \(C/M\) | PROVED UNDER EXPLICIT ASSUMPTIONS |
| One bad vertex | bilinear bound retains \(M\|z\|_{\rm RMS}^2\) | PROVED |
| High-frequency path | acceleration remains necessary for \(M^{-2}\); a length-only claim fails | DISPROVED |
| Flat Hilbert/common flat | curvature derivative vanishes; restricted theorem still valid but trivial frame channel | PROVED |
| Constant curvature/moving mean | hyperbolic example is nonempty and non-rigid | PROVED |
| Zero signal | correction coefficient vanishes but loading is unidentified | PROVED |
| CE-B5 | one-step \(K\)-term captures the noncommuting frame derivative; GLO alone does not | DISPROVED |
| High-dimensional bounded energy | full empirical Hessian operator recovery does not follow; action-only routes are not ruled out | SUPERSEDED |
| Arbitrary external frame | no centre-derived derivative | DISPROVED |
| Smooth versus polygon | theorem uses polygon; lens \(M^{-2}\) is explicit | PROVED |

## 8. Final conclusion

This pre-addendum conclusion established Gate B and is **SUPERSEDED** by §10 together with B §11/C §13:

- the earlier generic growing-dimensional disproof is **SUPERSEDED**: the available lower bound attacks full operator recovery, not every composed-action estimator;
- the fixed-dimensional known-geometry finite-parameter polygonal one-step estimator (3.1) is feasible and genuinely curved;
- its empirical influence row is root-\(n\), and its nuisance remainder is
  \(O_p(Mn^{-1}+M^{-2})=o_p(n^{-1/2})\) at \(M\asymp n^{2/7}\);
- all base-log, Karcher, ordered cell, connector, partial-cell, gauge, mask, and lag-law terms are included.

**PROVED UNDER EXPLICIT ASSUMPTIONS.**

## 9. First hostile cross-audit of B

| B claim | Geometric attack | Repair verified in frozen B | Status |
|---|---|---|---|
| every vertex derivative is \(C/M\) | the anchor moves the output fibre and an unmatched connector can be order one | B now uses radial fixed-fibre comparison, whose initial generator is zero; the first-cell curvature and base-log mass are \(C/M\) | PROVED UNDER EXPLICIT ASSUMPTIONS |
| adjacent-cell generators telescope | fold-specific connectors could leave boundary skews | B declares one connector convention and differentiates the ordered polygon, including completed and partial cells | PROVED UNDER EXPLICIT ASSUMPTIONS |
| positive barycentre stability controls the Richardson output | signed tangent recombination is not itself a barycentre | B assumes the explicit post-map has uniform first and second differentials and applies the chain rule to the three positive stages | PROVED UNDER EXPLICIT ASSUMPTIONS |
| the nonlinear row remainder is \(M(r_T^2+r_V^2)\) | the mixed second variation was omitted | B retains \(Mr_Tr_V\), the vertex maximum tube, and \(M^{-2}\) chord lens | PROVED UNDER EXPLICIT ASSUMPTIONS |
| common gauge costs no row error | only a genuinely common anchor motion may be quotiented | base row and derivative conjugate together; all time-varying curvature integrals remain in the correction | PROVED |
| two-path formula is observable | an oracle ribbon or true connector would invalidate it | every Jacobi/connector derivative is evaluated along the fitted geodesic polygon in the pilot anchor fibre | PROVED UNDER EXPLICIT ASSUMPTIONS |

The repaired B geometry is consistent with Lemmas 1--2. No unresolved geometric objection remains. This pass initially certified fixed-dimensional Gate B; the completion audit in §10 and the statistical audits in B §11/C §13 promote the combined theorem to Gate A.

## 10. Gate-A addendum: dimension-uniform geometry of FRAME-2P

Assume the HD-G constants themselves are uniform in (p): chord length (L/M); strong convexity; operator norms of curvature and the required first two Exp/Log/PT/Jacobi endpoint derivatives; the (C^2) Richardson post-map norm; fixed (h_0,m_0); design occupancy (Cn/M); and total tangent energy (E\|Y_t\|^2\le R^2). Then the geometric part of FRAME-2P is dimension-uniform.

Indeed, the shared endpoint generators cancel as typed operators, independently of dimension. Each remaining curvature integral has interval length (O(M^{-1})) and uniformly bounded operator integrand, while the base-log term occupies only (O(n/M)) lag rows. The Hilbert--Schmidt inequalities
\[
\|Av\otimes w\|_{HS}\le\|A\|_{op}\|v\|\|w\|,
\qquad
\|v\otimes Aw\|_{HS}\le\|A\|_{op}\|v\|\|w\|
\]
use total energy, not dimension. Consequently
\[
\max_j\|K_{n,j}\|\le C/M,
\qquad \sum_j\|K_{n,j}\|\le C,
\tag{10.1}
\]
with (C) independent of (p). The same operator-norm calculation gives diagonal/adjacent Hessian blocks (C) and nonadjacent blocks (C/M^2); Cauchy--Schwarz over the (M) vertices, not over tangent coordinates, yields
\[
\|D^2\mathfrak T_M[z,z]\|_{\oplus HS}
\le C M\|z\|_{RMS}^2,
\tag{10.2}
\]
again uniformly in (p). Radial fixed-fibre comparison proves (10.1) for the moving anchor; partial cells and the terminal vertex retain the same (M^{-1}) bound. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

The class is nonempty in growing dimension: take
\(\mathbb H^2(-1)\times\mathbb R^{p_n-2}\), embed the Section 5 producer in the hyperbolic factor plus one Euclidean coordinate, and set all added coordinates to zero (or give them noise with uniformly bounded total squared norm). Product curvature and all fixed-order generated-map operator constants are the maximum of the hyperbolic and Euclidean constants; the Hadamard squared-distance Hessian remains uniformly coercive; the rank-one lag row and its noncommuting hyperbolic curvature coefficient are unchanged. **PROVED UNDER EXPLICIT ASSUMPTIONS.**

This closes the dimension-uniform geometry audit. HD-G geometry alone does not imply the required stochastic producers—arbitrary-grid vertex maxima, first and mixed replacement stability of the three-stage Richardson map, finite-memory HS concentration, and sub-root-\(n\) mask/local-law defects. B §11 and C §13 separately prove the full theorem when those explicit uniform producers are imposed. Therefore the combined FRAME-2P-U result earns Gate A, while any claim that bounded energy alone supplies the package is **DISPROVED**.
