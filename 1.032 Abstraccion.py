from abc import ABC,abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        "Este es un metodo abstracto para calcular el área de la forma"
        pass
    def __str__(self):
        "Este es un metodo para representar una cadena"
        return f"{self.__class__.__name__} con área: {self.calcular_area()}"
class circulo(Forma):
    def __init__(self,radio):
        self.radio=radio
    def calcular_area(self):
        "Calcular el area del circulo"
        return math.pi*self.radio**2

class rectangulo(Forma):
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    def calcular_area(self):
        return self.ancho*self.alto

class  Triangulo(Forma):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        return 0.5*self.base*self.altura

"Función tipo forma que muestre su área"
def mostrar_area(forma):
    print(forma)

"Crear instancia"
mi_circulo=circulo(radio=5)
mi_rectangulo=rectangulo(ancho=4,alto=6)
mi_triangulo=Triangulo(base=3,altura=7)

mostrar_area(mi_triangulo)
mostrar_area(mi_rectangulo)
mostrar_area(mi_circulo)