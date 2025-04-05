import streamlit as st
import os
from summarizer import (
    load_and_chunk_pdf,
    build_vectorstore,
    summarize_document,
    answer_query
)

st.set_page_config(page_title="SummarizerAgent", layout="centered")
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 SummarizerAgent")
st.markdown("Upload a research paper, get a smart summary, and chat with it in real-time.")
st.markdown("---")
st.subheader("📄 Upload PDF")
st.subheader("📜 Auto-generated Summary")
st.subheader("💬 Ask a Question")


# Upload PDF
pdf_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])

# Session state for storing vector store and docs
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



if pdf_file:
    with st.spinner("Reading and processing PDF..."):
        # Save PDF temporarily
        pdf_path = os.path.join("papers", pdf_file.name)
        st.session_state.chat_history = []

        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())

        # Load, chunk, embed
        docs = load_and_chunk_pdf(pdf_path)
        st.session_state.vectorstore = build_vectorstore(docs)

        # Summarize
        summary = summarize_document(docs)
        st.success("Summary generated!")
        st.markdown("### 📜 Summary")
        st.info(summary)

    # Question-Answer Chat Interface
    st.markdown("### 💬 Ask a question about the paper")

    user_input = st.text_input("Your question", placeholder="e.g., What is the methodology used?")
    if user_input and st.session_state.vectorstore:
        with st.spinner("Thinking..."):
            response = answer_query(st.session_state.vectorstore, user_input)
            st.session_state.chat_history.append((user_input, response))

    # Display chat history
    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**AI:** {a}")
        st.markdown("---")

        output_dir = "outputs"
        os.makedirs(output_dir, exist_ok=True)

        summary_path = os.path.join(output_dir, "summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)

    with open("outputs/chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Q: {user_input}\nA: {response}\n\n")