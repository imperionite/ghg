import os
import streamlit as st
from dotenv import load_dotenv
from utils.api import fetch_community_summary
from visuals.map import community_emission_map
from visuals.region_bar import region_emissions_bar
from visuals.community_type import community_type_bar
from visuals.submission_trend import submission_density_over_time
from visuals.sectoral_breakdown import sectoral_emissions_by_location
from visuals.sectoral_trend import sectoral_trend_over_time
from visuals.sectoral_by_type import sectoral_by_community_type
from visuals.lowest_emitters import lowest_emitters_table
from visuals.top_emitters import top_emitters_leaderboard
from utils.footer import add_footer

load_dotenv()

GHG_SCOUT_URL = os.getenv("GHG_SCOUT_URL", "http://localhost:5173")

st.set_page_config(page_title="Public Dashboard", page_icon="📊", layout="wide")
st.title("🌍 Public GHG Emissions Dashboard")
st.caption("Explore aggregated greenhouse gas emissions across Philippine regions and community types shared by users.")
# st.link_button("Go back to GHG-Scout Community Data", f"{GHG_SCOUT_URL}/community-dashboard")

st.markdown(f"""
    <style>
    .stButton > button, .custom-link-button {{
        background-color: #F0F2F6;
        color: #262730;
        padding: 0.375rem 0.75rem;
        border-radius: 0.5rem;
        border: 1px solid rgba(49, 51, 63, 0.2);
        font-weight: 500;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.2s ease;
        text-decoration: none;
        display: inline-block;
        text-align: center;
    }}
    .custom-link-button:hover {{
        background-color: rgba(49, 51, 63, 0.05);
    }}
    </style>

    <a href="{GHG_SCOUT_URL}/community-dashboard" target="_self" class="custom-link-button">
        Go back to GHG-Scout Community Data
    </a>
    """, unsafe_allow_html=True)


# Fetch data
summary_data = fetch_community_summary()

# Sidebar navigation menu
menu_options = [
    "🌍 Map of Emissions",
    "📊 Emissions by Region",
    "🏘️ Emissions by Community Type",
    "📭 Submission Trends",
    "🏭 Sectoral Breakdown by Location",
    "📉 Sectoral Trends Over Time",
    "📚 Sectoral by Community Type",
    "🥶 Lowest Emitters",
    "🔥 Top Emitters",
    "📄 Raw Data"
]

selected_menu = st.sidebar.radio("Navigate Dashboard", menu_options)

# Render content based on selection
if selected_menu == "🌍 Map of Emissions":
    st.markdown("### Map of GHG Emissions by Community")
    st.markdown(
        "This interactive map visualizes reported greenhouse gas emissions across cities in the Philippines. "
        "Bubble size and color intensity represent the magnitude of emissions, helping identify geographic hotspots and regional disparities."
    )

    community_emission_map(summary_data)

elif selected_menu == "📊 Emissions by Region":
    st.markdown("### Total Emissions by Region")
    st.markdown(
        "Bar chart showing total GHG emissions aggregated by region. "
        "Compare which regions contribute most to national emissions to guide targeted mitigation efforts."
    )
    region_emissions_bar(summary_data)

elif selected_menu == "🏘️ Emissions by Community Type":
    st.markdown("### Emissions by Community Type")
    st.markdown(
        "Compare average emissions across community types such as LGUs, schools, or barangays. "
        "Identify emission-intensive community types for focused policy interventions."
    )
    community_type_bar()

elif selected_menu == "📭 Submission Trends":
    st.markdown("### Submission Trends Over Time")
    st.markdown(
        "Track how many communities submit data over time. "
        "Reveal engagement trends with the reporting platform and assess participation levels."
    )
    submission_density_over_time()

elif selected_menu == "🏭 Sectoral Breakdown by Location":
    st.markdown("### Sectoral Emissions by Location")
    st.markdown(
        "Grouped bar chart presenting emissions broken down by sector and location. "
        "Detect dominant sectors in specific areas to support regional policy planning."
    )
    sectoral_emissions_by_location()

elif selected_menu == "📉 Sectoral Trends Over Time":
    st.markdown("### Sectoral Emission Trends Over Time")
    st.markdown(
        "Line chart tracking changes in emissions from sectors like energy, waste, and transport. "
        "Assess impact of sector-specific interventions or external events."
    )
    sectoral_trend_over_time()

elif selected_menu == "📚 Sectoral by Community Type":
    st.markdown("### Sectoral Emissions by Community Type")
    st.markdown(
        "Compare emissions by sector across community types (e.g., barangay vs. school). "
        "Gain insight into structural emission contributions by community category."
    )
    sectoral_by_community_type()

elif selected_menu == "🥶 Lowest Emitters":
    st.markdown("### Lowest Emitting Communities")
    st.markdown(
        "Table listing communities with the lowest recorded total emissions. "
        "Identify best practices or flag potential underreporting."
    )
    lowest_emitters_table()

elif selected_menu == "🔥 Top Emitters":
    st.markdown("### Top Emitting Communities")
    st.markdown(
        "Leaderboard showing highest-emitting communities based on reported data. "
        "Support prioritization of interventions or resource allocation."
    )
    top_emitters_leaderboard()

elif selected_menu == "📄 Raw Data":
    st.markdown("### Raw Data (Community Summary)")
    st.markdown(
        "Raw GHG summary data per city or region. "
        "Use to validate visuals, export, or conduct independent analysis."
    )
    st.dataframe(summary_data)

add_footer()
