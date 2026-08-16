---
type: build-plan
title: BUILD — the ordered engineering plan
status: active
audience: me, only
created: 2026-08-16
---

# BUILD

The theory notes live in `notes/`. This file is the other thing: **what to actually type, in what order.**

## How to use this

- Work top to bottom. Tasks are sized to **one sitting of 2–3 hours**. On a break day, close the laptop; every task ends somewhere you can commit and walk away.
- Each task is **Do / How / Done when**. The *Done when* is the contract — if it isn't met the task isn't finished, and you don't move on by feel.
- Tick as you go. `[ ]` → `[x]`, and put the commit hash next to it.
- **Anything that disagrees with a theorem gets written down, not tuned away.** That's the whole reason the numbers exist.

**The one rule for the repo:** `sandbox/` may import from `py/rfd/`. Nothing ever imports from `sandbox/`. When scratch code proves useful, promote it into the package and give it a test.

---

## Phase 0 — scaffold

### [ ] B0.1 — repo shape (1 h)

**Do.** Rename `Ideas/` → `notes/`, then build the tree around it.

```
riemannian-factor-dynamics/
├── BUILD.md                  ← this file
├── notes/                    ← all .md (was Ideas/)
│   ├── canonical/            Paper 1, Analytical reconstruction, OPEN OBLIGATIONS
│   ├── boundaries/           P1-ID, P1-LOSS, HE, BW-*, FRAME-2P-U
│   ├── literature/           Literature review, References audit
│   └── archive/              proof provenance — read-only in practice
├── reference/                ← frozen clone of the parent's R repo. NEVER EDIT.
├── py/
│   ├── rfd/                  ← the importable package
│   │   ├── spd/              geometry primitives
│   │   ├── dgp/              data-generating processes
│   │   ├── estimators/       centre, frame, lag operator, selectors
│   │   └── eval/             losses, proxies, forecast comparison
│   └── tests/
├── R/                        ← R functions YOU write (not the parent's)
├── experiments/              ← one dir per N-row; run.py or run.R, doesn't matter
│   └── N19_loss_distortion/
├── config/                   ← predeclared grids, seeds, tolerances (yaml)
├── results/
│   ├── raw/  intermediate/  final/
└── sandbox/                  ← notebooks, scratch, throwaway
```

**How.** `git mv Ideas notes`, then `mkdir -p`. Add a `.gitignore` covering `results/raw/`, `results/intermediate/`, `sandbox/**/*.ipynb_checkpoints`, `__pycache__`, `.Rhistory`, `.RData`. **Commit `results/final/` and `config/` — those are the paper.**

**Done when.** The tree exists, `git status` is clean, and the staged deletions currently sitting in `Ideas/Archived/` have been resolved deliberately one way or the other.

---

### [ ] B0.2 — environments, both languages, frozen (2 h)

**Do.** A reproducible Python env and a reproducible R env, with versions recorded.

**How.** Python: `venv` + `requirements.txt` pinned with `==`. You need `numpy scipy pandas pyyaml matplotlib pytest`. R: `renv::init()` inside `reference/`, which snapshots exactly what the parent's scripts pull. Write `env/VERSIONS.md` by hand recording OS, Python version, R version, BLAS backend. **The BLAS matters** — matrix square roots differ in the last bits between OpenBLAS and MKL and you will chase that ghost otherwise.

**Done when.** `pytest` runs (zero tests, exits clean), `renv.lock` exists, `VERSIONS.md` is filled in.

---

### [ ] B0.3 — the predeclaration file (2 h)

**Do.** Write `config/predeclaration.yaml` before any experiment runs. This is the thing that makes the numbers evidence rather than decoration.

**How.** Fields: for each planned N-row — Monte Carlo size, RNG seeds (a fixed list, not a base seed), tolerance for a PASS, and *what result would count as disagreement with the theorem*. Plus a global `kill_criteria` block: a numerical contradiction downgrades the affected theorem in the ledger to **UNDER AUDIT**, and the fix is not to widen the tolerance.

**Done when.** The file exists, is committed, and contains at minimum the N-19 and N-18a entries. Tolerances chosen **before** you see any output.

> Watch out: it is very tempting to set a tolerance as a relative error. For quantities that are near zero (the BW defect at large $M$) relative error is dominated by Monte Carlo noise and the test tells you nothing. Think about whether each check is testing the *value* or the *order*, and say which in the file.

---

## Phase 1 — SPD geometry primitives

This is the reusable core. Everything downstream imports it. Build it once, properly.

### [ ] B1.1 — matrix functions (2 h)

**Do.** `py/rfd/spd/linalg.py`: `sym`, `spd_sqrt`, `spd_invsqrt`, `spd_log`, `spd_exp`, `geometric_mean(A, B)`.

