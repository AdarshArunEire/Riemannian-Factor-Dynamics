# RFD paper — session notes

Handoff for the next Claude session. `rfd_spl_draft.tex` is a hidden scaffold:
**do not show it to the author.** Ask questions so their own sentences
rebuild it, then they compare and polish.

## Setup
- Target: IEEE Signal Processing Letters (4 pages + 1 page references).
- Model paper: Maman, Yair, Eytan, Talmon, "Domain adaptation using Riemannian
  geometry of SPD matrices", ICASSP 2019.
- Parent paper: Huang, Chen, Chen, "A Riemannian Factor Model for
  Manifold-Valued Time Series", arXiv:2607.28385. Its assumption (P2), a fixed
  Fréchet mean, is the one RFD drops.
- Author preferences: tutoring mode (author writes, Claude critiques); maths in
  rendered LaTeX (`$...$` / `$$...$$`), never bold plain text.

## Covered so far
- Why tangent spaces can't be compared: inner product depends on base point.
- Parallel transport = a rule for choosing the rotation; it is path-dependent
  on curved manifolds (holonomy).
- Metric → Levi-Civita connection → geodesics and transport. BW was inherited
  from the parent (optimal-transport argument); AIRM is also supported.
- Identification: a slow centre and a persistent factor look alike; bandwidth
  `h` and `n_cells` decide the split (h → ∞ gives RFM, h → 0 gives no factors).
- Orthogonality: tangent dimension d = p(p+1)/2; random drift puts ≈ r/d in the
  factor space (19/210 ≈ 9% for crypto); real drift is likely aligned.
- Alignment test caveats: noise biases toward r/d (if isotropic); the result
  depends on h, so report a curve and build an empirical null.
- Crypto result is formally a tie (Newey–West intervals cross zero).

## Author's drafts so far
Method paragraph (feedback: say *why* tangent spaces differ, why pooling
needs comparability, name the destination frame):
> RFD is a framework for analysing and forecasting covariance data with a
> moving baseline. It is an extension of RFM, where deviations in data exist in
> the tangent space of the Fréchet mean of your data. They therefore assign the
> role of a baseline covariance state to the geometric mean, but RFD proposes
> that baseline can drift over time. The issue with a dynamic centre is the
> tangent spaces are not directly comparable. Parallel transport defines the
> rules for comparing the varying tangent vectors, allowing them to be
> transported along the path the baseline took over time.

Results claim (feedback: add numbers, include fixed-centre case, soften
"does not encode", qualify as in-sample synthetic, name the metric):
> RFD does not encode the centre drift in its factors, while RFM absorbs the
> centre drift it can describe with its factors. Therefore, RFD performs
> (numbers) better in cases where the centre drift is orthogonal to the factor
> space and therefore can't be absorbed by RFM's factors, but loses by (numbers)
> when the centre drift is aligned with the factors.

## Next
1. Q1 (intro): one sentence: what RFM assumes and what happens to drift.
2. Limitations sentences on the alignment test (noise + bandwidth).
3. Then walk the draft in order: abstract, geometry, method, identification,
   experiments, conclusion. Resolve `TODO(author)` items in the .tex.
