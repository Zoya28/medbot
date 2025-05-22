import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

groq_token = os.getenv("GROQ_API_KEY")

# Step 1: Load PDFs
def load_files(data_path="data/"):
    loader = DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
    return loader.load()

# Step 2: Chunk documents
def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

# Step 3: Embeddings
def create_embedding():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 4: Create vectorstore (or load)
def get_vectorstore():
    path = "vectorstore/faiss_index"
    embeddings = create_embedding()

    if os.path.exists(path):
        return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    else:
        data = create_chunks(load_files())
        db = FAISS.from_documents(data, embeddings)
        db.save_local(path)
        return db

# Step 5: Custom prompt
def set_custom_prompt():
    template = """Use the information provided in the context to answer the question.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{question}

(Answer directly, avoid small talk.)
"""
    return PromptTemplate(template=template, input_variables=["context", "question"])

# Step 6: Build QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.9,
        max_tokens=512,
    ),
    retriever=get_vectorstore().as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True,
    chain_type="stuff",
    chain_type_kwargs={"prompt": set_custom_prompt()},
)
