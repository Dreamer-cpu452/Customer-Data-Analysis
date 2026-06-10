import streamlit as st


def ai_score(df):

    st.markdown("---")

    st.header("🏆 AI Business Score")

    score = 100

    score -= df.isnull().sum().sum()
    score -= df.duplicated().sum()

    if score < 0:
        score = 0

    st.metric(
        "Dataset Quality Score",
        f"{score}%"
    )