---
type: working-proof-ledger
title: BW-SIZE-FIXED-MARGIN — lead claim and objection ledger
status: gate-a-adjudicated-ready-to-archive
authority: lead-working-file-only
---

# BW-SIZE-FIXED-MARGIN — lead claim and objection ledger

> **STAGE 1 ADJUDICATED / ARCHIVAL RECORD.** Both hostile passes are complete. The lead selected Gate A under the compatible generated-domain package recorded below. Canonical theorem status is maintained in the primary proof ledger, not here.

## Assumption package under audit

Fix (0<\alpha<\beta<\infty), (\chi>0), (r_0>0), and a finite derivative order (k_0). All base matrices and complete generated tuples must lie in declared full-rank BW primitive domains; all lifts, cross-Gram polar inputs, Exp endpoints, chords, ODE trajectories, and ruled surfaces must retain their declared singular-value/domain margins; every score pair used for convexity must lie in the ultimately proved normal radius; and the total BW/Frobenius lift length of every path whose transport is consumed is at most (r_0). Spectral band, polar/Exp margin, normal radius, generated-set closure, total BW energy, path length, statistical signal, and eigengap are separate inputs.

The common constant, if it exists, must be a finite explicit function (C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)), independent of matrix size. Its geometric conclusion must not be presented as an energy, concentration, target, or signal theorem.

## Common claim ledger

| ID | Exact claim | Domain and margins | Input/output norms | Producer | Direct consumer | Dimension dependence | Objection | Resolution | Status |
|---|---|---|---|---|---|---|---|---|---|
| Q-0 | (\pi(L)=LL^T), (\mathcal V_L=L\mathfrak{so}(m)), (\mathcal H_L=\{H:L^TH=H^TL\}) define the free full-rank quotient | (LL^T\in[\alpha I,\beta I]) | lift Frobenius / base BW | Lead + A | all quotient maps | none expected | signs and gauge equivariance | pending A cross-check | IN REVIEW |
| Q-1 | (P_L^HZ=Z-L\Omega), (G\Omega+\Omega G=L^TZ-Z^TL), (G=L^TL) | (G\succeq\alpha I) | (F\to F); derivatives (F^{k+1}\to F) | A | connection, curvature, PT | none expected | exact differentiation and variable (Z) typing | pending | IN REVIEW |
| Q-2 | Horizontal lift (\mathscr H(L,U)=\mathcal L_{LL^T}^{-1}(U)L) is an isometry | fixed spectral band | BW tangent to lift (F) | A | connection, norm conversion | none | the archived tangent/Frobenius equivalence is coarse; exact bound is (\|U\|_F^2/(4\beta)\le\|U\|_A^2\le\|U\|_F^2/(4\alpha)) | pending independent check | IN REVIEW |
| Q-3 | Quotient Levi–Civita connection and fixed derivatives are dimension-uniform | primitive quotient domain | multilinear BW/Frobenius operator norms | A | PT, Hessian, curvature | none expected | basic-field/gauge types and product bounds | pending | IN REVIEW |
| Q-4 | Exact O'Neill tensor/curvature operator and consumed derivatives are dimension-uniform | same | trilinear BW operator norm and derivatives | A | connection variation, PF | none expected | archived seed gives only a vague signed sum | pending exact formula | OPEN IN CAMPAIGN |
| T-1 | Horizontal lift of PT satisfies the explicit typed linear ODE and is BW-isometric | complete horizontal path, length (\le r_0) | lift (F), base BW | B + lead | radial/polygonal connectors | none | distinguish speed from total length; check ODE sign | pending | IN REVIEW |
| T-2 | Endpoint/parameter derivatives of radial, connector, chord, polygonal, and ruled PT are uniformly bounded | canonical generated path families and margins | multilinear endpoint BW norms to transport operator norm | B | G1/PF | no (m); polygon dependence must be explicit | arbitrary path families are not controlled by length alone; only canonical generated families qualify | pending exact family statement | OPEN IN CAMPAIGN |
| E-1 | Exp, Log, square-root, polar, and alignment derivatives through consumed order are dimension-uniform | spectral and singular-value margins | typed BW/Frobenius multilinear norms | A/B | score, Richardson, observations | none expected | no eigenvector eigengap allowed | pending | IN REVIEW |
| H-1 | (H(A,B)=-\nabla_A\Log_A B) and its consumed base/observation derivatives are uniformly bounded | generated score-pair domain | endomorphism norm on (T_A), covariant derivatives | B | G1, recentering | none expected | must compare at a common base and not assume the radius | pending | OPEN IN CAMPAIGN |
| H-2 | A positive Hessian radius follows uniformly from (H(A,A)=I) and a proved first derivative bound | complete score pairs within (r_{\rm nor}) | BW endomorphism norm | B + lead | constrained mean strong convexity | none | radius must be inside all spectral/Exp/generated margins | pending | OPEN IN CAMPAIGN |
| G-1 | Richardson, blend, chord, connector, and ruled-surface maps have uniform derivatives | complete generated tuple domain | typed multilinear BW norms | B | mean bias, closure, PF | none expected | signed Richardson can leave SPD absent explicit closure | pending | IN REVIEW |
| P-1 | Finite polygonal accumulation has a coefficient independent of (m), with all dependence on total length, cell count, and vertex errors displayed | complete paired polygons/ribbons | transport operator norm; path length in BW/lift (F) | B + lead | PF | no (m); (M) may occur only explicitly | composition derivatives may grow with segment count even though transports are isometries | pending exact consumer form | OPEN IN CAMPAIGN |
| C-1 | One common finite (C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)) reaches every G1/PF geometric consumer | compatible single assumption package | maximum of typed primitive/composed constants | lead after hostile passes | BW growing-size geometry | must be independent of (m) | recursive constant and order losses must be explicit | pending | OPEN IN CAMPAIGN |

