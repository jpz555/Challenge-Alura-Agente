"""
=========================================================
RAG - Response Parser
=========================================================

Responsabilidad:
    Convertir la respuesta del LLM en un objeto
    RagResponse independiente del proveedor.

Versión:
    1.0.0
=========================================================
"""

from __future__ import annotations

import json

from langchain_core.messages import AIMessage
from pydantic import ValidationError

from rag.schemas import RagResponse


class ResponseParser:
    """
    Convierte la respuesta del proveedor en un RagResponse.
    """

    def parse(self, response) -> RagResponse:
        """
        Convierte la respuesta del LLM en un RagResponse.
        """

        # Ya es el modelo esperado
        if isinstance(response, RagResponse):
            return response

        # Respuesta de LangChain
        if isinstance(response, AIMessage):
            return self._parse_text(response.content)

        # Texto plano
        if isinstance(response, str):
            return self._parse_text(response)

        raise TypeError(
            f"Tipo de respuesta no soportado: {type(response).__name__}"
        )

    # =====================================================
    # Métodos privados
    # =====================================================
    # def _parse_text(self, text: str) -> RagResponse:
    #     try:
    #         print("\n========== RESPUESTA DEL LLM ==========\n")
    #         print(text)
    #         print("\n=======================================\n")

    #         data = json.loads(text)

    #         return RagResponse.model_validate(data)

    #     except json.JSONDecodeError as e:
    #         print("\n========== JSON ERROR ==========\n")
    #         print(e)
    #         raise

    #     except ValidationError as e:
    #         print("\n========== VALIDATION ERROR ==========\n")
    #         print(e)
    #         print("\n======================================\n")
    #         raise


    def _parse_text(self, text: str) -> RagResponse:
        """
        Convierte un texto JSON en RagResponse.
        """
        try:
            text = self._extract_json(text)
            data = json.loads(text)
            return RagResponse.model_validate(data)

        except json.JSONDecodeError as e:

            raise ValueError("La respuesta del modelo no es un JSON válido.") from e

        except ValidationError as e:

            raise ValueError("La respuesta del modelo no cumple el esquema RagResponse.") from e
    
    def _extract_json(self, text: str) -> str:
        """
        Extrae el objeto JSON de la respuesta del modelo.

        Soporta respuestas como:

        ```json
        {...}
        ```

        o texto adicional antes/después del JSON.
        """

        text = text.strip()

        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No se encontró un objeto JSON en la respuesta del modelo.")
        return text[start:end + 1]

