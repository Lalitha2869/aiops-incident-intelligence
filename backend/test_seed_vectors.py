# backend/test_seed_vectors.py

from backend.services.vector_store import (
    store_incident_vector
)

store_incident_vector(
    "INC-002",
    "Redis connection refused"
)

store_incident_vector(
    "INC-003",
    "API Gateway timeout"
)

store_incident_vector(
    "INC-004",
    "Database connection timeout due to pool exhaustion"
)

print("Seed Data Inserted")