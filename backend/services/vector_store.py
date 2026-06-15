# backend/services/vector_store.py

from sqlalchemy import text
from backend.database.vector_db import VectorSessionLocal
from backend.services.embedding_service import generate_embedding


def store_incident_vector(
    incident_id: str,
    content: str
):

    embedding = generate_embedding(content)

    db = VectorSessionLocal()

    try:

        db.execute(
            text("""
                INSERT INTO incident_vectors
                (incident_id, content, embedding)
                VALUES
                (:incident_id, :content, :embedding)
            """),
            {
                "incident_id": incident_id,
                "content": content,
                "embedding": str(embedding)
            }
        )

        db.commit()

    finally:
        db.close()