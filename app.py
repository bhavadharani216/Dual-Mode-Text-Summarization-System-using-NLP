import streamlit as st
import time
from extractive import extractive_summary
from abstractive import abstractive_summary

st.set_page_config(page_title="Dual-Mode Text Summarizer", layout="centered")

# ---------- Theme Toggle (use checkbox for compatibility) ----------
theme = st.checkbox("🌗 Dark Mode", value=False)

# ---------- Custom CSS & Fonts ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 40%, #e8f9ff 100%);
        padding: 1.5rem 2rem 2rem 2rem;
    }

    /* Header */
    .app-header {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .app-title {
        font-size: 2.2rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #3b82f6, #a78bfa, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .app-sub {
        color: #374151;
        margin-top: 0.25rem;
        margin-bottom: 0.75rem;
    }

    /* Card style for inputs and results */
    .card {
        background: linear-gradient(180deg, rgba(255,255,255,0.85), rgba(250,250,250,0.8));
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 6px 18px rgba(14,30,37,0.08);
        margin-bottom: 1rem;
        border: 1px solid rgba(99,102,241,0.06);
    }

    /* Textarea & inputs */
    textarea, .stTextArea textarea, input, .stTextInput input {
        border-radius: 8px !important;
        padding: 0.75rem !important;
        font-size: 0.95rem !important;
        background: #ffffff !important;
        color: #0f172a !important;
        box-shadow: inset 0 1px 3px rgba(2,6,23,0.04);
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg,#7c3aed,#06b6d4);
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.6rem 1rem;
        box-shadow: 0 8px 20px rgba(12,18,52,0.08);
    }
    .stDownloadButton>button {
        background: linear-gradient(90deg,#10b981,#06b6d4);
        color: white;
        font-weight: 600;
        border-radius: 10px;
    }

    /* Result panels */
    .summary-box {
        background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(248,250,252,0.95));
        border-radius: 10px;
        padding: 0.75rem;
        border: 1px solid rgba(2,6,23,0.03);
        min-height: 180px;
    }

    /* Compact radio and info */
    .stRadio > div, .stInfo {
        margin-top: 0.25rem;
    }

    /* Dark mode overrides (apply when .stApp has `dark` class) */
    .stApp.dark {
        background: linear-gradient(135deg, #0f1724 0%, #071327 60%);
        color: #e6eef6;
    }
    .stApp.dark textarea, .stApp.dark .stTextArea textarea, .stApp.dark input, .stApp.dark .stTextInput input {
        background: #0b1220 !important;
        color: #e6eef6 !important;
    }
    .stApp.dark .card {
        background: linear-gradient(180deg, rgba(8,10,15,0.6), rgba(12,16,22,0.5));
        border: 1px solid rgba(255,255,255,0.04);
        box-shadow: 0 6px 18px rgba(2,6,23,0.6);
    }
    .stApp.dark .app-sub { color: #bcd4ff; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inject JS to add/remove 'dark' class on the Streamlit root element (.stApp)
if theme:
    st.markdown(
        "<script>const root=document.querySelector('.stApp'); if(root) root.classList.add('dark');</script>",
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        "<script>const root=document.querySelector('.stApp'); if(root) root.classList.remove('dark');</script>",
        unsafe_allow_html=True,
    )

# ---------- Title ----------
st.markdown(
    """
    <div class="app-header">
      <h1 class="app-title">📝 Dual-Mode Text Summarizer</h1>
      <p class="app-sub">Summarize long text using Extractive and Abstractive using NLP</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------- File Upload / Text Input ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📂 Upload a .txt file (optional)", type=["txt"])
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
    else:
        text = st.text_area("✍ Paste your text here:", height=220)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Mode Selection ----------
col1, col2 = st.columns([2,1])
with col1:
    mode = st.radio("Choose Mode:", ["Extractive", "Abstractive", "Compare Both"])
with col2:
    st.info("Extractive = picks important sentences" \
    "\nAbstractive = generates a new concise summary")

st.divider()

# ---------- Summarize ----------
if st.button("✨ Summarize Now"):
    if not text or not text.strip():
        st.warning("Please enter or upload some text.")
    else:
        start = time.time()
        with st.spinner("Summarizing... This may take a few seconds depending on input length."):
            if mode == "Extractive":
                summary = extractive_summary(text)
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("📌 Extractive Summary")
                st.markdown(f'<div class="summary-box"><pre style="white-space:pre-wrap; font-family:inherit;">{summary}</pre></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            elif mode == "Abstractive":
                summary = abstractive_summary(text)
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("📌 Abstractive Summary")
                st.markdown(f'<div class="summary-box"><pre style="white-space:pre-wrap; font-family:inherit;">{summary}</pre></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            else:
                ex = extractive_summary(text)
                ab = abstractive_summary(text)
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("🔁 Comparison")
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("### Extractive")
                    st.markdown(f'<div class="summary-box"><pre style="white-space:pre-wrap; font-family:inherit;">{ex}</pre></div>', unsafe_allow_html=True)
                with c2:
                    st.markdown("### Abstractive")
                    st.markdown(f'<div class="summary-box"><pre style="white-space:pre-wrap; font-family:inherit;">{ab}</pre></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

                summary = "EXTRACTIVE:\n" + ex + "\n\nABSTRACTIVE:\n" + ab

        end = time.time()
        st.success(f"⏱ Done in {round(end-start,2)} seconds")

        st.download_button(
            "📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )