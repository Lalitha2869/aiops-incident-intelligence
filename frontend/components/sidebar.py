import gradio as gr


def build_sidebar():

    with gr.Column(scale=1):

        gr.Markdown("## Navigation")

        dashboard_btn = gr.Button("📊 Dashboard")

        incidents_btn = gr.Button("🚨 Incidents")

        rca_btn = gr.Button("🔍 RCA")

        recommendations_btn = gr.Button(
            "💡 Recommendations"
        )

        approvals_btn = gr.Button(
            "🛡 Approvals"
        )

        audit_btn = gr.Button(
            "📜 Audit Logs"
        )
        logout_btn = gr.Button(
            "🚪 Logout"
        )

    return (
        dashboard_btn,
        incidents_btn,
        rca_btn,
        recommendations_btn,
        approvals_btn,
        audit_btn
    )