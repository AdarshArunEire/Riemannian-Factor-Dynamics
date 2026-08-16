---
type: canonical-proof
title: BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary
status: canonical-proof
last-audited: 2026-08-12
verdict: the safeguarded fixed-size BW statistical theorem and the fixed-margin matrix-size-uniform geometry producer are proved; growing-size statistical conclusions require separate energy, dependence, target, and gap producers
---

# BW-FIXED-MARGIN — canonical local and size-uniform theorem boundary

> **Scope boundary.** This file contains two proved results at different levels. For fixed matrix size, the localized/regularized full-rank estimator has a complete robust statistical theorem. For growing matrix size on fixed compatible margins, the quotient and generated-map geometry is dimension-uniform. The second result does not itself supply energy, concentration, lag factorisation, signal, or an eigengap.

## 1. Estimator and domain actually proved

The observation space is the full-rank manifold \({\rm SPD}(m)\), represented by the free quotient

\[
\pi(L)=LL^T,\qquad L\in{\rm GL}(m),\qquad L\sim LQ, Q\in O(m),
\]

with Frobenius lift metric and Bures--Wasserstein base metric. Rank-changing PSD matrices are outside this manifold.

The surviving estimator is local and safeguarded:

1. positive stage means are constrained to a declared compact strongly geodesically convex regular domain;
2. the complete tuple of population and empirical stages, signed Richardson/blend outputs, chords, radial connectors, quotient ODE paths, polygonal/ruled surfaces, and reconstructions is tested for generated-domain membership;
3. an inadmissible Richardson or reconstruction output triggers a deterministic full-rank fallback.

The fallback is asymptotically inactive relative to this constrained estimator on its regular event. No equality with the original unconstrained global argmin is claimed.

## 2. Primitive compatible generated-domain package

For fixed constants \(0<\alpha<\beta<\infty\), \(\chi>0\), \(r_0>0\), and finite consumer derivative order \(k_0\), the application supplies one compatible generated domain satisfying:

1. every base, observation, population/empirical stage, Richardson/blend output, chord, connector, ODE trajectory, ruled surface, and reconstruction belongs to its declared full-rank primitive domain;
2. base spectra remain in \([\alpha I,\beta I]\);
3. cross-Gram polar inputs and Exp factors retain their separately typed singular-value margins; no eigenvector or repeated-eigenvalue gap is imposed;
4. every score pair lies strictly inside the produced positive-Hessian/normal radius;
5. every canonical path consumed by transport has total BW/lift-Frobenius length at most \(r_0\), with the required endpoint/path jets supplied for differentiated families;
6. signed generated maps have positive population slack and the empirical grid/vertex event is small relative to that slack.

For the statistical theorem, the application separately supplies total tangent energy, mean bias/local-stationarity, finite-memory or proved Hilbert/HS dependence, included-lag target factorisation or defect, lag count, \(A_{2,n}\), target rank, actual eigengap \(\Delta_n\), and selector window.

Raw spectral conditioning does not imply any item about signed generated outputs, normal-pair support, total energy, dependence, signal, or gap.

## 3. Derived geometry producers

| Producer | Status | What proves it | What remains visible |
|---|---|---|---|
| horizontal projector and quotient connection | derived | Sylvester inverse and direct-lift recurrence on the spectral band | typed BW/Frobenius norms |
| exact tangent norm comparison | derived | horizontal-lift isometry and spectral calculus | \(\alpha,\beta\) |
| O'Neill curvature and consumed derivatives | derived | fixed-ambient tensor recurrence followed by invariant base conversion | derivative order; no hidden \(m\) |
| Exp, Log, square root, polar alignment | derived | invariant functional calculus and singular-value margins | polar and Exp margins remain distinct |
| radial/chord transport and endpoint variations | derived | isometric horizontal-lift ODE and typed variational equations | total length and family jets |
| observation Hessian and positive normal radius | derived | mixed base/observation derivatives and \(H(A,A)=I\) | score pairs must lie inside the produced radius |
| Richardson, blend, connector, and ruled maps | derived | finite recurrence on the complete generated domain | generated slack and object membership |
| polygonal PF comparison | derived | connector-typed cell telescoping and ruled-area inequality | \(N,r_N,v_\mu,a_\mu\) remain explicit |

These producers are not assumptions merely renamed as conclusions: their low-level spectral, singular-value, path, and generated-membership inputs are the primitives in §2. An application may verify a high-level producer directly, but must identify that invocation level.

## 4. Fixed-margin matrix-size-uniform geometry theorem

On the compatible package of §2, the recurrence-defined coefficient

\[
C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)
=1+C_A(\alpha,\beta,\chi,k_*)
+C_B^{\rm rec}(\alpha,\beta,\chi,r_0,k_0),
\qquad k_*=\max\{k_0,2\},
\tag{BWF.1}
\]

