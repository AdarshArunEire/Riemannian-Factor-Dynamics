# reference/ — provenance

The parent's code. **Not committed** — see `reference/.gitignore`.

| | |
|---|---|
| upstream | `https://github.com/shuochieh/Riemannian_factor_model` |
| commit | `c07d49c257d489e00b7e15bdd432954946a2a694` |
| commit date | 2026-04-30 21:10 -0400, message "update" |
| obtained | 2026-08-18, as the `main` ZIP |
| verified | all 14 file MD5s match a `git clone` of the above commit |
| licence | **none** |

## Why it is gitignored rather than vendored

There is no LICENSE file in the upstream repo. Absent one, the default is all
rights reserved — "it is on GitHub" is not a licence. Redistributing it inside
this repo would be a problem this project does not need, so only this file and
`AUDIT.md` are tracked.

To reconstitute:

    git clone https://github.com/shuochieh/Riemannian_factor_model.git reference/
    cd reference && git checkout c07d49c257d489e00b7e15bdd432954946a2a694

Pinning matters more than usual: Huang has said he intends to tidy the repo
after his travel. Everything in `AUDIT.md` describes the commit above.

## One directory added, no file modified

`sp500_reproduce.R:12` and `:138` read `./sp500_covariance/VIXCLS.csv` and
`./sp500_covariance/sp500_12bySector.RData`. **That directory is not in the
upstream repo**, and nothing in the repo builds it: the realised-covariance
panel is an *input* to their code, not an output of it. The gap between
`stock_price_extract.ipynb` (which stops at prices) and `sp500_reproduce.R`
(which starts at covariances) is exactly the step Huang supplied by email.

Reproduction therefore requires creating that directory. It contains only
files we generate:

    sp500_covariance/panel_flat.csv           experiments/export_for_parent.py
    sp500_covariance/tickers.csv              experiments/export_for_parent.py
    sp500_covariance/VIXCLS.csv               FRED VIXCLS, via the same script
    sp500_covariance/sp500_12bySector.RData   R/make_panel_rdata.R

**No upstream file is edited, at any point.** `R/run_parent_reproduce.R`
sources `sp500_reproduce.R` verbatim and reads what it leaves behind. Delete
`sp500_covariance/` and the clone is byte-identical to the pin above — the
MD5 check in this file still applies unchanged.

## Files present

12 R scripts and 2 Jupyter notebooks. **Not 15** — BUILD.md said 15 before
anyone counted.

    BWS_simulation.R  BWS_util.R  Sim_summary_sphere.R  Sphere_simulation.R
    main_func.R  sim_do.R  sim_summary.R  simulation.R  simulation_main.R
    sp500_analysis.R  sp500_reproduce.R  sphere_util.R
    Crawling wikipedia page table.ipynb   stock_price_extract.ipynb
