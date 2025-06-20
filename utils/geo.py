import time
import json
from pathlib import Path
from geopy.geocoders import Nominatim

# --- Region and Cities Data ---
REGIONS_AND_CITIES = [
    ("National Capital Region (NCR)", ["Manila", "Quezon City", "Makati", "Pasig", "Taguig", "Caloocan"]),
    ("Cordillera Administrative Region (CAR)", ["Baguio City", "Tabuk City", "La Trinidad"]),
    ("Region I – Ilocos Region", ["Vigan City", "Laoag City", "San Fernando City"]),
    ("Region II – Cagayan Valley", ["Tuguegarao City", "Ilagan City", "Santiago City"]),
    ("Region III – Central Luzon", ["San Fernando City", "Angeles City", "Malolos City", "Olongapo City"]),
    ("Region IV-A – CALABARZON", ["Calamba City", "Batangas City", "Cavite City", "Santa Rosa City"]),
    ("Region IV-B – MIMAROPA", ["Puerto Princesa", "Calapan City", "Romblon"]),
    ("Region V – Bicol Region", ["Legazpi City", "Naga City", "Sorsogon City"]),
    ("Region VI – Western Visayas", ["Iloilo City", "Bacolod City", "Roxas City"]),
    ("Region VII – Central Visayas", ["Cebu City", "Lapu-Lapu City", "Tagbilaran City"]),
    ("Region VIII – Eastern Visayas", ["Tacloban City", "Ormoc City", "Borongan City"]),
    ("Region IX – Zamboanga Peninsula", ["Zamboanga City", "Pagadian City", "Dipolog City"]),
    ("Region X – Northern Mindanao", ["Cagayan de Oro City", "Iligan City", "Malaybalay City"]),
    ("Region XI – Davao Region", ["Davao City", "Tagum City", "Panabo City"]),
    ("Region XII – SOCCSKSARGEN", ["Koronadal City", "General Santos City", "Kidapawan City"]),
    ("Region XIII – Caraga", ["Butuan City", "Surigao City", "Bayugan City"]),
    ("Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)", ["Cotabato City", "Marawi City", "Jolo"]),
]

# --- Fallback coordinates if geocode fails ---
FALLBACK_COORDS = {
    "Jolo": {"lat": 6.0522, "lon": 121.0028},
    "Bacolod City": {"lat": 10.6769, "lon": 122.9560},
    # Add more here if needed in future
}

# --- Setup geocoder ---
geolocator = Nominatim(user_agent="ph-emissions-geocoder")
results = []

# --- Loop over each city and geocode ---
for region, cities in REGIONS_AND_CITIES:
    for city in cities:
        location = None
        for attempt in range(3):  # retry up to 3 times
            try:
                location = geolocator.geocode(f"{city}, {region}, Philippines", timeout=10)
                if location:
                    break
            except Exception:
                time.sleep(2)

        if location:
            lat, lon = location.latitude, location.longitude
        else:
            fallback = FALLBACK_COORDS.get(city)
            if fallback:
                lat, lon = fallback["lat"], fallback["lon"]
                print(f"Used fallback for: {city}")
            else:
                lat, lon = None, None
                print(f"Missing coordinates for: {city}")

        results.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat] if lat is not None and lon is not None else None
            },
            "properties": {
                "region": region,
                "city": city
            }
        })

        time.sleep(1)  # Respect Nominatim rate limit

# --- Save to GeoJSON file ---
output_path = Path("data/cities.geojson")
output_path.parent.mkdir(exist_ok=True)
with open(output_path, "w") as f:
    geojson = {
        "type": "FeatureCollection",
        "features": [r for r in results if r["geometry"]["coordinates"] is not None]
    }
    json.dump(geojson, f, indent=2)

print(f"\nSaved {len(geojson['features'])} cities to {output_path.resolve()}")
