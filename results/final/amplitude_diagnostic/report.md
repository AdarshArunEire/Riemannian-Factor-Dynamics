# Low-n factor-amplitude diagnosis

**Complete paired diagnostic.**

## Reading the experiment

OT is the irreducible noisy-oracle floor. FT changes only the centre/frame rows; OF changes only the loading directions; FF changes both and is complete RFD. OO estimates loading directions from oracle rows. Contrasts are paired on identical draws.

The 2×2 numbers are descriptive contrasts of a nonlinear error metric, not variance shares and not a proof of causality.

## Automated read

- n=240: largest descriptive contrast is **centre/frame rows** (+0.683 NRMSE); one scalar removes 0.226 NRMSE.
- n=512: largest descriptive contrast is **centre/frame rows** (+0.465 NRMSE); one scalar removes 0.123 NRMSE.
- n=2,048: largest descriptive contrast is **centre/frame rows** (+0.204 NRMSE); one scalar removes 0.035 NRMSE.

## Scalar-damping test

The calibrated score permits only one post-hoc scalar after the usual orthogonal gauge alignment. A large reduction means uniform attenuation is important; a large remaining error means trajectory shape is also wrong. This diagnostic does not install or tune a correction.

## Outputs

- `summary.csv`: mean, median, and interquartile range by estimator variant.
- `paired_attribution.csv`: paired medians and bootstrap 95% intervals.
- `factor_score_attribution.png`: all estimator paths.
- `paired_error_attribution.png`: row/loading/interaction contrasts.
- `scalar_damping_diagnostic.png`: raw versus scalar-calibrated RFD.

Rows analysed: 192.