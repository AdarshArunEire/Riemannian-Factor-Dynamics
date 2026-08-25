param(
    [ValidateRange(0, 3600)]
    [int]$BreakSeconds = 300,

    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 60,

    [ValidateRange(30, 900)]
    [int]$PreflightTimeoutSeconds = 180,

    [switch]$NoShutdown,

    [switch]$CheckOnly
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$rscriptCommand = Get-Command Rscript -ErrorAction Stop
$rscript = $rscriptCommand.Source
$parentTarget = Join-Path $repoRoot 'results\raw\n00'
$logDirectory = Join-Path $repoRoot 'results\intermediate\overnight'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$logPath = Join-Path $logDirectory "overnight_$stamp.log"
$processLogDirectory = Join-Path $logDirectory "process_$stamp"

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Python environment is missing: $python"
}

Set-Location -LiteralPath $repoRoot
$env:PYTHONUNBUFFERED = '1'

function Resolve-ProjectRLibrary {
    $libraryRoot = Join-Path $repoRoot 'renv\library\windows'
    if (-not (Test-Path -LiteralPath $libraryRoot -PathType Container)) {
        throw "renv library root is missing: $libraryRoot"
    }

    $candidates = @(
        Get-ChildItem -LiteralPath $libraryRoot -Directory | ForEach-Object {
            Get-ChildItem -LiteralPath $_.FullName -Directory
        } | Where-Object {
            Test-Path -LiteralPath (Join-Path $_.FullName 'renv\DESCRIPTION') -PathType Leaf
        }
    )

    if ($candidates.Count -ne 1) {
        throw "expected exactly one restored renv library; found $($candidates.Count) under $libraryRoot"
    }

    return $candidates[0].FullName
}

function Get-ProcessTreeStats {
    param(
        [Parameter(Mandatory)]
        [int]$RootProcessId
    )

    $allProcesses = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue)
    $ids = @($RootProcessId)
    do {
        $children = @(
            $allProcesses | Where-Object {
                $_.ParentProcessId -in $ids -and $_.ProcessId -notin $ids
            } | Select-Object -ExpandProperty ProcessId
        )
        if ($children.Count -gt 0) {
            $ids += $children
        }
    } while ($children.Count -gt 0)

    $live = @($ids | ForEach-Object { Get-Process -Id $_ -ErrorAction SilentlyContinue })
    return [pscustomobject]@{
        Count = $live.Count
        CPUSeconds = [math]::Round(($live | Measure-Object -Property CPU -Sum).Sum, 1)
        WorkingSetMB = [math]::Round(($live | Measure-Object -Property WorkingSet64 -Sum).Sum / 1MB, 1)
    }
}

function Stop-ProcessTree {
    param([int]$RootProcessId)

    if (Get-Process -Id $RootProcessId -ErrorAction SilentlyContinue) {
        & taskkill.exe /PID $RootProcessId /T /F 2>&1 | Out-Null
    }
}

