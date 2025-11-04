class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def hacer_sonido(self):
        raise NotImplemented("Este método debe ser sobreescrito por las subclases")
    def __str__(self):
        return f"{self.nombre}, {self.edad}"
class Perro(Animal):
    def hacer_sonido(self):
        return "Ladrido"

class Gato(Animal):
    def hacer_sonido(self):
        return "Maullido"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"

def hacer_sonido_animal(Animal):
    print(f"{Animal} hace: {Animal.hacer_sonido()}")

mi_perro=Perro(nombre="Rex",edad=5)
mi_gato=Gato(nombre="Felix",edad=10)
mi_vaca=Vaca(nombre="Blanca",edad=7)

hacer_sonido_animal(mi_perro)
hacer_sonido_animal(mi_gato)
hacer_sonido_animal(mi_vaca)