from datetime import datetime
from pathlib import Path
from uuid import uuid4
from app.services.model_loader import ModelLoader
import torch
from fastapi import HTTPException
from PIL import Image

class InferenceService:
    def __init__(self, model_loader : ModelLoader):
        self.model_loader = model_loader
        self.device = model_loader.device
        self.sample_dir = Path(__file__).resolve().parents[1] / "test_samples"
        self.predict_history =[]

    def predict(self, path: str):
        sample_path = self.sample_dir / path
        if not sample_path.exists():
            raise HTTPException(status_code=404, detail=f"Sample '{path}' not found.")
        image = Image.open(sample_path).convert("L")
        x = torch.tensor(list(image.getdata()), dtype=torch.float32).view(1, 1, 28, 28) / 255
        x = x.to(self.device)

        model = self.model_loader.load_model()

        with torch.no_grad():
            y = model(x)
            predicted_class = y.argmax(dim=1).item()
            confidence = torch.softmax(y, dim=1)[0, predicted_class].item()

        prediction ={
            "id": str(uuid4()),
            "model_name": self.model_loader.get_activated_model(),
            "model_path": self.model_loader.get_activated_model_path(),
            "predicted_class": predicted_class,
            "confidence": confidence,
            "timestamp": datetime.now().isoformat(),
        }
        self.predict_history.append(prediction)
        return prediction


    def list_predict_history(self):
        return self.predict_history
    
    def get_prediction_by_id(self, prediction_id: str):
        for prediction in self.predict_history:
            if prediction["id"] == prediction_id:
                return prediction
        raise HTTPException(status_code=404, detail=f"Prediction with ID '{prediction_id}' not found.")
    
    def delete_prediction_by_id(self, prediction_id: str):
        removing_prediction = self.get_prediction_by_id(prediction_id)
        self.predict_history.remove(removing_prediction)
        return {"message": "Prediction deleted", "id": prediction_id} 
    
    
        