function Invoke-ExternalWithHeartbeat {
    param(
        [Parameter(Mandatory)]
        [string]$StageId,

        [Parameter(Mandatory)]
        [string]$Name,

        [Parameter(Mandatory)]
        [string]$FilePath,

        [Parameter(Mandatory)]
        [string[]]$ArgumentList,

        [string]$ProgressPath,

        [int]$TimeoutSeconds = 0
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
    $stdoutTask = $null
    $stderrTask = $null

    try {
        # Start-Process on Windows PowerShell 5.1 leaves ExitCode null when
        # WaitForExit() is called manually. A direct .NET Process preserves a
        # reliable exit code while still allowing periodic heartbeat checks.
        $startInfo = New-Object System.Diagnostics.ProcessStartInfo
        $startInfo.FileName = $FilePath
        $startInfo.Arguments = $ArgumentList -join ' '
        $startInfo.WorkingDirectory = $repoRoot
        $startInfo.UseShellExecute = $false
        $startInfo.CreateNoWindow = $true
        $startInfo.RedirectStandardOutput = $true
        $startInfo.RedirectStandardError = $true

        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $startInfo
        if (-not $process.Start()) {
            throw "$Name could not be started"
        }
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()

        while (-not $process.WaitForExit($HeartbeatSeconds * 1000)) {
            if ($TimeoutSeconds -gt 0 -and $timer.Elapsed.TotalSeconds -ge $TimeoutSeconds) {
                Stop-ProcessTree -RootProcessId $process.Id
                throw "$Name exceeded its $TimeoutSeconds-second timeout"
            }

            $stats = Get-ProcessTreeStats -RootProcessId $process.Id
            $progress = ''
            if ($ProgressPath -and (Test-Path -LiteralPath $ProgressPath -PathType Container)) {
                $files = @(Get-ChildItem -LiteralPath $ProgressPath -Recurse -File -ErrorAction SilentlyContinue)
                $latest = $files | Sort-Object LastWriteTime -Descending | Select-Object -First 1
                if ($latest) {
                    $age = [math]::Round(((Get-Date) - $latest.LastWriteTime).TotalMinutes, 1)
                    $progress = " | outputs=$($files.Count), latest=${age}m ago"
                } else {
                    $progress = ' | outputs=0'
                }
            }

            Write-Host (
                '[heartbeat {0}] {1} | elapsed={2:hh\:mm\:ss} | processes={3} | CPU={4}s | RAM={5}MB{6}' -f
                (Get-Date -Format 'HH:mm:ss'), $Name, $timer.Elapsed,
                $stats.Count, $stats.CPUSeconds, $stats.WorkingSetMB, $progress
            ) -ForegroundColor Cyan
        }

        $process.WaitForExit()
        $stdout = $stdoutTask.Result
        $stderr = $stderrTask.Result
        [System.IO.File]::WriteAllText($stdoutPath, $stdout)
        [System.IO.File]::WriteAllText($stderrPath, $stderr)

        if ($stdout.Length -gt 0) {
            Write-Host $stdout.TrimEnd()
        }
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
            Stop-ProcessTree -RootProcessId $process.Id
        }
    }

    Write-Host "Completed: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') (elapsed $($timer.Elapsed.ToString('hh\:mm\:ss')))"
}

function Start-Intermission {
    param([int]$Seconds)

    if ($Seconds -le 0) {
        return
    }
    $resumeAt = (Get-Date).AddSeconds($Seconds)
    Write-Host ''
    Write-Host "Cooling-off break: $Seconds seconds; next stage at $($resumeAt.ToString('HH:mm:ss'))."
    while ((Get-Date) -lt $resumeAt) {
        $remaining = [math]::Ceiling(($resumeAt - (Get-Date)).TotalSeconds)
        $sleepFor = [math]::Min($HeartbeatSeconds, $remaining)
        Start-Sleep -Seconds $sleepFor
        $remaining = [math]::Max(0, [math]::Ceiling(($resumeAt - (Get-Date)).TotalSeconds))
        if ($remaining -gt 0) {
            Write-Host "[heartbeat $(Get-Date -Format 'HH:mm:ss')] cooling-off break | remaining=${remaining}s" -ForegroundColor Cyan
        }
    }
}

New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $processLogDirectory -Force | Out-Null
$transcriptStarted = $false
$allSucceeded = $false
$checkSucceeded = $false

$projectRLibrary = Resolve-ProjectRLibrary
$env:R_LIBS_USER = $projectRLibrary
$env:RENV_CONFIG_AUTOLOADER_ENABLED = 'FALSE'

