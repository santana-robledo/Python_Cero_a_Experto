
precios=[]
valores=list()
frutas=["manzana","banana","cereza"]
valores=[1200,1900,"Juan",True,[1200,90]]
print(valores[0])
print(valores[-1])
valores.append("Armando")
valores.insert(2,"Maria")
valores.pop(2)
valores.remove("Armando")
valores[2]=1900
cant_ele=len(valores)
cant_1900=valores.count(1900)
print(cant_1900)
print(cant_ele,valores)

frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

for fruta in frutas:
    print(fruta)