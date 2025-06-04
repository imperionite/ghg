import streamlit as st

from utils import add_footer

# Page configuration
st.set_page_config(
    page_title="GHG Data Explorer PH",
    page_icon="🧩",
    layout="centered"
)

# Title
st.markdown("# 🌏 GHG Data Explorer PH")
st.markdown("### Your Gateway to Understanding Greenhouse Gas Emissions in the Philippines")

# Introduction
st.write("""
**Welcome to GHG Data Explorer PH**, a digital advocacy platform created to raise awareness and inspire action on climate change by focusing on **Greenhouse Gas (GHG) emissions in the Philippines**.
""")

# What We Do
st.markdown("## 🔍 What We Do")
st.markdown("""
We **inform**, **educate**, and **inspire** through:

- 📊 **Credible Data**: Access verified and localized GHG emissions data.
- 📚 **Educational Content**: Understand where emissions come from and why they matter.
- 🛠 **Interactive Tools**: Visualizations and insights to explore trends and impacts.
- 💬 **Community Voice**: Stories and solutions from Filipinos on the frontlines of climate change.
""")

# Why It Matters
st.markdown("## 🌿 Why It Matters")
st.markdown("""
The Philippines is among the most climate-vulnerable countries in the world. Understanding our GHG emissions is a **critical step** toward:

- Building climate resilience 🌧  
- Advocating for sustainable policies 📣  
- Empowering individual and collective climate action 👫🌱  
""")

# Explore the Data
st.markdown("## 📈 Explore the Data")
st.info("👉 *[Developer's Playground: Visual Experiment](https://ghgdataexplorerph.streamlit.app/Visual_Experiment)*")
st.info("👉 *[Coming Soon: Interactive Emissions Dashboard](https://ghgdataexplorerph.streamlit.app/Visual_Experiment)*")

# Learn More
st.markdown("## 🧠 Learn More")
st.success("📘 *[Featured Content (Comming Soon): What are GHGs and why should Filipinos care?](https://ghgdataexplorerph.streamlit.app/Issue)*")

# Join the Movement
st.markdown("## 🚀 Join the Movement")
st.markdown("""
Be part of a growing community committed to protecting people and the planet.

- [**Get Involved**](https://ghgdataexplorerph.streamlit.app)
- [**Subscribe for Updates**](https://ghgdataexplorerph.streamlit.app)
- [**Follow Us**](https://ghgdataexplorerph.streamlit.app)
""")

# About the Project
st.markdown("## 🧩 About the Project")
st.markdown("""
GHG Data Explorer PH was developed by [Arnel Imperial](https://github.com/imperionite) as part of the **People and Earth’s Ecosystem MO-ENV076** course from Mapua Malayan Digital College. 
            
Please check the following links to know more about the project:
- [Project Lineage](https://github.com/imperionite/ilmanala) & [Notebook Project](https://github.com/imperionite/ilmanala/blob/main/EDA_GHG.ipynb)
- [Web App](https://github.com/imperionite/ghg)

It’s more than a project—it’s a call to action.

> “Change begins with knowledge. Knowledge leads to action.”
""")

# Footer
st.markdown("---")

st.markdown("""
  ⚠️ *This digital advocacy page is a school project for educational purposes. It aims to raise awareness about greenhouse gas (GHG) emissions in the Philippines and promote collective actions for protecting Earth’s ecosystems.*

  **Some of the links here are only a placeholder**.       
""")

add_footer()