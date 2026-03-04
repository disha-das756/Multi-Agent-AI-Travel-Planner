from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Vector DB     creating a Chroma vector database object trip_db is just a Python variable name .This objct will store embeddings (vectors) and allow similarity search
trip_db = Chroma(
    persist_directory="memory/db",   #This tells Chroma where to store data on disk
    embedding_function=embeddings
)

def save_trip_memory(state):
    """
    Stores past trip details in vector memory
    """
    text = f"""
    Destination: {state['destination']}
    Days: {state['days']}
    Budget: {state['budget']}
    Interests: {', '.join(state['interests'])}
    """

    trip_db.add_texts([text])
    


def get_similar_trips(destination, interests):
    """
    Finds similar past trips
    """
    query = f"{destination} {', '.join(interests)}"
    results = trip_db.similarity_search(query, k=2)
    return [doc.page_content for doc in results]