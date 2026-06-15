from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from datetime import datetime

from backend.database.base import Base


class Incident(Base):

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)

    incident_id = Column(String, unique=True)

    title = Column(String)

    severity = Column(String)

    status = Column(String)

    logs = Column(Text)
    summary = Column(Text)

    affected_service = Column(String)

    error_type = Column(String)

    root_cause = Column(Text)

    recommendation = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    username = Column(String)

    action = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )