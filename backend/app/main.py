from fastapi import FastAPI

from app.api.dives import router as dives_router
from app.api.health import router as health_router

app = FastAPI(
    title="BlueDepth",
    version="0.1.0",
    description="Dive. Explore. Remember."
)

app.include_router(health_router)
app.include_router(dives_router)


@app.get("/")
def root():
    return {
        "application": "BlueDepth",
        "version": "0.1.0",
        "status": "Development"
    }