**How.** All of them via `numpy.linalg.eigh` on the symmetrised input, then act on eigenvalues — **not** `scipy.linalg.sqrtm`/`logm`, which are general-purpose, slower, and return complex dtypes you'll have to keep stripping. Clip eigenvalues at a floor before `sqrt`/`log`.

**Done when.** Round-trip tests pass: `spd_exp(spd_log(A)) ≈ A` and `spd_sqrt(A) @ spd_sqrt(A) ≈ A` to `1e-12` on 100 random SPD matrices at $m \in \{2,3,12\}$. Add a test with condition number $10^8$ and record what precision you actually get — you'll want that number later when N-12 drives the reconstruction toward rank loss.

---

### [ ] B1.2 — BW distance and barycentre (3 h)

**Do.** `py/rfd/spd/bw.py`: `bw_dist2(A,B)`, `bw_barycentre(S, ...)`, `bw_log`, `bw_exp`.

**How.** Distance is $\operatorname{tr}A+\operatorname{tr}B-2\operatorname{tr}(A^{1/2}BA^{1/2})^{1/2}$. For the barycentre use the Álvarez-Esteban fixed point,
$$X \leftarrow X^{-1/2}\Big(\tfrac1N\sum_i (X^{1/2}S_iX^{1/2})^{1/2}\Big)^2 X^{-1/2},$$
initialised at the arithmetic mean. It's provably convergent on the full-rank cone. Return the iteration count and final residual, don't just return the matrix — you'll want convergence diagnostics in N-12.

**Done when.** For $m=2$ it matches the closed form on commuting pairs; the fixed point satisfies the stationarity equation $X=\frac1N\sum(X^{1/2}S_iX^{1/2})^{1/2}$ to `1e-10`; and it converges in under 50 iterations for well-conditioned inputs.

> Watch out: the fixed point slows down badly as the smallest eigenvalue approaches zero. Record the iteration count as a function of condition number now — that curve *is* your empirical picture of the BW-SHRINKING-MARGIN regime, and it's cheap to get.

---

### [ ] B1.3 — AIRM distance and Karcher mean (2 h)

**Do.** `py/rfd/spd/airm.py`: `airm_dist2`, `airm_barycentre`, `airm_log`, `airm_exp`, `parallel_transport`.

**How.** Distance $\|\log(A^{-1/2}BA^{-1/2})\|_F^2$. Karcher mean by Riemannian gradient descent: iterate $X \leftarrow X^{1/2}\exp\!\big(\frac1N\sum\log(X^{-1/2}S_iX^{-1/2})\big)X^{1/2}$, stop on gradient norm.

**Done when.** Affine invariance verified numerically: `airm_barycentre(A S A')` equals `A airm_barycentre(S) A'` to `1e-10` for random invertible `A`. That single test catches most implementation errors in one shot.

---

### [ ] B1.4 — log-Euclidean, Frobenius, and the loss module (1.5 h)

**Do.** `py/rfd/eval/losses.py`: squared Frobenius, multivariate QLIKE, squared BW, squared AIRM, squared log-Euclidean. Plus `logeuclid_barycentre`.

**How.** QLIKE for matrices: $\operatorname{tr}(H^{-1}S)-\log\det(H^{-1}S)-m$. Use `slogdet`, never `log(det(...))`.

**Done when.** Every loss is zero iff its arguments are equal, and QLIKE is finite and positive on 1000 random pairs.

---

## Phase 2 — the first falsifier

Nothing here needs external data. This is the cheapest independent check on the canon that exists.

### [ ] B2.1 — Wishart and non-Wishart proxy samplers (2 h)

**Do.** `py/rfd/dgp/proxies.py`: draw $S\sim W_m(\Sigma/M, M)$ so that $\mathbb E[S]=\Sigma$, and a non-Wishart proxy with the same conditional mean.

**How.** Use the **Bartlett decomposition** — lower-triangular $A$ with $A_{ii}=\sqrt{\chi^2_{M-i+1}}$ and $A_{ij}\sim N(0,1)$ below the diagonal, then $S=LAA^\top L^\top$ with $L$ the Cholesky factor of $\Sigma/M$. Cost is $O(m^2)$ per draw instead of $O(Mm)$; the naive route is unusable at $M=1638$. For the non-Wishart proxy use multivariate-$t$ innovations rescaled so the mean is still exactly $\Sigma$.

**Done when.** Sample mean matches $\Sigma$ to Monte Carlo error at every cell of $m\in\{3,12\}$, $M\in\{21,78,1638\}$, and drawing 40 000 matrices at $m=12,M=1638$ takes seconds, not minutes.

---

### [ ] B2.2 — N-19, the loss-distortion diagnostic (3 h)

