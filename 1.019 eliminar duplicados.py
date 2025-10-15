"""
Eliminar los duplicados de una lista de valores
"""
lista=[1,2,3,4,4,5]
conjunto=set(lista)#Convertir la lista en conjunto
lista_sin_duplicar=list(conjunto)#Lo vuelve a convertir en lista

for numero in lista_sin_duplicar:
    print(numero)
def elementos_comunes(conjunto1,conjunto2):
    return conjunto1&conjunto2
conjunto1={1,2,3,4,5}
conjunto2={4,5,6,7.8}
print(elementos_comunes(conjunto1,conjunto2))

almacen1={"laptop","mouse","teclado","monitor","impresora"}
almacen2={"teclado","monitor","tablet","smartphone","impresora"}
comunes=almacen1.intersection(almacen2)
print(f"Productos comunes en ambos almacenes{comunes}")
print(f"Producto exclusivo de almacen 1{almacen1.difference(almacen2)}")
print(f"Producto exclusivo de almacen 2{almacen2.difference(almacen1)}")
print(f"Inventario completo{almacen1.union(almacen2)}")
