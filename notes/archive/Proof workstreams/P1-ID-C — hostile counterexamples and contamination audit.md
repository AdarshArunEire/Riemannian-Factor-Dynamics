---
type: archived-proof-dossier
title: P1-ID-C — hostile counterexamples and contamination audit
status: terminal-workstream-hostile-pass-ii-passed
last-audited: 2026-08-12
---

# P1-ID-C — hostile counterexamples and contamination audit

## 0. Verdict and notation

Gate 1 has a sharp split. Equality of known marginal laws plus uniqueness of their Fréchet means identifies the centre trivially as a law-functional. It does not identify temporal law, a factor/noise decomposition, or a split of a fixed-centre lag row. The nontrivial targets are therefore the full-law factor quotient, one-path recoverability, weakened-reference changes, and fixed-centre contamination.

For a real Hilbert space \(H\), write \(x\otimes y:v\mapsto\langle y,v\rangle x\). A lag row is
\[
\mathcal G=[S(1)\ \cdots\ S(h_0)]:H^{h_0}\to H,
\qquad \mathbb L=\mathcal G\mathcal G^*=\sum_{h=1}^{h_0}S(h)S(h)^*.
\]
Equality of \(\mathcal G\) or \(\mathbb L\) is never called equality of the observation law.

## 1. Gate 1 and information-boundary counterexamples

### C-1 — same marginals, different temporal laws

**Construction.** Take \(M=\mathbb R\) with its Euclidean metric and \(Q=\tfrac12(\delta_{-1}+\delta_1)\). Let \(X_t\) be iid with law \(Q\), while \(\widetilde X_t=V\) for every \(t\), where \(V\sim Q\).

**Audit.** Both processes are bounded, strictly stationary, supported in the global normal chart, and have every marginal equal to \(Q\). The squared-distance Fréchet functional is \(F_Q(x)=x^2+1\), so the unique Fréchet mean is \(0\) in both models. They may be represented with loading \(A=1\), rank one, no idiosyncratic noise, and factors \(f_t=X_t\) and \(\widetilde f_t=V\). The iid factor has flat spectral density and zero nonzero-lag covariance; the invariant factor has spectral measure \(\delta_0\) and covariance one at every lag. In particular,
\[
\mathbb P(X_0=X_1)=\tfrac12\ne1=\mathbb P(\widetilde X_0=\widetilde X_1).
\]
Thus \(\mathcal I_M\not\Rightarrow\mathcal I_J\). The failure is insufficient temporal information, not curvature. **Status: PROVED INTERNALLY.**

The converse cannot fail: equality of all finite-dimensional distributions includes the one-dimensional distributions. Any purported “vice versa” counterexample with equal full path law and different marginals is logically impossible.

### C-2 — same marginals and every second-order lag, different full laws

**Construction.** Again take \(M=\mathbb R\). Model I is an iid Rademacher sequence \(R_t\). For Model II, independently draw \(J\sim\mathrm{Unif}\{0,1,2\}\) and iid pairs \((U_k,V_k)\) of independent Rademacher variables. Partition \(\mathbb Z\) into blocks with starts \(J+3k\), and place
\[
(Z_{J+3k},Z_{J+3k+1},Z_{J+3k+2})=(U_k,V_k,U_kV_k).
\]

**Audit.** Randomising the block origin makes \(Z\) strictly stationary: a shift only changes the uniformly distributed phase and relabels blocks. Every coordinate is Rademacher. Any two coordinates in one block are independent, and coordinates in distinct blocks are independent, hence
\[
\mathbb E[Z_tZ_{t-h}]=0=\mathbb E[R_tR_{t-h}],\qquad h\ne0.
\]
Both laws have unique Fréchet mean zero and identical covariance rows at every lag, including variance one at lag zero. Yet
\[
\mathbb E[Z_tZ_{t+1}Z_{t+2}]=\tfrac13,
\qquad
\mathbb E[R_tR_{t+1}R_{t+2}]=0.
\]
Indeed, with probability \(1/3\), \(t\) is a block start and the product is \(U_kV_k(U_kV_k)=1\); in the other phases its expectation is zero. Thus even all covariance lags do not determine the full law. Model II is temporally uncorrelated “white noise” but not independent white noise. Any theorem using white noise must choose which meaning it needs. **Status: PROVED INTERNALLY.**

### C-3 — fixed-centre lag rows do not identify a drift/factor split

Take \(M=\mathbb R\), fixed anchor \(c_0=0\), and \(a>0\). Model D is deterministic, \(X_t=a\), and is described as fixed-anchor drift \(d_t=a\) with no factor. Model F is \(X_t=V\) for all \(t\), where \(V=\pm a\) with equal probability, and is described as a zero-mean invariant factor with no drift. For every \(h\ge1\), both have the exact uncentred fixed-anchor lag moment
\[
S(h)=\mathbb E[X_tX_{t-h}]=a^2.
\]
Their full laws and marginal centres differ, so they are **not** observationally equivalent under \(\mathcal I_J\) or \(\mathcal I_M\). They are equivalent only under \(\mathcal I_F(c_0)\), because their entire fixed-centre lag rows agree. Therefore \(\mathcal I_F(c_0)\) identifies only the contaminated row/operator, not its physical split. The failure is loss of information in the lag functional. **Status: PROVED INTERNALLY.**

