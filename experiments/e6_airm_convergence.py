"""E6 -- AIRM convergence surface, and whether the full step is right.

E1's finding for BW was that iteration count follows DISPERSION, not
conditioning. Gradient descent on a Hadamard manifold is a different
algorithm with a different convergence story, so that result does not
transfer for free -- it has to be measured again.

Also sweeps the step size. step=1.0 is the standard full step and converges
globally in theory; the question is whether a widely dispersed family
overshoots in practice, which is the one situation where damping earns its
keep. If step=0.5 never wins, the parameter can stay at its default forever
and this settles it.

    python experiments/e6_airm_convergence.py
"""

from _common import SEED, header, write

import numpy as np

from rfd.dgp.spd import random_spd_family
from rfd.spd.airm import airm_barycentre

MS = [3, 12]
CONDS = [1e1, 1e3, 1e5]
SHAPES = ["geom", "linear", "dominant"]
DELTAS = [0.0, 0.1, 0.5, 1.0, 2.0]
STEPS = [1.0, 0.5]
N = 200
TOL = 1e-11
MAX_ITER = 500


def main():
    rows = []
    for m in MS:
        for shape in SHAPES:
            for cond in CONDS:
                for delta in DELTAS:
                    for step in STEPS:
                        rng = np.random.default_rng(SEED)
                        S = random_spd_family(rng, m=m, cond=cond, delta=delta,
                                              n=N, shape=shape)
                        r = airm_barycentre(S, tol=TOL, max_iter=MAX_ITER,
                                            step=step)
                        rows.append((m, shape, f"{cond:g}", delta, step,
                                     r.n_iter, f"{r.residual:.3e}",
                                     int(r.converged)))
                        print(f"  m={m:<3d} {shape:<9s} cond={cond:<7.0e} "
                              f"delta={delta:<4.1f} step={step:<4.1f} -> "
                              f"{r.n_iter:4d} iters"
                              f"{'' if r.converged else '   NOT CONVERGED'}",
                              flush=True)

    lines = header("E6 -- AIRM convergence surface",
                   extra=[f"N per cell: {N}, tol: {TOL:.0e}, max_iter: {MAX_ITER}"])
    lines += [
        "Compare against E1. If iterations here also follow delta and ignore",
        "cond, the two geometries share a cost story and one sentence covers",
        "both. If AIRM behaves differently, that difference is itself a",
        "result -- gradient descent and a fixed-point map need not agree.",
        "",
        "On step: 1.0 should win everywhere. Any cell where 0.5 converges in",
        "fewer sweeps is a cell where the full step overshoots, and that is",
        "the only evidence that would justify exposing the parameter at all.",
    ]
    write("e6_airm_convergence", lines,
          ["m", "shape", "cond", "delta", "step", "iters", "residual",
           "converged"], rows)


if __name__ == "__main__":
    main()
