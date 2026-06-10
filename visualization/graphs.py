import streamlit as st
import plotly.express as px


def show_graphs(df):

    st.markdown("---")
    st.header("📈 Business Analytics Dashboard")

    # ================= PIE CHARTS =================

    col1, col2 = st.columns(2)

    with col1:
        if "Gender" in df.columns:
            st.subheader("🥧 Gender Distribution")

            fig = px.pie(
                df,
                names="Gender",
                hole=0.5,
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if "Churn" in df.columns:
            st.subheader("🥧 Churn Distribution")

            fig = px.pie(
                df,
                names="Churn",
                hole=0.5,
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ================= BAR CHARTS =================

    col3, col4 = st.columns(2)

    with col3:
        if "PurchaseCount" in df.columns:
            st.subheader("📊 Purchase Count")

            fig = px.histogram(
                df,
                x="PurchaseCount",
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)

    with col4:
        if "SpendingScore" in df.columns:
            st.subheader("📊 Spending Score")

            fig = px.histogram(
                df,
                x="SpendingScore",
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ================= LINE GRAPH =================

    if "Revenue" in df.columns:

        st.subheader("📈 Revenue Trend")

        temp = df.copy()
        temp["Index"] = range(len(temp))

        fig = px.line(
            temp,
            x="Index",
            y="Revenue",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ================= SCATTER =================

    col5, col6 = st.columns(2)

    with col5:

        if "Age" in df.columns and "SpendingScore" in df.columns:

            st.subheader("🎯 Age vs Spending Score")

            fig = px.scatter(
                df,
                x="Age",
                y="SpendingScore",
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)

    with col6:

        if "AnnualIncome" in df.columns and "Revenue" in df.columns:

            st.subheader("☁️ Income vs Revenue")

            fig = px.scatter(
                df,
                x="AnnualIncome",
                y="Revenue",
                size="PurchaseCount",
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ================= BOX PLOT =================

    if "Revenue" in df.columns:

        st.subheader("📦 Revenue Box Plot")

        fig = px.box(
            df,
            y="Revenue",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ================= FUNNEL =================

    if "PurchaseCount" in df.columns:

        st.subheader("🧩 Purchase Funnel")

        funnel = (
            df["PurchaseCount"]
            .value_counts()
            .head(5)
            .reset_index()
        )

        funnel.columns = ["Stage", "Customers"]

        fig = px.funnel(
            funnel,
            x="Customers",
            y="Stage",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ================= TREEMAP =================

    if "Gender" in df.columns and "Revenue" in df.columns:

        st.subheader("🌳 Revenue Treemap")

        fig = px.treemap(
            df,
            path=["Gender"],
            values="Revenue"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ================= HEATMAP =================

    st.subheader("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(
        include=["int64", "float64"]
    )

    fig = px.imshow(
        numeric_df.corr(),
        text_auto=True,
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)
    