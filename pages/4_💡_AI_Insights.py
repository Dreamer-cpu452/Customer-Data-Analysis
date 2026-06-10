import streamlit as st

from preprocessing.data_loader import load_data

from models.kmeans_model import perform_kmeans
from models.purchase_prediction import train_prediction_model

from analytics.business_insights import show_insights
from analytics.cluster_statistics import cluster_statistics
from analytics.ai_score import ai_score

# Churn Prediction
from models.churn_prediction import train_churn_model
from visualization.churn_graph import show_churn_graph
from analytics.churn_insights import show_churn_insights

# CLV Prediction
from models.clv_prediction import calculate_clv
from visualization.clv_graph import show_clv_graph
from analytics.clv_insights import show_clv_insights

# Future Purchase Prediction
from models.future_purchase import future_purchase_prediction
import importlib
import visualization.future_purchase_graph
from analytics.future_purchase_insights import future_purchase_insights

# Marketing Strategy
from analytics.marketing_strategy import marketing_strategy

from analytics.executive_dashboard import executive_dashboard

st.set_page_config(
    page_title="AI Insights",
    page_icon="💡",
    layout="wide"
)


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

st.title("💡 AI Business Insights")

st.markdown("---")


# Load dataset from Dashboard

if "file_path" in st.session_state:

    df = load_data(
        st.session_state["file_path"]
    )

    # ----------------------------
    # K-Means Clustering
    # ----------------------------

    df = perform_kmeans(df)

    # ----------------------------
    # Purchase Prediction
    # ----------------------------

    model, df = train_prediction_model(df)

    # ----------------------------
    # AI Score
    # ----------------------------

    ai_score(df)

    # ----------------------------
    # Business Insights
    # ----------------------------

    show_insights(df)

    # ----------------------------
    # Cluster Statistics
    # ----------------------------

    cluster_statistics(df)

    # ----------------------------
    # Churn Prediction
    # ----------------------------

    churn_model, churn_df = train_churn_model(df)

    show_churn_graph(
        churn_df
    )

    show_churn_insights(
        churn_df
    )

    # ----------------------------
    # Customer Lifetime Value
    # ----------------------------

    clv_df = calculate_clv(df)

    show_clv_graph(
        clv_df
    )

    show_clv_insights(
        clv_df
    )

    # ----------------------------
    # Future Purchase Prediction
    # ----------------------------

    purchase_model, purchase_df = future_purchase_prediction(df)

    importlib.reload(
    visualization.future_purchase_graph
)

    visualization.future_purchase_graph.show_future_purchase_graph(
    purchase_df
)
    future_purchase_insights(
        purchase_df
    )

    # ----------------------------
    # Marketing Strategy
    # ----------------------------

    merged_df = churn_df.copy()

    merged_df[
        "Customer Lifetime Value"
    ] = clv_df[
        "Customer Lifetime Value"
    ]

    marketing_strategy(
        merged_df
    )
    executive_dashboard(
    df,
    churn_df,
    clv_df,
    purchase_df
)

else:

    st.warning(
        "⚠️ Please upload a dataset from the Dashboard page."
    )