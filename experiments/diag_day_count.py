"""D4 -- how many trading days per month did they actually use?

Where this came from. check_panel_vs_parent.py found BW and Frobenius matching
to 0.7-2.4% while the GMV risk error missed by 15-28%, systematically low.
diag_risk_gap.py then RULED OUT the obvious explanation: a 2.4% panel
perturbation moves the risk error by only +-2-5%, so it is not simply an
amplified version of the disagreement we already have. And shrinking the
weights made the gap worse, which says their Sigma_t is MORE ill-conditioned
than ours, not less.

The structural reason those two groups can disagree:

    Frobenius and BW are dominated by the LARGEST eigenvalues -- the bulk.
    The GMV risk error runs through 1 / (1' Sigma^-1 1), which is dominated by
    the SMALLEST eigenvalues -- the tail.

Two panels can agree at the top of the spectrum and differ at the bottom. And
the bottom is exactly what the number of observations per month controls: at
m=12 with M~21 we sit near the Marchenko-Pastur edge, where the small
eigenvalues are mostly estimation noise whose size is set by m/M.

So: rebuild the panel using K days per month and sweep K. If some K below our
actual count lands the risk errors on 2.61 and 1.45 WHILE leaving BW and
Frobenius near 2.66 and 12.51, that is the answer, and it names their effective
M. If no such K exists, day count is not the mechanism and the next suspect is
the return construction itself.

Days are dropped EVENLY SPACED rather than from the end, because the realistic
mechanism is scattered: their notebook downloads all ~500 S&P constituents and
selects twelve later, so dropping rows where any stock in the full universe had
a missing price removes days from throughout the month.

    python experiments/diag_day_count.py

Needs the daily returns, which build_rc_panel.py now stores in the .npz.
Re-run that first if your panel predates this diagnostic.
"""

from _common import header, write, ROOT

import sys

import numpy as np

from rfd.spd.bw import bw_dist2

RAW = ROOT / "results" / "raw" / "rc_panel_adjusted.npz"
N_MONTHS = 240
SCALE = 10000.0
TEST_SIZE = 36
LAMBDA = 0.94
# K must exceed m: np.cov uses ddof=1, so rank <= K-1 and a 12x12 covariance
# is singular for K <= 12. That is a fact about THEIR pipeline too -- their
# solve(truth_lag) would fail outright -- so their effective M is at least 13.
# Found by dry run: K=10 raises "Eigenvalues did not converge" inside bw_dist2.
KS = [13, 14, 15, 16, 17, 18, 20, None]     # None = every available day

PUBLISHED = {
    ("LOCF", "BW"): 2.66, ("EWMA", "BW"): 2.36,
    ("LOCF", "Frob"): 12.51, ("EWMA", "Frob"): 11.97,
    ("LOCF", "risk"): 2.61, ("EWMA", "risk"): 1.45,
}
BULK = [k for k in PUBLISHED if k[1] in ("BW", "Frob")]
TAIL = [k for k in PUBLISHED if k[1] == "risk"]


def build(rets, ret_month, months, k):
    """Monthly covariance from k evenly spaced days (or all if k is None)."""
    panel = []
    for mo in months:
        r = rets[ret_month == mo]
        if k is not None and r.shape[0] > k:
            idx = np.unique(np.linspace(0, r.shape[0] - 1, k).round().astype(int))
            r = r[idx]
        panel.append(np.cov(r, rowvar=False) * SCALE)
    return np.stack(panel)


def ewma_series(panel, lam=LAMBDA):
    res = np.zeros_like(panel)
    sigma = np.zeros(panel.shape[1:])
    for i in range(1, panel.shape[0]):
        sigma = lam * sigma + (1.0 - lam) * panel[i - 1]
        res[i] = sigma
    return res


def score(panel):
    n, q = panel.shape[0], panel.shape[-1]
    ewma = ewma_series(panel)
    models = {"LOCF": lambda t: panel[t - 1], "EWMA": lambda t: ewma[t]}
    acc = {k: {"BW": [], "Frob": [], "risk": []} for k in models}
    for t in range(n - TEST_SIZE, n):
        truth, lag = panel[t], panel[t - 1]
        w = np.linalg.solve(lag, np.ones(q))
        w = w / w.sum()
        true_risk = float(w @ truth @ w)
        for name, fn in models.items():
            hat = fn(t)
            acc[name]["BW"].append(np.sqrt(float(bw_dist2(hat, truth))))
            acc[name]["Frob"].append(float(np.linalg.norm(hat - truth, "fro")))
            acc[name]["risk"].append(abs(float(w @ hat @ w) - true_risk))
    return {(k, s): float(np.mean(v)) for k, d in acc.items() for s, v in d.items()}


