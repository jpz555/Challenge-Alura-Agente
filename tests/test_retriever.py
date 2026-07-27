from pathlib import Path

from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore

# ======================================================
# Embeddings
# ======================================================

embedding = EmbeddingModel().langchain_model

# ======================================================
# Base vectorial
# ======================================================

vector_store = VectorStore(
    persist_directory=Path("vector_db"),   # <-- cambia si tu carpeta tiene otro nombre
    embedding_function=embedding
)

vector_store.load()

# ======================================================
# Pruebas
# ======================================================

consultas = [
    "CD-01 Barranquilla",
    "¿Dónde está ubicado el CD-01?",
    "Horario operativo"
]

for consulta in consultas:

    print("\n" + "=" * 80)
    print("CONSULTA:", consulta)
    print("=" * 80)

    docs = vector_store.similarity_search(
        query=consulta,
        k=5
    )

    for doc in docs:

        print(doc.metadata["chunk_id"])
        print(doc.metadata["section_path"])
        print()
# def main():
#     print("=" * 70)
#     print("TEST - RETRIEVER")
#     print("=" * 70)

#     # -----------------------------------------------------
#     # Modelo de embeddings
#     # -----------------------------------------------------
    
#     embedding_model = EmbeddingModel()

#     embeddings = embedding_model.langchain_model

#     # -----------------------------------------------------
#     # Cargar ChromaDB
#     # -----------------------------------------------------

#     vector_store = VectorStore(persist_directory=VECTOR_DB_DIR, embedding_function=embeddings)

#     vector_store.load()

#     # -----------------------------------------------------
#     # Retriever
#     # -----------------------------------------------------

#     retriever = KnowledgeRetriever(vector_store=vector_store, k=4)

#     query = "¿Optimiza las rutas de distribución?"

#     print(f"\nConsulta:\n{query}")


#     results = retriever.search(query)

#     print("\n===== METADATA =====")

#     for i, doc in enumerate(results, start=1):
#         print(f"\nDocumento {i}")
#         print(doc.metadata)
    

#     # retriever.print_results(results)

#     return
     
# if __name__ == "__main__":
#     main()