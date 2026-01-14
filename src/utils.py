def churn_risk_bucket(prob):
    if prob >= 0.55:
        return "High"
    elif prob >= 0.35:
        return "Medium"
    else:
        return "Low"