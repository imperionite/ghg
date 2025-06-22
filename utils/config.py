import streamlit as st
import os

def get_backend_url():
    return st.secrets.get("BACKEND_URL") or os.getenv("BACKEND_URL") or "http://localhost:8000"

def get_ghg_sc_url():
    return st.secrets.get("GHG_SC_URL") or os.getenv("GHG_SC_URL") or "http://localhost:5173"

BACKEND_URL = get_backend_url()
GHG_SC_URL = get_ghg_sc_url()
