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

    query = "¿Optimiza las rutas de distribución?"

    print(f"\nConsulta:\n{query}")


    results = retriever.search(query)

    print("\n===== METADATA =====")

    for i, doc in enumerate(results, start=1):
        print(f"\nDocumento {i}")
        print(doc.metadata)
    

    # retriever.print_results(results)

    return
     
if __name__ == "__main__":
    main()