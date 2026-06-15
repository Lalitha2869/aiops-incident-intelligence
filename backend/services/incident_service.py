from backend.database.db import SessionLocal
from backend.database.models import Incident


def save_incident(result, logs):

    db = SessionLocal()

    try:

        analysis = result["analysis"]

        rca = result["rca"]

        recommendations = result["recommendations"]

        incident = Incident(

            incident_id=f"INC-{db.query(Incident).count()+1:03}",

            title=analysis.error_type,

            severity=analysis.severity,

            status="Open",

            logs=logs,

            summary=analysis.summary,

            affected_service=analysis.affected_service,

            error_type=analysis.error_type,

            root_cause=rca["root_cause"],

            recommendation="\n".join(
                recommendations["recommendations"]
            )
        )

        db.add(incident)

        db.commit()

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

        print("INCIDENTS FOUND:", len(incidents))

        for incident in incidents:
            print(
                incident.incident_id,
                incident.severity
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