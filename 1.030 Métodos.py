"""
Métodos de Instancia
"""
class Circulo():
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        import math
        return math.pi *(self.radio**2)
    def cambiar_radio(self,nuevo_radio):
        self.radio=nuevo_radio

mi_circulo=Circulo(5)
print(f"Area del cicrulo ={mi_circulo.area()}")
mi_circulo.cambiar_radio(10)
print(f"Nueva area del circulo: {mi_circulo.area()}")

"""
Métodos de Clase
"""

class Circulo():
    pi=3.1416
    def __init__(self,radio):
        self.radio=radio
    @classmethod
    def crear_unidad(cls):
        return cls(1)
    def area(self):
        return Circulo.pi*(self.radio**2)

circulo_unidad=Circulo.crear_unidad()
print(f"Area del circulo {circulo_unidad.area()}")

"""
Métodos estáticos
"""

class Calculadora():
    @staticmethod
    def sumar(a,b):
        return a+b
    @staticmethod
    def restar(a,b):
        return a-b

print(f"Suma{Calculadora.sumar(5,3)}")
print(f"Resta{Calculadora.restar(5,3)}")