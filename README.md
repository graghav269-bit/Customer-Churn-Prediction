# Customer Churn Prediction Analytics System

## Overview
link https://raghav-customer-churn-ai.streamlit.app/

This project is a complete end-to-end Machine Learning and Business Analytics solution that predicts customer churn using the IBM Telco Customer Churn Dataset.

The system combines:

- Data Cleaning
- Feature Engineering
- Machine Learning
- SQL Analytics
- Interactive Dashboard
- Business Reporting

---

# Problem Statement

Customer churn is one of the biggest challenges for subscription-based businesses.

The goal is to:

- Predict whether a customer will churn
- Understand key churn drivers
- Provide actionable business insights
- Improve customer retention

---

# Dataset

IBM Telco Customer Churn Dataset

Features:

- Customer Demographics
- Services Used
- Contract Information
- Payment Information
- Billing Information

Target Variable:

- Churn (Yes / No)

---

# Project Architecture

```

Raw Dataset
│
▼

Data Cleaning
│
▼

Feature Engineering
│
▼

Model Training
│
▼

Model Evaluation
│
▼

Model Deployment
│
▼

Streamlit Dashboard

```

---

# Folder Structure

```

Customer-Churn-Prediction/

├── data/
├── notebooks/
├── src/
├── models/
├── dashboard/
├── reports/
├── screenshots/
├── sql/
├── requirements.txt
├── README.md

```

---

# Technologies Used

## Programming

- Python

## Machine Learning

- Scikit-Learn
- XGBoost

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly
- Matplotlib
- Seaborn

## Dashboard

- Streamlit

## Database

- SQL

---

# Models Used

### Logistic Regression

Advantages:

- Simple
- Fast
- Interpretable

### Random Forest

Advantages:

- High Accuracy
- Handles Non-Linearity
- Feature Importance

---

# Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

---

# Installation

Clone repository:

```bash
git clone https://github.com/yourusername/Customer-Churn-Prediction.git
```

Move to project folder:

```bash
cd Customer-Churn-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running Data Cleaning

```bash
python src/data_cleaning.py
```

---

# Training Model

```bash
python models/train_model.py
```

---

# Running Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Dashboard Features

## Home Dashboard

Displays:

- Total Customers
- Churn Rate
- Revenue
- High-Risk Customers

---

## Customer Analytics

Interactive Charts:

- Churn Distribution
- Contract Analysis
- Internet Service Analysis
- Monthly Charges Analysis
- Tenure Analysis

---

## Churn Prediction

Input customer information and instantly receive:

- Prediction
- Churn Probability
- Risk Category

---

# Business Insights

Key churn drivers:

- Month-to-Month Contracts
- High Monthly Charges
- Fiber Optic Users
- New Customers
- Electronic Check Payments

---

# Future Improvements

- XGBoost Model
- Hyperparameter Tuning
- Customer Segmentation
- Real-Time Predictions
- Cloud Deployment
- Docker Containerization
- CI/CD Pipeline

---

# Sample Results

Random Forest:

- Accuracy: ~80%+
- ROC-AUC: ~85%+

---

# Author

Data Analytics & Machine Learning Project

Built using Python, SQL, Machine Learning and Streamlit.

<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/b97fc3ba-f471-4cb9-9223-7eedc065023b" />

<img width="1920" height="1080" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/484bba4c-c53f-4887-8a9c-764527e3d0a3" />

<img width="1920" height="1080" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/a5be70a1-3acc-4065-8c20-6e62d097e61f" />

<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/3dcd5d78-ffa5-427b-9650-f5c93b913e61" />

<img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/58cd87f9-d53d-4868-8dc3-a9474991564b" />

<img width="1920" height="1080" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/5be96b7e-94ee-4287-94a7-49d43331d47f" />

<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/4f88e3d6-0440-4644-94ba-79699f475261" />







