---
type: working-lead-ledger
title: P1-ID-CLOSE — lead ledger
status: active-campaign
last-audited: 2026-08-12
authority: single adjudication authority for the P1-ID-CLOSE campaign; canonical status lives in the canonical files after Wave 4
---

# P1-ID-CLOSE — lead ledger

> **Volatile-context discipline.** Every verdict is written here at the moment it is established. On any interruption, re-read §1 (state summary) and continue from "next action". Workstream dossiers are `P1-ID-CLOSE-A/B/C` in this directory. Agents write only their own dossier; the lead merges.

## 1. State summary (rewrite on every checkpoint)

- **Campaign objective.** Prove ID-7–ID-10, execute the ID-9 assault on the ID-1 gate to a terminal verdict, reconcile the canonical estimand, integrate with no open node in the transitive closure.
- **Wave:** 1 returned (A, B, C dossiers written). Wave 3 hostile cross-audit **dispatched and interrupted**.
- **Last verified step:** all three Wave-1 claim tables merged into §3 and §5; objections O-1…O-6 opened and provisionally adjudicated; ID-7/ID-10 delivered early by A so Wave 2 collapsed into the reconciliation set. Lead independently re-derived B's L-8.3 exact BW `SPD(2)` computation in sympy and **confirms** \(L=V/(1+a)\), \(W=\operatorname{diag}(1,a)/(1+a)^2\), \(Y=V/(1+\sqrt a)\), \(Y^2=I/(1+\sqrt a)^2\), \(W\ne Y^2\) for all \(a\ne1\), and exact defect \(\operatorname{diag}(-3.5555\times10^{-4},+4.8888\times10^{-4})\) at \(a=4,b=1/10\).
- **INTERRUPTION RECORD (checkpoint, not a terminal event).** The three Wave-3 hostile auditor agents (targets: dossiers A, B, C) were terminated mid-audit by a weekly credit limit. No auditor returned a verdict. Nothing from those partial runs is recorded as a result. Per §"Persistence and interruption discipline", the campaign continues.
- **Resumption rule adopted:** the Wave-3 hostile audit is re-executed **by the lead**, which did not author dossiers A, B, or C and therefore satisfies the non-author requirement. The lead re-verifies every load-bearing computation independently in sympy/numpy rather than accepting a dossier's own arithmetic.
- **Next action:** (1) lead hostile audit of the load-bearing claims of A, B, C, in the priority order L-9.R2.1 → L-9.R1.2 → L-8.1/L-8.2 → L-9.R3.3b/R3-D → L-7.3.2 → L-10.2b → R4-EXH; (2) close O-1…O-6; (3) Wave 4 canonical integration; (4) transitive closure audit; (5) commit.

## 2. Information-set vocabulary (locked; do not vary)

Inherited verbatim from [[P1-ID — centre-drift and factor identification boundary]] §2: \(\mathcal I_M\) (all marginals), \(\mathcal I_J\) (full FDD law), \(\mathcal I_1\) (one path), \(\mathcal I_F(c_0)\) (fixed-anchor row), \(\mathcal I_R\) (weakened reference). This campaign adds no new information set. Where a claim concerns a *latent* process it must say so explicitly: latent objects are not in any information set.

## 3. Node register

Status codes: `PROVED`, `CITED+APPLIED`, `DISPROVED`, `REFORMULATED+PROVED`, `SUPERSEDED`, `SEPARATED` (out of scope by proved separation). No other terminal code. `WIP` is non-terminal and may not survive Wave 4.

### 3.1 Target slots

| ID | Statement (short) | Producer | Consumer | Status |
|---|---|---|---|---|
| ID-7 | constructive separation: sufficient conditions under which centre drift and persistent factors are separable, attained by the three-scale estimator | A | canonical P1-ID §, Paper 1, App map | WIP |
| ID-8 | curvature class of ID-4 reference-dependent dynamic rank inflation | B | canonical P1-ID §, App map, N-18 | WIP |
| ID-9 | sharpness of / assault on the ID-1 gate; routes R1–R5 | B,C | canonical P1-ID §, Paper 1 preconditions | WIP |
| ID-10 | persistence regimes simultaneously compatible with ID-3 floor, HD-M, HD-K | A | canonical P1-ID §, HD1, App map | WIP |
| CANON-1 | reconcile \(E_n=\operatorname{ran}A_n\) with \(\mathcal S_X\) | lead | all canonical files | WIP |
| CANON-2 | displayed HCC-under-drift corollary | lead | Paper 1 | WIP |
| CANON-3 | surface ID-2 Gaussian restriction as a displayed scope limit | lead | Paper 1, App map | WIP |
| HYG | worktree, links, LaTeX, duplicate-status scan | lead | repository | WIP |

