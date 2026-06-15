import gradio as gr

from frontend.app_state import (
    WORKFLOW_RESULT
)
from backend.services.audit_service import (
    log_action
)


def load_recommendations():

    if not WORKFLOW_RESULT:

        return (
            "No recommendations available",
            ""
        )

    log_action(
        "admin",
        "Viewed Recommendations"
    )

    return (
        "\n".join(
            WORKFLOW_RESULT[
                "recommendations"
            ][
                "recommendations"
            ]
        ),

        WORKFLOW_RESULT[
            "recommendations"
        ][
            "priority"
        ]
    )


def recommendations_page():

    gr.Markdown(
        "## 💡 Recommendations"
    )

    recommendations = gr.Textbox(
        label="Recommendations",
        lines=10
    )

    priority = gr.Textbox(
        label="Priority"
    )

    refresh_btn = gr.Button(
        "Refresh Recommendations"
    )

    refresh_btn.click(
        load_recommendations,
        outputs=[
            recommendations,
            priority
        ]
    )