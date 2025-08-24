import streamlit as st
import pandas as pd
import time
import numpy as np

st.title("🌎 Live Earthquake Dashboard (Big Data Simulation)")

# Load dataset from online URL
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"
df = pd.read_csv(url)
df = df[['time','latitude','longitude','depth','mag','place']]

# Sidebar filters
mag_filter = st.sidebar.slider("Minimum Magnitude", 0.0, 10.0, 4.0, 0.1)

# Placeholder for live simulation
placeholder = st.empty()

# Simulate streaming in batches
batch_size = 20
for start in range(0, len(df), batch_size):
    batch = df.iloc[start:start+batch_size]
    batch = batch[batch['mag'] >= mag_filter]

    with placeholder.container():
        st.subheader(f"Earthquakes with Magnitude ≥ {mag_filter}")
        st.dataframe(batch)

        st.subheader("Earthquake Locations")
        st.map(batch.rename(columns={'latitude':'lat','longitude':'lon'}))
    
    time.sleep(1)  # simulate real-time streaming
