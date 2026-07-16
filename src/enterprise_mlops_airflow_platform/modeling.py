from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Mapping

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from .data_pipeline import FEATURE_COLUMNS, TARGET_COLUMN


def train_and_evaluate_model(train_df: pd.DataFrame, test_df: pd.DataFrame, random_state: int = 7) -> Dict[str, Any]:
    """Train a logistic regression model and return evaluation metrics."""
    X_train = train_df[FEATURE_COLUMNS]
    y_train = train_df[TARGET_COLUMN]
    X_test = test_df[FEATURE_COLUMNS]
    y_test = test_df[TARGET_COLUMN]

    model = LogisticRegression(max_iter=500, solver="lbfgs", random_state=random_state)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return {
        "accuracy": float(accuracy),
        "model_type": "logistic_regression",
        "classes": model.classes_.tolist(),
        "feature_columns": FEATURE_COLUMNS,
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
    }


def save_model(model: Any, output_path: Path) -> Path:
    """Persist a trained model to disk."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)
    return output_path


def save_metrics(metrics: Mapping[str, Any], output_path: Path) -> Path:
    """Persist evaluation metrics to a JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return output_path
