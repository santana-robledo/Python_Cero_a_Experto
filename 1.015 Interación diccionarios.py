#
# cuadrados={ x:x**2 for x in range(5)}
# print(cuadrados)
#
# cuadrados={ x:x**2 for x in range(10) if x%2==0}
# print(cuadrados)

diccionaro={"a":1,"b":2,"c":3}
invertido={v:k for k,v in diccionaro.items()}
#print(invertido)

tuplas=[("a",1),("b",2),("c",3)]

diccionaro={k:v for k,v in tuplas}
# print(diccionaro)

claves=["x","y","c"]
diccionaro={clave:0 for clave in claves}
print(diccionaro)