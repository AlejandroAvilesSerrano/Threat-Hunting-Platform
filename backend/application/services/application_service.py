from application.use_cases.ingest_event_uc import IngestEventUC
from application.commands.events import IngestEventCommand
from application.dto.events import EventDTO

#Revisar no devuelve DTO a API
class EventApplicationService:
    def __init__(self, ingest_event_uc: IngestEventUC):
        self.ingest_event_uc = ingest_event_uc

    async def ingest_event(self, command: IngestEventCommand) -> EventDTO:
        result = await self.ingest_event_uc.ingest_event(command)
        return result 