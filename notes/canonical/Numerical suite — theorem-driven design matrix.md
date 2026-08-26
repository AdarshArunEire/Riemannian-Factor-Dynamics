---
title: Numerical suite — theorem-driven design matrix
type: numerical-design
status: active
authority: canonical-design-only
updated: 2026-08-25
---

# Numerical suite — theorem-driven design matrix

## 1. Scope and status

The AIRM Paper 1 stack is now empirically complete through centre calibration,
bounded-energy recovery, the fixed-rank selector diagnostic, the eleven-cell control matrix,
the drift-orientation phase grid, and the low-sample amplitude attribution.
The recorded controls contain 1,536 paired rows with no recorded error; the
amplitude attribution adds 192 clean paired draws. They establish a strong
synthetic loading/reconstruction result and localize low-$n$ factor-score loss
to the feasible-row bundle, not to loading-direction estimation. They do not
constitute forecasting evidence. The compact fixed-size BW closure in §3E is
now complete with a qualified fixed-rank pass: 496 frozen tasks, no ordinary
error or failed verdict, safe-domain rate evidence, and honest hostile-boundary
behaviour. Rank-positive synthetic cells use the known true rank, so no
automatic-rank claim is made. The literal parent comparison on common BW draws
is now complete. The non-forecasting APP-FIN identification illustration and
its centre-detectability gate are also complete with a qualified boundary:
suggestive regularised centre motion, no 5% rejection of a dependent
constant-centre null, and severe full-Richardson variance at monthly
\(n=240\). Predictive rank, score dynamics, finite-sample centre redesign, and
forecasting move together to the application follow-up. The
repository also contains audited SPD geometry and loss
primitives, a rebuilt realised-covariance panel, an APP-FIN parent-pipeline
reproduction whose Python/R harness agrees to roundoff and whose published
model rankings are preserved, and [[notation-map|the full parent-to-project
notation map]]. N-00 remains partial only because the long parent simulations
are unfinished; that unattended reproduction is no longer on the critical
path. No numerical result proves an analytical theorem.

The primary targets are:

0. how a forecast is **scored** — the loss/target/proxy declaration required by [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]] §8, which is a reporting scope condition and not an estimation target;
1. centre, frame, and feasible tangent reconstruction error;
2. lag-row error \(d_n\), assembly error \(\eta_n=2A_{2,n}d_n+d_n^2\), loading error, and null eigenvalues;
3. factor-number threshold and ridged-ratio behaviour;
4. domain, spectral-margin, and generated-object failures;
5. forecasting only as a separate downstream experiment after reconstruction has been evaluated.

The parent APP-FIN reproduction is the implementation seed for N-16/N-17 and the finance benchmark, not a substitute for them. Reusable centre, BW, lag-operator, factor, forecasting, and data-pipeline code should be adapted only after its conventions and targets are matched to the canonical notation. FRAME's three-colour split, fitted-polygon derivative, nuisance/influence decomposition, and common-gauge tests are new work.

Analytical predictions in this suite are governed by [[HE — canonical growing-energy theorem boundary]], [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]], [[BW-SHRINKING-MARGIN — canonical restricted theorem boundary]], and [[FRAME-2P-U — conditional two-path debiasing theorem]].

[[P1-ID — centre-drift and factor identification boundary]] governs the interpretation of drift/factor sensitivity experiments. Archived campaign files are proof provenance, not alternative simulation specifications.

## 2. Common experimental axes

| Axis | Planned values |
|---|---|
| sample size | logarithmic grid in \(n\), with at least four asymptotic scales |
| smoother bandwidth | theorem choice and controlled under/over-smoothing around \(b_n=n^{-(1-2\rho)/7}\) |
| energy | bounded \(R_n\), \(R_n=n^\rho\), and pervasive \(R_n\asymp\sqrt{p_n}\) |
| ambient size | Hilbert truncation \(p_n\); SPD matrix size \(m_n\); record \(p=m(m+1)/2\) separately |
| factor rank | fixed \(r\), growing \(r_n\), and zero-signal \(r=0\) |
| lag structure | included lags \(h_0\), finite-memory length, weak long-tail contamination |
| dependence | independent, finite-memory, causal physical dependence, overlap-induced covariance dependence |
| geometry margin | fixed tube; shrinking lower eigenvalue \(\alpha_n\); generated Richardson/blend margin |
| signal | actual \(A_{2,n}\) and \(\Delta_n\), including fixed, pervasive, diluted, and vanishing gaps |
| contamination | target defect \(\zeta_n\), moving axes, coloured idiosyncratic lag, preliminary covariance error |

All rate plots use the actual empirical \(R_n,A_{2,n},\Delta_n\) and the theorem ledger. Dimension is never substituted for total energy without verifying the DGP.

## 3. Planned analytical stress matrix

