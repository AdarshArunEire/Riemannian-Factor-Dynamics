"""Fit a small covariance series: python examples/quickstart.py."""

import numpy as np

from rfd.geometry import AIRM_GEOMETRY
from rfd.model import RFDConfig, fit_rfd


def main() -> None:
    time = np.linspace(0, 1, 96)
    tangent = np.zeros((len(time), 2, 2))
    tangent[:, 0, 0] = 0.25 * time
    tangent[:, 1, 1] = -0.15 * time
    tangent[:, 0, 1] = tangent[:, 1, 0] = 0.04 * np.sin(12 * np.pi * time)
    covariances = AIRM_GEOMETRY.exp(np.eye(2), tangent)

    fit = fit_rfd(
        covariances,
        time,
        AIRM_GEOMETRY,
        RFDConfig(bandwidth=0.2, n_cells=4, max_lag=2,
                  rank_method="fixed", rank=1),
    )
    print(f"Covariances: {covariances.shape}")
    print(f"Factor scores: {fit.factor_scores.shape}")
    print(f"Reconstructed covariances: {fit.reconstructed_observations.shape}")
    rms = np.sqrt(np.mean(AIRM_GEOMETRY.dist2(
        covariances, fit.reconstructed_observations)))
    print(f"Intrinsic reconstruction RMS: {rms:.6f}")


if __name__ == "__main__":
    main()
