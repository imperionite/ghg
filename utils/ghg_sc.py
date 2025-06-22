import streamlit as st

from .config import GHG_SC_URL

def ghg_sc_btn():
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
            transition: background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease;
            text-decoration: none;
            display: inline-block;
            text-align: center;
            outline: none;
        }}
        .custom-link-button:hover {{
            background-color: rgba(49, 51, 63, 0.05);
            border-color: #8B0000;          
            outline: 2px solid #8B0000;     
            outline-offset: 2px;
            color: #8B0000;                 
        }}
        </style>

        <a href="{GHG_SC_URL}/community-dashboard" target="_self" class="custom-link-button">
        Go back to GHG-Scout Community Data
        </a>
    """, unsafe_allow_html=True)
