class Archivo():
    def __init__(self,nombre_archivo):
        self.nombre_archivo=nombre_archivo
        self.archivo=open(nombre_archivo,"w")
        print(f"Archivo{nombre_archivo} abierto")

    def escribir(self,contenido):
        self.archivo.write(contenido)

    def __del__(self):
        self.archivo.close()
        print(f"Archivo{self.nombre_archivo} esta cerrado")

archivo=Archivo("ejemplo.txt")
archivo.escribir("Hola desde el curso")

##del archivo