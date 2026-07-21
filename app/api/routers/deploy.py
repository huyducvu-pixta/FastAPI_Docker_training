from fastapi import APIRouter, Depends

from app.api.dependencies import get_model_loader
from app.schemas.deploy import DeployRequest, DeployResponse
from app.services.model_loader import ModelLoader


router = APIRouter(prefix="/api/deploy", tags=["deploy"])


@router.get("/current", response_model=DeployResponse)
def get_current_model(model_loader: ModelLoader = Depends(get_model_loader)):
    return {"activated_model": model_loader.get_activated_model()}


@router.put("/current", response_model=DeployResponse)
def update_current_model(
    request: DeployRequest,
    model_loader: ModelLoader = Depends(get_model_loader),
):
    active_model = model_loader.set_activated_model(request.model_name)
    return {"activated_model": active_model}
