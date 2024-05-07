from fastapi import APIRouter
from models import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return {"message": "Healthy"}
