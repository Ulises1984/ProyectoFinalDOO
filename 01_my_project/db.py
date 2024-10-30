from document import Document
from collection import Collection


class BaseDeDatosDocumental:
    def __init__(self):
        self.colecciones = {}
    
    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Collection(nombre_coleccion)
    
    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def obtener_coleccion(self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones" 
    
class Document:
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}
        
    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor
    
    def __str__(self):
        return f"Documento(id={self.id}, contenido={self.contenido})"

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