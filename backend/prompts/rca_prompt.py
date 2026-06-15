RCA_PROMPT = """
You are a Senior Site Reliability Engineer.

Analyze:

1. Current Incident
2. Historical Similar Incidents

Determine:

1. Most likely root cause
2. Confidence level

Current Incident:

{incident}

Historical Context:

{historical_context}

Return JSON only:

{{
    "root_cause":"",
    "confidence":""
}}
"""