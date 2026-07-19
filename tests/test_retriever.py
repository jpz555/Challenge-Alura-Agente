from document_processor.config import VECTOR_DB_DIR

from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore
from indexer.retriever import KnowledgeRetriever

def main():
    print("=" * 70)
    print("TEST - RETRIEVER")
    print("=" * 70)

    # -----------------------------------------------------
    # Modelo de embeddings
    # -----------------------------------------------------
    
    embedding_model = EmbeddingModel()

    embeddings = embedding_model.langchain_model

    # -----------------------------------------------------
    # Cargar ChromaDB
    # -----------------------------------------------------

    vector_store = VectorStore(persist_directory=VECTOR_DB_DIR, embedding_function=embeddings)

    vector_store.load()

    # -----------------------------------------------------
    # Retriever
    # -----------------------------------------------------

    retriever = KnowledgeRetriever(vector_store=vector_store, k=4)

    query = "¿Cuál es el horario operativo de la empresa?"

    print(f"\nConsulta:\n{query}")

    results = retriever.search(query)
    

    retriever.print_results(results)
    
    print("\nChunk UUIDs recuperados:\n")

    for doc in results:
        print(doc.metadata["chunk_uuid"])


if __name__ == "__main__":
    main()