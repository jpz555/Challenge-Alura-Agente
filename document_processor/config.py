"""
=========================================================
Document Processor - Configuración General
Challenge IA Empresarial
=========================================================
Autor: Juan
Proyecto: Asistente Corporativo Inteligente
=========================================================
"""

from pathlib import Path

# =========================================================
# DIRECTORIOS DEL PROYECTO
# =========================================================

# Carpeta donde está document_processor
BASE_DIR = Path(__file__).resolve().parent

# Carpeta raíz del proyecto
PROJECT_ROOT = BASE_DIR.parent

# Documentación fuente (17 documentos Markdown)
DOCUMENTS_DIR = PROJECT_ROOT / "documents"

# Carpeta donde se almacenarán los documentos procesados
PROCESSED_DIR = PROJECT_ROOT / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

# JSON generados
JSON_OUTPUT_DIR = PROCESSED_DIR / "json"
JSON_OUTPUT_DIR.mkdir(exist_ok=True)

# Chunks generados
CHUNKS_OUTPUT_DIR = PROCESSED_DIR / "chunks"


# =====================================================
# Base Vectorial
# =====================================================
# Carpeta de Vector DB
VECTOR_DB_DIR = PROJECT_ROOT/ "vector_db"
VECTOR_DB_DIR.mkdir(exist_ok=True)

# Logs
LOGS_DIR = PROJECT_ROOT / "logs"

# =========================================================
# CREAR DIRECTORIOS SI NO EXISTEN
# =========================================================

for directory in [
    PROCESSED_DIR,
    JSON_OUTPUT_DIR,
    CHUNKS_OUTPUT_DIR,
    LOGS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# =========================================================
# FORMATOS SOPORTADOS
# =========================================================

SUPPORTED_FORMATS = [
    ".md",
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".csv",
    ".json",
    ".html",
]

# =========================================================
# CONFIGURACIÓN DE CHUNKING
# (Se utilizará posteriormente)
# =========================================================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

ENCODING = "utf-8"

REMOVE_EMPTY_LINES = True
REMOVE_EXTRA_SPACES = True

# =========================================================
# LOGGING
# =========================================================

LOG_LEVEL = "INFO"

# =========================================================
# VERSIÓN DEL DOCUMENT PROCESSOR
# =========================================================

PROCESSOR_NAME = "Document Processor"

PROCESSOR_VERSION = "1.0.0"

# =========================================================
# FUNCIÓN DE VALIDACIÓN
# =========================================================

def validate_environment():
    """
    Verifica que exista la carpeta de documentos.
    """

    if not DOCUMENTS_DIR.exists():
        raise FileNotFoundError(
            f"No existe la carpeta de documentos:\n{DOCUMENTS_DIR}"
        )

    return True