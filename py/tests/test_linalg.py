from rfd.dgp.spd import random_spd
from rfd.spd.linalg import *
from tests.conftest import num_tol
import numpy as np
import pytest

@pytest.fixture
def rng():
    return np.random.default_rng(20260816)

@pytest.mark.parametrize("m", [2, 3, 12])
def test_round_trip(rng, m):
    A = random_spd(rng, m=m, cond=10.0, n=100)
    B = spd_exp(spd_log(A))
    np.testing.assert_allclose(B, A, rtol=1e-12, atol=1e-14)

@pytest.mark.parametrize("m", [2, 3, 12])
def test_inverses(rng, m):
    cond = 10.0
    S = random_spd(rng, m=m, cond=cond, n=100)
    tol = num_tol(kappa=cond)

    A = spd_sqrt(S)
    rel = np.linalg.norm(A @ A - S, axis=(-2, -1)) / np.linalg.norm(S, axis=(-2, -1))
    assert rel.max() < tol

    B = spd_invsqrt(S)
    rel = np.linalg.norm(B @ S @ B - np.eye(m), axis=(-2, -1)) / np.sqrt(m)
    assert rel.max() < tol
