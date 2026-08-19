---
type: build-plan
title: BUILD — the ordered engineering plan
status: active
audience: me, only
created: 2026-08-16
reordered: 2026-08-18
---

# BUILD

The theory notes live in `notes/`. This file is the other thing: **what to actually type, in what order.**

## What changed on 2026-08-18, and why

The original order was written before three things were known. It is reordered, not corrected — the tasks were right, the sequencing assumed facts that have since been replaced by measurements.

1. **The ticker list and the RC recipe arrived.** Table 3 of the paper has the twelve companies; Huang confirmed by email that realised covariances are the monthly sample covariance of daily log returns. B3.4 is no longer blocked, which was the single biggest reason it sat at the back.
2. **The falsifiers were costed.** N-19's full grid is ~2.5 h of unattended compute (E5). Anything that runs unattended should never sit in front of work that needs a human, so Phase 2 moves off the critical path rather than gating it.
3. **E7 raised a question only real data can answer.** The BW and AIRM centres diverge in proportion to dispersion. Nobody knows what dispersion real monthly RCs have, so a cheap measurement is currently blocked on data — which promotes data acquisition from "last" to "soon".

**Task IDs are unchanged** so that anything referring to them still resolves. They are therefore no longer in document order; the running order is the queue below.

---

## Running order

| # | task | why here |
|---|---|---|
| ~~1~~ | ~~**B1.4** loss module~~ | **done** — `py/rfd/eval/losses.py`, 315 tests green |
| ~~2~~ | ~~**B3.4a** RC panel, δ and κ~~ | **done** — panel built and verified against the published LOCF/EWMA numbers |
| ~~3~~ | ~~**B3.1** clone + audit~~ | **done** — `reference/AUDIT.md`, commit `c07d49c` |
| ~~4~~ | ~~**B3.3** notation map~~ | **done** — notes/canonical/notation-map.md, parent paper ↔ pinned code ↔ canon |
| ~~5~~ | ~~**B3.4b** — APP-FIN reproduction and loss-ranking check~~ | **done** — forecasting order reproduced; matched-rank losses disagree at 5/15 ranks |
| 1 | **B3.2** — run their simulations | remaining reproduction task |
| 2 | Phase 4 — the estimator stack | |
| — | **B2.1 → B2.3** — falsifiers | **fire overnight, any time.** Never block on these |

The principle: **latency-bound work first, compute-bound work unattended, desk work when blocked.** Data acquisition and correspondence have latency measured in days. N-19 has latency measured in hours and needs nobody watching.

---

## How to use this

- Work top to bottom **of the queue**. Tasks are sized to **one sitting of 2–3 hours**. On a break day, close the laptop; every task ends somewhere you can commit and walk away.
- Each task is **Do / How / Done when**. The *Done when* is the contract — if it isn't met the task isn't finished, and you don't move on by feel.
- Tick as you go. `[ ]` → `[x]`, and put the commit hash next to it.
- **Anything that disagrees with a theorem gets written down, not tuned away.** That's the whole reason the numbers exist.

**The one rule for the repo:** `sandbox/` may import from `py/rfd/`. Nothing ever imports from `sandbox/`. When scratch code proves useful, promote it into the package and give it a test.

---

## Measured facts

Everything below was measured on this machine and is recorded in `results/final/`. Superseding a number here means re-running its generator and appending, not editing.

**Tolerances.** `num_tol(amplification) = safety * eps * amplification`, `safety = 10`, in `py/tests/conftest.py`. The amplification is a property of the *operation*, not of the inputs — find the worst-conditioned intermediate in the formula and that sets the power of κ:

| operation | amplification |
|---|---|
| `exp(log S)`, `R @ R` — forward compositions | 1 (in practice `m log κ`) |
| `Ri S Ri = I` — whitening | κ |
| `g_mean`, all AIRM **distance** identities | κ² |
| BW and AIRM **barycentre** identities | κ |

Source: `experiments/calibrate_spd.py` → `results/final/spd_calibration.md`. Max implied constant 2.23, min headroom 4.1×.

**Working ranges.**

| | tol | floor | converges to | dead at |
|---|---|---|---|---|
| BW barycentre | 1e-12 | ~1e-14 | κ=1e6 | κ=1e8 |
| AIRM barycentre | 1e-11 | ~6e-12 | κ=1e6 | κ=1e8 |
| `g_mean` | — | ε·κ² | — | κ~1e8 |

**Cost.** N-19's declared grid: BW 44 min, AIRM 105 min, **2.5 h total**. At `m=12, M=1638` the draws are 7.9 GB if materialised at once — the proxy generator **must** chunk. (E4, E5.)

**Convergence is driven by dispersion, not conditioning.** BW iteration count also depends on spectrum shape; AIRM's depends on neither, because affine invariance lets you conjugate the base to the identity, so κ and shape are not properties of the problem. (E1, E6.)

**Geometry divergence.** `d(BW centre, AIRM centre) / spread ≈ c(m)·δ`, with `c(3)≈0.13`, `c(12)≈0.075`, independent of κ. (E7.)

