from fastapi import FastAPI

from api.routes import api_router
from api.state import APIComponents, configure_app_state


def create_api_app(components: APIComponents) -> FastAPI:
    app = FastAPI(
        title="Threat Hunting Platform API",
        version="0.1.0",
    )

    configure_app_state(app, components)
    app.include_router(api_router)

    return app
