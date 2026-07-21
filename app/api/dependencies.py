from app.services.inference_service import InferenceService
from app.services.model_loader import ModelLoader


model_loader = ModelLoader()
inference_service = InferenceService(model_loader)


def get_model_loader():
    return model_loader


def get_inference_service():
    return inference_service
