# Parent RFM versus RFD on paired regular BW draws

## Verdict

RFD is not a universal efficiency improvement. It pays a finite-sample
price when the centre is fixed or when drift lies inside the loading
space, but decisively improves recovery when drift has mixed, orthogonal,
or curved components outside that space.

## Recorded matrix

- 576/576 paired draws completed; no duplicate keys, failures, fallbacks,
  nonconverged RFD stages, or nonfinite primary metrics.
- Each draw used known rank two and the same two lags for RFD and the
  cloned parent `rfm_bws`.
- Sample sizes were 240, 512, 2,048, and 8,192 with 24 paired replicates
  in six regular BW regimes.

## Primary latent-signal result

Median RFD error reduction relative to parent RFM:

| regime | n=240 | n=8192 | paired wins |
|---|---:|---:|---:|
| parent home | -11.7% | -1.0% | 0/96 |
| fixed control | -11.8% | -1.0% | 0/96 |
| aligned | -13.0% | -1.0% | 0/96 |
| mixed | +38.7% | +42.5% | 96/96 |
| orthogonal | +49.8% | +57.8% | 96/96 |
| curved | +45.0% | +55.8% | 96/96 |

At n=8,192, RFD reduced loading-projector error by 96.3%, 98.3%,
and 97.9% in the mixed, orthogonal, and curved regimes. In the same
cells it reduced latent-signal RMS by 42.5%, 57.8%, and 55.8%.

The fixed/home/aligned penalty shrank from roughly 12% at n=240 to
roughly 1% at n=8,192. This is the correct placebo behavior: extra
moving-centre machinery does not manufacture a win where it is not needed.

## Identification result

The aligned cell is the key boundary. At n=8,192, RFD reduces centre-path
error by 60.5%, yet parent RFM retains about a 1% reconstruction
advantage at n=8,192. Centre drift inside the loading space can be absorbed
as common movement, so better centre estimation alone does not establish a
better scientific decomposition. Relative centre gains are not reported for
the two fixed-centre controls because their parent denominator tends to zero.

## Rate and numerical health

The six empirical RFD centre exponents range from
0.370 to
0.410, close to the robust 3/7
reference over this finite grid. The smallest observed eigenvalue was
0.034.

Replacing the parent's published stochastic mean budget with the verified
global mean changed median latent-signal RMS by only
0.0007% (95th percentile
0.0095%). The verdict is not
an artefact of the parent's mean budget.

## Boundary

These are in-sample known-rank recovery and reconstruction results on a
regular synthetic BW design. They are not forecasting results, automatic
rank-selection evidence, or APP-FIN performance.

Approximate eight-worker compute implied by summed task time: 9.8 hours.

The interactive figure source is
`notebooks/parent_rfd_bw_parity_plot_lab.ipynb`.
