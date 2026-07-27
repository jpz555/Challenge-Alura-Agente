from sentence_transformers import CrossEncoder
from langchain_core.documents import Document


class CrossEncoderReranker:
    def __init__(self):

        self.model = CrossEncoder(
                "BAAI/bge-reranker-base"
            )

    def rerank(self,
            query: str,
            documents: list[Document],
            top_k: int
        ) -> list[Document]:

        if not documents:
            return []

        pairs = [
            [query, doc.page_content]
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(scores, documents),
            key=lambda x: x[0],
            reverse=True
        )

        return [
                doc
                for _, doc in ranked[:top_k]
                ]