**Panel agreement with the parent.** Our rebuilt panel reproduces their published LOCF and EWMA numbers to **≤2.4% on bulk statistics** (BW, Frobenius) but was **14.7–27.5% low on the tail statistic** (GMV risk error). The two families are dominated by opposite ends of the spectrum, and the gap is a day-count effect: at ~20 effective trading days per month instead of 21, worst bulk gap falls to 1.5% and worst tail gap to 5.3%, both minimised at the same K. Adjusted close beats raw. The mechanism is a hypothesis, not a fact — see `reference/AUDIT.md` §2b for the argument and the caveats, including that the sweep is non-monotonic. (D1–D4.)

**Panel conditioning.** κ median 4.28e2, max 1.48e4 — well inside E2's working range, which ends near 1e6. δ (mean AIRM distance from the panel's own centre) = **5.23**. Against E7's `c(12)≈0.075`, BW and AIRM centres on this panel sit ~0.39 apart in AIRM units. (`rc_panel_summary.md`.)

**Closed defect (2026-08-19).** `spd_eigh`'s strict PSD comparison was blind to NaN because every ordered comparison with NaN is false. Two cheap guards now reject nonfinite matrices before LAPACK and nonfinite eigenvalues afterwards; one direct regression test injects NaN at the shared primitive. The parent implementation's separate unguarded `sqrt(res)` NaN remains pinned by the parity test and is not silently repaired in the reference code.

---

## Phase 0 — scaffold ✅

- [x] **B0.1** repo shape — `2f29ace`
- [x] **B0.2** environments, both languages, frozen — `VERSIONS.md`, `renv.lock`, `requirements.txt`
- [x] **B0.3** the predeclaration file — `config/predeclaration.yaml`, three dated amendments

> Note on B0.3: the file was not valid YAML until 2026-08-18 — a bare `|` in value position opened a block scalar. Recorded as a `syntax-repair` amendment. A predeclaration no parser can read is a predeclaration no tool can enforce; check it parses whenever you touch it.

---

## Phase 1 — SPD geometry primitives

The reusable core. Everything downstream imports it.

### [x] B1.1 — matrix functions

`py/rfd/spd/linalg.py`: `sym`, `rebuild_spd`, `spd_eigh`, `spd_op`, `spd_sqrt`, `spd_invsqrt`, `spd_log`, `spd_exp`, `g_mean`.

**Done, with two corrections to the original plan.** The function is `g_mean`, not `geometric_mean`. And eigenvalues are *not* clipped before `sqrt`/`log` — `spd_eigh` raises instead, under a `strict` flag, which is the better failure mode. Tests: `py/tests/test_linalg.py`.

The κ=10⁸ case the original *Done when* asked for lives in E2 rather than in a unit test, because what it produces is a boundary rather than a pass.

---

### [x] B1.2 — BW distance and barycentre

`py/rfd/spd/bw.py`: `bw_dist2`, `bw_barycentre`, `bw_frechet`, `trace`. Tests: `py/tests/test_bw.py`, 111 cases.

**Superseding the original watch-out.** It said to record iteration count as a function of condition number, and called that curve the empirical picture of BW-SHRINKING-MARGIN. **E1 shows that is the wrong variable.** Iterations track dispersion δ; across κ at fixed δ they *fall*. If the canon's BW-SHRINKING-MARGIN discussion is written against κ, it needs revisiting before it reaches a draft.

Two things the original *Done when* didn't anticipate. The stationarity test is semi-tautological — the loop terminates on exactly that residual — so the load-bearing test is the Fréchet one: perturb the answer and confirm the objective rises. And `bw_dist2` on a commuting family gives one-step convergence, which makes the commuting closed form an excellent *correctness* test and a useless *convergence* test.

---

### [x] B1.3 — AIRM distance and Karcher mean

`py/rfd/spd/airm.py`: `airm_dist2`, `airm_log`, `airm_exp`, `airm_parallel_transport`, `airm_barycentre`, `airm_frechet`. Tests: `py/tests/test_airm.py`, 72 cases.

Affine equivariance verified as the original plan predicted — it does catch most implementation errors in one shot. Added beyond plan: the N=2 Karcher mean equals `g_mean`, a cross-module check against `linalg.py` with no shared code path.

**`step` is pinned at 1.0.** E6 tested `step=0.5` in 90 cells and it lost in all 90 — the full step converges superlinearly, damping drops it to linear convergence at rate 0.5 and needs `log(tol)/log(0.5) ≈ 36` sweeps regardless of where it starts. Either remove the parameter or document it as do-not-touch.

---

### [x] B1.4 — log-Euclidean, Frobenius, and the loss module (1.5 h)

**Do.** `py/rfd/eval/losses.py`: squared Frobenius, multivariate QLIKE, squared BW, squared AIRM, squared log-Euclidean. Plus `logeuclid_barycentre`.

**How.** QLIKE for matrices: $\operatorname{tr}(H^{-1}S)-\log\det(H^{-1}S)-m$. Use `slogdet`, never `log(det(...))`. The BW and AIRM losses are one-line wrappers over `bw_dist2` and `airm_dist2` — do not reimplement them.

