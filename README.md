#Customer Churn Prediction System

#Overview
 An end-to-end Machine Learning system that predicts customer churn probability and segments customers into actionable risk buckets (Low / Medium / High).
 The project covers the full ML lifecycle from data preprocessing to deployment with an API and interactive dashboard.


#Tech Stack

-Python
-Pandas
-NumPy
-Scikit-learn
-Logistic Regression
-Random Forest
-XGBoost
-FastAPI
-Streamlit
-Joblib
-Git & GitHub


#Workflow
Data loading and preprocessing
Exploratory Data Analysis (EDA)
Feature engineering and encoding
Model training and evaluation
Feature importance analysis
Risk scoring and segmentation
Saving trained models and metadata
Deployment using FastAPI
Interactive dashboard using Streamlit


#Models Used
-Logistic Regression (baseline model for interpretability)
-Random Forest
-XGBoost
Models were evaluated using Accuracy, Precision, Recall, ROC-AUC, and Confusion Matrix.


#Risk Scoring Logic
Predicted churn probabilities are mapped into risk buckets:
-High Risk: Probability ≥ 0.60
-Medium Risk: Probability between 0.40 and 0.59
-Low Risk: Probability < 0.40
This makes predictions easy to understand for business users.


Streamlit Dashboard
        ↓
FastAPI REST API
        ↓
ML Pipeline (Preprocessing + Model)


#Output
-Churn probability score
-Risk classification (Low / Medium / High)
-Feature importance visualization
-Interactive dashboard for predictions


#Key Features
-End-to-end ML pipeline
-Handles missing customer information
-Schema-consistent inference
-Real-time predictions via API
-Business-friendly risk segmentation
-Interactive Streamlit dashboard

This project focuses on production-ready machine learning, not just model training.


Author

Adam
Machine Learning & AI Engineer / Data Scientist