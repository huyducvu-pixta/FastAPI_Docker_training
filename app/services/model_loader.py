import torch
from fastapi import HTTPException
from app.services.model_registry import get_model_info, list_models


class ModelLoader:
    def __init__(self):
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.activated_model_name = "cnn"
        self.cache = {}

    def get_activated_model(self):
        return self.activated_model_name
    
    
    def get_activated_model_path(self):
        model_info = get_model_info(self.activated_model_name)
        return str(model_info["weight_path"])
    
    def set_activated_model(self, model_name: str):
        self.load_model(model_name)
        self.activated_model_name = model_name
        return self.activated_model_name
    
    def load_model(self, model_name: str = None):
        if model_name is None:
            model_name = self.activated_model_name
        if model_name not in [model["name"] for model in list_models()]:
            raise HTTPException(status_code=404, detail=f"Model '{model_name}' not found.")
        model_info = get_model_info(model_name)

        model_class = model_info["class"]
        model = model_class().to(self.device)

        if model_name not in self.cache:
            model.load_state_dict(torch.load(model_info["weight_path"], map_location=self.device))
            model.eval()
            self.cache[model_name] = model

        return self.cache[model_name]
    
    def list_models(self):
        return list_models()