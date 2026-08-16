---
type: wave-3-hostile-audit
title: P1-LOSS — Wave 3 audit BC
scope: hostile audit of P1-LOSS-B and P1-LOSS-C
auditor: non-author agent (Wave 3). Did not author, and did not read, any dossier script under /home/claude/verif. Every load-bearing computation below was re-derived from the definitions and recomputed in a fresh working directory (/home/claude/audit3).
date: 2026-08-15
method: independent re-derivation + sympy/numpy recomputation; second-order formulas checked against *exactly solved* barycentres and against Monte-Carlo barycentres of genuine Wishart draws; flagship configuration checked against the **exact** (non-expanded) barycentre.
---

# P1-LOSS — Wave 3 hostile audit of dossiers B and C

## 0. Headline

Four one-line verdicts, as requested.

- **The matrix bias formula B-3.2 / B-3.3 — CORRECT.** Re-derived independently; the operator form and the eigenbasis form agree to 1e-15; against exactly solved barycentres on SPD(3) and SPD(4) the residual is `O(ε³)` with the ratio converging to 8.00 under ε-halving. The λ_k in the numerator is right; nothing else belongs there.
- **The Wishart closed form B-3.5 — CORRECT, including the 1/4.** Verified symbolically for m = 1…5 and against Monte-Carlo barycentres of genuine Wishart draws at M = 100, 400 (ratio empirical/theory = 0.999–1.001, off-diagonals at Monte-Carlo zero). Its *commentary* is wrong in one place: for a genuine Wishart proxy the rotation does **not** "return at O(M⁻²)" — it is **exactly zero at every order**.
- **The expansion at the flagship configuration — VALID, and the dossier's numbers are conservative, but the status label "PROVED" is not earned.** I computed the exact barycentre at m = 12, M = 21 and got 8.82 %→35.86 % (BW) and 32.92 % (AIRM) against the dossier's 8.9 %→33.4 % and 31.0 %. The expansion is far more accurate at m/M = 0.57 than one has any right to expect (1–7.5 % relative error), and it errs *downward*. But the dossier had no remainder bound and no right to call a truncated expansion at m/M = 0.57 "PROVED (arithmetic)". The smallest-eigenvalue entry is understated by 7.5 % relative. **I independently agree with the lead's later check** — see §2.5a for the cross-comparison, a sharper isotropic computation that needs no barycentre iteration at all, and a stress test establishing that the expansion does not break anywhere in the admissible range M > m or at condition numbers up to 100.
- **The GMV theorem C-7.1 — CORRECT and unusually clean.** Exact scale invariance verified to 1e-17; the Jacobian ∂w/∂H at m = 12 has numerical rank exactly **11** out of 78. The codimension argument is sound.

Nine other findings follow, four of them MATERIAL. Nothing in either dossier is FATAL. Two constructive formulas (the recalibration constants) are **inverted** and would misapply in practice; one stated parameter range in §4.2 is wrong at both ends; one "theorem" in dossier C (C-E3.2) does not follow from its stated proof.

## 1. Findings table

Most severe first.

