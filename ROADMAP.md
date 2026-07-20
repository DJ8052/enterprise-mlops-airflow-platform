# Enterprise MLOps Airflow Platform

# Authoritative Project Roadmap

## Mission

Build a production-minded MLOps platform whose engineering foundation can support different business problems by replacing the domain-specific data, features, model, and decision logic.

**Portfolio Focus:** Construction and Field Operations

---

# Completed Phases

## ✅ Phase 1 — Local Development Foundation

Established the software engineering foundation.

Completed:

- Git & GitHub
- VS Code
- Python package structure
- Virtual environment
- Unit testing with pytest
- Local training pipeline
- Streamlit inference application
- Model persistence

---

## ✅ Phase 2 — Docker Validation

Validated containerization.

Completed:

- Dockerfile
- Docker Compose
- Streamlit container
- Artifact mounting
- Local Docker validation

---

## ✅ Phase 3 — Kubernetes Platform Validation

Validated Kubernetes deployment.

Completed:

- Minikube
- kubectl
- Kubernetes Deployment
- Kubernetes Service
- Local cluster validation

---

## ✅ Phase 4 — Kubernetes-Native Training Workflow

Separated model training from model serving.

Completed:

- Kubernetes Job
- Persistent Volume Claim (PVC)
- Shared model artifacts
- Training container
- Streamlit artifact consumption
- End-to-end Kubernetes training validation

---

## ✅ Phase 5 — Workflow Orchestration

### ✅ Phase 5.1 — Airflow Platform Validation

Completed:

- Apache Airflow
- PostgreSQL backend
- Docker Compose development environment

### ✅ Phase 5.2 — DAG Discovery & Execution

Completed:

- Scheduler validation
- Web UI validation
- DAG discovery
- DAG execution

### ✅ Phase 5.3 — Airflow → Kubernetes Orchestration

Completed:

- KubernetesJobOperator
- Kubernetes Job execution
- Shared artifact persistence
- End-to-end workflow orchestration

Validated workflow:

```text
Apache Airflow
        │
        ▼
KubernetesJobOperator
        │
        ▼
Kubernetes Training Job
        │
        ▼
Shared Persistent Volume
        │
        ▼
Model Artifacts
        │
        ▼
Streamlit Inference Application
```

---

# Remaining Roadmap

## ⬜ Phase 6 — Operational Reliability

**Goal**

Move from:

> "It works."

to

> "It behaves predictably."

Deliverables:

- Artifact validation
- Retry strategy
- Failure handling
- Logging improvements
- Cleanup strategy
- Idempotent execution

Success Criteria:

- Failed jobs retry appropriately.
- Missing artifacts generate controlled failures.
- Jobs clean up according to policy.
- Logs support troubleshooting.
- Re-running the workflow leaves the system in a consistent state.

---

## ⬜ Phase 7 — CI/CD & Engineering Automation

Deliverables:

- GitHub Actions
- Automated testing
- Docker build validation
- Linting
- Documentation validation

Goal:

Automatically validate engineering changes before they are merged.

---

## ⬜ Phase 8 — Documentation & Engineering Portfolio

Deliverables:

- Architecture diagrams
- Deployment guide
- Technical walkthrough
- Screenshots
- Interview discussion guide
- Repository polish

Goal:

Allow reviewers to understand the system quickly without reading the implementation first.

---

## ⬜ Phase 9 — Construction Domain Design

Replace the Iris demonstration with a construction and field operations domain.

Business entities:

- Projects
- Crews
- Equipment
- Weather
- Labor
- Schedules
- Safety
- Delays
- Operational risk definitions

No infrastructure changes occur during this phase.

---

## ⬜ Phase 10 — Operational Data Platform

Build realistic operational datasets.

Sources include:

- Projects
- Crews
- Equipment
- Weather
- Historical outcomes
- Resource assignments

The engineering platform remains unchanged.

Only the business data changes.

---

## ⬜ Phase 11 — Construction Risk Model

Replace the Iris classifier with an operational risk model.

Deliverables:

- Feature engineering
- Model training
- Validation
- Risk scoring
- Decision logic
- Model documentation

---

## ⬜ Phase 12 — Field Operations Decision Support

Transform predictions into business recommendations.

The application should answer questions such as:

- Which projects are at elevated operational risk?
- Why are they at risk?
- What actions should leadership consider?
- Which crews or schedules require attention?

---

## ⬜ Phase 13 — Production Readiness & Portfolio Polish

Finalize the platform with:

- Configuration management
- Environment separation
- Packaging improvements
- Operational documentation
- Portfolio refinement

The emphasis is demonstrating production-minded engineering practices while remaining evidence-based.

---

# Final Portfolio Outcome

The completed project demonstrates three connected capabilities.

## 1. Software & Platform Engineering

- Git
- GitHub
- Python
- Testing
- Docker
- Kubernetes
- Apache Airflow
- CI/CD

↓

## 2. Production-Minded MLOps

- Workflow orchestration
- Kubernetes-native training
- Artifact management
- Reliability
- Validation
- Model deployment

↓

## 3. Business Decision Support

Construction & Field Operations

↓

Operational Data Platform

↓

Risk Modeling

↓

Decision Support

---

## Guiding Principle

The engineering platform is intentionally reusable.

Future business problems should require replacing only:

- Domain-specific data
- Features
- Models
- Decision logic

while preserving the underlying engineering architecture.