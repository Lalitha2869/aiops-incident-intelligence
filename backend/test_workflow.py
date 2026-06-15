from backend.workflows.incident_graph import (
    graph
)

result = graph.invoke(
    {
        "logs": """
        Database connection timeout.
        Connection pool exhausted.
        """
    }
)

print("\n")
print("=" * 50)
print("FINAL OUTPUT")
print("=" * 50)
print(result)