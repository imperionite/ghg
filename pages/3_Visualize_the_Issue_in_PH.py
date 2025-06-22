import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from utils.footer import add_footer
from utils.ghg_sc import ghg_sc_btn

# ----------------------------
# Load and Clean Data
# ----------------------------
# 📘 Set page config
st.set_page_config(page_title="Visual Experiment", page_icon="🧩", layout="wide")

data_path = Path("phil_synthetic_ghg_emissions_2010_2050.csv")

# 📂 Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(data_path)
    return df

df = load_data()

# Drop rows with missing sector or year
df = df.dropna(subset=["Sector", "Year"])

# Melt gas columns to long format
gases = ["CO2", "CH4", "N2O", "HFCs"]
df_long = df.melt(id_vars=["Year", "Sector"], value_vars=gases,
                  var_name="Gas", value_name="Emissions")
df_long = df_long.dropna(subset=["Emissions"])

# ----------------------------
# Page Configuration
# ----------------------------
# 📊 Sidebar info
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the menu on top to switch pages. You're on: **Visual Experiment Page**")

st.title("🧩 GHG Emissions in the Philippines")
st.markdown("""
This interactive dashboard provides an exploratory analysis of **Greenhouse Gas (GHG)** emissions in the Philippines, covering the period from 2010 to 2050. 
As part of a digital advocacy project aimed at raising awareness about climate and ecosystem action, it utilizes a synthetic dataset derived from [PSA OpenSTAT](https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__3A/0143A5EGHG1.px/table/tableViewLayout1/?rxid=bdf9d8da-96f1-4100-ae09-18cb3eaeb313).

Users are encouraged to consult the [project documentation](https://github.com/imperionite/ilmanala/blob/main/SYNTHETIC_DATASET_GENERATION.md) and the [notebook project in R](https://github.com/imperionite/ilmanala/blob/main/EDA_GHG.ipynb) to understand the experimental data analysis and visualization methods employed.
""")

st.markdown("""
**Note:** This is a prototype dashboard for Milestone 1. More detailed insights and filters will be included in **Milestone 2** as we expand this platform into a full data-driven web app.
""")

ghg_sc_btn()

# ----------------------------
# Emissions Overview Table
# ----------------------------
st.subheader("📋 Emissions Summary Table by Gas (Gg CO2e)")
overview_table = df_long.groupby(["Year", "Gas"], as_index=False)["Emissions"].sum()
overview_pivot = overview_table.pivot(index="Year", columns="Gas", values="Emissions")
st.dataframe(overview_pivot.style.format("{:.2f}"), use_container_width=True)

st.info(
    "🔍 **Insight:** This table provides a year-by-year overview of total emissions by gas. "
    "It helps identify trends, such as steady increases in certain gases or years with unusual emission values. "
    "CO₂ consistently dominates, but CH₄ and N₂O also contribute significantly."
)

# --- Visualization: Gas Composition Pie by Year ---
st.markdown("### 🥧 Gas Composition by Year")
year_selected = st.selectbox("Choose a Year:", sorted(df['Year'].unique()))
year_data = df_long[df_long['Year'] == year_selected].groupby('Gas')['Emissions'].sum().reset_index()
fig6 = px.pie(year_data, values='Emissions', names='Gas', title=f"GHG Composition in {year_selected}")
st.plotly_chart(fig6, use_container_width=True)
st.info(f"Pie chart of gas shares for {year_selected}. Useful for checking changing compositions.")

# 📈 Summary stats by gas
st.subheader("📊 Summary Statistics by Gas Type")
summary_stats_gas = df_long.groupby("Gas")["Emissions"].agg(
    count="count", mean="mean", median="median", sd="std", min="min", max="max", sum="sum"
).reset_index()
st.dataframe(summary_stats_gas)

st.info("""
Each gas (CO2, CH4, N2O, HFCs) contributes differently in terms of volume and distribution.
The table above shows their average, spread, and overall share in the dataset.
""")

# ----------------------------
# Boxplot Distribution by Gas
# ----------------------------
# Transform to long format

