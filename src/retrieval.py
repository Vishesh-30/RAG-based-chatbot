import numpy as np

class FaissRetriever:
    def __init__(self, index, chunks):
        self.index = index
        self.chunks = chunks

    def retrieve(self, query_embedding, k=2):
        distances, indices = self.index.search(np.array([query_embedding]), k)
        # print(f"Indices: {indices}, Distances: {distances}")  # Debugging line
        if len(indices) == 0 or len(indices[0]) == 0:
            return []
        retrieved_chunks = [(self.chunks[idx], distances[0][i]) for i, idx in enumerate(indices[0]) if idx < len(self.chunks)]
        # print(retrieved_chunks)
        return retrieved_chunks

