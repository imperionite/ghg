import streamlit as st

from utils import add_footer

st.set_page_config(
    page_title="GHG Data Explorer PH",
    page_icon="🧩"
)

st.title("🌏 GHG Data Explorer PH")
st.markdown("""
Welcome to **GHG Data Explorer PH**, a digital advocacy platform focused on raising awareness about **Greenhouse Gas (GHG) Emissions in the Philippines**.

This is part of a school project for the course *People and Earth’s Ecosystem*. The goal is to inform, educate, and inspire action through a combination of credible information and data insights.

👉 Explore the tabs to learn more about the issue, view a concept map, and stay tuned for the upcoming interactive **Data Explorer**.


⚠️ *This digital advocacy page is a school project for educational purposes. It aims to raise awareness about greenhouse gas (GHG) emissions in the Philippines and promote collective actions for protecting Earth’s ecosystems.*
""")

st.markdown("""---""")

add_footer()
