from fastapi import Request
from application.services.application_service import EventApplicationService


def get_event_application_service(request: Request) -> EventApplicationService:
    return request.app.state.event_application_service