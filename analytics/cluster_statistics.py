import streamlit as st


def cluster_statistics(df):

    st.markdown("---")

    st.header("📋 Cluster Statistics")

    table = df.groupby(
        "Cluster"
    ).agg(
        Customer_Count=("Cluster", "count"),
        Average_Income=("AnnualIncome", "mean"),
        Average_Spending=("SpendingScore", "mean")
    )

    st.dataframe(
        table,
        use_container_width=True
    )