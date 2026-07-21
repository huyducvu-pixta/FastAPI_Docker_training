from fastapi import APIRouter, Depends

from app.api.dependencies import get_inference_service
from app.schemas.predict import PredictRequest, PredictV1Response, PredictV2Response
from app.services.inference_service import InferenceService


router = APIRouter(prefix="/api/predict", tags=["predict"])


@router.post("/v1", response_model=PredictV1Response)
def create_prediction_v1(
    request: PredictRequest,
    inference_service: InferenceService = Depends(get_inference_service),
):
    return inference_service.predict(request.image_path)


@router.post("/v2", response_model=PredictV2Response)
def create_prediction_v2(
    request: PredictRequest,
    inference_service: InferenceService = Depends(get_inference_service),
):
    return inference_service.predict(request.image_path)


@router.get("")
def get_predictions(inference_service: InferenceService = Depends(get_inference_service)):
    return inference_service.list_predict_history()


@router.get("/{predict_id}")
def get_prediction(
    predict_id: str,
    inference_service: InferenceService = Depends(get_inference_service),
):
    return inference_service.get_prediction_by_id(predict_id)


@router.delete("/{predict_id}")
def delete_prediction(
    predict_id: str,
    inference_service: InferenceService = Depends(get_inference_service),
):
    return inference_service.delete_prediction_by_id(predict_id)
