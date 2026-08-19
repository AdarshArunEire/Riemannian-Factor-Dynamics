"""Metric calibration, step 2 of 2 -- do we and the parent report the same number?

Reads results/final/parent_bw_reference.csv, produced by R/calib_bw_metric.R
using THEIR geod_BWS_core, and checks our bw_dist2 agrees on the same matrices.

Why this matters more than it looks. The two implementations compute the same
formula by different routes:

    theirs   sqrtm(X) then sqrtm(sqrtm(X) Y sqrtm(X)) via expm::sqrtm, and
             elsewhere sqrtm of the NON-symmetric products X %*% M
    ours     numpy.linalg.eigh on symmetrised inputs throughout

So agreement here is a genuine cross-check, not a tautology -- it is the same
mathematics through two different numerical paths in two different languages
on two different BLAS libraries. Disagreement would mean every comparison
between their results and ours is meaningless, and it is far better to learn
that in five minutes with no data than three weeks in.

SKIPS if the CSV is absent, so the suite still runs before R has been set up.
"""

import csv
from pathlib import Path

import numpy as np
import pytest

from rfd.spd.bw import bw_dist2, trace

REF = Path(__file__).resolve().parents[2] / "results" / "final" / "parent_bw_reference.csv"

pytestmark = pytest.mark.skipif(
    not REF.exists(),
    reason=f"{REF.name} not built yet -- run `Rscript R/calib_bw_metric.R`",
)


def _num(v):
    """R writes NA for NaN. Both mean the parent produced no number."""
    return float("nan") if v in ("NA", "NaN", "NaN ", "") else float(v)


def _load():
    if not REF.exists():
        return []
    with open(REF, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        m = int(r["m"])
        X = np.array([float(v) for v in r["X"].split(";")]).reshape(m, m, order="F")
        Y = np.array([float(v) for v in r["Y"].split(";")]).reshape(m, m, order="F")
        out.append((int(r["case"]), r["tag"], m, float(r["cond"]),
                    _num(r["d2_parent"]), _num(r["d2_imag"]), X, Y))
    return out


def _finite(rows):
    return [r for r in rows if np.isfinite(r[4])]


def test_reference_file_is_sane():
    rows = _load()
    assert len(rows) >= 12
    assert {r[1] for r in rows} == {"generic", "identical", "near"}


def test_no_complex_leakage_in_parent():
    """Their sqrtm runs on non-symmetric products and can return complex
    values -- which is why Re(...) wrappers appear in their Frac_Var_LYB. On
    these inputs it does not. Checked only where they returned a number at
    all; the NaN rows have their own test below."""
    for case, tag, m, cond, d2, d2_imag, X, Y in _finite(_load()):
        assert d2_imag == 0.0, f"case {case} ({tag}, m={m}, cond={cond:.0e})"


def test_parent_returns_nan_on_identical_matrices():
    """A DEFECT IN THEIR CODE, pinned here rather than treated as our failure.

    geod_BWS_core ends `return(sqrt(res))` with

        res = tr X + tr Y - 2 tr (X^(1/2) Y X^(1/2))^(1/2)

    and no clip. When X == Y that is a difference of large traces which should
    be zero and lands slightly NEGATIVE, so sqrt gives NaN. Ours clips at zero
    (np.maximum(d2, 0.0)) and returns a finite value.

    Measured at commit c07d49c: cases 5 and 14 -- identical matrices at
    kappa=1e3, m=3 and m=12. Whether it fires is the luck of the roundoff sign;
    case 11 came back as exactly 0.0 and cases 2, 8, 17 as small positives.

    Where it bites in their pipeline:
      * mean_on_BWS computes loss = mean(geod_BWS(X, mu_new)). One NaN makes
        the mean NaN, so `loss_old - loss < tol` is NA and `if (i > 1 && NA)`
        raises "missing value where TRUE/FALSE needed" -- a hard stop.
      * Frac_Var_bws accumulates geod_BWS_core(x_hat, x_test)^2. A near-perfect
        prediction poisons the whole sum, and predictions get closer to the
        data as the factor count rises -- which their application sweeps to 15.

    This test asserts the SHAPE of the defect: NaNs occur only on identical
    pairs, and we return a finite small number in exactly those places. If a
    future commit fixes it, this test fails and that is the correct signal.
    """
    rows = _load()
    nan_rows = [r for r in rows if not np.isfinite(r[4])]
    assert nan_rows, "parent no longer produces NaN -- check whether they fixed it"
    for case, tag, m, cond, d2, _, X, Y in nan_rows:
        assert tag == "identical", f"case {case}: NaN on a {tag!r} pair, not just identical"
        ours = float(bw_dist2(X, Y))
        assert np.isfinite(ours), f"case {case}: we produced {ours} too"
        assert ours < 1e-9 * float(trace(X) + trace(Y)), f"case {case}: ours = {ours}"


@pytest.mark.parametrize("row", _finite(_load()), ids=lambda r: f"c{r[0]}-{r[1]}-m{r[2]}")
def test_bw_dist2_matches_parent(row):
    """The calibration itself.

    Normalised by tr X + tr Y, never by d2 -- d2 is a difference of large
    traces, so the `identical` and `near` cases have essentially no relative
    accuracy and dividing by them would measure nothing. Same reasoning as
    test_bw.py.

    Tolerance is generous on purpose: this asks whether two independent
    implementations agree to numerical precision, not whether either is
    accurate to its own noise floor. A real discrepancy would be orders of
    magnitude larger, not marginally over a tight bound.

    Measured at commit c07d49c: worst disagreement 4.2e-12 across all 16
    finite cases, against a bound of 1e-9. Two languages, two BLAS libraries,
    two completely different routes through the formula -- theirs via
    expm::sqrtm on non-symmetric products, ours via eigh on symmetrised
    inputs -- and the numbers agree. The metrics are calibrated.

    Rows where the parent returned NaN are excluded here and handled by
    test_parent_returns_nan_on_identical_matrices.
    """
    case, tag, m, cond, d2_parent, _, X, Y = row
    ours = float(bw_dist2(X, Y))
    scale = float(trace(X) + trace(Y))
    assert abs(ours - d2_parent) / scale < 1e-9, (
        f"case {case} ({tag}, m={m}, cond={cond:.0e}): "
        f"parent {d2_parent!r} vs ours {ours!r}"
    )
