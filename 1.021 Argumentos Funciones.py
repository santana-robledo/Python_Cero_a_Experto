"""
Argumentos Posicionales
"""
def suma(a,b):
    return a+b
resultado=suma(3,5)
print(resultado)

"""
Argumentos Nombrados
"""
def describir_persona(nombre,edad):
    return f"{nombre} tiene {edad} años"

resultado=describir_persona(edad=30,nombre="Alberto")
print(resultado)

"""
Argumentos por defecto
"""
def mensaje_bienvenida(nombre,saludo="Hola"):
    return f"{saludo}, {nombre}"
resultado=mensaje_bienvenida("Armando")
print(resultado)

"""
Argumentos variables
*args = captura multiples argumentos posicionales en una tupla
**kwargs= captura multiples elementos nombrados en un diccionario
"""

def suma_valor(*args):
    return sum(args)

resultado=suma_valor(7,8,4,5,6,7,3,4,5,6,77)
print(resultado)

def mostrar_info(**kwargs):
    for clave,valor  in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(Nombre="Armando",edad=38,ciudad="Madrid")

"""
Combinar Argumentos
Argumentos posicionales, por defecto,*args,**kwargs
"""

def ejemplo_combinacion(a,b=5,*args,**kwargs):
    print(f"a:{a}, b:{b}")
    print("args:",args)
    print("kwargs:", kwargs)

ejemplo_combinacion(1,2,3,4,x=10,y=10)