from __future__ import annotations

from typing import Tuple

import pandas as pd
from sklearn.datasets import load_iris

FEATURE_COLUMNS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
TARGET_COLUMN = "target"
TARGET_NAME_COLUMN = "target_name"


def load_dataset() -> pd.DataFrame:
    """Load the Iris dataset into a tidy DataFrame."""
    iris = load_iris(as_frame=True)
    frame = iris.frame.copy()
    frame = frame.rename(
        columns={
            "sepal length (cm)": FEATURE_COLUMNS[0],
            "sepal width (cm)": FEATURE_COLUMNS[1],
            "petal length (cm)": FEATURE_COLUMNS[2],
            "petal width (cm)": FEATURE_COLUMNS[3],
        }
    )
    frame[TARGET_COLUMN] = iris.target
    frame[TARGET_NAME_COLUMN] = frame[TARGET_COLUMN].map({0: "setosa", 1: "versicolor", 2: "virginica"})
    return frame.loc[:, [*FEATURE_COLUMNS, TARGET_COLUMN, TARGET_NAME_COLUMN]].copy()


def split_dataset(data: pd.DataFrame, test_size: float = 0.2, random_state: int = 7) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Split the dataset into deterministic training and testing sets."""
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")

    shuffled = data.sample(frac=1.0, random_state=random_state).reset_index(drop=True)
    split_index = int(len(shuffled) * (1 - test_size))
    train_frame = shuffled.iloc[:split_index].copy()
    test_frame = shuffled.iloc[split_index:].copy()
    return train_frame, test_frame
