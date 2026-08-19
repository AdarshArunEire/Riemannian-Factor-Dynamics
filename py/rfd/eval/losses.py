"""Evaluation losses for covariance forecasts.

B1.4. Five losses, and they are not five of the same thing.

FOUR ARE SQUARED DISTANCES -- Frobenius, Bures-Wasserstein, affine-invariant,
log-Euclidean. Symmetric, zero iff the arguments agree, and each induces a
different notion of "close". P1-LOSS is the claim that this choice is not
innocent, so having all four behind one interface is the point of the module.

THE FIFTH, QLIKE, IS NOT A DISTANCE. It comes from the Gaussian likelihood
and it is ASYMMETRIC: qlike(H, S) != qlike(S, H). That asymmetry is a
feature -- it penalises under-forecasting variance harder than
over-forecasting, which is why it is standard in volatility forecasting --
but it means argument order silently changes the answer.

    ARGUMENT ORDER, EVERYWHERE IN THIS MODULE:  loss(H, S)
        H   the FORECAST / model output / the thing being judged
        S   the TARGET  / realisation    / the thing judged against

The four distances do not care. QLIKE does. One convention for all five so
that swapping a loss never silently swaps a meaning.

Log-Euclidean vs AIRM. They agree exactly when A and B commute and differ
otherwise, so log-Euclidean is the flat approximation to AIRM. It is also
much cheaper: its barycentre is a closed form, no iteration at all.
"""

import numpy as np

from rfd.spd.linalg import sym, spd_log, spd_exp
from rfd.spd.bw import bw_dist2
from rfd.spd.airm import airm_dist2


def frobenius_loss(H, S):
    """Squared Frobenius distance ||H - S||_F^2.

    The flat loss -- no geometry at all. Its barycentre is the arithmetic
    mean, which is why it is the natural null against which the curved
    losses are compared.
    """
    return np.linalg.norm(H - S, axis=(-2, -1)) ** 2


def bw_loss(H, S, strict=True):
    """Squared Bures-Wasserstein distance. Thin wrapper -- see rfd.spd.bw."""
    return bw_dist2(H, S, strict)


def airm_loss(H, S, strict=True):
    """Squared affine-invariant distance. Thin wrapper -- see rfd.spd.airm."""
    return airm_dist2(H, S, strict)


def logeuclid_loss(H, S, strict=True):
    """Squared log-Euclidean distance || log H - log S ||_F^2.

    Equals the AIRM loss exactly when H and S commute, and is strictly
    smaller otherwise -- log-Euclidean flattens the cone by taking logs
    once, so it never sees the curvature AIRM follows.

    Invariant under orthogonal conjugation and under joint scaling, but NOT
    under general congruence. That is the concrete difference from AIRM and
    it is worth testing rather than asserting.
    """
    return np.linalg.norm(spd_log(H, strict) - spd_log(S, strict),
                          axis=(-2, -1)) ** 2


def qlike_loss(H, S):
    """Multivariate QLIKE:  tr(H^-1 S) - log det(H^-1 S) - m.

    NOT a distance. Asymmetric by construction, and that is the point.

    Non-negative, zero iff H == S: writing the eigenvalues of H^-1 S as
    lambda_i, the expression is sum_i (lambda_i - log lambda_i - 1), and
    x - log x - 1 >= 0 with equality only at x = 1.

    Computed as trace(solve(H, S)) - (logdet S - logdet H) - m. Two reasons
    not to form H^-1 S and take its determinant directly: the product is not
    symmetric, and slogdet on each argument separately avoids the overflow
    that log(det(...)) invites at m=12 with a spread spectrum.
    """
    H = np.asarray(H)
    S = np.asarray(S)
    m = H.shape[-1]

    tr = np.trace(np.linalg.solve(H, S), axis1=-2, axis2=-1)
    _, ldS = np.linalg.slogdet(S)
    _, ldH = np.linalg.slogdet(H)
    return tr - (ldS - ldH) - m


def logeuclid_barycentre(S, strict=True):
    """Log-Euclidean barycentre:  exp( mean_i log S_i ).

    Closed form. No iteration, no tolerance, no convergence flag -- which is
    the whole reason it exists alongside bw_barycentre and airm_barycentre.
    It returns a bare matrix rather than a result tuple because there is no
    diagnostic to report.

    S has shape (N, m, m); the mean is over axis 0.
    """
    return sym(spd_exp(sym(spd_log(np.asarray(S), strict).mean(axis=0)),
                       strict=False))


LOSSES = {
    "frobenius": frobenius_loss,
    "bw": bw_loss,
    "airm": airm_loss,
    "logeuclid": logeuclid_loss,
    "qlike": qlike_loss,
}
"""Registry, so an experiment can sweep losses by name rather than by import.

The whole reason B1.4 comes before the reproduction: the predeclaration's
highest_value_check asks which of these ranks RFM against LFM/LOCF/EWMA in
the parent's own scripts, and whether two of them ever disagree. That sweep
wants a dict, not five imports.
"""
