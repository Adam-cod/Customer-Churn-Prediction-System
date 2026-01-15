import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("📉 Customer Churn Prediction Dashboard")
st.write("Enter customer information below. Missing fields are allowed.")

# -----------------------------
# Input fields
# -----------------------------
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Has Partner?", ["Yes", "No"])
Dependents = st.selectbox("Has Dependents?", ["Yes", "No"])

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=500.0)

# -----------------------------
# Build payload
# -----------------------------
payload = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "PhoneService": PhoneService,
    "InternetService": InternetService,
    "Contract": Contract,
    "PaymentMethod": PaymentMethod,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

# -----------------------------
# Call FastAPI
# -----------------------------
if st.button("Predict Churn"):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            churn_prob = result["churn_probability"]
            risk = result["risk_bucket"]

            st.subheader("📊 Prediction Result")

            st.metric("Churn Probability", f"{churn_prob:.2%}")

            if risk == "High":
                st.error(f"⚠️ High Risk of Churn")
            elif risk == "Medium":
                st.warning(f"🟠 Medium Risk of Churn")
            else:
                st.success(f"🟢 Low Risk of Churn")

        else:
            st.error("API error. Please check FastAPI server.")

    except Exception as e:
        st.error(f"Connection error: {e}")

