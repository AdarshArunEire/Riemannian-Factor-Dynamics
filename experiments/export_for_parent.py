"""B3.4b step 1 -- write the two input files `sp500_reproduce.R` expects.

THE THING THAT IS NOT IN THEIR REPO. `sp500_reproduce.R:12` and `:138` read

    ./sp500_covariance/VIXCLS.csv
    ./sp500_covariance/sp500_12bySector.RData

and the directory `sp500_covariance/` does not exist in the clone at commit
c07d49c. Their code does not build the RC panel from prices -- nothing in the
repo does. The panel is an INPUT. So reproduction means supplying it, and this
script writes the two files in the exact shape their code reads.

Nothing upstream is modified. A new directory is created inside the pinned
clone containing only our generated inputs; delete it and the clone is
byte-identical again. Recorded in reference/PROVENANCE.md.

TWO TRAPS, both load-bearing:

  1. SCALE. build_rc_panel.py already multiplied by 10000 (their
     sp500_analysis.R:150). Their script does it AGAIN at line 148. So this
     exporter DIVIDES BY 10000 on the way out. Skip that and every distance
     comes out 10000x too big and every ranking still looks fine, which is
     the worst kind of bug.

  2. ARRAY ORDER. `covariances` is 4-D, (year, month, asset, asset), year
     slow and month fast. Their line 141 does
         array(aperm(dta, c(2,1,3,4)), c(d1*d2, q, q))
     and R is column-major, so the flattened row index is
     month + 12*(year-1) -- chronological only if year is axis 1. Verified
     numerically before this was written. Get it backwards and the panel is
     silently transposed in time: it runs, it produces numbers, and they are
     the numbers for a shuffled history.

VIX is a second, unrelated dependency: FRED series VIXCLS, daily, which their
lines 14-24 average into months. Not used in estimation -- it is the overlay
on the Factor 1 plot -- but line 12 runs before everything and the script dies
without it. FRED writes "." for missing days; their `mean(..., na.rm=TRUE)`
only works if that column is numeric, so we blank it here rather than let
read.csv silently make the column character.

    python experiments/export_for_parent.py            # adjusted (the closer variant)
    python experiments/export_for_parent.py --variant raw
"""

from _common import header, write, ROOT

import argparse
import sys

import numpy as np

SCALE = 10000.0                     # must match build_rc_panel.py
N_MONTHS = 240                      # 2000-01 .. 2019-12
YEARS, MONTHS_PER_YEAR = 20, 12
FRED = ("https://fred.stlouisfed.org/graph/fredgraph.csv"
        "?id=VIXCLS&cosd=2000-01-01&coed=2019-12-31")

PARENT = ROOT / "reference" / "Riemannian_factor_model-main" / "sp500_covariance"
RAW = ROOT / "results" / "raw"


def load_panel(variant):
    path = RAW / f"rc_panel_{variant}.npz"
    if not path.exists():
        sys.exit(f"{path} missing -- run experiments/build_rc_panel.py first")
    z = np.load(path, allow_pickle=False)
    panel, months, tickers = z["panel"], z["months"], z["tickers"]

    if panel.shape != (N_MONTHS, 12, 12):
        sys.exit(f"panel is {panel.shape}, expected ({N_MONTHS}, 12, 12)")
    if str(months[0]) != "2000-01" or str(months[-1]) != "2019-12":
        sys.exit(f"window is {months[0]}..{months[-1]}, expected 2000-01..2019-12")

    return panel / SCALE, [str(m) for m in months], [str(t) for t in tickers]


def write_panel_csv(panel, months, tickers):
    """240 rows x 144 columns, row t = vec(Sigma_t) in C order, plus a month column.

    Flat and dumb on purpose. R reads it with read.csv and reshapes; there is
    no binary format shared between numpy and R that does not add a dependency
    to one side or the other.
    """
    PARENT.mkdir(parents=True, exist_ok=True)
    path = PARENT / "panel_flat.csv"

    cols = [f"v{i}_{j}" for i in range(12) for j in range(12)]
    lines = ["month," + ",".join(cols)]
    for t, m in enumerate(months):
        lines.append(m + "," + ",".join(f"{x:.17g}" for x in panel[t].ravel(order="C")))

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (PARENT / "tickers.csv").write_text(
        "ticker\n" + "\n".join(tickers) + "\n", encoding="utf-8")
    print(f"written -> {path.relative_to(ROOT)}  ({len(months)} months)")
    print(f"written -> {(PARENT / 'tickers.csv').relative_to(ROOT)}")


