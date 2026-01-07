import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Kreiranje aplikacije
app = FastAPI(title="Real Estate Price Prediction API")

# Učitavanje modela
model = joblib.load("models/model.pkl")

# Struktura ulaznih podataka
class Apartment(BaseModel):
    kvadratura: float
    lokacija: str
    trzisni_trend: float

@app.get("/")
def home():
    return {"message": "API radi!"}

@app.post("/predict")
def predict_price(apartment: Apartment):
    data = pd.DataFrame([apartment.dict()])
    prediction = model.predict(data)
    return {
        "predicted_price_eur": round(prediction[0], 2)
    }
