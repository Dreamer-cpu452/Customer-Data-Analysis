import streamlit as st


def executive_dashboard(
    df,
    churn_df,
    clv_df,
    purchase_df
):

    st.markdown("---")

    st.header("🏆 Executive AI Dashboard")

    total_customers = len(df)

    churn_risk = (
        churn_df["Churn Prediction"]
        .sum()
    )

    future_buyers = (
        purchase_df[
            "Future Purchase Prediction"
        ]
        .sum()
    )

    high_value = len(
        clv_df[
            clv_df[
                "Customer Lifetime Value"
            ] == "High"
        ]
    )

    ai_score = round(
        (
            (
                future_buyers
                +
                high_value
            )
            /
            (
                total_customers * 2
            )
        )
        * 100,
        2
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "👥 Customers",
            total_customers
        )

    with c2:
        st.metric(
            "🚪 Churn Risk",
            churn_risk
        )

    with c3:
        st.metric(
            "💰 High CLV",
            high_value
        )

    with c4:
        st.metric(
            "📈 Future Buyers",
            future_buyers
        )

    st.markdown("---")

    st.metric(
        "🏆 Overall AI Business Score",
        f"{ai_score}%"
    )

    if ai_score >= 80:

        st.success(
            "🟢 Excellent Business Performance"
        )

    elif ai_score >= 60:

        st.warning(
            "🟡 Moderate Business Performance"
        )

    else:

        st.error(
            "🔴 Business Needs Attention"
        )

    st.markdown("---")

    st.subheader(
        "🤖 CEO Recommendations"
    )

    st.info(
        """
        ✅ Retain High Value Customers

        ✅ Target Future Buyers

        ✅ Reduce Customer Churn

        ✅ Launch Personalized Campaigns

        ✅ Increase Customer Engagement
        """
    )