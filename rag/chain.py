"""
chain.py
---------

Orquestador principal del flujo RAG.

Responsabilidades:
- Recuperar documentos relevantes.
- Construir el prompt.
- Invocar el modelo.
- Retornar un RagResponse.

No contiene lógica de negocio.
No construye prompts.
No interactúa directamente con Chroma.
No conoce detalles del proveedor LLM.
"""

from __future__ import annotations

import logging

from document_processor.config import VECTOR_DB_DIR
from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore
from indexer.retriever import KnowledgeRetriever
from rag.models import ModelFactory
from rag.prompt_builder import PromptBuilder
from rag.schemas import RagResponse
from rag.response_parser import ResponseParser



logger = logging.getLogger(__name__)


class RagChain:
    """
    Orquestador del flujo Retrieval-Augmented Generation (RAG).
    """

    def __init__(self, vector_store: VectorStore | None = None, 
                 provider: str | None = None, 
                 model: str | None = None, 
                 k:int = 4) -> None:
        """
        Inicializa todos los componentes necesarios del flujo RAG.
        """
        
        embedding_model = EmbeddingModel()
        try:
            self.vector_store = VectorStore(persist_directory=VECTOR_DB_DIR, embedding_function = embedding_model.langchain_model)
            self.vector_store.load()
            self.retriever = KnowledgeRetriever(vector_store=self.vector_store, k=k)
            self.prompt_builder = PromptBuilder()
            self.llm = ModelFactory.create(provider=provider,model=model)
                
            logger.info("RagChain inicializado correctamente.")

        except Exception as e:
            logger.exception("Error inicializando RagChain.")
            raise RuntimeError(
                "No fue posible inicializar el flujo RAG."
            ) from e
    
    def retrieve(self, question: str):
        return self.retriever.search(question)
    def invoke(self, question: str) -> RagResponse:
        """
        Ejecuta el flujo completo del RAG.

        Parameters
        ----------
        question : str
            Pregunta del usuario.

        Returns
        -------
        RagResponse
        """

        if not isinstance(question, str):
            raise TypeError("La pregunta debe ser una cadena de texto.")

        question = question.strip()

        if not question:
            raise ValueError(
                "La pregunta no puede estar vacía.")

        logger.info("Nueva consulta recibida.")

        try:
            # --------------------------------------------------
            # Recuperación
            # --------------------------------------------------
            documents = self.retriever.search(question)

            logger.info("Se recuperaron %s documentos.", len(documents))

            # --------------------------------------------------
            # Construcción del Prompt
            # --------------------------------------------------
            prompt = self.prompt_builder.build(
                question=question,
                documents=documents,
            )

            # --------------------------------------------------
            # Inferencia
            # --------------------------------------------------
            self.response_parser = ResponseParser()
            # print("\n========== PROMPT ==========")
            # print(prompt)
            response = self.llm.invoke(prompt)
            
            # print("\n========== RESPUESTA LLM ==========")
            # print(response)

            logger.info("Respuesta generada correctamente.")
            
            # print("\n========== CONTENT ==========")

            try:
                print(response.content)
            except AttributeError:
                print(response)
            return self.response_parser.parse(response)

        except Exception as e:

            logger.exception("Error durante la ejecución del flujo RAG.")
            
            raise
            # raise RuntimeError("Ocurrió un error durante la generación de la respuesta.") from e
        