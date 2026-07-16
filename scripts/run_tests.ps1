$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (-not (Test-Path ".venv")) {
    throw "The virtual environment does not exist. Run .\\scripts\\setup_env.ps1 first."
}

.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = "$projectRoot\src"
python -m pytest -q
