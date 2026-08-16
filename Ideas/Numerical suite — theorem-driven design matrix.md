---
title: Numerical suite — theorem-driven design matrix
type: numerical-design
status: planned
authority: canonical-design-only
updated: 2026-08-12
---

# Numerical suite — theorem-driven design matrix

## 1. Scope and status

Every project-specific item in this note is **PLANNED**. As of 2026-08-12, this repository contains **zero implementation and zero empirical output for the extension suite**, so its new analytical results remain empirically unvalidated. The parent paper nevertheless supplies a public R/BW reference implementation at <https://github.com/shuochieh/Riemannian_factor_model>, including simulation, main-function, and S&P 500 reproduction scripts. We therefore begin by reproducing and auditing that baseline; the new HE, BW-uniformity, selector-repair, and FRAME correction layers remain unimplemented. No future simulation result can prove a theorem.

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
| N-00 | parent-paper reproduction baseline | run the public BW/sphere simulations and S&P 500 reproduction scripts under a frozen environment | recover the parent estimator, raw-ratio behaviour, reconstruction/forecast pipeline, and reported benchmark definitions before adding project corrections | version drift, unavailable Yahoo data, or target/convention mismatch must be logged rather than silently repaired | **PLANNED; PUBLIC CODE AVAILABLE** |
| N-01 | bounded-energy HD1 baseline | fixed \(R,h_0,r,\Delta>0\); increasing \(n,p\) | \(d_n=O_p(n^{-1/2}+\ell_n)\); loading \(O_p(d_n/\Delta)\); null eigenvalues \(O_p(d_n^2)\) | generated-tube or dependence violation | **PLANNED** |
| N-02 | HE flat/rigid frame | \(\rho\) below, at, and above \(3/13\); \(b_n=n^{-(1-2\rho)/7}\) | leading balanced rate \(n^{-(3-13\rho)/7}\), plus \(n^{-(a-\rho)}\) | consistency transition at \(\rho=3/13\); balanced headline also needs \(a\ge(3-6\rho)/7\) | **PLANNED** |
| N-03 | HE generic curved moving frame | \(\rho\) below, at, and above \(3/20\) | rate \(n^{-(3-20\rho)/7}+n^{-(a-2\rho)}\) | frame-energy multiplier causes the \(3/20\) boundary | **PLANNED** |
| N-04 | pervasive rescue | \(Y_{t,n}=\sqrt{p_n}a_ng_t+\epsilon_{t,n}\) with centred bounded one-dependent components | \(R_n\asymp\sqrt p\), \(A_{2,n}\asymp p\), \(\Delta_n\asymp p^2\); relative loading error behaves as \(d_n/p\) | replace white idiosyncratic lag by proportional coloured lag to force target contamination | **PLANNED** |
| N-05 | localised high-dimensional background | fixed signal gap with \(R_n^2\asymp p_n\) | spurious lag row of order \(p_n/\sqrt n\) can destroy fixed-gap consistency | directly contrasts N-04; energy growth alone is not rescued | **PLANNED** |
| N-06 | normalisation preserved versus diluted | compare raw \(Y\) and \(Y/\sqrt p\) for pervasive and localised signals | recompute \(A_2,\Delta,d\); pervasive direction can remain stable while localised gap collapses | report estimand change and \(\eta/\Delta\), not nominal scale | **PLANNED** |
| N-07 | growing factor rank | equal-energy factors and fixed total lag energy | verify \(\Delta_n\le h_0F_n^4/r_n\) and predicted selector degradation | increasing \(r_n\) forces gap dilution | **PLANNED** |
| N-08 | zero signal and zero noise | \(\Delta=0\); then noise-free observations with estimated centre/frame | no positive-r loading theorem when \(\Delta=0\); mean/frame errors persist without observation noise | separate null-row selector window for \(r=0\) | **PLANNED** |
| N-09 | fixed-size BW interior | fixed \(m\), compact full-rank regular domain, bounded tangent energy | local constrained means, generated admissibility, \(d_n=O_p(n^{-1/2}+\ell_n)\), null square | compare ordinary safe event with deterministic fallback frequency | **PLANNED** |
| N-10 | BW fractional-normal shrinking margin | \(\alpha_n\asymp m_n^{-A}\), \(m_n=n^x\), with \(x\) below, at, and above \(3/(5A)\) | local coefficients inflate at their proved powers; the conservative matched rank-one branch is consistent for \(x<3/(5A)\) | separate failure of normal-pair support, generated-domain reach, frame/loading balance, and actual gap; the boundary is sufficient, not minimax | **PLANNED** |
| N-11 | rank-changing BW attack | orthogonal rank-one PSD endpoints and regularised approaches to them | nonunique alignments/geodesics/means at the boundary | numerical solver dependence is a symptom, not a repaired estimand | **PLANNED** |
| N-12 | signed Richardson root collapse | positive diagonal roots whose signed extrapolation reaches zero | raw correction exits the domain; admissibility test activates fallback | compare raw, tested, and clipped reconstruction while retaining target labels | **PLANNED** |
| N-13 | fixed-basis diagonal HE–BW | positive root process, \(b=n^{-1/7}\), growing \(m\) | nonempty sufficient window \(m=o(n^{6/7}/\log n)\) under the dossier conditions; frame is rigid | coordinatewise root margin and maximum-error event, not only \(\ell^2\) error | **PLANNED** |
| N-14 | moving eigenvectors | fixed eigenvalues with rotating eigenbasis | diagonal/root reduction fails despite stable spectra | quantify off-basis defect and compare with approximate-match penalty | **PLANNED** |
| N-15 | noncommuting fixed-margin growing-size BW | fixed compatible spectral/polar/Exp/normal/path margins, growing \(m\) | the proved geometric producer has no direct matrix-size factor; statistical error follows the separately supplied energy, dependence, row, and gap budgets | detect hidden implementation dimension costs, generated-domain escape, energy growth, or gap dilution rather than attributing every failure to geometry | **PLANNED** |
| N-16 | FRAME-2P-U curved oracle branch | three exactly separated colours; \(b=n^{-1/7}\), \(M\asymp n^{2/7}\), \(c=n^{-\gamma}\); sweep \(\gamma\) below, inside, and above \((1/6,3/14)\) | inside the window the corrected row is root-\(n\), its post-influence nuisance remainder is sub-root-\(n\), and null eigenvalues are \(O_p(n^{-1})\) when U2P and the actual gap hold | separate validation influence from nuisance remainder; record U2P/tube/mask failures rather than treating bounded energy as sufficient | **PLANNED** |
| N-17 | FRAME correction negative controls | compare the valid two-path correction with direct \(\Omega\) plug-in, same-band score/Richardson, invariant-only redesign, and the robust uncorrected row | same-band retains a generic curved \(n^{-3/7}\) bias; invariant-only changes the estimand; direct plug-in succeeds only when its extra frame producer is verified | use a noncommuting curved witness and a common-gauge conjugation check | **PLANNED** |
| N-18 | centre-drift/factor identification diagnostic | controlled drift-only, factor-only, aligned, orthogonal, mixed, cross-term, and curved-reference rank-inflation DGPs; then the APP-FIN fixed-centre baseline versus moving-centre fits | verify implementation against ID-4/ID-5 and Corollary P-DRIFT: stable aligned span, clean orthogonal rank addition of exactly \(\dim P_{\mathcal S_X^\perp}D\), partial rotation/cancellation, and exact sphere reference-rank change | validates code and reports sensitivity; it cannot determine empirical component dominance without the canonical identifying assumptions | **PLANNED; RUN ONLY AFTER CLEAN N-00 REPRODUCTION** |
| N-18a | ID-8 rank-inflation witnesses | reproduce the three exact analytic constructions as code checks: BW \({\rm SPD}(2)\) with \(x=\operatorname{diag}(a,1)\), \(V\) off-diagonal, \(a\ne1\); AIRM \({\rm SPD}(2)\) noncommuting; \(H^2\); plus the diagonal-BW rigid control | the three curved cases inflate affine dimension \(1\to2\) and the diagonal-BW control does not; the BW defect matches the closed form for every \(a\ne1\), \(0<\vert b\vert<1+a\) | a **code-verification** diagnostic against theorems already proved analytically; agreement confirms the implementation, disagreement indicts the code, and neither outcome can alter ID-8 | **PLANNED** |
| N-18b | ID-7/ID-10 persistence diagnostic | sweep the frozen-factor persistence: short memory, \(\rho_n=1-n^{-\theta}\) for \(\theta\) inside and outside \([0,1)\), and ARFIMA with \(d\in\{0,0.1,0.25,0.4\}\); at each, record \(\psi^+(nb_n)\) against \(b_n^3\) and the realised mean/loading error | the mean error tracks \(\ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1}\); the re-optimised bandwidth \(n^{-(1-2d)/(7-2d)}\) beats \(n^{-1/7}\) for \(d>0\); separation degrades as \(x_n=(1-\rho_n)nb_n\to O(1)\) | measures the **constant and the finite-\(n\) onset**, not the exponent, which is proved. It cannot establish the memory exponent of any real dataset; APP-FIN's \(d\) remains an assumption under test | **PLANNED** |

