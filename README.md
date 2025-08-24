# 🌎🌩️ Live Earthquake Dashboard – Big Data Simulation

![Earthquake Dashboard](https://raw.githubusercontent.com/yourusername/earthquake_dashboard/main/screenshot.png)

An **interactive Streamlit dashboard** for visualizing **earthquake events worldwide** with a **Big Data flavor**.
🚀 Fully online, lightweight, and easy to deploy on **Streamlit Cloud**.

---

## **📚 Table of Contents**

* [Project Overview](#project-overview)
* [✨ Features](#-features)
* [🗄️ Dataset](#-dataset)
* [💻 Installation](#-installation)
* [🚀 Usage](#-usage)
* [🗂️ Project Structure](#-project-structure)
* [📸 Screenshots](#-screenshots)
* [🔮 Future Enhancements](#-future-enhancements)
* [⚖️ License](#-license)

---

## **🌟 Project Overview**

This project simulates **real-time earthquake streaming** using the **USGS Earthquake Dataset**.

It demonstrates:

* 💡 **Big Data preprocessing** (PySpark-style)
* 📊 **Interactive visualization** with Streamlit
* 🛠️ Multi-tabbed dashboard for **magnitude, depth, and stats**

Perfect for a **Big Data portfolio project** or **data visualization demo**.

---

## **✨ Features**

* **📊 Dashboard Tab** – Table + Map of earthquakes
* **📈 Magnitude Analysis Tab** – Histogram + Top 10 strongest earthquakes
* **🌋 Depth Analysis Tab** – Depth distribution + Average depth per place
* **🧮 Summary Stats Tab** – Descriptive statistics, total events, strongest quake
* **🎛️ Interactive Filters** – Slider to filter earthquakes by magnitude
* Fully deployable on **Streamlit Cloud** or locally

---

## **🗄️ Dataset**

* **Source:** [USGS Earthquake Feed](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv) 🌍
* **Columns used:** `time`, `latitude`, `longitude`, `depth`, `mag`, `place`
* **Size:** Lightweight (\~few MB), no need to download manually

---

## **💻 Installation**

1. Clone the repo:

```bash
git clone https://github.com/yourusername/earthquake_dashboard.git
cd earthquake_dashboard
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## **🚀 Usage**

### Local Deployment

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

### Streamlit Cloud Deployment

1. Push the repository to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Deploy your repository → `main` branch → `app.py` as the main file.
4. Get a **live public URL**.

---

## **🗂️ Project Structure**

```
earthquake_dashboard/
├── app.py             # Main Streamlit application
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
└── screenshot.png     # Optional screenshots
```

---

## **📸 Screenshots**

**Dashboard Tab**
![Dashboard](https://raw.githubusercontent.com/yourusername/earthquake_dashboard/main/screenshot.png)

**Magnitude Analysis Tab**
![Magnitude](https://raw.githubusercontent.com/yourusername/earthquake_dashboard/main/screenshot_magnitude.png)

**Depth Analysis Tab**
![Depth](https://raw.githubusercontent.com/yourusername/earthquake_dashboard/main/screenshot_depth.png)

**Summary Stats Tab**
![Summary](https://raw.githubusercontent.com/yourusername/earthquake_dashboard/main/screenshot_summary.png)

---

## **🔮 Future Enhancements**

* ⏱️ True **real-time streaming** from USGS API
* ⚡ **PySpark Structured Streaming** integration
* 📊 Live charts updating automatically
* 🌐 Filters by region, depth, and time range



Do you want me to do that next?
