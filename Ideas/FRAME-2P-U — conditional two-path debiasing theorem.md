---
type: canonical-proof
title: FRAME-2P-U — conditional two-path debiasing theorem
status: canonical-conditional-proof
last-audited: 2026-08-12
verdict: the U2P assumption-to-root-n implication is proved; U2P is verified only for fixed-dimensional curved models and flat-padded growing-dimensional witnesses, not for a genuinely growing-curvature family or growing-size AIRM/BW
---

# FRAME-2P-U — conditional two-path debiasing theorem

> **Scope correction.** FRAME-2P-U is an abstract conditional theorem, not a generic growing-curvature theorem. It is uniform over triangular arrays for which every U2P primitive below is uniform in \(p_n\). The repository currently verifies nonemptiness through a fixed curved active block, optionally padded by flat inactive coordinates. It does not verify U2P for growing-size AIRM SPD, growing-size noncommuting BW, or any family whose active curved dimension diverges.

## 1. Observable estimator

Use three innovation-separated colours. Training vertices \(\widehat q^T\) use \(b_n=n^{-1/7}\); validation vertices \(\check q^V\) use \(c_n=n^{-\gamma}\); the evaluation colour constructs the complete masked polygon lag-row functional \(\widehat{\mathfrak T}_E(q)\). Let \(M_n\asymp n^{2/7}\) and

\[
d_j^{TV}=\log_{\widehat q_j^T}\check q_j^V,\qquad
\widehat{\mathfrak T}^{2p}_{T,V,E}
=\widehat{\mathfrak T}_E(\widehat q^T)
+D\widehat{\mathfrak T}_E(\widehat q^T)[d^{TV}].
\tag{F2P.1}
\]

Average (F2P.1) over the three cyclic assignments. Every quantity is computed from fitted paths and the declared geometry. No true centre, true frame, \(e_t\), \(\Omega_t\), population Hessian, or unobserved ribbon enters the estimator.

## 2. Primitive U2P assumptions

The theorem assumes the following low-level producers uniformly in \(n,p_n\):

1. fixed included-lag count and finite-memory length; bounded total tangent energy; exact GLO and included-lag factorisation, or separately displayed defects;
2. a uniformly \(C^4\) mean/law, unique Karcher means, and a fixed positive strong-convexity modulus;
3. one generated tube on which the consumed score-Hessian derivative, first two positive-barycentre implicit derivatives, Exp, Log, Richardson post-map, chord transport/Jacobi maps, radial connectors, and first two complete masked-row polygon variations have uniform operator bounds;
4. deterministic local weights bounded by \(C/(na_n)\), supported on \(O(na_n)\) observations per vertex, with the stated third-order population bias;
5. training, validation, and evaluation cores with disjoint innovation sigma-fields, gaps at least the memory-plus-lag range, identical phase-balanced masks, and one common finite-array target;
6. exact local-law sampling, or \(a>1/2\) with coupling, design, and mask defects \(o(n^{-1/2})\).

These assumptions are much stronger than bounded energy. In particular, bounded energy supplies Hilbert/HS envelopes but does not supply uniform polygon actions, replacement stability, masks, GLO, or sample separation.

GLO is not a generic symmetry consequence. Outside the exact flat/centrally symmetric constructions already checked, the repository has no broad natural data class for which both lag-specific GLO identities are automatic. Characterising such application classes is an open model-verification problem.

## 3. Derived producers—not consequences of positive weights alone

| Producer | Status | What proves it | What is still assumed |
|---|---|---|---|
| vertex action \(\max_j\|K_{n,j}\|\le C/M_n\), \(\sum_j\|K_{n,j}\|\le C\) | derived conditionally | typed cancellation of adjacent-cell endpoint generators plus \(O(M_n^{-1})\) curvature/local-row mass; archived FRAME-IF-A §10 | uniform low-level curvature/Jacobi/row-variation bounds in U2P-3 |
| one barycentre replacement \(C/(nc_n)\) and mixed replacement \(C/(n^2c_n^2)\) | derived conditionally | strong monotonicity of the Karcher equation and two implicit derivatives; archived FRAME-IF-B §11.2 | uniform strong-convexity and \(C^2\) barycentre/Richardson constants in U2P-2–4 |
| aggregate row replacement \(C/n\) and \(C/(n^2c_n)\) | derived conditionally | local-window support count multiplied by the preceding replacement and \(C/M_n\) action; archived FRAME-IF-B §11.3 | composed row is a sum of one-vertex maps with the uniform \(C^2/M_n\) bound |

