import numpy as np
from rfd.spd.linalg import rebuild_spd, spd_sqrt, spd_exp

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


def spectrum(m, cond=10.0, shape="geom"):
    """Eigenvalue vector spanning [1, cond]. Same condition number, different
    shape -- which lets an experiment separate "how ill-conditioned" from
    "how the mass is distributed".

        geom      log-uniform between 1 and cond
        linear    evenly spaced, so most mass sits near the top
        dominant  one large eigenvalue over a decaying tail (equity-like)
    """
    if shape == "geom":
        return np.geomspace(1.0, cond, m)
    if shape == "linear":
        return np.linspace(1.0, cond, m)
    if shape == "dominant":
        if m == 1:
            return np.array([cond])
        return np.concatenate([np.geomspace(1.0, np.sqrt(cond), m - 1), [cond]])
    raise ValueError(f"unknown shape {shape!r}")


def random_spd_family(rng, m, cond=10.0, delta=0.0, n=1, shape="geom"):
    """n SPD matrices dispersed around one common base B:

        S_i = B^(1/2) exp(delta * E_i) B^(1/2),   E_i random symmetric, ||E_i||=1

    Two INDEPENDENT knobs. cond and shape set the conditioning of the base;
    delta sets how far apart the S_i are. random_spd cannot do this -- there,
    raising cond makes the matrices both worse conditioned and further apart
    at the same time, so any curve drawn against cond is confounded.

    delta=0 returns n copies of B, whose barycentre is B exactly.
    """
    B = rebuild_spd(spectrum(m, cond, shape), random_Q(rng, (m, m)))
    if delta == 0.0:
        return np.broadcast_to(B, (n, m, m)).copy()
    E = rng.standard_normal((n, m, m))
    E = 0.5 * (E + E.mT)
    E = E / np.linalg.norm(E, axis=(-2, -1), keepdims=True)
    rB = spd_sqrt(B)
    return rB @ spd_exp(delta * E) @ rB
