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

Write-Host '1/2 APP-HF-2 focused tests'
& $python -m pytest py/tests/test_hf2_representation.py py/tests/test_lag.py py/tests/test_centre_low_n.py -q
if ($LASTEXITCODE -ne 0) { throw "Tests failed with exit code $LASTEXITCODE" }

Write-Host '2/2 APP-HF-2 frozen design preflight'
& $python experiments/run_hf2_representation.py --dry-run
if ($LASTEXITCODE -ne 0) { throw "Preflight failed with exit code $LASTEXITCODE" }
if ($CheckOnly) { Write-Host 'APP-HF-2 check-only passed.' -ForegroundColor Green; return }

$arguments = @('experiments/run_hf2_representation.py')
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
$outputName = if ($Smoke) { 'hf2_crypto_representation_smoke' } else { 'hf2_crypto_representation' }
$output = Join-Path $repoRoot "results\intermediate\$outputName"

Write-Host ''
Write-Host 'Running APP-HF-2: head-free global RFM versus piecewise-6 RFD.' -ForegroundColor Cyan
Write-Host 'The first 26 weeks choose an independent rank for each arm; the final 26 evaluate those frozen ranks.'
Write-Host 'Both folds run in parallel, every cache write is atomic and digest-checked, and 2025 remains sealed.'
Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
try {
    if (-not $process.Start()) { throw 'APP-HF-2 process could not be started' }
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
        $live = @(Get-Process -Id $process.Id -ErrorAction SilentlyContinue)
        $ram = [math]::Round(($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1)
        $folds = @(Get-ChildItem -LiteralPath $output -Recurse -Filter 'fold_*.npz' -ErrorAction SilentlyContinue).Count
        Write-Host ('[heartbeat {0}] APP-HF-2 | elapsed={1:hh\:mm\:ss} | phase/folds={2}/4 | RAM={3}MB' -f (Get-Date -Format 'HH:mm:ss'), $timer.Elapsed, $folds, $ram) -ForegroundColor Cyan
    }
    $process.WaitForExit()
    $stdout = $stdoutTask.Result
    $stderr = $stderrTask.Result
    if ($stdout) { Write-Host $stdout.TrimEnd() }
    if ($stderr) { Write-Host $stderr.TrimEnd() -ForegroundColor DarkYellow }
    if ($process.ExitCode -ne 0) { throw "APP-HF-2 failed with exit code $($process.ExitCode)" }
}
finally {
    $timer.Stop()
    if ($process -and -not $process.HasExited) { & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null }
}

Write-Host "Completed in $($timer.Elapsed.ToString('hh\:mm\:ss'))." -ForegroundColor Green
Write-Host "Report: $(Join-Path $output 'report.md')"
Write-Host "Plots:  $output"
