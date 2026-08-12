---
type: working-proof-dossier
title: BW-SIZE-FIXED-MARGIN — Agent C hostile audit
status: noncanonical-first-hostile-pass
authority: none
stage: 1-fixed-margin-only
owner: Agent C
last-audited: 2026-08-09
---

# BW-SIZE-FIXED-MARGIN — Agent C hostile audit

> **NONCANONICAL FIRST-PASS HOSTILE DOSSIER.** This file does not prove or disprove BW-SIZE-FIXED-MARGIN and must not be cited as theorem status. It audits the archived incomplete sketch and the exact fixed-margin consumer chain. It does no shrinking-margin work. A failed proof step is labelled as such, not promoted to a counterexample.

## 0. First-pass verdict

No analytic counterexample presently disproves the dimension-uniform fixed-margin theorem after retaining a fixed lower/upper spectral band, a genuine Exp/output margin, a fixed normal/support radius, and a correctly typed total path-length/variation budget. The invariant Sylvester, square-root, polar, and horizontal-lift primitives are consistent with dimension-free operator-by-Frobenius estimates.

The archived seed nevertheless does **not** prove the theorem. Its main unresolved defects are:

1. the O'Neill row is not an exact typed curvature formula and does not establish signs or derivative orders;
2. the PT variation row replaces an integral speed/variation budget by an unjustified pointwise-speed statement and does not state the norms on path parameters;
3. whole-polygon composition and segment-count dependence are absent;
4. the normal-radius argument does not write the exact observation-variable covariant derivative and its tensor identifications;
5. path length does not control the higher jets used by chord/ruled/path-parameter differentiation;
6. generated-domain closure is not a consequence of raw fixed bands, and a common constant cannot repair a failed membership event;
7. the displayed common constant contains unspecified universal constants and no recurrence, so it is not yet the requested explicit function;
8. the derivative-order budget is shifted: a Hessian derivative of order (j) consumes higher Log and connection orders than the table records;
9. the proposed constant has not been propagated to the exact G1/PF hypotheses, especially the score radius, Hessian lower bound, mean-path length/acceleration, whole-polygon accumulation, and generated-tuple event.

Accordingly the first-pass status is **OPEN — MATERIAL FORMULA, TYPING, AND CONSUMER-REACH GAPS**. This is not an adjudicated Gate C verdict; A and B repairs and both later hostile passes remain mandatory.

## 1. Conventions used in this audit

For (A=LL^T\in {\rm SPD}(m)), write

\[
\mathcal H_L=\{H:L^TH=H^TL\},\qquad
\mathcal V_L=\{L\Omega:\Omega^T=-\Omega\}.
\]

The lift norm is Frobenius. A base tangent (U\in{\rm Sym}(m)) has (S_U=\mathcal L_A^{-1}U), horizontal lift (H_U=S_UL), and

\[
\|U\|_{A,\rm BW}=\|H_U\|_F.
\]

For a multilinear map, the input norm is the product of the displayed lift Frobenius or base BW norms. A path speed is (|\dot L(t)|_F); total lift length is (int|\dot L(t)|_Fdt). A polygon is not assigned the maximum of its segment lengths when the proof consumes its total length.

The exact metric identity in an eigenbasis of (A) is

\[
\|U\|_{A,\rm BW}^2
=\frac12\sum_{i,j}\frac{|U_{ij}|^2}{a_i+a_j},
\]

so the sharper dimension-free equivalence is

\[
\frac1{4\beta}\|U\|_F^2
\le \|U\|_{A,\rm BW}^2
\le \frac1{4\alpha}\|U\|_F^2.
\tag{1.1}
\]

The looser equivalence in the seed is valid, but (1.1) should be used to prevent artificial margin powers.

## 2. Exact first-pass claim ledger

| ID | Exact claim | Domain and margins | Input/output norms | Producer | Direct consumer | Dimension dependence | Objection | Required resolution | First-pass status |
|---|---|---|---|---|---|---|---|---|---|
| C-PROJ-0 | (P_L^{\mathcal H}Z=Z-L\Omega), ((L^TL)\Omega+\Omega(L^TL)=L^TZ-Z^TL) | (\alpha I\preceq LL^T\preceq\beta I) | (Z,H_i\) in (F); output in (F) | Sylvester equation | lift, connection, PT | none visible | Formula and zeroth bound survive. Higher derivatives are only sketched by subset notation and do not distinguish (L)- versus (Z)-directions. | Give a joint-map recurrence and a numeric fixed-order bound. | **LIKELY REPAIRABLE; NOT YET PROVED HERE** |
| C-LIFT | (U\mapsto S_UL) and fixed-coordinate quotient connection derivatives | same band | base inputs in BW or (F), horizontal output in (F) | differentiated (AS+SA=U) | connection, curvature, ODE | none visible | “(D^k\Gamma^{\rm BW})” is not intrinsically typed: a connection is not a tensor, and vertical/gauge versus horizontal base directions are not specified. | Fix a basic-lift chart or write the covariant difference actually used by the ODE; state every domain/codomain. | **MATERIAL TYPING GAP** |
| C-ON | exact O'Neill tensor and quotient curvature, including required covariant derivatives | band and basic horizontal fields | BW inputs, BW output; or exact 4-tensor norm | (P^{\mathcal V}D\bar Y[X]) | holonomy, connection variation, Hessian/Jacobi bounds | no trace factor is forced | Seed (4.2) is only “a universal signed sum.” Its displayed definition of (\mathcal A_XY) covers horizontal (Y), while terms such as (\mathcal A_X\mathcal A_YZ) require the vertical-argument type too. Bracket, sign convention, and derivative orders are missing. | State one exact O'Neill formula with both horizontal/vertical types, or derive (R) from an exact basic connection formula. Rederive all signs independently. | **OPEN — EXACT EQUATIONS MISSING** |
| C-PT-0 | PT along a horizontal lift solves a vertical ODE | band along full path | transported lift (F	o F) | horizontality derivative | radial/connector/polygonal PT | none | Seed (5.3) is correct in sign under the stated convention, but (5.4) has the wrong coefficient when (\beta<1). The direct bound is (\|\dot H\|_F\le(\sqrt\beta/\alpha)\|\dot L\|_{op}\|H\|_F). | Repair the coefficient or use a valid monotone envelope such as (\max(1,\sqrt\beta)/\alpha). | **FORMULA REPAIR REQUIRED** |
| C-PT-1 | fixed-order endpoint/surface derivatives of PT | band, complete path in domain, total length (\le r_0), generated path-family margins | endpoint/surface directions in a declared product norm; output operator (F\to F) | typed variational ODE | connector and ruled comparisons | none if path variations are controlled | Length only bounds (int\|B\|), not (sup\|\dot L\|), and does not bound (int\|\partial_\theta^j\dot L\|). The seed silently replaces length by pointwise speed. | Use integral Gronwall and state (W^{1,1})-type variation bounds derived from the explicit chord/radial/ruled formulas. | **MATERIAL GAP** |
| C-PT-POLY | PT along a finite polygon and derivatives of the whole composition | every segment and complete polygon in generated domain | vertex parameters in a declared direct-sum norm; output operator norm | composition of segment PT | PF and connector frame | segment count can enter unless cancellation/total variation is proved | Seed says “corners introduce composition” but gives no product-rule accumulation, no total polygon length, and no segment-count factor. | Prove an exact bound in total length and state any (M)-dependence. Do not hide (M) in (C_{\rm BW}). | **OPEN — DIRECT CONSUMER GAP** |
| C-EXPLOG | fixed-order Exp/Log/alignment derivatives | all principal factors in band; every generated Exp factor (L+H) has (\sigma_{min}\ge\chi) and its output lies in the band | base directions BW, lift directions (F), output BW/(F) as declared | square-root, polar, lift, (\pi) | score, Richardson, observations | no multiplicity factor | The invariant route is sound in principle. The seed cites a common bound without giving the square-root/polar recurrences and does not count the extra derivative order needed downstream. | Supply fixed-order recurrences and an order budget from final consumers backward. | **INCOMPLETE, NOT COUNTEREXAMPLED** |
| C-HESS | (H(A,B)=-\nabla_A\Log_AB) and all consumed base/observation derivatives | generated score pairs; path varying (B) remains in domain | endomorphism operator norm on (T_A), derivatives in BW product norm | Exp/Log plus connection | G1 coercivity and recentering | no dimension cost shown | The seed says “base-varying tangent spaces” while the simplest proof fixes (A) and varies observation (B). It does not write (\nabla_BH), connector identifications, or the exact order. | Prove (\|H(A,B)-I_A\|_{op}\le C,d(A,B)) by varying the observation variable with all tensors based at (A), or write the alternative identification exactly. | **NORMAL-RADIUS STEP INCOMPLETE** |
| C-RICH | Richardson/blend/chord derivatives | complete input tuple and output in band; Exp factor margin (\chi) | product BW input norm to BW output | finite invariant compositions | G1 estimator and PF vertices | none for fixed maps | The composition argument is credible only after the previous rows. Fixed Richardson weights are harmless, but a blend profile and its derivative bounds must be fixed; “fixed width” alone does not determine a universal numeric constant. | Declare the exact cutoff/profile and include its (C^{k_0}) norm, or fix it once and make it a numeric universal. | **DOMAIN/DESIGN SPECIFICATION GAP** |
| C-RULED | derivatives and Jacobi/area constants for the exact ruled surfaces used cellwise | whole two-parameter image in band and margins | surface parameters in a typed norm; output tangent/area/PT operator norms | chord maps, connection, PT variation | PF cell holonomy | possible path-jet and cell accumulation factors | “Same composition” does not identify the two ruled triangles, their boundary conditions, or the normalized curvature operator used by PF. | Write the actual ruled map, (s,t) derivatives, wedge/area norm, and cellwise constant. | **OPEN — EXACT CONSUMER MAP MISSING** |
| C-NORM | base-varying tangent/lift norm equivalence and connector comparisons | band and connector path domain | BW to (F), (F) to BW, operator norms | (1.1), horizontal lift, PT | every base change | none | Pointwise equivalence is proved. Derivatives of the identification and comparison after changing bases are not supplied merely by citing (1.1). | State which comparisons use PT isometry and which use radial connector derivatives. | **PARTIAL** |
| C-DOM | every empirical/population pair, Richardson output, blend, chord, connector, ODE trajectory, ruled surface, and reconstruction satisfies the declared margins | full generated event | membership and singular-value tests, not a norm estimate | statistical localization plus continuity | every geometric row | number of generated objects may enter probability control, not deterministic derivatives | Fixed bands do not close signed Richardson images. Assuming membership is admissible only if checkable and propagated; a derivative constant cannot prove the event that authorizes its own use. | Separate primitive deterministic domain from the probabilistic generated-event proof and avoid circular localization. | **LOAD-BEARING DOMAIN GAP** |
| C-PF-ACC | cellwise connection variation sums to the exact PF error | total mean length, mean chord defect, grid RMS errors, segment count (M) | frame operator norm | C-ON, C-RULED, C-PT-POLY | PF then feasible observations | must be explicit | The seed never reaches (L_\mu r_\mu+Mr_\mu^2+K_\mu M^{-2}), nor shows which factors are geometric and which are path smoothness/statistical inputs. | Reproduce the full PF inequality with (C_{\rm BW}) and every nongeometric multiplier visible. | **COMMON CONSTANT DOES NOT YET REACH PF** |
| C-G1-REACH | common geometric constant reaches score localization, bias, Hessian, Richardson, and grid event | score radius and all population/proxy/generated tuples | exact G1 norms | C-HESS, C-RICH, C-DOM | G1 | number of tuples only in probability step | No row shows that (r_0) is simultaneously the observation score radius, normal radius, connector/path length, and generated-pair radius. Those are logically distinct even if a theorem upper-bounds all by one number. | State distinct radii first, then take their maximum/minimum in the final explicit function. | **COMMON CONSTANT DOES NOT YET REACH G1** |
| C-COMMON | one explicit (C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)) dominates every fixed-order geometric producer | compatible, nonempty full package | maximum of typed operator constants | all prior rows | G1/PF | must be independent of (m) | (c_{k_0}\Lambda^{e_{k_0}}e^{c_{k_0}r_0\Lambda^{e_{k_0}}}) contains unspecified (c_{k_0}), omits blend/path-family norms, and has no recurrence proving dominance. | Give an explicit recurrence or a finite maximum of fully defined producer constants. State compatibility such as nonempty band/output margins. | **NOT ESTABLISHED** |

