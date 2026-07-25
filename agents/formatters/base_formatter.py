from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    """
    Clase base para todos los formateadores de resultados.
    """

    @abstractmethod
    def format(self, tool_name: str, tool_result: dict) -> dict:
        """
        Convierte el resultado de una herramienta en un
        resultado técnico estructurado.
        """
        pass
    
    