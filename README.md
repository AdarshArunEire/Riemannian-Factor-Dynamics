# Riemannian Factor Dynamics

Factor models for sequences of covariance matrices whose baseline moves over
time.

RFD extends the Riemannian factor model (RFM) of
[Huang, Chen and Chen (2026)](https://arxiv.org/abs/2607.28385). RFM measures
every observation against one Fréchet mean and extracts factors from the
lagged dependence of the deviations. RFD replaces that single centre with an
estimated centre path, transports the deviations along the path into a common
tangent frame, and then extracts the factors in the same way.

The question this repository studies is when that change matters.

## Results

**Synthetic data.** On paired Bures–Wasserstein simulations with known rank,
RFD reduces median latent-signal error by 42.5–57.8% at n = 8,192 when the
centre drifts outside the factor space. When the centre is fixed, or its drift
lies inside the factor space, the parent model is about 1% better. These are
in-sample recovery results.

![RFD reduces signal error when the centre drift leaves the factor space and costs about 1% otherwise.](results/figures/synthetic_boundary.png)

In the aligned case RFD estimates the centre path 60.5% more accurately, yet
the parent still reconstructs slightly better: drift inside the factor space
can be absorbed by the factors. Separating the baseline from the factors needs
an assumption, here the bandwidth of the centre path.
[Full report](results/synthetic/report.md)

**Hourly crypto covariances.** One-hour-ahead forecasts of 20 × 20 realised
covariance matrices for every hour of 2025, with all choices made on 2024.
RFD's mean loss is lower than the parent's on four measures, but the paired
intervals cross zero, so the comparison is a statistical tie. Log-SPD HAR and
EWMA remain the strongest methods.

![Average forecast losses relative to the best method.](results/figures/crypto_benchmarks.png)

[Full report](results/crypto/report.md)

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
