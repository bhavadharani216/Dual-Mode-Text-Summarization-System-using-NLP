import streamlit as st
from extractive import extractive_summary
from abstractive import abstractive_summary

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Dual Mode AI Summarizer",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main background */
body {
    background-color: #f4f6fb;
}

/* Header gradient */
.main-container {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

/* Section box clean white */
.section-box {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background: linear-gradient(to right, #4f46e5, #9333ea);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "summary_output" not in st.session_state:
    st.session_state.summary_output = ""

# ---------------- HEADER ----------------
st.markdown("""
<div class="main-container">
    <h1>🧠 Dual Mode AI Text Summarizer</h1>
    <p>Generate Smart Extractive & Abstractive Summaries Instantly</p>
</div>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

# ================= INPUT SECTION =================
with col1:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("📥 Input Section")

    uploaded_file = st.file_uploader("Upload .txt file", type=["txt"])

    st.text_area(
        "Or Paste Your Text",
        height=250,
        key="input_text"
    )

    mode = st.selectbox(
        "Select Summarization Mode",
        ("Extractive", "Abstractive", "Compare Both")
    )

    colA, colB = st.columns(2)

    with colA:
        generate = st.button("🚀 Generate")

    with colB:
        clear = st.button("🧹 Clear")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= OUTPUT SECTION =================
with col2:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("📤 Summary Output")

    if generate:
        if uploaded_file:
            text = uploaded_file.read().decode("utf-8")
        else:
            text = st.session_state.input_text

        if not text.strip():
            st.warning("Please provide some text.")
        else:
            with st.spinner("AI is generating summary... ⏳"):
                if mode == "Extractive":
                    summary = extractive_summary(text)
                    st.session_state.summary_output = summary

                elif mode == "Abstractive":
                    summary = abstractive_summary(text)
                    st.session_state.summary_output = summary

                elif mode == "Compare Both":
                    extract = extractive_summary(text)
                    abstract = abstractive_summary(text)

                    combined = (
                        "🔹 Extractive Summary:\n\n"
                        + extract
                        + "\n\n---------------------------------------\n\n"
                        + "🔹 Abstractive Summary:\n\n"
                        + abstract
                    )

                    st.session_state.summary_output = combined

    if st.session_state.summary_output:
        st.success("✨ Summary Generated Successfully!")
        st.write(st.session_state.summary_output)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CLEAR FUNCTION ----------------
if clear:
    st.session_state.input_text = ""
    st.session_state.summary_output = ""
    st.rerun()

 
