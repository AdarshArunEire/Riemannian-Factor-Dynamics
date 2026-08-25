param(
    [ValidateRange(1, 8)]
    [int]$Workers = 8,

    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 60,

    [ValidateRange(0, 3600)]
    [int]$BreakSeconds = 60,

    [switch]$CheckOnly,

    [switch]$Shutdown
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$logDirectory = Join-Path $repoRoot 'results\intermediate\paper1_control_runner'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$transcriptPath = Join-Path $logDirectory "runner_$stamp.log"
$processLogDirectory = Join-Path $logDirectory "process_$stamp"

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Python environment is missing: $python"
}

Set-Location -LiteralPath $repoRoot
$env:PYTHONUNBUFFERED = '1'

# Eight independent simulations may run concurrently.  Each simulation gets
# one BLAS thread so an eight-worker job cannot silently become a 64-thread job.
foreach ($name in @(
    'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
    'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS'
)) {
    Set-Item -Path "Env:$name" -Value '1'
}

function Get-ProcessTreeStats {
    param([Parameter(Mandatory)][int]$RootProcessId)

    $all = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue)
    $ids = @($RootProcessId)
    do {
        $children = @(
            $all | Where-Object {
                $_.ParentProcessId -in $ids -and $_.ProcessId -notin $ids
            } | Select-Object -ExpandProperty ProcessId
        )
        if ($children.Count -gt 0) { $ids += $children }
    } while ($children.Count -gt 0)

    $live = @($ids | ForEach-Object { Get-Process -Id $_ -ErrorAction SilentlyContinue })
    [pscustomobject]@{
        Count = $live.Count
        CPUSeconds = [math]::Round(($live | Measure-Object CPU -Sum).Sum, 1)
        WorkingSetMB = [math]::Round(
            ($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1
        )
    }
}

function Stop-ProcessTree {
    param([int]$RootProcessId)
    if (Get-Process -Id $RootProcessId -ErrorAction SilentlyContinue) {
        & taskkill.exe /PID $RootProcessId /T /F 2>&1 | Out-Null
    }
}

function Get-RowProgress {
    param([string]$ProgressPath, [int]$ExpectedRows)

    $rawPath = Join-Path $ProgressPath 'raw.csv'
    if (-not (Test-Path -LiteralPath $rawPath -PathType Leaf)) {
        return "rows=0/$ExpectedRows"
    }
    $lines = [System.IO.File]::ReadLines($rawPath) | Measure-Object
    $rows = [math]::Max(0, $lines.Count - 1)
    $age = [math]::Round(((Get-Date) - (Get-Item -LiteralPath $rawPath).LastWriteTime).TotalMinutes, 1)
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
    $process = $null

    try {
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
        if (-not $process.Start()) { throw "$Name could not be started" }
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()

        while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
            $stats = Get-ProcessTreeStats -RootProcessId $process.Id
            $progress = if ($ProgressPath) {
                Get-RowProgress -ProgressPath $ProgressPath -ExpectedRows $ExpectedRows
            } else { 'working' }
            Write-Host (
                '[heartbeat {0}] {1} | elapsed={2:hh\:mm\:ss} | processes={3} | CPU={4}s | RAM={5}MB | {6}' -f
                (Get-Date -Format 'HH:mm:ss'), $Name, $timer.Elapsed,
                $stats.Count, $stats.CPUSeconds, $stats.WorkingSetMB, $progress
            ) -ForegroundColor Cyan
        }

        $process.WaitForExit()
        $stdout = $stdoutTask.Result
        $stderr = $stderrTask.Result
        [System.IO.File]::WriteAllText($stdoutPath, $stdout)
        [System.IO.File]::WriteAllText($stderrPath, $stderr)
        if ($stdout.Length -gt 0) { Write-Host $stdout.TrimEnd() }
        if ($stderr.Length -gt 0) { Write-Host $stderr.TrimEnd() -ForegroundColor DarkYellow }
        if ($process.ExitCode -ne 0) {
            throw "$Name failed with exit code $($process.ExitCode)"
        }
    }
    finally {
        $timer.Stop()
        if ($process -and -not $process.HasExited) {
            Stop-ProcessTree -RootProcessId $process.Id
        }
    }

    Write-Host "Completed: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') (elapsed $($timer.Elapsed.ToString('hh\:mm\:ss')))"
}

