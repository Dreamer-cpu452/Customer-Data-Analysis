import streamlit as st
import plotly.express as px


def show_future_purchase_graph(data):

    st.markdown("---")

    st.header("📈 Future Purchase Prediction")

    fig = px.pie(
        data,
        names="Future Purchase Prediction",
        title="Future Purchase Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    count = (
        data["Future Purchase Prediction"]
        .value_counts()
        .reset_index()
    )

    count.columns = [
        "Prediction",
        "Customers"
    ]

    fig2 = px.bar(
        count,
        x="Prediction",
        y="Customers",
        color="Prediction",
        title="Future Buyers",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


if __name__ == "__main__":
    pass
