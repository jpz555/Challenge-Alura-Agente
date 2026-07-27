from pathlib import Path

from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore


QUERIES = [

    "CD-01",
    "CD-01 Barranquilla",
    "Barranquilla",

    "¿Dónde está ubicado el CD-01?",

    "horario",
    "horario operativo",
    "¿Cuál es el horario operativo?",

    "stock mínimo",

    "nivel de servicio",

    "TR30",

    "elefante azul"

]


def main():

    embeddings = EmbeddingModel()

    vector_store = VectorStore(
        persist_directory=Path("vector_db"),
        embedding_function=embeddings.langchain_model
    )

    vector_store.load()

    vector_store.info()

    for query in QUERIES:

        print("\n")
        print("=" * 100)
        print(query)
        print("=" * 100)

        vector_store.similarity_search(
            query=query,
            k=5
        )


if __name__ == "__main__":
    main()