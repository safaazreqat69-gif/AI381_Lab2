
from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}



def test_health_returns_json():
    response = client.get("/health")

    assert "application/json" in response.headers["content-type"]


from pathlib import Path
import joblib


def test_saved_model_loads():
    model_path = Path(__file__).resolve().parents[1] / "model.joblib"

    model = joblib.load(model_path)

    assert model is not None



def test_predict_endpoint():
    response = client.post(
        "/predict",
        json={"feature": 2}
    )

    assert response.status_code == 200
    assert "prediction" in response.json()


def test_predict_rejects_invalid_input():
    response = client.post(
        "/predict",
        json={"feature": "hello"}
    )

    assert response.status_code == 422



def test_prediction_is_deterministic():
    first_response = client.post(
        "/predict",
        json={"feature": 2}
    )

    second_response = client.post(
        "/predict",
        json={"feature": 2}
    )

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert (
        first_response.json()["prediction"]
        == second_response.json()["prediction"]
    )
