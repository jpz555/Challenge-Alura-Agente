"""
agents/base/base_agent.py

Clase base para todos los agentes del sistema.
Define el contrato común que deberán implementar los agentes.
"""

from abc import ABC, abstractmethod

from agents.base.state import AgentState
from prompts.responses.responses import (INVENTORY_RESPONSE_PROMPT, ROUTING_RESPONSE_PROMPT, SCHEDULING_RESPONSE_PROMPT)
from agents.formatters.routing_formatter import RoutingFormatter
from agents.formatters.inventory_formatter import InventoryFormatter
from agents.formatters.scheduling_formatter import SchedulingFormatter

class BaseAgent(ABC):
    """
    Clase base para todos los agentes del sistema.
    """

    def __init__(self, name: str):
        self.name = name

        # Formateadores
        self.routing_formatter = RoutingFormatter()
        self.inventory_formatter = InventoryFormatter()
        self.scheduling_formatter = SchedulingFormatter()
    
    def _format_tool_result(self, tool_name: str, tool_result: dict) -> str:
        """
        Convierte el resultado de una herramienta en un
        resumen estructurado para el LLM.
        """
        if tool_name in  ("optimize_routes", "estimate_delivery_time","calculate_route_cost",):
            return self.routing_formatter.format(tool_name, tool_result)
        
        elif tool_name in ("check_stock", "forecast_demand","reorder_point",):
            return self.inventory_formatter.format(tool_name, tool_result)

        elif tool_name in ("optimize_schedule", "assign_resource","check_availability",):
            return self.scheduling_formatter.format(tool_name, tool_result)

        return str(tool_result)
    
    
            
    def _interpret_result(self, user_query: str, tool_name:str, tool_result: dict,context: str) -> str:
        formatted_result = self._format_tool_result(tool_name, tool_result)
        
        if tool_name  in ("optimize_routes", "estimate_delivery_time", "calculate_route_cost"):
            system_prompt = ROUTING_RESPONSE_PROMPT 
            
        elif tool_name in ("check_stock","forecast_demand", "reorder_point"):
            system_prompt = INVENTORY_RESPONSE_PROMPT

        elif tool_name in ("optimize_schedule", "assign_resource", "check_availability"):
            system_prompt = SCHEDULING_RESPONSE_PROMPT
        else:
            system_prompt = ROUTING_RESPONSE_PROMPT
        
        prompt = f"""
        {system_prompt}

        CONSULTA

        {user_query}

        CONTEXTO

        {context}

        RESUMEN TÉCNICO

        {formatted_result}
        """
        
        response = self.llm.invoke(prompt)
        return response.content
        
    
    
    @abstractmethod
    def invoke(self, state: AgentState) -> AgentState:
        """
        Ejecuta la lógica del agente.

        Parameters
        ----------
        state : AgentState
            Estado compartido del flujo.

        Returns
        -------
        AgentState
            Estado actualizado.
        """
        raise NotImplementedError
    
