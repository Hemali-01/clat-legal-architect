import streamlit as st

st.set_page_config(
    page_title="JurisPulse | NLU Pocket Lab",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dyslexia-friendly styling, generous spacing, low glare
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
        border: 1px solid #E2E8F0;
        border-left: 6px solid #2B6CB0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 22px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .socio-card {
        background-color: #F7FAFC;
        border: 1px solid #CBD5E0;
        border-left: 6px solid #7B341E;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 22px;
    }
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85em;
        font-weight: 600;
        background-color: #EBF8FF;
        color: #2B6CB0;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.title("⚖️ JurisPulse")
st.sidebar.caption("High-Order Legal Reasoning Engine")
section = st.sidebar.radio(
    "Choose Module:",
    [
        "🧩 Constitutional Logic Lab",
        "🔍 Landmark Ratio Extractor",
        "🌐 Law & Sociological Reality",
        "🎯 CLAT PG Passage Drill"
    ]
)

st.title(section)

# -------------------------------------------------------------
# MODULE 1: CONSTITUTIONAL LOGIC LAB (Pips-Style Deduction)
# -------------------------------------------------------------
if section == "🧩 Constitutional Logic Lab":
    st.markdown("""
    <div class="card">
        <span class="badge">LOGIC GRID DRILL</span>
        <h3>The Basic Structure Deduction</h3>
        <p><b>Premise:</b> Parliament passes a Constitutional Amendment inserting a clause into Article 368 that states: <i>"No amendment made under this article shall be called into question in any court on any ground."</i></p>
        <p>You are challenging this on behalf of a civil liberties petitioner. To strike down this clause, your legal reasoning chain requires three sound anchors.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Step 1: Identify the Broken Principle")
    step1 = st.radio(
        "Which foundational doctrine is directly destroyed by removing judicial review of amendments?",
        [
            "Separation of Powers & Judicial Review (Kesavananda / Minerva Mills)",
            "Doctrine of Pith and Substance",
            "Principle of Colorable Legislation alone"
        ]
    )

    st.subheader("Step 2: Spot the False Analogy")
    step2 = st.radio(
        "Opposing counsel argues: 'Constituent power is sovereign and equivalent to original constituent assembly authority.' How do you dismantle this?",
        [
            "By conceding that Article 368 gives limitless constituent power.",
            "By distinguishing between 'original' constituent power (framing the Constitution) and 'derivative' amending power under Article 368 (limited by the Constitution itself).",
            "By relying strictly on the preamble without citing case law."
        ]
    )

    if st.button("Verify Deduction Chain"):
        if (step1 == "Separation of Powers & Judicial Review (Kesavananda / Minerva Mills)" and 
            step2 == "By distinguishing between 'original' constituent power (framing the Constitution) and 'derivative' amending power under Article 368 (limited by the Constitution itself)."):
            st.success("🎯 **Flawless Analytical Linkage!** In *Minerva Mills (1980)*, the Supreme Court struck down Clauses (4) and (5) of Article 368 precisely because a limited amending power is itself a basic feature. A creature of the Constitution cannot expand its own power to become unlimited.")
        else:
            st.error("⚠️ **Logical Contradiction Detected.** Re-evaluate the distinction between original constituent power and derivative amendment power.")

# -------------------------------------------------------------
# MODULE 2: LANDMARK RATIO EXTRACTOR
# -------------------------------------------------------------
elif section == "🔍 Landmark Ratio Extractor":
    st.markdown("""
    <div class="card">
        <span class="badge">PRECEDENT BREAKDOWN</span>
        <h3>Deconstructing: <i>K.S. Puttaswamy v. Union of India (2017)</i></h3>
        <p>9-Judge Constitutional Bench on the Fundamental Right to Privacy under Article 21.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📌 Core Ratio", "⚖️ The Proportionality Test", "⚡ Overruled Precedents"])
    
    with tab1:
        st.markdown("**What did the Court actually hold?**")
        st.write("""
        - Privacy is not an elitist construct; it is an intrinsic element of life, personal liberty, and human dignity.
        - Privacy has both negative content (freedom from state intrusion) and positive content (state duty to protect personal autonomy).
        - It is protected under Article 21 as well as across the overarching architecture of Part III.
        """)
    
    with tab2:
        st.markdown("**The 4-Prong Proportionality Test (To Justify Any State Infringement):**")
        st.write("1. **Legality:** Must have an explicit statutory law backing the action.")
        st.write("2. **Legitimate Goal:** The law must serve a legitimate state aim.")
        st.write("3. **Suitability:** The measure adopted must be rationally connected to the objective.")
        st.write("4. **Necessity (Least Restrictive Measure):** No less intrusive means could achieve the same result.")

    with tab3:
        st.markdown("**Explicitly Overruled Jurisprudence:**")
        st.warning("""
        - **M.P. Sharma (1954):** Overruled to the extent it held that privacy was not constitutionally protected.
        - **Kharak Singh (1962):** Overruled where it denied a right to privacy regarding domiciliary police visits.
        - **ADM Jabalpur (1976):** Formally buried; the Court reaffirmed that fundamental rights are not gifts of the State that vanish during emergencies.
        """)

# -------------------------------------------------------------
# MODULE 3: LAW & SOCIOLOGICAL REALITY
# -------------------------------------------------------------
elif section == "🌐 Law & Sociological Reality":
    st.markdown("""
    <div class="socio-card">
        <span class="badge">SOCIO-LEGAL JURISPRUDENCE</span>
        <h3>The Bail Disparity: Formal Equality vs. Substantive Justice</h3>
        <p>How statutory criminal procedure clashes with economic and caste realities.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Statutory & Doctrinal Architecture**")
        st.write("- **Principle:** 'Bail is the rule, jail is the exception' (*State of Rajasthan v. Balchand*).")
        st.write("- **Statutory Anchor:** Section 479 of the Bharatiya Nagarik Suraksha Sanhita (BNSS) governing detention limits for undertrial prisoners.")
        st.write("- **Presumption:** Presumption of innocence remains intact until final conviction.")
    
    with col2:
        st.markdown("**Sociological Ground Reality**")
        st.write("- **The Undertrial Trap:** Over 70% of India's prison population comprises undertrial prisoners, overwhelmingly from Dalit, Adivasi, and economically disadvantaged groups.")
        st.write("- **The Surety Barrier:** Imposing monetary surety bonds treats indigent accused persons as flight risks simply because they lack property or influential sureties.")
        st.write("- **Systemic Inaction:** Formal rights mean nothing without institutional legal aid delivery at the remand stage.")

# -------------------------------------------------------------
# MODULE 4: CLAT PG PASSAGE DRILL
# -------------------------------------------------------------
elif section == "🎯 CLAT PG Passage Drill":
    st.markdown("""
    <div class="card">
        <span class="badge">CLAT PG COMPREHENSION PASSAGE</span>
        <p style="font-size: 1.05em; line-height: 1.8;">
        <i>"The test of proportionality is not a mere formal inquiry into legislative competence; it demands that the State justify the necessity of an encroaching measure with empirical demonstration. When fundamental freedoms under Part III are curtailed, the burden rests squarely on the State to demonstrate that no alternative, less-drastic measure could achieve the proclaimed statutory objective..."</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

    ans = st.radio(
        "Based on the passage and constitutional jurisprudence, on whom does the burden of justification lie once a prima facie violation of a fundamental right is established?",
        [
            "On the Petitioner, to prove malicious state intent beyond reasonable doubt.",
            "On the State, to prove necessity and proportionality using the least restrictive measure.",
            "Equally on both parties through administrative affidavits."
        ]
    )

    if st.button("Check Answer"):
        if ans == "On the State, to prove necessity and proportionality using the least restrictive measure.":
            st.success("✅ **Correct!** In constitutional scrutiny under proportionality, once a petitioner demonstrates that a fundamental right is curtailed, the evidentiary burden shifts to the State to satisfy the necessity and proportionality test.")
        else:
            st.error("❌ Review the burden-shifting mechanics under modern Article 21 and Article 14 review.")
