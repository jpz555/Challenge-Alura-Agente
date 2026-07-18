"""
=========================================================
RAG - Schemas
=========================================================

Modelos de datos utilizados por el RAG.
=========================================================
"""

from typing import List, Literal
from pydantic import BaseModel, Field


class Source(BaseModel):
    """Fuente utilizada para construir la respuesta."""
    document_code: str = Field(description="Código del documento")
    document_title: str = Field(description="Título del documento")
    section: str = Field(description="Sección utilizada")
    chunk_uuid: str = Field(description="Identificador único del chunk")


class RagResponse(BaseModel):
    """Respuesta estructurada del asistente."""
    answer: str = Field(description="Respuesta al usuario")
    confidence: Literal["Alta","Media", "Baja"] = Field(description="Nivel de confianza")
    reasoning: str = Field(description="Breve explicación de por qué se obtuvo esa respuesta")
    sources: List[Source] = Field(description="Fuentes utilizadas")
    limitations: str | None = Field(default=None,description="Limitaciones de la respuesta")
    
    @classmethod
    def response_format(cls) -> str:
        """
        Devuelve el formato de respuesta que debe seguir el LLM.
        """

        return """
                {
                    "answer": "<respuesta al usuario>",
                    "confidence": "Alta | Media | Baja",
                    "reasoning": "<explicación breve de la respuesta>",
                    "sources": [
                        {
                            "document_code": "<código del documento>",
                            "document_title": "<título del documento>",
                            "section": "<sección utilizada>",
                            "chunk_uuid": "<identificador único del chunk>"
                        }
                    ],
                    "limitations": "<limitaciones de la respuesta>" | null
                }
            """
    
# class PromptContext(BaseModel):
#     question: str
#     prompt: object
#     sources: List[Source]