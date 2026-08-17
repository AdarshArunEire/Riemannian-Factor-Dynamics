import numpy as np
from rfd.spd.linalg import rebuild_spd

def random_Q(rng, shape):
    A = rng.standard_normal(shape)
    Q, R = np.linalg.qr(A)
    d = np.diagonal(R, axis1=-2, axis2=-1) 
    return Q * np.sign(d)[..., None, :]

def random_spd(rng, m, cond=10.0, n=None):
    shape = (m, m) if n is None else (n, m, m)
    lam = np.geomspace(1.0, cond, m) 
    Q = random_Q(rng, shape)
    return rebuild_spd(lam, Q)