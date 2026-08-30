# P1-RANK — weak dynamic factors and lag-rank selection literature bridge

You are the **focused primary-source literature auditor and theorem-positioning
researcher** for the Riemannian Factor Dynamics project. This is a bounded
literature-and-analysis task. It is not a numerical experiment, code task,
new proof campaign, or invitation to redesign Paper 1.

## Objective

Determine exactly how the internally proved AR(1) signal-to-lag-operator
bridge relates to established work on dynamic-factor rank selection, weak
factors, lag-autocovariance operators, eigenvalue thresholding, eigenvalue
ratios, and detection boundaries. Produce a citation-safe audit that tells
the lead which parts are standard, which are adaptations, which appear
project-specific because the tangent coordinates are estimated geometrically,
and which novelty claims must not be made.

The internal theorem is already proved. You are auditing its external
position and its connection to the project's existing theorems. Do not run
simulations, numerical checks, notebooks, or code.

## Read before searching

Read completely:

1. `notes/proofs/P1-RANK — AR1 signal strength and threshold boundary.md`;
2. `notes/proofs/HD1 — growing-dimension Paper 1 proof dossier.md`, especially
   HD-L, §3, P1-OP-HD, EV, TAU, and HD-E;
3. `notes/canonical/Paper 1 — Locally stationary Riemannian factor model.md`,
   especially the signal, factor-number, and P-RATIO sections;
4. `notes/canonical/notation-map.md`;
5. `notes/literature/References and external claim audit.md`;
6. `notes/literature/Literature review — external positioning and prior art.md`;
7. the local parent paper `reference/2607.28385v1.pdf`, especially its model,
   Proposition 3, Eq. (5), Example 1, and Table 2;
8. `reference/AUDIT.md` wherever it discusses the parent's selector and public
   implementation.

Archived proof workstreams are provenance, not status authority. Preserve all
uncommitted work. Do not edit canonical files.

## Internal result to position, not re-assume

For independent stationary AR(1) coordinates with marginal scales \(s_j\),
persistences \(\rho_j\), an isometric loading map, and exact HD-L
factorisation, the internal proposition proves

\[
\lambda_j(\mathbb L)
=s_j^4\sum_{h\in\mathcal H}\rho_j^{2h}
\]

up to decreasing rearrangement. HD1's empirical bounds then give exact
threshold recovery on

\[
d_n^2<\tau_n<\lambda_r(\mathbb L)-\eta_n.
\]

Under a weak-tail amplitude multiplier \(w\), the corresponding operator
signal is multiplied by \(w^4\). Under fixed total factor-scale norm, a
separate rank-dilution denominator appears. The proof note explicitly does
**not** claim minimax necessity or selector optimality.

## Question register

Every item must end as `CITED AND APPLIED`, `COMPARISON ONLY`,
`SCOPE MISMATCH`, `CONTRADICTED`, or `NOT FOUND AFTER DOCUMENTED SEARCH`.
Do not use `plausible`, `probably`, or an uncited novelty claim.

### LIT-R1 — lag-operator population spectrum

Find the closest primary-source derivations of loading-space identification
and factor-number recovery from sums/products of nonzero-lag covariance
operators. Determine whether the exact diagonal AR(1) formula above is
explicit in the literature or merely an elementary specialisation of a more
general theorem. Record the exact model, operator, normalisation, theorem or
proposition number, and whether factors/noise are finite-dimensional,
functional, high-dimensional, stationary, or locally stationary.

### LIT-R2 — weak dynamic factors and minimum signal

Find primary work defining strong, weak, pervasive, localised, or
non-pervasive dynamic factors and state the precise signal quantity used:
loading norm, covariance spike, spectral-density eigenvalue, lag-row singular
value, or lag-operator eigenvalue. Determine whether a fourth-power map from
factor amplitude to a squared lag operator is recognised explicitly. Do not
equate incompatible notions of factor strength.

### LIT-R3 — factor-number selectors

Audit threshold, information-criterion, raw eigenvalue-ratio, and ridged-ratio
results relevant to nonzero-lag factor operators. For each theorem record:

