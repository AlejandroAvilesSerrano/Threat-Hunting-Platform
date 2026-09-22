from application.commands.events import IngestEventCommand
from application.dto.events import EventDTO

#Revisar no devuelve DTO a API
class EventApplicationService:
    
    async def ingest_event(self, command: IngestEventCommand) -> EventDTO:
        return EventDTO(
            id="temporary-event-id",
            **command.__dict__,
        )