import streamlit as st

from analytics.product_recommendation import product_recommendation

st.set_page_config(
    page_title="Product Recommendations",
    page_icon="🛒",
    layout="wide"
)

st.title(
    "🛒 Smart Product Recommendation Engine"
)

st.markdown("---")

product = st.selectbox(

    "Select Purchased Product",

    [
        "Laptop",
        "Mobile",
        "Camera",
        "Headphones",
        "Printer"
    ]
)

product_recommendation(
    product
)