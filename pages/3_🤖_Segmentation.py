import streamlit as st
from preprocessing.data_loader import load_data
from models.kmeans_model import perform_kmeans
from models.purchase_prediction import train_prediction_model
from visualization.cluster_graph import show_cluster
from analytics.prediction_insights import prediction_insights
from analytics.recommendation_engine import show_recommendations

st.set_page_config(
    page_title="Segmentation",
    page_icon="🤖",
    layout="wide"
)


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

st.title("🤖 AI Customer Segmentation")

st.markdown("---")

# Load dataset from Dashboard

if "file_path" in st.session_state:

    df = load_data(
        st.session_state["file_path"]
    )

    # K-Means Clustering

    df = perform_kmeans(df)

    # Purchase Prediction

    model, df = train_prediction_model(df)

    # Cluster Visualization

    show_cluster(df)

    # Prediction Results

    prediction_insights(df)

    # Recommendation Engine

    show_recommendations(df)

else:

    st.warning(
        "⚠️ Please upload a dataset from the Dashboard page."
    )