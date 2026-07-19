from document_processor.config import DOCUMENTS_DIR
from document_processor.parser import DocumentParser
from document_processor.metadata import MetadataExtractor


parser = DocumentParser()

metadata = MetadataExtractor()


documents = parser.read_directory(DOCUMENTS_DIR)

print(f"\nDocumentos encontrados: {len(documents)}\n")


for doc in documents:

    enriched = metadata.extract(doc)

    print("=" * 60)

    print(enriched["metadata"]["title"])

    print(enriched["metadata"])