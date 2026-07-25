"""
Decision Support Agent.

Responsabilidades
-----------------
- Coordinar problemas de optimización (routing, inventory, scheduling).
- Seleccionar la herramienta adecuada utilizando el LLM (vía ManualToolDispatcher).
- Ejecutar la herramienta seleccionada.
- Actualizar el AgentState.

NOTA DE IMPLEMENTACIÓN
----------------------
Inicialmente se evaluó utilizar `langchain.agents.create_agent()`
(y su predecesor deprecado `langgraph.prebuilt.create_react_agent()`)
para realizar Tool Calling automático.

Durante las pruebas de integración con:

    - LangChain 1.3.13
    - langchain-groq 1.1.3
    - Groq 0.37.1
    - llama-3.1-8b-instant

se presentó el error:

    groq.BadRequestError
    tool_use_failed

Este error está documentado también con otros modelos de Groq (Llama4)
y en otros frameworks (Agno, Langflow) — es un problema de la capa de
tool-calling nativo de Groq/langchain-groq, no de este código.

Adicionalmente, bind_tools()/create_agent() dependen del soporte de
tool-calling nativo de cada proveedor, el cual varía en madurez entre
Groq, Gemini y Ollama — lo que rompería la compatibilidad multi-proveedor
que este proyecto requiere.

Por lo anterior, DecisionSupportAgent usa ManualToolDispatcher
(ver tools/base/manual_tool_dispatcher.py) para clasificar la tool
vía texto/JSON, y ejecuta la tool directamente en Python.

Nota de diseño: DecisionSupportAgent HEREDA de BaseAgent (cumple el
contrato que espera el orchestrator/grafo: .invoke(state), .name).
ManualToolDispatcher NO es una superclase — se usa por COMPOSICIÓN,
como un atributo más (self.dispatcher), igual que self.llm.
"""
from agents.base.base_agent import BaseAgent
from agents.base.state import AgentState

from rag.models import ModelFactory

from tools.base.tool_distpatcher import ToolDispatcher

# Las tools viven en sus propias carpetas por dominio
from tools.rag.rag_tool import RAGTool
from tools.routing.routing_tool import optimize_routes_tool, estimate_delivery_time_tool, calculate_route_cost_tool
from tools.inventory.inventory_tool import check_stock_tool, forecast_demand_tool, reorder_point_tool
from tools.scheduling.scheduling_tool import optimize_schedule_tool, assign_resource_tool, check_availability_tool
from indexer.retriever import KnowledgeRetriever


class DecisionSupportAgent(BaseAgent):  # ← sigue heredando de BaseAgent, sin cambios
    def __init__(self, rag_tool: RAGTool, model: ModelFactory):
        super().__init__("Decision Support Agent")

        # Modelo (solo se usa para clasificar, no para tool-calling nativo)
        print("[DecisionSupportAgent] Inicializando LLM...")
        self.llm = model #ModelFactory.create(provider="groq")
    
        # contexto
        self.rag_tool = rag_tool

        # Diccionario plano con las 9 tools de los 3 dominios.
        tools = {
            "optimize_routes": optimize_routes_tool,
            "estimate_delivery_time": estimate_delivery_time_tool,
            "calculate_route_cost": calculate_route_cost_tool,
            "check_stock": check_stock_tool,
            "forecast_demand": forecast_demand_tool,
            "reorder_point": reorder_point_tool,
            "optimize_schedule": optimize_schedule_tool,
            "assign_resource": assign_resource_tool,
            "check_availability": check_availability_tool,
        }

        # Composición: el dispatcher es un atributo del agente, no una superclase
        self.dispatcher = ToolDispatcher(
            llm=self.llm,
            tools=tools,
            system_context=("Eres un clasificador de herramientas para un sistema logístico."),
        )

    # ==========================================================
    # Invoke
    # ==========================================================
    def invoke(self, state: AgentState) -> AgentState:

        print("\n========== DECISION SUPPORT ==========")
        print(f"Pregunta : {state.user_query}")
        state.current_agent = self.name
        # decision = self.dispatcher.classify(state.user_query)

        # Recuperar contexto documental
        documents = self.rag_tool.retrieve(state.user_query)
        context = "\n\n".join(doc.page_content for doc in documents)
        
        # print("\n========== DOCUMENTOS RECUPERADOS ==========")

        # for i, doc in enumerate(documents, start=1):

        #     print(f"\nDocumento {i}")
        #     print("Metadata:", doc.metadata)
        #     print("Contenido:")
        #     print(doc.page_content[:300])
        #     print("-" * 60)       
        # selección herramienta
        decision = self.dispatcher.classify(user_query=state.user_query, context=context)
        
        if decision is None:
            state.response = "No fue posible interpretar la respuesta del modelo."
            return state

        tool_name = decision.get("tool")
        if tool_name not in self.dispatcher.tools:
            print(f"[WARN] Tool inválida devuelta por el LLM: {tool_name!r}")
            state.response = "No existe una herramienta válida para la consulta."
            return state
        
        # ==========================================================
        # Inyectar el contexto recuperado por el RAG
        # ==========================================================
        arguments = decision.setdefault("arguments", {})
        
        arguments["problem"] = state.user_query
        arguments["context"] = context

        state.current_tool = tool_name
        result = self.dispatcher.execute(decision)
        state.tool_result = result
        state.response = self._interpret_result(
            user_query=state.user_query,
            tool_name = state.current_tool,
            tool_result=result,
            context=context,
              
        )
        # print("\n===== RESULTADO =====")
        # print(result)
        return state