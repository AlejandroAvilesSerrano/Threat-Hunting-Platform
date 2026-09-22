from fastapi import FastAPI
from api.routes import api_router
from composition.bootstrap import bootstrap


app = FastAPI(
    title="Threat Hunting Platform API",
    version="0.1.0",
)

app.include_router(api_router)