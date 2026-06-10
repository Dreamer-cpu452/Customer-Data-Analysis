import streamlit as st


def product_recommendation(product):

    recommendations = {

        "Laptop": [
            "Laptop Bag",
            "Wireless Mouse",
            "Keyboard",
            "Cooling Pad",
            "Laptop Stand",
            "USB Hub",
            "Laptop Charger"
        ],

        "Mobile": [
            "Mobile Cover",
            "Tempered Glass",
            "Earbuds",
            "Power Bank",
            "Fast Charger"
        ],

        "Camera": [
            "Tripod",
            "Memory Card",
            "Camera Bag",
            "Lens Cleaner"
        ],

        "Headphones": [
            "Headphone Case",
            "Bluetooth Adapter",
            "Audio Splitter"
        ],

        "Printer": [
            "Ink Cartridge",
            "A4 Paper",
            "USB Cable"
        ]
    }

    if product in recommendations:

        st.subheader(
            "🛒 Recommended Products"
        )

        for item in recommendations[product]:

            st.success(
                f"✅ {item}"
            )

    else:

        st.info(
            "No recommendations available."
        )