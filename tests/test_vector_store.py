from document_processor.config import CHUNKS_OUTPUT_DIR, VECTOR_DB_DIR

from indexer.loader import ChunkLoader
from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore


def main():

    print("=" * 70)
    print("TEST - VECTOR STORE")
    print("=" * 70)

    # -------------------------------------------------
    # Loader
    # -------------------------------------------------

    loader = ChunkLoader(CHUNKS_OUTPUT_DIR)

    documents = loader.load()
    
    for doc in documents:
        if doc.metadata["document_code"] == "CORP-001":
            if "CD-01" in doc.page_content:
                print("="*80)
                print(doc.metadata)
                print(doc.page_content)

    print(f"\nDocumentos cargados: {len(documents)}")

    # -------------------------------------------------
    # Embeddings
    # -------------------------------------------------

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.langchain_model

    # -------------------------------------------------
    # Vector Store
    # -------------------------------------------------

    vector_store = VectorStore(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embeddings
    )

    db = vector_store.create(documents)
    
    print("Query")
    docs = vector_store.similarity_search(
    query="¿Dónde está ubicado el CD-01?",
        k=10
    )

    vector_store.info()

    print("\nBase vectorial creada correctamente.")

    print(f"Documentos indexados: {db._collection.count()}")
    print(f"Collection Count     : {vector_store.db._collection.count()}")

    print("=" * 70)


if __name__ == "__main__":
    main()