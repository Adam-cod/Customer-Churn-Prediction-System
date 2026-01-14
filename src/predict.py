import joblib
import pandas as pd
from utils import churn_risk_bucket

model = joblib.load("models/churn_model.joblib")

df = pd.read_csv("data/processed/churn_clean.csv")
X = df.drop("Churn", axis=1)

probs = model.predict_proba(X)[:, 1]

df["Churn_Probability"] = probs
df["Risk_Bucket"] = df["Churn_Probability"].apply(churn_risk_bucket)

df.to_csv("outputs/churn_predictions.csv", index=False)

print("Predictions generated.")