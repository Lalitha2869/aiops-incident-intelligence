from sqlalchemy import text

from backend.database.vector_db import (
    VectorSessionLocal
)

from backend.services.embedding_service import (
    generate_embedding
)


def hybrid_search(query):

    db = VectorSessionLocal()

    try:

        # Vector Search
        embedding = generate_embedding(query)

        vector_results = db.execute(
            text("""
                SELECT
                    incident_id,
                    content
                FROM incident_vectors
                ORDER BY embedding <=> CAST(:embedding AS vector)
                LIMIT 3
            """),
            {
                "embedding": str(embedding)
            }
        ).fetchall()

        # Keyword Search
        keyword_results = db.execute(
            text("""
                SELECT
                    incident_id,
                    content
                FROM incident_vectors
                WHERE content ILIKE :query
                LIMIT 3
            """),
            {
                "query": f"%{query}%"
            }
        ).fetchall()

        # Merge Results
        combined = []

        seen = set()

        for row in vector_results + keyword_results:

            if row[0] not in seen:

                combined.append(row)

                seen.add(row[0])

        return combined

    finally:

        db.close()