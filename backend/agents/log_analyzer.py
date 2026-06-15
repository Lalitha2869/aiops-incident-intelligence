# backend/agents/log_analyzer.py

import json

from backend.services.llm_service import get_llm
from backend.prompts.log_prompt import LOG_ANALYZER_PROMPT
from backend.schemas.log_analysis import LogAnalysis


def analyze_log(log_text: str):

    client = get_llm()

    prompt = LOG_ANALYZER_PROMPT.format(
        log_text=log_text
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "Analyze logs carefully. "
                    "Reason step-by-step internally. "
                    "Return only valid JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = json.loads(
        response.choices[0].message.content
    )

    return LogAnalysis(**result)