## 2. Fréchet-mean and Log-domain boundaries

### C-4 — nonunique Fréchet means

Let \(M=S^1\) with unit geodesic metric and
\[
Q=\tfrac12\delta_{(1,0)}+\tfrac12\delta_{(-1,0)}.
\]
Writing a point on the upper semicircle by angle \(\theta\in[0,\pi]\),
\[
F_Q(\theta)=\tfrac12\theta^2+\tfrac12(\pi-\theta)^2,
\]
whose unique upper-semicircle minimiser is \(\pi/2\). The lower semicircle gives the second minimiser \(3\pi/2\), and there are no others. Hence the law identifies the two-point set \(\mathfrak M(Q)\), not a selected centre. Both minimisers are within distance \(\pi/2\) of the support, so their support Logs are unique; the ambiguity is genuinely failure of Fréchet uniqueness, not a Log artefact. **Status: PROVED INTERNALLY; this is the exact failure boundary of ID-1.**

### C-5 — a unique marginal mean does not license an arbitrary fixed Log

On \(S^1\), let \(Q=\delta_S\), where \(S\) is the antipode of \(N\). Its Fréchet mean is uniquely \(S\). If the imposed fixed anchor is \(c_0=N\), then \(\log_N(S)\) has the two values \(\pm\pi e\) and is not a function. Thus uniqueness of the true marginal mean does not imply that a misspecified fixed-anchor score is well-defined. ID-5 must explicitly assume that the observation support avoids \(\operatorname{Cut}(c_0)\), or specify a measurable branch and accept branch-dependent targets. **Status: PROVED INTERNALLY.**

## 3. Persistence, factor/noise, and rank attacks

### C-6 — invariant and near-zero components

The invariant process \(f_t=V\), \(V=\pm1\), is bounded, stationary, zero-mean, and has spectral measure \(\delta_0\). Every local or global sample average equals \(V\), so one path cannot average it to its ensemble mean. Shifting this random constant into a random intercept preserves the realised process, but the intercept is not a distinct deterministic unique Fréchet centre. Therefore this example attacks weakened centring/random-intercept identification, not the unique-marginal-centre theorem.

For the sharp near-zero boundary, let \(f^{(\rho)}\) be a variance-one stationary Gaussian AR(1) with covariance \(\rho^{|h|}\), \(0<\rho<1\). Its spectrum is continuous and has no atom at zero, so for each fixed \(\rho\), averages converge to zero in \(L^2\). For a window of length \(N\), choose \(\rho_N=1-N^{-2}\). Then
\[
\operatorname{Var}\!\left(N^{-1}\sum_{t=1}^N f_t^{(\rho_N)}\right)
=N^{-2}\sum_{i,j=1}^N\rho_N^{|i-j|}
\ge \rho_N^{N-1}\ge1-\frac{N-1}{N^2}\longrightarrow1.
\]
Every member has no zero-frequency atom, yet convergence is not uniform over the class. No-atom gives pointwise mean-square ergodicity; uniform recovery needs a quantitative exclusion of near-zero concentration. **Status: PROVED INTERNALLY.**

### C-7 — exact factor/noise reallocation and the minimum-dynamic-rank boundary

Let \(H=\mathbb R^2\). Let \(G_t\) be a stationary Gaussian AR(1) with nonzero lag covariance, and let \(W_{1t},W_{2t}\) be mutually independent iid Gaussian white noises, independent of \(G\). Define
\[
X_t=e_1G_t+e_2(W_{1t}+W_{2t}).
\]
Representation I has rank-one loading \(A=e_1\), factor \(G\), and iid noise \(e_2(W_1+W_2)\). Representation II has isometric loading \(\widetilde A=[e_1,e_2]\), factor \((G,W_1)^\top\), and iid noise \(e_2W_2\). The equalities hold pathwise; in each representation the factor and its residual noise are independent, and the residual is iid. Yet the declared ranks are one and two and the loading spans are \(\operatorname{span}(e_1)\) and \(\mathbb R^2\). The added direction has zero covariance at every nonzero lag. Thus a raw factor dimension/loading span is not identified unless every retained direction is dynamically active or one adopts the minimum dynamic rank
\[
r_{\rm dyn}=\dim\overline{\operatorname{span}}\{\operatorname{ran}\Gamma_X(h):h\in H_*\}
\]
for the declared lag set \(H_*\). Under two-sided factor/noise lag orthogonality, a genuinely persistent component cannot be moved into white noise without violating whiteness; only dynamically silent reallocation survives. **Status: PROVED INTERNALLY.**

### C-8 — the two cross-lag directions are distinct

