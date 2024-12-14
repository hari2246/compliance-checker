from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
    try:
        embeddings = model.encode(chunks, show_progress_bar=True)
        return embeddings
    except Exception as e:
        return {"error": f"Embedding generation failed: {str(e)}"}
