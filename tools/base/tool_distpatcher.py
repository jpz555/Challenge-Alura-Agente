"""
ToolDispatcher
==============

Despachador de herramientas basado en LLM.

Esta clase reemplaza el uso de `create_agent()` cuando se desea mantener
compatibilidad entre múltiples proveedores de modelos (Groq, Gemini,
Ollama, OpenAI, etc.) sin depender del protocolo de Tool Calling nativo.

Funcionamiento
--------------
1. Solicita al LLM que seleccione una herramienta.
2. El LLM responde únicamente un JSON.
3. Se valida y parsea el JSON.
4. Se ejecuta la herramienta correspondiente.
5. Se retorna el resultado.

Responsabilidades
-----------------
- Construir el prompt de clasificación.
- Obtener la decisión del LLM.
- Validar la respuesta.
- Ejecutar la herramienta seleccionada.

No conoce reglas de negocio ni lógica logística.
"""

import json
import re

from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional


class ToolDispatcher:
    def __init__(self,llm, tools: Dict[str, Callable],system_context: str = ""):
        """
        Parameters
        ----------
        llm
            Modelo de lenguaje compatible con invoke().

        tools
            Diccionario con las herramientas disponibles.

            {
                "optimize_routes": optimize_routes_tool,
                "forecast_demand": forecast_demand_tool,
                ...
            }

        system_context
            Contexto general del dominio.
        """

        self.llm = llm
        self.tools = tools
        self.system_context = system_context

    # ==========================================================
    # Construcción del prompt
    # ==========================================================

    def _build_prompt(self, user_query: str, context: str = "",) -> str:

        return f"""
            {self.system_context}

            ====================================================
            CONTEXTO DOCUMENTAL
            ====================================================

            El siguiente contexto fue recuperado de la Base de
            Conocimiento Corporativa.

            Utilízalo únicamente para comprender el contexto de la
            empresa y seleccionar la herramienta más adecuada.

            {context}

            ====================================================
            CONSULTA DEL USUARIO
            ====================================================

            {user_query}

            ====================================================
            HERRAMIENTAS DISPONIBLES
            ====================================================

            {self._tools_description()}

            ====================================================
            INSTRUCCIONES
            ====================================================

            Tu tarea NO es responder la consulta.

            Tu tarea es seleccionar la herramienta más adecuada.

            Analiza:
            - El contexto documental.
            - La consulta del usuario.
            - La descripción de las herramientas.

            IMPORTANTE:

            - Todas las herramientas reciben UN SOLO argumento llamado "problem".
            - Nunca inventes nombres de argumentos.
            - El valor de "problem" debe ser la consulta original del usuario exactamente como fue recibida.

            Responde únicamente un JSON válido.

            No agregues texto.
            No expliques tu decisión.
            No uses markdown.

            La respuesta debe seguir EXACTAMENTE este formato:

            {{
                "tool": "<nombre_tool>",
                "arguments": {{
                    "problem": "{user_query}"
                }}
            }}
        """

    # ==========================================================
    # Descripción automática de tools
    # ==========================================================

    def _tools_description(self) -> str:
        description = []
        for name, tool in self.tools.items():
            doc = getattr(tool, "description", "")
            if doc:
                first_line = doc.strip().splitlines()[0]
            else:
                first_line = "Sin descripción."
                
            description.append(
                f"- {name}: {first_line}"
            )

        return "\n".join(description)

    # Extraer JSON

    def _extract_json(self, text: str) -> Dict[str, Any]:
        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL,
        )

        if not match:
            raise ValueError(
                "No se encontró un JSON válido."
            )

        return json.loads(match.group())


    # Clasificación
    def classify(self, user_query: str, context: str = "",) -> Optional[Dict[str, Any]]:
        prompt = self._build_prompt(user_query, context=context)
        response = self.llm.invoke(prompt)
              
        try:
            decision = self._extract_json(response.content)
            return decision
                       
        except Exception as e:
            print(f"[ToolDispatcher] Error clasificando: {e}")
            return None


    # Ejecución
    def execute(self,decision: Dict[str, Any],) -> Any:
        tool_name = decision.get("tool")
        arguments = decision.get("arguments", {})
        
        if tool_name not in self.tools:
            print(f"[ToolDispatcher] Tool inválida: {tool_name}")
            return None

        if not isinstance(arguments, dict):
            print("[ToolDispatcher] arguments debe ser un objeto JSON.")
            return None

        tool = self.tools[tool_name]

        print(f"[ToolDispatcher] Ejecutando: {tool_name}")
        
        # print("\n===== ARGUMENTS =====")
        # print(arguments)
        return tool.invoke(arguments)

    #
    # Flujo completo
    
    def run(self, user_query: str,) -> Any:
        decision = self.classify(user_query)
        if decision is None:
            return None

        return self.execute(decision)