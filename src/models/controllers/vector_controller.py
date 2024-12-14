import faiss
import numpy as np

def create_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))
    return index

def save_faiss_index(index, path='data/vector_store/faiss.index'):
    faiss.write_index(index, path)

def load_faiss_index(path='data/vector_store/faiss.index'):
    return faiss.read_index(path)
