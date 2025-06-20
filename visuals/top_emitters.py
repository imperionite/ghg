import streamlit as st
from utils.api import fetch_top_emitters_by_sector
import pandas as pd

def top_emitters_leaderboard():
    data = fetch_top_emitters_by_sector()
    if not data:
        st.warning("No data found for top emitters.")
        return

    st.markdown("#### Top GHG Contributors per Sector")

    for sector, emitters in data.items():
        st.markdown(f"##### 🏭 {sector.capitalize()} Sector")
        df = pd.DataFrame(emitters)
        df["Rank"] = range(1, len(df) + 1)
        df = df[["Rank", "community_name", "region", "city", "total_emissions"]]
        df.rename(columns={
            "community_name": "Community",
            "region": "Region",
            "city": "City",
            "total_emissions": "Total Emissions (kg)"
        }, inplace=True)

        st.dataframe(df, use_container_width=True)
