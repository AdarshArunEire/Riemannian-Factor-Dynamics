# reference/AUDIT.md — reading the parent's code

Commit `c07d49c`, read 2026-08-18. See `PROVENANCE.md`.

**Rule for this file: log, do not fix.** Everything below is a description of
what their code does, not a judgement about what it should do. Where their code
and their paper appear to disagree, that is recorded as an observation with
enough detail to check later — not as an error.

---

## 1. What is here, and what is not

| file | what it is | priority |
|---|---|---|
| `main_func.R` | `subspace_d`, `main_BWS`, `main_sphere` — the top-level drivers | **core** |
| `BWS_util.R` | all BW geometry + the estimator + all evaluation | **core** |
| `sp500_reproduce.R` | the application, **seeded** | **core** |
| `sp500_analysis.R` | the same application, unseeded, older plotting | reference |
| `BWS_simulation.R` | the SPD simulation study | **core** |
| `sim_do.R` | 4-line driver that seeds and sources `BWS_simulation.R` | **core** |
| `sim_summary.R` | reads `./save/*.RData`, makes the SPD tables | core |
| `stock_price_extract.ipynb` | the data pipeline | **core** |
| `Crawling wikipedia page table.ipynb` | S&P 500 constituent list from Wikipedia | supporting |
| `sphere_util.R`, `Sphere_simulation.R`, `simulation.R`, `simulation_main.R`, `Sim_summary_sphere.R` | the sphere branch — vMF noise, unit vectors | **not our problem** |

**Nothing runs out of the box**, and that is deliberate on their side rather
than an omission. Their `.gitignore` excludes `sp500_covariance/`, `save/`,
`Figs/`, `defunct/`, `trial_and_error/`. So the following are referenced by the
scripts and absent from the repo:

- `./sp500_covariance/sp500_12bySector.RData` — the realised-covariance panel,
  plus `selected_companies` and `overall_covariance_training`
- `./sp500_covariance/VIXCLS.csv` — VIX close, i.e. FRED series `VIXCLS`
- `./save/` — every simulation output that `sim_summary.R` reads
- `./sp500_covariance/sp500_13.RData` — a 13-asset panel, referenced only in a
  commented-out line

The panel has to be rebuilt. The notebook says exactly how.

---

## 2. The data pipeline — `stock_price_extract.ipynb`

```python
import yfinance as yf
data = yf.download(tickers, start="2000-01-01", end="2024-12-31")
data["Close"].to_csv("stock_price_data", index=True)
```

- **vendor**: Yahoo, via `yfinance`
- **window**: 2000-01-01 to 2024-12-31 (the analysis then uses only 2000–2019)
- **field**: `Close`
- tickers come from a CIK → ticker map built off SEC `company_tickers.json`
  cross-referenced with a Wikipedia S&P 500 table, plus a hand-written fixup
  list for twelve ambiguous CIKs (GOOG, BRK-B, BF-B, META, …). They download
  **all** constituents; the twelve are selected later.

**Open question, and the sharpest one for reproduction.** `yf.download` changed
its default: older `yfinance` returned raw `Close` with `Adj Close` separate;
newer versions auto-adjust, so `Close` *is* adjusted. The notebook pins no
version. Over 2000–2024, splits and dividends are not a rounding error. Which
series they actually got depends on when they ran the cell.

This is a well-posed question for Huang if reproduction diverges materially.
Do not ask it before trying.

**Scaling is settled**, though — `sp500_analysis.R:150`:

```r
dta = dta * 10000 # Convert to percentage points
```

Returns are decimal; covariances are multiplied by 1e4 afterwards. So distances
are reported in "percentage points squared" units.

---

## 2b. How many trading days are in their month? Consistent with ~20, not 21

`experiments/diag_risk_gap.py` and `experiments/diag_day_count.py` ->
`results/final/diag_risk_gap.md`, `results/final/diag_day_count.md`, 2026-08-18.

