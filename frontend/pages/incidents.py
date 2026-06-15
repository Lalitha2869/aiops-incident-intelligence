import gradio as gr
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)

from frontend.app_state import (
    WORKFLOW_RESULT
)

from frontend.dashboard_state import (
    DASHBOARD_DATA
)
from backend.workflows.incident_graph import (
    graph
)

from backend.services.audit_service import (
    log_action
)

from backend.services.incident_service import (
    save_incident
)
def analyze_incident(logs):

    result = graph.invoke(
        {
            "logs": logs
        }
    )
    save_incident(
    result,
    logs
)
    WORKFLOW_RESULT.clear()

    WORKFLOW_RESULT.update(
        result
    )

    log_action(
        "admin",
        "Analyzed Incident"
    )
    WORKFLOW_RESULT.update(
    result
)





    analysis = result["analysis"]

    return (
        analysis.summary,
        analysis.affected_service,
        analysis.error_type,
        analysis.severity,
        "\n".join(
            analysis.symptoms
        )
    )

def incidents_page():

    gr.Markdown(
        "## 🚨 Incident Analysis"
    )

    logs = gr.Textbox(
        label="Paste Incident Logs",
        lines=8,
        placeholder="""
Database connection timeout.
Connection pool exhausted.
"""
    )

    analyze_btn = gr.Button(
        "🔍 Analyze Incident",
        variant="primary"
    )

    gr.Markdown(
        "## 📊 Analysis Results"
    )

    summary = gr.Textbox(
        label="Summary",
        lines=3
    )

    service = gr.Textbox(
        label="Affected Service"
    )

    error_type = gr.Textbox(
        label="Error Type"
    )

    severity = gr.Textbox(
        label="Severity"
    )

    symptoms = gr.Textbox(
        label="Symptoms",
        lines=4
    )

    analyze_btn.click(
        fn=analyze_incident,
        inputs=logs,
        outputs=[
            summary,
            service,
            error_type,
            severity,
            symptoms
        ]
    )