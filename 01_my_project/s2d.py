schema = "Nombre,Apellido,Edad,Mail"
row = "Ulises,Cortes,39,ulisescortes@gmail.com"

class Str2Dic(object): # object es solo una formalidad, en python no hace falta, podria no ponerse y va igual
    def __init__(self, schemaStr, separator=","):
        self.schema = schemaStr.split(separator)
        self.separator = separator
    
    def convert(self, row): # row =  # def convert espera un string
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            while i < len(tmp):
                # Forma desglosada:
                # --------------------
                # key = self.schema[i]
                # val = tmp[i]
                #---------------------
                # d[key] = val
                #---------------------
                # Forma resumida:
                d[self.schema[i]] = tmp[i] 
                i = i +1
            return d

"""
# schema: es el esquema de la tabla(excel)
o = Str2Dic(schema) # creo el objeto "o", lo inicializo.

# row: es la fila de la tabla con sus respectivos datos
d = o.convert(row) # lo convierto (al objeto "o") en diccionario: "d".
print(d)

"""