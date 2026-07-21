from fastapi import APIRouter, Depends

from app.api.dependencies import get_model_loader
from app.services.model_loader import ModelLoader


router = APIRouter(prefix="/api/models", tags=["models"])


@router.get("")
def get_models(model_loader: ModelLoader = Depends(get_model_loader)):
    return model_loader.list_models()
