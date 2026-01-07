import joblib
import pandas as pd

# Učitavamo istrenirani model
model = joblib.load("../models/model.pkl")

# Novi stan 
novi_stan = pd.DataFrame([{
    "kvadratura": 55,
    "lokacija": "Centar",
    "trzisni_trend": 1.10
}])

# Predikcija
cijena = model.predict(novi_stan)

print("Procjena cijene stana:", round(cijena[0], 2), "EUR")