| ID | Regime and DGP | Parameter sweep | Predicted analytical behaviour | Failure boundary or diagnostic | Status |
|---|---|---|---|---|---|
| N-00 | parent-paper reproduction baseline | run the public BW/sphere simulations and S&P 500 reproduction scripts under a frozen environment | recover the parent estimator, raw-ratio behaviour, reconstruction/forecast pipeline, and reported benchmark definitions before adding project corrections | version drift, unavailable Yahoo data, or target/convention mismatch must be logged rather than silently repaired | **PARTIAL — APP-FIN PIPELINE AND NOTATION MAP COMPLETE; PARENT SIMULATIONS AND PREDECLARED FACTOR-COUNT/LOSS LOOP OUTSTANDING** |
| N-LS-A / B4.2 | three-scale centre and local-stationarity calibration | AIRM \(m=3\); \(n=256,\ldots,8192\); 64 replicates; bandwidth multipliers \(0.7,1.0,1.3\); bias-only, variance-only, full, and coherent \(n^{-a}\) discrepancy controls | corrected full path error follows the \(n^{-3/7}\) ceiling; injected \(n^{-a}\) discrepancy transfers through the predicted two-term competition; Richardson removes smoothing bias but amplifies stochastic variance | safe fixed-band design only; zero fallback here does not test cone-boundary failure; bandwidth optimum is not bracketed because \(1.3\) wins at the tested edge | **COMPLETED — CENTRE LAYER ACCEPTED; FACTOR RANK FIXED AT ZERO** |
| N-01 | bounded-energy HD1 baseline | fixed \(R,h_0,r,\Delta>0\); increasing \(n,p\) | \(d_n=O_p(n^{-1/2}+\ell_n)\); loading \(O_p(d_n/\Delta)\); null eigenvalues \(O_p(d_n^2)\) | generated-tube or dependence violation | **QUALIFIED PASS — §3C; SAME-DRAW COMPARATORS COMPLETE** |
| N-P1-CONTROL | Paper 1 scientific control and drift-orientation matrix | eleven core AIRM cells over \(n=512,2048,8192\), plus 15 paired orientation/drift cells at \(n=8192\) | fixed-centre and rank-zero placebos do not gain; moving mixed/orthogonal and curved cells recover the declared span and improve reconstruction; aligned drift preserves the fixed span | conclusions are conditional on one small-matrix bounded-energy DGP and are not forecasts | **COMPLETED — 1,536/1,536 ROWS, ZERO RECORDED ERRORS** |
| N-P1-AMP | low-sample factor-amplitude attribution | oracle/feasible rows crossed with true/feasible directions at \(n=240,512,2048\), 64 paired draws each | distinguishes noisy-oracle floor, feasible-row cost, loading-direction cost, and their interaction before any learned correction | nonlinear NRMSE contrasts are descriptive; the row bundle is not yet split into centre/Log/polygon/frame subchannels | **COMPLETED — FEASIBLE-ROW COST DOMINATES; LOADING COST IS NUMERICALLY ZERO** |
| N-02 | HE flat/rigid frame | \(\rho\) below, at, and above \(3/13\); \(b_n=n^{-(1-2\rho)/7}\) | leading balanced rate \(n^{-(3-13\rho)/7}\), plus \(n^{-(a-\rho)}\) | consistency transition at \(\rho=3/13\); balanced headline also needs \(a\ge(3-6\rho)/7\) | **PLANNED** |
| N-03 | HE generic curved moving frame | \(\rho\) below, at, and above \(3/20\) | rate \(n^{-(3-20\rho)/7}+n^{-(a-2\rho)}\) | frame-energy multiplier causes the \(3/20\) boundary | **PLANNED** |
| N-04 | pervasive rescue | \(Y_{t,n}=\sqrt{p_n}a_ng_t+\epsilon_{t,n}\) with centred bounded one-dependent components | \(R_n\asymp\sqrt p\), \(A_{2,n}\asymp p\), \(\Delta_n\asymp p^2\); relative loading error behaves as \(d_n/p\) | replace white idiosyncratic lag by proportional coloured lag to force target contamination | **PLANNED** |
| N-05 | localised high-dimensional background | fixed signal gap with \(R_n^2\asymp p_n\) | spurious lag row of order \(p_n/\sqrt n\) can destroy fixed-gap consistency | directly contrasts N-04; energy growth alone is not rescued | **PLANNED** |
| N-06 | normalisation preserved versus diluted | compare raw \(Y\) and \(Y/\sqrt p\) for pervasive and localised signals | recompute \(A_2,\Delta,d\); pervasive direction can remain stable while localised gap collapses | report estimand change and \(\eta/\Delta\), not nominal scale | **PLANNED** |
| N-07 | growing factor rank | equal-energy factors and fixed total lag energy | verify \(\Delta_n\le h_0F_n^4/r_n\) and predicted selector degradation | increasing \(r_n\) forces gap dilution | **PLANNED** |
| N-RANK | fixed-rank selector diagnostic | \(n\in\{512,2048,8192\}\); AIRM sizes \(m\in\{2,3,4,6,8\}\) oracle and \(m\in\{3,4\}\) feasible; ranks up to 10 subject to tangent dimension; equal, decaying, and weak-tail AR(1) profiles with fixed total factor scale | oracle/feasible parity on common cells; selector success controlled by \(\chi_j=s_j^4\sum_h\rho_j^{2h}\), not by AR(1) as a required model class | fixed rank within each time series; feasible branch omits decaying profile and does not record general-rank projector/factor errors; does not close N-07 | **COMPLETED DIAGNOSTIC — SEE §3B** |
| N-08 | zero signal and zero noise | \(\Delta=0\); then noise-free observations with estimated centre/frame | no positive-r loading theorem when \(\Delta=0\); mean/frame errors persist without observation noise | separate null-row selector window for \(r=0\) | **PLANNED** |
| N-09 | fixed-size BW robust-rate closure | fixed \(m\), compact full-rank compatible domain, bounded tangent energy, short memory, exact lag target and fixed gap; instrument every primitive in §3E | \(r_{\mu,n},q_{R,n},d_n,\eta_n\), and loading error follow the robust \(n^{-3/7}\) ceiling; beyond-rank eigenvalues follow \(n^{-6/7}\) | every spectral/polar/Exp/normal/path/generated slack, energy, dependence, target defect and gap condition is reported separately | **COMPLETE — QUALIFIED FIXED-RANK PASS; SEE §3E** |
| N-10 | BW fractional-normal shrinking margin | \(\alpha_n\asymp m_n^{-A}\), \(m_n=n^x\), with \(x\) below, at, and above \(3/(5A)\) | local coefficients inflate at their proved powers; the conservative matched rank-one branch is consistent for \(x<3/(5A)\) | separate failure of normal-pair support, generated-domain reach, frame/loading balance, and actual gap; the boundary is sufficient, not minimax | **POST–PAPER 1; ONLY A FINITE-SIZE LOWER-EIGENVALUE HOSTILE CELL IS CONSUMED BY §3E** |
| N-11 | rank-changing BW attack | orthogonal rank-one PSD endpoints and regularised approaches to them | nonunique alignments/geodesics/means at the boundary | numerical solver dependence is a symptom, not a repaired estimand | **PAPER 1 HOSTILE BOUNDARY CELL; NOT A RATE CELL** |
| N-12 | signed Richardson root collapse | positive diagonal roots whose signed extrapolation reaches zero | raw correction exits the domain; admissibility test activates fallback | compare raw, tested, and clipped reconstruction while retaining target labels | **PAPER 1 HOSTILE FALLBACK CELL; NOT A RATE CELL** |
| N-13 | fixed-basis diagonal HE–BW | positive root process, \(b=n^{-1/7}\), growing \(m\) | nonempty sufficient window \(m=o(n^{6/7}/\log n)\) under the dossier conditions; frame is rigid | coordinatewise root margin and maximum-error event, not only \(\ell^2\) error | **PLANNED** |
| N-14 | moving eigenvectors | fixed eigenvalues with rotating eigenbasis | diagonal/root reduction fails despite stable spectra | quantify off-basis defect and compare with approximate-match penalty | **PLANNED** |
| N-15 | noncommuting fixed-margin growing-size BW | fixed compatible spectral/polar/Exp/normal/path margins, growing \(m\) | the proved geometric producer has no direct matrix-size factor; statistical error follows the separately supplied energy, dependence, row, and gap budgets | detect hidden implementation dimension costs, generated-domain escape, energy growth, or gap dilution rather than attributing every failure to geometry | **POST–PAPER 1; FIXED-SIZE N-09 COMPLETED** |
| N-16 | FRAME-2P-U curved oracle branch | three exactly separated colours; \(b=n^{-1/7}\), \(M\asymp n^{2/7}\), \(c=n^{-\gamma}\); sweep \(\gamma\) below, inside, and above \((1/6,3/14)\) | inside the window the corrected row is root-\(n\), its post-influence nuisance remainder is sub-root-\(n\), and null eigenvalues are \(O_p(n^{-1})\) when U2P and the actual gap hold | separate validation influence from nuisance remainder; record U2P/tube/mask failures rather than treating bounded energy as sufficient | **PLANNED** |
| N-17 | FRAME correction negative controls | compare the valid two-path correction with direct \(\Omega\) plug-in, same-band score/Richardson, invariant-only redesign, and the robust uncorrected row | same-band retains a generic curved \(n^{-3/7}\) bias; invariant-only changes the estimand; direct plug-in succeeds only when its extra frame producer is verified | use a noncommuting curved witness and a common-gauge conjugation check | **PLANNED** |
| N-18 | centre-drift/factor identification diagnostic | controlled drift-only, factor-only, aligned, orthogonal, mixed, cross-term, and curved-reference rank-inflation DGPs; then the APP-FIN fixed-centre baseline versus moving-centre fits | verify implementation against ID-4/ID-5 and Corollary P-DRIFT: stable aligned span, clean orthogonal rank addition of exactly \(\dim P_{\mathcal S_X^\perp}D\), partial rotation/cancellation, and exact sphere reference-rank change | validates code and reports sensitivity; it cannot determine empirical component dominance without the canonical identifying assumptions | **PAPER 1 DISCRETE CONTROLS AND APP-FIN CENTRE GATE COMPLETE; EXHAUSTIVE CONTINUOUS PHASE POST-FREEZE** |
| N-18a | ID-8 rank-inflation witnesses | reproduce the three exact analytic constructions as code checks: BW \({\rm SPD}(2)\) with \(x=\operatorname{diag}(a,1)\), \(V\) off-diagonal, \(a\ne1\); AIRM \({\rm SPD}(2)\) noncommuting; \(H^2\); plus the diagonal-BW rigid control | the three curved cases inflate affine dimension \(1\to2\) and the diagonal-BW control does not; the BW defect matches the closed form for every \(a\ne1\), \(0<\vert b\vert<1+a\) | a **code-verification** diagnostic against theorems already proved analytically; agreement confirms the implementation, disagreement indicts the code, and neither outcome can alter ID-8 | **PLANNED** |
| N-18b | ID-7/ID-10 persistence diagnostic | sweep the frozen-factor persistence: short memory, \(\rho_n=1-n^{-\theta}\) for \(\theta\) inside and outside \([0,1)\), and ARFIMA with \(d\in\{0,0.1,0.25,0.4\}\); at each, record \(\psi^+(nb_n)\) against \(b_n^3\) and the realised mean/loading error | the mean error tracks \(\ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1}\); the re-optimised bandwidth \(n^{-(1-2d)/(7-2d)}\) beats \(n^{-1/7}\) for \(d>0\); separation degrades as \(x_n=(1-\rho_n)nb_n\to O(1)\) | measures the **constant and the finite-\(n\) onset**, not the exponent, which is proved. It cannot establish the memory exponent of any real dataset; APP-FIN's \(d\) remains an assumption under test | **PLANNED** |
| N-18c | static-centre breakdown phase diagram | \(\mu_\nu(u)=\operatorname{Exp}_{\mu_0}\{\nu g(u)V\}\); sweep \(\nu,n,\Delta\), noise/energy, persistence, drift shape/speed/orientation, geometry and SPD conditioning; compare fixed- and moving-centre estimators | estimate the complete structural- and forecast-risk advantage sets. In the clean flat/orthogonal/centred branch, the first row defect is \(O(\nu^2)\) and the candidate onset is \(\nu_{\rm est}^\star\asymp(n^{-1/2}+\ell_n)^{1/2}\), hence \(n^{-3/14}\) when short-memory \(\ell_n\) dominates | no universal exponent or unique crossover is presumed: surviving cross/curved terms may be \(O(\nu)\), aligned drift may preserve the loading span, and forecasting depends on horizon and a P1-LOSS-admissible loss | **PLANNED; AFTER N-00 AND THE N-18 POSITIVE/PLACEBO CONTROLS** |

