import os
import requests
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def fetch_community_summary():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/community-summary")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch community summary: {e}")
        return []

def fetch_aggregated_by_type():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/aggregated-by-type")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch aggregated community type data: {e}")
        return []

def fetch_sectoral_by_region():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/sectoral-by-region")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch sectoral data by region: {e}")
        return {}

def fetch_sectoral_by_community_type():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/sectoral-by-community-type")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch sectoral data by community type: {e}")
        return {}

def fetch_timeseries():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/timeseries")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch timeseries: {e}")
        return {}

def fetch_sectoral_by_region():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/sectoral-by-region")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch sectoral by region: {e}")
        return {}

def fetch_sectoral_trend():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/sectoral-trend")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch sectoral trend: {e}")
        return {}
    
def fetch_sectoral_by_type():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/sectoral-by-community-type")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch sectoral by community type: {e}")
        return {}

def fetch_top_emitters_by_sector():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/top-by-sector?limit=5")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch top emitters: {e}")
        return {}
    
def fetch_lowest_emitters():
    try:
        response = requests.get(f"{BACKEND_URL}/api/ghg/lowest-emitters?limit=5")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch lowest emitters: {e}")
        return []
