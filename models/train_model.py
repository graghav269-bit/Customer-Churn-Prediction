"""
Model Training Module
"""
import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from src.feature_engineering import (
    encode_features,
    scale_features
)

import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from src.feature_engineering import (
    encode_features,
    scale_features
)


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "customer_churn_cleaned.csv"
)
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "churn_model.pkl"
)

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    print("\nModel Metrics")
    print("-" * 40)

    print(
        "Accuracy:",
        accuracy_score(y_test, predictions)
    )

    print(
        "Precision:",
        precision_score(y_test, predictions)
    )

    print(
        "Recall:",
        recall_score(y_test, predictions)
    )

    print(
        "F1:",
        f1_score(y_test, predictions)
    )

    print(
        "ROC AUC:",
        roc_auc_score(y_test, probabilities)
    )

    print(
        "\nConfusion Matrix:\n",
        confusion_matrix(y_test, predictions)
    )


def train():
    
    print("Loading data from:")
    print(DATA_PATH)

    print("Saving model to:")
    print(MODEL_PATH)

    df = pd.read_csv(DATA_PATH)

    df = encode_features(df)

    y = df["Churn"]

    X = df.drop(
        columns=[
            "Churn",
            "customerID"
        ],
        errors="ignore"
    )

    X_scaled, scaler = scale_features(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    logistic = LogisticRegression(
        max_iter=1000
    )

    random_forest = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )

    logistic.fit(X_train, y_train)
    random_forest.fit(X_train, y_train)

    print("\nLOGISTIC REGRESSION")
    evaluate_model(
        logistic,
        X_test,
        y_test
    )

    print("\nRANDOM FOREST")
    evaluate_model(
        random_forest,
        X_test,
        y_test
    )

    best_model = random_forest

    joblib.dump(
        {
            "model": best_model,
            "scaler": scaler,
            "columns": X.columns.tolist()
        },
        MODEL_PATH
    )

    print(
        f"\nModel saved at {MODEL_PATH}"
    )


if __name__ == "__main__":
    train()