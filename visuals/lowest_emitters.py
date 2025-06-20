import streamlit as st
from utils.api import fetch_lowest_emitters
import pandas as pd

def lowest_emitters_table():
    data = fetch_lowest_emitters()
    if not data:
        st.warning("No data available for lowest emitters.")
        return

    st.markdown("#### Communities with the Lowest GHG Emissions")
    
    df = pd.DataFrame(data)
    df["Rank"] = range(1, len(df) + 1)
    df = df[["Rank", "community_name", "region", "city", "total_emissions", "global_percentile_rank"]]
    df.rename(columns={
        "community_name": "Community",
        "region": "Region",
        "city": "City",
        "total_emissions": "Total Emissions (kg)",
        "global_percentile_rank": "Global Rank (%)"
    }, inplace=True)

    st.dataframe(df, use_container_width=True)
