import json

from backend.services.llm_service import get_llm
from backend.prompts.rca_prompt import RCA_PROMPT
from langsmith import traceable

@traceable(name="generate_rca")
def generate_rca(
    incident,
    historical_context
):

    client = get_llm()

    prompt = RCA_PROMPT.format(
        incident=incident,
        historical_context=historical_context
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