param(
    [switch]$SkipN240,
    [switch]$SkipN8192
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "Project Python was not found at $Python"
}

Push-Location $ProjectRoot
try {
    & $Python -m pytest py/tests/test_covariance_proxy.py py/tests/test_matched_centre_tournament.py py/tests/test_centre_low_n.py -q
    if ($LASTEXITCODE -ne 0) { throw "Focused tests failed" }

    & $Python experiments/run_matched_centre_tournament.py --profile n240 --smoke --force
    if ($LASTEXITCODE -ne 0) { throw "Matched n=240 smoke failed" }

    if (-not $SkipN240) {
        & $Python experiments/run_matched_centre_tournament.py --profile n240
        if ($LASTEXITCODE -ne 0) { throw "Matched n=240 tournament failed" }
    }
    if (-not $SkipN8192) {
        & $Python experiments/run_matched_centre_tournament.py --profile n8192
        if ($LASTEXITCODE -ne 0) { throw "Matched n=8192 tournament failed" }
    }
} finally {
    Pop-Location
}
