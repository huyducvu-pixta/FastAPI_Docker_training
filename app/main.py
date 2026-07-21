from fastapi import FastAPI

from app.api.routers import deploy, models, predict


app = FastAPI(title="MNIST Model API")

app.include_router(models.router)
app.include_router(deploy.router)
app.include_router(predict.router)


@app.get("/")
def root():
    return {"message": "MNIST Model API"}
