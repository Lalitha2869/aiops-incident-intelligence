from backend.services.embedding_service import (
    generate_embedding
)

result = generate_embedding(
    "Database connection timeout"
)

print(type(result))

print(len(result))

print(result[:10])