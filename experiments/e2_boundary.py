"""E2 -- where the BW barycentre stops working.

Pushes lambda_min toward zero at fixed lambda_max and records what happens:
iterations, final residual, whether it converged, and whether spd_eigh's
strict guard fired because an intermediate went numerically indefinite.

Why this is not academic. The flagship application is 12 assets from ~21
daily observations. With m/M = 12/21 = 0.57, Marchenko-Pastur puts the
sample eigenvalue spread at roughly

    ((1 + sqrt(0.57)) / (1 - sqrt(0.57)))**2 ~ 51

ON TOP OF the true condition number. Realised covariances there will
plausibly sit at kappa ~ 1e3-1e4. This says whether that is comfortably
inside the working range or uncomfortably near the edge -- answered before
the data exists, which is the only time the answer is cheap.

    python experiments/e2_boundary.py
"""

from _common import SEED, header, write

import numpy as np

from rfd.dgp.spd import random_spd_family
from rfd.spd.bw import bw_barycentre

MS = [2, 3, 12]
CONDS = [1e2, 1e4, 1e6, 1e8, 1e10, 1e12]
DELTA = 1.0
N = 50
TOL = 1e-12
MAX_ITER = 500


def main():
    rows = []
    for m in MS:
        for cond in CONDS:
            rng = np.random.default_rng(SEED)
            raised = ""
            try:
                S = random_spd_family(rng, m=m, cond=cond, delta=DELTA, n=N)
                r = bw_barycentre(S, tol=TOL, max_iter=MAX_ITER)
                iters, res, ok = r.n_iter, f"{r.residual:.3e}", int(r.converged)
            except Exception as exc:                    # strict guard, or worse
                iters, res, ok = -1, "nan", 0
                raised = type(exc).__name__
            rows.append((m, f"{cond:g}", iters, res, ok, raised or "-"))
            print(f"  m={m:<3d} cond={cond:<8.0e} -> "
                  f"{'RAISED ' + raised if raised else f'{iters:4d} iters, res {res}'}"
                  f"{'' if ok or raised else '   NOT CONVERGED'}", flush=True)

    lines = header("E2 -- boundary of the working range",
                   extra=[f"N per cell: {N}, delta: {DELTA}, tol: {TOL:.0e}, "
                          f"max_iter: {MAX_ITER}"])
    lines += [
        "iters = -1 means an exception was raised rather than a number returned.",
        "That is not necessarily a bug: spd_eigh's strict guard firing means an",
        "intermediate stopped being numerically positive definite, which is the",
        "guard doing its job at the edge of what float64 can represent.",
        "",
        "Three outcomes, in increasing severity: converged; ran to max_iter with",
        "a finite residual (stalled at the noise floor); raised. Record where each",
        "boundary sits -- the first is the working range, the second is the",
        "degraded band, the third is off the map.",
        "",
        "Sanity anchor for the real application: realised covariance of 12 assets",
        "from ~21 daily returns is expected around kappa ~ 1e3-1e4.",
    ]
    write("e2_boundary", lines,
          ["m", "cond", "iters", "residual", "converged", "raised"], rows)


if __name__ == "__main__":
    main()
