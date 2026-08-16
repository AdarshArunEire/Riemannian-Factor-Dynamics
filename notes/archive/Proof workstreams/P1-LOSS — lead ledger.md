---
type: working-lead-ledger
title: P1-LOSS — lead ledger
status: active-campaign
last-audited: 2026-08-14
authority: single adjudication authority for the P1-LOSS campaign; canonical status lives in the canonical files after Wave 4
---

# P1-LOSS — lead ledger

> **Volatile-context discipline.** Every verdict is written here at the moment it is established. On any interruption, re-read §1 (state summary) and continue from "next action". Workstream dossiers are `P1-LOSS-A/B/C` in this directory. Agents write only their own dossier; the lead merges. The lead authors no workstream dossier and is therefore an admissible hostile auditor of last resort.

## 1. State summary (rewrite on every checkpoint)

- **Campaign objective.** Settle whether a Riemannian geodesic loss can be proxy-robust; prove the exact induced bias and its constructive companions; close E1–E5 to terminal verdicts; prove the separation from the closed estimation theorems; integrate with no open node in the transitive closure.
- **Wave:** 1 dispatched 2026-08-14; **INTERRUPTED**; re-executed by the lead.
- **INTERRUPTION RECORD (checkpoint, not a terminal event).** The three Wave-1 workstream agents A, B, C were terminated by a session credit limit after 5, 9 and 24 tool calls respectively. **No agent wrote any dossier and no agent returned a verdict. Nothing from those partial runs is recorded as a result.** Per §"Persistence and interruption discipline" the campaign continues. Resumption rule adopted: the lead executes the Wave-1 derivations itself and **authors dossiers A, B and C**, recording that authorship explicitly. The consequence is recorded honestly in §6: the lead is no longer an admissible non-author auditor for the claims it authored, so the Wave-3 hostile audit must be performed by fresh non-author agents, and where that is impossible the closure statement must say so rather than claim a clean non-author audit.
- **Last verified step (lead, independent computation).** All load-bearing computations re-derived in closed form and verified numerically in `/home/claude/verif`:
  (i) scalar identity \((\mathbb E\sqrt x)^2=\mathbb E[x]-\operatorname{Var}(\sqrt x)\) to machine precision;
  (ii) matrix second-order BW, AIRM and log-Euclidean induced-bias formulas checked against exactly-solved barycentres of random discrete laws — relative error halves when the noise scale halves, the signature of a correct second-order formula;
  (iii) Wishart fourth-moment tensor gives **exactly** zero off-diagonal bias (machine zero) and matches the closed diagonal forms to \(10^{-17}\);
  (iv) a non-Wishart two-point proxy gives **nonzero** off-diagonal bias and a genuinely rotated eigenbasis — so "the distortion is purely spectral" is a property of the noise model, not of the geometry;
  (v) the exact scalar ranking reversal in closed form for \(a\in(0,1]\);
  (vi) \(\Gamma(cH)=\sqrt c\,\Gamma(H)\) exactly.
- **Next action:** (1) write dossiers A, B, C; (2) dispatch narrow single-purpose agents for primary-source verification (Patton, Laurent–Rombouts–Violante, Gneiting/Savage) and for the LO-7 paper hunt; (3) Wave 3 hostile audit by non-authors; (4) LO-6, canonical integration; (5) transitive closure audit; (6) commit.

## 2. Locked vocabulary (do not vary)

