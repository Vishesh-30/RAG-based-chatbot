import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from src.config import Config

def create_embeddings(chunks):
    encoder = SentenceTransformer(Config.EMBEDDING_MODEL)
    embeddings = encoder.encode([chunk.page_content for chunk in chunks])
    return embeddings, encoder

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dim)
    faiss_index.add(embeddings)
    print(f"FAISS index populated with {embeddings.shape[0]} embeddings.")
    return faiss_index
