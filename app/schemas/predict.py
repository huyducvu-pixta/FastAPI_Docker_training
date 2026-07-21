from pydantic import BaseModel


class PredictRequest(BaseModel):
    image_path: str


class PredictV1Response(BaseModel):
    predicted_class: int


class PredictV2Response(PredictV1Response):
    confidence: float
    execution_time: float