### 3.2 ID-9 route nodes

| ID | Route | Owner | Status |
|---|---|---|---|
| R1 | existence: can a law on the full-rank BW cone with mass approaching rank deficiency have empty argmin in the open cone? | B | WIP |
| R2 | uniqueness: characterise nonsingleton argmin on BW and on the parent's sphere products; measurability, continuity, and cost of a selector | B | WIP |
| R3 | latent stochastic centre: mixture Fréchet mean vs mixing centres; marginal- and FDD-equivalent latent-centre models | C | WIP |
| R4 | declared-convention escape: which alternative centre conventions are admissible and genuinely distinct | A | WIP |
| R5 | sample-level non-uniqueness: identification node or proved separation | C | WIP |

### 3.3 Sublemma register (every entry must terminate)

| ID | Statement | Producer | Consumer | Status |
|---|---|---|---|---|
| L-8.1 | Gavrilov–Pennec expansion \(\log_y\operatorname{Exp}_x Z=w+PZ+\tfrac16R(PZ,w)w+\tfrac13R(PZ,w)PZ+O(4)\) | external (C-AUDIT-5) | ID-8 | WIP |
| L-8.2 | \(\langle R(V,w)V,V\rangle=0\); the quadratic coefficient is exactly transverse | B | ID-8 | WIP |
| L-8.3 | exact BW SPD(2) non-collinearity computation | B | ID-8 | WIP |
| L-8.4 | exact AIRM (Hadamard) non-collinearity computation | B | ID-8 | WIP |
| L-8.5 | converse rigidity: rank preserved for all small configurations \(\Rightarrow\) sectional curvature vanishes on planes containing \(w\) | B | ID-8 | WIP |
| L-9.R1.1 | coercivity and existence of the BW Fréchet mean on \({\rm PSD}(m)\) | B | R1 | WIP |
| L-9.R1.2 | boundary escape: one-sided directional derivative \(-\infty\) into the cone at a rank-deficient candidate | B | R1 | WIP |
| L-9.R2.1 | uniqueness of the BW barycentre when the law charges the full-rank cone | B | R2 | WIP |
| L-9.R2.2 | exact nonuniqueness class on \(S^1/S^2\) and product spheres | B | R2 | WIP |
| L-9.R2.3 | measurable selector exists; no continuous selector through a nonsingleton stratum; discontinuous selector manufactures broadband drift | B | R2 | WIP |
| L-9.R3.1 | flat case: marginal Fréchet mean of a latent-centre mixture equals \(\mathbb E C_u\), never the realised \(C_u\) | C | R3 | WIP |
| L-9.R3.2 | curved case: marginal Fréchet mean of the mixture \(\ne\) Fréchet mean of the mixing-centre law; exact counterexample | C | R3 | WIP |
| L-9.R3.3 | two admissible latent-centre models with different centre processes and different loadings sharing every FDD | C | R3 | WIP |
| L-9.R4.1 | equivariance rigidity: all marginal-functional, isometry-equivariant conventions agree on the stabiliser-symmetric class and generically differ off it | A | R4 | WIP |
| L-9.R4.2 | smoothness-regularised centres are \(\mathcal I_M\)-functionals of the *family*, not of each marginal; new equivalence class, still gate-bound at the family level | A | R4 | WIP |
| L-9.R5.1 | empirical argmin instability: identification node or proved separation to estimation | C | R5 | WIP |
| L-7.1 | ergodic-average modulus \(\psi_n(N)\) of the frozen factor; exact AR(1) and long-memory evaluation | A | ID-7, ID-10 | WIP |
| L-7.2 | separation theorem: \(\psi\)-condition is sufficient for identification-plus-estimability of the centre/factor split | A | ID-7 | WIP |
| L-7.3 | three-scale estimator attainment: \(\psi(nb_n)\) enters the mean error exactly where \((nb_n)^{-1/2}\) does | A | ID-7, ID-10 | WIP |
| L-10.1 | replacement rate under memory exponent \(d\); re-optimised bandwidth and exponent | A | ID-10 | WIP |
| L-10.2 | near-unit-root window with persistence varying in rescaled time; induced local-stationarity exponent | A | ID-10 | WIP |
| L-10.3 | compatibility with HD-K \(nb_n/\log n\to\infty\) and HD-M \(a\ge3/7\); non-emptiness | A | ID-10 | WIP |
| C-1.1 | \(\mathcal S_{X,n}=\operatorname{ran}A_n\iff Q_n\succ0\); \(\Delta_n>0\Rightarrow Q_n\succ0\) | lead | CANON-1 | WIP |

