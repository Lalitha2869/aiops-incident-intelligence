def kpi_card(
    title,
    value,
    color="#2563EB"
):

    return f"""
    <div style="
        background:white;
        padding:20px;
        border-radius:12px;
        text-align:center;
        box-shadow:0 4px 12px rgba(0,0,0,0.15);
        border-top:5px solid {color};
    ">
        <h3>{title}</h3>
        <h1>{value}</h1>
    </div>
    """