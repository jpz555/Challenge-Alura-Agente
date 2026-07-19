"""
agents/base/state.py

Estado compartido entre todos los agentes del sistema.
Este modelo representa el estado que viajará a través del grafo de LangGraph.

Versión:
    1.0.0

"""

from typing import Any

from pydantic import BaseModel, Field


class AgentState(BaseModel):
    """
    Estado compartido del flujo multiagente.
    """
    # Conversación
    
    messages: list[Any] = Field(default_factory=list)
    # Consulta original del usuario
    user_query: str = ""
    
    # Intención detectada por el Supervisor
    intent: str | None = None

    # Agente seleccionado
    current_agent: str | None = None

    # Herramienta utilizada
    current_tool: str | None = None

    # Resultado devuelto por la herramienta
    tool_result: Any = None

    # Respuesta final
    response: str | None = None

    # Información adicional
    metadata: dict[str, Any] = Field(default_factory=dict)