try {
    Start-Transcript -LiteralPath $logPath | Out-Null
    $transcriptStarted = $true

    Write-Host "Repository: $repoRoot"
    Write-Host "Transcript: $logPath"
    Write-Host "Process logs: $processLogDirectory"
    Write-Host "Heartbeat interval: $HeartbeatSeconds seconds"
    Write-Host "R startup: --vanilla with R_LIBS_USER=$projectRLibrary"
    Write-Host "Break between stages: $BreakSeconds seconds"
    Write-Host "Automatic shutdown: $(-not $NoShutdown)"

    Write-Host 'Preflight: validating both Python profiles and the parent R environment.'
    Invoke-ExternalWithHeartbeat `
        -StageId 'preflight_centre_rate' `
        -Name 'Preflight: centre-rate profile' `
        -FilePath $python `
        -ArgumentList @('experiments/run_centre_rate.py', '--profile', 'centre_rate', '--dry-run') `
        -TimeoutSeconds $PreflightTimeoutSeconds

    Invoke-ExternalWithHeartbeat `
        -StageId 'preflight_discrepancy' `
        -Name 'Preflight: discrepancy profile' `
        -FilePath $python `
        -ArgumentList @('experiments/run_centre_rate.py', '--profile', 'discrepancy', '--dry-run') `
        -TimeoutSeconds $PreflightTimeoutSeconds

    Invoke-ExternalWithHeartbeat `
        -StageId 'preflight_parent' `
        -Name 'Preflight: parent R environment' `
        -FilePath $rscript `
        -ArgumentList @('--vanilla', 'R/run_parent_simulations.R', '--check') `
        -TimeoutSeconds $PreflightTimeoutSeconds

    if (Test-Path -LiteralPath $parentTarget) {
        throw "Parent target already exists: $parentTarget. Preserve/move it before a new recorded run."
    }

    $checkSucceeded = $true
    if ($CheckOnly) {
        Write-Host 'OVERNIGHT CHECK PASSED. No experiment ran and no shutdown was scheduled.'
    } else {
        Invoke-ExternalWithHeartbeat `
            -StageId '01_centre_rate' `
            -Name '1/3 B4.2 centre-rate experiment' `
            -FilePath $python `
            -ArgumentList @('experiments/run_centre_rate.py', '--profile', 'centre_rate') `
            -ProgressPath (Join-Path $repoRoot 'results\intermediate\centre_rate')

        Start-Intermission -Seconds $BreakSeconds

        Invoke-ExternalWithHeartbeat `
            -StageId '02_discrepancy' `
            -Name '2/3 N-LS-A controlled discrepancy experiment' `
            -FilePath $python `
            -ArgumentList @('experiments/run_centre_rate.py', '--profile', 'discrepancy') `
            -ProgressPath (Join-Path $repoRoot 'results\intermediate\local_stationarity_discrepancy')

        Start-Intermission -Seconds $BreakSeconds

        Invoke-ExternalWithHeartbeat `
            -StageId '03_parent' `
            -Name '3/3 N-00 parent SPD reproduction' `
            -FilePath $rscript `
            -ArgumentList @('--vanilla', 'R/run_parent_simulations.R') `
            -ProgressPath $parentTarget

        $allSucceeded = $true
    }
}
catch {
    Write-Error "OVERNIGHT CHAIN STOPPED: $($_.Exception.Message)"
}
finally {
    if ($transcriptStarted) {
        Stop-Transcript | Out-Null
    }
}

if ($CheckOnly) {
    if ($checkSucceeded) {
        exit 0
    }
    exit 1
}

if (-not $allSucceeded) {
    Write-Host 'No shutdown was scheduled. Inspect the transcript and the stage-specific outputs.'
    exit 1
}

if ($NoShutdown) {
    Write-Host 'All three stages completed. -NoShutdown was supplied, so the PC will remain on.'
    exit 0
}

Write-Host ''
Write-Host 'All three stages completed successfully.'
Write-Host 'Windows will shut down in 120 seconds.'
Write-Host 'To cancel, run this in any terminal before the countdown expires:'
Write-Host '    shutdown.exe /a'

& shutdown.exe /s /t 120 /c 'RFD overnight experiments completed successfully. Run shutdown.exe /a to cancel.'
if ($LASTEXITCODE -ne 0) {
    throw "Could not schedule shutdown; shutdown.exe returned $LASTEXITCODE"
}
