param(
    [ValidateSet('DryRun', 'Selection', 'Pilot', 'Full')]
    [string]$Profile = 'Pilot'
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Python environment is missing: $python"
}

function Invoke-CheckedPython {
    param([Parameter(Mandatory)][string[]]$Arguments)
    & $python @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Python failed with exit code $LASTEXITCODE"
    }
}

Set-Location -LiteralPath $repoRoot
$env:PYTHONUNBUFFERED = '1'

Write-Host '1/2 APP-HF-0 focused tests'
Invoke-CheckedPython @('-m', 'pytest', 'py/tests/test_hf0_crypto_preflight.py', '-q')

$runnerProfile = $Profile.ToLowerInvariant()
if ($runnerProfile -eq 'dryrun') { $runnerProfile = 'dry-run' }

Write-Host "2/2 APP-HF-0 $Profile profile" -ForegroundColor Cyan
Write-Host 'Downloads are checksum-verified, cached, and written atomically.'
Write-Host 'Asset selection uses 2023-Q4 only; no 2024-2025 centre or forecast result enters selection.'
Invoke-CheckedPython @(
    'experiments/run_hf0_crypto_preflight.py',
    '--profile', $runnerProfile
)

if ($Profile -eq 'DryRun') {
    Write-Host 'Dry run passed; no network request was made.' -ForegroundColor Green
} elseif ($Profile -eq 'Selection') {
    Write-Host 'Selection is frozen. Run -Profile Pilot before the full panel.' -ForegroundColor Green
} else {
    $folder = if ($Profile -eq 'Pilot') { 'hf0_crypto_pilot' } else { 'hf0_crypto' }
    Write-Host "Completed. Report: results\intermediate\$folder\report.md" -ForegroundColor Green
}
