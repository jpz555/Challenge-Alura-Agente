"""
=========================================================
RAG Configuration
=========================================================

Configuración global del módulo RAG.

Este archivo centraliza la configuración del modelo
de lenguaje utilizado por el asistente.

Modificar únicamente este archivo permite cambiar
de proveedor sin alterar el resto del proyecto.

=========================================================
"""
import os
from dotenv import load_dotenv
load_dotenv()

# =========================================================
# PROVEEDOR DEL MODELO
# =========================================================
#
# Opciones disponibles:
#
#   gemini
#   ollama
#   groq
#
# =========================================================

DEFAULT_PROVIDER = "groq"


# =========================================================
# MODELOS DISPONIBLES
# =========================================================

MODELS = {
    "gemini": "gemini-2.5-flash",
    "ollama": "gemma3:1b",
    "groq": "llama-3.1-8b-instant"

}


# =========================================================
# PARÁMETROS DE GENERACIÓN
# =========================================================
TEMPERATURE = 0.0
TOP_P = 0.95
MAX_OUTPUT_TOKENS = 2048

# =========================================================
# CONFIGURACIÓN DEL RAG
# =========================================================

TOP_K_DOCUMENTS = 4
STRUCTURED_OUTPUT = True

# =========================================================
# API KEYS
# =========================================================
#
# Se leen desde variables de entorno.
#
# GEMINI_API_KEY
# GROQ_API_KEY
#
# Ollama no requiere API Key.
#
# =========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")