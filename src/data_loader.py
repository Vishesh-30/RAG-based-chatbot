from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_data(url):
    loader = UnstructuredURLLoader(urls=[url])
    data = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", "."],
        chunk_size=1000,
        chunk_overlap=50)
    chunks = text_splitter.split_documents(data)
    
    return chunks