**This section is an inference from our panel, not something read off their
code.** Their notebook states no day count. Read it as a band.

**Why we went looking.** `check_panel_vs_parent.py` matched their published
LOCF and EWMA numbers to <=2.4% on BW and on Frobenius, but missed the GMV
risk error by 14.7-27.5%, always LOW. LOCF and EWMA fit nothing -- no Frechet
mean, no seed, no convergence -- so the gap could only be in the panel.
`diag_risk_gap.py` then refuted the obvious explanation: a 2.4% perturbation
of our covariances moved the risk error by only 2-5% (D1), and shrinking them
towards better conditioning made the gap WORSE (D3). Both point the same way:
**their Sigma is more ill-conditioned than ours.**

**The split that explains it.** BW and Frobenius are BULK statistics --
dominated by the largest eigenvalues. The GMV risk error runs through
`1/(1' Sigma^-1 1)` and is a TAIL statistic -- dominated by the smallest.
Fewer observations per month moves the tail hard and the bulk barely. A small
day-count difference therefore produces exactly the observed pattern: bulk
agreeing, tail systematically low.

**A floor that holds before any number is computed.** `np.cov` uses `ddof=1`,
so a 12x12 covariance built on K days has rank at most K-1 and is singular at
K <= 12. Their own `solve(truth_lag)` would fail there. Their effective M is
at least 13 whatever else is true.

**The sweep** (adjusted-close panel; worst gap over LOCF and EWMA; days
removed evenly spaced, not from the end):

| K | mean days | kappa median | lambda_min median | worst bulk gap | worst tail gap |
|---|---|---|---|---|---|
| 13 | 13.0 | 1.203e+04 | 1.425e-03 | 17.3% | 3120.5% |
| 14 | 14.0 | 3.872e+03 | 5.189e-03 | 21.1% | 585.3% |
| 15 | 15.0 | 1.813e+03 | 1.055e-02 | 14.4% | 74.0% |
| 16 | 16.0 | 1.130e+03 | 1.601e-02 | 9.8% | 37.2% |
| 17 | 17.0 | 8.305e+02 | 2.371e-02 | 8.2% | 8.8% |
| 18 | 18.0 | 6.169e+02 | 2.866e-02 | 9.8% | 27.2% |
| 20 | 19.9 | 4.702e+02 | 3.814e-02 | **1.5%** | **5.3%** |
| all | 21.0 | 4.281e+02 | 4.149e-02 | 2.4% | 23.7% |

**K=20 minimises both families at once** -- bulk 2.4% -> 1.5%, tail
23.7% -> 5.3% -- at 19.9 mean effective days against 21.0 for the full panel.
Roughly **one trading day per month dropped**. That both families improve
together is what makes day count the mechanism rather than a coincidence: a
knob that only moved the tail would have left the bulk flat.

**Mechanism, offered as a hypothesis.** Section 2 records that they download
**all** S&P constituents and slice the twelve out later. If rows with a missing
price anywhere in the ~500-name universe were dropped before that slice, their
monthly covariances rest on slightly fewer days than ours -- worse conditioned,
sharper GMV weights, larger risk errors, negligible effect on the bulk. That is
consistent with everything measured here. It is not confirmed, and the notebook
at commit `c07d49c` does not show it.

**Do not over-read K=20.** The sweep is non-monotonic: K=17 gives a tail gap of
8.8%, and K=18 worsens it to 27.2%. So this identifies "consistent with ~20
effective days per month", not their M. One K should not be reported as a
determination.

**Still open if this is wrong**, in D4's stated order: whether they demean
within the month; whether returns are computed across month boundaries or reset
each month; whether any winsorising or missing-data fill preceded the covariance.

---

## 3. The estimator — `rfm_bws` in `BWS_util.R`

Pipeline, in order:

