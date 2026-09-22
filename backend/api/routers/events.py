from fastapi import APIRouter, Depends, status

from api.schemas.events import EventCreate, EventResponse
from application.services.application_service import EventApplicationService
from application.commands.events import IngestEventCommand
from api.dependencies import get_event_application_service

router = APIRouter()

@router.post(
    "",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED,
)

async def ingest_event(
    event: EventCreate,
    service: EventApplicationService = Depends(get_event_application_service),
) -> EventResponse:
    
    command = IngestEventCommand(**event.model_dump())
    result = await service.ingest_event(command)

    return EventResponse.model_validate(result)