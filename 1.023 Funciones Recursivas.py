
"""
def funcion_recursiva(parametros):
    if condicion base:
        return resultado base
    else:
        return funcion_recursiva(parametros modificados)

Caso base: Factorial
"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(7))