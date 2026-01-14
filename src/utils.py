def churn_risk_bucket(prob):
    if prob >= 0.6:
        return "High"
    elif prob >= 0.4:
        return "Medium"
    else:
        return "Low"