from backend.database.db import SessionLocal
from backend.database.models import Incident


def get_dashboard_metrics():

    db = SessionLocal()

    try:

        active_incidents = db.query(
            Incident
        ).count()

        critical_incidents = db.query(
            Incident
        ).filter(
            Incident.severity.in_(
                ["High", "Critical"]
            )
        ).count()

        resolved_incidents = db.query(
            Incident
        ).filter(
            Incident.status == "Resolved"
        ).count()

        return (
            active_incidents,
            critical_incidents,
            resolved_incidents
        )

    finally:

        db.close()


def get_recent_incidents():

    db = SessionLocal()

    try:

        incidents = (
            db.query(Incident)
            .order_by(
                Incident.created_at.desc()
            )
            .limit(10)
            .all()
        )

        return [
            [
                incident.incident_id,
                incident.severity,
                incident.status,
                incident.affected_service
            ]
            for incident in incidents
        ]

    finally:

        db.close()