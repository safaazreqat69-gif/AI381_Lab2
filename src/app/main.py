
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI381 Lab 2 API")

MODEL_PATH = Path(__file__).resolve().parents[2] / "model.joblib"
model = joblib.load(MODEL_PATH)


class PredictionInput(BaseModel):
    features: list[float] = Field(min_length=38, max_length=38)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: PredictionInput):
    columns = getattr(model, "feature_names_in_", None)

    if columns is None:
        columns = getattr(
            model.named_steps["scaler"], "feature_names_in_", None
        )

    if columns is not None:
        input_data = pd.DataFrame([data.features], columns=columns)
        prediction = model.predict(input_data)
    else:
        prediction = model.predict([data.features])

    return {"prediction": int(prediction[0])}
