"""Small forecasting primitives shared by RFM/RFD experiments.

The parent application fits projected factor scores with an OLS VAR(1) with
intercept. This module implements exactly that normal-equation convention and
also supplies the first declared alternative: a linear Gaussian latent-score
model fitted by EM and filtered by Kalman recursions. Neither route claims that
projected scores are noise-free latent states.
"""

from dataclasses import dataclass

import numpy as np


Array = np.ndarray


@dataclass(frozen=True)
class VAR1Fit:
    """OLS VAR(1) fit with an intercept in the first coefficient row."""

    coefficients: Array
    residuals: Array

    @property
    def rank(self) -> int:
        return int(self.coefficients.shape[1])

    def forecast(self, last_score: Array) -> Array:
        """Issue one forecast from the supplied final observed score."""
        last_score = np.asarray(last_score, dtype=float)
        if last_score.shape != (self.rank,):
            raise ValueError("last_score must have one value per VAR component")
        if not np.isfinite(last_score).all():
            raise ValueError("last_score contains NaN or Inf")
        return np.concatenate(([1.0], last_score)) @ self.coefficients


def fit_var1(scores: Array) -> VAR1Fit:
    """Match the parent's VAR1 normal-equation implementation.

    For score rows f_1,...,f_n, solve

        [1, f_t] B ~= f_(t+1)

    by solve(Z.T @ Z, Z.T @ Y). A singular design is reported rather than
    silently regularised because the parent routine also uses an exact solve.
    """
    scores = np.asarray(scores, dtype=float)
    if scores.ndim != 2 or scores.shape[0] < 3 or scores.shape[1] < 1:
        raise ValueError("scores must be a finite n by r array with n >= 3")
    if not np.isfinite(scores).all():
        raise ValueError("scores contain NaN or Inf")

    response = scores[1:]
    design = np.column_stack((np.ones(scores.shape[0] - 1), scores[:-1]))
    gram = design.T @ design
    right = design.T @ response
    try:
        coefficients = np.linalg.solve(gram, right)
    except np.linalg.LinAlgError as error:
        raise np.linalg.LinAlgError(
            "VAR(1) normal equations are singular; no ridge was applied"
        ) from error
    residuals = response - design @ coefficients
    return VAR1Fit(coefficients=coefficients, residuals=residuals)


def forecast_var1(scores: Array) -> tuple[Array, VAR1Fit]:
    """Fit the parent-style VAR(1) and forecast one score row."""
    fit = fit_var1(scores)
    return fit.forecast(np.asarray(scores, dtype=float)[-1]), fit


@dataclass(frozen=True)
class StateSpaceFit:
    """Fitted identity-observation linear Gaussian score model.

    The model is

        x_t - mean = transition @ (x_(t-1) - mean) + process noise,
        score_t = x_t + measurement noise.

    ``x_t`` is the latent factor amplitude in the fitted score gauge.  The
    identity observation matrix is deliberate: projected scores are treated
    as noisy measurements of the amplitudes, not as a second loading problem.
    """

    mean: Array
    transition: Array
    process_covariance: Array
    measurement_covariance: Array
    initial_mean: Array
    initial_covariance: Array
    log_likelihood: float
    converged: bool
    n_iter: int

    @property
    def rank(self) -> int:
        return int(self.mean.size)


@dataclass(frozen=True)
class StateSpaceFilterResult:
    """Causal predictions and posterior states from a fixed state-space fit."""

    predicted_states: Array
    filtered_states: Array
    predicted_covariances: Array
    filtered_covariances: Array
    log_likelihood: float


def _validate_scores(scores: Array, *, minimum_rows: int = 3) -> Array:
    scores = np.asarray(scores, dtype=float)
    if (
        scores.ndim != 2
        or scores.shape[0] < minimum_rows
        or scores.shape[1] < 1
    ):
        raise ValueError(
            f"scores must be a finite n by r array with n >= {minimum_rows}"
        )
    if not np.isfinite(scores).all():
        raise ValueError("scores contain NaN or Inf")
    return scores


def _positive_covariance(matrix: Array, floor: float) -> Array:
    matrix = 0.5 * (np.asarray(matrix, dtype=float) + np.asarray(matrix).T)
    values, vectors = np.linalg.eigh(matrix)
    values = np.maximum(values, floor)
    return 0.5 * (
        (vectors * values) @ vectors.T + ((vectors * values) @ vectors.T).T
    )


def _stable_transition(matrix: Array, maximum_radius: float) -> Array:
    matrix = np.asarray(matrix, dtype=float)
    radius = float(np.max(np.abs(np.linalg.eigvals(matrix))))
    if radius > maximum_radius:
        matrix = matrix * (maximum_radius / radius)
    return matrix


