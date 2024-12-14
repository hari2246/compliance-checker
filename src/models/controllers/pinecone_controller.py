import os
from pinecone import Pinecone, ServerlessSpec

# Load Pinecone API key from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize the Pinecone client by creating an instance
pc = Pinecone(api_key=PINECONE_API_KEY, environment="us-west1-gcp")

def upsert_to_pinecone(index_name, embeddings, ids):
    # Check if the index exists, if not, create it
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=len(embeddings[0]),  # Assumes embeddings are 2D, each with the same dimension
            metric="euclidean",  # You can use cosine or other metrics
            spec=ServerlessSpec(
                cloud="aws",  # or another cloud provider
                region="us-west-2"  # or other regions
            )
        )
    
    # Create the index instance
    index = pc.Index(index_name)

    # Prepare the vectors for upsert
    vectors = [{"id": str(ids[i]), "values": embeddings[i]} for i in range(len(embeddings))]

    # Upsert the vectors into Pinecone
    index.upsert(vectors)

    return {"message": f"Upserted {len(embeddings)} vectors to Pinecone index '{index_name}'"}
