"""
agents/base/base_agent.py

Clase base para todos los agentes del sistema.
Define el contrato común que deberán implementar los agentes.
"""

from abc import ABC, abstractmethod

from agents.base.state import AgentState


class BaseAgent(ABC):
    """
    Clase base para todos los agentes del sistema.
    """

    def __init__(self, name: str):
        self.name = name

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