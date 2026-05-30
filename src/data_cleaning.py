"""
Data Cleaning Module
"""

import pandas as pd


def load_data(file_path):
    """
    Load dataset from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully: {df.shape}")
        return df
    except Exception as error:
        print(f"Error loading data: {error}")
        raise


def clean_data(df):
    """
    Clean dataset.
    """

    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Fill missing values
    df["TotalCharges"].fillna(
        df["TotalCharges"].median(),
        inplace=True
    )

    return df


def save_clean_data(df, output_path):
    """
    Save cleaned data.
    """
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved at {output_path}")


import os

if __name__ == "__main__":

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    DATA_PATH = os.path.join(
        BASE_DIR,
        "data",
        "customer_churn.csv"
    )

    OUTPUT_PATH = os.path.join(
        BASE_DIR,
        "data",
        "customer_churn_cleaned.csv"
    )

    dataset = load_data(DATA_PATH)
    dataset = clean_data(dataset)
    save_clean_data(dataset, OUTPUT_PATH)