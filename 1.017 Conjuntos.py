# conjunto={0,1,2,3,4,5,6,7,8,9}
# conjunto_dos=set([1,2,3])
# #print(type(conjunto))
#
# conjunto.add(0)
# conjunto.remove(2)
# conjunto.discard(5)
# #elemento=conjunto.pop()
# #print(elemento)
#
# #conjunto.clear()
#
#
# print(conjunto)

frutas={"Manzana","Banana","Aguacate","Naranja"}
citrus={"Naranja","Limon","Lima"}

print(frutas.union(citrus))
print(frutas.intersection(citrus))
print(frutas.difference(citrus))

conjunto1={1,2,3}
conjunto2={3,4,5}
diferencia=conjunto2-conjunto1
diferencia_simetrica=conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)
print(diferencia)