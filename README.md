# 🏠 Real Estate Price Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)
![Docker](https://img.shields.io/badge/Docker-20%2F21-blue)
![Deployment](https://img.shields.io/badge/Render-deployed-brightgreen)

## 🔹 Project Description

This project is a **machine learning model for predicting real estate prices**.  
It helps **buyers, sellers, and real estate agents** to estimate the market value of properties based on features like area, number of rooms, location, floor, and year built.

The project solves a **real-world problem**: the lack of fast, reliable tools to estimate property prices, which are often subjective and require expert knowledge.

The deployed app is available here: [Render Link](https://real-estate-price-prediction-2-ar18.onrender.com/)

---

## ⚡ Features

- Predict property prices based on input features
- FastAPI REST API integration
- Can be easily integrated into web or mobile apps
- Docker support for easy deployment

---

## 🛠️ Technologies Used

- **Python 3.10**  
- **FastAPI** – API framework  
- **Joblib** – for saving/loading ML models  
- **Docker** – containerized deployment  
- **Render.com** – hosting platform  

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/njanjahier/real-estate-price-prediction.git
cd real-estate-price-prediction

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt

### 3️⃣ Run the local server
uvicorn api.main:app --reload

Server will be available at http://127.0.0.1:8000.

## 💻 API Usage

Endpoint:

POST /predict


Request Example (JSON):

{
  "area": 85,
  "rooms": 3,
  "bathrooms": 2,
  "location": "Belgrade",
  "floor": 2,
  "year_built": 2010
}


Response Example (JSON):

{
  "predicted_price": 120000
}


This returns the estimated property price based on the input features.

## 🐳 Docker Deployment

To run using Docker:

docker build -t real-estate-prediction .
docker run -p 8000:8000 real-estate-prediction


Server will be available at http://localhost:8000.

## 🌐 Live Deployment

The project is deployed and available online at:
https://real-estate-price-prediction-2-ar18.onrender.com/

## 🔍 How the project solves a real-world problem

Real estate valuation is often complex and subjective, even for professionals.
This project provides:

Buyers → a fast way to check the fair market price before making an offer

Sellers → an objective estimate to set the right listing price

Agents → a data-driven tool to provide precise advice to clients

The ML model uses historical data and property features to provide accurate, quantitative predictions.

