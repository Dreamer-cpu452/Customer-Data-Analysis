import streamlit as st


def future_purchase_insights(data):

    st.markdown("---")

    st.header("🤖 Future Purchase Insights")

    buyers = (
        data["Future Purchase Prediction"]
        .sum()
    )

    non_buyers = (
        len(data)
        - buyers
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🛒 Likely Buyers",
            buyers
        )

    with col2:
        st.metric(
            "🚫 Low Probability",
            non_buyers
        )

    st.info(
        """
        🎯 Offer premium products to likely buyers.

        🎯 Send discounts to low probability customers.
        """
    )