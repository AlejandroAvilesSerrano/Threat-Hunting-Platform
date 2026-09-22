from application.services.application_service import EventApplicationService
from application.use_cases.ingest_event_uc import IngestEventUC


class Bootstrap:
    def __init__(self) -> None:
        self.ingest_event_uc = IngestEventUC()
        self.event_application_service = EventApplicationService(
            ingest_event_uc=self.ingest_event_uc,
        )


def bootstrap() -> Bootstrap:
    return Bootstrap()