## Lead edge-case audit

| Case | Required reduction | Current check |
|---|---|---|
| Scalar (m=1) | root coordinate (r=\sqrt A); projector is identity, curvature zero, PT identity, Hessian identity | passes preliminarily |
| Common commuting diagonal | positive root orthant is flat; all nonzero curvature/frame terms must vanish | passes: (\mathcal A_XY=0) for diagonal lifts, hence O'Neill curvature and ruled holonomy vanish |
| Repeated positive eigenvalues | invariant square-root, polar, and Sylvester maps remain smooth; no multiplicity gap | passes primitive check |
| Identity base | (P_I^HZ=\operatorname{sym}Z); connection/curvature signs can be checked with symmetric matrices | passes: for constant symmetric (U,V), (\Gamma_I(U,V)=-(UV+VU)/4) and (\mathcal A_{U/2}(V/2)=-[U,V]/8); Agent A's convention gives (+3\|\mathcal A\|_F^2) sectional curvature |
| Zero path | PT is identity; no division by path length or singular endpoint parametrisation | passes at order zero; independent endpoint derivatives can remain nonzero and therefore must not be claimed length-weighted without connector/direct-sum typing |
| Many segments | composition remains isometric, but variation must accumulate by an explicit area/error sum and not be hidden in (C_{\rm BW}) | generic polygon derivatives pay an explicit direct-sum/segment factor; the PF consumer uses the separate cell-area sum with ((N+1)r_N^2) visible |
| High-dimensional fixed band and fixed length | block/diagonal directions with Frobenius norm one must not acquire (\sqrt m) | passes primitive hostile family: normalized diagonal and repeated noncommuting block directions remain bounded by op-by-F products; no coordinate-count counterexample found |

## Objection table

| Claim | Attack | Repair or counterexample | Independent checker | Final status | Canonical consequence |
|---|---|---|---|---|---|
| Archived PT bound (5.4)–(5.7) | It replaces a total-length hypothesis by the pointwise assertion (\|\dot L\|_F\le r_0) and does not define the canonical path-family derivative norms | Reparameterise canonical segments and integrate the coefficient against typed lift length; separately bound endpoint derivatives of the generated path map | B, then A/C | PENDING | none before gate |
| Archived curvature row (4.2) | No exact O'Neill identity, signs, or nested (\mathcal A) types are supplied | A must state an exact four-tensor or operator identity and derive the bound | C, lead | PENDING | none before gate |
| Polygonal PT derivative | A derivative of a product of (M) segment transports can contain explicit (M)-dependent sums | State the exact PF variation/area inequality; do not claim a segment-free global multilinear norm unless proved in a declared direct-sum norm | B, then C | PENDING | none before gate |
| Positive Hessian | Uniform closeness to (I) is valid only after the observation derivative and common-base identification are proved on a domain already inside every primitive margin | Intersect the derived radius with the spectral, Exp/polar, path, and generated-domain radii | A/C | PENDING | none before gate |
| Agent A common constant | The recursive ingredients (b_j,a_j,\gamma_j) are partly specified by an expression-tree instruction, while the closed domination (7.3) is asserted without a derivation | Retain only a fully defined recurrence/finite maximum, or prove the displayed coarse envelope from the depth and arity of every consumer expression | B/C, lead | PENDING | none before gate |
| Agent A derivative order | A consumer Hessian derivative of order (j) uses Log order (j+1); higher transport variations use shifted curvature/connection orders | Build a backward order ledger and evaluate primitives at the maximum shifted order, while keeping the public consumer order (k_0) fixed | B/C, lead | PENDING | none before gate |
| Agent B polygon derivative | Segment estimate (4.10) contains (C(1+\ell_j)); summing these scalar per-segment operator norms gives (C(N+\mathsf L)), not (C(1+\mathsf L)) | Type the global vertex parameter space. An (\ell^1) direct-sum norm can absorb endpoint sums; an (\ell^2) or (\ell^\infty) norm must display its exact (N)-factor. PF may instead use the sharper ruled-area cancellation (8.3) | A/C, lead | PENDING | none before gate |
| Agent B `GD` nonemptiness | Its ball radius (1.6) protects (\chi) and the upper band but omits the distance from (c) to the lower spectral edge (\alpha) when (\chi<\sqrt\alpha) | Add ((\sqrt c-\sqrt\alpha)/5) and require a positive minimum, or give a separate band calculation | C, lead | PENDING | none before gate |
| Agent B common constant | Display (9.1) contains malformed exponents and does not prove that its envelope dominates the Bell/composition recurrences | Replace it by a syntactically valid, fully defined recursive maximum; a coarse exponential is optional only after domination is shown | A/C, lead | PENDING | none before gate |

