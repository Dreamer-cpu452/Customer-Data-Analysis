import streamlit as st


def show_churn_insights(data):

    st.markdown("---")

    st.header("🤖 AI Churn Insights")

    total_customers = len(data)

    churn_customers = (
        data["Churn Prediction"]
        .sum()
    )

    retention_customers = (
        total_customers
        - churn_customers
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👥 Total Customers",
            total_customers
        )

    with col2:
        st.metric(
            "🚪 High Churn Risk",
            churn_customers
        )

    with col3:
        st.metric(
            "✅ Retained Customers",
            retention_customers
        )

    st.markdown("---")

    if churn_customers > total_customers * 0.5:

        st.error(
            "⚠️ High customer churn risk detected. Consider retention campaigns."
        )

    elif churn_customers > total_customers * 0.3:

        st.warning(
            "🟡 Moderate churn risk. Promotional offers are recommended."
        )

    else:

        st.success(
            "🟢 Customer retention is healthy."
        )

    st.subheader("🎯 AI Recommendation")

    st.info(
        """
        • Offer discounts to high-risk customers.

        • Send personalized marketing campaigns.

        • Reward loyal customers.

        • Improve customer engagement programs.
        """
    )
    