# One-hour covariance forecasts for 20 crypto assets

The frozen comparison covers all 8,760 hours of 2025. RFD and parent RFM use
the same rank-19 VAR(1) score head. Their representations refit every four
weeks on the trailing 26 weeks; forecasts use only information available at
their origin. EWMA tuning uses 2024 only. Last observation, EWMA and log-SPD
HAR are the external baselines.

RFD lowers mean loss versus parent RFM by **2.48% under squared Frobenius,
13.26% under QLIKE, 2.18% under squared Bures–Wasserstein, and 7.69% in realised
minimum-variance portfolio variance**. Log-SPD HAR has the lowest mean
Frobenius, BW and portfolio losses; EWMA has the lowest mean QLIKE.

The formal RFD/RFM verdict is a tie: both primary paired-loss intervals cross
zero. This means the study does not establish a forecasting advantage, not
that it establishes equivalence.

| Primary loss | Mean RFD minus parent | 95% Newey–West interval |
|---|---:|---:|
| Squared Frobenius | −2.57904 | [−7.58776, +2.42967] |
| QLIKE | −4.61754 | [−10.8746, +1.63953] |

The intervals use Bartlett weights and up to 168 hourly lags. BW and portfolio
variance are secondary diagnostics.

## The mean and median tell different stories

Mean losses fall on all four measures. Median losses rise by 6.52%, 2.24%
and 2.90% under Frobenius, QLIKE and BW; median portfolio variance falls by
0.07%. These are ratios of each method's separate loss summaries, not medians
of paired hourly percentage changes. The contrast suggests a role for
large-error hours; it does not identify a market-stress mechanism.

## Source of the public extracts

- `headline_losses.csv`: the five frozen headline rows from
  `results/intermediate/hf4_crypto_forecast/performance.csv`.
- `rfd_vs_parent.csv`: the mean and median contrasts from
  `simple_average_vs_typical.csv`, with mean-difference intervals from
  `simple_rfd_vs_rfm.csv`. The interval endpoints are scaled by the observed
  parent mean; they are not separately estimated ratio confidence intervals.
- Experiment: [`run_hf4_forecast.py`](../../../experiments/run_hf4_forecast.py).
- Frozen configuration: [`hf4_forecast.yaml`](../../../config/hf4_forecast.yaml).

Only the original VAR(1) comparison is included. Later coordinatewise HAR and
ridge-VHAR score-head experiments remain outside this result. The tracked
extracts regenerate the README plots; the full hourly losses and raw market
data are not bundled with this repository.
