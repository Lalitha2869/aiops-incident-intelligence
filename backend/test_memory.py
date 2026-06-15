from backend.workflows.incident_graph import (
    graph
)

config = {
    "configurable": {
        "thread_id": "incident-001"
    }
}

result = graph.invoke(
    {
        "logs":
        """
        Database connection timeout.
        Connection pool exhausted.
        """
    },
    config=config
)

print(result)