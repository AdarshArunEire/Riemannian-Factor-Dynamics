> **ARCHIVED RESEARCH NOTE — integrated 2026-08-19.** The durable mathematical boundary is now P1-ID §17; the citable Paper 1 interpretation is Remark P-DRIFT-\(\nu\); the experimental design is N-18c in the canonical numerical suite; and implementation is BUILD B4.1/B5.6. This note is preserved as the originating rationale. Its unconditional (n^{-3/14}) suggestion is superseded by the canon's conditional clean-quadratic statement: linear cross/base-change terms, aligned drift, curvature, persistence and the chosen risk can change or remove the crossover.

# Why $\nu$ matters — the static-centre breakdown threshold

## Core idea

Let $\nu$ control the strength of motion in the Fréchet-centre path $\mu_\nu(u)$.

A simple synthetic construction is

\[
\mu_\nu(u)
=
\operatorname{Exp}_{\mu_0}\{\nu g(u)V\},
\]

where $V$ fixes the direction of centre motion and $g(u)$ controls its shape through time.

Then $\nu$ has a clean interpretation:

- $\nu=0$: the centre is genuinely static;
- small $\nu$: weak centre drift;
- large $\nu$: increasingly strong violation of the static-centre assumption.

This makes $\nu$ more than a simulation parameter. It provides a controlled axis along which the assumption separating RFM from RFD can be broken.

## Why the threshold $\nu^\star$ matters

RFM has an advantage when the true centre is static because it estimates one pooled Fréchet centre. RFD is more flexible, but must estimate a moving path locally and therefore pays additional estimation variance and smoothing error.

When $\nu$ is very small, the misspecification incurred by RFM may be smaller than the estimation cost paid by RFD.

As $\nu$ grows, the opposite eventually becomes possible: the error caused by forcing the centre to remain static becomes larger than the cost of estimating a dynamic centre.

This suggests a crossover

\[
\nu^\star
=
\inf\left\{
\nu:
R_{\mathrm{RFD}}(\nu)
<
R_{\mathrm{RFM}}(\nu)
\right\},
\]

for an appropriate estimation or forecasting risk $R$.

Thus $\nu^\star$ is the **static-centre breakdown threshold**:

> the amount of genuine Fréchet-centre drift required before modelling the centre dynamically becomes worthwhile.

## Why this is more interesting than simply showing RFD wins

A result of the form

\[
R_{\mathrm{RFD}}<R_{\mathrm{RFM}}
\]

only shows that one estimator performed better in one design.

A threshold result asks a deeper question:

> **When is the static-centre assumption safe, and when does it begin to cost information?**

The useful scientific object is therefore not one numerical value of $\nu^\star$, but its dependence on the statistical problem:

\[
\nu^\star
=
\nu^\star
\left(
n,\,
\Delta,\,
\sigma_\varepsilon,\,
\text{factor persistence},\,
\text{drift orientation},\,
\text{geometry},\ldots
\right).
\]

This can reveal why static centring succeeds in some regimes and fails in others.

## Connection with the existing theory

The current theory already contains the beginning of such a boundary.

For the fixed-centre RFM, sufficiently small drift can be absorbed into the existing target-defect budget when its lag-row contribution is of the same order as the statistical error. In contrast, RFD pays the local-centre estimation rate

\[
\ell_n
=
b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}.
\]

At the robust bandwidth $b_n=n^{-1/7}$,

\[
\ell_n\asymp n^{-3/7}
\]

under the clean short-memory regime.

For a simple geodesic drift with displacement of order $\nu$, the pure drift contribution to a lag covariance is naturally quadratic:

\[
d_t=O(\nu)
\quad\Longrightarrow\quad
d_t\otimes d_{t+h}=O(\nu^2).
\]

This suggests that a first candidate boundary may arise from balancing

\[
\nu^2
\asymp
n^{-1/2}+\ell_n.
\]

If $\ell_n$ dominates, this heuristically gives

\[
\nu_n^\star
\asymp
n^{-3/14}.
\]

This is **not yet a theorem**. It is a concrete analytic conjecture to test against the synthetic phase diagram.

## Two thresholds may exist

There may be separate breakdown points for structural estimation and forecasting:

\[
\nu^\star_{\mathrm{est}}
\]

and

\[
\nu^\star_{\mathrm{forecast}}.
\]

The loading space could begin to suffer measurable contamination before forecast performance deteriorates materially, or forecasting could become sensitive before subspace estimation visibly fails.

This distinction may itself be scientifically informative.

For example:

> Static centring may remain adequate for prediction beyond the point at which it ceases to provide a faithful decomposition of centre drift and factor dynamics.

## What should be swept

The initial synthetic experiment should vary $\nu$ while keeping everything else fixed.

Then the sweep should be repeated over quantities likely to move the threshold:

- sample size $n$;
- factor eigengap $\Delta$;
- observation/noise energy;
- factor persistence;
- centre-path speed and shape;
- orientation of centre drift relative to the factor space;
- curvature / spectral conditioning in the SPD application.

The result should ideally be viewed as a **phase boundary**, not merely a benchmark table:

\[
\nu<\nu^\star
\quad\Rightarrow\quad
\text{static-centre restriction is worth keeping},
\]

\[
\nu>\nu^\star
\quad\Rightarrow\quad
\text{static-centre misspecification dominates}.
\]

## Intrinsic interpretation

Ultimately $\nu$ is only a convenient experimental knob.

The more intrinsic quantity is the motion of the centre path itself, for example its path energy

\[
\mathcal V_\mu^2
=
\int_0^1
\|\dot\mu(u)\|_{\mu(u)}^2\,du
\]

or its total path length

\[
\mathcal L_\mu
=
\int_0^1
\|\dot\mu(u)\|_{\mu(u)}\,du.
\]

For the simple family $\mu_\nu(u)=\operatorname{Exp}_{\mu_0}\{\nu g(u)V\}$, these scale directly with $\nu$, so $\nu$ remains an ideal simulation parameter.

The eventual theoretical goal is therefore not merely to estimate a particular $\nu^\star$, but to characterise:

> **how much intrinsic Fréchet-centre motion can be ignored before the static-centre approximation becomes statistically or predictively costly.**

That is the main reason $\nu^\star$ is important.
