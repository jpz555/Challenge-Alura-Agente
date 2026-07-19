from rag.models import ModelFactory

# Esta prueba es solo para conectar con el modelo y verificar que se pueda invocar correctamente.
# no tiene contexto
def main():
    
    llm = ModelFactory.create(provider="groq")
    
    print(type(llm))
    
    print("Modelo Cargado Correctamente")
    
    response  = llm.invoke("Hola, cuales son los horarios de la empresa?")
    print(response)
    
if __name__ == "__main__":
    main()