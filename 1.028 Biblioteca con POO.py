
class Autor:

    def __init__(self,nombre,fecha_nacimiento):
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento

    def __str__(self):
        return f"{self.nombre} nacido el {self.fecha_nacimiento}"

class Libro:
    def __init__(self,titulo,autor,año_publicacion):
        self.titulo=titulo
        self.año_publicacion=año_publicacion
        self.autor=autor

    def __str__(self):
        return f"{self.titulo} por {self.autor} publicado en {self.año_publicacion}"

class Biblioteca:
    def __init__(self):
        self.libros=[]

    def añadir_libros(self,libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            return "La Biblioteca esta vacía"
        return "\n".join(str(libro) for libro in self.libros)

autor1=Autor("Daniel García","1927-03-06")
autor2=Autor("Isabel García","1942-08-29")
libro1=Libro("100 años de Soledad",autor1,1967)
libro2=Libro("La Casa de los Espiritus",autor2,1982)
mi_biblioteca=Biblioteca()
mi_biblioteca.añadir_libros(libro1)
mi_biblioteca.añadir_libros(libro2)
print(mi_biblioteca.mostrar_libros())