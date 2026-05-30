import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "churn_model.pkl"
)


def predict_customer(customer_data):

    bundle = joblib.load(
        MODEL_PATH
    )

    model = bundle["model"]
    scaler = bundle["scaler"]
    columns = bundle["columns"]

    input_df = pd.DataFrame(
        [customer_data]
    )

    input_df = pd.get_dummies(
        input_df
    )

    input_df = input_df.reindex(
        columns=columns,
        fill_value=0
    )

    input_scaled = scaler.transform(
        input_df
    )

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    prediction = (
        "Likely To Churn"
        if probability > 0.5
        else "Not Likely To Churn"
    )

    return {
        "prediction": prediction,
        "probability": round(
            probability * 100,
            2
        )
    }