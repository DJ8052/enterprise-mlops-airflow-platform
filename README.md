# Enterprise MLOps Airflow Platform

This repository contains a local MLOps workflow that trains a machine-learning model from the Iris dataset, persists the trained model and evaluation metrics, exposes the model through a Streamlit inference app, and can be packaged with Docker and deployed to a local Kubernetes cluster with Minikube.

## Project objective

The project demonstrates a small but complete workflow for:

- loading and preparing tabular data,
- training a logistic regression classifier,
- saving a model artifact and evaluation metrics,
- orchestrating the training workflow with Apache Airflow,
- serving predictions through a lightweight Streamlit UI,
- containerizing the UI for local deployment,
- and describing a Kubernetes deployment for local testing.

This implementation is intentionally simple and understandable for interviews and portfolio demonstrations.

## Actual workflow

```text
Iris dataset
  -> Python training pipeline
  -> model artifact: artifacts/iris_classifier.joblib
  -> metrics artifact: artifacts/metrics.json
  -> Apache Airflow DAG
  -> Streamlit inference app
  -> Docker image
  -> Kubernetes deployment
```

## Dataset, model, artifacts, and metrics

- Dataset: scikit-learn Iris dataset
- Model: logistic regression classifier
- Model artifact: artifacts/iris_classifier.joblib
- Metrics artifact: artifacts/metrics.json
- Primary metric: accuracy
- Feature order used for training and inference:
  - sepal_length
  - sepal_width
  - petal_length
  - petal_width

## Repository tree

```text
.
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── deployment.yaml
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
├── airflow/
│   └── dags/
│       └── ml_pipeline_dag.py
├── scripts/
│   ├── build_docker.ps1
│   ├── deploy_k8s.ps1
│   ├── run_pipeline.ps1
│   ├── run_streamlit.ps1
│   ├── run_tests.ps1
│   └── setup_env.ps1
├── src/
│   └── enterprise_mlops_airflow_platform/
│       ├── __init__.py
│       ├── data_pipeline.py
│       ├── modeling.py
│       ├── pipeline.py
├── streamlit/
│   └── app.py
└── tests/
    └── test_pipeline.py
```

## Prerequisites

- Python 3.11+
- Windows PowerShell
- Docker Desktop and Docker Engine
- Docker Compose
- kubectl
- Minikube (optional for local validation)

## Local setup

From the repository root, run:

```powershell
./scripts/setup_env.ps1
```

This creates or reuses .venv and installs the project dependencies from requirements.txt.

## Run tests

```powershell
./scripts/run_tests.ps1
```

## Train the model

```powershell
./scripts/run_pipeline.ps1
```

Expected output:

- artifacts/iris_classifier.joblib
- artifacts/metrics.json

## Launch the Streamlit app

```powershell
./scripts/run_streamlit.ps1
```

The app expects the trained model artifact to exist at artifacts/iris_classifier.joblib.

## Docker

Build the image locally:

```powershell
./scripts/build_docker.ps1
```

Or run:

```powershell
docker compose up --build
```

The Docker image launches the Streamlit app on port 8501.

## Kubernetes / Minikube

Build or tag the image locally before applying the manifest:

```powershell
docker build -t enterprise-mlops-airflow-platform:local .
```

Then deploy with:

```powershell
./scripts/deploy_k8s.ps1
```

Or directly:

```powershell
kubectl apply -f deployment.yaml
```

## Airflow DAG

The Airflow DAG is defined in airflow/dags/ml_pipeline_dag.py and calls the shared training pipeline module from src/enterprise_mlops_airflow_platform/pipeline.py.

The DAG is intended for local development and uses a simple PythonOperator-based workflow. It does not bundle the full Airflow UI stack into the Docker image.

## Current status

The repository currently implements the core workflow locally and provides the files needed to run the training pipeline, test it, launch the Streamlit app, build the Docker image, and describe a Kubernetes deployment.

### Current limitations

- The Airflow DAG is intended for local development and has not been fully exercised in a production-grade Airflow deployment.
- The Docker image currently serves the Streamlit inference app only.
- The Kubernetes manifest is a local Minikube-oriented deployment example rather than a production-grade cluster configuration.
- The project does not include secrets management, CI/CD automation, or model registry integration yet.

## Validation commands

The following commands are available for local verification:

```powershell
./scripts/setup_env.ps1
./scripts/run_tests.ps1
./scripts/run_pipeline.ps1
./scripts/run_streamlit.ps1
./scripts/build_docker.ps1
kubectl apply --dry-run=client -f deployment.yaml
```
