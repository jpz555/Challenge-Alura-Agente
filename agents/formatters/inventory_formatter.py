from agents.formatters.base_formatter import BaseFormatter

class InventoryFormatter(BaseFormatter):

    # def format(self, tool_name: str, tool_result: dict) -> dict:

    #     return {
    #         "summary": "La herramienta aún no posee un formateador especializado.",
    #         "status": "",
    #         "indicators": {},
    #         "technical_conclusion": "",
    #         "recommendation": "",
    #     }

    def format(self, tool_name: str, tool_result: dict) -> str:
        return str(tool_result)
        
    # Provisionales
    def _format_inventory_result(self, tool_result: dict) -> str:
        return str(tool_result)