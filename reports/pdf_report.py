from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import streamlit as st


def generate_pdf(df):

    doc = SimpleDocTemplate(
        "Customer_Analytics_Report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Customer Analytics Report",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Rows: {df.shape[0]}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Columns: {df.shape[1]}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    with open(
        "Customer_Analytics_Report.pdf",
        "rb"
    ) as pdf:

        st.download_button(
            "📄 Download PDF Report",
            pdf,
            file_name="Customer_Analytics_Report.pdf"
        )