def _kalman_pass(
    centred_scores: Array,
    transition: Array,
    process_covariance: Array,
    measurement_covariance: Array,
    initial_mean: Array,
    initial_covariance: Array,
) -> tuple[StateSpaceFilterResult, Array, Array]:
    """Run one causal Kalman pass and its RTS smoother.

    The two extra returned arrays are the smoothed states and covariances used
    internally by EM.  Public callers receive only causal quantities.
    """
    observations = np.asarray(centred_scores, dtype=float)
    n, rank = observations.shape
    identity = np.eye(rank)
    predicted = np.empty((n, rank))
    filtered = np.empty((n, rank))
    predicted_cov = np.empty((n, rank, rank))
    filtered_cov = np.empty((n, rank, rank))
    log_likelihood = 0.0

    prediction = np.asarray(initial_mean, dtype=float)
    covariance = np.asarray(initial_covariance, dtype=float)
    for index, observation in enumerate(observations):
        predicted[index] = prediction
        predicted_cov[index] = covariance
        innovation = observation - prediction
        innovation_covariance = covariance + measurement_covariance
        sign, logdet = np.linalg.slogdet(innovation_covariance)
        if sign <= 0.0 or not np.isfinite(logdet):
            raise np.linalg.LinAlgError(
                "Kalman innovation covariance is not positive definite"
            )
        solved = np.linalg.solve(innovation_covariance, innovation)
        log_likelihood -= 0.5 * (
            rank * np.log(2.0 * np.pi) + logdet + innovation @ solved
        )
        gain = np.linalg.solve(
            innovation_covariance, covariance.T
        ).T
        posterior = prediction + gain @ innovation
        remainder = identity - gain
        posterior_covariance = (
            remainder @ covariance @ remainder.T
            + gain @ measurement_covariance @ gain.T
        )
        posterior_covariance = 0.5 * (
            posterior_covariance + posterior_covariance.T
        )
        filtered[index] = posterior
        filtered_cov[index] = posterior_covariance
        prediction = transition @ posterior
        covariance = (
            transition @ posterior_covariance @ transition.T
            + process_covariance
        )
        covariance = 0.5 * (covariance + covariance.T)

    smoothed = filtered.copy()
    smoothed_cov = filtered_cov.copy()
    for index in range(n - 2, -1, -1):
        gain = np.linalg.solve(
            predicted_cov[index + 1],
            (filtered_cov[index] @ transition.T).T,
        ).T
        smoothed[index] += gain @ (
            smoothed[index + 1] - predicted[index + 1]
        )
        smoothed_cov[index] += gain @ (
            smoothed_cov[index + 1] - predicted_cov[index + 1]
        ) @ gain.T
        smoothed_cov[index] = 0.5 * (
            smoothed_cov[index] + smoothed_cov[index].T
        )

    result = StateSpaceFilterResult(
        predicted_states=predicted,
        filtered_states=filtered,
        predicted_covariances=predicted_cov,
        filtered_covariances=filtered_cov,
        log_likelihood=float(log_likelihood),
    )
    return result, smoothed, smoothed_cov


