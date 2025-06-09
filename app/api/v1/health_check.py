from fastapi import APIRouter, status
from datetime import datetime

module_name = 'health_check'
module_text = 'HealthCheck'
router = APIRouter(
    prefix=f"/{module_name}",
    tags=[module_name]
)


@router.head("/", status_code=status.HTTP_200_OK)
@router.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    """Simple health check endpoint that returns the current time"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "message": "API is running correctly"
    }