**Done when.** Every loss is zero iff its arguments are equal, and QLIKE is finite and positive on 1000 random pairs. Tolerances from `num_tol`, with the amplification argued in a comment.

> **Why this is first.** The predeclaration's `highest_value_check` asks which loss ranks RFM against LFM/LOCF/EWMA in the parent's own scripts, and whether BW-ranked and Frobenius-ranked comparisons ever disagree. That check is the most valuable single output of the entire reproduction, and it cannot run without this module. 1.5 hours here unblocks it.
>
> Note also that `logeuclid_barycentre` is a third centre for E7 — currently it compares BW, AIRM and arithmetic only.

**Done 2026-08-18.** `py/rfd/eval/losses.py` — convention is `loss(H, S)`, forecast first, everywhere, plus a `LOSSES` registry. Suite at 315 green after the shared NaN-guard regression.

---

## What the parent actually does

Read from the code at commit `c07d49c`, 2026-08-18. Full detail in `reference/AUDIT.md`; this is what changes decisions.

**Their pipeline.** Fréchet mean → canonical tangent basis at that mean → log-map every observation to a $p(p+1)/2$ coordinate vector → Lam–Yao–Bathia factor model on those coordinates. Everything downstream of the mean is linear algebra in one fixed tangent space.

**Their Fréchet mean is a fixed budget, not a converged quantity.** `mean_on_BWS(tau = 0.5, tol = -1, max.iter = 100)`. With `tol = -1` the break condition is "the loss got *worse* by more than 1", so in normal operation it runs exactly `max.iter` gradient steps and stops. It is initialised at the **first observation**, and with `batch_size` set it is stochastic (mini-batches of 30 in the application, 16 in the simulations). Our `bw_barycentre` converges to a residual; theirs does not test.

**Their rank selector cannot exceed the rank you give it.** `LYB_fm` computes `ratios = evals[2:r] / evals[1:(r-1)]` and takes `which.min` — the search runs only over the first `r` eigenvalues, `r` being the argument. This is the raw eigenvalue-ratio selector that P-RATIO is about.

**Their BW log-map square-roots non-symmetric products.** `sqrtm(X %*% M) + sqrtm(M %*% X) - 2M`, via `expm::sqrtm` on a general matrix, which is why `Re(...)` wrappers appear downstream. Ours goes through symmetric sandwiches only, so an independent recomputation is a genuine check rather than a re-run.

---

### The four lines that Paper 1 is about

`dyn_RFM`, in `BWS_util.R`:

```r
if (m == 0) {
  aux    = main_BWS(x, r = r, test_size = test_size - m, ...)
  mu_hat = aux$mu_hat                                  # estimated once
} else {
  aux    = main_BWS(x, r = r, test_size = test_size - m, ..., mu_hat = mu_hat)
}                                                      # and reused thereafter
```

The training window expands month by month. The loading space, the factors and the VAR(1) are all re-estimated at every step. **The Fréchet centre is estimated once, on the first training window, and held fixed across all 36 forecast months.**

That is the fixed-centre restriction, in their code, at exactly the point where it could most plausibly cost something. Passing `mu_hat = NULL` would re-estimate it each step — so it is a choice their implementation already supports, not a limitation. Whether it is a costly choice is the open question, and this is where to measure it.

---

## Phase 3 — the parent, and the real data

Promoted ahead of Phase 2. This is where the project's actual risk lives: everything before it is self-checking, and this is the first thing you don't control — their data, their undocumented choices, no `set.seed`, a repo the author himself calls untidy.

### [x] B3.4a — build the RC panel and measure it (3 h)

**Do.** Rebuild the 12-stock monthly realised-covariance panel. Then measure two numbers off it.

**How.** Tickers from Table 3 of arXiv:2607.28385: MSFT, AAPL, ORCL, CSCO, JPM, BAC, WFC, GS, XOM, CVX, COP, EOG. Construction confirmed by Huang, 2026-08-17: *compute the log returns, then the sample covariance of the log returns in each month.*

**Most of the open choices are no longer open** — `stock_price_extract.ipynb` specifies them (AUDIT §2):

| | |
|---|---|
| vendor | Yahoo, via `yfinance` |
| download window | `start="2000-01-01"`, `end="2024-12-31"` |
| field | `data["Close"]` |
| analysis window | `[1:240]` = **2000-01 to 2019-12**, last **36** months are test |
| scaling | `dta * 10000` — decimal returns, covariances then in percentage-point² |

**The one genuinely open choice is adjusted vs raw close**, and it is open for them too: `yf.download`'s default changed, so `Close` is raw in older `yfinance` and auto-adjusted in newer, and the notebook pins no version. Over 2000–2024 that is not a rounding error. Build both, see which matches, and record it. This is the well-posed question to send Huang **if and only if** reproduction diverges materially.

**Second data dependency:** FRED series `VIXCLS`, monthly means over 2000–2019. Not used in estimation — it is the overlay on the Factor 1 plot — but `sp500_reproduce.R` reads it at line 12 and will fail without it.

