"""
agents/supervisor/router.py

Clasificador de intención del sistema multiagente.
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from rag.models import ModelFactory


class SupervisorRouter:
    """
    Clasifica la intención del usuario.
    """

    def __init__(self, model: ModelFactory):

        self.llm = self.llm = model

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    Eres el Supervisor de un sistema multiagente logístico.
                    Clasifica la consulta únicamente en una de estas categorías:
                    Clasificaciones:
                    
                    knowledge
                    - Preguntas sobre documentos corporativos.
                    - Políticas.
                    - Procedimientos.
                    - Manuales.
                    - Reglamentos.
                    - Horarios.
                    - Información almacenada en la base documental.
                    - Preguntas frecuentes.

                    analytics
                    - Consultas sobre indicadores.
                    - Reportes.
                    - KPIs.
                    - SQL.
                    - Excel.
                    - Estadísticas.
                    - Visualización de datos.
                    - Análisis de información.

                    decision
                    - Solicitudes para optimizar.
                    - Diseñar rutas.
                    - Optimizar inventarios.
                    - Programar vehículos.
                    - Asignar recursos.
                    - Resolver modelos matemáticos.
                    - Tomar decisiones usando optimización.

                    Reglas:

                    - Responde únicamente una palabra.
                    - Nunca expliques tu respuesta.
                    - Nunca escribas puntuación.
                    - Las únicas respuestas válidas son:
                        - knowledge
                        - analytics
                        - decision

                    Devuelve únicamente una palabra.
                    """,
                ),
                ("human", "{question}"),
            ]
        )

        self.chain = (
            self.prompt
            | self.llm
            | StrOutputParser()
        )

    def classify(self, question: str) -> str:
        """
        Clasifica la intención del usuario.

        Parameters
        ----------
        question : str

        Returns
        -------
        str
        """

        intent = self.chain.invoke({"question": question})

        return intent.strip().lower()
    # def classify(self, state: AgentState) -> AgentState:
    #     """
    #     Clasifica la intención del usuario.
    #     """

    #     intent = (
    #         self.chain.invoke(
    #             {"question": state.user_query}
    #         )
    #         .strip()
    #         .lower()
    #     )

    #     state.intent = intent

    #     return state