## 3. Analytic attacks and edge families

### CE-C1 — fixed band is not a radius or energy bound

Let

\[
A_m=I_m,\qquad B_m=cI_m,qquad c\in(0,\infty)\setminus\{1\}
\]

with (c) inside one fixed spectral band. Then

\[
d_{\rm BW}(A_m,B_m)=\sqrt m\,|1-\sqrt c|.
\]

Thus fixed bands and perfect polar uniqueness do not yield a fixed score radius, total BW energy, path length, or G1 support envelope. This family does **not** disprove a theorem that explicitly assumes the fixed (r_0) radius; it proves that (r_0) is independent and must reach every score/path consumer.

### CE-C2 — total path length does not control higher path jets

For (N\ge2), in every (m\ge1) define the diagonal lift path

\[
L_N(u)=I_m+\frac{\varepsilon}{N}\sin(Nu)E_{11},
\qquad A_N(u)=L_N(u)L_N(u)^T,
\tag{3.1}
\]

with fixed (0<\varepsilon<1/4). All (A_N(u)) lie, for example, in the fixed band ([1/2,2]); all polar maps are unique; and

\[
\int_0^1\|\dot L_N(u)\|_Fdu
=\varepsilon\int_0^1|\cos(Nu)|du=O(\varepsilon).
\]

But

\[
\sup_u\|\ddot L_N(u)\|_F=\varepsilon N\to\infty.
\]

Therefore a fixed total path length cannot bound the (C^2) path constants used by chord error, nor arbitrary time-parameter derivatives of path-dependent maps. This is a genuine counterexample to any overbroad formulation whose only path regularity input is length (r_0). It is **not** a counterexample to endpoint derivatives of the fixed radial/chord map; those may be bounded by invariant matrix calculus. The theorem must distinguish endpoint-map derivatives from derivatives of an externally supplied mean path.

### CE-C3 — “fixed-width blend” is not a numeric derivative bound unless the profile is fixed

In scalar BW root coordinates, choose two constant roots (r_-=1), (r_+=1+\delta), with (delta>0) small enough to retain fixed bands and all output margins. For smooth weights

\[
w_N(u)=\frac{1+\sin(Nu)}2,
\qquad r_N(u)=(1-w_N(u))r_-+w_N(u)r_+,
\]

all blend outputs remain in the same compact positive interval while

\[
\sup_u|r_N'(u)|=\frac{\delta N}{2}\to\infty.
\]

Hence a theorem quantifying over blend profiles cannot have a common constant depending only on ((\alpha,\beta,\chi,r_0,k_0)). The canonical estimator can avoid this attack by fixing one cutoff profile once and for all and including its derivative norms as universal numerical data.

### CE-C4 — per-segment radius does not control a whole polygon

Take a polygon with (M) segments, each of lift length (delta>0), inside a fixed compact band. A segmentwise statement (ell_j\le r_0) permits total length (M\delta). The coefficient integral in the PT ODE and every naive product-rule derivative can then grow with (M). This observation is not a counterexample if the declared hypothesis is (sum_j\ell_j\le r_0); it forces the theorem to say “total polygonal length,” not “every segment has radius (r_0).”

### CE-C5 — raw bands do not close Richardson

In scalar root coordinates, the canonical weights give

\[
\tfrac13(1)-2(3/2)+\tfrac83(1)=0.
\]

All stage eigenvalues lie in ([1,9/4]), while the Richardson output has rank zero. This does not retain the declared output margin (chi), so it is not a disproof of the fixed-margin theorem. It proves that generated membership is a separate assumption/event and cannot be inferred from raw spectral bands.

### EC-C6 — repeated positive eigenvalues and identity base

At (A=I_m), arbitrary multiplicity is maximal. The Sylvester inverse is (\mathcal L_I^{-1}U=U/2), the principal root is (I_m), and every full-rank polar input remains smooth. No eigenvector gap enters. I find no multiplicity counterexample on the full-rank cone. Any repair that introduces a positive-eigenvalue eigengap should be rejected unless a coordinate-dependent algorithm, rather than the invariant theorem, truly consumes it.

### EC-C7 — high-dimensional local diagonal perturbations

Let (D_m\) be diagonal with (|D_m|_F=1), (|D_m|_{op}\le1), and set (L_m=I_m+\varepsilon D_m). For fixed small (\varepsilon), the band, Exp margin, and lift distance are uniform in (m). In the common diagonal root flat, all invariant derivatives are dimension-free. This edge family defeats an attempted disproof based solely on the number of diagonal coordinates: a valid negative result must preserve the typed Frobenius/BW normalization and cannot count coordinates by inspection.

