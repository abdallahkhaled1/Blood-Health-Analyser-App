import streamlit as st
import os
import pandas as pd

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Blood Health Analyser",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Serif+Display&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Page background */
.stApp {
    background: #f0f4f8;
}

/* Hero banner */
.hero-banner {
    background: linear-gradient(135deg, #1a3c6e 0%, #2563a8 60%, #1e8bc3 100%);
    border-radius: 16px;
    padding: 2.5rem 2rem 2rem 2rem;
    margin-bottom: 1.8rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: "🩸";
    font-size: 9rem;
    position: absolute;
    right: 2rem;
    top: -1rem;
    opacity: 0.12;
    pointer-events: none;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.4rem;
    color: #ffffff;
    margin: 0;
    line-height: 1.2;
}
.hero-sub {
    color: #a8c8e8;
    font-size: 1rem;
    margin-top: 0.5rem;
    font-weight: 300;
}

/* Stage cards */
.stage-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    border-left: 5px solid #2563a8;
}
.stage-card.green { border-left-color: #16a34a; }
.stage-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: #1a3c6e;
    margin-bottom: 0.3rem;
}
.stage-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: #64748b;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}

/* Metric pills */
.metric-row {
    display: flex;
    gap: 1rem;
    margin: 1rem 0 1.2rem 0;
    flex-wrap: wrap;
}
.metric-pill {
    border-radius: 50px;
    padding: 0.5rem 1.4rem;
    font-size: 0.95rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.4rem;
    min-width: 100px;
    justify-content: center;
}
.pill-high   { background: #fee2e2; color: #b91c1c; }
.pill-low    { background: #dbeafe; color: #1d4ed8; }
.pill-normal { background: #dcfce7; color: #15803d; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #1a3c6e !important;
}
section[data-testid="stSidebar"] * {
    color: #e2eaf4 !important;
}
section[data-testid="stSidebar"] .stTextInput label,
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label {
    color: #a8c8e8 !important;
    font-size: 0.82rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
section[data-testid="stSidebar"] input {
    background: #243f66 !important;
    border: 1px solid #2e5182 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
}
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
    background: #243f66 !important;
    border: 1px solid #2e5182 !important;
    border-radius: 8px !important;
}
section[data-testid="stSidebar"] hr {
    border-color: #2e5182 !important;
}

/* How it works steps */
.step {
    display: flex;
    align-items: flex-start;
    gap: 0.7rem;
    margin-bottom: 0.7rem;
    font-size: 0.88rem;
    color: #a8c8e8 !important;
}
.step-num {
    background: #2563a8;
    color: #ffffff !important;
    border-radius: 50%;
    width: 22px;
    height: 22px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.72rem;
    font-weight: 700;
    flex-shrink: 0;
}

/* Upload area styling */
[data-testid="stFileUploaderDropzone"] {
    background: #ffffff !important;
    border: 2px dashed #93c5fd !important;
    border-radius: 12px !important;
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #2563a8, #1e8bc3) !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    padding: 0.75rem 2rem !important;
    letter-spacing: 0.02em !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 14px rgba(37,99,168,0.35) !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(37,99,168,0.45) !important;
}

/* Download button */
.stDownloadButton > button {
    background: #ffffff !important;
    color: #1a3c6e !important;
    border: 2px solid #2563a8 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: #f8fafc !important;
    border-radius: 8px !important;
    font-size: 0.88rem !important;
    color: #1a3c6e !important;
    font-weight: 500 !important;
}

/* Diet plan output styling */
.diet-section h3 { color: #1a3c6e; font-size: 1.1rem; }
.diet-section li  { margin-bottom: 0.35rem; line-height: 1.6; }

/* Empty state */
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: #94a3b8;
}
.empty-icon { font-size: 4rem; margin-bottom: 1rem; }
.empty-text { font-size: 1.1rem; font-weight: 500; }
.empty-sub  { font-size: 0.88rem; margin-top: 0.4rem; }

/* Alert overrides */
.stSuccess { border-radius: 10px !important; }
.stWarning { border-radius: 10px !important; }
.stError   { border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚕️ Configuration")
    st.markdown("---")

    google_api_key = st.text_input(
        "Google API Key",
        type="password",
        placeholder="AIza...",
        help="Get your free key at aistudio.google.com",
    )

    model_choice = st.selectbox(
        "Gemini Model",
        ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"],
        index=0,
    )

    st.markdown("---")
    st.markdown("**How it works**")
    for num, text in [
        ("1", "Upload a blood report (.txt)"),
        ("2", "AI extracts every test value"),
        ("3", "Values are classified HIGH / LOW / NORMAL"),
        ("4", "Get a personalised Egyptian diet plan"),
    ]:
        st.markdown(
            f'<div class="step"><span class="step-num">{num}</span>{text}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown(
        '<span style="font-size:0.75rem;color:#6b8eb5;">Powered by Google Gemini · Built with Streamlit</span>',
        unsafe_allow_html=True,
    )


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">Blood Health Analyser</div>
    <div class="hero-sub">
        Upload your blood work report → get an instant AI analysis<br>
        and a personalised Egyptian diet plan in seconds.
    </div>
</div>
""", unsafe_allow_html=True)


# ── File uploader ─────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Upload Blood Report (.txt)",
    type=["txt"],
    help="Paste your lab results into a plain-text file and upload it here.",
    label_visibility="collapsed",
)


# ── Helper: parse extracted values into a DataFrame ───────────────────────────
def parse_extracted_values(text: str) -> pd.DataFrame:
    rows = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not (line.startswith("-") or line.startswith("•")):
            continue
        line = line.lstrip("-•").strip()
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 2:
            continue
        try:
            # "Test Name: Value"
            name_val = parts[0]
            colon = name_val.index(":")
            name  = name_val[:colon].strip()
            value = name_val[colon + 1:].strip()

            status    = parts[1].replace("Status:", "").strip().upper()
            reference = parts[2].replace("Reference:", "").strip() if len(parts) > 2 else "N/A"

            rows.append({"Test": name, "Value": value, "Status": status, "Reference Range": reference})
        except Exception:
            continue
    return pd.DataFrame(rows)


def style_status(val: str) -> str:
    colours = {
        "HIGH":   "background-color:#fee2e2;color:#b91c1c;font-weight:700",
        "LOW":    "background-color:#dbeafe;color:#1d4ed8;font-weight:700",
        "NORMAL": "background-color:#dcfce7;color:#15803d;font-weight:700",
    }
    return colours.get(val, "")


# ── Main flow ─────────────────────────────────────────────────────────────────
if uploaded_file is None:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">🩸</div>
        <div class="empty-text">No report uploaded yet</div>
        <div class="empty-sub">Drop a .txt blood-work file above to begin your analysis</div>
    </div>
    """, unsafe_allow_html=True)

else:
    blood_report = uploaded_file.read().decode("utf-8")

    with st.expander("📄 Preview Uploaded Report", expanded=False):
        st.code(blood_report, language=None)

    st.markdown("<br>", unsafe_allow_html=True)

    if not google_api_key:
        st.warning("⚠️  Enter your **Google API Key** in the sidebar to run the analysis.")
    else:
        run = st.button("🔬  Analyse Blood Report", type="primary", use_container_width=True)

        if run:
            os.environ["GOOGLE_API_KEY"] = google_api_key

            try:
                from langchain_google_genai import ChatGoogleGenerativeAI
                llm = ChatGoogleGenerativeAI(model=model_choice)

                # ── Stage 1 ───────────────────────────────────────────────────
                st.markdown('<div class="stage-card">', unsafe_allow_html=True)
                st.markdown('<div class="stage-label">Stage 1</div>', unsafe_allow_html=True)
                st.markdown('<div class="stage-title">🔬 Blood Value Extraction & Classification</div>', unsafe_allow_html=True)

                extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or NORMAL
based on the reference ranges provided in the report.

Format your response EXACTLY as one line per test:
- Test Name: Value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
"""
                with st.spinner("Extracting and classifying blood values …"):
                    ext_resp = llm.invoke(extraction_prompt)
                    extracted_values = ext_resp.content

                df = parse_extracted_values(extracted_values)

                if not df.empty:
                    # Summary metrics
                    high_n   = (df["Status"] == "HIGH").sum()
                    low_n    = (df["Status"] == "LOW").sum()
                    normal_n = (df["Status"] == "NORMAL").sum()

                    st.markdown(
                        f"""
                        <div class="metric-row">
                            <div class="metric-pill pill-high">🔴 High &nbsp; {high_n}</div>
                            <div class="metric-pill pill-low">🔵 Low &nbsp; {low_n}</div>
                            <div class="metric-pill pill-normal">🟢 Normal &nbsp; {normal_n}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    styled = df.style.applymap(style_status, subset=["Status"])
                    st.dataframe(styled, use_container_width=True, hide_index=True)
                else:
                    st.text(extracted_values)          # fallback if parsing fails

                st.markdown("</div>", unsafe_allow_html=True)

                # ── Stage 2 ───────────────────────────────────────────────────
                st.markdown('<div class="stage-card green">', unsafe_allow_html=True)
                st.markdown('<div class="stage-label">Stage 2</div>', unsafe_allow_html=True)
                st.markdown('<div class="stage-title">🥗 Health Summary & Egyptian Diet Plan</div>', unsafe_allow_html=True)

                diet_prompt = f"""
You are a clinical nutritionist specializing in Egyptian dietary habits.

Based on the blood work analysis below, write:
1. A short health summary in 4–5 lines explaining the patient's condition in simple language.
2. A short, practical Egyptian diet plan with ONLY TWO sections:
   (1) Foods to avoid
   (2) Foods to eat more of
   Do not add any other sections.

Blood Work Analysis:
{extracted_values}
"""
                with st.spinner("Generating personalised diet plan …"):
                    diet_resp = llm.invoke(diet_prompt)
                    diet_plan = diet_resp.content

                st.markdown('<div class="diet-section">', unsafe_allow_html=True)
                st.markdown(diet_plan)
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

                # ── Download ──────────────────────────────────────────────────
                full_report = (
                    "BLOOD HEALTH ANALYSIS REPORT\n"
                    + "=" * 50 + "\n\n"
                    "STAGE 1 – EXTRACTED VALUES\n"
                    + extracted_values + "\n\n"
                    + "=" * 50 + "\n\n"
                    "STAGE 2 – HEALTH SUMMARY & DIET PLAN\n"
                    + diet_plan
                )

                st.download_button(
                    label="📥  Download Full Report",
                    data=full_report,
                    file_name="health_analysis_report.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
                st.success("✅  Analysis complete!")

            except ImportError:
                st.error(
                    "Missing dependency — run:  "
                    "`pip install langchain-google-genai`"
                )
            except Exception as exc:
                st.error(f"❌  Error: {exc}")
                st.info("Double-check your API key and make sure you have internet access.")