**Do.** `experiments/N19_loss_distortion/run.py`. Test the P1-LOSS §3–§4 closed forms against Monte Carlo.

The five claims:

1. the **Frobenius** barycentre of the proxy law is $\Sigma$ — no distortion;
2. the **AIRM** barycentre is $c\Sigma$ with $c=1-\frac{m+1}{2M}$;
3. the **BW** barycentre is diagonal in $\Sigma$'s eigenbasis with per-eigenvalue defect
   $$\frac{|B_{ii}|}{\lambda_i}=\frac1M\Big[\tfrac14+\sum_k\frac{\lambda_k^2}{(\lambda_i+\lambda_k)^2}\Big];$$
4. **QLIKE** is minimised at $\Sigma$;
5. a **non-Wishart** proxy rotates the induced BW eigenbasis; a Wishart one does not.

**How.** For each $(m,M)$ cell: build $\Sigma$ with a spread spectrum and a random eigenbasis $Q$ (so that "diagonal in $\Sigma$'s eigenbasis" is a real test, not an artefact of starting diagonal). Draw the proxy sample, compute each barycentre, rotate back through $Q^\top(\cdot)Q$ and compare against prediction. For AIRM, affine invariance means the answer must be a scalar multiple of $\Sigma$ — recover the scalar as $\operatorname{tr}(\Sigma^{-1}A)/m$, which is a much more stable estimate than any single entry. Read tolerances from `config/predeclaration.yaml`; do not hard-code them in the script.

**Done when.** Every cell reports PASS/FAIL against the predeclared tolerance, results are written to `results/final/n19.json`, and **any failure is diagnosed as either a code bug, a test-design error, or a theorem problem — explicitly, in writing.**

> Two warnings, because both will bite. First, claim 2's formula is a **first-order** expansion in $\frac{m+1}{2M}$. At the flagship cell $m=12$, $M=21$ that quantity is about $0.31$, which is not small — think about what "agreement" should mean there before you run it, and check what your canon's stated percentage actually corresponds to. Second, at $M=1638$ the defects are near zero and a relative-error test measures nothing but noise. Decide per cell whether you're testing the value or the order.

---

### [ ] B2.3 — N-18a, rank-inflation witnesses (2.5 h)

**Do.** `experiments/N18a_rank_inflation/run.py`. Reproduce ID-8's three analytic constructions as code checks: BW on $\mathrm{SPD}(2)$ with $x=\operatorname{diag}(a,1)$ and $V$ off-diagonal, $a\ne1$; AIRM on $\mathrm{SPD}(2)$ noncommuting; $H^2$. Plus the diagonal-BW rigid control.

**How.** Each is a small deterministic calculation, not a simulation — no seeds needed. Compute the affine dimension of the image of the score/observation set under the reference change and check it goes $1\to2$ in the three curved cases and stays at $1$ in the flat control. For the BW case, check the defect against the closed form across a grid of $a\ne1$ and $0<|b|<1+a$.

**Done when.** All three curved cases inflate, the control does not, and the BW defect matches the closed form to `1e-10` across the whole grid. Agreement confirms the implementation; disagreement indicts the code. **Neither outcome can change ID-8** — it's proved analytically. This is a code check.

---

## Phase 3 — the parent, in R

Independent of Phases 1–2. Good work for a day when you want something mechanical.

### [ ] B3.1 — clone and freeze (1.5 h)

**Do.** Clone `github.com/shuochieh/Riemannian_factor_model` into `reference/`. Snapshot the environment. Read every script before running any.

**How.** `renv::init()`, then `renv::snapshot()`. Write `reference/AUDIT.md` as you read: what each of the 15 scripts does, what it reads, what it writes. **Do not fix anything you find.** Log it.

**Done when.** `AUDIT.md` maps all 15 scripts, and `renv.lock` is committed.

---

### [ ] B3.2 — run the simulations (3 h)

**Do.** `BWS_simulation.R`, `Sphere_simulation.R`, `simulation_main.R`, `sim_do.R`, `sim_summary.R`. These need **no external data** — they run today.

**How.** Run unchanged. Capture stdout to `results/raw/n00/`. Compare against the paper's tables — especially Table 2, the raw-eigenvalue-ratio selection rates (above 80% at $n=100$, ~100% at $n=200$).

**Done when.** Their simulation outputs are reproduced within Monte Carlo error, or every divergence is logged in `AUDIT.md` with a hypothesis. This is the half of N-00 that isn't blocked on Huang's reply.

---

### [ ] B3.3 — notation map (2 h)

**Do.** `notes/canonical/notation-map.md`. Every object in their code ↔ every object in your canon.

