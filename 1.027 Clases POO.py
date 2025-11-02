

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def saludar(self):
        return f"Hola mi nombre es {self.nombre} y tengo {self.edad} años"

objeto1=Persona("Armando",48)
objeto2=Persona("Raul",12)

print(objeto1.nombre)
print(objeto2.edad)
print(objeto1.__dict__)
print(objeto2.saludar())