- exact selector;
- candidate-rank range and whether rank zero is allowed;
- weakest-signal/eigengap and adjacent-spectrum assumptions;
- dimension and dependence regime;
- signal and null eigenvalue rates;
- whether the theorem proves consistency or only reports simulation
  performance.

Explicitly compare every raw-ratio result with the repository's P-RATIO
counterexample. A paper using a stronger post-rank or adjacent-spectrum
condition is not contradicted by P-RATIO.

### LIT-R4 — detection lower bounds

Search for information-theoretic or minimax lower bounds for detecting a weak
serial factor, a weak covariance/spectral spike, or distinguishing rank
\(r\) from \(r-1\) in dependent data. State the metric, observation model,
parameter class, and boundary exactly. Decide whether any result can be
legitimately mapped to
\(s_{\min}^4\sum_h\rho^{2h}\) without adding unproved assumptions.

If no applicable lower bound is found, say so after documenting databases,
queries, citation chains, and rejected near-matches. Do not upgrade the
internal sufficient threshold boundary into an impossibility theorem.

### LIT-R5 — estimated-coordinate nuisance layer

Search for factor/rank-selection theorems where the observed rows are first
estimated, aligned, registered, transported, projected, or otherwise
generated by a nuisance estimator. Determine whether a perturbation theorem
of the form

\[
\|\widehat{\mathbb L}-\mathbb L\|\ll\text{spectral margin}
\]

is standard in such two-stage settings, and whether any source covers a
moving manifold centre or polygonally transported tangent coordinates. A
generic Davis--Kahan citation is not evidence that the complete RFD nuisance
construction already exists.

### LIT-R6 — parent-paper scope

Verify against the parent's actual PDF precisely what Proposition 3 proves,
what Eq. (5) uses, what Example 1 verifies about growing dimension and
dependence, and what Table 2 demonstrates numerically. Preserve the project's
existing careful conclusion: the displayed rates alone do not justify the
raw ratio, which is different from claiming practical failure in the
parent's designs.

### LIT-R7 — publication-safe positioning

End with three short lists:

1. statements Paper 1 may safely call standard and cite;
2. statements that are internally proved adaptations and should be described
   as such;
3. statements Paper 1 must not call novel, optimal, necessary, or universal.

Propose at most one compact related-work paragraph and one theorem-note
paragraph. Do not reprioritise Paper 1 around the selector result.

## Source and evidence rules

- Use search engines and citation indices only for discovery. Read the actual
  primary paper before recording a claim.
- Prefer journal/arXiv author manuscripts, official proceedings, and books.
  Reviews may locate sources but cannot carry a theorem claim.
- Record author, title, year, stable URL/DOI/arXiv identifier, exact theorem or
  section, hypotheses, conclusion, and project-specific application.
- Quote sparingly and never infer a theorem from an abstract.
- Distinguish a theorem stated by an author from an algebraic specialisation
  derived internally here.
- Claims about novelty require documented search coverage and must remain
  negative-form, e.g. `we found no prior result combining ...`; never `this is
  the first`.
- A near-match rejected for scope must be recorded with the precise mismatch.
- Do not fabricate bibliographic metadata. If a source cannot be opened or a
  theorem cannot be verified, mark it unverified and do not cite it as a
  producer.

## Write scope and deliverable

Write exactly one dossier:

`notes/literature/P1-RANK — weak dynamic factors and lag-rank literature audit.md`

Do not edit any other file. The dossier must contain:

1. a ten-line executive verdict;
2. the seven-item question register with terminal statuses;
3. a primary-source claim table;
4. theorem-by-theorem mappings into AR1-SIG, AR1-THR, HD1 EV/TAU, HD-E, and
   P-RATIO;
5. rejected near-matches and search coverage;
6. the publication-safe wording requested in LIT-R7;
7. a final distinction between what the literature proves, what this project
   proves internally, and what remains unproved but is **not consumed** by
   Paper 1.

No computation is authorised. No canonical claim changes during this task.
Return only after all seven literature questions have a terminal evidence
status and the dossier has passed a self-audit for exact citations, working
links, scope mismatches, and unsupported novelty language.
