$os   = Get-CimInstance Win32_OperatingSystem
$cpu  = Get-CimInstance Win32_Processor | Select-Object -First 1
$py   = python -c "import sys;print('.'.join(map(str,sys.version_info[:3])))"
$npv  = python -c "import numpy;print(numpy.__version__)"
$spv  = python -c "import scipy;print(scipy.__version__)"
$blas = python -c "import numpy as n
try:
    b=n.show_config('dicts')['Build Dependencies']['blas']
    print(b.get('name','?'), b.get('version','?'))
except Exception: print('unknown')"
$rv   = Rscript -e "cat(R.version.string)"
$rlap  = Rscript -e 'cat(La_version())'
$rhome = Rscript -e 'cat(R.home())'
$rdll  = Get-ChildItem (Join-Path $rhome "bin\x64\Rblas.dll") -ErrorAction SilentlyContinue
$rbl   = if ($rdll) {
    "bundled Rblas.dll, {0:N2} MB, {1:yyyy-MM-dd}" -f ($rdll.Length/1MB), $rdll.LastWriteTime
} else { "bundled reference BLAS (Rblas.dll)" }

@"
# Environment record

Regenerate with versions.ps1 whenever a toolchain changes.
Committed because the numerical results depend on every row.

| item | value |
|---|---|
| generated | $(Get-Date -Format 'yyyy-MM-dd HH:mm') |
| OS | $($os.Caption) $($os.Version) $($os.OSArchitecture) |
| CPU | $($cpu.Name.Trim()) - $($cpu.NumberOfCores)C/$($cpu.NumberOfLogicalProcessors)T |
| Python | $py |
| numpy | $npv |
| numpy BLAS | $blas |
| scipy | $spv |
| R | $rv |
| R BLAS | $rbl |
| R LAPACK | $rlap |
"@ | Set-Content VERSIONS.md