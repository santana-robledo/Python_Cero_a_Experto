saldo_cajero=1000

def consultar_saldo():
    print(f"Tu saldo actual es {saldo_cajero}")

def retirar_dinero():
    global saldo_cajero
    cantidad=float(input("Ingrese la cantidad a retirar "))

    if cantidad>saldo_cajero:
        print("No tienes suficiente saldo para retirar")
    else:
        saldo_cajero-=cantidad
        print(f"Retiraste: ${cantidad}. Tu saldo actual es: {saldo_cajero}")

def depositar_dinero():
    global saldo_cajero
    cantidad = float(input("Ingrese la cantidad a depositar "))
    saldo_cajero+=cantidad
    print(f"Depositaste: ${cantidad}. Tu saldo actual es: {saldo_cajero}")

def mostrar_menu():
    print("Menu de Opciones")
    print("1.Retirar dinero")
    print("2.Depositar dinero")
    print("3.Consultar saldo")
    print("4.Salir")

while True:
    mostrar_menu()
    opcion=int(input("Seleccione una opción "))
    if opcion==1:
        retirar_dinero()
    elif opcion==2:
        depositar_dinero()
    elif opcion==3:
        consultar_saldo()
    elif opcion==4:
        break
    else:
        print("Opcion invalida")