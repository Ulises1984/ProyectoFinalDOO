from db import Collection
from db import Document
from s2d import Str2Dic

def import_collection(nombre_archivo):
    collection = Collection("Personas")

    with open(nombre_archivo, "r") as archivo:
        schema_line = archivo.readline().strip()
        str2dic = Str2Dic(schema_line)
        
        doc_id = 1
        
        line = archivo.readline().strip()

        while line:
            if line!="":
                contenido = str2dic.convert(line)
                document = Document(doc_id, contenido)
                collection.add_document(document)

                doc_id += 1

            line = archivo.readline().strip()
    
    print(collection)
          
    return collection


#import_collection(r"C:\Users\ulise\Desktop\Ulises\IFTS11\ANALISIS_DE_SISTEMA_PLAN_NUEVO_2024\2DO_CUATRIMESTRE\03-DESARROLLO_ORIENTADO_A_OBJETOS\my_project\datos_personales.csv")