"""
Analytics Agent.

Responsabilidades
-----------------
- Recuperar contexto documental mediante RAG.
- Obtener datos operacionales.
- Delegar el análisis a AnalyticsTool.
- Actualizar el AgentState.

v1.0.0
"""

from agents.base.base_agent import BaseAgent
from agents.base.state import AgentState

from rag.models import ModelFactory
from tools.analytics.analytics_tool import AnalyticsTool
from tools.data.corporate_data_loader import CorporateDataLoader
from tools.rag.rag_tool import RAGTool


class AnalyticsAgent(BaseAgent):
    def __init__(self, rag_tool: RAGTool, model: ModelFactory, corporate_data: CorporateDataLoader):
        super().__init__("Analytics Agent")
        print("[AnalyticsAgent] Inicializando LLM...")
        self.llm = model
        self.rag_tool = rag_tool
        self.corporate_data = corporate_data
        self.analytics_tool = AnalyticsTool(model=self.llm)
        
        

    # Invoke
    def invoke(self, state: AgentState) -> AgentState:
        print("\n========== ANALYTICS AGENT ==========")
        # print(f"Pregunta : {state.user_query}")
        state.current_agent = self.name
    
        # Recuperar el contexto documental RAG
        documents = self.rag_tool.retrieve(state.user_query, include_data=True)
        context  =   "\n\n".join(doc.page_content for doc in documents)  
        
        # Datos operacionales (Excel)
        corporate_data = self.corporate_data.load_summary()
        
        # Analytics 
        result = self.analytics_tool.invoke(question=state.user_query, context=context, data=corporate_data)
        
        state.current_tool = self.analytics_tool.name
        state.tool_result = result
        state.response = result["response"]
        
        return state
        
         
        