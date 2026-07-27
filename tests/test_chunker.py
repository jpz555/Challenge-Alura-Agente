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
# doc = metadata.extract(documents[0])

# Buscar específicamente CORP_001.md
doc = None

for document in documents:
    if document["file_name"] == "CORP_001.md":
        doc = metadata.extract(document)
        break

if doc is None:
    raise ValueError("No se encontró CORP_001.md")

chunks = chunker.split(doc)

print(f"Documento: {doc['metadata']['document_code']}")
print(f"Chunks generados: {len(chunks)}")

for chunk in chunks:
    print("=" * 80)
    print(f"Chunk ID      : {chunk['chunk_id']}")
    print(f"Section Path  : {chunk['section_path']}")
    print(f"H1            : {chunk['headers']['h1']}")
    print(f"H2            : {chunk['headers']['h2']}")
    print(f"H3            : {chunk['headers']['h3']}")
    print()
    print(chunk["text"])

# print("\nPrimer chunk\n")

# print(chunks[0]["metadata"])
# print("-" * 60)
# print(chunks[0]["text"][:500])