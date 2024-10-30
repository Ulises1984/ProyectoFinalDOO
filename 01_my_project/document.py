import os
os.system('cls')

class Document:
    def __init__(self, id, contenido=None):
        self.id = id
        #self.contenido = contenido if contenido is not None else {}
        if contenido is not None:
            self.contenido = contenido
        else:
            self.contenido = {}
        
    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor
    
    def __str__(self):
        return f"Documento(id={self.id}, contenido={self.contenido})"

"""    
doc = Document(1)  # Crea un documento con id=1 y contenido vacío
print(doc)  # Muestra: Documento(id=1, contenido={})

doc.modificar_valor('titulo', 'Mi Documento')
print(doc.obtener_valor('titulo'))  # Muestra: Mi Documento

doc.modificar_valor('autor', 'Juan')
print(doc)  # Muestra: Documento(id=1, contenido={'titulo': 'Mi Documento', 'autor': 'Juan'})
"""