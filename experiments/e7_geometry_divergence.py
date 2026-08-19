"""E7 -- how far apart are the BW, AIRM and arithmetic barycentres?

This is the first experiment in the repo that bears directly on the PAPER
rather than on the code.

P1-LOSS says the choice of loss is not innocent. E7 is the smallest possible
empirical version of that claim: take one family of matrices, compute its
centre three ways, and measure how far apart the answers are as dispersion
grows. Even on commuting families the geometries disagree by construction --
BW gives (mean sqrt)**2, AIRM gives exp(mean log), Frobenius gives the plain
mean -- so the question is never WHETHER they differ but by HOW MUCH at
realistic spread.

READ THIS BEFORE LOOKING AT THE OUTPUT. The result can go against you, and
that has to be acceptable in advance:

  * If the three centres agree to within estimation noise at realistic
    dispersion, then loss choice is empirically irrelevant HERE, and no
    amount of theorem-proving about P1-LOSS makes it matter for this
    application. That would be a real finding and it belongs in the paper.
  * If they diverge materially, that supports the thesis -- but divergence
    of CENTRES is still not divergence of RANKINGS, which is the claim the
    predeclaration's highest_value_check actually cares about. Do not let
    the stronger reading in through the back door.

Reference scale. Divergences are reported relative to the spread of the data
itself (mean AIRM distance from the AIRM centre). A gap of 1e-3 means
nothing on its own; a gap that is 10% of the data's own spread means a lot.

    python experiments/e7_geometry_divergence.py
"""

from _common import SEED, header, write

import numpy as np

from rfd.dgp.spd import random_spd_family
from rfd.spd.bw import bw_barycentre, bw_dist2
from rfd.spd.airm import airm_barycentre, airm_dist2

MS = [3, 12]
CONDS = [1e1, 1e3, 1e5]
DELTAS = [0.05, 0.1, 0.25, 0.5, 1.0, 2.0]
N = 200
TOL = 1e-10
MAX_ITER = 500


def main():
    rows = []
    for m in MS:
        for cond in CONDS:
            for delta in DELTAS:
                rng = np.random.default_rng(SEED)
                S = random_spd_family(rng, m=m, cond=cond, delta=delta, n=N)

                bw = bw_barycentre(S, tol=TOL, max_iter=MAX_ITER)
                ai = airm_barycentre(S, tol=TOL, max_iter=MAX_ITER)
                fr = S.mean(axis=0)

                # spread of the data about its own AIRM centre -- the yardstick
                spread = np.sqrt(airm_dist2(
                    np.broadcast_to(ai.X, S.shape), S).mean())

                d_bw_ai = np.sqrt(airm_dist2(ai.X, bw.X))
                d_ai_fr = np.sqrt(airm_dist2(ai.X, fr))
                d_bw_fr = np.sqrt(bw_dist2(bw.X, fr))

                rows.append((m, f"{cond:g}", delta,
                             f"{spread:.4e}",
                             f"{d_bw_ai:.4e}", f"{d_bw_ai / spread:.4f}",
                             f"{d_ai_fr:.4e}", f"{d_ai_fr / spread:.4f}",
                             f"{d_bw_fr:.4e}",
                             int(bw.converged and ai.converged)))
                print(f"  m={m:<3d} cond={cond:<7.0e} delta={delta:<5.2f} -> "
                      f"spread {spread:.3e} | BW-AIRM {d_bw_ai / spread:7.4f} "
                      f"| AIRM-Frob {d_ai_fr / spread:7.4f} of spread"
                      f"{'' if (bw.converged and ai.converged) else '  NOT CONV'}",
                      flush=True)

    lines = header("E7 -- divergence between BW, AIRM and arithmetic centres",
                   extra=[f"N per cell: {N}, tol: {TOL:.0e}"])
    lines += [
        "The two `_rel` columns are the ones to read: distance between",
        "centres divided by the spread of the data about its own centre.",
        "Absolute distances scale with whatever units the matrices carry and",
        "mean nothing across rows.",
        "",
        "Expected shape: -> 0 as delta -> 0 (all three agree on a tight",
        "family), growing with delta. What matters is the VALUE at the",
        "dispersion real data actually shows, which is not yet known -- so",
        "measuring the real panel's delta is the follow-up this creates.",
        "",
        "Divergence of centres is NOT divergence of rankings. The",
        "predeclaration's highest_value_check asks whether BW-ranked and",
        "Frobenius-ranked model comparisons ever disagree; that is a",
        "different and stronger question and needs its own experiment.",
    ]
    write("e7_geometry_divergence", lines,
          ["m", "cond", "delta", "spread", "d_bw_airm", "d_bw_airm_rel",
           "d_airm_frob", "d_airm_frob_rel", "d_bw_frob", "converged"], rows)


if __name__ == "__main__":
    main()
