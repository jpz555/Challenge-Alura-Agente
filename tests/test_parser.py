from document_processor.config import DOCUMENTS_DIR
from document_processor.parser import DocumentParser

parser = DocumentParser()

documents = parser.read_directory(DOCUMENTS_DIR)

print(f"Documentos encontrados: {len(documents)}")

# for doc in documents:
#     print(f"- {doc['file_name']}")
    
# print("Ruta documentos:")
# print(DOCUMENTS_DIR)

# print("¿Existe?:", DOCUMENTS_DIR.exists())

# print("Contenido:")

# for f in DOCUMENTS_DIR.iterdir():
#     print(f)