**Done when.** The panel exists and is documented, **and** you have two numbers written into `results/final/`:

- **κ of the realised covariances.** Marchenko–Pastur predicts sample eigenvalues spread by roughly $\big(\tfrac{1+\sqrt{12/21}}{1-\sqrt{12/21}}\big)^2 \approx 51$ on top of the true condition number, so expect κ ~ 1e3–1e4. E2 says the working range ends near κ=1e6. Confirm you are inside it.
- **δ, the dispersion of the panel** — mean AIRM distance from its own centre, in the units E7 uses. That number decides whether E7's 7%-of-spread divergence between BW and AIRM centres is interesting or noise, and therefore whether a whole strand of the paper is worth pursuing.

> This single task retires two open questions that are currently blocking. It is the highest-value three hours available.

**Done 2026-08-18.** `experiments/build_rc_panel.py` builds both variants and saves the daily returns alongside, so later diagnostics can re-slice without re-downloading. `experiments/check_panel_vs_parent.py` scores them against Figures 3 and 4.

| | |
|---|---|
| κ median / max | 4.28e2 / 1.48e4 — inside E2's range, which ends ~1e6 |
| δ | 5.23 — so BW and AIRM centres sit ~0.39 apart in AIRM units (E7's `c(12)≈0.075`) |
| adjusted vs raw | **adjusted** is closer on every statistic; the working choice, not a settled fact |
| agreement, bulk | BW 0.0–1.0%, Frobenius 0.6–2.4% |
| agreement, tail | GMV risk error 14.7–27.5% **low** — chased in D1–D4 |

**The one thing that did not match was the risk error**, and it took four diagnostics to explain. Short version: BW and Frobenius are bulk statistics, the risk error is a tail statistic, and their month appears to rest on ~20 trading days rather than 21. `reference/AUDIT.md` §2b has the argument and the caveats. The acceptance tolerance is split accordingly and fixed in `config/predeclaration.yaml` **before** our own estimator runs: **2% bulk, 6% tail**.

**Not sent to Huang.** The divergence is explained, and explained by something on our side. The adjusted-vs-raw question stays unasked.

---

### [x] B3.1 — clone and freeze

Done 2026-08-18. `reference/AUDIT.md` (9 sections) and `reference/PROVENANCE.md`.

**Not committed.** The upstream repo has **no LICENSE file**, so by default all rights are reserved. `reference/.gitignore` excludes everything except the audit and the provenance record. The pin is commit `c07d49c257d489e00b7e15bdd432954946a2a694` (2026-04-30), verified by MD5 against a clone. Pinning matters here: Huang intends to tidy the repo after his travel.

**It is 14 files, not 15** — 12 R scripts and 2 notebooks. Only 8 are ours; five are the sphere branch.

**Nothing runs out of the box, and that is deliberate.** Their `.gitignore` excludes `sp500_covariance/`, `save/` and `Figs/`, so the RC panel, the VIX series and every simulation output are absent by design. Everything referenced-and-missing is listed in AUDIT §1.

Still open: `renv::snapshot()` against their actual package set (`maotai`, `expm`, `deSolve`, `vMF`, `MASS`, `reshape2`, `gridExtra`, `ggplot2`, `lubridate`, `doParallel`, `foreach`).

---

### [ ] B3.2 — run the simulations (3 h)

**Do.** `BWS_simulation.R`, `Sphere_simulation.R`, `simulation_main.R`, `sim_do.R`, `sim_summary.R`. These need **no external data**.

**How.** Do **not** call upstream `sim_do.R` directly. It sources the already-complete four-case sweep four times while its `type` variable is unused, overwriting the same 192 files on every pass; only pass four survives. It also lacks `./save/` and contains a proven stray worker-side `sink()`. Use the audited wrapper from the repository root:

```powershell
Rscript R/run_parent_simulations.R --check
Rscript R/run_parent_simulations.R
```

The wrapper leaves upstream byte-for-byte untouched, patches only the stray `sink()` in a disposable `results/raw/n00` copy, runs the complete four-case sweep once with the final driver seed, and captures the raw files, manifest, console log and summary plots. Compare against the paper's tables — especially Table 2, the raw-eigenvalue-ratio selection rates.

The grid as coded: `num_sim = 300`, `p ∈ {5,10}`, `n ∈ {50,100,200}`, 4 cases = **24 cells**. True rank 5, ten factors evaluated, train `n`, test 200, `batch_size = 16`, `max.iter = 16`. Cases and their parameters are in AUDIT §7 — including a comment/code mismatch on case 4's `z_noise`.

The wrapper must abort if either audited defect changes: exactly one bare worker-side `sink()` and the redundant four-pass driver. That is a prompt to re-audit upstream, not broaden the patch.

**Done when.** Their outputs are reproduced within Monte Carlo error, or every divergence is logged in `AUDIT.md` with a hypothesis. Use the Stage A / Stage B criteria in `config/predeclaration.yaml` — and remember Stage A's band is roughly a quarter of a standard deviation. It catches gross pipeline errors. **It cannot certify agreement; do not report it as though it does.**

> **Corrected 2026-08-18.** `sim_do.R` *does* call `set.seed(5566 + type)`, and `sp500_reproduce.R` calls `set.seed(1)` — the old claim that nothing was seeded was wrong. But `BWS_simulation.R` runs its replicates in a 12-worker `makeCluster` and a master-side seed does not reach `parallel` workers without `clusterSetRNGStream` or `doRNG`, neither of which is used. So exact reproduction of the *simulation* tables is still unavailable, and a numeric mismatch is still not a failure of this project. See the dated amendment in the predeclaration.

---

### [x] B3.3 — notation map (completed 2026-08-19)

**Do.** `notes/canonical/notation-map.md`. Every object in their code ↔ every object in your canon.

**How.** A table: their symbol, their file and line, your symbol, your canonical note. Cover at minimum $\kappa$ vs your $s_n$ and $\Delta_n$, their $\lambda_r$ vs your $\lambda_r(\mathbb L_n)$, their loading estimator vs your $\mathcal S_{X,n}$, and their raw ratio (Eq. 5) vs your threshold/ridged selectors.

**Completed.** `notes/canonical/notation-map.md` pins the paper/code/project crosswalk at upstream commit `c07d49c`, accounts for every formal, returned field, and substantive local symbol in `main_func.R`, maps the supporting BW/sphere APIs, and records all non-equivalences needed by reproduction and Paper 1.

**Done when.** Every symbol in their `main_func.R` has a row. **Notation-only rewriting must not change any hypothesis, norm, target or rate** — if you find yourself wanting to, that's a finding, log it.

> Read the paper properly here, not generally: the appendix, the tables, the data section. Table 3 sat unread for a week while the front half was studied closely. When the task is reproduction, the back of the paper is where the spec lives.

---

### [x] B3.4b — APP-FIN (completed 2026-08-19)

**Do.** Run **`sp500_reproduce.R`** against the panel from B3.4a. Not `sp500_analysis.R` — same analysis, but unseeded and with older plotting. `sp500_reproduce.R` calls `set.seed(1)`, is single-threaded, and its only randomness is the mini-batch sampling in `mean_on_BWS`. It is the one that might reproduce exactly.

**How — five commands, from the repo root.** Install `maotai`, `expm`, `deSolve` first, then `renv::snapshot()` (the B3.1 leftover). The first three run the published application, the fourth retains the matched-rank FVU curves, and the final command validates and reports both.

```
python experiments/export_for_parent.py      # panel + VIX -> their input dir
Rscript R/make_panel_rdata.R                 # -> sp500_12bySector.RData
Rscript R/run_parent_reproduce.R             # sources THEIR script verbatim
Rscript R/run_parent_victory_lap.R            # one fit -> rank-specific FVU curves
python experiments/check_parent_run.py       # -> integrated parent_reproduce report
```

**The blocker nobody predicted:** `sp500_covariance/` **does not exist in their repo**, and nothing in the repo builds it. The RC panel is an *input* to their code. Step 1 supplies it; `reference/PROVENANCE.md` records that a directory was added and no upstream file touched.

**Two traps in step 1**, both silent if you get them wrong: the panel must be written **unscaled**, because `build_rc_panel.py` already applied their ×10000 and `sp500_reproduce.R:148` applies it again; and `covariances` must be `(year, month, asset, asset)` with **year on axis 1**, because their `aperm(dta, c(2,1,3,4))` plus column-major flattening only comes out chronological that way. Both are asserted, not assumed.

**Read Stage 1 before Stage 2.** Their script computes LOCF and EWMA itself from the panel we hand it, and we already have both in Python. Same input, two harnesses — they must agree at round-off. A failure there is *our evaluation code*, and without the check a bad RFM number is ambiguous between three causes instead of one. `check_parent_run.py` exits non-zero if Stage 1 fails, precisely so you cannot read past it.

**Done when.** Every divergence from the paper's reported numbers is logged rather than repaired. Bands were fixed **before** this ran — 2% bulk, 6% tail, `config/predeclaration.yaml` amendment 2026-08-18 — and were set from LOCF and EWMA, which fit nothing. Expect *approximate* reproduction only; the ~20-vs-21 trading-day difference of AUDIT §2b is **not** corrected for. The number to judge on is Stage 3, the **ranking**: a decimal outside the band with the ordering intact is a data difference, a flipped ordering is a reproduction failure.

> **The highest-value check needs one additional fit, not a loop of fits.** Their `k = 1:15` loop at line 156 calls `main_BWS` fifteen times and discards the FVU vectors. But one `main_BWS(..., r = 15)` call already returns all four length-15 curves: `FVU_RFM_BWS`, `FVU_LYB_BWS`, `FVU_RFM_Euc`, and `FVU_LYB_Euc`. `run_parent_victory_lap.R` retains them. Whether BW and Frobenius prefer different model families is then a pointwise comparison of those curves.
>
> Two things to check before attributing any disagreement to P1-LOSS. LYB predictions are pushed onto the cone by `project_to_SPD(x_hat, 1e-6)` **before** the BW distance is taken but not before the Frobenius one, so the two losses are not scoring identical objects and the repair can only help the linear model on the BW side. And in the out-of-sample comparison RFM gets `r=2` while LFM gets `r=1` — not matched on capacity.

**Result, corrected 2026-08-19.** The completed shared-mean run originally stored `mean(FVU[1:r])`, a prefix average. Because the same mean and deterministic rank curves were used at every `r`, the desired curve was recovered exactly by $v_r=r\bar v_r-(r-1)\bar v_{r-1}$. RFM wins 15/15 ranks under BW and 10/15 under Frobenius; the winner reverses at ranks 2, 3, 11, 14, and 15. `run_parent_victory_lap.R` now writes the returned curves directly, and `check_parent_run.py` integrates the result with the forecasting reproduction. No rerun is required.

**Correction to what we assumed.** There are *two* comparisons, not one. In-sample it is RFM vs **LYB** alone. Out-of-sample it is RFM / LFM / LOCF / EWMA(0.94) over the last 36 months, scored four ways: sine-θ subspace distance on leading eigenspaces, squared BW, Frobenius (**not** squared — the arrays are stored inconsistently, see AUDIT §4), and GMV risk error under weights taken from the *previous* month's realised covariance, identically for all four models.

---

## Phase 2 — the falsifiers (unattended)

**Off the critical path.** Nothing here needs external data or supervision. Cost is known: ~2.5 h for the full N-19 grid across BW and AIRM (E5). Fire it overnight whenever a machine is free, and never sequence anything behind it.

The one caveat: if a theorem in P1-LOSS or ID-8 is wrong, the reproduction is beside the point. So run these early — just don't *wait* on them.

### [ ] B2.1 — Wishart and non-Wishart proxy samplers (2 h)

**Do.** `py/rfd/dgp/proxies.py`: draw $S\sim W_m(\Sigma/M, M)$ so that $\mathbb E[S]=\Sigma$, and a non-Wishart proxy with the same conditional mean.

**How.** Use the **Bartlett decomposition** — lower-triangular $A$ with $A_{ii}=\sqrt{\chi^2_{M-i+1}}$ and $A_{ij}\sim N(0,1)$ below the diagonal, then $S=LAA^\top L^\top$ with $L$ the Cholesky factor of $\Sigma/M$. Cost is $O(m^2)$ per draw instead of $O(Mm)$. For the non-Wishart proxy use multivariate-$t$ innovations rescaled so the mean is still exactly $\Sigma$.

**Done when.** Sample mean matches $\Sigma$ to Monte Carlo error at every cell of $m\in\{3,12\}$, $M\in\{21,78,1638\}$, and drawing 40 000 matrices at $m=12,M=1638$ takes seconds.

> **Hard constraint from E4:** at $m=12$, $M=1638$ the full 50 000 draws need **7.9 GB** if materialised at once. The generator must chunk over draws — roughly 157 MB per thousand. This is not a preference; it fails outright rather than merely being slow.

---

### [ ] B2.2 — N-19, the loss-distortion diagnostic (3 h)

**Do.** `experiments/N19_loss_distortion/run.py`. Test the P1-LOSS §3–§4 closed forms against Monte Carlo. The five claims are enumerated in `config/predeclaration.yaml` under `N19.claims` — read them from there, not from here, so there is one source of truth.

**How.** For each $(m,M)$ cell: build $\Sigma$ with a spread spectrum and a random eigenbasis $Q$ (so "diagonal in $\Sigma$'s eigenbasis" is a real test, not an artefact of starting diagonal). Draw the proxy sample, compute each barycentre, rotate back through $Q^\top(\cdot)Q$ and compare against prediction. For AIRM, affine invariance means the answer must be a scalar multiple of $\Sigma$ — recover the scalar as $\operatorname{tr}(\Sigma^{-1}A)/m$, far more stable than any single entry. Read tolerances from `config/predeclaration.yaml`; never hard-code them.

**Done when.** Every cell reports PASS/FAIL against the predeclared tolerance, results are written to `results/final/n19.json`, and **any failure is diagnosed as either a code bug, a test-design error, or a theorem problem — explicitly, in writing.**

> Two warnings, both of which will bite. Claim 2's formula is a **first-order** expansion in $\frac{m+1}{2M}$; at the flagship cell $m=12$, $M=21$ that quantity is about $0.31$, which is not small. Decide what "agreement" means there before you run it. And at $M=1638$ the defects are near zero, so a relative-error test measures nothing but noise. The predeclaration's `known_limitation` block already commits you to reporting the smallest defect each cell could have resolved — honour it.
>
> Still outstanding: the canon quotes 8.8–35.9% for the BW distortion at $m=12$, $M=21$. That range is spectrum-dependent and its provenance is unrecovered. Either find the spectrum that produced it or restate it against one of the three declared spectra.

---

### [ ] B2.3 — N-18a, rank-inflation witnesses (2.5 h)

**Do.** `experiments/N18a_rank_inflation/run.py`. Reproduce ID-8's three analytic constructions as code checks: BW on $\mathrm{SPD}(2)$ with $x=\operatorname{diag}(a,1)$ and $V$ off-diagonal, $a\ne1$; AIRM on $\mathrm{SPD}(2)$ noncommuting; $H^2$. Plus the diagonal-BW rigid control.

**How.** Each is a small deterministic calculation — no seeds. Compute the affine dimension of the image of the score/observation set under the reference change and check it goes $1\to2$ in the three curved cases and stays at $1$ in the flat control.

**Done when.** All three curved cases inflate, the control does not, and the BW defect matches the closed form across the grid — at the tolerance recorded in the predeclaration's 2026-08-17 amendment, **not** the superseded provisional values. Agreement confirms the implementation; disagreement indicts the code. **Neither outcome can change ID-8.**

> Also produce the detectability boundary the predeclaration asks for: the value of $a$ at which the predicted defect falls below the tolerance. That is the difference between "rank inflation is universal in curvature" (a theorem, true everywhere) and "rank inflation is detectable" (an empirical question) — and the second is what P-DRIFT case 3 relies on when it reaches real data.

---

## Phase 4 — the estimator stack

### [ ] B4.1 — locally stationary DGP (3 h)

**Do.** `py/rfd/dgp/lsrfm.py`. Generate $X_{t,n}=\operatorname{Exp}_{\mu_n(u_t)}[\mathcal P A_n f_{t,n}+\delta_{t,n}]$ with a controllable centre path, factor rank, lag structure and noise.

**How.** Parameterise the centre path so you can dial drift from zero to large, and the factor from zero to large, independently — you need all four corners for N-18. The canonical family is \(\mu_\nu(u)=\operatorname{Exp}_{\mu_0}\{\nu g(u)V\}\): expose \(\nu\), \(g\), \(V\), and orientation relative to the loading span, while also returning intrinsic path length and energy. Make the geometry a plug-in argument so the same DGP runs on BW, AIRM and the sphere.

**Done when.** With drift off and factor off, the sample Fréchet mean is constant to Monte Carlo error. With factor off and drift on, it tracks $\mu_n(u)$. Both checks pass on all three geometries.

> `random_spd_family(rng, m, cond, delta, n, shape)` in `py/rfd/dgp/spd.py` already separates conditioning from dispersion. Reuse that design here: any DGP whose knobs are confounded produces curves you cannot read.

---

### [ ] B4.2 — three-scale centre estimator (3 h)

**Do.** `py/rfd/estimators/centre.py`. The positive three-scale kernel estimator with Richardson combination, $c=(1,1/2,1/4)$, $\lambda=(1/3,-2,8/3)$.

**How.** Each stage barycentre uses **positive** weights, so no signed-existence issue arises there. The signed $\lambda$ act only afterwards, in the tangent space, via Exp/Log Richardson. Kernels and first derivatives vanish at support endpoints. Forward/backward blend on a fixed-width interior overlap.

**Done when.** On the B4.1 DGP with known $\mu_n(u)$, the error tracks $b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}$ across a bandwidth sweep, and the fitted slope of $\log(\text{error})$ against $\log n$ at $b_n=n^{-1/7}$ is near $-3/7$.