| N-19 | evaluation-loss distortion and recalibration diagnostic | \(m\in\{3,12\}\), \(M\in\{21,78,1638\}\) Wishart-type and non-Wishart proxies; score a known conditional mean and its shrunk versions under squared BW, AIRM, log-Euclidean, Frobenius and multivariate QLIKE | the finite-sample distortion tracks the closed forms of [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]] §3–§4: BW \(|B_{ii}|/\lambda_i=\frac1M[\frac14+\sum_k\lambda_k^2/(\lambda_i+\lambda_k)^2]\), AIRM \((m+1)/(2M)\); the AIRM scalar recalibration \(c=1-\frac{m+1}{2M}\) removes it and a scalar BW recalibration does not; Frobenius and QLIKE show no distortion; the non-Wishart proxy rotates the induced eigenbasis and the Wishart proxy does not | a **diagnostic**, never a proof: it measures the finite-sample size of an already-proved distortion and the effect of recalibration. It cannot establish or refute LO-1–LO-5, and it does not feed any estimation row | **PLANNED** |

### 3A. Completed B4.2/N-LS-A centre calibration

The recorded design is AIRM at matrix size \(m=3\), with a well-conditioned cubic centre path, drift scale \(0.35\), constant-norm iid tangent noise of magnitude \(0.25\), and factor rank \(r=0\). It uses \(n\in\{256,512,1024,2048,4096,8192\}\), 64 replicates, bandwidth \(b=0.5c_b n^{-1/7}\), \(c_b\in\{0.7,1.0,1.3\}\), and polygon cell count of order \(n^{3/7}\). The centre-rate and discrepancy profiles completed all \(3456+2304=5760\) requested result rows with zero run errors, zero nonconverged stages, and zero admissibility fallbacks. The minimum estimated eigenvalue was \(0.398\); the largest observed condition number was \(5.38\). These health numbers establish safe operation on this interior design only.

The corrected full path-RMS exponents are \(0.413\) at \(c_b=1.0\) (95% bootstrap interval \(0.401\)–\(0.435\)) and \(0.429\) at \(c_b=1.3\) (\(0.407\)–\(0.448\)), against the theoretical \(3/7=0.429\). The injected discrepancy exponents

\[
a=(0.2,2/7,1/3,3/7,1/2,\infty)
\]

