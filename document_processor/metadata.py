"""
=========================================================
Document Processor - Metadata Extractor
=========================================================
Responsabilidad:
    Extraer automáticamente los metadatos del documento.

Versión:
    1.0.0
=========================================================
"""

import re
from typing import Dict


class MetadataExtractor:
    """
    Extrae los metadatos definidos en la plantilla corporativa.
    """

    def __init__(self):
        pass

    # =====================================================
    # API PRINCIPAL
    # =====================================================

    def extract(self, document: Dict) -> Dict:
        """
        Enriquece el documento con sus metadatos.
        """

        text = document["content"]

        metadata = {
            "document_code": self._extract_field(text, "Código"),
            "version": self._extract_field(text, "Versión"),
            "status": self._extract_field(text, "Estado"),
            "responsible_area": self._extract_field(text, "Área Responsable"),
            "parent_document": self._extract_parent_document(text),
            "date": self._extract_field(text, "Fecha"),
            "title": self._extract_title(text),
        }

        document["metadata"] = metadata

        return document

    # =====================================================
    # CAMPOS GENERALES
    # =====================================================

    def _extract_field(self, text: str, field_name: str):

        pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.+)"

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

        return None

    # =====================================================
    # TITULO
    # =====================================================

    def _extract_title(self, text: str):

        match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)

        if match:
            return match.group(1).strip()

        return None

    # =====================================================
    # DOCUMENTO PADRE
    # =====================================================

    def _extract_parent_document(self, text: str):

        parent = self._extract_field(text, "Documento Padre")

        if parent is None:
            parent = self._extract_field(text, "Documento Fuente")

        return parent