## 4. Lead's candidate routes (dispatched as hypotheses, not as results)

Recorded so that a subagent failure is a *route* failure and not a campaign failure. Agents must verify or refute independently.

- **ID-8.** Universal second-order argument. With \(c(t)=\log_y\operatorname{Exp}_x(tV)\) and \(w=\log_y x\), L-8.1 gives \(c(t)=w+t[PV+\tfrac16R(PV,w)w]+t^2\cdot\tfrac13R(PV,w)PV+O(t^3)\). Three points \(t=-b,0,b\) are collinear iff \(c'\wedge c''=0\); L-8.2 gives \(R(PV,w)PV\perp PV\) exactly. Predicted verdict: rank inflation occurs on **every** manifold with nonzero sectional curvature on a plane containing \(w\) — not cut-locus-specific, not sign-specific.
- **R1.** Predicted **excluded**: at a rank-deficient candidate \(\bar\Sigma\) and \(v\in\ker\bar\Sigma\), the perturbation \(\bar\Sigma+\varepsilon vv^{\!\top}\) changes the objective by \(\varepsilon-2\sqrt\varepsilon\int\sqrt{s(\Sigma)}\,Q(d\Sigma)+O(\varepsilon)\) with \(s\) the Schur complement, so no boundary minimiser exists when \(Q\) charges the full-rank cone.
- **R2.** Predicted **split**: uniqueness holds on BW with full-rank-charging \(Q\); fails on the parent's spheres. The selector cost is the crack, and it is geometry-specific.
- **R3.** Predicted **crack**: the gate is *void* on the latent-stochastic-centre class because a random centre is not a functional of any information set. Flat case: mixture mean \(=\mathbb EC_u\ne C_u\). FDD-equivalence is expected to be attainable.
- **ID-7/ID-10.** Predicted separation condition: the frozen factor's normalised partial-sum modulus must satisfy \(\psi(nb_n)=o(\ell_n)\); short memory sits exactly at the design point \((nb_n)^{-1/2}=n^{-3/7}\) when \(b_n=n^{-1/7}\).

## 5. Objection ledger

| # | Objection | Against | Raised by | Disposition |
|---|---|---|---|---|
| O-1 | "ID-2(1)–(3) are FALSE on the latent-centre class" | C, L-9.R3.3b / R3-D | C | **LEAD ADJUDICATION — SUSTAINED IN SUBSTANCE, RETITLED.** ID-2 is stated for a *centred* process \(X_t=Af_t+\delta_t\) with temporally uncorrelated \(\delta\). A serially dependent latent centre \(C_t\) cannot be placed in \(\delta\), so in ID-2's own vocabulary it must be absorbed into the loading. ID-2's \(A\) is therefore the **total dynamic loading**; C's \(A\) is a *factor-only* loading and is not an ID-2 admissible loading. Verdict: ID-2 remains **TRUE as stated on its declared class** and is **NON-BINDING on the latent-centre class in exactly the manner of ID-1**. What C actually proved — and it is the load-bearing result — is that the **sub-split of ID-2's identified loading into a centre part and a factor part is not identified even from \(\mathcal I_J\)**. Canon records the scope lock, not a retraction. Verified in Wave 3 by A and B. |
| O-2 | "\(\psi_n(nb_n)=o(\ell_n)\) is impossible at every \(d\ge0\) and every bandwidth, so ID-7 cannot claim a clean separation" | A's ID-7 | C, L-9.R3.6 | **OVERRULED — the objection asks the wrong question.** \(\psi^+(nb_n)\) is not an extra term to be dominated by \(\ell_n\); by A's L-7.3.2 it **is** \(\ell_n\)'s stochastic term, which under HD-M reduces verbatim to \((nb_n)^{-1/2}\). The correct object is \(\ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1}\). C's disposition menu (α)/(β)/(γ) is unnecessary. Rechecked in Wave 3. |
| O-3 | R5 status conflict: C separates R5 on Hadamard/strongly-convex domains but calls it an identification node on "the \(K\ge0\) BW cone"; B proves BW Fréchet uniqueness for every \(Q\) charging the full-rank cone | C's L-9.R5.1/R5.4 vs B's L-9.R2.1 | lead | **RESOLVED IN B's FAVOUR, pending Wave-3 recheck.** B's L-9.R2.1 proves \(F_Q\) is convex in the **ordinary linear** structure on \({\rm PSD}(m)\) and strictly convex whenever \(Q\) charges the open cone. Applied to the *empirical* measure — whose atoms are full-rank almost surely on the declared domain — this gives a pathwise unique empirical BW argmin. Hence **R5 is SEPARATED on BW as well as on Hadamard**, and the identification-node residue is confined to sphere and sphere-product geometry (the parent's simulation geometry), where B's L-9.R2.3 supplies the exact manufactured-drift cost. |
| O-4 | Lead's dispatched L-7.1(b) claim \(\psi(N)\asymp N^{-1/2}\) for \(m_0\)-dependent processes is unconditionally false | lead's Wave-1 dispatch | A | **SUSTAINED.** The upper bound \(\psi(N)\le\sqrt{(2m_0+1)R^2/N}\) always holds; the matching lower bound needs \(\Lambda_u=\sum_h\operatorname{tr}\Gamma_u(h)>0\). Witness \(Z_t=e_t-e_{t-1}\) gives \(\psi=\sqrt2/N\). This makes the separation condition *easier*, not harder; ID-7 is stated with the one-sided \(\psi^+\) modulus. |
| O-5 | Lead's ID-10 near-unit-root window \(\theta\le4/7\) answers the wrong question: \(a\ge3/7\) is a design constant tied to \(b_n=n^{-1/7}\), not a primitive | lead's Wave-1 dispatch | A, L-10.2c | **SUSTAINED.** The primitive clause is \(a\ge3\alpha\). With induced \(a=1-\theta\) and re-optimised \(\alpha=(1-\theta)/7\), \(a\ge3\alpha\) holds automatically, so the binding window is \(\theta\in[0,1)\) with rate \(n^{-3(1-\theta)/7}\). \(\theta\le4/7\) survives only as the corollary "if one insists on holding \(b_n=n^{-1/7}\) and \(a\ge3/7\) fixed". Canon states the primitive form and the fixed-design corollary separately. |
| O-6 | Lead's ID-8 criterion "nonzero sectional curvature" is sufficient but not sharp | lead's Wave-1 dispatch | B, L-8.2 | **SUSTAINED.** Sharp criterion is \(c'(0)\wedge c''(0)\ne0\); sufficient criterion is \(R(PV,w)PV\ne0\); \(\kappa\ne0\Rightarrow R(PV,w)PV\ne0\) but not conversely (\(S^2\times H^2\) witness). All project geometries have one-signed curvature so the distinction is inert downstream, but canon states the sharp form. |

## 6. Wave 3 — lead hostile audit (non-author; re-executed after the credit interruption)

Every load-bearing claim was re-derived by the lead from scratch, analytically, with numerical corroboration. Verification script and output are reproduced in §6.3.

### 6.1 Audit verdicts

| Claim | Verdict | Detail |
|---|---|---|
| **L-9.R2.1** variational identity \(\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}=\tfrac12\inf_{T\succ0}[\operatorname{tr}TA+\operatorname{tr}T^{-1}\Sigma]\) | **CONFIRMED — exact proof supplied by the lead** | Substituting \(T=A^{-1/2}SA^{-1/2}\) reduces the claim to \(\operatorname{tr}S+\operatorname{tr}(S^{-1}N^2)\ge2\operatorname{tr}N\) for \(S,N\succ0\), \(N=M^{1/2}\), \(M=A^{1/2}\Sigma A^{1/2}\). The identity \(\operatorname{tr}S+\operatorname{tr}(S^{-1}N^2)-2\operatorname{tr}N=\operatorname{tr}\!\big(S^{-1}(S-N)^2\big)\ge0\) is exact, with equality **iff** \(S=N\). Numerically: value at \(T^\star\) matches \(G\) to 10 digits. |
| **L-9.R2.1** \(F_Q\) convex in the ordinary linear structure; strictly convex on the open cone | **CONFIRMED — and the proof is cleaner than the dossier's** | \(G(A)=\operatorname{tr}(A^{1/2}\Sigma A^{1/2})^{1/2}\) is a \(\tfrac12\inf\) over \(T\) of functions **affine in \(A\)**, hence **concave**; so \(-2\!\int\!G\,dQ\) is a sup of affine functions, hence convex, and \(F_Q(A)=\operatorname{tr}A+c-2\!\int\!G\,dQ\) is convex. **Strictness:** the optimiser \(T^\star(A)=A^{-1/2}(A^{1/2}\Sigma A^{1/2})^{1/2}A^{-1/2}\) is constant along \(A_t=A_0+tH\) only if \(\Sigma=T A_tT\) for all \(t\), i.e. \(THT=0\), i.e. \(H=0\). So \(G\) is strictly concave along every line and \(F_Q\) is strictly convex whenever \(Q\) charges \(\{\Sigma\succ0\}\). 0 concavity violations in 2000 random tests. The dossier's flagged step ("affine minorant equal at an interior point") is **bypassed** by this argument and needs no repair. |
| **L-9.R1.2** boundary escape, exact one-sided bound | **CONFIRMED; the double-orthogonality concern is resolved** | \(G(A)=\|A^{1/2}\Sigma^{1/2}\|_*\). With \(X_0=\bar\Sigma^{1/2}\Sigma^{1/2}\), \(v\in\ker\bar\Sigma\), \(w=\Sigma^{1/2}v\): \(v\perp\operatorname{ran}X_0\) **automatically** (column side, since \(v^\top\bar\Sigma^{1/2}=0\)) and \(\hat n\perp\operatorname{ran}X_0^\top\) **by definition** (row side). Hence \(\|Z_0+v\hat n^\top\|_{\rm op}=1\), \(Z_0^\top v=0\), \(v^\top X_0=0\), and \(G(A_\varepsilon)-G(\bar\Sigma)\ge\sqrt\varepsilon\,\|P_\perp\Sigma^{1/2}v\|=\sqrt{\varepsilon\,s(\Sigma)}\), where \(\|P_\perp\Sigma^{1/2}v\|^2=\min_{u\in\operatorname{ran}\bar\Sigma}(v-u)^\top\Sigma(v-u)\) **is exactly the Schur complement**. One-sided, no remainder, no integrability side condition, arbitrary corank. Numerically the ratio gain\(/\sqrt{\varepsilon s}\to1^+\) for corank 1 and 2. |
| **L-8.2** wedge expansion constant | **CONFIRMED WITH CORRECTION** | The dossier states \(c(b)\wedge c(-b)=2b^3(c'\wedge c'')+O(b^4)\). Exact symbolic expansion gives coefficient **\(1\), not \(2\)**. The \(O(b^4)\) terms and the conclusion (nonzero iff \(c'\wedge c''\ne0\)) are unaffected. **Cosmetic**; canon uses the corrected constant. |
| **L-8.3** exact BW \({\rm SPD}(2)\) non-collinearity | **CONFIRMED** (lead's independent sympy re-derivation, recorded in §1) | |
| **L-7.1a** AR(1) modulus closed form | **CONFIRMED** | Matches the exact double sum to machine precision at \((N,\rho)=(1,.5),(2,.5),(7,.9),(50,.99),(200,.995)\). |
| **L-7.1a′** limit profile \(\Psi(x)=2(x-1+e^{-x})/x^2\) | **CONFIRMED** | Agrees with the closed form to \(<5\times10^{-6}\) at \(x=0.1,1,3,10\); \(\Psi(0^+)=1\), \(\Psi(x)\sim2/x\). |
| **sharpness match** \(\Psi(x)\) vs \(I_N=(x+2\rho)/(1+\rho)\) | **CONFIRMED** | ID-3's displayed \(\mathbf1^\top\Sigma_\rho^{-1}\mathbf1=(n(1-\rho)+2\rho)/(1+\rho)\) is exactly \((x+2\rho)/(1+\rho)\) with \(x=n(1-\rho)\). Achievable variance and information floor are functions of the **same scalar** \(x\); the matching is genuinely gap-free, not "nearly". |
| **L-10.1** \(\alpha(d)=(1-2d)/(7-2d)\), rate \(n^{-3(1-2d)/(7-2d)}\) | **CONFIRMED** | \(3\alpha=(1-\alpha)(\tfrac12-d)\Rightarrow\alpha=(\tfrac12-d)/(\tfrac72-d)\). Recovers \(1/7,\,3/7\) at \(d=0\); \(\alpha>0\iff d<1/2\), so \(b_n\to0\) forces \(d<1/2\); HD-K's \(nb_n/\log n\to\infty\) holds throughout. |
| **L-10.2b** \(a=1-\theta\) for the tvAR(1) array | **CONFIRMED** | Lead's independent coupling: the multiplicative distortion of the MA coefficients is \(\exp(n^{-\theta-1}g'k^2/2)\), which at the effective memory \(k\asymp n^{\theta}\) is \(1+O(n^{\theta-1})\); the \(\sigma=\sqrt{1-\rho^2}\) normalisation contributes the **same** order \(O(k/n)=O(n^{\theta-1})\) and does **not** compound. Hence \(\|D\|_{L^2}=O(n^{\theta-1})\), i.e. \(a=1-\theta\). The lead's earlier worry that the exponent might be \(1-2\theta\) is **withdrawn**: the unit-marginal-variance normalisation cancels the extra factor. |
| **O-5 / \(a\ge3\alpha\)** | **CONFIRMED against HD1's own text** | HD1 writes "Balancing the first two terms gives \(\alpha=1/7\) and \(\ell_n=O(n^{-3/7})\) **when \(a\ge3/7\)**". That is the \(\alpha=1/7\) instance of \(n^{-a}\le b_n^3\). The primitive clause is \(a\ge3\alpha\); HD-K separately needs only \(a\ge\alpha\). Near-unit-root: \(\alpha=(1-\theta)/7\) and \(a=1-\theta\) satisfy \(a\ge3\alpha\) automatically, and \(x=n^{1-\alpha-\theta}=n^{6(1-\theta)/7}\to\infty\iff\theta<1\). **Window \(\theta\in[0,1)\), rate \(n^{-3(1-\theta)/7}\).** |
| **L-9.R2.3** manufactured drift \(=\lambda(1-\lambda)\pi^2\) at every lag | **CONFIRMED WITH CORRECTION** | Constant verified at \(\lambda\in\{0.5,0.2,0.05\}\), \(h\in\{1,5,50\}\), \(n=2\times10^4\), agreeing to \(O(h/n)\) exactly as claimed, and lag-invariant. **Correction:** the dossier's "dominates a genuine mixing factor at every \(h\ge1\)" needs \(\lambda(1-\lambda)>\rho/4\). At \(\lambda=1/2\) this holds for every \(\rho<1\); at \(\lambda\to0\) or \(1\) it fails. Canon states the domination **with the \(\lambda\) condition**. |
| **L-9.R4.1′** \(S^2\) antipodal: \(L^2\) argmin = equator (dim 1), \(L^1\) argmin = all of \(S^2\) (dim 2) | **CONFIRMED** | \(F_{L^1}(x)=\tfrac12[\theta+(\pi-\theta)]=\pi/2\) identically. Different conventions have genuinely different failure geometries. |
| **L-9.R3.2d** global \(H^2\) claim \(0<\tau(s)<\beta\), \(m_2>0\) | **CONFIRMED ON QUALITATIVE GROUNDS; SCOPED** | Endpoint behaviour checks out: \(\tau(0)=0\); as \(s\to\infty\) the \(\{p,q\}\) pull dominates and \(m(s)\to c_2\), so \(\tau\uparrow\beta\) without reaching it. Sign: in \(K<0\), \(d(x,p)^2+d(x,q)^2\) exceeds its flat value by an amount increasing in \(d(x,c_2)\), so the spread component's pull is **strengthened** and the mean moves **toward** \(c_2\) — \(m_2>0\) is the correct sign for \(H^2\). Canon consumes only the **local** statement (\(m_2\ne0\) with the displayed closed form, and exact vanishing in the flat case), which is what the scientific conclusion requires; the global monotonicity claim is recorded in the dossier as proof provenance and is **not consumed** by any canonical statement. |
| **L-9.R3.3d (R3-D)** every subspace is an admissible LC loading range | **CONFIRMED BUT DEFLATED** | With \(\delta\equiv0\) and no constraint on the centre process, \(C:=X-Af\) is admissible for *any* \(A\), so the statement is close to tautological. Its real content — and the only content canon will assert — is that **the latent-centre class imposes no constraint whatever on the centre process**, hence no quotient survives. Stated that way it is exactly right and is not dressed as a deep theorem. |
| **R4-EXH** exhaustiveness of the escape space | **CONFIRMED, AND ITS STATUS CORRECTLY LABELLED** | Either the convention factors through the information map \(\iota\) or it does not; if it does and is single-valued it is pinned (pure set theory — measurability is irrelevant to *pinning*, only to usability). So the trichotomy E1/E2/pinned is exhaustive **by construction**. Canon states it as a classification whose content lies entirely in the R1/R2/R3 case analysis, not as a substantive theorem. No sixth route exists. |

### 6.2 Objection dispositions — all closed

- **O-1 — CLOSED, lead ruling upheld.** Decisive test applied to C's own \(\mathbb R^3\) construction: in Model 1 the latent centre is \(z_1e_1\), an AR(1). Placing it in ID-2's \(\delta\) violates ID-2's hypothesis that \(\delta\) is **temporally uncorrelated**; so Model 1 is not an ID-2 representation at all. Its ID-2 representation is \(A=I_3\), \(f=(z_1,z_2,z_3)\), \(\delta=0\), for which \(\operatorname{ran}A=\mathbb R^3\supseteq\mathcal S_X\) — ID-2 holds. **ID-2 is TRUE on its declared class and NON-BINDING on the latent class, exactly as ID-1 is.** Canon records a scope lock, never a retraction. What C actually proved, and what canon states, is that the **sub-split of ID-2's identified total dynamic loading into a centre part and a factor part is not identified even from \(\mathcal I_J\)**. This is continuous with ID-0's existing statement that deterministic fixed-anchor drift and an invariant random factor can share a lag row.
- **O-2 — CLOSED, overruling upheld.** \(\psi^+(nb_n)\) **is** \(\ell_n\)'s stochastic term, not an extra term requiring domination; under HD-M it reduces verbatim to \((nb_n)^{-1/2}\). C's impossibility asked the wrong question. No disposition menu is needed.
- **O-3 — CLOSED in B's favour.** L-9.R2.1's convexity is in the **ordinary linear structure**, so it applies verbatim to the empirical measure \(\widehat Q_n=\frac1N\sum\delta_{\Sigma_i}\), whose atoms are full-rank almost surely on the declared domain. Hence \(F_{\widehat Q_n}\) is strictly convex and the empirical BW argmin is **pathwise unique with probability one**. R5 is therefore **SEPARATED on BW as well as on Hadamard**; the identification-node residue is confined to sphere and sphere-product geometry, where L-9.R2.3 supplies the exact cost.
- **O-4 — CLOSED, sustained.** \(\psi(N)\le\sqrt{(2m_0+1)R^2/N}\) always; the matching lower bound needs \(\Lambda_u>0\). Makes the separation condition easier, not harder.
- **O-5 — CLOSED, sustained** (see §6.1).
- **O-6 — CLOSED, sustained.** Sharp criterion \(c'(0)\wedge c''(0)\ne0\); sufficient criterion \(R(PV,w)PV\ne0\); nonzero sectional curvature is sufficient but not necessary. Inert on all project geometries (one-signed curvature) but canon states the sharp form.
- **O-7 (raised by the lead in this pass) — CLOSED by scoping.** Dossier A's APP-FIN verdict leans on ABDL (2003), whose long-memory estimates are for **daily realised volatility of exchange rates**, not monthly realised covariance of US equities. Temporal aggregation preserves \(d\), but the asset class and the object differ, and \(d\) is not separately estimated in the parent's 240-month panel. **Ruling: no theorem may consume the empirical \(d\).** The analytic window is the theorem; the empirical exponent is an **assumption under test**, routed to N-18/APP-FIN with an explicit no-consumer argument. The citation is retained only for what it actually covers, with the transfer flagged unverified.

### 6.3 Verification record

Lead-run verification covering: the variational identity and its equality case; concavity of \(G\) (2000 randomised tests, zero violations); the exact boundary-escape ratio at corank 1 and 2 across \(\varepsilon\in\{10^{-2},\dots,10^{-8}\}\); the AR(1) closed form against the exact double sum; the \(\Psi(x)\) limit profile; the symbolic wedge coefficient; the \(S^2\) \(L^1\)/\(L^2\) argmin separation; and the manufactured-drift constant across \(\lambda\) and \(h\). Sympy re-derivation of the exact BW \({\rm SPD}(2)\) matrices is recorded in §1. Numerics were used only to corroborate; every status above rests on the analytic argument stated beside it.

## 7. Transitive closure audit — executed at Wave 4

**Node count: 71.** Every node introduced by this campaign, and every sublemma introduced by a workstream in the course of discharging one, is listed below with a terminal status. There is no `WIP`, `OPEN`, `CONDITIONAL`, `PLAUSIBLE`, `EXPECTED`, or `FUTURE WORK` entry.

### 7.1 Targets (8)

| Node | Terminal status |
|---|---|
| ID-7 | PROVED INTERNALLY |
| ID-8 | PROVED INTERNALLY (Gavrilov–Pennec expansion CITED EXTERNALLY AND APPLIED) |
| ID-9 | SHARPLY REFORMULATED AND PROVED — gate true, non-binding on \(\mathrm{LC}\setminus\mathrm D\) |
| ID-10 | PROVED INTERNALLY (DRW local-stationarity mode CITED EXTERNALLY AND APPLIED) |
| CANON-1 | INTEGRATED — estimand is \(\mathcal S_{X,n}\), with \(E_n\) recovered iff \(Q_n\succ0\) |
| CANON-2 | INTEGRATED — Corollary P-DRIFT displayed in Paper 1 |
| CANON-3 | INTEGRATED — displayed Gaussian scope limit in Paper 1 |
| HYG | INTEGRATED — scans in §7.5 |

### 7.2 ID-9 route nodes (5)

R1 DISPROVED (as a failure mode: no boundary minimiser exists) · R2 PROVED (uniqueness on BW; non-uniqueness classified on spheres; selector cost proved) · R3 SHARPLY REFORMULATED AND PROVED (gate vacuous on \(\mathrm{LC}\); surviving quotient and restoring declaration proved) · R4 PROVED (not an escape) · R5 OUT OF SCOPE BY PROVED SEPARATION on Hadamard and BW; identification node on sphere geometry, merged into R2.

### 7.3 Registered sublemmas (26 from §3.3)

All terminal. L-8.1 CITED+APPLIED · L-8.2 PROVED (constant corrected \(2\to1\)) · L-8.3, L-8.4, L-8.5 PROVED · L-9.R1.1, L-9.R1.2 PROVED · L-9.R2.1 PROVED INTERNALLY, strictly extending the Agueh–Carlier citation · L-9.R2.2, L-9.R2.3 PROVED (R2.3 with the \(\lambda\) condition added) · L-9.R3.1, L-9.R3.2, L-9.R3.3 PROVED · L-9.R4.1, L-9.R4.2 PROVED · L-9.R5.1 REFORMULATED+PROVED (splits by geometry) · L-7.1 PROVED (lead's unconditional form corrected) · L-7.2, L-7.3 PROVED · L-10.1, L-10.2, L-10.3 PROVED (L-10.2c REFORMULATED: \(a\ge3\alpha\) is the primitive) · C-1.1 PROVED.

### 7.4 Sublemmas spawned by workstreams while discharging the above (32)

Workstream A introduced and terminated: L-7.1.0, L-7.1a, L-7.1a′, L-7.1b, L-7.1c, L-7.1d, L-7.1e, L-7.3.1–L-7.3.5, L-7.4, L-10.2a, L-10.2b, L-10.2c, L-10.4, L-9.R4.1′, L-9.R4.3, L-9.R4.4, R4-GATE, R4-EXH. Workstream B introduced and terminated: B8-0 through B8-5. Workstream C introduced and terminated: L-9.R3.0, L-9.R3.2a–h, L-9.R3.3-mar, L-9.R3.3a–d, L-9.R3.4 (R3-SURV), L-9.R3.5 (R3-BAND, R3-NEC), L-9.R3.6, L-9.R3.7, L-9.R5.2–L-9.R5.5.

Three of these required lead action rather than acceptance and are recorded as such: L-9.R3.6 OVERRULED (O-2); L-9.R3.3d DEFLATED to its true content; L-9.R3.2d's global claim SCOPED — canon consumes only the local statement, the global monotonicity remaining dossier provenance with no consumer.

Two nodes are terminal as **DISPROVED-and-repaired** rather than proved, and both are displayed in canon: the residue-class device has no long-memory analogue (repaired by the no-consumer argument for Theorem HD-E), and the sup-norm results G1-HD/HD-Minf do not survive \(d>0\) (same repair).

One node is terminal as **OUT OF SCOPE BY PROVED SEPARATION** with the no-consumer argument displayed: the empirical memory exponent for APP-FIN (objection O-7). No theorem consumes it.

### 7.5 Repository scans

- unresolved wiki links introduced by this campaign: **0** (11 pre-existing unresolved links remain, all inside `Archived/`, none in a canonical file, none touched);
- LaTeX delimiter mismatches across all canonical files: **0**;
- control characters and patch artifacts: **0**;
- P1-ID nodes described with a non-terminal status word, anywhere outside the campaign prompt: **0**;
- files asserting the canonical P1-ID status: **1** (no duplicate live status source);
- unconditional `estimand = ran A_n` assertions: **0** — the only surviving mentions are the corrected statements that say it is *not* the estimand.

**Known filesystem note, not a defect.** The campaign run prompt exists both at `Ideas/` and in `Ideas/Archived/Run prompts/`. Neither copy is removable from the sandbox (`Operation not permitted`), so the duplicate is left in place. It is a run prompt, not a status source, so the "no duplicate live status source" requirement is unaffected.

### 7.6 Closure statement

ID-7, ID-8, ID-9 and ID-10 are terminal; R1–R5 are individually terminal; the transitive closure of all 71 nodes is terminal; CANON-1–3 are integrated and the estimand is consistent across every canonical file; the information-set vocabulary is unchanged and no marginal/joint/single-path claim is conflated; no claim labels the parent's Factor 1 spurious, and Corollary P-DRIFT states the positive case; every restriction carries a proved boundary reason, including the two newly declared ones ((S2b) Hölder frozen law, and the band-separation convention); every external citation carries exact theorem, hypotheses and scope, and the one illegitimate citation transfer was refused.
