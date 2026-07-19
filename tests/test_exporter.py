from document_processor.config import DOCUMENTS_DIR

from document_processor.parser import DocumentParser
from document_processor.metadata import MetadataExtractor
from document_processor.chunker import DocumentChunker
from document_processor.exporter import DocumentExporter


parser = DocumentParser()
metadata = MetadataExtractor()
chunker = DocumentChunker()
exporter = DocumentExporter()

documents = parser.read_directory(DOCUMENTS_DIR)

print(f"Documentos encontrados: {len(documents)}\n")

# Solo el primero
doc = metadata.extract(documents[0])

chunks = chunker.split(doc)

document_path = exporter.export_document(doc)

chunks_path = exporter.export_chunks(chunks)

print(f"Documento exportado : {document_path}")
print(f"Chunks exportados   : {chunks_path}")