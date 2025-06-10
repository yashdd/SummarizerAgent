# 🤖 SummarizerAgent

**SummarizerAgent** is an AI-powered research assistant that reads, understands, and summarizes academic PDFs. It also supports an interactive Q&A experience where you can ask questions about the paper as if you're chatting with someone who already read it deeply.

Built with **LangChain**, **OpenAI**, and **Streamlit**, this project brings smart document understanding to your fingertips.

---

## 🧠 Key Features
- 📄 Upload any research paper (PDF)
- 📝 Get an automatic summary
- 💬 Ask follow-up questions via chat
- 🔍 Retrieves accurate context from the paper using embeddings


---

## ⚙️ Tech Stack
- **LangChain**: Agent logic, chains, retrieval
- **OpenAI**: GPT-3.5 / GPT-4 (LLM + Embeddings)
- **FAISS**: Vector similarity search
- **Streamlit**: Chat-style frontend
- **PyMuPDF / LangChain PDFLoader**: PDF parsing

---

## 📂 Folder Structure

```bash
SummarizerAgent/
│
├── README.md                  # Project overview
├── requirements.txt           # All required Python packages
├── .env.example               # Sample env file for OpenAI key
│
├── app/
│   ├── app.py                 # Main Streamlit app (chat interface)
│   ├── qa_summarizer.py       # LangChain logic (summary + Q&A)
│   ├── utils.py               # Helper functions: chunking, file handling
│   └── __init__.py
│
├── papers/                    # Uploaded papers
│   └── sample_paper.pdf
│
├── outputs/                   # Auto-generated summary & chat history
│   ├── summary.txt
│   └── chat_log.txt
│
└── assets/                    # Screenshots or logos for the README/UI
    └── demo.png
```

## 📄 License

This project is for Learning Purpose only


## 👤 Author

**Yash Deshpande**  
📧 yashdd10@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/yash-deshpande-70827417b)  
🌐 [Portfolio](https://yashdd.github.io/Portfolio-Website)