## 4. Formula-level objections to the archived seed

### O-C1 — PT coefficient in (5.4)

From

\[
(L^TL)\Omega+\Omega(L^TL)=H^T\dot L-\dot L^TH,
\qquad \dot H=L\Omega,
\]

one obtains

\[
\|\Omega\|_F\le\alpha^{-1}\|H\|_F\|\dot L\|_{op},
\qquad
\|\dot H\|_F\le\frac{\sqrt\beta}{\alpha}
\|\dot L\|_{op}\|H\|_F.
\tag{4.1}
\]

The seed's coefficient (\beta/\alpha) is not an upper bound when (0<\beta<1). This is repairable and does not create dimension dependence.

### O-C2 — exact O'Neill types are absent

The seed defines (\mathcal A_XY=P^{\mathcal V}D\bar Y[X]) for basic horizontal (X,Y), then writes compositions with (\mathcal A_YZ) as a vertical argument without defining the horizontal-output (\mathcal A_XV) type. It also gives no exact four-tensor formula. A norm bound on a “universal finite signed sum” is not a proof of the required curvature operator, and it is not enough for a hostile sign/type check.

### O-C3 — Gronwall uses the wrong path datum

On ([0,1]), a length bound gives

\[
\int_0^1\|\dot L(t)\|_Fdt\le r_0,
\]

not (|\dot L(t)\|_F\le r_0) pointwise. Zeroth-order Gronwall can use the integral directly. Parameter derivatives additionally require integral bounds for the differentiated coefficient, including (\partial_\theta\dot L). These must be derived from the explicit endpoint-generated paths; they do not follow from length.

### O-C4 — derivative order is undercounted

If (H(A,B)=-\nabla_A\Log_AB), then a (j)-th derivative of (H) generically uses a ((j+1))-st derivative of Log together with connection derivatives through order (j). Curvature derivatives used by (k)-th PT/surface variation likewise require an explicit shifted order. A table claiming every row through (k_0) while proving Log only through (k_0) and Hessian only through (k_0-1) does not meet a target that labels the Hessian consumer itself through order (k_0). The campaign needs a backward order ledger.

### O-C5 — “explicit constant” is not explicit yet

The symbols (c_k) are unspecified and no induction gives their recurrence. The proposed (e_k) only inflates an unknown coefficient. A compliant output can be coarse, but it must be an actual finite recurrence based on the finite list of primitive derivatives, fixed Richardson weights, fixed blend profile, path variation norms, and total length.

### O-C6 — positivity proof must vary the correct argument

Since (H(A,A)=I_A), the shortest local proof fixes (A), follows (B_s=\Exp_A(s\Log_AB)), and integrates (\nabla_BH(A,B_s)[\dot B_s]) as an endomorphism of (T_A). The seed instead invokes “base-varying tangent spaces” without a formula. If it intends to vary both entries, connector derivatives and the diagonal map (A\mapsto H(A,A)) enter. Either route can work, but the present line does not prove (6.6).

## 5. Exact dependency audit to G1 and PF

### 5.1 G1 reach

The positive three-stage G1 proof needs, on every actual/proxy/population/empirical tuple:

1. a typed score bound (|\Log_A X|_{A,\rm BW}\le R_{\rm score});
2. a Hessian lower bound (H(A,X)\succeq\kappa I), preferably obtained from a proven normal radius;
3. score/Hessian law derivatives and Exp/Log/Richardson derivatives to the exact bias order;
4. a complete generated-domain event before those derivatives are invoked;
5. fixed Richardson weights and a fixed blend profile;
6. grid-uniform constants whose probability control may depend on the number of evaluated tuples, even though the deterministic geometry constant does not.

The fixed spectral band reaches only the invariant matrix derivatives. A normal radius reaches Hessian positivity only for pairs inside that radius. Neither reaches law smoothness, score concentration, energy, dependence, or generated-event probability. A final theorem may set all geometric radii below one declared (r_0), but the proof must first show which minimum/maximum is being taken.

### 5.2 PF reach

The polygonal frame proof needs an inequality of the form

\[
\|P_{\widehat{\rm poly}}-P_{\rm true}\|_{op}
\le C_{\rm BW}
\left\{
L_\mu r_{\mu,\rm grid}
+M r_{\mu,\rm grid}^2
+K_\mu M^{-2}
\right\},
\tag{5.1}
\]

up to the exact canonical discretization convention. Here (L_\mu) is a typed total mean-path length/speed budget, (K_\mu) is the (C^2) chord-defect budget, (M) is the segment count, and (r_{\mu,\rm grid}) is the grid RMS error. The deterministic geometric constant can be dimension-free while these multipliers remain visible.

The seed supplies neither (5.1) nor an equivalent cellwise summation. Its segment PT bound does not by itself prove the whole polygonal comparison. In particular:

- (M r_{\mu,\rm grid}^2) is an accumulation term, not a geometric derivative constant;
- (K_\mu M^{-2}) is not controlled by total path length, by CE-C2;
- a common constant cannot hide the number of cells;
- connector domains/codomains must be equal before subtracting transports;
- the curvature norm must be the normalized curvature-operator action used on the actual ruled planes, not sectional-curvature shorthand.

### 5.3 Downstream observation and lag consumers

If G1 and PF close, the robust feasible observation error still has the typed form

\[
q_{R,n}^{\rm BW}
\lesssim L_{\log}\{r_{\mu,n}+K_\mu M^{-2}\}
+r_{F,n}\{\mathcal E_{2,n}+L_{\log}r_{\mu,n}\}
+\rho_{\rm con,n}+\rho_{\rm obs,n}.
\]

BW-SIZE-FIXED-MARGIN supplies, at most, the geometric constants (L_{\log}) and those inside (r_F). It does not bound total energy, target contamination, (A_{2,n}), (\Delta_n), dependence, or factor selection. A lead claim that the common geometry constant directly proves G1/PF is acceptable only after the exact arrows above are filled; a claim that it proves lag/loading recovery by itself is false.

## 6. Required repairs for the complete-chain hostile pass

The later complete-chain audit should reject any proposed proof unless it contains all of the following:

1. an exact O'Neill or exact connection-derived curvature formula, with sign convention and horizontal/vertical types;
2. a backward derivative-order ledger from G1 and PF to square-root, polar, Sylvester, projector, connection, curvature, and PT primitives;
3. integral Gronwall in total path length and explicit (W^{1,1})-type bounds for endpoint/surface variations;
4. whole-polygon accumulation with total length, segment count, and direct-sum parameter norms visible;
5. the exact ruled maps and normalized curvature/operator area bound used in each PF cell;
6. an observation-variable Hessian Lipschitz proof yielding a numeric positive radius and covering every generated score pair;
7. complete generated-domain hypotheses and a noncircular localization/membership argument;
8. fixed blend/Richardson design constants;
9. an explicit recurrence or finite maximum defining the common constant;
10. a consumer table showing that the same compatible package reaches every G1 and PF occurrence without importing energy, law, dependence, signal, or eigengap conclusions.

## 7. First-pass objection table

| Claim | Attack | Repair or counterexample | Independent checker needed | Provisional status | Canonical consequence now |
|---|---|---|---|---|---|
| Projector derivatives are uniform | Joint derivative recurrence not fully stated | Give recurrence; no dimension counterexample found | Agent A + lead | **OPEN/REPAIRABLE** | none |
| Connection derivatives are uniform | Connection is not a tensor; chart/gauge typing missing | Define exact basic coefficient used by ODE | Agent A + lead | **MATERIAL GAP** | none |
| O'Neill chain is closed | No exact typed formula or sign | Replace Section 4 completely or derive curvature from connection | Agent A + lead | **OPEN — EXACT EQUATION** | no curvature/PF promotion |
| PT derivative bound is closed | false coefficient, length/speed substitution, no variation norm | repair by (4.1), integral Gronwall, explicit generated-path derivatives | Agents A/B + lead | **MATERIAL GAP** | no PT promotion |
| Polygon composition is harmless | no (M), total length, or product-rule bound | exact accumulation theorem; CE-C4 defeats per-segment reading | Agent B + lead | **OPEN — DIRECT CONSUMER** | PF remains unverified |
| Normal radius is uniform | incorrect/unstated tensor variation route | exact (B)-variable Hessian Lipschitz integration | Agents A/B + lead | **MATERIAL GAP** | G1 coercivity unverified |
| Generated bands close maps | scalar Richardson rank collapse | full generated membership event and output margin | Agent B + lead | **DISPROVED AS SHORTCUT** | raw bands insufficient |
| Path length controls all path derivatives | CE-C2 | separate endpoint-map derivatives from mean-path jets | Agent B + lead | **DISPROVED AS OVERBROAD CLAIM** | retain (K_\mu) separately |
| Any fixed-width blend is covered | CE-C3 | fix one profile and include its (C^{k_0}) norm | Agent B + lead | **DISPROVED AS UNIFORM DESIGN CLAIM** | design constant required |
| Repeated positive eigenvalues need a gap | identity-base invariant calculus | remove eigengap; retain zero-singular-value margin | Agent A + lead | **REJECTED ATTACK** | no multiplicity margin |
| Fixed band implies bounded energy/radius | CE-C1 | retain separate (r_0)/energy assumptions | lead | **DISPROVED AS SHORTCUT** | no statistical reach |
| Proposed (C_{\rm BW}) is explicit and common | unspecified constants, omitted path/design norms, no consumer maximum | define recurrence and exact finite maximum | all | **NOT ESTABLISHED** | no canonical edit |