1. **Fréchet mean** `mean_on_BWS(x, tau = 0.5, tol = -1, max.iter = 100, batch_size)`
2. **Tangent basis** `tan_basis_bws(mu_hat)` — a canonical orthonormal basis `E`
   and its Lyapunov image `E_lyapunov`, both built from the eigendecomposition
   of `mu_hat`
3. **Log-map to coordinates** `log_vec_construct` — each `x_i` becomes a
   `p(p+1)/2` vector via `0.5 * tr(E_lyapunov[k] %*% Log_BWS(x_i, mu))`
4. **Factor model** `LYB_fm(log_x_vec, r, h)` — Lam–Yao–Bathia on the
   log-mapped coordinates

Four observations, logged not fixed:

**(a) The Fréchet mean never tests for convergence.** `mean_on_BWS` is called
with `tol = -1`. Its break condition is `loss_old - loss < tol`, i.e.
`loss_old - loss < -1` — true only if the loss got *worse by more than 1*. In
normal operation it runs exactly `max.iter` gradient steps at fixed `tau` and
stops. Not iterate-until-converged; a fixed budget.

**(b) It is initialised at the first observation.** `mu = X[1,,]`, not the
arithmetic mean.

**(c) With `batch_size` set it is stochastic.** `idx = sample(n, batch_size)`
each step, with `tau` decayed as `tau_0 / sqrt(i)`. The application uses
`batch_size = 30`; the simulations use `16`. This is the only source of
randomness in the application, and it is unseeded in `sp500_analysis.R`.

**(d) `Log_BWS` takes square roots of non-symmetric products.**
`sqrtm(X %*% M) + sqrtm(M %*% X) - 2*M`. `X %*% M` is not symmetric, so this is
`expm::sqrtm` on a general matrix, which can return complex values — which is
why `Re(...)` appears around `geod_BWS_core` in `Frac_Var_LYB`. Our
`rfd.spd.bw` computes the same objects through symmetric sandwiches only.

**(e) `LYB_fm`'s rank estimate can never exceed `r - 1`.**

```r
ratios = evals[2:r] / evals[1:(r - 1)]
r_hat  = which.min(ratios)
```

The search runs only over the first `r` eigenvalues, where `r` is the number of
factors *you passed in*. So `r_hat` is bounded by the argument. This is the raw
eigenvalue-ratio selector — the one the canon's P-RATIO correction is about.

---

## 4. The evaluation — and the answer to `highest_value_check`

The predeclaration asks: *which loss ranks RFM against LFM/LOCF/EWMA, and do
BW-ranked and Frobenius-ranked comparisons ever disagree?*

**They compute both side by side in the same returned object.** No estimator
reimplementation is needed: one retained `main_BWS(..., r = 15)` result
contains the four complete curves.

**Measured result (corrected 2026-08-19):** RFM has lower held-out FVU at all
15 ranks under BW and 10 of 15 under Frobenius. Frobenius narrowly prefers LYB
at ranks 2, 3, 11, 14, and 15, so the loss changes the winner at 5 of 15 ranks.
This is a reconstruction comparison, not a forecasting result or selector.

### In-sample / test-set fit (`main_BWS`)

Returns, for each number of factors 1..r:

| | RFM | LYB (their "LFM") |
|---|---|---|
| BW | `FVU_RFM_BWS` | `FVU_LYB_BWS` |
| Frobenius | `FVU_RFM_Euc` | `FVU_LYB_Euc` |

FVU = fraction of variance unexplained, i.e. `sum d(x_hat, x)^2 / sum d(centre, x)^2`.
The normaliser is metric-consistent: BW uses the BW Fréchet mean, Euclidean uses
the arithmetic mean. That is a fair choice and worth saying so.

Before a BW distance is taken of an LYB prediction, the prediction is pushed
back onto the cone: `project_to_SPD(x_hat, epsilon = 1e-6)`. The linear model
does not produce SPD forecasts, so the BW comparison is against a *repaired*
prediction. The Frobenius comparison is against the raw one. **The two losses
are therefore not scoring quite the same object**, and the repair only ever
helps the linear model on the BW side.

