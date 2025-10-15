#Conjunto de todos los invitados

invitados={"Ana","Pedro","Sofia","Jorge","Luis","Alejandra"}
confirmaciones={"Ana","Pedro","Luis"}

for invitado in confirmaciones:
    if invitado in confirmaciones:
        print("Confirmo")
    else:
        print("No confirmado")

no_confirmados=invitados-confirmaciones
print("invitados que no han confirmado asistencia",no_confirmados)

todos_invitados= invitados|confirmaciones
print("Todos los invitados",todos_invitados)

conjunto={1,2,3}
copia=conjunto.copy()

print(copia)

conjunto1={1,2}
conjunto2={1,2,3}
print(conjunto1.issubset(conjunto2))
print(conjunto1.isdisjoint(conjunto2))