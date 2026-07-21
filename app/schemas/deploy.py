from pydantic import BaseModel

class DeployRequest(BaseModel):
    model_name: str


class DeployResponse(BaseModel):
    activated_model: str