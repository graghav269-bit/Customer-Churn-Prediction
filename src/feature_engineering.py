"""
Feature Engineering Module
"""

import pandas as pd

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)


def encode_features(df):
    """
    Encode categorical variables.
    """

    df = df.copy()

    label_columns = []

    for column in df.columns:

        if df[column].dtype == "object":

            if df[column].nunique() <= 2:
                label_columns.append(column)

    encoder = LabelEncoder()

    for column in label_columns:
        df[column] = encoder.fit_transform(df[column])

    remaining_columns = []

    for column in df.columns:

        if (
            df[column].dtype == "object"
            and column != "customerID"
        ):
            remaining_columns.append(column)

    df = pd.get_dummies(
        df,
        columns=remaining_columns,
        drop_first=True
    )

    return df


def scale_features(X):

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler