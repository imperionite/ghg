import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_sectoral_by_type

def sectoral_by_community_type():
    data = fetch_sectoral_by_type()
    if not data:
        st.warning("No data available for sectoral emissions by community type.")
        return

    records = []
    for ctype, entry in data.items():
        labels = entry.get("labels", [])
        values = entry.get("data", [])
        for sector, emission in zip(labels, values):
            records.append({
                "Community Type": ctype.capitalize(),
                "Sector": sector.capitalize(),
                "Emissions (kg)": emission
            })

    df = pd.DataFrame(records)

    st.markdown("#### Sectoral Breakdown: Urban vs. Rural")

    # Define a muted, neutral color palette
    neutral_palette = [
        "#6c757d",  # Muted gray
        "#495057",  # Darker gray
        "#adb5bd",  # Light gray
        "#868e96",  # Medium gray
        "#343a40",  # Almost black
        "#ced4da"   # Pale gray
    ]

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Community Type:N", title="Community Type"),
        y=alt.Y("Emissions (kg):Q", stack="normalize"),
        color=alt.Color(
            "Sector:N",
            title="Sector",
            scale=alt.Scale(range=neutral_palette)
        ),
        tooltip=["Community Type", "Sector", "Emissions (kg)"]
    ).properties(
        width="container",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
