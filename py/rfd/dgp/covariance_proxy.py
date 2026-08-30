"""Finite-window covariance proxies around known latent SPD centres."""

from __future__ import annotations

import numpy as np


Array = np.ndarray


def sample_covariance_proxies(
    rng: np.random.Generator,
    centres: Array,
    window_sizes: Array,
    *,
    distribution: str = "gaussian",
    student_degrees_of_freedom: float = 6.0,
) -> Array:
    """Draw unbiased sample-covariance observations around latent centres.

    Each observation is the ordinary demeaned covariance of ``window_sizes[t]``
    synthetic returns.  Gaussian draws give the Wishart proxy.  Standardised
    Student draws retain the same conditional covariance while adding the
    heavy tails absent from the original theorem-verification DGP.
    """
    centres = np.asarray(centres, dtype=float)
    window_sizes = np.asarray(window_sizes, dtype=int)
    if centres.ndim != 3 or centres.shape[1] != centres.shape[2]:
        raise ValueError("centres must have shape (n, m, m)")
    if window_sizes.shape != (centres.shape[0],):
        raise ValueError("window_sizes must have one entry per centre")
    if np.any(window_sizes <= centres.shape[1]):
        raise ValueError("every window must exceed matrix size for full-rank proxies")
    if distribution not in {"gaussian", "student_t"}:
        raise ValueError("distribution must be gaussian or student_t")
    if distribution == "student_t" and student_degrees_of_freedom <= 4.0:
        raise ValueError("Student degrees of freedom must exceed four")

    proxies = np.empty_like(centres)
    for index, (centre, count) in enumerate(zip(centres, window_sizes, strict=True)):
        root = np.linalg.cholesky(centre)
        standard = rng.standard_normal((int(count), centre.shape[0]))
        if distribution == "student_t":
            scales = np.sqrt(
                rng.chisquare(student_degrees_of_freedom, size=int(count))
                / student_degrees_of_freedom
            )
            standard = standard / scales[:, None]
            standard *= np.sqrt(
                (student_degrees_of_freedom - 2.0)
                / student_degrees_of_freedom
            )
        returns = standard @ root.T
        returns -= returns.mean(axis=0, keepdims=True)
        proxies[index] = returns.T @ returns / (int(count) - 1)
    return 0.5 * (proxies + proxies.mT)
