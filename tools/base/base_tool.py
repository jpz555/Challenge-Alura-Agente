"""
tools/base/base_tool.py

Contrato base para todas las herramientas del sistema.
"""

from abc import ABC, abstractmethod

class BaseTool(ABC):

    def __init__(self, name=None):

        self.name = (
            name
            or getattr(self.__class__, "name", self.__class__.__name__)
        )

    @abstractmethod
    def get_tools(self):
        """
        Retorna la lista de herramientas LangChain.
        """
        pass