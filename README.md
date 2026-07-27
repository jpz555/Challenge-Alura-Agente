<!-- ====================================================================== -->
<!--                          LOGIMIND AI                                   -->
<!-- ====================================================================== -->

<p align="center">

# 🚚 LogiMind AI

### Sistema Inteligente Multi-Agente para el Soporte a la Toma de Decisiones en Logística y Cadena de Suministro

*"Combinando Inteligencia Artificial, Recuperación Aumentada por Generación (RAG) y Modelos de Optimización para apoyar decisiones empresariales."*

---

🚧 **Versión:** 1.0.0

📅 **Estado del proyecto:** Estable

🧠 **Arquitectura:** Multi-Agent + RAG + Optimización Matemática

</p>

---

> 📌 **Figura 1. Arquitectura General de LogiMind AI**


# 🚀 Introducción

**LogiMind AI** es una plataforma inteligente diseñada para asistir la toma de decisiones en operaciones logísticas mediante la integración de Inteligencia Artificial Generativa, Recuperación Aumentada por Generación (Retrieval-Augmented Generation - RAG), arquitecturas Multi-Agente y modelos de optimización matemática.

A diferencia de un chatbot tradicional, este proyecto fue concebido como un **sistema de soporte a decisiones**, capaz de comprender documentación corporativa, analizar información empresarial y resolver problemas propios de la gestión logística, todo ello bajo una arquitectura modular y escalable.

El sistema permite centralizar el conocimiento organizacional y convertirlo en un activo inteligente capaz de asistir a analistas, planificadores y responsables operativos mediante respuestas fundamentadas y procesos de razonamiento estructurados.

---

# 🌎 El problema

En la mayoría de las organizaciones, el conocimiento operativo se encuentra distribuido en múltiples fuentes de información:

- Manuales operativos
- Procedimientos
- Políticas corporativas
- Indicadores de gestión
- Bases de datos
- Archivos Excel
- Presentaciones
- Preguntas frecuentes
- Documentación técnica

Como consecuencia, responder una simple pregunta puede implicar revisar numerosos documentos o consultar diferentes áreas de la organización.

Al mismo tiempo, los responsables logísticos deben resolver diariamente problemas relacionados con:

- Optimización de rutas.
- Planeación de inventarios.
- Programación de operaciones.
- Cumplimiento de políticas.
- Análisis de indicadores.
- Interpretación de procedimientos.
- Consulta de reglas de negocio.

Estas actividades suelen realizarse utilizando diferentes herramientas, generando tiempos elevados de búsqueda, reprocesos y dificultades para acceder al conocimiento correcto en el momento oportuno.

---

# 💡 La solución

LogiMind AI propone una solución basada en Inteligencia Artificial capaz de unificar estas capacidades dentro de una única plataforma.

El sistema combina diferentes componentes especializados para ofrecer respuestas contextualizadas y apoyar la toma de decisiones operativas.

Entre sus principales capacidades se encuentran:

- Comprensión de documentación corporativa mediante RAG.
- Recuperación semántica de información.
- Consulta inteligente sobre políticas, procedimientos y manuales.
- Soporte a modelos de optimización logística.
- Arquitectura Multi-Agente especializada.
- Integración con diferentes Modelos de Lenguaje (LLMs).
- Procesamiento automático de documentos empresariales.
- Base de conocimiento corporativa centralizada.

De esta manera, el usuario interactúa con un único asistente inteligente mientras el sistema coordina internamente múltiples agentes especializados para resolver cada consulta.

---

# 🎯 Objetivo del proyecto

Desarrollar una plataforma inteligente de soporte a decisiones que integre Recuperación Aumentada por Generación (RAG), arquitecturas Multi-Agente y modelos de optimización matemática para facilitar la consulta de conocimiento corporativo y apoyar la resolución de problemas logísticos de manera modular, escalable y explicable.

---

# 🎯 Objetivos específicos

- Diseñar una arquitectura Multi-Agente utilizando LangGraph.

- Construir una base de conocimiento empresarial basada en documentación corporativa.

- Implementar un pipeline completo de Recuperación Aumentada por Generación (RAG).

