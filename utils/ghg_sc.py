import streamlit as st

from .config import GHG_SC_URL

def ghg_sc_btn():
    st.link_button("Go to Community Data", url=f"{GHG_SC_URL}/community-dashboard")
    
