from backend.agents.recommendation_agent import (
    generate_recommendations
)

result = generate_recommendations(
    "Connection pool size too small for current load"
)

print(result)