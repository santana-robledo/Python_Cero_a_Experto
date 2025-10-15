"""
Ambito global
"""

x=10
def mi_funcion():
    y=5
    print(f"Dentro de mi funcion x={x}")
    print(f"Dentro de mi función y={y}")

mi_funcion()
contador=0
def incrementar():
    global contador
    contador+=1
    print(f"Dentro de incrementar contador={contador}")

incrementar()

usuarios_activos=0

def iniciar_sesion(nombre_usuario):
    global usuarios_activos
    usuarios_activos+=1
    print(f"Usuario {nombre_usuario}. Haz iniciado sesion")
    print(f"Numero de usuarios activos {usuarios_activos}")

def cerrar_sesion(nombre_usuario):
    global usuarios_activos
    usuarios_activos-=1
    print(f"Usuario {nombre_usuario}. Haz cerrado sesion")
    print(f"Numero de usuarios activos {usuarios_activos}")

"""
Usuarios iniciando y cerrando sesión
"""
iniciar_sesion("Ana")
iniciar_sesion("Luis")
cerrar_sesion("Carlos")
cerrar_sesion("Ana")
