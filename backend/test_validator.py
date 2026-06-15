from backend.agents.validator_agent import (
    validate_incident
)

result = validate_incident(
    root_cause="Connection pool size too small for current load",
    recommendations="""
    Increase pool size.
    Configure monitoring.
    Review timeout settings.
    """
)

print(result)