from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.job import KubernetesJobOperator


with DAG(
    dag_id="enterprise_mlops_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["mlops", "portfolio"],
) as dag:
    training_task = KubernetesJobOperator(
        task_id="train_model_on_kubernetes",
        namespace="default",
        name="enterprise-mlops-training",
        job_template_file="/opt/airflow/project/training-job.yaml",
        config_file="/home/airflow/.kube/config",
        in_cluster=False,
        get_logs=True,
        wait_until_job_complete=True,
        job_poll_interval=5,
        on_finish_action="keep_pod",
    )

    training_task
