from document_processor.config import VECTOR_DB_DIR
from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore

embedding_model = EmbeddingModel()

vector_store = VectorStore(
    persist_directory=VECTOR_DB_DIR,
    embedding_function=embedding_model.langchain_model,
)

vector_store.load()

# queries = [
#     "CD-01 Barranquilla",
#     "¿Dónde está ubicado el CD-01?",
#     "Horario operativo",
#     "¿Cuál es el horario operativo de la empresa?",
#     "Lead Time",
#     "Barranquilla",
# ]

queries = [
    "CD-01",
    "CD01",
    "Centro de distribución CD-01",
    "Centro principal",
    "CD-01 Barranquilla",
]

for query in queries:

    print("\n" + "=" * 100)
    print(f"CONSULTA: {query}")
    print("=" * 100)

    docs = vector_store.similarity_search(
        query=query,
        k=10,
    )

    for i, doc in enumerate(docs, 1):

        print(f"\n{i}. Score")
        print(f"Chunk      : {doc.metadata['chunk_id']}")
        print(f"Documento  : {doc.metadata['document_code']}")
        print(f"Sección    : {doc.metadata['section_path']}")
        print("Contenido:")
        print(doc.page_content[:250])