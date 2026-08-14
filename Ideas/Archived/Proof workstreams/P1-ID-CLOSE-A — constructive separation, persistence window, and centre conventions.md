---
type: working-proof-dossier
title: P1-ID-CLOSE-A — constructive separation, persistence window, and centre conventions
status: wave-1-author-complete
last-audited: 2026-08-12
authority: Workstream A producer record only; the P1-ID-CLOSE lead ledger remains campaign authority
owns: ID-7, ID-10, ID-9 route R4
---

# P1-ID-CLOSE-A — constructive separation, persistence window, and centre conventions

> **Scope.** Workstream A of the P1-ID-CLOSE campaign. This file is a producer record. It does not edit or supersede any canonical file. Where a result here would require a canonical edit, that edit is listed in §9 as a *recommendation to the lead*, never as an accomplished change.
>
> **Status codes** (locked by the lead ledger §3): `PROVED`, `CITED+APPLIED`, `DISPROVED`, `REFORMULATED+PROVED`, `SUPERSEDED`, `SEPARATED`. Every node introduced below carries one.
>
> **Numerics discipline.** Section 10 records every numerical check. No numerical evaluation assigns a status anywhere in this dossier. Numerics are used to *discover* the exact scaling profile \(\Psi\) of §1.3 and to *evaluate* the finite-sample diagnostic of §7; both are then proved or explicitly labelled as diagnostics.

---

## 0. Node register (all terminal)

| Node | One-line statement | Status | §|
|---|---|---|---|
| L-7.1.0 | exact spectral/Cesàro identity for the ergodic-average modulus | PROVED | 1.1 |
| L-7.1a | exact Hilbert AR(1) modulus, both regimes | PROVED | 1.2 |
| L-7.1a′ | exact scaling profile \(\psi^2\to\Psi(x)=2(x-1+e^{-x})/x^2\), \(x=N(1-\rho)\) | PROVED (new) | 1.3 |
| L-7.1b | \(m_0\)-dependent: \(\psi(N)\le\sqrt{(2m_0+1)\operatorname{tr}\Gamma(0)/N}\); \(\asymp N^{-1/2}\) **iff** \(\sum_h\operatorname{tr}\Gamma(h)>0\) | REFORMULATED+PROVED | 1.4 |
| L-7.1c | summable Hilbert physical dependence: same, with \(\Delta_2\) in place of \(2m_0+1\) | REFORMULATED+PROVED | 1.5 |
| L-7.1d | long memory \(d\in(0,1/2)\): \(\psi(N)\sim\sqrt{c_\gamma/(d(2d+1))}\,N^{-(1/2-d)}\) | PROVED | 1.6 |
| L-7.1e | \(\psi\le\psi^+\); equality on classes (a)–(d); \(\psi^+\) is the estimator-relevant modulus | PROVED | 1.7 |
| L-7.3.1 | kernel-window reduction: \(\|\sum_tw_t\xi_t\|_{L^2}\le C_2\psi^+(N)\), two-sided under regular variation | PROVED | 2.2 |
| L-7.3.2 | \(\psi^+(nb_n)\) enters G1-HD-L2 **exactly** where \((nb_n)^{-1/2}\) sits, and nowhere else in the mean channel | PROVED | 2.3 |
| L-7.3.3 | GRID, PF, OBS, P1-ROW, P1-OP, EV, Davis–Kahan propagate verbatim in \(\ell_n(\psi)\) | PROVED | 2.4 |
| L-7.3.4 | oracle lag row degrades to \(n^{-1/2}+n^{-(1-2d)}\); Isserlis proof; dominated at the re-optimised bandwidth | PROVED (honest degradation) | 2.5 |
| L-7.3.5 | the residue-class device is unavailable under long memory; G1-HD/HD-Minf die; HD-E does not consume them | DISPROVED (device) + SEPARATED (consumer) | 2.6 |
| L-7.2 | **Theorem ID-7** — constructive separation with attainment | PROVED | 3 |
| L-7.4 | sharpness: exact boundary \(x_n=(1-\rho_n)nb_n\to\infty\), both directions | PROVED | 4 |
| L-10.1 | \(\alpha(d)=(1-2d)/(7-2d)\), rate \(n^{-3(1-2d)/(7-2d)}\); HD-K slack | PROVED (lead algebra confirmed) | 5.1 |
| L-10.2a | constant persistence: \(\theta<1-\alpha\); at \(b_n=n^{-1/7}\), \(\theta<6/7\) | PROVED (lead confirmed) | 5.2 |
| L-10.2b | tvAR(1) triangular array: **\(a=1-\theta\) exactly and sharply** | PROVED | 5.3 |
| L-10.2c | \(a\ge3/7\Rightarrow\theta\le4/7\) is correct but is **not** the binding constraint | REFORMULATED+PROVED | 5.4 |
| L-10.3 | window nonempty; binding constraint per regime; \(\theta=2\) excluded by a full unit of exponent | PROVED | 6 |
| L-10.4 | APP-FIN diagnostic (labelled diagnostic, not proof) | PROVED (as a computation) + DIAGNOSTIC | 7 |
| L-9.R4.1 | equivariance rigidity on the stabiliser-rigid class; exact flat and curved separations off it | PROVED | 8.1 |
| L-9.R4.2 | regularised centre is not a marginal functional but is an \(\mathcal I_M\)-functional; **Theorem R4-GATE** | PROVED | 8.2 |
| L-9.R4.3 | exactly three chart classes; (b),(c),(d) generically in the new \(\mathcal L^{\rm tv}\); (e) in \(\mathcal L^{\rm rand}\) | PROVED + SEPARATED to C | 8.3 |
| L-9.R4.4 | (d) changes the estimand; Paper 1 as declared is **incompatible** with (d) | PROVED | 8.4 |
| R4-EXH | the escape space is exhausted by (E1)+(E2); R4 is proved *not* an escape | PROVED | 8.2 |

---

## 1. L-7.1 — the ergodic-average modulus

### 1.1 Definition and the exact identity

Let \(H\) be a real separable Hilbert space. For each rescaled time \(u\in[0,1]\) let \(\{Z^{(u)}_t\}_{t\in\mathbb Z}\) be centred, square-integrable and weakly stationary in \(H\), with autocovariance operators \(\Gamma_u(h)=\mathbb E[Z^{(u)}_{t+h}\otimes Z^{(u)}_t]\), operator-valued spectral measure \(F_u\), and finite scalar measure \(\nu_u(B)=\operatorname{tr}F_u(B)\). Put

\[
\psi_u(N)=\Big\|\tfrac1N\sum_{t=1}^NZ^{(u)}_t\Big\|_{L^2(\Omega;H)},
\qquad
\psi(N)=\sup_{u\in[0,1]}\psi_u(N).
\]

> **Lemma L-7.1.0 (exact identity).**
> \[
> \psi_u(N)^2
> =\frac1{N^2}\sum_{s,t=1}^N\operatorname{tr}\Gamma_u(s-t)
> =\frac1N\sum_{|h|<N}\Big(1-\frac{|h|}N\Big)\operatorname{tr}\Gamma_u(h)
> =\int_{-\pi}^{\pi}|D_N(\lambda)|^2\nu_u(d\lambda),
> \]
> with \(D_N(\lambda)=N^{-1}\sum_{t=1}^Ne^{it\lambda}\).

**Proof.** Expand \(\mathbb E\|N^{-1}\sum_tZ_t\|^2=N^{-2}\sum_{s,t}\mathbb E\langle Z_s,Z_t\rangle\) and use \(\mathbb E\langle Z_{t+h},Z_t\rangle=\operatorname{tr}\Gamma(h)\) (finite because \(\Gamma(0)\) is trace class for a square-integrable \(H\)-valued variable). Collecting diagonals gives the Cesàro form. The spectral form is the displayed identity of P1-ID-A §6, which is **PROVED INTERNALLY** there. \(\square\)

**Status: PROVED** (it is P1-ID-A §6 restated; no new external input).

This identity is the whole of L-7.1: every evaluation below is a computation of \(\sum_{|h|<N}(1-|h|/N)\operatorname{tr}\Gamma(h)\).

**Consistency with ID-3.** By L-7.1.0 and dominated convergence, \(\psi_u(N)\to\nu_u(\{0\})^{1/2}\); hence \(\psi_u(N)\to0\iff F_u(\{0\})=0\), which is exactly ID-3's pointwise statement. \(\psi\) is the *quantitative refinement* of ID-3: it replaces the qualitative predicate "no atom at zero" by a sample-size-indexed number, and taking \(\sup_u\) makes it uniform by construction. This is precisely the "quantitative upper bound on low-frequency concentration" that P1-ID-A §8 flagged as the missing object.

### 1.2 L-7.1a — Hilbert AR(1), exact formula

Let \(e_t\) be iid centred in \(H\) with \(\mathbb E\|e_0\|^2=1\), and let
\(Z_t=\rho Z_{t-1}+\sigma e_t\) with \(0<\rho<1\), \(\sigma^2=1-\rho^2\). Then
\(\operatorname{tr}\Gamma(0)=1\) (unit marginal energy) and \(\operatorname{tr}\Gamma(h)=\rho^{|h|}\). The scalar Gaussian AR(1) of ID-3 §8 is the case \(\dim H=1\).

> **Lemma L-7.1a.** For every \(N\ge1\) and \(\rho\in(0,1)\),
> \[
> \boxed{\;\psi(N)^2=\frac1{N^2}\left[N\frac{1+\rho}{1-\rho}-\frac{2\rho(1-\rho^N)}{(1-\rho)^2}\right]\;}
> \tag{1.1}
> \]
> equivalently \(\psi(N)^2=N^{-2}\dfrac{N(1-\rho^2)-2\rho+2\rho^{N+1}}{(1-\rho)^2}\).

**Proof.** By L-7.1.0, \(N^2\psi(N)^2=\sum_{s,t=1}^N\rho^{|s-t|}=N+2\sum_{h=1}^{N-1}(N-h)\rho^h\). Using
\(\sum_{h=1}^{N-1}\rho^h=\rho(1-\rho^{N-1})/(1-\rho)\) and
\(\sum_{h=1}^{N-1}h\rho^h=\rho\{1-N\rho^{N-1}+(N-1)\rho^N\}/(1-\rho)^2\),

\[
N+2N\frac{\rho(1-\rho^{N-1})}{1-\rho}
-2\frac{\rho\{1-N\rho^{N-1}+(N-1)\rho^N\}}{(1-\rho)^2}
=\frac{N(1-\rho^2)-2\rho+2\rho^{N+1}}{(1-\rho)^2},
\]

after clearing \((1-\rho)^2\) and cancelling the two \(N\rho^N\) terms. Rewriting \(N(1-\rho^2)/(1-\rho)^2=N(1+\rho)/(1-\rho)\) and \(-2\rho+2\rho^{N+1}=-2\rho(1-\rho^N)\) gives (1.1). \(\square\)

The identity \(N^2\psi^2=\{N(1-\rho^2)-2\rho+2\rho^{N+1}\}/(1-\rho)^2\) was verified symbolically (§10, check C1); the lead's displayed candidate is **exactly** correct.

**Regime \(N(1-\rho)\gg1\).** Write \(x=N(1-\rho)\). Then
\(\psi(N)^2=\frac{1+\rho}{x}-\frac{2\rho(1-\rho^N)}{x^2}\), and the second term is at most \(2/x^2\), a fraction \(2/\{x(1+\rho)\}\le2/x\) of the first. Hence
\[
\psi(N)^2=\frac1N\cdot\frac{1+\rho}{1-\rho}\{1+O(x^{-1})\},
\]
which is the lead's \(\psi(N)^2\approx N^{-1}\frac{1+\rho}{1-\rho}\). **PROVED.**

**Regime \(N(1-\rho)\lesssim1\).** Sharpened to an exact limit in §1.3.

**Status: PROVED.**

### 1.3 L-7.1a′ — the exact scaling profile (new)

> **Lemma L-7.1a′.** Let \(N\to\infty\), \(\rho=\rho_N\uparrow1\) with \(x_N:=N(1-\rho_N)\to x\in[0,\infty)\). Then
> \[
> \psi(N)^2\longrightarrow\Psi(x):=\frac{2\{x-1+e^{-x}\}}{x^2},
> \qquad \Psi(0):=1 .
> \tag{1.2}
> \]
> \(\Psi\) is continuous and strictly decreasing on \([0,\infty)\), with \(\Psi(0)=1\), \(\Psi(x)=1-x/3+O(x^2)\) as \(x\downarrow0\), and \(\Psi(x)=2/x-2/x^2+o(x^{-2})\) as \(x\to\infty\). Moreover \(\psi(N)^2\le\min\{1,\,2/x_N\}\) for every \(N,\rho\).

**Proof.** From (1.1), \(\psi(N)^2=(1+\rho)/x_N-2\rho(1-\rho^N)/x_N^2\). Since
\(\rho^N=(1-x_N/N)^N\to e^{-x}\) and \(\rho\to1\), the limit is \(2/x-2(1-e^{-x})/x^2=2\{x-1+e^{-x}\}/x^2\). The value at \(x=0\) follows from \(x-1+e^{-x}=x^2/2-x^3/6+O(x^4)\), giving \(\Psi(x)=1-x/3+O(x^2)\); this also shows the limit at \(x\downarrow0\) is \(1\), consistent with the elementary bound \(\psi(N)\le\|Z_0\|_{L^2}=1\) (Jensen). Strict monotonicity: \(x^2\Psi(x)/2=x-1+e^{-x}\), so
\(\frac{d}{dx}\Psi=\frac{2}{x^3}\{x^2(1-e^{-x})/1-2(x-1+e^{-x})\}\cdot\) — more simply, \(\Psi(x)=2\int_0^1(1-y)e^{-xy}\,dy\cdot\) is verified by
\(\int_0^1 2(1-y)e^{-xy}dy=2[(1-e^{-x})/x^2-e^{-x}/x]\cdot\)… we use instead the direct representation

\[
\Psi(x)=2\int_0^1(1-y)e^{-xy}\,dy ,
\]

which is checked by evaluating the elementary integral: \(\int_0^1e^{-xy}dy=(1-e^{-x})/x\) and \(\int_0^1ye^{-xy}dy=\{1-(1+x)e^{-x}\}/x^2\), so
\(2\{(1-e^{-x})/x-[1-(1+x)e^{-x}]/x^2\}=2\{x-x e^{-x}-1+(1+x)e^{-x}\}/x^2=2\{x-1+e^{-x}\}/x^2\) ✓.
Since the integrand is strictly decreasing in \(x\) for a.e. \(y\in(0,1)\), \(\Psi\) is strictly decreasing; and \(\Psi(0)=2\int_0^1(1-y)dy=1\) ✓. Finally \(\psi(N)^2\le1\) by Jensen and \(\psi(N)^2\le(1+\rho)/x_N\le2/x_N\) by dropping the negative term in (1.1). \(\square\)

The representation \(\Psi(x)=2\int_0^1(1-y)e^{-xy}dy\) is the continuum limit of the Cesàro form of L-7.1.0 with \(\operatorname{tr}\Gamma(h)=e^{-(1-\rho)|h|}\) — i.e. the Ornstein–Uhlenbeck kernel. Numerical confirmation at \(x=0.1,1,10\) in §10 (check C2), agreement to \(10^{-6}\).

**Why this matters.** \(\Psi\) is the *exact interpolating profile* between "no averaging" (\(\Psi(0)=1\): the local average is as noisy as a single observation) and "full averaging" (\(\Psi(x)\approx2/x\)). It converts the qualitative statement "\(N(1-\rho)\lesssim1\Rightarrow\psi\asymp1\)" into an exact continuous boundary, which is what §4 needs to close the gap between the positive theorem and ID-3's impossibility without slack.

**Status: PROVED.**

### 1.4 L-7.1b — \(m_0\)-dependent (HD-M baseline): a required correction

> **Lemma L-7.1b.** If \(\operatorname{tr}\Gamma_u(h)=0\) for \(|h|>m_0\), uniformly in \(u\), and \(\sup_u\operatorname{tr}\Gamma_u(0)\le R^2\), then for all \(N>m_0\)
> \[
> \psi(N)\le\sqrt{\frac{(2m_0+1)R^2}{N}} .
> \tag{1.3}
> \]
> Moreover \(N\psi_u(N)^2\to\Lambda_u:=\sum_{|h|\le m_0}\operatorname{tr}\Gamma_u(h)=2\pi\operatorname{tr}f_u(0)\ge0\), so
> \[
> \psi_u(N)\asymp N^{-1/2}\iff\Lambda_u>0 .
> \]
> If \(\Lambda_u=0\) the true order is strictly faster: \(\psi_u(N)=O(N^{-1})\).

**Proof.** (1.3): by L-7.1.0, \(N\psi_u(N)^2\le\sum_{|h|\le m_0}|\operatorname{tr}\Gamma_u(h)|\le(2m_0+1)\operatorname{tr}\Gamma_u(0)\), using \(|\operatorname{tr}\Gamma(h)|=|\mathbb E\langle Z_{t+h},Z_t\rangle|\le\mathbb E\|Z_0\|^2=\operatorname{tr}\Gamma(0)\) by Cauchy–Schwarz and stationarity. The limit is immediate since for \(N>m_0\), \(N\psi_u^2=\sum_{|h|\le m_0}(1-|h|/N)\operatorname{tr}\Gamma_u(h)\to\Lambda_u\). If \(\Lambda_u=0\) then \(N\psi_u^2=-N^{-1}\sum_{|h|\le m_0}|h|\operatorname{tr}\Gamma_u(h)=O(N^{-1})\). \(\square\)

