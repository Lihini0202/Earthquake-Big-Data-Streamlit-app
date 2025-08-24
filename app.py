import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="🌎 Live Earthquake Dashboard", layout="wide")
st.title("🌎 Enhanced Earthquake Dashboard")

# Load dataset
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"
df = pd.read_csv(url)
df = df[['time','latitude','longitude','depth','mag','place']]

# Sidebar filter
mag_filter = st.sidebar.slider("Minimum Magnitude", 0.0, 10.0, 4.0, 0.1)
filtered_df = df[df['mag'] >= mag_filter]

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Dashboard", "Magnitude Analysis", "Depth Analysis", "Summary Stats"])

# ---------------- Tab 1: Dashboard ----------------
with tab1:
    st.subheader("Earthquake Table & Map")
    st.dataframe(filtered_df)
    st.map(filtered_df.rename(columns={'latitude':'lat','longitude':'lon'}))

# ---------------- Tab 2: Magnitude Analysis ----------------
with tab2:
    st.subheader("Magnitude Distribution")
    st.bar_chart(np.histogram(filtered_df['mag'], bins=20, range=(0,10))[0])

    st.subheader("Top 10 Strongest Earthquakes")
    st.dataframe(filtered_df.nlargest(10,'mag')[['time','place','mag']])

# ---------------- Tab 3: Depth Analysis ----------------
with tab3:
    st.subheader("Depth Distribution")
    st.bar_chart(filtered_df['depth'])

    st.subheader("Average Depth by Place (Top 10)")
    avg_depth = filtered_df.groupby('place')['depth'].mean().nlargest(10)
    st.bar_chart(avg_depth)

# ---------------- Tab 4: Summary Stats ----------------
with tab4:
    st.subheader("Summary Statistics")
    st.write(filtered_df.describe())

    st.subheader("Total Earthquakes")
    st.metric(label="Total Events", value=len(filtered_df))

    st.subheader("Strongest Earthquake")
    strongest = filtered_df.loc[filtered_df['mag'].idxmax()]
    st.write(f"{strongest['place']} – Magnitude {strongest['mag']} on {strongest['time']}")
