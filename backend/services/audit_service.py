from backend.database.db import SessionLocal
from backend.database.models import AuditLog


def log_action(
    username,
    action
):

    db = SessionLocal()

    try:

        audit = AuditLog(
            username=username,
            action=action
        )

        db.add(audit)

        db.commit()

    finally:

        db.close()


def get_audit_logs():

    db = SessionLocal()

    try:

        logs = db.query(
            AuditLog
        ).all()

        return [
            [
                log.username,
                log.action,
                str(log.timestamp)
            ]
            for log in logs
        ]

    finally:

        db.close()