def main():
    if not RAW.exists():
        sys.exit(f"no {RAW} -- run experiments/build_rc_panel.py first")
    z = np.load(RAW, allow_pickle=True)
    if "rets" not in z:
        sys.exit("this panel predates the daily-return store -- "
                 "re-run experiments/build_rc_panel.py")

    rets, ret_month = z["rets"], z["ret_month"]
    months = [str(m) for m in z["months"]][:N_MONTHS]

    rows = []
    print(f"{'K':>5} {'days':>6} {'kappa med':>10} {'lam_min med':>11} | "
          f"{'LOCF BW':>9} {'LOCF Frob':>10} {'LOCF risk':>10} {'EWMA risk':>10} | "
          f"{'bulk':>6} {'tail':>6}")
    for k in KS:
        panel = build(rets, ret_month, months, k)
        eig0 = np.linalg.eigvalsh(panel)[:, 0]
        if (eig0 <= 0).any():
            n_bad = int((eig0 <= 0).sum())
            print(f"{str(k):>5}  SKIPPED -- {n_bad} months singular "
                  f"(rank <= K-1 < m); their solve() would fail here too",
                  flush=True)
            rows.append((str(k), "", "SINGULAR", "", *[""] * len(PUBLISHED), "", ""))
            continue
        used = np.array([(rets[ret_month == mo].shape[0] if k is None
                          else min(k, rets[ret_month == mo].shape[0]))
                         for mo in months])
        eig = np.linalg.eigvalsh(panel)
        s = score(panel)
        gap = {key: abs(s[key] - PUBLISHED[key]) / PUBLISHED[key] for key in PUBLISHED}
        bulk = max(gap[key] for key in BULK)
        tail = max(gap[key] for key in TAIL)

        label = "all" if k is None else str(k)
        print(f"{label:>5} {used.mean():>6.1f} {np.median(eig[:, -1] / eig[:, 0]):>10.3e} "
              f"{np.median(eig[:, 0]):>11.3e} | "
              f"{s[('LOCF','BW')]:>9.3f} {s[('LOCF','Frob')]:>10.3f} "
              f"{s[('LOCF','risk')]:>10.3f} {s[('EWMA','risk')]:>10.3f} | "
              f"{bulk:>5.1%} {tail:>6.1%}", flush=True)

        rows.append((label, f"{used.mean():.1f}",
                     f"{np.median(eig[:, -1] / eig[:, 0]):.3e}",
                     f"{np.median(eig[:, 0]):.3e}",
                     *[f"{s[key]:.3f}" for key in PUBLISHED],
                     f"{bulk:.1%}", f"{tail:.1%}"))

    ok = [r for r in rows if r[-1].endswith("%")]
    if not ok:
        sys.exit("every K was singular -- nothing to compare")
    best_tail = min(ok, key=lambda r: float(r[-1].rstrip("%")))
    best_bulk = min(ok, key=lambda r: float(r[-2].rstrip("%")))
    print(f"\n  best bulk agreement at K = {best_bulk[0]} ({best_bulk[-2]})")
    print(f"  best tail agreement at K = {best_tail[0]} ({best_tail[-1]})")
    if best_tail[0] == best_bulk[0]:
        print("  -> SAME K explains both. Day count is the mechanism.")
    else:
        print("  -> different K. Day count alone does not explain it; look at "
              "the return construction next.")

    lines = header("D4 -- day-count sweep",
                   extra=["published targets: BW 2.66/2.36, Frobenius 12.51/11.97, "
                          "risk 2.61/1.45",
                          "days removed evenly spaced, not from the end"])
    lines += [
        "`bulk` is the worst gap among the BW and Frobenius statistics -- the ones",
        "dominated by the LARGEST eigenvalues. `tail` is the worst gap among the",
        "GMV risk errors, which run through 1/(1' Sigma^-1 1) and are dominated by",
        "the SMALLEST eigenvalues. They are different claims about the panel and",
        "the whole point of this sweep is that they may be minimised at different K.",
        "",
        "If one K minimises both, day count is the mechanism and that K is their",
        "effective M. If bulk is flat while tail moves sharply, the day count is",
        "changing only the spectrum tail -- which is still informative, but means",
        "our bulk agreement was never evidence about the tail.",
        "",
        "K cannot go below 13: np.cov uses ddof=1, so the rank is at most K-1 and",
        "a 12x12 covariance is singular at K <= 12. Their own solve(truth_lag)",
        "would fail there, so their effective M is at least 13 whatever else is",
        "true. That bounds the search from below before any number is computed.",
        "",
        "If no K brings the tail close, day count is not it. The next suspects, in",
        "order: whether they demean within the month; whether returns are computed",
        "across month boundaries or reset each month; and whether any winsorising",
        "or missing-data fill was applied before the covariance.",
    ]
    write("diag_day_count", lines,
          ["K", "mean_days", "kappa_median", "lambda_min_median",
           *[f"{a}_{b}" for a, b in PUBLISHED], "worst_bulk_gap", "worst_tail_gap"],
          rows)


if __name__ == "__main__":
    main()
