from backend.services.audit_service import (
    log_action
)

log_action(
    "lalitha",
    "Approved Incident INC-001"
)

print(
    "Audit Logged"
)