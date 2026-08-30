param(
    [ValidateRange(0, 36)]
    [int]$SmokeMonths = 0,

    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 30,

    [switch]$CheckOnly,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$runner = Join-Path $repoRoot 'experiments\run_appfin_centre_head_tournament.py'
$outputName = if ($SmokeMonths -gt 0) { 'appfin_centre_head_tournament_smoke' } else { 'appfin_centre_head_tournament' }
$outputDirectory = Join-Path $repoRoot "results\intermediate\$outputName"
$logDirectory = Join-Path $repoRoot 'results\intermediate\appfin_centre_head_tournament_runner'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$stdoutPath = Join-Path $logDirectory "centre_heads_$($stamp)_stdout.log"
$stderrPath = Join-Path $logDirectory "centre_heads_$($stamp)_stderr.log"

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Python environment is missing: $python"
}

function Resolve-ProjectRLibrary {
    $root = Join-Path $repoRoot 'renv\library\windows'
    $candidates = @(
        Get-ChildItem -LiteralPath $root -Directory | ForEach-Object {
            Get-ChildItem -LiteralPath $_.FullName -Directory
        } | Where-Object {
            Test-Path -LiteralPath (Join-Path $_.FullName 'renv\DESCRIPTION') -PathType Leaf
        }
    )
    if ($candidates.Count -ne 1) {
        throw "expected one restored renv library; found $($candidates.Count)"
    }
    return $candidates[0].FullName
}

Set-Location -LiteralPath $repoRoot
$env:PYTHONUNBUFFERED = '1'
$env:R_LIBS_USER = Resolve-ProjectRLibrary
$env:RENV_CONFIG_AUTOLOADER_ENABLED = 'FALSE'
foreach ($name in @(
    'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
    'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS'
)) {
    Set-Item -Path "Env:$name" -Value '1'
}
New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null

Write-Host '1/2 APP-FIN centre-head focused tests'
& $python -m pytest py/tests/test_appfin_centre_head_tournament.py py/tests/test_appfin_score_filter.py py/tests/test_centre_low_n.py -q
if ($LASTEXITCODE -ne 0) { throw 'focused tests failed' }

Write-Host '2/2 APP-FIN data and R preflight'
& $python $runner --dry-run --check-r
if ($LASTEXITCODE -ne 0) { throw 'preflight failed' }
if ($CheckOnly) {
    Write-Host 'Check-only mode passed; no forecasts were fitted.' -ForegroundColor Green
    return
}

$arguments = @($runner)
if ($SmokeMonths -gt 0) { $arguments += @('--smoke-months', $SmokeMonths.ToString()) }
if ($Force) { $arguments += '--force' }
$argumentString = ($arguments | ForEach-Object { '"' + $_ + '"' }) -join ' '
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

Write-Host 'Running APP-FIN centre construction x VAR/KF tournament.' -ForegroundColor Cyan
Write-Host 'The literal parent cache is reused; every new RFD origin is atomic and resumable.'
Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
try {
    if (-not $process.Start()) { throw 'APP-FIN centre-head process could not be started' }
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
        $originDirectory = Join-Path $outputDirectory 'rfd_origins'
        $completed = @(Get-ChildItem -LiteralPath $originDirectory -Filter 'target_*.json' -ErrorAction SilentlyContinue).Count
        $target = if ($SmokeMonths -gt 0) { $SmokeMonths } else { 36 }
        $live = @(Get-Process -Id $process.Id -ErrorAction SilentlyContinue)
        $ram = [math]::Round(($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1)
        Write-Host (
            '[heartbeat {0}] APP-FIN centre heads | elapsed={1:hh\:mm\:ss} | origins={2}/{3} | RAM={4}MB' -f
            (Get-Date -Format 'HH:mm:ss'), $timer.Elapsed, $completed, $target, $ram
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
        throw "APP-FIN centre-head run failed with exit code $($process.ExitCode)"
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
Write-Host "Plot:   $(Join-Path $outputDirectory 'centre_head_tournament.png')"
