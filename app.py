import streamlit as st
import tempfile
import base64
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pipeline import run_full_pipeline

# Helper to load image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# Helper to generate PDF
def generate_insights_pdf(insights):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "AI-Generated Medical Insights")
    y -= 30

    pdf.setFont("Helvetica", 10)

    for item in insights:
        if y < 80:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = height - 50

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, f"{item['test']}")
        y -= 15

        pdf.setFont("Helvetica", 10)
        text = pdf.beginText(50, y)
        for line in item["insight"].split("\n"):
            text.textLine(line)
            y -= 12
        pdf.drawText(text)
        y -= 15

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer

# Load logo
logo_base64 = get_base64_image("app_logo.jpeg")

# Custom CSS
st.markdown(
    """
    <style>
        .header-container {
            text-align: center;
            margin-bottom: 2rem;
        }
        .logo {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            margin-bottom: 12px;
        }
        .app-title {
            color: #1f4fd8;
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        .app-quote {
            color: #1f4fd8;
            font-size: 1.05rem;
            font-style: italic;
        }
        .medical-note {
            color: #c62828;
            font-size: 0.9rem;
            margin-top: 1.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown(
    f"""
    <div class="header-container">
        <img class="logo" src="data:image/png;base64,{logo_base64}">
        <div class="app-title">MedAssist Insight</div>
        <div class="app-quote">AI-powered lab report analysis for faster, safer patient care.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# App Logic
pdf_type = st.radio(
    "Select PDF type",
    [
        "Text-based PDF (Recommended)",
        "Tabular PDF",
        "Image-based PDF (Scanned)"
    ]
)

uploaded_file = st.file_uploader("Upload lab report (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    type_map = {
        "Text-based PDF (Recommended)": "text",
        "Tabular PDF": "table",
        "Image-based PDF (Scanned)": "image"
    }

    with st.spinner("Analyzing report..."):
        results = run_full_pipeline(pdf_path, type_map[pdf_type])

    st.subheader("Abnormal Results found in your report:")
    st.json(results["abnormal_tests"])

    st.subheader("MedAssist's AI-Powered Insights:")
    for item in results["insights"]:
        st.markdown(f"### {item['test']}")
        st.write(item["insight"])

    # Medical Disclaimer
    st.markdown(
        """
        <div class="medical-note">
        <strong>Disclaimer:</strong> These insights are AI-generated for informational and educational purposes only. 
        They are not a substitute for professional medical advice. Please consult a qualified healthcare professional 
        or physician for diagnosis and treatment decisions.
        </div>
        """,
        unsafe_allow_html=True
    )

    # PDF Download
    pdf_file = generate_insights_pdf(results["insights"])

    st.download_button(
        label="Download MedAssist's Insights as PDF",
        data=pdf_file,
        file_name="MedAssist_Insights.pdf",
        mime="application/pdf"
    )
