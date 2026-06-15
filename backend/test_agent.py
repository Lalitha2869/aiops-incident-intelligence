# backend/test_agent.py

from backend.agents.log_analyzer import analyze_log

log = """
ERROR Database connection timeout
ERROR Connection pool exhausted
WARN High latency detected
"""

result = analyze_log(log)

print(result.model_dump_json(indent=4))