def fit_score_state_space(
    scores: Array,
    *,
    max_iter: int = 60,
    tolerance: float = 3e-4,
    covariance_floor: float = 1e-6,
    maximum_radius: float = 0.995,
) -> StateSpaceFit:
    """Fit a latent-score state-space model by guarded EM.

    The score mean is fixed at its training-sample value.  Covariance floors
    are relative to the average marginal score variance, and the transition
    matrix is radially restricted to the declared stable region.  These are
    numerical identification guards, not forecast-loss tuning parameters.
    """
    scores = _validate_scores(scores, minimum_rows=8)
    if max_iter < 1:
        raise ValueError("max_iter must be positive")
    if not np.isfinite(tolerance) or tolerance <= 0.0:
        raise ValueError("tolerance must be finite and positive")
    if not np.isfinite(covariance_floor) or covariance_floor <= 0.0:
        raise ValueError("covariance_floor must be finite and positive")
    if not np.isfinite(maximum_radius) or not 0.0 < maximum_radius < 1.0:
        raise ValueError("maximum_radius must lie strictly between zero and one")

    mean = scores.mean(axis=0)
    observations = scores - mean
    rank = scores.shape[1]
    empirical_covariance = np.cov(observations, rowvar=False, bias=True)
    empirical_covariance = np.atleast_2d(empirical_covariance)
    scale = max(
        float(np.trace(empirical_covariance) / rank),
        np.finfo(float).eps,
    )
    floor = covariance_floor * scale

    initial_var = fit_var1(observations)
    transition = _stable_transition(
        initial_var.coefficients[1:].T, maximum_radius
    )
    residual_covariance = np.cov(
        initial_var.residuals, rowvar=False, bias=True
    )
    residual_covariance = np.atleast_2d(residual_covariance)
    process_covariance = _positive_covariance(
        0.5 * residual_covariance, floor
    )
    measurement_covariance = _positive_covariance(
        0.5 * residual_covariance, floor
    )
    initial_mean = np.zeros(rank)
    initial_covariance = _positive_covariance(empirical_covariance, floor)

    previous_likelihood = -np.inf
    converged = False
    likelihood = -np.inf
    for iteration in range(1, max_iter + 1):
        causal, smoothed, smoothed_cov = _kalman_pass(
            observations,
            transition,
            process_covariance,
            measurement_covariance,
            initial_mean,
            initial_covariance,
        )
        likelihood = causal.log_likelihood
        expected = smoothed_cov + np.einsum(
            "ti,tj->tij", smoothed, smoothed
        )
        smoother_gain = np.empty((scores.shape[0] - 1, rank, rank))
        for index in range(scores.shape[0] - 1):
            smoother_gain[index] = np.linalg.solve(
                causal.predicted_covariances[index + 1],
                (causal.filtered_covariances[index] @ transition.T).T,
            ).T
        lag_covariance = np.einsum(
            "tij,tkj->tik", smoothed_cov[1:], smoother_gain
        )
        lag_expected = lag_covariance + np.einsum(
            "ti,tj->tij", smoothed[1:], smoothed[:-1]
        )
        previous_sum = expected[:-1].sum(axis=0)
        lag_sum = lag_expected.sum(axis=0)
        transition = np.linalg.solve(previous_sum.T, lag_sum.T).T
        transition = _stable_transition(transition, maximum_radius)

        process_terms = (
            expected[1:]
            - np.einsum("ij,tjk->tik", transition, lag_expected.transpose(0, 2, 1))
            - np.einsum("tij,kj->tik", lag_expected, transition)
            + np.einsum(
                "ij,tjk,lk->til", transition, expected[:-1], transition
            )
        )
        process_covariance = _positive_covariance(
            process_terms.mean(axis=0), floor
        )
        residual = observations - smoothed
        measurement_covariance = _positive_covariance(
            (
                smoothed_cov
                + np.einsum("ti,tj->tij", residual, residual)
            ).mean(axis=0),
            floor,
        )
        initial_mean = smoothed[0]
        initial_covariance = _positive_covariance(smoothed_cov[0], floor)

        improvement = likelihood - previous_likelihood
        if np.isfinite(previous_likelihood) and (
            abs(improvement) <= tolerance * (1.0 + abs(previous_likelihood))
        ):
            converged = True
            break
        previous_likelihood = likelihood

    final, _, _ = _kalman_pass(
        observations,
        transition,
        process_covariance,
        measurement_covariance,
        initial_mean,
        initial_covariance,
    )
    return StateSpaceFit(
        mean=mean,
        transition=transition,
        process_covariance=process_covariance,
        measurement_covariance=measurement_covariance,
        initial_mean=initial_mean,
        initial_covariance=initial_covariance,
        log_likelihood=final.log_likelihood,
        converged=converged,
        n_iter=iteration,
    )


def filter_score_state_space(
    scores: Array,
    fit: StateSpaceFit,
) -> StateSpaceFilterResult:
    """Apply a fixed score-state model causally to supplied observations."""
    scores = _validate_scores(scores, minimum_rows=1)
    if scores.shape[1] != fit.rank:
        raise ValueError("scores and fitted state rank disagree")
    causal, _, _ = _kalman_pass(
        scores - fit.mean,
        fit.transition,
        fit.process_covariance,
        fit.measurement_covariance,
        fit.initial_mean,
        fit.initial_covariance,
    )
    return StateSpaceFilterResult(
        predicted_states=causal.predicted_states + fit.mean,
        filtered_states=causal.filtered_states + fit.mean,
        predicted_covariances=causal.predicted_covariances,
        filtered_covariances=causal.filtered_covariances,
        log_likelihood=causal.log_likelihood,
    )


def forecast_score_state_space(
    scores: Array,
    fit: StateSpaceFit,
) -> tuple[Array, StateSpaceFilterResult]:
    """Filter an observed score prefix and issue its next latent-state forecast."""
    result = filter_score_state_space(scores, fit)
    last = result.filtered_states[-1]
    forecast = fit.mean + fit.transition @ (last - fit.mean)
    return forecast, result
