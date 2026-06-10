from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def future_purchase_prediction(df):

    data = df.copy()

    if "PurchaseCount" in data.columns:

        data["Future Purchase"] = (
            data["PurchaseCount"]
            >
            data["PurchaseCount"].median()
        ).astype(int)

    else:

        numeric = data.select_dtypes(
            include="number"
        )

        data["Future Purchase"] = (
            numeric.sum(axis=1)
            >
            numeric.sum(axis=1).median()
        ).astype(int)

    encoder = LabelEncoder()

    for col in data.select_dtypes(
        include="object"
    ).columns:

        data[col] = encoder.fit_transform(
            data[col].astype(str)
        )

    X = data.drop(
        "Future Purchase",
        axis=1
    )

    y = data["Future Purchase"]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    prediction = model.predict(X)

    data["Future Purchase Prediction"] = prediction

    return model, data