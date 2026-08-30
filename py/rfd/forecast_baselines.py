"""Causal covariance-forecast baselines for the hourly application.

LOCF and EWMA operate directly on SPD matrices.  The HAR baseline models each
coordinate of the symmetric matrix logarithm from its hourly, daily, and weekly
history, then maps the forecast back with the matrix exponential.  This is a
small classical benchmark, not a learned competitor or an RFD component.
"""

from dataclasses import dataclass

import numpy as np

from rfd.spd.linalg import spd_exp, spd_log, sym


Array = np.ndarray


def _validate_panel(observations: Array, *, minimum: int = 1) -> Array:
    observations = np.asarray(observations, dtype=float)
    if (
        observations.ndim != 3
        or observations.shape[0] < minimum
        or observations.shape[1] != observations.shape[2]
        or not np.isfinite(observations).all()
    ):
        raise ValueError("observations must be a finite n-by-m-by-m array")
    if np.any(np.linalg.eigvalsh(observations) <= 0.0):
        raise ValueError("observations must be strictly positive definite")
    return observations


def locf_forecasts(previous: Array, revealed_targets: Array) -> Array:
    """Forecast each target by the most recently revealed covariance."""
    targets = _validate_panel(revealed_targets)
    previous = np.asarray(previous, dtype=float)
    if previous.shape != targets.shape[1:] or np.any(np.linalg.eigvalsh(previous) <= 0.0):
        raise ValueError("previous must be one SPD matrix of the target size")
    return np.concatenate((previous[None], targets[:-1]), axis=0)


def ewma_forecasts(training: Array, revealed_targets: Array, decay: float) -> Array:
    """Issue causal EWMA forecasts, updating only after each target is seen."""
    training = _validate_panel(training)
    targets = _validate_panel(revealed_targets)
    if training.shape[1:] != targets.shape[1:]:
        raise ValueError("training and target matrices must have the same size")
    if not np.isfinite(decay) or not 0.0 < decay < 1.0:
        raise ValueError("decay must lie strictly between zero and one")
    state = training[0].copy()
    for observation in training[1:]:
        state = decay * state + (1.0 - decay) * observation
    forecasts = np.empty_like(targets)
    for index, observation in enumerate(targets):
        forecasts[index] = state
        state = decay * state + (1.0 - decay) * observation
    return forecasts


def symmetric_coordinates(matrices: Array) -> Array:
    matrices = np.asarray(matrices, dtype=float)
    if matrices.ndim < 2 or matrices.shape[-1] != matrices.shape[-2]:
        raise ValueError("matrices must end in equal square axes")
    indices = np.triu_indices(matrices.shape[-1])
    return matrices[..., indices[0], indices[1]]


def symmetric_matrices(coordinates: Array, size: int) -> Array:
    coordinates = np.asarray(coordinates, dtype=float)
    expected = size * (size + 1) // 2
    if coordinates.shape[-1] != expected:
        raise ValueError("coordinate dimension does not match matrix size")
    output = np.zeros(coordinates.shape[:-1] + (size, size), dtype=float)
    indices = np.triu_indices(size)
    output[..., indices[0], indices[1]] = coordinates
    output[..., indices[1], indices[0]] = coordinates
    return output


@dataclass(frozen=True)
class LogHARFit:
    """Coordinatewise log-SPD HAR with fixed hourly/daily/weekly windows."""

    coefficients: Array
    matrix_size: int
    daily_window: int
    weekly_window: int


def fit_log_har(
    training: Array,
    *,
    daily_window: int = 24,
    weekly_window: int = 168,
) -> LogHARFit:
    training = _validate_panel(training, minimum=weekly_window + 2)
    if not 1 < daily_window < weekly_window < training.shape[0]:
        raise ValueError("HAR windows must be ordered inside the training sample")
    logs = symmetric_coordinates(spd_log(training))
    responses = logs[weekly_window:]
    coefficients = np.empty((logs.shape[1], 4), dtype=float)
    for coordinate in range(logs.shape[1]):
        series = logs[:, coordinate]
        features = np.column_stack((
            np.ones(responses.shape[0]),
            series[weekly_window - 1:-1],
            np.asarray([
                series[index - daily_window:index].mean()
                for index in range(weekly_window, series.size)
            ]),
            np.asarray([
                series[index - weekly_window:index].mean()
                for index in range(weekly_window, series.size)
            ]),
        ))
        coefficients[coordinate] = np.linalg.lstsq(
            features, responses[:, coordinate], rcond=None
        )[0]
    return LogHARFit(
        coefficients=coefficients,
        matrix_size=int(training.shape[1]),
        daily_window=int(daily_window),
        weekly_window=int(weekly_window),
    )


def forecast_log_har(
    fit: LogHARFit,
    training: Array,
    revealed_targets: Array,
) -> Array:
    """Forecast sequentially; target t enters the history only after forecast t."""
    training = _validate_panel(training, minimum=fit.weekly_window)
    targets = _validate_panel(revealed_targets)
    if training.shape[1] != fit.matrix_size or targets.shape[1] != fit.matrix_size:
        raise ValueError("HAR fit and panels have different matrix sizes")
    history = list(symmetric_coordinates(spd_log(training)))
    target_logs = symmetric_coordinates(spd_log(targets))
    forecasts = []
    for target_log in target_logs:
        values = np.asarray(history)
        feature = np.stack((
            np.ones(values.shape[1]),
            values[-1],
            values[-fit.daily_window:].mean(axis=0),
            values[-fit.weekly_window:].mean(axis=0),
        ), axis=1)
        predicted = np.sum(feature * fit.coefficients, axis=1)
        forecasts.append(predicted)
        history.append(target_log)
    log_matrices = symmetric_matrices(np.asarray(forecasts), fit.matrix_size)
    return sym(spd_exp(sym(log_matrices), strict=False))