Let \(\varepsilon_t\) be iid centred variance-one noise, \(f_t=\varepsilon_{t-1}\), and \(e_t=\varepsilon_t\). Marginally, both \(f\) and \(e\) are white. At lag one,
\[
\mathbb E[f_te_{t-1}]=1,
\qquad
\mathbb E[e_tf_{t-1}]=0.
\]
Consequently, declaring only one factor/noise cross-lag direction zero does not remove the other term from \(S(1)\). Independence of the two *processes*, rather than marginal whiteness of each, would remove both. **Status: PROVED INTERNALLY.**

### C-9 — one lag can be rank deficient while the lag row is complete

Let \(H=\mathbb R^2\), \(A=I_2\), and take independent innovations. Set
\[
f_{1t}=\epsilon_t+\theta\epsilon_{t-1},
\qquad
f_{2t}=\eta_t+\theta\eta_{t-2},\qquad \theta\ne0.
\]
Then
\[
\Gamma_f(1)=\operatorname{diag}(\theta,0),
\qquad
\Gamma_f(2)=\operatorname{diag}(0,\theta).
\]
Each lag matrix has rank one, but the row \([\Gamma_f(1)\ \Gamma_f(2)]\) has rank two. Any claim that a single included lag identifies the whole loading space is false without a full-rank condition at that lag; row completeness is the correct weaker condition. **Status: PROVED INTERNALLY.**

### C-10 — additive ranks can cancel

Take \(H=\mathbb R\), one included lag, drift moment \(M=m>0\), and a variance-\(2m\) stationary AR(1) factor with coefficient \(-1/2\). Its lag-one covariance is \(-m\), so the clean additive fixed-centre row is \(S(1)=M+\Gamma_f(1)=0\). Thus \(\operatorname{rank}(M+\Gamma_f(1))\) need not equal the sum, maximum, or union of the component ranks. Alignment/rank theorems require an orthogonal block structure, lag contrasts, or an explicit row nondegeneracy condition. **Status: PROVED INTERNALLY.**

## 4. Exact fixed-centre decomposition (ID-5 producer)

### 4.1 The universal fixed-Log identity on a manifold

Fix \(c_0\in M\). Assume \(X_{t,n}\notin\operatorname{Cut}(c_0)\) almost surely and \(\mathbb E\|\log_{c_0}X_{t,n}\|^2<\infty\). In the single Hilbert fibre \(H=T_{c_0}M\), define
\[
Z_{t,n}=\log_{c_0}X_{t,n},\qquad
b_{t,n}=\mathbb EZ_{t,n},\qquad
U_{t,n}=Z_{t,n}-b_{t,n}.
\]
For \(h\ge1\), with denominator \(n\), set
\[
\widehat S_n(h)=\frac1n\sum_{t=h+1}^n Z_{t,n}\otimes Z_{t-h,n},
\qquad
S_n(h)=\mathbb E\widehat S_n(h).
\]
Then, exactly,
\[
\boxed{
S_n(h)=D_{b,n}(h)+R_{U,n}(h),
}
\]
where
\[
D_{b,n}(h)=\frac1n\sum_{t=h+1}^n b_{t,n}\otimes b_{t-h,n},
\quad
R_{U,n}(h)=\frac1n\sum_{t=h+1}^n
\mathbb E[U_{t,n}\otimes U_{t-h,n}].
\]
Both population cross terms vanish because \(b_{t,n}\) is deterministic and \(\mathbb EU_{t,n}=0\) separately at every time. At sample level they do not vanish:
\[
\widehat S_n(h)=D_{b,n}(h)+R_{U,n}(h)+E_{n,h},
\]
with the exact centred sampling term
\[
E_{n,h}=\frac1n\sum_{t=h+1}^n
\left{
b_{t,n}\otimes U_{t-h,n}+U_{t,n}\otimes b_{t-h,n}
+U_{t,n}\otimes U_{t-h,n}
-\mathbb E(U_{t,n}\otimes U_{t-h,n})
\right}.
\]
No geometry approximation is used. However, \(b_{t,n}\) is the mean fixed-anchor **score**. On a curved manifold it need not equal \(\log_{c_0}\mu(u_t)\), even when \(\mu(u_t)\) is the unique marginal Fréchet mean. Calling \(b\) centre drift would therefore be an additional theorem or assumption. **Status: PROVED INTERNALLY.**

### 4.2 Exact nine-term affine score expansion

