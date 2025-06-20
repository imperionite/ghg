

import streamlit as st
import pandas as pd
import altair as alt
from utils.api import fetch_per_capita

def emissions_per_capita_chart():
    data = fetch_per_capita()
    if not data:
        st.warning("No per capita data available.")
        return

    df = pd.DataFrame(data)
    df["per_capita"] = df["total_emissions"] / df["population"]
    df = df.sort_values(by="per_capita", ascending=False)

    st.markdown("#### Per Capita Emissions by Region")

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("region:N", sort="-y", title="Region"),
        y=alt.Y("per_capita:Q", title="Emissions per Capita (kg)"),
        tooltip=["region", "per_capita"]
    ).properties(
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
