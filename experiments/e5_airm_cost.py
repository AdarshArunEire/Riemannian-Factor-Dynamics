"""E5 -- AIRM cost, measured against BW rather than assumed.

E4's caveat list says of the Karcher mean: "typically SLOWER per iteration
than the AE fixed point -- assume this roughly doubles the total, at least."
That was a guess written into a budget. This replaces it with a number.

Same grid as E4 so the two are directly comparable, and both are timed in
the same process on the same machine in the same run -- which matters more
than absolute speed, because the thing being decided is a RATIO.

    python experiments/e5_airm_cost.py
"""

from _common import SEED, header, write

import time

import numpy as np

from rfd.dgp.spd import random_spd
from rfd.spd.bw import bw_barycentre
from rfd.spd.airm import airm_barycentre

MS = [3, 12]
NS = [100, 1000, 10000, 50000]
CONDS = [1e1, 1e3]
TOL = 1e-11               # common tolerance: AIRM's floor is looser than BW's,
                          # so comparing at BW's 1e-12 would be rigged
MAX_ITER = 500

N19_STREAMS, N19_DRAWS, N19_CELLS_PER_M = 20, 50000, 9


def timed(fn, m, n, cond):
    rng = np.random.default_rng(SEED)
    S = random_spd(rng, m=m, cond=cond, n=n)
    t0 = time.perf_counter()
    r = fn(S, tol=TOL, max_iter=MAX_ITER)
    return time.perf_counter() - t0, r.n_iter, r.converged


def main():
    timed(bw_barycentre, 3, 100, 10.0)          # warmup
    timed(airm_barycentre, 3, 100, 10.0)

    rows = []
    for m in MS:
        for cond in CONDS:
            for n in NS:
                bt, bi, bok = timed(bw_barycentre, m, n, cond)
                at, ai, aok = timed(airm_barycentre, m, n, cond)
                rows.append((m, f"{cond:g}", n, f"{bt:.4f}", bi, int(bok),
                             f"{at:.4f}", ai, int(aok), f"{at / bt:.2f}"))
                print(f"  m={m:<3d} cond={cond:<7.0e} N={n:<6d} | "
                      f"BW {bt:7.3f}s {bi:3d}it | AIRM {at:7.3f}s {ai:3d}it | "
                      f"ratio {at / bt:5.2f}x"
                      f"{'' if (bok and aok) else '   NOT CONVERGED'}", flush=True)

    big = [r for r in rows if r[2] == N19_DRAWS]
    airm_worst = {m: max(float(r[6]) for r in big if r[0] == m) for m in MS}
    bw_worst = {m: max(float(r[3]) for r in big if r[0] == m) for m in MS}
    airm_total = sum(N19_CELLS_PER_M * N19_STREAMS * airm_worst[m] for m in MS)
    bw_total = sum(N19_CELLS_PER_M * N19_STREAMS * bw_worst[m] for m in MS)

    lines = header("E5 -- AIRM vs BW barycentre cost",
                   extra=[f"common tol: {TOL:.0e}, max_iter: {MAX_ITER}"])
    lines += [
        "The ratio column is the number this experiment exists for. E4's",
        "budget assumed ~2x for AIRM; anything materially above that is a",
        "reason to revisit N-19's allocation BEFORE any result is seen.",
        "",
        "Both methods are timed at a COMMON tolerance. Comparing them at",
        "their own defaults would be rigged, since AIRM's measured floor",
        "(~6e-12) is looser than BW's (~1e-14) and it would be charged for",
        "chasing a precision it cannot reach.",
        "",
        f"Projected over the N-19 grid ({N19_CELLS_PER_M} cells per m, "
        f"{N19_STREAMS} streams, {N19_DRAWS} draws):",
        f"  BW    {bw_total / 60:.1f} min",
        f"  AIRM  {airm_total / 60:.1f} min",
        f"  both  {(bw_total + airm_total) / 60:.1f} min "
        f"({(bw_total + airm_total) / 3600:.2f} h)",
        "",
        "Still excluded: proxy generation, the Frobenius barycentre (free),",
        "and C5's non-Wishart proxy.",
    ]
    write("e5_airm_cost", lines,
          ["m", "cond", "N", "bw_seconds", "bw_iters", "bw_converged",
           "airm_seconds", "airm_iters", "airm_converged", "ratio"], rows)


if __name__ == "__main__":
    main()