## 8. Message for the lead

The invariant fixed-margin theorem remains analytically possible; this pass found no valid fixed-((\alpha,\beta,\chi,r_0,k_0)) dimension counterexample after retaining a correctly interpreted full generated-domain package. It did find material proof defects, two exact overbreadth counterexamples (path length versus higher jets; unspecified blend profiles), and three indispensable dependency separations (band versus radius/energy, segment versus whole polygon, geometry versus G1/PF statistical consumers). The lead should not adjudicate the node as proved until the required repairs survive the complete-chain and second hostile passes.

## 9. Mandatory complete-chain hostile pass 1

This section audits the first complete Agent A and B dossiers together. It does no work on any later margin regime and does not adjudicate Stage 1.

### 9.1 Verdict

The combined route remains analytically viable: I found no retained-hypothesis family forcing an \(m\), \(\sqrt m\), trace, or multiplicity-gap factor. Agent A's projector, tangent norm, connection sign at the identity, and O'Neill relative signs pass direct checks. Agent B's PT ODE, corrected coefficient, isometry, Hessian lift formula, and the algebraic shape of the PF accumulation pass direct checks.

The combined proof is not closed. Load-bearing defects remain in Agent A's moving-adjoint curvature derivatives and coarse bound (7.3), and in Agent B's whole-polygon derivative accumulation, varying initial fibre, generated-domain nonemptiness, exact ruled-area producer, G1 constraint-domain reach, and common constant (9.1). These are repairable proof/formula defects unless the repairs fail; they are not a dimension counterexample.

### 9.2 Agent A attacks

#### A-C1 — identity, connection, and O'Neill signs

At \(L=I\), Agent A gives

\[
P_I^{\mathcal H}Z=(Z+Z^T)/2,
\quad
Z_{U,V}(I)=-UV/4,
\]

\[
(\nabla_UV)^H_I=-(UV+VU)/8,
\quad
\mathcal A_UV=(VU-UV)/8.
\]

These have the correct horizontal/vertical types and \(\mathcal A_UV=-\mathcal A_VU\). Under Agent A's curvature convention, its four-tensor (5.2) implies its operator form (5.5), and \(W=X,Z=Y\) gives \(+3\|\mathcal A_XY\|_F^2\). The relative O'Neill coefficients therefore pass this hostile check.

#### A-C2 — invalid zeroth coarse simplification

Agent A obtains connection/A-tensor contributions

\[
2\beta/\alpha^2
\quad\text{and}\quad
\beta^{3/2}/\alpha^2
\]

but replaces their sum by \(3\beta^{3/2}/\alpha^2\). That domination requires \(\beta\ge1\). For \(0<\beta<1\) the displayed algebra is false. Use, for example,

\[
a_0=(2\beta+\beta^{3/2})/\alpha^2
\]

or \(3\max\{\beta,\beta^{3/2}\}/\alpha^2\). This is a fixed-margin constant repair, not a dimension counterexample.

#### A-C3 — moving adjoint/subspace is not yet differentiated

Agent A has

\[
\mathcal A_L:\mathcal H_L\times\mathcal H_L\to\mathcal V_L,
\qquad
\mathcal A_X^\dagger:\mathcal V_L\to\mathcal H_L.
\]

The domains and codomains move with \(L\). The phrase “after enlarging \(a_j\) to include projector derivatives” does not define the fixed-space map whose ordinary derivative appears in (5.7)--(5.8). A valid repair is to define an ambient extension such as

\[
\widetilde{\mathcal A}_L(X,Y)
=P_L^{\mathcal V}
\mathcal A_L(P_L^{\mathcal H}X,P_L^{\mathcal H}Y),
\]

take its Frobenius adjoint on the fixed ambient matrix space, and insert the projector recurrences explicitly. Until then the curvature derivative row is a material gap.

#### A-C4 — coarse bound (7.3) is unverified

The recurrence-defined maximum (7.2) could become a valid explicit constant after A-C2/A-C3. The closed claim

\[
C_A\le (k_0+2)^{k_0+2}(k_0+2)!\,
\Lambda_A^{16(k_0+2)^2}
\]

does not follow from the dossier: no induction bounds the node count/depth of \(\gamma_j,\widehat r_j\), and the undefined adjoint enlargement is already inside \(r_j\). I find no counterexample to the existence of some coarse finite bound; this particular bound is **unverified**, not disproved. Prove a node-count induction or retract (7.3) and retain a fully defined repaired recurrence.

#### A-C5 — derivative-order shift

A \(j\)-th derivative of \(\mathsf H=-\nabla\Log\) generally consumes a \((j+1)\)-st Log derivative and connection derivatives through \(j\). Ruled/PT variation similarly shifts curvature orders. The shared label \(k_0\) is not an order ledger. A and B must work backward from the exact G1/PF consumers and run primitive recurrences to whatever finite shifted order results.

### 9.3 Agent B transport attacks

#### B-C1 — PT ODE and isometry pass

The formulas

\[
(L^TL)\Omega+\Omega(L^TL)=H^T\dot L-\dot L^TH,
\quad \dot H=L\Omega,
\]

\[
\|\dot H\|_F\le(\sqrt\beta/\alpha)
\|\dot L\|_{\rm op}\|H\|_F,
\quad
\frac d{dt}\|H\|_F^2=0
\]

are correct. Zeroth-order PT is dimension-free and isometric.

#### B-C2 — varying initial fibre is omitted

When the initial base varies, a fixed ambient \(H(0)\) is not horizontal for every \(L(0,\theta)\). The endpoint-varying PT map needs an explicit initial-fibre trivialization, such as \(P_{L(0,\theta)}^{\mathcal H}\) applied to a fixed ambient input or a radial connector. Its derivatives become initial data in the variational equation. Agent B's Bell polynomial (4.8) contains only coefficient budgets \(K_j\), so it does not yet prove the full endpoint-varying PT derivative.

#### B-C3 — per-segment \(+1\) aggregation fails

Agent B proves per segment

\[
K_{q,j}\le C_{\mathrm{ode},q}(1+\ell_j)
\]

and defines \(K_q^{\rm pol}=\sum_jK_{q,j}\). Therefore its own inequalities imply

\[
\boxed{
K_q^{\rm pol}
\le C_{\mathrm{ode},q}(N+\mathsf L_N)
\le C_{\mathrm{ode},q}(N+r_0),}
\]

not \(C_{\mathrm{ode},q}(1+r_0)\). PT isometry prevents a multiplicative \(C^N\); it does not erase this additive sum. Under an \(\ell^2\) vertex direct-sum norm a naive shared-vertex estimate can still cost \(\sqrt N\); segmentwise normalized parameters cost \(N\).

Thus B-PTK/B-POLY are **not proved segment-free**. A repair must expose \(N\), choose a path-level variation norm, or prove exact shared-vertex/gauge cancellation. This is not yet a counterexample to PF because PF can use the separate cellwise curvature-area route rather than differentiating the whole polygon map.

#### B-C4 — curvature convention mismatch

Under Agent A's convention and commuting surface coordinates,

\[
\nabla_t\nabla_sW-\nabla_s\nabla_tW
=R(F_s,F_t)W.
\]

Agent B writes \(R(F_t,F_s)W\), the negative. Its norm bound is sign-free, but the exact shared formula must be synchronized.

#### B-C5 — higher ruled derivatives remain schematic

