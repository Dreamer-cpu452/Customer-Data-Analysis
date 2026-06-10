import streamlit as st
import plotly.express as px


def show_churn_graph(data):

    st.markdown("---")

    st.header("🚪 Customer Churn Analysis")

    # Pie Chart

    fig1 = px.pie(
        data,
        names="Churn Prediction",
        title="Customer Churn Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # Bar Chart

    churn_count = (
        data["Churn Prediction"]
        .value_counts()
        .reset_index()
    )

    churn_count.columns = [
        "Churn Status",
        "Count"
    ]

    fig2 = px.bar(
        churn_count,
    )