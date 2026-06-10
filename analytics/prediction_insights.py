import streamlit as st


def prediction_insights(df):

    st.markdown("---")

    st.header("🤖 AI Purchase Prediction")

    high = len(
        df[df["PurchasePrediction"] == 1]
    )

    low = len(
        df[df["PurchasePrediction"] == 0]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Likely High Purchasers",
            high
        )

    with col2:
        st.metric(
            "Likely Low Purchasers",
            low
        )

    st.dataframe(
        df[
            [
                "CustomerID",
                "PurchasePrediction"
            ]
        ].head(20),
        use_container_width=True
    )