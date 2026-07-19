"""
test_chain.py
-------------

Prueba de integración del flujo completo RAG.

Flujo probado:

Pregunta
    ↓
RagChain
    ↓
Retriever
    ↓
PromptBuilder
    ↓
LLM
    ↓
RagResponse
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

# ---------------------------------------------------------
# Agregar el directorio raíz al PATH
# ---------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------
# Proyecto
# ---------------------------------------------------------

from rag.chain import RagChain


def print_separator(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def print_sources(response) -> None:

    if not response.sources:
        print("No se encontraron fuentes.")
        return

    for idx, source in enumerate(response.sources, start=1):

        print(f"\nFuente #{idx}")
        print(f"Código      : {source.document_code}")
        print(f"Título      : {source.document_title}")
        print(f"Sección     : {source.section}")
        print(f"Chunk UUID  : {source.chunk_uuid}")


def main():

    try:

        print_separator("INICIALIZANDO RAG")

        chain = RagChain(provider="grok")

        logger.info("RagChain inicializado correctamente.")

        # -------------------------------------------------

        question = (
            "¿Cuál es el horario operativo de la empresa?"
        )

        print_separator("PREGUNTA")

        print(question)

        # -------------------------------------------------

        response = chain.invoke(question)

        # -------------------------------------------------

        print_separator("RESPUESTA")

        print(response.answer)

        print_separator("CONFIANZA")

        print(response.confidence)

        print_separator("RAZONAMIENTO")

        print(response.reasoning)

        print_separator("FUENTES")

        print_sources(response)

        print_separator("PRUEBA FINALIZADA")

        logger.info("Prueba ejecutada correctamente.")

    except Exception as e:

        logger.exception("La prueba del flujo RAG falló.")

        print_separator("ERROR")

        print(type(e).__name__)

        print(e)


if __name__ == "__main__":
    main()