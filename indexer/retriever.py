"""
=========================================================
Indexer - Retriever
=========================================================

Responsabilidad:
    Recuperar documentos relevantes desde ChromaDB.

Versión:
    1.0.0
=========================================================
"""

from typing import List

from langchain_core.documents import Document

from indexer.vector_store import VectorStore


class KnowledgeRetriever:
    """
    Recupera documentos relevantes desde la base vectorial.
    """

    def __init__(self, vector_store: VectorStore, k: int = 4):

        self.vector_store = vector_store
        self.k = k

        self.retriever = self.vector_store.as_retriever(k=self.k)

    # =====================================================
    # BÚSQUEDA SEMÁNTICA
    # =====================================================

    def search(self, query: str) -> List[Document]:
        """
        Realiza una búsqueda semántica.

        Parameters
        ----------
        query : str

        Returns
        -------
        List[Document]
        """

        return self.retriever.invoke(query)

    # =====================================================
    # MOSTRAR RESULTADOS
    # =====================================================

    @staticmethod
    def print_results(documents: List[Document]):

        print("\n")

        print("=" * 80)

        print(f"Resultados encontrados: {len(documents)}")

        print("=" * 80)

        for i, doc in enumerate(documents, start=1):

            print(f"\nResultado {i}")

            print("-" * 80)

            print(f"Código      : {doc.metadata['document_code']}")

            print(f"Título      : {doc.metadata['document_title']}")

            print(f"Categoría   : {doc.metadata['category']}")

            print(f"Sección     : {doc.metadata['section_path']}")

            print(f"Chunk ID    : {doc.metadata['chunk_id']}")

            print(f"Chunk UUID  : {doc.metadata['chunk_uuid']}")

            print("\nContenido\n")

            print(doc.page_content[:500])

            print("\n" + "=" * 80)