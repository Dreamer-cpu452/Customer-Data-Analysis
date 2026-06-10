import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def calculate_clv(df):

    data = df.copy()

    # Create Revenue column if not available

    if "Revenue" not in data.columns:

        if (
            "AnnualIncome" in data.columns
            and
            "PurchaseCount" in data.columns
        ):

            data["Revenue"] = (
                data["AnnualIncome"]
                * data["PurchaseCount"]
            )

        else:

            numeric_cols = data.select_dtypes(
                include="number"
            ).columns

            data["Revenue"] = (
                data[numeric_cols]
                .sum(axis=1)
            )

    scaler = MinMaxScaler()

    data["CLV Score"] = scaler.fit_transform(
        data[["Revenue"]]
    )

    def label(score):

        if score >= 0.7:
            return "High"

        elif score >= 0.4:
            return "Medium"

        else:
            return "Low"

    data["Customer Lifetime Value"] = (
        data["CLV Score"]
        .apply(label)
    )

    return data