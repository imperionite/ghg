import folium
import json
import pandas as pd
import numpy as np
from streamlit_folium import st_folium
import streamlit as st
from branca.colormap import linear

def community_emission_map(data):
    if not data:
        st.warning("No emission data to display.")
        return

    # Load GeoJSON
    try:
        with open("data/cities.geojson", "r") as f:
            geojson_data = json.load(f)
    except Exception as e:
        st.error(f"Failed to load cities.geojson: {e}")
        return

    df_geo = pd.json_normalize(geojson_data["features"])
    df_geo["city"] = df_geo["properties.city"]

    df_data = pd.DataFrame(data)
    df = pd.merge(df_data, df_geo, on="city", how="inner")

    missing = set(df_data["city"]) - set(df["city"])
    if missing:
        st.warning(f"Missing coordinates for: {', '.join(missing)}")

    emissions_series = df["total_emissions"]
    emissions_max = emissions_series.max()
    emissions_min = emissions_series.min()

    # Define a smooth linear color scale (no legend rendered)
    colormap = linear.YlOrRd_09.scale(emissions_min, emissions_max)

    # Create map centered on the Philippines
    m = folium.Map(
        location=[12.8797, 121.7740],
        zoom_start=6.3,
        control_scale=True,
        tiles="cartodb positron"
    )

    # Add circles with color + radius scaled to emissions
    for _, row in df.iterrows():
        lon, lat = row["geometry.coordinates"]
        emissions = row["total_emissions"]

        folium.CircleMarker(
            location=[lat, lon],
            radius=min(25, max(5, emissions / (emissions_max / 10))),  # Scale 5–25px
            popup=(
                f"<b>{row['city']}</b><br>"
                f"Region: {row['region']}<br>"
                f"Emissions: {emissions:,.0f} kg<br>"
                f"Submissions: {row['count']}"
            ),
            color=colormap(emissions),
            fill=True,
            fill_color=colormap(emissions),
            fill_opacity=0.7,
            weight=1,
        ).add_to(m)

    # Final render
    st_folium(m, width=1500, height=750)
