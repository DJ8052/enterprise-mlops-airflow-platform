from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

from sklearn.linear_model import LogisticRegression

from .data_pipeline import FEATURE_COLUMNS, TARGET_COLUMN, load_dataset, split_dataset
from .modeling import save_metrics, save_model, train_and_evaluate_model


def resolve_artifact_dir(output_dir: Path | str | None = None) -> Path:
    """Resolve a writable directory for training artifacts."""
    repo_root = Path(__file__).resolve().parents[2]
    if output_dir is None:
        configured_dir = os.getenv("MODEL_ARTIFACT_DIR")
        if configured_dir:
            candidate = Path(configured_dir).expanduser()
            if not candidate.is_absolute():
                candidate = (repo_root / candidate).resolve()
            return candidate
        return (repo_root / "artifacts").resolve()

    candidate = Path(output_dir).expanduser()
    if not candidate.is_absolute():
        candidate = (repo_root / candidate).resolve()
    return candidate


def run_training_pipeline(output_dir: Path | str | None = None) -> Dict[str, Any]:
    """Run the end-to-end training workflow and save model and metrics artifacts."""
    artifact_dir = resolve_artifact_dir(output_dir)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    data = load_dataset()
    train_df, test_df = split_dataset(data, test_size=0.2, random_state=7)
    metrics = train_and_evaluate_model(train_df, test_df, random_state=7)

    model = LogisticRegression(max_iter=500, solver="lbfgs", random_state=7)
    model.fit(train_df[FEATURE_COLUMNS], train_df[TARGET_COLUMN])

    model_path = save_model(model, artifact_dir / "iris_classifier.joblib")
    metrics_path = save_metrics(metrics, artifact_dir / "metrics.json")
    return {
        "model_path": model_path,
        "metrics_path": metrics_path,
        "metrics": metrics,
        "artifact_dir": artifact_dir,
    }