> Watch out: this is where the signed Richardson step can push the reconstruction out of the full-rank cone. Instrument it — count how often the admissibility fallback fires, as a function of condition number. That count is a result, not a nuisance. See queue item L-8.

---

### [ ] B4.3 — polygonal frame and transport (3 h)

**Do.** `py/rfd/estimators/frame.py`. Join estimated mean vertices by geodesic chords, parallel-transport along the polygon, $M_n\asymp\ell_n^{-2/3}$ cells.

**Done when.** With a known constant centre the frame is the identity. With a known moving centre on a flat, transport around a closed loop returns the identity — and on a curved one it doesn't, by an amount you can compare to the curvature. `airm_parallel_transport` in `airm.py` is already there.

---

### [ ] B4.4 — lag operator, loading space, selectors (3 h)

**Do.** `py/rfd/estimators/lag.py`. $\widehat\Gamma_n(h)$, $\widehat{\mathbb L}_n=\sum_h\widehat\Gamma\widehat\Gamma^*$, the leading $r$-space, and both selectors — threshold and ridged ratio — plus the raw ratio as a negative control.

**Done when.** On a DGP with known $r$: $\widehat\lambda_{r+1}\le d_n^2$ holds empirically, both proved selectors recover $r$, and you have reproduced the counterexample $\widehat{\mathbb L}=\operatorname{diag}(1,d_n^2,0)$ where the raw ratio picks 2. That last one is the P-RATIO correction made concrete.

