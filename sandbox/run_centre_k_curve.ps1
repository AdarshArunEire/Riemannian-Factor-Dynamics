$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

Push-Location $ProjectRoot
try {
    & $Python -m pytest py/tests/test_centre_k_curve.py py/tests/test_centre_low_n.py -q
    if ($LASTEXITCODE -ne 0) { throw "Centre K-curve tests failed" }
    & $Python experiments/run_centre_k_curve.py
    if ($LASTEXITCODE -ne 0) { throw "Centre K curve failed" }
} finally {
    Pop-Location
}