- Automatizar el procesamiento y segmentación de documentos.

- Integrar motores de optimización para apoyar decisiones logísticas.

- Diseñar una arquitectura desacoplada que facilite futuras ampliaciones.

- Implementar una solución reutilizable para proyectos empresariales de Inteligencia Artificial.

---

# ✨ Características principales

## 🤖 Arquitectura Multi-Agente

El sistema está conformado por agentes especializados que colaboran entre sí para resolver diferentes tipos de consultas.

Actualmente la arquitectura incorpora:

- Supervisor Agent
- Knowledge Agent
- Decision Support Agent
- Analytics Agent

Cada agente posee responsabilidades claramente definidas, permitiendo mantener una arquitectura modular y fácilmente escalable.

---

# 🏗️ Arquitectura General

LogiMind AI implementa una arquitectura basada en **LangGraph**, donde un agente supervisor coordina la ejecución de agentes especializados según la intención de la consulta.

En el archivo 'tree.txt' pueden observar la estructura del proyecto

---

# 🔄 Flujo General de Ejecución

Cada consulta sigue un flujo de procesamiento claramente definido, desde la recepción de la solicitud hasta la generación de la respuesta final.

```
Usuario
    │
    ▼
Supervisor Agent
    │
    ▼
LangGraph Router
    │
 ┌──┼──────────┐
 ▼  ▼          ▼
Knowledge   Analytics   Decision Support
 Agent        Agent          Agent
      │
      ▼
Herramientas Especializadas
      │
      ▼
LLM + Base Vectorial + Modelos Matemáticos
      │
      ▼
Respuesta Final
```

> 📌 **Figura 2. Flujo General del Sistema**
>

---

# 🧠 Grafo de LangGraph

El comportamiento del sistema está gobernado por un grafo de estados construido con LangGraph.

Cada nodo representa un agente o una etapa del flujo de procesamiento, mientras que las transiciones determinan el siguiente paso de acuerdo con el estado de la conversación.

 📌 **Figura 3. Grafo de LangGraph**
    <p align="center">
    <img src="assets/agent_graph.png" width="900">
    </p>


---

# 📚 Pipeline RAG

Las consultas documentales siguen un pipeline de Recuperación Aumentada por Generación (RAG) diseñado para proporcionar respuestas fundamentadas.

```
Pregunta
    │
    ▼
Retriever
    │
    ▼
Reranker
    │
    ▼
Construcción del Contexto
    │
    ▼
Prompt
    │
    ▼
LLM
    │
    ▼
Respuesta
```

> 📌 **Figura 4. Pipeline RAG**
>
> *(Placeholder: insertar diagrama del flujo RAG.)*

---

# 📄 Pipeline de Procesamiento Documental

Antes de responder preguntas, los documentos son procesados automáticamente para construir la base de conocimiento.

```
Documentos
     │
     ▼
Parser
     │
     ▼
Metadatos
     │
     ▼
Chunker
     │
     ▼
Embeddings
     │
     ▼
ChromaDB
```

> 📌 **Figura 5. Pipeline de Indexación**
>
> *(Placeholder: insertar diagrama del proceso de indexación.)*

---

# 🚚 Flujo del Decision Support Agent

Cuando una consulta requiere optimización, el sistema activa el agente de soporte a decisiones.

```
Pregunta
    │
    ▼
Decision Support Agent
    │
 ┌──┼───────────────┐
 ▼  ▼               ▼
Routing    Inventory    Scheduling
 Tool         Tool          Tool
      │
      ▼
Modelo Matemático
      │
      ▼
Resultado
```

> 📌 **Figura 6. Flujo del Decision Support Agent**
>
> *(Placeholder: insertar diagrama del flujo de optimización.)*

---

# 📊 Flujo del Analytics Agent

Las consultas sobre datos estructurados son atendidas por el agente analítico.

```
Pregunta
    │
    ▼
Analytics Agent
    │
    ▼
Carga del DataFrame
    │
    ▼
Análisis
    │
 ┌──┼────────────┐
 ▼  ▼            ▼
KPIs Estadísticas Gráficos
      │
      ▼
Respuesta
```