---

### [ ] B4.5 — N-01, the bounded-energy baseline (2.5 h)

**Do.** `experiments/N01_baseline/run.py`. Fixed $R,h_0,r,\Delta>0$; increasing $n,p$.

**Done when.** $d_n=O_p(n^{-1/2}+\ell_n)$, loading error $O_p(d_n/\Delta)$, null eigenvalues $O_p(d_n^2)$ — all three confirmed on a log–log plot with fitted slopes, against the **actual empirical** $R_n, A_{2,n}, \Delta_n$, never against dimension as a proxy.

---

## Phase 5 — after the stack works

Sequenced but not detailed yet; write the detail when you get here, because Phases 1–4 will change your view of what these need.

- [ ] **B5.1** N-18 — the drift/factor identification diagnostic. Runs only after a clean B3.2. Validates the implementation against ID-4/ID-5 and P-DRIFT. It **cannot** determine empirical dominance; that's ID-6.
- [ ] **B5.2** N-08, N-11, N-12 — the failure boundaries. Zero signal, rank-changing BW attack, signed Richardson collapse. These are meant to break; instrument them.
- [ ] **B5.3** N-09, N-10, N-15 — the BW branch.
- [ ] **B5.4** N-16, N-17 — FRAME-2P-U and its negative controls. New code, no reuse from the parent.
- [ ] **B5.5** The forecast comparison. Frobenius and QLIKE as primary, geodesic losses reported only with the P1-LOSS §4 recalibration and the induced target stated. Diebold–Mariano or Giacomini–White for whether any difference is real. **R for this** — `multDM` and `forecast` have no clean Python equivalent.
- [ ] **B5.6 / N-18c** The where-it-helps map. Sweep the canonical \(\nu\)-family and report the complete fixed-minus-moving risk curve, not one cherry-picked crossing. Structural and forecast risks are separate; Frobenius and QLIKE are the primary forecast losses. Include the placebo — fit both on a *provably* fixed-centre DGP and check whether the moving-centre model still wins. If it does, you've learned it is flexibility rather than structure. The positive control matters more: without it, a null on real data is uninterpretable. Test clean quadratic, linear-cross-term, aligned, orthogonal, partial and curved regimes; treat \(n^{-3/14}\) only as the clean short-memory candidate.

