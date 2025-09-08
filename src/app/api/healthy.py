from fastapi import APIRouter, status
from app.core.config import APP_NAME, APP_VERSION, APP_DESCRIPTION

router = APIRouter()

@router.get("/health",status_code=status.HTTP_200_OK, tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "app_description": APP_DESCRIPTION,
        "status": "Healthy"
    }