# 📚 Flujo de Consulta Documental (RAG)

Las consultas relacionadas con políticas, procedimientos y documentación corporativa siguen un flujo de Recuperación Aumentada por Generación (RAG), permitiendo responder con base en la información contenida en la base de conocimiento.

```text
Usuario
    │
    ▼
Supervisor Agent
    │
    ▼
Knowledge Agent
    │
    ▼
Retriever
    │
    ▼
ChromaDB
    │
    ▼
Reranker
    │
    ▼
Construcción del Prompt
    │
    ▼
LLM
    │
    ▼
Respuesta
```

---

# 🖼️ Capturas de la Aplicación

La interfaz gráfica será desarrollada en Streamlit y contará con diferentes módulos especializados.

| Pantalla | Estado |
|----------|--------|
| 🏠 Inicio | 🚧 Placeholder |
| 💬 Chat Inteligente | 🚧 Placeholder |
| 📚 Asistente Documental | 🚧 Placeholder |
| 📊 Analytics | 🚧 Placeholder |
| 🚚 Routing | 🚧 Placeholder |
| 📦 Inventory | 🚧 Placeholder |
| 📅 Scheduling | 🚧 Placeholder |
| ⚙️ Configuración | 🚧 Placeholder |
| 📈 Dashboard | 🚧 Placeholder |


## 📚 Base de conocimiento corporativa

El proyecto incorpora una base documental empresarial compuesta por:

- Documentos corporativos.
- Políticas.
- Procedimientos.
- Manuales.
- Indicadores (KPIs).
- Preguntas frecuentes.
- Presentaciones.
- Datos corporativos.

Toda esta información es procesada automáticamente para transformarse en conocimiento accesible mediante búsqueda semántica.

---

## 🔎 Recuperación Aumentada por Generación (RAG)

El sistema no responde únicamente utilizando el conocimiento interno del modelo de lenguaje.

Antes de generar una respuesta:

- Recupera documentos relevantes.
- Analiza el contexto.
- Reordena los resultados mediante un Reranker.
- Construye un contexto optimizado.
- Genera respuestas fundamentadas.

Este enfoque reduce considerablemente las alucinaciones y mejora la confiabilidad de las respuestas.

---

## 🚚 Soporte a decisiones logísticas

Además de responder preguntas documentales, LogiMind AI incorpora herramientas orientadas al apoyo de decisiones operativas.

Actualmente incluye módulos para:

- Optimización de rutas.
- Gestión de inventarios.
- Programación de operaciones.
- Consultas analíticas.

La arquitectura fue diseñada para incorporar nuevos modelos de optimización sin modificar el núcleo del sistema.

---

## 🧩 Diseño modular

Todos los componentes fueron desarrollados siguiendo principios de ingeniería de software orientados a la reutilización y el desacoplamiento.

Cada módulo posee una responsabilidad específica dentro de la arquitectura, facilitando:

- Mantenimiento.
- Escalabilidad.
- Reutilización.
- Pruebas.
- Evolución del sistema.

---

# ⭐ ¿Qué hace diferente a LogiMind AI?

Existen numerosos proyectos que implementan asistentes conversacionales utilizando modelos de lenguaje.

Sin embargo, este proyecto busca ir un paso más allá.

LogiMind AI no fue concebido como un chatbot, sino como una plataforma inteligente capaz de combinar múltiples paradigmas de Inteligencia Artificial dentro de una única arquitectura.

Entre ellos:

- Sistemas Multi-Agente.
- Recuperación Aumentada por Generación (RAG).
- Bases de conocimiento corporativas.
- Recuperación semántica.
- Modelos matemáticos de optimización.
- Motores de reglas.
- Modelos de Lenguaje (LLMs).
- Bases vectoriales.
- Ingeniería de Software modular.

El resultado es un sistema capaz de responder preguntas, recuperar conocimiento organizacional y asistir procesos de toma de decisiones en logística y cadena de suministro.

---

# 📌 Estado actual del proyecto

Actualmente la primera versión estable incorpora:

- ✅ Arquitectura Multi-Agente.
- ✅ Pipeline completo de procesamiento documental.
- ✅ Base de conocimiento corporativa.
- ✅ Recuperación semántica mediante ChromaDB.
- ✅ Integración con múltiples modelos de lenguaje.
- ✅ Agente documental.
- ✅ Agente de soporte a decisiones.
- ✅ Agente analítico.
- ✅ Herramientas de optimización.
- ✅ Motor de recuperación RAG.
- ✅ Base vectorial persistente.
- ✅ Suite de pruebas.

Las próximas versiones incorporarán una interfaz gráfica basada en Streamlit, nuevas herramientas analíticas y capacidades avanzadas de visualización.

---

> **"La Inteligencia Artificial no debe reemplazar al responsable de la decisión. Debe proporcionarle mejor información, mejor contexto y mejores herramientas para decidir."**

---

# 🤖 Agentes Inteligentes

La arquitectura de LogiMind AI está basada en un enfoque **Multi-Agente**, donde cada agente posee una responsabilidad específica dentro del sistema. Esta separación permite mantener una arquitectura modular, escalable y fácil de extender.

## 🎯 Supervisor Agent

Es el punto de entrada del sistema.

Su responsabilidad principal es comprender la intención del usuario y decidir cuál de los agentes especializados debe atender la solicitud.

### Responsabilidades

- Analizar la intención de la consulta.
- Clasificar el tipo de problema.
- Coordinar el flujo de ejecución.
- Enrutar solicitudes mediante LangGraph.
- Consolidar la respuesta final.

---

## 📚 Knowledge Agent

Especializado en consultas sobre la documentación corporativa.

Utiliza un pipeline RAG para recuperar información relevante antes de generar una respuesta.

### Responsabilidades

- Recuperar documentos relacionados.
- Construir el contexto de la consulta.
- Consultar la base vectorial.
- Utilizar el Reranker para mejorar la recuperación.
- Generar respuestas fundamentadas.

---

## 📊 Analytics Agent

Especializado en el análisis de datos estructurados.

Permite responder preguntas sobre archivos tabulares y generar indicadores, estadísticas y visualizaciones.

### Responsabilidades

- Analizar archivos Excel y CSV.
- Calcular indicadores.
- Generar gráficos.
- Resumir resultados.
- Interpretar información cuantitativa.

---

## 🚚 Decision Support Agent

Especializado en problemas de optimización logística.

Este agente coordina diferentes herramientas matemáticas para asistir la toma de decisiones.

Actualmente integra módulos para:

- Optimización de rutas.
- Optimización de inventarios.
- Programación de operaciones.

Su arquitectura permite incorporar fácilmente nuevos modelos de optimización en futuras versiones.

---

# 🛠️ Herramientas disponibles

Cada agente utiliza herramientas especializadas para resolver tareas concretas.

| Herramienta | Descripción |
|-------------|-------------|
| 📚 RAG Tool | Recuperación semántica de documentos corporativos. |
| 🚚 Routing Tool | Optimización de rutas de distribución mediante modelos matemáticos. |
| 📦 Inventory Tool | Soporte para políticas y optimización de inventarios. |
| 📅 Scheduling Tool | Asignación y programación de recursos. |
| 📊 Analytics Tool | Análisis estadístico y generación de visualizaciones. |

Las herramientas son independientes del agente que las utiliza, permitiendo su reutilización dentro de la arquitectura.

---

# 💬 Ejemplos de consultas

LogiMind AI es capaz de responder preguntas provenientes de diferentes dominios.

### 📄 Documentación corporativa

- ¿Cuál es la política de inventarios?
- ¿Qué procedimiento debo seguir para recibir mercancía?
- ¿Cuál es el tiempo estándar de entrega?
- ¿Qué KPIs utiliza la empresa?
- ¿Qué restricciones existen para el transporte refrigerado?

---

### 📊 Análisis de datos

- ¿Cuál fue el producto con mayor demanda?
- Muéstrame las ventas por ciudad.
- ¿Cuál fue el nivel promedio de inventario?
- Genera un gráfico de ocupación del almacén.
- Resume el archivo Excel.

