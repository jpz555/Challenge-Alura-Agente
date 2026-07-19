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

    vector_store.info()

    print("\nBase vectorial creada correctamente.")

    print(f"Documentos indexados: {db._collection.count()}")
    print(f"Collection Count     : {vector_store.db._collection.count()}")

    print("=" * 70)


if __name__ == "__main__":
    main()