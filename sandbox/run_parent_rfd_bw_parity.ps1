param(
    [ValidateRange(1, 8)]
    [int]$Workers = 8,

    [ValidateRange(10, 600)]
    [int]$HeartbeatSeconds = 60,

    [switch]$CheckOnly,

    [switch]$Shutdown
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$rscript = (Get-Command Rscript -ErrorAction Stop).Source
$logDirectory = Join-Path $repoRoot 'results\intermediate\parent_rfd_bw_parity_runner'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$transcriptPath = Join-Path $logDirectory "runner_$stamp.log"
$processLogDirectory = Join-Path $logDirectory "process_$stamp"

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Python environment is missing: $python"
}

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
        throw "expected one restored renv library; found $($candidates.Count)"
    }
    return $candidates[0].FullName
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
    return [pscustomobject]@{
        Count = $live.Count
        CPUSeconds = [math]::Round(($live | Measure-Object CPU -Sum).Sum, 1)
        WorkingSetMB = [math]::Round(($live | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 1)
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
            & taskkill.exe /PID $process.Id /T /F 2>&1 | Out-Null
        }
    }
    Write-Host "Completed: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') (elapsed $($timer.Elapsed.ToString('hh\:mm\:ss')))"
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
New-Item -ItemType Directory -Path $processLogDirectory -Force | Out-Null
$transcriptStarted = $false
$allSucceeded = $false

try {
    Start-Transcript -LiteralPath $transcriptPath | Out-Null
    $transcriptStarted = $true
    Write-Host "Repository: $repoRoot"
    Write-Host "Python: $python"
    Write-Host "Rscript: $rscript"
    Write-Host "R library: $env:R_LIBS_USER"
    Write-Host "Workers: $Workers (one BLAS thread per worker)"
    Write-Host "Transcript: $transcriptPath"
    Write-Host 'Recorded profile: 576 paired draws, 1,728 estimator fits.'
    Write-Host 'Runtime guide on this machine: budget roughly 8--14 hours; n=8192 dominates.'
    Write-Host 'Interrupted recorded runs are resumable by rerunning this command.'

    Invoke-WithHeartbeat -StageId 'tests' -Name '1/4 focused parity harness tests' -Arguments @(
        '-m', 'pytest', 'py/tests/test_parent_rfd_bw_parity.py', '-q'
    )
    Invoke-WithHeartbeat -StageId 'preflight' -Name '2/4 workload and parent-R preflight' -Arguments @(
        'experiments/run_parent_rfd_bw_parity.py', '--profile', 'overnight',
        '--workers', "$Workers", '--dry-run', '--check-r'
    )
    if ($CheckOnly) {
        Write-Host 'Check-only mode passed; no synthetic fits were run.' -ForegroundColor Green
        $allSucceeded = $true
        return
    }

    Invoke-WithHeartbeat `
        -StageId 'smoke' `
        -Name '3/4 actual paired parent/RFD smoke' `
        -Arguments @(
            'experiments/run_parent_rfd_bw_parity.py', '--profile', 'smoke',
            '--workers', '2'
        ) `
        -ProgressPath (Join-Path $repoRoot 'tmp\parent_rfd_bw_parity_smoke_v4') `
        -ExpectedRows 2

    $smoke = Import-Csv -LiteralPath (Join-Path $repoRoot 'tmp\parent_rfd_bw_parity_smoke_v4\raw.csv')
    $badSmoke = @($smoke | Where-Object { $_.status -ne 'ok' })
    if ($smoke.Count -ne 2 -or $badSmoke.Count -gt 0) {
        throw "paired smoke did not produce exactly two fully successful rows"
    }

    Invoke-WithHeartbeat `
        -StageId 'overnight' `
        -Name '4/4 recorded parent RFM versus RFD BW parity sweep' `
        -Arguments @(
            'experiments/run_parent_rfd_bw_parity.py', '--profile', 'overnight',
            '--workers', "$Workers"
        ) `
        -ProgressPath (Join-Path $repoRoot 'results\intermediate\parent_rfd_bw_parity') `
        -ExpectedRows 576

    $allSucceeded = $true
    Write-Host ''
    Write-Host 'Paired BW parity sweep completed.' -ForegroundColor Green
    Write-Host "Report: $(Join-Path $repoRoot 'results\intermediate\parent_rfd_bw_parity\report.md')"
    Write-Host "Plots: $(Join-Path $repoRoot 'results\intermediate\parent_rfd_bw_parity')"
}
finally {
    if ($transcriptStarted) { Stop-Transcript | Out-Null }
    if ($allSucceeded -and $Shutdown -and -not $CheckOnly) {
        Write-Host 'All stages passed. Windows will shut down in 120 seconds.' -ForegroundColor Yellow
        Write-Host 'Cancel with: shutdown /a' -ForegroundColor Yellow
        & shutdown.exe /s /t 120 /c 'Parent RFM versus RFD BW parity sweep completed.'
    } elseif ($Shutdown -and -not $allSucceeded) {
        Write-Warning 'Shutdown suppressed because a stage failed.'
    }
}
