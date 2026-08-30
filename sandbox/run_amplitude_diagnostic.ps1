param(
    [ValidateRange(1, 8)]
    [int]$Workers = 8,

    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 30,

    [switch]$CheckOnly
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$runnerLog = Join-Path $repoRoot 'results\intermediate\amplitude_diagnostic_runner'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$processLogs = Join-Path $runnerLog "process_$stamp"
$transcript = Join-Path $runnerLog "runner_$stamp.log"
$rawPath = Join-Path $repoRoot 'results\intermediate\amplitude_diagnostic\raw.csv'

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

function Get-RowProgress {
    if (-not (Test-Path -LiteralPath $rawPath -PathType Leaf)) {
        return 'rows=0/192'
    }
    $count = ([System.IO.File]::ReadLines($rawPath) | Measure-Object).Count - 1
    $age = [math]::Round(
        ((Get-Date) - (Get-Item -LiteralPath $rawPath).LastWriteTime).TotalSeconds,
        0
    )
    return "rows=$([math]::Max(0, $count))/192, latest=${age}s ago"
}

function Invoke-PythonStage {
    param(
        [Parameter(Mandatory)][string]$Id,
        [Parameter(Mandatory)][string]$Title,
        [Parameter(Mandatory)][string[]]$Arguments,
        [switch]$TrackRows
    )
    Write-Host ''
    Write-Host $Title -ForegroundColor Cyan
    Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    $stdoutPath = Join-Path $processLogs "${Id}_stdout.log"
    $stderrPath = Join-Path $processLogs "${Id}_stderr.log"
    $timer = [System.Diagnostics.Stopwatch]::StartNew()
    $start = New-Object System.Diagnostics.ProcessStartInfo
    $start.FileName = $python
    $start.Arguments = $Arguments -join ' '
    $start.WorkingDirectory = $repoRoot
    $start.UseShellExecute = $false
    $start.CreateNoWindow = $true
    $start.RedirectStandardOutput = $true
    $start.RedirectStandardError = $true
    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $start
    try {
        if (-not $process.Start()) { throw "$Title could not be started" }
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()
        while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
            $progress = if ($TrackRows) { Get-RowProgress } else { 'working' }
            Write-Host (
                '[heartbeat {0}] elapsed={1:hh\:mm\:ss} | {2}' -f
                (Get-Date -Format 'HH:mm:ss'), $timer.Elapsed, $progress
            ) -ForegroundColor DarkCyan
        }
        $process.WaitForExit()
        $stdout = $stdoutTask.Result
        $stderr = $stderrTask.Result
        [System.IO.File]::WriteAllText($stdoutPath, $stdout)
        [System.IO.File]::WriteAllText($stderrPath, $stderr)
        if ($stdout.Length -gt 0) { Write-Host $stdout.TrimEnd() }
        if ($stderr.Length -gt 0) { Write-Host $stderr.TrimEnd() -ForegroundColor DarkYellow }
        if ($process.ExitCode -ne 0) {
            throw "$Title failed with exit code $($process.ExitCode)"
        }
    }
    finally {
        $timer.Stop()
        if ($process -and -not $process.HasExited) {
            & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null
        }
    }
    Write-Host "Completed in $($timer.Elapsed.ToString('hh\:mm\:ss'))"
}

New-Item -ItemType Directory -Path $runnerLog -Force | Out-Null
New-Item -ItemType Directory -Path $processLogs -Force | Out-Null
$transcriptStarted = $false
try {
    Start-Transcript -LiteralPath $transcript | Out-Null
    $transcriptStarted = $true
    Write-Host "Workers: $Workers; each worker is restricted to one BLAS thread."
    Write-Host 'The recorded run has 192 paired draws and is append-only/resumable.'
    Write-Host 'Planning budget: roughly 1--3 minutes on eight workers; the heartbeat will refine this.'

    Invoke-PythonStage -Id 'tests' -Title 'Focused diagnostic tests' -Arguments @(
        '-m', 'pytest', 'py/tests/test_amplitude_diagnostic.py', '-q'
    )
    Invoke-PythonStage -Id 'plan' -Title 'Recorded workload preflight' -Arguments @(
        'experiments/run_amplitude_diagnostic.py', '--profile', 'diagnostic',
        '--workers', "$Workers", '--dry-run'
    )
    if ($CheckOnly) {
        Write-Host 'Check-only mode passed; no recorded draws were run.' -ForegroundColor Green
        return
    }
    Invoke-PythonStage -Id 'run' -Title 'Paired low-n amplitude diagnostic' -Arguments @(
        'experiments/run_amplitude_diagnostic.py', '--profile', 'diagnostic',
        '--workers', "$Workers"
    ) -TrackRows
    Invoke-PythonStage -Id 'analysis' -Title 'Attribution tables and plots' -Arguments @(
        'experiments/analyze_amplitude_diagnostic.py', '--profile', 'diagnostic'
    )
    Write-Host ''
    Write-Host 'Diagnostic complete.' -ForegroundColor Green
    Write-Host (Join-Path $repoRoot 'results\final\amplitude_diagnostic\report.md')
}
finally {
    if ($transcriptStarted) { Stop-Transcript | Out-Null }
}
