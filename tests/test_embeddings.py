from indexer.embeddings import EmbeddingModel

embedding_model = EmbeddingModel()

embedding_model.info()

model = embedding_model.langchain_model

print("\nModelo LangChain cargado correctamente.")

vector = model.embed_query(
    "¿Cuál es el horario operativo de la empresa?"
)

print(f"\nDimensión del embedding: {len(vector)}")

print(f"\nPrimeros 10 valores:\n")

print(vector[:10])