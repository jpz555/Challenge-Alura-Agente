"""
=========================================================
RAG - Model Factory
=========================================================

Responsabilidad:
    Crear y configurar el modelo de lenguaje
    seleccionado en config.py.

Proveedores soportados:

    • Gemini
    • Ollama
    • Groq

El resto del proyecto nunca debe importar
ChatGoogleGenerativeAI, ChatOllama o ChatGroq.

Siempre deberá utilizar:

    ModelFactory.create()

=========================================================
"""

import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq

from rag.config import (
    DEFAULT_PROVIDER,
    MODELS,
    TEMPERATURE,
    TOP_P,
    MAX_OUTPUT_TOKENS,
    STRUCTURED_OUTPUT,
    GEMINI_API_KEY,
    GROQ_API_KEY,
)

from rag.schemas import RagResponse


class ModelFactory:
    """
    Factory para crear modelos de lenguaje.

    Ejemplos
    --------
    llm = ModelFactory.create()

    llm = ModelFactory.create(provider="ollama")

    llm = ModelFactory.create(
        provider="gemini",
        model="gemini-2.5-pro"
    )
    """

    @classmethod
    def create(cls, provider: str | None = None, model: str | None = None):
        """
        Crea un modelo completamente configurado.
        """
        provider = (provider or DEFAULT_PROVIDER).lower()
        if provider not in MODELS:
            raise ValueError(f"Proveedor no soportado: {provider}")

        model = model or MODELS[provider]
        # print(f"Inicializando modelo Groq ({model})...")
        if provider == "gemini":
            llm = cls._create_gemini(model)
        elif provider == "ollama":
            llm = cls._create_ollama(model)
        elif provider == "groq":
            llm = cls._create_groq(model)
        else:
            raise ValueError(
                f"Proveedor no soportado: {provider}"
            )

        return llm

    # =====================================================
    # GEMINI
    # =====================================================
    @staticmethod
    def _create_gemini(model: str):
        # api_key = os.getenv(GEMINI_API_KEY)
        if not GEMINI_API_KEY:
            raise ValueError("No se encontró GEMINI_API_KEY.")
        return ChatGoogleGenerativeAI(
            model=model,
            google_api_key=GEMINI_API_KEY,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            max_output_tokens=MAX_OUTPUT_TOKENS,
        )

    # =====================================================
    # OLLAMA
    # =====================================================
    @staticmethod
    def _create_ollama(model: str):

        return ChatOllama(
            model=model,
            temperature=TEMPERATURE,
        )

    # =====================================================
    # GROQ
    # =====================================================

    @staticmethod
    def _create_groq(model: str):
        # api_key = os.getenv(GROQ_API_KEY)
        # print("Seleccionando Modelo Groq")
        if not GROQ_API_KEY:
            raise ValueError("No se encontró GROQ_API_KEY.")

        return ChatGroq(
            model=model,
            api_key=GROQ_API_KEY,
            temperature=TEMPERATURE,
        )

    # =====================================================
    # CONFIGURACIÓN COMÚN
    # =====================================================

    # @staticmethod
    # def _configure_llm(llm):
    #     """
    #     Aplica la configuración común
    #     para todos los proveedores.
    #     """

    #     # if STRUCTURED_OUTPUT:
    #     #     llm = llm.with_structured_output(RagResponse)

    #     return llm