Suppose, as an exact model in one Hilbert fibre (in particular in Euclidean space or a declared common totally geodesic flat),
\[
Z_{t,n}=d_{t,n}+Af_{t,n}+e_{t,n},
\]
with deterministic \(d_{t,n}\in H\) and bounded \(A:\mathbb R^r\to H\). No centring or orthogonality is initially imposed. Define \(\langle C^{xy}_{n,h}\rangle=n^{-1}\sum_{t=h+1}^n\mathbb E[x_{t,n}\otimes y_{t-h,n}]\). Direct multiplication gives all nine population terms:
\[
\boxed{
\begin{aligned}
S_n(h)={}&
\langle C^{dd}_{n,h}\rangle
+\langle C^{df}_{n,h}\rangle A^*
+\langle C^{de}_{n,h}\rangle\\
&+A\langle C^{fd}_{n,h}\rangle
+A\langle C^{ff}_{n,h}\rangle A^*
+A\langle C^{fe}_{n,h}\rangle\\
&+\langle C^{ed}_{n,h}\rangle
+\langle C^{ef}_{n,h}\rangle A^*
+\langle C^{ee}_{n,h}\rangle.
\end{aligned}}
\]
Here the notation in a \(d,f\) term means the evident finite average, e.g.
\(
\langle C^{df}_{n,h}\rangle=n^{-1}\sum d_{t,n}\otimes\mathbb Ef_{t-h,n}
\), with the tensor interpreted between the appropriate spaces. The sample row has the identical nine-term expansion with expectations removed. Equivalently,
\[
\widehat S_n(h)=S_n(h)+E^{\rm samp}_{n,h},
\quad
E^{\rm samp}_{n,h}=\frac1n\sum_{t=h+1}^n
\{Z_{t,n}\otimes Z_{t-h,n}-\mathbb E(Z_{t,n}\otimes Z_{t-h,n})\}.
\]
Thus drift-factor cross terms vanish only if \(\mathbb Ef_{t,n}=0\) at every time (or the displayed averages cancel); drift-noise terms require \(\mathbb Ee_{t,n}=0\); factor-noise terms require both
\[
\mathbb E[f_{t,n}\otimes e_{t-h,n}]=0,
\qquad
\mathbb E[e_{t,n}\otimes f_{t-h,n}]=0;
\]
and the idiosyncratic term at an included lag requires \(\mathbb E[e_{t,n}\otimes e_{t-h,n}]=0\). Under these primitive restrictions the population identity reduces to
\[
S_n(h)=D_{d,n}(h)+A\Gamma_{f,n}(h)A^*.
\]
Even then, every empirical cross product remains inside \(E^{\rm samp}_{n,h}\); it is not identically zero. **Status: PROVED INTERNALLY; the historical schematic formula is valid only under these displayed restrictions.**

### 4.3 Geometry remainder outside a common flat

Let the truth be centred at a unique \(\mu(u_t)\), let
\[
V_{t,n}=\log_{\mu(u_t)}X_{t,n}=A_t f_{t,n}+e_{t,n},
\]
and assume all points lie in a common normal domain for \(\mu(u_t)\) and \(c_0\). Along a chosen unique connecting geodesic let \(P_t:T_{\mu(u_t)}M\to T_{c_0}M\) be parallel transport, and set
\[
d_t=\log_{c_0}\mu(u_t),
\qquad
g_{t,n}=\Phi_{\mu(u_t)\to c_0}(V_{t,n})-d_t-P_tV_{t,n}.
\]
This is an exact definition, yielding
\[
Z_{t,n}=d_t+(P_tA_t)f_{t,n}+P_te_{t,n}+g_{t,n}.
\]
If \(q_{t,n}=d_t+(P_tA_t)f_{t,n}+P_te_{t,n}\), the fixed-centre lag has the exact geometry remainder
\[
R^{\rm geom}_{n,h}=\frac1n\sum_{t=h+1}^n\mathbb E[
q_{t,n}\otimes g_{t-h,n}+g_{t,n}\otimes q_{t-h,n}+g_{t,n}\otimes g_{t-h,n}].
\]
It vanishes on a common convex flat with its affine parallel frame, because then \(\Phi(V)=d+PV\). On a general curved manifold it is not white noise and cannot silently be absorbed into \(e\). Consequently the clean affine ID-5 formula is exact only in a common flat/geodesic reduction, under an explicitly imposed fixed-score affine model, or after retaining \(R^{\rm geom}\). **Status: PROVED INTERNALLY.**

### 4.4 End, local-stationarity, and sampling terms

Assume \(d:[0,1]\to H\) is Lipschitz with \(\|d\|_\infty\le R\), Lipschitz constant \(L\), and \(d_{t,n}=d(t/n)\). Let
\[
M_d=\int_0^1d(u)\otimes d(u)\,du.
\]
Then
\[
D_{d,n}(h)=M_d+R^{\rm end}_{n,h},
\qquad
\|R^{\rm end}_{n,h}\|_{HS}
\le \frac{RLh+hR^2+2RL}{n}.
\]
The three terms respectively come from shifting \(d((t-h)/n)\) to \(d(t/n)\), deleting the first \(h\) indices, and the Riemann sum. Hence the drift contribution is lag-invariant uniformly for \(h=o(n)\), and the order \(h/n\) is attained by a nonconstant linear path.

