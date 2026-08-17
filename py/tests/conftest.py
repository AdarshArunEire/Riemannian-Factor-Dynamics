import numpy as np


def num_tol(amplification=1.0, dtype=np.float64, safety=10.0):
    """Tolerance for a RELATIVE Frobenius residual.

    Backward stability gives err ~ eps * amplification, where amplification
    is how much the OPERATION under test magnifies rounding error -- not the
    condition number of the inputs. They coincide for whitening-type
    identities and differ elsewhere:

        R @ R vs S              amplification ~ 1     (squaring, no growth)
        Ri @ S @ Ri vs I        amplification ~ kappa
        X # Y vs Y # X          amplification ~ kappa**2

    Rule of thumb: find the worst-conditioned INTERMEDIATE quantity in the
    formula; that sets the power of kappa.

    safety=10 calibrated against measured headroom (min 4.1x across
    m in {2,3,12} and cond in {1e1,1e3,1e5}). Re-measure if the BLAS
    changes -- see VERSIONS.md.
    """
    return safety * np.finfo(dtype).eps * amplification
