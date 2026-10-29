# Riemannian Factor Dynamics

How do the risks of a group of assets move together, when the market's
"normal" level of risk is itself changing?

A covariance matrix records how much each asset moves and how assets move
together. Watching one over time, two things happen at once: a slow drift in
what counts as normal, and shorter-lived swings around it that many assets
share. Factor models try to pull out those shared swings.

The [Riemannian factor model (RFM)](https://arxiv.org/abs/2607.28385) of
Huang, Chen and Chen does this while respecting the geometry of covariance
matrices, but it measures every swing against one fixed "normal". If normal
drifts, that drift gets mixed into the factors.

**RFD lets the baseline move.** It tracks a path of baselines over time,
measures each observation against the baseline at that moment, and lines
those measurements up so they can be compared before finding the factors.

The question here is simple: when does letting the baseline move make a
difference?

## Results

### When the baseline drifts somewhere the factors can't reach, RFD helps a lot

![Signal error reduction of RFD versus parent RFM in six simulated settings.](results/figures/synthetic_boundary.png)

*Simulated covariance series where the truth is known. When the baseline
drifts in a direction the factors cannot describe, RFD's error is 42–58%
lower, and it wins every one of 288 paired runs. When the baseline is fixed,
or drifts in a direction the factors can absorb, the parent model is about 1%
better. Median at 8,192 observations, true number of factors given to both.
[Full report](results/synthetic/report.md)*

The "drift inside factor space" row is the subtle one: RFD finds the baseline
60% more accurately there, yet reconstructs no better, because the parent's
factors quietly absorb the drift. Which movement counts as baseline and which
as factor is partly a modelling choice, set here by how smoothly the baseline
may move.

### On real crypto data, RFD beats the parent on average, but simple methods still win

![Next-hour forecast loss of each method relative to the best, on four measures.](results/figures/crypto_benchmarks.png)

*One-hour-ahead forecasts of 20 × 20 covariance matrices for 20 crypto assets,
every hour of 2025, with all choices made on 2024 data. RFD (teal) has lower
average loss than the parent RFM (purple) on all four measures, but the
difference is within noise, so formally it is a tie. Classical methods (grey)
lead every measure. [Full report](results/crypto/report.md)*

![RFD versus parent RFM on average and typical hours.](results/figures/crypto_mean_median.png)

*RFD wins on the average hour but loses slightly on the typical hour for three
of the four measures. That
pattern means its gains come from a minority of hours where the parent makes
large errors. These compare each model's own mean and median, not hour-by-hour
differences.*

## Install and try it

Python 3.10 or newer.

```bash
git clone https://github.com/AdarshArunEire/Riemannian-Factor-Dynamics.git
cd Riemannian-Factor-Dynamics
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -e .
python examples/quickstart.py
```

To fit your own sequence:

```python
import numpy as np
from rfd import BW_GEOMETRY, RFDConfig, fit_rfd

covariances = np.load("covariances.npy")  # (n, m, m), symmetric positive definite
time = np.linspace(0, 1, len(covariances))

fit = fit_rfd(covariances, time, BW_GEOMETRY,
              RFDConfig(bandwidth=0.2, n_cells=4, max_lag=2, rank_method="fixed", rank=2))

fit.factor_scores, fit.loadings, fit.centre.polygon, fit.reconstructed_observations
```

`bandwidth` is in the units of `time`, `n_cells` sets the number of segments in
the centre path, and `max_lag` sets how many lags enter factor extraction.
`AIRM_GEOMETRY` and `SPHERE_GEOMETRY` are also available.

## Layout

```
rfd/            the package
  model.py      fit_rfd: centre path → transport → factors → reconstruction
  forecast.py   forecasting, baselines and losses
  simulate.py   synthetic data generators
  data.py       minute bars to hourly covariance matrices
  _maths/       geometry and estimators used by the model
experiments/    scripts that produce the results above
results/        reports, tables and figures
tests/
```

## Reproduce

```bash
pip install -e ".[test]"
pytest                               # unit tests
python experiments/figures.py        # redraw the figures from results/
```

**Synthetic comparison.** Needs R, the packages in `renv.lock` and the parent's
code (see [reference/README.md](reference/README.md)). The full run took about
10 hours on eight workers.

```bash
Rscript -e "renv::restore(prompt = FALSE)"
python experiments/synthetic.py --profile smoke --check-r
python experiments/synthetic.py --profile overnight --workers 8
python experiments/synthetic.py --analyze
```

**Crypto study.** Downloads Binance public minute data, then runs four stages.
This is a substantial download and compute run.

```bash
pip install -e ".[experiments]"
python experiments/crypto/data.py --profile full
python experiments/crypto/centre.py
python experiments/crypto/representation.py
python experiments/crypto/forecast.py
```

## Licence

AGPL-3.0. The parent model is the work of Shuo-Chieh Huang, Rong Chen and
Yaqing Chen; this repository builds on their paper and does not include their
code.
