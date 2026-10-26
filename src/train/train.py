
from pathlib import Path

import joblib


def train_model():
    project_root = Path(__file__).resolve().parents[2]
    source_model = project_root / "CleanModel.pkl"

    if not source_model.exists():
        raise FileNotFoundError(
            f"Trained model not found: {source_model}"
        )

    model = joblib.load(source_model)

    if model.n_features_in_ != 38:
        raise ValueError("Expected a model with 38 input features.")

    output_path = project_root / "model.joblib"
    joblib.dump(model, output_path)

    return output_path


if __name__ == "__main__":
    print(f"Model saved to: {train_model()}")
