"""
agents/knowledge/agent.py

Agente especializado en consultas documentales.

Responsabilidades
-----------------
- Recibir el AgentState.
- Delegar la consulta al RAGTool.
- Retornar el AgentState actualizado.
"""

from agents.base.base_agent import BaseAgent
from agents.base.state import AgentState
from tools.rag.rag_tool import RAGTool


class KnowledgeAgent(BaseAgent):
    """
    Agente encargado de responder consultas documentales.
    """

    def __init__(
        self,
        provider: str | None = None,
        model: str | None = None,
        k: int = 4,
    ):
        super().__init__("Knowledge Agent")

        self.rag_tool = RAGTool(
            provider=provider,
            model=model,
            k=k,
        )

    def invoke(self, state: AgentState) -> AgentState:
        """
        Ejecuta una consulta documental utilizando el RAG.
        """
        print("\n========== KNOWLEDGE ==========")
        # print(f"Pregunta : {state.user_query}")

         # Registrar el agente que está ejecutando
        state.current_agent = "Knowledge Agent"
        state.current_tool = self.rag_tool.name

        return self.rag_tool.invoke(state)