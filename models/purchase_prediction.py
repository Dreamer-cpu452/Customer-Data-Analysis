from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def train_prediction_model(df):

    if "PurchaseCount" not in df.columns:
        return None, None

    df["Target"] = (
        df["PurchaseCount"]
        > df["PurchaseCount"].median()
    ).astype(int)

    features = [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "Revenue"
    ]

    X = df[features]
    y = df["Target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X)

    df["PurchasePrediction"] = predictions

    return model, df