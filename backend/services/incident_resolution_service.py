from backend.database.db import SessionLocal
from backend.database.models import Incident


def get_open_incidents():

    db = SessionLocal()

    try:

        incidents = (
            db.query(Incident)
            .filter(
                Incident.status == "Open"
            )
            .all()
        )

        return [
            incident.incident_id
            for incident in incidents
        ]

    finally:

        db.close()


def resolve_incident(incident_id):

    db = SessionLocal()

    try:

        incident = (
            db.query(Incident)
            .filter(
                Incident.incident_id == incident_id
            )
            .first()
        )

        if not incident:

            return "Incident Not Found"

        incident.status = "Resolved"

        db.commit()

        return f"{incident_id} Resolved Successfully"

    finally:

        db.close()