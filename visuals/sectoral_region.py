import streamlit as st
import pandas as pd
import requests
from utils.api import fetch_sectoral_by_region
import altair as alt

def sectoral_region_bar():
    data = fetch_sectoral_by_region()
    if not data:
        st.warning("No sectoral emissions data by region.")
        return

    # Transform from dict of region → {labels, data} into DataFrame
    records = []
    for region, d in data.items():
        for sector, value in zip(d["labels"], d["data"]):
            records.append({"region": region, "sector": sector, "emissions": value})

    df = pd.DataFrame(records)

    st.markdown("#### Sectoral Emissions per Region (kg CO₂e)")
    
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("region:N", title="Region"),
        y=alt.Y("emissions:Q", title="Total CO₂e Emissions (kg)"),
        color="sector:N",
        tooltip=["region", "sector", "emissions"]
    ).properties(
        width="container",
        height=450
    )

    st.altair_chart(chart, use_container_width=True)
