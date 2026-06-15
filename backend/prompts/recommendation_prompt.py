RECOMMENDATION_PROMPT = """
You are a Senior Site Reliability Engineer.

Based on the root cause analysis, generate:

1. Recommended actions
2. Priority level

Root Cause:

{root_cause}

Return JSON only:

{{
    "recommendations": [],
    "priority": ""
}}
"""