| N-19 | evaluation-loss distortion and recalibration diagnostic | \(m\in\{3,12\}\), \(M\in\{21,78,1638\}\) Wishart-type and non-Wishart proxies; score a known conditional mean and its shrunk versions under squared BW, AIRM, log-Euclidean, Frobenius and multivariate QLIKE | the finite-sample distortion tracks the closed forms of [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]] §3–§4: BW \(|B_{ii}|/\lambda_i=\frac1M[\frac14+\sum_k\lambda_k^2/(\lambda_i+\lambda_k)^2]\), AIRM \((m+1)/(2M)\); the AIRM scalar recalibration \(c=1-\frac{m+1}{2M}\) removes it and a scalar BW recalibration does not; Frobenius and QLIKE show no distortion; the non-Wishart proxy rotates the induced eigenbasis and the Wishart proxy does not | a **diagnostic**, never a proof: it measures the finite-sample size of an already-proved distortion and the effect of recalibration. It cannot establish or refute LO-1–LO-5, and it does not feed any estimation row | **PLANNED** |

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

No reconstruction theorem is described as a forecasting guarantee.

## 7. Reproducibility contract

- Store every DGP and estimator choice in a versioned immutable configuration.
- Fix and publish seed lists; use independent seeds for train, validation, and test generation.
- Predeclare the sample-size, dimension, energy, bandwidth, gap, dependence, and contamination grids.
- Preserve raw simulation draws, generated covariance series, intermediate centres/frames, and final metrics in separate directories.
- Record software versions, numerical tolerances, convergence/fallback flags, wall time, and hardware/session metadata.
- Use validation only for tuning constants; freeze them before evaluating the test grid.
- Produce tables from saved results, never from manual transcription.
- Report Monte Carlo uncertainty and failure/missingness rates.
- Keep negative controls and theorem-violating regimes in the released design.

## 8. Execution gate

The load-bearing HE, BW, and FRAME-2P-U analytical campaigns are complete. Implementation begins with N-00: freeze and audit the parent public environment, reproduce its simulations/APP-FIN pipeline where the upstream data remain accessible, and map its objects to the canonical notation. N-16/N-17 then extend that audited baseline rather than beginning from zero, while their correction-specific components remain new code. Infinite-memory cancellation, signed-AIRM, higher positive smoothing, and BW exponent-sharpness are not prerequisites unless the selected design consumes them.