**The correction.** The lead's L-7.1(b) asserts \(\psi(N)\asymp N^{-1/2}\) unconditionally for \(m_0\)-dependent processes. That is **false**. Counterexample: \(Z_t=e_t-e_{t-1}\) with \(e\) iid unit-energy, \(m_0=1\). Then \(\operatorname{tr}\Gamma(0)=2\), \(\operatorname{tr}\Gamma(\pm1)=-1\), \(\Lambda=0\), and
\(N^2\psi(N)^2=\mathbb E\|e_N-e_0\|^2=2\), so \(\psi(N)=\sqrt2/N\). The over-differenced case genuinely averages faster than \(N^{-1/2}\).

This is not a threat to HD1: HD1 needs only the **upper** bound (1.3), which is unconditional. It is a threat to any claim that \(\psi\) is *sharp* at \(N^{-1/2}\) without \(\Lambda_u>0\). The boundary reason is exact: the \(N^{-1/2}\) order is governed by the zero-frequency *density*, not by the memory length.

**Status: REFORMULATED+PROVED.**

### 1.5 L-7.1c — summable Hilbert physical dependence (HD-L / T-APP-4)

Let \(Z_t=G(\eta_t,\eta_{t-1},\dots)\) be a causal Hilbert Bernoulli shift with \(L^2\) innovation effects \(\delta_2(k)=\|Z_k-Z_k^{*}\|_{L^2}\) (\(Z_k^*\) the coupled version) and \(\Delta_2=\sum_{k\ge0}\delta_2(k)<\infty\), uniformly in \(u\).

> **Lemma L-7.1c.** \(\psi(N)\le\Delta_2N^{-1/2}\). Furthermore \(\sum_h|\operatorname{tr}\Gamma(h)|<\infty\) and \(N\psi_u(N)^2\to\Lambda_u=\sum_h\operatorname{tr}\Gamma_u(h)\); hence \(\psi_u(N)\asymp N^{-1/2}\iff\Lambda_u>0\).

**Proof.** T-APP-4 display (3.3) of the Application map — proved internally in APP-C §3 — gives
\(\|\sum_ta_t(Z_t-\mathbb EZ_t)\|_{L^2}\le\Delta_2\|a\|_2\) for deterministic \(a\). Take \(a_t=1/N\) on the window, \(\|a\|_2=N^{-1/2}\). Absolute summability of \(\operatorname{tr}\Gamma(h)\) follows from the standard physical-dependence covariance bound \(|\operatorname{tr}\Gamma(h)|\le\|Z_0\|_{L^2}\sum_{k\ge h}\delta_2(k)\), whose sum over \(h\) is \(\sum_k(k+1)\delta_2(k)\) — finite when \(\sum_k k\delta_2(k)<\infty\); under bare \(\Delta_2<\infty\) one gets \(\sum_h|\operatorname{tr}\Gamma(h)|\le\|Z_0\|_{L^2}\Delta_2\cdot\) by Fubini on the tail sums only if \(\sum_k k\delta_2(k)<\infty\). We therefore state the *limit* clause under the (standard, strictly stronger) condition \(\sum_kk\delta_2(k)<\infty\), and the *upper bound* under bare \(\Delta_2<\infty\). Dominated convergence in the Cesàro form gives the limit. \(\square\)

**Same correction as L-7.1b:** \(\asymp N^{-1/2}\) requires \(\Lambda_u>0\); the upper bound is unconditional and is all HD1 consumes.

**Status: REFORMULATED+PROVED** (upper bound CITED+APPLIED from T-APP-4, itself internally proved; the two-sided clause PROVED here).

### 1.6 L-7.1d — long memory

> **Lemma L-7.1d.** Suppose \(\operatorname{tr}\Gamma_u(h)=c_\gamma(u)|h|^{2d-1}\{1+o(1)\}\) as \(|h|\to\infty\), with \(d\in(0,1/2)\) and \(0<\underline c\le c_\gamma(u)\le\bar c<\infty\) uniformly in \(u\). Then
> \[
> \psi_u(N)^2=\frac{c_\gamma(u)}{d(2d+1)}\,N^{-(1-2d)}\{1+o(1)\},
> \qquad
> \psi(N)\asymp N^{-(1/2-d)} .
> \tag{1.4}
> \]

**Proof.** By L-7.1.0,
\(N\psi_u(N)^2=\operatorname{tr}\Gamma_u(0)+2\sum_{h=1}^{N-1}(1-h/N)\operatorname{tr}\Gamma_u(h)\).
The function \(h\mapsto h^{2d-1}\) is regularly varying of index \(2d-1\in(-1,0)\), so by the Riemann-sum/Karamata argument
\[
\sum_{h=1}^{N-1}\Big(1-\frac hN\Big)h^{2d-1}
=N^{2d}\int_0^1(1-y)y^{2d-1}dy\,\{1+o(1)\}
=N^{2d}\Big\{\frac1{2d}-\frac1{2d+1}\Big\}\{1+o(1)\},
\]
and \(\frac1{2d}-\frac1{2d+1}=\frac1{2d(2d+1)}\). Hence
\(N\psi_u^2=2c_\gamma N^{2d}/\{2d(2d+1)\}\{1+o(1)\}=c_\gamma N^{2d}/\{d(2d+1)\}\{1+o(1)\}\), giving (1.4). The \(o(1)\) in the hypothesis is absorbed because the weight \((1-h/N)\in[0,1]\) is bounded and the sum is dominated by \(h\asymp N\); uniformity in \(u\) follows from the uniform bounds on \(c_\gamma\). Since \(\operatorname{tr}\Gamma_u(0)\) is bounded and \(N^{2d}\to\infty\), the lag-zero term is negligible. \(\square\)

**Exact constant check.** For ARFIMA\((0,d,0)\) normalised to \(\operatorname{tr}\Gamma(0)=1\), the autocorrelation tail constant is \(c_\gamma=\Gamma(1-d)/\Gamma(d)\), giving
\(\psi(N)\sim\{\Gamma(1-d)/(\Gamma(d)\,d(2d+1))\}^{1/2}N^{-(1/2-d)}\). At \(d=0.4\) this is \(0.9657\); the numerically computed constant at \(N=8000\) is \(0.966\) (§10, check C3). Empirical exponents match \(1/2-d\) to four decimals for \(d\in\{0.1,0.25,0.4,0.45\}\).

**Status: PROVED.**

### 1.7 L-7.1e — the absolute modulus \(\psi^+\)

Estimator bounds require a modulus that dominates *weighted* averages with non-uniform weights. Define

\[
\psi^+_u(N)=\Big\{\frac1{N^2}\sum_{s,t=1}^N|\operatorname{tr}\Gamma_u(s-t)|\Big\}^{1/2},
\qquad \psi^+(N)=\sup_u\psi^+_u(N).
\]

> **Lemma L-7.1e.** \(\psi\le\psi^+\), with equality whenever \(\operatorname{tr}\Gamma_u(h)\ge0\) for all \(h\). In particular \(\psi=\psi^+\) for the AR(1) class of §1.2 (\(\rho>0\)), for the long-memory class of §1.6 (\(c_\gamma>0\)), and for any \(m_0\)-dependent or physically-dependent process with nonnegative autocovariance trace. For a general \(m_0\)-dependent process, \(\psi^+(N)\le\sqrt{(2m_0+1)R^2/N}\); for a general physically dependent process with \(\sum_kk\delta_2(k)<\infty\), \(\psi^+(N)=O(N^{-1/2})\).

**Proof.** Immediate from L-7.1.0 and the triangle inequality; the last two claims repeat the proofs of L-7.1b/c with \(|\operatorname{tr}\Gamma|\) in place of \(\operatorname{tr}\Gamma\), which changes nothing in the upper bounds. \(\square\)

**All statements below use \(\psi^+\).** Since \(\psi=\psi^+\) on every class this dossier evaluates, no numerical statement changes; the distinction is required only so that §2 is honest for a general process with sign-changing autocovariance trace.

**Status: PROVED.**

---

## 2. L-7.3 — attainment by the three-scale estimator

This is the load-bearing section. The claim to prove is not that "a smoother of some kind" attains \(\psi\), but that HD1's *own* estimator does, with \(\psi^+(nb_n)\) sitting **exactly** where \((nb_n)^{-1/2}\) sits and nowhere else in the mean channel.

### 2.1 Where the stochastic term actually lives

Recall the exact structure of HD1's mean proof (HD1 §2; G1 audit §§2, 5; HD1-A §§3–4).

1. **Empirical Sturm** (G1 audit Theorem A′): for positive weights \(w_t(u)\ge0\), \(\sum_tw_t(u)=1\),
\[
d(\hat\mu(u),\mu_b(u))\le\big\|\widehat G_u(\mu_b(u))-G_u(\mu_b(u))\big\|
=\Big\|\sum_tw_t(u)\,\xi_t(u)\Big\|,
\tag{2.1}
\]
\[
\xi_t(u):=\operatorname{Log}_{\mu_b(u)}X_{t,n}-\mathbb E\operatorname{Log}_{\mu_b(u)}X_{t,n}.
\]
Here \(\mu_b(u)\) is the *deterministic* smoothed population barycentre, so \(\xi_t(u)\) is a centred array in a fixed tangent space, parallel-trivialised as in HD1-A Lemma 4.2.

2. **Deterministic bias**: \(d(\mu_b(u),\mu(u))\) is controlled by Theorem X and the scale identities \(\sum_j\lambda_jc_j=\sum_j\lambda_jc_j^2=0\), producing \(O(b_n^3)+O(n^{-a})\). This channel is a functional of the *marginal proxy laws* \(Q_u\) and their \(u\)-smoothness only.

3. **Design/discretisation**: \(O(n^{-1})\) from the total-variation Riemann-sum bound (HD1-A §3).

4. **Local stationarity**: \(O(n^{-a})\) from (HD-M2), via mean square and Markov.

**Therefore the entire dependence structure of the process enters the level rate through the single object \(\|\sum_tw_t(u)\xi_t(u)\|_{L^2}\).** This is the exact sense in which the claim "the persistent factor enters exactly where \((nb_n)^{-1/2}\) sits" is to be proved: it enters through (2.1) and through no other channel of the mean rate.

HD1 bounds (2.1) by HD1-A Lemma 4.1 display **(4.1)**:
\(\mathbb E\|\sum_ta_t\xi_t\|^2\le(2m+1)B^2\sum_ta_t^2\).
With \(a_t=w_t(u)\), \(\|w\|_2^2\asymp(nb_n)^{-1}\), this yields \((nb_n)^{-1/2}\).

**Observation (load-bearing).** Display (4.1) is a *covariance identity plus a triangle inequality* — it uses \(m\)-dependence only to truncate the double sum. The residue-class/Hoeffding device appears solely in display **(4.2)**, the exponential tail. This is verified verbatim in HD1-A §4: "*Expand the squared norm. Only pairs \(|s-t|\le m\) remain; use \(2|a_sa_t|\le a_s^2+a_t^2\), proving (4.1). For (4.2), split indices into \(m+1\) residue classes; each class is independent.*"

Consequently the \(L^2\) branch of the mean theorem — the branch \(\ell_n\) that HD-E actually consumes — never touches the residue-class device. §2.6 makes this precise and terminal.

### 2.2 L-7.3.1 — kernel-window reduction

> **Lemma L-7.3.1.** Let \(w_t\ge0\), \(\sum_tw_t=1\), supported on a set \(W\) of consecutive indices with \(|W|=N\), and \(\max_tw_t\le C_2/N\). Let \(\{\xi_t\}\) be centred, weakly stationary in \(H\). Then
> \[
> \Big\|\sum_tw_t\xi_t\Big\|_{L^2}\le C_2\,\psi^+(N).
> \tag{2.2}
> \]
> Conversely, suppose \(\operatorname{tr}\Gamma_\xi(h)\ge0\) for all \(h\), \(w_t\ge c_3/N\) on a sub-window \(W'\subseteq W\) with \(|W'|\ge c_4N\), and \(\psi\) is regularly varying (true for §§1.2–1.6). Then
> \[
> \Big\|\sum_tw_t\xi_t\Big\|_{L^2}\ge c_3c_4\,\psi(c_4N)\ \ge\ c\,\psi(N)
> \tag{2.3}
> \]
> for a constant \(c>0\) depending only on \(c_3,c_4\) and the index of regular variation.

**Proof.** Upper: \(\mathbb E\|\sum_tw_t\xi_t\|^2=\sum_{s,t}w_sw_t\operatorname{tr}\Gamma_\xi(s-t)\le\sum_{s,t\in W}\frac{C_2^2}{N^2}|\operatorname{tr}\Gamma_\xi(s-t)|=C_2^2\psi^+(N)^2\).
Lower: with \(\operatorname{tr}\Gamma\ge0\) every summand is nonnegative, so restricting the double sum to \(W'\times W'\) and using \(w_t\ge c_3/N\) gives
\(\sum_{s,t}w_sw_t\operatorname{tr}\Gamma\ge\frac{c_3^2}{N^2}\sum_{s,t\in W'}\operatorname{tr}\Gamma(s-t)=c_3^2\frac{|W'|^2}{N^2}\psi(|W'|)^2\ge c_3^2c_4^2\psi(c_4N)^2\), using monotonicity of \(N\mapsto N^2\psi(N)^2\) (which holds because the summand is nonnegative). Regular variation of \(\psi\) with index \(-(1/2-d)\), \(d\in[0,1/2)\), gives \(\psi(c_4N)\ge c_4^{1/2-d}\psi(N)\{1+o(1)\}\). \(\square\)

**Application to HD1's kernels.** HD1's stage-\(j\) weights are
\(w_{j,t}(u)=K(\{u_t-u\}/(c_jb_n))/\sum_sK(\{u_s-u\}/(c_jb_n))\) with \(K\ge0\) compactly supported and \(\int K>0\). HD1-A §3 proves the denominators are Riemann sums bounded above and below by multiples of \(nb_n\int K\), uniformly. Hence \(\max_tw_{j,t}\le C_2/(c_jnb_n)\) with \(C_2=\|K\|_\infty/\int K\) up to the Riemann error, and the support has \(|W_j|\le C_1c_jnb_n\). Applying (2.2) at each stage and combining by the Richardson map with \(\|\lambda\|_1=5\):

\[
\Big\|\text{stochastic part of }\log_{\mu_b}\hat\mu^{(3)}\Big\|_{L^2}
\le 5\,C_2\,\psi^+(nb_n/4)\,.
\tag{2.4}
\]

The worst stage is \(c_3=1/4\), i.e. the narrowest window. Under regular variation \(\psi^+(nb_n/4)\asymp\psi^+(nb_n)\) with constant \(4^{1/2-d}\le2\). This constant inflation is **already present in HD1** (G1 audit §5: "the tangent combination inflates constants by \(\|\lambda\|_1=5\)"); the only new content is that the *narrowest* window, not the widest, sets the modulus. Recorded so that the lead can display \(\psi^+(nb_n/4)\) if a constant-explicit statement is wanted.

**Status: PROVED.**

### 2.3 L-7.3.2 — the replaced mean theorem

> **Proposition L-7.3.2.** Replace HD-M's finite-memory clause by
>
> **(HD-M-\(\psi\))** *the frozen tangent score family \(\{\xi^{(u)}_t\}\) is centred, square-integrable and weakly stationary in \(H\), uniformly in \(u\), with \(\sup_u\operatorname{tr}\Gamma_u(0)\le R^2\) and absolute modulus \(\psi^+\).*
>
> Keep HD-G, HD-X, HD-M2, HD-K and the smoothness inputs of Theorem X unchanged. Then, provided \(\psi^+(nb_n)=o(1)\),
> \[
> \big\|\log_{\mu_n}\hat\mu_n^{(3)}\big\|_{L^2}=O_p(\ell_n(\psi)),
> \qquad
> \boxed{\ \ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1}.\ }
> \tag{G1-HD-L2-\(\psi\)}
> \]

**Proof.** Terms 1, 3, 4 of \(\ell_n(\psi)\) are unchanged: the bias expansion (Theorem X and the scale identities) is a statement about the *marginal proxy laws* and the design moments, both untouched by (HD-M-\(\psi\)); the \(n^{-a}\) coupling term is bounded in mean square and then by Markov (HD1 §2: "*For G1-HD-L2 and GRID, the coupling contribution is bounded in mean square and then by Markov; no essential-sup coupling is consumed*"); the \(n^{-1}\) term is the deterministic Riemann/TV error of HD1-A §3. Term 2 is (2.1) bounded by (2.4). Empirical Sturm (2.1) requires only positivity of the weights and Sturm's barycentre inequality on the Hadamard tube, both from HD-G. Markov converts the \(L^2\) bound to \(O_p\). \(\square\)

> **Corollary (exact recovery of HD1).** Under HD-M's \(m_0\)-dependence, L-7.1e gives \(\psi^+(nb_n)\le\sqrt{(2m_0+1)R^2/(nb_n)}\), and (G1-HD-L2-\(\psi\)) reduces **verbatim** to HD1's (G1-HD-L2). Under T-APP-4's summable physical dependence, \(\psi^+(nb_n)=O((nb_n)^{-1/2})\) and the same reduction holds.
>
> **Corollary (the separation condition was already there).** Therefore HD1's finite-memory assumption, and T-APP-4's summable-physical-dependence assumption, *are* separation conditions in the sense of ID-7: each implies \(\psi^+(nb_n)\asymp(nb_n)^{-1/2}\to0\), which is exactly (S5). What HD1 does not do is display that this is what the assumption is buying, or state the weakest condition under which it is bought. (G1-HD-L2-\(\psi\)) does both.

**Status: PROVED.** This discharges the load-bearing half of the lead's L-7.3.

### 2.4 L-7.3.3 — propagation through the rest of the chain

Each node below is checked for what it consumes. "Unchanged" means the node's proof uses no dependence input beyond what has already been replaced, so the statement holds with \(\ell_n\) replaced by \(\ell_n(\psi)\) and nothing else altered.

| Node | What its proof consumes | Verdict |
|---|---|---|
| **GRID** | (G1-HD-L2-\(\psi\)) at each deterministic vertex, then Markov on the average of \(M+1\) squared errors | **Unchanged.** RMS \(=O_p(\ell_n(\psi))\). |
| **Theorem PF** | GRID; \(M_n=\lceil\bar\ell_n^{-2/3}\rceil\); \(\max_je_j\le\sqrt{M_n+1}\,\mathrm{RMS}=O_p(\ell_n^{2/3})=o_p(1)\); Busemann convexity; uniform Jacobi/holonomy bounds from HD-G; the algebraic facts \(M_n\ell_n^2,M_n^{-2}=O(\ell_n^{4/3})\) | **Unchanged.** All inputs are deterministic geometry or GRID. The algebra \(M_n\ell_n^2=\ell_n^{4/3}\) is identity-level in \(\ell_n\), hence holds for \(\ell_n(\psi)\). Requires \(\ell_n(\psi)\to0\), i.e. (S5). |
| **OBS** | PF plus uniform Log base-point Lipschitz stability; explicitly *pathwise* ("the transformed feasible row need not remain \(m_0\)-dependent: the next comparison is pathwise") | **Unchanged.** \(q_n=O_p(\ell_n(\psi))\). |
| **\(d_{\rm or,n}\)** (oracle HS lag-row) | Hilbert–Schmidt concentration of the *products* \(Y_t\otimes Y_{t-h}\) | **DEGRADES.** See L-7.3.4. |
| **P1-ROW, P1-OP, P1-OP-zeta** | pathwise Cauchy–Schwarz expansion + deterministic row-operator multiplication | **Unchanged** given \(d_{\rm or,n}\) and \(q_n\). |
| **SIG, SIG2** | HD-L algebra | **Unchanged** (population). |
| **EV / beyond-rank square** | singular-value min–max on \(\widehat{\mathcal G}=\mathcal G+\mathcal D\) | **Unchanged.** |
| **Davis–Kahan / HD-E** | deterministic perturbation with the actual gap \(\Delta_n\) | **Unchanged.** |
| **TAU / threshold / ridged selectors** | \(d_n^2=o_p(\tau_n)\), \(\tau_n=o(\Delta_n)\), \(\eta_n=o_p(\Delta_n)\) | **Unchanged in form**; the admissible \(\tau_n\) window narrows because \(d_n\) is larger. |
| **G1′-HD (derivative)** | differentiated weights; \((nb_n^3)^{-1/2}\) | **Degrades to \(\psi^+\) at the differentiated weight scale**, but is *not consumed by HD-E* (HD1 §2 and §5: "SUPERSEDED: G1′ as a loading-theorem dependency"). Recorded, not repaired. |
| **G1-HD (sup-norm) / HD-Minf** | Lemma 4.1 **(4.2)**, i.e. the residue-class device | **DIES under long memory.** See L-7.3.5. Not consumed by HD-E. |

Net conclusion:

\[
\boxed{\;
\|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
=O_p\!\left(\frac{d_{\rm or,n}+\ell_n(\psi)}{\Delta_n}\right),
\qquad
\ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1},}
\tag{HD-E-\(\psi\)}
\]

