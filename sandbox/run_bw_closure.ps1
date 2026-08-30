param(
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
$logDirectory = Join-Path $repoRoot 'results\intermediate\bw_closure_runner'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$transcriptPath = Join-Path $logDirectory "runner_$stamp.log"
$processLogDirectory = Join-Path $logDirectory "process_$stamp"

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
    param([string]$ProgressPath, [int]$ExpectedRows)

    $rawPath = Join-Path $ProgressPath 'raw.csv'
    if (-not (Test-Path -LiteralPath $rawPath -PathType Leaf)) {
        return "rows=0/$ExpectedRows"
    }
    $lines = [System.IO.File]::ReadLines($rawPath) | Measure-Object
    $rows = [math]::Max(0, $lines.Count - 1)
    $age = [math]::Round(
        ((Get-Date) - (Get-Item -LiteralPath $rawPath).LastWriteTime).TotalMinutes,
        1
    )
    return "rows=$rows/$ExpectedRows, latest=${age}m ago"
}

function Invoke-WithHeartbeat {
    param(
        [Parameter(Mandatory)][string]$StageId,
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string[]]$Arguments,
        [string]$ProgressPath = '',
        [int]$ExpectedRows = 0
    )

    Write-Host ''
    Write-Host ('=' * 72)
    Write-Host $Name
    Write-Host "Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    Write-Host ('=' * 72)

    $stdoutPath = Join-Path $processLogDirectory "${StageId}_stdout.log"
    $stderrPath = Join-Path $processLogDirectory "${StageId}_stderr.log"
    $timer = [System.Diagnostics.Stopwatch]::StartNew()
    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = $python
    $startInfo.Arguments = $Arguments -join ' '
    $startInfo.WorkingDirectory = $repoRoot
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $startInfo
    try {
        if (-not $process.Start()) { throw "$Name could not be started" }
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()

        while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
            $progress = if ($ProgressPath) {
                Get-RowProgress -ProgressPath $ProgressPath -ExpectedRows $ExpectedRows
            } else {
                'working'
            }
            Write-Host (
                '[heartbeat {0}] {1} | elapsed={2:hh\:mm\:ss} | {3}' -f
                (Get-Date -Format 'HH:mm:ss'), $Name, $timer.Elapsed, $progress
            ) -ForegroundColor Cyan
        }

        $process.WaitForExit()
        $stdout = $stdoutTask.Result
        $stderr = $stderrTask.Result
        [System.IO.File]::WriteAllText($stdoutPath, $stdout)
        [System.IO.File]::WriteAllText($stderrPath, $stderr)
        if ($stdout.Length -gt 0) { Write-Host $stdout.TrimEnd() }
        if ($stderr.Length -gt 0) {
            Write-Host $stderr.TrimEnd() -ForegroundColor DarkYellow
        }
        if ($process.ExitCode -ne 0) {
            throw "$Name failed with exit code $($process.ExitCode)"
        }
    }
    finally {
        $timer.Stop()
        if ($process -and -not $process.HasExited) {
            & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null
        }
    }
    Write-Host "Completed: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') (elapsed $($timer.Elapsed.ToString('hh\:mm\:ss')))"
}

New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $processLogDirectory -Force | Out-Null
$transcriptStarted = $false

try {
    Start-Transcript -LiteralPath $transcriptPath | Out-Null
    $transcriptStarted = $true

    Write-Host "Repository: $repoRoot"
    Write-Host "Workers: $Workers (one BLAS thread each)"
    Write-Host "Heartbeat: $HeartbeatSeconds seconds"
    Write-Host "Transcript: $transcriptPath"
    Write-Host 'Interrupted full runs are resumable: rerun this exact command.'

    Invoke-WithHeartbeat -StageId 'tests' -Name '1/4 focused BW closure tests' -Arguments @(
        '-m', 'pytest', 'py/tests/test_bw_closure.py', 'py/tests/test_bw.py',
        'py/tests/test_centre.py', 'py/tests/test_frame.py', 'py/tests/test_lag.py', '-q'
    )
    Invoke-WithHeartbeat -StageId 'plan' -Name '2/4 frozen workload preflight' -Arguments @(
        'experiments/run_bw_closure.py', '--profile', 'bw_closure',
        '--workers', "$Workers", '--dry-run'
    )

    if ($CheckOnly) {
        Write-Host 'Check-only mode complete; no simulations were run.' -ForegroundColor Green
        return
    }

    Invoke-WithHeartbeat `
        -StageId 'smoke' `
        -Name '3/4 BW safe/hostile smoke matrix' `
        -Arguments @(
            'experiments/run_bw_closure.py', '--profile', 'smoke',
            '--workers', "$Workers"
        ) `
        -ProgressPath (Join-Path $repoRoot 'tmp\bw_closure_smoke_v3') `
        -ExpectedRows 9

    $smoke = Import-Csv -LiteralPath (Join-Path $repoRoot 'tmp\bw_closure_smoke_v3\raw.csv')
    $failedSmoke = @($smoke | Where-Object { $_.boundary_verdict -eq 'fail' })
    if ($failedSmoke.Count -gt 0) {
        throw "Smoke matrix produced $($failedSmoke.Count) failed verdict(s); full run suppressed."
    }

    Invoke-WithHeartbeat `
        -StageId 'closure' `
        -Name '4/4 recorded compact BW closure matrix' `
        -Arguments @(
            'experiments/run_bw_closure.py', '--profile', 'bw_closure',
            '--workers', "$Workers"
        ) `
        -ProgressPath (Join-Path $repoRoot 'results\intermediate\bw_closure') `
        -ExpectedRows 496

    Write-Host ''
    Write-Host 'P1-BW-CLOSE completed.' -ForegroundColor Green
    Write-Host "Raw results: $(Join-Path $repoRoot 'results\intermediate\bw_closure\raw.csv')"
    Write-Host "Report: $(Join-Path $repoRoot 'results\intermediate\bw_closure\report.md')"
}
finally {
    if ($transcriptStarted) { Stop-Transcript | Out-Null }
}
