---
type: historical
title: Future programme ideation — identifiable geometric learning for RFD
aliases:
  - Geometric masked RFD
  - Self-supervised RFD
  - Task-aware RFD
status: historical
verdict: archived expanded masked-learning ideation; the live application programme is the canonical factor-score, predictive-rank, and online RFD note
last-audited: 2026-08-25
area:
  - geometry
  - self-supervised-learning
  - time-series
  - factor-models
tags:
  - idea
  - future-programme
  - machine-learning
---

# Future programme ideation — identifiable geometric learning for RFD

> **Archived expanded ideation, not a separate canonical programme.** The live
> scope is [[Future application programme — factor scores, predictive rank, and online RFD]]
> on the same fixed-loading RFD branch as Paper 1; it is not part of the
> moving-loading-subbundle programme. Parent:
> [[Paper 1 — Locally stationary Riemannian factor model]]. Governing boundaries:
> [[P1-ID — centre-drift and factor identification boundary]] and
> [[P1-LOSS — forecast-evaluation geometry and proxy-robustness boundary]].
> Masked/learned extensions remain outside Paper 1, while the compact causal
> APP-FIN forecast-rank comparator is now explicitly inside its numerical scope.
> Novelty is provisional until a dedicated literature audit is complete.

## Research question

Can backpropagation learn nonlinear predictive structure in a manifold-valued time series while preserving the scientific decomposition that makes RFD interpretable?

The worthwhile version is not “apply a neural network to SPD matrices.” It is:

1. mask information the model must genuinely predict;
2. make the model reconstruct that information through a moving centre, transported loading space, and factor dynamics;
3. enforce the symmetries and identification boundary of RFD in the architecture or objective; and
4. prove what the population minimisers identify.

## Fixed scientific object; floating engineering choices

**Fixed for the first attack**

- the RFD split into a moving centre, persistent transported tangent directions, amplitudes, and residual noise;
- common-frame gauge equivariance: rotating the reference tangent basis may rotate coordinates but cannot change the reconstructed manifold observation or forecast;
- geometric transport consistency along the estimated centre polygon;
- the P1-ID equivalence class as the maximum recoverable target;
- proxy-aware training and evaluation whenever an observed covariance is only a noisy proxy for a latent conditional covariance.

**Allowed to float during problem selection**

- transformer, state-space, recurrent, or masked-autoencoder implementation;
- exact masking distribution;
- AIRM, Bures–Wasserstein, flat Hilbert, or spherical application;
- supervised outcome, if any;
- whether the nonlinear dynamics act on factors, centre velocity, or both.

Fixing the scientific estimand while floating the neural implementation prevents an architecture search from silently changing the question.

## Lead route — identifiable geometric masked RFD

For a masked block of times $B$, let the visible observations be $X_{B^c}$. A geometric encoder produces context $h$ and two structured heads:

$$
\widehat\mu_t=G_\theta^{\mu}(h,t),
\qquad
\widehat f_t=G_\theta^{f}(h,t),
\qquad t\in B.
$$

The decoder is not a free Euclidean output layer. It reconstructs through the RFD geometry,

$$
\widehat X_t
=
\operatorname{Exp}_{\widehat\mu_t}
\left[
\mathcal P_{\mu_0\to\widehat\mu_t}
\{\widehat A\widehat f_t\}
\right],
$$

with an explicit residual/noise head only if the target requires a predictive distribution. The centre head is smooth, the loading projector is lag-persistent, and the composed output is required to remain in the generated domain.

Training information must be genuinely withheld: contiguous future/past blocks, interior blocks, or structured variable masks. Randomly hiding entries that can be recovered algebraically from their duplicates is not self-supervision.

### What makes this more than learned coefficients

The model may learn nonlinear conditional distributions of centre velocity and factor evolution, but it must do so through:

- a geometric decoder rather than an unconstrained matrix output;
- transport consistency rather than unrelated tangent charts;
- projector/gauge-equivariant latent variables rather than coordinate-dependent “factors”;
- temporal masking rather than reconstruction of an input it was allowed to see; and
- an identification theorem rather than a claim that low prediction error uniquely discovers the centre/factor split.