whenever \(\eta_n=2A_{2,n}\{d_{\rm or,n}+\sqrt{h_0}(2Rq_n+q_n^2)\}+(\cdot)^2=o_p(\Delta_n)\).

**Status: PROVED.**

### 2.5 L-7.3.4 — the oracle row degrades, and by exactly how much

This is the "be honest" clause. Under long memory the *products* \(Y_t\otimes Y_{t-h}\) are not weakly dependent even in the second-moment sense, and \(d_{\rm or,n}=O_p(n^{-1/2})\) fails.

> **Lemma L-7.3.4.** Let \(Y_t=Af_t+\varepsilon_t\) with \((f_t)\) a centred stationary Gaussian \(\mathbb R^r\) process with \(|\gamma_{f,ij}(h)|\le C(1+|h|)^{2d-1}\), \(d\in(0,1/2)\), \(A^*A=I_r\), and \(\varepsilon\) a bounded temporally uncorrelated sequence with zero factor–noise cross-lags at all lags and \(\mathbb E[\varepsilon_t\otimes\varepsilon_s]=0\) for \(s\ne t\) (HD-L). Then for each fixed \(h\le h_0\),
> \[
> \Big\|\frac1n\sum_t\{Y_t\otimes Y_{t-h}-\Gamma(h)\}\Big\|_{L^2(\rm HS)}
> \asymp
> \begin{cases}
> n^{-1/2}, & d<1/4,\\[2pt]
> n^{-1/2}\sqrt{\log n}, & d=1/4,\\[2pt]
> n^{-(1-2d)}, & 1/4<d<1/2 .
> \end{cases}
> \tag{2.5}
> \]
> Hence \(d_{\rm or,n}=O_p(n^{-1/2}+n^{-(1-2d)})\).