---

## Diagnostics already run

Engineering measurements, not paper content. Each writes `.md` + `.csv` to `results/final/`; `python sandbox/run_all.py` re-runs the lot in ~2 min and `sandbox/look.py` redraws the plots into the gitignored `sandbox/plots/`.

| | what it decided |
|---|---|
| `calibrate_spd.py` | `safety=10`, and which amplification each identity needs |
| **E4** `e4_bw_cost.py` | N-19 affordable; batching is linear in N; the 7.9 GB memory constraint |
| **E2** `e2_boundary.py` | working range ends at κ=1e6; found the NaN guard hole |
| **E1** `e1_convergence_surface.py` | cost follows dispersion, not conditioning |
| **E3** `e3_tol_accuracy.py` | `tol=1e-12` is the knee; tighter is pure waste |
| **E5** `e5_airm_cost.py` | AIRM/BW ratio 2.05× at m=12, 4.78× at m=3 — replaced a guess |
| **E6** `e6_airm_convergence.py` | `step=1.0` wins 90/90; AIRM cost is blind to κ and shape |
| **E7** `e7_geometry_divergence.py` | divergence ≈ c(m)·δ — the one with paper content in it |
| **D1–D3** `diag_risk_gap.py` | **refuted** amplification as the cause of the risk gap; shrinkage made it worse, so theirs is the more ill-conditioned Σ |
| **D4** `diag_day_count.py` | ~20 effective trading days per month reconciles bulk *and* tail at once — the finding that closed B3.4a |

