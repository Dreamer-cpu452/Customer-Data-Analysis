import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def train_churn_model(df):

    data = df.copy()

    if "Churn" not in data.columns:

        data["Churn"] = (
            data.select_dtypes(include=["number"])
            .sum(axis=1)
            >
            data.select_dtypes(include=["number"])
            .sum(axis=1).median()
        ).astype(int)

    encoder = LabelEncoder()

    for col in data.select_dtypes(include="object").columns:
        data[col] = encoder.fit_transform(
            data[col].astype(str)
        )

    X = data.drop("Churn", axis=1)

    y = data["Churn"]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    prediction = model.predict(X)

    data["Churn Prediction"] = prediction

    return model, data