Repeated surface differentiation introduces \(\nabla^qR\), mixed derivatives of \(F_s,F_t\), endpoint/initial-field derivatives, and commutator terms. “A Bell polynomial” is not the requested exact recurrence or order ledger. This row remains open pending the actual canonical ruled maps and boundary data.

### 9.4 Agent B Hessian, GD, and PF attacks

#### B-C6 — Hessian formula passes; full G1 reach does not

The lift identity

\[
\overline{\mathsf H(A,B)U}
=P_L^{\mathcal H}
\{E-D_L\mathcal N(L,M)[E]\}
\]

has the correct sign. At \(A=B=I\), \(D\,\mathrm{polar}_I[E]=0\) for symmetric \(E\), so \(\mathsf H(A,A)=I\). Holding \(A\) fixed and integrating the observation derivative is the right noncircular route to

\[
\|\mathsf H(A,B)-I_A\|_{\rm op}
\le L_Hd_{\rm BW}(A,B).
\]

But pairwise Hessian positivity is not yet the full G1 stage-minimizer theorem. That consumer also needs a named compact strongly geodesically convex constraint domain, existence/uniqueness there, every internal \(q\)-observation pair within the positive-Hessian set, and population-stage interior slack. GD names no such constraint set and the spectral band alone is not declared geodesically convex.

#### B-C7 — GD nonemptiness is false as stated for arbitrary inputs

An Exp output in \(\mathcal B_{\alpha,\beta}\) has factor norm at most \(\sqrt\beta\), so requiring \(\sigma_{\min}(L+H)\ge\chi\) forces \(\chi\le\sqrt\beta\). Example:

\[
\alpha=1,\quad\beta=4,\quad\chi=3
\]

makes the Exp-output portion empty. This refutes the unconditional nonemptiness sentence, not the theorem on a compatible nonempty domain.

The ball in B (1.6) also omits lower-band slack. To keep a Richardson factor above \(\sqrt\alpha\), include

\[
\delta<(\sqrt c-\sqrt\alpha)/5
\]

as well as the displayed \(\sqrt c-\chi\) and upper-band slacks. If the same \(\chi\) is imposed on polar inputs, choose \(c\in(\alpha,\beta)\) with \(\chi<\min\{c,\sqrt c\}\). State this compatibility explicitly.

#### B-C8 — growing-grid generated event is not propagated

From grid RMS alone,

\[
\max_{0\le j\le N}e_j\le\sqrt{N+1}\,r_N.
\]

Thus fixed population slack \(\delta_{\rm GD}\) requires

\[
\sqrt{N+1}\,r_N=o(\delta_{\rm GD})
\]

unless a separate sup rate is used. Complete chord/connector/ruled images also need Lipschitz image control, not merely endpoint membership. Section 7 does not state this statistical reach.

#### B-C9 — Richardson condition is not band closure

B (7.3) correctly gives an invertibility/Exp margin. It cannot retain the same lower band \(\alpha I\) for nonzero signed movement unless a separate inner-band slack exists. B does retain a full GD membership test, so the final theorem must use nested bands/inner slack and must not call (7.3) alone “band closure.”

#### B-C10 — PF algebra passes after an unproved area producer

If B (8.2) holds, then

\[
\sum_j\ell_j(e_j+e_{j+1})
\le2v_\mu\sqrt{(N+1)/N}\,r_N,
\quad
\sum_je_j^2=(N+1)r_N^2,
\]

and the PF shape

\[
v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}
\]

is correct and keeps segment accumulation visible.

The missing step is (8.2). Bounded derivatives of an unnamed “nested chord” ruled map do not by themselves yield the sharper area scaling

\[
\ell_j(e_j+e_{j+1})+e_j^2+e_{j+1}^2.
\]

B must write the exact two ruled triangles, their boundary conditions, and the Taylor/area argument showing first-order vanishing at coincident errors. Therefore (8.7) is not yet proved, although its downstream algebra is sound.

The per-segment \(+1\) failure and the PF area route are distinct: the former defeats segment-free derivatives of the whole polygon; it does not by itself disprove cellwise PF accumulation.

### 9.5 Common-constant and consumer audit

Agent A (7.3) is unverified for A-C2--A-C4. Agent B (9.1) is not a mathematical constant as written because its powers contain malformed commas. Even reading those commas as typographical:

- \(C_A^*\) includes only connection/curvature constants, while B also consumes projector, lift, square-root, polar, alignment, and initial-fibre constants;
- no proof shows \(10\Lambda C_A^*\) dominates those primitives;
- the whole-polygon derivative still carries the unresolved \(N\)-aggregation;
- fixed blend-profile derivative constants are not numerically specified.

So neither proposed display is yet the requested common \(C_{\rm BW}(\alpha,\beta,\chi,r_0,k_0)\).

Exact downstream separation must remain:

| Consumer | Geometry may supply | Separate nongeometric input |
|---|---|---|
| G1 score/Hessian | Log/Hessian derivative constants and local \(\kappa\) | observation radius, law derivatives, concentration, dependence |
| generated event | Lipschitz image/margin conversion | population slack and sup or \(\sqrt N r_N\) probability control |
| PF | curvature/ruled/PT coefficient | \(v_\mu r_N+(N+1)r_N^2+v_\mu a_\mu N^{-2}\) |
| feasible observations | Log/connector/frame constants | tangent energy and statistical errors |
| lag/loading | none beyond feasible geometry | dependence, target, \(A_2,\Delta\), selector window |

### 9.6 Complete-chain objection table

| Claim | Attack | Repair or counterexample verdict | Pass-1 status | Consequence |
|---|---|---|---|---|
| A connection/O'Neill relative signs | identity and sectional checks | pass under A convention | **PASS** | synchronize B sign |
| A \(a_0\) works for all \(\beta\) | invalid \(\beta<1\) simplification | replace coarse constant | **REPAIR** | recompute curvature envelope |
| A moving adjoint derivatives | moving H/V spaces not embedded explicitly | define ambient projected extension | **MATERIAL GAP** | (5.7)--(5.10) open |
| A coarse (7.3) | no node-count induction; depends on prior gap | prove induction or retract | **UNVERIFIED** | no common constant |
| B PT ODE/isometry | direct sign/type check | pass | **PASS** | zeroth PT closes |
| B endpoint PT derivatives | varying initial fibre omitted | add initial-trivialization terms | **MATERIAL GAP** | connector derivatives open |
| B whole-polygon derivative independent of \(N\) | per-segment \(+1\) sums to \(N+\mathsf L\) | expose \(N\) or prove cancellation/new norm | **FAILED AS PROVED** | B-PTK/B-POLY open |
| A/B curvature convention | \(R(F_s,F_t)\) versus \(R(F_t,F_s)\) | flip consistently | **REPAIR** | norm bound may survive |
| B Hessian radius reaches G1 | no convex constrained stage domain | declare/prove domain and internal pair reach | **MATERIAL GAP** | G1 not closed |
| GD nonempty for arbitrary five inputs | \(\chi>\sqrt\beta\) empties Exp outputs; lower slack omitted | state compatibility/corrected ball | **FALSE AS STATED** | avoid vacuity |
| generated event follows from RMS | maximum costs \(\sqrt{N+1}\) | add slack condition or sup rate | **REPAIR** | GD probability open |
| Richardson test closes same band | it gives factor margin only | nested band/full test | **SHORTCUT REJECTED** | domain remains load-bearing |
| B area (8.2) | exact ruled triangles/Taylor scaling absent | derive producer | **MATERIAL GAP** | PF not yet proved |
| B common (9.1) | malformed/incomplete and ignores segment issue | replace completely | **FAILED** | no common constant |
| repeated positive spectra need eigengap | invariant maps smooth | reject attack | **NO COUNTEREXAMPLE** | zero-singular margin only |
| hidden \(\|L\|_F\)/trace factor | all displayed primitive multiplications inspected | none found | **PASS SO FAR** | dimension-free route viable |

### 9.7 Lead handoff

Before the second hostile pass:

1. B must repair the per-segment \(+1\) aggregation or display exact \(N\)-dependence.
2. A must define the ambient O'Neill adjoint extension and prove/retract coarse (7.3).
3. B must add varying-initial-fibre terms, synchronize curvature signs, and prove the PF area row.
4. The lead must require compatible/nonempty GD parameters, a true G1 constraint domain, the \(\sqrt N r_N\) slack condition, and a backward derivative-order table.
5. Both common-constant displays must be replaced or fully proved.

No canonical edit is justified. No fixed-margin dimension counterexample has been found. Await A/B repairs and then rerun the entire chain.

## 10. Mandatory second hostile pass on the repaired chain

