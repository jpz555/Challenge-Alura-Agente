from langchain.agents import create_agent

from rag.models import ModelFactory
from tools.routing.routing_functions import optimize_routes_tool
from tools.routing.routing_tool import RoutingTool

tools = RoutingTool().get_tools()

print(tools)

for t in tools:
    print("=" * 60)
    print(type(t))
    print("name:", t.name)
    print("args:", t.args)
    print("description:", t.description)
    
llm = ModelFactory.create(provider="groq")

agent = create_agent(
    model=llm,
    tools=[optimize_routes_tool],   # <-- NO RoutingTool()
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Optimiza las rutas de distribución"
            }
        ]
    }
)

print(result)