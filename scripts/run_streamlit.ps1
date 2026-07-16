$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (-not (Test-Path ".venv")) {
    throw "The virtual environment does not exist. Run .\scripts\setup_env.ps1 first."
}

.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = "$projectRoot\src"
$env:MODEL_ARTIFACT_DIR = "$projectRoot\artifacts"

if (-not (Test-Path "$projectRoot\artifacts\iris_classifier.joblib")) {
    Write-Host "No trained model artifact was found. Run .\scripts\run_pipeline.ps1 first." 
    exit 1
}

streamlit run streamlit/app.py --server.port 8501 --server.address 0.0.0.0
