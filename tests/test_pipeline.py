import pandas as pd
import pytest

from enterprise_mlops_airflow_platform.data_pipeline import FEATURE_COLUMNS, TARGET_COLUMN, load_dataset, split_dataset
from enterprise_mlops_airflow_platform.modeling import train_and_evaluate_model
from enterprise_mlops_airflow_platform.pipeline import run_training_pipeline


def test_load_dataset_returns_expected_shapes():
    data = load_dataset()

    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert set(FEATURE_COLUMNS + [TARGET_COLUMN, "target_name"]) <= set(data.columns)


def test_split_dataset_returns_train_and_test_frames():
    data = load_dataset()
    train_df, test_df = split_dataset(data, test_size=0.2, random_state=7)

    assert len(train_df) > 0
    assert len(test_df) > 0
    assert len(train_df) + len(test_df) == len(data)


def test_train_and_evaluate_model_returns_metrics():
    data = load_dataset()
    train_df, test_df = split_dataset(data, test_size=0.2, random_state=7)
    metrics = train_and_evaluate_model(train_df, test_df)

    assert 0.0 <= metrics["accuracy"] <= 1.0
    assert metrics["model_type"] == "logistic_regression"
    assert metrics["train_rows"] == len(train_df)
    assert metrics["test_rows"] == len(test_df)


def test_run_training_pipeline_creates_artifacts(tmp_path):
    output_dir = tmp_path / "artifacts"
    result = run_training_pipeline(output_dir=output_dir)

    assert result["model_path"].exists()
    assert result["metrics_path"].exists()
    assert 0.0 <= result["metrics"]["accuracy"] <= 1.0


def test_invalid_split_size_raises_value_error():
    data = load_dataset()

    with pytest.raises(ValueError):
        split_dataset(data, test_size=0.0)
