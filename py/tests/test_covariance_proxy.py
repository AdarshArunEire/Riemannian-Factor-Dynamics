import numpy as np
import pytest

from rfd.dgp.covariance_proxy import sample_covariance_proxies


def test_covariance_proxies_are_symmetric_positive_definite() -> None:
    centres = np.broadcast_to(np.diag([1.0, 2.0]), (40, 2, 2)).copy()
    result = sample_covariance_proxies(
        np.random.default_rng(11), centres, np.full(40, 8), distribution="gaussian"
    )
    assert result.shape == centres.shape
    assert np.allclose(result, result.mT)
    assert np.linalg.eigvalsh(result).min() > 0.0


def test_student_proxies_preserve_covariance_in_expectation() -> None:
    centre = np.array([[1.0, 0.25], [0.25, 2.0]])
    centres = np.broadcast_to(centre, (2000, 2, 2)).copy()
    result = sample_covariance_proxies(
        np.random.default_rng(12), centres, np.full(2000, 30),
        distribution="student_t", student_degrees_of_freedom=6.0,
    )
    assert np.allclose(result.mean(axis=0), centre, atol=0.07)


@pytest.mark.parametrize("distribution", ["bad", "student_t"])
def test_covariance_proxy_rejects_invalid_contract(distribution: str) -> None:
    centres = np.broadcast_to(np.eye(2), (3, 2, 2)).copy()
    kwargs = {"distribution": distribution}
    if distribution == "student_t":
        kwargs["student_degrees_of_freedom"] = 4.0
    with pytest.raises(ValueError):
        sample_covariance_proxies(
            np.random.default_rng(1), centres, np.full(3, 3), **kwargs
        )
