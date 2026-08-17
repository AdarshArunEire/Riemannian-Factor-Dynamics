"""E3 -- what a given `tol` actually buys you.

`tol` is the residual the iteration stops at. It is NOT the accuracy of the
answer, and the two differ by orders of magnitude. This maps one to the other.

Design note, learned the hard way. The obvious reference is a COMMUTING
family, where the barycentre has a closed form. That turns out to be useless
here: on a commuting family every S_i shares an eigenbasis, the whole problem
is simultaneously diagonalisable, and the fixed point lands in ONE step
regardless of tol. Every row comes back identical and the sweep measures
nothing. (Worth knowing in its own right -- it is a real property of the
iteration, and it means the commuting closed form is a good CORRECTNESS test
and a bad CONVERGENCE test.)

So the reference here is a gold-standard run instead: the same dispersed,
non-commuting family taken to tol=0 for REF_ITER sweeps, i.e. iterated until
it can go no further. Every tol is then measured against that.

Decides the production default. tol=1e-12 is currently a defensible guess
sitting an order above the measured stall; this turns it into a curve.

    python experiments/e3_tol_accuracy.py
"""

from _common import SEED, header, write

import numpy as np

from rfd.dgp.spd import random_spd_family
from rfd.spd.bw import bw_barycentre

MS = [3, 12]
CONDS = [1e1, 1e3, 1e5]
TOLS = [1e-6, 1e-8, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14, 1e-15]
N = 200
DELTA = 1.0
REF_ITER = 2000
MAX_ITER = 500


def main():
    rows = []
    for m in MS:
        for cond in CONDS:
            rng = np.random.default_rng(SEED)
            S = random_spd_family(rng, m=m, cond=cond, delta=DELTA, n=N)
            ref = bw_barycentre(S, tol=0.0, max_iter=REF_ITER).X
            n_ref = np.linalg.norm(ref)

            for tol in TOLS:
                r = bw_barycentre(S, tol=tol, max_iter=MAX_ITER)
                err = np.linalg.norm(r.X - ref) / n_ref
                rows.append((m, f"{cond:g}", f"{tol:g}", r.n_iter,
                             f"{r.residual:.3e}", f"{err:.3e}", int(r.converged)))
                print(f"  m={m:<3d} cond={cond:<7.0e} tol={tol:<7.0e} -> "
                      f"{r.n_iter:4d} iters, err {err:.2e}"
                      f"{'' if r.converged else '   STALLED'}", flush=True)

    lines = header("E3 -- tol vs achieved accuracy",
                   extra=[f"N per cell: {N}, delta: {DELTA}",
                          f"reference: same family at tol=0, {REF_ITER} sweeps"])
    lines += [
        "Two columns to compare: `residual` is what the loop stopped at,",
        "`err_vs_ref` is the actual distance to the converged answer. They are",
        "not the same quantity and the gap between them is the point.",
        "",
        "Look for the knee. Below some tol, err stops improving while iters keep",
        "climbing -- more sweeps buy nothing but time. That knee is the",
        "production default. Below it again, `converged` goes false: the",
        "requested tol is under the machine's floor and the loop runs to",
        "max_iter for nothing.",
    ]
    write("e3_tol_accuracy", lines,
          ["m", "cond", "tol", "iters", "residual", "err_vs_ref", "converged"],
          rows)


if __name__ == "__main__":
    main()