produce fitted corrected-error exponents

\[
(0.243,0.362,0.406,0.433,0.435,0.442).
\]

The curve therefore rises with \(a\) and saturates near the estimator's \(3/7\) ceiling. Values above the asymptotic \(\min(a,3/7)\) line at small \(a\) are finite-sample mixtures of the discrepancy and estimator terms, not evidence of a new exponent.

Richardson's finite-sample verdict is deliberately conditional. At \(n=8192,c_b=1.0\), its median error reduction relative to the ordinary broad local mean is \(99.2\%\) in the bias-only control and \(9.4\%\) in the full DGP, while the variance-only corrected error is \(4.37\times\) the ordinary error. In the full DGP it remains \(14.3\%\) harmful at \(n=4096\) and becomes beneficial only at \(n=8192\). This directly exhibits the analytical comparison

\[
\text{bias removed}>\text{variance inflation}
\]

as the condition for practical gain. Multiplier \(1.3\) is best in every tested cell; hence the rate verdict is accepted, but the finite-sample bandwidth constant is not bracketed and must be tuned on validation data rather than promoted from this grid.

The noiseless example shows the residual polygon-chord structure clearly: at \(n=8192\), median midpoint error is about \(33\times\) median vertex error. In the variance-only and full examples the midpoint/vertex ratios are \(0.80\) and \(0.69\), respectively, because interpolation smooths some noise. The polygon term is visible in the clean control but is analytically lower order than the \(n^{-3/7}\) statistical term.

The original bandwidth grid ended with multiplier \(1.3\) best in every cell. B4.2-BWCONST is therefore predeclared as a finite-sample follow-up: tune \(c_b\in\{1.3,1.5,1.7,1.9,2.1\}\) on independent full-DGP draws at \(n=4096,8192\), freeze the mean-log-median winner, then compare it with \(c_b=1.0\) on fresh paired draws. A winner at \(2.1\) is a constrained boundary winner because the fixed-overlap construction prevents a silent extension at \(n=4096\). This can improve finite-sample error and the correction crossover; it cannot change the rate verdict above.

Sources: results/intermediate/centre_rate/, results/intermediate/local_stationarity_discrepancy/, and the independently runnable notebook experiment_plot_lab.ipynb. This experiment contains no factors and makes no claim about lag rows, loading recovery, rank selection, reconstruction, or forecasting; those begin at N-01.

**Plot-language lock from this adjudication.** Show ordinary comparisons as direct signed percentages (positive means improvement) or as “× baseline” multipliers. Use logarithmic axes only for rate slopes or genuine orders of magnitude, and label them explicitly in those terms. Sequential magnitude plots use viridis; gain/harm plots use a zero-centred diverging scale. Tables retain exact values even when the figure uses reader-facing percentages or multipliers.

### 3B. Completed N-RANK fixed-rank selector diagnostic

The oracle screen completed 15,936 DGP tasks and 111,552 selector rows; the
full feasible moving-centre RFD screen completed 1,056 fits and 7,392 selector
rows. Both recorded zero run errors. Every time series had one constant rank;
rank varied only across independent DGP cells. Factor scales were normalised
within each cell so increasing rank did not silently leave the bounded-total-
energy regime.

On equal-strength common cells, oracle versus feasible threshold accuracy was
78.4% versus 79.4% at \(n=512\), 92.0% versus 92.5% at \(n=2048\), and 100%
versus 100% at \(n=8192\). The raw ratio was 100% on those deliberately clean
cells. Thus centre estimation, polygon construction and transport caused no
detectable extra rank-selection boundary in this DGP. That is a modularity
result, not evidence that the geometry layer is costless in every regime.

The weak-tail cells isolate the actual failure. At \(n=8192\), both threshold
pipelines missed the final factor with amplitude multiplier \(0.2\) for every
\(r\ge2\); the feasible raw ratio missed it in 97.7% of those cells. The
threshold selected zero in every null cell, while ratio rules cannot represent
rank zero. This matches the internal calibration

\[
\chi_j=s_j^4\sum_h\rho_j^{2h},
\qquad
d_n^2<\tau_n<\chi_{\min,n}-\eta_n:
\]

amplitude enters to the fourth power, so the weak-tail signal is only
\(0.2^4=0.0016\) of an otherwise comparable factor before persistence is
accounted for. The selector is not hard-coded to rank two; the screen varies
rank from zero up to ten subject to the available tangent dimension.

Two gaps are deliberately left visible. The full feasible profile did not run
the oracle screen's gradually decaying signal, and the harness harvested
spectra and selector decisions rather than general-rank loading-projector and
factor-score errors. They define the deferred implementation experiment
**N-RANK-CLOSE**:

1. add the decaying profile to feasible RFD at \(n\in\{512,2048,8192\}\) on
   the already-supported \(m\in\{3,4\}\) cells;
2. record loading-projector error, factor-score/reconstruction error after an
   explicit rotation convention, \(\chi_{\min}\), \(d_n^2\), \(\eta_n\), and
   the selected rank;
3. use the threshold selector as primary, raw ratio as the parent comparator,
   and ridged ratio only as a documented tuning diagnostic;
4. stop if feasible errors track the oracle/signal boundary; expand selector
   research only if a reproducible feasible–oracle gap appears.

N-RANK-CLOSE is not a Paper 1 gate. The completed diagnostic and proved
threshold theorem are sufficient for the foundational paper; selector tuning,
general-rank implementation efficiency, minimax weak-factor theory, adaptive
time-varying population-rank inference, and N-07's growing-rank asymptotics are
later work. Synthetic loading/reconstruction headlines use known DGP rank.
Paper 1 APP-FIN uses fixed \(r=2\) and labels other ranks as sensitivity only.
Causal predictive-rank selection among nested fits is governed by
[[Future application programme — factor scores, predictive rank, and online RFD]].
Analytical calibration: [[P1-RANK — AR1 signal strength and threshold boundary]].
Literature positioning: [[P1-RANK — weak dynamic factors and lag-rank literature audit]].

### 3C. Completed B4.5/N-01 bounded-energy adjudication

Namespaces 4501 and 4502 supply 480 paired DGP draws and 960 result rows over
\(n=512,\ldots,8192\) and AIRM SPD sizes \(m=2,3,4\). All rows completed with
zero recorded errors, admissibility fallbacks, or nonconverged local means.
The production fit uses the predeclared clipped bandwidth schedule; fixed
\(c_b=1.3\) is retained on each identical draw as a paired reference.

