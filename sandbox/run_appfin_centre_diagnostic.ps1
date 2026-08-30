param(
    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 60,

    [switch]$CheckOnly,

    [switch]$SkipBootstrap,

    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$logDirectory = Join-Path $repoRoot 'results\intermediate\appfin_centre_diagnostic_runner'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$stdoutPath = Join-Path $logDirectory "centre_${stamp}_stdout.log"
$stderrPath = Join-Path $logDirectory "centre_${stamp}_stderr.log"

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Python environment is missing: $python"
}

function Invoke-CheckedPython {
    param([Parameter(Mandatory)][string[]]$Arguments)
    & $python @Arguments
    if ($LASTEXITCODE -ne 0) { throw "Python failed with exit code $LASTEXITCODE" }
}

Set-Location -LiteralPath $repoRoot
$env:PYTHONUNBUFFERED = '1'
foreach ($name in @(
    'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
    'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS'
)) {
    Set-Item -Path "Env:$name" -Value '1'
}
New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null

Write-Host '1/2 APP-FIN centre-diagnostic tests'
Invoke-CheckedPython @(
    '-m', 'pytest',
    'py/tests/test_appfin_centre_diagnostic.py',
    'py/tests/test_appfin_identification.py',
    '-q'
)

Write-Host '2/2 frozen-design preflight'
Invoke-CheckedPython @('experiments/run_appfin_centre_diagnostic.py', '--dry-run')
if ($CheckOnly) {
    Write-Host 'Check-only mode passed; no centre diagnostic was fitted.' -ForegroundColor Green
    return
}

$arguments = @('experiments/run_appfin_centre_diagnostic.py')
if ($SkipBootstrap) { $arguments += '--skip-bootstrap' }
if ($Force) { $arguments += '--force' }
$argumentString = ($arguments | ForEach-Object { '"' + $_.Replace('"', '\"') + '"' }) -join ' '
$startInfo = New-Object System.Diagnostics.ProcessStartInfo
$startInfo.FileName = $python
$startInfo.Arguments = $argumentString
$startInfo.WorkingDirectory = $repoRoot
$startInfo.UseShellExecute = $false
$startInfo.CreateNoWindow = $true
$startInfo.RedirectStandardOutput = $true
$startInfo.RedirectStandardError = $true
$process = New-Object System.Diagnostics.Process
$process.StartInfo = $startInfo
$timer = [System.Diagnostics.Stopwatch]::StartNew()

Write-Host ''
Write-Host 'Running the APP-FIN centre-detectability diagnostic.' -ForegroundColor Cyan
Write-Host 'Annual folds and fixed-centre bootstrap replicates are digest-checked and resumable.'
Write-Host 'The primary comparison is squared BW loss; QLIKE and relative Frobenius are sensitivity checks.'
Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

try {
    if (-not $process.Start()) { throw 'Centre-diagnostic process could not be started' }
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
        $live = @(Get-Process -Id $process.Id -ErrorAction SilentlyContinue)
        $ram = [math]::Round(($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1)
        $foldRows = @(Get-ChildItem -LiteralPath (Join-Path $repoRoot 'results\intermediate\appfin_centre_diagnostic\folds') -Filter 'fold_*.npz' -ErrorAction SilentlyContinue).Count
        $nullRows = @(Get-ChildItem -LiteralPath (Join-Path $repoRoot 'results\intermediate\appfin_centre_diagnostic\constant_centre_bootstrap') -Filter 'replicate_*.json' -ErrorAction SilentlyContinue).Count
        Write-Host (
            '[heartbeat {0}] centre diagnostic | elapsed={1:hh\:mm\:ss} | folds={2}/20 | null={3}/99 | RAM={4}MB' -f
            (Get-Date -Format 'HH:mm:ss'), $timer.Elapsed, $foldRows, $nullRows, $ram
        ) -ForegroundColor Cyan
    }
    $process.WaitForExit()
    $stdout = $stdoutTask.Result
    $stderr = $stderrTask.Result
    [System.IO.File]::WriteAllText($stdoutPath, $stdout)
    [System.IO.File]::WriteAllText($stderrPath, $stderr)
    if ($stdout) { Write-Host $stdout.TrimEnd() }
    if ($stderr) { Write-Host $stderr.TrimEnd() -ForegroundColor DarkYellow }
    if ($process.ExitCode -ne 0) {
        throw "Centre diagnostic failed with exit code $($process.ExitCode)"
    }
}
finally {
    $timer.Stop()
    if ($process -and -not $process.HasExited) {
        & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null
    }
}

Write-Host "Completed in $($timer.Elapsed.ToString('hh\:mm\:ss'))." -ForegroundColor Green
Write-Host "Report: $(Join-Path $repoRoot 'results\intermediate\appfin_centre_diagnostic\report.md')"
Write-Host "Plots:  $(Join-Path $repoRoot 'results\intermediate\appfin_centre_diagnostic')"
