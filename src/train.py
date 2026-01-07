import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor, StackingRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error

from preprocess import build_preprocessor

data = pd.read_csv("../data/nekretnine.csv")

X = data.drop("cijena", axis=1)
y = data["cijena"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

estimators = [
    ("ridge", Ridge()),
    ("lasso", Lasso()),
    ("gbr", GradientBoostingRegressor())
]

model = StackingRegressor(
    estimators=estimators,
    final_estimator=Ridge()
)

pipeline = Pipeline([
    ("preprocessor", build_preprocessor()),
    ("model", model)
])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print("Greška modela (MAE):", mae)

joblib.dump(pipeline, "../models/model.pkl")
print("Model sačuvan.")
