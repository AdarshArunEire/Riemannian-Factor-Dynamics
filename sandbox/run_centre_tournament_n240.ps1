$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $projectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $python)) {
    throw "Project Python environment not found: $python"
}

& $python -m pytest py/tests/test_centre_low_n.py py/tests/test_appfin_centre_diagnostic.py -q
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& $python experiments/run_centre_tournament.py
exit $LASTEXITCODE
