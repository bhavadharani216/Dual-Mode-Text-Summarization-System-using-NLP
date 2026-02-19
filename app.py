import streamlit as st
from extractive import extractive_summary
from abstractive import abstractive_summary

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Dual Mode Text Summarizer",
    page_icon="🧠",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: white;
    }
    .sub-title {
        text-align: center;
        color: #f0f0f0;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background: linear-gradient(to right, #667eea, #764ba2);
        color: white;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("""
    <div style="background: linear-gradient(to right, #667eea, #764ba2);
                padding: 20px; border-radius: 10px;">
        <div class="main-title">🧠 Dual Mode Text Summarizer</div>
        <div class="sub-title">
            Generate summaries using Extractive & Abstractive NLP
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# ------------------ TWO COLUMN LAYOUT ------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Input Section")

    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

    text_input = st.text_area("Or Paste Your Text Here", height=250)

    mode = st.radio(
        "Choose Summarization Mode",
        ("Extractive", "Abstractive", "Compare Both")
    )

    generate = st.button("Generate Summary")

with col2:
    st.subheader("📤 Summary Output")

    if generate:
        if uploaded_file:
            text = uploaded_file.read().decode("utf-8")
        else:
            text = text_input

        if not text.strip():
            st.warning("Please provide some text.")
        else:
            if mode == "Extractive":
                summary = extractive_summary(text)
                st.success("Extractive Summary Generated")
                st.write(summary)

            elif mode == "Abstractive":
                summary = abstractive_summary(text)
                st.success("Abstractive Summary Generated")
                st.write(summary)

            elif mode == "Compare Both":
                st.success("Comparison Mode")
                st.markdown("### 🔹 Extractive Summary")
                st.write(extractive_summary(text))

                st.markdown("### 🔹 Abstractive Summary")
                st.write(abstractive_summary(text))

 
 