The theorem must not list the derived bounds as if they followed from positive weights or energy alone. An application may instead verify the aggregate bounds directly; that invokes the theorem at a higher abstraction level.

## 4. Conditional theorem

Assume U2P-1–6 and the derived producers of §3. If

\[
\frac16<\gamma<\frac3{14},\qquad
b_n=n^{-1/7},\qquad c_n=n^{-\gamma},\qquad M_n\asymp n^{2/7},
\]

then in direct-sum Hilbert–Schmidt norm

\[
\widehat{\mathfrak T}^{2p}_n-\mathfrak T_n
=\mathbb G_{E,n}[Z_n]+\mathbb G_{V,n}[\varphi_{n,c}]+R_n,\qquad
\|R_n\|_{\oplus HS}=o_p(n^{-1/2}),
\tag{F2P.2}
\]

and both centred influence rows are \(O_p(n^{-1/2})\). Consequently the corrected lag row has root-\(n\) order. If its total row error \(d_n^{db}\), including any target defect, satisfies

\[
2A_{2,n}d_n^{db}+(d_n^{db})^2=o_p(\Delta_n),
\]

then the existing deterministic assembly and Davis–Kahan steps give loading error \(O_p(n^{-1/2}/\Delta_n)\) when all other defects are sub-root-\(n\), and the beyond-rank sample spectrum is \(O_p(n^{-1})\) under exact rank-\(r\) target factorisation.

This is **oracle-rate order, not oracle equivalence**. The validation influence \(\mathbb G_{V,n}[\varphi_{n,c}]\) is a second leading fluctuation and generally changes the limit variance. No equality with the parent estimator's limiting law or efficiency bound is claimed.

## 5. What the proof cancels

Radial comparison gives \(d^{TV}=e_V-e_T+O(e_T^2+e_V^2)\). The plus derivative in (F2P.1) therefore cancels the training path's complete first variation. The base-log part contains the inverse-Karcher mean action; the polygon derivative contains transport, Jacobi, connector, and curvature actions. A common rigid gauge jointly conjugates the base row and correction and is never treated as additive error.

The remaining nonlinear bound is

\[
M_n(r_T^2+r_Tr_V+r_V^2)+M_n^{-2}
+c_n^3+(nc_n)^{-1}+(n\sqrt{c_n})^{-1}+n^{-1/2}r_V,
\]

with \(r_T=n^{-3/7}\) and \(r_V=c_n^3+(nc_n)^{-1/2}\). Direct exponent substitution yields \(o(n^{-1/2})\) on the displayed open \(\gamma\)-window, apart from separately budgeted coupling, mask, and target defects.

## 6. Nonemptiness and application boundary

The verified curved witness has one fixed hyperbolic active factor. The arbitrary-\(p_n\) version is

\[
\mathbb H^2(-1)\times\mathbb R^{p_n-2},
\]

with the lag signal and non-rigid curvature action confined to the hyperbolic block; the added flat coordinates are inactive or serially white with bounded total energy. This proves logical nonemptiness for every ambient dimension. It does **not** prove robustness to a growing number of active curved directions.

Accordingly:

- fixed-dimensional curved geometries with checked constants are legitimate conditional applications;
- flat-padded sequences demonstrate ambient-dimension uniformity only;
- growing-size AIRM/BW and other growing-curvature applications remain **UNVERIFIED FOR U2P**;
- failure to verify U2P returns the analysis to robust HD1 if its assumptions hold.

## 7. Rejected and conditional alternatives

- Same-band score/Richardson correction is **DISPROVED**: it generically retains \(b_n^3K[B_3]\asymp n^{-3/7}\).
- Direct frame/\(\Omega\) plug-in is **CONDITIONAL** on an additional observable frame producer.
- Invariant-only redesign is **REJECTED FOR THE ORIGINAL ESTIMAND** because it changes the target.

## 8. Proof provenance

The complete derivations and two hostile passes are preserved in [[FRAME-IF — closure adjudication]], [[FRAME-IF-A — geometry closure]], [[FRAME-IF-B — statistical closure]], and [[FRAME-IF-C — impossibility and replacement]]. Those archived files are citable proof provenance; this file is the canonical theorem boundary and producer classification.
