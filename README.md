# Enterprise MLOps Airflow Platform

This repository demonstrates a production-minded local MLOps workflow that trains a machine learning model, orchestrates training with Apache Airflow and Kubernetes, persists model artifacts to shared storage, and serves predictions through a Streamlit application.

The project is designed as an engineering portfolio that demonstrates software engineering, workflow orchestration, containerization, Kubernetes-native execution, and machine learning infrastructure rather than model complexity.

---

# Project Objective

The objective of this project is to demonstrate a complete end-to-end machine learning workflow that follows production-minded engineering practices.

The repository demonstrates:

* Python software engineering
* Git-based development workflow
* Automated unit testing with pytest
* Docker containerization
* Kubernetes-native model training
* Apache Airflow workflow orchestration
* Shared model artifact management
* Streamlit model inference
* Modular project organization

Although the current implementation uses the Iris dataset, the engineering platform is intentionally designed so the underlying business problem, data, features, and model can be replaced without redesigning the infrastructure.

---

# System Architecture

```text
Developer
      │
      ▼
Apache Airflow
      │
      ▼
KubernetesJobOperator
      │
      ▼
Kubernetes Training Job
      │
      ▼
Shared Persistent Storage
      │
      ▼
Model Artifact
      │
      ▼
Streamlit Inference Application
```

The engineering responsibilities are intentionally separated:

* **Apache Airflow** orchestrates the workflow.
* **Kubernetes** executes model training.
* **Shared storage** persists trained model artifacts.
* **Streamlit** loads the trained model for inference.
* **Docker** packages the application for consistent execution.
* **Git and GitHub** provide version control.

---

# Current Demonstration Workflow

```text
Iris Dataset
      │
      ▼
Python Training Pipeline
      │
      ▼
Kubernetes Training Job
      │
      ▼
Shared Model Artifacts
      │
      ▼
Streamlit Inference
```

---

# Dataset, Model, and Artifacts

**Dataset**

* scikit-learn Iris dataset

**Current Model**

* Logistic Regression classifier

**Artifacts**

* `artifacts/iris_classifier.joblib`
* `artifacts/metrics.json`

**Primary Evaluation Metric**

* Classification Accuracy

**Feature Order**

* sepal_length
* sepal_width
* petal_length
* petal_width

---

# Repository Structure

```text
.
├── airflow/
│   └── dags/
├── artifacts/
├── k8s/
├── scripts/
├── src/
│   └── enterprise_mlops_airflow_platform/
├── streamlit/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── deployment.yaml
├── pyproject.toml
├── requirements.txt
└── README.md
```

> The exact contents of each directory may evolve as additional engineering capabilities are added.

---

# Prerequisites

* Python 3.11+
* Docker Desktop
* Docker Compose
* kubectl
* Minikube
* Apache Airflow (Docker Compose environment)

---

# Local Setup

Create the virtual environment and install dependencies:

```powershell
./scripts/setup_env.ps1
```

---

# Run Unit Tests

```powershell
./scripts/run_tests.ps1
```

---

# Train the Model

```powershell
./scripts/run_pipeline.ps1
```

Expected artifacts:

* `artifacts/iris_classifier.joblib`
* `artifacts/metrics.json`

---

# Launch the Streamlit Application

```powershell
./scripts/run_streamlit.ps1
```

The Streamlit application loads the trained model artifact and performs interactive predictions.

---

# Docker

Build the application:

```powershell
./scripts/build_docker.ps1
```

or

```powershell
docker compose up --build
```

Docker packages the Streamlit inference application for consistent local execution.

---

# Kubernetes

Deploy the application to the local Minikube cluster:

```powershell
kubectl apply -f deployment.yaml
```

The Kubernetes deployment demonstrates local container orchestration and shared artifact usage.

---

# Apache Airflow

Apache Airflow orchestrates the machine learning workflow using a **KubernetesJobOperator**.

The validated orchestration flow is:

```text
Airflow
      │
      ▼
Kubernetes Job
      │
      ▼
Training Container
      │
      ▼
Shared Persistent Storage
      │
      ▼
Model Artifacts
```

This separates workflow orchestration from model serving while allowing training artifacts to be reused by downstream applications.

---

# Validated Capabilities

The following capabilities have been implemented and validated locally:

* ✅ Modular Python package
* ✅ Git version control
* ✅ GitHub repository
* ✅ Virtual environment
* ✅ Unit testing with pytest
* ✅ Machine learning training pipeline
* ✅ Model persistence
* ✅ Streamlit inference application
* ✅ Docker containerization
* ✅ Docker Compose environment
* ✅ Kubernetes deployment with Minikube
* ✅ Kubernetes Job execution
* ✅ Shared persistent model artifacts
* ✅ Apache Airflow scheduler and web interface
* ✅ Airflow DAG execution
* ✅ KubernetesJobOperator orchestration

---

# Current Status

The repository demonstrates a complete local MLOps workflow in which Apache Airflow orchestrates Kubernetes-native model training, persists trained artifacts to shared storage, and serves predictions through a separate Streamlit application.

The project emphasizes engineering architecture, orchestration, reproducibility, and maintainability over model complexity.

---

# Current Limitations

The current implementation intentionally focuses on local infrastructure validation.

The following capabilities have **not** yet been implemented:

* Cloud deployment
* CI/CD automation
* Model registry
* Secrets management
* Production monitoring
* Distributed storage
* Multi-node Kubernetes deployment

These features are planned as future enhancements after the core engineering workflow has been fully validated.

---

# Roadmap

Planned future work includes:

* Operational reliability improvements
* Retry and failure handling
* Artifact validation
* CI/CD with GitHub Actions
* Architecture diagrams
* Technical documentation
* Construction and field operations business domain
* Operational risk prediction model
* Decision-support workflow

The long-term objective is to demonstrate how a reusable engineering platform can support business decision-making by replacing the domain-specific data, features, model, and decision logic while keeping the underlying MLOps architecture intact.