For local stationary copies \(f_t^{(u)},e_t^{(u)}\), suppose the relevant components have \(L^2\)-norm at most \(B\) and admit couplings
\[
\|f_{t,n}-f_t^{(u_t)}\|_2+\|e_{t,n}-e_t^{(u_t)}\|_2\le\rho_n,
\]
at both time indices, with \(u_t=t/n\) and \(u_{t-h}=(t-h)/n\). In addition assume either process-level \(L^2\)-Lipschitz coupling
\[
\|f_s^{(u)}-f_s^{(v)}\|_2+\|e_s^{(u)}-e_s^{(v)}\|_2\le L_0|u-v|
\]
uniformly in \(s,u,v\), or directly assume the corresponding pair-moment approximation at order \(O(\rho_n+h/n)\). Let all retained loading maps and local lag moments be Lipschitz in \(u\). Put \(\eta_{n,h}=\rho_n+L_0h/n\). Cauchy–Schwarz gives, term by term,
\[
\|\mathbb E[x_{t,n}\otimes y_{t-h,n}]-\mathbb E[x_t^{(u_t)}\otimes y_{t-h}^{(u_t)}]\|_{HS}
\le 2B\eta_{n,h}+\eta_{n,h}^2,
\]
and the factor/cross/noise shift, end, and Riemann errors contribute \(O((h+1)/n)\). The separate deterministic drift error is already \(R^{\rm end}_{n,h}\) and is not counted again. Therefore the complete exact-score decomposition may be written
\[
\boxed{
\widehat S_n(h)=M_d+B_h+C_h+N_h
+R^{\rm geom}_{n,h}+R^{\rm LS}_{n,h}+R^{\rm end}_{n,h}+E^{\rm samp}_{n,h},
}
\]
where \(B_h=\int A(u)\Gamma_f(u,h)A(u)^*du\); \(C_h\) is the sum of the six drift-factor, drift-noise, and two-sided factor-noise terms; \(N_h=\int\Gamma_e(u,h)du\); and
\(
\|R^{\rm LS}_{n,h}\|_{HS}=O(\rho_n+(h+1)/n)
\)
under the displayed primitive coupling and Lipschitz bounds. The label \(E^{\rm samp}\) denotes the centred empirical fluctuation and has no asserted rate without a dependence/moment theorem. This separates population specification error, geometric error, local approximation/end error, and sampling error. **Status: PROVED INTERNALLY.**

If \(B_h=A\Gamma_f(h)A^*\) is stationary and \(\sum_{h\ge1}\|\Gamma_f(h)\|<\infty\), then \(\sum_hB_hB_h^*\) and the drift-factor assembly cross term converge, whereas the repeated drift row contributes exactly \(h_0M_d^2\). Near-zero factors can make \(B_h\) nearly lag-invariant over a finite lag range, so finite rows can be arbitrarily ill-conditioned for separating the two even when the factor has no atom at zero.

## 5. Exact operator and rank consequences

First impose the clean flat population conditions \(C_h=N_h=R_h^{\rm geom}=0\), and write
\[
S_h=M+B_h,\qquad E=\overline{\operatorname{ran}A},\qquad
D=\overline{\operatorname{ran}M},\qquad
\mathbb L=\sum_{h=1}^{h_0}(M+B_h)(M+B_h)^*.
\]
Always,
\[
\mathbb L=h_0M^2+\sum_hB_hB_h^*
+\sum_h(MB_h^*+B_hM),
\qquad
\overline{\operatorname{ran}\mathbb L}
=\overline{\operatorname{ran}\mathcal G}
=\overline{\operatorname{span}}_h\operatorname{ran}(M+B_h).
\]
The first equality follows from \(\mathbb L=\mathcal G\mathcal G^*\) and
\(\ker\mathbb L=\ker\mathcal G^*\), hence both closed ranges are the common
orthogonal complement of \(\ker\mathcal G^*\). Unclosed range equality follows
when these ranges are known closed, in particular in the finite-rank class.
No stronger rank formula holds without additional structure, by C-10.

**Aligned drift.** If \(D\subseteq E\), then
\(\overline{\operatorname{ran}\mathbb L}\subseteq E\). In the finite-rank class equality holds exactly when
\[
\bigcap_{h=1}^{h_0}\ker((M+B_h)^*|_E)=\{0\}.
\]
Thus drift adds no direction, but it can change rank, eigenvalues, and eigenvectors inside \(E\). It leaves a common eigenbasis with the factor-only operator \(\mathbb L_f=\sum B_hB_h^*\) when their spectral resolutions commute. In finite dimensions this is equivalent to \([\mathbb L,\mathbb L_f]=0\); if \(\mathbb L_f\) has simple spectrum, commutation preserves its eigenvectors, so only their eigenvalues change. Equality of the two operators' literal spectral projectors is stronger and is not claimed. In one aligned dimension commutation is automatic.

