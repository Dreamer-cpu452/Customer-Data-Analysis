import streamlit as st
import os
from preprocessing.data_loader import load_data

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

st.title("📊 Customer Dashboard")

st.markdown("---")

# Upload Dataset

uploaded_file = st.file_uploader(
    "📂 Upload Customer Dataset",
    type=["csv"]
)

# Save uploaded file

if uploaded_file is not None:

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    file_path = os.path.join(
        "data",
        "raw",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(
            uploaded_file.getbuffer()
        )

    st.session_state["file_path"] = file_path


# Load Dataset

if "file_path" in st.session_state:

    df = load_data(
        st.session_state["file_path"]
    )

    st.success(
        "✅ Dataset Uploaded Successfully!"
    )

    st.markdown("---")

    # Dashboard Overview

    st.subheader("📊 Dashboard Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📄 Total Rows",
            df.shape[0]
        )

    with c2:
        st.metric(
            "📑 Total Columns",
            df.shape[1]
        )

    with c3:
        st.metric(
            "❌ Missing Values",
            df.isnull().sum().sum()
        )

    with c4:
        st.metric(
            "💾 Dataset Size (KB)",
            round(
                df.memory_usage(
                    deep=True
                ).sum() / 1024,
                2
            )
        )

    st.markdown("---")

    # Dataset Preview

    st.subheader(
        "📋 Dataset Preview"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    # Data Types and Missing Values

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "🔍 Data Types"
        )

        dtype_df = (
            df.dtypes
            .astype(str)
            .reset_index()
        )

        dtype_df.columns = [
            "Column",
            "Type"
        ]

        st.table(
            dtype_df
        )

    with col2:

        st.subheader(
            "❌ Missing Values"
        )

        missing_df = (
            df.isnull()
            .sum()
            .reset_index()
        )

        missing_df.columns = [
            "Column",
            "Missing"
        ]

        st.table(
            missing_df
        )

    st.markdown("---")

    # Statistical Summary

    st.subheader(
        "📊 Statistical Summary"
    )

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

    st.markdown("---")

    # Data Cleaning Report

    st.subheader(
        "🧹 Data Cleaning Report"
    )

    a, b, c = st.columns(3)

    with a:
        st.metric(
            "Duplicate Rows",
            df.duplicated().sum()
        )

    with b:
        st.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )

    with c:

        if "CustomerID" in df.columns:

            st.metric(
                "Unique Customers",
                df["CustomerID"].nunique()
            )

        else:

            st.metric(
                "Unique Records",
                len(df)
            )

else:

    st.info(
        "👆 Please upload a CSV file to continue."
    )