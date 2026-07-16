from __future__ import annotations

import os
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

repo_root = Path(__file__).resolve().parents[1]
configured_dir = os.getenv("MODEL_ARTIFACT_DIR")
if configured_dir:
    artifact_dir = Path(configured_dir).expanduser()
    if not artifact_dir.is_absolute():
        artifact_dir = (repo_root / artifact_dir).resolve()
else:
    artifact_dir = (repo_root / "artifacts").resolve()

MODEL_PATH = artifact_dir / "iris_classifier.joblib"

st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")

if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)
else:
    st.warning("No trained model artifact found. Please run the training pipeline first.")
    st.stop()

st.title("Enterprise Iris Classifier")
st.write("Use the form below to generate an inference from the trained model.")

feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
class_names = ["setosa", "versicolor", "virginica"]

with st.form("prediction_form"):
    values = []
    for feature in feature_names:
        value = st.number_input(feature.replace("_", " ").title(), value=5.0, step=0.1, min_value=0.0, max_value=10.0)
        values.append(value)

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = pd.DataFrame([values], columns=feature_names)
    prediction = model.predict(payload)[0]
    st.success(f"Predicted class: {class_names[int(prediction)]}")
