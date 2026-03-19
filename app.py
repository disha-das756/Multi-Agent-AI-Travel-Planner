import streamlit as st
import re
import io
from graph import app_graph

# PDF imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="IntelliTrip AI",
    
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>
.main-title {
    font-size:42px;
    font-weight:800;
    color:#1F618D;
}
.subtitle {
    font-size:18px;
    color:gray;
    margin-bottom:20px;
}
.stButton > button {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 12px;
    padding: 12px 28px;
    font-size: 16px;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# PDF GENERATION FUNCTION
# -------------------------------------------------

def generate_pdf(trip_text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    elements = []
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    # Title
    elements.append(Paragraph("<b>IntelliTrip AI - Travel Plan</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    # Split text into lines
    lines = trip_text.split("\n")

    for line in lines:
        if line.strip() == "":
            elements.append(Spacer(1, 0.2 * inch))
        else:
            elements.append(Paragraph(line, normal_style))
            elements.append(Spacer(1, 0.15 * inch))

    doc.build(elements)
    buffer.seek(0)
    return buffer


# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown('<div class="main-title"> IntelliTrip AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Multi-Agent AI Travel Planning System</div>', unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:
    st.title("About IntelliTrip AI")
    st.write("""
    Features:          
    • AI Itinerary Generation  
    • Budget Estimation  
    • Attraction Discovery  
    • Multi-Agent Workflow  
    • AI Evaluation System   
    • PDF Export  
    """)
    st.markdown("---")
    st.caption("Built with LangGraph + Streamlit")
    st.caption("© 2026 Disha Das")

# -------------------------------------------------
# USER INPUTS
# -------------------------------------------------

st.markdown("##  Plan Your Trip")

col1, col2 = st.columns(2)

with col1:
    source = st.text_input("Starting City")
    destination = st.text_input("Destination")
    days = st.slider("Trip Duration (Days)", 1, 15, 5)

with col2:
    budget = st.selectbox("Budget Level", ["Budget", "Mid-range", "Luxury"])
    travel_style = st.selectbox(
        "Travel Style",
        ["Adventure", "Family", "Relaxation", "Backpacking", "Luxury"]
    )
    interests = st.multiselect(
        "Interests",
        ["Food", "Adventure", "History", "Shopping", "Nightlife", "Nature", "Beach"]
    )

st.markdown("---")

generate = st.button(" Generate Smart Trip Plan")

st.markdown("---")

# -------------------------------------------------
# GENERATE TRIP
# -------------------------------------------------

if generate:

    if not source or not destination:
        st.warning("⚠ Please enter both Starting City and Destination.")
    else:
        # Verify API Key exists
        import os
        from dotenv import load_dotenv
        load_dotenv()
        
        if not os.getenv("GROQ_API_KEY"):
            st.error("❌ GROQ_API_KEY not found! Please add it to your environment variables or Streamlit Secrets.")
            st.stop()

        with st.spinner(" AI Agents are planning your trip..."):
            state = {
                "source": source,
                "destination": destination,
                "days": days,
                "budget": budget,
                "interests": interests,
                "travel_style": travel_style,
                "itinerary": "",
                "budget_estimate": "",
                "evaluation_report": "",
                "popular_places": ""
            }

            try:
                result = app_graph.invoke(state)
                st.success("✅ Trip Plan Generated Successfully!")
            except Exception as e:
                st.error(f"❌ An error occurred during generation: {str(e)}")
                st.info("💡 Hint: Check your internet connection or API key limits.")
                st.stop()

        # -------------------------------------------------
        # QUALITY SCORE
        # -------------------------------------------------

        if "evaluation_report" in result:
            match = re.search(r'Quality Score:\s*(\d+)/10', result["evaluation_report"])
            if match:
                score = match.group(1)
                st.metric(" AI Quality Score", f"{score}/10")

        # -------------------------------------------------
        # TABS
        # -------------------------------------------------

        tab1, tab2 = st.tabs(["🗺️ Travel Plan", "🧠 AI Evaluation"])

        with tab1:
            trip_text = result.get("itinerary", "No itinerary generated.")
            st.markdown(trip_text)

            # Generate PDF
            pdf_file = generate_pdf(trip_text)

            st.download_button(
                label="📄 Download Trip Plan as PDF",
                data=pdf_file,
                file_name="IntelliTrip_Plan.pdf",
                mime="application/pdf"
            )

        with tab2:
            st.markdown(result.get("evaluation_report", "No evaluation generated."))

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("---")
st.caption("IntelliTrip AI – Autonomous Multi-Agent Travel Planning System")