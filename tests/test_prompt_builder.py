from document_processor.config import VECTOR_DB_DIR

from indexer.embeddings import EmbeddingModel
from indexer.vector_store import VectorStore
from indexer.retriever import KnowledgeRetriever

from rag.prompt_builder import PromptBuilder


def main():

    embedding_model = EmbeddingModel()

    vector_store = VectorStore(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embedding_model.langchain_model
    )

    vector_store.load()

    retriever = KnowledgeRetriever(
        vector_store=vector_store
    )

    question = "¿Cuál es el horario operativo de la empresa?"

    documents = retriever.search(question)

    builder = PromptBuilder()

    context = builder.build(question, documents)

    print(context.prompt.to_string())

    print("\n")

    print("=" * 70)

    print("FUENTES ESTRUCTURADAS")

    print("=" * 70)

    for source in context.sources:

        print(source)

if __name__ == "__main__":
    main()