from rag.models import ModelFactory
from langchain_core.tools import tool


@tool
def optimize_routes_tool(problem: str) -> str:
    """Optimiza rutas."""
    print(">>> TOOL EJECUTADA")
    return f"OK: {problem}"


llm = ModelFactory.create(provider="groq")

llm_tools = llm.bind_tools([optimize_routes_tool])

response = llm_tools.invoke(
    "Optimiza las rutas de distribución."
)

print("=" * 80)
print(type(response))
print(response)
print("=" * 80)

print("Tool Calls:")
print(response.tool_calls)