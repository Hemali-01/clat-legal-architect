import streamlit as st

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
    .anchor-box {
        background-color: #FFFFFF;
        border-left: 6px solid #2B6CB0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .diagnostic-sound {
        background-color: #F0FFF4;
        border-left: 6px solid #38A169;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 14px;
    }
    .diagnostic-flaw {
        background-color: #FFF5F5;
        border-left: 6px solid #E53E3E;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 14px;
    }
    .diagnostic-socio {
        background-color: #FFFAF0;
        border-left: 6px solid #DD6B20;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 14px;
    }
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85em;
        font-weight: 600;
        background-color: #EBF8FF;
        color: #2B6CB0;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.title("⚖️ JurisPulse Lab")
st.sidebar.caption("Socratic Neuro-Adaptive Legal Engine")

topic = st.sidebar.selectbox(
    "Select Master Subject:",
    [
        "Constitutional Law: Article 21 & Proportionality",
        "Criminal Law: Section 479 BNSS & Undertrial Detention",
        "Statutory Interpretation: Strict vs. Purposive Construction"
    ]
)

# -------------------------------------------------------------
# TOPIC 1: ARTICLE 21 & PROPORTIONALITY
# -------------------------------------------------------------
if topic == "Constitutional Law: Article 21 & Proportionality":
    st.title("🎯 Module: Article 21 & The Proportionality Standard")
    
    # 1. THE ANCHOR (Teaching with High Context)
    st.markdown("""
    <div class="anchor-box">
        <span class="badge">DECONSTRUCTED CONCEPT</span>
        <h3>The Shift from 'Procedure Established by Law' to 'Proportionality'</h3>
        <p><b>The Evolution:</b></p>
        <ul>
            <li><b>A.K. Gopalan (1950):</b> Formalistic, compartmentalized reading. Law just needed legislative competence.</li>
            <li><b>Maneka Gandhi (1978):</b> The Golden Triangle (Arts 14, 19, 21). The procedure must be <i>just, fair, and reasonable</i>.</li>
            <li><b>Puttaswamy (2017):</b> The 4-prong Proportionality Test replaces judicial intuition with strict empirical scrutiny.</li>
        </ul>
        <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 15px 0;">
        <p><b>The 4 Non-Negotiable Prongs:</b></p>
        <ol>
            <li><b>Legality:</b> State action must be backed by an enacted statutory law (not mere executive fiat).</li>
            <li><b>Legitimate State Goal:</b> The aim must fall within permissible constitutional limits.</li>
            <li><b>Suitability (Rational Nexus):</b> The measure must realistically further the stated goal.</li>
            <li><b>Necessity (Least Restrictive Measure):</b> The state must prove <i>no less intrusive alternative</i> was available.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧪 Deductive Reasoning Test")
    st.write("**Scenario:** The State implements biometric face-recognition surveillance across public transport hubs by an internal Police Department Circular to prevent petty theft. A citizen challenges this under Article 21.")

    # Deductive choice
    selected_flaw = st.radio(
        "Which prong of the Proportionality Standard collapses first and fatal to the State's defence?",
        [
            "Legality: An executive circular is not an enacted statutory law passed by the legislature.",
            "Suitability: Preventing theft has no rational connection to identifying people.",
            "Legitimate Goal: Preventing crime is not a valid state objective."
        ]
    )

    # Explanation input for deep active recall
    user_justification = st.text_area(
        "In your own words: Why can't the State rely on public interest or security to bypass formal statutory enactment?",
        placeholder="Type your reasoning here (1-2 sentences)..."
    )

    if st.button("Audit My Legal Reasoning"):
        st.divider()
        st.subheader("📊 Diagnostic Breakdown & Blind-Spot Audit")

        if selected_flaw.startswith("Legality"):
            st.markdown("""
            <div class="diagnostic-sound">
                <b>🎯 Sound Doctrinal Link:</b> Correct! Under <i>Puttaswamy</i> and <i>Anuradha Bhasin</i>, the threshold barrier is <b>Legality</b>. A fundamental right cannot be restricted by an executive notification, circular, or departmental guideline. Without an enacted statute, the inquiry ends immediately—the court doesn't even need to examine the other 3 prongs.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="diagnostic-flaw">
                <b>⚠️ Flawed Legal Deduction:</b> You jumped ahead to balancing tests while skipping the threshold requirement! Even if preventing crime is a legitimate goal, the State instantly loses at Prong 1 (Legality) if there is no legislative statute authorizing the intrusion.
            </div>
            """, unsafe_allow_html=True)

        if user_justification:
            st.markdown(f"""
            <div class="diagnostic-socio">
                <b>🌐 Sociological Reality Anchor:</b> Your response: <i>"{user_justification}"</i>.<br><br>
                <b>Systemic Reality Check:</b> In practice, executive bodies routinely use internal SOPs and informal circulars to enforce surveillance before laws are enacted. In CLAT PG questions, the examiners specifically test whether you can separate <i>executive convenience</i> from <i>constitutional legality</i>.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("💡 Pro-tip: Next time, write your brief rationale above so the engine can test your articulation.")

# -------------------------------------------------------------
# TOPIC 2: SECTION 479 BNSS & UNDERTRIAL DETENTION
# -------------------------------------------------------------
elif topic == "Criminal Law: Section 479 BNSS & Undertrial Detention":
    st.title("🎯 Module: Section 479 BNSS & The Undertrial Crisis")

    st.markdown("""
    <div class="anchor-box">
        <span class="badge">STATUTORY ARCHITECTURE</span>
        <h3>Section 479 of the Bharatiya Nagarik Suraksha Sanhita (BNSS)</h3>
        <p>Replaces and amends former Section 436A CrPC regarding maximum detention periods for undertrials.</p>
        <p><b>Key Rules:</b></p>
        <ul>
            <li><b>General Rule:</b> Release on bail if an undertrial has undergone detention extending up to <b>one-half</b> of the maximum imprisonment specified for that offense.</li>
            <li><b>First-Time Offender Proviso:</b> Release if the person has undergone <b>one-third</b> of the maximum imprisonment (if never previously convicted of any offense).</li>
            <li><b>Carve-Outs / Exceptions:</b> Does not apply to offenses punishable with death or life imprisonment.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧪 Deductive Reasoning Test")
    st.write("**Scenario:** 'A', a first-time offender with no prior criminal record, is charged under a section where the maximum prescribed punishment is 6 years. 'A' has spent 2 years and 1 month in jail awaiting trial because he cannot furnish financial sureties. The Magistrate refuses bail, stating trial will commence soon.")

    ans_bnss = st.radio(
        "What is the statutory imperative under Section 479 BNSS?",
        [
            "The Magistrate has complete discretion to withhold bail until trial concludes.",
            "Release is mandatory because 'A' has served more than one-third (2 years) as a first-time offender, on personal bond without sureties if indigent.",
            "Release is only permissible after completing one-half (3 years), irrespective of prior record."
        ]
    )

    if st.button("Audit My Legal Reasoning"):
        st.divider()
        st.subheader("📊 Diagnostic Breakdown & Blind-Spot Audit")
        
        if ans_bnss.startswith("Release is mandatory"):
            st.markdown("""
            <div class="diagnostic-sound">
                <b>🎯 Sound Statutory Extraction:</b> Exactly right. Section 479(1) Proviso 1 mandates release after one-third detention for first-time offenders. Furthermore, indigent persons unable to provide sureties must be released on a personal recognizance bond.
            </div>
            <div class="diagnostic-socio">
                <b>🌐 Sociological Context:</b> Over 70% of India's prison population are undertrials. The Supreme Court in <i>Re Inhuman Conditions in 1382 Prisons</i> noted that monetary sureties act as an economic barrier to liberty, disproportionately incarcerating impoverished citizens.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="diagnostic-flaw">
                <b>⚠️ Statutory Blind Spot:</b> You missed the critical amendment in BNSS! The new code specifically lowered the threshold from one-half to <b>one-third</b> for first-time offenders. Remember this distinction for both procedural practice and CLAT PG MCQs.
            </div>
            """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TOPIC 3: STATUTORY INTERPRETATION
# -------------------------------------------------------------
elif topic == "Statutory Interpretation: Strict vs. Purposive Construction":
    st.title("🎯 Module: Strict Construction vs. Purposive Rule")

    st.markdown("""
    <div class="anchor-box">
        <span class="badge">JURISPRUDENTIAL ANCHOR</span>
        <h3>Balancing Textualism and Social Purpose</h3>
        <ul>
            <li><b>Strict Construction (Penal & Taxing Statutes):</b> If two reasonable interpretations exist, the ambiguity must be resolved in favor of the subject/accused, protecting personal liberty and property.</li>
            <li><b>Purposive Construction (Beneficial & Remedial Statutes):</b> Focuses on the "mischief" the legislature intended to cure (Heydon's Rule), suppressing subtle inventions for continuance of the mischief.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    ans_stat = st.radio(
        "In socio-welfare legislation (e.g., maternity benefit, employee compensation, domestic violence protection), which interpretive canon takes precedence?",
        [
            "Strict literal construction to prevent judicial overreach.",
            "Purposive construction to give effect to the remedial objective of the Parliament.",
            "Golden rule strictly limited to grammatical corrections."
        ]
    )

    if st.button("Audit My Legal Reasoning"):
        st.divider()
        if ans_stat.startswith("Purposive construction"):
            st.markdown("""
            <div class="diagnostic-sound">
                <b>🎯 Sound Jurisprudential Grasp:</b> Correct. Beneficial legislation demands a liberal, purposive interpretation to fulfill the constitutional directive principles (Part IV) that animated its drafting.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="diagnostic-flaw">
                <b>⚠️ Interpretive Blind Spot:</b> Applying strict textualism to beneficial legislation defeats the purpose of remedial statutes. Courts consistently favor interpretations that advance social justice over literal technicalities.
            </div>
            """, unsafe_allow_html=True)
