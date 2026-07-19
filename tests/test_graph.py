"""
test_graph.py
-------------

Prueba de integración del sistema multiagente.

Flujo probado:

Pregunta
    ↓
LangGraph
    ↓
Supervisor
    ↓
Knowledge Agent
    ↓
RAG Tool
    ↓
RagChain
    ↓
Respuesta
"""

from __future__ import annotations
import logging
import sys
from pathlib import Path

# Agregar el directorio raíz al PATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# Logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

# Proyecto
from agents.base.state import AgentState  # noqa: E402
from orchestrator.graph import AgentGraph  # noqa: E402


def print_separator(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def print_sources(state: AgentState) -> None:
    sources = state.metadata.get("sources", [])
    if not sources:
        print("No se encontraron fuentes.")
        return
    
    for idx, source in enumerate(sources, start=1):

        print(f"\nFuente #{idx}")
        print(f"Código      : {source.document_code}")
        print(f"Título      : {source.document_title}")
        print(f"Sección     : {source.section}")
        print(f"Chunk UUID  : {source.chunk_uuid}")

def main():
    try:
        print_separator("INICIALIZANDO AGENTE")
        graph = AgentGraph()
        logger.info("AgentGraph inicializado correctamente.")
        state = AgentState(user_query="¿Cuál es el horario operativo de la empresa?")
        # result = graph.invoke(state)

        # print("TIPO:", type(result))
        # print("VALOR:", result)

        # return
        
        
        # =====================================================
        # Ejecutar grafo
        # =====================================================

        state = graph.invoke(state)

        # =====================================================
        # Resultado
        # =====================================================

        print_separator("RESULTADO")

        print(f"Intent      : {state.intent}")
        print(f"Agente      : {state.current_agent}")
        print(f"Herramienta : {state.current_tool}")

        print("\nRespuesta:")
        print(state.response)

        print("\nMetadata:")
        print(state.metadata)

        logger.info("Prueba completada correctamente.")

    except Exception:

        print_separator("ERROR")

        logger.exception("La prueba del agente falló.")

        raise

if __name__ == "__main__":
    main()