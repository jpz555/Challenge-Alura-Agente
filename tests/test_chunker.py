from document_processor.config import DOCUMENTS_DIR
from document_processor.parser import DocumentParser
from document_processor.metadata import MetadataExtractor
from document_processor.chunker import DocumentChunker


parser = DocumentParser()
metadata = MetadataExtractor()
chunker = DocumentChunker()


documents = parser.read_directory(DOCUMENTS_DIR)

print(f"\nDocumentos encontrados: {len(documents)}\n")

# Probar únicamente con el primero
doc = metadata.extract(documents[0])

chunks = chunker.split(doc)

print(f"Documento: {doc['metadata']['document_code']}")
print(f"Chunks generados: {len(chunks)}")

for chunk in chunks:
    print("-" * 60)
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Chunk UUID: {chunk['chunk_uuid']}")
    print(f"Document Code: {chunk['document_code']}")
    print(f"Document Title: {chunk['document_title']}")
    print(f"Category: {chunk['category']}")
    print(f"Metadata: {chunk['metadata']}")
    print(f"Text (first 100 chars): {chunk['text'][:100]}")

# print("\nPrimer chunk\n")

# print(chunks[0]["metadata"])
# print("-" * 60)
# print(chunks[0]["text"][:500])