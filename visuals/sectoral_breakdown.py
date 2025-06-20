import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_sectoral_by_region

def sectoral_emissions_by_location():
    data = fetch_sectoral_by_region()
    if not data:
        st.warning("No sectoral regional data available.")
        return

    records = []
    for region, info in data.items():
        labels = info.get("labels", [])
        values = info.get("data", [])
        for sector, value in zip(labels, values):
            records.append({"Region": region, "Sector": sector.capitalize(), "Emissions (kg)": value})
    
    df = pd.DataFrame(records)

    st.markdown("#### Sectoral Emissions Breakdown per Region")

    neutral_palette = [
        "#6c757d", "#495057", "#adb5bd", "#868e96", "#343a40", "#ced4da"
    ]

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Region:N", title="Region"),
        y=alt.Y("Emissions (kg):Q", stack="normalize"),
        color=alt.Color(
            "Sector:N",
            title="Sector",
            scale=alt.Scale(range=neutral_palette)
        ),
        tooltip=["Region", "Sector", "Emissions (kg)"]
    ).properties(
        width="container",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