This pass rereads the repaired Agent A Sections 4.1, 5, 7, and 12 and the repaired Agent B GD, Sections 3--9, 14.5, and 13. It corrects one error in my first hostile pass and attacks every repair from definitions to the G1/PF consumers.

### 10.1 Correction of my pass-1 A-C2 objection

My objection to Agent A's

\[
a_0=3\beta^{3/2}/\alpha^2
\]

was wrong and is withdrawn. Agent A (4.10) bounds

\[
X=\mathcal L_A^{-1}(UT+TU)
\]

before the term \(-XL\) in (4.6) is formed. Multiplication by \(L\) adds \(\|L\|_{\rm op}\le\sqrt\beta\), so that contribution is \(2\beta^{3/2}/\alpha^2\); (4.11) contributes another \(\beta^{3/2}/\alpha^2\). The displayed \(a_0\) is valid for every \(\beta>0\).

This correction does not resolve the separate moving-gauge/recurrence issues below.

### 10.2 Agent A repair audit

#### A2-C1 — ambient extension idea is correct, displayed adjoint is malformed

Defining

\[
\widetilde{\mathcal A}_L(X,Y)
=\mathbf A_L(d\pi_LP_L^HX,d\pi_LP_L^HY)
\]

is a valid way to place the moving horizontal inputs into a fixed ambient matrix space. The adjoint should be the applied operator

\[
\mathcal A_X^\dagger\xi
=P_L^H\,
\widetilde{\mathcal A}_{L,P_L^HX}^{\,*}
\bigl(P_L^V\xi\bigr).
\tag{10.1}
\]

Agent A (4.18) instead contains a comma between
\(\widetilde{\mathcal A}^{*}\) and \(P_L^V\xi\), so the boxed display is not a well-formed map. The intended repair is evident and dimension-free, but the exact formula must be corrected before (5.5) is said to have a differentiated ambient representative.

#### A2-C2 — the new recurrence mixes base and lift derivatives

The repaired recurrence does not consistently type \(a^{\rm coef}\):

- Section 4.13/4.15 defines \(a_j^{\rm coef}\) from ordinary \(D_L^j\mathbf A_L(U,V)\), with \(L\) the lift variable.
- Equations (7.3)--(7.7) build \(a^{\rm coef}\) using base-\(A\) Sylvester derivatives, the principal-root sequence \(l\), and \(p=h\circledast l\). That is a base-\(A\) derivative of the coefficient evaluated in the principal section.
- The next line defines \(a^L=a^{\rm coef}\circledast g^L\), composing again with \(L\mapsto LL^T\).

If \(a^{\rm coef}\) is already \(D_L\mathbf A_L\), the last composition double-counts the Gram map. If it is a base-\(A\) coefficient in the principal section, it is not the \(D_L\) coefficient claimed in Section 4.13.

Moreover, for an arbitrary lift \(L=A^{1/2}Q\), the actual ambient tensor differs from its principal representative by the gauge \(Q=A^{-1/2}L\). Derivatives in vertical/gauge directions require derivatives of \(Q\), or the entire curvature calculation must be declared intrinsic in the principal base section and differentiated only in \(A\). The repaired recurrence does neither explicitly.

This is a material recurrence/type gap. It does not exhibit a dimension factor: derivatives of \(Q=A^{-1/2}L\) are themselves dimension-free on the band. A repair is available, but (7.9)--(7.11) are not yet proved as written.

#### A2-C3 — moving-adjoint concept repaired, numeric recurrence still pending

Once A2-C1/A2-C2 are fixed, taking an adjoint in a fixed Frobenius space adds no norm factor, and differentiating the outer \(P_H/P_V\) projectors is legitimate. The withdrawal of the unsupported closed power bound is correct.

The recurrence-defined \(C_A\) is not yet a valid common producer because its sequences \(\widetilde a,a^\dagger,\rho,\widehat\rho\) depend on the inconsistent \(a^L\) construction above. The hostile status is therefore:

- fixed-order uniform curvature remains likely and has no counterexample;
- the proposed explicit recurrence is **not closed**.

#### A2-C4 — derivative-order floor repaired

Using \(K=\max\{k_0,2\}\) correctly supplies the first observation derivative of the Hessian when \(k_0=1\). The stated shift \(\nabla^qR\), \(q\le k_0-1\), for \(k_0\)-th ruled variation is acceptable once B writes the exact recurrence. This objection is resolved.

### 10.3 Agent B repair audit

#### B2-C1 — segment-count repair accepted

Agent B now states

\[
K_s^{\rm pol}\le C_s\{N+\mathsf L(\gamma)\}
\]

in the direct-sum maximum norm and retains the corresponding Bell-polynomial \(N\)-dependence. This is the honest correction. It distinguishes the generic independently parameterized polygon map from the PF ruled-area route. The per-segment \(+1\) objection is resolved by narrowing/exposing dependence, not by proving an \(N\)-free generic derivative.

#### B2-C2 — varying initial fibre, connector typing, and curvature sign repaired

Equations (4.9a)--(4.9b) add the initial trivialization derivatives and type the endpoint-varying operator. Equations (8.1a), (8.3), and (8.7) insert endpoint connectors before subtraction. Section 5 now uses Agent A's convention and \(R(F_s,F_t)\). These repairs pass, conditional on the repaired primitive recurrence.

#### B2-C3 — mixed observation derivative repaired

Agent B now writes

\[
D_B\overline{\mathsf H(A,B)U}[V]
=-P_L^H D_MD_L\mathcal N(L,M)[\dot M,E],
\]

which is the correct mixed derivative. The normal-radius route is no longer one polar derivative short.

#### B2-C4 — GD compatibility is still incomplete because polar and Exp margins differ in scale

The repaired GD assumes only \(\chi<\sqrt\beta\) and chooses

\[
c=\{\beta+\max(\alpha,\chi^2)\}/2.
\]

The same \(\chi\) is imposed on:

1. an Exp/output factor \(L+H\), whose singular values scale like \(\sqrt c\);
2. a polar input \(M^TL\), whose singular values scale like \(c\).

The scalar construction therefore also needs \(c>\chi\), not merely \(\sqrt c>\chi\). For example,

\[
\alpha=0.01,\qquad \beta=0.25,\qquad \chi=0.4
\]

satisfies \(\chi<\sqrt\beta=0.5\), while the prescribed
\(c=(0.25+0.16)/2=0.205<0.4\). At the proposed scalar base,

\[
\sigma_{\min}(M^TL)=c<\chi.
\]

Thus the claimed nonempty example still fails. With one common \(\chi\), compatibility requires a \(c\in(\alpha,\beta)\) satisfying

\[
c>\max\{\chi,\chi^2\},
\]

so a sufficient global condition is

\[
\max\{\chi,\chi^2\}<\beta.
\tag{10.2}
\]

For perturbations, ensuring each factor is at least \(\sqrt\chi\) is what guarantees the product polar margin \(\chi\). The lower slack in (1.6) must therefore include

\[
\sqrt c-\sqrt\chi
\]

in addition to \(\sqrt c-\sqrt\alpha\) and \(\sqrt c-\chi\).

This refutes only B's repaired nonemptiness claim for all \(\chi<\sqrt\beta\). It is not a counterexample to the theorem on a compatible generated domain.

#### B2-C5 — the local G1 ball proof still misses a factor-three band slack

For \(A,B\in\mathcal D_c\), B correctly notes that a point \(q\) on their chord obeys

\[
d_{\rm BW}(q,A_*)\le3\rho_c.
\]

It then applies the Hessian bound along the chord before it has proved the chord stays inside \(\mathcal D_c\). To know the invariant derivative/Hessian bound is available on the declared band, the \(3\rho_c\)-ball around \(A_*=cI\) must itself remain inside the band. The current choice only requires

\[
\rho_c<\sqrt c-\sqrt\alpha,
\qquad
\rho_c<\sqrt\beta-\sqrt c,
\]

not three times those inequalities. A direct repair is

\[
3\rho_c<
\min\{\sqrt c-\sqrt\alpha,\sqrt\beta-\sqrt c,\rho_H\}.
\tag{10.3}
\]

After (10.3), strong convexity of \(q\mapsto\tfrac12d(q,A_*)^2\) along the chord does prove that the ball is geodesically convex. As written, the domain-reach proof is incomplete but repairable.

The nonempty perturbation example also needs a smallness condition relative to \(\rho_H\) to verify every internal criterion pair, not just the spectral/Exp margins.

#### B2-C6 — growing-grid generated-event condition remains absent

