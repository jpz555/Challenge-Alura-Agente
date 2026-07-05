# CORP-002 - Arquitectura Documental de la Base de Conocimiento

**Código:** CORP-002
**Versión:** 3.0
**Estado:** Vigente
**Área Responsable:** Dirección General
**Documento Padre:** CORP-001 – Documento Maestro de la Empresa
**Fecha:** Julio 2026

---

# 1. Objetivo

Definir la arquitectura documental oficial de la Base de Conocimiento Empresarial de LogiMind Logistics S.A.S.

Este documento establece la estructura, organización, dependencias y lineamientos para la creación, mantenimiento y evolución de toda la documentación corporativa utilizada por los colaboradores y por el Asistente Corporativo Inteligente.

Su propósito es garantizar que toda la información sea consistente, trazable, reutilizable y mantenga una única fuente oficial de conocimiento.

---

# 2. Alcance

La presente arquitectura aplica a toda la documentación corporativa utilizada por:

- Dirección General.
- Dirección de Operaciones.
- Compras.
- Inventarios.
- Transporte.
- Calidad.
- Tecnología.
- Todos los colaboradores de LogiMind Logistics S.A.S.
- Sistema RAG.
- Agentes desarrollados con LangChain y LangGraph.
- Herramientas de optimización logística.
- Interfaces del Asistente Corporativo.

Todo documento nuevo deberá respetar esta arquitectura documental.

---

# 3. Principios de la Arquitectura

La Base de Conocimiento Empresarial se fundamenta en los siguientes principios:

- Existencia de una única fuente oficial de información.
- No duplicación de información entre documentos.
- Coherencia documental.
- Trazabilidad completa.
- Separación clara de responsabilidades.
- Facilidad de mantenimiento.
- Optimización para recuperación mediante RAG.
- Escalabilidad para futuras versiones.

---

# 4. Estructura de la Base de Conocimiento

La Base de Conocimiento Empresarial está compuesta por **diecisiete documentos oficiales**, organizados según el siguiente catálogo.

| Código | Documento | Tipo | Propósito |
|---------|-----------|------|-----------|
| CORP-001 | Documento Maestro de la Empresa | Corporativo | Define la identidad, estructura organizacional y reglas generales de la empresa. |
| CORP-002 | Arquitectura Documental | Corporativo | Define la organización, dependencias y reglas de construcción de la Base de Conocimiento. |
| MAN-001 | Manual Operativo General | Manual | Describe el funcionamiento general de la operación logística. |
| POL-001 | Política de Transporte | Política | Define las reglas corporativas del transporte y distribución. |
| POL-002 | Política de Inventarios | Política | Define las reglas corporativas para la administración de inventarios. |
| POL-003 | Política de Compras | Política | Define las reglas para abastecimiento y gestión de proveedores. |
| POL-004 | Política de Calidad | Política | Define el Sistema de Gestión de Calidad de la operación logística. |
| PRO-001 | Procedimiento de Recepción | Procedimiento | Describe el proceso de recepción de mercancía. |
| PRO-002 | Procedimiento de Almacenamiento | Procedimiento | Describe el almacenamiento y ubicación de mercancía. |
| PRO-003 | Procedimiento de Picking | Procedimiento | Describe la preparación de pedidos. |
| PRO-004 | Procedimiento de Packing | Procedimiento | Describe el empaque y acondicionamiento de pedidos. |
| PRO-005 | Procedimiento de Despacho | Procedimiento | Describe la liberación y despacho de mercancía. |
| PRO-006 | Procedimiento de Planeación de Rutas | Procedimiento | Describe la planificación de rutas de distribución. |
| PRO-007 | Procedimiento de Gestión de Inventarios | Procedimiento | Describe la operación diaria del inventario. |
| KPI-001 | Manual de Indicadores Logísticos | Manual | Define los indicadores oficiales de desempeño logístico. |
| FAQ-001 | Preguntas Frecuentes | Base de Conocimiento | Consolida las consultas frecuentes de los colaboradores utilizando información oficial. |
| PRE-001 | Presentación Corporativa | Presentación | Resume la información institucional de LogiMind Logistics. |

---

# 5. Responsabilidad de Cada Documento

Cada documento posee una responsabilidad específica dentro de la Base de Conocimiento. Ningún documento deberá duplicar la información contenida en otro.

## CORP-001 – Documento Maestro de la Empresa

**Contiene:**

- Identidad corporativa.
- Historia de la empresa.
- Estructura organizacional.
- Infraestructura.
- Procesos corporativos.
- Recursos logísticos.
- Reglas generales del negocio.
- Glosario corporativo.

**No contiene:**

- Procedimientos operativos.
- Políticas específicas.
- Indicadores detallados.

---

## CORP-002 – Arquitectura Documental

**Contiene:**

- Organización de la Base de Conocimiento.
- Catálogo oficial de documentos.
- Relaciones de dependencia.
- Reglas de construcción documental.
- Lineamientos de trazabilidad.

**No contiene:**

- Información operativa.
- Políticas.
- Procedimientos.

---

## MAN-001 – Manual Operativo General

**Contiene:**

