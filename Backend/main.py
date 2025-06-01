from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle
import os

app = FastAPI(title="Iris Flower Prediction API")

# Enable CORS for all origins 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Helper function to load model and scaler
def load_pickle(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "rb") as f:
        return pickle.load(f)

try:
    model = load_pickle("../ml/clf.pkl")
    scaler = load_pickle("../ml/scaler.pkl")

except Exception as e:
    raise RuntimeError(f"Error loading model or scaler: {e}")

@app.post("/predict")
def predict(data: IrisInput) -> dict:
    try:
        input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        species = ["setosa", "versicolor", "virginica"][prediction]
        return {
            "prediction": int(prediction),
            "species": species
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")
