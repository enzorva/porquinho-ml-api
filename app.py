from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("category_model.pkl")

class Transactions(BaseModel):
    description: str

@app.post("/predict")
def predict(transactions: Transactions):
    category = model.predict([transactions.description])[0]

    return {
        "category": category
    }