The result is a **qualified numerical pass**. Production median exponents are
0.44--0.48 for the centre, 0.80--1.08 for the lag row, 0.89--1.23 for the
squared lag operator, 0.60--0.67 for the loading projector, and 1.06--1.13 for
the first beyond-rank eigenvalue. Every production draw satisfies
\(\widehat\lambda_{r+1}\le d_n^2\), and the threshold selector returns the
declared rank two on every draw. At \(n=8192\), median projector error is
0.010--0.016, equivalent to a largest principal angle of 0.59--0.91 degrees.
This is error against the generated DGP loading span: the noiseless factor lag
row has a positive rank-two gap and exactly the generated loading projector on
these draws. Factor-score NRMSE remains 30--44%, so accurate subspace recovery
must not be rewritten as equally accurate per-time score recovery.

The qualification is the theorem's finite-sample separation event. At
\(n=8192\), only 47--69% of draws (depending on \(m\)) have actual lag-operator
error below the oracle eigengap. The frequency rises and the median assembly-
bound/eigengap multiplier falls toward one with \(n\), but the grid has not
entered that sufficient regime uniformly. The experiment therefore supports
the predicted mechanism and useful recovery; it does not prove the analytical
rate or license a universal finite-\(n\) guarantee.

The production bandwidth improves the paired centre by a median 17%, lag row
42%, operator 47%, loading projector 9%, and factor scores 10% relative to
\(c_b=1.3\). Observation and latent-signal reconstruction improve by less than
1%, exposing their per-observation score/noise floor. The full audit, exact
tables, and reader-facing figures are in `results/final/b45_adjudication/`.

The same-draw comparator replay is complete: all 480 tasks finished without a
recorded error or global-mean nonconvergence. At $n=8192$, the true-centre noisy,
full-RFD, and one-centre loading angles are respectively 0.47/0.59/7.48 degrees
for $m=2$, 0.70/0.66/17.26 degrees for $m=3$, and 0.93/0.91/17.28 degrees for
$m=4$. Thus feasible RFD is already at the known-centre loading floor while
the fixed-centre representation retains a large misspecification angle. On
the paired draws, RFD reduces loading error by a median 93--96% and wins every
$n=8192$ replicate; it reduces observation reconstruction error by 10--21%
and wins 94--100%. Factor-score recovery is deliberately less flattering:
RFD pays a large centre-estimation cost at small $n$, approaches the nonzero
known-centre noise floor, and only at large $n$ overtakes the one-centre fit;
at $n=8192$ its median factor-NRMSE reduction is 6--13%, with 69--94% wins.

This is strong enough for a Paper 1 positive-control figure because it is
paired, truth-referenced, and includes a known-centre ceiling. It is not a
general application result: the DGP has one cubic drift path, rank two, AR(1)
factors, white constant-norm tangent noise, and small AIRM matrices. The
fixed-centre placebo and wider control matrix remain necessary, and literal
parent-code comparison belongs on the BW cells.

The wider control run is complete. All 1,056 core and 480 phase rows finished
without a recorded error, fallback, or nonconverged stage. At $n=8192$ the
threshold selector is correct in every core regime and loading angles are
below $1$ degree except for the deliberately lag-coloured violation
($1.46$ degrees). On the smooth moving-centre B0 control, RFD reduces loading
projector error by a paired median $95.5\%$ and observation reconstruction
error by $21.4\%$. On the fixed-centre C0 placebo it changes reconstruction by
$-0.1\%$ and does not improve loading recovery. Aligned drift remains a
near-tie or loss, while mixed and orthogonal gains grow with drift magnitude;
the noncommuting curved cell remains numerically healthy. These results close
the predeclared AIRM scientific-control gate but remain conditional synthetic
evidence. The authoritative artifacts are
`results/final/paper1_control_matrix/`.

The 192-draw amplitude attribution is also complete. At
$n=240,512,2048$, replacing oracle rows by feasible centre/frame rows while
retaining true loading directions adds median NRMSE $0.683,0.465,0.204$.
Replacing true directions by RFD-estimated directions on oracle rows adds
approximately zero, and the interaction is negligible. The complete RFD
score norms are inflated, not uniformly damped; one best scalar improves but
does not repair the trajectories. This localizes the low-sample bottleneck to
the feasible-row bundle without deciding whether centre estimation, Log
recentering, polygon interpolation, or frame transport dominates inside that
bundle. The authoritative artifacts are
`results/final/amplitude_diagnostic/`.

### 3D. N-18c protocol — estimate a phase boundary, do not assume one

For each declared target \(T\), compute

\[
\widehat{\mathcal D}_T(\nu)
=\widehat R_T(\widehat T^{\rm mov};\nu)
-\widehat R_T(\widehat T^{\rm stat};\nu)
\]

on common Monte Carlo draws. Report the full curve with uncertainty. Define a first crossover only if the negative set is nonempty, and call it a breakdown threshold only if the observed/theoretically justified advantage set is an upper interval. Multiple crossings and no crossing are valid outcomes.

The minimum design contains:

- the exact placebo \(\nu=0\);
- a positive-control range large enough that the moving-centre estimator should resolve drift;
- clean flat aligned, orthogonal and partial orientations;
- a cross-term design with an \(O(\nu)\) defect;
- noncommuting AIRM/BW and a curved rank-inflation control;
- sample-size and persistence sweeps, using \(\psi^+(nb_n)\) rather than silently retaining short-memory \((nb_n)^{-1/2}\);
- structural outputs: centre error, row defect, loading subspace, within-span eigenordering, selected rank and actual gap;
- forecast outputs at each declared horizon, scored primarily by squared Frobenius and multivariate QLIKE; any geodesic score carries its induced target and P1-LOSS recalibration;
- intrinsic motion \(\mathcal L_{\mu_\nu}\) and \(\mathcal V_{\mu_\nu}^2\) alongside the design coordinate \(\nu\).

Keep factor strength fixed when sweeping \(\nu\), then repeat over \(\Delta\), observation/noise energy, factor persistence, drift shape/speed, orientation, geometry and spectral conditioning. This experiment measures when dynamic centring is worth its estimation cost. It does not prove that a real centre moves, identify empirical component dominance, or prove the clean-case \(n^{-3/14}\) exponent.

### 3E. Paper 1 compact BW closure — every robust-rate input stays visible

**Recorded status (2026-08-25): COMPLETE — QUALIFIED FIXED-RANK PASS.** The
immutable workload is `config/bw_closure.yaml`, the append-only harness is
`experiments/run_bw_closure.py`, and the one-line runner is
`sandbox/run_bw_closure.ps1`. The 189-test BW/centre/frame/lag preflight and
the nine-cell safe/hostile smoke matrix pass. The frozen 496-task profile then
completed with 496 unique rows, zero duplicates, zero ordinary errors, and zero
failed or unknown verdicts.

