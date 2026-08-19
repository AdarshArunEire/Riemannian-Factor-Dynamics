"""B3.4b step 4 -- read the parent's run and decide whether it reproduced.

    python experiments/check_parent_run.py

Two questions, asked in this order, because the second is only interpretable
once the first has passed.

STAGE 1 -- IS OUR EVALUATION HARNESS RIGHT?
    Their script computes LOCF and EWMA itself (sp500_reproduce.R:295-307 and
    :246-262) from the panel we handed it. We computed both independently in
    Python. Identical input, two harnesses, two languages, two BLAS libraries.
    Agreement should be at round-off. This is the same manoeuvre as the BW
    metric calibration and it isolates the same way: a failure here is OUR
    evaluation code, not the data and not their estimator. Without it, a bad
    RFM number would be ambiguous between three causes instead of one.

    Small residual disagreement is expected and is not a bug: they demean the
    EWMA recursion from Sigma_tilde = 0 and so do we, but LOCF at m=1 reaches
    back one month before the test window, and any off-by-one there shows up
    here rather than anywhere else.

STAGE 2 -- DID THE REPRODUCTION SUCCEED?
    RFM and LFM against the published figures, judged against the bands fixed
    in config/predeclaration.yaml BEFORE this ran: 2% on bulk statistics (BW,
    Frobenius), 6% on the tail statistic (GMV risk error). Those bands came
    from LOCF and EWMA, which fit nothing and cannot be tuned.

    A number outside the band is NOT automatically a failure of our pipeline.
    reference/AUDIT.md 2b records that their month appears to rest on ~20
    trading days against our 21, which we did not correct for. What would be a
    failure is the RANKING changing -- and that is reported separately below,
    because it is the claim the paper actually makes.
"""

from _common import header, write, ROOT, FINAL

import csv
import sys

RUN = ROOT / "results" / "raw" / "parent_run"

# arXiv:2607.28385v1, Figures 3 and 4.  (mean, median)
PUBLISHED = {
    ("RFM",  "bw"):   (2.22, 2.00),  ("LFM",  "bw"):   (3.57, 3.63),
    ("LOCF", "bw"):   (2.66, 2.33),  ("EWMA", "bw"):   (2.36, 2.28),
    ("RFM",  "frob"): (10.79, 7.14), ("LFM",  "frob"): (17.25, 17.01),
    ("LOCF", "frob"): (12.51, 8.02), ("EWMA", "frob"): (11.97, 9.81),
    ("RFM",  "risk"): (0.94, 0.52),  ("LFM",  "risk"): (3.66, 2.29),
    ("LOCF", "risk"): (2.61, 0.91),  ("EWMA", "risk"): (1.45, 0.89),
}
FAMILY = {"bw": "bulk", "frob": "bulk", "risk": "tail"}
BAND = {"bulk": 0.02, "tail": 0.06}          # predeclaration, amendment 2026-08-18
STAT_LABEL = {"bw": "BW distance", "frob": "Frobenius", "risk": "risk error"}

OURS_KEY = {"BW distance": "bw", "Frobenius distance": "frob",
            "risk prediction error": "risk"}

# Stage 1 must be compared at FULL PRECISION, so recompute rather than read.
#
# SUPERSEDED 2026-08-18, first run: this used to read `ours_mean` / `ours_median`
# out of results/final/panel_vs_parent.csv. Those are written `f"{x:.2f}"` --
# two decimals, because that file exists to sit beside published figures printed
# to two decimals. Comparing a full-precision R number against a 2-dp artifact
# has a floor of ~5e-3, and Stage 1's gate is 1e-6, so it reported a 2.539e-3
# "failure" that was entirely the rounding in our own storage. The check was
# sound; the data it was fed could not support it.
#
# `score()` returns full-precision floats, so import it and call it. Same
# function check_panel_vs_parent.py uses -- not a second transcription, which
# would defeat the purpose of an independent-implementation check.
from check_panel_vs_parent import score as py_score       # noqa: E402

RAW_PANEL = ROOT / "results" / "raw" / "rc_panel_adjusted.npz"

# Gate: the risk statistic runs through solve(), so it inherits amplification
# ~kappa, and the panel's kappa median is 4.3e2 -- a floor near eps*kappa ~ 1e-13.
# 1e-8 leaves five orders of headroom and still catches any real disagreement.
HARNESS_GATE = 1e-8


def read_csv(path):
    if not path.exists():
        sys.exit(f"{path} missing -- run Rscript R/run_parent_reproduce.R first")
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def gap(a, b):
    """Relative difference against the larger magnitude -- symmetric, and does
    not blow up when one side is near zero."""
    denom = max(abs(a), abs(b))
    return abs(a - b) / denom if denom else 0.0


