import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_region_trend

def regional_emission_trend():
    data = fetch_region_trend()
    if not data:
        st.warning("No regional emission trend data available.")
        return

    records = []
    for region, d in data.items():
        for date_str, value in zip(d["labels"], d["data"]):
            records.append({
                "region": region,
                "date": pd.to_datetime(date_str),
                "emissions": value
            })

    df = pd.DataFrame(records)

    st.markdown("#### Emission Trends Over Time by Region")

    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("emissions:Q", title="Total CO₂e Emissions (kg)"),
        color="region:N",
        tooltip=["region", "date", "emissions"]
    ).properties(
        width="container",
        height=450
    )

    st.altair_chart(chart, use_container_width=True)
