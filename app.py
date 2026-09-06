import streamlit as st
import google.generativeai as genai

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
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("⚖️ Pocket NLU Engine")

# Auto-fetch permanent key from secrets if available
saved_key = st.secrets.get("GEMINI_API_KEY", "")

if not saved_key:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password", help="Add to Streamlit Secrets to avoid re-entering.")
else:
    api_key = saved_key
    st.sidebar.success("🔑 API Key permanently loaded")

st.sidebar.subheader("CLAT PG Modules")
preset_topic = st.sidebar.selectbox(
    "Select or Customize Pillar:",
    [
        "Custom Topic (Enter below)",
        "Unlawful Activities (Prevention) Act: Section 43D(5) vs. Article 21 (Watali to Najeeb)",
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
    custom_topic = st.text_input(
        "Enter any statute, section, doctrine, or case law:",
        placeholder="e.g., Section 43D(5) UAPA and Watali judgment"
    )

active_topic = custom_topic if preset_topic == "Custom Topic (Enter below)" else preset_topic

st.title("📚 Pocket NLU: Master Class & Diagnostic")
if active_topic:
    st.markdown(f"**Current Subject Focus:** `{active_topic}`")

if not api_key:
    st.warning("👈 Add your API key in Streamlit App Settings > Secrets or enter it in the sidebar.")
else:
    if st.button("Generate Deep Dive & Logic Drill"):
        if not active_topic.strip():
            st.error("Please enter or select a topic first!")
        else:
            try:
                genai.configure(api_key=api_key.strip())
                model = genai.GenerativeModel("models/gemini-3.6-flash")

                prompt = f"""
                You are an elite Constitutional Law and Jurisprudence professor at NLSIU Bengaluru teaching a high-ranking CLAT PG aspirant.
                Provide an exhaustive, high-yield deconstruction of: '{active_topic}'.
                
                Strictly format into these 3 scannable sections:
                
                ### 1. High-Order Doctrinal Architecture
                - The statutory and constitutional matrix.
                - Ratio decidendi, shifting judicial standards, and core precedents.
                - Use punchy bullet points and bold keywords. No walls of text.
                
                ### 2. Sociological & Ground-Level Reality
                - Institutional mechanics, power asymmetry, executive friction, and systemic impact.
                
                ### 3. Pips-Style Logic & Elimination Drill
                - A complex, multi-layered problem matrix scenario.
                - 3 distinct deductive options (Sound Law, Flawed Premise, Subtle Procedural Error).
                - Demarcated solution with detailed rationale explaining why the distractors collapse.
                """

                def stream_response():
                    response = model.generate_content(prompt, stream=True)
                    for chunk in response:
                        if chunk.text:
                            yield chunk.text

                st.write_stream(stream_response)

            except Exception as e:
                st.error(f"Execution notice: {e}")
