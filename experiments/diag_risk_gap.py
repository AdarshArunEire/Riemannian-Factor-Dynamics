"""Why does the GMV risk error miss by ~20% when everything else matches to 2%?

check_panel_vs_parent.py found: BW 0.0-1.0%, Frobenius 0.6-2.4%, risk error
14.7-27.5% and systematically LOW. The risk statistic is the only one that
INVERTS a realised covariance, and E2 measured what inversion costs at the
conditioning Marchenko-Pastur predicts for 12 assets from ~21 observations.

Three diagnostics, in order of how decisive they are.

D1  SENSITIVITY. Perturb the panel by the size of our own disagreement with
    them (the measured Frobenius gap) and recompute everything. If BW and
    Frobenius barely move while the risk error swings by tens of percent, then
    a 20% risk gap is simply what a 2% panel gap looks like after inversion,
    and the statistic cannot be pinned down at this data precision. This is the
    one that answers the question.

D2  AMPLIFIER. Per-month kappa and gross leverage ||w||_1, and how strongly our
    own risk error tracks kappa. Extreme weights are the mechanism; this shows
    whether they are present.

D3  SHRINKAGE. Recompute the weights from (1-a)Sigma + a*(tr Sigma/m)I. If the
    risk error collapses toward theirs as the weights are tamed, the difference
    lives in the inverse and not in the panel.

    python experiments/diag_risk_gap.py
"""

from _common import header, write, ROOT, SEED

import sys

import numpy as np

from rfd.spd.bw import bw_dist2
from rfd.spd.linalg import sym, spd_eigh, rebuild_spd, spd_exp

RAW = ROOT / "results" / "raw" / "rc_panel_adjusted.npz"
TEST_SIZE = 36
LAMBDA = 0.94
N_DRAWS = 20
TARGET_PERTURB = 0.024          # the Frobenius gap we actually measured

PUBLISHED = {
    ("LOCF", "BW"): 2.66, ("EWMA", "BW"): 2.36,
    ("LOCF", "Frob"): 12.51, ("EWMA", "Frob"): 11.97,
    ("LOCF", "risk"): 2.61, ("EWMA", "risk"): 1.45,
}


def ewma_series(panel, lam=LAMBDA):
    res = np.zeros_like(panel)
    sigma = np.zeros(panel.shape[1:])
    for i in range(1, panel.shape[0]):
        sigma = lam * sigma + (1.0 - lam) * panel[i - 1]
        res[i] = sigma
    return res


def gmv_weights(S, alpha=0.0):
    """Minimum-variance weights, optionally shrunk toward the identity."""
    m = S.shape[-1]
    if alpha > 0:
        S = (1.0 - alpha) * S + alpha * (np.trace(S) / m) * np.eye(m)
    w = np.linalg.solve(S, np.ones(m))
    return w / w.sum()


def score(panel, alpha=0.0):
    n, q = panel.shape[0], panel.shape[-1]
    ewma = ewma_series(panel)
    models = {"LOCF": lambda t: panel[t - 1], "EWMA": lambda t: ewma[t]}
    acc = {k: {"BW": [], "Frob": [], "risk": []} for k in models}
    for t in range(n - TEST_SIZE, n):
        truth, lag = panel[t], panel[t - 1]
        w = gmv_weights(lag, alpha)
        true_risk = float(w @ truth @ w)
        for name, fn in models.items():
            hat = fn(t)
            acc[name]["BW"].append(np.sqrt(float(bw_dist2(hat, truth))))
            acc[name]["Frob"].append(float(np.linalg.norm(hat - truth, "fro")))
            acc[name]["risk"].append(abs(float(w @ hat @ w) - true_risk))
    return {(k, s): float(np.mean(v)) for k, d in acc.items() for s, v in d.items()}


def perturb(panel, rng, t):
    """Sigma^(1/2) exp(t E) Sigma^(1/2) -- stays SPD for any symmetric E."""
    out = np.empty_like(panel)
    for i, S in enumerate(panel):
        E = rng.standard_normal(S.shape)
        E = sym(E) / np.linalg.norm(sym(E))
        lam, V = spd_eigh(S)
        rS = rebuild_spd(np.sqrt(lam), V)
        out[i] = sym(rS @ spd_exp(t * E, strict=False) @ rS)
    return out


