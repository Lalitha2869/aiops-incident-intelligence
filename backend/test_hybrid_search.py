from backend.services.hybrid_search import (
    hybrid_search
)

results = hybrid_search(
    "Database connection timeout"
)

for row in results:

    print(row)