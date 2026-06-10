import streamlit as st


def show_clv_insights(data):

    st.markdown("---")

    st.header("🤖 AI CLV Insights")

    high = len(
        data[
            data["Customer Lifetime Value"] == "High"
        ]
    )

    medium = len(
        data[
            data["Customer Lifetime Value"] == "Medium"
        ]
    )

    low = len(
        data[
            data["Customer Lifetime Value"] == "Low"
        ]
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🏆 High Value",
            high
        )

    with c2:
        st.metric(
            "⭐ Medium Value",
            medium
        )

    with c3:
        st.metric(
            "📉 Low Value",
            low
        )

    st.markdown("---")

    st.subheader("🎯 Business Strategy")

    st.info(
        """
        💰 Reward High Value Customers

        ⭐ Upsell Medium Value Customers

        📢 Run Campaigns for Low Value Customers
        """
    )