# 📦 Boxplot by Gas
st.subheader("📦 Emissions Distribution by Gas")
fig1 = px.box(df_long, x="Gas", y="Emissions", color="Gas",
              title="GHG Emissions by Gas", range_y=[-5000, 50000])
st.plotly_chart(fig1, use_container_width=True)

st.info(
    "🔍 **Insight:** This boxplot highlights the typical emission values and variability for each greenhouse gas. "
    "CO₂ has the widest range, reflecting its dominant role across various sectors. "
    "Meanwhile, gases like HFCs show fewer but occasionally extreme values, indicating sporadic high emissions."
)


# ----------------------------
# Emissions Over Time
# ----------------------------
st.subheader("📉 GHG Emissions Trend Over Time")
fig_trend = px.line(df_long.groupby(["Year", "Gas"], as_index=False)
                    .agg({"Emissions": "sum"}),
                    x="Year", y="Emissions", color="Gas",
                    markers=True, title="Total GHG Emissions by Gas Over Time")
st.plotly_chart(fig_trend, use_container_width=True)

st.info(
    "🔍 **Insight:** Emissions of CO₂, CH₄, and N₂O show relatively steady or increasing trends over time, "
    "while HFCs remain low with minor fluctuations. This visualization helps track long-term patterns and potential progress in emission control."
)

# 📈 Emissions Trend Over Time
fig3 = px.line(df_long, x="Year", y="Emissions", color="Gas", facet_col="Gas", facet_col_wrap=2,
               title="GHG Emissions Trends Over Time (2010–2050)", height=600)
st.plotly_chart(fig3, use_container_width=True)

st.info("""
This time-series plot reveals emission patterns by gas type over the years.
Trends may indicate policy effectiveness, economic changes, or technology shifts.
""")


# ----------------------------
# Emissions by Sector and Gas (Stacked Bar)
# ----------------------------
# 📈 Summary stats by Sector and Gas
summary_stats_sector = df_long.groupby(["Sector", "Gas"])["Emissions"].agg(
    mean="mean", sum="sum", min="min", max="max"
).reset_index()

# 📊 Total Emissions by Sector and Gas
st.subheader("🏭 Total Emissions by Sector and Gas")
fig2 = px.bar(summary_stats_sector, x="sum", y="Sector", color="Gas", orientation="h",
              title="Total Emissions by Sector and Gas", height=700)
st.plotly_chart(fig2, use_container_width=True)

st.info(
    "🔍 **Insight:** This chart shows which sectors produce the most emissions and which gases dominate in each. "
    "For instance, energy-related sectors are major emitters of CO₂, while waste and agriculture contribute more to CH₄ and N₂O."
)



# ----------------------------
# Heatmap of Mean Emissions
# ----------------------------
st.subheader("🌡️ Mean Emissions Heatmap by Sector and Gas")
heatmap_data = df_long.groupby(["Sector", "Gas"], as_index=False)["Emissions"].mean()
heatmap_pivot = heatmap_data.pivot(index="Sector", columns="Gas", values="Emissions")
fig_heatmap = go.Figure(data=go.Heatmap(
    z=heatmap_pivot.values,
    x=heatmap_pivot.columns,
    y=heatmap_pivot.index,
    colorscale="YlOrRd",
    colorbar=dict(title="Mean Emissions")
))
fig_heatmap.update_layout(title="Mean Emissions Heatmap", xaxis_title="Gas", yaxis_title="Sector")
st.plotly_chart(fig_heatmap, use_container_width=True)

st.info(
    "🔍 **Insight:** The heatmap reveals emission intensity per gas and sector. "
    "Darker colors indicate sectors where average emissions are particularly high for specific gases, "
    "such as CO₂ in manufacturing or CH₄ in agriculture."
)

# ----------------------------
# Top 10 Sectors
# ----------------------------
st.subheader("🏆  Top 10 Highest Emitting Sectors (All Gases Combined)")
top_sectors = df_long.groupby("Sector", as_index=False)["Emissions"].sum()
top_sectors_sorted = top_sectors.sort_values("Emissions", ascending=False).head(10)
fig_top10 = px.bar(top_sectors_sorted, x="Emissions", y="Sector", orientation="h",
                   title="Top 10 Sectors by Total GHG Emissions", color="Emissions")
