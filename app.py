import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="🌎 Live Earthquake Dashboard", layout="wide")
st.title("🌎 Enhanced Live Earthquake Dashboard (Big Data Simulation)")

# -------------------------
# Load Dataset
# -------------------------
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"
df = pd.read_csv(url)
df = df[['time','latitude','longitude','depth','mag','place']]

# -------------------------
# Sidebar filters
# -------------------------
mag_filter = st.sidebar.slider("Minimum Magnitude", 0.0, 10.0, 4.0, 0.1)
batch_size = 20

# -------------------------
# Tabs / Interfaces
# -------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Dashboard","Magnitude Analysis","Depth Analysis","Summary Stats"])

# -------------------------
# Tab 1: Dashboard (Live Streaming Simulation)
# -------------------------
with tab1:
    st.subheader("Live Earthquake Stream")
    placeholder = st.empty()
    for start in range(0, len(df), batch_size):
        batch = df.iloc[start:start+batch_size]
        batch = batch[batch['mag'] >= mag_filter]

        with placeholder.container():
            st.write(f"Displaying batch {start//batch_size + 1}")
            st.dataframe(batch)

            st.subheader("Earthquake Locations")
            st.map(batch.rename(columns={'latitude':'lat','longitude':'lon'}))
        
        time.sleep(1)  # simulate real-time streaming

# -------------------------
# Tab 2: Magnitude Analysis
# -------------------------
with tab2:
    st.subheader("Magnitude Distribution")
    hist_values = np.histogram(df['mag'], bins=20, range=(0,10))[0]
    st.bar_chart(hist_values)

    st.subheader("Top 10 Strongest Earthquakes")
    top10 = df.nlargest(10,'mag')[['time','place','mag']]
    st.dataframe(top10)

# -------------------------
# Tab 3: Depth Analysis
# -------------------------
with tab3:
    st.subheader("Depth Distribution")
    st.bar_chart(df['depth'])

    st.subheader("Average Depth by Place (Top 10)")
    avg_depth = df.groupby('place')['depth'].mean().nlargest(10)
    st.bar_chart(avg_depth)

# -------------------------
# Tab 4: Summary Statistics
# -------------------------
with tab4:
    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Total Earthquakes")
    st.metric(label="Total Events", value=len(df))

    st.subheader("Strongest Earthquake")
    strongest = df.loc[df['mag'].idxmax()]
    st.write(f"{strongest['place']} – Magnitude {strongest['mag']} on {strongest['time']}")
