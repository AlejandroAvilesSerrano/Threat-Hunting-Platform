from application.commands.events import IngestEventCommand
from application.dto.events import EventDTO

class IngestEventUC:

    def __init__(self):
        ...

    async def ingest_event(self, iec: IngestEventCommand) -> EventDTO:
        ...