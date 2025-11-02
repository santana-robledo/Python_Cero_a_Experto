
class Vehiculo:
    def __init__(self,marca,modelo,año):
        self.año=año
        self.marca=marca
        self.modelo=modelo

    def mostrar_informacion(self):
        return f"{self.marca} {self.modelo} {self.año}"
    
class Auto(Vehiculo):
    def __init__(self,marca,modelo,año,numero_puertas):
        super().__init__(marca,modelo,año)
        self.numero_puertas=numero_puertas

    def mostrar_informacion(self):
        base_info= super().mostrar_informacion()
        return f"{base_info}, Puertas {self.numero_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self,marca,modelo,año,tipo_motor):
        super().__init__(marca,modelo,año)
        self.tipo_motor=tipo_motor


##Crear instancias de vehiculos
mi_coche= Auto("Toyota","Corola",2020,5)
mi_motocicleta=Motocicleta("Harley","Iron883",2023,"3 Bujes")

##Mostrar info de los vehiculos
print(mi_coche.mostrar_informacion())
print(mi_motocicleta.mostrar_informacion())