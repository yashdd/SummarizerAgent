import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
print(f"✅ Currently using model: {llm.model_name}")


# Load the pdf file and chunk it into smaller pieces 
def load_and_chunk_pdf(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = splitter.split_documents(pages)
    return docs

#Build the vectorstore from the loaded and chunked pdf documents
def build_vectorstore(docs):
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# Function to Summarize PDF Docs 
def summarize_document(docs):
    chain = load_qa_chain(llm, chain_type="map_reduce")
    summary = chain.run(input_documents=docs, question="Give me a concise summary of this research paper.")
    return summary

#Function to answer queries using the vectorstore
def answer_query(vectorstore, query):
    chain = load_qa_chain(llm, chain_type="stuff")
    relevant_docs = vectorstore.similarity_search(query,k=5)
    return chain.run(input_documents=relevant_docs, question=query)