**Proof.** Write \(\zeta_t=Y_t\otimes Y_{t-h}-\Gamma(h)\). Then
\(n^{-2}\mathbb E\|\sum_t\zeta_t\|_{\rm HS}^2=n^{-2}\sum_{s,t}\operatorname{tr}\operatorname{Cov}_{\rm HS}(\zeta_t,\zeta_s)\).
Decompose \(Y_t\otimes Y_{t-h}=Af_t\otimes Af_{t-h}+Af_t\otimes\varepsilon_{t-h}+\varepsilon_t\otimes Af_{t-h}+\varepsilon_t\otimes\varepsilon_{t-h}\). The three terms containing \(\varepsilon\) have covariance zero for \(|t-s|>h\), by whiteness of \(\varepsilon\), independence of \(\varepsilon\) from \(f\), and \(h\ge1\); they contribute \(O(n^{-1})\) to the variance. For the pure factor term, \(A^*A=I_r\) makes the HS inner product equal to the Euclidean one on \(\mathbb R^{r\times r}\), and Isserlis' theorem for centred jointly Gaussian \(f\) gives, for indices \(i,j,k,l\),
\[
\operatorname{Cov}(f_{t,i}f_{t-h,j},\,f_{s,k}f_{s-h,l})
=\gamma_{ik}(t-s)\gamma_{jl}(t-s)+\gamma_{il}(t-s+h)\gamma_{jk}(t-s-h).
\]
For \(|t-s|\ge2h\) each product is bounded by \(C'(1+|t-s|)^{2(2d-1)}\); for \(|t-s|<2h\) it is bounded by a constant, contributing \(O(n^{-1})\). Therefore
\[
n^{-2}\sum_{s,t}|\operatorname{Cov}|\le C''n^{-2}\sum_{s,t}(1+|s-t|)^{-\beta}+O(n^{-1}),
\qquad\beta:=2(1-2d).
\]
The elementary estimate \(n^{-2}\sum_{s,t=1}^n(1+|s-t|)^{-\beta}\asymp n^{-1}\) for \(\beta>1\), \(\asymp n^{-1}\log n\) for \(\beta=1\), \(\asymp n^{-\beta}\) for \(\beta<1\), together with \(\beta>1\iff d<1/4\), gives the upper half of (2.5); the matching lower order follows by retaining only the first Isserlis term, which is nonnegative on the diagonal blocks when \(\gamma\) is nonnegative. \(\square\)

> **Corollary (the degradation does not bind).** At the re-optimised bandwidth of L-10.1, \(\ell_n(\psi)\asymp n^{-3(1-2d)/(7-2d)}\), and
> \[
> \frac{3(1-2d)}{7-2d}<1-2d\quad\text{for all }d\in[0,1/2),
> \]
> because \(3/(7-2d)<1\). Hence \(n^{-(1-2d)}=o(\ell_n(\psi))\): the oracle-row degradation is strictly dominated by the mean channel and the headline (HD-E-\(\psi\)) numerator is \(\ell_n(\psi)\) alone.

**Scope honesty.** (2.5) is proved for the *Gaussian* factor class — which is exactly the class on which P1-ID-A §3.3 gives the full-FDD quotient, so it is the class ID-2 already privileges. Outside Gaussianity the same conclusion holds under a fourth-cumulant summability condition
\(\sum_{k}|\operatorname{cum}_4(f_{t,i},f_{t-h,j},f_{t+k,k'},f_{t+k-h,l'})|<\infty\); I state that as the general hypothesis and prove only the Gaussian case, per the campaign's standard.

**Status: PROVED** (Gaussian class), with the general class stated as an explicit cumulant hypothesis.

### 2.6 L-7.3.5 — the residue-class device, and what actually dies

> **Claim (device unavailable).** The device "split an \(m_0\)-dependent row into \(m_0+1\) independent residue classes" has no long-memory analogue. For any fixed \(m\ge0\), the residue subsequence \(\{\xi_{j+(m+1)k}\}_{k}\) of a process with \(\operatorname{tr}\Gamma(h)\asymp|h|^{2d-1}\) has \(\operatorname{tr}\Gamma_{\rm sub}(k)=\operatorname{tr}\Gamma((m+1)k)\asymp(m+1)^{2d-1}|k|^{2d-1}\) — the *same* memory exponent \(d\). The split therefore produces \(m+1\) sequences each of which is again long-memory, never independent. **Status: DISPROVED as available.**

> **Claim (consumers).** The device is consumed only by HD1-A Lemma 4.1 display (4.2), which feeds Lemma 4.2's uniform bound \(\sup_u\|Z_j(u)\|=O_p(\sqrt{\log n/(nb_n)})\), which feeds the sup-norm theorem G1-HD and, through it, the optional continuous-\(u\) branch under HD-Minf. It is **not** consumed by (4.1), by G1-HD-L2, by GRID, by PF, by OBS, by P1-ROW/P1-OP, by EV, or by Davis–Kahan. This is verifiable line by line in HD1 §2 ("The proof is empirical Sturm at each deterministic population barycentre, the weighted Hilbert inequality obtained by splitting an \(m_0\)-dependent row into \(m_0+1\) independent residue classes …" — the splitting is attributed to the *weighted Hilbert inequality*, whose \(L^2\) form (4.1) is proved without it) and in Theorem HD-E's proof, which lists exactly: G1-HD-L2, GRID, PF, OBS, P1-ROW, P1-OP, Davis–Kahan, EV, TAU. **Status: SEPARATED — HD-E does not consume the device.**

**Replacement argument supplied.** For the mean channel, the replacement is L-7.3.1's exact quadratic form, which needs *no* dependence theorem — only weak stationarity of the frozen score. For the row channel, the replacement is L-7.3.4's Isserlis computation. Both are supplied above.

**Restriction declared and its boundary reason.** Under \(\psi^+\) alone (i.e. a second-moment condition), the following are **not** available and are explicitly out of scope of L-7.3:

* the sup-norm level theorem \(r_{\infty,n}=b_n^3+n^{-a}+n^{-1}+\sqrt{\log n/(nb_n)}\) and every consumer of a *uniform-in-\(u\)* statement;
* the essential-sup coupling branch HD-Minf;
* the derivative theorem G1′-HD at its stated order.

The **boundary reason** is not "the proof got hard": a second-moment condition cannot produce an exponential tail, and the specific device HD1 uses to produce one is proved unavailable above. A replacement sup-norm theorem would need a genuinely new maximal inequality for long-memory Hilbert averages (e.g. via a Hermite/Wiener-chaos expansion), which is a different theorem, not a repair of this one. Since no HD-E consumer needs it, the honest disposition is separation, not repair.

**Status: DISPROVED (device) + SEPARATED (consumer) — terminal.**

---

## 3. L-7.2 — Theorem ID-7 (constructive separation)

### 3.1 Primitive assumptions

All five are stated in primitive geometric or probabilistic terms; §3.4 gives each one a proved boundary.

**(S1) Deterministic smooth centre path.** \(\mu:[0,1]\to M_n\) is deterministic and \(C^3\) in the sense of covariant derivatives along itself, with \(\sup_u\|\nabla_u^{(k)}\mu\|\le L_k\), \(k=1,2,3\), uniformly in \(n\); the whole curve lies inside the HD-G tube.

**(S2) Frozen persistence controlled by \(\psi\).** For each \(u\) the frozen transported tangent score
\(Z^{(u)}_t=\mathcal P^{\mu}_{u\to u_0}\operatorname{Log}_{\mu(u)}X^{(u)}_t\)
is centred, square-integrable and weakly stationary in \(H\), with \(\sup_u\operatorname{tr}\Gamma_u(0)\le R^2\) and absolute modulus \(\psi^+\). Additionally the family is Hölder in \(u\):

\[
\big\|Z^{(u)}_t-Z^{(v)}_t\big\|_{L^2}\le L_{\rm fr}|u-v|^{\alpha_{\rm fr}},
\qquad \alpha_{\rm fr}\in(0,1],
\tag{S2b}
\]

on one common probability space. **(S2b) is not new**: it is exactly the same-freeze process-level coupling that P1-ID-A §12 (objection AC-5) *required* as a mandatory repair, and it is exactly the first display of Dahlhaus–Richter–Wu (2019) Assumption 2.1(S1) with \(q=2\).

**(S3) Local stationarity with exponent \(a\).** \(\sup_{t,n}\|d(X_{t,n},X^{(u_t,n)}_t)\|_{L^2}\le Cn^{-a}\), \(a>0\) — i.e. (HD-M2) unchanged, and the second display of DRW Assumption 2.1(S1) with \(q=2\), \(\alpha=a\).

**(S4) ID-2's frozen-in-\(u\) conditions.** At every \(u\): \(Z^{(u)}_t=Af^{(u)}_t+\delta^{(u)}_t\) with \(A:\mathbb R^r\to H\) injective, \(A^*A=I_r\), common in \(u\); \(f^{(u)}\) centred and weakly stationary; \(\delta^{(u)}\) temporally uncorrelated; both factor–noise cross-lag directions zero at every included nonzero lag \(h\in\{\pm1,\dots,\pm h_0\}\); minimum dynamic rank, i.e. \(Q(u)=\sum_{h=1}^{h_0}C_f(u,h)C_f(u,h)^*\succ0\).

**(S5) Bandwidth compatibility.** \(b_n\to0\), \(nb_n/\log n\to\infty\), \(n^{-a}=O(b_n)\) (these three are HD-K verbatim), **and**

\[
\boxed{\ \psi^+(nb_n)=o(1).\ }
\tag{S5-\(\psi\)}
\]

### 3.2 Statement

> **Theorem ID-7 (constructive separation, with attainment by the project's own estimator).**
> Assume HD-G, HD-X, and (S1)–(S5), with (HD-M-\(\psi\)) of §2.3 replacing HD-M's finite-memory clause, and HD-L holding frozen-in-\(u\) as in (S4). Then:
>
> **(i) Identification.** From \(\mathcal I_J\) the centre path \(u\mapsto\mu(u)\) and the loading space \(E=\operatorname{ran}A\) are *separately* identified: \(\mu(u)\) is the unique Fréchet mean of the frozen marginal \(Q_u\), and \(E=\overline{\operatorname{span}}\{\operatorname{ran}\Gamma_{Z^{(u)}}(h):u\in[0,1],\,h\ne0\}\).
>
> **(ii) Estimability.** The three-scale polygonal estimator of HD-K/PF satisfies
> \[
> \|\log_{\mu_n}\hat\mu_n^{(3)}\|_{L^2}=O_p(\ell_n(\psi)),
> \qquad
> \ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1},
> \]
> and, with \(d_n(\psi)=O_p(d_{\rm or,n}+\ell_n(\psi))\) and \(\eta_n(\psi)=2A_{2,n}d_n(\psi)+d_n(\psi)^2\), if \(\eta_n(\psi)=o_p(\Delta_n)\) then
> \[
> \|\sin\Theta(\widehat E_n,E_n)\|_{\rm op}
> =O_p\!\left(\frac{d_{\rm or,n}+\ell_n(\psi)}{\Delta_n}\right),
> \qquad
> \widehat\lambda_{r+1,n}\le d_n(\psi)^2 .
> \]
>
> **(iii) Separation.** Both are simultaneously consistent, so the centre drift and the persistent tangent factor are separately *recoverable from one path*, not merely separately *defined*.

### 3.3 Proof

**(i) Identification.** By HD-G the frozen Fréchet objective \(F_{Q_u}\) is strongly convex on the tube with Hessian lower bound \(I\), so its argmin is a singleton; by (S1) and the model it equals \(\mu(u)\). ID-1 (P1-ID §4; P1-ID-A Claim A1) then identifies \(\mu(u)\) from \(Q_u\), hence from \(\mathcal I_M\subseteq\mathcal I_J\).

For the loading space: under (S4), P1-ID-A Claim A3 equations (4.2)–(4.3) give, at each frozen \(u\),
\(\mathcal S_{Z^{(u)}}=A\,\mathcal D_{f^{(u)}}\) and, because \(Q(u)\succ0\) forces \(\operatorname{span}_{h\le h_0}\operatorname{ran}C_f(u,h)=\mathbb R^r\), \(\mathcal D_{f^{(u)}}=\mathbb R^r\); hence \(\mathcal S_{Z^{(u)}}=\operatorname{ran}A=E\) for every \(u\), and a fortiori the union span is \(E\).

It remains to show \(\Gamma_{Z^{(u)}}(h)\) is an \(\mathcal I_J\)-functional. Fix \(u\) and a window \(W_n(u)\) of size \(k_n\to\infty\), \(k_n/n\to0\). By (S3) and (S2b), for \(t\in W_n(u)\),
\(\|Z_{t,n}-Z^{(u)}_{t}\|_{L^2}\le C n^{-a}+L_{\rm fr}(k_n/n)^{\alpha_{\rm fr}}\to0\)
(the first from the array coupling at \(u_t\), the second from re-freezing \(u_t\) to \(u\)) — this is precisely the AC-5 repair of P1-ID-A §12. Cauchy–Schwarz on the products then gives
\(\Gamma_{Z^{(u)}}(h)=\lim_n k_n^{-1}\sum_{t\in W_n(u)}\mathbb E[Z_{t,n}\otimes Z_{t-h,n}]\),
a limit of two-time population moments of the array, hence of \(\mathcal I_J\). \(\square\)

**(ii) Estimability.** Proposition L-7.3.2 gives the mean rate. Table L-7.3.3 propagates it through GRID, PF and OBS unchanged, and Lemma L-7.3.4 supplies \(d_{\rm or,n}\). P1-ROW, P1-OP, EV and Davis–Kahan are deterministic given those two inputs. (S5-\(\psi\)) is what makes \(\ell_n(\psi)\to0\), which PF requires for the common tube event \(\max_je_j=o_p(1)\). \(\square\)

**(iii)** Immediate from (i) and (ii). \(\square\)

### 3.4 What the theorem buys that ID-1 + ID-2 do not — stated plainly

ID-1 and ID-2 are *population* statements. ID-1 says: if you know every marginal, the unique Fréchet centre is pinned. ID-2 says: if you know every frozen lag covariance, the minimum dynamic loading span is pinned up to gauge. Neither says anything about one path of length \(n\). ID-3 supplies the one-path bridge but in a form that is deliberately unusable for design: recovery holds pointwise iff there is no atom at frequency zero, and — this is A7 — **no uniform rate follows from that qualitative predicate**, because the AR(1) sequence \(\rho_n=1-n^{-2}\) has no atom for any \(n\) and yet a fixed positive minimax risk.

ID-7's content is exactly the quantitative replacement A7 asked for:

1. It replaces the predicate "\(F_{Z^{(u)}}(\{0\})=0\)" by the **number** \(\psi^+(nb_n)\), indexed by the sample size and the bandwidth actually used.
2. It makes the condition **uniform by construction** (\(\psi^+=\sup_u\psi^+_u\)), which is the precise defect A7 exhibits.
3. It proves the condition is **attained by the project's own three-scale polygonal estimator**, not by an abstract smoother, and displays the exact position of the term in the rate.
4. It exhibits the constant: (S5-\(\psi\)) is *not* an extra assumption bolted on — under HD1's own HD-M it is automatically satisfied with \(\psi^+(nb_n)\asymp(nb_n)^{-1/2}\). ID-7 therefore proves that **HD1's finite-memory assumption already is the separation condition**, and identifies the weakest condition that does the same job.
5. It comes with an exact meeting point with the impossibility (§4), so the positive and negative results share a boundary rather than leaving a gap.

### 3.5 Boundary reason for every restriction

| Restriction | Proved boundary | Where |
|---|---|---|
| (S1) \(C^3\), not \(C^2\) | positive-weight Richardson is *capped* at certified bias order 3 because the uncorrected change-of-base-point error is cubic; the four-shape system \((1,m_1,m_2,m_1^2)\) is singular for every scale family | G1 audit §5 (internal, already proved) |
| (S1) deterministic centre | a random invariant component cannot be inserted into a deterministic centre curve | P1-ID-A §5 item 5 |
| (S2)/(S5-\(\psi\)) | exact: §4 below, with the profile \(\Psi\) and the two-point Pinsker floor meeting at \(x\asymp1\) | §4 |
| (S2b) Hölder in \(u\) | without it the lagged frozen variable is frozen at the *wrong* time and Cauchy–Schwarz does not close; sustained objection AC-5 | P1-ID-A §12 AC-5 |
| (S3) exponent \(a\) | sharp: the tvAR(1) array of §5.3 attains \(a=1-\theta\) exactly and no better | §5.3 |
| (S4) both cross-lag directions | one-sided cross-lag failure is exhibited; colored idiosyncratic noise destroys persistent factor/noise separation outright | P1-ID-A §3.4 "Assumptions, consumer, weakness" |
| (S4) minimum rank | dynamically silent directions: an iid loaded coordinate is reallocable and is not identified | P1-ID-A §4 "Dynamically silent directions" |
| (S5) \(nb_n/\log n\to\infty\) | **inherited from HD-K, not newly imposed by A.** Its consumer in the \(L^2\) branch is the uniform boundedness of the kernel denominators (HD1-A §3). Recorded as inherited. | HD1 §1 (HD-K) |

No restriction in (S1)–(S5) is the conclusion renamed as a primitive.

**Status of L-7.2 / ID-7: PROVED.**

---

## 4. L-7.4 — sharpness: the positive theorem and ID-3's impossibility meet exactly

Take the flat scalar array of ID-3 §8 / P1-ID-A §8: unknown constant centre \(m\), frozen factor a Gaussian AR(1) with unit marginal variance and coefficient \(\rho_n\), local window of \(N_n=nb_n\) observations. Put

\[
x_n:=(1-\rho_n)\,nb_n .
\]

> **Theorem L-7.4 (exact boundary, both directions).**
>
> **(a) Sufficiency.** If \(x_n\to\infty\) then \(\psi(N_n)^2\le2/x_n\to0\), so (S5-\(\psi\)) holds and ID-7 applies: \(\ell_n(\psi)=b_n^3+O(x_n^{-1/2})+n^{-a}+n^{-1}\to0\) and both the centre path and the loading space are consistently estimated.
>
> **(b) Failure of the estimator.** If \(\limsup_nx_n=x_0<\infty\), then along any subsequence with \(x_n\to x'\le x_0\), \(\psi(N_n)^2\to\Psi(x')\ge\Psi(x_0)>0\) by L-7.1a′ and strict monotonicity of \(\Psi\). The local-average error therefore does not tend to zero; (S5-\(\psi\)) fails.
>
> **(c) Failure of every estimator (information floor).** Under the same condition, no estimator of \(m\) based on the window is uniformly consistent. Indeed
> \[
> I_{N}(\rho)=\mathbf1^\top\Sigma_\rho^{-1}\mathbf1=\frac{N(1-\rho)+2\rho}{1+\rho}
> =\frac{x+2\rho}{1+\rho}\le x_0+2 ,
> \]
> so for the two-point family with means \(\pm a\),
> \(\mathrm{KL}(P_{+a}\|P_{-a})=\tfrac12(2a)^2I_N\le2a^2(x_0+2)\),
> and Pinsker gives \(\|P_{+a}-P_{-a}\|_{\rm TV}\le a\sqrt{x_0+2}\). Choosing \(a^2=1/\{4(x_0+2)\}\) gives \(\mathrm{TV}\le1/2\) and
> \[
> \sup_{m\in\{-a,a\}}\mathbb E_m(\widehat m-m)^2\ \ge\ \frac{a^2}2\{1-\mathrm{TV}\}\ \ge\ \frac1{16(x_0+2)}>0
> \]
> uniformly in \(n\).
>
> **(d) Meeting point.** \(\Psi\) is continuous and strictly decreasing with \(\Psi(0)=1\) and \(\Psi(\infty)=0\); \(I_N(\rho)=(x+2\rho)/(1+\rho)\) is an increasing function of \(x\) alone in the limit \(\rho\to1\). Both the achievable variance and the information floor are governed by the **same scalar \(x=(1-\rho)nb_n\)**. Hence
> \[
> \boxed{\ \text{ID-7 holds}\iff x_n\to\infty;\qquad \text{ID-3's floor bites}\iff x_n=O(1).\ }
> \]
> There is no gap.

**Proof.** (a) is the second bound of L-7.1a′. (b) is L-7.1a′ plus strict monotonicity. (c) is P1-ID-A §8 equation (8.1)–(8.2) with \(n\) replaced by \(N_n\) and \(a\) rechosen; the identity (8.1) is proved there by direct multiplication with the tridiagonal AR(1) precision matrix, and the substitution is legitimate because the window is a set of consecutive indices, so its marginal law is again AR(1) of length \(N_n\). (d) collects (a)–(c) and L-7.1a′. \(\square\)

### 4.1 By how much ID-3's construction violates (S5)

ID-3 uses \(\rho_n=1-n^{-2}\). At the robust design point \(b_n=n^{-1/7}\):

\[
x_n=(1-\rho_n)\,nb_n=n^{-2}\cdot n^{6/7}=n^{-8/7}\longrightarrow0 .
\]

Therefore \(\psi(nb_n)^2\to\Psi(0)=1\): **the local average is exactly as noisy as a single observation — the smoothing window buys nothing at all.** Even at the full sample (\(b_n\equiv1\)) one has \(x_n=n^{-1}\to0\), consistent with the repository's \(I_n(\rho_n)\le3/2\).

Quantitatively, (S5-\(\psi\)) at \(b_n=n^{-1/7}\) requires \(1-\rho_n\gg n^{-6/7}\). ID-3's construction takes \(1-\rho_n=n^{-2}\), i.e. it misses the boundary by the polynomial factor

\[
\frac{n^{-6/7}}{n^{-2}}=n^{8/7}.
\]

So the impossibility construction is not marginally outside ID-7 — it is outside by a full polynomial order \(n^{8/7}\), and it is outside for *every* admissible bandwidth (since \(b_n\le1\) forces \(x_n\le n^{-1}\)).

**Status: PROVED.**

---

## 5. ID-10 — the persistence compatibility window

Three constraints must hold simultaneously: (i) ID-3's information floor, now in the exact form \(x_n\to\infty\) / \(\psi^+(nb_n)\to0\); (ii) HD-M's local stationarity \(O(n^{-a})\) with the design clause \(a\ge3/7\); (iii) HD-K's \(nb_n/\log n\to\infty\) (and \(n^{-a}=O(b_n)\)).

### 5.1 L-10.1 — memory-exponent window

Let \(\psi^+(N)\asymp N^{-(1/2-d)}\), \(d\in[0,1/2)\), and \(b_n=n^{-\alpha}\).

**Balance.** \(b_n^3=n^{-3\alpha}\) and \(\psi^+(nb_n)=n^{-(1-\alpha)(1/2-d)}\). Setting \(3\alpha=(1-\alpha)(1/2-d)\):

\[
\alpha\Big(3+\tfrac12-d\Big)=\tfrac12-d
\ \Longrightarrow\
\boxed{\ \alpha(d)=\frac{1/2-d}{7/2-d}=\frac{1-2d}{7-2d}\ },
\qquad
\ell_n(\psi)\asymp n^{-3\alpha(d)}=n^{-\frac{3(1-2d)}{7-2d}} .
\]

**The lead's algebra is exactly correct.** Checks: \(d=0\Rightarrow\alpha=1/7\), rate \(n^{-3/7}\) ✓. \(d\uparrow1/2\Rightarrow\alpha\downarrow0\), rate \(\to n^0\): degenerate ✓. \(\alpha(d)\) is strictly decreasing on \([0,1/2)\) with range \((0,1/7]\).

**HD-K at the re-optimised bandwidth.** \(nb_n=n^{1-\alpha(d)}\) with \(1-\alpha(d)\ge6/7\), so \(nb_n/\log n\to\infty\) ✓ with room to spare. \(n^{-a}=O(b_n)\) requires \(a\ge\alpha(d)=(1-2d)/(7-2d)\), which is at most \(1/7\) ✓ mild. **HD-K never binds.**

**HD-M at the re-optimised bandwidth.** Rate-matching requires \(n^{-a}=O(\ell_n(\psi))\), i.e. \(a\ge3\alpha(d)=3(1-2d)/(7-2d)\). Since \(3(1-2d)/(7-2d)\le3/7\) for all \(d\ge0\) (equivalent to \(7-14d\le7-2d\)), the literal HD-M clause \(a\ge3/7\) is *more* than sufficient. **HD-M never binds in the pure long-memory regime.**

**The exact window in \(d\):**

\[
\boxed{\ d\in[0,1/2),\quad b_n=n^{-(1-2d)/(7-2d)},\quad \ell_n(\psi)\asymp n^{-3(1-2d)/(7-2d)} ;
\quad\text{the headline }n^{-3/7}\text{ holds iff }d=0.\ }
\]

**Two honest caveats.**

* **The whole window \(d\in(0,1/2)\) lies outside every dependence assumption currently stated in the repository.** \(m_0\)-dependence (HD-M) fails for all \(d>0\); T-APP-4's summable \(L^2\) innovation effects fail for all \(d>0\) (\(\delta_2(k)\asymp k^{d-1}\) is not summable for \(d>0\)). The minimal replacement that makes the mean channel work is (HD-M-\(\psi\)) of §2.3; the minimal replacement that makes the row channel work is L-7.3.4's cumulant condition. This is a genuine gap in the canonical assumption set, recorded in §9.
* **The row channel changes character at \(d=1/4\)** (L-7.3.4) but is proved dominated, so the headline is unaffected.

**Status: PROVED (lead algebra confirmed exactly).**

### 5.2 L-10.2a — near-unit-root, persistence constant in rescaled time

If \(\rho\) does not depend on \(u\), the array is exactly stationary, so (HD-M2) holds with any \(a\) (take \(X^{(u)}_t\equiv X_{t,n}\)). Only the \(\psi\) constraint is live. With \(\rho_n=1-n^{-\theta}\) and \(b_n=n^{-\alpha}\), \(x_n=n^{1-\alpha-\theta}\), so

\[
\psi^+(nb_n)=o(1)\iff x_n\to\infty\iff\theta<1-\alpha .
\]

At the robust design point \(\alpha=1/7\): \(\boxed{\theta<6/7}\) — **the lead's value is exactly correct.**

**Re-optimisation.** \(\psi(nb_n)\approx\sqrt2\,x_n^{-1/2}=\sqrt2\,n^{-(1-\alpha-\theta)/2}\). Balancing against \(b_n^3=n^{-3\alpha}\):
\(3\alpha=(1-\alpha-\theta)/2\Rightarrow7\alpha=1-\theta\Rightarrow\alpha=(1-\theta)/7\), rate \(n^{-3(1-\theta)/7}\). HD-K: \(nb_n=n^{1-(1-\theta)/7}\to\infty\) ✓.

So the *consistency* window is \(\theta<6/7\) at fixed \(b_n=n^{-1/7}\), but the *rate-optimal* window is \(\theta\in[0,1)\) with bandwidth \(b_n=n^{-(1-\theta)/7}\) and rate \(n^{-3(1-\theta)/7}\). The headline \(n^{-3/7}\) requires \(\theta=0\).

**Status: PROVED.**

### 5.3 L-10.2b — near-unit-root with persistence varying in \(u\): the induced exponent \(a\)

Model (a genuine triangular array, not a heuristic). Fix \(\theta\in(0,1)\), \(\varepsilon_n=n^{-\theta}\), and \(g\in C^2([0,1])\) with \(0<\underline g\le g\le\bar g\) and \(\|g'\|_\infty,\|g''\|_\infty<\infty\). Put

\[
\rho(u)=1-\varepsilon_ng(u),\qquad \sigma(u)=\{1-\rho(u)^2\}^{1/2},
\]
\[
X_{t,n}=\rho(u_t)X_{t-1,n}+\sigma(u_t)e_t,
\qquad
X^{(u)}_t=\rho(u)X^{(u)}_{t-1}+\sigma(u)e_t,
\]

with \((e_t)\) iid \(N(0,1)\) — **the same innovations**, so the two processes are coupled on one probability space, as (S2b)/(HD-M2) require. Each frozen process has unit marginal variance.

> **Proposition L-10.2b.** For this array,
> \[
> \boxed{\ \sup_t\big\|X_{t,n}-X^{(u_t)}_t\big\|_{L^2}\ \asymp\ n^{-(1-\theta)},
> \qquad\text{i.e. } a=1-\theta\ \text{ exactly.}}
> \]
> The exponent is attained (not merely bounded): whenever \(g'\not\equiv0\) the coupling error is bounded below by \(c\,n^{-(1-\theta)}\) with \(c>0\). The array satisfies Dahlhaus–Richter–Wu (2019) Assumption 2.1(S1) with \(q=2\) and \(\alpha=1-\theta\), and no larger \(\alpha\).

**Proof.** Both processes admit MA\((\infty)\) representations with the same innovations:

\[
X_{t,n}=\sum_{k\ge0}\tilde a_k e_{t-k},\quad
\tilde a_k=\Big(\prod_{j=0}^{k-1}\rho(u_{t-j})\Big)\sigma(u_{t-k});
\qquad
X^{(u_t)}_t=\sum_{k\ge0}a_ke_{t-k},\quad a_k=\rho(u_t)^k\sigma(u_t).
\]

Hence \(\|X_{t,n}-X^{(u_t)}_t\|_{L^2}^2=\sum_{k\ge0}(\tilde a_k-a_k)^2=\sum_{k\ge0}a_k^2(r_k-1)^2\) with \(r_k=\tilde a_k/a_k\), and \(\sum_ka_k^2=1\) (unit marginal variance).

Write \(h(u)=\log\rho(u)\), so \(h'(u)=-\varepsilon_ng'(u)/\{1-\varepsilon_ng(u)\}=-\varepsilon_ng'(u)\{1+O(\varepsilon_n)\}\) and \(h''=O(\varepsilon_n)\). Then

\[
\log r_k=\underbrace{\sum_{j=0}^{k-1}\{h(u_t-j/n)-h(u_t)\}}_{=:T_1}
+\underbrace{\tfrac12\log\frac{g(u_t-k/n)}{g(u_t)}+O(\varepsilon_n)}_{=:T_2},
\]

using \(\sigma(u)^2=\varepsilon_ng(u)\{2-\varepsilon_ng(u)\}\), so \(\sigma(u_{t-k})/\sigma(u_t)=\{g(u_t-k/n)/g(u_t)\}^{1/2}\{1+O(\varepsilon_n)\}\).

By Taylor, \(h(u_t-j/n)-h(u_t)=-(j/n)h'(u_t)+O(j^2n^{-2}\|h''\|_\infty)\), so

\[
T_1=\frac{k(k-1)}{2n}\,\varepsilon_n g'(u_t)\{1+O(\varepsilon_n)\}+O\!\Big(\frac{k^3\varepsilon_n}{n^2}\Big),
\qquad
T_2=-\frac{k}{2n}\frac{g'(u_t)}{g(u_t)}+O\!\Big(\frac{k^2}{n^2}\Big)+O(\varepsilon_n).
\]

The coefficients \(a_k^2=\sigma(u_t)^2\rho(u_t)^{2k}\) decay like \(2\varepsilon_ng\,e^{-2\varepsilon_ngk}\), so the effective range is \(k\asymp(\varepsilon_ng)^{-1}=n^{\theta}/g\). On that range,

\[
T_1\asymp\frac{\varepsilon_ng'}{2n}\cdot\frac1{(\varepsilon_ng)^2}
=\frac{g'}{2g^2}\cdot\frac1{n\varepsilon_n}
=\frac{g'}{2g^2}\,n^{\theta-1},
\qquad
T_2\asymp-\frac{g'}{2g^2}\,n^{\theta-1},
\]

both of exact order \(n^{-(1-\theta)}\), while the remainders are \(O(k^3\varepsilon_n/n^2)=O(n^{2\theta-2})\) and \(O(k^2/n^2)=O(n^{2\theta-2})\), i.e. \(O(n^{-2(1-\theta)})\), strictly smaller for \(\theta<1\). Setting \(x=\varepsilon_ng(u_t)k\), we obtain uniformly on the effective range

\[
\log r_k=n^{-(1-\theta)}\,\frac{g'(u_t)}{g(u_t)^2}\,\phi(x)+O(n^{-2(1-\theta)}),
\qquad
\phi(x)=\tfrac12x^2-\tfrac12x ,
\]

so \(r_k-1=n^{-(1-\theta)}\frac{g'}{g^2}\phi(x)\{1+o(1)\}\). Therefore

\[
\sum_ka_k^2(r_k-1)^2
=n^{-2(1-\theta)}\frac{g'(u_t)^2}{g(u_t)^4}\int_0^\infty 2e^{-2x}\phi(x)^2dx\,\{1+o(1)\},
\]

a finite positive constant times \(n^{-2(1-\theta)}\) whenever \(g'(u_t)\ne0\). Taking the supremum over \(t\) gives the upper bound with constant \(C=\sup_u|g'|/g^2\cdot(\int2e^{-2x}\phi^2)^{1/2}\), and evaluating at any \(t\) with \(g'(u_t)\ne0\) gives the matching lower bound. \(\square\)

**Numerical confirmation** (§10, check C4): with \(g(u)=1+0.8\sin(2\pi u)\), the empirical exponent of \(\sup_t\|X_{t,n}-X^{(u_t)}_t\|_{L^2}\) over \(n\in\{2000,\dots,32000\}\) converges to \(0.697\) at \(\theta=0.3\) (target \(0.700\)) and rises monotonically to \(0.467\) at \(\theta=0.5\) (target \(0.500\)); the ratio coupling\(/n^{-(1-\theta)}\) is constant to three digits at \(\theta=0.3\).

**Verdict on the lead's estimate.** The lead's \(a\approx1-\theta\) is **exactly right**, and the proof above shows it is *sharp*, not merely an upper bound. The lead's derived consequence \(a\ge3/7\Rightarrow\theta\le4/7\) is therefore arithmetically correct.

**DRW citation, applied line by line.** Dahlhaus, Richter and Wu (2019), *Bernoulli* 25(2), 1013–1044, Assumption 2.1 (*Stationary approximation*), condition (S1), reads verbatim (arXiv:1704.02860, §2): *"Let \(q>0\) and \(\|W\|_q:=(\mathbb E|W|^q)^{1/q}\). Let \(X_{t,n}\), \(t=1,\dots,n\) be a triangular array of stochastic processes. For each \(u\in[0,1]\), let \(\tilde X_t(u)\) be a stationary and ergodic process such that: \(\sup_{u\in[0,1]}\|\tilde X_t(u)\|_q<\infty\). There exists \(1\ge\alpha>0\), \(C_B>0\) such that uniformly in \(t=1,\dots,n\) and \(u,v\in[0,1]\),*
\[
\big\|\tilde X_t(u)-\tilde X_t(v)\big\|_q\le C_B|u-v|^{\alpha},
\qquad
\big\|X_{t,n}-\tilde X_t(\tfrac tn)\big\|_q\le C_Bn^{-\alpha}."
\]
**Application.** Take \(q=2\). The array above has \(\sup_u\|\tilde X_t(u)\|_2=1<\infty\) ✓. The first display holds with \(\alpha=1\): the same MA\((\infty)\) computation with \(\rho(u)^k\sigma(u)-\rho(v)^k\sigma(v)\) gives \(\|\tilde X_t(u)-\tilde X_t(v)\|_2\le C|u-v|\) with \(C\) depending on \(\|g'\|_\infty,\underline g\) only ✓. The second display holds with \(\alpha=1-\theta\) by Proposition L-10.2b, and with no larger \(\alpha\). Since DRW require **one common \(\alpha\)** for both displays, the array satisfies Assumption 2.1(S1) with \(\alpha=\min\{1,1-\theta\}=1-\theta\), and \(C_B\) as computed. **The exponent identification \(a=1-\theta\) is proved internally here; DRW supplies only the local-stationarity *mode*, exactly as C-AUDIT-8 requires.** No rate, no uniformity, and no triangular-array conclusion is imported from DRW.

**Status: PROVED (internally), with the mode CITED+APPLIED from DRW Assumption 2.1(S1).**

### 5.4 L-10.2c — \(\theta\le4/7\) is correct but is not the binding constraint

With \(a=1-\theta\), the three constraints at bandwidth \(b_n=n^{-\alpha}\) read:

1. **\(\psi\)**: \(\alpha<1-\theta\) (consistency) — or \(\alpha=(1-\theta)/7\) at the optimum;
2. **HD-M2 rate-matching**: \(n^{-a}=O(\ell_n(\psi))\), i.e. \(1-\theta\ge3(1-\theta)/7\) — **automatically true for every \(\theta<1\)**;
3. **HD-K**: \(n^{-a}=O(b_n)\), i.e. \(1-\theta\ge(1-\theta)/7\) — **automatically true**; and \(nb_n/\log n\to\infty\) ✓.

Hence the *self-consistent* window is \(\theta\in[0,1)\), with

\[
b_n=n^{-(1-\theta)/7},\qquad \ell_n(\psi)\asymp n^{-3(1-\theta)/7},\qquad a=1-\theta .
\]

Note that this is the *same* rate as in the constant-persistence case L-10.2a: the induced local-stationarity exponent \(a=1-\theta\) is exactly \(7/3\) times the rate exponent, so it is never binding.

**Where \(\theta\le4/7\) comes from, and what it really means.** The clause "\(a\ge3/7\)" in HD1 §4 is **not a primitive**: it is the design constant that makes \(n^{-a}\) dominated by \(n^{-3/7}\) at the specific bandwidth \(b_n=n^{-1/7}\). Reading it as a primitive and combining with \(a=1-\theta\) gives \(\theta\le4/7\) — arithmetically correct, but it answers the question "for which \(\theta\) does the array satisfy HD1's literal assumption list?" rather than "for which \(\theta\) is the separation achievable?". The honest statement is:

> **\(\theta\le4/7\)** is the window inside which the array satisfies HD-M's literal \(a\ge3/7\) clause.
> **\(\theta<1\)** is the window inside which ID-7's separation is achievable, at the degraded rate \(n^{-3(1-\theta)/7}\).
> **\(\theta=0\)** is required for the advertised \(n^{-3/7}\).

All three are proved; the lead should display the third, because it is the one a referee will ask about.

**Status: REFORMULATED+PROVED.**

---

## 6. L-10.3 — non-emptiness, binding constraint, and reconciliation with ID-3

### 6.1 Non-emptiness (explicit witness)

> **Lemma.** The window is nonempty. Witness: \(d=0\), \(\theta=0\), \(b_n=n^{-1/7}\), frozen factor
> \(f^{(u)}_t=\sum_{j=0}^{m_0}c_j(u)e_{t-j}\) with \(e\) iid unit-variance, \(c_j\in C^1\), and \(\sum_{j}c_j(u)\ne0\) for every \(u\).
> Then: \(\psi^+(N)\asymp N^{-1/2}\) exactly (L-7.1b, since \(\Lambda_u=(\sum_jc_j(u))^2>0\)); \(a=1\) (Lipschitz coefficients give an \(O(n^{-1})\) coupling by the same MA computation as L-10.2b with \(\varepsilon_n\equiv1\)); HD-K holds with \(nb_n=n^{6/7}\); HD-M's \(m_0\)-dependence holds by construction; and \(\ell_n(\psi)=n^{-3/7}\). All three constraints are satisfied with strict slack in two of them. \(\square\)

**Status: PROVED.**

### 6.2 Which constraint binds, by regime

| Regime | \(\psi\) (ID-3 floor) | HD-M (local stationarity) | HD-K | Binding |
|---|---|---|---|---|
| \(d=0,\theta=0\) (short memory, mild persistence) | slack: \(\psi=(nb_n)^{-1/2}\) | tight only through the *design* clause \(a\ge3/7\) | slack | bias/variance balance; nothing else |
| \(d\in(0,1/2)\) (long memory) | **binds** — sets \(\alpha(d)\) and the rate | slack (\(3\alpha(d)\le3/7\le a\)) | slack (\(nb_n\ge n^{6/7}\)) | **ID-3's floor** |
| \(\theta\in(0,1)\), persistence constant in \(u\) | **binds** — sets \(\alpha=(1-\theta)/7\) | vacuous (array is stationary) | slack | **ID-3's floor** |
| \(\theta\in(0,1)\), persistence varying in \(u\) | **binds** | tracks it exactly (\(a=1-\theta=\tfrac73\times\)rate exponent), never binds | slack | **ID-3's floor** |

**HD-K's \(nb_n/\log n\to\infty\) never binds** at any re-optimised bandwidth, because \(\alpha\le1/7\) in every regime, so \(nb_n\ge n^{6/7}\).

### 6.3 The final window in one display

\[
\boxed{
\begin{aligned}
&\text{Long memory: } d\in[0,\tfrac12),\quad b_n=n^{-\frac{1-2d}{7-2d}},\quad
\ell_n(\psi)\asymp n^{-\frac{3(1-2d)}{7-2d}},\quad \text{need }a\ge\tfrac{3(1-2d)}{7-2d};\\[4pt]
&\text{Near unit root: } \theta\in[0,1),\quad b_n=n^{-\frac{1-\theta}{7}},\quad
\ell_n(\psi)\asymp n^{-\frac{3(1-\theta)}{7}},\quad a=1-\theta\ \text{(induced, sharp)};\\[4pt]
&\text{HD-K: } nb_n\ge n^{6/7}\ \text{throughout — never binding};\\[4pt]
&\text{Headline } n^{-3/7}\iff d=0\ \text{ and }\ \theta=0 .
\end{aligned}}
\]

### 6.4 Reconciliation with ID-3's \(\rho_n=1-n^{-2}\) (\(\theta=2\))

**There is no contradiction.** \(\theta=2\) is excluded by HD1's assumptions three times over:

1. **By HD-M2 directly.** L-10.2b gives \(a=1-\theta=-1<0\) for the varying-persistence array; a negative exponent means the coupling *diverges*, so (HD-M2) fails outright. HD-M2 requires \(a>0\), i.e. \(\theta<1\). The margin is a **full unit of exponent**: \(\theta=2\) against \(\theta<1\), i.e. a factor \(n\).
2. **By HD-M's \(m_0\)-dependence.** An AR(1) with \(\rho_n=1-n^{-2}\) has effective memory \(n^2\), which is not \(m_0\)-dependent for any fixed \(m_0\), and not summably physically dependent uniformly in \(n\).
3. **By \(\psi\).** \(x_n=n^{-8/7}\to0\), so \(\psi^+(nb_n)\to1\) (§4.1).

**How thin is the margin, honestly.** The *theorem* survives on the whole open window \(d<1/2\), \(\theta<1\) — that is comfortable. The *advertised rate* does not: \(n^{-3/7}\) requires \(d=0\) **exactly** and \(\theta=0\) **exactly**. Any long memory whatsoever degrades the headline, continuously:

| \(d\) | 0 | 0.05 | 0.10 | 0.20 | 0.30 | 0.40 | 0.45 |
|---|---|---|---|---|---|---|---|
| rate exponent \(3(1-2d)/(7-2d)\) | 0.4286 | 0.3913 | 0.3529 | 0.2727 | 0.1875 | 0.0968 | 0.0492 |

At \(d=0.1\) — a very mild long memory — the rate has already fallen from \(n^{-0.43}\) to \(n^{-0.35}\). The lead's reading is confirmed: **the advertised \(n^{-3/7}\) requires genuine short memory, and any long memory degrades the headline.**

**Status: PROVED.**

---

## 7. L-10.4 — the APP-FIN verdict

APP-FIN: 240 monthly realised covariance matrices, 12 U.S. stocks, Bures–Wasserstein geometry (References audit §1).

### 7.1 The category error, handled explicitly

A finite dataset does not sit inside or outside an asymptotic window; the window is a statement about sequences. I therefore give (a) the asymptotic statement and (b) a finite-sample diagnostic, and I label the second as a diagnostic in every place it appears. **Nothing in §7 is used to establish or modify any analytic status.**

### 7.2 (a) The asymptotic statement

The window is \(d\in[0,1/2)\), \(\theta\in[0,1)\). Log realised volatility is empirically fractionally integrated with \(d\) around \(0.4\) (§7.4), i.e. **formally inside** the window, with re-optimised bandwidth \(\alpha(0.4)=0.2/6.2=0.0323\) and rate \(n^{-0.0968}\).

"Inside the window" is therefore true and almost worthless: the rate \(n^{-0.097}\) is barely a rate at all, and the re-optimised bandwidth \(b_n=n^{-0.0323}\) at \(n=240\) equals \(0.838\) — a smoothing window covering **84% of the sample**, which contradicts the scientific premise that the centre moves.

### 7.3 (b) The finite-sample diagnostic

Take \(n=240\), \(b_n=n^{-1/7}\). Then \(b_n=0.4571\), \(nb_n=109.7\approx110\), \(b_n^3=0.0955\). The diagnostic quantities are the *stochastic/bias ratio* \(\psi(nb_n)/b_n^3\) and the *effective number of independent factor draws per smoothing window*

\[
x_{\rm eff}:=\psi(nb_n)^{-2}
\qquad(\text{}=nb_n\text{ exactly for iid; }=\tfrac12(1-\rho)nb_n\{1+o(1)\}\text{ for AR(1) with }x\gg1).
\]

**AR(1) frozen factor, unit marginal variance (exact formula (1.1)):**

| \(\rho\) | \(x=(1-\rho)nb_n\) | \(\psi(nb_n)\) | \(\psi/b_n^3\) | \(x_{\rm eff}\) |
|---|---|---|---|---|
| 0 (iid) | 110 | 0.0953 | **1.00** | 110 |
| 0.30 | 77 | 0.1295 | 1.36 | 60 |
| 0.50 | 55 | 0.1641 | 1.72 | 37 |
| 0.70 | 33 | 0.2241 | 2.35 | 20 |
| 0.80 | 22 | 0.2802 | 2.93 | 13 |
| 0.90 | 11 | 0.3973 | 4.16 | 6.3 |
| 0.95 | 5.5 | 0.5403 | 5.66 | 3.4 |
| 0.98 | 2.2 | 0.7341 | 7.69 | 1.9 |
| 0.99 | 1.1 | 0.8452 | 8.85 | 1.4 |

**ARFIMA\((0,d,0)\) frozen factor, unit marginal variance (exact ACF):**

| \(d\) | \(\psi(nb_n)\) | \(\psi/b_n^3\) | \(x_{\rm eff}\) | asymptotic rate |
|---|---|---|---|---|
| 0.00 | 0.0953 | **1.00** | 110 | \(n^{-0.429}\) |
| 0.10 | 0.1476 | 1.55 | 46 | \(n^{-0.353}\) |
| 0.20 | 0.2323 | 2.43 | 19 | \(n^{-0.273}\) |
| 0.30 | 0.3714 | 3.89 | 7.3 | \(n^{-0.188}\) |
| **0.40** | **0.6035** | **6.32** | **2.7** | \(n^{-0.097}\) |
| 0.45 | 0.7747 | 8.11 | 1.7 | \(n^{-0.049}\) |

Note the design check: at \(d=0\) the ratio is exactly \(1.00\), confirming that \(b_n=n^{-1/7}\) is the balanced choice for short memory even at \(n=240\).

### 7.4 Primary-source verification of the empirical memory exponent

**Andersen, T. G., Bollerslev, T., Diebold, F. X. and Labys, P. (2003). "Modeling and Forecasting Realized Volatility." *Econometrica* 71(2), 579–625.** (Working-paper text verified at <https://www.bis.org/cgfs/Diebold-et-al.pdf>; NBER WP 8160.)

Verified verbatim from the source:

* Table 2, last column: GPH log-periodogram estimates of the fractional integration parameter \(d\) for **logarithmic** realised volatility: **DM/\$ 0.387, ¥/\$ 0.413, ¥/DM 0.430**, using \(m=[T^{4/5}]=514\) lowest-frequency periodogram ordinates, asymptotic s.e. \(\pi(24m)^{-1/2}=0.028\) for all three.
* Multivariate Robinson (1995) estimator: *"we obtain \(\hat d=0.401\)"*, with the test for a common \(d\) across the three series having p-value 0.510.
* Fractional-cointegration residual estimates: **0.356, 0.424, 0.393**.
* Footnote 21: *"the corresponding estimates of \(d\) for \(v_t\) [the realised standard deviation, not its log] … are about 0.15 less than those for \(y_t\)"*, i.e. \(\approx0.25\) on the untransformed scale.
* Estimator provenance recorded exactly: Geweke and Porter-Hudak (1983) log-periodogram regression as formally developed by Robinson (1995).

**Two transfer steps and their honest status.**

1. *Daily \(\to\) monthly.* Temporal aggregation is standard-claimed to preserve the order of fractional integration: Chambers, M. J. (1998), "Long Memory and Aggregation in Macroeconomic Time Series," *International Economic Review* 39(4), 1053–1072, concludes that a temporally aggregated series retains the same (possibly fractional) order of integration as the underlying series. **Status: CITED, not verified in depth, and not load-bearing** — it affects only the diagnostic's input, not any analytic claim. Chambers himself reports that empirical estimates were "at considerable variance with what was expected from the theory," so the transfer should be treated as indicative.
2. *Log realised volatility \(\to\) BW tangent score of realised covariance.* The APP-FIN score is a smooth nonlinear matrix functional of the realised covariance. If that functional has Hermite rank 1 in the underlying long-memory driver, \(d\) is preserved; if Hermite rank 2, the effective memory exponent of the score is \(d_{\rm eff}=2d-\tfrac12\) (Taqqu/Dobrushin–Major reduction), which at \(d=0.40\) gives \(d_{\rm eff}=0.30\), \(\psi/b_n^3=3.89\), \(x_{\rm eff}=7.3\). **This is an honest caveat that would improve, not worsen, the diagnostic.** I state both endpoints and claim neither.

### 7.5 Verdict

> **APP-FIN verdict.**
> *(a) Asymptotically*: monthly realised covariance under the documented persistence sits **formally inside** the window (\(d\approx0.4<1/2\)), but on the degenerate edge: the achievable rate is \(n^{-0.10}\) rather than \(n^{-0.43}\), and the rate-optimal bandwidth at \(n=240\) covers 84% of the sample, which is incompatible with the model's own premise of a moving centre.
> *(b) Finite-sample diagnostic*: at \(n=240\), \(b_n=n^{-1/7}\), the effective number of independent factor draws per smoothing window is \(x_{\rm eff}\approx2.7\) at \(d=0.40\) (\(\approx7.3\) under the Hermite-rank-2 caveat), against 110 for an iid factor, and the stochastic channel exceeds the bias channel by a factor \(\approx6\). For an AR(1) proxy the same adverse regime is reached at \(\rho\gtrsim0.95\).
> *(c) Consequence*: the diagnostic says the centre-drift/persistent-factor separation is **not empirically resolvable at APP-FIN's sample size under the documented persistence**. This is a diagnostic, not a theorem. It does not show that any published APP-FIN result is wrong; it shows that a moving-centre refit on that dataset must be reported as sensitivity evidence, which is exactly ID-6's existing wording, and that the persistence check should be reported alongside it.

**Status: PROVED as a computation; DIAGNOSTIC as an application claim.** No analytic status anywhere in this dossier depends on §7.

---

## 8. R4 — the declared-convention escape (ID-9 route 4)

### 8.1 L-9.R4.1 — equivariance rigidity

**Definitions.** Let \((M,d)\) be a metric space with isometry group \(\mathrm{Isom}(M)\). A **centre convention** on a class \(\mathcal D\subseteq\mathcal P(M)\) is a partial map \(c:\mathcal D\to M\) that is
(i) *marginal-functional*: \(c(Q)\) depends on \(Q\) alone; and
(ii) *equivariant*: \(c(g_\#Q)=g\cdot c(Q)\) for every \(g\in\mathrm{Isom}(M)\) with \(g_\#Q\in\mathcal D\).
For \(Q\in\mathcal D\) let \(G_Q=\{g\in\mathrm{Isom}(M):g_\#Q=Q\}\) (the stabiliser) and \(\mathrm{Fix}(G_Q)=\{x:gx=x\ \forall g\in G_Q\}\). Call \(Q\) **stabiliser-rigid** if \(\mathrm{Fix}(G_Q)\) is a singleton, and write \(\mathcal Q_{\rm rig}\) for the class of stabiliser-rigid laws.

> **Theorem L-9.R4.1.**
> **(1) Rigidity.** If \(Q\in\mathcal Q_{\rm rig}\cap\mathcal D\) and \(c(Q)\) is defined and single-valued, then \(c(Q)=x_Q\), the unique element of \(\mathrm{Fix}(G_Q)\). Consequently **all** marginal-functional equivariant conventions agree on \(\mathcal Q_{\rm rig}\).
> **(2) The Fréchet mean is one of them.** If \(Q\in\mathcal P_2(M)\) has a unique Fréchet mean \(m_Q\), then \(m_Q\in\mathrm{Fix}(G_Q)\); hence if in addition \(Q\in\mathcal Q_{\rm rig}\), \(c(Q)=m_Q\) for every such \(c\).
> **(3) Off \(\mathcal Q_{\rm rig}\) the conventions genuinely differ**, by the exact examples below.

**Proof of (1).** For \(g\in G_Q\), equivariance and \(g_\#Q=Q\) give \(c(Q)=c(g_\#Q)=g\cdot c(Q)\). So \(c(Q)\in\mathrm{Fix}(G_Q)=\{x_Q\}\). \(\square\)

**Proof of (2).** For \(g\in G_Q\),
\(F_Q(gx)=\int d(gx,z)^2Q(dz)=\int d(gx,gz)^2Q(dz)=\int d(x,z)^2Q(dz)=F_Q(x)\),
using \(g_\#Q=Q\) in the second equality and the isometry property in the third. Hence \(F_Q\circ g=F_Q\), so \(g\) permutes \(\operatorname{argmin}F_Q=\{m_Q\}\), forcing \(gm_Q=m_Q\). \(\square\)

**Which conventions are covered.** Marginal-functional and equivariant: (a) the Fréchet mean \(\operatorname{argmin}\int d(x,z)^2Q(dz)\); (b) the Fréchet median \(\operatorname{argmin}\int d(x,z)Q(dz)\); (c) any \(M\)-centre \(\operatorname{argmin}\int\rho(d(x,z))Q(dz)\) with \(\rho\) increasing, and any trimmed/quantile-type centre defined by an isometry-invariant trimming rule (e.g. discard the \(\alpha\)-fraction of mass farthest from the candidate, then minimise). Equivariance is immediate in each case because the objective is built from \(d\) alone. **Not** covered: (d) the smoothness-regularised centre — it fails (i) (§8.2); (e) a conditional centre given a latent variable — it fails (i) too (it is not a functional of any marginal).

**Exact separation off \(\mathcal Q_{\rm rig}\), flat.** \(M=\mathbb R\), \(Q=\tfrac34\delta_0+\tfrac14\delta_1\). Then \(m_Q=1/4\); the median objective \(\tfrac34|x|+\tfrac14|x-1|\) is minimised uniquely at \(x=0\). So mean \(\ne\) median. Consistency check: \(G_Q=\{\mathrm{id}\}\) (a reflection would have to exchange the atoms, which carry different masses), so \(\mathrm{Fix}(G_Q)=\mathbb R\) is not a singleton and \(Q\notin\mathcal Q_{\rm rig}\) ✓.

**Exact separation off \(\mathcal Q_{\rm rig}\), curved.** Let \(C\subset S^2\) be a great circle (totally geodesic) with intrinsic distance, and \(Q=(1-p)\delta_{z_0}+p\delta_{z_\beta}\) with atoms at arclength \(0\) and \(\beta\in(0,\pi)\), \(p\in(0,1/2)\). On the minor arc, parametrised by \(\vartheta\in[0,\beta]\), \(F_Q(\vartheta)=(1-p)\vartheta^2+p(\beta-\vartheta)^2\), minimised at \(\vartheta=p\beta\); points off the arc have strictly larger objective since \(\beta<\pi\). The median objective \((1-p)\vartheta+p(\beta-\vartheta)\) is minimised at \(\vartheta=0\) since \(p<1/2\). So mean \(=p\beta\ne0=\) median.

**A curvature-specific structural separation (new).** Take \(Q=\tfrac12(\delta_N+\delta_S)\) on \(S^2\) with \(N,S\) antipodal. Then:
* \(F_Q(x)=\tfrac12\{\vartheta^2+(\pi-\vartheta)^2\}\) with \(\vartheta=d(x,N)\), minimised at \(\vartheta=\pi/2\): \(\operatorname{argmin}F_Q\) is the **equator**, a 1-dimensional submanifold.
* The median objective is \(\tfrac12\{\vartheta+(\pi-\vartheta)\}=\pi/2\), **constant on all of \(S^2\)**: \(\operatorname{argmin}\) is the **entire sphere**, 2-dimensional.

So on one and the same law the mean's and the median's degeneracy sets have different dimensions. This proves the conventions are not merely different selections from a common set: **they have different failure geometries.** (The flat analogue: \(Q=\tfrac12(\delta_0+\delta_1)\) on \(\mathbb R\) has mean argmin \(\{1/2\}\), a singleton, and median argmin \([0,1]\), an interval.)

Here \(G_Q\) contains all rotations about the \(NS\) axis and the reflection swapping \(N,S\), so \(\mathrm{Fix}(G_Q)=\emptyset\) and \(Q\notin\mathcal Q_{\rm rig}\) ✓ — the theorem correctly declines to apply.

**Status: PROVED.**

### 8.2 L-9.R4.2 — the structural point, and the sharp form of the gate

**(A) The regularised centre is not a functional of each marginal.** Consider

\[
\hat\mu_\lambda=\operatorname*{argmin}_{\mu\in\mathcal C}\ \int_0^1F_{Q_u}(\mu(u))\,du+\lambda\int_0^1\|\mu'(u)\|^2du,
\qquad\lambda>0 .
\]

> **Proposition.** In \(M=\mathbb R\), \(\mathcal C=H^1([0,1])\), \(\hat\mu_\lambda(u_0)\) is **not** a functional of \(Q_{u_0}\).

**Proof.** With \(m(u)=\mathbb EQ_u\), \(F_{Q_u}(x)=(x-m(u))^2+\mathrm{Var}(Q_u)\), so the objective is \(\int(\mu-m)^2+\lambda\int(\mu')^2\) plus a constant. It is strictly convex and coercive on \(H^1\), so the minimiser is unique and solves the Euler–Lagrange equation with natural boundary conditions

\[
\mu-\lambda\mu''=m,\qquad \mu'(0)=\mu'(1)=0 .
\]

With \(k=\lambda^{-1/2}\) the Neumann Green's function is

\[
G(u,v)=\frac{\cosh\{k(u\wedge v)\}\ \cosh\{k(1-u\vee v)\}}{\sqrt\lambda\ \sinh k}\ >\ 0
\qquad\text{for all }(u,v)\in[0,1]^2,
\]

so \(\hat\mu_\lambda(u)=\int_0^1G(u,v)m(v)dv\) with a **strictly positive** kernel. Now take \(Q_u=\delta_{m(u)}\) and \(\widetilde Q_u=\delta_{\tilde m(u)}\) with \(m\equiv0\) and \(\tilde m=\mathbf1_{[1/2,1]}\). For any \(u_0<1/2\), \(Q_{u_0}=\delta_0=\widetilde Q_{u_0}\), yet
\(\hat\mu_\lambda(u_0)=0\) while \(\widetilde{\hat\mu}_\lambda(u_0)=\int_{1/2}^1G(u_0,v)dv>0\). \(\square\)

Two immediate consequences, both used below:
* **ID-1 does not apply pointwise to (d).** Two models with the same marginal at \(u_0\) can have different regularised centres at \(u_0\).
* **(d) is a different estimand.** \(\widetilde{\hat\mu}_\lambda(u_0)>0=\tilde m(u_0)\): the regularised centre is not the Fréchet mean of the marginal at that time.

**(B) But (d) is an \(\mathcal I_M\)-functional of the family.** The objective depends on \(\{Q_u\}_{u\in[0,1]}\) only through \(u\mapsto F_{Q_u}\), and \(\{Q_u\}_{u\in[0,1]}\) **is** \(\mathcal I_M\) (P1-ID §2, first row: "\(\mathcal I_M\) | every marginal \(Q_u\)"). Hence two models with equal \(\mathcal I_M\) have equal objectives, equal argmin sets, and — the argmin being a singleton by strict convexity in the flat case, or by an assumed convexity/uniqueness hypothesis in general — equal regularised centres. **The gate is not escaped; it is only relocated from the pointwise level to the family level.**

**(C) The sharp form of the gate.**

> **Theorem R4-GATE.** Let \(\mathcal I\) be a declared information set with realisation map \(\iota\) from admissible models to \(\mathcal I\)-values. Let \(c\) be a **single-valued centre convention that is a measurable functional of \(\iota\)**, i.e. \(c=\Psi\circ\iota\) for some measurable \(\Psi\). Then
> \[
> \iota(\mathcal M_1)=\iota(\mathcal M_2)\ \Longrightarrow\ c(\mathcal M_1)=c(\mathcal M_2).
> \]
> Consequently, two admissible models with the same \(\mathcal I\)-value can carry different centres **only** if:
> **(E1)** the defining variational problem is empty or has a nonsingleton solution set, so that \(c\) is single-valued only after a selection rule, and that selection rule is not itself a function of \(\iota\); or
> **(E2)** \(c\) is not a functional of \(\iota\) at all, i.e. \(c\) is measurable with respect to a latent \(\sigma\)-field not contained in \(\sigma(\iota)\).

**Proof.** The implication is the definition of a function. (E1)+(E2) is the exact negation of "\(c\) is a single-valued functional of \(\iota\)". \(\square\)

The theorem is trivial, and that is precisely its value: it shows the entire content of ID-1 lives in the word *declared*, and it bounds the escape space.

> **Corollary (ID-1).** Take \(\mathcal I=\mathcal I_M\), \(\Psi(Q)=\) the unique element of \(\operatorname{argmin}F_Q\). Then Theorem ID-1 follows: equal marginals give equal objectives, hence equal argmin sets, hence — when singleton — equal centres. The empty and nonsingleton cases are exactly (E1), which is why P1-ID §4 must separate the three cases.

> **Corollary R4-EXH (the campaign's escape space is exhausted).**
> * **R1** (empty argmin on the BW cone) \(\subset\) (E1);
> * **R2** (nonsingleton argmin and the cost of a selector) \(\subset\) (E1) — and it is *exactly* (E1), because a measurable selector restores single-valuedness only at the price of a rule not determined by \(\iota\);
> * **R3** (latent stochastic centre) \(\subset\) (E2) — a latent object is, by the lead ledger §2, in no information set;
> * **R4** (declared-convention escape) is **PROVED NOT AN ESCAPE**: every convention (a)–(d) is of the form \(\Psi\circ\iota\) for \(\iota=\) the \(\mathcal I_M\)-realisation, with only \(\Psi\) changing;
> * **R5** (sample-level non-uniqueness) is not a population escape at all: it concerns the empirical argmin, hence estimation, and is **SEPARATED** from identification by R4-GATE (the gate quantifies over models, not over samples).
>
> Hence \(\{R1,R2\}\cup\{R3\}\) exhausts the population escape space, and no sixth route exists. **Status: PROVED.**

**Status of L-9.R4.2: PROVED.**

### 8.3 L-9.R4.3 — ID-4 coverage: exactly three chart classes

ID-4's orbit is
\(\mathcal L_y=((\Phi_{x\to y})^{\mathbb Z})_\#\mathcal L_x\) — a **single, fixed, deterministic** chart change \(\Phi_{x\to y}\) applied identically to every time coordinate. Call this \(\mathcal L^{\rm fix}\). Define two further orbits:

* \(\mathcal L^{\rm tv}\): the **time-varying deterministic** compatible-chart orbit, generated by a deterministic base-point path \(\nu(\cdot)\) via the family \(\{\Phi_{\mu(u_t)\to\nu(u_t)}\}_t\);
* \(\mathcal L^{\rm rand}\): the **random** chart orbit, generated by a random base-point path.

> **Proposition L-9.R4.3.**
> 1. In a *fixed-centre* model, conventions (b) and (c) produce points \(y=c(Q)\) and their representations lie in \(\mathcal L^{\rm fix}\) — **covered by ID-4, no new class** — provided ID-4's declared hypotheses hold (compatible normal branches, and the complete score/observation support in the declared common domain \(U_{xyz}\), per Hostile Pass II lock 4).
> 2. In Paper 1's *moving-centre* model, (b) and (c) produce a path \(u\mapsto c(Q_u)\). If \(c(Q_u)\ominus\mu(u)\) is not constant in \(u\), the representation lies in \(\mathcal L^{\rm tv}\setminus\mathcal L^{\rm fix}\) — **a new class**.
> 3. Convention (d) lies in \(\mathcal L^{\rm tv}\setminus\mathcal L^{\rm fix}\) generically, and in addition is not a pointwise marginal functional (§8.2).
> 4. Convention (e) lies in \(\mathcal L^{\rm rand}\), which is **disjoint from \(\mathcal L^{\rm tv}\)** whenever the latent centre has positive variance.
> 5. **Exactly three classes exist:** \(\mathcal L^{\rm fix}\subsetneq\mathcal L^{\rm tv}\), and \(\mathcal L^{\rm rand}\cap\mathcal L^{\rm tv}=\emptyset\) off the degenerate case. No further class is produced by (a)–(e).

**Proof.** 1 is ID-4's statement applied at the pair \((m_Q,c(Q))\).

2 and 3 (strictness \(\mathcal L^{\rm fix}\subsetneq\mathcal L^{\rm tv}\)): suppose a time-varying change coincided with some fixed \(\Phi_{x\to y}\). Work in a totally geodesic flat (permitted by ID-4's own sufficient geometry), where \(\Phi_{x\to y}(v)=v+(x\ominus y)\) is translation by a constant vector. Equality for every \(t\) forces \(\mu(u_t)\ominus\nu(u_t)\) to be the same vector for all \(t\); i.e. the base-point offset is constant. Contradiction with the hypothesis that it is not. \(\square\)

4: in \(\mathcal L^{\rm tv}\) the centre process is deterministic, so \(\mathrm{Var}(\nu(u))=0\) for every \(u\); in \(\mathcal L^{\rm rand}\) with a nondegenerate latent centre it is positive. Disjointness follows. This is the quantitative version of P1-ID-A §5 item 5: *"a time-constant random variable \(Z\) cannot be inserted into a deterministic centre curve."*

5: (a) gives the base representation; (b),(c) give deterministic points or paths, hence \(\mathcal L^{\rm fix}\) or \(\mathcal L^{\rm tv}\); (d) gives a deterministic path, hence \(\mathcal L^{\rm tv}\); (e) gives a random path, hence \(\mathcal L^{\rm rand}\). No convention in the list produces anything else. \(\square\)

**Answer to "does (e) produce a new class, and is it the same class C is constructing in R3?"**
* *New class*: **yes**, \(\mathcal L^{\rm rand}\), proved disjoint from both deterministic orbits.
* *Same as R3*: **yes by classification** — R3 is defined in the lead ledger as the latent-stochastic-centre route, which is exactly escape (E2) with orbit \(\mathcal L^{\rm rand}\). Whether that class is *nonempty in the FDD-equivalent sense* (i.e. whether two admissible latent-centre models can share every FDD, per L-9.R3.3) is C's node and is **SEPARATED to C**. My node terminates with the classification: (e) is escape route (E2), its orbit is \(\mathcal L^{\rm rand}\), and \(\mathcal L^{\rm rand}\) is disjoint from \(\mathcal L^{\rm fix}\cup\mathcal L^{\rm tv}\).

**A consequence with teeth (do not bury this).** ID-4 **disproves** generic fixed-rank preservation under a chart change (the \(S^2\) reset-chain example: minimum rank one at \(x\), minimum rank two at \(y\)). Since (b) and (c) are chart changes, it follows that:

> Refitting Paper 1 with a *median* centre instead of a *mean* centre is **not** a robustness check. The two fits can report a different number of dynamic factors for a reason that is pure geometry and has nothing to do with the data's factor structure. Any such comparison must first verify ID-4's flat/geodesic hypotheses, exactly as Paper 1's identification precondition 6 already requires for fixed-anchor comparisons.

**Status: PROVED (classification) + SEPARATED (R3 nonemptiness to Workstream C).**

### 8.4 L-9.R4.4 — does (d) change the estimand, and is Paper 1 compatible?

**Estimand.** Yes, (d) changes the estimand, proved in §8.2(A): \(\widetilde{\hat\mu}_\lambda(u_0)\ne\tilde m(u_0)\) with the explicit Green's-function example. A regularised centre is a *smoothed* population target: it bakes a bias–variance tradeoff into the estimand rather than into the estimator. For a fixed \(\lambda>0\) it is a genuinely different scientific object; for \(\lambda=\lambda_n\to0\) at a suitable rate it is an estimator design for the *unregularised* target, which is a legitimate but entirely different claim requiring its own rate theorem.

**Paper 1 compatibility: NO, not as declared.** Three specific incompatibilities:

1. **HD-M** states "*The proxy laws have Fréchet mean \(\mu_n(u)\)*". Under (d), \(\hat\mu_\lambda(u)\) is not the Fréchet mean of \(Q_u\), so HD-M is false as written.
2. **Paper 1's model equation** \(X_{t,n}=\operatorname{Exp}_{\mu_n(u_t)}[\mathcal P A_nf_{t,n}+\delta_{t,n}]\) with pointwise-centred score requires \(\mathbb E\operatorname{Log}_{\mu_n(u)}X^{(u)}_t=0\). Under (d) the score mean is \(\ne0\) by exactly the Green's-function displacement.
3. That nonzero score mean is precisely ID-5's \(b_{t,n}\ne\log_{c_0}\mu(u_t)\) contamination. By P1-ID-A §9 equation (9.1) it enters the fitted lag row as a \(d\otimes d\) drift operator that can **change rank** (orthogonal drift), **change eigenstructure without changing rank** (aligned drift), or **be invisible at a selected lag** (the \(\cos(\pi t/2h_0)\) example). So adopting (d) without re-declaring the estimand reproduces exactly the fixed-centre contamination ID-5 exists to warn about.

**Recommendation to the lead:** if Paper 1 ever wants (d), it must (i) re-declare the estimand as \(\mu_\lambda\), (ii) restate HD-M in terms of \(\mu_\lambda\), and (iii) carry the ID-5 nine-term budget for the residual \(\mu_\lambda-\mu\). Nothing less suffices.

**Status: PROVED.**

---

## 9. Recommended canonical edits (for the lead; nothing here has been applied)

Every item below is a place where a result in this dossier contradicts or refines an existing canonical statement.

| # | Canonical location | Current text | What this dossier proves | Recommended action |
|---|---|---|---|---|
| E1 | **HD1 §1 (HD-M)** | "The actual and proxy rows are \(m_0\)-dependent for one fixed \(m_0\)." | The \(L^2\)/GRID/PF/OBS/HD-E chain consumes only (i) a *second-moment* weighted bound on the frozen score (\(\psi^+\)) and (ii) a *fourth-moment* product-covariance bound for the oracle row. \(m_0\)-dependence is strictly stronger than either. HD1's own Lemma 4.1 shows this: (4.1) is a covariance identity; the residue-class split appears only in (4.2). | Split HD-M's dependence clause into a **mean-channel** condition and a **row-channel** condition; state that the residue-class device has exactly one consumer, the sup-norm branch. |
| E2 | **HD1 §2 / Paper 1 "Dimension-free mean results"** | \(\ell_n=b_n^3+(nb_n)^{-1/2}+n^{-a}+n^{-1}\) | The \((nb_n)^{-1/2}\) is not universal; it is \(\psi^+(nb_n)\), the frozen score's ergodic-average modulus, and equals \((nb_n)^{-1/2}\) exactly under a finite-memory/summable budget **with positive long-run variance** (L-7.1b/c). | Display \(\ell_n(\psi)\) as the general form with \((nb_n)^{-1/2}\) as the short-memory special case; note the \(\Lambda_u>0\) proviso. |
| E3 | **HD1 §4 / Paper 1 "Final robust loading theorem"** | "Balancing the first two terms gives \(\alpha=1/7\) and \(\ell_n=O(n^{-3/7})\) when \(a\ge3/7\)." | The balance is persistence-specific: \(\alpha=(1-2d)/(7-2d)\), rate \(n^{-3(1-2d)/(7-2d)}\). The headline requires \(d=0\) **and** \(\theta=0\) exactly. | Add a displayed persistence proviso to the headline. |
| E4 | **HD1 §1 (HD-M) design clause \(a\ge3/7\)** | treated as a primitive | \(a\ge3/7\) is a *design constant* tied to \(b_n=n^{-1/7}\) and the \(d=\theta=0\) headline, not a primitive. Under varying near-unit-root persistence, \(a=1-\theta\) is *induced*, and the correct requirement \(a\ge3\alpha\) is automatically satisfied. Reading it as a primitive yields the over-strict \(\theta\le4/7\). | State \(a\ge3\alpha\) (rate-matching) as the requirement, with \(a\ge3/7\) as its value at the design point. |
| E5 | **Application map T-APP-4 (C-PD)** | "uniform summable \(L^2\) and essential-sup innovation effects" | Correct as stated, but does **not** cover any \(d>0\): \(\delta_2(k)\asymp k^{d-1}\) is non-summable. The entire ID-10 window \(d\in(0,1/2)\) is currently outside every stated repository dependence assumption. | Add a row for the \(\psi\)-indexed mean channel; mark the long-memory row as covered by ID-7 (HD-M-\(\psi\)) plus L-7.3.4's cumulant condition, and by nothing else. |
| E6 | **Paper 1, identification precondition 5** | "One-path mean recovery is pointwise under the no-zero-frequency-atom condition ... No theorem is uniform over persistence approaching frequency zero." | ID-7 now supplies exactly that uniform theorem, on the \(\psi\)-indexed class, with the exact boundary \(x_n=(1-\rho_n)nb_n\to\infty\). This discharges the obligation P1-ID-A §8 explicitly left open. | Add (S5-\(\psi\)) as the quantitative version, and record the exact boundary. |
| E7 | **HD1 §2 (G1-HD, HD-Minf)** | stated alongside G1-HD-L2 | The sup-norm branch and HD-Minf **do not survive** any \(d>0\) or \(\theta>0\) with the current proof, because the residue-class device is unavailable (L-7.3.5). HD-E does not consume them. | Add a scope note: the sup-norm branch is short-memory-only; a long-memory version would need a new maximal inequality (Wiener-chaos route), not a repair. |
| E8 | **References audit §1 (APP-FIN row)** | describes APP-FIN without a persistence check | §7's diagnostic: \(x_{\rm eff}\approx2.7\) at \(d=0.40\), \(n=240\), \(b_n=n^{-1/7}\); rate-optimal bandwidth covers 84% of the sample. | Add the persistence diagnostic and repeat ID-6's sensitivity-only wording. |
| E9 | **Lead ledger, R4 row** | "declared-convention escape: which alternative centre conventions are admissible and genuinely distinct" | R4 is **not** an escape (R4-EXH). Exactly one new deterministic equivalence class \(\mathcal L^{\rm tv}\) appears; (e) gives \(\mathcal L^{\rm rand}\) = R3's class. The escape space is exhausted by (E1)+(E2). | Record R4 as `DISPROVED as an escape` with the classification result attached, and record R4-EXH as a campaign-level closure argument for the R-route space. |

**No result in this dossier contradicts ID-0–ID-6.** ID-7 is a positive companion to ID-3 that lives on a proper subclass; §4 proves the two share a boundary with no gap.

---

## 10. Numerical checks (discovery and diagnostic only — no status assigned)

| # | What was checked | Method | Outcome |
|---|---|---|---|
| C1 | AR(1) closed form (1.1) | `sympy`: exact evaluation of \(\sum_{s,t=1}^N\rho^{|s-t|}\), symbolic subtraction from the candidate | difference simplifies to \(0\) for \(\rho\ne1\); candidate exact |
| C2 | scaling profile \(\Psi(x)=2(x-1+e^{-x})/x^2\) | \(N=2\times10^5\), \(\rho=1-x/N\), \(x\in\{0.1,1,10\}\) | \(0.9674836\) vs \(0.9674836\); \(0.7357584\) vs \(0.7357589\); \(0.1799969\) vs \(0.1800009\) |
| C3 | long-memory exponent and constant | exact ARFIMA\((0,d,0)\) ACF, \(N\in\{500,\dots,8000\}\), \(d\in\{0.1,0.25,0.4,0.45\}\) | empirical exponents \(0.4000,0.2500,0.1000,0.0500\) = \(1/2-d\); constant at \(d=0.4\): \(0.966\) numeric vs \(0.9657\) from \(\{\Gamma(1-d)/(\Gamma(d)d(2d+1))\}^{1/2}\) |
| C4 | \(a=1-\theta\) for the tvAR(1) array | exact MA\((\infty)\) coefficient difference, \(g(u)=1+0.8\sin2\pi u\), \(n\in\{2000,\dots,32000\}\) | \(\theta=0.3\): empirical exponent \(0.677\to0.697\) (target \(0.700\)); ratio to \(n^{-0.7}\) constant at \(9.7\). \(\theta=0.5\): \(0.393\to0.467\) (target \(0.500\)), monotone |
| C5 | APP-FIN diagnostic table (§7.3) | exact (1.1) and exact ARFIMA ACF at \(n=240\), \(b_n=n^{-1/7}\) | as tabulated; design check \(\psi/b_n^3=1.00\) at \(d=0\) confirms the \(n^{-1/7}\) balance |

---

## 11. External citation record

| Source | Exact locus | Exact hypotheses used | Line-by-line application | What is **not** imported |
|---|---|---|---|---|
| Dahlhaus, R., Richter, S., Wu, W. B. (2019), "Towards a general theory for nonlinear locally stationary processes," *Bernoulli* 25(2), 1013–1044 (arXiv:1704.02860) | **Assumption 2.1 (Stationary approximation), condition (S1)**, quoted verbatim in §5.3 | \(q>0\); triangular array \(X_{t,n}\); for each \(u\) a stationary ergodic \(\tilde X_t(u)\); \(\sup_u\|\tilde X_t(u)\|_q<\infty\); \(\exists\,1\ge\alpha>0,C_B>0\) with \(\|\tilde X_t(u)-\tilde X_t(v)\|_q\le C_B|u-v|^\alpha\) and \(\|X_{t,n}-\tilde X_t(t/n)\|_q\le C_Bn^{-\alpha}\), uniformly in \(t,u,v\) | \(q=2\); \(\sup_u\|\tilde X_t(u)\|_2=1\) ✓; first display verified with \(\alpha=1\), \(C_B=C(\|g'\|_\infty,\underline g)\); second display verified with \(\alpha=1-\theta\) and no larger, by Proposition L-10.2b; common \(\alpha=1-\theta\) | **Only the mode of local stationarity is cited.** No rate, no uniformity, no CLT, no bias expansion, and no triangular-array conclusion is taken from DRW. The exponent identification \(a=1-\theta\) is proved internally. This is exactly the discipline C-AUDIT-8 requires. |
| Doob, J. L. (1953), *Stochastic Processes*, Wiley, Ch. X §7 | mean-square ergodic theorem | centred, square-integrable, weakly stationary Hilbert process; unitary shift on the generated \(L^2\)-span | used only through P1-ID-A §6, i.e. only for the *qualitative* limit \(\psi_u(N)\to\nu_u(\{0\})^{1/2}\) in §1.1 | **No rate.** Every rate in this dossier comes from the exact Cesàro identity L-7.1.0, which is elementary and internal (C-AUDIT-6 discipline). |
| Andersen, T. G., Bollerslev, T., Diebold, F. X., Labys, P. (2003), "Modeling and Forecasting Realized Volatility," *Econometrica* 71(2), 579–625 | Table 2 (last column) and the Robinson multivariate estimate | GPH log-periodogram regression, \(m=[T^{4/5}]=514\) ordinates, asymptotic s.e. \(0.028\); Robinson (1995) multivariate extension | supplies the *diagnostic input* \(d\approx0.39\)–\(0.43\) (common \(\hat d=0.401\)) for **daily log** realised volatility, §7.4 | **Diagnostic only.** No analytic status in this dossier depends on it. The daily\(\to\)monthly and log-RV\(\to\)BW-score transfers are flagged with their own caveats. |
| Chambers, M. J. (1998), "Long Memory and Aggregation in Macroeconomic Time Series," *International Economic Review* 39(4), 1053–1072 | conclusion on temporal aggregation | aggregated series retains the order of integration | used only as an indicative transfer for daily\(\to\)monthly in §7.4 | **CITED, not verified in depth; not load-bearing.** Chambers's own empirical estimates diverge from the theory; recorded as such. |
| Geweke, J., Porter-Hudak, S. (1983); Robinson, P. M. (1995) | estimator provenance | — | recorded because ABDL's numbers are estimator-specific | no independent use |
| T-APP-4 (Application map), display (3.3) | causal Hilbert Bernoulli shift, martingale projection | uniform summable \(L^2\) innovation effects \(\Delta_2<\infty\) | applied with \(a_t=1/N\) in L-7.1c | this is an **internal** repository result (APP-C §3), not an external citation |

---

## 12. Claim table (return format)

| Node | Exact statement | Assumptions | Conclusion | Status | Proof location | Known weak point |
|---|---|---|---|---|---|---|
| L-7.1.0 | \(\psi_u(N)^2=N^{-2}\sum_{s,t\le N}\operatorname{tr}\Gamma_u(s-t)=\int|D_N|^2d\nu_u\) | centred, \(L^2\), weakly stationary in \(H\) | exact identity; \(\psi_u(N)\to\nu_u(\{0\})^{1/2}\) | **PROVED** | §1.1 | none; it is P1-ID-A §6 restated |
| L-7.1a | \(\psi(N)^2=N^{-2}[N\frac{1+\rho}{1-\rho}-\frac{2\rho(1-\rho^N)}{(1-\rho)^2}]\) | Hilbert AR(1), \(\operatorname{tr}\Gamma(0)=1\), \(0<\rho<1\) | lead's formula exact; \(\psi^2\approx N^{-1}\frac{1+\rho}{1-\rho}\) when \(N(1-\rho)\gg1\) | **PROVED** | §1.2 | requires \(\rho>0\); \(\rho<0\) reverses the sign pattern (then \(\psi\le\psi^+\) strictly) |
| L-7.1a′ | \(\psi(N)^2\to\Psi(x)=2(x-1+e^{-x})/x^2=2\int_0^1(1-y)e^{-xy}dy\), \(x=N(1-\rho)\); \(\Psi(0)=1\), strictly decreasing | \(N\to\infty,\rho\uparrow1,N(1-\rho)\to x\) | exact interpolating profile; \(\psi\asymp1\) iff \(x=O(1)\) | **PROVED (new)** | §1.3 | a limit statement; finite-\(N\) constants not tracked (bounds \(\min\{1,2/x\}\) are) |
| L-7.1b | \(\psi(N)\le\sqrt{(2m_0+1)R^2/N}\); \(\asymp N^{-1/2}\) **iff** \(\Lambda_u=\sum_h\operatorname{tr}\Gamma_u(h)>0\) | \(m_0\)-dependence uniform in \(u\) | lead's unconditional \(\asymp N^{-1/2}\) is **false**; upper bound unconditional | **REFORMULATED+PROVED** | §1.4 | counterexample \(Z_t=e_t-e_{t-1}\) gives \(\psi=\sqrt2/N\) |
| L-7.1c | \(\psi(N)\le\Delta_2N^{-1/2}\); two-sided iff \(\Lambda_u>0\) | causal Hilbert Bernoulli shift, \(\Delta_2<\infty\) (two-sided clause needs \(\sum_kk\delta_2(k)<\infty\)) | T-APP-4 budget \(\Rightarrow\) (S5) | **REFORMULATED+PROVED** (upper: CITED+APPLIED, T-APP-4) | §1.5 | two-sided clause needs the stronger weighted summability |
| L-7.1d | \(\psi_u(N)^2=\frac{c_\gamma(u)}{d(2d+1)}N^{-(1-2d)}\{1+o(1)\}\) | \(\operatorname{tr}\Gamma_u(h)=c_\gamma(u)|h|^{2d-1}\{1+o(1)\}\), \(d\in(0,1/2)\), \(c_\gamma\) uniformly bounded above/below | \(\psi(N)\asymp N^{-(1/2-d)}\); ARFIMA constant \(\{\Gamma(1-d)/(\Gamma(d)d(2d+1))\}^{1/2}\) confirmed | **PROVED** | §1.6 | needs the tail constant uniform in \(u\); \(d=0\) boundary not covered by this display (use L-7.1b/c) |
| L-7.1e | \(\psi\le\psi^+\), equality when \(\operatorname{tr}\Gamma\ge0\) | — | \(\psi^+\) is the estimator-relevant modulus | **PROVED** | §1.7 | for sign-changing \(\operatorname{tr}\Gamma\), \(\psi^+\) can be strictly larger, so ID-7 is then conservative |
| L-7.3.1 | \(\|\sum_tw_t\xi_t\|_{L^2}\le C_2\psi^+(N)\); \(\ge c\psi(N)\) under \(\operatorname{tr}\Gamma\ge0\) + regular variation | \(w\ge0\), \(\sum w=1\), \(\max w\le C_2/N\), support in a window of length \(N\) | kernel weights are equivalent to uniform ones, up to kernel constants | **PROVED** | §2.2 | lower bound needs \(\operatorname{tr}\Gamma\ge0\) and regular variation; the narrowest stage \(c_3=1/4\) sets the modulus |
| L-7.3.2 | \(\ell_n(\psi)=b_n^3+\psi^+(nb_n)+n^{-a}+n^{-1}\); reduces verbatim to HD1's \(\ell_n\) under HD-M | HD-G, HD-X, (HD-M-\(\psi\)), HD-M2, HD-K, Theorem X smoothness | \(\psi^+(nb_n)\) sits exactly where \((nb_n)^{-1/2}\) sits, and nowhere else in the mean channel | **PROVED** | §2.3 | the bias channel still needs \(C^3\) marginal-law smoothness in \(u\), untouched by \(\psi\) |
| L-7.3.3 | GRID, PF, OBS, P1-ROW, P1-OP, EV, Davis–Kahan hold with \(\ell_n\to\ell_n(\psi)\) | \(\ell_n(\psi)\to0\) | (HD-E-\(\psi\)) | **PROVED** | §2.4 | PF's \(M_n\ell_n^2=O(\ell_n^{4/3})\) is identity-level, so it is safe; TAU's admissible \(\tau_n\) window narrows |
| L-7.3.4 | \(d_{\rm or,n}=O_p(n^{-1/2}+n^{-(1-2d)})\); \(n^{-1/2}\sqrt{\log n}\) at \(d=1/4\) | HD-L; Gaussian factor with \(|\gamma_f(h)|\le C(1+|h|)^{2d-1}\); white \(\varepsilon\) independent of \(f\) | oracle row degrades but is **strictly dominated** by \(\ell_n(\psi)\) at every re-optimised bandwidth | **PROVED** (Gaussian class) | §2.5 | non-Gaussian case needs the stated fourth-cumulant summability, assumed not proved |
| L-7.3.5 | residue-class split has no long-memory analogue; G1-HD/HD-Minf die; HD-E does not consume them | \(\operatorname{tr}\Gamma(h)\asymp|h|^{2d-1}\), \(d>0\) | device DISPROVED as available; consumer SEPARATED | **DISPROVED + SEPARATED** | §2.6 | a long-memory sup-norm theorem remains genuinely unavailable (would need a Wiener-chaos maximal inequality) — declared out of scope with a boundary reason |
| **L-7.2 (ID-7)** | under (S1)–(S5): \(\mu\) and \(E\) separately identified from \(\mathcal I_J\) **and** separately estimable at \(\ell_n(\psi)\) and \((d_{\rm or,n}+\ell_n(\psi))/\Delta_n\) | (S1) \(C^3\) deterministic centre; (S2)+(S2b) frozen weak stationarity, \(\psi^+\), Hölder in \(u\); (S3) HD-M2; (S4) ID-2 frozen conditions; (S5) HD-K + \(\psi^+(nb_n)=o(1)\) | constructive companion to ID-0–ID-6, attained by the project's own estimator | **PROVED** | §3 | (S2b) is an extra primitive relative to HD1 as written — but it is already mandated by P1-ID-A §12 AC-5 and is DRW Assumption 2.1(S1)'s first display |
| L-7.4 | \(x_n=(1-\rho_n)nb_n\); ID-7 holds iff \(x_n\to\infty\); ID-3's floor bites iff \(x_n=O(1)\); both governed by the same \(x\) | flat scalar Gaussian AR(1) window | positive theorem and impossibility meet exactly, no gap; ID-3's construction misses by \(n^{8/7}\) | **PROVED** | §4 | the two-point lower bound is for the scalar Gaussian subfamily; it lower-bounds the sup over any larger class |
| L-10.1 | \(\alpha(d)=(1-2d)/(7-2d)\); rate \(n^{-3(1-2d)/(7-2d)}\); HD-K and HD-M slack | \(\psi^+(N)\asymp N^{-(1/2-d)}\), \(b_n=n^{-\alpha}\) | **lead's algebra exactly confirmed**; window \(d\in[0,1/2)\); headline iff \(d=0\) | **PROVED** | §5.1 | the whole window \(d>0\) lies outside HD-M and T-APP-4 as currently written (canonical gap E5) |
| L-10.2a | constant persistence: consistency iff \(\theta<1-\alpha\); at \(\alpha=1/7\), \(\theta<6/7\); optimal \(\alpha=(1-\theta)/7\), rate \(n^{-3(1-\theta)/7}\) | \(\rho_n=1-n^{-\theta}\) constant in \(u\) | **lead's \(\theta<6/7\) exactly confirmed** | **PROVED** | §5.2 | assumes exact stationarity, so HD-M2 is vacuous here |
| L-10.2b | tvAR(1) array with \(\rho(u)=1-n^{-\theta}g(u)\), unit marginal variance: \(a=1-\theta\) **exactly and sharply** | \(g\in C^2\), \(0<\underline g\le g\le\bar g\), \(g'\not\equiv0\); same-innovation coupling | lead's \(a\approx1-\theta\) confirmed and upgraded to sharp; array satisfies DRW Assumption 2.1(S1) with \(q=2\), \(\alpha=1-\theta\), no larger | **PROVED** (internal) + **CITED+APPLIED** (DRW mode) | §5.3 | proved for the scalar Gaussian tvAR(1); the manifold-valued statement needs the flat/tangent reduction, which is (S1)+HD-G |
| L-10.2c | \(a\ge3/7\Rightarrow\theta\le4/7\) is arithmetically right but not the binding constraint; self-consistent window is \(\theta<1\) | \(a=1-\theta\) induced | \(a\ge3/7\) is a **design constant**, not a primitive; \(a=1-\theta=\frac73\times\)rate exponent, never binds | **REFORMULATED+PROVED** | §5.4 | requires reading HD-M's \(a\ge3/7\) as derived; if the lead insists it is primitive, \(\theta\le4/7\) stands |
| L-10.3 | window nonempty (explicit \(m_0\)-dependent witness); ID-3's floor binds in both nontrivial regimes; HD-K never binds; \(\theta=2\) excluded by a full unit of exponent | as tabulated in §6.2 | final window displayed in §6.3; headline iff \(d=\theta=0\) | **PROVED** | §6 | the two persistence families are treated separately; a joint \((d,\theta)\) model is not analysed (no consumer needs it) |
| L-10.4 | APP-FIN: \(n=240\), \(b_n=n^{-1/7}\Rightarrow nb_n=110\), \(b_n^3=0.0955\); at \(d=0.40\), \(\psi=0.604\), \(\psi/b_n^3=6.3\), \(x_{\rm eff}=2.7\); rate-optimal \(b_n=0.838\) | ABDL (2003) \(\hat d=0.401\) (common), Table 2 \(0.387/0.413/0.430\), s.e. \(0.028\) | formally **inside** the asymptotic window, on the degenerate edge; **diagnostically adverse** at \(n=240\) | **PROVED as computation; DIAGNOSTIC as application claim** | §7 | daily\(\to\)monthly transfer (Chambers) and log-RV\(\to\)BW-score Hermite-rank transfer are both caveated; the rank-2 case gives \(d_{\rm eff}=0.30\), \(x_{\rm eff}=7.3\) |
| L-9.R4.1 | any marginal-functional, isometry-equivariant, single-valued convention equals the unique fixed point of \(G_Q\) on \(\mathcal Q_{\rm rig}\); \(m_Q\in\mathrm{Fix}(G_Q)\) when unique | \(Q\in\mathcal Q_{\rm rig}\); \(c(Q)\) defined and single-valued | mean, median, trimmed and all \(M\)-centres agree on \(\mathcal Q_{\rm rig}\); differ off it | **PROVED** | §8.1 | requires existence/uniqueness as hypotheses; says nothing about laws with empty argmin |
| L-9.R4.1′ | exact separations off \(\mathcal Q_{\rm rig}\): \(\mathbb R\) two-point (mean \(1/4\), median \(0\)); great-circle two-point; **and \(S^2\) antipodal: mean argmin = equator (dim 1), median argmin = \(S^2\) (dim 2)** | as displayed | conventions have **different failure geometries**, not merely different selections | **PROVED (curved example new)** | §8.1 | the \(S^2\) example is degenerate by design; that is the point |
| L-9.R4.2 | (d) is not a functional of each marginal (explicit Neumann Green's function \(G>0\)); but \(\{Q_u\}=\mathcal I_M\), so (d) is an \(\mathcal I_M\)-functional and stays pinned at the family level | \(M=\mathbb R\), \(\mathcal C=H^1\), \(\lambda>0\) | ID-1 fails pointwise for (d) but the gate holds at the family level | **PROVED** | §8.2 | proved in the flat case; the curved case needs a convexity/uniqueness hypothesis on \(\mathcal C\), stated not proved |
| **R4-GATE** | any single-valued centre convention that is a measurable functional of the declared information set is pinned by that information set; the only escapes are (E1) empty/nonsingleton argmin with a non-\(\iota\)-measurable selector, and (E2) not a functional of \(\iota\) | \(c=\Psi\circ\iota\) | **ID-1 is a corollary** (\(\mathcal I=\mathcal I_M\)) | **PROVED** | §8.2 | the theorem is trivial; its content is the exhaustiveness corollary |
| **R4-EXH** | R1,R2 \(\subset\) (E1); R3 \(\subset\) (E2); **R4 is not an escape**; R5 is estimation, hence separated | R4-GATE | the campaign's population escape space is **exhausted**; no sixth route exists | **PROVED** | §8.2 | assumes the lead ledger's definitions of R1–R5, which are quoted |
| L-9.R4.3 | exactly three chart classes: \(\mathcal L^{\rm fix}\subsetneq\mathcal L^{\rm tv}\), \(\mathcal L^{\rm rand}\cap\mathcal L^{\rm tv}=\emptyset\); (b),(c) covered by ID-4 in the fixed-centre model but generically in \(\mathcal L^{\rm tv}\) in the moving-centre model; (d) in \(\mathcal L^{\rm tv}\); (e) in \(\mathcal L^{\rm rand}\) = R3's class | ID-4's declared branch/support hypotheses; flat reduction for the strictness proof | **one new deterministic class only**; no multiplication of conventions | **PROVED** + **SEPARATED** (R3 nonemptiness to C) | §8.3 | strictness proved in a flat; the curved strictness follows from ID-4's own \(S^2\) example but is not re-proved here |
| L-9.R4.4 | (d) changes the estimand (explicit \(\widetilde{\hat\mu}_\lambda(u_0)>0=\tilde m(u_0)\)); Paper 1 as declared is **incompatible** with (d) via HD-M, the pointwise-centring model equation, and ID-5's \(d\otimes d\) term | as in §8.2(A) | (d) requires re-declaring the estimand, restating HD-M, and carrying the ID-5 nine-term budget | **PROVED** | §8.4 | \(\lambda=\lambda_n\to0\) is a different (estimator-design) claim, not analysed |

---

## 13. Adjudication notes for the lead (12 lines)

1. **ID-7 separation condition (one line).** \(\psi^+(nb_n)=o(1)\), where \(\psi^+(N)=\sup_u\{N^{-2}\sum_{s,t\le N}|\operatorname{tr}\Gamma_u(s-t)|\}^{1/2}\) is the frozen tangent score's absolute ergodic-average modulus; it enters \(\ell_n\) exactly in place of \((nb_n)^{-1/2}\) and nowhere else in the mean channel, and HD1's own \(m_0\)-dependence already implies it.
2. **ID-10 window (one line).** \(d\in[0,1/2)\) with \(b_n=n^{-(1-2d)/(7-2d)}\) and rate \(n^{-3(1-2d)/(7-2d)}\); \(\theta\in[0,1)\) with \(b_n=n^{-(1-\theta)/7}\), rate \(n^{-3(1-\theta)/7}\) and induced \(a=1-\theta\); HD-K never binds; the headline \(n^{-3/7}\) holds **iff \(d=0\) and \(\theta=0\) exactly**.
3. **APP-FIN verdict (one line).** Formally inside the window but on its degenerate edge (\(d\approx0.40\) from ABDL 2003 gives rate \(n^{-0.10}\)); the finite-sample diagnostic at \(n=240\), \(b_n=n^{-1/7}\) gives \(\approx2.7\) effective independent factor draws per smoothing window and a stochastic/bias ratio \(\approx6\) — the drift/factor separation is **not empirically resolvable** on that dataset, which is a diagnostic, not a theorem.
4. **R4 verdict (one line).** R4 is **not an escape**: every convention (a)–(d) is a functional of \(\mathcal I_M\); exactly one new deterministic equivalence class appears (\(\mathcal L^{\rm tv}\), time-varying chart), (e) gives \(\mathcal L^{\rm rand}\) = C's R3 class, and R4-GATE proves the escape space is exhausted by (E1)+(E2), so R1/R2/R3 are the only population routes and R5 is estimation.
5. **Contradiction 1 (HD1).** HD-M's \(m_0\)-dependence is **strictly stronger than any HD-E consumer needs**: the \(L^2\) chain needs only a second-moment weighted bound (\(\psi^+\)), the row needs only a product-covariance bound; HD1's own Lemma 4.1 proves this, since the residue-class device appears only in the exponential-tail display (4.2).
6. **Contradiction 2 (HD1 / Paper 1).** The displayed \((nb_n)^{-1/2}\) in \(\ell_n\) is not universal and is not even sharp for \(m_0\)-dependence: it requires the long-run variance \(\Lambda_u=\sum_h\operatorname{tr}\Gamma_u(h)>0\); \(Z_t=e_t-e_{t-1}\) gives \(\psi=\sqrt2/N\). The lead's L-7.1(b) as dispatched was therefore **wrong as stated** and is reformulated.
7. **Contradiction 3 (HD1).** \(a\ge3/7\) is a design constant tied to \(b_n=n^{-1/7}\), not a primitive; the correct requirement is \(a\ge3\alpha\), which the induced \(a=1-\theta\) always satisfies. The lead's \(\theta\le4/7\) is arithmetically right but answers the wrong question.
8. **Contradiction 4 (Application map).** T-APP-4's summable physical dependence covers **no** \(d>0\); the entire ID-10 long-memory window is currently outside every stated repository dependence assumption, and (HD-M-\(\psi\)) plus L-7.3.4's cumulant condition is the minimal replacement.
9. **Contradiction 5 (HD1 §2).** The sup-norm branch G1-HD and the HD-Minf coupling **do not survive** long memory with the current proof; the residue-class device is proved unavailable. HD-E does not consume them, so this is a separation, not a hole — but it must be displayed.
10. **What ID-7 buys.** ID-1+ID-2 pin the objects in population; ID-3 says one-path recovery is pointwise and **not uniform**; ID-7 supplies the quantitative, uniform, sample-size-indexed replacement that A7 §8 explicitly left open, and proves the project's own three-scale polygonal estimator attains it.
11. **Sharpness is exact, not asymptotic-only.** \(\psi(N)^2\to\Psi(x)=2(x-1+e^{-x})/x^2\) with \(x=(1-\rho)N\), and the Fisher information is \(I_N=(x+2\rho)/(1+\rho)\): the achievable variance and the information floor are governed by the **same scalar**, so the positive theorem and ID-3's impossibility share a boundary with no gap; ID-3's \(\rho_n=1-n^{-2}\) misses it by the polynomial factor \(n^{8/7}\) at every admissible bandwidth.
12. **One warning to carry into the canonical text.** By ID-4's disproof of generic rank preservation, a median-centred or trimmed-centred refit is **not** a robustness check of the mean-centred fit: it can report a different number of dynamic factors for purely geometric reasons, and Paper 1's identification precondition 6 must be extended to cover centre-convention changes, not only fixed-anchor comparisons.
