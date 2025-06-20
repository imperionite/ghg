import streamlit as st
from utils.footer import add_footer

# Page info
st.set_page_config(page_title="Issue", page_icon="🧩")

st.sidebar.title("Navigation")
st.sidebar.markdown("Use the menu on top to switch pages. You're on: **Issue page**")

st.title("🌿 The Issue: Greenhouse Gas (GHG) Emissions in the Philippines")

st.markdown("""
## 🌐 Introduction: What Are GHGs?

Greenhouse gases (GHGs) include carbon dioxide (CO₂), methane (CH₄), nitrous oxide (N₂O), and fluorinated gases. These gases trap heat in the atmosphere, amplifying the greenhouse effect and leading to global warming and climate change.

While GHG emissions and air pollution are related environmental issues in the Philippines, they have distinct characteristics and impacts. GHG emissions contribute to long-term, global-scale climate change, while air pollution primarily affects local and regional air quality. The mitigation strategies for these two issues may differ, with GHG emissions requiring a focus on reducing fossil fuel consumption and promoting renewable energy sources, while air pollution may require more localized solutions, such as emission control technologies and urban planning. 
""")

st.markdown("""
## 📊 Current Status in the Philippines

> In 2020, the Philippines had a GHG emission footprint of approximately **204.33 teragrams of CO₂ equivalent (Tg CO₂e)**, about **12.3% lower than in 2019** (232.99 Tg CO₂e).  
> 
> **Global Rank**: 34th in total GHG emissions  
> **Global Contribution**: ~0.5% of total global emissions  
> **Per Capita Emissions**: **1.98 metric tons**, compared to global average of **4 metric tons**  
> 
> *Source: Philippine Statistics Authority, 2024; Emission Index, 2021*
""")

st.markdown("""
## 🛠️ Causes of GHG Emissions in the Philippines

- **Urbanization and Industrialization**  
  Rapid growth in cities and industries increases energy use, transport needs, and emissions.

- **Population Growth**  
  More people = more demand on resources and infrastructure = more emissions.

- **Agricultural Practices**  
  Especially **rice farming**, releases **methane (CH₄)** and **nitrous oxide (N₂O)**.
""")

st.markdown("""
## 🚨 Effects of GHG Emissions

- **Climate Change and Natural Disasters**  
  Increased typhoons, droughts, floods causing damage to life and property

- **Environmental Degradation**  
  Sea level rise, weather pattern shifts, biodiversity loss

- **Health and Socioeconomic Impacts**  
  GHGs worsen air quality, health outcomes, and economic vulnerabilities.
""")

st.markdown("""
## 🧭 Infographic: GHG Concept Map

Below is the concept map that outlines the core themes, relationships, and impact areas of GHG emissions in the Philippines.
""")

st.image(
    "https://i.imgur.com/26s1LhY.png",  # Fixed the image link here!
    caption="Conceptual Map: GHG Emissions in the Philippines (Created by Arnel Imperial, 2025)",
    use_container_width=True
)

st.markdown("""
## 💡 Reflection & Analysis

Although the Philippines ranks 34th in total GHG emissions, it is **one of the most vulnerable** countries to climate change due to its geography and socioeconomic conditions.

> 🧠 *We must recognize that even low-emitting countries suffer greatly from the consequences of global emissions. Mitigation and adaptation strategies are urgently needed.*
""")

st.markdown("""
## 📚 References

- Emission-Index. (2021). Global greenhouse gas emissions by country. *Emission-Index*. [https://www.emission-index.com](https://www.emission-index.com)

- Jamora, J. B., Go, A. W., Gudia, S. E. L., Giduquio, M. B., Capareda, S. C., & Culaba, A. B. (2021). Evaluating the use of rice residue ash in cement-based industries in the Philippines: Greenhouse gas reduction, transportation, and cost assessment. *Cleaner Engineering and Technology, 3*, 100108. [https://doi.org/10.1016/j.jclepro.2023.136623](https://doi.org/10.1016/j.jclepro.2023.136623)

- Kawanishi, M., Kato, M., Matsuda, E., Fujikura, R., & Kawamura, A. (2021). Comparative study on institutional designs and performance of national greenhouse gas inventories: The cases of Vietnam and the Philippines. *Environmental Science & Policy, 123*, 1–11. [https://doi.org/10.1007/s10668-019-00460-y](https://doi.org/10.1007/s10668-019-00460-y)

- Lu, J. L. (2022). Correlation of climate change indicators with health and environmental data in the Philippines. *Environmental and Sustainability Indicators, 13*, 100170. [https://doi.org/10.47895/amp.v56i1.3976](https://doi.org/10.47895/amp.v56i1.3976) 

- Philippine Statistics Authority (PSA). (2024). Greenhouse gas emissions statistics in the Philippines, 2020. *Philippine Statistics Authority*. [https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB\_\_3A/0143A5EGHG1.px/?rxid=bdf9d8da-96f1-4100-ae09-18cb3eaeb313](https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__3A/0143A5EGHG1.px/?rxid=bdf9d8da-96f1-4100-ae09-18cb3eaeb313)

- Wenlong, Z., Tien, N. H., Sibghatullah, A., Asih, D., & Alam, M. S. (2021). Impact of energy efficiency, technology innovation, institutional quality, and trade openness on greenhouse gas emissions in ten Asian economies. [https://doi.org/10.1007/s11356-022-20079-3](https://doi.org/10.1007/s11356-022-20079-3)
""")

st.markdown("""---""")

add_footer()