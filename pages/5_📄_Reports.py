import streamlit as st

from preprocessing.data_loader import load_data
from models.kmeans_model import perform_kmeans
from models.purchase_prediction import train_prediction_model

from reports.export_report import export_csv
from reports.pdf_report import generate_pdf

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

st.title("📄 Reports")

st.markdown("---")

# Load dataset from Dashboard

if "file_path" in st.session_state:

    df = load_data(
        st.session_state["file_path"]
    )

    # K-Means

    df = perform_kmeans(df)

    # Purchase Prediction

    model, df = train_prediction_model(df)

    st.success(
        "✅ Report Generated Successfully!"
    )

    st.markdown("## 📥 Download Reports")

    # CSV Download

    export_csv(df)

    # PDF Download

    generate_pdf(df)

else:

    st.warning(
        "⚠️ Please upload a dataset from the Dashboard page."
    )