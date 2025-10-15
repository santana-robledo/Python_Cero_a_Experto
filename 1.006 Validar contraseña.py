
def ejemplos_any_01():
    valores=[False,False,True]
    resultado_1=any(valores)
    print(resultado_1)

def ejemplos_any_02():
    numeros=[0,0,0,0]
    resultado_2=any(numeros)
    print(resultado_2)

vacia=[]
def ejemplo_any_03():
    resultado=any(vacia)
    print(resultado)
def verificar_contraseña(contrasena):
    if len(contrasena)<8:
        return False
    if not any(char.isdigit() for char in contrasena):
        return False
    if not any(char.isupper() for char in contrasena):
        return False
    especiales="@!#$%&/()=-*+"
    if not any(char in especiales for char in contrasena):
        return False

    return True
##Ejemplo contraseña
contrasena="Segur@12"
print(verificar_contraseña(contrasena))