### Out-of-sample forecasting (`sp500_reproduce.R`)

Four models — **RFM (r = 2)**, **LFM (r = 1)**, **LOCF** (previous month), and
**EWMA** (λ = 0.94) — over the last 36 months, scored four ways:

1. `subspace_d` on the leading k eigenspaces, k = 1..q (sine-θ)
2. `BWS_errors` — squared BW distance, plotted as `sqrt(...)`
3. `Euc_errors` — Frobenius norm, **not squared**, plotted raw
4. `risk_error` — GMV portfolio risk error

Two things to be careful with:

- The arrays are stored inconsistently — BW squared, Frobenius not — and each
  is then transformed at plot time so that both figures show a distance. The
  figures are consistent; the arrays are not. Anyone reusing `BWS_errors` and
  `Euc_errors` directly will compare a squared quantity to an unsquared one.
- **RFM is given 2 factors and LFM is given 1.** Not matched on capacity.

The GMV weights come from the *previous month's realised* covariance,
`w ∝ solve(truth_lag) %*% 1`, identically for all four models. So the risk
comparison holds the portfolio fixed and varies only the risk forecast — it is
not a portfolio-construction comparison.

---

## 5. The finding that matters most for Paper 1

`dyn_RFM` in `BWS_util.R`:

```r
if (m == 0) {
  aux = main_BWS(x, r = r, test_size = test_size - m, ...)
  mu_hat = aux$mu_hat                                 # estimated once
} else {
  aux = main_BWS(x, r = r, test_size = test_size - m, ..., mu_hat = mu_hat)
}                                                     # and reused thereafter
```

The training window expands month by month, and the loading space, the factors
and the VAR(1) are all re-estimated at every step — **but the Fréchet centre is
estimated once, on the first training window, and held fixed for all 36 forecast
months.**

That is the fixed-centre restriction, in their code, in the one place where it
could most plausibly cost something. It is the concrete point of contact
between this repo and the entire thesis of Paper 1, and it is four lines long.

Note also that the alternative is *available* to them — passing `mu_hat = NULL`
would re-estimate it each step — so this is a choice, not a limitation of the
implementation. Whether it is a costly one is exactly the open question.

---

## 6. Seeding — correcting what we assumed

The predeclaration's `N00.established_fact` currently reads:

> Neither `simulation_main.R` nor `BWS_simulation.R` calls `set.seed()`.
> Exact reproduction was never available.

**The conclusion holds. The reason is wrong.** What is actually there:

- `sim_do.R` **does** seed: `set.seed(5566 + type)` for `type` in 1:4, then
  sources `BWS_simulation.R`. So the SPD simulations are driven from a seeded
  entry point.
- `sp500_reproduce.R` **does** seed: `set.seed(1)`.
- `simulation_main.R` (sphere) does not, and `sp500_analysis.R` does not.

But `BWS_simulation.R` runs its 300 replicates inside
`foreach(...) %dopar%` on a 12-worker `makeCluster`. A master-side `set.seed`
does **not** propagate to `parallel` workers — that needs
`clusterSetRNGStream` or `doRNG`, and neither is used. `.inorder = FALSE`
compounds it: results come back in completion order.

So exact reproduction of the simulation tables is still unavailable, because
the randomness happens in unseeded workers. A numeric mismatch remains not a
failure of this project. **Amend the predeclaration to say that** — the current
wording would not survive a referee who opened `sim_do.R`.

`sp500_reproduce.R` is a different case: seeded, single-threaded, and the only
randomness is the mini-batch sampling in `mean_on_BWS`. That one may well be
exactly reproducible. It is the script to run.

---

## 7. Simulation design, as coded

`BWS_simulation.R`, driven by `sim_do.R`:

- `num_sim = 300` replicates
- `p ∈ {5, 10}`, `n ∈ {50, 100, 200}`, 4 cases → 24 cells
- data: `dta_gen_BWS(n = n + 200, p, mu_type, r = 5, s, z_noise, alpha)`;
  **true rank 5**, 100 burn-in steps discarded
- fitted with `main_BWS(dta$X, 10, test_size = 200, h = 6, batch_size = 16, max.iter = 16)`
  — so **10 factors evaluated against a true rank of 5**, train `n`, test 200
- an oracle is computed via `Frac_Var_ora` using the true `A` and true `mu`

Cases (`case_param`):

| case | alpha | z_noise | s | mu_type |
|---|---|---|---|---|
| 1 | 0.8 | 1.0 | 1.5 | 1 = identity |
| 2 | 0.2 | 1.0 | 1.5 | 1 = identity |
| 3 | 0.8 | 1.0 | 1.5 | 2 = Toeplitz |
| 4 | 0.2 | 1.0 | 1.5 | 2 = Toeplitz |

The comment block above `case_param` says case 4 has `z_noise = 1.5`. The code
says `1.0`. Comment/code mismatch — logged, not resolved.

`max.iter = 16` here versus `100` in the application: the Fréchet mean gets a
sixth of the budget in the simulations, and (per §3a) that budget is the whole
stopping rule.

---

## 7b. A defect, found by the metric calibration

`geod_BWS_core` in `BWS_util.R` ends:

```r
res = sum(diag(X)) + sum(diag(Y)) - 2 * sum(diag(temp))
return (sqrt(res))
```

with no clip. When `X == Y` that is a difference of large traces which should
be zero and lands **slightly negative** from roundoff, so `sqrt` returns
**NaN**. Confirmed 2026-08-18 by `R/calib_bw_metric.R`: of 18 pairs, cases 5
and 14 — identical matrices at kappa = 1e3, m = 3 and m = 12 — came back NaN,
with `Warning message: In sqrt(res) : NaNs produced`.

Whether it fires is the luck of the roundoff sign. Case 11 returned exactly
0.0; cases 2, 8 and 17 returned small positives. Our `bw_dist2` clips at zero
and returned a finite value on all 18.

Where it bites in their pipeline:

- **`mean_on_BWS`** computes `loss = mean(geod_BWS(X, mu_new))`. One NaN makes
  the mean NaN, so `loss_old - loss < tol` evaluates to `NA` and
  `if (i > 1 && NA)` raises *"missing value where TRUE/FALSE needed"* — a hard
  stop, not a silent wrong answer. If their scripts die there, this is why.
- **`Frac_Var_bws`** accumulates `geod_BWS_core(x_hat, x_test)^2`. One NaN
  poisons the whole sum, and predictions approach the data as the factor count
  rises — which `sp500_analysis.R` sweeps to 15.

The trigger needs near-exact coincidence: perturbing by 1e-6 of the Frobenius
norm (the `near` cases) did not fire it. With real monthly data an exact hit is
unlikely. It is a latent crash, not an active one.

One-line fix on their side would be `sqrt(max(res, 0))`. **Not our fix to
make** — but it is a small, checkable, useful thing to mention to Huang, and
the kind of thing that is a gift rather than a criticism.

---

## 8. Smaller things, logged

- `BWS_simulation.R` calls bare `sink()` inside each `%dopar%` worker with no
  matching `sink(file)`. In a worker with no active sink this errors. Expect it
  to bite on the first run.
- `Frac_Var_bws`, Euclidean branch, non-array `x_test`: `res = norm(...)`
  overwrites the whole result vector instead of `res[i] =`. Only reachable when
  a single test matrix is passed.
- `dyn_RFM` sets `x_test = x[c(1:(n - test_size + m)),,]` — identical to
  `x_train`. Never used afterwards; harmless.
- `subspace_d` returns `Inf` rather than erroring when dimensions disagree; the
  `stop()` calls are commented out.
