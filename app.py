import streamlit as st
from src.data_loader import load_and_split_data
from src.embed_faiss import create_embeddings, create_faiss_index
from src.retrieval import FaissRetriever
from src.chain_of_thoughts import generate_summary
from src.save_model import download_and_save_models

# Download and save models
summarizer, encoder = download_and_save_models()

# Placeholder for FAISS index and chunks
faiss_index = None
chunks = []

st.title("Summarizer Bot")
st.sidebar.title("Document Uploader")

# URL input
url = st.sidebar.text_input("Enter the URL of the document")

if st.sidebar.button("Load Document"):
    with st.spinner('Loading document...'):
        try:
            chunks = load_and_split_data(url)
            embeddings, encoder = create_embeddings(chunks)
            faiss_index = create_faiss_index(embeddings)
            st.sidebar.success("Document loaded and embeddings generated!")
            st.session_state.chunks = chunks
            st.session_state.faiss_index = faiss_index
        except Exception as e:
            st.sidebar.error(f"Error loading document: {e}")

# Chat interface
st.subheader("Chat with the Summarizer Bot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You: ", key="user_input")

if st.button("Send"):
    if "faiss_index" in st.session_state and "chunks" in st.session_state:
        faiss_index = st.session_state.faiss_index
        chunks = st.session_state.chunks
        faiss_retriever = FaissRetriever(faiss_index, chunks)
        try:
            bot_response = generate_summary(user_input, faiss_retriever, encoder, summarizer)
            st.session_state.history.append({"user": user_input, "bot": bot_response})
        except Exception as e:
            st.error(f"Error generating response: {e}")
    else:
        st.warning("Please load a document first.")

# Display chat history
for chat in reversed(st.session_state.history):
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
