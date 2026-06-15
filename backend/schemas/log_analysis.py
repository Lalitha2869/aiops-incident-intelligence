# backend/schemas/log_analysis.py

from pydantic import BaseModel
from typing import List


class LogAnalysis(BaseModel):
    summary: str
    affected_service: str
    error_type: str
    severity: str
    symptoms: List[str]