- `sp500_analysis.R` has a commented-out `cov2cor` block — a correlation-matrix
  variant that was explored and dropped.
- `sp500_analysis.R` has a commented-out `[109:240]` slice — a 2010–2019
  variant. The live code uses `[1:240]`, i.e. **2000-01 to 2019-12**, 240
  months, of which the last **36** are test.
- **`sp500_covariance/` is absent from the repo**, and no file in the repo
  builds it. `sp500_reproduce.R:12` and `:138` read `VIXCLS.csv` and
  `sp500_12bySector.RData` from it. The RC panel is an INPUT to their code —
  the notebook stops at prices, the R scripts start at covariances, and the
  step between them exists only in Huang's email. Recorded in PROVENANCE.
- **`sp500_reproduce.R` is a pruned copy of `sp500_analysis.R`.** The
  subspace comparison was removed but its scaffolding was not: lines 276, 290,
  295 and 304 still compute `v = as.matrix(temp$vectors[,1:k])` and never read
  `v`, and the enclosing `for (k in 1:q)` loop runs twelve times with every
  body guarded by `if (k == 1)`. The live version is `sp500_analysis.R:417-449`,
  `cos_dist[k,model,m] = subspace_d(v, truth$vectors[,1:k])`. So the sine-θ
  distance the predeclaration lists as "present in the scripts" is present in
  `sp500_analysis.R` only — if we want a leading-k eigenvector comparison, that
  is where it lives, and `sp500_reproduce.R` will not produce one.
- **The published means and medians are never printed.** They are computed
  inside `sprintf()` calls that build plot legend labels (lines 330-336,
  379-385, 461-467) and die with the graphics device. What survives in the
  global environment is `BWS_errors`, `Euc_errors` and `risk_error`, 4×36 each,
  rows in the order RFM / LFM / LOCF / EWMA. Only `BWS_errors` is stored
  SQUARED; the legend takes `sqrt` of it and reports the other two directly.
  `R/run_parent_reproduce.R` harvests these rather than editing their file.
- `overall_covariance_training` is loaded from the RData and scaled at
  `sp500_reproduce.R:149`, then never read again in either sp500 script. Dead.
- **The `k = 1:15` loop at `sp500_reproduce.R:156` is 14/15 dead compute.** It
  runs `main_BWS` fifteen times and stores `RFM_xhat[k,,,]` and
  `LFM_xhat[k,,,]` — both of which are assigned at lines 161-162 and **never
  read again**. The only surviving output is `results`, left holding `k = 15`,
  used for the Factor 1 and Factor 2 plots at lines 168-200. So fourteen of
  the fifteen fits contribute nothing, and all fifteen discard the four FVU
  vectors `main_BWS` returns — the exact quantities `highest_value_check`
  needs. Sourcing their script therefore costs fifteen fits we cannot avoid
  and cannot use. The check itself should make one separate call at `r = 15`;
  it must not repeat the discarded fifteen-fit loop.
- **Where the time actually goes, and why the loop is worse than it looks.**
  `rfm_bws` (`BWS_util.R:445`) computes `mu_hat` via `mean_on_BWS` only when
  none is supplied — and `mean_on_BWS` takes no `r`. It is called with
  `tol = -1`, so the early-exit test `loss_old - loss < tol` can never fire and
  it always runs the full `max.iter = 100`. Each of those hundred iterations
  draws a 30-matrix batch for the *gradient* but then evaluates
  `mean(geod_BWS(X, mu_new))` on **all 204** training matrices
  (`BWS_util.R:252`), so the mini-batching saves less than it appears to. That
  full pass, a hundred times, is the cost of a fit; the r-dependent part
  (`LYB_fm`, an eigenproblem on a 78-dimensional vech) is comparatively free.
  So every one of their fifteen fits costs about the same, and fourteen of them
  recompute an r-independent Fréchet mean. `main_BWS` takes a `mu_hat` argument
  (`main_func.R:73`) and forwards it, which is the supported way not to.
  **They already do exactly this elsewhere**: `dyn_RFM` (`BWS_util.R:767-785`)
  loops 36 times over the test window and only `m = 0` computes the mean —
  every later iteration passes `mu_hat = mu_hat`. So the 36-fit rolling
  forecast costs about one expensive fit plus 35 cheap ones, while the 15-fit
  factor sweep costs fifteen expensive ones. The optimisation is theirs; it
  just was not applied to the `k` loop.
