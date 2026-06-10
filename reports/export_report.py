import streamlit as st


def export_csv(df):

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.markdown("---")

    st.header("📥 Download Report")

    st.download_button(
        label="📄 Download Processed Dataset",
        data=csv,
        file_name="customer_analytics_report.csv",
        mime="text/csv"
    )