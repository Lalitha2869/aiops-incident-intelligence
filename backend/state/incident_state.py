from typing import TypedDict


class IncidentState(TypedDict):

    logs: str

    analysis: dict

    retrieved_incidents: list

    rca: dict

    recommendations: dict

    validation: dict