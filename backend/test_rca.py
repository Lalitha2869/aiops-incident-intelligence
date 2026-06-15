# backend/test_rca.py

from backend.agents.rca_agent import (
    generate_rca
)

incident = """
Database connection timeout.
Connection pool exhausted.
"""

history = """
INC-001:
Database timeout caused by pool exhaustion.

Resolution:
Increase pool size.

INC-004:
Connection pool reached limit.
"""

result = generate_rca(
    incident,
    history
)

print(result)