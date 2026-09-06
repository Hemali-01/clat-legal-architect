import streamlit as st

# Set page layout for mobile and desktop
st.set_page_config(
    page_title="JurisPulse | Legal Logic Lab",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom dyslexia-friendly styling and soft contrast
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        letter-spacing: 0.03em;
        line-height: 1.6;
    }
    .stApp {
        background-color: #FBFBFA;
        color: #1A1A1A;
    }
    .puzzle-box {
        background-color: #F0F4F8;
        border-left: 5px solid #2B6CB0;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("⚖️ JurisPulse: Legal Logic Lab")
st.caption("Neuro-Adaptive CLAT PG & High-Order Legal Reasoning Engine")

# Mode selector
mode = st.radio(
    "Select Operating Mode:",
    ["🧩 Case Law Logic Puzzle", "🌐 Sociological & Doctrinal Map"],
    horizontal=True,
)

st.divider()

if mode == "🧩 Case Law Logic Puzzle":
    st.subheader("Challenge 01: Constitutional Symmetry")

    st.markdown(
        """
    <div class="puzzle-box">
    <b>Fact Matrix:</b> Parliament enacts an amendment restricting certain statutory appeals. 
    The petitioner claims this violates the Basic Structure doctrine by impairing judicial review.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.write("**Deductive Goal:** Identify the missing doctrinal anchor.")

    puzzle_choice = st.radio(
        "Which landmark precedent established that judicial review under Article 32/226 forms an inviolable basic feature?",
        [
            "Minerva Mills v. Union of India",
            "L. Chandra Kumar v. Union of India",
            "A.K. Gopalan v. State of Madras",
        ],
    )

    if st.button("Submit Inference"):
        if puzzle_choice == "L. Chandra Kumar v. Union of India":
            st.success(
                "🎯 Correct Deduction! L. Chandra Kumar (1997) held that the power of judicial review vested in the High Courts and Supreme Court is an integral and essential feature of the Constitution."
            )
        else:
            st.error(
                "❌ Flawed Link. Consider the specific ruling on tribunalization and Article 226 powers."
            )

elif mode == "🌐 Sociological & Doctrinal Map":
    st.subheader("Doctrinal Ecosystem: Criminal Law & Bail Jurisprudence")
    st.info(
        "**Principle:** 'Bail is the rule, jail is the exception' (State of Rajasthan v. Balchand, 1977)."
    )

    st.markdown("### Structural Dimensions:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Statutory Anchor (BNSS / CrPC)**")
        st.write(
            "- Section 479 BNSS (Maximum period of detention for undertrials)"
        )
        st.write("- Presumption of innocence until proven guilty")
    with col2:
        st.markdown("**Sociological Reality**")
        st.write("- Overrepresentation of undertrials from marginalized groups")
        st.write(
            "- Financial barriers in executing monetary bail bonds vs. personal release"
        )
