"""
=========================================================
Indexer - Embedding Model
=========================================================
Responsabilidad:
    Administrar el modelo de embeddings utilizado por el
    sistema RAG.

Versión:
    1.0.0
=========================================================
"""

from sentence_transformers import SentenceTransformer

from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    Clase encargada de administrar el modelo de embeddings.
    """

    # DEFAULT_MODEL = "BAAI/bge-m3"
    DEFAULT_MODEL = "intfloat/multilingual-e5-small"

    def __init__(self, model_name: str = DEFAULT_MODEL):

        self.model_name = model_name

        self._sentence_model = None
        self._langchain_model = None

    # =====================================================
    # MODELO SENTENCE TRANSFORMERS
    # =====================================================

    @property
    def sentence_model(self) -> SentenceTransformer:

        if self._sentence_model is None:

            print(f"Cargando modelo: {self.model_name}")

            self._sentence_model = SentenceTransformer(
                self.model_name
            )

        return self._sentence_model

    # =====================================================
    # MODELO LANGCHAIN
    # =====================================================

    @property
    def langchain_model(self) -> HuggingFaceEmbeddings:

        if self._langchain_model is None:

            self._langchain_model = HuggingFaceEmbeddings(
                model_name=self.model_name,
                model_kwargs={
                    "device": "cpu"
                },
                encode_kwargs={
                    "normalize_embeddings": True
                }
            )

        return self._langchain_model

    # =====================================================
    # INFORMACIÓN DEL MODELO
    # =====================================================

    def info(self):

        print("=" * 60)

        print("Embedding Model")

        print("=" * 60)

        print(f"Modelo : {self.model_name}")

        print("=" * 60)