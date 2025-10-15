#
# def nombre_funcion(parametro)
#     cuerpo de nombre_funcion
#     pass

def mi_primer_funcion():
    pass

mi_primer_funcion()

def sumar(a,b):
    return a+b
print(sumar(7,8))

def externa():
    def interna():
        return "Soy la funcion interna"
    return interna()
print(externa())

suma=lambda x,y:x+y
print(suma(3,5))

def multiplicar_ahora(x,y):
    return x*y
print(multiplicar_ahora(6,7))

def calculadora_minima(x,y):
    def suma(a,b):
        return a+b
    def resta(a,b):
        return a-b
    return suma(x,y),resta(x,y)

resultado_suma,resultado_resta=calculadora_minima(8,5)
print(f"El resultado de suma es {resultado_suma}, y el de resta es:{resultado_resta}")