- Modelo operativo de la empresa.
- Cadena de valor logística.
- Macroprocesos.
- Relación entre procesos.
- Roles generales.
- Sistemas de información utilizados en la operación.

**No contiene:**

- Políticas corporativas.
- Procedimientos detallados.
- Reglas específicas.

---

## Políticas (POL-001 a POL-004)

**Contienen:**

- Lineamientos corporativos.
- Restricciones.
- Responsabilidades.
- Reglas del negocio.
- Criterios de cumplimiento.

**No contienen:**

- Procedimientos paso a paso.

---

## Procedimientos (PRO-001 a PRO-007)

**Contienen:**

- Objetivo del procedimiento.
- Entradas.
- Actividades.
- Responsables.
- Registros.
- Controles.
- Salidas.

**No contienen:**

- Políticas corporativas.
- Reglas estratégicas.

---

## KPI-001 – Manual de Indicadores Logísticos

**Contiene:**

- Definición de cada indicador.
- Objetivo del indicador.
- Fórmula de cálculo.
- Unidad de medida.
- Frecuencia de medición.
- Meta corporativa.
- Responsable del seguimiento.
- Interpretación de resultados.

**No contiene:**

- Procedimientos operativos.
- Reglas corporativas.

---

## FAQ-001 – Preguntas Frecuentes

**Contiene:**

- Preguntas frecuentes realizadas por los colaboradores.
- Respuestas construidas utilizando únicamente información contenida en la documentación oficial.

**No contiene:**

- Nuevas reglas de negocio.
- Información que no exista previamente en otro documento.

---

## PRE-001 – Presentación Corporativa

**Contiene:**

- Resumen institucional de la empresa.
- Información corporativa para procesos de inducción, capacitación y presentaciones ejecutivas.

**No contiene:**

- Información técnica detallada.
- Procedimientos.
- Políticas.
- Indicadores completos.

---

# 6. Dependencias Documentales

La relación jerárquica entre los documentos oficiales es la siguiente:

```text
CORP-001
│
├── CORP-002
│
├── MAN-001
│   ├── PRO-001
│   ├── PRO-002
│   ├── PRO-003
│   ├── PRO-004
│   └── PRO-005
│
├── POL-001
│   └── PRO-006
│
├── POL-002
│   └── PRO-007
│
├── POL-003
│
├── POL-004
│   └── KPI-001
│
├── FAQ-001
│
└── PRE-001
```

La dependencia documental indica el documento del cual deriva cada documento y la fuente oficial que debe utilizar para su construcción.

---

# 7. Reglas de Consistencia

Toda la documentación corporativa deberá cumplir las siguientes reglas:

1. CORP-001 constituye la única fuente oficial de información corporativa.
2. Ningún documento podrá contradecir la información definida en CORP-001.
3. Cada documento tendrá una única responsabilidad funcional.
4. La información no deberá duplicarse entre documentos.
5. Los manuales describen el funcionamiento general de la organización.
6. Las políticas establecen reglas, lineamientos y restricciones.
7. Los procedimientos describen la ejecución operativa de las actividades.
8. Los indicadores oficiales únicamente podrán definirse en KPI-001.
9. FAQ-001 únicamente podrá reutilizar información existente en la documentación oficial.
10. PRE-001 resumirá la información corporativa sin generar contenido nuevo.
11. Todo documento deberá mantener la terminología definida en el glosario corporativo de CORP-001.
12. Las referencias entre documentos deberán realizarse utilizando exclusivamente los códigos oficiales definidos en esta arquitectura.

---

# 8. Orden Oficial de Construcción

La Base de Conocimiento deberá desarrollarse siguiendo el siguiente orden:

## Fase 1 – Gobierno Corporativo

- CORP-001
- CORP-002

---

## Fase 2 – Operación General

- MAN-001

---

## Fase 3 – Políticas Corporativas

- POL-001
- POL-002
- POL-003
- POL-004

---

## Fase 4 – Procedimientos Operativos

- PRO-001
- PRO-002
- PRO-003
- PRO-004
- PRO-005
- PRO-006
- PRO-007

---

## Fase 5 – Indicadores

- KPI-001

---

## Fase 6 – Base de Conocimiento

- FAQ-001

---

## Fase 7 – Comunicación Corporativa

- PRE-001

---

# 9. Trazabilidad Documental

Todo documento oficial deberá incluir obligatoriamente el siguiente encabezado documental:

- Código del documento.
- Nombre del documento.
- Versión.
- Estado.
- Área responsable.
- Documento padre.
- Fecha de emisión.
- Historial de versiones.

La actualización de cualquier documento deberá mantener la trazabilidad con su documento padre y respetar la arquitectura definida en CORP-002.

---

# 10. Control de Cambios

| Versión | Fecha | Descripción |
|----------|-------|-------------|
| 1.0 | Julio 2026 | Emisión inicial de la arquitectura documental. |
| 2.0 | Julio 2026 | Reestructuración de la Base de Conocimiento y definición de responsabilidades documentales. |
| 3.0 | Julio 2026 | Consolidación definitiva de la arquitectura documental con 17 documentos oficiales, incorporación de PRO-002 y PRO-004, actualización de dependencias y definición del estándar documental corporativo. |