import streamlit as st


def show_recommendations(df):

    st.markdown("---")

    st.header("🎯 Customer Recommendation Engine")

    premium = df[
        (df["Cluster"] == 2)
        &
        (df["PurchasePrediction"] == 1)
    ]

    regular = df[
        (df["Cluster"] == 1)
    ]

    budget = df[
        (df["Cluster"] == 0)
    ]

    st.success(
        f"💎 Premium Customers : {len(premium)}"
    )

    st.info(
        f"🛍️ Regular Customers : {len(regular)}"
    )

    st.warning(
        f"🏷️ Budget Customers : {len(budget)}"
    )

    st.markdown("### 📢 Marketing Suggestions")

    st.write("✅ Offer Premium Membership to Premium Customers")

    st.write("✅ Provide Discount Coupons to Regular Customers")

    st.write("✅ Launch Promotional Campaigns for Budget Customers")