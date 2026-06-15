from fastapi import FastAPI

from backend.api.incidents import router as incident_router
from backend.api.health import router as health_router

app = FastAPI(
    title="AIOps Platform"
)

@app.get("/")
def root():
    return {
        "message": "AIOps Platform Running"
    }

app.include_router(incident_router)
app.include_router(health_router)