"""
=========================================================
Document Processor - Chunker
=========================================================
Responsabilidad:
    Dividir un documento en chunks utilizando LangChain.

Versión:
    1.1.0
=========================================================
"""

import uuid
from typing import Dict, List

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from document_processor.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class DocumentChunker:
    """
    Convierte un documento en una colección de chunks
    preservando la estructura jerárquica del Markdown.
    """

    def __init__(self):

        # -------------------------------------------------
        # Divide primero por encabezados Markdown
        # -------------------------------------------------

        self.header_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "h1"),
                ("##", "h2"),
                ("###", "h3"),
            ],
            strip_headers=False,
        )

        # -------------------------------------------------
        # Si una sección sigue siendo grande,
        # la divide recursivamente.
        # -------------------------------------------------

        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )

    # =====================================================
    # API PRINCIPAL
    # =====================================================

    def split(self, document: Dict) -> List[Dict]:
        """
        Convierte un documento enriquecido en una lista de chunks.

        Parameters
        ----------
        document : Dict

        Returns
        -------
        List[Dict]
        """

        markdown = document["content"]

        sections = self.header_splitter.split_text(markdown)

        chunks = []

        chunk_id = 1

        for section in sections:

            pieces = self.recursive_splitter.split_text(
                section.page_content
            )

            for piece in pieces:

                metadata = section.metadata

                section_path = " > ".join(
                    value for value in metadata.values()
                )

                chunk = {

                    # =====================================
                    # Identificación
                    # =====================================

                    "chunk_uuid": str(uuid.uuid4()),
                    "chunk_id": chunk_id,

                    # =====================================
                    # Documento origen
                    # =====================================

                    "document_code": document["metadata"]["document_code"],
                    "document_title": document["metadata"]["title"],
                    "document_version": document["metadata"]["version"],
                    "document_status": document["metadata"]["status"],
                    "document_date": document["metadata"]["date"],

                    # =====================================
                    # Archivo origen
                    # =====================================

                    "source_file": document["file_name"],
                    "source_path": document["file_path"],

                    # =====================================
                    # Organización documental
                    # =====================================

                    "category": document["category"],

                    # =====================================
                    # Ubicación dentro del documento
                    # =====================================

                    "metadata": metadata,
                    "headers": {
                        "h1": metadata.get("h1"),
                        "h2": metadata.get("h2"),
                        "h3": metadata.get("h3"),
                        },
                    "section_path": section_path,

                    # =====================================
                    # Contenido
                    # =====================================

                    "text": piece,
                    "text_length": len(piece),
                }

                chunks.append(chunk)

                chunk_id += 1

        return chunks