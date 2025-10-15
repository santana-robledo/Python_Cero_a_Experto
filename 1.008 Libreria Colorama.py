#Colorama
from colorama import Fore,Back,Style,init
init(autoreset=True)
def uso_colorama():
    print(Fore.RED+"Esto es un texto en rojo")
    print(Back.GREEN+"Esto es un texto en fondo verde")
    print(Fore.YELLOW+Back.BLUE+"Texto amarillo con fondo azul")
    print(Style.BRIGHT+"Texto en negrita")
    print(Fore.WHITE+Back.BLACK+"Texto en blanco sobre fondo negro"+Style.RESET_ALL)

def menu_opcion():
    icono_opcion1= "\U0001F4C8"
    icono_opcion2 = "\U0001F4B0"
    icono_opcion3 = "\U0001F4DA"

    borde_superior=f"{Fore.YELLOW}{Back.BLUE}+" + "-"*30+ "+"
    opciones=[
        f"{Fore.CYAN}{Back.BLACK}  |1. Opción 1 {icono_opcion1.strip()}      |",
        f"{Fore.CYAN}{Back.BLACK}  |2. Opción 2 {icono_opcion2.strip()}     |",
        f"{Fore.CYAN}{Back.BLACK}  |3. Opción 3 {icono_opcion3.strip()}     |"
    ]
    borde_inferior = f"{Fore.YELLOW}{Back.BLUE}+" + "-" * 30 + "+"
    print(borde_superior)

    for opcion in opciones:
        print(opcion)
    print(borde_inferior)
menu_opcion()

seleccion=int(input(f"{Fore.GREEN} Selecciones una opcion "))
if seleccion==1:
    print(f"{Fore.GREEN} Haz seleccionado la opción 1")
elif seleccion==2:
    print(f"{Fore.GREEN} Haz seleccionado la opción 2")
elif seleccion==3:
    print(f"{Fore.GREEN} Haz seleccionado la opción 3")
else:
    print(f"{Fore.RED} Opción no valida. Intente de nuevo")