**Orthogonal drift.** If \(D\perp E\), \(M\) is positive definite on its finite-dimensional range, and the factor row has finite-dimensional range \(E\), then \(MB_h^*=B_hM=0\) and
\[
\mathbb L=h_0M^2\oplus\mathbb L_f,
\qquad
\operatorname{ran}\mathbb L=D\oplus E,
\qquad
\operatorname{rank}\mathbb L=\dim D+\dim E.
\]
Its nonzero spectrum is the multiset union of the two block spectra. The leading selected directions come from drift exactly when the relevant eigenvalues of \(h_0M^2\) exceed those of \(\mathbb L_f\); no dominance follows from orthogonality alone.

**Partial drift.** In general, if the lag contrasts are factor-complete,
\[
\overline{\operatorname{span}}_{h,k}\operatorname{ran}(B_h-B_k)=E,
\]
then differences \(S_h-S_k=B_h-B_k\) show
\(E\subseteq\overline{\operatorname{ran}\mathcal G}\), after which
\(M=S_h-B_h\) shows
\(D\subseteq\overline{\operatorname{ran}\mathcal G}\). Hence, in general,
\[
\overline{\operatorname{ran}\mathcal G}=\overline{E+D}.
\]
If \(E+D\) is finite-dimensional (hence closed), this strengthens to
\[
\operatorname{ran}\mathcal G=E+D,\qquad
\operatorname{rank}\mathcal G=\dim E+\dim(P_{E^\perp}D).
\]
This gives exact addition by the outside component on the finite-rank class. Without contrast completeness, only the tautologically sharp closed-range formula
\(\overline{\operatorname{ran}\mathcal G}=\overline{\operatorname{span}}_h\operatorname{ran}(M+B_h)\) survives, and cancellation is possible.

**Examples.** With \(A=e_1\), \(B_h=\gamma_h e_1\otimes e_1\): (i) \(M=me_1\otimes e_1\) is aligned and preserves the one-dimensional span unless \(m+\gamma_h=0\) at every included lag; (ii) \(M=me_2\otimes e_2\) is orthogonal and adds exactly \(e_2\); (iii) \(M=m(e_1+e_2)\otimes(e_1+e_2)\) is oblique, and for any \(\gamma_h\ne0\), \(M+B_h\) has determinant \(m\gamma_h\ne0\), so the fixed-centre lag is full rank and its eigenvectors rotate.

**General contamination.** Let \(K_h=C_h+N_h+R_h^{\rm geom}\), and let rows \(\mathcal G_0=[M+B_h]_h\) and \(\mathcal K=[K_h]_h\). Then exactly
\[
\mathbb L-\mathbb L_0=\mathcal G_0\mathcal K^*+\mathcal K\mathcal G_0^*+\mathcal K\mathcal K^*,
\]
so
\[
\|\mathbb L-\mathbb L_0\|\le2\|\mathcal G_0\|\,\|\mathcal K\|+\|\mathcal K\|^2.
\]
Cross/noise/geometry terms can add or rotate ranges arbitrarily. Eigenspace claims therefore require this bound to be small relative to an actual eigengap; exact rank claims require exact zeros or a threshold convention, since arbitrarily small nonzero contamination can increase population rank.

## 6. Hostile curved audit

### C-11 — failure of rank-one affine preservation immediately outside a common geodesic

Take the unit \(S^2\). Let \(x=N=(0,0,1)\), choose \(y=(0,\sin a,\cos a)\) with \(0<a<\pi/2\), and consider the source rank-one geodesic support
\[
q(s)=(\sin s,0,\cos s),\qquad s\in\{-\pi/2,0,\pi/2\}.
\]
Every source Log at \(x\) and target Log at \(y\) is unique. In the tangent basis \(e_1=(1,0,0)\), \(e_2=(0,\cos a,-\sin a)\), the sphere Log formula gives
\[
\log_y q(s)=\frac{\theta(s)}{\sin\theta(s)}
\big(\sin s\,e_1-\sin a\cos s\,e_2\big),
\qquad \cos\theta(s)=\cos a\cos s.
\]
At \(s=\pm\pi/2\) these are \(\pm(\pi/2)e_1\), while at \(s=0\) the vector is \(-ae_2\). The three transformed points are not collinear. Therefore an exact noiseless rank-one affine law at \(x\) need not remain a noiseless rank-one affine law at an off-geodesic reference \(y\), despite a common normal domain. Curvature/noncollinearity is the obstruction; a Taylor expansion is unnecessary. This supplies an immediate boundary example for the common-geodesic restriction. **Status: PROVED INTERNALLY.**

This does not attack the unique-marginal-centre gate: \(x,y\) are weakened references. It attacks only a claim that arbitrary base-point change preserves the affine factor class.

## 7. Scientific interpretation (ID-6 audit)

The proved statement is:

> Under a fixed-centre misspecification, the fitted lag row can superpose a repeated fixed-score drift term, factor lag structure, drift/factor and factor/noise cross terms, idiosyncratic lag, nonlinear geometry error, local-stationarity/end effects, and sampling error. The row alone does not report their split.

Under pointwise score centring, two-sided factor/noise lag orthogonality, included-lag idiosyncratic whiteness, a common-flat (or exact fixed-score affine) model, and the displayed rank/eigengap conditions, the clean drift/factor operator conclusions apply. A moving-centre refit that changes the leading direction is an empirical sensitivity result unless these identifying assumptions are justified for the application.

