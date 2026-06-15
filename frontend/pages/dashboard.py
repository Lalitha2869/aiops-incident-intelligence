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

from components.cards import kpi_card

from backend.services.dashboard_service import (
    get_dashboard_metrics,
    get_recent_incidents
)


def load_dashboard():

    active, critical, resolved = (
        get_dashboard_metrics()
    )

    return (
        kpi_card(
            "Active Incidents",
            str(active),
            "#2563EB"
        ),

        kpi_card(
            "Critical",
            str(critical),
            "#EF4444"
        ),

        kpi_card(
            "Resolved",
            str(resolved),
            "#22C55E"
        ),

        get_recent_incidents()
    )


def dashboard_page():

    gr.Markdown(
        "## 📊 AIOps Dashboard"
    )

    refresh_btn = gr.Button(
        "🔄 Refresh Dashboard"
    )

    with gr.Row():

        active_card = gr.HTML()

        critical_card = gr.HTML()

        resolved_card = gr.HTML()

    incidents_table = gr.Dataframe(
        headers=[
            "Incident ID",
            "Severity",
            "Status",
            "Service"
        ]
    )

    refresh_btn.click(
        fn=load_dashboard,
        outputs=[
            active_card,
            critical_card,
            resolved_card,
            incidents_table
        ]
    )

    