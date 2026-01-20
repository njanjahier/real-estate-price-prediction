import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# ==============================
# App initialization
# ==============================
app = FastAPI(
    title="Real Estate Price Prediction API",
    version="1.0.0",
    description="FastAPI service for predicting real estate prices"
)


# ==============================
# Load ML model (absolute path)
# ==============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "src", "models", "model.pkl")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)


# ==============================
# Input schema
# ==============================
class Apartment(BaseModel):
    kvadratura: float
    lokacija: str
    trzisni_trend: float


# ==============================
# Health check
# ==============================
@app.get("/", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "message": "Real Estate Price Prediction API is running"
    }


# ==============================
# Prediction endpoint
# ==============================
@app.post("/predict", tags=["Prediction"])
def predict_price(apartment: Apartment):
    try:
        input_df = pd.DataFrame([apartment.dict()])
        prediction = model.predict(input_df)

        return {
            "predicted_price_eur": round(float(prediction[0]), 2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
