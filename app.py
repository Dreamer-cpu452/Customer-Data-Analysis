import streamlit as st

st.set_page_config(
    page_title="AI Customer Analytics",
    page_icon="🤖",
    layout="wide"
)


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

# ---------------- HERO ----------------

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg,#141E30,#243B55);
        padding:30px;
        border-radius:15px;
        text-align:center;
        color:white;
    ">

    <h1>🤖 AI CUSTOMER ANALYTICS PLATFORM</h1>

    <h3>
    Customer Segmentation | AI Prediction |
    Business Intelligence
    </h3>

    <p>
    Transform customer data into actionable business insights
    using Artificial Intelligence and Machine Learning.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FEATURES ----------------

st.header("🚀 Platform Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.info(
        """
        ### 📊 Dashboard

        • Upload Dataset

        • KPI Cards

        • Data Cleaning

        • Statistics
        """
    )

with c2:
    st.success(
        """
        ### 🤖 AI Modules

        • Churn Prediction

        • CLV Prediction

        • Future Purchase

        • Customer Segmentation
        """
    )

with c3:
    st.warning(
        """
        ### 📈 Business Intelligence

        • Marketing Strategy

        • Executive Dashboard

        • AI Insights

        • Automated Reports
        """
    )

st.markdown("---")

# ---------------- AI CARDS ----------------

st.header("🏆 AI Capabilities")

a, b, c, d = st.columns(4)

with a:
    st.metric(
        "🤖 AI Models",
        "5+"
    )

with b:
    st.metric(
        "📊 Visualizations",
        "10+"
    )

with c:
    st.metric(
        "📄 Reports",
        "2"
    )

with d:
    st.metric(
        "🚀 AI Features",
        "8+"
    )

st.markdown("---")

# ---------------- WORKFLOW ----------------

st.header("⚙️ System Workflow")

st.markdown(
    """
    ```text
    Upload Dataset
            ↓

    Data Cleaning
            ↓

    Customer Segmentation
            ↓

    AI Predictions
            ↓

    Business Insights
            ↓

    Executive Dashboard
            ↓

    Reports Generation
    ```
    """
)

st.markdown("---")

# ---------------- FOOTER ----------------

st.markdown(
    """
    <center>

    <h4>🤖 AI Customer Analytics Platform</h4>

    <p>
    Developed using Python | Streamlit | Machine Learning
    </p>

    <p>
    K-Means | Random Forest | Plotly | AI Analytics
    </p>

    </center>
    """,
    unsafe_allow_html=True
)