## Identification boundary — the load-bearing theorem

Backpropagation cannot resolve observational equivalence. P1-ID already proves that centre drift and persistent factors are not always separately identified from the observed law. Therefore the desired theorem is of the form:

> Under the declared centre convention, frequency/persistence separation, generated-domain, and gauge conditions, every population minimiser of the masked objective recovers the P1-ID identified quotient; outside those conditions there exist observationally equivalent laws with identical optimal masked risk and different centre/factor decompositions.

The negative half is as important as the positive half. A trained network that reports a unique split on a P1-ID equivalence pair has learned a convention, leakage, or optimiser preference—not new information.

## Objective design and noisy covariance proxies

For latent-observation DGP experiments, an intrinsic reconstruction loss may be used if its estimand is stated. For realised covariance applications, however, the observed matrix may be only a noisy proxy for the latent conditional covariance. If the intended target is the conditional mean in the ordinary matrix coordinate, training and headline evaluation must use a loss consistent in that coordinate, such as squared Frobenius or multivariate QLIKE under the conditions in P1-LOSS. AIRM, Bures–Wasserstein, and log-Euclidean loss against that proxy generally learn a different, shrunken target.

This does not forbid geometry inside the network. It separates the geometry of the representation and decoder from the statistical functional elicited by the loss.

## Candidate branches

### A. Transported masked prediction — lead candidate

Mask time blocks and predict both centre motion and persistent factor motion through the geometric decoder above. This has the best combination of RFD-specific structure, self-supervised scale, and a sharp identification question.

**Potential verdicts**

- **strong win:** the constrained learner improves masked forecasting and its population minimisers recover the proved quotient;
- **useful module:** nonlinear factor dynamics help, but the full centre/factor joint learner does not;
- **negative theorem:** no masked objective can sharpen identification without extra views or interventions;
- **decoration:** gains disappear against an equally sized black-box or RFD plus a generic dynamics head.

### B. Transported multi-view/projector self-supervision

Construct two legitimate views using disjoint time windows, sensor/asset subsamples, or independent covariance proxies. Transport each view to a common reference and match loading **projectors** or predicted masked functionals, not coordinate-labelled factors. Use variance/covariance preservation or self-distillation to prevent collapse; do not assume arbitrary negative pairs are scientifically different.

The theorem target is view-consistency up to common gauge. The main risk is that an augmentation changes the estimand instead of preserving it.

### C. Supervised task-aware RFD

For a future outcome $Y$—portfolio risk, a stress event, seizure onset, or another scientifically defined target—estimate a transported tangent subspace that is simultaneously persistent and predictive:

$$
\mathcal L
=
\mathcal L_{\rm lag}
+\lambda\mathcal L_{\rm task},
$$

subject to intrinsic orthonormality, gauge equivariance, and a geometric reconstruction check. The new estimand is a minimal predictive transported tangent subspace, not merely a high-variance or highly persistent subspace.

This is likely an application-led later paper because the answer depends on the label and decision problem.

### D. Gauge-equivariant nonlinear state dynamics

Keep the Paper 1 estimator and learn only the transition law for centre velocity and factor scores. For a gauge change $Q$, the latent forecast must transform as $\widehat f\mapsto Q^*\widehat f$ while the decoded manifold forecast remains invariant. A Koopman, neural state-space, recurrent, or transformer head is admissible.

This is highly useful machinery but is probably not a paper by itself unless the equivariance, stability, uncertainty, or identification theorem is substantive.

### E. Changing-universe masked RFD

Mask assets, sensors, regions, or matrix blocks and learn a permutation/congruence-equivariant representation robust to entry and exit. This could connect RFD to large sensor, financial, genomic, or connectivity panels without pretending fixed total energy is automatic. It is high-impact and high-risk: partial observation can destroy SPD structure and may change the target.

## First falsification campaign

The programme earns further proof work only after these tests:

1. **P1-ID equivalence pairs.** Train on observationally equivalent DGPs. The method must fail to distinguish their decompositions unless the identifying information is supplied.
2. **Gauge test.** Apply a common orthogonal change of tangent frame. Latent coordinates may rotate; projectors, decoded forecasts, and losses must not change beyond numerical tolerance.
3. **Masked forecasting grid.** Compare fixed/moving centres, aligned/orthogonal drift, curved paths, persistent factors, and lag-correlated noise against RFD plus a linear dynamics model and a parameter-matched black box.
4. **Proxy-loss test.** Under noisy realised-covariance proxies, verify that proxy-robust losses target the declared conditional covariance and that geometric losses exhibit the P1-LOSS target shift.
5. **Collapse and augmentation test.** Check that multi-view representations retain factor rank and predictive information and that each view transformation preserves the estimand.
6. **Capacity placebo.** Match parameter count and training budget. A win due only to more parameters is an engineering result, not the proposed scientific contribution.

## Risk and impact assessment

| route | scientific impact | technical risk | decisive failure mode |
|---|---:|---:|---|
| identifiable masked geometric RFD | high | medium-high | no gain beyond capacity, or no quotient-recovery theorem |
| transported multi-view/projector learning | medium-high | high | views do not preserve the estimand or collapse persists |
| supervised task-aware RFD | medium-high | medium | entirely task-specific and loses interpretable dynamics |
| equivariant nonlinear dynamics head | medium alone; high as a module | medium | becomes “RFD features plus a forecaster” |
| changing-universe masked RFD | high | high | partial observation breaks identifiability/SPD validity |

## Explicit non-contributions

The following are benchmarks or engineering features, not the core paper:

- an MLP or transformer applied to $z_t$ or $f_t$ with no geometric or gauge constraint;
- an end-to-end neural Fréchet mean with no identification theorem;
- learning only a bandwidth, kernel, lag weight, or Richardson coefficient;
- training against a realised covariance proxy with an incompatible geodesic loss and calling the result a conditional-mean forecast;
- renaming a generic SPD network “RFD”; or
- claiming that prediction accuracy proves the learned centre/factor split is the true one.

## Relationship to the moving-loading programme

The two parked programmes are complementary, not duplicates. [[Parked programme — Intrinsically moving loading subspace]] asks whether the loading projector itself changes with rescaled time and currently needs cross-tangent algebra, localised concentration, and bootstrap closure. This programme asks whether nonlinear predictive structure can be learned while respecting the identified RFD quotient. A future model may combine them only after each programme's separate identification target is clear; otherwise a neural moving loading space can absorb centre error without diagnosis.

## External novelty anchors — provisional

- Bucci, Palma and Zhang, [*Geometric Deep Learning for Realized Covariance Matrix Forecasting*](https://arxiv.org/abs/2412.09517), already establishes that geometry-aware deep forecasting of realised covariance is an active baseline. The novelty cannot be “deep learning on SPD data.”
- Sonoda et al., [*Fully-Connected Network on Noncompact Symmetric Space and Its Generalization Capability*](https://proceedings.mlr.press/v162/sonoda22a.html), supplies a broad neural-network baseline on symmetric spaces including SPD manifolds.
- [SimMTM](https://arxiv.org/abs/2302.00861) and [Predictive Functional Masked Learning](https://arxiv.org/abs/2411.10087) are generic masked/self-supervised anchors. They do not by themselves establish the RFD identification, transport, or gauge claims proposed here.

A dedicated search must test the exact conjunction: moving-centre manifold factor identification + transport/gauge-equivariant masked prediction + proxy-correct covariance objective. Absence from the preliminary search is not a novelty proof.

## Decision rule

Proceed to theorem design only if the gauge and P1-ID falsification tests pass and the constrained learner beats both RFD plus a simple dynamics head and a parameter-matched black box on held-out masked/future observations. If only the dynamics head wins, retain it as Paper 1 follow-up software. If the learner appears to separate a P1-ID equivalence pair, stop and diagnose leakage before interpreting any result.
