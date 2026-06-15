import gradio as gr

from backend.services.incident_resolution_service import (
    get_open_incidents,
    resolve_incident
)

from backend.services.audit_service import (
    log_action
)


def resolve_and_log(incident_id):

    result = resolve_incident(
        incident_id
    )

    log_action(
        "admin",
        f"Resolved {incident_id}"
    )

    return result


def approvals_page():

    gr.Markdown(
        "## ✅ Incident Resolution"
    )

    incident_dropdown = gr.Dropdown(
        choices=get_open_incidents(),
        label="Open Incidents"
    )

    resolve_btn = gr.Button(
        "Resolve Incident"
    )

    result_box = gr.Textbox(
        label="Result"
    )

    refresh_btn = gr.Button(
        "Refresh Incidents"
    )

    refresh_btn.click(
        fn=get_open_incidents,
        outputs=incident_dropdown
    )

    resolve_btn.click(
        fn=resolve_and_log,
        inputs=incident_dropdown,
        outputs=result_box
    )