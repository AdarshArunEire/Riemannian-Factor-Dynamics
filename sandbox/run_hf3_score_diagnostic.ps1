param(
    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 60,
    [switch]$CheckOnly,
    [switch]$Smoke,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) { throw "Python environment is missing: $python" }

Set-Location -LiteralPath $repoRoot
$env:PYTHONUNBUFFERED = '1'
foreach ($name in @('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS')) {
    Set-Item -Path "Env:$name" -Value '1'
}

Write-Host '1/2 APP-HF-3 focused tests'
& $python -m pytest py/tests/test_hf3_score_diagnostic.py py/tests/test_score_filter.py py/tests/test_hf2_representation.py -q
if ($LASTEXITCODE -ne 0) { throw "Tests failed with exit code $LASTEXITCODE" }

Write-Host '2/2 APP-HF-3 frozen-source preflight'
& $python experiments/run_hf3_score_diagnostic.py --dry-run
if ($LASTEXITCODE -ne 0) { throw "Preflight failed with exit code $LASTEXITCODE" }
if ($CheckOnly) { Write-Host 'APP-HF-3 check-only passed.' -ForegroundColor Green; return }

$arguments = @('experiments/run_hf3_score_diagnostic.py')
if ($Smoke) { $arguments += '--smoke' }
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
$outputName = if ($Smoke) { 'hf3_crypto_scores_smoke' } else { 'hf3_crypto_scores' }
$output = Join-Path $repoRoot "results\intermediate\$outputName"

Write-Host ''
Write-Host 'Running APP-HF-3: frozen 2024 projected-score diagnostic.' -ForegroundColor Cyan
Write-Host 'HF-2 geometry is reused; VAR uses genuine within-week pairs; Kalman is not retuned; 2025 remains sealed.'
Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
try {
    if (-not $process.Start()) { throw 'APP-HF-3 process could not be started' }
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
        $live = @(Get-Process -Id $process.Id -ErrorAction SilentlyContinue)
        $ram = [math]::Round(($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1)
        $folds = @(Get-ChildItem -LiteralPath (Join-Path $output 'materialized') -Filter '*.meta.json' -ErrorAction SilentlyContinue).Count
        Write-Host ('[heartbeat {0}] APP-HF-3 | elapsed={1:hh\:mm\:ss} | score sources={2}/4 | RAM={3}MB' -f (Get-Date -Format 'HH:mm:ss'), $timer.Elapsed, $folds, $ram) -ForegroundColor Cyan
    }
    $process.WaitForExit()
    $stdout = $stdoutTask.Result
    $stderr = $stderrTask.Result
    if ($stdout) { Write-Host $stdout.TrimEnd() }
    if ($stderr) { Write-Host $stderr.TrimEnd() -ForegroundColor DarkYellow }
    if ($process.ExitCode -ne 0) { throw "APP-HF-3 failed with exit code $($process.ExitCode)" }
}
finally {
    $timer.Stop()
    if ($process -and -not $process.HasExited) { & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null }
}

Write-Host "Completed in $($timer.Elapsed.ToString('hh\:mm\:ss'))." -ForegroundColor Green
Write-Host "Report: $(Join-Path $output 'report.md')"
Write-Host "Plots:  $output"
