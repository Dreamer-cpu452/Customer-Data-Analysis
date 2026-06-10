import streamlit as st


def marketing_strategy(df):

    st.markdown("---")

    st.header("🎯 AI Marketing Strategy")

    if (
        "Customer Lifetime Value" not in df.columns
        or
        "Churn Prediction" not in df.columns
    ):

        st.warning(
            "Required AI columns not found."
        )

        return

    high_clv = len(
        df[
            df["Customer Lifetime Value"] == "High"
        ]
    )

    high_churn = (
        df["Churn Prediction"]
        .sum()
    )

    if high_clv > len(df) * 0.4:

        st.success(
            "🏆 Focus on VIP Loyalty Programs."
        )

    if high_churn > len(df) * 0.3:

        st.warning(
            "🎁 Launch Customer Retention Campaigns."
        )

    st.info(
        """
        🎯 Personalized Product Recommendations

        🎯 Email Marketing Campaigns

        🎯 Discount Coupons

        🎯 Cross Selling

        🎯 Upselling

        🎯 Customer Loyalty Rewards
        """
    )