- **Target functional** \(\theta(\mathcal F)\): the conditional functional a forecast is meant to report. Default here: the conditional mean \(\Sigma_t=\mathbb E[\Sigma^\ast_t\mid\mathcal F_{t-1}]\) of the latent covariance.
- **Proxy** \(\widehat\Sigma_t\): an observable ex-post estimate. **Conditionally unbiased in coordinate \(\varphi\)** means \(\mathbb E[\varphi(\widehat\Sigma_t)\mid\mathcal F_{t-1}]=\varphi(\theta)\). Default \(\varphi=\mathrm{id}\) on \(\mathrm{Sym}(m)\).
- **Loss** \(L(\text{proxy},\text{forecast})\), first argument always the realisation.
- **Forecast class** \(\mathcal H\): the set of forecasts actually compared.
- **Proxy-robust** (Patton's notion): for all \(H_1,H_2\in\mathcal H\) and all admissible proxy laws, \(\operatorname{sign}\{\mathbb E L(\widehat\Sigma,H_1)-\mathbb E L(\widehat\Sigma,H_2)\}=\operatorname{sign}\{\mathbb E L(\Sigma^\ast,H_1)-\mathbb E L(\Sigma^\ast,H_2)\}\).
- **Consistent for \(\theta\)** (Savage/Gneiting): \(\theta(\mathcal F)\in\arg\min_H\mathbb E[L(\cdot,H)]\); strictly consistent if the argmin is the singleton.
- **Estimation** vs **evaluation**: estimation produces \(\widehat E_n,\hat\mu_n\) from the observed array; evaluation scores a forecast against a proxy. This campaign touches only the second. The words are never interchanged.

Status codes (no others are terminal): `PROVED`, `CITED+APPLIED`, `DISPROVED`, `REFORMULATED+PROVED`, `SUPERSEDED`, `SEPARATED`. `WIP` is non-terminal and may not survive Wave 4.

## 3. Node register

### 3.1 Target slots

| ID | Statement (short) | Producer | Consumer | Status |
|---|---|---|---|---|
| LO-1 | characterise the proxy-robust loss class for matrix-valued forecasts; settle whether robust ranking ⟺ consistency for the conditional mean; verify Patton (2011) and Laurent–Rombouts–Violante (2013) against primary sources | A | LO-2, LO-4, canonical boundary, References | WIP |
| LO-2 | is squared Bures–Wasserstein distance proxy-robust? | B | LO-3, LO-4, Paper 1 | WIP |
| LO-3 | exact induced bias, scalar and matrix; spectral vs eigenvector distortion | B | LO-5, LO-6, N-row | WIP |
| LO-4 | general no-go for non-flat Riemannian geodesic losses; sharpness | A | canonical boundary | WIP |
| LO-5 | constructive companions: infill rate and recalibration | B | Paper 1, App map, N-row | WIP |
| LO-6 | proved separation from the closed estimation theorems | lead | Analytical reconstruction, all canonical | WIP |
| LO-7 | external-work positioning, verified verbatim or withdrawn | C | canonical boundary, References | WIP |
| HYG | worktree, links, LaTeX, duplicate-status, containment scan | lead | repository | WIP |

### 3.2 Escape-route nodes

| ID | Route | Owner | Status |
|---|---|---|---|
| E1 | weaken the robustness notion (restricted forecast class, local robustness, monotone transform) | A | WIP |
| E2 | change the target to the conditional Fréchet barycentre | C | WIP |
| E3 | change the proxy: conditionally unbiased for \(\Sigma^{1/2}\) or \(\log\Sigma\) | C | WIP |
| E4 | restrict the forecast class | A | WIP |
| E5 | infill asymptotics; microstructure-noise conflict | B | WIP |

### 3.3 Sublemma register (every entry must terminate)

| ID | Statement | Producer | Consumer | Status |
|---|---|---|---|---|
| L-1.1 | robustness over a rich proxy class ⟹ \(L(y,h)=\psi(y)+a(h)+b(h)\cdot y\) | A | LO-1 | WIP |
| L-1.2 | that form + \(L\ge0\), \(L(h,h)=0\) ⟹ \(L=B_\varphi\) Bregman, \(\varphi\) strictly convex | A | LO-1 | WIP |
| L-1.3 | Bregman ⟹ robust (exact, not merely in ordering) | A | LO-1 | WIP |
| L-1.4 | Bregman ⟺ strictly consistent for the mean (Savage/Gneiting), and the exact class of laws on which the equivalence holds | A | LO-1, E1 | WIP |
| L-1.5 | Patton (2011) primary-source verification: exact proposition, hypotheses, scalar-only scope | A | References | WIP |
| L-1.6 | Laurent–Rombouts–Violante (2013) primary-source verification: matrix statement, necessity, invertibility hypotheses | A | References | WIP |
| L-1.7 | multivariate QLIKE: does ranking survive a singular proxy? | A | Paper 1 advice | WIP |
| L-4.1 | symmetric Bregman ⟹ generator quadratic ⟹ squared Mahalanobis (low-regularity proof, no \(C^3\) assumption) | A | LO-4 | WIP |
| L-4.2 | \(d_g^2\) is a quadratic form in the linear coordinate ⟺ \(g\) is a constant metric in that coordinate | A | LO-4 | WIP |
| L-4.3 | flat-but-misaligned counterexample: log-Euclidean is flat and still not robust for a \(\Sigma\)-unbiased proxy | A | LO-4 sharpening | WIP |
| L-2.1 | \(d_{\rm BW}^2\) is strictly convex, not affine, in its first argument | B | LO-2 | WIP |
| L-2.2 | BW barycentre fixed point \(\mathbb E[(H^{1/2}\widehat\Sigma H^{1/2})^{1/2}]=H\) from \(\mathbb E[\mathrm{Log}_H\widehat\Sigma]=0\) | B | LO-3 | WIP |
| L-3.1 | scalar exact bias \(H^\star=\mathbb E[x]-\operatorname{Var}(\sqrt x)\) | B | LO-3 | WIP |
| L-3.2 | matrix second-order bias in Sylvester form | B | LO-3 | WIP |
| L-3.3 | commuting/fixed-eigenbasis case: bias is exactly eigenvalue-wise, zero eigenvector rotation | B | LO-3 | WIP |
| L-3.4 | general noncommuting case: exact condition for zero second-order eigenvector rotation; generic failure | B | LO-3, LO-6 | WIP |
| L-3.5 | Wishart/Gaussian-fourth-moment proxy: eigenvector rotation vanishes at second order; closed-form diagonal | B | LO-3, LO-5 | WIP |
| L-5.1 | infill rate of the distortion and its uniformity over the forecast class | B | LO-5 | WIP |
| L-5.2 | what a scalar Mincer–Zarnowitz recalibration restores and does not restore | B | LO-5 | WIP |
| L-5.3 | gap-corrected loss: feasible order improvement | B | LO-5, E1 | WIP |
| L-5.4 | microstructure noise vs conditional unbiasedness: trade-off or conflict | B | E5 | WIP |
| L-6.1 | no evaluation node is an ancestor of any estimation node; explicit edge audit | lead | LO-6 | WIP |
| L-6.2 | the one real edge: proxy measurement error enters the existing \(\zeta_n\) and centre-path budgets at an explicit order | lead | LO-6 | WIP |
| L-7.1 | identify the geometric-deep-learning paper and quote its displayed training loss, target, and evaluation | C | LO-7 | WIP |

## 4. Lead's candidate routes (dispatched as hypotheses, NOT as results)

Recorded here so they can be attacked. None of these is a campaign result until a non-author workstream derives it independently and the lead re-verifies.

1. **LO-1.** Robustness over a class containing all two-point conditional laws forces \(L(y,h)=\psi(y)+a(h)+b(h)^\top y\); normalisation \(L(h,h)=0\) and \(L\ge0\) then force \(b=-\nabla\psi\), i.e. Bregman. Conversely Bregman gives an exactly \(h\)-free Jensen offset. Equivalence with mean-consistency holds on rich classes and **can fail on restricted classes** — that restriction is the whole content of E1/E4.
2. **LO-4 symmetry step.** Symmetric Bregman ⟹ trapezoid rule exact along every segment ⟹ generator quadratic along every line ⟹ quadratic ⟹ squared Mahalanobis. The candidate headline "the robust class is flat" is suspected **necessary but not sufficient**: the sharp criterion should be "flat *and* the proxy's unbiasedness coordinate is an affine chart". Log-Euclidean is the suspected witness that separates the two.
3. **LO-2/LO-3.** \(d_{\rm BW}^2\) is strictly convex in its first argument, hence not Bregman; the minimiser is the BW barycentre; scalar bias \(\mathbb E[x]-\operatorname{Var}(\sqrt x)\); matrix bias \(-\Sigma^{-1/2}\mathbb E[G^2]\Sigma^{-1/2}\) with \(\Sigma G+G\Sigma=\Sigma^{1/2}\Delta\Sigma^{1/2}\).
4. **LO-3 spectral claim.** Suspected **false in general and true for Wishart-type proxies**. If so the informal "the distortion is almost entirely in the eigenvalues" is a property of the noise model, not of the geometry, and must be restated as such.
5. **E1/E4.** Suspected positive result: *local* robustness on the far-from-truth class, with failure exactly on the near-optimal class and on level-differing comparisons.
6. **E2.** Suspected fatal objection: the conditional BW barycentre *of the proxy* depends on the proxy's conditional variance, hence on the sampling scheme; it is not a DGP functional.
7. **E3.** Suspected fatal obstruction: \(\int\sigma_s\,ds\ne(\int\sigma_s^2\,ds)^{1/2}\), so no infill-consistent estimator is conditionally unbiased for \(\Sigma^{1/2}\) outside constant volatility on the window.
8. **E5.** Distortion \(=\) proxy conditional variance transformed by the Sylvester operator, so \(O(M^{-1})\); relative distortion suspected to **grow with matrix size**, which would make it non-negligible at APP-FIN's monthly-from-daily sampling.

## 5. Objection ledger

Wave 3 was executed by two **non-author** hostile auditors: one on dossier A, one on dossiers B and C. Records: [[P1-LOSS — Wave 3 audit A]], [[P1-LOSS — Wave 3 audit BC]]. Both re-derived every load-bearing computation independently rather than checking the dossiers' algebra by reading it. Neither auditor wrote the dossier it audited.

**Verdict of record: two FATAL findings against dossier A, both against the *proof* of the characterisation and neither against the headline; no fatal finding against B or C; no route verdict changed.**

| # | Objection | Raised by | Disposition |
|---|---|---|---|
| O-1 | **A-1.1 is false as stated.** \(L(y,h)=(1+h^2)e^y\) is proxy-robust over every class and is not affine in \(y\). Richness cannot save it | audit A (FATAL) | **SUSTAINED.** The normalisation \(L\ge0,\ L(h,h)=0\) belongs in A-1.1's hypotheses, not only in A-1.2's. Repaired: A-1.1 and A-1.2 are merged into one normalised statement A-1.1′ |
| O-2 | **A-1.1's proof is a non sequitur.** The indifference-surface move replaces \(\Phi\) by a different function; and two-atom laws at a single mean give only odd homogeneity, not affinity, in dimension \(\ge2\). Explicit witness: \(\rho(w)=w_1+w_2^3/(w_1^2+w_2^2)\) | audit A (FATAL) | **SUSTAINED.** The proof is retracted and replaced. The repaired route does not need affinity at all: *robustness plus normalisation implies strict consistency for the conditional mean in one line*, after which the Savage/Gneiting–LRV characterisation applies. Three-atom richness replaces two-atom richness where an internal necessity proof is wanted. See A §2.1′ |
| O-3 | \(\mathcal A\succ0\) in A-4.3 is false; degenerate \(\mathcal A\succeq0\) is robust | audit A | **SUSTAINED.** \(\mathcal A\succeq0\) for robustness, \(\mathcal A\succ0\) for strict consistency. Corrected |
| O-4 | "symmetric" does not typecheck on \(\mathcal Y\times\mathcal H\) when \(\mathcal Y\ne\mathcal H\) | audit A | **SUSTAINED.** LO-4 is stated on \(\mathcal H\times\mathcal H\) (the open cone) with the boundary extension by continuity named explicitly |
| O-5 | Gneiting Theorem 3.1 is **scalar** (\(I\subseteq\mathbb R\)); dossier A used it for the matrix case while flagging only Patton's scalar scope | audit A | **SUSTAINED.** The matrix producer is Laurent–Rombouts–Violante Proposition 3, which is matrix-valued and necessary-and-sufficient. Gneiting is retained for the scalar case only. Their \(C^2\) hypothesis is recorded |
| O-6 | A-E4.2's "iff" is false: an explicit pair with non-constant \(\Gamma\) has its ranking preserved | audit A | **SUSTAINED.** Constancy of \(\Gamma\) is **sufficient**; necessity holds only on classes containing an indifference pair. Corrected |
| O-7 | A-E1.2's "iff" is not proved; only the "if" direction is | audit A | **SUSTAINED.** Restated as a sufficient condition plus the exact failure witness at \(\eta=0\) |
| O-8 | \(\nabla_H\Gamma=O(\varepsilon^2)\) uniformly is asserted, and the pointer to B-3.2 is wrong | audit A | **SUSTAINED.** Restricted to compact subsets of the cone bounded away from the boundary, with the derivative computed from the exact \(\Gamma\) rather than asserted |
| O-9 | A-4.1's last step ("quadratic on every line \(\Rightarrow\) polynomial") is asserted, and the stated criterion is insufficient | audit A | **SUSTAINED.** Repaired by continuity of convex \(\psi\) on the interior plus Fréchet's theorem (\(\Delta_v^3\psi\equiv0\) and continuity \(\Rightarrow\) quadratic polynomial). The auditor's own counterexample hunt in dimensions 1 and 2 found nothing; the theorem is true and now has a complete proof |
| O-10 | **B-5.2's stated range is wrong at both ends.** The correct range of the BW relative distortion is \([\,1/(2M),\ (m-\tfrac12)/M\,]\); \((m+1)/(4M)\) is the *isotropic* value, an interior point | audit BC (MATERIAL) | **SUSTAINED.** The \(k=i\) term contributes exactly \(1/4\) always, so the infimum is \(1/(2M)\); when \(\lambda_i\) is dominated the sum tends to \(m-1+\tfrac14\). At \(m=12\) the true upper end is \(11.5/M\), a factor \(3.54\) larger than the figure the dossier gave. This makes the finding **stronger**, not weaker. Corrected |
| O-11 | **B-5.5/B-5.6's recalibration map is inverted.** \(\mathbb EL(\widehat\Sigma,u)\) is minimised at \(u=\Phi(\Sigma)\), so the map a conditional-mean forecaster must apply is \(\rho=\Phi\), not \(\Phi^{-1}\); the AIRM constant is \(c=1-\tfrac{m+1}{2M}\), not its reciprocal | audit BC (MATERIAL) | **SUSTAINED.** Corrected. The qualitative content (exact for AIRM, partial for BW) is confirmed by the auditor's independent computation |
| O-12 | **C-E3.2's theorem does not follow from Cauchy–Schwarz.** C–S excludes the absolute-variation family; it does not exclude every estimator. Counterexample: with a *known* within-window volatility shape an unbiased and consistent estimator exists | audit BC (MATERIAL) | **SUSTAINED and the claim is narrowed to what is proved.** The obstruction now has a stated boundary: it excludes (i) the absolute-variation/bipower family by Cauchy–Schwarz and (ii) every continuous function of realised covariance by strict operator concavity of the square root. A general impossibility over *all* estimators is **not** claimed, and the boundary reason — no auxiliary knowledge of the within-window volatility path — is stated. E3's route verdict is unchanged |
| O-13 | **C-E2.2 contradicts itself** ("not consistent" in the table, "consistent under infill" in the body) — the exact conflation the campaign polices — and quotes B-3.5's constant for a setting B-3.5 was not derived for | audit BC (MATERIAL) | **SUSTAINED.** Corrected to: not consistent at fixed \(M\); consistent as \(M\to\infty\) at rate \(\Theta(M^{-1})\); the constant is **not** B-3.5's, because B-3.5 assumes a degenerate latent law. The auditor measured \(\text{gap}\times M\to1.149\) against B-3.5's \(1.321\) |
| O-14 | **B-5.3's flagship numbers are labelled "PROVED (arithmetic)" but rest on a truncated expansion with no remainder bound.** Exact values differ | audit BC (MATERIAL) | **SUSTAINED.** The lead had independently computed exact Wishart barycentres before the audit returned and the two computations agree. The canonical numbers are now the **exact** ones: BW \(8.82\%\to35.86\%\), AIRM \(32.92\%\). The second-order formula understates by \(3\)–\(8\%\) of itself. Label corrected from PROVED to PROVED-BY-EXACT-COMPUTATION, and the second-order figures are labelled as the approximation they are. "Shrinks by roughly a third" is true of AIRM and not of BW (BW mean \(\approx19\%\)); corrected |
| O-15 | **B-3.5's commentary is wrong in the project's favour**: for a genuine Wishart the eigenvector rotation is not \(O(M^{-2})\), it is **exactly zero at every order**, by sign-flip equivariance of the Wishart law plus orthogonal equivariance and uniqueness of the BW barycentre | audit BC (MINOR) | **SUSTAINED — a strengthening.** Corrected, with the equivariance argument recorded. The lead's off-diagonal figure \(5.7\times10^{-3}\) is a Monte-Carlo floor, not a measured rotation; corrected |
| O-16 | C-7.2's "entirely invisible" does not follow from second-order scalarity — but is **exactly** true by an argument not given (congruence-equivariance of the Karcher mean plus orthogonal invariance of the Wishart law) | audit BC (MINOR) | **SUSTAINED — a strengthening.** Corrected, with the exact \(h\) recorded |
| O-17 | B-3.3's rotation criterion and angle break at \(\lambda_i=\lambda_j\), and near-degeneracy is where second-order rotation is largest; no non-degeneracy hypothesis was stated | audit BC (MINOR) | **SUSTAINED.** Non-degeneracy hypothesis added, and the degenerate case handled by rotation within the eigenspace |
| O-18 | B-2.4's restriction \(a\in(0,1]\) bounds the parameterisation, not the phenomenon — the reversal holds on all of \((0,2)\); and at \(a=1\) the proxy charges the boundary, violating B-2.2's own hypothesis | audit BC (MINOR) | **SUSTAINED.** Restricted to \(a\in(0,1)\) for the closed form, with the wider range recorded as the true extent |
| O-19 | Dossier B §7's blanket "no status rests on numerics alone" is false; three claims do | audit BC (MINOR) | **SUSTAINED.** The three are named and either proved or relabelled |
| O-20 | B-E5.2's prose is disproportionate: the drift constant is roughly \(50\times\) smaller than the distortion constant | audit BC (MINOR) | **SUSTAINED.** Order retained, prose proportioned |
| O-21 | C-ATT was not independently audited (it rests on A-4.2/A-4.3, outside the BC auditor's write scope) | audit BC | **SUSTAINED and recorded.** C-ATT is a corollary of A-4.3, which audit A did audit; it carries no independent content. Recorded in the closure statement rather than claimed as separately audited |

**Not sustained / no change:** the auditors found no route verdict that changes. LO-2, LO-3, LO-5, LO-7, E2, E3 and E5 stand. The headline LO-4 stands **with correction** — its statement needed \(\mathcal A\succeq0\), a domain condition, and "affinely parametrised" rather than "affine chart"; its proof needed a different first link.

## 6. Wave 3 — audit record and the honesty note this campaign owes

Because the Wave-1 agents were killed before writing anything, **the lead authored dossiers A, B and C.** The lead is therefore not an admissible non-author auditor of them. That is why Wave 3 was executed by two fresh agents that authored none of the three, and why their findings were adopted rather than argued with: two FATAL defects in dossier A's proof were found and both are real.

What this run can honestly claim: every load-bearing computation has been derived twice, once by the lead and once by an auditor who did not see the lead's scripts, and the two agree. What it cannot claim: three independent workstreams reaching the results separately. The single-author origin of the mathematics is a real limitation of this campaign and is recorded here rather than concealed by the two-stage structure.

## 7. Transitive closure audit — executed at Wave 4

**Node count: 107.** Every node introduced by this campaign, and every sublemma introduced while discharging one, is listed below with a terminal status. There is no `WIP`, `OPEN`, `CONDITIONAL`, `PLAUSIBLE`, `EXPECTED` or `FUTURE WORK` entry.

### 7.0 Proportionality budget — recorded before integration, checked after

Budget set at the start of Wave 4, before the canonical file was written: **Paper 1, 450–600 words**; one subsection in the reconstruction ledger; **one** row in the application-map preflight; **one** numerical row; a references block; a scoped canonical boundary file.

Realised: Paper 1 **455 words** (365 in the displayed CANON-4 scope limit plus four exclusion bullets) — inside budget. Reconstruction §7A **355 words**. Application map: one row. Numerical suite: one row (N-19). Canonical boundary: 27 KB, which is larger than the other branch boundaries (FRAME-2P-U 8 KB, HE 10 KB, BW-FIXED-MARGIN 10 KB) because it must carry five route dispositions and their counterexamples, as the campaign contract requires; it is well below P1-ID's 49 KB. **The footprint that matters for proportionality is the programme-facing one, and that is one displayed remark in Paper 1, one paragraph in the ledger, one preflight row and one diagnostic row.**

### 7.1 Targets (8)

| Node | Terminal status |
|---|---|
| LO-1 | PROVED INTERNALLY (robustness ⟹ consistency; converse) + CITED EXTERNALLY AND APPLIED (LRV Prop 3 for the matrix Bregman step; Gneiting Thm 3.1 scalar) |
| LO-2 | DISPROVED — squared BW is not proxy-robust, with an exact closed-form ranking reversal |
| LO-3 | PROVED INTERNALLY — scalar exact; matrix second order; the spectral-versus-rotation question SHARPLY REFORMULATED AND PROVED (true for Wishart-type proxies exactly at all orders, false in general with an explicit counterexample) |
| LO-4 | SHARPLY REFORMULATED AND PROVED — "the robust class is flat" is necessary but not sufficient; the sharp criterion is flat **and** affinely parametrised in the proxy's coordinate |
| LO-5 | PROVED INTERNALLY — infill rate \(\Theta(m/M)\), exact flagship magnitudes, and the recalibration dichotomy |
| LO-6 | PROVED — separation by edge audit, with the single \(\zeta_n^{\rm proxy}=O(m/M)\) edge into an existing budget displayed |
| LO-7 | CITED+APPLIED (verbatim) for what the paper does, REFORMULATED+PROVED for the GMV clause, which is this campaign's theorem and not an attribution |
| HYG | INTEGRATED — scans in §7.6 |

### 7.2 Escape-route nodes (5)

E1 REFORMULATED+PROVED (no weakening admits a non-flat geodesic loss as exactly robust; local robustness and gap correction are stated with their exact cost) · E2 DISPROVED as an escape (the proxy barycentre is not a DGP functional; the latent barycentre is not estimated, only approached) · E3 DISPROVED as an escape, with a stated boundary (no auxiliary knowledge of the within-window volatility path) · E4 REFORMULATED+PROVED (exact cancellation on \(\Gamma\)-level sets and symmetry orbits, and on nothing richer) · E5 REFORMULATED+PROVED (infill conflicts with microstructure noise; consistency is not conditional unbiasedness).

### 7.3 Workstream claims (61)

Dossier A (23): A-1.1 **DISPROVED and retracted** · A-1.1′, A-1.2, A-1.3, A-1.4, A-1.4b PROVED · A-1.5, A-1.6 CITED+APPLIED · A-1.7 REFORMULATED+PROVED · A-4.1 PROVED INTERNALLY (with the \(C^2\) form CITED) · A-4.2 PROVED · A-4.3 REFORMULATED+PROVED · A-4.4 PROVED and independently corroborated · A-4.5 PROVED · A-E1.1 DISPROVED as an escape · A-E1.2 PROVED as sufficiency plus an exact failure witness · A-E1.3 PROVED · A-E1 REFORMULATED+PROVED · A-E4.1, A-E4.3, A-E4.4 PROVED · A-E4.2 PROVED as sufficiency, original "iff" DISPROVED · A-E4 REFORMULATED+PROVED.

Dossier B (23): B-2.1, B-2.2, B-2.4, B-3.1, B-3.2, B-3.3, B-3.4, B-3.5, B-3.7, B-3.8, B-5.1, B-5.2, B-5.3, B-5.4, B-5.5, B-5.6, B-5.7 PROVED · B-2.3 DISPROVED · B-3.6 DISPROVED as a general claim · B-E5.1 PROVED/CITED+APPLIED · B-E5.2, B-E5.3 CITED+APPLIED · B-E5 REFORMULATED+PROVED.

Dossier C (15): C-E2.1, C-E2.2, C-E2.3, C-E3.1, C-E3.3, C-E3.4, C-7.1, C-7.2, C-7.3 PROVED · C-E3.2 REFORMULATED+PROVED with its boundary stated · C-E2, C-E3 DISPROVED as escapes · C-7.4 CITED+APPLIED · C-7.5 REFORMULATED+PROVED · C-ATT PROVED as a corollary of A-4.3.

### 7.4 Ledger sublemma register and the two nodes with no dossier home

The §3.3 register (24 entries L-1.1 … L-7.1) is a planning index; each entry maps one-to-one onto a dossier claim listed in §7.3 and is **not** counted twice. Two entries have no dossier home because the lead owns them: **L-6.1** (no evaluation node is an ancestor of an estimation node) and **L-6.2** (the single \(\zeta_n\) edge and its order). Both are PROVED, in [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]] §6.

### 7.5 External producers (10) and objections (21)

External (10): Patton (2011) Def 1 + Prop 1 · LRV (2013) Prop 3 + Cor 1 · Gneiting (2011) Thm 3.1 · Boissonnat–Nielsen–Nock Lemma 2 · Barndorff-Nielsen–Shephard (2002) · Zhang–Mykland–Aït-Sahalia (2005) Eq. (18) and Thm 4 · realised kernels · pre-averaging · Bucci–Palma–Zhang arXiv:2412.09517 · the Daleckiĭ–Kreĭn second-derivative formula. All CITED+APPLIED with exact result, hypotheses and scope, **except** Savage (1971), which could not be obtained and is therefore **OUT OF SCOPE BY PROVED SEPARATION**: no claim consumes its text, and Gneiting Theorem 3.1 — which is verified verbatim — is the producer. One citation transfer was refused on those grounds rather than made on memory.

Objections (21): O-1 … O-21, all disposed in §5. Two were FATAL and both were sustained in full; the affected node (A-1.1) terminates as DISPROVED and its consumer is repaired rather than weakened. Three objections **strengthened** the campaign's results (O-10, O-15, O-16).

**8 + 5 + 61 + 2 + 10 + 21 = 107 nodes, all terminal.**

### 7.6 Repository scans

- unresolved wiki links introduced by this campaign: **0** (one apparent match is a NumPy array printed inside a fenced code block in an audit file, not a link);
- LaTeX delimiter mismatches in every file this campaign touched: **0**;
- control characters and patch artifacts: **0**;
- P1-LOSS nodes described with a non-terminal status word in any canonical file: **0**;
- files asserting canonical P1-LOSS status: **1** (no duplicate live status source);
- files touched outside the campaign's §7 integration list: **0**.

### 7.7 §2.1 containment constraints — verified explicitly, one by one

1. **Live queue not reprioritised.** `OPEN OBLIGATIONS` §5 is byte-identical to its pre-campaign text; verified by reading it back after integration. **N-00 is still item 2 and still the first computational action.**
2. **No simulation row displaced or rewritten.** N-16, N-17, N-18, N-18a and N-18b retain their scope, labels and order. Exactly **one** evaluation row was added, N-19, placed after N-18b, labelled a diagnostic that "cannot establish or refute LO-1–LO-5", and not promoted above any existing row.
3. **Application map not narrowed.** APP-FIN, APP-NEURO, APP-SENSOR/GENE and APP-FRAME keep their standing. Exactly one row was added to the §0A preflight — an evaluation declaration. **No application changed from viable to non-viable**, and none is implied to have.
4. **Paper 1's contribution not restated.** The stated contribution remains the moving-centre estimator, the identified subspace and the rate theorems; the addition is one displayed scope limit that says so explicitly.
5. **No vocabulary colonisation.** Only the seven files in the integration list were touched. The impulse to add an evaluation caveat to the geometry and estimation boundary files was recorded and not acted on: **BW-FIXED-MARGIN, BW-SHRINKING-MARGIN, HE, FRAME-2P-U, HD1, P1-ID and G1 are untouched.**
6. **Proportionality budget** recorded before integration and respected — §7.0.

### 7.8 Closure statement

LO-1 through LO-7 are terminal; E1–E5 are individually terminal; HYG is integrated; the transitive closure of all 107 nodes is terminal. LO-6 shows by edge audit that **no closed P1-ID, HD1, HE, BW-FIXED-MARGIN, BW-SHRINKING-MARGIN or FRAME-2P-U node is disturbed**, and the single real edge — a \(\Theta(m/M)\) proxy contribution to the existing (P1-OP-zeta) target-defect budget — is displayed rather than absorbed silently. One vocabulary is used throughout for target, proxy, loss and forecast class, and the estimation/evaluation distinction is never conflated; the one place where the first draft did conflate consistency with conditional unbiasedness was caught by the audit and corrected (O-13). Every claim about another author's paper is verified verbatim or withdrawn: one paper is quoted with equation and section numbers and is explicitly described as *silent*, not wrong; Savage (1971) is withdrawn for want of verification; five candidate papers were screened and rejected. Every restriction carries a proved boundary reason, including the two the audit forced into the open (E3's "no auxiliary knowledge of the within-window volatility path", and A-4.3's affine-parametrisation clause).

**The limitation this campaign will not paper over:** because the Wave-1 agents were killed before writing anything, the mathematics was authored by one party and audited by two others. Every load-bearing computation has been derived twice by parties that did not share scripts, and the two derivations agree — but this is not the same as three independent workstreams reaching the results separately, and it is recorded as such in §6.