The two rate spines support the robust chain without being treated as proof.
For commuting and noncommuting paths respectively, fitted exponents were
\(0.41,0.42\) for centre error, \(0.58,0.58\) for polygon error,
\(0.68,0.75\) for lag-row error, and \(0.55,0.57\) for loading error. These are
compatible with the \(3/7\) centre/loading ceiling and \(4/7\) polygon design.
At \(n=8192\), median loading-projector errors were \(0.0105\)–\(0.0191\)
across the regular scientific cells. All rank-positive recovery summaries use
the DGP's **known true rank**; selector outputs remain diagnostics in the raw
file and support no Paper 1 automatic-rank claim.

All 400 safe fit rows passed the generated-domain checks with zero fallback or
nonconvergence. Operator assembly and the beyond-rank null bound held in every
fit row. The deliberately conservative finite-sample condition “operator error
below oracle eigengap” was not uniform, however: median assembly/gap ratios at
\(n=8192\) remained about \(1.45\)–\(1.82\). Thus the strong empirical loading
recovery is reported alongside, not as a replacement for, this sufficient-gap
qualification. Every hostile probe behaved as declared: signed exit fell back,
rank loss and incompatible Exp input rejected, near-identical matrices stayed
finite/nonnegative, dispersion barycentres converged, and all 16 lower-margin
fits exposed that they lay outside the fixed-margin theorem. The final
adjudication is `results/final/bw_closure_adjudication/report.md`.

Paper 1 consumes only the **fixed-size, full-rank, safeguarded** statistical
theorem in [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]] §5. It does not consume the full growing-size experiment N-15 or
the restricted shrinking-margin phase diagram N-10. A finite fixed-size
lower-eigenvalue stress is retained as a boundary diagnostic, not presented as
evidence for the shrinking-margin theorem.

On the safe short-memory exact-target spine,

\[
\ell_n\asymp n^{-3/7},\qquad
d_n=O_p(n^{-3/7}),\qquad
\eta_n=2A_{2,n}d_n+d_n^2,
\]

so bounded $A_{2,n}$ and a fixed eigengap give an $n^{-3/7}$ loading ceiling,
while the first beyond-rank eigenvalue has the $n^{-6/7}$ square ceiling. The
experiment reports finite-grid slopes and scaled errors; it cannot prove these
orders. The rate spine uses a commuting diagonal BW-flat path and a genuinely
noncommuting curved path at fixed $m=3$, with
$n\in\{512,1024,2048,4096,8192\}$ and common paired draws. Other scientific
and hostile cells may use the smaller diagnostic grid
$n\in\{512,2048,8192\}$; the immutable configuration fixes replicate counts
before results are viewed.

The rate spine retains the fixed theorem-track bandwidth
$b_n=0.5(1.3)n^{-1/7}$. The already frozen bounded production rule may appear
on the same draws as a labelled finite-sample comparator, but it does not
generate the BW slope claim. No BW bandwidth constant is selected from the
recorded rate or APP-FIN outcomes.

Each theorem input below receives its own output column, summary row, and
pass/boundary verdict even when several are measured on the same draw.

| ID | Theorem input or conclusion | What is recorded directly | Independent control |
|---|---|---|---|
| BW-R0 | full-rank spectral band | minimum and maximum eigenvalue over observations, every positive stage mean, centre vertices and reconstructions | safe interior; one-at-a-time lower-eigenvalue approach; rank-deficient rejection |
| BW-R1 | polar cross-Gram margin | minimum singular value of every alignment cross-Gram consumed by Log, transport, connectors and polygon cells | noncommuting path with increasing dispersion while spectra remain fixed-conditioned |
| BW-R2 | Exp-factor margin | minimum singular value of every generated BW Exp factor | increase tangent/centre amplitude holding the base spectrum fixed |
| BW-R3 | positive-Hessian/normal radius | minimum sampled observation-Hessian eigenvalue and maximum score-pair radius ratio | safe scores versus a radius-approach cell; multiplicity is not treated as a failure |
| BW-R4 | path and cell domain | maximum canonical path length, cell length, endpoint speed/acceleration and ruled-cell diagnostic | commuting path versus curved noncommuting path, then long-path stress |
| BW-R5 | signed/generated-set slack | minimum eigenvalue or typed singular slack of all Richardson/blend outputs, chords, connectors, ruled objects and reconstructions | engineered signed Richardson exit; tested fallback must activate without clipping |
| BW-S0 | bounded total tangent energy | empirical supremum and RMS BW score energy, separately from spectral conditioning | fixed energy versus increased dispersion/energy at fixed condition number |
| BW-S1 | smoothing/localisation design | actual bandwidth, kernel support, signed weights, effective sample size at every positive stage, polygon count, generated-object count and grid/supremum event | fixed $c_b=1.3$ rate track; frozen production rule only as a paired finite-sample comparator |
| BW-S2 | local law and cubic centre bias | truth-referenced centre RMS, grid supremum, bias-only and noise-only components, path speed/acceleration and declared $n^{-a}$ coupling with $a\ge3/7$ on the rate spine | smooth interior path versus rough/local-stationarity violation |
| BW-S3 | polygon/frame and feasible observation | oracle-frame error, polygon/chord error, connector residual and feasible tangent RMS $q_{R,n}$ | commuting rigid frame versus noncommuting curvature |
| BW-S4 | short-memory Hilbert/HS dependence | declared DGP memory plus empirical oracle score/product lag envelope | iid/finite-memory pass versus lag-coloured-noise violation |
| BW-S5 | included-lag target factorisation | oracle lag-row defect $\zeta_n$ against the declared clean factor target | exact factorisation versus factor-noise cross-lag or coloured-noise contamination |
| BW-S6 | lag count and masks | actual included lags, row counts, normalization, missing/mask and discretisation defects | common-lag clean design; no silent variable-tail substitution |
| BW-S7 | signal and assembly | $A_{2,n}$, actual $\Delta_n$, $d_n$, $\eta_n$, $\eta_n/\Delta_n$ and empirical operator error | fixed gap, weak/diluted gap, and rank-zero selector null |
| BW-C0 | robust-rate outputs | rates for centre, frame, $q_R$, $d_n$, $\eta_n$, loading projector and first null eigenvalue | diagonal-flat and noncommuting safe-interior rate spines |
| BW-C1 | selector diagnostics | threshold window $d_n^2<\tau_n<\Delta_n-\eta_n$, ridged-ratio side conditions and selected rank | diagnostic only in this closure run; rank-positive scientific recovery uses known true rank and no automatic-rank conclusion is drawn |
| BW-H0 | numerical honesty | finite-value guards, convergence, fallback reason, fallback count and complete object that failed membership | near-identical matrices, NaN regression, signed exit, compatibility-margin stress and rank loss |