def main():
    import numpy as np

    theirs = {r["model"]: r for r in read_csv(RUN / "summary.csv")}
    if not RAW_PANEL.exists():
        sys.exit(f"{RAW_PANEL} missing -- run experiments/build_rc_panel.py first")
    ours = py_score(np.load(RAW_PANEL, allow_pickle=True)["panel"])

    rows, notes = [], []

    # ---- stage 1: harness agreement on the two model-free baselines --------
    worst_harness = 0.0
    for (model, statistic), (py_mean, py_median) in ours.items():
        stat = OURS_KEY[statistic]
        for moment, py in (("mean", py_mean), ("median", py_median)):
            R = float(theirs[model][f"{stat}_{moment}"])
            g = gap(py, R)
            worst_harness = max(worst_harness, g)
            rows.append(("1 harness", model, STAT_LABEL[stat], moment,
                         f"{py:.12g}", f"{R:.12g}", f"{g:.2e}", ""))

    # ---- stage 2: the reproduction proper ---------------------------------
    verdicts = []
    for model in ("RFM", "LFM", "LOCF", "EWMA"):
        for stat in ("bw", "frob", "risk"):
            band = BAND[FAMILY[stat]]
            for i, moment in enumerate(("mean", "median")):
                pub = PUBLISHED[(model, stat)][i]
                got = float(theirs[model][f"{stat}_{moment}"])
                g = gap(pub, got)
                ok = g <= band
                verdicts.append(ok)
                rows.append((f"2 {FAMILY[stat]}", model, STAT_LABEL[stat], moment,
                             f"{pub:.4g}", f"{got:.4g}", f"{g * 100:.1f}%",
                             "in band" if ok else f"OUT (band {band:.0%})"))

    # ---- the claim the paper actually makes: does RFM win? ----------------
    for stat in ("bw", "frob", "risk"):
        for moment in ("mean", "median"):
            got = {m: float(theirs[m][f"{stat}_{moment}"])
                   for m in ("RFM", "LFM", "LOCF", "EWMA")}
            ours_order = sorted(got, key=got.get)
            pub = {m: PUBLISHED[(m, stat)][0 if moment == "mean" else 1]
                   for m in got}
            pub_order = sorted(pub, key=pub.get)
            rows.append(("3 ranking", "-", STAT_LABEL[stat], moment,
                         " < ".join(pub_order), " < ".join(ours_order), "",
                         "same" if ours_order == pub_order else "DIFFERENT"))
            notes.append((stat, moment, ours_order == pub_order))

    fvu = RUN / "fvu_by_factor.csv"
    if fvu.exists():
        d = read_csv(fvu)
        n_dis = sum(1 for r in d if r["disagree"].strip().upper() == "TRUE")
        rows.append(("4 P1-LOSS", "RFM vs LYB", "FVU ranking", "r = 1..%d" % len(d),
                     "", "", f"{n_dis}/{len(d)}",
                     "BW and Frobenius disagree" if n_dis else "no disagreement"))

    lines = header("B3.4b -- their estimator, our panel",
                   extra=["their code sourced verbatim; no upstream file modified",
                          "bands: bulk 2%, tail 6% (predeclaration, 2026-08-18)",
                          "anchors: arXiv:2607.28385v1 Figures 3 and 4"])
    lines += [
        f"**Stage 1, harness agreement: worst {worst_harness:.2e}"
        f" (gate {HARNESS_GATE:.0e}).** Their R and our Python compute LOCF and",
        "EWMA from the same panel, at full precision on both sides. A failure",
        "here is OUR evaluation code, and every Stage 2 number below would be",
        "uninterpretable until it were fixed.",
        "",
        f"**Stage 2: {sum(verdicts)} of {len(verdicts)} published figures inside the",
        "predeclared band.** LOCF and EWMA are not evidence here -- the band was",
        "set from them. RFM and LFM are the reproduction.",
        "",
        "**Stage 3 is the one to read.** The paper's claim is an ordering, not a",
        "set of decimals. A number outside the band with the ranking intact is a",
        "data difference; a ranking that flips is a reproduction failure.",
        "",
        "Not corrected for: the ~20-vs-21 trading-day difference of AUDIT 2b.",
    ]
    write("parent_reproduce", lines,
          ["stage", "model", "statistic", "moment", "published/ours",
           "theirs-on-our-panel", "gap", "verdict"], rows)

    print(f"\nstage 1 worst harness disagreement: {worst_harness:.3e}")
    print(f"stage 2 in band: {sum(verdicts)}/{len(verdicts)}")
    print(f"stage 3 rankings preserved: {sum(ok for _, _, ok in notes)}/{len(notes)}")

    if worst_harness > HARNESS_GATE:
        sys.exit("STAGE 1 FAILED -- our evaluation code disagrees with theirs on "
                 "identical input. Fix that before reading anything else.")


if __name__ == "__main__":
    main()
