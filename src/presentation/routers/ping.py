from fastapi import APIRouter
from application.ping_service import PingService

router = APIRouter()
ping_service = PingService()


@router.get("/ping")
def ping():
    return {"message": ping_service.ping()}
