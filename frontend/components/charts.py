import pandas as pd
import plotly.express as px


def incident_trend_chart():

    df = pd.DataFrame(
        {
            "Day": [
                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"
            ],
            "Incidents": [
                8,
                12,
                15,
                10,
                14,
                9,
                12
            ]
        }
    )

    fig = px.line(
        df,
        x="Day",
        y="Incidents",
        markers=True,
        title="Incident Trend"
    )

    return fig