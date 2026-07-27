"""
Analytics Tool.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from tools.base.base_tool import BaseTool


class AnalyticsTool(BaseTool):

    name = "Analytics Tool"

    description = (
        "Herramienta para realizar análisis logístico utilizando "
        "información documental y datos operacionales."
    )
    
    def __init__(self, model):
        self.llm = model

    def invoke(self, question: str, context:str, data:dict) -> dict:
        prompt = ChatPromptTemplate.from_template(
            """
            Eres un analista logístico experto.

            Tu tarea es responder preguntas utilizando DOS fuentes
            de información:

            1. CONTEXTO CORPORATIVO
            (Manuales, políticas, procedimientos y reglas del negocio)

            2. DATOS OPERACIONALES
            (Indicadores, inventario, transporte, demanda, etc.)

            Reglas:

            - Usa SIEMPRE ambas fuentes cuando sea posible.
            - Si los datos contradicen la política corporativa,
            explícalo.
            - Si falta información, indícalo claramente.
            - No inventes datos.
            - Responde de forma profesional.

            ====================================================

            CONTEXTO CORPORATIVO

            {context}

            ====================================================

            DATOS OPERACIONALES

            {data}

            ====================================================

            PREGUNTA

            {question}

            ====================================================

            Genera un análisis ejecutivo.
            """
        )

        chain = prompt | self.llm
        response = chain.invoke(
            {
                "question": question,
                "context": context,
                "data": data,
            }
        )

        return {
            "question": question,
            "response": response.content,
            "data": data,
        }
    
    @tool
    def analyze(self, question: str):
        """
        Realiza análisis logísticos utilizando
        datos corporativos y documentación.
        """
        return []

    def get_tools(self):

        return [
            self.analyze,
        ]

    


    # @tool
    # def analyze_inventory(problem: str):
    #     """Analiza indicadores de inventario."""
    #     pass

    # @tool
    # def analyze_transport(problem: str):
    #     """Analiza indicadores de transporte."""
    #     pass

    # @tool
    # def calculate_kpis(problem: str):
    #     """Calcula KPIs logísticos."""
    #     pass

    # @tool
    # def forecast_demand(problem: str):
    #     """Realiza pronósticos de demanda."""
    #     pass

    # def get_tools(self):

    #     return [
    #         self.analyze_inventory,
    #         self.analyze_transport,
    #         self.calculate_kpis,
    #         self.forecast_demand,
    #     ]