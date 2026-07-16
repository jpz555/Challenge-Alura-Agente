"""
=========================================================
Document Processor - Main
=========================================================
Pipeline completo de procesamiento documental.

Versión:
    1.0.0
=========================================================
"""

import time

from document_processor.config import DOCUMENTS_DIR, validate_environment

from document_processor.parser import DocumentParser
from document_processor.metadata import MetadataExtractor
from document_processor.chunker import DocumentChunker
from document_processor.exporter import DocumentExporter


def main():

    print("=" * 70)
    print("DOCUMENT PROCESSOR")
    print("=" * 70)

    start_time = time.time()

    # -----------------------------------------------------
    # Validación del entorno
    # -----------------------------------------------------

    validate_environment()

    # -----------------------------------------------------
    # Inicialización
    # -----------------------------------------------------

    parser = DocumentParser()
    metadata = MetadataExtractor()
    chunker = DocumentChunker()
    exporter = DocumentExporter()

    # -----------------------------------------------------
    # Lectura de documentos
    # -----------------------------------------------------

    documents = parser.read_directory(DOCUMENTS_DIR)

    print(f"\nDocumentos encontrados: {len(documents)}\n")

    total_chunks = 0

    # -----------------------------------------------------
    # Procesamiento
    # -----------------------------------------------------

    for index, document in enumerate(documents, start=1):

        print("-" * 70)
        print(f"[{index}/{len(documents)}] {document['file_name']}")

        # Extraer metadatos
        enriched_document = metadata.extract(document)

        # Generar chunks
        chunks = chunker.split(enriched_document)

        # Exportar documento
        document_path = exporter.export_document(enriched_document)

        # Exportar chunks
        chunks_path = exporter.export_chunks(chunks)

        total_chunks += len(chunks)

        print(f"Documento : {enriched_document['metadata']['document_code']}")
        print(f"Chunks    : {len(chunks)}")
        print(f"JSON Doc  : {document_path.name}")
        print(f"JSON Chunk: {chunks_path.name}")

    # -----------------------------------------------------
    # Resumen
    # -----------------------------------------------------

    elapsed = time.time() - start_time

    print("\n" + "=" * 70)

    print("PROCESAMIENTO FINALIZADO")

    print("=" * 70)

    print(f"Documentos procesados : {len(documents)}")
    print(f"Chunks generados      : {total_chunks}")
    print(f"Tiempo total          : {elapsed:.2f} segundos")

    print("=" * 70)


if __name__ == "__main__":
    main()