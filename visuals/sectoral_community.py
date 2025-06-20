import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_sectoral_by_community_type

def sectoral_community_bar():
    data = fetch_sectoral_by_community_type()
    if not data:
        st.warning("No data found for sectoral emissions by community type.")
        return

    records = []
    for comm_type, d in data.items():
        for sector, value in zip(d["labels"], d["data"]):
            records.append({
                "community_type": comm_type,
                "sector": sector,
                "emissions": value
            })

    df = pd.DataFrame(records)

    st.markdown("#### Sectoral Emissions per Community Type (kg CO₂e)")

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("community_type:N", title="Community Type"),
        y=alt.Y("emissions:Q", title="Total CO₂e Emissions (kg)"),
        color="sector:N",
        tooltip=["community_type", "sector", "emissions"]
    ).properties(
        width="container",
        height=450
    )

    st.altair_chart(chart, use_container_width=True)
