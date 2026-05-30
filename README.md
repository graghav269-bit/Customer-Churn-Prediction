# Customer Churn Prediction Analytics System

## Overview

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
