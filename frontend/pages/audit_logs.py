import gradio as gr

from backend.services.audit_service import (
    get_audit_logs
)


def load_audit_logs():

    return get_audit_logs()


def audit_logs_page():

    gr.Markdown(
        "## 📜 Audit Logs"
    )

    refresh_btn = gr.Button(
        "🔄 Refresh Audit Logs"
    )

    audit_table = gr.Dataframe(
        headers=[
            "Username",
            "Action",
            "Timestamp"
        ]
    )

    refresh_btn.click(
        fn=load_audit_logs,
        outputs=audit_table
    )