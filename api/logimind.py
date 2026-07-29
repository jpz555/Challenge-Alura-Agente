import time


from orchestrator.graph import AgentGraph
from orchestrator.nodes import GraphNodes
from agents.base.state import AgentState

from api.agent_response import AgentResponse
from api.chat_session import ChatSession
from api.enums import SearchMode

from rag.config  import DEFAULT_PROVIDER, MODELS

class LogiMindAI:
    """
    Entrada principal al sistema
    Acesso único para streamlit
    """
    

    def __init__(self, 
                 provider: str = DEFAULT_PROVIDER, 
                 model: str  | None = None,
                  api_key: str | None = None,
                  search_mode : SearchMode = SearchMode.HYBRID):
        
        self.provider = provider
        self.model = model or  MODELS[self.provider]
        self.api_key = api_key
        self.search_mode = search_mode
        self.session = ChatSession()
        self._build_graph()
        
    def _build_graph(self):
        nodes = GraphNodes(
            provider=self.provider,
            model=self.model,
            # api_key=self.api_key
        )
        self.graph = AgentGraph(nodes)
         
    def ask(self, question: str):
        state = AgentState(messages=self.session.messages, user_query=question)

        start = time.perf_counter()
        result = self.graph.invoke(state)
        self.session.messages = result.messages
        
        elapsed = time.perf_counter() - start
                
        return AgentResponse(
            response = result.response,
            current_agent= result.current_agent,
            current_tool=result.current_tool,
            metadata=result.metadata,
            tool_result=result.tool_result,
            execution_time = elapsed
        )
    def new_chat(self):
        self.session.reset()  
        
    def get_history(self):
        return self.session.messages
    
    def set_provider(self, provider):
        
        if provider != self.provider:
            self.provider = provider
            self.model = MODELS[provider]
            self._build_graph()
        
    def set_model(self, model: str):
        
        if model != self.model:
            self.model = model
            self._build_graph()
            
    def set_api_key(self, api_key: str | None):
        self.api_key = api_key
    
    def set_search_mode(self, mode: SearchMode):
        self.search_mode = mode
        
    def get_system_status(self):
        return {
            "provider": self.provider,
            "model": self.model,
            "search_mode": self.search_mode.value,
            "messages": len(self.session.messages)
        }
