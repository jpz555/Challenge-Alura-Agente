"""
=========================================================
Indexer - Vector Store
=========================================================

Responsabilidad:
    Crear, cargar y administrar la base vectorial ChromaDB.

Versión:
    2.0.0
=========================================================
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_chroma import Chroma


class VectorStore:

    COLLECTION_NAME = "logimind_knowledge_base"

    def __init__(self, persist_directory: Path, embedding_function):

        self.persist_directory = str(persist_directory)

        self.embedding_function = embedding_function

        self.db = None

    # =====================================================
    # CREAR BASE VECTORIAL (REINDEXACIÓN COMPLETA)
    # =====================================================

    def create(self, documents: List[Document]):

        # ---------------------------------------------
        # Si existe una colección previa la eliminamos
        # ---------------------------------------------

        try:

            existing_db = Chroma(

                collection_name=self.COLLECTION_NAME,

                embedding_function=self.embedding_function,

                persist_directory=self.persist_directory

            )

            existing_db.delete_collection()

            print("Colección anterior eliminada.")

        except Exception:

            print("No existe una colección previa.")

        # ---------------------------------------------
        # Crear nueva colección
        # ---------------------------------------------

        self.db = Chroma.from_documents(

            documents=documents,

            embedding=self.embedding_function,

            collection_name=self.COLLECTION_NAME,

            persist_directory=self.persist_directory

        )

        print("Nueva colección creada.")

        return self.db

    # =====================================================
    # CARGAR BASE EXISTENTE
    # =====================================================

    def load(self):

        self.db = Chroma(

            collection_name=self.COLLECTION_NAME,

            embedding_function=self.embedding_function,

            persist_directory=self.persist_directory

        )

        return self.db

    # =====================================================
    # AGREGAR NUEVOS DOCUMENTOS
    # =====================================================

    def add_documents(self, documents: List[Document]):

        if self.db is None:

            self.load()

        self.db.add_documents(documents)

        print(f"{len(documents)} documentos agregados.")

    # =====================================================
    # RETRIEVER
    # =====================================================

    def as_retriever(self, k: int = 4):

        if self.db is None:

            raise RuntimeError(
                "Debe crear o cargar la base vectorial primero."
            )

        return self.db.as_retriever(

            search_kwargs={

                "k": k

            }

        )

    # =====================================================
    # TOTAL DE DOCUMENTOS
    # =====================================================

    def count(self):

        if self.db is None:

            return 0

        return self.db._collection.count()

    # =====================================================
    # INFORMACIÓN
    # =====================================================

    def info(self):

        print("\n")

        print("=" * 60)

        print("VECTOR STORE")

        print("=" * 60)

        print(f"Colección : {self.COLLECTION_NAME}")

        print(f"Directorio: {self.persist_directory}")

        if self.db is not None:

            print(f"Documentos: {self.count()}")

        print("=" * 60)

    # =====================================================
    # ELIMINAR COLECCIÓN
    # =====================================================

    def delete(self):

        try:

            if self.db is None:

                self.load()

            self.db.delete_collection()

            print("Colección eliminada.")

        except Exception:

            print("No existe ninguna colección.")