---

### 🚚 Optimización logística

- Optimiza las rutas para los vehículos disponibles.
- ¿Cuál es la mejor asignación de pedidos?
- Calcula la cantidad óptima de inventario.
- Genera un cronograma de asignación.
- ¿Cuál es la ruta con menor costo?

---

# ❓ Preguntas frecuentes

## ¿Qué tipo de documentos puedo utilizar?

Actualmente el sistema permite trabajar con documentos corporativos como:

- PDF
- Word
- PowerPoint
- Excel
- Archivos de texto

---

## ¿Qué modelos de lenguaje son compatibles?

Actualmente el proyecto soporta:

- Google Gemini
- Groq
- Ollama

La arquitectura fue diseñada para incorporar nuevos proveedores con un impacto mínimo sobre el resto del sistema.

---

## ¿Es posible utilizar modelos locales?

Sí.

El sistema permite utilizar modelos ejecutados mediante Ollama, facilitando el desarrollo sin depender exclusivamente de servicios en la nube.

---

## ¿Cómo se evita que el modelo genere respuestas incorrectas?

Las respuestas se generan utilizando un pipeline RAG, donde primero se recupera información relevante desde la base de conocimiento antes de consultar el modelo de lenguaje.

Este enfoque mejora significativamente la precisión y reduce las alucinaciones.

---

## ¿Puedo agregar nuevos agentes?

Sí.

La arquitectura fue diseñada para facilitar la incorporación de nuevos agentes especializados sin modificar el resto del sistema.

---

## ¿Puedo agregar nuevas herramientas?

Sí.

Cada herramienta implementa una interfaz desacoplada, lo que permite integrarla dentro del flujo de LangGraph con cambios mínimos.

---

# 🚀 Próximas mejoras

El proyecto continuará evolucionando con nuevas capacidades orientadas a Inteligencia Artificial aplicada a logística.

Entre las funcionalidades planificadas se encuentran:

## 🖥️ Interfaz de usuario

- Aplicación completa en Streamlit.
- Historial de conversaciones.
- Gestión de sesiones.
- Configuración dinámica del modelo.
- Panel administrativo.

---

## 📊 Analítica

- Dashboard interactivo.
- KPIs en tiempo real.
- Gráficos dinámicos.
- Exportación de reportes.
- Comparación de indicadores.

---

## 🤖 Inteligencia Artificial

- Memoria conversacional.
- Agentes colaborativos.
- Autoevaluación de respuestas.
- Selección automática del mejor modelo.
- Mejoras en el pipeline RAG.
- Recuperación híbrida (BM25 + búsqueda semántica).
- Caché semántica para consultas repetidas.

---

## 🚚 Optimización

- Vehicle Routing Problem (VRP).
- Capacitated VRP (CVRP).
- Vehicle Routing with Time Windows (VRPTW).
- Multi Depot VRP (MDVRP).
- Heterogeneous Fleet VRP (HVRP).
- Dynamic Vehicle Routing (DVRP).
- Facility Location Problem (FLP).
- Network Design.
- Demand Forecasting.
- Simulación de inventarios.
- Optimización multiobjetivo.

---

## ☁️ Infraestructura

- Docker.
- FastAPI.
- Autenticación de usuarios.
- API REST.
- Despliegue en la nube.
- CI/CD con GitHub Actions.
- Monitoreo y observabilidad.
- Registro centralizado de logs.

---

# 🌟 Visión del proyecto

LogiMind AI nace con el propósito de demostrar cómo las técnicas modernas de Inteligencia Artificial pueden integrarse con modelos de Investigación de Operaciones para construir sistemas capaces de comprender el conocimiento organizacional y asistir la toma de decisiones logísticas.

Más que un asistente conversacional, el objetivo es evolucionar hacia una plataforma inteligente que combine recuperación de conocimiento, análisis de datos y optimización matemática dentro de una arquitectura modular, extensible y preparada para entornos empresariales.


<p align="center">Copyright © 2026 - Desarrollado por Juan Pablo Palacio Zapata - para AluraLatam </p>