The scientific matrix contains fixed centre plus factors, moving centre plus no
factors, aligned/mixed/orthogonal drift, one commuting diagonal path, and one
noncommuting curved path. The hostile matrix contains the one-at-a-time lower
spectral margin, signed Richardson exit, near-identical matrices,
rank-deficient input, compatibility-margin stress, and fixed-conditioning
increasing-dispersion cells. Hostile success means a declared rejection or
fallback at the correct boundary; attractive estimation error is not required.

Derived differential bounds in [[BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary]] §3 are already proved and are not re-promoted
to statistical assumptions. Numerical derivative identities remain ordinary
unit/regression tests. Nguyen--Uribe's optional a-priori signed-barycentre
condition may supplement BW-R5 if it is verified, but the robust rate already
survives through the complete runtime generated-membership test and
deterministic fallback; that literature item is not a Paper 1 gate.

For synthetic draws, S0--S7 are known producer checks because the DGP exposes
truth. For APP-FIN they become diagnostics or sensitivity analyses: finite
data cannot prove smoothness, short memory, clean lag factorisation, or a
population eigengap. The paper must state which are imposed conventions and
which are empirically measured.

### 3F. P1-PARENT-SHARED — literal fixed-rank BW parity

The recorded comparison is frozen at \(n\in\{240,512,2048,8192\}\), 24 paired
replicates, and six regular full-rank regimes: the parent-style identity
home field, a conditioned fixed-centre control, aligned/mixed/orthogonal
moving-centre paths, and one noncommuting curved path. Every generated panel
is passed unchanged to complete RFD and the cloned parent `rfm_bws`; both use
the known DGP rank and the same two nonzero lags. The parent arm retains both
its published simulation mean budget and a separately verified deterministic-global-mean
sensitivity.

`P-HOME` matches the parent's fixed identity-centre geometry but deliberately
retains the project's common factor/noise generator so paired component and
orientation controls remain available. It is not described as a byte-for-byte
replay of the parent's `dta_gen_BWS`; the estimator arm itself is literal.

The primary paired outcome is intrinsic RMS reconstruction error against the
latent noiseless signal. Centre-path RMS, loading-projector error,
factor-score NRMSE, observation reconstruction, numerical failures, fallback
counts, timings, paired win rates, and direct error multipliers remain visible.
No selector is run and no in-sample output is called a forecast. The append-only
resumable harness is `experiments/run_parent_rfd_bw_parity.py`; the one-line
tested launcher is `sandbox/run_parent_rfd_bw_parity.ps1`.

The full recorded matrix completed 576/576 rows with zero failures, duplicate
keys, fallbacks, nonconverged RFD stages, or nonfinite primary metrics. Parent
RFM won all 288 home/fixed/aligned paired draws; RFD won all 288
mixed/orthogonal/curved draws. At \(n=8192\), RFD reduced median latent-signal
RMS by 42.5%, 57.8%, and 55.8% in the latter three regimes, whereas its
home/fixed/aligned penalty had shrunk to about 1%. In the aligned cell it
reduced centre-path error by 60.5% but remained 1% worse in reconstruction,
showing that a better centre/factor split need not improve the fitted sum when
drift lies inside the loading space. Empirical RFD centre exponents ranged
from 0.370 to 0.410, near the finite-grid \(3/7\) reference. The verified parent
mean sensitivity was negligible. The adjudication is
`results/final/parent_rfd_bw_parity_adjudication/report.md`; the executed plot
lab is `notebooks/parent_rfd_bw_parity_plot_lab.ipynb`.

### 3G. Post-freeze causal bridge and declared home application

These experiments do not enter Paper 1's theorem or empirical claims. They
begin only after the Paper 1 result/configuration freeze and follow the
authoritative contract in
[[Home application — hourly crypto realised covariance]].

| ID | design | fixed controls | primary outputs | terminal interpretation |
|---|---|---|---|---|
| APP-MONTHLY-VAR | existing 240-month, 12-stock APP-FIN panel; initial months \(1{:}204\), then 36 expanding one-step forecasts | fixed \(r=2\), lag horizon \(h=6\), and the same OLS VAR(1) with intercept, covariance inputs, origins, and losses; parent global centre frozen from the initial window; RFD expanding-prefix path with one-sided terminal-centre carry | squared Frobenius, multivariate QLIKE, labelled parent BW/risk diagnostics, convergence/fallbacks, centre motion, and wall time | **COMPLETE — 36/36 CAUSAL FORECASTS.** Parent/RFD mean Frobenius²: 206.48/241.34; mean QLIKE: 11.12/1717.40. The RFD decoder produced two clips, minimum eigenvalue \(4.16\times10^{-6}\), and 69 centre fallbacks. This is an instability diagnosis, not a dominance or factor-score claim |
| APP-BW-SCORE-FILTER | identical regular BW synthetic draws; \(n\in\{240,512,2048,8192\}\), six fixed/moving/noiseless/noisy controls, 16 replicates; known rank two supplied | oracle, fixed-centre RFM-compatible, and feasible RFD representations each feed a frozen OLS VAR(1) and identity-observation linear Gaussian/Kalman head; first 80% fits, final 20% is revealed sequentially; every BW decode uses the same compatibility guard | observed/filtered score NRMSE, one-step factor forecast NRMSE, KF/VAR ratio, latent-signal and observation reconstruction, clips, eigenvalue/condition margins, convergence and transition radii | **MACHINERY + TWO-DRAW REAL SMOKE COMPLETE; 384-DRAW RECORD PENDING.** The smoke is plumbing evidence only; the recorded run decides whether filtering lowers the projected-noise floor without buying unsafe reconstruction |
| APP-MONTHLY-HEADS | same 204/36 APP-FIN expanding origins and fixed rank as APP-MONTHLY-VAR | literal parent and RFD representations each feed VAR and Kalman heads; the representation is held fixed within each pair; all controls frozen before evaluation | same forecast losses plus head transition radii, inferred measurement fraction, convergence, clips, minimum eigenvalue, condition number, and exact parent-R parity | **MACHINERY + REAL ONE-ORIGIN SMOKE COMPLETE; 36-MONTH RECORD PENDING.** Parent VAR score/forecast parity errors were \(1.83\times10^{-15}\)/\(5.18\times10^{-14}\); both KF fits converged and no arm clipped. One origin cannot establish a forecast verdict |
| APP-HF-0 | 20 predeclared liquid spot crypto assets; official one-second bars synchronized to ten-second returns; non-overlapping hourly realised covariance | one venue/quote; fixed asset, missingness, regularisation, seasonality, and split rules | valid returns per hour, stale/missing fractions, eigenvalue/condition/ridge distributions, proxy-noise diagnostics, and data exclusions | pass fixes the observation process; failure changes or rejects the application before model comparison |
| APP-HF-1 | blocked centre comparison plus dependent fixed-centre null | global, positive-local, Richardson, and predeclared global/local shrinkage; training-only tuning | proxy-robust held-out loss, path stability, effective sample size, correction/fallback events, and null-calibrated motion | global wins: reject RFD on panel; jumps dominate: reject smooth path; regularised local wins: continue with that centre and record Richardson boundary |
| APP-HF-2 | literal parent RFM versus RFD on identical hourly matrices | one validation-chosen fixed rank; identical lags, coordinate conventions, and reconstruction targets | loading stability, reconstruction, lag spectra/gaps, residual dependence, margins, and centre/loading sensitivity | establishes a representation gain, tie, or cost before forecasting |
| APP-HF-3 | projected-score observation model | direct projected scores and parent VAR(1) baseline versus a frozen linear state-space/Kalman treatment | score innovation diagnostics, residual serial structure, reconstruction, and forecast-origin state uncertainty | isolates whether filtering addresses the in-span projected-noise floor |
| APP-HF-4 | sequential one-hour covariance forecasts over a frozen evaluation year | frozen centre, rank, filter, future-centre rule, and refit schedule; causal updates only | Frobenius and QLIKE primary; labelled geodesic and economic diagnostics; LOCF/EWMA, HAR/SPD, covariance-dynamics, factor/state-space, parent RFM, and reproducible geometric comparators | application verdict; no post-test tuning |
| APP-HF-5 | frozen transfer to 20 US equities | explicit market-hours, asynchronous-trading, intraday-seasonality, and overnight policies | same primary losses and health diagnostics | external validation, not a second tuning panel |

