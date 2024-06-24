from transformers import pipeline
from sentence_transformers import SentenceTransformer
from src.config import Config

def download_and_save_models():
    summarizer = pipeline("summarization", model=Config.SUMMARIZATION_MODEL)
    encoder = SentenceTransformer(Config.EMBEDDING_MODEL)
    return summarizer, encoder