def main():
    if not RAW.exists():
        sys.exit(f"no {RAW} -- run experiments/build_rc_panel.py first")
    panel = np.load(RAW, allow_pickle=True)["panel"]
    n, q = panel.shape[0], panel.shape[-1]
    base = score(panel)
    rows = []

    # ---- D1 ---------------------------------------------------------------
    rng = np.random.default_rng(SEED)
    t = TARGET_PERTURB
    for _ in range(3):                       # calibrate t to the target size
        p = perturb(panel, np.random.default_rng(SEED), t)
        got = float(np.median(np.linalg.norm(p - panel, axis=(-2, -1))
                              / np.linalg.norm(panel, axis=(-2, -1))))
        t *= TARGET_PERTURB / got
    achieved = got
    print(f"D1: perturbation calibrated to {achieved:.3%} relative Frobenius\n",
          flush=True)

    draws = [score(perturb(panel, rng, t)) for _ in range(N_DRAWS)]
    print(f"{'model':<5} {'stat':<5} {'ours':>8} {'theirs':>8} "
          f"{'perturbed range':>22} {'covers theirs?':>15}")
    for key, pub in PUBLISHED.items():
        vals = np.array([d[key] for d in draws])
        lo, hi = vals.min(), vals.max()
        swing = (hi - lo) / base[key]
        covers = lo <= pub <= hi
        rows.append(("D1 sensitivity", f"{key[0]} {key[1]}", f"{base[key]:.3f}",
                     f"{pub:.2f}", f"{lo:.3f}..{hi:.3f}", f"{swing:.1%}",
                     "YES" if covers else "no"))
        print(f"{key[0]:<5} {key[1]:<5} {base[key]:>8.3f} {pub:>8.2f} "
              f"{lo:>10.3f} .. {hi:<9.3f} {'YES' if covers else 'no':>15}")

    # ---- D2 ---------------------------------------------------------------
    kap, lev, rerr = [], [], []
    ewma = ewma_series(panel)
    for tt in range(n - TEST_SIZE, n):
        lag, truth = panel[tt - 1], panel[tt]
        e = np.linalg.eigvalsh(lag)
        w = gmv_weights(lag)
        kap.append(e[-1] / e[0])
        lev.append(np.abs(w).sum())
        rerr.append(abs(float(w @ ewma[tt] @ w) - float(w @ truth @ w)))
    kap, lev, rerr = map(np.array, (kap, lev, rerr))
    corr = float(np.corrcoef(np.log(kap), rerr)[0, 1])
    print(f"\nD2: kappa median {np.median(kap):.3e}  "
          f"gross leverage ||w||_1 median {np.median(lev):.2f} "
          f"(max {lev.max():.2f})")
    print(f"    corr(log kappa, EWMA risk error) = {corr:+.3f}")
    rows += [("D2 amplifier", "kappa median", f"{np.median(kap):.3e}", "", "", "", ""),
             ("D2 amplifier", "kappa max", f"{kap.max():.3e}", "", "", "", ""),
             ("D2 amplifier", "gross leverage median", f"{np.median(lev):.2f}", "", "", "", ""),
             ("D2 amplifier", "gross leverage max", f"{lev.max():.2f}", "", "", "", ""),
             ("D2 amplifier", "corr(log kappa, risk err)", f"{corr:+.3f}", "", "", "", "")]

    # ---- D3 ---------------------------------------------------------------
    print(f"\nD3: {'alpha':>6} {'LOCF risk':>10} {'(theirs 2.61)':>14} "
          f"{'EWMA risk':>10} {'(theirs 1.45)':>14}")
    for a in (0.0, 0.01, 0.05, 0.10, 0.20, 0.50):
        s = score(panel, alpha=a)
        l, e = s[("LOCF", "risk")], s[("EWMA", "risk")]
        print(f"    {a:>6.2f} {l:>10.3f} {abs(l - 2.61) / 2.61:>13.1%} "
              f"{e:>10.3f} {abs(e - 1.45) / 1.45:>13.1%}")
        rows.append(("D3 shrinkage", f"alpha={a:.2f}", f"{l:.3f}",
                     f"{abs(l - 2.61) / 2.61:.1%}", f"{e:.3f}",
                     f"{abs(e - 1.45) / 1.45:.1%}", ""))

    lines = header("Diagnostic -- the GMV risk-error gap",
                   extra=[f"panel: adjusted, {n} months",
                          f"D1: {N_DRAWS} draws at {achieved:.2%} relative perturbation"])
    lines += [
        "D1 is the decisive one. If BW and Frobenius barely move under a",
        "perturbation the size of our own disagreement with them, while the risk",
        "error swings enough to cover their published value, then a 20% risk gap",
        "is what a 2% panel gap looks like after inverting a matrix at this",
        "conditioning -- and the risk statistic cannot verify a panel.",
        "",
        "If the perturbed range does NOT cover their value, amplification is not",
        "the whole story and something in the construction differs. The leading",
        "candidate is the effective number of trading days: their notebook",
        "downloads all ~500 constituents and selects twelve later, so if days",
        "with any missing price were dropped across the full universe, their",
        "monthly covariances rest on fewer observations -- worse conditioned,",
        "more extreme weights, larger risk errors, and almost no effect on BW or",
        "Frobenius. That is the shape of what we see.",
    ]
    write("diag_risk_gap", lines,
          ["diagnostic", "item", "value", "theirs", "range", "swing", "covers"], rows)


if __name__ == "__main__":
    main()
