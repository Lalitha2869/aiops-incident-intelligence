from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.schemas.incident import IncidentCreate
from backend.database.dependencies import get_db
from backend.database.models import Incident

router = APIRouter()


@router.post("/ingest-log")
def ingest_log(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):

    new_incident = Incident(
        incident_id=incident.incident_id,
        title=incident.title,
        severity=incident.severity,
        status="Open",
        logs=incident.logs
    )

    db.add(new_incident)
    db.commit()

    return {
        "message": "Incident Created Successfully"
    }