is finite and independent of matrix size. It controls through the consumed order the projector, quotient connection, O'Neill curvature, canonical PT variations, Exp/Log/polar alignment, score/Hessian, positive normal radius, and canonical generated maps listed in §3.

For \(A\in[\alpha I,\beta I]\) and \(U\in T_A{\rm SPD}(m)\), the exact norm comparison is

\[
\frac1{4\beta}\|U\|_F^2
\le \|U\|_{\rm BW,A}^2
\le \frac1{4\alpha}\|U\|_F^2.
\tag{BWF.2}
\]

No \(\sqrt m\) factor appears in these intrinsic/Frobenius operator bounds.

The common coefficient does not hide polygon or localization counts. An independently parameterised \(N\)-segment polygon retains its Bell-polynomial dependence on \(N+\mathsf L\) in the declared endpoint norm. The PF consumer instead retains

\[
C_{\rm PF}\{v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}\},
\tag{BWF.3}
\]

and complete grid localization pays either a proved supremum event or the visible \(\sqrt{N+1}\,r_N\) cost.

## 5. Fixed-size safeguarded statistical theorem

For fixed \(m\), compactness on the primitive regular sets plus the derived fixed-order calculus closes the positive mean, grid, polygonal frame, feasible observation, lag row, assembly, loading, null-spectrum, and selector chain for the safeguarded estimator.

Under bounded BW tangent energy and the stated dependence, local-law, target, and gap assumptions,

\[
d_n=O_p(n^{-1/2}+\ell_n+\zeta_n),
\tag{BWF.4}
\]

where \(\zeta_n=0\) under exact included-lag factorisation. With the matching ideal or actual target,

\[
\|\widehat{\mathbb L}_n-\mathbb L_n\|_{\rm op}
\le 2A_{2,n}d_n+d_n^2,
\tag{BWF.5}
\]

and if this is \(o_p(\Delta_n)\),

\[
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
\lesssim\frac{2A_{2,n}d_n+d_n^2}{\Delta_n},
\qquad
\widehat\lambda_{r+1,n}\le d_n^2.
\tag{BWF.6}
\]

Under bounded fixed-size signal this reduces to the familiar \(O_p\{(n^{-1/2}+\ell_n+\zeta_n)/\Delta_n\}\) display. Threshold and ridged selectors require their canonical separation conditions; raw-ratio consistency does not follow from the eigenvalue orders alone.

## 6. What growing-size fixed-margin composition does—and does not—give

For \(m=m_n\to\infty\), §4 supplies every geometric producer consumed by G1/PF without direct matrix-size blow-up. A growing-size statistical theorem follows only after a separate HD1 or HE package supplies:

- support/energy and score/product concentration;
- generated-object counts and localization rates;
- local-stationarity and numerical defects;
- a declared clean or contaminated lag target;
- \(A_{2,n}\), \(\Delta_n\), and a nonempty selector window.

The final condition remains

\[
2A_{2,n}d_n+d_n^2=o_p(\Delta_n).
\]

Thus fixed-margin dimension-uniform geometry is a verified producer, not a universal arbitrary-size covariance theorem. Bounded spectra do not bound total BW energy.

## 7. Nonemptiness and exact boundaries

The scalar-centred compatible construction is nonempty when \(\max\{\chi,\chi^2\}<\beta\). More generally, strict population slack divided by the generated-map recurrence gives an open admissible neighbourhood. Common commuting diagonal models reduce to a flat positive-root chart; repeated positive eigenvalues remain regular because invariant square-root, polar, and Sylvester maps are smooth on the invertible cone.

The following claims are rejected:

- raw spectral bands close signed Richardson/blend outputs;
- the safeguarded estimator equals the original global unconstrained estimator;
- repeated positive eigenvalues cause alignment nonuniqueness;
- fixed bands imply bounded total energy;
- geometry supplies dependence, lag signal, or an eigengap;
- the full result extends through rank loss or across PSD strata.

Orthogonal rank-one PSD endpoints give nonunique alignments, geodesics, logarithms, midpoints, and two-point means. Rank loss—not multiplicity—is the genuine global boundary.

## 8. Proof provenance

The fixed-size local estimator and statistical proof are in [[BW — moving-centre Bures-Wasserstein working dossier]]. Matrix-size-uniform quotient/curvature derivations are in [[BW-SIZE-FIXED-MARGIN — Agent A quotient calculus]]; transport, Hessian, generated-map, and PF derivations are in [[BW-SIZE-FIXED-MARGIN — Agent B transport and generated geometry]]; the adversarial checks are in [[BW-SIZE-FIXED-MARGIN — Agent C hostile audit]]; and the final adjudication is [[BW-SIZE-FIXED-MARGIN — lead claim and objection ledger]]. Those archived files are citable proof provenance; this file is the canonical theorem boundary and producer classification.
