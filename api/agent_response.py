from dataclasses import dataclass

@dataclass
class AgentResponse:
    """
    Respuesta estándar del sistema LogiMind AI.
    """
    response: str
    current_agent: str
    current_tool: str | None
    metadata: dict
    tool_result: dict | None
    execution_time: float | None