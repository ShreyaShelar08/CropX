<div align="center">

<!-- Banner -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1b4332"/>
      <stop offset="100%" style="stop-color:#52b788"/>
    </linearGradient>
  </defs>
  <rect width="900" height="200" fill="url(#bg)" rx="12"/>
  <text x="450" y="95" font-family="Arial, sans-serif" font-size="58" font-weight="bold" fill="white" text-anchor="middle">🌾 CropX</text>
  <text x="450" y="140" font-family="Arial, sans-serif" font-size="18" fill="#d8f3dc" text-anchor="middle">AI-Powered Crop Yield Prediction &amp; Optimization Platform</text>
  <text x="450" y="170" font-family="Arial, sans-serif" font-size="13" fill="#95d5b2" text-anchor="middle">Empowering small-scale farmers</text>
</svg>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest%20|%20CNN--LSTM-52b788?style=for-the-badge&logo=scikit-learn&logoColor=white)
<br/>

> **Empowering small-scale farmers with AI-driven insights, regional language support — from soil to harvest.**

<br/>

</div>

---

## 🌿 Overview

**CropX** is a comprehensive AI-driven decision support platform built to empower small-scale farmers across India — especially in regions like Odisha, Bihar, and tribal areas — where low crop productivity, unpredictable weather, and limited access to farming expertise remain persistent challenges.

Many farmers today still depend on guesswork instead of data-backed decisions. CropX bridges that gap with machine learning, IoT integration, and a climate resilience simulator — all accessible through regional language interfaces designed for farmers with varying digital literacy.

---

## 📄 Abstract

Small-scale farmers in India face low crop productivity due to unpredictable weather, poor soil health, and inefficient resource use. Climate change compounds these problems, while limited access to correct information leaves farmers without the tools to adapt.

CropX solves this by combining:
- **ML-based yield prediction** trained on soil, weather, and historical crop data
- **Real-time recommendations** for irrigation, fertilization, and pest control
- **Regional language interfaces** (including offline USSD support)
- **Climate simulation** for proactive risk planning

Preliminary results indicate a potential **>10% yield increase** through optimized resource utilization, along with reductions in water and fertilizer costs.

---

## ✨ Features

### 🌾 AI Yield Predictor
Predicts optimal crop yields using an ensemble of ML models — Random Forest, Regression, and a CNN-LSTM hybrid — trained on soil properties, weather data, satellite imagery, and historical crop yields.

### 🌦️ Climate Simulator
A "what-if" scenario tool that lets farmers visualize the yield and price impact of different weather conditions, enabling proactive planning and risk management.

### 🛰️ Real-Time Data Integration
- **India Meteorological Department (IMD)** API for live weather feeds
- **NASA POWER** and **Sentinel-2** for satellite imagery and environmental data

### 🗣️ Regional Language Support
Chatbot and dashboard interfaces available in regional Indian languages, with key features available **offline** and critical alerts delivered via **SMS/USSD** for low-connectivity zones.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML,CSS,3D Visualization Tools |
| **Backend** | Python, Flask / FastAPI |
| **ML Models** | Random Forest, Regression, CNN-LSTM Neural Networks |
| **Data Sources** | IMD API, NASA POWER API, Sentinel-2 Satellite |
| **Database** | MongoDB / Firebase |
| **Language Support** | Regional NLP Chatbot |
---

## ⚙️ Setup

### Prerequisites

- Python 3.10+
- HTML
- MongoDB or Firebase account
- IMD / NASA POWER API keys

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/cropx.git
cd cropx
```

### 2. Backend Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

Create a `.env` file in `backend/`:

```env
IMD_API_KEY=your_imd_api_key
NASA_API_KEY=your_nasa_api_key
SENTINEL_API_KEY=your_sentinel_key
MONGO_URI=your_mongodb_uri
SECRET_KEY=your_flask_secret
```

Run the backend:

```bash
python predict.py
```

The app will be live at `http://localhost:3000`

---

## 📊 Feasibility Analysis

| Dimension | Status |
|---|---|
| ✅ Technical | Proven ML models; regional NLP; 3D visualization |
| ✅ Economic | Reduces input costs; enables market price planning |
| ✅ Operational | User-friendly forms; continuous model retraining |
| ✅ Regulatory | Ethical AI; data privacy compliance; govt. policy alignment |

---

## 🧪 Prototype

📽️ **Demo Video:** [Watch on ScreenPal](https://go.screenpal.com/watch/cTQZfbnDopo)

---

## 🌍 Impact & Vision

> *"CropX is not just a crop predictor — it's a full farm management ecosystem."*

- 🌾 **Food Security** — Increased yields for India's smallest farmers
- 💧 **Environmental Sustainability** — Optimized water and fertilizer use
- 📊 **Agricultural Policy** — Rich data generated for evidence-based governance
- 🤝 **Inclusive Growth** — Democratizing access to advanced agricultural AI

---

