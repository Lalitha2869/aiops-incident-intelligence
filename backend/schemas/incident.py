from pydantic import BaseModel


class IncidentCreate(BaseModel):
    incident_id: str
    title: str
    severity: str
    logs: str