**How.** A table: their symbol, their file and line, your symbol, your canonical note. Cover at minimum $\kappa$ vs your $s_n$ and $\Delta_n$, their $\lambda_r$ vs your $\lambda_r(\mathbb L_n)$, their loading estimator vs your $\mathcal S_{X,n}$, and their raw ratio (Eq. 5) vs your threshold/ridged selectors.

**Done when.** Every symbol in their `main_func.R` has a row. **Notation-only rewriting must not change any hypothesis, norm, target or rate** — if you find yourself wanting to, that's a finding, log it.

---

### [ ] B3.4 — APP-FIN, when the data question resolves (3 h, BLOCKED)

**Do.** Rebuild the 12-stock monthly realised-covariance panel, then run `sp500_analysis.R` and `sp500_reproduce.R`.

**How.** Blocked on Huang's reply for the ticker list and the RC construction. If no reply within two weeks, use the documented fallback panel and say so in the paper. **This is where R genuinely earns its place** — the `highfrequency` package for realised covariance construction, and `xts`/`quantmod` for the price handling.

**Done when.** The panel exists, its construction is fully documented, and every divergence from the paper's reported numbers is logged rather than repaired. Expect *approximate* reproduction only — Yahoo back-adjusts for splits and dividends, so a 2026 rebuild differs from theirs by construction. Decide the acceptable divergence threshold **before** you look.

> The single highest-value thing in this task isn't the reproduction. It's finding out which loss they used to rank RFM against LFM/LOCF/EWMA. If it's squared Bures–Wasserstein, your P1-LOSS result applies directly to their headline comparison. Check that first, before anything else in the file runs.

---

## Phase 4 — the estimator stack

### [ ] B4.1 — locally stationary DGP (3 h)

**Do.** `py/rfd/dgp/lsrfm.py`. Generate $X_{t,n}=\operatorname{Exp}_{\mu_n(u_t)}[\mathcal P A_n f_{t,n}+\delta_{t,n}]$ with a controllable centre path, factor rank, lag structure and noise.

**How.** Parameterise the centre path so you can dial drift from zero to large, and the factor from zero to large, independently — you need all four corners for N-18. Make the geometry a plug-in argument so the same DGP runs on BW, AIRM and the sphere.

**Done when.** With drift off and factor off, the sample Fréchet mean is constant to Monte Carlo error. With factor off and drift on, it tracks $\mu_n(u)$. Both checks pass on all three geometries.

---

### [ ] B4.2 — three-scale centre estimator (3 h)

**Do.** `py/rfd/estimators/centre.py`. The positive three-scale kernel estimator with Richardson combination, $c=(1,1/2,1/4)$, $\lambda=(1/3,-2,8/3)$.

**How.** Each stage barycentre uses **positive** weights, so no signed-existence issue arises there. The signed $\lambda$ act only afterwards, in the tangent space, via Exp/Log Richardson. Kernels and first derivatives vanish at support endpoints. Forward/backward blend on a fixed-width interior overlap.

**Done when.** On the B4.1 DGP with known $\mu_n(u)$, the error tracks $b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}$ across a bandwidth sweep, and the fitted slope of $\log(\text{error})$ against $\log n$ at $b_n=n^{-1/7}$ is near $-3/7$.

> Watch out: this is where the signed Richardson step can push the reconstruction out of the full-rank cone. Instrument it — count how often the admissibility fallback fires, as a function of condition number. That count is a result, not a nuisance. See queue item L-8.

---

### [ ] B4.3 — polygonal frame and transport (3 h)

**Do.** `py/rfd/estimators/frame.py`. Join estimated mean vertices by geodesic chords, parallel-transport along the polygon, $M_n\asymp\ell_n^{-2/3}$ cells.

**Done when.** With a known constant centre the frame is the identity to `1e-10`. With a known moving centre on a flat, transport around a closed loop returns the identity — and on a curved one it doesn't, by an amount you can compare to the curvature.

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
- [ ] **B5.6** The where-it-helps map. The actual contribution: the region where a moving centre pays, the region where it doesn't, and the boundary. Includes the placebo — fit both on a *provably* fixed-centre DGP and check whether the moving-centre model still wins. If it does, you've learned it's flexibility rather than structure, and that's a real finding.

---

## Standing rules

1. **Predeclare, then run.** Tolerance and grid go into `config/` before the script executes.
2. **No silent repairs.** A divergence from the parent gets logged in `reference/AUDIT.md`. A divergence from your own theorem gets the theorem marked UNDER AUDIT in the ledger.
3. **Tables come from `results/final/`.** Never typed by hand, never copied out of a terminal.
4. **Seeds are lists, not a base seed.** Independent lists for train, validation and test.
5. **Numerical success proves nothing analytical.** It can only ever falsify.
6. **`sandbox/` is disposable.** If you'd be upset to lose it, it belongs in `py/rfd/` with a test.