The first monthly bridge deliberately uses the parent's forecast model. RFD
changes the centre/frame construction, not the VAR. Its completed instability
diagnosis motivates, but does not prejudge, two frozen follow-ups. The synthetic
score-filter gate first measures hidden-factor amplitude recovery under known
truth. The APP-FIN four-arm replay then changes only VAR versus Kalman within
each fixed representation. Adaptive rank remains absent from both.

## 4. Estimator and selector comparisons

For each eligible regime, plan the following estimators:

- oracle known-centre and oracle-frame lag row;
- robust positive three-scale centre with polygonal frame;
- FRAME-2P-U cyclic training/validation/evaluation correction where the complete U2P package holds;
- split or structural signed mean only where its assumptions hold;
- fixed-size BW localized/regularized estimator with full generated-object admissibility fallback;
- diagonal BW root-coordinate estimator;
- direct covariance dynamics, linear Euclidean factor model, log-Euclidean model, AIRM model, and BW model only when they estimate comparable targets.

Factor-number diagnostics:

- threshold selector with a documented \(d_n^2\ll\tau_n\ll\Delta_n\) window;
- ridged ratio with a documented ridge and nonzero adjacent-spectrum condition;
- raw unregularised ratio as both a parent-baseline comparator and a targeted negative control: favourable finite-sample behaviour is compatible with failure on the known rate-valid over-selection counterexample.

## 5. Covariance construction is a separate experiment

For realised covariance, correlation, connectivity, and diffusion applications, use two distinct layers:

1. a direct-covariance DGP where the matrix series is observed without error, to test the RFM theorem;
2. raw multivariate observations followed by an explicit covariance estimator, to measure sampling noise, asynchronicity or overlap dependence, regularisation bias, rank modification, and target contamination.

The second layer reports an added measurement-error/dependence budget before the matrix series enters AIRM or BW analysis. It must not be folded silently into \(q_{R,n}\).

## 6. Reconstruction and forecasting outputs

Reconstruction outputs:

- centre RMS and grid supremum error;
- frame error and the empirical-energy multiplier;
- feasible tangent RMS \(q_{R,n}\);
- lag-row error \(d_n\), assembly error, loading subspace distance, null eigenvalues, and selected rank;
- domain/fallback/clipping frequency and minimum generated eigenvalue/root coordinate.

Forecasting outputs are separately labelled:

- one-step and multi-step factor-score forecasts;
- covariance or functional reconstruction from forecast scores;
- comparison with direct covariance and linear-factor forecasts;
- calibration and loss appropriate to the stated metric.
- these are post–Paper 1 outputs. APP-FIN forecasting eventually issues every
  candidate before its outcome and distinguishes a causal policy from a
  retrospective oracle, but the foundational paper does not consume that run.
- the first post-freeze bridge instead holds \(r=2\) fixed and matches the
  parent's 204/36 expanding VAR(1) loop. The hourly home initially keeps one
  validation-chosen rank fixed; predictive-rank adaptation enters only later.

No reconstruction theorem is described as a forecasting guarantee.

## 7. Reproducibility contract

- Store every DGP and estimator choice in a versioned immutable configuration.
- Fix and publish seed lists; use independent seeds for train, validation, and test generation.
- Predeclare the sample-size, dimension, energy, bandwidth, gap, dependence, and contamination grids.
- Preserve raw simulation draws, generated covariance series, intermediate centres/frames, and final metrics in separate directories.
- Record software versions, numerical tolerances, convergence/fallback flags, wall time, and hardware/session metadata.
- Use validation only for tuning constants; freeze them before evaluating the test grid. An online policy may adapt during evaluation only through its predeclared update applied to completed forecasts.
- Produce tables from saved results, never from manual transcription.
- Report Monte Carlo uncertainty and failure/missingness rates.
- Keep negative controls and theorem-violating regimes in the released design.

## 8. Execution gate

The load-bearing HE, BW, and FRAME-2P-U analytical campaigns are complete. The
compact fixed-size N-09 closure and the 576-draw literal parent/RFD BW parity
matrix are complete with qualified fixed-rank verdicts. The public environment
and APP-FIN parent pipeline have been audited and reproduced and
[[notation-map|the notation map]] is complete; the long parent simulations are
optional unattended reproduction work. The fixed-rank non-forecasting APP-FIN
illustration and its centre gate are complete; Paper 1 now proceeds to freeze.
Predictive rank, factor-score dynamics, finite-sample centre redesign,
future-centre policy, and forecasting are one post-freeze programme, now
ordered as APP-MONTHLY-VAR followed by APP-HF-0 through APP-HF-5 in
[[Home application — hourly crypto realised covariance]]. Infinite-memory
cancellation, signed-AIRM, higher positive smoothing, selector efficiency,
FRAME implementation, and BW exponent-sharpness are not prerequisites unless a
required compact comparison exposes a genuine dependency.
