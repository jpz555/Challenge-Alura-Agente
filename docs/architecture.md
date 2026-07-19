# Arquitectura del Sistema Multiagente

**Proyecto:** Agente Inteligente para Logística  
**Estado:** Congelado (Baseline v1.0)

---

# 1. Objetivo

Este documento define los contratos arquitectónicos del proyecto.

Una vez aprobados, estos contratos NO deben modificarse durante el desarrollo,
salvo una decisión arquitectónica explícita.

Las implementaciones deberán adaptarse a estos contratos.

---

# 2. Arquitectura General

```
Usuario
    │
    ▼
Supervisor Agent
    │
    ├──────────────┬───────────────────┐
    ▼              ▼                   ▼
Knowledge      Analytics      Decision Support
    │              │                   │
    ▼              ▼                   ▼
RAG         LangChain Tools     LangChain Tools
```

---

# 3. Componentes Base

## 3.1 AgentState

Responsabilidad

Contener el estado compartido del sistema durante toda la ejecución del grafo.

Debe almacenar únicamente información de contexto.

Ejemplos

- messages
- user_query
- intent
- current_agent
- current_tool
- response

No contiene lógica.

---

## 3.2 BaseAgent

Responsabilidad

Representar un agente del sistema.

Todas las clases derivadas deben implementar:

```

invoke(state)

```

Clases derivadas

- SupervisorAgent
- KnowledgeAgent
- AnalyticsAgent
- DecisionSupportAgent

---

## 3.3 BaseTool

Responsabilidad

Representar un proveedor de herramientas de LangChain.

NO representa una herramienta individual.

Su responsabilidad es registrar herramientas mediante get_tools().

Contrato obligatorio

```

get_tools()

```

NO posee invoke().

Clases derivadas

- RoutingTool
- InventoryTool
- SchedulingTool
- AnalyticsTool

---

# 4. Adaptadores

Los adaptadores NO heredan de BaseTool.

Representan componentes internos del sistema.

Actualmente

- RAGTool

Responsabilidad

Conectar el KnowledgeAgent con el pipeline RAG.

No participa en Tool Calling.

No implementa get_tools().

---

# 5. Agentes

## SupervisorAgent

Responsabilidad

Clasificar la intención del usuario.

No ejecuta herramientas.

No consulta documentos.

No realiza optimización.

Salida

- knowledge
- analytics
- decision

---

## KnowledgeAgent

Responsabilidad

Responder preguntas utilizando el sistema RAG.

Utiliza

RAGTool

No utiliza Tool Calling.

---

## AnalyticsAgent

Responsabilidad

Resolver consultas analíticas.

Utiliza

AnalyticsTool

Implementará Tool Calling.

---

## DecisionSupportAgent

Responsabilidad

Resolver problemas de optimización.

Utiliza

- RoutingTool
- InventoryTool
- SchedulingTool

Implementará Tool Calling.

---

# 6. Herramientas

## RoutingTool

Responsabilidad

Proveer herramientas de optimización de rutas.

Expone

- optimize_routes_tool()
- estimate_delivery_time_tool()
- calculate_route_cost_tool()

No ejecuta automáticamente ningún modelo.

La selección del modelo matemático se realiza internamente.

---

## InventoryTool

Responsabilidad

Proveer herramientas de optimización de inventarios.

Expone

- optimize_inventory_tool()
- reorder_point_tool()
- classify_inventory_tool()

---

## SchedulingTool

Responsabilidad

Proveer herramientas de programación.

Expone

- optimize_schedule_tool()
- allocate_resources_tool()
- balance_workload_tool()

---

## AnalyticsTool

Responsabilidad

Proveer herramientas analíticas.

Expone

- analyze_inventory_tool()
- analyze_transport_tool()
- calculate_kpis_tool()
- forecast_demand_tool()

---

# 7. Flujo del Sistema

```
Usuario

↓

Supervisor

↓

Intent

↓

Knowledge
Analytics
Decision Support

↓

Herramientas

↓

Respuesta
```

---

# 8. Principios de Diseño

1. Las clases base no se modifican para corregir errores de implementación.

2. Las implementaciones deben adaptarse a los contratos definidos.

3. Los cambios arquitectónicos requieren revisión explícita.

4. Las herramientas LangChain se registran mediante get_tools().

5. RAGTool es un adaptador, no una herramienta LangChain.

6. El grafo coordina agentes; los agentes coordinan herramientas.

7. Los modelos matemáticos permanecen encapsulados dentro de cada herramienta.

---

# 9. Estado de la Arquitectura

Estado: Congelada

Versión: 1.0

Fecha: Julio 2026

Toda modificación posterior deberá reflejarse primero en este documento antes de implementarse en el código.