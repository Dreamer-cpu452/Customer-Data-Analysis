import streamlit as st
from preprocessing.data_loader import load_data
from visualization.graphs import show_graphs

st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
    layout="wide"
)


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

st.title("📈 Business Analytics Dashboard")

st.markdown("---")

# Load dataset uploaded from Dashboard

if "file_path" in st.session_state:

    df = load_data(
        st.session_state["file_path"]
    )

    st.success(
        "✅ Dataset Loaded Successfully!"
    )

    show_graphs(df)

else:

    st.warning(
        "⚠️ Please upload a dataset from the Dashboard page."
    )