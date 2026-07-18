"""
=========================================================
RAG - Prompt Builder
=========================================================

Responsabilidad:
    Construir el ChatPromptTemplate que será enviado
    al modelo de lenguaje.

Versión:
    2.0.0
=========================================================
"""

from typing import List
from rag.schemas import RagResponse
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,HumanMessagePromptTemplate
from rag.schemas import Source


class PromptBuilder:
    """
    Construye el prompt corporativo del RAG.
    """

    def __init__(self):
        self.system_template = """
                    Eres el asistente oficial de LogiMind Logistics S.A.S.

                    Tu única fuente de información es la documentación corporativa proporcionada.

                    =========================
                    REGLAS
                    =========================

                    1. Responde únicamente utilizando la documentación suministrada.

                    2. Nunca inventes información.

                    3. No utilices conocimiento externo.

                    4. Si la respuesta no aparece en la documentación,
                    indícalo claramente.

                    5. Si existen varias fuentes,
                    utiliza la siguiente prioridad documental:

                    CORP
                    MAN
                    POL
                    PRO
                    KPI
                    FAQ

                    6. Si existe conflicto entre documentos,
                    prevalece el de mayor jerarquía.

                    7. Siempre responde en español.

                    8. Siempre cita:

                    - Código del documento
                    - Nombre del documento
                    - Sección utilizada

                    9. Sé claro, profesional y preciso.
                    
                    =========================
                    FORMATO DE RESPUESTA
                    =========================
                    
                   El objeto JSON debe contener exactamente las siguientes propiedades:

                    - answer (string)
                    - confidence (Alta | Media | Baja)
                    - reasoning (string)
                    - sources (lista de objetos)
                    - limitations (string o null)
                    La propiedad "sources" debe ser una lista de objetos.

                    Cada objeto de la lista debe contener exactamente las siguientes propiedades:

                    - document_code
                    - document_title
                    - section
                    - chunk_uuid

                    No traduzcas los nombres de estas propiedades.

                    No cambies el nombre de las propiedades.

                    No utilices nombres como:

                    - código
                    - documento
                    - título
                    - sección

                    Utiliza únicamente:

                    - document_code
                    - document_title
                    - section
                    - chunk_uuid

                    Si utilizas una fuente documental, debes incluirla dentro de "sources".

                    Si no utilizaste ninguna fuente documental, devuelve:

                    "sources": []

                    No agregues propiedades adicionales.

                    No omitas ninguna propiedad.

                    La salida debe ser exclusivamente el objeto JSON válido.
                 
        """

    # =====================================================
    # Construir contexto documental
    # =====================================================

    def _build_context(self,documents: List[Document],) -> str:

        context = ""

        for i, doc in enumerate(documents, start=1):

            metadata = doc.metadata

            context += (
                f"\n{'=' * 70}\n"
                f"FUENTE {i}\n"
                f"{'=' * 70}\n"
                f"Código: {metadata['document_code']}\n"
                f"Título: {metadata['document_title']}\n"
                f"Versión: {metadata['document_version']}\n"
                f"Estado: {metadata['document_status']}\n"
                f"Categoría: {metadata['category']}\n"
                f"Sección: {metadata['section_path']}\n\n"
                f"Chunk UUID: {metadata['chunk_uuid']}\n\n"
                f"Contenido:\n"
                f"{doc.page_content.strip()}\n"
            )

        return context

    # =====================================================
    # Construir Prompt
    # =====================================================

    def build(self,question: str, documents: List[Document]):

        context = self._build_context(documents)

        prompt = ChatPromptTemplate.from_messages(

            [

                SystemMessagePromptTemplate.from_template(
                    self.system_template
                ),

                HumanMessagePromptTemplate.from_template(
                    """
                    =========================
                    DOCUMENTACIÓN
                    =========================

                    {context}

                    =========================
                    PREGUNTA
                    =========================

                    {question}
                    """
                )

            ]

        )
        
        prompt_value = prompt.invoke(

            {

                "context": context,

                "question": question,

            }

        )
        
        return prompt_value

        # sources = self._build_sources(documents)

        # return PromptContext(

        #     question=question,

        #     prompt=prompt_value,

        #     sources=sources

        # )
        
    # =====================================================
    # Construir fuentes utilizadas
    # =====================================================

    def _build_sources(self,documents: List[Document],) -> List[Source]:
        sources = []

        for doc in documents:

            metadata = doc.metadata

            source = Source(

                document_code=metadata["document_code"],

                document_title=metadata["document_title"],

                section=metadata["section_path"],

                chunk_uuid=metadata["chunk_uuid"]

            )

            sources.append(source)

        return sources