

from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI381 Lab 2 API")

MODEL_PATH = Path(__file__).resolve().parents[2] / "model.joblib"
model = joblib.load(MODEL_PATH)


class PredictionInput(BaseModel):
    feature: float


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: PredictionInput):
    prediction = model.predict([[data.feature]])
    return {"prediction": int(prediction[0])}
