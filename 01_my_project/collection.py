from document import Document

class Collection:
    def __init__(self, name):
        self.name = name
        self.documents = {}
    
    def add_document(self, document):
        self.documents[document.id] = document
    
    def delete_document(self, id_document):
        if id_document in self.documents:
            del self.documents[id_document]
    
    def search_document(self, id_document):
        return self.documents.get(id_document, None)
    
    def __str__(self):
        return f"Collecion {self.name} con {len(self.documents)} documentos"

"""    
    # Crear documentos

libro1 = Document(1, {'titulo': 'Documento 1', 'autor': 'Autor 1'})
libro2 = Document(2, {'titulo': 'Documento 2', 'autor': 'Autor 2'})

# Crear una colección
coleccion = Collection("Libros")

# Añadir documentos a la colección
coleccion.add_document(libro1)
coleccion.add_document(libro2)

# Buscar un documento
print(coleccion.search_document(1))  # Muestra: Documento(id=1, contenido={'titulo': 'Documento 1', 'autor': 'Autor 1'})

# Eliminar un documento
coleccion.delete_document(1)

# Ver la colección
print(coleccion)  # Muestra: Coleccion Mi Colección con 1 documentos

"""
        