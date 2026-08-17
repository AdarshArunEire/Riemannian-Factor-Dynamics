from rfd.dgp.spd import random_spd
from rfd.spd.linalg import *
from tests.conftest import num_tol
import numpy as np
import pytest

# Naming convention in this file:
#   S       a random SPD matrix (or a stack of them) -- the input
#   R, Ri   S**(1/2) and S**(-1/2), DERIVED from S
#   X, Y    two independent random SPD draws


def rel_fro(X, ref):
    """Relative Frobenius residual, batched over the leading stack axis."""
    return np.linalg.norm(X - ref, axis=(-2, -1)) / np.linalg.norm(ref, axis=(-2, -1))


@pytest.mark.parametrize("cond", [1e1, 1e3, 1e5])
@pytest.mark.parametrize("m", [2, 3, 12])
def test_round_trip(rng, m, cond):
    """exp(log(S)) == S.

    Forward composition -- it does not amplify by kappa in practice, so
    amplification=cond is deliberately loose here (up to ~4e4x slack at
    cond=1e5). Kept uniform with the other tests rather than fitted.
    """
    S = random_spd(rng, m=m, cond=cond, n=100)
    assert rel_fro(spd_exp(spd_log(S)), S).max() < num_tol(amplification=cond)


@pytest.mark.parametrize("cond", [1e1, 1e3, 1e5])
@pytest.mark.parametrize("m", [2, 3, 12])
def test_inverses(rng, m, cond):
    """R is really a square root, and Ri really whitens S."""
    S = random_spd(rng, m=m, cond=cond, n=100)
    tol = num_tol(amplification=cond)

    R = spd_sqrt(S)
    assert rel_fro(R @ R, S).max() < tol

    Ri = spd_invsqrt(S)
    assert rel_fro(Ri @ S @ Ri, np.eye(m)).max() < tol


@pytest.mark.parametrize("cond", [1e1, 1e3, 1e5])
@pytest.mark.parametrize("m", [2, 3, 12])
def test_gmean_symmetry(rng, m, cond):
    """X # Y == Y # X.

    Exact as mathematics (Ando: the geometric mean is the largest Z with
    [[X, Z], [Z, Y]] >= 0, manifestly symmetric in X and Y), so any residual
    measured here is PURE implementation error -- there is no modelling slack
    to hide in.

    g_mean decomposes only its FIRST argument, so the two calls run entirely
    different arithmetic. Amplification is cond**2: the intermediate
    X**(-1/2) @ Y @ X**(-1/2) sandwiches a different matrix, nothing cancels,
    and its condition number reaches kappa(X) * kappa(Y).

    NOT swept to cond=1e8: there eps*kappa**2 ~ 1, the intermediate goes
    numerically indefinite, and spd_sqrt's strict guard raises before any
    number comes back. That is the guard working, not a bug -- but it is a
    hard ceiling on g_mean in float64 and it constrains B1.3 (AIRM).
    """
    X = random_spd(rng, m=m, cond=cond, n=200)
    Y = random_spd(rng, m=m, cond=cond, n=200)
    assert rel_fro(g_mean(X, Y), g_mean(Y, X)).max() < num_tol(amplification=cond**2)
