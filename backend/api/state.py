from typing import Protocol
from fastapi import FastAPI
from application.services.application_service import EventApplicationService


class APIComponents(Protocol):
    event_application_service: EventApplicationService


def configure_app_state(app: FastAPI, components: APIComponents) -> None:
    app.state.event_application_service = components.event_application_service