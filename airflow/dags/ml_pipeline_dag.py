from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s


with DAG(
    dag_id="enterprise_mlops_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["mlops", "portfolio"],
) as dag:
    training_task = KubernetesPodOperator(
        task_id="train_model_on_kubernetes",
        namespace="default",
        name="enterprise-mlops-training",
        image="enterprise-mlops-airflow-platform:latest",
        image_pull_policy="Never",
        cmds=["python", "-c"],
        arguments=[
            "from enterprise_mlops_airflow_platform.pipeline import run_training_pipeline\n"
            "result = run_training_pipeline(output_dir='/app/artifacts')\n"
            "print(result)\n"
        ],
        volumes=[
            k8s.V1Volume(
                name="model-storage",
                persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                    claim_name="model-artifacts-pvc"
                ),
            )
        ],
        volume_mounts=[
            k8s.V1VolumeMount(name="model-storage", mount_path="/app/artifacts")
        ],
        config_file="/home/airflow/.kube/config",
        in_cluster=False,
        get_logs=True,
        is_delete_operator_pod=False,
    )

    training_task
