from pathlib import Path

from app.models.cnn import CNN
from app.models.mlp import MLP

APP_DIR = Path(__file__).resolve().parents[1]

MODELS = {
    "mlp": {
        "name": "mlp",
        "class": MLP,
        "weight_path": APP_DIR / "model_weights" / "mnist_mlp.pth",
    },
    "cnn": {
        "name": "cnn",
        "class": CNN,
        "weight_path": APP_DIR / "model_weights" / "mnist_cnn.pth",
    },
}


def list_models():
    return [
        {
            "name": model["name"],
            "weight_path": str(model["weight_path"]),
            "available": model["weight_path"].exists(),
        }
        for model in MODELS.values()
    ]


def get_model_info(model_name: str):
    return MODELS.get(model_name.lower())

