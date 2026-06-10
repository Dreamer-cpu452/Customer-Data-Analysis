import streamlit as st


def show_insights(df):

    st.markdown("---")

    st.header("💡 AI Business Insights")

    cluster_count = df["Cluster"].value_counts()

    premium = cluster_count.idxmax()

    st.success(
        f"✅ Cluster {premium} has the highest number of customers."
    )

    st.info(
        "📈 High spending customers can be targeted with premium offers."
    )

    st.warning(
        "🎯 Medium spending customers are good candidates for upselling."
    )

    st.error(
        "📉 Low spending customers may require promotional campaigns."
    )