The repaired Section 7 still says uniform stage convergence places empirical tuples inside the strict inequalities, without choosing the sup-rate route or stating the RMS-to-maximum condition

\[
\sqrt{N+1}\,r_N=o(\delta_{\rm GD}).
\tag{10.4}
\]

The canonical PF route consumes grid RMS, so (10.4), or a stronger independently proved sup event, must be propagated. This was not repaired.

#### B2-C7 — the PF area producer remains unproved

Agent B retypes the global transport difference correctly, but (8.2) is unchanged:

\[
\operatorname{Area}(F_j)
\le C_J\{\ell_j(e_j+e_{j+1})+e_j^2+e_{j+1}^2\}.
\]

No exact formulas for the two ruled triangles or derivative calculation producing the \(\ell e+e^2\) scaling were added. Section 9's symbol \(g_q\), described as the expression-tree majorant of a “canonical nested-chord ruled map,” is not a definition of that map and cannot prove first-order vanishing at \(e_j=e_{j+1}=0\).

The algebra from (8.2) to (8.7) remains correct, but its load-bearing geometric producer is still open.

#### B2-C8 — repaired common recurrence is not fully defined

Agent B (9.1) now uses

\[
\mathbf a_q=\max\{q_q,p_q,h_q,b_q,\gamma_q,\widehat r_q\},
\]

but the repaired Agent A notation uses \(p_q^{\rm pol}\), \(\widehat\rho_q\), and the expanded sequences in (7.11). The symbols \(p_q\) and \(\widehat r_q\) are ambiguous/withdrawn, and the recurrence does not explicitly substitute Agent A's repaired \(C_A\).

Further:

- \(g_q\) refers to an unwritten nested-chord ruled formula;
- \(w_0=1+C_{R,0}\mathsf A_0\) contains an actual ruled-area budget, but (9.7) claims dependence only on the five campaign inputs without displaying or bounding \(\mathsf A_0\);
- (9.6) writes actual norms \(\|\nabla^bF_s\|\), \(\|\nabla^cF_t\|\) and says they are bounded by \(g\), but the direction magnitudes that generate the PF factors \(\ell_j,e_j\) are not separated from the operator constants;
- the generic polygon derivative is correctly excluded from (9.7), but the target must still record its explicit \(N\)-dependent coefficient separately.

Therefore \(C_B^{\rm rec}\) is not yet a fully computable five-input recurrence and does not yet dominate the exact PF producer.

### 10.4 Second-pass counterexample classification

| Attack | Retains the corrected theorem hypotheses? | Verdict |
|---|---|---|
| repeated positive eigenvalues | yes | no failure; invariant calculus remains smooth |
| \(A_m=I_m,B_m=cI_m\) fixed band | no fixed radius as \(m\to\infty\) | proves band does not imply radius/energy, not theorem failure |
| high-frequency small-amplitude mean path | fixed band and length, but unbounded acceleration | proves \(r_0\) does not replace \(a_\mu\), not fixed canonical-path-map failure |
| \(\chi<\sqrt\beta\) scalar GD example above | retains B's repaired stated compatibility but violates its polar-margin conclusion | analytic counterexample to B's nonemptiness claim; repair by (10.2) |
| independently varied \(N\)-segment polygon | yes, with explicit \(N\) retained | no theorem failure after B's narrowing |
| raw-band Richardson rank collapse | violates generated output margin | disproves raw-band closure shortcut only |

No analytic family satisfying the fully corrected band, polar/Exp, normal-pair, generated-path, total-length, fixed-design, and explicit segment/path-smoothness package forces dimension dependence. Fixed-margin theorem falsity is not established.

### 10.5 Second-pass objection table

| Claim | Second-pass attack | Resolution status | Final hostile status | Canonical consequence |
|---|---|---|---|---|
| A \(a_0\) is invalid for \(\beta<1\) | pass-1 omitted final \(L\) multiplication | corrected/withdrawn | **PASS** | retain A (4.12) |
| A ambient O'Neill repair | intended formula sound; boxed adjoint malformed | one-line formula repair | **MINOR EXACT-TYPE DEFECT** | curvature recurrence not yet exact |
| A recurrence (7.3)--(7.11) | mixes \(D_L\) coefficient, principal base section, and a second Gram composition; gauge \(Q\) omitted | requires retyping/rederivation | **MATERIAL GAP** | \(C_A\) not proved |
| A order floor | \(K=\max(k_0,2)\) | repaired | **PASS** | normal-radius derivative order available |
| B generic polygon derivatives | \(N\) now explicit in max direct-sum norm | repaired by narrowing | **PASS** | exact \(N\) dependence retained |
| B initial fibre/connectors | (4.9a)--(4.9b), (8.1a) | repaired | **PASS** | endpoint maps typed |
| A/B curvature sign | B now uses \(R(F_s,F_t)\) | repaired | **PASS** | exact convention synchronized |
| B Hessian mixed derivative | (6.3a) | repaired | **PASS** | local radius route viable |
| B GD nonempty | Exp margin compatibility does not imply polar-input compatibility | repair (10.2) and \(\sqrt\chi\) slack | **COUNTEREXAMPLE TO STATED NONEMPTINESS** | current package may be empty |
| B G1 ball convexity | chord is only known within \(3\rho_c\), while band slack is only \(\rho_c\) | impose (10.3) | **MATERIAL DOMAIN GAP** | G1 reach incomplete |
| B generated event | no sup route or (10.4) | add exact localization condition | **MATERIAL REACH GAP** | GD probability unproved |
| B PF area (8.2) | exact ruled triangles/Taylor scaling still absent | must derive | **IRREDUCIBLE CURRENT GAP** | PF not proved |
| B common recurrence (9.1)--(9.7) | undefined/old A symbols, unwritten ruled map, uncapped \(\mathsf A_0\) | replace after A/PF repairs | **NOT ESTABLISHED** | no common constant |
| fixed-margin dimension counterexample | all retained families checked | none found | **NO DISPROOF** | do not call later stages impossible |

### 10.6 Second hostile verdict for the lead

The repaired dossiers do not yet earn Gate A. Agent A's invariant primitive strategy remains credible, and Agent B repaired the segment-count, endpoint-fibre, sign, mixed-Hessian, and derivative-order objections. But four load-bearing equations remain unproved:

1. a consistently typed intrinsic-or-ambient Agent A curvature recurrence;
2. a compatible and genuinely nonempty full GD package covering both polar and Exp margins and the G1 constraint ball;
3. the exact ruled-cell area estimate (8.2), with grid-event reach;
4. one fully defined common recurrence reaching every G1/PF constant while leaving \(N,v_\mu,a_\mu,r_N\) visible.

There is still no valid fixed-margin counterexample, so Gate B is unavailable. Under the campaign's status rules, the present analytical state is **OPEN — EXACT REPAIRS ABOVE**, not “disproved” and not “impossible.” The later margin stage remains blocked unless the lead supplies and independently verifies these equations.

## 11. Superseding true final hostile pass on the frozen repaired chain

This section is the mandated final hostile pass on the frozen Agent A and Agent B files. It **supersedes Section 10 wherever the later files repaired an objection**. Section 10 remains only as provenance for what was attacked and why the repairs were required.

### 11.1 Final Agent A audit

#### A2-C1 — ambient adjoint: repaired

Agent A (4.18) is now the applied, well-typed map

\[
\mathcal A_X^\dagger\xi
=P_L^{\mathcal H}\!\left[
\widetilde{\mathcal A}_{L,X}^{*}
\bigl(P_L^{\mathcal V}\xi\bigr)\right].
\]

The fixed-ambient adjoint preserves the Frobenius operator norm. The outer \(P_H/P_V\) derivatives and both internal \(d\pi_LP_H\) input-slot derivatives are present in (7.9)--(7.10). The stale comma/type objection is closed.

#### A2-C2/A2-C3 — gauge and recurrence: repaired

The final recurrence no longer composes a principal-section coefficient with a second Gram map. Its order is:

1. differentiate \(\mathbf A_L\), \(\widetilde{\mathcal A}_L\), the moving adjoint, and the curvature coefficient wholly in the arbitrary lift \(L\), using
   \[
   v_0^L=1,\quad v_j^L=h_j,\quad
   a^{\rm coef,L}=v^L\star\bar z,\quad
   \widetilde a=a^{\rm coef,L}\star d\star d,\quad
   a^\dagger=h\star\widetilde a\star v^L;
   \]
2. only after this equivariant ambient calculation, compose with the principal root as a computational section and insert the three basic horizontal input lifts and the horizontal output:
   \[
   \rho^A
   =p\star(\rho\circledast l)\star b\star b\star b.
   \]

