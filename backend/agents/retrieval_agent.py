from langsmith import traceable

from backend.services.hybrid_search import (
    hybrid_search
)

@traceable(name="retrieve_similar_incidents")
def retrieve_similar_incidents(query):

    print("Hybrid Search Started")

    results = hybrid_search(
        query
    )

    print(
        "Results Found:",
        len(results)
    )

    return results