| Claim ID | Verdict | Exact objection or corrected statement | Severity |
|---|---|---|---|
| **B-5.2 (§4.2, 2nd para)** | **OVERTURNED** (the range statement only; the isotropic result stands) | The dossier claims the general-spectrum relative distortion "lies between 1/(4M) … and m/(4M)+1/(4M)". Both ends are wrong. The k = i term contributes exactly 1/4 always, so as λ_i dominates the sum → 1/4 + 1/4 and the **infimum is 1/(2M)**, twice the claimed lower bound. As λ_i is dominated the sum → (m−1) + 1/4, so the **supremum is (m−½)/M**, not (m+1)/(4M). At m = 12 that is 11.5/M against a claimed 3.25/M — a factor 3.54. (m+1)/(4M) is the *isotropic* value and is an interior point of the range, not a bound. Corrected sentence: "the relative distortion lies in (1/(2M), (m−½)/M), attaining (m+1)/(4M) in the isotropic case." | **MATERIAL** |
| **B-5.5 (§5.1) and B-5.6 (§5.2)** | **SUSTAINED WITH CORRECTION** (conclusions right, both constants inverted) | §5.1 defines recalibration as ρ acting *inside* the loss, L̃(y,h)=L(y,ρ(h)), and then asserts "if ρ = Φ⁻¹ … then argmin_h E L̃ = Σ". That is backwards. E L(Σ̂,u) is minimised at u = Φ(Σ); setting u = ρ(h) and solving ρ(h) = Φ(Σ) gives h = Σ **iff ρ = Φ**, not Φ⁻¹. With ρ = Φ⁻¹ the minimiser is Φ(Φ(Σ)) = (1−κ)²Σ. Consequently §5.2's AIRM constant `c = (1−(m+1)/(2M))⁻¹` is inverted: under §5.1's own convention the correct scalar is **c = 1 − (m+1)/(2M)**. Verified symbolically (m=1 two-point law, κ=0.234375): c = Φ gives argmin = 1.000000, c = Φ⁻¹ gives argmin = 0.586182. At the flagship the dossier's c = 1.448 yields argmin = 0.477Σ — a 52 % error where 0 was claimed. (If the intent was post-hoc recalibration of a geodesically-trained model's *output*, then Φ⁻¹ is right and §5.1's definition is what must change. The dossier states both and they are mutually inconsistent; one of the two must be fixed.) The *qualitative* content — exact for AIRM, partial for BW — is independently confirmed: Σ_k λ_k²/(x+λ_k)² has derivative −2Σλ_k²/(x+λ_k)³ < 0, hence is strictly decreasing, hence constant across i iff all λ_i are equal. ("or m = 1" in B-5.6 is redundant: m = 1 is a special case of "all equal".) | **MATERIAL** |
| **C-E3.2** | **NOT PROVED AS WRITTEN** | The Cauchy–Schwarz step is correct and the infill limit is correct (both verified numerically — see §2.7). The **theorem does not follow**. Stated: "No estimator can be conditionally unbiased for [(∫σ²ds)^{1/2}] and infill-consistent, because its infill limit would have to be both objects at once." An estimator that is conditionally unbiased for (∫σ²)^{1/2} and infill-consistent for (∫σ²)^{1/2} has one limit, not two; there is no contradiction. Cauchy–Schwarz only kills the *absolute-variation family*, whose limit is ∫σ ds. The literal universal claim is **false**: take σ_s = σ_a on [0,½] and σ_s = cσ_a on [½,1] for a known c ≠ 1 (non-constant volatility). C-E3.1's estimator run on the first half is exactly conditionally unbiased for σ_a; multiplying by √((1+c²)/2) gives an estimator that is both conditionally unbiased for (∫σ²)^{1/2} and infill-consistent. **Repair available and stronger than what is written:** the real obstruction is operator-Jensen at the conditioning step, exactly as in C-E3.4's log argument. √ is operator concave, so E[(Σ*)^{1/2}|F] ≺ (E[Σ*|F])^{1/2} = Σ^{1/2} strictly for non-degenerate conditional laws (verified: the difference has eigenvalues 0.019, 0.040, 0.087 > 0 on a random 4-atom law). The dossier makes this argument for log and not for the root, where it is equally available. | **MATERIAL** |
| **C-E2.2 (§1.2)** | **SUSTAINED WITH CORRECTION** | Two defects. (a) The sentence "by B-3.2 the two barycentres differ at order M⁻¹ **with the explicit constant above**" is wrong on the constant. B-3.5's constant is derived for a *degenerate* latent law (Σ* ≡ Σ given F); when the latent conditional law has O(1) spread the linearisation runs through the Fréchet Hessian at a non-degenerate barycentre, which is not the identity. Measured (m=3, 4 latent atoms with eigenvalue range 12.6:1, per-atom mean-matched Wisharts, N = 6×10⁵ per atom): gap×M converges to **1.149** at M = 400/1600/6400 (1.1527, 1.1490, 1.1491), against B-3.5's constant of **1.321** evaluated at Σ and **1.250** evaluated at the latent barycentre. Order Θ(M⁻¹) is right; the constant is 13–15 % off and is not B-3.5's. (b) **Internal contradiction and precisely the conflation the campaign polices**: the claim table row C-E2.2 reads "…is **not** consistent for it", while §1.2's parenthetical reads "BW-loss minimisation is **consistent** for the latent barycentre under infill". Both cannot be the row's statement. The table row should read "is not *conditionally unbiased* / not equal at fixed M, though consistent under infill". | **MATERIAL** |
| **B-5.3** | **SUSTAINED WITH CORRECTION** (numbers understated; status label unearned) | The arithmetic reproduces exactly: my independent evaluation of (3.5) at m = 12, M = 21, λ = linspace(3.0, 0.5, 12) gives 8.906 % → 33.370 % and (3.7) gives 30.952 %. But B-3.5/B-3.7 are truncated expansions with an unbounded O(ε³) remainder, and m/M = 0.571 is not a small-noise regime — the Marchenko–Pastur support at q = 0.571 is [0.06, 3.08], i.e. the proxy's own spectrum is spread by a factor 50. Calling the resulting table "PROVED (arithmetic from B-3.5/B-3.7)" is a status error: an unbounded truncation error is not arithmetic. **I therefore computed the exact barycentre.** Exact BW at the flagship: **8.816 % → 35.864 %** (fixed point converged to 4.8e-13 on N = 1.5×10⁵ mean-matched genuine Wishart draws). Exact AIRM: **32.922 %** (closed form, no Monte Carlo — see §2.5). So the expansion survives, with relative error 1.0 % at the largest eigenvalue rising monotonically to **7.5 % at the smallest**, and it errs **downward** in 11 of 12 entries. Corrected row: BW 8.8 %–35.9 % (second-order approximation 8.9 %–33.4 %), AIRM 32.9 % (second-order 31.0 %); status **PROVED to second order, exact values computed numerically**. Separately, the `m = 3, M = 500` row quotes "0.13 % to 0.37 %" without stating the spectrum, so it is not reproducible; and "shrinks the covariance by roughly a third" is true of AIRM but not of BW, whose mean shrink is ≈ 19 %. **Stress-tested** (§2.5a): the expansion holds to <8 % relative all the way down to M = 13 (m/M = 0.92, one step above singularity) and is insensitive to condition numbers up to 100, so m/M is *not* the fragile ingredient. The fragile ingredient is that B-3.5's hypothesis (3.4) constrains only second moments while the remainder is governed by E[Δ³]; the flagship numbers are safe because realised covariance is approximately Wishart, not because (3.4) suffices. That substitution of a stronger law for a weaker hypothesis is undeclared. | **MATERIAL** |
| **B-3.5 (commentary)** | **SUSTAINED WITH CORRECTION** (the boxed formula is right; the rotation remark is wrong) | "eigenvector rotation for such a proxy reappears only at O(M⁻²)" is **false for a genuine Wishart proxy**, and the flagship proxy is a genuine Wishart. Proof (mine, exact, no expansion): for Σ̂ = Σ^{1/2}(W/M)Σ^{1/2} with W ~ W_m(I,M) and Σ diagonal, conjugation by any sign matrix D = diag(±1) leaves the law of Σ̂ invariant (D commutes with Σ^{1/2}, and the law of W is orthogonally invariant); the BW barycentre is equivariant under orthogonal conjugation (verified to 2.3e-15); uniqueness then forces D H* D = H* for all 2^m sign matrices, hence **H\* is exactly diagonal in Σ's eigenbasis at every order**. The correct statement is: "for a *general* law satisfying (3.4) only, rotation is bounded by O(M⁻²); for a genuine Wishart it is exactly zero." The dossier's version understates its own result and misdescribes the flagship case. | MINOR |
| **C-7.2 (AIRM bullet)** | **SUSTAINED WITH CORRECTION** (true, wrong proof) | "the Wishart-case AIRM distortion is H* = (1−(m+1)/(2M))Σ **exactly to second order** — a pure scalar multiple. … it is therefore **entirely invisible** to GMV." Scalar *to second order* only buys invisibility up to the O(M⁻²) residual, which is not in general scalar; "entirely invisible" is stated more strongly than the given argument proves. The conclusion is nevertheless **exactly** true, by an argument the dossier does not give: the AIRM (Karcher) mean is equivariant under congruence, A ↦ CAC^T (verified to 1.3e-15 relative), and W ~ W_m(I,M) is orthogonally invariant, so bary_AIRM(Σ^{1/2}(W/M)Σ^{1/2}) = Σ^{1/2}·hI·Σ^{1/2} = hΣ **exactly, all orders**, with log h = (1/m)[Σ_{i=1}^m ψ((M+1−i)/2) + m log 2 − m log M]. Under hypothesis (3.4) alone (a second-moment condition) the exactness genuinely fails and only the second-order statement survives. State the difference; the dossier states neither. | MINOR |
| **C-7.2 (BW bullet)** | **NOT PROVED AS WRITTEN** (numeric unreproducible; qualitative conclusion independently confirmed) | "a comparable non-scalar spectral shrink moved the GMV weights by ‖Δw‖ ≈ 0.02 — detectable in principle, negligible against sampling noise in a 240-month panel." The configuration is not specified, so the number cannot be checked; run at the dossier's own flagship (m=12, M=21, λ = 3.0→0.5) I get **‖Δw‖₂ = 0.0404** in the eigenbasis and 0.0384 in a random basis, i.e. **12 % of ‖w‖₂**, double the quoted figure. "Negligible against sampling noise" is asserted with no sampling-noise computation. The qualitative claim does survive on a better statistic than ‖Δw‖: the *excess GMV variance* w(H\*)ᵀΣw(H\*)/w(Σ)ᵀΣw(Σ) − 1 = **1.17 %** (eigenbasis) / **1.43 %** (random basis), which is indeed small — this is the number the dossier should quote, since a GMV evaluation consumes realised portfolio variance, not the weight vector. | MINOR |
| **B-2.4** | **SUSTAINED WITH CORRECTION** (all algebra exact; the "boundary reason" is an artefact) | Every number verified symbolically: E x̂ = 1; E√x̂ = 1 − a²/2 for a ≤ 1; E L(x̂,H₁) = a²; E L(x̂,H₂) = a² − a⁴/4; reversal margin a⁴/4 > 0; true loss L(1,H₂) = a⁴/4 (equal to the margin). Two objections. (i) The restriction a ∈ (0,1] is exactly right **for the stated H₂ = (1−a²/2)²**, and the §7 note that a = 1.5 "correctly fails, confirming the stated restriction" is confirming a property of the *parameterisation*, not of the phenomenon. The proxy is unbiased for all a ∈ (0,2), and for a ∈ (1,2) the true barycentre is (E√x̂)² = a²/4, giving reversal margin (2−a)²/4 > 0 and true loss (1−a/2)² > 0. **The reversal holds on all of (0,2).** Presenting (0,1] with a failure at a = 1.5 as the boundary is a restriction stated without its real boundary reason. (ii) At the endpoint a = 1 the proxy puts mass 3/4 on x̂ = 0, i.e. on the boundary of the cone — which violates B-2.2's own standing hypothesis "law charges the open cone" and (in the m ≥ 2 lift) makes Σ̂ singular. Either exclude a = 1 or note that only the loss, not the barycentre theory, is being used there. The √m factor in the m ≥ 2 lift is a common positive scale on both losses and correctly does not matter (d²_BW(xI,hI) = m(√x−√h)², verified symbolically). | MINOR |
| **B-3.3 (rotation criterion)** | **SUSTAINED WITH CORRECTION** | G_ij, (G²)_ij and B_ij all re-derived and confirmed, including the index placement: the numerator weight is **λ_k**, not √(λ_iλ_j) — it arises as s_k·s_k from G_ik G_kj = (s_i s_k Δ_ik/(λ_i+λ_k))(s_k s_j Δ_kj/(λ_k+λ_j)), and the outer s_i s_j is cancelled by the Σ^{-1/2}(·)Σ^{-1/2} conjugation. The rotation angle B_ij/(λ_i−λ_j) is standard first-order perturbation theory and is confirmed numerically in §3.6 (predicted −1.667e-4 at ε = 0.05, observed eigenvector off-diagonal 1.67e-4). **Objection:** the criterion and the angle formula both break at degenerate eigenvalues, where λ_i = λ_j makes the angle undefined and Σ's own eigenvectors are not unique, so "zero eigenvector rotation ⟺ B_ij = 0 for all i≠j" is false as stated. The claim needs an explicit non-degeneracy hypothesis, and near-degeneracy is where the second-order rotation is *largest* — exactly the case a covariance application cares about. Nowhere mentioned. | MINOR |
| **B-3.2** | **SUSTAINED** (formula), **NOT PROVED AS WRITTEN** (rigour label) | The formula is right (see §2.3). But the derivation *posits* B = O(ε²) rather than establishing it, gives no bound on the O(ε³) remainder, and never states the regularity under which E and the expansion may be interchanged. This is a formal expansion; the honest label is "PROVED as a formal second-order expansion; remainder verified numerically to be O(ε³)", not "PROVED". The step "replacing H by Σ to leading order" **is** legitimate: B = O(ε²) and the term it sits in is already O(ε²), so the substitution perturbs at O(ε⁴). Confirmed by the observed exact ε³ scaling. | MINOR |
| **B-E5.2** | **SUSTAINED** (order), **overstated in prose** | The order is exactly right and I verified it in closed form and by Monte Carlo: for dX = α dt + σ dW with M equal increments, E[RV] = σ² + α²/M exactly, so the drift bias is Θ(M⁻¹) (M = 21/84/336 → 1.072e-1 / 2.679e-2 / 6.724e-3 against α²/M = 1.071e-1 / 2.679e-2 / 6.696e-3). **But**: "fails at *exactly the same order* … as the distortion" is true of the order and misleading about the magnitude. Relative drift bias is α²/(Mσ²); the geodesic distortion constant is (m+1)/4 = 3.25 at m = 12. With any plausible equity α/σ (say α = 0.05/yr, σ = 0.2/yr) the drift constant is 0.0625 — **~50× smaller**. The weak-point column does say "only the order is consumed", so this is declared; §6.2's prose ("a genuine and uncomfortable finding") is not proportionate to a factor-50 constant gap. | MINOR |
| **B §7 ("No status … rests on numerics alone")** | **OVERTURNED** | Three statuses do rest on numerics alone: B-3.8's "in the noncommuting case it does not [coincide with AIRM], and the discrepancy was verified numerically to be O(1) relative"; B-3.6's "the eigenvector matrix of H\* is not a signed permutation"; and C-7.2's ‖Δw‖ ≈ 0.02. All three happen to be **true** (I get LE-vs-AIRM relative discrepancy 0.197 at O(1), a genuine 1.67e-4 rotation, and ‖Δw‖ = 0.040), but the blanket sentence is false and should be replaced by naming the three. | MINOR |
| **C-E3.2 (displayed line)** | **SUSTAINED WITH CORRECTION** | The intermediate display in §2.2, "E[Σ|r_ℓ| | σ] = √(2/(πM)) Σ_ℓ(∫_{I_ℓ}σ²ds)^{1/2}·√M → √(2/π)·√M⋯", is dimensionally garbled: it carries both √(1/M) and √M and arrows to a divergent expression. The correct identity is E[Σ_ℓ|r_ℓ| | σ] = √(2/π) Σ_ℓ(∫_{I_ℓ}σ²ds)^{1/2}, with no M-power at all. The final limit is right (verified: M = 200/2000/20000 give 0.86125/0.86107/0.86122 against ∫σ = 0.861179 and (∫σ²)^{1/2} = 0.913392). | MINOR |
| **C-E2.3** | **SUSTAINED WITH CORRECTION** | The linearity argument, the direction of the error and the VaR arithmetic are all right (√0.7 = 0.8367, a 16.3 % understatement ✓). The quoted "by 9 %–33 %" should read 8.8 %–35.9 % per the exact computation; and "H\* ⪯ Σ in the sense that its spectrum is uniformly shrunk" is loose phrasing — H\* ≺ Σ genuinely holds here (H\*−Σ = B is negative definite under (3.4)), but "spectrum is uniformly shrunk" is not what ⪯ means and is only equivalent because the eigenbasis is shared. | MINOR |
| **B-2.1** | **SUSTAINED** | The variational identity, the concavity-as-infimum-of-affines argument and the strictness argument are all correct. Strictness: 2G(·,Σ) affine on a segment forces the midpoint optimiser T* to be optimal throughout (an affine majorant equal at an interior point), and T*AT* = Σ throughout then forces T*HT* = 0, hence H = 0. A concave function that is affine on no segment is strictly concave. No objection. The claim-table weak-point note ("strictness fails on the commuting scalar ray") is confusing and appears to be wrong — on the scalar ray G(xI,Σ) = √x·tr Σ^{1/2} is strictly concave in x — but nothing depends on it. | NONE |
| **B-2.2** | **SUSTAINED** | Every primitive verified from scratch: T Σ T = A to 7e-15; d²= tr(LΣL); ⟨V,V⟩_Σ = ½tr(V S_Σ[V]) = d²; Exp∘Log = id to 9e-15; d²(Σ,Exp_Σ(tV)) = t²⟨V,V⟩ to 10 digits at t = 0.1…1.0. The reduction E[Log_H Σ̂] = 0 ⇒ E T = I ⇒ E[(H^{1/2}Σ̂H^{1/2})^{1/2}] = H is correct, and the Sylvester step is valid: X ↦ XH + HX has eigenvalues λ_i+λ_j > 0 for H ≻ 0, hence injective. Independently confirmed by direct numerical minimisation of E d²_BW over the Cholesky chart on a random 5-atom law on SPD(3): the minimiser and the fixed point agree to 2.3e-8 (the optimiser's tolerance), fixed-point residual 7.8e-16. | NONE |
| **B-3.1, B-3.4** | **SUSTAINED** | Trivially correct and correctly labelled exact. | NONE |
| **B-3.5 (boxed formula)** | **SUSTAINED** | Verified symbolically for m = 1,2,3,4,5: off-diagonals identically zero, B_ii = −(λ_i/M)[1/4 + Σ_k λ_k²/(λ_i+λ_k)²], isotropic value −(m+1)/(4M)·λ. **The 1/4 is right** and it does come from k = i: λ_i·λ_i²/(2λ_i)²/M = λ_i/(4M). Verified against genuine Wishart draws (Bartlett, N = 1.5×10⁶, mean-matched control variate) at m = 3, Σ = diag(3,1,0.5): empirical/theory = (0.9987, 0.9998, 1.0005) at M = 100 and (0.9997, 1.0013, 1.0003) at M = 400, with off-diagonals at 6.8e-6 and 1.7e-6 — exactly the Monte-Carlo floor ‖Δ‖²/√N, i.e. indistinguishable from zero. | NONE |
| **B-3.6** | **SUSTAINED** | Genuinely a disproof. Conditional unbiasedness is exact (mean − Σ = 0.0 to machine zero); both atoms are positive definite (min eigenvalue 0.9975 at ε = 0.05 with Σ = diag(3,2,1)); the exact barycentre gives B₁₃ = −3.3347e-4 against theory −ε²λ₂/((λ₁+λ₂)(λ₂+λ₃)) = −3.3333e-4 (ratio 1.00042, improving to 1.00002 at ε = 0.01); and the eigenvector matrix of H\* carries an off-diagonal of 1.67e-4 in the (1,3) slot against the predicted angle −1.667e-4, so it is not a signed permutation. The general "purely spectral" claim is dead. Worth stating that the rotation is O(ε²/(λ_i−λ_j)) and therefore *second-order small*, which the §3.6 rhetoric does not say. | NONE |
| **B-3.7** | **SUSTAINED** | Re-derived from E[log(H^{-1/2}Σ̂H^{-1/2})] = 0. The (m+1) factor confirmed symbolically at m = 1,2,3,4,5 (isotropic B_ii/λ = −(m+1)/(2M) = −1/M, −3/(2M), −2/M, −5/(2M), −3/M) and against genuine Wishart Karcher means: empirical/theory = (1.0014, 1.0007, 1.0007) at M = 100 and (1.0014, 1.0003, 1.0000) at M = 400. Against exactly solved Karcher means of a 5-atom law on SPD(3) the residual is O(ε³) with ratio 8.05 under ε-halving. The m = 1 digamma cross-check is right. | NONE |
| **B-3.8** | **SUSTAINED** | H\*_LE = exp(E log Σ̂) is exact and trivial. The Daleckiĭ–Kreĭn route was re-derived and both ingredients checked against finite differences: D²log_Σ[X,X]_ij = 2Σ_k X_ik X_kj ℓ[λ_i,λ_k,λ_j] to 2.2e-7, and D exp_Λ[Y]_ij = Y_ij/ℓ[λ_i,λ_j] to 3.4e-8. Formula (3.8) then reproduces exp(E log Σ̂) with residual O(ε³) (ratio 8.01). The m = 1 specialisation ℓ[λ,λ,λ] = −1/(2λ²), ℓ[λ,λ] = 1/λ ⇒ −EΔ²/(2λ) is right and coincides with AIRM. Commuting case: |B_LE − B_AIRM| = 2.2e-16. Noncommuting: relative discrepancy 0.197, i.e. O(1) — the dossier's claim confirmed. Diagonality under (3.4) confirmed symbolically. (Caution for whoever implements this: the second divided difference at repeated arguments is ℓ[x,x,y] = (f′(x) − f[x,y])/(x−y); I initially coded the negative of this and it silently degrades the formula from O(ε³) to O(ε²) accuracy while leaving all off-diagonals correct.) | NONE |
| **B-5.1** | **SUSTAINED** | Θ(M⁻¹) rate follows from (3.1). Γ(cH) = √c Γ(H) is exact and follows from G((cH)^{1/2}A(cH)^{1/2}) = √c·G(H,A); verified to 12 digits at c = 1/4, 4, 9 (ratios 0.500000000000, 2.000000000000, 3.000000000000). | NONE |
| **B-5.4** | **SUSTAINED** | λ_k²/(λ_i+λ_k)² is strictly decreasing in λ_i termwise, so |B_ii|/λ_i is strictly decreasing in λ_i; verified monotone across the flagship spectrum (8.91 % → 33.37 %). The scope warning about Δ_n is correct and correctly placed. | NONE |
| **B-5.7** | **SUSTAINED** | Correct and correctly labelled conditional on a fourth-moment model. | NONE |
| **B-E5.1** | **SUSTAINED** | E[RV] = IV + 2Mσ_u² verified by simulation (σ = 0.4, σ_u = 0.001: M = 21/84/336 give 0.1600242/0.1601565/0.1606784 against 0.1600420/0.1601680/0.1606720). Θ(M) versus Θ(M⁻¹) is real and the two effects genuinely move in opposite directions. | NONE |
| **B-E5.3** | **SUSTAINED** | The consistency-vs-conditional-unbiasedness distinction is correct and the "absence of an unbiasedness theorem is not a proof of bias" disclaimer is present and correctly worded. Not independently re-verified against the primary sources (out of this audit's scope; see LO-7 file). | NONE |
| **C-7.1** | **SUSTAINED** | w(cH) = w(H) to 1e-17 at c = 0.1, 3, 100. The dimension count is exactly right: I formed the 12×78 Jacobian of H ↦ w(H) by central differences at a random SPD(12) and its numerical rank is **11** (singular values drop from 8.48e-2 to 1.58e-10 between the 11th and 12th). The codimension argument is sound: {H ≻ 0 : H^{-1}𝟏 ∥ v} = {H : Hv ∈ span 𝟏} imposes m−1 independent linear conditions on Sym(m). One pedantic footnote: the image of H ↦ [H^{-1}𝟏] is not all of ℝP^{m−1} but the open subset {[v] : vᵀ𝟏 ≠ 0} (since vᵀ𝟏 = vᵀHv > 0); this does not change the dimension count. | NONE |
| **C-7.3** | **SUSTAINED** | The calibration-regression slope 1/(1−β) is right for a scalar distortion; the VaR and QLIKE remarks are right. | NONE |
| **C-E2.1** | **SUSTAINED** | The measurement-scheme dependence is real and ∂H\*/∂(1/M) ≠ 0 follows from (3.5). This is the strongest argument in dossier C. | NONE |
| **C-E3.1** | **SUSTAINED** | E|r_ℓ| = σ√(2/(πM)) for r_ℓ ~ N(0, σ²/M), so √(πM/2)·M⁻¹Σ|r_ℓ| is exactly unbiased for σ; the two hypotheses doing the work are correctly identified. | NONE |
| **C-E3.3, C-E3.4** | **SUSTAINED** | The non-commutativity argument and the strict-operator-concavity argument for log are both correct, and C-E3.4 is the *model* for how C-E3.2 should have been argued. The M < m singularity remark is right, though at the flagship M = 21 > m = 12 so log Σ̂ is defined there — the dossier says "only barely nonsingular", which is fair. | NONE |
| **C-7.4, C-7.5** | **SUSTAINED** | Cross-checked against the LO-7 verbatim record. The attribution is scoped as narrowly as the evidence supports: the training loss (their Eq. 7), the GMV evaluation (§5, Table 4), the LRV citation scoped to Frobenius/Euclidean *evaluation* metrics, the preprint caveat, and the explicit "silence is not error" and "this is our theorem, not their defect" statements. I find **no claim about these authors that goes beyond what is quoted**. This is the best-disciplined external claim in either dossier. | NONE |
| **C-ATT** | **NOT INDEPENDENTLY AUDITED** | Rests on A-4.2/A-4.3, which are outside this audit's write scope. The table's internal logic is coherent and each row's "which hypothesis it attacks" is correctly assigned. Flagged only so the closure record does not treat it as audited here. | — |

## 2. Independent recomputation — code and output

All scripts in `/home/claude/audit3` (not part of the repository). No file under `/home/claude/verif` was opened.

### 2.1 BW primitives and the barycentre fixed point (B-2.2)

```python
T = Sig^{-1/2}(Sig^{1/2} A Sig^{1/2})^{1/2} Sig^{-1/2};  L = T - I;  V = L Sig + Sig L
```
```
T Sig T = A residual: 7.11e-15          T symmetric: 1.11e-16
d^2 vs tr(L Sig L): 1.5186011208812218  1.5186011208812311
S_Sig[Log] = T-I residual: 6.66e-16
metric 0.5 tr(V L): 1.5186011208812316  vs d^2: 1.5186011208812218
Exp_Sig(Log_Sig A) = A residual: 9.33e-15
  t=0.1: d^2=0.0151860112  t^2<V,V>=0.0151860112
  t=1.0: d^2=1.5186011209  t^2<V,V>=1.5186011209
```
Direct Nelder–Mead minimisation of E d²_BW over the Cholesky chart, 5-atom law on SPD(3), against the Álvarez-Esteban fixed point:
```
max |optimiser - fixed point| = 2.31e-08
residual of E[(H^1/2 S H^1/2)^1/2] - H : 7.77e-16
eigs of H : [0.630906 0.856365 1.48968]   (Sylvester operator eigenvalues lam_i+lam_j > 0)
```

### 2.2 B-2.4, sympy

```
E xhat = 1   (holds for p in (0,1), i.e. a in (0,2))
E sqrt(xhat), a<=1 : (2 - a**2)/2        E sqrt(xhat), a>1 : a/2
E L(xhat,H1) = a**2                      E L(xhat,H2) = -a**4/4 + a**2
E L(H1) - E L(H2) = a**4/4               true L(1,H2) = a**4/4
(E sqrt x)^2 == H2 : True
a>1 with the dossier's H2:  a=3/2 -> 0.5 vs 0.828125, reversal False   (dossier's check reproduces)
a>1 with the TRUE barycentre H2*=(a/2)^2:
   E L(H1) = 2 - a ;  E L(H2*) = 1 - a**2/4 ;  diff = (a - 2)**2/4  > 0 on (0,2)
   a=1.2 -> 0.800 vs 0.640 reversal True, true loss 0.160
   a=1.9 -> 0.100 vs 0.0975 reversal True, true loss 0.0025
a=1 endpoint: atoms are [4.0, 0.0] with probs [0.25, 0.75]   <- singular realisation
d_BW^2(xI,hI) = m(sqrt x - sqrt h)^2 : True
```

### 2.3 B-3.2 / B-3.3, against exactly solved barycentres

Expansion check, (H²+E)^{1/2} = H + D₁ + D₂, D₁ = S_H[E], D₂ = −S_H[D₁²]:
```
eps=1e-02 |r after D1|=1.62e-04 (/eps^2=1.622)  |r after D1+D2|=4.32e-06 (/eps^3=4.324)
eps=1e-03 |r after D1|=1.58e-06 (/eps^2=1.583)  |r after D1+D2|=4.19e-09 (/eps^3=4.192)
eps=1e-04 |r after D1|=1.58e-08 (/eps^2=1.579)  |r after D1+D2|=4.18e-12 (/eps^3=4.181)
```
Operator form vs eigenbasis form, and both vs the exact barycentre of a random 5-atom conditionally-unbiased law:
```
--- m=3 ---   |operator form - eigenbasis form| = 1.60e-16
  eps=0.080  |H*-Sig|=8.70e-04  |H*-pred|=2.46e-05  rel=2.75e-02  err/eps^3=0.04802
  eps=0.040  |H*-Sig|=2.20e-04  |H*-pred|=3.22e-06  rel=1.44e-02  err/eps^3=0.05033  ratio=7.63
  eps=0.020  |H*-Sig|=5.55e-05  |H*-pred|=4.12e-07  rel=7.38e-03  err/eps^3=0.05155  ratio=7.81
  eps=0.010  |H*-Sig|=1.39e-05  |H*-pred|=5.22e-08  rel=3.73e-03  err/eps^3=0.05218  ratio=7.90
--- m=4 ---   |operator form - eigenbasis form| = 1.89e-15
  eps=0.080  |H*-Sig|=5.25e-03  |H*-pred|=2.36e-04  rel=4.71e-02  err/eps^3=0.46112
  eps=0.040  |H*-Sig|=1.28e-03  |H*-pred|=2.48e-05  rel=1.98e-02  err/eps^3=0.38709  ratio=9.53
  eps=0.020  |H*-Sig|=3.16e-04  |H*-pred|=2.83e-06  rel=9.03e-03  err/eps^3=0.35346  ratio=8.76
  eps=0.010  |H*-Sig|=7.86e-05  |H*-pred|=3.37e-07  rel=4.31e-03  err/eps^3=0.33730  ratio=8.38
```
`err/eps^3` converging to a constant and `ratio` → 8 = 2³ is the signature of a correct second-order formula with a genuine O(ε³) remainder.

### 2.4 B-3.5 / B-3.7, symbolic and against genuine Wishart draws

Symbolic, from E[Δ_ab Δ_cd] = (1/M)(Σ_ac Σ_bd + Σ_ad Σ_bc) only, for m = 1…5:
```
m=1..5: BW off-diagonals all zero: True      AIRM off-diagonals all zero: True
        BW B_ii == -lam_i/M[1/4 + sum_k lam_k^2/(lam_i+lam_k)^2] : True
        AIRM B_ii == -lam_i(m+1)/(2M) : True
isotropic BW B/lam:  -1/(2M), -3/(4M), -1/M, -5/(4M), -3/(2M)   = -(m+1)/(4M)
isotropic AIRM B/lam: -1/M, -3/(2M), -2/M, -5/(2M), -3/M        = -(m+1)/(2M)
```
Monte Carlo, Bartlett-drawn W_3(diag(3,1,0.5), M)/M, N = 1.5e6, mean-matched:
```
M=  100  BW   empirical=[-0.01746 -0.01173 -0.00840] theory=[-0.01749 -0.01174 -0.00840] ratio=[0.9987 0.9998 1.0005]
         max|offdiag(H-Sig)| = 6.81e-06   (diag effect 1.75e-02; MC floor ~ ||D||^2/sqrt(N) = 8e-06)
     AIRM empirical=[-0.06008 -0.02001 -0.01001] theory=[-0.0600 -0.0200 -0.0100] ratio=[1.0014 1.0007 1.0007]
M=  400  BW   ratio=[0.9997 1.0013 1.0003]     max|offdiag| = 1.68e-06
     AIRM ratio=[1.0014 1.0003 1.0000]
```

### 2.5 Item 8 — the flagship configuration, exact

Isotropic Σ = I: the exact BW barycentre is hI with √h = E[(1/m)tr(W/M)^{1/2}]; the exact AIRM barycentre is hI with log h = (1/m)[Σ_{i=1}^m ψ((M+1−i)/2) + m log 2 − m log M] (no Monte Carlo).
```
  m    M   exact BW    2nd order (m+1)/(4M)   exact AIRM   2nd order (m+1)/(2M)
 12   21    16.063%          15.476%           32.922%          30.952%
 12   78     4.202%           4.167%            8.437%           8.333%
 12 1638     0.199%           0.198%            0.397%           0.397%
  3  500     0.200%           0.200%            0.400%           0.400%
  3   21     4.750%           4.762%            9.566%           9.524%
 12   42     7.857%           7.738%           15.867%          15.476%
 12  200     1.635%           1.625%            3.265%           3.250%
(m=3,M=500 and m=3,M=21 re-run at N=4e6/2e6: 0.2002% +- 0.0018% and 4.7504% +- 0.0122%)
```
Non-isotropic flagship, Σ = diag(linspace(3.0, 0.5, 12)), M = 21, exact barycentre of N = 1.5e5 genuine mean-matched Wishart draws, fixed point converged in 12 iterations to 4.8e-13:
```
  lam_i    exact rel. distortion   2nd-order (3.5)    ratio
  3.000          8.816%              8.906%          0.9899
  2.545         10.522%             10.500%          1.0021
  2.091         12.877%             12.664%          1.0168
  1.636         16.244%             15.722%          1.0332
  1.182         21.312%             20.286%          1.0506
  0.727         29.636%             27.682%          1.0706
  0.500         35.864%             33.370%          1.0747
AIRM exact (congruence-equivariant, h*Sigma): 32.922%   vs 2nd-order 30.952%
```
**Reading.** The expansion is valid at m/M = 0.571 to 1–7.5 % relative and errs downward. The dossier's headline survives; its *status label* does not, and its smallest-eigenvalue figure should be 35.9 %, not 33.4 %.

### 2.5a Item 8 — cross-comparison with the lead's later check, and a stress test

The lead subsequently ran the same flagship check (m = 12, λ = linspace(3, 0.5, 12), N = 3×10⁴ draws) and reports per-eigenvalue exact/second-order ratios of 0.99–1.08 with mean 1.034 at M = 21, 0.97–1.05 at M = 78, 0.99–1.11 at M = 200.

**My verdict: AGREE, and my computation is the tighter of the two.** My independent run at the same configuration used N = 1.5×10⁵ draws (5× the lead's) with an exact mean-matching control variate, and gives ratios **0.9899–1.0747, mean 1.031** — inside the lead's interval and materially narrower. Three points where my evidence is stronger than a Monte-Carlo barycentre:

1. **The isotropic case needs no barycentre iteration and no matrix Monte Carlo at all.** By orthogonal equivariance H\* = hI with √h = E[(1/m) tr (W/M)^{1/2}], so the whole question collapses to the mean of a scalar. At m = 12, M = 21 that gives exact/second-order = **1.0376** (Monte-Carlo se on √h of 6.7e-5, i.e. ~0.1 % of the effect), agreeing with the lead's 1.034 to within the lead's own error bar.
2. **The AIRM number involves no Monte Carlo whatsoever.** log h = (1/m)[Σ_{i=1}^m ψ((M+1−i)/2) + m log 2 − m log M] is exact and closed form. At m = 12, M = 21: exact 32.922 % against second-order 30.952 %, ratio **1.0637**. This is a hard number, not an estimate, and it is the single cleanest piece of evidence that the expansion holds at the flagship.
3. **The lead's residual off-diagonal (5.7e-3 against min |B_ii| = 1.67e-1) is not evidence of anything.** At N = 3×10⁴ the Monte-Carlo floor for the barycentre is ‖Δ‖²/√N ≈ 0.57/173 ≈ 3.3e-3, so 5.7e-3 is the noise level, not a measured rotation. My N = 1.5×10⁵ run gives 6.2e-4 against a floor of 1.5e-3. In fact the true off-diagonal is **exactly zero at every order** for a genuine Wishart proxy (sign-flip equivariance, §2.6), so no amount of Monte Carlo will ever resolve it. This should be stated as a theorem, not measured.

**Stress test — where would it break?** Two levers, both pushed to the limit:

```
isotropic Sigma=I, m=12, exact vs second order as M -> m   (N=6e5 per row)
    M    m/M    exact BW  2nd order   ratio  exact AIRM  2nd order   ratio
   13   0.92     26.973%    25.000%   1.079     58.623%    50.000%   1.172
   14   0.86     24.833%    23.214%   1.070     52.876%    46.429%   1.139
   16   0.75     21.441%    20.312%   1.056     44.788%    40.625%   1.102
   21   0.57     16.057%    15.476%   1.038     32.922%    30.952%   1.064
   30   0.40     11.091%    10.833%   1.024     22.499%    21.667%   1.038
   50   0.24      6.585%     6.500%   1.013     13.267%    13.000%   1.021
  100   0.12      3.274%     3.250%   1.007      6.562%     6.500%   1.010

spectral spread at m=12, M=21, exact barycentre (N=6e4, mean-matched)
cond=   6.0  exact  8.82% ->  35.83% | 2nd order  8.91% ->  33.37% | ratio 0.991-1.075 mean 1.030
cond=  30.0  exact  7.88% ->  48.64% | 2nd order  7.96% ->  47.09% | ratio 0.990-1.058 mean 1.025
cond= 100.0  exact  7.73% ->  52.62% | 2nd order  7.81% ->  51.95% | ratio 0.990-1.063 mean 1.024
```

Neither lever breaks it. Pushing M down to 13 — one increment above the point where the Wishart proxy becomes singular, m/M = 0.92 — costs only 8 % relative on BW and 17 % on AIRM, and the error is monotone and *always in the conservative direction*. Pushing the condition number from 6 to 100 does not degrade the ratio at all (it slightly improves, mean 1.030 → 1.024). So the expansion is not merely lucky at the flagship; it is uniformly good over the whole admissible region.

**What would change my mind.** Three things, none of which is realised here:
- **M < m.** Below M = m the proxy is singular, (H^{1/2}Σ̂H^{1/2})^{1/2} sits on the boundary of the cone, and neither the fixed point nor the expansion has a reason to hold. Everything above is conditional on M > m, which the flagship satisfies (21 > 12) but only by a factor 1.75. If anyone applies this table with weekly windows (M ≈ 5) or to m > 21 assets at monthly frequency, all of it is void — and dossier C's own C-E3.4 already flags the M < m regime as live.
- **A proxy that is not a genuine Wishart.** Everything above uses the actual Wishart law. For a general law satisfying only the second-moment condition (3.4) — which is what B-3.5 actually hypothesises — the third-order term is governed by E[Δ³], which (3.4) does not constrain at all. A law with the same second moments and a large third cumulant could have an O(ε³) term of any size. **This is the real gap in B-5.3, not the size of m/M**: the flagship numbers are safe because realised covariance is approximately Wishart, not because (3.4) is enough.
- **A remainder bound.** None of this is a proof. It is a dense numerical check over the parameter region of interest. If the campaign wants "PROVED" it needs an actual bound on ‖H\* − Σ − B‖ in terms of E‖Δ‖³ and λ_min(Σ); absent that, the honest status is "second-order approximation, exact values computed numerically, verified accurate to <8 % relative over M ∈ [13, ∞), cond(Σ) ∈ [1, 100] at m = 12".

**One incidental corroboration of the B-5.2 objection.** At cond(Σ) = 100 the second-order relative distortion of the smallest eigenvalue is **51.95 %**, which is 3.4× the dossier's claimed upper bound (m+1)/(4M) = 15.48 %. The range stated in §4.2 is not merely loose; it is violated by a factor of 3–4 in exactly the ill-conditioned regime a 12-asset covariance matrix actually occupies.

### 2.6 B-3.6 and the exact symmetry facts

```
### B-3.6 rotating counterexample, m=3, Sigma=diag(3,2,1), A = tridiag(0,1,0)
  eps=0.05  both atoms PD: [True, True]  min eig: 0.99750
  conditionally unbiased: |mean - Sigma| = 0.0
   empirical B_13=-3.334742e-04   theory=-3.333333e-04   ratio=1.00042
   eigenvector matrix of H*:
     [[-0.000167  0.  -1.      ]
      [ 0.        1.   0.      ]
      [-1.        0.   0.000167]]              <- not a signed permutation
   predicted rotation angle B13/(l1-l3) = -1.6667e-04
  eps=0.01  ratio=1.00002, off-diagonal 6.7e-06, predicted -6.667e-06

### exact symmetry facts (no expansion)
 BW  orthogonal equivariance |Q H Q' - bary(QAQ')| = 2.31e-15
 AIRM congruence  equivariance |C H C' - bary(CAC')| = 1.31e-15 (relative)
 => for Shat = Sig^{1/2}(W/M)Sig^{1/2}:
    AIRM barycentre = h*Sigma EXACTLY (all orders)
    BW barycentre EXACTLY diagonal in Sigma's eigenbasis (sign-flip invariance), all orders
```

### 2.7 Dossier C — GMV, E5, E3, E2

```
### C-7.1
  w(cH)=w(H) for c=0.1,3,100 : [5.55e-17, 6.94e-17, 2.78e-17]
  m(m+1)/2 = 78,  visible = m-1 = 11,  invisible = 67
  numerical rank of dw/dH : 11    (sv 11 = 8.48e-02, sv 12 = 1.58e-10)

### C-7.2 at m=12, M=21, spectrum 3.0->0.5
  Sigma diagonal       : ||w(H*)-w(Sigma)||_2 = 0.04038, ||w||=0.3410, relative 11.8%
  Sigma random basis   : ||w(H*)-w(Sigma)||_2 = 0.04254, ||w||=0.3401, relative 12.5%
  excess GMV variance  : 1.1715% (eigenbasis) / 1.4268% (random basis)
  AIRM (scalar)        : ||w(H*)-w(Sigma)|| = 2.78e-17   <- exactly blind

### B-E5.1 / B-E5.2
  symbolic: E[RV] = sigma^2 + alpha^2/M ; bias = alpha^2/M ; relative = alpha^2/(M sigma^2)
  MC (alpha=1.5, sigma=0.4): M=21/84/336 -> bias 1.072e-1 / 2.679e-2 / 6.724e-3
                             alpha^2/M    = 1.071e-1 / 2.679e-2 / 6.696e-3
  iid noise (sigma_u=0.001): M=21/84/336 -> E[RV] 0.1600242/0.1601565/0.1606784
                             IV+2M su^2   =       0.1600420/0.1601680/0.1606720

### C-E3.2   sigma(t) = 0.2 + 0.8t + 0.5 sin(6t)^2
  int sigma ds = 0.861179 ;  (int sigma^2 ds)^(1/2) = 0.913392 ;  gap = 0.052213 (C-S holds)
  M=  200 : E[sqrt(pi/2) M^(-1/2) sum|r|] = 0.861246 (se 2.5e-04)
  M= 2000 :                                 0.861072 (se 1.1e-04)
  M=20000 :                                 0.861222 (se 7.7e-05)     -> int sigma, not (int sigma^2)^(1/2)

### C-E2.2   latent law = 4 atoms on SPD(3), eigenvalue range 12.6:1, per-atom mean-matched Wisharts
   M    |bary(Shat) - bary(latent)| x M    B-3.5 constant at Sigma x M   at H_lat x M
  400            1.1527                            1.3209                   1.2503
 1600            1.1490                            1.3209                   1.2503
 6400            1.1491                            1.3209                   1.2503
   -> gap is Theta(1/M) with constant 1.149, NOT B-3.5's 1.321

### operator Jensen (the repair for C-E3.2)
 (E Y)^{1/2} - E[Y^{1/2}] eigenvalues : [0.01933 0.03951 0.08738]  > 0, strict
```

### 2.8 B-5.2 range and B-5.5/B-5.6 recalibration

```
### B-5.2 relative distortion (1/M)[1/4 + sum_k lam_k^2/(lam_i+lam_k)^2], M=1
  m= 3 lam_i dominant :  0.500000   (dossier lower bound 0.25)   true inf = 1/2
  m= 3 lam_i dominated:  2.499996   (dossier upper bound 1.00)   true sup = m-1/2 = 2.5
  m=12 lam_i dominant :  0.500000   (dossier lower bound 0.25)   true inf = 1/2
  m=12 lam_i dominated: 11.499978   (dossier upper bound 3.25)   true sup = m-1/2 = 11.5
  m=12 isotropic      :  3.250000   = (m+1)/4                    <- interior, not a bound

### B-5.5/B-5.6 direction of recalibration (m=1 two-point law, a=1/2)
  Phi(Sigma) = (E sqrt x)^2 = 49/64 = 0.765625 ;  kappa = 0.234375
  argmin_h of E L(y, c h) = Phi(Sigma)/c
  c = Phi     = 1-kappa       : c=0.765625  argmin_h = 1.000000   restores Sigma : True
  c = Phi^{-1}= (1-kappa)^{-1}: c=1.306122  argmin_h = 0.586182   restores Sigma : False
  AIRM flagship: dossier c = (1-13/42)^{-1} = 1.4483 -> argmin_h = 0.4768 Sigma  (should be Sigma)
                 correct  c =  1-13/42      = 0.6905 -> argmin_h = 1.0000 Sigma
  d/dx [ lam^2/(x+lam)^2 ] = -2 lam^2/(x+lam)^3 < 0 -> strictly decreasing -> B-5.6 criterion correct
```

### 2.9 B-3.8 and the Daleckiĭ–Kreĭn ingredients

```
D^2 log_Sig[X,X] : max |finite difference - DK formula| = 2.23e-07
D exp_Lam[Y]     : max |finite difference - Y_ij/l[li,lj]| = 3.38e-08

--- B-3.8 LE second-order formula vs exact exp(E log Shat) ---
  eps=0.080 |H_LE-Sig|=4.98e-03 |resid|=1.390e-04 err/eps^3=0.2715
  eps=0.040 |H_LE-Sig|=1.23e-03 |resid|=1.701e-05 err/eps^3=0.2657 ratio=8.17
  eps=0.020 |H_LE-Sig|=3.08e-04 |resid|=2.113e-06 err/eps^3=0.2642 ratio=8.05
  eps=0.010 |H_LE-Sig|=7.68e-05 |resid|=2.637e-07 err/eps^3=0.2637 ratio=8.01
--- B-3.7 AIRM second-order formula vs exact Karcher mean ---
  eps=0.080 |resid|=1.337e-04 err/eps^3=0.2612
  eps=0.010 |resid|=2.461e-07 err/eps^3=0.2461 ratio=8.05
noncommuting: max|B_LE - B_AIRM| / max|B_AIRM| = 0.1966     (O(1), as claimed)
commuting  : |B_LE - B_AIRM| = 2.22e-16
```

### 2.10 Γ homogeneity (B-5.1 / A-E4.1, used by B-5.1)

```
Gamma(0.25 H)/Gamma(H) = 0.500000000000   sqrt(c) = 0.500000000000
Gamma(   4 H)/Gamma(H) = 2.000000000000   sqrt(c) = 2.000000000000
Gamma(   9 H)/Gamma(H) = 3.000000000000   sqrt(c) = 3.000000000000
```

## 3. Global observations (item 15)

1. **Claims stated more strongly than proved.** (a) C-7.2's "entirely invisible" from a second-order-only premise. (b) B-3.5's "rotation returns at O(M⁻²)" — an upper bound presented as an exact order, and false for the flagship proxy. (c) C-E3.2's "no infill-consistent estimator" — a universal impossibility drawn from an inequality that only kills one family. (d) B-5.5's "no recalibration of a non-Bregman loss" — proved for BW via strict convexity in y, asserted for the whole non-Bregman class (it does generalise, but the given proof is BW-specific).
2. **Numerical results presented as proof.** B-5.3's status is "PROVED (arithmetic from B-3.5/B-3.7)" for a truncated expansion at m/M = 0.571 with no remainder bound. B §7's blanket "No status in this dossier rests on numerics alone" is false (three counts, listed above). C-7.2's ‖Δw‖ ≈ 0.02 is a numeric with no stated configuration.
3. **"Consistent" versus "conditionally unbiased" conflated.** Exactly once, and in the worst possible place: C-E2.2's claim-table row says "not consistent" while its own §1.2 says "consistent under infill". Everywhere else (B-E5.3, the §1.2 parenthetical's own cross-reference) the distinction is handled well — which makes the one slip a drafting error, not a conceptual one, but it is in the transitive-closure register and would propagate.
4. **Restriction without a boundary reason.** B-2.4's a ∈ (0,1]: the stated boundary evidence (a = 1.5 fails) tests the parameterisation, not the phenomenon, which extends to (0,2). And the a = 1 endpoint sits outside B-2.2's own "law charges the open cone" hypothesis.
5. **Claims about other authors.** None that exceed what is quoted. C-7.4/C-7.5 are exemplary: the training loss and the GMV evaluation are verbatim-verified, the LRV scoping is verbatim-verified, the preprint status is flagged, and the bias-non-detection claim is explicitly reassigned to this campaign rather than to the authors. No objection.
6. **Missing hypotheses.** Non-degeneracy of Σ's spectrum (B-3.3's rotation criterion, silently assumed and materially wrong without it); regularity/interchange conditions for the B-3.2 expansion; whether ρ is non-degenerate in B-5.5.
7. **Unforced conservatism worth reclaiming.** Two exact results are available for free and are stronger than what the dossiers state: for a genuine Wishart proxy the BW barycentre is exactly diagonal in Σ's eigenbasis (sign-flip equivariance) and the AIRM barycentre is exactly hΣ (congruence equivariance). Both are one-line arguments with no expansion. They should replace the O(M⁻²) hedging in B-3.5 and the "to second order" hedging in C-7.2.

## 4. What a repair pass must change

Ordered by how much depends on it.

1. Fix B-5.2's stated range to (1/(2M), (m−½)/M) and note that (m+1)/(4M) is the isotropic value, not a bound.
2. Fix the recalibration direction in B-5.5 (ρ = Φ, not Φ⁻¹) and B-5.6 (c = 1 − (m+1)/(2M)), or else redefine recalibration as acting on the model's output and say so once, in both places.
3. Replace C-E3.2's proof with the operator-Jensen argument already used in C-E3.4, and restate the theorem as "the absolute-variation family is conditionally unbiased for ∫σ ds, not for (∫σ²ds)^{1/2}; and no proxy is conditionally unbiased for Σ^{1/2} without a law-specific debiasing, by strict operator concavity of the square root".
4. Repair C-E2.2: delete "with the explicit constant above" (the order is right, the constant is not B-3.5's), and reconcile the table row's "not consistent" with §1.2's "consistent under infill".
5. Downgrade B-5.3's status from PROVED to "second-order approximation; exact values computed numerically", insert the exact figures 8.8 %–35.9 % (BW) and 32.9 % (AIRM), and state the validity envelope established in §2.5a (M > m, <8 % relative for M ≥ 13 at m = 12, insensitive to cond(Σ) ≤ 100) together with the caveat that the envelope is established for a *genuine Wishart* law and not for the weaker hypothesis (3.4) that B-3.5 nominally assumes.
6. Replace B-3.5's O(M⁻²) rotation remark and C-7.2's "to second order" with the two exact equivariance arguments.
7. Add the non-degeneracy hypothesis to B-3.3; state the a ∈ (0,2) extension and the a = 1 singularity in B-2.4; delete or itemise B §7's blanket numerics sentence; specify the m = 3, M = 500 spectrum in B-5.3.

None of these changes any route verdict. LO-2, LO-3, LO-5, E2, E3, E5 and the LO-7 adjudication all stand as recorded.
