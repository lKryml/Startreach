from fastapi import APIRouter
from models import HealthResponse

route = APIRouter()


@route.get("/health", response_model=HealthResponse)
def health_check():
    return {"message": "Healthy"}