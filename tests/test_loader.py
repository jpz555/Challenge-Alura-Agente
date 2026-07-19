from pathlib import Path

from indexer.loader import ChunkLoader


CHUNKS_DIR = Path("processed/chunks")

loader = ChunkLoader(CHUNKS_DIR)

documents = loader.load()

print(f"\nDocumentos LangChain: {len(documents)}\n")

for document in documents:
    print("-" * 60)
    print(document)


# print("=" * 80)

# print(documents[0])

# print("=" * 80)

# print("\nMetadata\n")

# for key, value in documents[0].metadata.items():

#     print(f"{key}: {value}")