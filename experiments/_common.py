"""Shared plumbing for the experiment scripts. Not an experiment itself."""

import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "py"))     # pyproject's pythonpath is pytest-only

SEED = 20260816
FINAL = ROOT / "results" / "final"


def header(title, extra=()):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return [
        f"# {title}",
        "",
        "Measurement only: no assertions, no pass/fail. Re-run and append a",
        "dated section rather than editing.",
        "",
        f"- generated: {stamp}",
        f"- seed: {SEED}",
        f"- numpy {np.__version__}, python {platform.python_version()}",
        f"- machine: {platform.processor() or 'unknown'} / {platform.platform()}",
        f"- eps: {np.finfo(np.float64).eps:.6e}",
        *[f"- {e}" for e in extra],
        "",
    ]


def write(name, lines, cols, rows):
    """Write results/final/<name>.md and .csv from the same rows."""
    FINAL.mkdir(parents=True, exist_ok=True)
    md = FINAL / f"{name}.md"
    csv = FINAL / f"{name}.csv"

    body = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        body.append("| " + " | ".join(str(x) for x in r) + " |")

    md.write_text("\n".join(lines[:-1] + ["## Measured", ""] + body + ["", lines[-1]]),
                  encoding="utf-8")
    csv.write_text(
        ",".join(cols) + "\n"
        + "\n".join(",".join(str(x) for x in r) for r in rows) + "\n",
        encoding="utf-8",
    )
    print(f"\nwritten -> {md.relative_to(ROOT)}")
    print(f"written -> {csv.relative_to(ROOT)}")
