# 🌎🌩️ Live Earthquake Dashboard – Big Data Simulation

![Earthquake Dashboard](https://github.com/Lihini0202/Earthquake-Big-Data-Streamlit-app/blob/main/Dashboard.png)

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
git clone https://github.com/Lihini0202/Earthquake-Big-Data-Streamlit-app.git
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

## **📸 Screenshots**

**Dashboard Tab**
![Dashboard](https://github.com/Lihini0202/Earthquake-Big-Data-Streamlit-app/blob/main/Dashboard.png)

**Magnitude Analysis Tab**
![Magnitude](https://github.com/Lihini0202/Earthquake-Big-Data-Streamlit-app/blob/main/magnitude.png)

**Depth Analysis Tab**
![Depth](https://github.com/Lihini0202/Earthquake-Big-Data-Streamlit-app/blob/main/depth.png)

**Summary Stats Tab**
![Summary](https://github.com/Lihini0202/Earthquake-Big-Data-Streamlit-app/blob/main/summary.png)

---

## **🔮 Future Enhancements**

* ⏱️ True **real-time streaming** from USGS API
* ⚡ **PySpark Structured Streaming** integration
* 📊 Live charts updating automatically
* 🌐 Filters by region, depth, and time range

## 🚀 MLOps & DevOps Pipeline (Docker, Terraform & Azure)

This project is not just a Streamlit script; it's a complete, end-to-end **MLOps (Machine Learning Operations)** pipeline deployed on **Microsoft Azure**.

The entire cloud infrastructure is built and managed using **Terraform (Infrastructure as Code)**, and the application is containerized with **Docker**.



### Core Technologies
* **Containerization:** **Docker** (using `Dockerfile`)
* **IaC (Infrastructure as Code):** **Terraform**
* **Cloud Provider:** **Microsoft Azure**
* **Azure Services:**
    * `azurerm_resource_group` (A dedicated project folder)
    * `azurerm_container_registry` (A private "factory" to store Docker images)
    * `azurerm_container_group` (A serverless container to run the live app)
* **CI/CD:** **GitHub Actions** (for automated testing) & a **Manual CD Pipeline** (for deployment)

### 1. The Infrastructure (Terraform)
This repository contains a dedicated `/terraform` folder. This code is a reusable, automated "blueprint" that:
1.  Creates a new Resource Group.
2.  Builds a private Azure Container Registry (ACR) to store the app's image.
3.  Deploys the app from that registry to a live, public-facing URL using Azure Container Instances (ACI).

### 2. The Application (Docker)
The `Dockerfile` in this repo packages the entire Python/Streamlit application, its dependencies (`requirements.txt`), and any models (`.pkl` file) into a lightweight, portable container.

### 3. The CI/CD Pipeline
This project uses a "hybrid" pipeline:
* **Continuous Integration (CI):** The `.github/workflows/ci-pipeline.yml` file defines a **fully automated GitHub Action**. On every push, it automatically:
    1.  Lints the code with `flake8`.
    2.  Scans for vulnerabilities with `Trivy`.
    3.  Tests that the `Dockerfile` can be built successfully.
* **Continuous Deployment (CD):** Due to student account permissions (which block automated "robot accounts"), deployment is a **professional manual process**:
    1.  `docker build ...` (Build the new image)
    2.  `docker push ...` (Push the image to our Azure Registry)
    3.  `terraform apply ...` (Tell Azure to deploy the new image)
