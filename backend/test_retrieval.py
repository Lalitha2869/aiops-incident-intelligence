from backend.agents.retrieval_agent import (
    retrieve_similar_incidents
)

results = retrieve_similar_incidents(
    "Database connection timeout"
)

print("Results:", results)

for row in results:
    print(row)