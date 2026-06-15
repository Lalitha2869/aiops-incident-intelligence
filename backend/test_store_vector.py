from backend.services.vector_store import (
    store_incident_vector
)

store_incident_vector(
    incident_id="INC-001",
    content="Database connection timeout. Connection pool exhausted."
)

print("Vector Stored Successfully")