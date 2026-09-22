from fastapi import APIRouter
from api.routers import events

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    events.router,
    prefix="/events",
    tags=["events"],
)