import streamlit as st
import plotly.express as px


def show_clv_graph(data):

    st.markdown("---")

    st.header("💰 Customer Lifetime Value Analysis")

    # Pie Chart

    fig1 = px.pie(
        data,
        names="Customer Lifetime Value",
        title="CLV Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # Bar Chart

    clv_count = (
        data["Customer Lifetime Value"]
        .value_counts()
        .reset_index()
    )

    clv_count.columns = [
        "CLV",
        "Customers"
    ]

    fig2 = px.bar(
        clv_count,
        x="CLV",
        y="Customers",
        color="CLV",
        title="Customer Lifetime Value Categories",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # Top Customers

    st.subheader("🏆 Top 10 Valuable Customers")

    if "CustomerID" in data.columns:

        top_customers = (
            data.sort_values(
                by="CLV Score",
                ascending=False
            )
            [["CustomerID",
              "Revenue",
              "Customer Lifetime Value"]]
            .head(10)
        )

    else:

        top_customers = (
            data.sort_values(
                by="CLV Score",
                ascending=False
            )
            [["Revenue",
              "Customer Lifetime Value"]]
            .head(10)
        )

    st.dataframe(
        top_customers,
        use_container_width=True
    )

    # Revenue Distribution

    fig3 = px.histogram(
        data,
        x="Revenue",
        title="Revenue Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )