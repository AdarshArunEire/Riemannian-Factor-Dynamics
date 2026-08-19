import numpy as np

# SPD matrix functions
# All take (m, m) or stacked (..., m, m)

def sym(A):
    return 0.5 * (A + A.mT)

def rebuild_spd(s, V):
    return (V * s[..., None, :]) @ V.mT

def spd_eigh(A, strict=True):  # validated decomposition
    if not np.isfinite(A).all():
        raise ValueError("matrix contains NaN or Inf")

    lam, V = np.linalg.eigh(sym(A))
    if not np.isfinite(lam).all():
        raise ValueError("eigendecomposition returned NaN or Inf")

    bad = lam.min(axis=-1) < -1e-10 * lam.max(axis=-1)
    if strict and bad.any():
        # strict flag catches non-PSD eigenvalues
        raise ValueError(f"not PSD at index/indices {np.flatnonzero(bad)}")
    return lam, V

def spd_op(A, op, strict=True):
    lam, V = spd_eigh(A, strict)
    return rebuild_spd(op(lam), V)


def spd_sqrt(A, strict=True):
    return spd_op(A, np.sqrt, strict)

def _invsqrt(lam):
    return 1.0 / np.sqrt(lam)
def spd_invsqrt(A, strict=True):
    return spd_op(A, _invsqrt, strict)

def g_mean(A, B, strict=True):
    lam, V = spd_eigh(A, strict)
    r_lam = np.sqrt(lam) # one sqrt
    r_A = rebuild_spd(r_lam, V)
    ir_A = rebuild_spd(1.0 / r_lam, V) 
    return r_A @ spd_sqrt(ir_A @ B @ ir_A, strict) @ r_A

def spd_log(A, strict=True):
    return spd_op(A, np.log, strict)

def spd_exp(A, strict=False): # maps sym -> SPD, non-strict
    return spd_op(A, np.exp, strict)
