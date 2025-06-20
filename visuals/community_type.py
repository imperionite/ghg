import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_aggregated_by_type

def community_type_bar():
    data = fetch_aggregated_by_type()
    if not data:
        st.warning("No data available for community type emissions.")
        return

    df = pd.DataFrame(data)
    df["average_emissions"] = df["total_emissions"] / df["count"]

    st.markdown("#### Average Emissions per Community Type (kg CO₂e)")
    
    chart = alt.Chart(df).mark_bar(opacity=0.6).encode(  # Set opacity here
        x=alt.X("community_type:N", title="Community Type"),
        y=alt.Y("average_emissions:Q", title="Average CO₂e Emissions (kg)"),
        tooltip=["community_type", "average_emissions", "count"]
    ).properties(
        width="container",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
