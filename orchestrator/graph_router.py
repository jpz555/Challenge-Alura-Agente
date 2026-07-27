"""
orchestrator/router.py

Router del grafo de LangGraph.

Responsabilidades
-----------------
- Leer el intent generado por el Supervisor.
- Retornar el siguiente nodo del grafo.
"""

from agents.base.state import AgentState


class GraphRouter:
    """
    Router del grafo.
    """
    ROUTES = {
        "knowledge": "knowledge",
        "analytics": "analytics",
        "decision": "decision",
    }

    @classmethod
    def route(cls, state: AgentState) -> str:
        """
        Retorna el siguiente nodo del grafo.

        Parameters
        ----------
        state : AgentState

        Returns
        -------
        str
        """
        
        # print(type(state))
        # print(state)
        
        # Si LangGraph entrega un dict
        if isinstance(state, dict):
            intent = state.get("intent")

        # Si recibimos nuestro modelo
        elif isinstance(state, AgentState):
            intent = state.intent

        else:
            raise TypeError(f"Estado no soportado: {type(state)}")

        return cls.ROUTES.get(intent,"knowledge")