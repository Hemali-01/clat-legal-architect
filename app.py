import streamlit as st
from google import genai

st.set_page_config(
    page_title="JurisPulse | Pocket NLU",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dyslexia-friendly styling, high scannability, soft contrast
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        letter-spacing: 0.03em;
        line-height: 1.7;
    }
    .stApp {
        background-color: #FBFBFA;
        color: #1A1A1A;
    }
    .card {
        background-color: #FFFFFF;
        border-left: 6px solid #2B6CB0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("⚖️ Pocket NLU Engine")

# Secure API input in sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password", help="Get a free key from aistudio.google.com")

st.sidebar.subheader("Core CLAT PG Syllabus")
preset_topic = st.sidebar.selectbox(
    "Choose a Landmark Pillar:",
    [
        "Custom Topic (Enter below)",
        "Article 21 & The Evolution of Proportionality (Puttaswamy to modern benches)",
        "Basic Structure Doctrine & Limits of Article 368 (Kesavananda, Minerva Mills)",
        "Preventive Detention & Procedural Safeguards (Article 22 vs. National Security)",
        "BNSS Section 479 & Undertrial Rights vs. Judicial Discretion",
        "BNS Changes in Sexual Offences & Marital Immunity Jurisprudence",
        "Bharatiya Sakshya Adhiniyam: Electronic Records & Certificate Requirements",
        "Hohfeld's Analysis of Rights, Duties, Liberties, and Liabilities",
        "Hart vs. Fuller Debate on Law and Morality"
    ]
)

custom_topic = ""
if preset_topic == "Custom Topic (Enter below)":
    custom_topic = st.text_input("Enter any legal concept, case, or section to deconstruct:", "Doctrine of Severability and Eclipse")

active_topic = custom_topic if preset_topic == "Custom Topic (Enter below)" else preset_topic

st.title("📚 Pocket NLU: Master Class & Diagnostic")
st.write(f"**Current Subject Focus:** {active_topic}")

if not api_key:
    st.warning("👈 Paste your free API key into the sidebar to activate the infinite study engine.")
else:
    client = genai.Client(api_key=api_key)

    if st.button("Generate Pocket NLU Deep Dive & Logic Drill"):
        with st.spinner("Deconstructing legal doctrine and sociological context..."):
            prompt = f"""
            You are a senior Constitutional Law and Jurisprudence professor at a premier National Law School (NLU) teaching an elite aspirant for CLAT PG.
            Break down the following legal subject: '{active_topic}'.
            
            Format the response strictly into these 3 structured neurodivergent-friendly sections:
            
            ### 1. The High-Order Doctrinal Architecture
            - Break down the core ratio decidendi, statutory hooks, and the historical legal tension.
            - Keep paragraphs short, punchy, and scannable with inline bolding. Avoid dense walls of text.
            
            ### 2. The Sociological & Systemic Reality (Law in Society)
            - How does this formal legal doctrine operate on the ground?
            - Highlight systemic disparities (caste, class, gender, state power) and institutional friction.
            
            ### 3. The Pips-Style Eliminative Logic Drill
            - Present a complex fact-matrix scenario testing this doctrine.
            - Present 3 distinct choices: one legally sound deduction, one based on a common flawed premise, and one subtle procedural error.
            - Provide the answer clearly demarcated below with an explanation of why the distractors fail.
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            st.session_state["study_material"] = response.text

    if "study_material" in st.session_state:
        st.markdown(st.session_state["study_material"])
