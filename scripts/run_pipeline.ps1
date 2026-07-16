$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (-not (Test-Path ".venv")) {
    throw "The virtual environment does not exist. Run .\scripts\setup_env.ps1 first."
}

.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = "$projectRoot\src"
$env:MODEL_ARTIFACT_DIR = "$projectRoot\artifacts"
python -c "from enterprise_mlops_airflow_platform.pipeline import run_training_pipeline; result = run_training_pipeline(output_dir='artifacts'); print(result['model_path']); print(result['metrics_path']); print(result['metrics'])"
