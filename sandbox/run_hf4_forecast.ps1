param(
    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 30,
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

Write-Host '1/2 APP-HF-4 focused tests'
& $python -m pytest py/tests/test_forecast_baselines.py py/tests/test_score_har.py py/tests/test_hf4_forecast.py py/tests/test_score_filter.py py/tests/test_hf2_representation.py py/tests/test_lag.py -q
if ($LASTEXITCODE -ne 0) { throw "Tests failed with exit code $LASTEXITCODE" }

Write-Host '2/2 APP-HF-4 frozen-design preflight'
& $python experiments/run_hf4_forecast.py --dry-run
if ($LASTEXITCODE -ne 0) { throw "Preflight failed with exit code $LASTEXITCODE" }
if ($CheckOnly) { Write-Host 'APP-HF-4 check-only passed.' -ForegroundColor Green; return }

$arguments = @('experiments/run_hf4_forecast.py')
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
$outputName = if ($Smoke) { 'hf4_crypto_forecast_smoke' } else { 'hf4_crypto_forecast' }
$output = Join-Path $repoRoot "results\intermediate\$outputName"
$expectedBlocks = if ($Smoke) { 2 } else { 14 }

Write-Host ''
Write-Host 'Running APP-HF-4: causal one-hour covariance forecast tournament.' -ForegroundColor Cyan
Write-Host 'LOCF, 2024-tuned EWMA, log-SPD HAR, parent RFM and piecewise-6 RFD share every target.'
Write-Host 'Both geometric representations receive matched VAR(1), coordinate-OLS-HAR, and ridge-VHAR heads across ranks 1--19.'
Write-Host 'Rank-19 VAR(1) is the original headline; OLS HAR is the main new head; ridge VHAR is optional sensitivity.'
Write-Host 'Geometric arms refit every four weeks on the trailing 26 weeks; block caches are atomic and digest-checked.'
Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
try {
    if (-not $process.Start()) { throw 'APP-HF-4 process could not be started' }
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
        $family = @(Get-CimInstance Win32_Process -Filter "ParentProcessId=$($process.Id)" -ErrorAction SilentlyContinue)
        $processIds = @($process.Id) + @($family.ProcessId)
        $live = @(Get-Process -Id $processIds -ErrorAction SilentlyContinue)
        $ram = [math]::Round(($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1)
        $statusPath = Join-Path $output 'run_status.json'
        $blocks = 0
        if (Test-Path -LiteralPath $statusPath -PathType Leaf) {
            try { $blocks = [int](Get-Content -LiteralPath $statusPath -Raw | ConvertFrom-Json).completed_blocks } catch { $blocks = 0 }
        }
        Write-Host ('[heartbeat {0}] APP-HF-4 | elapsed={1:hh\:mm\:ss} | refit blocks={2}/{3} | processes={4} | RAM={5}MB' -f (Get-Date -Format 'HH:mm:ss'), $timer.Elapsed, $blocks, $expectedBlocks, $live.Count, $ram) -ForegroundColor Cyan
    }
    $process.WaitForExit()
    $stdout = $stdoutTask.Result
    $stderr = $stderrTask.Result
    if ($stdout) { Write-Host $stdout.TrimEnd() }
    if ($stderr) { Write-Host $stderr.TrimEnd() -ForegroundColor DarkYellow }
    if ($process.ExitCode -ne 0) { throw "APP-HF-4 failed with exit code $($process.ExitCode)" }
}
finally {
    $timer.Stop()
    if ($process -and -not $process.HasExited) { & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null }
}

Write-Host "Completed in $($timer.Elapsed.ToString('hh\:mm\:ss'))." -ForegroundColor Green
Write-Host "Report: $(Join-Path $output 'report.md')"
Write-Host "Plots:  $output"
