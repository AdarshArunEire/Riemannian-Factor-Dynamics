"""Run every B1.2 experiment in order, then redraw the plots.

    python sandbox/run_all.py              # everything
    python sandbox/run_all.py e1 e2        # only these
    python sandbox/run_all.py --skip e4    # everything except e4

Order is deliberate: E4 first, because it is the only one whose answer can
invalidate the plan (if N-19 is unaffordable the budget gets amended before
anything else is worth measuring). Then E2, which fixes the range you are
allowed to operate in. Then E1, the surface. Then E3, a refinement.

Rough cost: E4 ~1 min, the rest a few seconds each.

This lives in sandbox/ because it is a convenience, not a result. Nothing
imports from here; the experiments themselves are the reproducible units and
each one runs standalone.
"""

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STEPS = [
    ("e4", "experiments/e4_bw_cost.py", "cost model -- is N-19 affordable"),
    ("e2", "experiments/e2_boundary.py", "boundary -- where it stops working"),
    ("e1", "experiments/e1_convergence_surface.py", "surface -- dispersion vs kappa"),
    ("e3", "experiments/e3_tol_accuracy.py", "tol vs accuracy"),
    ("e5", "experiments/e5_airm_cost.py", "AIRM cost vs BW -- replaces E4's guess"),
    ("e6", "experiments/e6_airm_convergence.py", "AIRM surface + step size"),
    ("e7", "experiments/e7_geometry_divergence.py", "BW vs AIRM vs arithmetic centres"),
]


def main(argv):
    skip = set()
    only = set()
    if "--skip" in argv:
        i = argv.index("--skip")
        skip = set(argv[i + 1:])
        argv = argv[:i]
    if argv:
        only = set(argv)

    chosen = [s for s in STEPS
              if (not only or s[0] in only) and s[0] not in skip]
    if not chosen:
        sys.exit(f"nothing to run. known steps: {', '.join(s[0] for s in STEPS)}")

    total = time.perf_counter()
    failed = []
    for tag, script, blurb in chosen:
        print(f"\n{'=' * 70}\n{tag.upper()}  {blurb}\n{'=' * 70}", flush=True)
        t0 = time.perf_counter()
        r = subprocess.run([sys.executable, script], cwd=ROOT)
        dt = time.perf_counter() - t0
        if r.returncode != 0:
            failed.append(tag)
            print(f"  !! {tag} exited {r.returncode} after {dt:.1f}s", flush=True)
        else:
            print(f"  {tag} done in {dt:.1f}s", flush=True)

    print(f"\n{'=' * 70}\nPLOTS\n{'=' * 70}", flush=True)
    subprocess.run([sys.executable, "sandbox/look.py"], cwd=ROOT)

    print(f"\ntotal {time.perf_counter() - total:.1f}s")
    if failed:
        # non-zero exit so a failure is not something you have to notice
        sys.exit(f"FAILED: {', '.join(failed)}")


if __name__ == "__main__":
    main(sys.argv[1:])
