import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_sectoral_trend

def sectoral_trend_over_time():
    data = fetch_sectoral_trend()
    if not data:
        st.warning("No sectoral trend data available.")
        return

    # Normalize to long-form DataFrame
    all_rows = []
    for sector, values in data.items():
        dates = values.get("labels", [])
        emissions = values.get("data", [])
        for date, emission in zip(dates, emissions):
            all_rows.append({
                "Date": pd.to_datetime(date),
                "Sector": sector.capitalize(),
                "Emissions (kg)": emission
            })
    
    df = pd.DataFrame(all_rows)

    st.markdown("#### National Sectoral Emissions Over Time")

    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y("Emissions (kg):Q"),
        color=alt.Color("Sector:N", title="Sector"),
        tooltip=["Date:T", "Sector:N", "Emissions (kg):Q"]
    ).properties(
        width="container",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