Nothing proved here implies that the parent model's Factor 1 is spurious, drift-dominated, or erroneous. Its (P2) defines a fixed-centre factor within that model. Dataset-specific dominance would require an identified decomposition plus estimation and uncertainty analysis beyond equality of the fixed-centre lag row.

## 8. Hostile Pass II against the synthesized ID-0--ID-6 package

This pass attacks the lead synthesis §8 after the producer repairs. Every objection below has a terminal disposition.

| Slot | Hostile attack | Exact test | Disposition |
|---|---|---|---|
| ID-0 | The arrows can be overstated if a “lag functional” is undefined. | FDD equality pushes forward every integrable, single-valued fixed-Log tensor functional, but C-5 shows an arbitrary anchor Log can fail to be single-valued. | **SUSTAINED SCOPE LOCK:** add integrability and compatible-Log hypotheses to the lag-functional implication. With that lock, C-1/C-2/C-3 prove both strict converses and ID-0 passes. |
| ID-1 | Completeness might be mistaken for existence/uniqueness. | C-4 has a complete compact manifold and an existing but non-singleton minimizer set. | **REPAIRED IN SYNTHESIS AND PASSED:** the theorem identifies \(\mathfrak M(Q)\) and separately assumes singleton status; it does not derive uniqueness from completeness. |
| ID-2 | Minimum loading rank might secretly identify the full nonlinear law, or one lag might be assumed full rank. | C-2 gives identical all-lag covariance and different non-Gaussian FDDs; C-9 gives complementary rank-deficient lags; C-7 gives exact dynamically silent reallocation. | **REPAIRED IN SYNTHESIS AND PASSED:** the general result is explicitly second-order, the full-FDD quotient is restricted to the jointly Gaussian/independent-noise class, and the identified loading is the complete signed-lag row span rather than any single lag. |
| ID-2 | “Absorbable shift” might violate centring or stationarity and then be treated as an admissible equivalence. | Algebraically \(d(u)\in\operatorname{ran}A\) is necessary and sufficient for \(d=Ag\), but \(f-g\) may cease to be centred or stationary. | **SCOPE LOCK PRESENT AND PASSED:** the synthesis requires separate satisfaction of the declared factor rules; when both references are unique marginal means, ID-1 kills the shift. |
| ID-3 | No zero atom might be advertised as a uniform rate or uniform estimator. | C-6 chooses \(\rho_N=1-N^{-2}\) and obtains average variance tending to one despite no zero atom for any fixed AR(1) law. | **PASSED:** the theorem is pointwise for a fixed law and separately proves non-uniformity. Canonical wording should say “moving nonzero-frequency atom/mass near zero,” not “near-zero spectral atom,” which can be confused with an atom at exactly zero. |
| ID-3 | Invariant random factors might be mislabeled deterministic centre drift. | C-6's \(f_t=V\) is invariant and zero-mean in ensemble but cannot be a second deterministic unique Fréchet centre. | **PASSED:** synthesis treats it as an invariant projection/recoverability obstruction, not as a counterexample to ID-1. |
| ID-4 | Unique marginal centre might be conflated with a unique weakened reference. | C-11 changes to an off-centre reference while retaining unique Log branches; the new reference is not asserted to be a Fréchet mean. | **PASSED:** the orbit theorem is explicitly under weakened centring. ID-1 remains untouched. |
| ID-4 | The flat restriction might be merely convenient, and a local Taylor term might be sold as exact. | C-11 gives three exact spherical support points whose image has affine dimension two; no remainder argument is used. | **PASSED WITH GENUINE BOUNDARY:** common-geodesic/common-flat translation is exact, while an immediately off-geodesic reference destroys rank-one affine preservation. The finite-probe theorem classifies exactly the retained invariant (finite-support affine dimension). |
| ID-5 | Historical additivity may suppress cross, idiosyncratic, or curved terms. | C-8 shows the two cross-lag directions differ; §4.2 expands all nine tensors; §4.3 defines the exact geometry remainder. | **REPAIRED AND PASSED:** the clean formula is expressly conditional on pointwise centring, both cross-lag zeros, included-lag idiosyncratic whiteness, and a common-flat/exact-score model. |
| ID-5 | Score drift may be mislabeled geodesic centre drift. | Universally \(b_t=\mathbb E\log_{c_0}X_t\); on curvature there is no general identity \(b_t=\log_{c_0}\mu(u_t)\). | **PASSED:** synthesis retains this warning and the nonlinear \(g_t\) remainder. |
| ID-5 | General Hilbert ranges and finite-dimensional ranks may be conflated. | For \(\mathbb L=\mathcal G\mathcal G^*\), only \(\overline{\operatorname{ran}\mathbb L}=\overline{\operatorname{ran}\mathcal G}\) is universal; C-10 shows cancellation even in one dimension. | **SUSTAINED, REPAIRED, RECHECKED:** §5 now uses closed-range identities and states unclosed row range/dimension formulas only when \(E+D\) is finite-dimensional. Both foreign auditors passed the repair. |
| ID-5 | “Only eigenvalues change” may be inferred merely from aligned drift. | Alignment alone allows rotations within \(E\). | **SUSTAINED, REPAIRED, RECHECKED:** §5 requires commuting spectral resolutions; in finite dimensions \([\mathbb L,\mathbb L_f]=0\), and simple factor-only spectrum pins its eigenvectors. |
| ID-5 | Local-stationarity error may double-count drift end effects or freeze the lagged variable at the wrong local time. | Own-time coupling controls \(t-h\) at \(u_{t-h}\), not directly at \(u_t\). | **SUSTAINED, REPAIRED, RECHECKED:** §4.4 adds process-level \(L^2\)-Lipschitz same-freeze control, \(\eta_{n,h}=\rho_n+L_0h/n\), and excludes deterministic \(R^{\rm end}\) from \(R^{\rm LS}\). |
| ID-6 | A sensitivity change may be converted rhetorically into drift dominance or a “spurious Factor 1” claim. | C-3 proves only lag-row equivalence, not full-law equivalence; C-10 shows even component ranks can cancel; general \(K_h\) can rotate the fitted leading eigenspace. | **PASSED:** the synthesis says only superposition/non-labeling. Dominance requires a dataset-specific identified split, eigengap, estimation, and uncertainty analysis. |

