"""
Investigación:
Groq + Tool Calling paso a paso.

Objetivo:
Descubrir si el fallo está en create_agent()
o en la segunda llamada al modelo.
"""

from rag.models import ModelFactory

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage


# ==========================================================
# TOOL
# ==========================================================

@tool
def optimize_routes_tool(problem: str) -> str:
    """
    Optimiza rutas de distribución.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print(problem)

    return f"Ruta optimizada para: {problem}"


# ==========================================================
# MODELO
# ==========================================================

llm = ModelFactory.create(provider="groq")

llm_tools = llm.bind_tools(
    [optimize_routes_tool]
)

# ==========================================================
# PRIMERA LLAMADA
# ==========================================================

print("\n==============================")
print("PRIMERA LLAMADA")
print("==============================")

response = llm_tools.invoke(
    [
        HumanMessage(
            content="Optimiza las rutas de distribución."
        )
    ]
)

print("\nAI RESPONSE")
print(response)

print("\nTOOL CALLS")
print(response.tool_calls)

# ==========================================================
# EJECUTAR TOOL MANUALMENTE
# ==========================================================

tool_call = response.tool_calls[0]

print("\n==============================")
print("EJECUTANDO TOOL")
print("==============================")

tool_result = optimize_routes_tool.invoke(
    tool_call["args"]
)

print(tool_result)

# ==========================================================
# SEGUNDA LLAMADA
# ==========================================================

print("\n==============================")
print("SEGUNDA LLAMADA")
print("==============================")

messages = [

    HumanMessage(
        content="Optimiza las rutas de distribución."
    ),

    response,

    ToolMessage(
        content=tool_result,
        tool_call_id=tool_call["id"],
        name=tool_call["name"],
    ),

]

for m in messages:
    print(type(m).__name__)
    print(m)
    print()

print("\n==============================")
print("RESPUESTA FINAL")
print("==============================")

try:

    final = llm.invoke(messages)

    print(final)

except Exception as e:

    print("\n========== ERROR ==========")
    print(type(e))
    print(e)

    if hasattr(e, "body"):
        print("\nBODY")
        print(e.body)

    if hasattr(e, "response"):
        print("\nRESPONSE")
        print(e.response)

    raise