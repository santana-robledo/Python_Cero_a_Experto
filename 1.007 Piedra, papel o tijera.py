import random
def jugar():
    opciones=["piedra","papel","tijera"]
    jugador=input("Elige piedra,papel o tijera ").lower()
    if jugador not in opciones:
        print("Opción no valida, elija piedra, papel o tijera ")
        return
    computadora=random.choice(opciones)

    print(f"Tu elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")

    if jugador==computadora:
        print("Es un empate")
    elif (jugador=="piedra" and computadora=="tijera") or (jugador=="papel" and computadora=="piedra") or (jugador=="tijera" and computadora=="papel"):
        print("Le ganaste a la computadora")
    else:
        print("Perdiste")

def juego():
    print("Bienvenido al juego")
    while True:
        jugar()

        jugar_otravez=input("Quieres jugar otra vez? si/no ").lower()
        if jugar_otravez == "no":
            print("Gracias por jugar")
            break

juego()