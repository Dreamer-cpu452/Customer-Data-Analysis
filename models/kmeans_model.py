from sklearn.cluster import KMeans


def perform_kmeans(df):

    features = df[[
        "AnnualIncome",
        "SpendingScore"
    ]]

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = model.fit_predict(features)

    return df