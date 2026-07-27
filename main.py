"""
main.py

Punto de entrada del sistema multiagente LogiMind AI.

Responsabilidades
-----------------
- Inicializar el sistema.
- Crear una única instancia del grafo.
- Exponer el backend para cualquier interfaz
  (Streamlit, FastAPI, pruebas, CLI, etc.).
"""

from orchestrator.graph import AgentGraph

class LogiMindAI:
    """
    Aplicación principal del sistema multiagente.
    """
    def __init__(self):
        self.graph = AgentGraph()

    def invoke(self, query: str):
        """
        Ejecuta una consulta utilizando el grafo principal.
        """
        from agents.base.state import AgentState

        state = AgentState(
            user_query=query
        )

        return self.graph.invoke(state)

# ------------------------------------------------------------------
# Instancia única de la aplicación
# ------------------------------------------------------------------
app = LogiMindAI()

def get_app() -> LogiMindAI:
    """
    Retorna la aplicación principal.
    """
    return app


def get_graph() -> AgentGraph:
    """
    Retorna el grafo principal.
    """
    return app.graph

# ------------------------------------------------------------------
# Ejecución desde consola (opcional)
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 80)
    print("LogiMind AI - Multi-Agent System")
    print("=" * 80)

    while True:
        query = input("\nConsulta ('salir' para terminar): ")

        if query.lower() in {"salir", "exit", "quit"}:
            break
        result = app.invoke(query)

        print("\nRespuesta:\n")
        print(result.response)