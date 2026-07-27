"""
=========================================================
Indexer - Chunk Loader
=========================================================
Responsabilidad:
    Cargar los chunks generados por el Document Processor
    y convertirlos en objetos Document de LangChain.

Versión:
    1.0.0
=========================================================
"""

import json
from pathlib import Path
from typing import List

from langchain_core.documents import Document

from datetime import datetime, timezone


class ChunkLoader:
    """
    Carga todos los archivos *_chunks.json y los convierte
    en objetos Document de LangChain.
    """

    def __init__(self, chunks_directory: Path):

        self.chunks_directory = chunks_directory

    # =====================================================
    # API PRINCIPAL
    # =====================================================

    def load(self) -> List[Document]:

        documents = []

        json_files = sorted(self.chunks_directory.glob("*_chunks.json"))

        for json_file in json_files:

            documents.extend(
                self._load_json(json_file)
            )

        return documents

    # =====================================================
    # CARGAR UN ARCHIVO JSON
    # =====================================================

    def _load_json(self, json_file: Path) -> List[Document]:

        with open(
            json_file,
            "r",
            encoding="utf-8"
        ) as f:

            chunks = json.load(f)

        documents = []

        for chunk in chunks:
            source_path = Path(chunk["source_path"])

            metadata = {

                "chunk_uuid": chunk["chunk_uuid"],
                "chunk_id": chunk["chunk_id"],

                "document_code": chunk["document_code"],
                "document_title": chunk["document_title"],
                "document_version": chunk["document_version"],
                "document_status": chunk["document_status"],
                "document_date": chunk["document_date"],

                "category": chunk["category"],
                "header_h1": chunk["headers"].get("h1"),
                "header_h2": chunk["headers"].get("h2"),
                "header_h3": chunk["headers"].get("h3"),

                "section_path": chunk["section_path"],
                
                "source_file": chunk["source_file"],
                "source_path": str(Path(source_path.parent.name) / source_path.name),

                "text_length": chunk["text_length"],
                
                "indexed_at": datetime.now(timezone.utc).isoformat()

            }

            document = Document(
                page_content=chunk["text"],
                metadata=metadata

            )

            documents.append(document)

        return documents