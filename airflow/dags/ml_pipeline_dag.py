from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from enterprise_mlops_airflow_platform.pipeline import run_training_pipeline


def run_pipeline_task(**context):
    result = run_training_pipeline(output_dir="/tmp/enterprise-mlops-artifacts")
    context["ti"].xcom_push(key="model_path", value=str(result["model_path"]))
    context["ti"].xcom_push(key="accuracy", value=result["metrics"]["accuracy"])


with DAG(
    dag_id="enterprise_mlops_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["mlops", "portfolio"],
) as dag:
    training_task = PythonOperator(
        task_id="train_model",
        python_callable=run_pipeline_task,
        provide_context=True,
    )

    training_task
