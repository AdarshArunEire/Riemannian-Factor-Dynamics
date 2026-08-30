param(
    [ValidateSet('smoke', 'calibration', 'overnight')]
    [string]$Profile = 'overnight',

    [ValidateRange(1, 8)]
    [int]$Workers = 8,

    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 60,

    [switch]$CheckOnly
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$runner = Join-Path $repoRoot 'experiments\run_score_filter_bw.py'
$outputDirectory = switch ($Profile) {
    'smoke' { Join-Path $repoRoot 'tmp\score_filter_bw_smoke' }
    'calibration' { Join-Path $repoRoot 'results\intermediate\score_filter_bw_calibration' }
    default { Join-Path $repoRoot 'results\intermediate\score_filter_bw' }
}
$logDirectory = Join-Path $repoRoot 'results\intermediate\score_filter_bw_runner'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$stdoutPath = Join-Path $logDirectory "score_filter_$($Profile)_$($stamp)_stdout.log"
$stderrPath = Join-Path $logDirectory "score_filter_$($Profile)_$($stamp)_stderr.log"

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Python environment is missing: $python"
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

Write-Host '1/2 score-filter focused tests'
& $python -m pytest py/tests/test_score_filter.py py/tests/test_score_filter_bw.py -q
if ($LASTEXITCODE -ne 0) { throw 'focused tests failed' }

Write-Host '2/2 workload preflight'
& $python $runner --profile $Profile --workers $Workers --dry-run
if ($LASTEXITCODE -ne 0) { throw 'preflight failed' }
if ($CheckOnly) {
    Write-Host 'Check-only mode passed; no experiment rows were fitted.' -ForegroundColor Green
    return
}

$startInfo = New-Object System.Diagnostics.ProcessStartInfo
$startInfo.FileName = $python
$startInfo.Arguments = "`"$runner`" --profile $Profile --workers $Workers"
$startInfo.WorkingDirectory = $repoRoot
$startInfo.UseShellExecute = $false
$startInfo.CreateNoWindow = $true
$startInfo.RedirectStandardOutput = $true
$startInfo.RedirectStandardError = $true
$process = New-Object System.Diagnostics.Process
$process.StartInfo = $startInfo
$timer = [System.Diagnostics.Stopwatch]::StartNew()

Write-Host "Running BW score-filter profile '$Profile' with $Workers workers." -ForegroundColor Cyan
Write-Host 'Rows append atomically as tasks finish; rerun the same command to resume.'
Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
try {
    if (-not $process.Start()) { throw 'score-filter process could not be started' }
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
        $raw = Join-Path $outputDirectory 'raw.csv'
        $rows = if (Test-Path -LiteralPath $raw -PathType Leaf) {
            [math]::Max(0, (Get-Content -LiteralPath $raw | Measure-Object -Line).Lines - 1)
        } else { 0 }
        $live = @(Get-Process -Id $process.Id -ErrorAction SilentlyContinue)
        $ram = [math]::Round(($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1)
        Write-Host (
            '[heartbeat {0}] BW score filter | elapsed={1:hh\:mm\:ss} | rows={2} | RAM={3}MB' -f
            (Get-Date -Format 'HH:mm:ss'), $timer.Elapsed, $rows, $ram
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
        throw "score-filter run failed with exit code $($process.ExitCode)"
    }
}
finally {
    $timer.Stop()
    if ($process -and -not $process.HasExited) {
        & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null
    }
}
Write-Host "Completed in $($timer.Elapsed.ToString('hh\:mm\:ss'))." -ForegroundColor Green
Write-Host "Report: $(Join-Path $outputDirectory 'report.md')"
