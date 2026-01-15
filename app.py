from fastapi import FastAPI
import pandas as pd
import joblib

# -----------------------------
# Load model & metadata
# -----------------------------
model = joblib.load("models/churns_model.joblib")
feature_columns = joblib.load("models/feature_columns.joblib")

# -----------------------------
# Initialize FastAPI
# -----------------------------
app = FastAPI(title="Customer Churn Prediction API")

# -----------------------------
# Helper: risk bucket logic
# -----------------------------
def churn_risk_bucket(p):
    if p >= 0.55:
        return "High"
    elif p >= 0.35:
        return "Medium"
    else:
        return "Low"

# -----------------------------
# Health check endpoint
# -----------------------------
@app.get("/")
def home():
    return {"message": "Customer Churn API is running"}

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict_churn(customer: dict):
    """
    Expects customer data as JSON
    """

    # Convert input to DataFrame
    input_df = pd.DataFrame([customer])

    # Add missing columns
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = "No"   # safe default for categorical features

    # Ensure correct column order
    input_df = input_df[feature_columns]

    # Predict probability
    churn_prob = model.predict_proba(input_df)[0, 1]

    # Assign risk bucket
    risk = churn_risk_bucket(churn_prob)

    return {
        "churn_probability": round(float(churn_prob), 4),
        "risk_bucket": risk
    }