**Pass-II verdict.** No counterexample defeats the repaired theorem package. The surviving qualifications are definition-level scope locks; every mathematical node is terminal. ID-0 must quantify only defined integrable lag functionals; ID-3 must distinguish an atom at zero from moving near-zero mass; ID-5 must retain the already repaired closed-range and local-freeze wording. Subject to those exact locks, ID-0--ID-6 have terminal proofs or proved impossibility boundaries. **Status: HOSTILE PASS II PASSED.**

## 9. Foreign-audit disposition

Workstream B audited §§4--5 for connector typing, both cross terms, population/sample separation, and rank consequences. It sustained the closed-range/finite-dimensional and local-stationarity wording objections; both were repaired, and B's recheck passed. Workstream A independently sustained the same range issue plus the same-freeze and commuting-spectral-resolution issues; all were repaired, and A's final recheck passed. No objection was resolved by adding an assumption equivalent to the conclusion.

## 10. Terminal claim table

| Claim / attack | Assumptions and information set | Terminal status | Proof location | Residual objection disposition |
|---|---|---|---|---|
| Same marginals, different joint laws | nondegenerate \(Q\), \(\mathcal I_M\) | PROVED INTERNALLY | C-1 | unique mean verified |
| Same marginals/all lag covariances, different laws | bounded stationary laws, covariance information | PROVED INTERNALLY | C-2 | weak versus independent white separated |
| Lag row does not identify split | \(\mathcal I_F(c_0)\) | PROVED INTERNALLY | C-3 | no full-law equality claimed |
| Nonunique mean boundary | \(S^1\), antipodal mixture | PROVED INTERNALLY | C-4 | Logs at selected means are unique |
| Cut-locus boundary | unique true mean, arbitrary fixed anchor | PROVED INTERNALLY | C-5 | branch issue explicit |
| Zero/near-zero recovery boundary | stationary \(L^2\) processes | PROVED INTERNALLY | C-6 | pointwise versus uniform separated |
| Factor/noise rank reallocation | full path equality, independent iid residual | PROVED INTERNALLY | C-7 | only dynamically silent coordinate moved |
| Two-sided cross-lag need | marginal white components | PROVED INTERNALLY | C-8 | process independence not assumed |
| Complementary lag ranks | stationary MA factors | PROVED INTERNALLY | C-9 | row rank computed exactly |
| Rank cancellation | aligned scalar drift/factor | PROVED INTERNALLY | C-10 | stationary covariance feasible |
| Universal fixed-Log split | cut-locus avoidance, second moments | PROVED INTERNALLY | 4.1 | score mean not called Fréchet drift |
| Nine-term affine expansion | exact one-fibre score model | PROVED INTERNALLY | 4.2 | all cross directions displayed |
| Curved geometry remainder | common normal domain | PROVED INTERNALLY | 4.3 | no affine preservation assumed |
| End/LS/sample separation | primitive Lipschitz and coupling bounds | PROVED INTERNALLY | 4.4 | no unsupported sampling rate |
| Aligned/orthogonal/partial consequences | clean terms plus stated completeness | PROVED INTERNALLY | 5 | cancellations and eigengaps retained |
| Off-geodesic curved obstruction | unit sphere, exact Logs | PROVED INTERNALLY | C-11 | weakened-reference scope explicit |
| Factor 1 language | conclusions above | PROVED INTERNALLY | 7 | dominance expressly not inferred |

Every node introduced in this dossier has a terminal status. No external theorem is load-bearing.
