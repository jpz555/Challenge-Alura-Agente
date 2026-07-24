"""
tests/test_graph_routing.py

Prueba de integración del grafo.
"""

from orchestrator.graph import AgentGraph
from agents.base.state import AgentState
from pprint import pprint

graph = AgentGraph()
graph.visualize()  # Visualiza el grafo en Jupyter Notebook
graph.save_graph("agent_graph.png")  # Guarda el grafo como PNG

TEST_CASES = [

    # -----------------------------
    # KNOWLEDGE
    # -----------------------------

    # {
    #     "query": "¿Cuál es el horario operativo de la empresa?",
    #     "intent": "knowledge",
    #     "agent": "Knowledge Agent",
    # },

    # {
    #     "query": "¿Cuál es el lead time corporativo?",
    #     "intent": "knowledge",
    #     "agent": "Knowledge Agent",
    # },

    # -----------------------------
    # ANALYTICS
    # -----------------------------

    # {
    #     "query": "Calcula los indicadores logísticos del último trimestre.",
    #     "intent": "analytics",
    #     "agent": "Analytics Agent",
    # },

    # {
    #     "query": "Analiza el comportamiento del inventario.",
    #     "intent": "analytics",
    #     "agent": "Analytics Agent",
    # },

    # -----------------------------
    # DECISION SUPPORT
    # -----------------------------

    {
        "query": "Optimiza las rutas de distribución.",
        "intent": "decision",
        "agent": "Decision Support Agent",
    },

    {
        "query": "Calcula el punto de reorden del producto A.",
        "intent": "decision",
        "agent": "Decision Support Agent",
    },

    # {
    #     "query": "Programa las entregas para mañana.",
    #     "intent": "decision",
    #     "agent": "Decision Support Agent",
    # }

]
print("\n")
print("=" * 80)
print("PRUEBA DE INTEGRACIÓN DEL GRAFO")
print("=" * 80)

for case in TEST_CASES:

    print("\n" + "-" * 80)
    print("Comenzando....")
    print(f"Pregunta : {case['query']}")

    state = AgentState(
        user_query=case["query"]
    )
    result = graph.invoke(state)

    print(f"Intent esperado   : {case['intent']}")
    print(f"Intent obtenido   : {result.intent}")

    print(f"Agente esperado   : {case['agent']}")
    print(f"Agente obtenido   : {result.current_agent}")
    print(f"Herramienta       : {result.current_tool}")
    ok = (
        result.intent == case["intent"]
        and
        result.current_agent == case["agent"]
    )

    print(
        "Resultado         : "
        + ("OK" if ok else "ERROR")
    )
    
    print("\nRespuesta:")
    print(result.response)

    # pprint(result.tool_result)
    print("\n")
    print("=" * 80)

