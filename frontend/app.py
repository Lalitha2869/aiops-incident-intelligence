import gradio as gr

from users import USERS

from pages.dashboard import dashboard_page
from pages.incidents import incidents_page
from pages.rca_view import rca_page
from pages.recommendations import recommendations_page
from pages.approvals import approvals_page
from pages.audit_logs import audit_logs_page


# ==========================================
# LOGIN
# ==========================================

def login(username, password):

    user = USERS.get(username)

    if not user:
        return (
            "❌ Invalid Username",
            gr.update(visible=True),
            gr.update(visible=False)
        )

    if user["password"] != password:
        return (
            "❌ Invalid Password",
            gr.update(visible=True),
            gr.update(visible=False)
        )

    return (
        f"✅ Welcome {username} ({user['role']})",
        gr.update(visible=False),
        gr.update(visible=True)
    )


# ==========================================
# PAGE SWITCHING
# ==========================================

def show_dashboard():

    return (
        gr.update(visible=True),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False)
    )


def show_incidents():

    return (
        gr.update(visible=False),
        gr.update(visible=True),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False)
    )


def show_rca():

    return (
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=True),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False)
    )


def show_recommendations():

    return (
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=True),
        gr.update(visible=False),
        gr.update(visible=False)
    )


def show_approvals():

    return (
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=True),
        gr.update(visible=False)
    )


def show_audit():

    return (
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=True)
    )


def logout():

    return (
        gr.update(
            visible=True
        ),
        gr.update(
            visible=False
        )
    )
# ==========================================
# UI
# ==========================================

with gr.Blocks(
    title="AIOps Platform"
) as demo:

    # -------------------------
    # LOGIN PAGE
    # -------------------------

    with gr.Column(visible=True) as login_page:

        gr.Markdown(
            "# 🚀 AIOps Incident Intelligence Platform"
        )

        username = gr.Textbox(
            label="Username"
        )

        password = gr.Textbox(
            label="Password",
            type="password"
        )

        login_status = gr.Textbox(
            label="Status"
        )

        login_btn = gr.Button(
            "Login"
        )

    # -------------------------
    # DASHBOARD AREA
    # -------------------------

    with gr.Column(visible=False) as dashboard_area:

        gr.Markdown(
            "# 🚀 AIOps Platform"
        )

        with gr.Row():

            # SIDEBAR

            with gr.Column(scale=1):

                dashboard_btn = gr.Button(
                    "📊 Dashboard"
                )

                incidents_btn = gr.Button(
                    "🚨 Incidents"
                )

                rca_btn = gr.Button(
                    "🔍 RCA"
                )

                recommendations_btn = gr.Button(
                    "💡 Recommendations"
                )

                approvals_btn = gr.Button(
                    "🛡 Approvals"
                )

                audit_btn = gr.Button(
                    "📜 Audit Logs"
                )

                gr.Markdown("---")

                gr.Markdown(
                    """
                    ### 👤 User

                    Admin

                    Role: Administrator
                    """
                )

                logout_btn = gr.Button(
                    "🚪 Logout"
                )

            # MAIN CONTENT

            with gr.Column(scale=5):

                with gr.Column(
                    visible=True
                ) as dashboard_view:

                    dashboard_page()

                with gr.Column(
                    visible=False
                ) as incidents_view:

                    incidents_page()

                with gr.Column(
                    visible=False
                ) as rca_view:

                    rca_page()

                with gr.Column(
                    visible=False
                ) as recommendations_view:

                    recommendations_page()

                with gr.Column(
                    visible=False
                ) as approvals_view:

                    approvals_page()

                with gr.Column(
                    visible=False
                ) as audit_view:

                    audit_logs_page()

    # -------------------------
    # LOGIN ACTION
    # -------------------------

    login_btn.click(
        login,
        [username, password],
        [
            login_status,
            login_page,
            dashboard_area
        ]
    )

    # -------------------------
    # NAVIGATION
    # -------------------------

    outputs = [
        dashboard_view,
        incidents_view,
        rca_view,
        recommendations_view,
        approvals_view,
        audit_view
    ]

    dashboard_btn.click(
        show_dashboard,
        outputs=outputs
    )

    incidents_btn.click(
        show_incidents,
        outputs=outputs
    )

    rca_btn.click(
        show_rca,
        outputs=outputs
    )

    recommendations_btn.click(
        show_recommendations,
        outputs=outputs
    )

    approvals_btn.click(
        show_approvals,
        outputs=outputs
    )

    audit_btn.click(
        show_audit,
        outputs=outputs
    )

    logout_btn.click(
    logout,
    outputs=[
        login_page,
        dashboard_area
    ]
)

import os


demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.getenv("PORT", 7860))
)