- `main_BWS` is **stochastic**: `mean_on_BWS` draws
  `idx = sample(n, batch_size, replace = FALSE)` every iteration
  (`BWS_util.R:242`), consuming the global RNG stream. With `set.seed(1)` at
  `sp500_reproduce.R:9` the serial order of `r = 1..15` is part of the result.
  Anything parallelised over `r` gets different draws and must say so.

---

## 8b. Metric calibration result

`R/calib_bw_metric.R` -> `py/tests/test_parity_with_parent.py`, 2026-08-18.

**The two implementations agree.** Worst disagreement across the 16 cases where
they returned a number: **4.2e-12**, relative to `tr X + tr Y`, against a test
bound of 1e-9.

That is two languages, two BLAS libraries and two genuinely different routes
through the same formula — theirs via `expm::sqrtm` on non-symmetric products,
ours via `eigh` on symmetrised inputs — landing on the same numbers. Any later
disagreement between their results and ours is therefore about the DATA or the
ESTIMATOR, not about the metric. That was the whole purpose of doing this
before touching prices.

No complex leakage on any finite case, so the `Re(...)` wrappers in their
`Frac_Var_LYB` are defensive rather than load-bearing on inputs like these.

---

## 9. What this changes for us

1. **B3.2 cannot run as written.** `sim_summary.R` reads `./save/`, which is
   empty until `sim_do.R` has run. Run `sim_do.R` first; expect the `sink()`
   error. A second defect is now recorded: `sim_do.R` loops `type=1:4`, but
   `BWS_simulation.R` does not consume `type` and already loops all four cases.
   The driver therefore runs the complete 24-cell suite four times and
   overwrites the same 192 files; only its fourth pass survives. The audited
   `R/run_parent_simulations.R` wrapper removes the one stray `sink()` only in
   a disposable copy and executes that retained complete pass once.
2. **B3.4a is fully specified** — vendor, window, field, scaling all recorded
   above. The only open choice is adjusted-vs-raw close, and that is open for
   them too.
   *(2026-08-18: built and verified. Adjusted close is the closer variant.
   Agreement is ~2% on bulk statistics and ~5% on tail statistics once the
   day count of §2b is allowed for. See §2b.)*
3. **`sp500_reproduce.R` is the target, not `sp500_analysis.R`.**
4. **`highest_value_check` needs one parent fit, not fifteen.**
   `main_BWS(..., r = 15)` returns all four length-15 vectors:
   `FVU_RFM_BWS`, `FVU_LYB_BWS`, `FVU_RFM_Euc`, and `FVU_LYB_Euc`.
   Read them from that single fit and compare rankings factor-by-factor. The
   completed shared-mean run initially stored prefix means; these recover the
   rank curve exactly as $v_r=r\bar v_r-(r-1)\bar v_{r-1}$. The corrected result
   is RFM 15/15 under BW and 10/15 under Frobenius, with winner reversals at
   ranks 2, 3, 11, 14, and 15. `R/run_parent_victory_lap.R` now writes the
   returned curves directly.
5. **The competitor set was mis-stated in our notes.** In-sample it is RFM vs
   **LYB**, one competitor. Out-of-sample it is RFM vs LFM vs LOCF vs EWMA.
   BUILD.md and the predeclaration both said LFM/LOCF/EWMA throughout.
6. **VIX is a second data dependency** — FRED `VIXCLS`, monthly means over
   2000–2019 — used for the Factor 1 overlay, not for estimation.
