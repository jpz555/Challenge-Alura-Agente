"""
tools/rag/tool.py

Herramienta que encapsula el flujo RAG.

Responsabilidades
-----------------
- Invocar el RagChain.
- Actualizar el AgentState.
- No contiene lógica RAG.
"""

from agents.base.state import AgentState
from rag.chain import RagChain



class RAGTool():
    """
    Herramienta para consultas documentales.
    """
    
    name = "Rag Tool"

    def __init__(self,provider: str | None = None, model: str | None = None, k:int = 4):

        self.chain = RagChain(
            provider=provider,
            model=model,
            k=k
        )
        
        print(self.chain.llm)

    def invoke(self, state: AgentState) -> AgentState:
        """
        Ejecuta el flujo RAG.
        """
        print("\n========== RAG TOOL ==========")
        # print(f"Pregunta : {state.user_query}")
        response = self.chain.invoke(state.user_query)
        
        state.response = response.answer
        state.metadata["confidence"] = response.confidence
        state.metadata["reasoning"] = response.reasoning
        state.metadata["sources"] = response.sources
        state.metadata["limitations"] = response.limitations

        return state