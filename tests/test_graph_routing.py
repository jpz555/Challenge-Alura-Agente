"""
tests/test_graph_routing.py

Prueba de integración del grafo.
"""
from orchestrator.graph import AgentGraph
from agents.base.state import AgentState
from pprint import pprint
import json
from pathlib import Path
from pprint import pformat


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
    
    #     {
    #     "query": "¿Dónde está ubicado el CD-01?",
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

    {
        "query": "Calcula los indicadores logísticos del último trimestre.",
        "intent": "analytics",
        "agent": "Analytics Agent",
    },

    {
        "query": "Analiza el comportamiento del inventario.",
        "intent": "analytics",
        "agent": "Analytics Agent",
    },

    # -----------------------------
    # DECISION SUPPORT
    # -----------------------------

    # {
    #     "query": "Optimiza las rutas de distribución.",
    #     "intent": "decision",
    #     "agent": "Decision Support Agent",
    # },

    # {
    #     "query": "Calcula el punto de reorden del producto A.",
    #     "intent": "decision",
    #     "agent": "Decision Support Agent",
    # },

    # {
    #     "query": "Programa las entregas para mañana.",
    #     "intent": "decision",
    #     "agent": "Decision Support Agent",
    # }
]

# crear carpeta
results_path = Path("results")
results_path.mkdir(parents=True, exist_ok=True)

txt_report = []
json_report = []

txt_report.append("=" * 100)
txt_report.append("PRUEBA DE INTEGRACIÓN DEL GRAFO")
txt_report.append("=" * 100)
txt_report.append("")

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
    
    
# Segunda parte
    # Reporte TXT
    txt_report.append("-" * 100)
    txt_report.append(f"Pregunta            : {case['query']}")
    txt_report.append(f"Intent esperado     : {case['intent']}")
    txt_report.append(f"Intent obtenido     : {result.intent}")
    txt_report.append(f"Agente esperado     : {case['agent']}")
    txt_report.append(f"Agente obtenido     : {result.current_agent}")
    txt_report.append(f"Herramienta         : {result.current_tool}")
    txt_report.append(f"Resultado           : {'OK' if ok else 'ERROR'}")
    txt_report.append("")
    txt_report.append("Respuesta:")
    txt_report.append(str(result.response))
    txt_report.append("")
    txt_report.append("Tool Result:")
    txt_report.append(pformat(result.tool_result))
    txt_report.append("")
    txt_report.append("=" * 100)
    txt_report.append("")
    
    # Reporte JSON
    json_report.append(
        {
            "query": case["query"],
            "expected_intent": case["intent"],
            "obtained_intent": result.intent,
            "expected_agent": case["agent"],
            "obtained_agent": result.current_agent,
            "tool": result.current_tool,
            "status": "OK" if ok else "ERROR",
            "response": result.response,
            "tool_result": result.tool_result
        }
    )
# Guardar archivo texto

with open(results_path / "response.txt","w",encoding="utf-8") as f:
    f.write("\n".join(txt_report))
    
# Guardar JSON

with open(results_path / "response.json","w", encoding="utf-8") as f:
    json.dump(json_report,f,indent=4,ensure_ascii=False)

print("\n")
print("=" * 80)
print("Resultados guardados correctamente")
print(f"TXT  : {results_path / 'response.txt'}")
print(f"JSON : {results_path / 'response.json'}")
print("=" * 80)

