from datetime import date

def calcular_edad(fecha_nacimiento):
    hoy=date.today()
    edad=hoy.year-fecha_nacimiento.year
    if (hoy.month,hoy.day < fecha_nacimiento.month,fecha_nacimiento.day):
        edad-=1
    return edad

fecha_nacimiento=date(year=1990,month=10,day=10)
print(calcular_edad(fecha_nacimiento))