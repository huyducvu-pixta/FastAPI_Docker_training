from pydantic import BaseModel


class PredictRequest(BaseModel):
    image_path: str


class PredictResponse(BaseModel):
    id: str
    model_name: str
    predicted_class: int
    confidence: float