Every \(L\mapsto LL^T\), \(d\pi_L\), projector, input-lift, and root factor occurs exactly in its typed layer. Right-orthogonal equivariance makes the resulting base tensor independent of the computational section. No nonsmooth singular-vector/eigenvector gauge is differentiated.

The order ranges also close. Algebraic lists run through \(K=\max\{k_0,2\}\); \(\widehat\rho\) is required only through \(K-1\); the Hessian observation derivative at \(k_0=1\) uses algebraic order two but only curvature order zero. The withdrawn unsupported closed power is not used. The recurrence-defined \(C_A\) is finite and dimension-free.

#### A signs, norms, and edge cases

The O'Neill operator form still calibrates to
\(\langle R(X,Y)X,Y\rangle=3\|\mathcal A_XY\|_F^2\).
All products pay undifferentiated matrix coefficients in operator norm and differentiated directions in Frobenius/BW norm. The final \(a_0=3\beta^{3/2}/\alpha^2\) coefficient is valid; the contrary stale objection omitted the last multiplication by \(L\). Scalar, commuting-diagonal, repeated-eigenvalue, and arbitrary-gauge tests produce no contradiction or hidden \(\sqrt m\), trace, or \(\|L\|_F\).

**Final A verdict: PASS.**

### 11.2 Final Agent B audit and prior-objection dispositions

| Prior objection | Frozen-file repair | Final disposition |
|---|---|---|
| per-segment \(+1\) was incorrectly removed | (4.12)--(4.13) retain the Bell-polynomial \(N+\mathsf L\) dependence in the \(\oplus,\infty\) endpoint norm | **PASS; \(N\) remains explicit** |
| varying initial fibre and endpoint subtraction were untyped | (4.9a)--(4.9b), (8.1a), and \(c^{\rm end}=t\star t\star t\) include both connector trivializations and the inverse endpoint connector | **PASS** |
| curvature sign did not match Agent A | Section 5 uses the same convention and \(R(F_s,F_t)\) | **PASS** |
| Hessian observation derivative was one derivative short | (6.3a) uses \(D_MD_L\mathcal N\), and \(k_*=\max\{k_0,2\}\) supplies it | **PASS** |
| polar and Exp margins had incompatible scalar scales | GD now assumes \(\max\{\chi,\chi^2\}<\beta\), chooses \(c>\max\{\alpha,\chi,\chi^2\}\), and (1.6a) enforces \((\sqrt c-5\delta)^2>\chi\) | **PASS under the explicit compatible GD package** |
| the G1 ball used only one-radius band slack | (1.5a) imposes \(3\rho_c\) below both root-band slacks and \(\rho_H\); the preliminary chord is therefore in the Hessian domain before convexity is invoked | **PASS** |
| no growing-grid localization reached complete generated images | (7.5)--(7.6) require either the sup-grid event or \(\sqrt{N+1}r_N=o_p(\delta_{\rm GD}/C_B^{\rm rec})\) | **PASS; condition is explicit** |
| Richardson rank/band closure was inferred from raw bands | Section 7 separates the Exp-factor estimate from output-band, polar, chord, ruled, and interior membership tests | **PASS** |
| ruled-cell area (8.2) was asserted | (8.2a) defines the exact geodesic quadrilateral; endpoint Jacobi operators vanish at the opposite endpoint, giving (8.2b); (8.2c)--(8.2d) integrate to \(\ell_j(e_j+e_{j+1})+e_j^2+e_{j+1}^2\) | **PASS** |
| lens and PF accumulation hid segment growth | (8.3) telescopes with isometric outside factors; (8.5) uses the uniform-grid speed bound; (8.6) pays \(v_\mu a_\mu N^{-2}\); (8.7) leaves \((N+1)r_N^2\), \(v_\mu\), \(a_\mu\), and \(N\) visible | **PASS** |
| the proposed common recurrence used stale A symbols and an uncapped ruled budget | (9.1)--(9.7) use the exact A lists, isolate \(\widehat\rho\) at its consumed range, define the canonical ruled map by (8.2a), bound \(\mathsf A_0\le g_1^2\), include endpoint connectors, and exclude the stronger generic polygon derivative | **PASS** |

The PT ODE itself remains exact:

\[
(L^TL)\Omega+\Omega(L^TL)
=H^T\dot L-\dot L^TH,\qquad
\dot H=L\Omega,
\]

and PT is an isometry because \(H^TL\) is symmetric while \(\Omega\) is skew. The ruled-surface comparison is therefore additive in curvature-weighted area; it does not acquire \(C^N\).

The G1 coercivity route is no longer circular. The observation-Hessian derivative is uniform on the checked radial path, so
\(\rho_H=\min\{r_0,(2L_H)^{-1}\}\) is produced before the normal-pair restriction is used. The constraint ball is compact for each \(m\), lies uniformly away from the singular boundary, and is strongly geodesically convex by the three-radius argument.

### 11.3 Precision notes that do not block the fixed-margin theorem

Two literal notational/quantitative points should be normalized during canonical integration:

1. Agent A's square-root order-zero symbol is introduced as \(q_0^{\rm op}=\sqrt\beta\) and later abbreviated \(q_0\) in recurrence maxima. These are the same order-zero majorant.
2. The phrase in B (1.6a) that every generated factor is within exactly \(5\delta\) is immediate for the signed affine combination once its aligned inputs have that declared perturbation budget. Starting only from arbitrary noncommuting raw principal-factor perturbations, polar alignment can change the numerical neighborhood constant. This does not threaten nonemptiness: the all-equal centre \(cI\) has strict positive slack, every finite generated map has the dimension-free derivative bound \(C_B^{\rm rec}\), and a sufficiently smaller open Frobenius neighborhood, for example with radius capped by the population slack divided by the corresponding finite recurrence constant, remains inside every GD test. Canonical text should state that recurrence-controlled radius rather than treat the numeral \(5\) as a universal alignment Lipschitz constant.

Neither point creates a missing lemma, dimension factor, or counterexample to the theorem under GD.

### 11.4 Fresh retained-hypothesis counterexample search

The final search re-ran the following families:

- \(m=1\) and commuting diagonal families, including fixed bands with BW radius of order \(\sqrt m\);
- repeated positive eigenvalues and repeated positive singular values;
- arbitrary right-orthogonal gauges and noncommuting small perturbations;
- zero-length and many-segment polygons with independently varied vertices;
- high-frequency small-amplitude paths with bounded length but growing acceleration;
- signed Richardson combinations near the band boundary;
- RMS vertex errors concentrated at one grid point.

Each apparent failure now violates or activates an explicit visible hypothesis/input:

- the \(\sqrt m\) scalar family violates the fixed radius/energy condition;
- high-frequency paths pay the visible \(a_\mu\);
- generic endpoint derivatives pay the visible \(N+\mathsf L\);
- Richardson escape fails the GD output-membership/slack test;
- a concentrated grid error pays \(\sqrt{N+1}r_N\);
- polar/Exp near-singularity fails the declared \(\chi\) test.

No analytic matrix family retaining fixed \(\alpha,\beta,\chi,r_0,k_0\), the compatible GD package, the displayed path-smoothness inputs, and the exact G1/PF consumer assumptions violates a dimension-uniform bound.

### 11.5 Final dependency and gate recommendation

The frozen chain now reaches the direct consumers as follows:

\[
(\alpha,\beta,\chi,k_0)
\longrightarrow C_A
\longrightarrow
\{\Gamma,\nabla^qR,\mathrm{polar},\mathrm{Log},\mathrm{Hess}\},
\]

\[
(C_A,r_0)
\longrightarrow C_B^{\rm rec}
\longrightarrow
\{\text{G1 coercivity/generated closure},\text{PF ruled accumulation}\},
\]

with \(N,r_N,v_\mu,a_\mu\) and the stronger generic-polygon \(N+\mathsf L\) factor left visible rather than hidden in the five-input geometry constant.

My recommendation is **Gate A — fixed-margin proved under the explicit compatible GD assumptions**. Gate B is unavailable because no retained-hypothesis counterexample exists. Gate C is unnecessary because the former exact gaps have been repaired and the recurrence reaches G1/PF.

Shrinking margins **may start only after** the lead completes the Gate A actions: canonical integration of the fixed-margin theorem, archival of the Stage 1 dossiers/ledger, and termination of the Stage 1 team. It must then start with a fresh team and fresh ledger. This dossier performs no shrinking-margin analysis.
