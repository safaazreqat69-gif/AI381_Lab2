
from pathlib import Path

import joblib
from sklearn.dummy import DummyClassifier


def train_model():
    model = DummyClassifier(strategy="most_frequent")

    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]

    model.fit(X, y)

    model_path = Path(__file__).resolve().parents[2] / "model.joblib"
    joblib.dump(model, model_path)

    return model_path


if __name__ == "__main__":
    print(f"Model saved to: {train_model()}")