function Start-Intermission {
    param([int]$Seconds)
    if ($Seconds -le 0) { return }
    Write-Host "Cooling break: $Seconds seconds."
    Start-Sleep -Seconds $Seconds
}

New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $processLogDirectory -Force | Out-Null
$transcriptStarted = $false
$allSucceeded = $false

try {
    Start-Transcript -LiteralPath $transcriptPath | Out-Null
    $transcriptStarted = $true

    Write-Host "Repository: $repoRoot"
    Write-Host "Workers: $Workers (one BLAS thread each)"
    Write-Host "Heartbeat: $HeartbeatSeconds seconds"
    Write-Host "Transcript: $transcriptPath"
    if ($Workers -eq 8) {
        Write-Host 'Runtime guide: about 43 minutes of historical compute; budget 45--70 minutes including overhead.'
    }
    Write-Host 'Interrupted runs are resumable: rerun this same command.'

    Write-Host 'Preflight: configuration, focused tests, and dry-run plans.'
    Invoke-WithHeartbeat -StageId 'tests' -Name 'Focused harness tests' -Arguments @(
        '-m', 'pytest', 'py/tests/test_paper1_controls.py', '-q'
    )
    Invoke-WithHeartbeat -StageId 'preflight_core' -Name 'Preflight: core matrix' -Arguments @(
        'experiments/run_paper1_controls.py', '--profile', 'control_core',
        '--workers', "$Workers", '--dry-run'
    )
    Invoke-WithHeartbeat -StageId 'preflight_phase' -Name 'Preflight: phase curve' -Arguments @(
        'experiments/run_paper1_controls.py', '--profile', 'phase_curve',
        '--workers', "$Workers", '--dry-run'
    )

    if ($CheckOnly) {
        Write-Host 'Check-only mode complete; no recorded simulations were run.' -ForegroundColor Green
        $allSucceeded = $true
        return
    }

    Invoke-WithHeartbeat `
        -StageId 'core' `
        -Name '1/3 Paper 1 core control matrix' `
        -Arguments @(
            'experiments/run_paper1_controls.py', '--profile', 'control_core',
            '--workers', "$Workers"
        ) `
        -ProgressPath (Join-Path $repoRoot 'results\intermediate\paper1_control_core') `
        -ExpectedRows 1056

    Start-Intermission -Seconds $BreakSeconds

    Invoke-WithHeartbeat `
        -StageId 'phase' `
        -Name '2/3 drift-orientation phase curve' `
        -Arguments @(
            'experiments/run_paper1_controls.py', '--profile', 'phase_curve',
            '--workers', "$Workers"
        ) `
        -ProgressPath (Join-Path $repoRoot 'results\intermediate\paper1_phase_curve') `
        -ExpectedRows 480

    Invoke-WithHeartbeat -StageId 'analysis' -Name '3/3 summaries and plots' -Arguments @(
        'experiments/analyze_paper1_controls.py'
    )

    $allSucceeded = $true
    Write-Host ''
    Write-Host 'Paper 1 control matrix completed successfully.' -ForegroundColor Green
    Write-Host "Report: $(Join-Path $repoRoot 'results\final\paper1_control_matrix\report.md')"
}
finally {
    if ($transcriptStarted) { Stop-Transcript | Out-Null }

    if ($allSucceeded -and $Shutdown -and -not $CheckOnly) {
        Write-Host 'All stages passed. Windows will shut down in 120 seconds.' -ForegroundColor Yellow
        Write-Host 'Cancel with: shutdown /a' -ForegroundColor Yellow
        & shutdown.exe /s /t 120 /c 'Paper 1 control matrix completed successfully.'
    } elseif ($Shutdown -and -not $allSucceeded) {
        Write-Warning 'Shutdown was requested but has been suppressed because a stage failed.'
    }
}