## Gate A adjudication — 2026-08-09

**Verdict: BW-SIZE-FIXED-MARGIN is PROVED UNDER EXPLICIT COMPATIBLE GENERATED-DOMAIN ASSUMPTIONS.**

The proof produces an explicit recurrence-defined finite coefficient

\[
C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)
:=1+C_A(\alpha,\beta,\chi,k_*)
+C_B^{\rm rec}(\alpha,\beta,\chi,r_0,k_0),
\qquad k_*=\max\{k_0,2\},
\]

independent of matrix size. The exact recurrence lists are in the Agent A and Agent B dossiers. The theorem requires one checked generated domain containing every base, observation, stage mean, Richardson/blend output, chord, connector, ODE path, ruled surface, and reconstruction; fixed spectral band; polar and Exp singular-value margins; total transport-path length at most \(r_0\); and all score pairs inside the produced positive-Hessian radius. The displayed nonempty scalar-centred construction requires \(\max\{\chi,\chi^2\}<\beta\); for a general generated tuple, nonemptiness is stated through strict population slack divided by the proved generated-map recurrence, not through a universal raw-alignment numeral.

The common coefficient covers the fixed-order horizontal projector, quotient connection, O'Neill curvature and consumed derivatives, typed PT variations, Exp/Log/polar alignment, score/Hessian derivatives, the dimension-uniform normal radius, and the canonical Richardson/blend/chord/ruled maps. It does not hide the following visible consumer inputs:

- an independently parameterised \(N\)-segment polygon has a Bell-polynomial coefficient in \(N+\mathsf L\) in the declared \(\oplus,\infty\) endpoint norm;
- the PF comparison is bounded by
  \[
  C_{\rm PF}\{v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}\};
  \]
- complete generated-set localization uses either a sup-grid error or \(\sqrt{N+1}r_N=o_p(\delta_{\rm GD}/C_B^{\rm rec})\);
- total tangent energy, dependence, lag signal, eigengap, and selector thresholds remain separate statistical assumptions.

### Final objection dispositions

| Claim | Attack | Repair or counterexample | Independent checker | Final status | Canonical consequence |
|---|---|---|---|---|---|
| quotient norm/projector | hidden \(\|L\|_F\) or coordinate count | exact BW norm equivalence; every fixed lift paid in operator norm | A/C/lead | PASS | fixed-size compactness no longer needed for fixed-margin size uniformity |
| O'Neill curvature recurrence | moving subspaces, malformed adjoint, principal-gauge/double-Gram ambiguity | fixed-ambient tensor/adjoint; wholly direct-\(L\) recurrence; one subsequent invariant base conversion | B/C/lead | PASS | recurrence-defined \(C_A\) retained; unsupported closed exponent withdrawn |
| PT and polygon derivatives | path length confused with pointwise speed; false generic \(N\)-free derivative | exact isometric lift ODE; varying-fibre connectors; explicit \(N+\mathsf L\) Bell budget | A/C/lead | PASS WITH VISIBLE \(N\) | generic polygon derivative is not hidden in \(C_{\rm BW}\) |
| Hessian/normal radius | circular coercivity and wrong observation derivative | mixed \(D_MD_L\) derivative, order floor \(k_*\), produced \(\rho_H\), three-radius constraint ball | A/C/lead | PASS | G1 strong convexity has an actual dimension-uniform producer |
| generated-domain nonemptiness | polar and Exp margins scale differently; signed outputs can escape | compatibility \(\max\{\chi,\chi^2\}<\beta\), full membership/slack test, recurrence-controlled open neighbourhood | C/lead | PASS UNDER EXPLICIT GD | no raw-band closure claim |
| ruled-cell/PF accumulation | asserted area law, fibre mismatch, hidden segment factor | exact geodesic quadrilateral, endpoint Jacobi vanishing, connector-typed telescoping | C/lead | PASS | PF coefficient and all \(N,r_N,v_\mu,a_\mu\) terms remain visible |
| retained-hypothesis counterexample | scalar, diagonal, repeated-spectrum, arbitrary gauge, many segment, high frequency, concentrated RMS | each failure either vanishes or activates a displayed hypothesis/input | C/lead | NONE FOUND | Gate B unavailable |

Both mandatory hostile passes are complete. Agent C's final Section 11 supersedes its stale pre-repair Section 10. Stage 2 was not started during this adjudication.
