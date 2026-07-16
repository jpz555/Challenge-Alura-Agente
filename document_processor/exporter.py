"""
=========================================================
Document Processor - Exporter
=========================================================
Responsabilidad:
    Exportar documentos y chunks a formato JSON.

Versión:
    1.0.0
=========================================================
"""

import json
from pathlib import Path
from typing import Dict, List

from document_processor.config import (JSON_OUTPUT_DIR,CHUNKS_OUTPUT_DIR,ENCODING,)


class DocumentExporter:

    def __init__(self):
        pass

    # =====================================================
    # DOCUMENTO COMPLETO
    # =====================================================

    def export_document(self, document: Dict) -> Path:
        """
        Guarda el documento enriquecido en formato JSON.
        """

        code = document["metadata"]["document_code"]

        output_file = JSON_OUTPUT_DIR / f"{code}.json"

        with open(
            output_file,
            "w",
            encoding=ENCODING,
        ) as f:

            json.dump(
                document,
                f,
                indent=4,
                ensure_ascii=False,
            )

        return output_file

    # =====================================================
    # CHUNKS
    # =====================================================

    def export_chunks(self, chunks: List[Dict]) -> Path:
        """
        Guarda todos los chunks de un documento.
        """

        if len(chunks) == 0:
            raise ValueError("No existen chunks para exportar.")

        code = chunks[0]["document_code"]

        output_file = CHUNKS_OUTPUT_DIR / f"{code}_chunks.json"

        with open(
            output_file,
            "w",
            encoding=ENCODING,
        ) as f:

            json.dump(
                chunks,
                f,
                indent=4,
                ensure_ascii=False,
            )

        return output_file