def write_vix():
    """FRED VIXCLS -> the two-column CSV their lines 12-24 expect."""
    try:
        import pandas as pd
    except ImportError:
        sys.exit("pandas not installed:  pip install pandas")

    print(f"fetching {FRED}", flush=True)
    df = pd.read_csv(FRED)
    df.columns = ["DATE", "VIXCLS"]                     # FRED renamed col 1 in 2025
    df["VIXCLS"] = pd.to_numeric(df["VIXCLS"], errors="coerce")

    n_missing = int(df["VIXCLS"].isna().sum())
    path = PARENT / "VIXCLS.csv"
    df.to_csv(path, index=False, na_rep="")             # blank, not "." -> numeric in R
    print(f"written -> {path.relative_to(ROOT)}  "
          f"({len(df)} rows, {n_missing} missing blanked, "
          f"{df['DATE'].iloc[0]} .. {df['DATE'].iloc[-1]})")
    return len(df), n_missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="adjusted", choices=["adjusted", "raw"])
    ap.add_argument("--skip-vix", action="store_true")
    args = ap.parse_args()

    panel, months, tickers = load_panel(args.variant)
    write_panel_csv(panel, months, tickers)
    n_vix, n_missing = (0, 0) if args.skip_vix else write_vix()

    # Round-trip the reshape their script will do, on OUR side, so the check is
    # independent of whether the R half is right.
    cube = panel.reshape(YEARS, MONTHS_PER_YEAR, 12, 12)     # (year, month, i, j)
    back = np.transpose(cube, (1, 0, 2, 3))                  # R's aperm(c(2,1,3,4))
    back = back.reshape(-1, order="F").reshape(
        (N_MONTHS, 12, 12), order="F")                       # R's array(), column-major

    # ---- scale, checked on a statistic that has a meaning -----------------
    # SUPERSEDED 2026-08-18: the first version of this check was
    # `max |Sigma| < 1e-2`, and it FAILED on a correct panel. The max is a tail
    # statistic -- it lands on 2000-09 AAPL, the month of the 29 September
    # profit warning and a single -52% day, giving a daily sd of 16.9%. A real
    # event, not a bug. The threshold was a typed power of ten, which standing
    # rule 7 forbids and rule 9 is about: a check whose failure carries no
    # information is not a check.
    #
    # What the guard is actually for is the DOUBLE-SCALING bug, and that is a
    # bulk property. So: take the median diagonal, read it as a variance of
    # daily log returns, annualise it, and require an equity-like number. If
    # the x10000 were left on, the median asset-month would annualise to
    # ~2400% and this fails loudly. The band is argued from what large-cap
    # equity volatility is, not chosen to pass.
    diag = np.diagonal(panel, axis1=1, axis2=2)
    ann_vol = float(np.sqrt(np.median(diag) * 252))

    # Read the file back rather than re-checking the array in memory: what goes
    # to R is the CSV, and %.17g is exact for float64, so this must be bitwise.
    reread = np.array([[float(x) for x in ln.split(",")[1:]]
                       for ln in (PARENT / "panel_flat.csv")
                       .read_text(encoding="utf-8").splitlines()[1:]]
                      ).reshape(N_MONTHS, 12, 12)

    checks = [
        ("the CSV bitwise round-trips the unscaled panel",
         bool(np.array_equal(reread, panel))),
        ("median asset-month annualises to equity-like vol (5%-100%)",
         bool(0.05 < ann_vol < 1.00)),
        ("their aperm+reshape returns chronological order",
         bool(np.allclose(back, panel, rtol=0, atol=0))),
        ("240 months, 12 assets", panel.shape == (N_MONTHS, 12, 12)),
        ("every RC still positive definite",
         bool((np.linalg.eigvalsh(panel)[:, 0] > 0).all())),
        ("VIX fetched", args.skip_vix or n_vix > 5000),
    ]
    for name, ok in checks:
        print(f"    {'PASS' if ok else 'FAIL'}  {name}")

    lines = header("B3.4b step 1 -- inputs handed to the parent's own script",
                   extra=[f"variant: {args.variant}",
                          f"window: {months[0]} .. {months[-1]}",
                          f"tickers: {' '.join(tickers)}",
                          "written into reference/.../sp500_covariance/ (gitignored)"])
    lines += [
        "`sp500_covariance/` is ABSENT from the clone at commit c07d49c, and no",
        "file in their repo builds the RC panel from prices. The panel is an",
        "input to their code, so reproduction requires supplying it. No upstream",
        "file is modified; deleting this directory restores the clone exactly.",
        "",
        "The panel is written UNSCALED. build_rc_panel.py applies their x10000",
        "(sp500_analysis.R:150) and sp500_reproduce.R:148 applies it again, so",
        "exactly one of the two must be undone and this is the one we control.",
        "",
        "Next: Rscript R/make_panel_rdata.R, then Rscript R/run_parent_reproduce.R.",
    ]
    write("parent_inputs", lines,
          ["quantity", "value"],
          [("variant", args.variant),
           ("months", str(len(months))),
           ("scale applied on export", f"1/{SCALE:.0f}"),
           ("max |Sigma| after unscaling", f"{np.abs(panel).max():.4e}"),
           ("  where", f"{months[int(np.abs(panel).max(axis=(1, 2)).argmax())]} "
                       f"-- AAPL, the -52% day of 2000-09-29"),
           ("median diagonal, unscaled", f"{np.median(diag):.4e}"),
           ("  as annualised vol", f"{ann_vol:.1%}"),
           ("median diagonal x 10000", f"{np.median(diag) * SCALE:.4f}"),
           ("vix rows", str(n_vix)),
           ("vix missing blanked", str(n_missing)),
           *[(f"check: {n}", "PASS" if ok else "FAIL") for n, ok in checks]])

    if any(not ok for _, ok in checks):
        sys.exit("one or more checks FAILED")


if __name__ == "__main__":
    main()
