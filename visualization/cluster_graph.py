import streamlit as st
import plotly.express as px


def show_cluster(df):

    st.markdown("---")

    st.header("🤖 AI Customer Segmentation")

    fig = px.scatter(
        df,
        x="AnnualIncome",
        y="SpendingScore",
        color="Cluster",
        template="plotly_dark",
        title="K-Means Customer Clusters"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )