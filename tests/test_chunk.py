from indexer.vector_store import VectorStore

vector_store = VectorStore()

print("=" * 120)
print("BUSCANDO: CD-01 Barranquilla")
print("=" * 120)

results = vector_store.similarity_search(
    query="CD-01 Barranquilla",
    k=20
)

for i, doc in enumerate(results, start=1):
    print(f"\nResultado {i}")
    print(f"Chunk ID      : {doc.metadata.get('chunk_id')}")
    print(f"Documento     : {doc.metadata.get('document_code')}")
    print(f"Section Path  : {doc.metadata.get('section_path')}")