class Empleado:
    def __init__(self,nombre,puesto,salario):
        self.nombre=nombre
        self.puesto=puesto
        self.salario=salario
    def mostrar_info(self):
        return f"Nombre: {self.nombre} Puesto:{self.puesto} Salario: {self.salario}"
    def tipo_empleado(self):
        return "Empleado Regular"
#Definir la subclase que herede de empleado

class Gerente(Empleado):
    def __init__(self,nombre,salario,bonos):
        super().__init__(nombre,"Gerente",salario)
        self.bonos=bonos

    def mostrar_info(self):
        info=super().mostrar_info()
        return f"{info} Bonos: {self.bonos}"
    def tipo_empleado(self):
        return "Gerente"
def mostrar_informaciom(empleados):
    for empleado in empleados:
        print(empleado.mostrar_info())
        print(f"Tipo de empleado {empleado.tipo_empleado()}")
        print("_"*30)

empleado1=Empleado("Ana","Developer",7000)
empleado2=Empleado("Luis","Diseñador Gráfico",6000)
gerente=Gerente("Martha",9000,500)

lista_empleado=[empleado2,empleado2]

mostrar_informaciom(lista_empleado)