import gradio as gr

from frontend.app_state import (
    WORKFLOW_RESULT
)

from backend.services.audit_service import (
    log_action
)


def load_rca():

    if not WORKFLOW_RESULT:

        return (
            "No incident analyzed yet",
            "",
            ""
        )

    # Audit Entry
    log_action(
        "admin",
        "Viewed RCA"
    )

    historical = "\n".join(
        [
            f"{x[0]} - {x[1]}"
            for x in WORKFLOW_RESULT[
                "retrieved_incidents"
            ]
        ]
    )

    return (
        WORKFLOW_RESULT[
            "rca"
        ][
            "root_cause"
        ],

        WORKFLOW_RESULT[
            "rca"
        ][
            "confidence"
        ],

        historical
    )

def rca_page():

    gr.Markdown(
        "## 🔍 Root Cause Analysis"
    )

    root_cause = gr.Textbox(
        label="Root Cause"
    )

    confidence = gr.Textbox(
        label="Confidence"
    )

    historical = gr.Textbox(
        label="Historical Matches",
        lines=6
    )

    refresh_btn = gr.Button(
        "Refresh RCA"
    )

    refresh_btn.click(
        load_rca,
        outputs=[
            root_cause,
            confidence,
            historical
        ]
    )