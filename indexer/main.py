"""
indexer/main.py

Construye la base vectorial a partir de los chunks generados
por el módulo document_processor.
"""

from time import perf_counter
from collections import Counter

from document_processor.config import CHUNKS_OUTPUT_DIR, VECTOR_DB_DIR

from indexer.loader import ChunkLoader
from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore


def main() -> None:
    """
    Ejecuta el proceso completo de indexación.

    Flujo
    -----
    Chunks
        ↓
    Loader
        ↓
    Embeddings
        ↓
    VectorStore.create()
        ↓
    Base Vectorial
    """

    start = perf_counter()

    print("\n" + "=" * 80)
    print("INDEXADOR DE DOCUMENTOS")
    print("=" * 80)

    try:
        # =====================================================
        # CARGAR CHUNKS
        # =====================================================
        print("\n[1/3] Cargando documentos...")

        loader = ChunkLoader(CHUNKS_OUTPUT_DIR)

        documents = loader.load()

        if not documents:
            raise RuntimeError(
                "No se encontraron documentos para indexar."
            )

        print(f"Documentos cargados : {len(documents)}")

        # =====================================================
        # MODELO DE EMBEDDINGS
        # =====================================================
        print("\n[2/3] Inicializando modelo de embeddings...")

        embedding_model = EmbeddingModel()

        # =====================================================
        # CREAR BASE VECTORIAL
        # =====================================================

        print("\n[3/3] Construyendo base vectorial...")
        vector_store = VectorStore(
            persist_directory=VECTOR_DB_DIR,
            embedding_function=embedding_model.langchain_model,
        )
        
        vector_store.create(documents)

        # =====================================================
        # INFORMACIÓN FINAL
        # =====================================================

        print("\n")

        vector_store.info()
        elapsed = perf_counter() - start

        print("\n" + "=" * 80)
        print("INDEXACIÓN FINALIZADA")
        print("=" * 80)
        print(f"Tiempo total : {elapsed:.2f} segundos")
        
                
        print("\n===== CATEGORÍAS =====")
        print(Counter(doc.metadata["category"] for doc in documents))

        print("\n===== PRIMEROS 20 DOCUMENTOS =====")
        for d in documents[:20]:
            print(
                d.metadata["document_code"],
                d.metadata["category"],
                d.metadata["source_file"],
    )

    except Exception as error:

        print("\n" + "=" * 80)
        print("ERROR DURANTE LA INDEXACIÓN")
        print("=" * 80)
        print(error)

        raise

if __name__ == "__main__":
    main()