**E7 is the only one that is embryonic paper material.** It is also the only one currently waiting on something: the real panel's δ (B3.4a). And note the caution in its docstring — divergence of *centres* is not divergence of *rankings*, which is the stronger claim `highest_value_check` actually tests.

---

## Standing rules

1. **Predeclare, then run.** Tolerance and grid go into `config/` before the script executes.
2. **No silent repairs.** A divergence from the parent gets logged in `reference/AUDIT.md`. A divergence from your own theorem gets the theorem marked UNDER AUDIT in the ledger.
3. **Tables come from `results/final/`.** Never typed by hand, never copied out of a terminal.
4. **Seeds are lists, not a base seed.** Independent lists for train, validation and test.
5. **Numerical success proves nothing analytical.** It can only ever falsify.
6. **`sandbox/` is disposable.** If you'd be upset to lose it, it belongs in `py/rfd/` with a test.
7. **Tolerances are measured, not typed.** Every tolerance traces to a number from this machine's BLAS. A plausible-looking power of ten is not a tolerance.
8. **Test the statistic the bound is about.** Backward stability bounds a norm, so test a norm. An elementwise relative test on a matrix fails on small entries for reasons that carry no information.
9. **A test that passes by construction is not a test.** If the quantity you assert is the one the loop terminates on, or if the algebra cancels before your parameter enters, you have written a tautology. Find the independent check — the closed form, the invariance, the objective.
10. **State the slack.** When a tolerance is deliberately loose, or a grid is capped, or a term is omitted from a cost model, say so where the result is reported. Silent truncation reads as coverage.
