import json

from backend.services.llm_service import get_llm
from backend.prompts.recommendation_prompt import (
    RECOMMENDATION_PROMPT
)
from langsmith import traceable
@traceable(name="generate_recommendations")

def generate_recommendations(root_cause):

    client = get_llm()

    prompt = RECOMMENDATION_PROMPT.format(
        root_cause=root_cause
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