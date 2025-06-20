import streamlit as st
import pandas as pd
import plotly.express as px

def region_emissions_bar(data):
    if not data:
        st.warning("No regional data to show.")
        return

    df = pd.DataFrame(data)
    totals = df.groupby("region")["total_emissions"].sum().reset_index()

    fig = px.bar(
        totals,
        x="region", y="total_emissions",
        title="Total Emissions by Region",
        labels={"total_emissions": "Emissions (kg CO2e)"},
        color_discrete_sequence=["#264653"]
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
