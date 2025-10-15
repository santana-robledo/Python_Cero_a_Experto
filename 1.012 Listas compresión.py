
"""[Expresion for elemento in iterable if condición]"""

#Comprensión de listas
# cuadrados=[x**2 for x in range(10)]
# print(cuadrados)
# print(type(cuadrados))
numeros=[1,2,3,4,5,6,7,8,9,10]
pares=[x for x in numeros if (x%2 == 0)]
print(pares)
#
palabras=["Python","Django","Flask"]
longitudes=[len(palabra) for palabra in palabras]
print(longitudes)

#Metodo tradicional
# cuadrados=[]
# for x in range(10):
#     cuadrados.append(x%2)
# print(cuadrados)

pares=[]
for x in numeros:
    if x%2==0:
        pares.append(x)
print(pares)

longitudes=[]
for palabra in palabras:
    longitudes.append(len(palabra))
print(longitudes)