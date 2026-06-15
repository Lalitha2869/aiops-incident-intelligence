import json

from backend.services.llm_service import get_llm
from backend.prompts.validator_prompt import (
    VALIDATOR_PROMPT
)


def validate_incident(
    root_cause,
    recommendations
):

    client = get_llm()

    prompt = VALIDATOR_PROMPT.format(
        root_cause=root_cause,
        recommendations=recommendations
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        response_format={
            "type": "json_object"
        },
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(
        response.choices[0].message.content
    )