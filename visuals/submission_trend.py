import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_timeseries

def submission_density_over_time():
    data = fetch_timeseries()
    if not data or "labels" not in data or "datasets" not in data:
        st.warning("No submission timeseries data available.")
        return

    dates = pd.to_datetime(data["labels"])
    values = data["datasets"][0]["data"]
    df = pd.DataFrame({"Date": dates, "Total Emissions (kg)": values})

    st.markdown("#### Daily GHG Submission Emissions Over Time")

    chart = alt.Chart(df).mark_area(
        line={"color": "#4BC0C0"},
        color=alt.Gradient(
            gradient="linear",
            stops=[{"offset": 0, "color": "#4BC0C099"}, {"offset": 1, "color": "#ffffff00"}],
            x1=1, x2=1, y1=1, y2=0
        )
    ).encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y("Total Emissions (kg):Q", title="Emissions"),
        tooltip=["Date", "Total Emissions (kg)"]
    ).properties(
        width="container",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
