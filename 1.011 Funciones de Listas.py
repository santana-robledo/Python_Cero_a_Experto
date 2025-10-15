# frutas=list()
#
# while True:
#     nueva_fruta=input("Ingrese la fruta ")
#     if nueva_fruta in frutas:
#         posicion=frutas.index(nueva_fruta)
#         print(f"La fruta ya existe y se encuentra en la posicion {posicion}")
#         rpta=input("Desea continuar? ")
#         if rpta=="n":
#             break
#     else:
#         frutas.append(nueva_fruta)
#         print(frutas)
#         rpta = input("Desea continuar? ")
#         if rpta == "n":
#             break

frutas=["manzana","banana","naranja","kiwi"]
for index,nombre in enumerate(frutas,start=1):
        print(f"{index} {nombre}")