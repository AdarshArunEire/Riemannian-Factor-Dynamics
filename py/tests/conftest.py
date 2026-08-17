import numpy as np

def num_tol(kappa=1.0, dtype=np.float64, safety=10.0):
    """Tolerance for RELATIVE Frobenius residuals: err ~ eps * kappa.
    safety=10 from measured headroom; re-measure if BLAS changes."""
    return safety * np.finfo(dtype).eps * kappa