st.plotly_chart(fig_top10, use_container_width=True)


# Identify top 10 sectors by total CO2 emissions
top_sectors = (
    df.groupby("Sector")["CO2"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .index
)

# Filter the data for top sectors only
top_sectors_data = df[df["Sector"].isin(top_sectors)]

# Plot the stacked area chart
fig = px.area(
    top_sectors_data,
    x="Year",
    y="CO2",
    color="Sector",
    title="CO₂ Emissions Contribution Over Time by the Top Emitters",
    labels={"CO2": "CO₂ Emissions (Mt CO₂e)", "Year": "Year"},
)

fig.update_layout(
    legend_title_text="Sector",
    legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
    margin=dict(t=60, b=60),
    template="plotly_white"
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Insight
st.info(
    "🔍 **Insight:** This area chart reveals that sectors such as 'Energy Industries', "
    "'Manufacturing and Construction', and 'Transportation' contribute significantly "
    "to CO₂ emissions. Monitoring their future trends is crucial to any GHG mitigation strategy."
)

# --- Visualization: Yearly Sectoral Trend (Faceted by Gas) ---
st.markdown("### 📉 Emission Trends by Sector Over Time (Faceted)")
fig7 = px.line(df_long, x='Year', y='Emissions', color='Sector', facet_col='Gas', facet_col_wrap=2,
               title="Trends in Sectoral Emissions (Split by Gas)", height=800)
st.plotly_chart(fig7, use_container_width=True)
st.info("This view shows which sectors are rising or declining contributors across gases.")

# --- Visualization: Sector-Gas Summary Table ---
st.markdown("### 📑 Sector-Gas Summary Table")
summary_stats = df_long.groupby(['Sector', 'Gas'])['Emissions'].agg(['mean', 'sum', 'min', 'max']).reset_index()
st.dataframe(summary_stats.round(2), use_container_width=True)
st.info("Compare sectoral averages, totals, and extremes across gas types.")

#######
# ----------------------------
# Descriptive Insights Summary
# ----------------------------
st.subheader("🧠 Generalization and Interpretation")

with st.expander("📌 Key Findings from Statistical and Visual Analysis", expanded=True):
    st.markdown("""
### 🔍 **General Insights**

- **Mean > Median** for **CO₂** and **CH₄**, indicating **positive skewness** — a few very high values inflate the mean.
- **High standard deviation** in **CO₂** and **CH₄** suggests substantial variability across years and sectors.
- **Negative values** in some gases (e.g., **CO₂**, **CH₄**, **N₂O**) may indicate **carbon removals/sequestration** or **data artifacts**, especially in **land use** categories.

---

### 🏭 **By Sector and Gas Type**

- **Energy Industries** and **Biomass Carbon Stock Deforestation** are the **highest CO₂ contributors**.
- **Enteric Fermentation** is the **main source of CH₄ emissions**.
- **Direct N₂O Emissions from Managed Soils** dominate **N₂O emissions**, highlighting key mitigation opportunities in **agriculture**.
- **Silvopasture** under **Biomass Carbon Stock** shows **large negative CO₂ values**, likely due to **carbon sequestration**.
- **Incineration and Open Burning of Waste** and **Fugitive Emissions** display **negative or unexpected values**, suggesting the need for **data validation** or consideration of **offset mechanisms**.

---

### 📈 **Summary**

- **CO₂** is the dominant greenhouse gas by both **magnitude** and **variability**, mainly driven by **energy** and **land use** sectors.
- **CH₄** from **agriculture** and **waste** exhibits a **highly skewed distribution**, indicating hotspots.
- **N₂O** emissions stem largely from **soil** and **manure management**, requiring **agriculture-specific controls**.
- **Negative values** in emissions data could reflect **carbon sinks or accounting offsets**, meriting **further investigation**.
- **Visualization tools** help highlight **patterns, outliers, and emission drivers**, aiding **evidence-based policy design**.
""")


# ----------------------------
# Footer
# ----------------------------

st.markdown("""---""")

add_footer()
