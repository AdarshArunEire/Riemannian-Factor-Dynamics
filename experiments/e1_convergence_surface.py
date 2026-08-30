"""E1 -- what actually drives the BW barycentre's iteration count.

The numerical test contract asks for iterations as a function of condition number. That alone
would be confounded: `random_spd` at higher cond produces matrices that are
both worse conditioned AND further apart, and the fixed point converges
instantly on a stack of identical matrices however ill-conditioned each one
is. So this sweeps two independent knobs --

    cond   conditioning of the common base B
    delta  how far the S_i are dispersed around B

plus three spectrum SHAPES at fixed cond, because the unexplained m=12
anomaly in g_mean is already evidence that shape matters at fixed kappa.

If iterations track delta and ignore cond, the "BW-SHRINKING-MARGIN" story
in the canon is written against the wrong variable, and that is worth
knowing before it reaches a paper.

    python experiments/e1_convergence_surface.py
"""

from _common import SEED, header, write

import numpy as np

from rfd.dgp.spd import random_spd_family
from rfd.spd.bw import bw_barycentre

MS = [3, 12]
CONDS = [1e1, 1e3, 1e5]
SHAPES = ["geom", "linear", "dominant"]
DELTAS = [0.0, 0.1, 0.5, 1.0, 2.0]
N = 200
TOL = 1e-12
MAX_ITER = 500


def main():
    rows = []
    for m in MS:
        for shape in SHAPES:
            for cond in CONDS:
                for delta in DELTAS:
                    rng = np.random.default_rng(SEED)
                    S = random_spd_family(rng, m=m, cond=cond, delta=delta,
                                          n=N, shape=shape)
                    r = bw_barycentre(S, tol=TOL, max_iter=MAX_ITER)
                    rows.append((m, shape, f"{cond:g}", delta, r.n_iter,
                                 f"{r.residual:.3e}", int(r.converged)))
                    print(f"  m={m:<3d} {shape:<9s} cond={cond:<7.0e} "
                          f"delta={delta:<4.1f} -> {r.n_iter:4d} iters"
                          f"{'' if r.converged else '   NOT CONVERGED'}",
                          flush=True)

    lines = header("E1 -- convergence surface",
                   extra=[f"N per cell: {N}, tol: {TOL:.0e}, max_iter: {MAX_ITER}"])
    lines += [
        "Read iterations DOWN a delta block at fixed cond, then ACROSS cond at",
        "fixed delta. Whichever direction moves the number is the variable the",
        "cost actually depends on. delta=0 is the anchor: all S_i identical, so",
        "the barycentre is B and the fixed point should land almost at once.",
        "",
        "Shape is varied at FIXED cond. Any spread across shape rows is spectral",
        "geometry that the condition number does not capture -- and would mean a",
        "single kappa axis cannot summarise difficulty.",
    ]
    write("e1_convergence_surface", lines,
          ["m", "shape", "cond", "delta", "iters", "residual", "converged"], rows)


if __name__ == "__main__":
    main()
